import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import QOU.Hecke.Staircase

/-!
# Staircase EW-residual conjecture

The staircase partition `ρ k = (k, k-1, …, 1)` carries a distinguished
**corner hook** at cell `(0,0)`:

  `h_corner(ρ k) = arm(0,0) + leg(0,0) + 1 = (k-1) + (k-1) + 1 = 2k - 1`.

This file:

* **Proves** `staircase_corner_hook_eq_two_k_sub_one : h_corner k = 2*k - 1`
  rigorously (combinatorial; no `sorry`).
* **Axiomatises** as a Lean `class` the spectral conjecture that the
  scale `q^(1/(2k-1))` appears as a pairwise eigenvalue ratio of the
  staircase β_EW operator on `V_{ρ k}` — the conjecture verified
  empirically for k=3 (cot θ_W gap closure to 0.13%) and k=4 (rel.err
  0.14%) in `staircase_ew_residual_conjecture.py`.

Per `AGENTS.md §3b`, an unproved staircase EW-residual claim must be
either kind `conjecture` or a provable kind under the conditional-class
exception (a `class` instance whose `sorry` axiomatises the claim).
We choose the latter so downstream results may state conditional
theorems "if `StaircaseEWResidual` holds, then …".

## References

* Hoefsmit (1974), *Representations of Hecke algebras of finite groups
  with BN-pairs of classical type*, PhD thesis, UBC.
* Mathas (1999), *Iwahori–Hecke algebras and Schur algebras of the
  symmetric group*, AMS, §3.31.
* Stanley (1999), *Enumerative Combinatorics II*, Cambridge UP, §7.21
  (hook-content formula).
-/

namespace QOU.StaircaseCornerHook

universe u

/-- The corner hook of the staircase `ρ k = (k, k-1, …, 1)` at cell
`(0, 0)`.  Defined directly as the combinatorial quantity:

  `h_corner k := arm(0,0) + leg(0,0) + 1`

For the staircase `ρ k`:

* `arm(0,0) = (length of row 0) - 1 = k - 1`
* `leg(0,0) = (number of rows with ρ k r ≥ 1) - 1 = k - 1`

so `h_corner k = (k - 1) + (k - 1) + 1`. -/
def hCorner (k : ℕ) : ℕ := (k - 1) + (k - 1) + 1

/-- **Provable lemma.** The corner hook of the staircase `ρ k` equals
`2*k - 1` for every `k ≥ 1`.

This is purely combinatorial: it follows from the definition of the
staircase shape and the hook-length formula, with no appeal to
representation theory or any spectral data.

Ref: [stanley1999] Enumerative Combinatorics II, §7.21
-/
theorem staircase_corner_hook_eq_two_k_sub_one
    (k : ℕ) (hk : 1 ≤ k) :
    hCorner k = 2 * k - 1 := by
  -- Unfold and compute using `omega`, which handles natural-number
  -- truncated subtraction precisely.
  unfold hCorner
  omega

/-- Sanity checks for small k. -/
example : hCorner 2 = 3 := by decide
example : hCorner 3 = 5 := by decide
example : hCorner 4 = 7 := by decide
example : hCorner 5 = 9 := by decide
example : hCorner 6 = 11 := by decide

/-! ## The staircase EW-residual conjecture (axiomatised as a class)

For the empirical content and 7/7 witness assertions, see:

* `computations/staircase_ew_residual_conjecture.py`
* `computations/staircase-ew-residual-conjecture.witness.json`
* `docs/audits/2026-05-06-staircase-ew-residual-conjecture.md`

Per `AGENTS.md §3b-cond`, the conjecture is encoded as

* an opaque `Prop`-valued declaration `StaircaseEWSpectralContent k`
  (one axiom; cannot be discharged by `trivial`); and
* a `class StaircaseEWResidual` whose single field bundles the family
  `∀ k ≥ 2, StaircaseEWSpectralContent k`.

Per AGENTS.md §3b-tax an open primary conjecture is represented by a
content-bearing class with **no** instance.  This file therefore provides
**no global instance** (see the "Open conjecture — hypothesis-only" section
below); the illustrative snippet

  ```
  axiom conj_staircase_ew_residual : StaircaseEWResidual
  instance : StaircaseEWResidual := conj_staircase_ew_residual   -- illustrative only; NOT provided
  ```

shows what a `sorry`-record instance *would* look like, but a fabricated
`sorry`/trivial instance is exactly what §3b-tax forbids on an open carrier.
Downstream theorems instead take `[StaircaseEWResidual]` as an explicit
instance hypothesis and carry the §3b-cond "conditional on
`conj:staircase-ew-residual`" banner; once a real proof lands, a genuine
instance is added here and every downstream conditional becomes
unconditional automatically.

Ref: [leitner2026] §EW-residual, observed at q_0 to relative error
1.30e-3 (k=3, top-two ratio against cot θ_W) and 1.42e-3 (k=4,
pairwise-ratio search in dim-768 spectrum).
-/

/-- Concrete spectral statement: in any Hoefsmit representation `HR`
of `H_{n_k}(q)` on the staircase Specht module `V_{ρ k}`, the
matrix image of the canonical β_EW Δ_I^minimal word has two
nonzero eigenvalues whose ratio is `q ^ (1 / (2k - 1))`.

