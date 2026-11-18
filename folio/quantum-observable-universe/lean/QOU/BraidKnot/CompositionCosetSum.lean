import QOU.BraidKnot.CompositionCosetExists

/-!
# `x_μ · T_e` is the sum over a coset — the algebraic core of Mathas' Corollary 3.4

Mathas 3.4 says `M^μ = x_μ H` is `R`-free on `{x_μ T_d : d ∈ D_μ}`.  The identity that
carries all of its content is the one proved here:

    `x_μ · T_e = Σ_{v ∈ S_μ} T_{e·v}`

i.e. multiplying the Murphy element by a *single* basis element of the algebra produces
the **sum over one whole coset** of the Young subgroup, with every coefficient `1`.  No
`q` appears.  Freeness is then a statement about disjoint cosets in the `T_w` basis, and
`Prop 3.3` (`CompositionCosetExists`) is what says the cosets partition `S_n`.

## Handedness — why `e⁻¹` and not `e`

Two conventions have to be reconciled and neither is negotiable.

* `TwBasis.Tw_mul_Tw` is **flipped**: `T_v · T_w = T_{w·v}` when the lengths add.  That
  is forced by the handedness of `orbitMap`, not a typo (see its module docstring).  So
  `x_μ · T_e = Σ_v T_v · T_e = Σ_v T_{e·v}` lands on the **left** coset `e·S_μ`.
* `CompositionMinimal.IsDistinguished` is the **right**-coset notion: it gives
  `ℓ(v·d) = ℓ(v) + ℓ(d)` for `v ∈ S_μ`, which is the hypothesis for `S_μ·d`.

The length hypothesis needed above is `ℓ(e·v) = ℓ(e) + ℓ(v)`, and inverting
`(e·v)⁻¹ = v⁻¹·e⁻¹` converts one into the other, because `ℓ` is inverse-invariant and
`S_μ` is a subgroup (so `v⁻¹` ranges over it too).  Hence the correct hypothesis on `e`
is that **`e⁻¹` is distinguished** — recorded as `IsDistinguishedL`.  This is not a
weakening: `IsDistinguishedL c` and `IsDistinguished c` are carried onto each other by
`e ↦ e⁻¹`, so Prop 3.3 transports verbatim (`existsUnique_isDistinguishedL`).
-/

namespace QOU.BraidKnot.CompositionCosetSum

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.BraidKnot.CompositionMurphy QOU.BraidKnot.HeckeMurphy
open QOU.Hecke.SymmetricCoxeter QOU.Hecke.TwBasis Equiv

variable {n : ℕ}

/-- **The left-coset form of `IsDistinguished`**: `e` is the minimal-length
representative of the *left* coset `e · S_μ` exactly when `e⁻¹` is distinguished for the
right cosets.  See the module docstring for why the flip is forced. -/
def IsDistinguishedL (c : Composition n) (e : Perm (Fin n)) : Prop :=
  IsDistinguished c e⁻¹

/-- **The length hypothesis `Tw_mul_Tw` needs**, on the left. -/
theorem length_mul_eq_add_of_isDistinguishedL {c : Composition (n + 1)}
    {e : Perm (Fin (n + 1))} (he : IsDistinguishedL c e)
    {v : Perm (Fin (n + 1))} (hv : v ∈ youngOfComp c) :
    (permCoxeterSystem n).length (e * v)
      = (permCoxeterSystem n).length e + (permCoxeterSystem n).length v := by
  have h := length_mul_eq_add_of_isDistinguished he (inv_mem hv)
  have hrw : (e * v)⁻¹ = v⁻¹ * e⁻¹ := mul_inv_rev e v
  have h1 := (permCoxeterSystem n).length_inv (e * v)
  have h2 := (permCoxeterSystem n).length_inv v
  have h3 := (permCoxeterSystem n).length_inv e
  rw [hrw] at h1
  omega

/-- **Prop 3.3 transported to left cosets.**  Every left coset `w · S_μ` contains exactly
one `e` with `e⁻¹` distinguished.  Nothing new is proved here: inversion is a bijection
between left and right cosets that preserves length, so
`CompositionCosetExists.existsUnique_isDistinguished_mem_coset` transfers verbatim. -/
theorem existsUnique_isDistinguishedL (c : Composition (n + 1)) (w : Perm (Fin (n + 1))) :
    ∃! e, IsDistinguishedL c e ∧ w⁻¹ * e ∈ youngOfComp c := by
  obtain ⟨d, ⟨hd, hdm⟩, huniq⟩ :=
    QOU.BraidKnot.CompositionCosetExists.existsUnique_isDistinguished_mem_coset c w⁻¹
  rw [inv_inv] at hdm
  refine ⟨d⁻¹, ⟨by simpa [IsDistinguishedL] using hd, ?_⟩, ?_⟩
  · have : (d * w)⁻¹ ∈ youngOfComp c := inv_mem hdm
    simpa [mul_inv_rev] using this
  · rintro e ⟨hed, hem⟩
    have h1 : IsDistinguished c e⁻¹ := hed
    have h2 : e⁻¹ * w⁻¹⁻¹ ∈ youngOfComp c := by
      rw [inv_inv]
      have : (w⁻¹ * e)⁻¹ ∈ youngOfComp c := inv_mem hem
      simpa [mul_inv_rev] using this
    have := huniq e⁻¹ ⟨h1, h2⟩
    rw [← this, inv_inv]

