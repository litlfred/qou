import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common
import QOU.HeckeAlgebra.QSubstrate
import QOU.HeckeAlgebra.Hoefsmit
import QOU.HeckeAlgebra.Wedderburn
import QOU.HeckeAlgebra.JonesMarkovWenzl

/-!
# QOU.HeckeAlgebra.MarkovTrace — extended Markov-trace structure

Builds on the abstract `markovTrace` axiom in
`QOU.HeckeAlgebra.Common` to expose the categorical structure
needed by the QOU mass formula `M = ρ · m_e · |tr_M(T_w)|`:

- The Markov property (cyclic invariance under conjugation)
- The Wenzl bridge: `tr_M(β) = Σ_{λ ⊢ n} y_λ(q) · χ^λ(β)` where
  `y_λ` are the Jones-Markov central coefficients and `χ^λ` is
  the trace of `β` in the irrep `V_λ` (Hoefsmit seminormal rep).

## What this module provides

- `MarkovProperty` — axiomatised cyclicity / Markov-axiom property
- `JonesMarkovCoefficient λ q` — `y_λ(q)` central coefficients
- `wenzlBridge` — the categorical identity
  `markovTrace n (wedderburnEmbed x) = Σ_λ y_λ(q_0) · trace (x λ)`

## Categorical content

The Markov trace satisfies:
- **Cyclicity**: `tr_M(x · y) = tr_M(y · x)` (inherited from
  ordinary matrix trace via the Wedderburn block decomposition)
- **Markov axiom**: `tr_M(x · σ_n) = z · tr_M(x)` for `x ∈ H_n(q)`,
  where `z = 1 / (q^{1/2} + q^{-1/2})` is the Markov parameter
  (per `prop:markov-trace-axioms` in the manuscript)
- **Wenzl bridge**: `tr_M = Σ_λ y_λ · χ^λ` is the partition-sum
  decomposition that powers the Python compute layer
  (`tr_m_q_hecke_seminormal.py`, `wedderburn_jones_markov.py`)

## Open Lean port

The full Markov-trace formalisation requires:
- A concrete `markovTrace` definition (currently axiomatic)
- The `y_λ(q)` formula (Wenzl 1988 §3) as a polynomial/Laurent
  expression in `q`
- The Hoefsmit seminormal representation matrices for `χ^λ`
  (started in `QOU.HeckeAlgebra.Hoefsmit`)

This module captures the type-level interface and the
categorical axioms; concrete formulas are deferred to the next
round.

## References

- [wenzl1988] Wenzl, *Hecke algebras of type A_n and subfactors*,
  Inventiones Math. 92 (1988), 349-383.
- [jones1985] Jones, *A polynomial invariant for knots via von
  Neumann algebras*, Bull. AMS 12 (1985).
- [kassel2008] Kassel-Turaev, *Braid Groups*, §13.6.
-/

namespace QOU.HeckeAlgebra.MarkovTrace

open QOU.HeckeAlgebra QOU.HeckeAlgebra.Hoefsmit QOU.HeckeAlgebra.Wedderburn

/-- **Jones-Markov central coefficient** `y_λ(q)` for partition
    `λ` at parameter `q`.  Axiomatised; concrete Wenzl 1988 §3
    formula is deferred to the next round of Lean port. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 §3 (Jones-Markov coefficients y_λ)
noncomputable def JonesMarkovCoefficient {n : ℕ} (lam : Nat.Partition n) (q : ℝ) : ℝ :=
    QOU.HeckeAlgebra.JonesMarkovWenzl.wenzlClosedForm lam q

/-- **Identification** (Wenzl 1988 Lemma 3.2): the abstract Jones-Markov
    coefficient IS the Wenzl closed form.

    Definitional, hence `rfl` — `JonesMarkovCoefficient` is defined as
    `wenzlClosedForm` directly above. Recorded as a named theorem anyway,
    because until 2026-08-25 this was an `axiom` in
    `QOU.HeckeAlgebra.JonesMarkovWenzl` and a reader looking for it there will
    now find only a comment. Stating it here also means a future refactor that
    makes `JonesMarkovCoefficient` something other than `wenzlClosedForm`
    breaks a theorem rather than silently changing what the corpus means by
    `y_λ`. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 Lemma 3.2
