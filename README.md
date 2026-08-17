# cl.indiana.edu

This repo builds the IU Computational Linguistics website.

Everything you can change lives in the `content/` folder. You do not need to touch
anything else.

The live site rebuilds itself every fifteen minutes. So once your change is merged, wait
fifteen minutes and it will be up.

## How to make a change

The easiest way is to do it on GitHub in your browser.

1. Find the file you want to change (see the list below).
2. Click the pencil icon to edit it.
3. Make your change.
4. At the bottom, click **Propose changes**, then **Create pull request**.

That sends the change to us for a quick look. You do not need to install anything.

If you want to preview the site first, see [Running it on your own computer](#running-it-on-your-own-computer)
at the end.

## Where things are

| What | File |
| --- | --- |
| People (faculty, students, alumni) | `content/people.yaml` |
| Photos of people | `content/images/people/` |
| News posts | `content/news/` |
| Alumni stories | `content/stories/` |
| Colloquium schedule | `content/colloquium/` |
| Courses | `content/courses.yaml` |
| Degree program pages | `content/programs/` |
| Which programs get listed | `content/programs.yaml` |
| Home page text | `content/index.md` |

## Add a news post

News posts are short. A paragraph or two. A paper, a talk, an award, a milestone.

Make a new file in `content/news/`. Name it with the date first, then a few words:
`2026-07-08-victor-peter-sharedtask.md`.

Put this at the top:

```
Title: IUCL students win shared task at AmericasNLP 2026
Date: 2026-07-08
```

Then leave a blank line and write the post underneath.

## Building locally

You only need this if you want to see your change before sending it.

Using [uv](https://docs.astral.sh/uv/):

```
uv run pelican content -o output -s pelicanconf.py -r -l
```

Or if you just want to use regular Python tools:

```
pip install -r requirements.txt
pelican content -o output -s pelicanconf.py -r -l
```

Open [http://localhost:8000](http://localhost:8000).
