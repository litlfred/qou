---
# qou-pn5j
title: 'GAP: derive Whitehead adjoint Reidemeister torsion |tau(L5a1)|=2sqrt2 from octahedron NZ data (upgrades c_sigma=2^{-3/4} from identification to derivation)'
status: completed
type: task
priority: normal
created_at: 2026-08-02T09:51:26Z
updated_at: 2026-08-08T02:40:00Z
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

---

## 2026-08-08 (later) — the c=1 anchor no longer rests on 4_1 alone.

The weakest point of the law `c_sigma = 2^{-1/2}|tau_DG|^{-1/2}` was that its
constant is calibrated at c=1 on the FIGURE-EIGHT ALONE, in a quadratic trace
field, from this corpus's own extraction. Fixed with an independent published
source.

Ohtsuki, "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot"
(library/ki52/ki52.pdf), Theorem 1.1 -- a RIGOROUS THEOREM, not a fit:

    <5_2>_N = e^{N zeta} N^{3/2} omega (1 + sum kappa_i (2 pi i/N)^i + O(N^{-d-1}))
    omega   = e^{-i pi/4} ((1 - y_0)/(2 y_0 + 1))^{1/2},  (y_0-1)^3 = y_0, Im y_0 > 0

That omega reproduces the paper's printed 0.0901905774... - i 0.6499757866... to
all 10 digits, so the formula is recovered rather than guessed. Then:

    predicted from the law, k from 4_1 alone   c_sigma(5_2) = 0.65620337051419987
    Ohtsuki |omega|                                         = 0.65620337047140662
                                     agreement: 10 digits = all the paper prints

NOTHING FITTED: k from 4_1, |tau_DG(5_2)| from the geometry, omega from the
paper. 5_2 is two-bridge, so Garoufalidis-Yoon prove 1-loop = adjoint torsion for
it -- both sides theorem-backed.

CLOSED FORM, as a by-product. Since |omega|^2 = 1/(2|tau_DG|):

    |tau_DG(5_2)| = |2 y_0 + 1| / (2 |y_0 - 1|)       exact to working precision

y_0 has minimal polynomial y^3 - 3y^2 + 2y - 1, discriminant -23 -- the same as
x^3 - x - 1, i.e. the 5_2 trace field (PR #4658) and the field of the ambiguity
generator sqrt(rho) (PR #4697). A CUBIC field, so this is not a quadratic-field
coincidence.

SCOPE. Strengthens the c = 1 leg only. 5_2 is one-cusped, so this says nothing
new about c-dependence: the only c = 2 test is still the Whitehead link, and
c = 3 is still supporting-only. And it confirms the constant on an independent
point; it does not prove the law. The prefactor form c_sigma ~ |tau|^{-1/2}
remains the carried assumption, so the DERIVATION status change is still left to
review.

Probe: computations/probes/one_loop_ohtsuki_5_2_crosscheck_probe.py
Audit: docs/audits/2026-08-08-per-cusp-factor-dissolves.md (addendum)

<!-- 2026-08-08T02:20:00Z branch claude/dg-scope-correction -->

---

## 2026-08-08 — CLOSED. IDENTIFICATION -> DERIVATION, user-authorized.

Status change made only after the user reviewed the evidence; I deliberately did
not flip it myself in the two prior passes.

Both objections that reopened this bean on 2026-08-07 are answered, separately:

  (1) the geometric quantity was not well defined -> it is now. The DG 1-loop
      invariant is triangulation-invariant across 13 manifolds x 25 randomised
      triangulations, with controls. |tau_DG(L5a1)| = sqrt(2).
  (2) the per-cusp factor was fitted against its own ambiguity -> the factor does
      not exist. k_c := c_sigma |tau_DG|^{1/2} is the SAME constant 2^{-1/2} at
      c = 1 and c = 2 to 17 digits (a per-cusp factor needs k_2/k_1 = sqrt 2;
      measured 0.999999999999999995). No free parameter remains.

THE CHAIN, with nothing adjustable:
  |tau_DG(4_1)| = sqrt(3)/2 (DG eq 3.2, given) ;  c_sigma(4_1) = 3^{-1/4}
  (measured, 17 digits) ;  k := 2^{-1/2} (one number, read off 4_1) ;
  |tau_DG(L5a1)| = sqrt(2) (computed) ;  => c_sigma(L5a1) = 2^{-3/4}, matching
  the 20-digit measured value to ~17 digits as a PREDICTION.

k is independently confirmed on 5_2 against Ohtsuki's Theorem 1.1 (a rigorous
theorem) to 10 digits, on a CUBIC trace field.

THE ONE CARRIED ASSUMPTION: the 1-loop prefactor form c_sigma ~ |tau|^{-1/2}.
Validated on 4_1 (17 digits), 5_2 (10 digits vs Ohtsuki), consistent on L6a4
(0.35%) -- but NOT PROVED, and no theorem covers the 2-cusped link case
(Garoufalidis-Yoon is two-bridge knots). Cite the upgrade WITH that clause:

  "c_sigma = 2^{-3/4} is DERIVED from the triangulation-invariant DG 1-loop
   invariant of L5a1 plus a single c=1 calibration, ASSUMING the prefactor form
   c_sigma ~ |tau|^{-1/2}."

Proving the prefactor form for links is the real remaining gap and is a research
problem, not a computation. Not beaned as actionable work here.

Audit: docs/audits/2026-08-08-c-sigma-derivation-status.md

<!-- 2026-08-08T02:40:00Z branch claude/dg-scope-correction — closed -->
