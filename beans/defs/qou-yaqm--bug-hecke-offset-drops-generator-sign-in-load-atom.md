---
# qou-yaqm
title: 'BUG: hecke offset drops generator sign in load_atom_braids (delta_lambda_jsj_phase3)'
status: in-progress
pr: 8344
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T15:03:20Z
updated_at: 2026-10-04T15:16:46Z
parent: qou-v2om
---

delta_lambda_jsj_phase3.py:69-76 builds the multi-nucleon braid words with `[g + 3 for g in n]`. The elements of `n` are SIGNED braid letters, so -2 (sigma_2^-1) maps to +1 (sigma_1), not to -5. Measured on the deuteron: as-coded word is [1,-2,1,-2,1,-2,1,1,2,1,1,3,4,1,4,1,4,1,4,4,1,4,4] (writhe +17, det 0); sign-correct is [...,4,-5,4,-5,4,-5,4,4,-5,4,4] (writhe +9, det 3472). Same bug in the T / 3He / 4He rows. Affects every closure this producer hands to SnapPy. Component count is unchanged (3) so the adjudication verdict in docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md does not depend on the fix.

Fix: sign(g)*(abs(g)+k). Found while adjudicating qou-e5jf (PR #5350).



CORRECTION (2026-08-21, second agent, re-verified from the tree on branch claude/deuteron-knot-adjudication-redo-2026-08-21):

1. Line numbers are 73 / 75 / 77, not 69-76.

2. 'Component count is unchanged (3)' is TRUE FOR THE DEUTERON ONLY. Re-measured by exact cycle count of the induced permutation: D 3 -> 3, T 4 -> 4, but 3He 2 -> 4. The bug DOES change the topology of the 3He closure. The adjudication verdict's independence from the fix still holds, because that independence was only ever claimed for the deuteron row (audit doc §4(a) scopes it correctly); this bean stated it unscoped while naming the T / 3He / 4He rows.

3. The as-coded deuteron closure is SPLIT. The as-coded word reaches only max|gen| = 4 on 6 strands, so strand 6 is never touched and the closure is (something on 5 strands) + a disjoint unknot. That is why det = 0 -- a split link has vanishing Alexander polynomial. The sign-corrected word reaches sigma_5. So det 0 is the signature of the defect, not an incidental number.

4. BROADER THAN ONE PRODUCER. The same [g + k for g in ...] pattern appears 8 more times in computations/atom_braid_words.py (lines 101, 103, 105, 110, 111, 114, 115, 157). The proton word p = [1,-2,1,-2,1,-2,1,1,2,1,1] also carries negative letters, so [g + 3 for g in p] is affected too.

Fix is unchanged: sign(g)*(abs(g)+k).


## Progress Update (PR #8344)
- Formalized in Lean 4.24.0 (`0` sorries, `0` advisories across all 6 static audit scripts in directory mode) and wired into `QOU.lean`.
- Verified at `mp.dps = 50` with 2-commit witness stamp (`291dd36ab34a42866efb444b586e05f0b621971e` -> `38f4a86a95df28f43dea57e331b0e3b812f7f526`) in PR #8344.
