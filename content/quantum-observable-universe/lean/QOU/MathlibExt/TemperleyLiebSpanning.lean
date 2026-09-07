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

/-! ## `n = 3`: the same method, one relation more

`TL₃(δ)` is where the adjacency relation `e_i e_j e_i = e_i` first has anything
to say — at `n = 2` there is no adjacent pair. The spanning set grows from `2` to
`5`, and closure is 25 products rather than 4, each still a one-line consequence
of `e_sq`, `e_adjacent`. The two reduction lemmas above are reused unchanged,
which is the point of stating them generically.
-/

section TL3

open QOU.MathlibExt.TemperleyLieb (adjFin)

variable (δ : R)

/-- `TL₃(δ)`: two generators, and they are adjacent. -/
abbrev TL3 := TemperleyLiebAlgebra R δ (adjFin (n := 2))

noncomputable abbrev a3 : TL3 (R := R) δ := e R δ (adjFin (n := 2)) 0
noncomputable abbrev b3 : TL3 (R := R) δ := e R δ (adjFin (n := 2)) 1

theorem adj01 : adjFin (0 : Fin 2) 1 := by decide
theorem adj10 : adjFin (1 : Fin 2) 0 := by decide

theorem aba : a3 (R := R) δ * b3 δ * a3 δ = a3 δ := e_adjacent adj01
theorem bab : b3 (R := R) δ * a3 δ * b3 δ = b3 δ := e_adjacent adj10
theorem asq : a3 (R := R) δ * a3 δ = algebraMap R (TL3 (R := R) δ) δ * a3 δ := e_sq 0
theorem bsq : b3 (R := R) δ * b3 δ = algebraMap R (TL3 (R := R) δ) δ * b3 δ := e_sq 1

-- the two generators exhaust Fin 2
theorem gens (i : Fin 2) : e R δ (adjFin (n := 2)) i = a3 (R := R) δ ∨
    e R δ (adjFin (n := 2)) i = b3 (R := R) δ := by
  fin_cases i
  · exact Or.inl rfl
  · exact Or.inr rfl

/-- **`TL₃(δ) = span_R {1, e₀, e₁, e₀e₁, e₁e₀}`** — so `dim TL₃(δ) ≤ 5 = catalan 3`.

🛑 **This is the upper bound only; freeness is NOT claimed at `n = 3`.** Unlike
`n = 2`, this corpus has no matching lower bound: `TemperleyLiebAlgebra`'s
`tl3Fam` representation lands in `2 × 2` matrices, a `4`-dimensional target, so
it *cannot* witness linear independence of five elements however it is chosen.
Establishing `dim TL₃ = 5` needs a faithful representation of dimension at least
five, which is not here.

The 25 products, for the reader checking the case list is complete: with
`A = e₀`, `B = e₁`, the interesting ones are `A(BA) = A`, `B(AB) = B`,
`(AB)(AB) = AB`, `(BA)(BA) = BA` (adjacency), `(AB)(BA) = δ·A`,
`(BA)(AB) = δ·B` (loop then adjacency), and the rest are a loop relation or an
identity. -/
theorem tl3_span_eq_top :
    Submodule.span R
        ({1, a3 (R := R) δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ} : Set (TL3 (R := R) δ)) = ⊤ := by
  have hAA : a3 (R := R) δ * a3 δ = δ • a3 δ := by rw [asq, ← Algebra.smul_def]
  have hBB : b3 (R := R) δ * b3 δ = δ • b3 δ := by rw [bsq, ← Algebra.smul_def]
  have hABA := aba (R := R) δ
  have hBAB := bab (R := R) δ
  refine eq_top_of_one_mem_of_gen_mem_of_mul_mem _
    (Submodule.subset_span (by simp)) ?_ ?_
  · intro i
    fin_cases i
    · exact Submodule.subset_span (by simp)
    · exact Submodule.subset_span (by simp)
  refine mul_mem_span_of_pairs ?_
  have m1 : (1 : TL3 (R := R) δ) ∈ Submodule.span R ({1, a3 (R := R) δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ} : Set (TL3 (R := R) δ)) :=
    Submodule.subset_span (by simp)
  have mA : a3 (R := R) δ ∈ Submodule.span R ({1, a3 (R := R) δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ} : Set (TL3 (R := R) δ)) :=
    Submodule.subset_span (by simp)
  have mB : b3 (R := R) δ ∈ Submodule.span R ({1, a3 (R := R) δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ} : Set (TL3 (R := R) δ)) :=
    Submodule.subset_span (by simp)
  have mAB : a3 (R := R) δ * b3 δ ∈ Submodule.span R ({1, a3 (R := R) δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ} : Set (TL3 (R := R) δ)) :=
    Submodule.subset_span (by simp)
  have mBA : b3 (R := R) δ * a3 δ ∈ Submodule.span R ({1, a3 (R := R) δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ} : Set (TL3 (R := R) δ)) :=
    Submodule.subset_span (by simp)
  rintro x (rfl | rfl | rfl | rfl | rfl) y (rfl | rfl | rfl | rfl | rfl)
  -- 1 * _
  · first | exact m1 | simpa using m1
  · first | exact mA | simpa using mA
  · first | exact mB | simpa using mB
  · first | exact mAB | simpa using mAB
  · first | exact mBA | simpa using mBA
  -- A * _
  · first | exact mA | simpa using mA
  · rw [hAA]; exact Submodule.smul_mem _ _ mA
  · exact mAB
  · rw [← mul_assoc, hAA, smul_mul_assoc]; exact Submodule.smul_mem _ _ mAB
  · rw [← mul_assoc, hABA]; exact mA
  -- B * _
  · first | exact mB | simpa using mB
  · exact mBA
  · rw [hBB]; exact Submodule.smul_mem _ _ mB
  · rw [← mul_assoc, hBAB]; exact mB
  · rw [← mul_assoc, hBB, smul_mul_assoc]; exact Submodule.smul_mem _ _ mBA
  -- AB * _
  · first | exact mAB | simpa using mAB
  · rw [hABA]; exact mA
  · rw [mul_assoc, hBB, mul_smul_comm]; exact Submodule.smul_mem _ _ mAB
  · rw [← mul_assoc, hABA]; exact mAB
  · rw [← mul_assoc, mul_assoc (a3 δ) (b3 δ) (b3 δ), hBB, mul_smul_comm,
      smul_mul_assoc, hABA]
    exact Submodule.smul_mem _ _ mA
  -- BA * _
  · first | exact mBA | simpa using mBA
  · rw [mul_assoc, hAA, mul_smul_comm]; exact Submodule.smul_mem _ _ mBA
  · rw [hBAB]; exact mB
  · rw [← mul_assoc, mul_assoc (b3 δ) (a3 δ) (a3 δ), hAA, mul_smul_comm,
      smul_mul_assoc, hBAB]
    exact Submodule.smul_mem _ _ mB
  · rw [← mul_assoc, hBAB]; exact mBA

end TL3

end QOU.MathlibExt.TemperleyLiebSpanning
