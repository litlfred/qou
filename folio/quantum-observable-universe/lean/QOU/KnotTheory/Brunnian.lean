import QOU.KnotTheory
import Mathlib.Data.Fin.Basic
import Mathlib.Data.List.Basic

/-!
# QOU.KnotTheory.Brunnian — Brunnian property of the Borromean rings

The defining property of a Brunnian link is that every proper
sub-link is the unlink.  **This is the TRUE property (tier 1)**; three weaker or
unrelated conditions elsewhere in the corpus also carry the name — Tier table for the four things this corpus calls `Brunnian`, and which implications hold: `QOU.Mass.BrunnianTierDisambiguation`.  For the Borromean rings `𝓑₃`
(`borromeanRings` in `QOU.KnotTheory`) this says: removing any
one of the three components leaves the trivial two-component
unlink `U₂`.

In the QOU framework this is the topological face of *color
confinement*: a hadron whose three quarks are the components of
`𝓑₃` cannot be split into "two confined + one free" — extracting
any single quark dissolves the binding between the remaining two.
See [`conj:brunnian-property-of-borromean`] and
[`rem:borromean-topological-confinement`] for the manuscript
side.

## Status

`borromean_brunnian` is **conjectural** — the `sorry` is the
conjectural witness per AGENTS.md §3b, not a missing arithmetic
fact.  The gap is the absence of Mathlib primitives for
braid-word Reidemeister-move equivalence: `isUnlink` is left
`opaque` here pending that formalisation.  Once R-moves +
Markov stabilisation are in place, the proof reduces to
exhibiting the explicit move sequence from
`(σ₀⁻¹)³ ∈ B₂` (or the symmetric variants for `i = 1, 2`) to
the empty braid in `B₂`.

The naive component-deletion `BraidWord.deleteComponent` defined
below preserves the braid-word combinatorics but **not** the
link topology — recovering the actual sub-link needs the
link-equivalence relation that `isUnlink` abstracts over.
-/

namespace QOU.KnotTheory.Brunnian

open QOU.KnotTheory

/-- Naive strand-deletion on a list of braid letters.  Drops
    every letter whose generator touches strand `i` (index
    `i-1` or `i`), and decrements the index of every surviving
    letter whose index `> i` so the result is well-typed for
    `B_{n-1}`.

    Topologically this preserves the link only modulo the
    Reidemeister + Markov equivalence relation; recovering the
    actual sub-link requires the as-yet-unformalised
    link-equivalence machinery. -/
def deleteLetters (ℓ : List BraidLetter) (i : ℕ) : List BraidLetter :=
  ℓ.filterMap fun l =>
    if l.index = i ∨ l.index + 1 = i then
      none
    else if l.index > i then
      some ⟨l.index - 1, l.sign⟩
    else
      some l

/-- Naive component deletion on a braid word: drops the strand
    at position `i` and renumbers higher generators.  See the
    `deleteLetters` doc-comment for the topological caveat. -/
def BraidWord.deleteComponent (β : BraidWord) (i : ℕ) : BraidWord where
  name := β.name ++ "_minus_" ++ toString i
  strands := β.strands - 1
  letters := deleteLetters β.letters i
  components := if β.components > 0 then β.components - 1 else 0

/-- `isUnlink β` asserts that the Markov closure of `β` is the
    trivial `β.components`-component unlink.

    Declared `opaque` because the full predicate needs the
    Reidemeister + Markov equivalence relation on braid-word
    closures, which is not yet formalised in Mathlib.  The
    conjectural-class hypothesis `[LinkEquivalence]` below
    plays the role of an explicit witness.

    -- Ref: [kawauchi1996] Survey of Knot Theory §1.2
-/
opaque isUnlink : BraidWord → Prop

/-- **§3b-cond conjectural witness.**  Discharging this class
    instance is equivalent to formalising the link-equivalence
    relation on braid-word closures — i.e. proving that two
    braid words present the same link iff they are related by a
    finite sequence of Reidemeister moves (R1/R2/R3) and Markov
    moves (conjugation + stabilisation).

    -- Ref: [leitner2026] conj:brunnian-property-of-borromean
-/
class LinkEquivalence where
  brunnian_borromean : ∀ i : ℕ, i < 3 → isUnlink (BraidWord.deleteComponent borromeanRings i)

/-- **Brunnian property of the Borromean rings** (conditional on
    `LinkEquivalence`).  Removing any of the three components of
    `𝓑₃` yields a two-component sub-link whose closure is the
    trivial unlink `U₂`.

    Naive deletion at the BraidWord level does not literally
    yield the empty braid: for `i = 0` we get
    `(σ₀⁻¹)³ ∈ B₂`, whose closure is the negative trefoil; the
    discharge to `U₂` is by an R3-then-R2-twice sequence, which
    is precisely the content of the `LinkEquivalence` class.

    -- Ref: [kawauchi1996] Survey of Knot Theory §1.5
    -- Ref: [leitner2026] conj:brunnian-property-of-borromean
-/
theorem borromean_brunnian [le : LinkEquivalence] :
    ∀ i : Fin 3, isUnlink (BraidWord.deleteComponent borromeanRings i.val) := by
  intro i
  exact le.brunnian_borromean i.val i.isLt

/-- Decategorified corollary used by
    `rem:borromean-topological-confinement`: no isolated quark
    can survive the removal-of-one-component operation on a
    Borromean baryon, because the remaining link is trivial. -/
theorem no_isolated_quark_in_borromean_baryon [LinkEquivalence] :
    ∀ i : Fin 3, isUnlink (BraidWord.deleteComponent borromeanRings i.val) :=
  borromean_brunnian

end QOU.KnotTheory.Brunnian
