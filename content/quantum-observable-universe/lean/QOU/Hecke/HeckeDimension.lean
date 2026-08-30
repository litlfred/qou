import QOU.Hecke.HeckeSpanning

/-!
# QOU.Hecke.HeckeDimension — `H_n(q)` is spanned by `(n+1)!` elements

Fourth brick of the type-`A` route to the `T_w` basis (bean `qou-twwf`).
`QOU.Hecke.HeckeSpanning` proved `H_{n+1}(q) = Σ_{k ≤ n+1} incl(H_n(q)) · c_k`;
inducting on that gives an explicit spanning family of the right size.

## What is proved

* `exists_spanning_finset` — for every `m` there is a `Finset` of at most
  `(m+1)!` elements spanning `H_m(q)` over `K`.

This is the `≤` half of the basis theorem in the form that does not mention
dimension, so it holds over any commutative ring.  Turning it into
`dim_K H_n(q) = (n+1)!` — and hence into injectivity of
`QOU.Hecke.TwBasis.orbitMap` — is a separate step that wants a **field**, and
is not done here.

The base case is `m = 0`: `H_0(q)` has an empty generating set, so
`Algebra.adjoin K ∅ = ⊤` collapses to `span K {1} = ⊤`.  That is why
`adjoin_range_σ` is stated at every `m` rather than only at `n+1`.
-/

namespace QOU.Hecke.IwahoriHecke

variable (K : Type*) [CommRing K] (q : K)

/-- **`H_m(q)` is spanned by at most `(m+1)!` elements.**  By induction on the
    tower: each step multiplies the bound by the `m+2` descending runs. -/
theorem exists_spanning_finset (m : ℕ) :
    ∃ s : Finset (IwahoriHecke K q m),
      s.card ≤ Nat.factorial (m + 1) ∧
        Submodule.span K (s : Set (IwahoriHecke K q m)) = ⊤ := by
  induction m with
  | zero =>
      refine ⟨{1}, by simp [Nat.factorial], ?_⟩
      have h := Algebra.adjoin_eq_span (R := K) (Set.range (σ K q 0))
      rw [adjoin_range_σ K q 0, Set.range_eq_empty, Submonoid.closure_empty] at h
      simpa using h.symm
  | succ m ih =>
      obtain ⟨s, hcard, hspan⟩ := ih
      classical
      refine ⟨Finset.image
        (fun p : Fin (m + 2) × IwahoriHecke K q m =>
          incl K q m p.2 * stair K q m (p.1 : ℕ)) (Finset.univ ×ˢ s), ?_, ?_⟩
      · calc (Finset.image _ (Finset.univ ×ˢ s)).card
            ≤ (Finset.univ ×ˢ s).card := Finset.card_image_le
          _ = (m + 2) * s.card := by simp [Finset.card_product]
          _ ≤ (m + 2) * Nat.factorial (m + 1) := Nat.mul_le_mul_left _ hcard
          _ = Nat.factorial (m + 2) := (Nat.factorial_succ (m + 1)).symm
      · refine top_unique ?_
        rw [← towerSpan_eq_top K q m]
        refine iSup_le fun k => ?_
        rintro _ ⟨a, ha, rfl⟩
        obtain ⟨b, rfl⟩ := ha
        simp only [LinearMap.mulRight_apply]
        have hb : b ∈ Submodule.span K (s : Set (IwahoriHecke K q m)) := by
          rw [hspan]; trivial
        induction hb using Submodule.span_induction with
        | mem x hx =>
            refine Submodule.subset_span ?_
            exact Finset.mem_coe.mpr (Finset.mem_image.mpr
              ⟨(k, x), Finset.mem_product.mpr ⟨Finset.mem_univ _, hx⟩, rfl⟩)
        | zero => simp
        | add x y _ _ hx hy =>
            rw [map_add, add_mul]; exact Submodule.add_mem _ hx hy
        | smul c x _ hx =>
            show incl K q m (c • x) * stair K q m (k : ℕ) ∈ _
            have hsm : incl K q m (c • x) = c • incl K q m x :=
              (incl K q m).toLinearMap.map_smul c x
            rw [hsm, smul_mul_assoc]
            exact Submodule.smul_mem _ _ hx

end QOU.Hecke.IwahoriHecke
