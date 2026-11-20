/-!
# QOU.Information.CountingDecisionBarrier — the Toda barrier to the counting→decision transfer

A machine-checked record of *why* the framework's **counting→decision transfer**
is not a chippable conjecture. The transfer is the open hypothesis
`(exact-Jones ∉ FP) ⟹ (P ≠ NP)` — the `transfer` argument of
`faithfulness_of_transfer` on `main`, and the entire remaining content of
`conj:qou-p-neq-np` (see `qou-p-neq-np.md`, PR #4866).

## What this is — and is NOT

This does **not** formalize Toda's theorem, construct an oracle, or make the
P≠NP conjecture any less open (Mathlib has no oracle / counting complexity). It
records the **propositional skeleton** of the barrier: the one implication
relating counting and decision that *is* a theorem —

  Toda: `FP = #P  ⟹  P = NP`   (`#P ⊆ FP ⟹ PH ⊆ P^{#P} = P ⟹ P = NP`)

— and the sorry-free fact that the framework's transfer is its **converse**,
which is **not entailed** by it. A concrete abstract world satisfies Toda yet
has counting-hardness (`¬ FP=#P`) coexisting with `P = NP`; so `#P`-hardness
*alone* cannot be the source of a P–NP separation. The actual barrier
strengthening (an *oracle* with `FP ≠ #P ∧ P = NP`) is Toda's relativization,
cited [toda1991]/[arora2009], not formalized here.

Purpose: anti-flip-flop infrastructure — stop future agents from "deriving" the
transfer from counting hardness; it is logically independent of the one true
counting↔decision implication.
-/

namespace QOU.Information

/-- An abstract world carrying the two separation propositions and the ONE
    implication between them that is a theorem: Toda's `FP = #P ⟹ P = NP`. -/
structure CountingDecisionWorld where
  /-- `P = NP` holds in this world. -/
  pEqNp : Prop
  /-- `FP = #P` (exact counting collapses to poly-time function computation)
      holds in this world. -/
  fpEqSharpP : Prop
  /-- **Toda's implication** (`#P ⊆ FP ⟹ PH ⊆ P^{#P} = P ⟹ P = NP`): if exact
      counting collapses to `FP`, so does the decision hierarchy. -/
  toda : fpEqSharpP → pEqNp

namespace CountingDecisionWorld

/-- **The direction that HOLDS: `P ≠ NP ⟹ FP ≠ #P`** — the contrapositive of
    Toda, discharged sorry-free from the field. A genuine *decision* separation
    forces a *counting* separation; this is the only implication between the two
    that the literature supplies. -/
theorem fpNe_of_pNe (W : CountingDecisionWorld) (h : ¬ W.pEqNp) :
    ¬ W.fpEqSharpP := fun hfp => h (W.toda hfp)

/-- **The counting→decision transfer** as a predicate on a world: counting
    hardness (`¬ FP=#P`) forces the decision separation (`¬ P=NP`). This is the
    framework's open hypothesis — the *converse* of `toda`. -/
def Transfer (W : CountingDecisionWorld) : Prop :=
  ¬ W.fpEqSharpP → ¬ W.pEqNp

end CountingDecisionWorld

/-- **Toda barrier (sorry-free): the transfer is NOT entailed by Toda.** A
    concrete world satisfies Toda (`fpEqSharpP → pEqNp`) yet **falsifies** the
    transfer — it has `P = NP` *together with* counting-hardness `¬(FP=#P)`. So
    no argument that uses only the counting↔decision implication which is
    actually a theorem can establish the transfer: `#P`-hardness alone cannot
    separate `P` from `NP`. This is the propositional skeleton of Toda's
    relativization barrier; the oracle strengthening is cited, not formalized. -/
theorem transfer_not_entailed_by_toda :
    ∃ W : CountingDecisionWorld, ¬ W.Transfer := by
  refine ⟨{ pEqNp := True, fpEqSharpP := False, toda := fun h => h.elim }, ?_⟩
  -- the world's `Transfer` unfolds to `¬False → ¬True`
  show ¬ (¬ False → ¬ True)
  intro htransfer
  exact htransfer (fun h => h) True.intro

/-- In any `CountingDecisionWorld`, `W.Transfer` holds if and only if the
    decision separation `¬ W.pEqNp` and counting separation `¬ W.fpEqSharpP`
    are logically equivalent (combining Toda's contrapositive `fpNe_of_pNe`
    with `W.Transfer`). -/
theorem CountingDecisionWorld.transfer_iff_separation_iff (W : CountingDecisionWorld) :
    W.Transfer ↔ (¬ W.pEqNp ↔ ¬ W.fpEqSharpP) :=
  ⟨fun htr => ⟨W.fpNe_of_pNe, htr⟩, fun hiff => hiff.mpr⟩

/-- Concrete separated `CountingDecisionWorld` in which both `P ≠ NP` and
    `FP ≠ #P` hold, satisfying both Toda's implication and `Transfer`. -/
def separatedCountingDecisionWorld : CountingDecisionWorld where
  pEqNp := False
  fpEqSharpP := False
  toda := fun h => h

/-- **Consistency of `Transfer` with Toda (`qou-gcwm`).** While `Transfer` is
    not entailed by `toda` (`transfer_not_entailed_by_toda`), it is consistent
    with `toda` in a separated world (`¬ pEqNp ∧ ¬ fpEqSharpP`), so `Transfer`
    is logically independent of `toda`. -/
theorem transfer_consistent_with_toda :
    ∃ W : CountingDecisionWorld, W.Transfer ∧ ¬ W.pEqNp ∧ ¬ W.fpEqSharpP :=
  ⟨separatedCountingDecisionWorld, fun _ hp => hp, fun hp => hp, fun hfp => hfp⟩

end QOU.Information
