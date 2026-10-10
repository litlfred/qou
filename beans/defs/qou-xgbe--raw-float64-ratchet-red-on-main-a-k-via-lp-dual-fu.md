---
# qou-xgbe
title: 'raw-float64 ratchet RED on main: a-K-via-lp-dual-full.witness.json regressed 395 -> 867 fields at 75fc8996d7'
status: completed
type: task
priority: normal
created_at: 2026-08-11T00:36:29Z
updated_at: 2026-09-08T07:45:46Z
---

RESOLVED -- and the bean's own number was stale in the OTHER direction.

I nearly re-filed this by READING the committed witness-raw-float64-audit.
witness.json, which still says 812 for this file. Running the audit live at main
08b6ff7e7d says:

      54 -> 38    computations/a-K-via-lp-dual-full.witness.json   [DRAINED]

i.e. the file is now BELOW its baseline, not above it. The 395 -> 867 regression
this bean recorded at 75fc8996d7 was real then and has since been drained by the
qou-j6gb / qou-ftuv work. The committed audit witness is itself stale output.

LESSON, worth carrying: for ratchet state, RUN THE GATE, do not read its last
committed witness. Same failure shape as the scriptCommitSha trap in AGENTS.md
-- a committed artifact describing a moving quantity.

## 2026-09-08: canonical tracker for the recurring "raw-float64 ratchet is RED on main" event is qou-sknx (most recent OPEN one, 2026-09-04); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 6 / §7.3 C7. Seven beans (08-11 … 09-06) record one recurring event; this one is kept as-is because its body carries its own finding.
