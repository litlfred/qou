import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
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

and the matching **lower** bounds, so both are exact:

    dim TL₂(δ) = 2 = catalan 2                   (`tl2Basis`)
    dim TL₃(δ) = 5 = catalan 3                   (`tl3Basis`)

At `n = 2` the lower bound is `TemperleyLiebAlgebra.tl2_linearIndependent`,
already in the corpus. At `n = 3` it was **not** — that file's `tl3Rep` lands in
`2 × 2` matrices, and a `4`-dimensional target cannot separate five elements.
`tl3Rep5` fixes this by summing the same family with the trivial representation
`e_i ↦ 0`; five dimensions is exactly enough, and the separation goes through as
soon as `δ` is a unit and `δ² − 1` is a non-zero-divisor. Both hold at the
substrate (`δ = q + q⁻¹ ≈ 2.01`, `δ² − 1 ≈ 3.05`).

These are the first two instances of `dim TL_n = catalan n` in this corpus
proved as *algebra* facts rather than as partition counts.

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

The lower bounds do not generalise for free either, and for a different reason:
each is a *representation exhibited by hand*, of exactly the right dimension.
General `n` wants the diagram basis again, from the other side.

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

This is the upper bound. The matching lower bound is `tl3_linearIndependent`
below, and the two together are `tl3Basis` — so `dim TL₃(δ) = 5` exactly, under
the genericity hypotheses stated there.

🛑 **This paragraph used to say freeness was NOT claimable at `n = 3`**, on the
ground that `TemperleyLiebAlgebra`'s `tl3Fam` lands in `2 × 2` matrices — a
`4`-dimensional target, which indeed cannot witness independence of five
elements however it is chosen. The obstruction was read correctly and the
conclusion drawn from it was too strong: the fix is not a different `2 × 2`
family but the *same* one summed with the trivial representation `e_i ↦ 0`,
giving a `5`-dimensional target. See `tl3Rep5`.

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

/-! ## `n = 3`: the matching lower bound, and freeness

`tl3_span_eq_top` used to end by saying no lower bound was available at `n = 3`,
because `TemperleyLiebAlgebra`'s `tl3Rep` lands in `2 × 2` matrices — a
`4`-dimensional target, which cannot witness independence of five elements
however it is chosen. That reading of the obstruction was right and the
conclusion drawn from it was too strong: the fix is not a *different* `2 × 2`
family but the **same** one carried into a target one dimension larger.

`TL₃(δ)` has a one-dimensional representation `e_i ↦ 0` — the trivial one — and
the direct sum of it with `tl3Rep` is `5`-dimensional. That is exactly enough,
and it separates the five spanning elements the moment `δ` is a unit and
`δ² − 1` is a non-zero-divisor.

Both hypotheses are used, and neither is decoration:

* `δ` a unit is what makes `e₀e₁e₀ = e₀` hold in the `2 × 2` block at all
  (`tl3Fam_adjacent` already needs it);
* `δ² − 1` a non-zero-divisor is genuine. At `δ = ±1` the algebra really does
  degenerate — `δ = 1` collapses `M₀M₁` and `M₁M₀` onto one another — so no
  argument can drop it.

At the substrate the relevant `δ = q + q⁻¹` with `q ≈ 1.11`, so `δ ≈ 2.01` and
`δ² − 1 ≈ 3.05`: both hypotheses hold, and hold with room.
-/

section TL3Rank

open QOU.MathlibExt.TemperleyLieb

variable {R : Type*} [CommRing R]

/-- `M₀M₁`, computed. The `1`s are `δc`, so this is where `δ` being a unit
enters. -/
theorem tl3M₀_mul_tl3M₁ {δ c : R} (hc : c * δ = 1) :
    tl3M₀ δ * tl3M₁ δ c = !![1, 1; 0, 0] := by
  simp only [tl3M₀, tl3M₁, Matrix.mul_fin_two]
  ext a b
  fin_cases a <;> fin_cases b <;> simp <;> linear_combination hc

/-- `M₁M₀`, computed. Its `(1,0)` entry is `δ² − 1` — the quantity the
non-degeneracy hypothesis below is about, arriving here on its own rather than
by assumption. -/
theorem tl3M₁_mul_tl3M₀ {δ c : R} (hc : c * δ = 1) :
    tl3M₁ δ c * tl3M₀ δ = !![1, 0; δ ^ 2 - 1, 0] := by
  simp only [tl3M₀, tl3M₁, Matrix.mul_fin_two]
  ext a b
  fin_cases a <;> fin_cases b <;> simp <;>
    (first | linear_combination hc | linear_combination -hc)

