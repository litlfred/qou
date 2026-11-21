import Mathlib.Algebra.Ring.Basic

/-!
# QOU.BraidKnot.CrystalGraphRealization — crystal-graph realisation (conjecture)

Class axiomatisation of [conj:crystal-graph-realization]: under the
Brundan–Kleshchev isomorphism, GS canonical basis elements `T_w`
correspond to indecomposable graded projective KLR modules realising
Kashiwara crystal highest-weight vectors of `Cryst(𝔰𝔩_n)`.

The class encodes the data needed by downstream blocks (the crystal
node, the Kashiwara raising/lowering operators, the highest-weight
predicate); the `crystal_realises` field is the conjectural input.

LaTeX: `\label{conj:crystal-graph-realization}`

References:
- Brundan, J. & Kleshchev, A. (2009). Blocks of cyclotomic Hecke
  algebras and Khovanov–Lauda algebras. Inv. Math. 178(3).
- Kashiwara, M. (1991). On crystal bases of the q-analogue of
  universal enveloping algebras. Duke Math. J. 63(2).
- Lecouvey, C. (2007). Combinatorics of crystal graphs for the root
  systems of types A_n, B_n, C_n, D_n and G_2. MSJ Memoirs 17.
- Khovanov, M. & Lauda, A. D. (2009). A diagrammatic approach …
-/

namespace QOU.BraidKnot

universe u

/-- **Crystal-graph realisation (conjecture).**

    A normal form `T_w ∈ H_n(R, q)` is realised by a Kashiwara
    crystal highest-weight vector via the Brundan–Kleshchev
    isomorphism.  The class fields encode:
    - `CrystalNode` — the crystal node type;
    - `nodeOf` — the node attached to a normal form;
    - `raising` / `lowering` — Kashiwara `ẽ_i` and `f̃_i` operators;
    - `crystal_realises` — the conjecture itself: every node attached
      to a GS normal form is annihilated by every raising operator. -/
-- Ref: [brundankleshchev2009] Brundan & Kleshchev, "Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras," Invent. Math. 178 (2009), arXiv:0808.2032
-- Ref: [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue of universal enveloping algebras," Duke Math. J. 63 (1991)
-- Ref: [lecouvey2007] Lecouvey, "Combinatorics of crystal graphs for the root systems of types A_n, B_n, C_n, D_n and G_2," Combinatorial Aspect of Integrable Systems (MSJ Memoirs 17, 2007)
-- Ref: [khovanovlauda2009] Khovanov & Lauda, "A diagrammatic approach to categorification of quantum groups," Repr. Theory 13 (2009), arXiv:0803.4121
class CrystalGraphRealization (R : Type u) [CommRing R] (q : R) where
  /-- Abstract type of Hecke normal forms. -/
  NormalForm : Type u
  /-- Abstract type of crystal nodes of `Cryst(𝔰𝔩_n)`. -/
  CrystalNode : Type u
  /-- Crystal node attached to a normal form. -/
  nodeOf : NormalForm → CrystalNode
  /-- Kashiwara raising operator `ẽ_i` (partial — `none` when applied
      to a highest-weight vector). -/
  raising : ℕ → CrystalNode → Option CrystalNode
  /-- Kashiwara lowering operator `f̃_i`. -/
  lowering : ℕ → CrystalNode → Option CrystalNode
  /-- **The conjecture itself**: every GS normal form's crystal node
      is a highest-weight vector.  Plays the role of `sorry`. -/
  crystal_realises : ∀ (T : NormalForm) (i : ℕ),
    raising i (nodeOf T) = none

namespace CrystalGraphRealization

/-- Unconditional structural lemma: applying any raising operator to
    `nodeOf T` returns `none`, i.e. `nodeOf T` is highest-weight.
    Direct consequence of `crystal_realises`. -/
-- Ref: [leitner2026] braids-and-knots/crystal-graph-realization
theorem nodeOf_highest_weight
    {R : Type u} [CommRing R] {q : R} [C : CrystalGraphRealization R q]
    (T : C.NormalForm) (i : ℕ) :
    C.raising i (C.nodeOf T) = none :=
  C.crystal_realises T i

/-- Highest-weight predicate on a crystal node: every Kashiwara raising
    operator `ẽ_i` annihilates it.  Standard Kashiwara/Lecouvey
    convention. -/
-- Ref: [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue of universal enveloping algebras," Duke Math. J. 63 (1991)
-- Ref: [lecouvey2007] Lecouvey, "Combinatorics of crystal graphs for the root systems of types A_n, B_n, C_n, D_n and G_2," Combinatorial Aspect of Integrable Systems (MSJ Memoirs 17, 2007)
def IsHighestWeight {R : Type u} [CommRing R] {q : R}
    [C : CrystalGraphRealization R q] (v : C.CrystalNode) : Prop :=
  ∀ i : ℕ, C.raising i v = none

/-- Unconditional packaged form: the crystal node attached to any GS
    normal form is a Kashiwara highest-weight vector.  This is the
    clean, downstream-usable restatement of `crystal_realises`. -/
-- Ref: [leitner2026] braids-and-knots/crystal-graph-realization
theorem nodeOf_isHighestWeight
    {R : Type u} [CommRing R] {q : R} [C : CrystalGraphRealization R q]
    (T : C.NormalForm) :
    IsHighestWeight (C.nodeOf T) :=
  fun i => C.crystal_realises T i

/-- **The degenerate model** — a `def`, deliberately NOT an `instance`.

Both carrier types collapse to `PUnit` and both crystal operators return
`none`, so `crystal_realises` closes by `rfl`: it holds because there is
nothing for it to say, not because the crystal structure was constructed.

It was declared `instance` and documented as *"Faithful instance. Carries the
explicit research-grade conjecture as a sorry."* Neither half held. There is no
`sorry` term anywhere in this file — the two occurrences of the word are both in
docstrings — so `#print axioms` on anything downstream reported no `sorryAx`,
and `nodeOf_isHighestWeight` above read as an established result about GS normal
forms whose only model in scope has exactly one normal form and one node.

As an `instance` it satisfied every `[CrystalGraphRealization R q]` binder by
synthesis. Demoting it changes nothing else: measured 2026-08-24, all twelve
files that bind this class — eight library modules and four content-block
siblings — build with **zero** errors afterwards, because every one of those
binders is a hypothesis in a signature (the honest §3b-cond shape) rather than a
synthesis site. The measurement is sensitive rather than vacuous: with this
declaration a `def`, `inferInstance` for the class fails with *"failed to
synthesize QOU.BraidKnot.CrystalGraphRealization"*, and succeeds again when it
is restored to an `instance`.

The model stays available to anyone who wants it by name; it is simply no longer
found by instance synthesis. Same disposition as `triv_hecke` /
`triv_wedderburn` (PR #5581) and `skeletonRealisation` (PR #5621).
`QOU/MassEndomorphism/VolumeBridge.lean` is the instance-free design this
follows. -/
-- Ref: [leitner2026] braids-and-knots/crystal-graph-realization
def canonical (R : Type u) [CommRing R] (q : R) :
    CrystalGraphRealization R q where
  NormalForm := PUnit
  CrystalNode := PUnit
  nodeOf _ := PUnit.unit
  raising _ _ := none
  lowering _ _ := none
  crystal_realises _ _ := rfl

end CrystalGraphRealization

end QOU.BraidKnot
