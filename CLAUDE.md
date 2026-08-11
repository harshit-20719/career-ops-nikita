# Working in this repo

A job-search workspace, not a software project. There's no build, no test suite, and
no application — just structured Markdown and CSV, plus one report script.

`README.md` has the layout and the workflow. Read it first.

## Rules

- **`applications/applications.csv` is the source of truth for state.** Markdown files
  hold detail. If they disagree, the CSV wins and the Markdown gets fixed.
- **Never invent facts.** Don't fill in a company, a date, a salary, or a person's name
  from inference. Blank is correct when the answer isn't known — ask instead.
- **Never write bullets for the resume that aren't backed by something Nikita said.**
  An invented accomplishment is the one failure mode that actually damages the search:
  it survives until an interviewer asks a follow-up question.
- **Preserve columns.** `scripts/report.py` reads `applications.csv` positionally by
  header name; renaming or removing a column breaks it. Update the script in the same
  change if a column has to move.
- **Dates are `YYYY-MM-DD`.** Blank means unknown, not zero.
- **Terminal rows stay.** Rejected and ghosted applications are never deleted from the
  CSV — the history is the point.

## Common requests, and where they land

| Ask | What to touch |
| --- | --- |
| "Add this job" | Row in `applications.csv` + file from `applications/active/TEMPLATE.md` |
| "Where does everything stand?" | `python3 scripts/report.py` |
| "What's overdue?" | `python3 scripts/report.py --due` |
| "Tailor my resume for X" | New file in `resume/versions/` from the master, per `resume/README.md` |
| "Draft a follow-up" | Start from `outreach/templates/`, then make it specific |
| "Prep me for this interview" | `interviews/prep/`, using the job description in the application file |
| "Weekly review" | New `weekly/YYYY-WW.md` from the template, driven by the report output |

## Tone for drafted messages

Short, specific, no filler. The templates in `outreach/` explain what makes each one
work — follow that guidance rather than producing generic professional prose. A draft
that could have been sent to any company is a bad draft.

## Privacy

Nothing sensitive gets committed: no offer letters with personal details, no candid
notes about named individuals, no compensation tied to a person. `private/` is
gitignored for anything that needs to stay local.
