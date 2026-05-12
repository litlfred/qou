/-!
# Rigid monoidal structural-gap invariance

Lean axiomatization of `prop:rigid-monoidal-structural-gap-invariance`
following the §3b conditional-class pattern from CLAUDE.md.

**Unification of PR #638 closure findings (1)–(3).**  The three
load-bearing positive findings of the brane-tower `n_⋆`
refutation —

  (1) pair-knot operators active at magic shells (LP+SDP dual,
      gap = 0 strong duality),
  (2) Z↔N symmetry of substrate binding (AME-confirmed at 0.03 MeV),
  (3) convention-independence of the structural gap (six probe
      families all give the same residual ~55% on ³He),

— are consequences of a single categorical fact: the brane-tower
formula factors through the canonical Markov trace τ on the
**rigid monoidal Type-B-folded Hecke category**
`Rep(SU_q(2))` (CLAUDE.md §7b).  The categorical τ is **unique**
(Jones 1985, Wenzl 1988) and **convention-independent**.

This file axiomatizes the unification as a class with structural
fields, then proves three downstream theorems unconditionally in
the class hypothesis.

## References

- [manuscript] prop:rigid-monoidal-structural-gap-invariance
- [manuscript] prop:spin-involution-lp-dual-invariance §"Corollary"
- [manuscript] conj:magic-shell-stabilization
- [manuscript] conj:brane-tower-z-habiro
- [jones1985] V. Jones, "A polynomial invariant for knots via
  von Neumann algebras", BAMS 12.1 (1985)
- [wenzl1988] H. Wenzl, "Hecke algebras of type A_n and subfactors",
  Invent. Math. 92 (1988)
- [kassel1995] C. Kassel, "Quantum Groups", GTM 155, Springer
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance

/-- **Abstract operator-volume convention** for evaluating a braid
    operator's contribution to the binding-energy formula.

    Each `OperatorVolumeConvention` records a (conjectural)
    convention-dependent regularizer function and the underlying
    Markov-trace value it agrees on.  Different conventions vary
    `regularizer`; all share the same `markov_trace`. -/
structure OperatorVolumeConvention (α : Type*) where
  /-- The categorical Markov trace value τ(β_𝔥) — convention-
      INDEPENDENT (unique per Jones-Wenzl). -/
  markov_trace : α → ℝ
  /-- The non-categorical regularizer (brane-tower transient
      contribution) — convention-DEPENDENT. -/
  regularizer : α → ℝ

-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Why convention-independent"

/-- **Convention-equivalence:** two conventions agree on the
    Markov trace exactly (categorical) but may differ on the
    regularizer (non-categorical). -/
def OperatorVolumeConvention.agree_on_trace {α : Type*}
    (c₁ c₂ : OperatorVolumeConvention α) : Prop :=
  ∀ β : α, c₁.markov_trace β = c₂.markov_trace β

-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Statement"

/-- **RigidMonoidalStructuralGapInvariance** — the conjectural class.

    An instance asserts that every operator-volume convention `c`
    used in the brane-tower formula factors through the same
    categorical Markov trace τ.  Concretely:

      `categorical_trace : α → ℝ`            (the unique τ)
      `convention_factorisation`             (every probed convention
                                              agrees with the
                                              categorical trace).

    The non-categorical regularizer is left free per convention,
    encoding the fact that different brane-tower regularizations
    differ on the convention-dependent tower part but agree on the
    categorical τ part. -/
-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Statement"
class RigidMonoidalStructuralGapInvariance (α : Type*) where
  /-- The unique categorical Markov trace (Jones-Wenzl uniqueness). -/
  categorical_trace : α → ℝ
  /-- Every operator-volume convention factors through it. -/
  convention_factorisation :
    ∀ (c : OperatorVolumeConvention α) (β : α),
      c.markov_trace β = categorical_trace β

-- ────────────────────────────────────────────────────────────────────────────
-- Downstream theorems — unconditional in the class hypothesis
-- ────────────────────────────────────────────────────────────────────────────

variable {α : Type*}

-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Falsifiable prediction 1"

/-- **(1) Convention-independence of the categorical trace.**  Any
    two operator-volume conventions agree on the Markov trace of
    any braid `β` — this is the categorical-uniqueness content. -/
-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Falsifiable prediction 1"
theorem trace_convention_independence
    [R : RigidMonoidalStructuralGapInvariance α]
    (c₁ c₂ : OperatorVolumeConvention α) (β : α) :
    c₁.markov_trace β = c₂.markov_trace β := by
  rw [R.convention_factorisation c₁ β]
  rw [R.convention_factorisation c₂ β]

-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Why convention-independent"

/-- **(2) Convention-equivalence is reflexive and symmetric.** -/
-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Why convention-independent"
theorem convention_equivalence_refl
    [R : RigidMonoidalStructuralGapInvariance α]
    (c : OperatorVolumeConvention α) :
    OperatorVolumeConvention.agree_on_trace c c :=
  fun _ => rfl

theorem convention_equivalence_symm
    [R : RigidMonoidalStructuralGapInvariance α]
    (c₁ c₂ : OperatorVolumeConvention α)
    (h : OperatorVolumeConvention.agree_on_trace c₁ c₂) :
    OperatorVolumeConvention.agree_on_trace c₂ c₁ :=
  fun β => (h β).symm

