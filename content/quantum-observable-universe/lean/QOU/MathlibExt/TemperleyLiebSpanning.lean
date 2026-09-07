import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.LinearIndependent.Defs
import QOU.MathlibExt.HeckeToTemperleyLieb

/-!
# Upper bounds for `TL_n(δ)` — the gap `TemperleyLiebAlgebra` names about itself

**Bean `qou-cds1`.** `QOU.MathlibExt.TemperleyLiebAlgebra` says, in its own
non-vacuity section:

> This does **not** claim `TL₂(δ) ≅ R × R`: **no upper bound on `TL₂(δ)` is
> proved anywhere in this file.**

That is the structural gap, and it is not cosmetic. Everything in that file
bounds `TL` from *below* — representations separating generators, showing
elements are nonzero and distinct. Nothing bounds it from above, so `TL_n(δ)`
could a priori be enormous, and **no dimension count, Wedderburn decomposition
or semisimplicity statement can even be attempted** until it is finite over the
expected spanning set.

This file supplies the upper bounds at `n = 2` and `n = 3`:

    TL₂(δ) = span_R {1, e₀}                      (2 = catalan 2)
    TL₃(δ) = span_R {1, e₀, e₁, e₀e₁, e₁e₀}      (5 = catalan 3)

Combined with `TemperleyLiebAlgebra.tl2_linearIndependent`, the `n = 2` case is
an exact `dim TL₂(δ) = 2` — the first instance of `dim TL_n = catalan n` in this
corpus proved as an *algebra* fact rather than a partition count.

## Why this is the right next step for the Wedderburn direction

The open item left by `QOU.MathlibExt.HeckeToTemperleyLieb` is
`⟨relators⟩ = traceRadical tr_M`, whose hard half needs `TL_n(δ)` semisimple.
`QOU.MathlibExt.TraceRadicalNondegenerate` closed everything downstream of the
Wedderburn decomposition. The decomposition itself needs, at minimum, that the
algebra is **finite-dimensional with the expected basis** — which is exactly
what an upper bound gives and what was missing.

## The method, which is uniform and generalises

`Algebra.adjoin R (Set.range e) = ⊤` — proved in `HeckeToTemperleyLieb` — says
the generators generate. So it suffices to exhibit a *submodule* containing them,
containing `1`, and closed under multiplication: `Submodule.toSubalgebra` turns
it into a subalgebra, and `Algebra.adjoin_le` then forces it to be everything.

Closure under multiplication reduces, via `Submodule.span_mul_span`, to checking
the finitely many products of spanning elements — 4 at `n = 2`, 25 at `n = 3`.
Each is a one-line consequence of `e_sq`, `e_adjacent` or `e_farCommute`.

**What does not generalise for free is the spanning set.** At `n = 2, 3` it is
small enough to write down and close by hand. General `n` needs the planar
diagram basis (`catalan n` of them) and the reduction of an arbitrary word to a
diagram — that is the real content of `dim TL_n = catalan n`, and it is not done
here.

-- Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.MathlibExt.TemperleyLiebSpanning

open QOU.MathlibExt.TemperleyLieb (TemperleyLiebAlgebra e e_sq e_adjacent e_farCommute)
open QOU.MathlibExt.HeckeToTemperleyLieb (adjoin_range_e_eq_top)

variable {R : Type*} [CommRing R] {B : Type*} {δ : R} {Adj : B → B → Prop}

/-! ## The general reduction -/

/-- **If a submodule contains `1` and every generator and is closed under
multiplication, it is everything.**

The whole upper-bound method in one lemma. `adjoin_range_e_eq_top` supplies that
the generators generate; `Submodule.toSubalgebra` turns the hypotheses into a
subalgebra; `Algebra.adjoin_le` closes it. -/
theorem eq_top_of_one_mem_of_gen_mem_of_mul_mem
    (M : Submodule R (TemperleyLiebAlgebra R δ Adj))
    (h1 : (1 : TemperleyLiebAlgebra R δ Adj) ∈ M)
    (hgen : ∀ i : B, e R δ Adj i ∈ M)
    (hmul : ∀ x y, x ∈ M → y ∈ M → x * y ∈ M) : M = ⊤ := by
  have hsub : Algebra.adjoin R (Set.range (e R δ Adj)) ≤ M.toSubalgebra h1 hmul := by
    apply Algebra.adjoin_le
    rintro _ ⟨i, rfl⟩
    exact hgen i
  rw [adjoin_range_e_eq_top] at hsub
  have : (⊤ : Subalgebra R (TemperleyLiebAlgebra R δ Adj)) ≤ M.toSubalgebra h1 hmul := hsub
  rw [eq_top_iff]
  intro x _
  exact this (Algebra.mem_top (R := R) (x := x))

