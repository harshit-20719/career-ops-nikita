# Application packages

One self-contained HTML file per role. Everything needed to apply is inside:
the tailored resume (embedded, downloadable), the route in, the cover note with
a copy button, likely questions, what to ask, risk flags, and a pre-send
checklist.

## Open them locally

Download the file and open it in a browser. **The resume download only works
from a local file** — a published artifact runs sandboxed and blocks any
download the page starts itself, data URIs included. The rest of the page
works either way, but the point of these is the download.

No network needed. The PDF is embedded as base64, so the file works offline
and will keep working after this repo's container is gone.

## Rebuild

```bash
python3 scripts/build_package.py                 # all roles
python3 scripts/build_package.py good-health     # one role
```

Role content lives in `ROLES` in `scripts/build_package.py`. To add a role,
build its tailored resume first with `scripts/build_resume.py`, then add an
entry pointing at the PDF.

## Current packages

| File | Role | Fit / Odds |
| --- | --- | --- |
| `ferty9-package.html` | Senior Manager / AGM — Strategy, CEO's Office | 4.3 / 4.0 |
| `entrepreneurs-first-package.html` | Talent Investor — Associate | 4.2 / 3.0 |
| `good-health-package.html` | Chief of Staff | 3.6 / 4.0 |

Each was scored from the full job description, not the listing.