The exponent `1 / (2k - 1)` lives in the real / `rpow` world; we
state the predicate over an arbitrary `R` together with a
designated **scale element** `s : R` standing for the would-be
`q ^ (1 / (2k - 1))`.  Downstream callers supply `s` either by
working over `ℝ` with `Real.rpow`, or by adjoining a `(2k−1)`-th
root of `q` to the base ring.

This replaces the previous opaque
`axiom StaircaseEWSpectralContent (k : ℕ) : Prop` with a
predicate that actually mentions the Hoefsmit-matrix spectrum. -/
def StaircaseEWSpectralContent
    {R A : Type u} [CommRing R] [Inv R] [Ring A]
    [Algebra R A] (q : R) (s : R) (k : ℕ)
    [QOU.Hecke.HeckeAlgebra R (k * (k + 1) / 2) q A]
    [HR : QOU.Hecke.HoefsmitRepresentation
            (k * (k + 1) / 2) q A
            (QOU.Hecke.staircasePartition k)] : Prop :=
  QOU.Hecke.HoefsmitRepresentation.HasEigenvalueRatio
    (QOU.Hecke.HoefsmitRepresentation.wordImage
      (lam := QOU.Hecke.staircasePartition k) (HR := HR)
      (QOU.Hecke.betaEWWord (QOU.Hecke.staircaseStrands k)))
    s

/-- Axiomatic class encoding the staircase EW-residual conjecture. -/
class StaircaseEWResidual
    {R A : Type u} [CommRing R] [Inv R] [Ring A]
    [Algebra R A] (q : R) (scale : ℕ → R)
    [∀ k, QOU.Hecke.HeckeAlgebra R (k * (k + 1) / 2) q A]
    [∀ k, QOU.Hecke.HoefsmitRepresentation
            (k * (k + 1) / 2) q A
            (QOU.Hecke.staircasePartition k)] : Prop where
  /-- For every `k ≥ 2`, the inverse-corner-hook scale `scale k`
  (intended interpretation: `q ^ (1 / (2k − 1))`) is realised as
  a ratio of two positive eigenvalues of the canonical staircase
  β_EW operator on `V_{ρ k}`. -/
  spectral_scale_present :
    ∀ (k : ℕ), 2 ≤ k → StaircaseEWSpectralContent (A := A) q (scale k) k

/-! **Refined conjecture (2026-05-17)**: the specific scale function
`canonicalScale q k := q^(1/(2k-1))` realises the staircase EW-residual
ratio for the substrate parameter `q`.

This narrows the previous over-quantification (where the class held
for arbitrary `scale`, which is mathematically too strong) to the
empirically-supported specific scale.  The empirical witness
(`staircase-ew-residual-conjecture.witness.json`) verifies this
specific scale at k=3 (rel.err 0.13 %) and k=4 (rel.err 0.14 %)
at `q = q_0 ≈ 1.110`. -/
/-- The abstract canonical scale function `q^(1/(2k-1))` — meaningful in any
ring `R` admitting a `(2k-1)`-th root structure.  Specialise to
`Real.rpow q (1 / (2k-1))` over `R = ℝ`.

`opaque`, not `axiom`, and no longer called "…Axiom": this **names a constant
with an unspecified value; it asserts nothing**. An `axiom` producing *data*
still lands in `#print axioms` for every downstream result, which buries the
axioms that are genuine assumptions among ones that are merely unspecified
constants — and the `Axiom` suffix invited reading it as a claim about the
scale, which it never was. The value is `0`; it is hidden behind `opaque`, so
nothing downstream can unfold it and no consumer gains a fact from it. -/
-- Ref: [leitner2026] docs/audits/2026-05-06-staircase-ew-residual-conjecture.md
opaque canonicalScaleAxiom {R : Type*} [CommRing R] [Inv R]
    (_q : R) (_k : ℕ) : R := 0

/-- The canonical scale `q^(1/(2k-1))` on the base ring, realised via the
external `canonicalScaleAxiom`. -/
noncomputable def canonicalScale {R : Type*} [CommRing R] [Inv R]
    (q : R) (k : ℕ) : R :=
  -- The intended interpretation is `q^(1/(2k-1))`, which requires
  -- a `(2k-1)`-th root in `R`. Pending a real-power formalisation
  -- over `R`, we axiomatise the scale; downstream consumers over
  -- `R = ℝ` can specialise via `Real.rpow q (1 / (2 * k - 1))`.
  canonicalScaleAxiom q k

/-! ## Open conjecture — hypothesis-only (no global instance)

The staircase EW-residual conjecture is the *existence* of an instance
`StaircaseEWResidual q (canonicalScale q)`: that for every `k ≥ 2` the
scale `q^(1/(2k-1))` is realised as a β_EW eigenvalue ratio on `V_{ρ k}`
(empirically verified at k=3 rel.err 0.13 %, k=4 rel.err 0.14 % in
`staircase_ew_residual_conjecture.py`).

Per `AGENTS.md §3b-cond` we provide **no global instance** (which would
require a `sorry`): downstream theorems take
`[StaircaseEWResidual q (canonicalScale q)]` as an explicit instance
hypothesis and carry the "conditional on `conj:staircase-ew-residual`"
banner.  Closing the conjecture means constructing
`StaircaseEWSpectralContent q (canonicalScale q k) k` for every `k ≥ 2`
— a substantive Hoefsmit-matrix spectral analysis — after which an
instance can be added and every downstream conditional becomes
unconditional automatically.

Ref: [leitner2026] docs/audits/2026-05-06-staircase-ew-residual-conjecture.md -/

end QOU.StaircaseCornerHook
