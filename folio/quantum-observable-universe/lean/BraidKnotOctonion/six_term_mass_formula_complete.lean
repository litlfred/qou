import Mathlib.Tactic

/-!
# QOU.BraidKnot.six_term_mass_formula_complete — six-term unified mass formula

**Conjecture** ([`conj:six-term-mass-formula-complete`](../../../mass-theory/six-term-mass-formula-complete.md)).

The `.md` states that the categorical mass of a vortex `ϱ` is the sum of six
**named, concrete** terms:

```
  𝔪(ϱ) = |tr_M(T_w)|                                            (Term 1)
       + Σ_{i=0}^{n-2} Φ_q(|V̂_i^full|)                          (Term 2)
       + z² Σ_{i<j} Φ_q(|V̂_i^full V̂_j^full|)                    (Term 3)
       + m_e · τ(C_{dim_q})                                     (Term 4)
       + a_K · 𝒞_K                                              (Term 5)
       + Σ_{ℓ≥2} Res_{q=ζ_ℓ}[·] / (q₀ − ζ_ℓ)                    (Term 6)
```

and adds that *"every term evaluates uniquely from the canonical braid word
and substrate parameter."*

## 2026-09-02 — this file encodes the SHAPE, not the formula

`SixTermMassFormulaContext` carried `term1 … term6` and `cat_mass` as seven
opaque elements of `R` plus a field `claim_six_term_sum` asserting the sum
identity, and `six_term_mass_formula_complete` returned that field. Removing
the projection is not the interesting part; the interesting part is what is
left when you do.

**None of the six terms is encoded.** Nothing in this file mentions the Markov
trace, `Φ_q`, the `V̂_i^full`, `z`, `m_e`, `τ(C_{dim_q})`, `a_K`, `𝒞_K`, or a
cyclotomic residue. With the terms opaque, `cat_mass = term1 + ⋯ + term6` is
not the six-term mass formula — it is the statement that some element is a sum
of six elements, which is the *definition* of a six-way additive split and
holds of every quantity that can be written as one.

So this is not a case where naming the claim over parameters (AGENTS.md §1a
disposition 3) would recover the content, as it did for
`QOU.Archimedean.knot_operator_selection`. There, the parameters were the
objects the claim is about. Here, naming `sixTermSplit m t₁ … t₆` names a
schema, not the proposition.

Both facts about that schema are **proved** below rather than asserted:

* `sixTermSplit_sum` — for *any* six terms a mass satisfying it exists (take
  the sum). So the schema constrains nothing whatever about the terms.
* `not_sixTermSplit_of_independent` — it is refutable when `cat_mass` is
  chosen independently (`1 ≠ 0 + ⋯ + 0`). So it constrains `cat_mass`, and
  only `cat_mass`.

Together: the schema pins one element to five additions and says nothing about
the mathematics the `.md` describes. That is also why a `sorry` here would be
wrong — it would read as "true, not yet proved" over a statement that is
refutable at free data.

## What is unencoded, term by term

| term | `.md` content | what encoding it needs |
|---|---|---|
| 1 | `\|tr_M(T_w)\|` | the Markov trace on the canonical Hecke normal form |
| 2 | `Σ_i Φ_q(\|V̂_i^full\|)` | `Φ_q` (Faddeev) and the full vertex operators |
| 3 | `z² Σ_{i<j} Φ_q(\|V̂_i V̂_j\|)` | the same, plus the Markov parameter `z` |
| 4 | `m_e · τ(C_{dim_q})` | the fibre functor `τ` on the `dim_q` Casimir |
| 5 | `a_K · 𝒞_K` | the chirality coefficient and knot invariant |
| 6 | `Σ_{ℓ≥2} Res_{q=ζ_ℓ}[·]/(q₀−ζ_ℓ)` | the cyclotomic pole expansion |

The `.md`'s further claims — that every term evaluates uniquely from the braid
word, that Markov-trace invariance is enforced, and that the breakdown locates
the origin of isospin and parity violation — have no encoding here either.

Bean `qou-z9ws`.
-/

namespace QOU.BraidKnot

/-- **A six-way additive split**: `m = t₁ + t₂ + t₃ + t₄ + t₅ + t₆`.

This is the *shape* of the manuscript's six-term formula with all six terms
left opaque. It is named here so the distance between the shape and the claim
is visible in the Lean rather than only in prose. See
`sixTermSplit_sum` and `not_sixTermSplit_of_independent` for exactly how much
it constrains. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/six-term-mass-formula-complete.md
def sixTermSplit {R : Type*} [AddCommMonoid R] (m t₁ t₂ t₃ t₄ t₅ t₆ : R) : Prop :=
  m = t₁ + t₂ + t₃ + t₄ + t₅ + t₆

/-- **The schema constrains nothing about the terms.** For *any* six elements
there is a mass satisfying the split — namely their sum. -/
theorem sixTermSplit_sum {R : Type*} [AddCommMonoid R] (t₁ t₂ t₃ t₄ t₅ t₆ : R) :
    sixTermSplit (t₁ + t₂ + t₃ + t₄ + t₅ + t₆) t₁ t₂ t₃ t₄ t₅ t₆ :=
  rfl

/-- **And it does constrain the mass.** Chosen independently of the terms, the
split fails — so the schema pins `m` to the sum and says nothing else.

Recorded as a theorem because it is also the reason a `sorry` would be the
wrong disposition here: it would read as "true, not yet proved" over a
statement refutable at free data. -/
theorem not_sixTermSplit_of_independent :
    ¬ sixTermSplit (1 : ℕ) 0 0 0 0 0 0 := by
  simp [sixTermSplit]

/-- **Six-term unified mass formula** ([`conj:six-term-mass-formula-complete`]).

The claim of the block, as a proposition over caller-supplied data — **named,
not asserted**.

Read the module docstring before using it: with `t₁ … t₆` opaque this states
only that `m` is their sum, and the six terms the `.md` names (`|tr_M(T_w)|`,
`Σ Φ_q(|V̂_i|)`, …) are **not encoded anywhere in this file**. A caller who has
actually constructed the six terms supplies them here; what they get is the
additive bookkeeping, not the manuscript's derivation. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/six-term-mass-formula-complete.md
def six_term_mass_formula_complete {R : Type*} [AddCommMonoid R]
    (cat_mass term1 term2 term3 term4 term5 term6 : R) : Prop :=
  sixTermSplit cat_mass term1 term2 term3 term4 term5 term6

end QOU.BraidKnot
