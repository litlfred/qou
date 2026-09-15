# Both unit-side bimonoid axioms are EXCLUDED — and one of them is excluded by the antipode axiom added the same day

**Date** 2026-09-14, extended 2026-09-15 · **Beans** `qou-c64q` (parent),
`qou-aawz` · **Branch** `claude/frobenius-bialgebra-collapse-2026-09-14`

## 🛑 The stronger result, found after the rest of this document was written

The sections below prove that adding the bimonoid *comultiplication-side* unit
axiom `Δ ∘ η = η ⊗ η` collapses the substrate. That was the question I set out
to answer. **The sharper result is that the antipode axiom added earlier the
same day, with no extra hypothesis at all, already forces**

    ε(1) · x  =  ε(x) · 1     for every x

— `QOU.FrobeniusHopfData.scalar_id_eq_counit_unit`, sorry-free, `#print axioms`
= `[propext, Quot.sound]`, no `Classical.choice`. Formally:

    ε ≫ η  =  (λ_A)⁻¹ ≫ ((η ≫ ε) ▷ A) ≫ (λ_A).hom

**The mechanism is two steps.** The Frobenius relation makes `Δ` a right
`A`-module map, so the convolution `S * id` is left multiplication by the single
element `(S * id)(1)` — `convolution_eq_left_mul`, which uses **no antipode
axiom at all** and is true whatever `S` is. Then `antipode_left` says that same
convolution is `ε(-)·1`. Evaluating at `1` identifies the element as `ε(1)·1`.

**Consequence, and this is what reframes the whole file.** `ε(1) = 1` is
Mathlib's `BimonObj.one_counit` — a *normalisation*, assumed without comment of
every bialgebra and every Hopf algebra there is. Given it:

| theorem | statement |
|---|---|
| `counit_comp_unit_of_unital` | `ε ≫ η = 𝟙_A` |
| `isoUnitOfUnital` | `A ≅ 𝟙_C` |
| `counit_not_unital_of_nontrivial` | contrapositive: a non-trivial substrate has a **non-unital counit** |

So the picture is not "one exotic compatibility is excluded". It is:

| bimonoid axiom (unit side) | in elements | excluded by |
|---|---|---|
| `one_comul` : `η ≫ Δ = (λ_𝟙)⁻¹ ≫ (η ⊗ η)` | `Δ(1) = 1 ⊗ 1` | `not_one_comul_of_nontrivial` (below) |
| `one_counit` : `η ≫ ε = 𝟙_𝟙` | `ε(1) = 1` | `counit_not_unital_of_nontrivial` (new) |

A non-trivial `FrobeniusHopfData` satisfies **neither**. The other two bimonoid
axioms need a braiding to state and are not addressed here.

**Scope, and it is load-bearing.** `ε(1) = 1` is **not** a field of
`FrobeniusHopfData` and nothing here supplies it. This is therefore **not** a
proof that the current axioms are inconsistent, nor that `A = 𝟙_C`. What is
proved is the identity above and its contrapositive. `qou-aawz` asked for
exactly one of two outcomes — a non-trivial witness, or a proof that the current
axioms already force `A = 𝟙`. **This is neither**; it is a third thing, and it
narrows the first: any non-trivial witness must have `ε(1) ≠ 1`, which rules out
every textbook Frobenius algebra one would reach for first. That bean stays
open.

**What it means for the 2026-09-14 axiom addition.** The owner's decision A
(add the Hopf antipode condition) is not neutral with respect to the rest of the
definition: it is what excludes counit-unitality. Before it, `S` was free data
and nothing of the kind followed. Whether the corpus wants a substrate whose
counit is non-unital is an owner question, recorded in `qou-aawz`; nothing here
decides it, and nothing here is a reason to revert the axiom.

## The claim (the bimonoid half, which is what prompted the file)

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
that *adding* either unit-side bimonoid axiom would. But they sharpen the
standing question: **is there a non-trivial `FrobeniusHopfData` in this
corpus?** Nothing currently exhibits one, so "the axioms are consistent" is
established only by the trivial object. Bean `qou-aawz`, still open.

The leading section narrows what such a witness could be: it must have
`ε(1) ≠ 1`. The candidate `qou-aawz` names — a group algebra `k[G]` with the
Frobenius (dual-basis) comultiplication and the standard antipode `g ↦ g⁻¹` —
has `ε(1) = 1` under the usual normalisation `ε(Σ a_g g) = a_e`, so **by the
theorem above it cannot satisfy `antipode_left` unless `|G| = 1`**. A hand check
agrees and shows why: the Frobenius `Δ(1) = Σ_h h ⊗ h⁻¹`, so
`(S * id)(1) = Σ_h S(h)·h⁻¹ = Σ_h h⁻²`, which is `1` only for the trivial group.
Rescaling `ε` by a constant `c` moves `ε(1)` off `1` and is the only visible
escape, at the cost of `ε` no longer being a counit in the normalised sense —
which is precisely the corner the theorem says a non-trivial witness has to sit
in. That is a concrete prediction about the first object anyone would try, and
it is the cheapest available test of the leading result.

## Verification

- `lean`-direct `-DautoImplicit=false -s 65536`, **exit 0, zero warnings**, on
  `FrobeniusBialgebraCollapse.lean` and on `AntipodeDetermined.lean` after its
  "still missing" section was corrected. Run against a hardlinked shadow of the
  QOU olean tree carrying a freshly built `CategoricalFoundations.olean`: the
  committed one predates the antipode-field addition, and against it the file
  reports eight errors that are entirely about the stale olean (`Invalid field
  'one_mul'`, `'comul_counit'`, `'mul_assoc'`, `'antipode_left'`).
- `#print axioms` on all **thirteen** declarations: **no `sorryAx`**. Three
  purely structural lemmas (`unitor_unit_mul`, `unitor_unit_mul'`,
  `comul_eq_frobenius`) depend on **no axioms at all**; the four bimonoid-half
  results on `[propext, Classical.choice, Quot.sound]`; the six antipode-half
  results on `[propext, Quot.sound]` — no choice.
- `qa-sweep` on the block after the `authorNotes` update: **0 critical, 0
  major, 0 minor**.
