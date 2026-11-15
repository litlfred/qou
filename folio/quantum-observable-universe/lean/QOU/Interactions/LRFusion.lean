import QOU.BraidKnot.ShellNeutrality
import QOU.LiftingDescent.HomologicalCondensation
import Mathlib.Data.Real.Basic

/-!
# QOU.Interactions.LRFusion — double-magic LR-fusion rigidity

A composite nuclear configuration `A = Z + N` is double-magic iff the
Littlewood–Richardson fusion of the proton representation `V_{ydZ}`
and the neutron representation `V_{ydN}` yields a dominant composite
`V_{ydA}` whose Jucys–Murphy multiset is gapless and globally
neutral: `κ_{ydA} = 0`.

Conjectural-propagation (AGENTS.md §3b): downstream of
`SaturatedShellConjecture` and `ShellCondensationConjecture`, so the
LR-rigidity claim is also axiomatised here.

LaTeX label: `conj:diagrammatic-double-magic-lr-fusion`

## References

- [mathas1999] https://doi.org/10.1090/ulect/015 — Iwahori–Hecke
  and Schur algebras (LR-rule version)
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [turaev2010] https://doi.org/10.1515/9783110221848
- [jucys1974] — Jucys–Murphy elements
- [murphy1992] https://doi.org/10.1016/0021-8693(92)90105-T
- [leitner2026] observations / diagrammatic-double-magic-lr-fusion
-/

namespace QOU.Interactions.LRFusion

open QOU.BraidKnot.ShellNeutrality
open QOU.LiftingDescent.HomologicalCondensation

/-! ## §1  Composite nuclear data -/

/-- A composite nucleus: proton diagram `ydZ`, neutron diagram
    `ydN`, and the dominant LR-composite diagram `ydA` they fuse
    to. The composite has `n = Z + N` boxes. -/
structure Composite where
  ydZ : YoungDiagram
  ydN : YoungDiagram
  ydA : YoungDiagram
  /-- Mass number condition. -/
  mass_eq : ydA.n = ydZ.n + ydN.n

/-! ## §2  Provable algebraic ingredient — content additivity -/

/-- **Content additivity** (provable from the LR rule, axiomatised
    here at the abstract framework level): the Jucys–Murphy charge
    of the dominant composite equals the sum of the constituent
    charges. This is the standard fact that contents add under
    tensor induction.

    A concrete *non-vacuous* instance is the disjoint-union
    composite `Composite.fromUnion`, where `ydA := ydZ ⊔ ydN`
    is the multiset disjoint union; in that case content additivity
    is *proved* directly from `kappa_unionDiagram`
    (see instance `contentAdditive_fromUnion`). The full LR-fusion
    `ydA` is conjecturally also content-additive but requires the
    LR rule to verify. -/
class ContentAdditive (C : Composite) : Prop where
  kappa_add : kappa C.ydA = kappa C.ydZ + kappa C.ydN

/-- The **trivial composite** built from the disjoint multiset union
    of constituents. This is *not* the LR-fusion composite — it is a
    structural lower bound: any well-defined composite must agree
    with this one on the level of content sums.

    Existence of this composite, together with the proved instance
    `contentAdditive_fromUnion`, shows that `ContentAdditive` is a
    consistent typeclass (non-vacuous). -/
def Composite.fromUnion (ydZ ydN : YoungDiagram) : Composite where
  ydZ := ydZ
  ydN := ydN
  ydA := unionDiagram ydZ ydN
  mass_eq := rfl

/-- The trivial union composite is content-additive *by direct
    proof* (no axiom). Provides a concrete instance of
    `ContentAdditive` against which downstream theorems can be
    smoke-tested. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
instance contentAdditive_fromUnion (ydZ ydN : YoungDiagram) :
    ContentAdditive (Composite.fromUnion ydZ ydN) where
  kappa_add := by
    -- goal: kappa (Composite.fromUnion ydZ ydN).ydA
    --       = kappa (Composite.fromUnion ydZ ydN).ydZ
    --         + kappa (Composite.fromUnion ydZ ydN).ydN
    show kappa (unionDiagram ydZ ydN) = kappa ydZ + kappa ydN
    exact kappa_unionDiagram ydZ ydN

/-! ## §3  Double-magic predicate -/

