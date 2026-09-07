import QOU.BraidKnot.PartitionLexWellFounded
import QOU.BraidKnot.DominanceWellFounded
import Mathlib.Data.Sigma.Lex

/-!
# 3.14's induction measure, both axes combined

`PartitionLexWellFounded` gives the outer axis (lex across shapes), `DominanceWellFounded`
the inner one (dominance within a shape).  Mathas' Lemma 3.14 inducts on **both at once**:
case (i) drops the shape in lex order, case (ii) keeps the shape and moves up dominance.
So the measure it actually runs on is the **lexicographic product**, and that is what this
file builds and proves well-founded.

    murphyLex n  :  Σ μ : PartOf n, Tabloid μ.1   →   … → Prop

with `⟨μ, a⟩ > ⟨ν, b⟩` when `μ >ₗ ν`, or `μ = ν` and `a` strictly dominates `b`.

## Why a sigma, and why that is not incidental

The tableau type **depends on the shape** (`Specht.Tabloid μ`), so the pair cannot be a
product — it is a `Sigma`.  `Sigma.Lex`'s `right` constructor is stated for two elements of
the *same* fibre, which is exactly what case (ii) needs and means no transport appears
anywhere in the argument.

## The well-foundedness route

Mathlib's `Sigma.Lex` carries `mono`/`decidable`/`swap` lemmas but, at the imports this
corpus has, **no well-foundedness lemma** (checked by enumerating the environment, not by
grepping source — a Mathlib source grep is worthless here, see
[`scripts/lean-probes/`](../../../../../scripts/lean-probes/README.md)).

So the proof goes the same way as both axes did: `Sigma.Lex` of two strict orders is a
strict order, the sigma of a `Fintype` with `Fintype` fibres is finite, and a strict order
on a finite type is well-founded.  The transitivity is a four-case analysis and the
irreflexivity a two-case one; neither needs the fibres to be related across shapes.

## Scope — this makes 3.14 STATABLE, not proved

With this, an induction proving 3.14 can be written down: `murphyLex_induction` is the
recursor it would use. **The mathematics of the Garnir step is untouched** — that is the
content of the lemma and remains the arc's open problem. What is settled is that the
induction it needs terminates.

> **🛑 RESOLVED — read this, not the doubt it replaced.**  The doubt was: the corpus retired a
> tabloid-dominance measure for Garnir straightening at `q = 1` on an exact-arithmetic
> counterexample (μ=(3,2), t=[[1,2,3],[5,4]]), concluding *"Garnir produces terms whose
> tabloids are dominance-incomparable to `{t}`"*, hence *"no tabloid-level measure orders
> them"* (`SpechtStandardBasisCore.lean` §"Measure correction (2026-07-07)").  This axis is a
> tabloid-level measure, so the doubt was real.
>
> **Mathas' own proof of 3.14 settles it, and in this axis's favour.**  Its case (ii) step is
>
>     m_st = T*_{d(s)} h T_w + Σ_{v ▷ t} r_v m_sv
>
> — the same-shape terms are indexed **by the dominance relation itself**, so they cannot be
> incomparable, and the relation is `▷`, **strict** (Corollary 3.15 states the same:
> *"ν = λ, u = s and v ▷ t"*).  3.14's *statement* uses the loose `⊵`; its *induction* steps
> on `▷`.  `domGtOn` is exactly that strict part, and `domGtOn_induction`'s direction —
> hypothesis available for strictly-dominating tableaux — is what *"by induction on `t`"*
> needs.
>
> **Why the `q = 1` counterexample does not carry, sharper than "different step":** there the
> terms fall out of a coset sum and their tabloids land where they land, so incomparability
> is possible; here the term set is *defined* as those `v` dominating `t`.  Different
> mechanisms, one of which cannot produce an incomparable term at all.  `colWordNum` remains
> the right measure for the `q = 1` polytabloid straightening and is not needed here.
>
> Full derivation and the two remaining 3.14 inputs it identifies (3.12, and **Corollary 3.8**,
> not previously named on this arc):
> [`docs/audits/2026-09-06-tabloid-dominance-vs-the-column-word-measure.md`](../../../../../docs/audits/2026-09-06-tabloid-dominance-vs-the-column-word-measure.md).
-/

namespace QOU.BraidKnot.MurphyInductionMeasure

open QOU.BraidKnot.PartitionLexWellFounded QOU.BraidKnot.DominanceWellFounded

/-- A shape of size `n` together with a tabloid of that shape — the object 3.14's double
induction runs on. -/
abbrev ShapedTabloid (n : ℕ) := Σ μ : PartOf n, Specht.Tabloid μ.1

/-- **3.14's induction measure**: lex on shapes, dominance inside a shape. -/
def murphyLex (n : ℕ) : ShapedTabloid n → ShapedTabloid n → Prop :=
  Sigma.Lex (lexGtOn n) (fun μ => domGtOn (μ := μ.1))

instance instIsIrreflMurphyLex (n : ℕ) : IsIrrefl (ShapedTabloid n) (murphyLex n) := by
  refine ⟨fun x hx => ?_⟩
  cases hx with
  | left _ _ h => exact (instIsIrreflLexGtOn n).irrefl _ h
  | right _ _ h => exact (instIsIrreflDomGtOn).irrefl _ h

instance instIsTransMurphyLex (n : ℕ) : IsTrans (ShapedTabloid n) (murphyLex n) := by
  refine ⟨fun x y z hxy hyz => ?_⟩
  cases hxy with
  | left a b hab =>
      cases hyz with
      | left _ c hbc => exact Sigma.Lex.left _ _ ((instIsTransLexGtOn n).trans _ _ _ hab hbc)
      | right _ _ _ => exact Sigma.Lex.left _ _ hab
  | right a b hab =>
      cases hyz with
      | left _ c hbc => exact Sigma.Lex.left _ _ hbc
      | right _ c hbc =>
          exact Sigma.Lex.right _ _ ((instIsTransDomGtOn).trans _ _ _ hab hbc)

/-- **Mathas 3.14's induction measure is well-founded.**  A strict order on a finite type;
the type is finite because there are finitely many shapes of size `n` and finitely many
tabloids of each. -/
theorem murphyLex_wellFounded (n : ℕ) : WellFounded (murphyLex n) :=
  Finite.wellFounded_of_trans_of_irrefl _

instance instIsWellFoundedMurphyLex (n : ℕ) :
    IsWellFounded (ShapedTabloid n) (murphyLex n) :=
  ⟨murphyLex_wellFounded n⟩

/-- **The recursor an induction proving 3.14 would use.**  To prove `C` at a
shape-and-tabloid, it suffices to prove it given `C` at every pair that is either of
lex-greater shape, or of the same shape with a strictly dominating tabloid — which are
exactly 3.14's cases (i) and (ii). -/
theorem murphyLex_induction {n : ℕ} {C : ShapedTabloid n → Prop}
    (ih : ∀ x, (∀ y, murphyLex n y x → C y) → C x) (x : ShapedTabloid n) : C x := by
  refine (murphyLex_wellFounded n).induction (C := fun z => C z) x ?_
  intro z hz
  exact ih z fun y hy => hz y hy

end QOU.BraidKnot.MurphyInductionMeasure
