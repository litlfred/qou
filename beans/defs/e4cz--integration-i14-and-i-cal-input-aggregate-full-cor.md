---
# e4cz
title: 'Integration: I14 and I-cal-input aggregate full-corpus re-runs'
status: todo
type: task
priority: normal
created_at: 2026-06-21T21:41:08Z
updated_at: 2026-08-21T16:01:22Z
---

## I14 half ANSWERED 2026-08-21 (PR #5373)

This bean carries the re-scope the watcher queue asked for
(`compute-integration-watcher-queue.json` entry `63a90056cb57`, converted
here). The I14 leg is now measured; the I-cal-input leg is untouched.

**The queue's own note was stale, in the direction of an all-clear.** It read
"scans only 32 files, PROV_MISSING=0, completeness 1.000 ... UNSURE/STALE".
The scan root has since been widened (`(HERE.parent).rglob("*.witness.json")`
walks the whole compute tree), so the audit DOES now produce a full-corpus
figure and the finding is real:

```
total scanned          : 2682
PROV_OK                : 2325
PROV_AUDIT_EXEMPT      :   74
PROV_EXEMPT_NO_READER  :  227
PROV_EXEMPT_ACKNOWLEDGED:   3
PROV_MISSING           :   52   (55 before this PR's drain)
PROV_PARSE_ERROR       :    1
completeness ratio     : 0.980
```

Neither the dashboard's old "26 of 707" nor the local "0 of 32" is the current
number. Do not quote either.

**The committed audit witness was also stale** — 2026-08-01, recording
`total_scanned 2296 / prov_missing 10`. So the class grew 10 -> 55 with nothing
observing it, because the audit is in no gate array and no workflow. Third
instance of the qou-j6gb pattern.

Live tracker for the drain + the wiring decision: bean `qou-7aum`.