/-- **Distinct left-distinguished elements give disjoint cosets.**  Contrapositive form:
if the cosets meet, the representatives are equal. -/
theorem eq_of_mul_mem {c : Composition (n + 1)} {e₁ e₂ : Perm (Fin (n + 1))}
    (h₁ : IsDistinguishedL c e₁) (h₂ : IsDistinguishedL c e₂)
    (hmem : e₂⁻¹ * e₁ ∈ youngOfComp c) : e₁ = e₂ := by
  have h := QOU.BraidKnot.CompositionCoset.isDistinguished_unique h₁ h₂
    (by simpa [inv_inv] using hmem)
  simpa using congrArg (·⁻¹) h

variable (K : Type*) [Field K] (q : K)

/-- **`x_μ · T_e = Σ_{v ∈ S_μ} T_{e·v}`.**  Every coefficient is `1`; no `q` appears. -/
theorem xComp_mul_Tw (c : Composition (n + 1)) [DecidablePred (· ∈ youngOfComp c)]
    {e : Perm (Fin (n + 1))} (he : IsDistinguishedL c e) :
    xComp K q c * Tw K q n e
      = ∑ v ∈ ({w | w ∈ youngOfComp c} : Finset (Perm (Fin (n + 1)))),
          Tw K q n (e * v) := by
  simp only [xComp, murphySum, Finset.sum_mul]

  refine Finset.sum_congr rfl fun v hv => ?_
  exact QOU.Hecke.TwBasis.Tw_mul_Tw K q n v e
    (length_mul_eq_add_of_isDistinguishedL he (by simpa using hv))

/-- **The same, as a Murphy element of the coset.**  `x_μ · T_e = x_{e·S_μ}` — the
Murphy element of the *left coset*, which is exactly Mathas' `m_{μ}T_d`. -/
theorem xComp_mul_Tw_eq_murphySum (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)]
    {e : Perm (Fin (n + 1))} (he : IsDistinguishedL c e) :
    xComp K q c * Tw K q n e
      = murphySum K q n
          (({w | w ∈ youngOfComp c} : Finset (Perm (Fin (n + 1)))).image (e * ·)) := by
  rw [xComp_mul_Tw K q c he]
  simp only [murphySum]
  rw [Finset.sum_image (fun a _ b _ h => mul_left_cancel h)]

/-- **The coordinates of `x_μ T_e` in the `T_w` basis are the indicator of the coset.**
Every coordinate is `0` or `1`; `q` does not appear.  This is the concrete form of
Mathas' Corollary 3.4, and everything below is bookkeeping on top of it. -/
theorem repr_xComp_mul_Tw (c : Composition (n + 1)) [DecidablePred (· ∈ youngOfComp c)]
    {e : Perm (Fin (n + 1))} (he : IsDistinguishedL c e) (w : Perm (Fin (n + 1))) :
    (basisTwOfField K q n).repr (xComp K q c * Tw K q n e) w
      = if e⁻¹ * w ∈ youngOfComp c then 1 else 0 := by
  rw [xComp_mul_Tw K q c he]
  have hb : ∀ u : Perm (Fin (n + 1)),
      Tw K q n u = basisTwOfField K q n u := fun u => by
    rw [coe_basisTwOfField]
  simp only [hb, map_sum, Module.Basis.repr_self, Finsupp.coe_finset_sum,
    Finset.sum_apply, Finsupp.single_apply]
  have hcond : ∀ v : Perm (Fin (n + 1)), (e * v = w) ↔ (v = e⁻¹ * w) := by
    intro v
    constructor
    · rintro rfl; simp [← mul_assoc]
    · rintro rfl; simp [← mul_assoc]
  simp only [hcond]
  rw [Finset.sum_ite_eq' ({w | w ∈ youngOfComp c} : Finset (Perm (Fin (n + 1))))
    (e⁻¹ * w) (fun _ => (1 : K))]
  simp

/-- **Mathas, Corollary 3.4** — `{x_μ T_e}` is linearly independent over any family of
left-distinguished representatives lying in distinct cosets. -/
theorem linearIndependent_xComp_mul_Tw (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] {ι : Type*} (e : ι → Perm (Fin (n + 1)))
    (he : ∀ i, IsDistinguishedL c (e i)) (hinj : Function.Injective e) :
    LinearIndependent K (fun i => xComp K q c * Tw K q n (e i)) := by
  rw [linearIndependent_iff']
  intro s g hg i₀ hi₀
  have h := congrArg (fun x => (basisTwOfField K q n).repr x (e i₀)) hg
  simp only [map_sum, map_smul, Finsupp.coe_finset_sum, Finset.sum_apply,
    Finsupp.smul_apply, smul_eq_mul, map_zero, Finsupp.coe_zero, Pi.zero_apply] at h
  rw [Finset.sum_congr rfl (fun i _ => by
    rw [repr_xComp_mul_Tw K q c (he i) (e i₀)])] at h
  rw [Finset.sum_eq_single i₀] at h
  · simpa using h
  · intro i _ hne
    have : ¬ ((e i)⁻¹ * e i₀ ∈ youngOfComp c) := by
      intro hmem
      exact hne (hinj (eq_of_mul_mem (he i₀) (he i) hmem).symm)
    simp [this]
  · intro hns
    exact absurd hi₀ hns

/-- Subtracting the coset basis sum from the product of the Murphy element and a left-distinguished basis element cancels to zero (`qou-gwe9`). -/
theorem xComp_mul_Tw_sub_sum_eq_zero (c : Composition (n + 1)) [DecidablePred (· ∈ youngOfComp c)]
    {e : Perm (Fin (n + 1))} (he : IsDistinguishedL c e) :
    xComp K q c * Tw K q n e
      - ∑ v ∈ ({w | w ∈ youngOfComp c} : Finset (Perm (Fin (n + 1)))),
          Tw K q n (e * v) = 0 := by
  rw [xComp_mul_Tw K q c he, sub_self]

end QOU.BraidKnot.CompositionCosetSum