theorem jonesMarkovCoefficient_eq_wenzlClosedForm
    {n : ℕ} (lam : Nat.Partition n) (q : ℝ) :
    JonesMarkovCoefficient lam q
      = QOU.HeckeAlgebra.JonesMarkovWenzl.wenzlClosedForm lam q := rfl

/-- The Jones-Markov coefficients `y_λ(q)` are real-valued and
    sum to 1 across partitions: `Σ_{λ ⊢ n} y_λ(q) = 1` (the
    central-element normalisation, per Wenzl 1988 Lemma 3.2).

    Stated against an explicit `Finset` of partitions
    (`partitions_as_finset n`) since `Nat.Partition n` is a
    proposition, not a `Finset`.  CLOSED: Mathlib provides
    `Fintype (Nat.Partition n)` in `Combinatorics.Enumerative.Partition`,
    so we can use `Finset.univ`. -/
-- Ref: [manuscript] Ch. Mass-theory, prop:markov-trace-axioms (Finset enumeration of Nat.Partition n; closed via Mathlib Fintype)
def partitions_as_finset (n : ℕ) : Finset (Nat.Partition n) := Finset.univ

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 Lemma 3.2 (central-element normalisation Σ_λ y_λ = 1)
axiom JonesMarkovCoefficient_sum_eq_one :
    ∀ (n : ℕ) (q : ℝ),
    (∑ lam ∈ partitions_as_finset n, JonesMarkovCoefficient lam q) = 1

/-- **Hecke-algebra multiplication** axiom.  Pending the
    concrete categorical definition (Hoefsmit matrix
    representation in `QOU.HeckeAlgebra.Hoefsmit`), we
    axiomatise the multiplication operation at the type level.
    Concrete instance comes from the matrix algebra under
    `wedderburnEmbed`. -/
-- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9 §13.6 (Iwahori-Hecke algebra multiplication)
opaque heckeMul : ∀ {n : ℕ}, HeckeElement n → HeckeElement n → HeckeElement n

/-- Notation for Hecke-algebra multiplication. -/
scoped infixl:70 " *_h " => heckeMul

/-- **Cyclicity** of the Markov trace.  `tr_M(x ·_h y) = tr_M(y
    ·_h x)`.  Inherited from ordinary matrix trace via the
    Wedderburn block decomposition. -/
