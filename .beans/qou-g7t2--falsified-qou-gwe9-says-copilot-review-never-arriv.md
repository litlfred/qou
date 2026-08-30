---
# qou-g7t2
title: 'FALSIFIED: qou-gwe9 says Copilot review never arrives — it did, on #6121'
status: scrapped
type: task
priority: normal
created_at: 2026-08-30T08:01:18Z
updated_at: 2026-08-30T08:40:25Z
---

## SCRAPPED 2026-08-30 — a sibling got there first, and measured it better

Superseded by the REOPENED section of `qou-gwe9` and by
`docs/audits/2026-08-30-copilot-review-works-again.md`, both of which landed on
main before this bean existed. I found the conflict only when rebasing.

Their measurement is strictly stronger than mine:

  - n=2 CONTROLLED with timings (qou#6122 requested 07:24Z -> reviewed 07:27:39Z;
    folio-assistant#153 requested 07:48Z -> reviewed 07:51:52Z), where I had one
    uncontrolled observation on #6121;
  - the second row is a DIFFERENT REPO, which rules out a qou-specific setting --
    something one observation in one repo cannot do;
  - an actionable rule falls out of it (request ONCE per PR when the branch is
    ready, wait ~3-4 min), which mine did not supply.

**And they correct my framing.** I titled this 'FALSIFIED'. That is too strong:
`qou-gwe9` recorded n=2 controlled, called its five background PRs weak
evidence, and said outright it did NOT prove org-level disablement. A bean that
scoped itself honestly is not falsified by the behaviour later changing --
it is superseded. The stronger claim was mine, not the bean's.

Fourth time this session I have re-derived something the corpus already held
(the others: alpha's derivation in my own #5864, the D-frame H_3 weights, the
bar-parity results). Same root cause each time: I search the vocabulary I just
invented rather than the corpus's.
