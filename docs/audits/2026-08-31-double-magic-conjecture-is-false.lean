/-
  Bean `qou-z9ws` — `DoubleMagicConjecture` is FALSE as stated.

  THE FINDING

  `QOU.Interactions.LRFusion.DoubleMagicConjecture` carries two fields.  The
  second is an **iff**, quantified over every `Composite`:

      magic_iff_double_magic :
        ∀ (C : Composite),
          (kappa C.ydA = 0 ∧ isSelfConjugate C.ydA ∧ C.ydA.n ∈ magicLadder)
          ↔ IsDoubleMagic C

  Instantiate it at the all-empty composite `⟨∅, ∅, ∅⟩`, whose `mass_eq` reads
  `0 = 0 + 0`.  Then:

  - `IsDoubleMagic C` is `isSelfConjugate ∅ ∧ isSelfConjugate ∅`, which **holds**
    — by the corpus's own `emptyDiagram_isSelfConjugate`;
  - so the `←` direction forces `C.ydA.n ∈ magicLadder`, i.e. `0 ∈ {2, 8, 20,
    28, 50, 82, 126}`, which is false.

  The class is therefore uninhabitable, and `¬ DoubleMagicConjecture` is proved
  below.

  SCOPE — this is a (b) STRUCTURAL EXCLUSION of the ENCODING, not of the physics.

  Under AGENTS.md §"Before declaring refuted", a (b) claim needs a proved
  invariant.  Here there are two, both already in the corpus: `magicSet` is the
  literal `{2, 8, 20, 28, 50, 82, 126}` (`QOU/Common/MagicNumbers.lean`) so `0`
  is not in it by `decide`, and `emptyDiagram_isSelfConjugate` is a sorry-free
  theorem in `ShellNeutrality.lean`.

  What is excluded is **the iff as written**, because it over-quantifies: the
  reverse direction claims that *every* double-magic composite lands on the
  magic ladder, and the empty composite is double-magic for the degenerate
  reason that the empty diagram is trivially self-conjugate.  The physical
  conjecture is about composites of *saturated* constituents; nothing in the
  Lean requires `C.ydZ` or `C.ydN` to be non-empty, or `C.ydA.n ≥ 2`.

  So this says nothing about whether double-magic nuclei sit on the magic
  ladder.  It says the Lean statement quantifies over a case the physics does
  not intend, and is false there.  The repair is a non-degeneracy hypothesis —
  authorial, and deliberately not applied here.

  WHY IT MATTERS ANYWAY.  Two theorems in the same file consume the class:
  `composite_self_conjugate_of_double_magic` and
  `composite_kappa_zero_of_double_magic`.  A class that cannot be inhabited
  makes both **vacuously true**: `False → P` holds for every `P`, so they prove
  nothing and would equally "prove" their own negations.  This is the second
  such case in the arc, after `QOU.HadronicMass.SkeinMassRelationHolds`.

  Note also that `DoubleMagicConjecture` is one NAME over TWO objects: this one
  (`QOU/Interactions/LRFusion.lean:133`, unparameterised) and a different class
  `DoubleMagicConjecture (Z N : ℕ) extends LRFusionData Z N` in the content
  block `observations/diagrammatic-double-magic-lr-fusion.lean:58`.  This
  refutation is about the first.  Resolve the name to its declaration before
  citing either.

  ON THE PROOF.  `→ False` rather than `¬`: the class is declared without
  `: Prop`, so it lives in `Type` and its instances are data.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<QOU build lib> \
        lean docs/audits/2026-08-31-double-magic-conjecture-is-false.lean

  Measured 2026-08-31: exit 0, 0 errors.
-/
import QOU.Interactions.LRFusion

namespace DoubleMagicRefutation
open QOU.Interactions.LRFusion QOU.BraidKnot.ShellNeutrality
  QOU.LiftingDescent.HomologicalCondensation

/-- The all-empty composite: `|λ_A| = |λ_Z| + |λ_N|` reads `0 = 0 + 0`. -/
def emptyComposite : Composite where
  ydZ := emptyDiagram
  ydN := emptyDiagram
  ydA := emptyDiagram
  mass_eq := by simp [emptyDiagram]

theorem emptyComposite_isDoubleMagic : IsDoubleMagic emptyComposite :=
  ⟨emptyDiagram_isSelfConjugate, emptyDiagram_isSelfConjugate⟩

/-- **`DoubleMagicConjecture` is FALSE as stated.** -/
theorem doubleMagicConjecture_false : DoubleMagicConjecture → False := by
  intro D
  have h := (D.magic_iff_double_magic emptyComposite).mpr emptyComposite_isDoubleMagic
  have hmem := h.2.2
  unfold magicLadder QOU.Common.magicSet at hmem
  simp [emptyComposite, emptyDiagram] at hmem

end DoubleMagicRefutation
