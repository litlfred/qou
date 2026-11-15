import QOU.Hecke.FullRankFromWedderburn
import QOU.Machinery.HeckeH3AlgebraLaws
import QOU.Machinery.HeckeH3AlgebraInstance

/-!
# `QOU.Hecke.InstanceOnH3A` — the `HeckeAlgebra` class, on the tree's own `H₃(q)`

`QOU.Machinery.HeckeH3AlgebraInstance.H3A` is the tree's three-strand Hecke
algebra: a `Ring` and `Algebra` on the six-dimensional normal-form module, with
the presentation proved in `QOU.Machinery.HeckeH3AlgebraLaws` (`mulσ₀_hecke`,
`mulσ₁_hecke`, `braid_operator`) and `mulNF_assoc` for associativity. What it
never had is an instance of the *class* `QOU.Hecke.HeckeAlgebra`, so every
`[HeckeAlgebra R n q A]` hypothesis in the corpus stayed unwitnessed at `n = 3`.

This file supplies it, on that carrier rather than on a new one. Together with
`QOU.Hecke.isHeckeOfFullRank_H3A` (rank `6 = 3!`) it gives the pair that actually
pins the algebra down: the relations plus the dimension. Bean qou-ti7p.

## The basis, and where the generators sit

`H3A R h` wraps `v : Fin 6 → R` on the normal-form basis `[γ, σ₀, σ₁, L₊, L₋, e⁻]`,
and `mulNF` decomposes its *right* argument, applying the composite generator
action of each basis element on the left one. So

    σ₀ = e₁,  σ₁ = e₂,  σ₁σ₀ = e₃,  σ₀σ₁ = e₄,  σ₀σ₁σ₀ = e₅,

which is what `sigma_mul_*` below record and what makes `spans` a finite check
rather than an argument.

## Far-commutativity is vacuous here, and that is a fact about `n = 3`

`Generator 3` carries `idx : Fin 2`, so no two generator indices differ by `≥ 2`
and `Generator.farCommuting` is never satisfied — exactly as `HeckeH3AlgebraLaws`
records ("far commutation is vacuous with two generators"). The first level where
it has content is `n = 4`.
-/

namespace QOU.Hecke.InstanceOnH3A

open QOU.Machinery.H3

universe u

variable (K : Type u) [Field K] (q : K)

/-- `σ₀ ∈ H₃(q)` — normal-form basis vector `e₁`. -/
def s0 : H3A K (q - q⁻¹) := ⟨![0, 1, 0, 0, 0, 0]⟩

/-- `σ₁ ∈ H₃(q)` — normal-form basis vector `e₂`. -/
def s1 : H3A K (q - q⁻¹) := ⟨![0, 0, 1, 0, 0, 0]⟩

/-! ## The presentation, as ring equations -/

/-- `σ₀² = (q − q⁻¹)·σ₀ + 1`. -/
theorem s0_sq : s0 K q * s0 K q = (q - q⁻¹) • s0 K q + 1 := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [s0, mulNF, mulσ₀, mulσ₁, unitNF] <;> ring

/-- `σ₁² = (q − q⁻¹)·σ₁ + 1`. -/
theorem s1_sq : s1 K q * s1 K q = (q - q⁻¹) • s1 K q + 1 := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [s1, mulNF, mulσ₀, mulσ₁, unitNF] <;> ring

/-- **The braid relation** `σ₀σ₁σ₀ = σ₁σ₀σ₁`. Both sides are `e₅`, the longest
element of `S₃`. -/
theorem braid : s0 K q * s1 K q * s0 K q = s1 K q * s0 K q * s1 K q := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [s0, s1, mulNF, mulσ₀, mulσ₁] <;> ring

/-! ## The remaining basis vectors are words in the generators -/

theorem s1_mul_s0 : s1 K q * s0 K q = (⟨![0, 0, 0, 1, 0, 0]⟩ : H3A K (q - q⁻¹)) := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [s0, s1, mulNF, mulσ₀, mulσ₁]

theorem s0_mul_s1 : s0 K q * s1 K q = (⟨![0, 0, 0, 0, 1, 0]⟩ : H3A K (q - q⁻¹)) := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [s0, s1, mulNF, mulσ₀, mulσ₁]