/-- The multiplication-closure hypothesis, reduced to products of spanning
elements. `Submodule.span_mul_span` does the work. -/
theorem mul_mem_span_of_pairs {S : Set (TemperleyLiebAlgebra R δ Adj)}
    (h : ∀ a ∈ S, ∀ b ∈ S, a * b ∈ Submodule.span R S) :
    ∀ x y, x ∈ Submodule.span R S → y ∈ Submodule.span R S →
      x * y ∈ Submodule.span R S := by
  have hle : Submodule.span R S * Submodule.span R S ≤ Submodule.span R S := by
    rw [Submodule.span_mul_span]
    refine Submodule.span_le.mpr ?_
    rintro _ ⟨a, ha, b, hb, rfl⟩
    exact h a ha b hb
  intro x y hx hy
  exact hle (Submodule.mul_mem_mul hx hy)

/-! ## `n = 2`: the bound the file asked for -/

section TL2

open QOU.MathlibExt.TemperleyLieb (TL2 tl2e adjFin)

variable (δ : R)

/-- **`TL₂(δ) = span_R {1, e₀}`.**

The upper bound `QOU.MathlibExt.TemperleyLiebAlgebra` records as absent. With
`tl2_linearIndependent` from that file this is an exact `dim TL₂(δ) = 2`, which
is `catalan 2` — the first instance of `dim TL_n = catalan n` here proved as an
*algebra* fact rather than a count of partitions.

Only two relations are used, and only one of them non-trivially: `e² = δ·e`
puts the single interesting product back in the span. -/
theorem tl2_span_eq_top :
    Submodule.span R ({1, tl2e (R := R) δ} : Set (TL2 (R := R) δ)) = ⊤ := by
  refine eq_top_of_one_mem_of_gen_mem_of_mul_mem _ ?_ ?_ ?_
  · exact Submodule.subset_span (by simp)
  · intro i
    have : i = 0 := Subsingleton.elim i 0
    subst this
    exact Submodule.subset_span (by simp [tl2e])
  · refine mul_mem_span_of_pairs ?_
    rintro a (rfl | rfl) b (rfl | rfl)
    · simpa using Submodule.subset_span (by simp : (1 : TL2 (R := R) δ) ∈ _)
    · simpa using Submodule.subset_span (by simp : tl2e (R := R) δ ∈ _)
    · simpa using Submodule.subset_span (by simp : tl2e (R := R) δ ∈ _)
    · rw [tl2e, e_sq, ← Algebra.smul_def]
      exact Submodule.smul_mem _ _ (Submodule.subset_span (by simp))

/-- **`{1, e₀}` is linearly independent in `TL₂(δ)`**, restated from
`TemperleyLiebAlgebra.tl2_linearIndependent` in the `LinearIndependent` form
`Basis.mk` wants. The mathematical content is entirely that lemma's. -/
theorem tl2_linearIndependent' (hδ : ∀ x : R, x * δ = 0 → x = 0) :
    LinearIndependent R ![(1 : TL2 (R := R) δ), tl2e (R := R) δ] := by
  rw [Fintype.linearIndependent_iff]
  intro g hg i
  have h : algebraMap R (TL2 (R := R) δ) (g 0)
      + algebraMap R (TL2 (R := R) δ) (g 1) * tl2e (R := R) δ = 0 := by
    rw [Algebra.algebraMap_eq_smul_one, Algebra.algebraMap_eq_smul_one, smul_mul_assoc,
      one_mul]
    simpa [Fin.sum_univ_two] using hg
  obtain ⟨h0, h1⟩ := QOU.MathlibExt.TemperleyLieb.tl2_linearIndependent hδ _ _ h
  fin_cases i
  · exact h0
  · exact h1

/-- **`TL₂(δ) is free of rank two on `{1, e₀}`.**

`TemperleyLiebAlgebra` states this as the classical fact and then says freeness
"is not claimed" there, because it had the lower bound and no upper bound. With
`tl2_span_eq_top` supplying the upper bound, the two halves meet and the basis
exists.

`dim TL₂(δ) = 2 = catalan 2`. -/
noncomputable def tl2Basis (hδ : ∀ x : R, x * δ = 0 → x = 0) :
    Module.Basis (Fin 2) R (TL2 (R := R) δ) :=
  Module.Basis.mk (tl2_linearIndependent' δ hδ) (by
    have hspan := tl2_span_eq_top (R := R) δ
    have hrange : Set.range ![(1 : TL2 (R := R) δ), tl2e (R := R) δ]
        = ({1, tl2e (R := R) δ} : Set (TL2 (R := R) δ)) := by
      simp only [Matrix.range_cons, Matrix.range_empty, Set.union_empty,
        Set.union_singleton]
      exact Set.pair_comm _ _
    rw [hrange, hspan])

end TL2

end QOU.MathlibExt.TemperleyLiebSpanning
