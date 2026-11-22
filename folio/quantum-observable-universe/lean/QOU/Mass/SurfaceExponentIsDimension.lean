import QOU.Mass.CoordinationSurfaceDeficit
import Mathlib.Tactic

/-!
# QOU.Mass.SurfaceExponentIsDimension — the surface exponent is not free, and the production chain's value is excluded

`QOU.Mass.CoordinationSurfaceDeficit` shows the per-nucleon binding of a bounded-degree bond
count splits as

    B/A = ε·k/2 − (ε(k−k')/2)·(A_surf/A)                        (`perNucleon_split`)

and left one question: what fixes the surface term. This file answers a sharper version of it.
**The `A`-dependence of the correction is carried entirely by the surface fraction `A_surf/A`,
and that fraction is where the DIMENSION of the coordination graph enters.** For a compact
`d`-dimensional cluster the boundary is `(d−1)`-dimensional, so

    A_surf ∼ c·A^((d−1)/d)   ⇒   A_surf/A ∼ c·A^(−1/d).

So *under that hypothesis* the exponent of the surface correction is **`1/d`**. Whatever it is
read as, the exponent is a one-number shape test rather than a ratio, and unlike the
surface-to-volume ratio (measured generic at 67.9 % of its plausible window, `qou-kqdn`) it is
**not free to be chosen**: `perNucleonExp_exponent_inj` proves distinct exponents give distinct
functions of `A`, so no choice of amplitude can disguise a wrong one. That much is proved here.
**The reading `p = 1/d` is NOT established** — see §"the sharpest objection" and the data section
below, which reject the chain's `p = 1` but do not select `d = 3`.

## The production word is one-dimensional, and this is exact

`atom_braid_word_3A` walks a chain: nucleon `j` writes generators `3j, 3j+1` and then a **single**
inter-nucleon letter at `3j+2`, for `j = 0 … A−2`. So the coordination graph is the path `P_A`:

* the two endpoint nucleons carry **one** bond each,
* every interior nucleon carries **two**,
* total bonds `A − 1`.

That is the boundary deficit of `CoordinationSurfaceDeficit` at `k = 2`, `k' = 1`, and
`A_surf = 2` — a **constant**, not a growing surface (`chain_bondCount`; the surface count is the
literal `2` appearing there, independent of `A`). Hence

    B/A = ε − ε/A                                               (`chain_perNucleon`)

i.e. exponent `p = 1`, the `d = 1` case. **The chain does have a boundary; its boundary is
zero-dimensional.**

## What is new here, and what the corpus already had

**The `A^(−1)` SCALING IS NOT NEW and must not be reported as a discovery.**
`QOU.MassTheory.ChainBindingNoSaturationPeak.chainPerNucleon_eq_hyperbola` already proves, by
`ring`, that an isobaric chain's per-nucleon binding is exactly `c₁ + c₂/A` — the same object as
`chain_perNucleon` at `k = 2, k' = 1`. What is new is the **derivation from the boundary DEGREE**:
the corpus states the same deficit only in bond-count language ("an open `A`-chain has one fewer
bond than nucleons", `2026-06-15-delta-lambda-offset-open-chain-boundary.md`), never as two
endpoints of degree 1 against an interior degree 2 — which is what makes it an instance of
`CoordinationSurfaceDeficit` rather than an isolated arithmetic fact.

`QOU.Mass.AffineCountIsNotASurfaceTerm` reaches "affine is not a surface term" by an independent
scope-(b) route (strict monotonicity of `(12A−1)/A^(2/3)`); since `A − 1` is affine, that theorem
covers this graph too. `chain_ne_semf` below is the complementary statement in the exponent
variable: it excludes **every** `p ≠ 1`, not one target exponent.

**The sharpest objection to reading `p = 1/d` as a dimension, met rather than avoided:** the
corpus's only *derived* three-dimensional coordination object is the deltahedron contact graph,
and by Euler it has `E = 3A − 6` — still affine, so it also gives `A^(−1)`. A convex deltahedron
puts every nucleon on the boundary, so it is `d = 3` geometrically while having no bulk at all.
`A_surf ∼ c·A^((d−1)/d)` needs a bulk; a surface-only graph is exactly the case where the reading
fails. So `p = 1/d` is a statement about **compact** clusters, and nothing here asserts the
substrate emits one.

Distinguish also the recorded negative in bean `qou-7e67`, *"Is the exponent a DIMENSION
question? NO: no single exponent fits"*. That tests `R ∼ A^x` for the **radius** over `A ≤ 4`,
varying `d` over ambient manifolds. This varies `d` over the nucleon coordination graph and
predicts the **deficit's** exponent. Different object, different observable; the negative does
not transfer, and is cited so a reader does not think it was missed.

## What the data say (companion probe, 19/19)

Profiling `p` against 2548 AME nuclides with Coulomb, asymmetry and pairing carried separately:

* **the chain's `p = 1` is rejected** — `RSS(1) = 147.0` against `RSS(p*) = 38.2`, and `p = 1`
  lies outside the interval where RSS stays within 1 % of its minimum, under every analysis
  variant tried;
* **but the data do not cleanly select `d = 3` either.** The full-sample optimum is `p* = 0.364`
  (`d = 2.75`); restricted to `A ≥ 40` it is `p* = 0.582` (`d = 1.72`), and the two 1 %-RSS
  intervals are **disjoint**. No single power-law exponent describes the whole chart.

So this file's `chain_ne_semf` is confirmed against data, and the positive reading `p = 1/d` is
**not** thereby established. A pre-registered expectation that the analysis variants would agree
failed; that is recorded in the probe rather than dropped.

## Scope

* **Proved:** the chain identities (exact, `k = 2, k' = 1, A_surf = 2`), the general
  `d`-dimensional surface fraction as a definition, injectivity of the exponent, and that the
  chain's law differs from any `p ≠ 1` law at some `A`.
* **Assumed:** that a compact `d`-dimensional cluster has `A_surf ∼ c·A^((d−1)/d)`. Standard
  geometry, stated as a hypothesis exactly as in `CoordinationSurfaceDeficit`; not proved. It
  fails for surface-only graphs, see the `E = 3A − 6` objection above.
* **NOT claimed:** that the substrate emits a `d = 3` graph, nor that the measured exponent *is*
  a dimension. What is shown is that the exponent is not free (`perNucleonExp_exponent_inj`),
  that the production word's graph is `d = 1`, and that the data exclude it.
* **Not a fit.** No coefficient is chosen against data here.
* **Note on shape:** `a − b·A^(−p)` with `b, p > 0` is monotone in `A`, so it cannot produce the
  iron peak alone — the same scope-(b) point the Faddeev–Niemi verdict records for pure power
  laws. The exponent measured is the **deficit's**, with Coulomb carried separately, exactly as
  `QOU.Mass.SaturationPeakStructure` sets the problem up.

Ground ring `ℝ` (§7c: archimedean — real powers).

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/CoordinationSurfaceDeficit.lean
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MassTheory/ChainBindingNoSaturationPeak.lean
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/AffineCountIsNotASurfaceTerm.lean
-- Ref: [leitner2026] computations/mass_at_3A_proper.py (atom_braid_word_3A: one bond letter per pair)
-/

namespace QOU.Mass.SurfaceExponentIsDimension

open QOU.Mass.CoordinationSurfaceDeficit

/-! ## The production chain, exactly -/

/-- **The path graph's bond count is `A − 1`.** With interior degree `k = 2`, endpoint degree
`k' = 1` and exactly two endpoints, the handshake count of `CoordinationSurfaceDeficit` gives
`A − 1` — which is the production word's one inter-nucleon letter per adjacent pair. -/
theorem chain_bondCount (A : ℝ) : bondCount 2 1 (A - 2) 2 = A - 1 := by
  unfold bondCount; ring

/-- **The chain's per-nucleon binding is `ε − ε/A`:** exponent `p = 1`. -/
theorem chain_perNucleon (ε A : ℝ) (hA : A ≠ 0) :
    ε * bondCount 2 1 (A - 2) 2 / A = ε - ε / A := by
  rw [chain_bondCount]
  field_simp

/-- The chain's law is the `d = 1` member of the family `B/A = a − b·A^(−1/d)`: taking
`a = ε`, `b = ε` and `1/d = 1` reproduces it exactly. -/
theorem chain_is_dimension_one (ε A : ℝ) (hA : 0 < A) :
    ε * bondCount 2 1 (A - 2) 2 / A = ε - ε * A ^ (-(1 : ℝ)) := by
  rw [chain_perNucleon ε A (ne_of_gt hA), Real.rpow_neg_one]
  ring

/-! ## The exponent determines the dimension -/

/-- The per-nucleon law with surface exponent `p`: `B/A = a − b·A^(−p)`. For a compact
`d`-dimensional cluster `p = 1/d`. -/
noncomputable def perNucleonExp (a b p A : ℝ) : ℝ := a - b * A ^ (-p)

/-- The chain is `perNucleonExp ε ε 1`. -/
theorem chain_eq_perNucleonExp (ε A : ℝ) (hA : 0 < A) :
    ε * bondCount 2 1 (A - 2) 2 / A = perNucleonExp ε ε 1 A := by
  unfold perNucleonExp
  simpa using chain_is_dimension_one ε A hA

/-- **Distinct exponents are distinct laws.** If two laws with the same nonzero amplitude agree
at every `A > 0`, their exponents are equal. So the exponent is not free: measuring it measures
`1/d`, and no choice of the other constants can disguise a wrong dimension. -/
theorem perNucleonExp_exponent_inj (a b p p' : ℝ) (hb : b ≠ 0)
    (h : ∀ A : ℝ, 0 < A → perNucleonExp a b p A = perNucleonExp a b p' A) : p = p' := by
  have h2 := h 2 (by norm_num)
  unfold perNucleonExp at h2
  have hrp : (2 : ℝ) ^ (-p) = (2 : ℝ) ^ (-p') := by
    have : b * (2 : ℝ) ^ (-p) = b * (2 : ℝ) ^ (-p') := by linarith
    exact mul_left_cancel₀ hb this
  have h2pos : (1 : ℝ) < (2 : ℝ) := by norm_num
  have hle : -p ≤ -p' := (Real.rpow_le_rpow_left_iff h2pos).mp (le_of_eq hrp)
  have hge : -p' ≤ -p := (Real.rpow_le_rpow_left_iff h2pos).mp (le_of_eq hrp.symm)
  linarith

/-- **The chain cannot be the SEMF surface law.** The `d = 1` chain law `ε − ε/A` and any
`d ≠ 1` law with the same amplitude differ at some `A > 0`. In particular the SEMF's `p = 1/3`
(a three-dimensional cluster) is not reachable by the production word's path graph, whatever
`ε` is. -/
theorem chain_ne_semf (ε : ℝ) (hε : ε ≠ 0) (p : ℝ) (hp : p ≠ 1) :
    ∃ A : ℝ, 0 < A ∧ perNucleonExp ε ε 1 A ≠ perNucleonExp ε ε p A := by
  by_contra hcon
  push_neg at hcon
  exact hp (perNucleonExp_exponent_inj ε ε 1 p hε (fun A hA => hcon A hA)).symm

/-- The `d`-dimensional surface fraction, as a hypothesis-level definition: a compact
`d`-dimensional cluster has boundary of dimension `d − 1`, so `A_surf/A = c·A^(−1/d)`. -/
noncomputable def surfaceFraction (c d A : ℝ) : ℝ := c * A ^ (-(1 / d))

/-- Feeding the `d`-dimensional surface fraction into `perNucleon_split` gives exactly
`perNucleonExp` with `p = 1/d`: **the surface exponent is the inverse dimension.** -/
theorem perNucleon_surfaceExponent (ε k k' c d A : ℝ) :
    ε * k / 2 - (ε * (k - k') / 2) * surfaceFraction c d A
      = perNucleonExp (ε * k / 2) (ε * (k - k') * c / 2) (1 / d) A := by
  unfold surfaceFraction perNucleonExp
  ring

end QOU.Mass.SurfaceExponentIsDimension
