# Contacts

People who can move an application forward, and the state of each relationship.

One row per person in `contacts.csv`. If someone changes companies, update the row —
the relationship is what's being tracked, not the job.

## Column reference

| Column | Meaning |
| --- | --- |
| `name` | Their name |
| `company` | Current employer |
| `role` | Their title |
| `relationship` | `recruiter` / `hiring-manager` / `referral` / `former colleague` / `alumni` / `cold` / `friend` |
| `email` | Preferred address |
| `linkedin` | Profile URL |
| `first_contact` | When you first spoke |
| `last_contact` | Most recent exchange — update this every time |
| `next_touch` | When to reach out again. Blank means no scheduled follow-up |
| `intro_via` | Who introduced you, if anyone |
| `notes` | One line: what they offered, what they asked for, what you owe them |

## How to use it

**Before applying anywhere**, grep this file for the company. A referral converts far
better than a cold application, and you may already know someone.

```bash
grep -i stripe contacts/contacts.csv
```

**`next_touch` is the important column.** Relationships decay silently. Set a date
whenever a conversation ends without a concrete next step — 2–4 weeks out is a normal
cadence for a warm contact, longer for someone you barely know.

## Etiquette worth keeping

- Ask for advice, not a job. The referral follows from the conversation.
- Follow up once after silence, then let it rest. Twice is persistent; three times is a
  problem.
- When someone refers you, tell them the outcome — including rejections. It's the whole
  reason they'll do it again.
- Close the loop with the people who helped, once the search ends.