/-- The composite is **double magic** when both constituents are
    saturated and self-conjugate (the LR-rigidity input).

    **Corrected 2026-08-31 — the `saturated` half was in this docstring but
    not in the definition.** The `.md`
    ([`conj:diagrammatic-double-magic-lr-fusion`](../../../observations/diagrammatic-double-magic-lr-fusion.md))
    opens *"Let `Z, N ∈ 𝔐`"* — both constituent levels are drawn from the magic
    set — and only then invokes `prop:categorical-neutrality-saturated-shells`
    for self-conjugacy. The definition here carried the self-conjugacy alone, so
    "double magic" meant "both constituents self-conjugate", with no magic
    number involved anywhere. Under that reading the **empty** composite
    `⟨∅, ∅, ∅⟩` is double-magic — the empty diagram is trivially self-conjugate
    (`emptyDiagram_isSelfConjugate`) — which is what refuted the class below. -/
def IsDoubleMagic (C : Composite) : Prop :=
  (C.ydZ.n ∈ magicLadder ∧ isSelfConjugate C.ydZ) ∧
  (C.ydN.n ∈ magicLadder ∧ isSelfConjugate C.ydN)

/-- **Lemma (proved):** self-conjugate constituents force zero global
    Jucys–Murphy charge `κ_{ydA} = 0`. Direct from
    `kappa_zero_of_self_conjugate` (proved in ShellNeutrality) plus
    content additivity (typeclass field).

    Stated on the two self-conjugacy facts rather than on `IsDoubleMagic`,
    because that is all the proof uses — saturation is irrelevant to it, and
    requiring it would weaken the lemma for no gain. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
theorem kappa_zero_of_selfConj_constituents
    (C : Composite) [CA : ContentAdditive C]
    (hZ' : isSelfConjugate C.ydZ) (hN' : isSelfConjugate C.ydN) :
    kappa C.ydA = 0 := by
  have hZ : kappa C.ydZ = 0 := kappa_zero_of_self_conjugate C.ydZ hZ'
  have hN : kappa C.ydN = 0 := kappa_zero_of_self_conjugate C.ydN hN'
  rw [CA.kappa_add, hZ, hN, add_zero]

/-- **Lemma (proved):** a double-magic composite has zero global
    Jucys–Murphy charge `κ_{ydA} = 0`. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
theorem doubleMagic_kappa_zero
    (C : Composite) [ContentAdditive C]
    (hM : IsDoubleMagic C) :
    kappa C.ydA = 0 :=
  kappa_zero_of_selfConj_constituents C hM.1.2 hM.2.2

/-! ## §4  The LR-fusion rigidity conjecture -/

/-- **Conjecture 3 — Diagrammatic double-magic and LR-fusion rigidity.**

    For saturated, self-conjugate constituents `λ_Z ⊢ Z` and `μ_N ⊢ N`
    (`Z, N ∈ 𝔐`), the LR-fusion at level `A = Z + N` is **rigid**: the dominant
    composite `ν_{ZN} ⊢ A` is itself self-conjugate. That is the `.md`'s claim
    and it is what `lr_rigidity` states.

    ### 🛑 The second field is gone (2026-08-31), and it was FALSE

    Until 2026-08-31 this class carried a second field:

    ```lean
    magic_iff_double_magic : ∀ (C : Composite),
      (kappa C.ydA = 0 ∧ isSelfConjugate C.ydA ∧ C.ydA.n ∈ magicLadder)
      ↔ IsDoubleMagic C
    ```

    It is removed for **two independent reasons**, both measured.

    **(1) The `A ∈ magicLadder` conjunct is not in the `.md`, and is false at
    every physically intended instance.** The source block claims that the
    dominant `ν_{ZN}` is self-conjugate with `c(ν) = 0` and LR multiplicity one;
    it never claims the *composite strand count* `A = Z + N` is a magic number.
    Magic numbers are shell closures for a proton or neutron count separately,
    and the sum of two of them is essentially never one: of the seven observed
    double-magic nuclei — ⁴He (A=4), ¹⁶O (16), ⁴⁰Ca (40), ⁴⁸Ca (48), ⁵⁶Ni (56),
    ¹³²Sn (132), ²⁰⁸Pb (208) — **not one** has `A ∈ {2, 8, 20, 28, 50, 82, 126}`.
    Exhaustively, the only magic pair whose sum is magic at all is `8 + 20 = 28`.

    **(2) The `↔` was refutable, and the repair to `IsDoubleMagic` moves the
    falsity rather than removing it.** With the old definition the `←`
    direction failed at the empty composite (double-magic by triviality,
    `A = 0 ∉ magicLadder`). Adding the missing saturation makes `←` safe and
    breaks `→` at the same point: `κ(∅) = 0` and `∅` is self-conjugate, but
    `0 ∉ magicLadder` so `∅` is not saturated. A converse of this shape cannot
    be rescued by a non-degeneracy guard alone.

    The converse was in any case a Lean addition: the removed docstring said
    *"The reverse direction asserts that **only** double-magic compositions
    reach the magic ladder"*, a claim the `.md` does not make.

    **Still not encoded**: the `.md` also claims the LR multiplicity is one
    (`c^{ν}_{λ,μ} = 1`, all others vanishing). That needs Littlewood–Richardson
    coefficients, which this file does not carry, so it is stated in the
    narrative and absent here. Recorded so the gap is visible rather than
    implied.

    Bean `qou-z9ws`; refutation of the old form in
    `docs/audits/2026-08-31-double-magic-conjecture-is-false.lean`. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
