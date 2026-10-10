/-
# A cost that factors through a quotient does not determine the selected word

`QOU.Mass.FrobeniusSelected B y cands cost w` picks the **minimal-cost**
reading-3-feasible candidate. Its `cost : W → R` is **wholly unconstrained** —
no injectivity, no order-sensitivity, not even that `W` is a word type — and
every instantiation in the corpus is `cost = fun w => (w.length : ℝ)`, the
crossing count (`frobeniusSelected_borromean`, `frobeniusSelected_borromean_ten`,
`interfaceSelected_three`).

`FrobeniusSelected.cost_eq` already says two selected words have equal **cost**.
It stops one step short of what bean `qou-99qc` needs, which is that the
selection predicate can hold of **two different words** — so the rule does not
determine the word. This file supplies that step, for an arbitrary quotient the
cost factors through.

## What is NEW here, and what is merely cited

The **invariance** half is already held in this corpus, sorry-free, and is
**cited rather than re-derived**:

* `QOU.QBeta.OptionELevelAcceptanceTest.monoidHom_order_blind` — a multiplicative
  functional is blind to word order (the multiplicative twin of
  `letterSumCost_perm` below);
* `QOU.Mass.AltCharShiftMultiset.wordChar_of_perm` — the alternating character is
  order-blind;
* `crossing-energy.lean` models `BraidWord := List Bool` and reads only two
  counts, so `E_cross`'s blindness is **definitional** there.

What is new is the **bridge**: nothing in the corpus draws the
non-determination consequence from blindness. That is
`selected_not_determined_of_cost_factors`.

## 🛑 A wrong turn recorded, because it is the interesting part

This file was first drafted around the **abelianization** — "a cost factoring
through `B_n^ab ≅ ℤ` cannot separate two words of equal exponent sum". That
framing is **wrong for its own targets** and is not used here.

`B_n^ab` records only `e = n₊ − n₋`. But the corpus's own decomposition
(`crossing-energy.lean`) is

    value = n₊·q − n₋·q⁻¹,   coulomb = ½(n₊ + n₋)(q − q⁻¹),   baseline = ½(n₊ − n₋)(q + q⁻¹)

so of the three only `baseline` (the writhe) factors through the abelianization.
**Crossing count `n₊ + n₋` does not** — and it is `FrobeniusSelected`'s only
instantiation in the entire corpus. Neither does `E_cross`. An
abelianization-quantified theorem would have claimed a family it provably does
not cover.

The right invariant **for a cost** is the **multiset** of letters (equivalently
`List.Perm`), which is what the sibling probe
`computations/qbeta/qbeta_embedding_energy_can_discriminate_probe.py` already
names, and it is strictly coarser: every function of the exponent sum is a
function of the multiset, not conversely.

### …but the abelianization framing is RIGHT one step over, for the EMBEDDING

