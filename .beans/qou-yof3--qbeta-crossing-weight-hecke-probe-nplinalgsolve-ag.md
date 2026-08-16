---
# qou-yof3
title: 'qbeta_crossing_weight_hecke_probe: np.linalg.solve against the identically-singular Gram'
status: todo
type: bug
priority: high
created_at: 2026-08-16T13:39:23Z
updated_at: 2026-08-16T13:39:23Z
---

`computations/qbeta/qbeta_crossing_weight_hecke_probe.py:128` runs

    np.linalg.solve(gram.G, np.ones(6))

to obtain the cointegral `omega = G^-1 . 1`. Under convention D the H_3 Gram
form `G` is **identically singular over Q(q)** — its radical is exactly
ker(H_3 -> TL_3), of dimension `3! - Catalan(3) = 6 - 5 = 1`. This is not a
q_0 artefact: `det G == 0` generically in q
(docs/audits/2026-08-16-s2-gram-radical-independent-revalidation.md), and the
vanishing is proved sorry-free for all n by
`QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`
(docs/audits/2026-08-16-tl-all-n-weight-vanishing.md).

The call is UNGUARDED. Every other site in the corpus that touches this form
handles the degeneracy: `pyhecke/gram.py:407` uses `np.linalg.pinv`,
`gram.rs:339` uses a rank-one-shift Moore-Penrose, `pyhecke.gram.gram_inverse`
deliberately raises, and `confinement-operator-selection.py:195` routes through
`_pg_safe_inverse` (an SVD rank guard). This one does not — so it either raises
LinAlgError or, worse, returns a numerically meaningless vector from a
near-singular float64 solve.

This is a WRONG ANSWER, not a slow one, which distinguishes it from the rest of
the TL_n compute move (where the discarded dimensions contribute exactly zero
and the change is pure speed).

Scope (a): the defect is in this call site. I have not checked whether any
result derived from this probe was carried into an audit doc or a downstream
probe; that is the follow-up. It is a probe, so this is not a production defect.

Fix options, cheapest first:
  1. Route through `pyhecke.gram.safe_inverse` (the existing SVD rank guard).
  2. Solve on the 5-dimensional TL_3 quotient, where the form is genuinely
     non-singular and no pseudo-inverse is needed. This is the correct fix and
     is the same move tracked under qou-8iru.

Estimated effort ~1 h for option 1. Independent of the wider TL_n move.

Found during the TL_n consumer survey, PR #5241.
