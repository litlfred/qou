# `def:frobenius-hopf-substrate` has no non-trivial model over a field

**Date** 2026-09-15 · **Beans** `qou-aawz` (stays open), `qou-c64q`, `qou-hmhw` ·
**Branch** `claude/frobenius-hopf-models-and-carriers-2026-09-15` · **PR** #7413

## The claim

Write `σ = η ≫ ε : 𝟙_C ⟶ 𝟙_C` for the scalar `ε(1)`.

In a preadditive monoidal category whose scalars `End(𝟙_C)` form a field, every
`QOU.FrobeniusHopfData` has `A` a **zero object** or a **retract of `𝟙_C`**.
Over `ModuleCat k` that is `dim A ≤ 1`.

`QOU.FrobeniusHopfData.dichotomy_of_scalars_field`, sorry-free,
`#print axioms` = `[propext, Classical.choice, Quot.sound]`, in
[`FrobeniusHopfModelDichotomy.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/FrobeniusHopfModelDichotomy.lean).

## What it supersedes, and it is my own claim being corrected

PR #7405 (merged 2026-09-14) proved `ε(1)·x = ε(x)·1` with no hypothesis, and
read off: *a non-trivial substrate has a non-unital counit*. That is true. What
it left standing — in its own body, in bean `qou-aawz`, and in the block's
`authorNotes` — was that a non-unital counit might be the **escape**, i.e. that
a non-trivial model could live in that corner.

**It cannot, over a field.** The same identity, pushed the other way, closes the
corner: a non-trivial model would need `ε(1)` to be neither invertible nor zero,
and a field has no such element. The 2026-09-15 wording *"any non-trivial
witness must have `ε(1) ≠ 1`"* understates the constraint by describing the
complement of one point when the admissible set is empty.

**What that contaminated.** The weaker reading is repeated in three places, all
of which this PR corrects or annotates: the `qou-aawz` body, the fourth
`authorNotes` caveat on `frobenius-hopf-substrate.ts`, and the leading section
of [`2026-09-14-frobenius-bialgebra-collapse.md`](2026-09-14-frobenius-bialgebra-collapse.md).
The *theorems* in #7405 are untouched — only the interpretive sentence attached
to them was too weak.

## The proof, in five steps

| step | statement | spends |
|---|---|---|
| 1 | `Δ ≫ (A ◁ (ε ≫ η)) ≫ μ = 𝟙_A` | right counit law, right unit law — **no antipode** |
| 2 | `𝟙_A` factors through a map carrying `σ` in the middle | step 1 + `scalar_id_eq_counit_unit` |
| 3 | `σ` invertible ⟹ `ε ≫ η` invertible ⟹ `A` retract of `𝟙_C` | whiskering preserves iso |
| 4 | `σ = 0` ⟹ `𝟙_A = 0` ⟹ `A` is a zero object | `MonoidalPreadditive` |
| 5 | scalars a field ⟹ 3 or 4, no third case | — |

Step 1 is worth isolating: it holds of **any** Frobenius object whatever its
`S`, so the antipode enters only at step 2, through `scalar_id_eq_counit_unit`.
The whole collapse is therefore attributable to the 2026-09-14 axiom addition
plus the Frobenius relation, and to nothing else.

Step 5 takes the field property as the hypothesis `∀ σ, σ = 0 ∨ IsIso σ` rather
than importing a field instance, so the theorem applies wherever that
disjunction holds — `ModuleCat k`, `FdRep k G`, any `k`-linear abelian monoidal
category with simple unit.

## The probe tests the SHARP form

The weak prediction is *"the standard antipode `g ↦ g⁻¹` fails on `k[G]`"*. The
theorem makes a stronger one: for `|G| > 1` **no linear map whatever** satisfies
the left antipode axiom against the Frobenius comultiplication. That is the
falsifiable statement, and it is what
[`frobenius_hopf_no_nontrivial_model_probe.py`](../../computations/probes/frobenius_hopf_no_nontrivial_model_probe.py)
tests: it builds the full `|G|²` system

```
for all g, m:   Σ_h M[gh][m h]  =  δ_{g,e} · δ_{m,e}
```

and decides consistency by exact Gaussian elimination over ℚ.

| G | \|G\| | system | expected |
|---|---|---|---|
| Z/1 | 1 | CONSISTENT | CONSISTENT ✓ |
| Z/2 | 2 | INCONSISTENT | INCONSISTENT ✓ |
| Z/3 | 3 | INCONSISTENT | INCONSISTENT ✓ |
| Z/4 | 4 | INCONSISTENT | INCONSISTENT ✓ |
| S₃ | 6 | INCONSISTENT | INCONSISTENT ✓ |

5/5. It also reports *why* the standard antipode fails rather than only that it
does: the Frobenius `Δ(1) = Σ_h h ⊗ h⁻¹`, so `(S * id)(1) = Σ_h h⁻²`, which is
`1` only for the trivial group.

Arithmetic is exact — integer group-algebra coefficients, `fractions.Fraction`
elimination, **no float anywhere** in the file. It emits no witness because it
records a structural yes/no about a linear system, not a numeric quantity
anything downstream re-derives.

## Scope — (b), a structural exclusion, with two stated limits

Per AGENTS.md §"Before declaring refuted": the invariant cited is a proved
implication, not a numerical probe.

**Excluded:** a non-trivial `FrobeniusHopfData` in any preadditive monoidal
category whose scalars form a field.

**NOT excluded, and these are not hedges:**

1. **A bare monoidal category.** The zero branch needs `MonoidalPreadditive` —
   over a bare monoidal category `σ = 0` is not statable and this proves nothing
   there. Whether such a category admits a non-trivial model is **open**, and is
   why `qou-aawz` stays open rather than being closed.
2. **A retract of `𝟙_C` need not be `𝟙_C`.** It is when the unit is
   indecomposable. "Retract of the unit" is the honest general conclusion.
3. **A Hopf structure on `A` borne by a *different* comultiplication.** That is
   a separate object the corpus does not have, and nothing here argues against
   building one.

## Why this is the expected state of affairs

A finite-dimensional Hopf algebra **is** Frobenius, but its Frobenius
comultiplication is **not** its Hopf comultiplication. Axiom 3 of
`def:frobenius-hopf-substrate` pins `Δ` to the Frobenius one; the antipode axiom
added on 2026-09-14 then demands an antipode against *that* `Δ`. The two are
being forced to coincide, and this is the exact price.

So the finding is about the **definition's shape**, not about the framework's
mathematics being wrong. The substrate is a Frobenius monoid carrying an
antipode — and over a field, only the trivial one is.

## The decision this hands the author

Stated as options rather than a recommendation dressed as a finding.

- **Accept and record.** The substrate is trivial over a field; the framework's
  `A` lives in a non-linear monoidal category, or the linear reading of
  `def:frobenius-hopf-substrate` was never the intended one. Cost: one
  `authorNotes` entry. Risk: the categorical Lagrangian consumes
  `FrobeniusHopfData`, so anything that instantiates it over `ModuleCat` is
  instantiating a trivial object.
- **Drop the antipode axiom.** Return `S` to free data. Cost: reverts #7369, and
  `S² = id` goes back to being *independent* rather than open. Risk: the
  definition again names a morphism it constrains with nothing, which is the
  defect #7369 was opened to fix.
- **Split the comultiplication.** Carry a Frobenius `Δ_F` and a Hopf `Δ_H`
  separately, with the antipode against `Δ_H` and the Frobenius relation against
  `Δ_F`. Cost: a real re-definition, new fields, every consumer re-checked.
  Risk: largest blast radius of the three; gain: it is what the classical
  mathematics actually says.

**Default if nothing is decided:** nothing changes. The theorems stand as
recorded facts, `qou-aawz` stays open for the non-linear case, and the
definition keeps a shape whose only linear model is trivial.