-- Ref: [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2 (Markov trace cyclicity tr(xy)=tr(yx))
axiom MarkovTrace_cyclic :
    ∀ {n : ℕ} (x y : HeckeElement n),
    markovTrace n (heckeMul x y) = markovTrace n (heckeMul y x)

/-- **Stabilisation map** `stab_n : HeckeElement n → HeckeElement
    (n + 1)` corresponding to multiplication by the generator
    `σ_n`.  Axiomatised pending the concrete construction
    (which requires the Hecke generator `σ_n` to be expressible
    as a `HeckeElement (n + 1)` — the natural inclusion). -/
-- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9 §13.6 (stabilisation by generator σ_n)
opaque heckeStab : ∀ {n : ℕ}, HeckeElement n → HeckeElement (n + 1)

/-- **Markov axiom** for the Markov trace: stabilisation scales
    the trace by *the* Markov parameter
    `z = 1 / (q_0^{1/2} + q_0^{-1/2})` — the single constant
    `QSubstrate.markovParameter`, not an arbitrary real:

    `tr_M(stab_n x) = z · tr_M(x)`.

    **The `z` used to be a `∀`-bound variable, which made this axiom
    collapse the Markov trace to zero.**  With `∀ (z : ℝ)` in front,
    instantiating at `z = 0` and `z = 1` gives

        markovTrace (n+1) (heckeStab x) = 0        (z := 0)
        markovTrace (n+1) (heckeStab x) = markovTrace n x   (z := 1)

    hence `markovTrace n x = 0` for *every* `n` and *every* `x`.  The
    corpus stayed consistent — the zero map satisfies
    `markovTrace_linear`, the only other constraint on `markovTrace` —
    but `tr_M`, the central object of the mass chain
    `M = ρ · m_e · |tr_M(T_w)|`, was pinned to the zero function, so
    every downstream statement about it was vacuously about `0`.
    The docstring already said "z := QSubstrate.markovParameter"; only
    the binder was wrong.  Bean `qou-ck1f`. -/
-- Ref: [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2 (Markov axiom: tr(stab x) = z·tr(x))
axiom MarkovTrace_markov_axiom :
    ∀ {n : ℕ} (x : HeckeElement n),
    markovTrace (n + 1) (heckeStab x) =
      QSubstrate.markovParameter * markovTrace n x

/-! ## The degeneracy is not excluded — checked, not asserted

`QOU.HeckeAlgebra.markovTrace`'s docstring observes that a zero weight satisfies
every axiom stated about the trace. That was an observation made by reading the
axioms; the two lemmas here make it a checked fact.

**What this does and does not establish.** It shows the stated axioms *do not
exclude* `tr_M ≡ 0`: under a zero weight each of them holds, so none of them can
be used to derive a contradiction from degeneracy. It is NOT a consistency proof
of the axiom set, which is a statement about models and is not the kind of thing
a theorem inside that same set can settle. Read it as "nothing here forces
`tr_M ≠ 0`", which is the claim being made, and not as more. -/

/-- A zero Riesz weight collapses the trace. -/
theorem markovTrace_eq_zero_of_weight_zero {n : ℕ}
    (hw : QOU.HeckeAlgebra.markovTraceWeight n = 0) (x : HeckeElement n) :
    markovTrace n x = 0 := by
  simp [QOU.HeckeAlgebra.markovTrace, QOU.HeckeAlgebra.frobeniusInner, hw]

/-- **Both trace axioms hold automatically under a zero weight.**

    So `MarkovTrace_cyclic` and `MarkovTrace_markov_axiom` impose no constraint
    that rules out the degenerate trace: cyclicity becomes `0 = 0` and the Markov
    axiom becomes `0 = z * 0`.

    This is the sharp form of the warning in `markovTrace`'s docstring, and it is
    the residue of bean `qou-ck1f`: that bean removed a `∀ (z : ℝ)` binder which
    *proved* `tr_M ≡ 0`. Removing it removed the proof of degeneracy. Nothing was
    added that excludes it, and this lemma is what makes that concrete. -/
theorem markov_axioms_vacuous_of_weight_zero
    (hw : ∀ n, QOU.HeckeAlgebra.markovTraceWeight n = 0) :
    (∀ (n : ℕ) (x y : HeckeElement n),
        markovTrace n (heckeMul x y) = markovTrace n (heckeMul y x))
      ∧ (∀ (n : ℕ) (x : HeckeElement n),
        markovTrace (n + 1) (heckeStab x)
          = QSubstrate.markovParameter * markovTrace n x) := by
  refine ⟨fun n x y => ?_, fun n x => ?_⟩
  · rw [markovTrace_eq_zero_of_weight_zero (hw n), markovTrace_eq_zero_of_weight_zero (hw n)]
  · rw [markovTrace_eq_zero_of_weight_zero (hw (n + 1)),
        markovTrace_eq_zero_of_weight_zero (hw n), mul_zero]

/-- **Categorical Markov trace on a Wedderburn decomposition**
    (axiomatised) — the categorical-level Markov trace `tr_M`
    applied directly to a `WedderburnDecomposition n`.  Bridges
    the gap between the abstract `markovTrace : HeckeElement n →
    ℝ` (vector form) and the per-block decomposition.  The
    `wenzlBridge` below relates this trace to the block-trace
    sum form. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 §3 (categorical Markov trace on Wedderburn blocks)
noncomputable def markovTraceOnWedderburn {n : ℕ} (x : WedderburnDecomposition n) : ℝ :=
    ∑ lam ∈ partitions_as_finset n,
      JonesMarkovCoefficient lam QSubstrate.q_0 * (x lam).trace

/-- **Wenzl bridge** (categorical identity): the Markov trace
    of an element via its Wedderburn decomposition equals the
    weighted sum of block traces.

    `tr_M(x) = Σ_{λ ⊢ n} y_λ(q) · tr(x λ)`

    where `tr` is the ordinary matrix trace per block.  This is
    the categorical content that the Python compute layer
    implements in `wedderburn_jones_markov.py`.

    **The `q` is `QSubstrate.q_0`, not a `∀`-bound variable.**  It used
    to be universally quantified, which is the same defect as in
    `MarkovTrace_markov_axiom` above and equally corrosive here:
    `markovTraceOnWedderburn x` does not mention `q`, so a `∀ q` on the
    right makes the weighted block-sum *provably independent of `q`*
    (`wenzlBridge_q_independent_defect` below, which no longer
    typechecks against this corrected statement).  The `q`-dependence of
    `y_λ(q)` is the entire content of the Wenzl bridge, so the old form
    asserted the negation of what it was for.  `WedderburnDecomposition`
    is defined as the decomposition of `H_n(q_0)` (see
    `Wedderburn.lean`), so `q_0` is the only `q` the statement can
    honestly mean.  Bean `qou-ck1f`. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 Lemma 3.2 (Wenzl bridge: tr_M = Σ_λ y_λ·χ^λ)
@[simp] theorem wenzlBridge {n : ℕ} (x : WedderburnDecomposition n) :
    markovTraceOnWedderburn x =
      ∑ lam ∈ partitions_as_finset n,
        JonesMarkovCoefficient lam QSubstrate.q_0 * (x lam).trace := rfl

/-- **Trace of an additive sum** distributes.

    **Theorem** (was previously `axiom markovTrace_add`).
    Discharged 2026-06-08: derived from the stronger
    `markovTrace_linear` axiom (which carries both `map_add` and
    `map_smul` via `IsLinearMap`). Net: this file shrinks by 2
    axioms (this `markovTrace_add` and the sibling
    `markovTrace_smul` below — both derive from `map_add` /
    `map_smul` of the upstream `markovTrace_linear`); the
    linearity claim is concentrated in the single
    `markovTrace_linear` axiom upstream. -/
theorem markovTrace_add {n : ℕ} (x y : HeckeElement n) :
    markovTrace n (x + y) = markovTrace n x + markovTrace n y :=
  (QOU.HeckeAlgebra.markovTrace_linear n).map_add x y

/-- **Trace of a scaled element** scales by the same factor.

    **Theorem** (was previously `axiom markovTrace_smul`).
    Discharged 2026-06-08: derived from `markovTrace_linear`'s
    `map_smul` field, with the `c • r = c * r` identity for
    `r : ℝ` (via `smul_eq_mul`). Term-mode proof for faster
    elaboration (per gemini-code-assist review on PR #1986). -/
theorem markovTrace_smul {n : ℕ} (c : ℝ) (x : HeckeElement n) :
    markovTrace n (c • x) = c * markovTrace n x :=
  ((QOU.HeckeAlgebra.markovTrace_linear n).map_smul c x).trans
    (smul_eq_mul c (markovTrace n x))

/-- **Trace of the zero element is zero** — derived from
    homogeneity via `0 • x = 0` and `markovTrace_smul`. -/
theorem markovTrace_zero : ∀ (n : ℕ),
    markovTrace n (0 : HeckeElement n) = 0 := by
  intro n
  -- 0 = 0 • x for any x, and markovTrace_smul gives markovTrace (0 • x) = 0 * markovTrace x = 0
  have := markovTrace_smul (n := n) (0 : ℝ) (0 : HeckeElement n)
  simpa using this

/-! ### Regression witnesses for the two binder fixes

Both theorems below are **vacuous** against the pre-fix axioms — under
`∀ (z : ℝ)`, `markovTrace n x = 0` for every `x`, so the hypothesis of
`markovTrace_stab_pos` is unsatisfiable and its conclusion is `0 < 0`.
They therefore fail loudly if either binder is ever re-universalised. -/

/-- The Markov parameter `z = 1 / (q_0^{1/2} + q_0^{-1/2})` is strictly
    positive: `q_0 > 1 > 0`, so both `rpow` terms are positive. -/
theorem markovParameter_pos : 0 < QSubstrate.markovParameter := by
  unfold QSubstrate.markovParameter
  have h0 : (0 : ℝ) < QSubstrate.q_0 :=
    lt_trans one_pos QSubstrate.q_0_gt_one
  positivity

/-- **Stabilisation preserves the sign of the Markov trace.**  Scaling
    by the strictly positive Markov parameter cannot flip or kill a
    positive trace.

    This is the content the `∀ (z : ℝ)` binder destroyed: with `z`
    universally quantified the trace was identically zero, so no `x`
    satisfied the hypothesis and the statement said nothing. -/
theorem markovTrace_stab_pos {n : ℕ} (x : HeckeElement n)
    (hx : 0 < markovTrace n x) :
    0 < markovTrace (n + 1) (heckeStab x) := by
  rw [MarkovTrace_markov_axiom x]
  exact mul_pos markovParameter_pos hx

end QOU.HeckeAlgebra.MarkovTrace