/-- The `2 × 2` family of `TemperleyLiebAlgebra` summed with the trivial
representation `e_i ↦ 0`. -/
noncomputable def tl3Fam5 (δ c : R) : Fin 2 → Matrix (Fin 2) (Fin 2) R × R :=
  fun i => (tl3Fam δ c i, 0)

theorem tl3Fam5_sq (δ c : R) (i : Fin 2) :
    tl3Fam5 δ c i * tl3Fam5 δ c i
      = algebraMap R (Matrix (Fin 2) (Fin 2) R × R) δ * tl3Fam5 δ c i := by
  simp only [tl3Fam5, Prod.mk_mul_mk, Prod.algebraMap_apply, tl3Fam_sq]
  simp

theorem tl3Fam5_adjacent {δ c : R} (hc : c * δ = 1) (i j : Fin 2) (h : adjFin i j) :
    tl3Fam5 δ c i * tl3Fam5 δ c j * tl3Fam5 δ c i = tl3Fam5 δ c i := by
  simp only [tl3Fam5, Prod.mk_mul_mk, tl3Fam_adjacent hc i j h]
  simp

theorem tl3Fam5_comm (δ c : R) (i j : Fin 2) (h : ¬ adjFin i j) :
    tl3Fam5 δ c i * tl3Fam5 δ c j = tl3Fam5 δ c j * tl3Fam5 δ c i := by
  simp only [tl3Fam5, Prod.mk_mul_mk, tl3Fam_comm δ c i j h]

/-- **The five-dimensional representation of `TL₃(δ)`.** -/
noncomputable def tl3Rep5 {δ c : R} (hc : c * δ = 1) :
    TL3 (R := R) δ →ₐ[R] Matrix (Fin 2) (Fin 2) R × R :=
  lift R δ (adjFin (n := 2)) (tl3Fam5 δ c) (tl3Fam5_sq δ c) (tl3Fam5_adjacent hc)
    (tl3Fam5_comm δ c)

@[simp] theorem tl3Rep5_e {δ c : R} (hc : c * δ = 1) (i : Fin 2) :
    tl3Rep5 hc (e R δ (adjFin (n := 2)) i) = tl3Fam5 δ c i :=
  lift_e R δ (adjFin (n := 2)) (tl3Fam5 δ c) (tl3Fam5_sq δ c) (tl3Fam5_adjacent hc)
    (tl3Fam5_comm δ c) i

/-- The independence, done in the matrix block. Reading the four entries in the
order `(1,1)`, `(0,1)`, `(1,0)`, `(0,0)` makes each coefficient vanish using only
the ones already known, so no linear system is ever solved:

* `(1,1)` gives `g₂(δ − c) = 0`; multiplying by `δ` turns it into
  `g₂(δ² − 1) = 0`, hence `g₂ = 0`;
* `(0,1)` then reads `g₃ = 0`;
* `(1,0)` then reads `g₄(δ² − 1) = 0`, hence `g₄ = 0`;
* `(0,0)` then reads `g₁δ = 0`, and `δ` is a unit. -/
theorem tl3_matrix_indep {δ c : R} (hc : c * δ = 1)
    (hu : ∀ x : R, x * (δ ^ 2 - 1) = 0 → x = 0) (g₁ g₂ g₃ g₄ : R)
    (h : g₁ • tl3M₀ δ + g₂ • tl3M₁ δ c + g₃ • (!![1, 1; 0, 0] : Matrix (Fin 2) (Fin 2) R)
        + g₄ • (!![1, 0; δ ^ 2 - 1, 0] : Matrix (Fin 2) (Fin 2) R) = 0) :
    g₁ = 0 ∧ g₂ = 0 ∧ g₃ = 0 ∧ g₄ = 0 := by
  have h11 := congrArg (fun M : Matrix (Fin 2) (Fin 2) R => M 1 1) h
  have h01 := congrArg (fun M : Matrix (Fin 2) (Fin 2) R => M 0 1) h
  have h10 := congrArg (fun M : Matrix (Fin 2) (Fin 2) R => M 1 0) h
  have h00 := congrArg (fun M : Matrix (Fin 2) (Fin 2) R => M 0 0) h
  simp only [tl3M₀, tl3M₁] at h00 h01 h10 h11
  simp at h00 h01 h10 h11
  have hg₂ : g₂ = 0 := by
    refine hu _ ?_
    linear_combination δ * h11 + g₂ * hc
  subst hg₂
  have hg₃ : g₃ = 0 := by linear_combination h01
  subst hg₃
  have hg₄ : g₄ = 0 := by
    refine hu _ ?_
    linear_combination h10
  subst hg₄
  have hg₁ : g₁ = 0 := by linear_combination c * h00 - g₁ * hc
  exact ⟨hg₁, rfl, rfl, rfl⟩