class DoubleMagicConjecture where
  /-- LR-rigidity: the dominant composite of two self-conjugate
      saturated constituents is itself self-conjugate. -/
  lr_rigidity :
    ∀ (C : Composite),
      IsDoubleMagic C → isSelfConjugate C.ydA

/-- Re-export: at a double-magic composite, the dominant module is
    self-conjugate. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
theorem composite_self_conjugate_of_double_magic
    [D : DoubleMagicConjecture]
    {C : Composite} (h : IsDoubleMagic C) :
    isSelfConjugate C.ydA :=
  D.lr_rigidity C h

/-- Re-export: a double-magic composite has zero global Jucys–Murphy
    charge.  Combines content additivity with the
    self-conjugate-zero-charge field. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
theorem composite_kappa_zero_of_double_magic
    [D : DoubleMagicConjecture]
    (C : Composite) [ContentAdditive C]
    (h : IsDoubleMagic C) :
    kappa C.ydA = 0 :=
  doubleMagic_kappa_zero C h

/-- **Concrete special case (fully proved, no axioms):** for the
    trivial union composite, double-magic constituents force
    `κ_{ydA} = 0`. This is `doubleMagic_kappa_zero` specialised to
    `Composite.fromUnion`, where `ContentAdditive` is a real
    instance rather than an axiomatic typeclass field. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
theorem fromUnion_kappa_zero_of_double_magic
    (ydZ ydN : YoungDiagram)
    (hZ : isSelfConjugate ydZ) (hN : isSelfConjugate ydN) :
    kappa (Composite.fromUnion ydZ ydN).ydA = 0 :=
  kappa_zero_of_selfConj_constituents (Composite.fromUnion ydZ ydN) hZ hN

/-- **LR-rigidity proved for the trivial composite.** If both
    constituents are self-conjugate, then the trivial union composite
    is itself self-conjugate. This is `DoubleMagicConjecture.lr_rigidity`
    proved without axioms in the trivial case — the disjoint multiset
    union of two negation-symmetric multisets is negation-symmetric.

    The honest LR fusion produces a *richer* composite via the
    Littlewood–Richardson rule, but content additivity and
    self-conjugacy preservation hold at the union level too, giving
    a non-vacuous structural lower bound. -/
-- Ref: [leitner2026] conj:diagrammatic-double-magic-lr-fusion
theorem fromUnion_lr_rigidity
    (ydZ ydN : YoungDiagram)
    (h : IsDoubleMagic (Composite.fromUnion ydZ ydN)) :
    isSelfConjugate (Composite.fromUnion ydZ ydN).ydA :=
  unionDiagram_isSelfConjugate h.1.2 h.2.2

/-! ## §5  Downstream — double-magic ⇒ homological condensation -/

/-! ### 🛑 The "capstone" is gone (2026-08-31) — it never made the connection

Until 2026-08-31 this section ended with

```lean
theorem doubleMagic_implies_condensation
    [D : DoubleMagicConjecture] [ShellCondensationConjecture]
    (C : Composite) [ContentAdditive C]
    (hM : IsDoubleMagic C) (hL : C.ydA.n ∈ magicLadder) :
    InfinityVanishesAtPositiveQ C.ydA.n :=
  condensation_at_magic hL
```

described as *"the algebraic-geometry capstone connecting"* three conjectures.
Its body is `condensation_at_magic hL`, which needs `hL` and
`[ShellCondensationConjecture]` and nothing else: **`D`, `[ContentAdditive C]`
and `hM` are all unused.** The theorem is `condensation_at_magic` under another
name, with three decoy binders making it look like a chain.

The link it appeared to supply — from *"C is double-magic"* to
*"`C.ydA.n ∈ magicLadder`"* — is exactly what the removed
`magic_iff_double_magic` asserted, and that assertion is false: no observed
double-magic nucleus has a magic mass number (see the class docstring above).
So the chain cannot be closed by repairing the binders; the step it needs does
not hold.

Removed rather than re-stated. A caller wanting the real content applies
`condensation_at_magic` directly, which says what it does. Whether some *other*
route leads from double-magic constituents to shell condensation is open, and
naming a theorem after that route does not create it.

Bean `qou-z9ws`. -/

end QOU.Interactions.LRFusion