theorem s0_mul_s1_mul_s0 :
    s0 K q * s1 K q * s0 K q = (⟨![0, 0, 0, 0, 0, 1]⟩ : H3A K (q - q⁻¹)) := by
  apply H3A.ext
  funext i
  fin_cases i <;> simp [s0, s1, mulNF, mulσ₀, mulσ₁]

/-- **Every element is an `K`-combination of words in the generators** — the six
basis vectors are `1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀`. -/
theorem decompose (x : H3A K (q - q⁻¹)) :
    x = x.v 0 • 1 + x.v 1 • s0 K q + x.v 2 • s1 K q
      + x.v 3 • (s1 K q * s0 K q) + x.v 4 • (s0 K q * s1 K q)
      + x.v 5 • (s0 K q * s1 K q * s0 K q) := by
  rw [s0_mul_s1_mul_s0, s1_mul_s0, s0_mul_s1]
  apply H3A.ext
  funext i
  obtain ⟨v⟩ := x
  fin_cases i <;> simp [s0, s1, unitNF] <;> ring

/-! ## The instance -/

/-- The generator embedding: `Generator 3` carries `idx : Fin 2`. -/
def embed3 : Generator 3 → H3A K (q - q⁻¹) := fun i =>
  if i.idx.val = 0 then s0 K q else s1 K q

@[simp] theorem embed3_zero : embed3 K q ⟨0⟩ = s0 K q := rfl
@[simp] theorem embed3_one : embed3 K q ⟨1⟩ = s1 K q := rfl

theorem generator_three_cases (i : Generator 3) : i = ⟨0⟩ ∨ i = ⟨1⟩ := by
  obtain ⟨⟨v, hv⟩⟩ := i
  interval_cases v
  · exact Or.inl rfl
  · exact Or.inr rfl

/-- **`H₃(q)` — the tree's own one — is a `HeckeAlgebra`.**

Paired with `QOU.Hecke.isHeckeOfFullRank_H3A` (rank `6 = 3!`), this is the first
place both halves hold of the same object: the relations *and* the dimension. -/
instance instHeckeAlgebraH3A : HeckeAlgebra K 3 q (H3A K (q - q⁻¹)) where
  embed := embed3 K q
  quadratic := by
    intro i
    rcases generator_three_cases i with rfl | rfl
    · simpa using s0_sq K q
    · simpa using s1_sq K q
  braid := by
    intro i j _
    rcases generator_three_cases i with rfl | rfl <;>
      rcases generator_three_cases j with rfl | rfl <;>
      simp only [embed3_zero, embed3_one]
    · exact braid K q
    · exact (braid K q).symm
  farCommute := by
    intro i j hij
    obtain ⟨hne, hadj⟩ := hij
    exact absurd
      (by
        rcases generator_three_cases i with rfl | rfl <;>
          rcases generator_three_cases j with rfl | rfl
        · exact absurd rfl hne
        · exact Or.inl rfl
        · exact Or.inr rfl
        · exact absurd rfl hne)
      hadj
  spans := by
    refine le_antisymm le_top ?_
    rintro x -
    have h0 : s0 K q ∈ Algebra.adjoin K (Set.range (embed3 K q)) :=
      Algebra.subset_adjoin ⟨⟨0⟩, rfl⟩
    have h1 : s1 K q ∈ Algebra.adjoin K (Set.range (embed3 K q)) :=
      Algebra.subset_adjoin ⟨⟨1⟩, rfl⟩
    rw [decompose K q x]
    exact Subalgebra.add_mem _
      (Subalgebra.add_mem _
        (Subalgebra.add_mem _
          (Subalgebra.add_mem _
            (Subalgebra.add_mem _
              (Subalgebra.smul_mem _ (Subalgebra.one_mem _) _)
              (Subalgebra.smul_mem _ h0 _))
            (Subalgebra.smul_mem _ h1 _))
          (Subalgebra.smul_mem _ (Subalgebra.mul_mem _ h1 h0) _))
        (Subalgebra.smul_mem _ (Subalgebra.mul_mem _ h0 h1) _))
      (Subalgebra.smul_mem _ (Subalgebra.mul_mem _ (Subalgebra.mul_mem _ h0 h1) h0) _)

end QOU.Hecke.InstanceOnH3A