/-- **`{1, e₀, e₁, e₀e₁, e₁e₀}` is linearly independent in `TL₃(δ)`** whenever
`δ` is a unit and `δ² − 1` is a non-zero-divisor.

The trivial summand does the first step on its own: only `1` has a non-zero
image there, so its coefficient dies before the matrix block is touched. -/
theorem tl3_linearIndependent {δ c : R} (hc : c * δ = 1)
    (hu : ∀ x : R, x * (δ ^ 2 - 1) = 0 → x = 0) :
    LinearIndependent R
      ![(1 : TL3 (R := R) δ), a3 δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ] := by
  rw [Fintype.linearIndependent_iff]
  intro g hg
  have hg' : algebraMap R (TL3 (R := R) δ) (g 0)
      + algebraMap R (TL3 (R := R) δ) (g 1) * a3 δ
      + algebraMap R (TL3 (R := R) δ) (g 2) * b3 δ
      + algebraMap R (TL3 (R := R) δ) (g 3) * (a3 δ * b3 δ)
      + algebraMap R (TL3 (R := R) δ) (g 4) * (b3 δ * a3 δ) = 0 := by
    simpa [Fin.sum_univ_five, Algebra.smul_def] using hg
  have hM := congrArg (tl3Rep5 hc) hg'
  simp only [map_add, map_mul, map_zero, AlgHom.commutes, a3, b3, tl3Rep5_e,
    tl3Fam5, tl3Fam_zero, tl3Fam_one, Prod.mk_mul_mk, Prod.algebraMap_apply,
    Prod.mk_add_mk, tl3M₀_mul_tl3M₁ hc, tl3M₁_mul_tl3M₀ hc, Prod.mk_eq_zero] at hM
  obtain ⟨hMat, hsc⟩ := hM
  have h0 : g 0 = 0 := by simpa using hsc
  rw [h0] at hMat
  simp only [map_zero, zero_add, ← Algebra.smul_def] at hMat
  obtain ⟨h1, h2, h3, h4⟩ := tl3_matrix_indep hc hu (g 1) (g 2) (g 3) (g 4) hMat
  intro i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3
  · exact h4

/-- **`TL₃(δ)` is free of rank five on `{1, e₀, e₁, e₀e₁, e₁e₀}`.**

`dim TL₃(δ) = 5 = catalan 3`, the second instance — after `tl2Basis` — of
`dim TL_n = catalan n` proved here as an algebra fact rather than read off a
count of planar diagrams. The two halves are `tl3_span_eq_top` (upper) and
`tl3_linearIndependent` (lower). -/
noncomputable def tl3Basis {δ c : R} (hc : c * δ = 1)
    (hu : ∀ x : R, x * (δ ^ 2 - 1) = 0 → x = 0) :
    Module.Basis (Fin 5) R (TL3 (R := R) δ) :=
  Module.Basis.mk (tl3_linearIndependent hc hu) (by
    have hspan := tl3_span_eq_top (R := R) δ
    have hrange : Set.range
        ![(1 : TL3 (R := R) δ), a3 δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ]
        = ({1, a3 (R := R) δ, b3 δ, a3 δ * b3 δ, b3 δ * a3 δ} : Set (TL3 (R := R) δ)) := by
      ext x
      simp only [Matrix.range_cons, Matrix.range_empty, Set.union_empty,
        Set.union_singleton, Set.mem_union, Set.mem_insert_iff, Set.mem_singleton_iff]
      tauto
    rw [hrange, hspan])

/-- The rank, as a number. `StrongRankCondition` is what makes "rank" a
well-defined natural number at all; it holds for every nontrivial commutative
ring, and is taken as a hypothesis here rather than derived so that the file
keeps its minimal import cone. -/
theorem tl3_finrank_eq_five [StrongRankCondition R] {δ c : R} (hc : c * δ = 1)
    (hu : ∀ x : R, x * (δ ^ 2 - 1) = 0 → x = 0) :
    Module.finrank R (TL3 (R := R) δ) = 5 := by
  simpa using Module.finrank_eq_card_basis (tl3Basis hc hu)

end TL3Rank

end QOU.MathlibExt.TemperleyLiebSpanning