Recorded 2026-09-14, after the retraction above and against it in part. The
`geodesic → O'Hara` bridge (`qbeta_bring_ohara_bridge_probe.py`, merged #7374)
sends a braid word to a cusp-torus lattice class

    (m, ℓ) = (exponent sum, strand count)

— its own words, at `:65`. **`m` is exactly the abelianization**: `e : B_d → ℤ`,
`σ_i ↦ 1`, induces `B_d/[B_d,B_d] ≅ ℤ` (Black–Samson,
`library/black-samson-phd2010sp/sections/sec-008-12-summary-of-thesis.md:126`),
and `ℓ` does not depend on the word at all.

So the abelianization is the wrong invariant for the **cost** and the right one
for the **embedding map** — and that map is *strictly coarser* than the multiset,
so it loses strictly more. `selected_not_determined_of_cost_factors` is
quantified over an **arbitrary** quotient `π` precisely so it covers this case:
instantiate `π = (writhe, strands)` and the sibling's measured negative — all
four two-crossing gluon dressings share one class, one geodesic and one energy —
is an instance of it.

The lesson is about *which object* a blindness claim is attached to, not about
the invariant: the same quotient that under-prunes on one side of the pipeline
over-collapses on the other.

## Scope (AGENTS.md (a)/(b) vocabulary)

* **(b) structural**, invariant = the target monoid's commutativity
  (`List.Perm.sum_eq`). No letter-sum cost separates a rearrangement pair.
* It does **NOT** prove that a selection cost must be order-sensitive. Blindness
  *precludes separating these candidates*; it does not *force* any replacement to
  see order. That caution is the corpus's own (`qou-99qc`, line ~1100) and is
  restated here so the theorems below are not read as more than they are.
* It does **not** exhibit a rearrangement pair inside the corpus's live `cands`
  that is also feasible — that is a measurement, not a corollary.
* It proposes **no** replacement cost.

Generic throughout: cost in an `AddCommMonoid`, comparison in a `Preorder`
(AGENTS.md §7c). Bean `qou-99qc`.

## 🟩 THE REPLACEMENT THIS FILE DEMANDS HAS BEEN BUILT — by a sibling, and
   not by me (2026-09-14, later the same day)

This file says, in the paragraph above, that it supplies **no** replacement
cost — only the statement that a replacement must not be constant on the fibre.
That gap is now filled, by `claude/99qc-crossing-budget-parity-2026-09-14`
(PR #7390) and its commits now on `main`:

* `QOU.QBeta.ECatBlockDecomposition.pairSum_not_perm_invariant` and
  `blockCost_can_separate` — a **pair kernel** in the cost socket, whose
  `1/d_arc²` separation weight is what breaks the tie; and
* `qbeta_ecat_pair_kernel_probe` (4/4), which measures it: four distinct
  values over the four gluon dressings, against **one** value for every
  letter-sum.

**It escapes THIS file's quotient, not only permutation.**
`QOU.QBeta.LetterSumBlindness.bridgeClass_perm_blind` is exactly the
`(exponent sum, strands)` map named in the paragraph above as the corpus's
embedding map, and the four candidates all sit at **writhe +2, length 2** —
one fibre of it — while the kernel gives four distinct values there. So the
positive instance of `selected_not_determined_of_cost_factors`'s hypothesis
failing is already measured, across assertions 1 and 2 of that probe.

**Deliberately NOT re-derived here.** Per the convergence rule, the second
route verifies and cites rather than re-deriving: nothing in this file is
changed, no companion lemma is added, and the credit is theirs. The two
results are complementary and their own commit says how — theirs turns on
**permutation** of letters, mine on the **writhe/count split** at fixed
writhe; neither implies the other.

**What is still open is narrower, not closed.** Their probe's own assertion 4
scopes it: the kernel is a *discretisation*, its continuum limit is not proved
to be `E_cat`, and the classical-limit leg it would need is assumed. That leg
is the `CategoricalMobiusEnergy.classicalLimit` field, which
`QOU.MobiusEnergy.classicalLimit_unconstraining` (this branch, sorry-free)
shows constrains **nothing** as encoded. Reported to them on #7390.
-/
import Mathlib.Data.List.Perm.Basic
import Mathlib.Algebra.BigOperators.Group.List.Lemmas
import Mathlib.Order.Defs.PartialOrder
import Mathlib.Data.Nat.Cast.Defs

namespace QOU.Mass.CostOrderSensitivity

universe u v w

variable {W : Type u} {Q : Type v} {R : Type w}

/-! ## The bridge: minimality transfers along a fibre of the quotient -/

/-- **Minimality transfers along the fibre.** If the cost is `f ∘ π` and `w₂`
lies in the same fibre of `π` as a cost-minimal `w₁`, then `w₂` is cost-minimal
too. Nothing about words is used: this is a statement about minimising a
function that is constant on fibres. -/
theorem minimal_transfers_along_fibre [Preorder R]
    {Feasible : W → Prop} {cands : Set W} (π : W → Q) (f : Q → R)
    {w₁ w₂ : W} (hfib : π w₂ = π w₁)
    (h₁min : ∀ w' ∈ cands, Feasible w' → f (π w₁) ≤ f (π w')) :
    ∀ w' ∈ cands, Feasible w' → f (π w₂) ≤ f (π w') := by
  intro w' hw' hf
  rw [hfib]
  exact h₁min w' hw' hf

/-- **The step `FrobeniusSelected.cost_eq` stops short of.** If two *distinct*
feasible candidates lie in the same fibre of a quotient the cost factors
through, then the minimal-cost selection predicate holds of **both**, so it does
not determine the word.

The three conjuncts are exactly `FrobeniusSelected`'s `mem`, `feasible` and
`minimal`, spelled out rather than by re-declaring that structure — this is a
statement *about* the corpus's selection rule, not a second copy of it. -/
theorem selected_not_determined_of_cost_factors [Preorder R]
    {Feasible : W → Prop} {cands : Set W} (π : W → Q) (f : Q → R)
    {w₁ w₂ : W} (hne : w₁ ≠ w₂) (hfib : π w₂ = π w₁)
    (h₁mem : w₁ ∈ cands) (h₁feas : Feasible w₁)
    (h₁min : ∀ w' ∈ cands, Feasible w' → f (π w₁) ≤ f (π w'))
    (h₂mem : w₂ ∈ cands) (h₂feas : Feasible w₂) :
    ∃ a b : W, a ≠ b
      ∧ (a ∈ cands ∧ Feasible a ∧ ∀ w' ∈ cands, Feasible w' → f (π a) ≤ f (π w'))
      ∧ (b ∈ cands ∧ Feasible b ∧ ∀ w' ∈ cands, Feasible w' → f (π b) ≤ f (π w')) :=
  ⟨w₁, w₂, hne, ⟨h₁mem, h₁feas, h₁min⟩,
   ⟨h₂mem, h₂feas, minimal_transfers_along_fibre π f hfib h₁min⟩⟩

/-! ## The instantiation the corpus actually uses -/

variable {L : Type u}

/-- A **letter-sum cost**: the cost of a word is the sum of a per-letter weight.
Crossing count is `weight ≡ 1`; writhe is `weight = ±1`; the crossing energy
`E_cross` measured in `qou-99qc` is `weight = ±h`. -/
def letterSumCost [AddCommMonoid R] (weight : L → R) (w : List L) : R :=
  (w.map weight).sum

/-- A letter-sum cost splits off its head letter. -/
theorem letterSumCost_cons [AddCommMonoid R] (weight : L → R) (a : L) (t : List L) :
    letterSumCost weight (a :: t) = weight a + letterSumCost weight t := rfl

/-- **The invariance, additive form.** A letter-sum cost is blind to word order.

This is the additive twin of the already-held
`QOU.QBeta.OptionELevelAcceptanceTest.monoidHom_order_blind`, and is stated here
only so the instantiations below can use it directly; the *result* is not new. -/
theorem letterSumCost_perm [AddCommMonoid R] (weight : L → R)
    {w w' : List L} (h : w.Perm w') :
    letterSumCost weight w = letterSumCost weight w' :=
  (h.map weight).sum_eq

/-- The corpus's own cost — `fun w => (w.length : R)`, the crossing count — is
the letter-sum cost with unit weight, hence is covered. -/
theorem length_eq_letterSumCost [AddCommMonoidWithOne R] (w : List L) :
    (w.length : R) = letterSumCost (fun _ => (1 : R)) w := by
  induction w with
  | nil => simp [letterSumCost]
  | cons a t ih =>
      rw [letterSumCost_cons, ← ih, List.length_cons, Nat.cast_add, Nat.cast_one]
      exact add_comm _ _

/-- **The corpus's crossing-count cost does not determine the word.** Two
distinct feasible candidates that rearrange one another are both selected.

`π` is the length; `f` is the cast. Because `List.length` is `Perm`-invariant,
the fibre hypothesis is supplied by the rearrangement itself. -/
theorem lengthCost_not_determined [AddCommMonoidWithOne R] [Preorder R]
    {Feasible : List L → Prop} {cands : Set (List L)}
    {w₁ w₂ : List L} (hne : w₁ ≠ w₂) (hp : w₂.Perm w₁)
    (h₁mem : w₁ ∈ cands) (h₁feas : Feasible w₁)
    (h₁min : ∀ w' ∈ cands, Feasible w' → ((w₁.length : R)) ≤ (w'.length : R))
    (h₂mem : w₂ ∈ cands) (h₂feas : Feasible w₂) :
    ∃ a b : List L, a ≠ b
      ∧ (a ∈ cands ∧ Feasible a ∧ ∀ w' ∈ cands, Feasible w' → ((a.length : R)) ≤ (w'.length : R))
      ∧ (b ∈ cands ∧ Feasible b ∧ ∀ w' ∈ cands, Feasible w' → ((b.length : R)) ≤ (w'.length : R)) :=
  selected_not_determined_of_cost_factors (R := R) List.length Nat.cast hne
    hp.length_eq h₁mem h₁feas h₁min h₂mem h₂feas

/-- The same for an arbitrary letter-sum cost — crossing count, writhe, and
`E_cross` as measured are all instances. -/
theorem letterSumCost_not_determined [AddCommMonoid R] [Preorder R]
    {Feasible : List L → Prop} {cands : Set (List L)} (weight : L → R)
    {w₁ w₂ : List L}
    (h₁min : ∀ w' ∈ cands, Feasible w' →
      letterSumCost weight w₁ ≤ letterSumCost weight w')
    (hp : w₂.Perm w₁) :
    ∀ w' ∈ cands, Feasible w' →
      letterSumCost weight w₂ ≤ letterSumCost weight w' := by
  intro w' hw' hf
  rw [letterSumCost_perm weight hp]
  exact h₁min w' hw' hf

/-! ## Non-vacuity

The fibre hypothesis with `w₁ ≠ w₂` is satisfiable, so the theorems above are
not about an empty case. This is the abstract shape of the pair the sibling
probe measured: `σ₁σ₀` and `σ₀σ₁` tie at `2q` under `E_cross` while the `Q_β`
they produce differ by roughly a factor of two. -/

/-- Two **distinct** words that are permutations of one another. -/
theorem exists_distinct_perm : ∃ a b : List ℕ, a.Perm b ∧ a ≠ b :=
  ⟨[0, 1], [1, 0], List.Perm.swap 1 0 [], by decide⟩

/-- A letter-sum cost really does fail to separate a concrete distinct pair:
those two words have equal cost under **every** weight. -/
theorem letterSumCost_fails_to_separate [AddCommMonoid R] (weight : ℕ → R) :
    letterSumCost weight [0, 1] = letterSumCost weight [1, 0] :=
  letterSumCost_perm weight (List.Perm.swap 1 0 [])

end QOU.Mass.CostOrderSensitivity
