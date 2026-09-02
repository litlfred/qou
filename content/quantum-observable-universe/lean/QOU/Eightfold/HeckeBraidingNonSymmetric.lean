import Mathlib.Tactic

/-!
# QOU.Eightfold.HeckeBraidingNonSymmetric — the Hecke braiding is symmetric iff `q² = 1`

Bean `qou-tzfm`. Companion to
`docs/audits/2026-08-25-4a-question-imports-symmetric-theory.md`.

## What this is for

The eightfold surface's surviving question is recorded as *"is `H¹(base, Aut^⊗)`
non-trivial, and can the resulting gerbe's band be `SU(3)`?"*. That formulation
is **symmetric**-category machinery: Tonini (`arxiv-1409.4073v1`,
`arxiv-2010.12445v1`) defines the relevant structure as *"symmetric or
commutative"*, and attributes the band identification to [DM82, Prop. 2.8 /
Thm. 3.2] — theorems about `Rep G`, which is symmetric.

QOU's category is **not** symmetric. The corpus asserts this in prose
(`qou-definition-intro.md`: *"the non-symmetric braiding provides a canonical
well-ordering on the Hecke basis"*). This file supplies the **reason**, as a
theorem rather than an assertion: non-symmetry is forced by the Hecke relation
together with `q² ≠ 1`, and the substrate sits at `q₀ ≈ 1.10998 > 1`.

## What is proved, and what is not

Proved here, over a generic field `R` and a generic `R`-algebra `A` (§7c: this
file is entirely wall-side, with no `ℝ` anywhere):

* `hecke_rel_iff_factored` — the two spellings of the Hecke relation agree.
  This is the AGENTS.md §7a convention `(σ - q)(σ + q⁻¹) = 0` matched to the
  quadratic `σ² = (q - q⁻¹)σ + 1`, and it needs `q ≠ 0`.
* `double_braiding_eq_one_iff` — **the main statement**: an element satisfying
  the Hecke relation squares to `1` if and only if `q² = 1`. Both directions.
The archimedean specialisation to the substrate value lives in a **separate**
file, `QOU.Archimedean.HeckeBraidingSubstrateNonSymmetric`, per §7c: nothing
below mentions `ℝ`, an ordering, or any archimedean construct.

**Not** proved here, and deliberately: that the QOU braiding *is* such a `σ`.
That is the corpus's Hecke–Skein convention (AGENTS.md §7a), an identification
this file consumes as a hypothesis and does not establish. Nor does anything
here say what QOU's category is instead of symmetric, nor exclude `SU(3)` from
the framework — see the audit's §4 for both non-claims.

The scalar hypothesis `hfree` says no nonzero scalar annihilates `σ`. It holds
in the Hecke algebra over a field, where `σ` is a nonzero element of a free
module; it is stated rather than assumed globally because it is what the
argument actually uses, and it fails exactly in the degenerate case `σ = 0`
that the statement must exclude (`hfree` applied at `r = 1` gives `σ ≠ 0`).

-- Ref: [kassel1995] Ch. XII (Hecke algebras, braiding eigenvalues `q`, `-q⁻¹`);
-- AGENTS.md §7a records the same convention for this corpus.
-/

namespace QOU.Eightfold.HeckeBraidingNonSymmetric

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A]

/-- The Hecke relation in its two standard spellings. The factored form
`(σ - q)(σ + q⁻¹) = 0` exhibits the eigenvalues; the quadratic form
`σ² = (q - q⁻¹)σ + 1` is what the braid relation is usually reduced against.
They agree precisely because `q · q⁻¹ = 1`, which is where `hq` is spent. -/
theorem hecke_rel_iff_factored (q : R) (σ : A) (hq : q ≠ 0) :
    σ ^ 2 = algebraMap R A (q - q⁻¹) * σ + 1 ↔
      (σ - algebraMap R A q) * (σ + algebraMap R A q⁻¹) = 0 := by
  have hmap : algebraMap R A q * algebraMap R A q⁻¹ = 1 := by
    rw [← map_mul, mul_inv_cancel₀ hq, map_one]
  have h1 : algebraMap R A q * σ = σ * algebraMap R A q := Algebra.commutes q σ
  have h2 : algebraMap R A q⁻¹ * σ = σ * algebraMap R A q⁻¹ := Algebra.commutes q⁻¹ σ
  have key : (σ - algebraMap R A q) * (σ + algebraMap R A q⁻¹)
      = σ ^ 2 - (algebraMap R A q - algebraMap R A q⁻¹) * σ - 1 := by
    simp only [sub_mul, mul_add, h1, h2, hmap]
    noncomm_ring
  rw [map_sub, key, sub_sub, sub_eq_zero]

/-- **The gate.** An element satisfying the Hecke relation has trivial double
braiding exactly when `q² = 1`.

The forward direction is the one that matters for the eightfold surface: if the
braiding were symmetric, the substrate parameter would be forced onto `q² = 1`.
The reverse direction is what makes this an honest `iff` rather than a bound —
at `q² = 1` the Hecke relation really does degenerate to `σ² = 1`, so the
statement is not vacuously one-sided. -/
theorem double_braiding_eq_one_iff (q : R) (σ : A) (hq : q ≠ 0)
    (hfree : ∀ r : R, algebraMap R A r * σ = 0 → r = 0)
    (hHecke : σ ^ 2 = algebraMap R A (q - q⁻¹) * σ + 1) :
    σ ^ 2 = 1 ↔ q ^ 2 = 1 := by
  have hsub : q - q⁻¹ = 0 ↔ q ^ 2 = 1 := by
    constructor
    · intro h
      field_simp at h
      linear_combination h
    · intro h
      field_simp
      linear_combination h
  constructor
  · intro hs
    rw [hs] at hHecke
    exact hsub.mp (hfree _ (right_eq_add.mp hHecke))
  · intro h2
    rw [hHecke, hsub.mpr h2, map_zero, zero_mul, zero_add]

end QOU.Eightfold.HeckeBraidingNonSymmetric
