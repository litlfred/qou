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
- `wenzlBridge` — `markovTraceOnWedderburn x = Σ_λ y_λ(q_0) · trace (x λ)`.

  This list used to advertise that identity as
  `markovTrace n (wedderburnEmbed x) = Σ_λ y_λ(q_0) · trace (x λ)`,
  which overstates it in two ways and is corrected here (2026-09-05,
  bean `qou-kp2z`).  The theorem's left-hand side is
  `markovTraceOnWedderburn`, whose *definition* is that very sum, so
  `wenzlBridge` is proved by `rfl` — it unfolds a definition rather
  than connecting two independently-given quantities.  And it never
  mentioned `wedderburnEmbed`: nothing in this module did, outside
  this sentence.  Relating a trace on the assembled matrix algebra to
  the block sum is genuine content, and it is now proved — in
  `QOU/HeckeAlgebra/WedderburnTrace.lean`, over the constructed
  `blockDiagonal`.  What is still **not** proved is that identity with
  `markovTrace` itself on the left: `markovTrace` is `opaque` in
  `QOU/HeckeAlgebra/Common.lean`, so connecting it to either sum
  remains open.

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
-- Ref: [leitner2026] Ch. Mass-theory, prop:markov-trace-axioms (Finset enumeration of Nat.Partition n; closed via Mathlib Fintype)
def partitions_as_finset (n : ℕ) : Finset (Nat.Partition n) := Finset.univ

/-! ### `Σ_λ y_λ(q) = 1` — REMOVED (it was false)

This carried

```lean
axiom JonesMarkovCoefficient_sum_eq_one :
    ∀ (n : ℕ) (q : ℝ),
    (∑ lam ∈ partitions_as_finset n, JonesMarkovCoefficient lam q) = 1
```

cited to Wenzl 1988 Lemma 3.2. **The proposition is false and the axiom is
deleted.** Refutation:
`QOU.HeckeAlgebra.JonesMarkovSumCounterexample.not_jonesMarkovCoefficient_sum_eq_one`
— sorry-free, depending on no QOU axiom, and registered in
`scripts/lean-axiom-guard.py`.

Take `q = 1`. `qInteger` uses **real** exponents, so every `rpow` is `1` there
and the quotient is `(1-1)/(1-1) = 0/0`, which Lean evaluates to `0` for every
`k`. Its inverse is `0`, each cell contributes a zero factor, the first row's
fold collapses, and every partition of every `n ≥ 1` has coefficient `0`. The
sum is `0`, not `1`.

Two further mismatches, independent of that collapse and worth recording:
`wenzlClosedForm`'s prefactor `QSubstrate.markovParameter ^ (n-1)` is a bare
constant pinned at the substrate `q_0` and does not depend on the quantified
`q`; and AGENTS.md records the measured fact that the q-deformed weights do not
sum to 1 away from `q = 1` either (0.987 … 1.517 across `n = 3…12`). Wenzl's
lemma is about a normalised trace, where the weights enter against their
dimensions — `Σ_λ y_λ · d_λ`, not the bare `Σ_λ y_λ`.

**The corrected statement is deliberately not supplied here.** It had zero Lean
consumers, so nothing needs it to proceed; naming the right normalisation is a
separate question and guessing it would repeat the error. Bean `qou-i6u4`.
-/

/-- **Hecke-algebra multiplication**, carried opaquely.

    An `opaque` definition is a datum: it adds nothing to the assumption surface
    (no `axiom`), it merely declines to say what the operation is. The concrete
    multiplication is the matrix algebra under the Wedderburn embedding
    (`QOU.HeckeAlgebra.Wedderburn.blockDiagonal`, and `wedderburnEmbedOf` for
    the `Fin (heckeDim n)` landing), via the Hoefsmit representation in
    `QOU.HeckeAlgebra.Hoefsmit`.  This pointed at `wedderburnEmbed` until that
    `opaque` was deleted on 2026-09-05; the target is now a real construction.

    Kept — unlike the cyclicity axiom that used to accompany it, see below —
    because `markov_axioms_vacuous_of_weight_zero` needs a multiplication to state
    what the removed axiom would have constrained. -/
-- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9 §13.6 (Iwahori-Hecke algebra multiplication)
opaque heckeMul : ∀ {n : ℕ}, HeckeElement n → HeckeElement n → HeckeElement n

/-- Notation for Hecke-algebra multiplication. -/
scoped infixl:70 " *_h " => heckeMul

/-! ## Cyclicity — removed from this layer, because it lives in two others

This module used to declare, alongside `heckeMul` above,

    axiom MarkovTrace_cyclic :
      ∀ {n} (x y : HeckeElement n),
        markovTrace n (heckeMul x y) = markovTrace n (heckeMul y x)

That axiom is gone as of 2026-08-26 (bean `qou-k5jt`). Measured corpus-wide first:
**it had zero consumers.** `heckeMul` is kept, since it is an `opaque` datum rather
than an axiom and the degeneracy lemma below needs it.

So it was assumed mathematics that bought nothing, and by
`markov_axioms_vacuous_of_weight_zero` below it did not even constrain the trace:
under a zero Riesz weight it reads `0 = 0`.

**Cyclicity itself is not lost — it is proved twice already, and neither proof
was reachable from here:**

* `QOU.MathlibExt.MarkovTrace.character_append_comm` — for the concrete Markov
  trace on a Hecke representation, `tr_ρ(v ++ w) = tr_ρ(w ++ v)`, by
  `ρ.eval_append` and `Matrix.trace_mul_comm`. Sorry-free.
* `QOU.Machinery.MarkovInductiveCyclicity` — the inductive Ocneanu route over a
  generic algebra: `cyclic_one_g`, `cyclic_two_g` and the `gwg_*` bricks, all
  sorry-free and axiom-free, stated conditionally on named hypotheses (`hIH`,
  `hgwg`, `hCE`) in the §3b-cond style.

Restoring an abstract cyclicity statement here should therefore **not**
reintroduce an opaque multiplication. `MarkovInductiveCyclicity` already works
over a generic algebra `A` with a membership predicate, which is the shape that
composes; an opaque binary operation is the shape that cannot.

⚠ Note what is NOT claimed. `MarkovInductiveCyclicity` is currently an **orphan**
— nothing imports it and nothing consumes `cyclic_two_g` — and its hypotheses are
not discharged anywhere. Conditional-proved is not premise-established (AGENTS.md
§"Conditional-proved ≠ premise-established"). The bricks exist; the assembly into
an unconditional statement about a specific algebra does not.
-/

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

/-- **Both trace properties hold automatically under a zero weight.**

    So neither imposes a constraint that rules out the degenerate trace:
    cyclicity becomes `0 = 0` and the Markov property becomes `0 = z * 0`.

    "Properties", not "axioms", as of 2026-08-26: cyclicity is **no longer an
    axiom here** — it was removed as a zero-consumer assumption (see the
    §Cyclicity note above), so the first conjunct is now an ordinary statement
    this lemma shows is satisfiable rather than one the module assumes.
    `MarkovTrace_markov_axiom` is still an axiom, and the second conjunct is
    still about it.

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
