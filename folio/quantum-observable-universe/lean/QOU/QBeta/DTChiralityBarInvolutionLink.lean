import QOU.QBeta.ChiralityGradedCount
import Mathlib.Algebra.GroupWithZero.Basic

set_option autoImplicit false

/-!
# QOU.QBeta.DTChiralityBarInvolutionLink — the chirality split IS `q ↦ q⁻¹` (D4, conditional)

The `qou-rtec` attack ledger's D4 lever, formalized conditionally: the `{S⁺, S⁻}`
DT chirality split and the corpus bar involution `q ↦ q⁻¹` are **the same ℤ/2
action**, transported along knot mirroring. The corpus already carries the two
halves separately:

* the **pair side** — `ChiralityGradedCount`: the mirror swap on an ordered
  split `(a, b)`, its faithful bar-grading `(a+b, a−b)`, and the proved
  no-symmetric-scalar obstruction;
* the **q side** — the Jones mirror rule `J_{m(K)}(q) = J_K(q⁻¹)` (the
  convention noted in `HabiroCyclotomicOddLocus`, `t = q⁻¹` = mirror) and the
  amphichiral σ-fixedness used by `FigureEightSelfDuality`.

This file ties them: a class `DTBarInvolutionLink` whose fields are the two
**transformation hypotheses** (the DT pair transforms under mirroring by the
swap; the carrying invariant transforms by bar), and theorems **deriving** the
consequences — the bar-even part of the DT datum is mirror-invariant, the
bar-odd part is a chirality obstruction, amphichirality kills it and forces the
invariant σ-fixed, and the two involutions compose coherently.

## Honesty (§3b-cond; anti-laundering)

The class axiomatises **hypotheses, not conclusions** (§3b-tax non-degeneracy):
neither transformation law is proved here — `dt_mirror_swap` is the GGM-style
chirality-split reading and `jones_mirror_bar` is the Jones mirror rule, both
literature facts about objects the corpus does not construct internally. Every
theorem is conditional on the instance; no instance for a real knot is
declared (a structural consistency instance on `Split` itself shows the class
is satisfiable — it carries no knot data). Nothing here derives `A_ω`, the DT
integers, or the split; the `5₂`/`4₁` numbers enter only through
`ChiralityGradedCount`'s literature `def`s, quoted in conditional corollaries.

## References

- [garoufalidis-gu-marino2023] https://doi.org/10.1007/s00220-023-04753-2 (the S± Stokes constants)
- [leitner2026] docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md §3 (Route C / D4);
  QOU/QBeta/ChiralityGradedCount.lean (the pair-side machinery this consumes).
-/

namespace QOU.QBeta.DTChiralityBarInvolutionLink

open QOU.QBeta.ChiralityGradedCount

universe u v

/-- **The D4 link, as an explicit conditional hypothesis class.** `K` is a type
of knot data with a mirror involution, `dt` the chirality-split DT reading, and
`jones` the carrying `q`-invariant. The two transformation fields assert that
mirroring acts on the DT pair by the swap and on the invariant by the bar
involution `q ↦ q⁻¹` — making the chirality split and bar parity the same ℤ/2
action. Both are hypotheses (literature transformation laws), not corpus
theorems; see the module docstring. -/
class DTBarInvolutionLink (K : Type u) (R : Type v) [GroupWithZero R] where
  /-- Knot mirroring. -/
  mirrorK : K → K
  /-- Mirroring is an involution. -/
  mirrorK_involutive : ∀ k, mirrorK (mirrorK k) = k
  /-- The chirality-split DT reading `(S⁺, S⁻)`. -/
  dt : K → Split
  /-- The carrying `q`-invariant (Jones-type). -/
  jones : K → R → R
  /-- **Hypothesis 1**: mirroring swaps the split. -/
  dt_mirror_swap : ∀ k, dt (mirrorK k) = ChiralityGradedCount.mirror (dt k)
  /-- **Hypothesis 2** (the Jones mirror rule): mirroring is the bar
  involution on the invariant. -/
  jones_mirror_bar : ∀ k (q : R), q ≠ 0 → jones (mirrorK k) q = jones k q⁻¹

variable {K : Type u} {R : Type v} [GroupWithZero R] [DTBarInvolutionLink K R]

open DTBarInvolutionLink

