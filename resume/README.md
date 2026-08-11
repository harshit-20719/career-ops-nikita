# Resume

`master/resume.md` holds every bullet you might ever use — the superset. It is not a
document you send anyone; it's the source material.

`versions/` holds the tailored cuts. Each one is a selection from the master, reordered
and reworded for a specific application, and each is named in the `resume_version`
column of `applications/applications.csv` so you know exactly what they read.

## Naming

`YYYY-MM-<role-slug>.md` — e.g. `2026-08-pm-platform.md`. Reuse a version across similar
applications rather than making a new file per company; only cut a fresh one when the
role type genuinely differs.

## Tailoring, in order

1. Read the job description twice. List their top five requirements.
2. Pull the bullets from `master/resume.md` that speak to those five. Cut everything
   that doesn't earn its line.
3. Reorder so the most relevant experience is highest on the page.
4. Match their vocabulary where it's honest to do so — if they say "platform" and you
   said "infrastructure" for the same work, use theirs.
5. Check every number is still true after the rewrite.

## Writing bullets

The form that works: **action → what you did → measurable result**.

> Rebuilt the billing reconciliation pipeline, cutting month-end close from 6 days to 2
> and eliminating ~40 hours of manual review per cycle.

Not: *"Responsible for billing systems."*

Rules that keep it honest:
- Lead with the verb. Never "Responsible for" or "Helped with".
- Quantify when you can, and only with numbers you could defend under questioning.
- If you can't measure it, say what changed anyway — scope, speed, who it unblocked.
- No adjectives about yourself. "Highly motivated" costs a line and says nothing.

## Format

Keep the master in Markdown. Export to PDF only when submitting, and send PDF unless
they explicitly ask for `.docx`. One page if under ~8 years of experience, two at most.

Filename for the file you actually send: `Nikita-<Lastname>-<Role>.pdf`. "resume.pdf"
in a recruiter's downloads folder is invisible.
