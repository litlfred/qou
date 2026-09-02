import QOU.Hecke.IwahoriHecke

/-!
# QOU.Hecke.HeckeTower — the inclusion `H_n(q) → H_{n+1}(q)`

First brick of the type-`A` spanning argument (bean `qou-twwf`), which is the
route to `dim_K H_n(q) ≤ (n+1)!` that does **not** go through Matsumoto's
theorem.

`QOU.Hecke.TwIndependent` reduces the `T_w` basis theorem to exactly one thing:
injectivity of `orbitMap`, equivalently that the `T_w` **span**.  Over a field
that follows from a spanning family of the right size, and the classical way to
produce one is the tower

  `H_{n+1}(q) = Σ_{k=0}^{n+1} incl(H_n(q)) · c_k`,  `c_k = σ_n σ_{n-1} ⋯ σ_{n-k+1}`,

inducted on `n`.  This file supplies the `incl` that statement is about.

## What is proved

* `incl` — the algebra map `H_n(q) →ₐ[K] H_{n+1}(q)` sending `σ_i ↦ σ_{i}`
  under `Fin.castSucc`.
* `incl_σ` — it does what it says on generators.

Nothing about the tower decomposition itself is proved here.
-/

namespace QOU.Hecke.IwahoriHecke

variable (K : Type*) [CommRing K] (q : K) (n : ℕ)

/-- The generators of `H_n(q)`, viewed inside `H_{n+1}(q)`. -/
noncomputable def freeIncl :
    FreeAlgebra K (Fin n) →ₐ[K] IwahoriHecke K q (n + 1) :=
  FreeAlgebra.lift K (fun i => σ K q (n + 1) i.castSucc)

@[simp] theorem freeIncl_ι (i : Fin n) :
    freeIncl K q n (FreeAlgebra.ι K i) = σ K q (n + 1) i.castSucc :=
  FreeAlgebra.lift_ι_apply _ _

theorem freeIncl_rel {x y : FreeAlgebra K (Fin n)} (h : HeckeRel K q n x y) :
    freeIncl K q n x = freeIncl K q n y := by
  induction h with
  | quadratic i =>
      simp only [map_mul, map_add, map_smul, map_one, freeIncl_ι]
      exact σ_quadratic K q (n + 1) i.castSucc
  | braid i hi =>
      simp only [map_mul, freeIncl_ι]
      have hi' : ((i.castSucc : Fin (n + 1)) : ℕ) + 1 < n + 1 := by
        simp
      have hcast : (⟨(i : ℕ) + 1, hi⟩ : Fin n).castSucc
          = (⟨((i.castSucc : Fin (n + 1)) : ℕ) + 1, hi'⟩ : Fin (n + 1)) := by
        apply Fin.ext; simp
      rw [hcast]
      exact σ_braid K q (n + 1) i.castSucc hi'
  | commute i j hij =>
      simp only [map_mul, freeIncl_ι]
      exact σ_commute K q (n + 1) i.castSucc j.castSucc (by simpa using hij)

/-- **The tower inclusion.**  `H_n(q)` maps into `H_{n+1}(q)` by sending each
    generator to the generator of the same index. -/
noncomputable def incl :
    IwahoriHecke K q n →ₐ[K] IwahoriHecke K q (n + 1) :=
  RingQuot.liftAlgHom K ⟨freeIncl K q n, fun _ _ h => freeIncl_rel K q n h⟩

@[simp] theorem incl_σ (i : Fin n) :
    incl K q n (σ K q n i) = σ K q (n + 1) i.castSucc := by
  have h := RingQuot.liftAlgHom_mkAlgHom_apply (S := K)
    (freeIncl K q n) (fun _ _ hr => freeIncl_rel K q n hr) (FreeAlgebra.ι K i)
  rw [freeIncl_ι] at h
  exact h

end QOU.Hecke.IwahoriHecke
