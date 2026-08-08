---
# qou-pn5j
title: 'GAP: derive Whitehead adjoint Reidemeister torsion |tau(L5a1)|=2sqrt2 from octahedron NZ data (upgrades c_sigma=2^{-3/4} from identification to derivation)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T09:51:26Z
updated_at: 2026-08-08T00:50:00Z
---

## Context

PR #4571 / bean qou-k00d identified the Whitehead-link (L5a1) VC sub-leading
constant `c_σ = 2^{-3/4}` to **20 digits** (mpmath dps=100, N≤3000, van der Veen
exact colored Jones). The 1-loop template `c_σ = |τ_adjoint|^{-1/2}` is validated
on the figure-eight (same pipeline → `3^{-1/4}`, 17 digits, known `|τ(4_1)|=√3`).

Applying the template gives `|τ_adjoint(L5a1)| = 2√2 = 2^{3/2}`. This is
**inferred from c_σ via the template**, NOT independently derived — so the result
is an "identification", not a "derivation" (anti-laundering discipline).

## What's open (the honest gap)

Compute `|τ_adjoint(L5a1)| = 2√2` **independently** of inverting c_σ, from the
geometry of the Whitehead complement = regular ideal octahedron. Two routes:

1. **Dimofte–Garoufalidis 1-loop** `τ = ±½ det(A·diag(1/z'') + B·diag(z'))` from
   the L5a1 Neumann–Zagier matrices A,B + shapes z. Needs the triangulation /
   NZ data — `import snappy; M=snappy.Manifold('L5a1')` is the natural source but
   SnapPy is unavailable in the current sandbox. Get a box with SnapPy, or input
   the 4-tetrahedron gluing of m129 by hand and verify against the known Vol=4G.
2. **Porti adjoint torsion** via Fox calculus on the Whitehead 2-generator group
   presentation at the geometric SL₂(ℂ) rep. Doable by hand but error-prone;
   cross-check the magnitude against 2√2.

Note the 2-cusp normalization subtlety: Porti torsion depends on a boundary-curve
basis; confirm the c_σ-convention matches the meridian normalization (as it does
for the 1-cusp figure-eight).

## Done-when

`|τ_adjoint(L5a1)| = 2√2` reproduced from first principles (route 1 or 2),
independent of c_σ. Then `c_σ = 2^{-3/4}` upgrades identification → derivation and
may be recorded as such (still audit-only unless wired via the categorical chain).

## Do NOT

- Do not "derive" 2√2 by inverting c_σ = 2^{-3/4} (circular — that's the
  identification already in hand).
- Do not wire c_σ = 2^{-3/4} to any production dashboard/script as canonical
  until it is a genuine derivation.

---

## 2026-08-07 — REOPENED. The derivation this bean was completed on does not stand.

This bean was marked `completed` because `|tau(L5a1)| = 2^{5/2}` was computed
from SnapPy NZ data by `whitehead_c_sigma_torsion.py`, satisfying the
anti-circularity requirement above. **That quantity is not well-defined.**

`|det J|` as implemented is NOT a topological invariant (PR #4691, merged).
Retriangulating the same manifold 25x (Pachner moves; controls: `is_isometric_to`
AND 212-bit volume identical, non-geometric solutions excluded):

    4_1, m003, m004   2 tet    1 distinct value    invariant
    5_2               3 tet    8                   VARIES  (one-cusped!)
    6_2               5 tet   15                   VARIES
    L5a1              4 tet    4                   VARIES
    L6a4              8 tet    8                   VARIES

The split is not about cusps — `5_2` is a one-cusped knot with eight values.
It tracks tetrahedron count. That is what defeats the non-circularity argument
specifically: it calibrates on `4_1`, a 2-tetrahedron manifold, i.e. the one
class that structurally CANNOT exhibit the dependence.

So `|tau(L5a1)| = 2^{5/2}` is a property of SnapPy's DEFAULT triangulation, not
of the link (it appears in a minority of trials), and the per-cusp factor
`2^{(c-1)/2}` is fitted against a sqrt(2) ladder of the same magnitude.

**`c_sigma = 2^{-3/4}` reverts to IDENTIFICATION.** The bean's "Do NOT" section
is still correct and is now the binding constraint again.

NOT affected: the NUMERICAL VALUE `c_sigma = 2^{-3/4}` stands to ~20 digits via
`whitehead_c_sigma_hiprec.py` (pure mpmath, van der Veen colored Jones + Neville;
no SnapPy, no det J). This removes a derivation, not a result.

Repair path is beaned separately — see the flattening bean below.

---

## 2026-08-08 — GAP CLOSED, and this bean's ORIGINAL inference was right.

The repair that this bean was waiting on is done (qou-fl4t):
`computations/one_loop_torsion.py` now computes the triangulation-invariant
Dimofte-Garoufalidis 1-loop invariant at any cusp number.

    |tau_DG(4_1)|  = sqrt(3)/2      |tau_DG(L5a1)| = sqrt(2)      |tau_DG(L6a4)| = 8

THE PER-CUSP FACTOR DISSOLVES. Against those values,

    k_c := c_sigma * |tau_DG|^{1/2}   =  2^{-1/2}  at c = 1 AND c = 2, to 17 digits.

A per-cusp factor would require k to move by sqrt(2); measured k_2/k_1 =
0.999999999999999995. So the law is c_sigma = 2^{-1/2}|tau_DG|^{-1/2} with no
c-dependence, and calibrating on 4_1 alone predicts c_sigma(L5a1) = 2^{-3/4} to
17 digits with NOTHING FITTED.

THE ORIGINAL TEMPLATE INFERENCE WAS CORRECT. Writing the law as
c_sigma = (2|tau_DG|)^{-1/2}, the T in the bare template c_sigma = |T|^{-1/2} is
T = 2|tau_DG|:

    T(4_1)  = sqrt(3)      (the normalization this corpus calls the known value)
    T(L5a1) = 2 sqrt(2)    <-- exactly this bean's title
    T(L6a4) = 16

So |tau_adj(L5a1)| = 2 sqrt(2) — the value whitehead_c_sigma_torsion.py declared
an error and "corrected" to 2^{5/2}, inventing the per-cusp factor to absorb the
difference. There was nothing to absorb: the factor of 2 was the wrong
determinant. This bean's inference stands, and is now DERIVED from geometry
rather than read off the template.

WHAT THE DERIVATION NOW RESTS ON. Both objections that demoted c_sigma = 2^{-3/4}
to IDENTIFICATION are answered: the quantity is well-defined (invariant over 25
randomisations each of 13 manifolds), and nothing is fitted (c=1 calibration,
c=2 prediction). The remaining assumption is the PREFACTOR FORM
c_sigma ~ |tau|^{-1/2}, validated on 4_1 to 17 digits by
whitehead_c_sigma_fig8_calib.py but not proved. Anyone moving this bean to
DERIVATION should state that assumption explicitly; I am recording the evidence
and leaving the status change to review rather than flipping it myself, since
this bean's "Do NOT" section exists precisely to prevent a premature upgrade.

c=3 is SUPPORTING ONLY: k_3/k_1 = 1.0035 (0.35%), but the Borromean tower's own
witness flags an unresolved normalization+cusp offset and returns p = 1.4993
vs the exact 3/2.

Audit: docs/audits/2026-08-08-per-cusp-factor-dissolves.md
Probe: computations/probes/one_loop_c_sigma_percusp_dissolution_probe.py

<!-- 2026-08-08T00:50:00Z branch claude/dg-scope-correction -->
