Title: From field linguistics to AI agents
Date: 2025-11-01
Alum: Kenneth Steimel, Ph.D. 2026
Role: Senior Software Engineer, Cisco
Image: images/people/kenneth_steimel.jpg
Quote: “Prior to being in the program I never would have been able to have a career like this.”
Summary: Kenneth Steimel picked Indiana because it was one of the few places that had both African linguistics and computational linguistics. Both halves are still in use—as a Swahili treebank, and as a way of debugging production software.

Kenneth Steimel came to Indiana straight out of an undergraduate program in linguistics,
drawn to a department where a field linguist could also become a computational linguist. The
dissertation that Ken wrote combines the two: a Swahili treebank, and a study of how to
train a parser with minimal amounts of data. Steimel spent three years as an applied
scientist at Educational Testing Service and is now a senior software engineer at Cisco
building AI agents.

**What was your background coming out of undergrad, and why a Ph.D. in CL?**

I did my bachelor's in linguistics at the University of Missouri, and I got really into
field linguistics there, and phonology in particular. But I had also taken a bunch of
computer science courses—Visual Basic, a few C classes, some database classes—mostly because
I thought they were interesting. I didn't really think there was any crossing point between
the two.

Toward the end of undergrad I started looking at computational linguistics programs, and I
picked IU because it had both African linguistics and computational linguistics. At the time
I was deep into African linguistics and fieldwork, and I didn't want to give that up.

**When did those two halves come together?**

I went to the Annual Conference on African Linguistics to present a paper, right around the
time I was starting at IU. Somebody there gave a presentation about a system they'd built to
verify their phonological rules. It was really handy for them, because they could test their
hypotheses very quickly.

I thought that was fascinating. It was also interesting because of the reception it got,
which from a lot of the other linguists in the room was essentially, *why would you want a
thing like that?* And I was thinking, well, that's awesome. That's really handy. That got me
thinking it would be exciting to mix those things.

**Did the program let you keep a foot in both?**

Yes. There's real ability to take CL classes as a linguistics student and vice versa, so I
pulled from both. I took the intro programming in Python class, which was probably
unnecessary because I already knew Python, but it was great, because it got me onto a
research project Sandra Kübler was directing, a shared task on sentiment analysis. Seeing
the way you write a field methods paper versus the way you write a CL paper was eye
opening—completely different. And being part of a big collaborative group like that was
important.

The coursework fed directly into the dissertation, too. I took field methods again as a
graduate student, plus alternative syntactic theories and corpus linguistics, and that
dovetailed straight into a thesis on building a treebank and evaluating dependency parsing.

**What is the dissertation about?**

Swahili and curriculum learning. I built a small treebank—only about 250 sentences, very
compact—and then developed rules to generate lower-quality silver-standard parse trees in
larger volume.

Part of the question is how you fit a Bantu language into Universal Dependencies when it's
typologically unlike what's already there; there are still no Bantu languages in UD, though
several projects are trying, including mine. The other part is what happens if you run
curriculum learning on *quality* instead of difficulty. How do you make sure a model starts
off on the right foot and isn't misguided by seeing low-quality data early, while still
getting high coverage?

**How did you get from there into industry?**

I got an internship at Educational Testing Service through an IU alum from a while back who
was looking for people to help with a research project on content scoring using transformer
models. It was a great opportunity. I had a fairly simple project, but I think that's ideal
for an internship—one thing to look at.

That turned into a full-time position at ETS the next summer, and I worked there for three
years. Now I'm at Cisco. I was an applied scientist, now I'm a senior software engineer, but
it's basically the same work.

**What do you work on now?**

AI agents—everything's about agents now. Mine is essentially a customer service agent, but
not one that customers deal with. Cisco sells to other businesses, and those contracts come
up for renewal on a cycle. It's hard for the people responsible for renewals to know whether
customers are actually having a good experience. A lot of that information already existed;
it just wasn't accessible, because it was scattered and not reasonable to trawl through. The
agent condenses it—here are recent surveys, they're emphasizing that the RMA process takes a
long time—and then the rep can follow up with the RMA team.

**Most of your colleagues presumably don't have linguistics degrees. Does the background
differentiate you?**

I think so. Prompt engineering seems like something linguistics should be really helpful
for, but honestly it isn't particularly—you mostly want to be as clear and plain as you can.

But attention to sequential ordering helps a lot. In phonology you have these ideas about
ordering rules—you have to apply this rule before that one, because otherwise it bleeds the
condition some subsequent rule needs in order to apply. I think about that constantly when
I'm debugging: okay, this can't be the culprit, because that was happening beforehand, so
the conditions where it would have applied are no longer there. In a log you only get to see
the surface representation, and you're working backwards to figure out the phonology—what
was actually going on in the program at the time. Maybe that's a weird metaphor, but it
helps quite a bit.

**What skills from the program have been most valuable?**

Definitely debugging, and being able to pick up someone else's code and understand it. That
happened all the time in the program—you have to replicate some other paper, you find their
code on GitHub, and surprise, it doesn't work, because they stopped maintaining it a year
and a half ago. That happens constantly at my job now: somebody wrote this piece of software
a year ago, it's abandoned, and we need to rip out what's good and use it over here. Being
able to read something and figure out what it does when nobody wrote you docs is really
helpful.

Also the practical things. At ClingDing we had talks on how to use supercomputers, how to
use git. You need that, and you don't normally have a class that says here's how to use
version control, but it's such a huge time saver.

And being able to read a paper and think critically about it. Right now there's a ton of
material coming out with maybe empirical evidence and maybe not—maybe it's a blog post, or
you're sitting in an internal company presentation thinking, but how did they determine it's
actually better? Learning to approach things with an open mind but also interrogate them a
little was something I picked up in graduate school that's always been helpful at work.

**Any last reflections on the program?**

It's helped me in numerous ways that are almost intangible—I can't pin down exactly how, but
I know that it has, because prior to being in the program I never would have been able to
have a career like this. Some of what I picked up was on my own. I got really into servers
and Kubernetes. But I don't think I ever would have gotten interested in that if it hadn't
been for getting involved with the supercomputers here.
