import QOU.Hecke.MarkovTraceOnH4A

/-!
# `QOU.Hecke.MarkovTraceClassNotUnique` — the `MarkovTrace` class does not determine the trace

`QOU.Hecke.MarkovTrace` records normalisation, cyclicity, `tr(σᵢ) = z` and
`tr(σᵢσⱼ) = z²` (`i < j`), but not the cross-level Markov property. This file shows that
those fields do **not** determine the trace, refuting the former
`axiom QOU.Hecke.markov_trace_unique_axiom` (which, being an `axiom` and false, made the
environment inconsistent).

## The counterexample

Carrier: the tree's own four-strand Hecke algebra `H4A K (q − q⁻¹)` with
`instHeckeAlgebraH4A`, over any field `K`, any `q`. For every `w : K`,
`markovTraceH4A K q w` is the Ocneanu trace at parameter `w`. All of them are cyclic, so
any `K`-linear combination is cyclic too. Take

    t_Z = 4·tr_Z − 3·tr_{Z+1} − tr_{Z−1} + tr_{Z+2}.

The weights `(4, −3, −1, 1)` at offsets `(0, 1, −1, 2)` have moments
`Σ a = 1`, `Σ a·d = 0`, `Σ a·d² = 0`, `Σ a·d³ = 6`. Hence

* `t_Z(1) = 1`, `t_Z(σᵢ) = Z`, `t_Z(σᵢσⱼ) = Z²` — every `MarkovTrace` field holds with
  `z_param = Z`;
* `t_Z(σ₀σ₁σ₂) = Z³ + 6`, while `tr_Z(σ₀σ₁σ₂) = Z³`.

So `t_Z ≠ tr_Z` whenever `6 ≠ 0` in `K`. Structurally: the cyclic traces on `H₄(q)` form a
5-dimensional space (one coordinate per partition of 4, i.e. per conjugacy class of `S₄`,
via the minimal-length class representatives `1, σ₀, σ₀σ₂, σ₀σ₁, σ₀σ₁σ₂`), and the class
fields fix only the first four coordinates; the 4-cycle class `σ₀σ₁σ₂` is free.

`t_Z` is not a Markov trace in the sense of (M3); `QOU.Hecke.markov_trace_unique` proves
uniqueness once (M3) is assumed.
-/

namespace QOU.Hecke.MarkovTraceClassNotUnique

open QOU.Hecke QOU.Hecke.MarkovTraceOnH4A QOU.Hecke.InstanceOnH4A QOU.Machinery.H4

universe u

variable (K : Type u) [Field K] (q : K)

/-- The signed mixture `4·tr_Z − 3·tr_{Z+1} − tr_{Z−1} + tr_{Z+2}` of Ocneanu traces. -/
def mix (Z : K) : H4A K (q - q⁻¹) →ₗ[K] K :=
  (4 : K) • traceMap K q Z - (3 : K) • traceMap K q (Z + 1) - traceMap K q (Z - 1)
    + traceMap K q (Z + 2)

theorem mix_apply (Z : K) (x : H4A K (q - q⁻¹)) :
    mix K q Z x = 4 * traceMap K q Z x - 3 * traceMap K q (Z + 1) x
      - traceMap K q (Z - 1) x + traceMap K q (Z + 2) x := by
  simp only [mix, LinearMap.add_apply, LinearMap.sub_apply, LinearMap.smul_apply, smul_eq_mul]

theorem traceMap_cyclic (w : K) (x y : H4A K (q - q⁻¹)) :
    traceMap K q w (x * y) = traceMap K q w (y * x) :=
  (markovTraceH4A K q w).cyclic x y

theorem traceMap_gen (w : K) (i : Generator 4) :
    traceMap K q w (HeckeAlgebra.embed (R := K) (q := q) i) = w :=
  (markovTraceH4A K q w).trace_gen i

theorem traceMap_prod_gen (w : K) (i j : Generator 4) (h : i.idx.val < j.idx.val) :
    traceMap K q w (HeckeAlgebra.embed (R := K) (q := q) i
      * HeckeAlgebra.embed (R := K) (q := q) j) = w * w :=
  (markovTraceH4A K q w).trace_prod_gen i j h

/-- `t_Z` satisfies every field of the `MarkovTrace` class, with `z_param = Z`. -/
def mixMarkov (Z : K) : MarkovTrace 4 q (H4A K (q - q⁻¹)) where
  trace := mix K q Z
  normalised := by
    rw [mix_apply]
    simp only [traceMap_one]
    norm_num
  cyclic x y := by
    rw [mix_apply, mix_apply, traceMap_cyclic K q Z x y, traceMap_cyclic K q (Z + 1) x y,
      traceMap_cyclic K q (Z - 1) x y, traceMap_cyclic K q (Z + 2) x y]
  z_param := Z
  trace_gen i := by
    rw [mix_apply]
    simp only [traceMap_gen]
    ring
  trace_prod_gen i j h := by
    rw [mix_apply]
    simp only [traceMap_prod_gen K q _ i j h]
    ring

/-- `σ₀σ₁σ₂` is the normal-form basis vector `b 10` (two steps of the word tree). -/
theorem s0_s1_s2 : s0 K q * s1 K q * s2 K q = b K q 10 := by
  show b K q 1 * s1 K q * s2 K q = b K q 10
  rw [b_tree_4, b_tree_10]

/-- The Ocneanu trace of the 4-cycle representative: `tr_w(σ₀σ₁σ₂) = w³`. -/
theorem traceMap_s0_s1_s2 (w : K) : traceMap K q w (s0 K q * s1 K q * s2 K q) = w ^ 3 := by
  rw [s0_s1_s2, traceMap_apply, trM4_b]
  simp [TRM4]

theorem mix_s0_s1_s2 (Z : K) : mix K q Z (s0 K q * s1 K q * s2 K q) = Z ^ 3 + 6 := by
  rw [mix_apply]
  simp only [traceMap_s0_s1_s2]
  ring

/-- **Two `MarkovTrace`s with the same `z_param` and different traces**, on `H₄(q)`, for
every `q` and every `Z`, over any field in which `6 ≠ 0`. -/
theorem mixMarkov_trace_ne (h6 : (6 : K) ≠ 0) (Z : K) :
    (mixMarkov K q Z).z_param = (markovTraceH4A K q Z).z_param ∧
      (mixMarkov K q Z).trace ≠ (markovTraceH4A K q Z).trace := by
  refine ⟨rfl, fun h => h6 ?_⟩
  have := LinearMap.congr_fun h (s0 K q * s1 K q * s2 K q)
  change mix K q Z _ = traceMap K q Z _ at this
  rw [mix_s0_s1_s2, traceMap_s0_s1_s2] at this
  linear_combination this

/-- **The former `markov_trace_unique_axiom` is false.** Its statement (at universe `0`)
is refuted by `mixMarkov` against `markovTraceH4A` over `ℚ`, `q = 2`, `Z = 0`. -/
theorem markov_trace_unique_axiom_false :
    ¬ (∀ {R : Type} {n : ℕ} {q : R} {A : Type}
        [CommRing R] [Inv R] [Ring A] [Algebra R A] [HeckeAlgebra R n q A]
        (MT₁ MT₂ : MarkovTrace n q A), MT₁.z_param = MT₂.z_param → MT₁.trace = MT₂.trace) := by
  intro hax
  obtain ⟨hz, hne⟩ := mixMarkov_trace_ne ℚ 2 (by norm_num) 0
  exact hne (hax _ _ hz)

end QOU.Hecke.MarkovTraceClassNotUnique
