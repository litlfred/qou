---
# qou-idvt
title: 'MATHLIB GAP: ideal-tetrahedron hyperbolic volume theory (blocks qou-krvm (iv) + qou-7y3g)'
status: scrapped
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T08:00:00Z
updated_at: 2026-10-04T15:11:02Z
---

Split out so two beans stop each carrying the same "large Mathlib gap" note.
**This one piece of infrastructure is the sole remaining blocker on both.**

## Who is blocked

  * `qou-krvm` hypothesis **(iv)** — the hyperbolic volume functional is CONCAVE
    and symmetry-INVARIANT on the angle-structure polytope (Rivin). With (i)-(iii)
    now Lean-proved for both anchors (PR #4513 m004, PR #4725 L6a4), (iv) is the
    ONLY thing between qou-krvm and closure.
  * `qou-7y3g` — `Vol(4_1) = 2*Cl_2(pi/3)` and `Vol(B_3) = 8*Catalan` are
    numerical only.

Both also feed `qou-skum`: if the volumes are FORCED by the cell decomposition
rather than measured, they reclassify from untraceable literals to `structural`
in the no-free-parameter certificate. That reclassification currently rests on
numerics.

## What Mathlib actually has (VERIFY before scoping — do not trust this list)

Mathlib has no ideal-simplex volume, no Mostow rigidity. What it may have, and
what makes the gap narrower than "build hyperbolic geometry":

  * `QOU.Archimedean.ClausenFunctionMathlibFiller` ALREADY EXISTS in this tree
    and is in the `FigureEightComplexVolume` import cone. **Start here.**
  * `Mathlib.Analysis.SpecialFunctions` — check for Clausen / Lobachevsky.
  * `FigureEightComplexVolume.V₄₁_zero_re` already states `V_41(0) = 2*Cl_2(pi/3)`
    EXACTLY at the Lean level (exact because `a_2` is purely imaginary).

So the corpus already has the closed FORM. What is missing is the bridge from
"this closed form" to "the hyperbolic volume of the manifold" — a much smaller,
much better-posed target than "hyperbolic volume theory".

## Suggested decomposition (tiered, so partial credit is real)

  T1  Lobachevsky function `Lambda(x) = -int_0^x log|2 sin t| dt` and its basic
      identities, on top of the existing Clausen filler.
  T2  Ideal-tetrahedron volume `Vol(alpha,beta,gamma) = Lambda(alpha)+Lambda(beta)+Lambda(gamma)`
      for a positive angle triple summing to pi.
  T3  **Concavity of T2 in the angles** — this alone discharges `qou-krvm` (iv)
      for the tetrahedral case, since invariance is immediate once the volume is
      a symmetric function of the angle triple. T3 IS THE PRIZE; T1-T2 are means.
  T4  The regular triple maximises T2 (gives `Vol(4_1) = 2*Lambda(pi/3)*...`
      forms and feeds `qou-7y3g`).

T3 is worth attempting on its own: concavity of a sum of `Lambda` over the
simplex `alpha+beta+gamma = pi` is a real-analysis statement, not a geometry one,
and does not need any manifold theory.

## GUARD — this bean exists BECAUSE of the laundering rule

Do NOT axiomatise "the volume functional is concave" as a Lean class and consume
it downstream to close `qou-krvm`. AGENTS.md: "Axiomatization is NOT a Proof."
A `class RivinConcavity` with a `sorry`-ed instance would make (iv) look
discharged while proving nothing. Either prove T3 or leave (iv) open and
labelled. `qou-7y3g` carries the same guard for the volume identity.

## Note on scale

This is infra-scale, not session-scale, as `qou-7y3g` says. But T3 alone may be
session-scale, and it is the piece that actually unblocks a downstream result.
Attack T3 first; do not start by building hyperbolic geometry.

---

## 2026-08-08 — T3's MATHEMATICAL CORE IS PROVED (sorry-free). Λ not needed.

`QOU/Archimedean/IdealTetrahedronConcavity.lean`. This bean assumed T3 needed
T1-T2 first (build Lobachevsky, then ideal-simplex volume, then concavity). **It
does not.** The concavity reduces to two trigonometric identities, and `Λ` does
not appear in the file at all.

Writing `f(α,β) = Λ(α)+Λ(β)+Λ(π−α−β)` with `Λ'' = −cot`, the Hessian is

    f_αα = −(cot α + cot γ)    f_αβ = −cot γ    f_ββ = −(cot β + cot γ)

and everything follows from:

  * `cot_cyclic_sum_eq_one` — `cot α cot β + cot β cot γ + cot γ cot α = 1`
    whenever `α+β+γ = π`. Hence `det H = 1` **exactly** (`hessian_det_eq_one`),
    not merely positive.
  * `cot_add_cot_pos` — `cot α + cot γ = sin β/(sin α sin γ) > 0`, so `f_αα < 0`.
  * `hessian_neg_definite` — negative definite at EVERY interior point.

Both identities are elementary (sine addition formula after clearing
denominators). No geometry, no manifold theory, no Rivin paper — the literature
was not needed.

**The awkward point is handled.** At `(π/4, π/4, π/2)` — L6a4's unique symmetric
point (`L6a4AngleStructure.unique_symmetric_point`) — `cot γ = 0`, the
off-diagonal vanishes, and the matrix looks degenerate. `det_eq_one_at_octahedron`
shows the determinant is still exactly 1 there. Since that is precisely the point
`qou-krvm` cares about, it is the case that had to work.

**Non-vacuity proved**: `regularTetrahedron` (m004's optimum) and
`regularOctahedron` (L6a4's) are exhibited, so `AngleTriple` is inhabited and the
universally-quantified theorems are not empty.

## WHAT THIS DOES NOT DO — read before citing

It does **not** close `qou-krvm` (iv), and the file says so. What is missing:

  1. `Λ` itself (T1) and `Vol = Λ(α)+Λ(β)+Λ(γ)` (T2). The corpus has `Cl_2` in
     `ClausenFunctionMathlibFiller` but no Lobachevsky function.
  2. `Λ'' = −cot`, which needs T1.
  3. The second-derivative test: "Hessian negative definite ⇒ strictly concave"
     needs Mathlib's `ContDiff`/`C²` machinery. Standard, but not free.

So the honest status is: **the part everyone assumed was hard is done; the
remaining part is plumbing.** T3 was mis-scoped in this bean as depending on
T1-T2 — it is the other way round for the *core*, though the plumbing does need
them.

Revised tiering: T1 (Lobachevsky on top of `Cl_2`) → T2 (`Vol` as the sum) →
**T3-core DONE** → T3-plumbing (second-derivative test) ⇒ `qou-krvm` (iv).

---

## 2026-08-08 (later) — T1 IS DONE. Two claims in this bean were stale.

`QOU/Archimedean/LobachevskyDerivative.lean` + `IdealTetrahedronShapeBridge.lean`,
both sorry-free (`#print axioms` clean, cone-built).

**Correction 1 — "the corpus has `Cl_2` but no `Λ`" was already false when
written.** `BlochWignerLobachevsky` has carried `Lob t = Cl_2 (2*t)/2` plus
`Lob_neg` / `Lob_zero` / `Lob_pi_div_two` / `Lob_pi` all along, and
`QOU/Knot/Clausen.lean` has carried `hasDerivAt_Cl_2_series`
(`Cl₂'(θ) = −log(2 sin(θ/2))` on `(0,2π)`). The same stale sentence is repeated
in `IdealTetrahedronConcavity.lean`'s docstring; both are now corrected.

**What was genuinely missing** was `Λ`'s OWN derivative — one chain rule away,
and the thing that makes `Lob` the primitive `Λ(x) = −∫₀ˣ log|2 sin t| dt`
rather than a rescaled `Cl₂`:

  * `hasDerivAt_Lob` — `Λ'(t) = −log(2 sin t)` on `(0,π)`
  * `hasDerivAt_deriv_Lob` / `deriv_deriv_Lob` — **`Λ''(t) = −cot t`**, which
    `IdealTetrahedronConcavity` had only in prose while writing its Hessian in
    `cot`. It is now a theorem, so that Hessian is the Hessian OF the
    Lobachevsky volume sum.

**Correction 2 — `Λ` is NOT concave on `(0,π)`.** `Λ'' = −cot` is negative only
on `(0,π/2)` and is POSITIVE on `(π/2,π)` (`deriv_deriv_Lob_neg` / `_pos`, both
proved). Concavity of the tetrahedron volume comes from the SUM via
`cot_add_cot_pos`, not from `Λ` termwise. Recorded because "Λ''=−cot, so Λ is
concave" is the plausible false next step, and the octahedral point
`(π/4,π/4,π/2)` sits exactly at the sign change.

**Bonus — the shape bridge.** `AngleTriple` is *precisely* what
`tetAngles_sum_eq_pi` produces, so `BlochWignerLobachevsky` and
`IdealTetrahedronConcavity` were describing one object from opposite ends with
no link. `AngleTriple.ofShape (z) (hz : 0 < z.im)` is the missing constructor;
concavity and the exact `det = 1` now transport to shape coordinates.

Its hypothesis is settled too:
`computations/qbeta/descartes_lambda_shape_upper_half_plane.py` shows the
Descartes cubic has NEGATIVE discriminant (−18.948) at both anchors, so
`z_q = λ(𝓔_q)` is necessarily non-real — a sign fact, no fit. (Two side
findings there, both scope-(a) and unwired: `D(z_q) = 0.91496` sits 0.11% off
Catalan — a near-match, not an identity — and `ξ = D/ℏ_q² = 93.2`, which
contradicts `conj:crossing-graded-mass-expansion`'s own "perturbative /
`ξ → 0`" framing.)

**Revised tiering — 2 of 4 closed:**
T1 **DONE** → T2 (`Vol` = the Λ-sum; GEOMETRIC, still open) → T3-core **DONE**
→ T3-plumbing (`C²` second-derivative test, still open) ⇒ `qou-krvm` (iv).

Still NOT closed, and not axiomatised anywhere per this bean's GUARD: T2 and
T3-plumbing. Bean stays open.



--------

## 2026-08-15 (PR #5142) — T2 packaged as a §3b-cond conditional class; STILL OPEN

New file QOU/Archimedean/MostowIdealTetVolume.lean (lean-direct exit 0,
#print axioms = [propext, Classical.choice, Quot.sound], NO sorryAx).
Does NOT close T2 and does NOT close qou-krvm (iv). It records the exact
remaining gap and packages it honestly.

**Sharpened gap statement.** The bean's older notes framed T2 as "Vol =
the Λ-sum (GEOMETRIC, still open)". Measured against the corpus, the
gap is narrower than that: the ANALYTIC identity is ALREADY PROVED,
sorry-free, against the genuine dx dy dz/z³ measure —
`hypVolume_chimney_inscribedTriangle` (OrthoschemeTiling):
  hypVolume (chimney (inscribedTriangle R t α β γ) R) = ofReal(Λα+Λβ+Λγ).
So "the Λ-sum IS the real hyperbolic volume of a concrete region" is
done (Milnor circumcentre subdivision, OrthoschemeLambdaSum + Tiling).
The ONE remaining piece is Milnor's geometric identification: that the
chimney over the inscribed triangle IS the ideal tetrahedron of dihedral
angles (α,β,γ). Mathlib has no ideal simplices — that cannot yet be
stated, let alone proved (qou-5gai H-tier).

**What the class does (§3b-cond, non-laundering).**
- class MostowIdealTetVolume — PRIMARY conjecture; content field
  `region_eq_chimney` axiomatises the geometric INPUT (region = chimney),
  NOT the volume conclusion.
- idealTetVolume_eq_lambda_sum [MostowIdealTetVolume] — DERIVES
  Vol = Λα+Λβ+Λγ by rw-ing the region identity and applying the PROVED
  analytic theorem. Genuine derivation, not a self-assuming projection.
- Non-vacuity is an `example : Nonempty ...` (region = a chimney,
  shape-witness) — deliberately NOT a global instance, so the theorem
  stays conditional and cannot fire on any real ideal tetrahedron.
- NO instance for the framework's genuine ideal tetrahedron — the honest
  open state. region_eq_chimney_is_restrictive gives §3b-tax non-degen.

**qou-krvm (iv) is now conditional-on-class, not proved.** Its analytic
half (concavity+invariance of the Λ-sum) was already done
(tetVol_strictConcaveOn); T2 was the geometric half, now conditional.

Bean STAYS OPEN. The GUARD holds: no instance discharges the geometric
input; the class is the labelled open conjecture, not a close.

--------

## 2026-08-15 (PR #5157) — T2 attempt: region_eq_chimney NOT dischargeable; verdict OPEN. Unconditional volume bridge added.

ATTEMPT to discharge `MostowIdealTetVolume.region_eq_chimney` and provide the
real instance (which would close T2 + qou-krvm (iv)).

**VERDICT: region_eq_chimney is NOT provable on main; NO genuine instance is
possible.** Sharpened reason: *the subject does not exist as a defined object.*
`tetRegion` is an ABSTRACT class field, so not even a single `⊆` containment is
statable, let alone `tetRegion = chimney`. There is no independent definition of
"the ideal tetrahedron of dihedral angles (α,β,γ) as a REGION of H³" anywhere:

- `IdealTetrahedronRegion.lean`: `chimney` is over an ARBITRARY base; the
  region↔tetrahedron identification is explicitly "not provable without
  hyperbolic geometry Mathlib does not have".
- `MathlibExt/IdealTriangulation.lean`: `IdealTetrahedron` is only a shape
  parameter z:ℂ; `IdealTetrahedron.volume := BlochWigner_lob z` is a NUMBER, not
  a region ("the identification with a hyperbolic volume in the metric sense is
  not available").
- 0 hyperbolic-geometry modules: no ideal vertices of ∂H³, no geodesic
  planes/half-spaces, no dihedral angle of an ideal simplex.

The §3b-cond conditional-class packaging in MostowIdealTetVolume is the correct
honest open state; the GUARD holds — no instance was fabricated.

**EXACT remaining step:** DEFINE the region `T_{αβγ} ⊆ upperHalfSpace` as the
intersection of four hyperbolic geodesic half-spaces (one hemisphere face + three
vertical faces from the inscribed triangle's chords), whose bounding planes meet
at IDEAL vertices on ∂H³ with dihedral angles (α,β,γ); then prove
`T_{αβγ} = chimney(inscribedTriangle 1 t α β γ) 1`. The geodesic-plane primitive
and the ideal-vertex/dihedral-angle notions are the missing Mathlib
infrastructure. NOTE: decomposing the chimney into its four bounding half-spaces
is trivial unfolding and is NOT progress — calling those pieces "geodesic" is
unbacked naming (that IS the missing metric content).

**qou-krvm (iv): unchanged — conditional-on-class, NOT proved.** Analytic half
(concavity+invariance of the Λ-sum) already done (`tetVol_strictConcaveOn`);
geometric half is T2, conditional via `idealTetVolume_eq_lambda_sum`.

**GENUINE PARTIAL added** (PR #5157, `IdealTetVolumeChimneyBridge.lean`;
lean-direct exit 0; `#print axioms` = [propext, Classical.choice, Quot.sound],
NO sorryAx / NO added axiom): `blochWigner_lob_eq_hypVolume_chimney` — for acute
shapes, `hypVolume(chimney(inscribedTriangle 1 t (α z)(β z)(γ z)) 1) =
ENNReal.ofReal (BlochWigner_lob z)`. The Bloch–Wigner ideal-tet volume D(z) (=
`IdealTetrahedron.volume`) IS the genuine dx dy dz/z³ measure of the concrete
normalized chimney. Composes the proved `hypVolume_chimney_inscribedTriangle`
with the def of `BlochWigner_lob`; joins the Archimedean-measure and
Knot/Bloch–Wigner subsystems and upgrades `IdealTetrahedron.volume`'s "not a
metric volume" apology for acute shapes.

**GUARD on the partial: it is a VOLUME equality, NOT a REGION equality.** Equal
volume ≠ equal set — it does NOT prove the ideal tetrahedron IS the chimney;
region_eq_chimney (T2) stays OPEN; (iv) not discharged; no instance/axiom.

Bean STAYS OPEN.



## Reasons for Scrapping

Duplicate of `qou-5gai` (work-plan reorganisation 2026-10-04). Evidence: [B 5gai] "the single blocker behind qou-idvt T2" — same gap | STALLED: in-progress, last update 2026-08-16
Content is untouched; only this work item is closed.