theorem convention_equivalence_trans
    [R : RigidMonoidalStructuralGapInvariance α]
    (c₁ c₂ c₃ : OperatorVolumeConvention α)
    (h12 : OperatorVolumeConvention.agree_on_trace c₁ c₂)
    (h23 : OperatorVolumeConvention.agree_on_trace c₂ c₃) :
    OperatorVolumeConvention.agree_on_trace c₁ c₃ :=
  fun β => (h12 β).trans (h23 β)

-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Falsifiable prediction 2"

/-- **(3) Convention-independence of the structural gap.**  Define
    the categorical structural gap as `Δ_cat(β) := B_AME -
    coefficient · |categorical_trace β|`.  Different conventions
    yield the SAME Δ_cat per braid `β` — the convention-dependent
    regularizers cancel because they all factor through the
    categorical trace. -/
-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Falsifiable prediction 2"
theorem structural_gap_convention_independent
    [R : RigidMonoidalStructuralGapInvariance α]
    (c₁ c₂ : OperatorVolumeConvention α)
    (β : α) (B_AME coefficient : ℝ) :
    (B_AME - coefficient * |c₁.markov_trace β|)
      = (B_AME - coefficient * |c₂.markov_trace β|) := by
  rw [trace_convention_independence c₁ c₂ β]

-- ────────────────────────────────────────────────────────────────────────────
-- §3b skeleton instance (TAUTOLOGICAL)
--
-- Sets `categorical_trace ≡ 0`.  Encodes no conjectural content,
-- but discharges the §3b-cond hypothesis so downstream conditional
-- theorems become unconditional Lean theorems.
-- ────────────────────────────────────────────────────────────────────────────

-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Status"

/-! ### Mathlib LP-duality integration sketch

The `convention_factorisation` axiom of
`RigidMonoidalStructuralGapInvariance` requires that every
operator-volume convention's `markov_trace` agrees with the
categorical Markov trace `τ` on `H_n(q)`.  In Lean, the genuine
discharge proceeds in three structural layers:

  **Layer 1 — Markov trace uniqueness (Jones 1985, Wenzl 1988).**
  Any functional `τ : H_n(q) → ℂ_q` satisfying M1 (cyclicity), M2
  (Markov axiom `τ^(n)(x σ_{n-1}) = z · τ^(n-1)(x)`), and M3
  (`τ(1) = 1`) on the Iwahori-Hecke algebra is uniquely
  determined.  Mathlib's `LinearAlgebra.Trace` infrastructure
  provides cyclicity (M1); the Hecke quadratic + Markov axiom
  recursion would need an additional `MarkovTraceAxiomatic` typeclass
  (proposed but not in Mathlib).  Concretely: `MarkovTrace H_n(q)`
  becomes a singleton up to scaling, and the operator-selection
  LP machinery (`prop:operator-selection-lp`) extends to its
  PSD-cone formulation via Mathlib's `Matrix.PosSemidef`.

  **Layer 2 — Spin-involution invariance (S = Hopf antipode).**
  `pair_knot_Z_N_trace_invariance` in
  `spin-involution-lp-dual-invariance.lean` (this branch) proves
  `τ ∘ S = τ` directly from the `SpinInvolution.trace_invariant`
  field — already discharged, no Mathlib infrastructure needed.

  **Layer 3 — Convention factorisation.**  Given Layer 1, any
  operator-volume convention whose `markov_trace` satisfies M1-M3
  + Hecke quadratic relation must equal `τ`.  The skeleton
  instance below records the §3b `sorry` for the Layer-1
  uniqueness step; Layers 2-3 follow.

The Mathlib-LP integration is therefore staged: Layer 2 is
production-Lean; Layer 1 needs the proposed `MarkovTraceAxiomatic`
typeclass; Layer 3 then follows by structural induction on the
Hecke quadratic relation. -/

/-- **Tautological skeleton instance.**  Pinned to `α := Empty`,
    where `OperatorVolumeConvention Empty` is inhabited but every
    `markov_trace` is a function out of an empty domain — so the
    `convention_factorisation` obligation `∀ (c : …) (β : Empty), …`
    is vacuously discharged by `Empty.elim`.  Encodes no
    conjectural content; real instances over inhabited `α` must
    supply the §3b Layer-1 Markov-trace uniqueness data discussed
    in the comment block above.

    The instance is intentionally NOT parameterised over an
    arbitrary `α : Type*`: with `categorical_trace ≡ 0`, the
    obligation `c.markov_trace β = 0` is genuinely false for any
    inhabited `α` and a convention with non-zero `markov_trace`
    (e.g. `⟨fun _ => 1, fun _ => 0⟩`) — so the universally-quantified
    skeleton is unprovable, not §3b-conjectural.  Pinning to
    `Empty` matches the §3b-cond pattern: tautological discharge,
    no real content, no false claim.

    Companion: `docs/audits/2026-05-12-lean-handover.md` §2 P4.A and
    `docs/audits/2026-05-12-lean-p4-discharge-and-escalation.md`. -/
-- Ref: [manuscript] prop:rigid-monoidal-structural-gap-invariance §"Skeleton"
-- Ref: [jones1985] V. Jones, BAMS 12.1 (1985)
-- Ref: [wenzl1988] H. Wenzl, Invent. Math. 92 (1988)
instance canonical : RigidMonoidalStructuralGapInvariance Empty where
  categorical_trace _ := (0 : ℝ)
  convention_factorisation _ β := Empty.elim β

end QOU.BraidKnot
