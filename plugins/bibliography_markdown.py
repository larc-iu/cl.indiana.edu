"""
Bibliography Plugin for Pelican (Markdown version)
Adds support for bibliography directives in Markdown files.
"""
import os
import re
import subprocess
import tempfile
from pathlib import Path
from pelican import signals

def register():
    """Register the plugin with Pelican."""
    signals.content_object_init.connect(process_bibliography)

def process_bibliography(content_object):
    """Process bibliography directives in Markdown content."""
    if content_object._content is None:
        return
    
    # Only process Markdown files
    if not hasattr(content_object, 'source_path') or not content_object.source_path.endswith('.md'):
        return
    
    # Process bibliography directives
    processor = BibliographyProcessor(content_object.source_path)
    content_object._content = processor.process_content(content_object._content)

class BibliographyProcessor:
    """Process bibliography directives in content."""
    
    def __init__(self, source_path):
        """Initialize the processor."""
        self.source_dir = os.path.dirname(source_path)
        self.plugin_dir = os.path.dirname(os.path.abspath(__file__))
        self.bst_path = os.path.join(self.plugin_dir, 'acl.bst')
        
        # Check if the BST file exists
        if not os.path.exists(self.bst_path):
            print("WARNING: acl.bst not found in plugin directory. The bibliography plugin may not work correctly.")
    
    def process_content(self, content):
        """Find and process bibliography directives in the content."""
        # Pattern for bibliography directive in Markdown: [bibliography: filename.bib]
        pattern = r'\[bibliography:\s*([^\]]+)\]'
        
        def replace_bibliography(match):
            bib_file = match.group(1).strip()
            
            # Try different paths for the bib file
            possible_paths = [
                os.path.join(self.source_dir, bib_file),
                os.path.join(self.source_dir, 'static', bib_file),
                os.path.join(os.path.dirname(self.source_dir), 'static', bib_file),
                bib_file  # Absolute path
            ]
            
            full_bib_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    full_bib_path = path
                    break
            
            if not full_bib_path:
                return f'<div class="error">Error: BibTeX file not found: {bib_file}</div>'
            
            return self._process_with_bibtex(full_bib_path)
        
        return re.sub(pattern, replace_bibliography, content)
    
    def _process_with_bibtex(self, bib_path):
        """Process bibliography with the bundled ACL BST file."""
        # Create a temporary directory for our work
        with tempfile.TemporaryDirectory() as temp_dir:
            # Define temp file paths
            temp_dir_path = Path(temp_dir)
            tex_path = temp_dir_path / "temp.tex"
            aux_path = temp_dir_path / "temp.aux"
            bbl_path = temp_dir_path / "temp.bbl"
            temp_bib_path = temp_dir_path / "temp.bib"
            temp_bst_path = temp_dir_path / "temp.bst"
            
            # Copy the bib file
            with open(bib_path, 'r', encoding='utf-8') as src, \
                    open(temp_bib_path, 'w', encoding='utf-8') as dst:
                dst.write(src.read())
            
            # Copy the bundled BST file
            if os.path.exists(self.bst_path):
                with open(self.bst_path, 'r', encoding='utf-8') as src, \
                        open(temp_bst_path, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
            
            # Create the LaTeX document
            with open(tex_path, 'w', encoding='utf-8') as f:
                f.write(r'''\documentclass{article}
\begin{document}
\nocite{*}
\bibliographystyle{temp}
\bibliography{temp}
\end{document}
''')
            
            # Create the aux file
            with open(aux_path, 'w', encoding='utf-8') as f:
                f.write(r'''\relax
\citation{*}
\bibstyle{temp}
\bibdata{temp}
''')
            
            # Run bibtex
            bibtex_proc = subprocess.run(
                ["bibtex", "temp"],
                cwd=temp_dir,
                capture_output=True,
                text=True
            )
            
            if bibtex_proc.returncode != 0:
                # Try to provide helpful error message
                error_msg = bibtex_proc.stderr if bibtex_proc.stderr else "Unknown error"
                return f'<div class="error">BibTeX error: {error_msg}</div>'
            
            # Read the generated BBL file
            if os.path.exists(bbl_path):
                return self._process_bbl_file(bbl_path)
            else:
                return '<div class="error">BibTeX did not generate a BBL file</div>'
    
    def _process_bbl_file(self, bbl_path):
        """Extract and convert bibliography entries from a BBL file to HTML."""
        with open(bbl_path, 'r', encoding='utf-8') as f:
            bbl_content = f.read()
        
        # Pattern to match the bibliography environment
        bib_env_pattern = r'\\begin\{thebibliography\}\{[^}]*\}(.*?)\\end\{thebibliography\}'
        bib_match = re.search(bib_env_pattern, bbl_content, re.DOTALL)
        
        if bib_match:
            # Get the content excluding the begin/end tags and any arguments
            bib_entries_content = bib_match.group(1).strip()
            
            # Split into individual bibliography entries
            bib_items = re.split(r'(?=\\bibitem)', bib_entries_content)
            bib_items = [item for item in bib_items if item.strip()]
            
            # Extract year from each entry for sorting
            def extract_year(entry):
                # Look for a year pattern (4 digits, typically in brackets or after certain markers)
                year_match = re.search(r'(\b|\D)(19|20)\d{2}(\b|\D)', entry)
                if year_match:
                    # Extract just the 4-digit year from the match
                    digit_match = re.search(r'(19|20)\d{2}', year_match.group(0))
                    if digit_match:
                        return int(digit_match.group(0))
                return 0  # Default for entries without a year
            
            # Sort entries by year in reverse chronological order
            sorted_items = sorted(bib_items, key=extract_year, reverse=True)
            
            # Convert each LaTeX entry to HTML
            html_entries = [self._latex_to_html(entry) for entry in sorted_items]
            
            # Join all entries into a single HTML string
            bib_entries_html = ''.join(html_entries)
            
            return f'<div class="bibliography"><ul>{bib_entries_html}</ul></div>'
        else:
            return '<div class="error">Could not extract bibliography entries from BibTeX output</div>'
    
    def _latex_to_html(self, latex_text):
        """Convert LaTeX formatting to HTML."""
        # Remove LaTeX command definitions
        latex_text = re.sub(r'\\providecommand\{\\natexlab\}\[1\]\{#1\}', '', latex_text)
        
        # Replace LaTeX commands with HTML
        html_text = latex_text
        
        # Handle \bibitem
        html_text = re.sub(
            r'\\bibitem\[([^\]]*)\]\{([^}]*)\}',
            r'<li class="bibliography-entry" id="bib-\2">',
            html_text
        )
        
        # Close each bibliography entry li - but avoid duplicate closing tags
        # First, ensure each entry ends properly before the next \bibitem or end of string
        html_text = re.sub(r'(?=\\bibitem)', r'</li>', html_text)
        # Add closing tag at the very end if it doesn't already exist
        if not html_text.strip().endswith('</li>'):
            html_text += '</li>'
        
        # Remove tildes (non-breaking spaces in LaTeX)
        html_text = html_text.replace('~', ' ')
        
        # Process \href commands
        html_text = self._process_href_commands(html_text)
        
        # Remove LaTeX-specific commands
        html_text = re.sub(r'\\newblock', '', html_text)
        html_text = re.sub(r'\\natexlab\{([^}]*)\}', '', html_text)
        
        # Handle LaTeX emphasis
        html_text = re.sub(r'\\emph\{([^}]*)\}', r'<em>\1</em>', html_text)
        
        # Remove braces
        prev_text = ""
        while prev_text != html_text:
            prev_text = html_text
            html_text = re.sub(r'\{([^{}]*?)\}', r'\1', html_text)
        
        # Handle special characters
        html_text = html_text.replace('--', '–')
        html_text = html_text.replace('---', '—')
        
        # Clean up remaining LaTeX commands
        html_text = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^}]*\})?', '', html_text)
        
        # Clean up whitespace
        html_text = re.sub(r'\s+', ' ', html_text)
        html_text = html_text.strip()
        
        return html_text
    
    def _process_href_commands(self, text):
        """Process \href LaTeX commands to HTML <a> tags, handling nested braces properly."""
        result = ""
        i = 0
        while i < len(text):
            # Look for \href
            href_match = text.find('\\href', i)
            if href_match == -1:
                # No more \href found
                result += text[i:]
                break
            
            # Add text up to \href
            result += text[i:href_match]
            i = href_match
            
            # Find URL opening brace
            url_start = text.find('{', i)
            if url_start == -1:
                # Malformed \href without opening brace
                result += text[i]
                i += 1
                continue
            
            # Find URL closing brace with brace counting
            url_end = self._find_matching_brace(text, url_start)
            if url_end == -1:
                # Unclosed URL brace
                result += text[i]
                i += 1
                continue
            
            # Extract URL
            url = text[url_start+1:url_end]
            
            # Find title opening brace
            title_start = text.find('{', url_end + 1)
            if title_start == -1:
                # No title brace found
                result += text[i:url_end+1]
                i = url_end + 1
                continue
            
            # Find title closing brace with brace counting
            title_end = self._find_matching_brace(text, title_start)
            if title_end == -1:
                # Unclosed title brace
                result += text[i:title_start+1]
                i = title_start + 1
                continue
            
            # Extract title
            title = text[title_start+1:title_end]
            
            # Create an HTML link
            result += f'<a href="{url}">{title}</a>'
            
            # Move past this \href
            i = title_end + 1
        
        return result
    
    def _find_matching_brace(self, text, start_pos):
        """Find the matching closing brace for an opening brace at start_pos."""
        brace_count = 1
        j = start_pos + 1
        while j < len(text) and brace_count > 0:
            if text[j] == '{':
                brace_count += 1
            elif text[j] == '}':
                brace_count -= 1
                if brace_count == 0:
                    return j
            j += 1
        return -1