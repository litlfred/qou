---
# qou-yaqm
title: 'BUG: hecke offset drops generator sign in load_atom_braids (delta_lambda_jsj_phase3)'
status: todo
type: task
created_at: 2026-08-21T15:03:20Z
updated_at: 2026-08-21T15:03:20Z
---

delta_lambda_jsj_phase3.py:69-76 builds the multi-nucleon braid words with `[g + 3 for g in n]`. The elements of `n` are SIGNED braid letters, so -2 (sigma_2^-1) maps to +1 (sigma_1), not to -5. Measured on the deuteron: as-coded word is [1,-2,1,-2,1,-2,1,1,2,1,1,3,4,1,4,1,4,1,4,4,1,4,4] (writhe +17, det 0); sign-correct is [...,4,-5,4,-5,4,-5,4,4,-5,4,4] (writhe +9, det 3472). Same bug in the T / 3He / 4He rows. Affects every closure this producer hands to SnapPy. Component count is unchanged (3) so the adjudication verdict in docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md does not depend on the fix.

Fix: sign(g)*(abs(g)+k). Found while adjudicating qou-e5jf (PR #5350).
