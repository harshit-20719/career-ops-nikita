# career-ops-nikita

A plain-text workspace for running Nikita's job search. Everything lives in Markdown
and CSV so it stays greppable, diffable, and readable without any tooling — but there
is a small script that turns the tracker into a pipeline summary when you want one.

## The loop

1. **Find** a target → add a row to `targets/companies.csv`
2. **Apply** → add a row to `applications/applications.csv`, create a file in
   `applications/active/` from the template
3. **Track** → update `status` and `next_action` on the row after every interaction
4. **Prep** → `interviews/prep/` before each round; `interviews/debriefs/` right after
5. **Review** → every Friday, fill in a `weekly/` entry and re-plan

The CSV is the source of truth for *state*. The Markdown files hold the *detail* — job
descriptions, notes, who said what. If they disagree, fix the CSV.

## Layout

| Path | What's in it |
| --- | --- |
| `applications/` | Master tracker CSV + one Markdown file per live application |
| `contacts/` | People: recruiters, referrals, hiring managers, alumni |
| `targets/` | Companies worth applying to, tiered, with the "why" written down |
| `resume/` | Master resume content plus tailored per-application versions |
| `interviews/` | Prep notes, the STAR story bank, and post-interview debriefs |
| `outreach/` | Reusable message templates — cold email, referral asks, follow-ups |
| `weekly/` | Friday review: what went out, what came back, what's next |
| `scripts/` | `report.py` — pipeline summary and overdue-action check |

Each directory has its own README explaining its conventions and CSV schema.

## Daily use

```bash
# Where does everything stand?
python3 scripts/report.py

# What's overdue or due today?
python3 scripts/report.py --due

# Everything at a given stage
python3 scripts/report.py --status interview
```

No dependencies — Python 3.9+ standard library only.

## Conventions

- **Dates** are `YYYY-MM-DD`, always. Blank means unknown/not yet.
- **IDs** in `applications.csv` are `NNN-company-slug` (e.g. `007-stripe`). They match
  the filename in `applications/active/`.
- **Commit** after each session's updates. The git history doubles as an activity log —
  `git log --oneline` shows exactly how active the search has been week to week.
- **Nothing sensitive** goes in this repo: no offer letters with personal details, no
  full compensation packages tied to named individuals, no private notes about people
  you'd be uncomfortable having them read. Salary *ranges* from public postings are fine.

## Status values

Applications move through these, defined in `applications/README.md`:

`prospect` → `applied` → `screen` → `interview` → `onsite` → `offer`

Terminal states: `rejected`, `withdrawn`, `ghosted` (no reply 21+ days after last contact).
