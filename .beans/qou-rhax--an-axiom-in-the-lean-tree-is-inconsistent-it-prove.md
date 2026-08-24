---
# qou-rhax
title: 'An axiom in the Lean tree is inconsistent — rh_iff_persistence_axiom proves False'
status: todo
type: task
priority: high
created_at: 2026-08-22T05:45:00Z
updated_at: 2026-08-22T05:45:00Z
---

Found by `agent:p01` on the stochastic-mechanics trap-drain; **confirmed by
reading the source** in the coordinating session. This is the most severe
class of defect the corpus admits: an axiom from which `False` follows.

## The derivation, in four lines

`stochastic-mechanics/macroscopic-stability-equivalence.lean`:

```lean
def RiemannHypothesis (ζ : ℂ → ℂ) : Prop :=
  ∀ (s : ℂ), 0 < s.re → s.re < 1 → ζ s = 0 → s.re = 1/2          -- line 44

def SpectralPersistence (spectral_limit : ℕ → Fin 8 → R_q) : Prop :=
  (∀ (n : ℕ) (i : Fin 8), spectral_limit n i = 1/2) →
    ∀ (i : Fin 8), spectral_limit 0 i = 1/2                        -- line 52

axiom rh_iff_persistence_axiom :
  ∀ ζ spectral_limit, RiemannHypothesis ζ ↔ SpectralPersistence spectral_limit
```

1. **`SpectralPersistence f` is a tautology for every `f`** — inhabited by
   `fun h i => h 0 i`. It says "if every level is ½ then level 0 is ½",
   which is instantiation, not persistence.
2. The axiom is universally quantified over **both** arguments, so it gives
   `RiemannHypothesis ζ ↔ True` for **every** `ζ`, hence
   `RiemannHypothesis ζ` for every `ζ`.
3. Take `ζ := fun _ => 0` and `s := (1/4 : ℂ)`. Then `0 < 1/4`, `1/4 < 1`,
   and `ζ s = 0`, so the definition forces `1/4 = 1/2`.
4. `False`.

## Blast radius: contained, and that is the only good news

`grep -rln` over every `.lean` in the tree: **the file references its own
names and nothing else does.** Nothing downstream inherits the
inconsistency today. But an axiom that proves `False` makes every
`#print axioms` result in that file meaningless, and if anything ever
imports it the whole library becomes unsound.

## Two aggravating details

**The caption attributes it to a paper that does not say it.** The axiom is
headed *"**External axiom (Weil 1948 explicit formula):** RH ↔ spectral
persistence"*. Weil's explicit formula is a duality between zeros and prime
powers; it is not an equivalence between RH and the statement above, and no
formulation of it makes RH equivalent to a proposition with no free
occurrence of ζ. The citation is what makes the axiom look load-bearing
rather than arbitrary.

**The "theorem" built on it is two axiom projections.**
`macroscopic_stability_equivalence` (line 99) is
`⟨macroscopic_iff_rh_axiom ψ ζ, rh_iff_persistence_axiom ζ spectral_limit⟩`.
It asserts a conjunction of two axioms and proves nothing. Under Strict Lean
Discipline §7 — *"No axiom/class may substitute for a proof … Creating
`axiom myResult : P` and then consuming it downstream is NOT proving `P`"* —
that is the pattern by name.

## What would close this

The fix is **not** to weaken the axiom until it is consistent, and **not**
to delete `SpectralPersistence` and keep the equivalence. Either:

1. **State `SpectralPersistence` so that it has content** — the docstring
   describes a genuine limit statement ("given `q_n → 1`, if the Reeb
   eigenvalues at each `q_n` satisfy `Re(ρ_i) = ½`, then the limiting
   spectral data also satisfies it"), which is a claim about a limit the
   type never mentions. Formalise that, and the axiom stops being vacuous
   on the right-hand side; then re-examine whether the equivalence is
   defensible at all.
2. **Or demote the whole file to a conjecture carrier** — a content-bearing
   `class` with no instance, per §3b. The honest state of "RH ↔ our spectral
   condition" is *open*, not axiomatised.

Either way the Weil attribution must go or be replaced with something that
actually states the claim.

## Note on the sibling that got this right

`ClassicalRiemannHypothesis.lean`, flagged clean in the same batch, is the
model: a content-bearing class, **no instance**, and a removed axiom
recorded in its docstring. Two files in one chapter, opposite dispositions.
