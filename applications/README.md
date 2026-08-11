# Applications

`applications.csv` is the source of truth for pipeline state. One row per application,
forever — rejected and withdrawn rows stay in the file so the history survives.

## Adding an application

1. Append a row to `applications.csv`. The `id` is the next number plus a company slug:
   `008-figma`.
2. Copy `active/TEMPLATE.md` to `active/008-figma.md` and fill it in — paste the full
   job description while the posting is still up, because they get taken down.
3. When it reaches a terminal state (`rejected` / `withdrawn` / `ghosted`), leave the
   CSV row alone and move the Markdown file to `archive/` (create it when first needed).

## Column reference

| Column | Meaning |
| --- | --- |
| `id` | `NNN-company-slug`, matches the filename in `active/` |
| `company` | Company name as they write it |
| `role` | Exact title from the posting, not your paraphrase |
| `location` | City, or `Remote` |
| `work_mode` | `remote` / `hybrid` / `onsite` |
| `source` | `referral` / `recruiter` / `job-board` / `direct` / `network` / `event` |
| `url` | Link to the posting |
| `date_applied` | When you actually submitted. Blank while status is `prospect` |
| `status` | See below |
| `next_action` | The single next thing *you* owe. Blank only if the ball is genuinely theirs |
| `next_action_date` | When it's due. `scripts/report.py --due` flags anything past today |
| `contact` | Primary human at the company — should also exist in `contacts/contacts.csv` |
| `resume_version` | Filename stem under `resume/versions/` |
| `comp_range` | From the posting or the recruiter screen. Quote it if it has a comma |
| `notes` | One line. Anything longer belongs in the Markdown file |

## Status values

| Status | Means |
| --- | --- |
| `prospect` | Identified, not submitted yet |
| `applied` | Submitted, no human response |
| `screen` | Recruiter or phone screen scheduled or done |
| `interview` | In the interview loop (any round with the team) |
| `onsite` | Final round / onsite / panel |
| `offer` | Offer extended |
| `rejected` | They said no |
| `withdrawn` | You said no |
| `ghosted` | No reply for 21+ days after your last contact. Applied with no answer counts |

`ghosted` exists so the pipeline number stays honest. A stack of `applied` rows from
three months ago is not a pipeline.

## CSV hygiene

- Quote any field containing a comma: `"€90k-110k, plus equity"`.
- Never reorder or rename columns without updating `scripts/report.py`.
- One row per application, not per interview round. Rounds go in the Markdown file.
