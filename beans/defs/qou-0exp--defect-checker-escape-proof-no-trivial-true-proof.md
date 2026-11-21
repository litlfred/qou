---
# qou-0exp
title: 'DEFECT (checker escape): proof-no-trivial-true / proof-statement-integrity / proof-substantive / proof-not-machine-trivial / proof-narrative-lean-equiv ALL PASSED on surreal-squeeze.lean''s ''theorem : 0<e and e<1 := <h_pos,h_inf>'' -- a hypothesis-repackaging tautology that also did not state the .md claim (which is over R(eps), not R). Detectors miss conclusion-equals-conjunction-of-hypotheses'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T01:06:34Z
updated_at: 2026-11-21T18:00:00Z
parent: qou-5vkl
---

- **Round 91 (`https://github.com/litlfred/qou/pull/8413`, head `1d95d75db1b41a96e3b4987d5771f9fd945187c9`)**: Formalized theorem + 80-dps witness (`status: in-progress`).

## 2026-11-21 (thread: Design the remaining Lean vacuity detectors)

Rule 4 hypotheses-conjunction-is-conclusion plus by-exact / And.intro unwrapping, in PR #8919. Corpus: rule 4 finds 0, unwrapping adds 2 rule-3 hits (acoustic_horizon_regularity new and ledgered needs-agent; discrete_vortex_spectrum already ledgered). Selftest units pin the 4 caught spellings and the applied-component negative. Not covered: exact tuples inside multi-line tactic blocks (needs elaboration). Open until #8919 merges.
