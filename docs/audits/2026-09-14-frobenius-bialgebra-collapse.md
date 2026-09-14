# The bialgebra axiom is EXCLUDED, not open — a Frobenius–Hopf substrate that is also a bimonoid is the tensor unit

**Date** 2026-09-14 · **Beans** `qou-c64q` (parent) ·
**Branch** `claude/frobenius-bialgebra-collapse-2026-09-14`

## The claim

Earlier today `def:frobenius-hopf-substrate` gained the Hopf antipode axiom on
owner decision, and I recorded one thing as still open and *"the owner's
call"*: whether to also add the bialgebra (bimonoid) compatibility, without
which the substrate is not a Hopf monoid in Mathlib's sense and results like
`HopfObj.antipode_antipode` cannot reach it.

**That is not a decision. It is settled, and the answer is no.**

One of the four bimonoid axioms *on its own* — `Δ ∘ η = η ⊗ η`, Mathlib's
`CategoryTheory.BimonObj.one_comul` — collapses the definition to the tensor
unit. Sorry-free, `lean`-direct exit 0, `#print axioms` clean:

| theorem | statement |
|---|---|
| `comul_eq_of_one_comul` | `Δ = (λ_A)⁻¹ ≫ (η ▷ A)` — in elements, `Δ(x) = 1 ⊗ x` |
| `counit_comp_unit` | `ε ≫ η = 𝟙_A` — the identity on `A` factors through `𝟙_C` |
| `isoUnit` | with `η ≫ ε = 𝟙` (the second unit-side bimonoid axiom), `A ≅ 𝟙_C` |
| `not_one_comul_of_nontrivial` | contrapositive: `A` non-trivial ⟹ the bimonoid unit axiom fails |

[`QOU/QuantumObservableUniverse/FrobeniusBialgebraCollapse.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/FrobeniusBialgebraCollapse.lean).

## The mechanism

Three lines, and each step is one of the structure's own axioms:

1. **The Frobenius relation makes `Δ` a map of `A`-bimodules**, so `Δ` is
   determined by `Δ(1)`. Formally: expand `Δ = 𝟙_A ≫ Δ` through the left unit
   law, then substitute `frobenius_relation`.
2. **The bimonoid axiom sets `Δ(1) = 1 ⊗ 1`**, which is degenerate — a
   Frobenius copairing cannot be a pure tensor unless the object is
   one-dimensional. Substituting collapses step 1 to `Δ(x) = 1 ⊗ x`.
3. **The counit law finishes it.** `Δ ≫ (A ◁ ε) = (ρ_A)⁻¹` applied to the
   degenerate `Δ` reads `ε(x)·1 = x` for every `x`, i.e. `ε ≫ η = 𝟙_A`.

No braiding is used anywhere, which is why the statement holds over a bare
monoidal category. Note also that `one_comul` is the *only* bimonoid axiom
statable without a braiding — `mul_comul` needs `tensorμ` — so the collapse is
reachable at exactly the level this structure lives at.

## Why this is the expected state of affairs, not an alarm

**A finite-dimensional Hopf algebra *is* Frobenius — but its Frobenius
comultiplication is not its Hopf comultiplication.** Forcing the two to
coincide is what collapses, and that is a classical fact rather than a defect
in this framework.

`def:frobenius-hopf-substrate` axiom 3 fixes `Δ` as the Frobenius one. So the
substrate is a **Frobenius monoid carrying an antipode**, not a Hopf monoid,
and the name "Frobenius–Hopf" should be read that way.

## What this does and does not exclude

**Scope (b), a structural exclusion** in the sense of AGENTS.md §"Before
declaring refuted / ruled out": the invariant cited is the proved implication
above, not a numerical probe.

- **Excluded:** the bimonoid compatibility, for a `Δ` satisfying the Frobenius
  relation, on a non-trivial `A`.
- **Not excluded:** a Hopf structure on `A` borne by a **different**
  comultiplication. That is a separate object the corpus does not currently
  have, and nothing here argues against building one.
- **Not affected:** the antipode axiom added earlier today. It constrains `S`
  against `(μ, η, Δ, ε)` and does not require `Δ` to be a bialgebra
  comultiplication. `antipode_unique_of_left` stands.

## A consequence worth stating plainly

**The corpus has exactly one witness of `FrobeniusHopfData`, and it is
`A = 𝟙`** (`QOU.TrivialWitness.unitFrobHopf`). That was already true before
today. The theorems here do *not* show the axioms force triviality — they show
that *adding* the bimonoid unit axiom would. But they sharpen the standing
question: **is there a non-trivial `FrobeniusHopfData` in this corpus?**
Nothing currently exhibits one, so "the axioms are consistent" is established
only by the trivial object. That is a real gap, it is not closed here, and it
is worth a bean of its own rather than a sentence in this one.

## Verification

- `lean`-direct `-DautoImplicit=false -s 65536`, **exit 0, zero warnings**, on
  `FrobeniusBialgebraCollapse.lean` and on `AntipodeDetermined.lean` after its
  "still missing" section was corrected.
- `#print axioms` on all six declarations: **no `sorryAx`**. The two purely
  structural lemmas (`unitor_unit_mul`, `comul_eq_frobenius`) depend on **no
  axioms at all**; the four substantive ones on `[propext, Classical.choice,
  Quot.sound]`.
- `qa-sweep` on the block after the `authorNotes` update: **0 critical, 0
  major, 0 minor**.
