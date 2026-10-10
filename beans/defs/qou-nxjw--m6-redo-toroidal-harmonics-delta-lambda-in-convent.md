---
# qou-nxjw
title: 'M6: redo toroidal-harmonics-delta-lambda in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:08Z
updated_at: 2026-10-10T09:04:19Z
parent: qou-d8c7
---

mass-theory/toroidal-harmonics-delta-lambda.md:12 sets z = sqrt(q)/(1+q), w = z^2 (1 user). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: redone in D on PR #7562 (subagent, reviewed). The C identity w=z^2=1/(2(cosh eta+1)) fails under D (sympy). z_D^2 gives x=0.332<1, no toroidal reading. Bar-invariant w = z_D z_- = 1/[2]_q^2 = 1/(2(cosh 2eta+1)) gives x = cosh 2eta. Golden-ratio 0.12% near-match does not survive (x=3/2 lands 14.7% below c_lambda^exp, which is itself circular). OPEN: whether z_D z_- is the right variable; link to the z-recursion never established. Also: ToroidalHarmonicsBasis.lean x_of_w docstring and computations/qbeta/toroidal_harmonics.py (C comments, scipy float64 lpmv) not edited. Stays open.