/-- The bar-even part of the DT datum is mirror-invariant — it is the
chirality-blind shadow (`7` for `5₂`). -/
theorem barEven_dt_mirror (k : K) :
    barEven (dt (R := R) (mirrorK (R := R) k)) = barEven (dt (R := R) k) := by
  rw [dt_mirror_swap, barEven_mirror]

/-- The bar-odd part of the DT datum is mirror-negated — it is the `−1`
eigenvector, the chirality witness. -/
theorem barOdd_dt_mirror (k : K) :
    barOdd (dt (R := R) (mirrorK (R := R) k)) = - barOdd (dt (R := R) k) := by
  rw [dt_mirror_swap, barOdd_mirror]

/-- **Amphichirality kills the bar-odd DT part.** A knot fixed by mirroring has
`S⁺ = S⁻` — the `4₁` degeneracy, derived rather than observed. -/
theorem barOdd_dt_eq_zero_of_amphichiral (k : K) (h : mirrorK (R := R) k = k) :
    barOdd (dt (R := R) k) = 0 := by
  have hm := barOdd_dt_mirror (R := R) k
  rw [h] at hm
  omega

/-- **The bar-odd DT part is a chirality obstruction**: a chiral split forces
the knot itself chiral (`5₂` from its `(4,3)` datum, conditionally). -/
theorem chiral_dt_forces_chiral (k : K) (hchi : IsChiral (dt (R := R) k)) :
    mirrorK (R := R) k ≠ k := by
  intro h
  exact (chiral_iff_odd_ne_zero _).mp hchi
    (barOdd_dt_eq_zero_of_amphichiral k h)

/-- **Amphichirality forces the invariant bar-even** (σ-fixed): the generic form
of `FigureEightSelfDuality`'s 4₁ statement, derived from the link. -/
theorem jones_bar_fixed_of_amphichiral (k : K) (h : mirrorK (R := R) k = k)
    (q : R) (hq : q ≠ 0) : jones k q⁻¹ = jones k q := by
  have hb := jones_mirror_bar (R := R) k q hq
  rw [h] at hb
  exact hb.symm

/-- **Coherence (direction reversal)**: the bar law also runs backwards —
`J_K(q) = J_{m(K)}(q⁻¹)`. Derived from the transformation law at the mirror
knot plus involutivity (not a bare `symm` of the field): the mirror involution
and `q ↦ q⁻¹` implement the *same* ℤ/2 action from either side. -/
theorem jones_mirror_bar_inv (k : K) (q : R) (hq : q ≠ 0) :
    jones (R := R) k q = jones (R := R) (mirrorK (R := R) k) q⁻¹ := by
  have h := jones_mirror_bar (R := R) (mirrorK (R := R) k) q hq
  rw [mirrorK_involutive] at h
  exact h

/-! ## Conditional corollaries at the literature data

The `5₂` and `4₁` numbers enter only via `ChiralityGradedCount`'s `def`s. -/

/-- **Conditional `5₂` chirality**: any knot datum whose DT reading is the
literature `(4, 3)` split is chiral under the link. -/
theorem five_two_datum_forces_chiral (k : K)
    (hdt : dt (R := R) k = dtSplit52) : mirrorK (R := R) k ≠ k := by
  apply chiral_dt_forces_chiral
  rw [hdt]
  exact dtSplit52_chiral_grading.1

/-- **Conditional `4₁` consistency**: an amphichiral knot datum must carry an
equal split — the literature `(3, 3)` satisfies this, so the link is consistent
with the `4₁` record. -/
theorem amphichiral_datum_consistent (k : K) (h : mirrorK (R := R) k = k) :
    (dt (R := R) k).1 = (dt (R := R) k).2 := by
  have h0 := barOdd_dt_eq_zero_of_amphichiral (R := R) k h
  unfold barOdd at h0
  omega

/-! ## Satisfiability (structural, knot-free)

A consistency instance on `Split` itself: mirroring = the pair swap, `dt` = the
identity, invariant = constant. Shows the class has a model — the theorems above
are not vacuous — while carrying no knot data (nothing is laundered). -/

instance : DTBarInvolutionLink Split R where
  mirrorK := ChiralityGradedCount.mirror
  mirrorK_involutive := mirror_involutive
  dt := id
  jones := fun _ _ => 1
  dt_mirror_swap := fun _ => rfl
  jones_mirror_bar := fun _ _ _ => rfl

end QOU.QBeta.DTChiralityBarInvolutionLink
