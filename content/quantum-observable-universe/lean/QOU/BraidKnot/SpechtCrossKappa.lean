import QOU.BraidKnot.SpechtCrossDominance

/-!
# The cross-shape column antisymmetriser `κ_t` acting on `M^ν`

`SpechtIrreducible` builds `κ_t = Σ_{π ∈ C_t} sgn(π) · π` acting on `M^μ`, where
`t` is a `μ`-tableau. Sagan's cross-shape theory (§2.4) needs the *same* operator
acting on `M^ν` for a **different** shape `ν` with the same number of cells: the
column group `C_t ≤ S_n` does not care which diagram the module came from.

This module supplies that, and the one fact about it Sagan 2.4.4 consumes:

> `κ_t {s} ≠ 0` forces no column of `t` to meet a row of `s` twice,

whose contrapositive is the sign-reversing involution already used same-shape in
`SpechtIrreducible.kap_of_mem_line_clash`. Composed with
`SpechtCrossDominance.dominance_of_tableau_noclash` (Sagan 2.2.6) it gives the
headline of this file:

> `κ_t {s} ≠ 0  ⟹  μ ⊵ ν`.

## The transport

`C_t ≤ Perm (Fin (nOf μ))` while `Mtab.rep ν` takes `Perm (Fin (nOf ν))`, so
everything is threaded through `transportPerm h`, the multiplicative transport
along `h : nOf μ = nOf ν`. It is definitionally
`SpechtClassification.transportPermHom h` — the same term — so the two agree by
`rfl` where they meet; that module is downstream and cannot be imported here.

Nothing else in the argument depends on `μ ≠ ν`; taking `ν = μ` and `h = rfl`
recovers the same-shape statements.

## Outcome

`SpechtClassification.spechtIso_imp_dom_both` is proved from this file plus
`SpechtCrossDominance`, and with it `specht_pairwise_noniso`. The assembly is
`SpechtClassification.dom_of_intertwiner`.

The extension of a homomorphism `S^μ → M^ν` to all of `M^μ` — the step the
textbook proof needs `M^μ = S^μ ⊕ (S^μ)ᗮ` for — turned out to be avoidable; see
§3-bis.
-/

open scoped BigOperators

namespace QOU.BraidKnot.SpechtCrossKappa

open QOU.BraidKnot QOU.BraidKnot.Specht
open Equiv (Perm)

variable {k : Type} [CommRing k]

/-! ## 1. Transport of permutations along `nOf μ = nOf ν` -/

/-- Relabelling `Fin a ≃ Fin b` as a group isomorphism of symmetric groups.
Definitionally equal to `SpechtClassification.transportPermHom`. -/
noncomputable def transportPerm {a b : ℕ} (h : a = b) : Perm (Fin a) →* Perm (Fin b) :=
  (Equiv.permCongrHom (finCongr h)).toMonoidHom

@[simp] theorem transportPerm_apply {a b : ℕ} (h : a = b) (π : Perm (Fin a)) (l : Fin b) :
    transportPerm h π l = finCongr h (π ((finCongr h).symm l)) := rfl

@[simp] theorem transportPerm_symm_apply {a b : ℕ} (h : a = b) (π : Perm (Fin a)) (l : Fin b) :
    (transportPerm h π).symm l = finCongr h (π.symm ((finCongr h).symm l)) := rfl

/-- Transport preserves the sign — it is a relabelling, not a rearrangement. -/
@[simp] theorem sign_transportPerm {a b : ℕ} (h : a = b) (π : Perm (Fin a)) :
    Equiv.Perm.sign (transportPerm h π) = Equiv.Perm.sign π :=
  Equiv.Perm.sign_permCongr _ _

/-! ## 2. The operator -/

/-- **The cross-shape column antisymmetriser.** `κ_t` for a `μ`-tableau `t`,
acting on `M^ν`: `Σ_{π ∈ C_t} sgn(π) · (transported π)`.

With `ν = μ` and `h = rfl` this is `SpechtIrreducible.kapL`. -/
noncomputable def kapCross {μ ν : YoungDiagram} (h : nOf μ = nOf ν) (t : Tableau μ) :
    Mtab (k := k) ν →ₗ[k] Mtab (k := k) ν :=
  ∑ π : colStab t,
    (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
      (Mtab.rep ν (transportPerm h (π : Perm (Fin (nOf μ)))))

theorem kapCross_apply {μ ν : YoungDiagram} (h : nOf μ = nOf ν) (t : Tableau μ)
    (x : Mtab (k := k) ν) :
    kapCross (k := k) h t x
      = ∑ π : colStab t, (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
          Mtab.rep ν (transportPerm h (π : Perm (Fin (nOf μ)))) x := by
  unfold kapCross
  rw [LinearMap.sum_apply]
  exact Finset.sum_congr rfl (fun π _ => by rw [LinearMap.smul_apply])

/-- `κ_t` on a basis tabloid vector is the signed sum over the column group. -/
theorem kapCross_of {μ ν : YoungDiagram} (h : nOf μ = nOf ν) (t : Tableau μ)
    (s : Tableau ν) :
    kapCross (k := k) h t (Mtab.of s)
      = ∑ π : colStab t, (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
          Mtab.of (k := k) ((transportPerm h (π : Perm (Fin (nOf μ)))) • s) := by
  rw [kapCross_apply]
  exact Finset.sum_congr rfl (fun π _ => by rw [Mtab.rep_of])

/-! ## 3. A clash kills it

The same sign-reversing involution as `SpechtIrreducible.kap_of_mem_line_clash`:
if two labels share a column of `t` and a row of `s`, the transposition swapping
them lies in `C_t`, fixes the tabloid `{s}`, and pairs the `C_t`-sum off against
itself with opposite signs. -/

/-- **Clash ⇒ vanishing.** If `a ≠ b` share a column of `t` and (after transport)
a row of `s`, then `κ_t {s} = 0`. -/
theorem kapCross_of_eq_zero_of_clash {μ ν : YoungDiagram} (h : nOf μ = nOf ν)
    (t : Tableau μ) (s : Tableau ν) (a b : Fin (nOf μ)) (hab : a ≠ b)
    (hcol : colPattern t a = colPattern t b)
    (hrow : rowPattern s (finCongr h a) = rowPattern s (finCongr h b)) :
    kapCross (k := k) h t (Mtab.of s) = 0 := by
  classical
  set τ : Perm (Fin (nOf μ)) := Equiv.swap a b with hτ
  -- `τ` stabilises the column pattern of `t`
  have hτcol : τ ∈ colStab t := by
    rw [mem_colStab]
    funext l
    show colPattern t (τ.symm l) = colPattern t l
    rw [hτ, Equiv.symm_swap]
    rcases eq_or_ne l a with rfl | hla
    · rw [Equiv.swap_apply_left]; exact hcol.symm
    · rcases eq_or_ne l b with rfl | hlb
      · rw [Equiv.swap_apply_right]; exact hcol
      · rw [Equiv.swap_apply_of_ne_of_ne hla hlb]
  -- the transported `τ` fixes the tabloid `{s}`
  have hτrow : Tabloid.mk ((transportPerm h τ) • s) = Tabloid.mk s := by
    rw [Tabloid.mk, Tabloid.mk, Quotient.eq, rowEquiv_iff]
    funext l
    show rowPattern ((transportPerm h τ) • s) l = rowPattern s l
    rw [rowPattern_smul]
    show rowPattern s ((transportPerm h τ).symm l) = rowPattern s l
    rw [transportPerm_symm_apply, hτ, Equiv.symm_swap]
    -- case on the pre-image of `l` under the relabelling
    set m : Fin (nOf μ) := (finCongr h).symm l with hm
    have hl : l = finCongr h m := by rw [hm]; simp
    rcases eq_or_ne m a with rfl | hma
    · rw [Equiv.swap_apply_left, hl]; exact hrow.symm
    · rcases eq_or_ne m b with rfl | hmb
      · rw [Equiv.swap_apply_right, hl]; exact hrow
      · rw [Equiv.swap_apply_of_ne_of_ne hma hmb, hl]
  rw [kapCross_of]
  refine Finset.sum_involution (fun π _ => π * ⟨τ, hτcol⟩) ?_ ?_ ?_ ?_
  · intro π _
    have hsgn : (Equiv.Perm.sign ((π * ⟨τ, hτcol⟩ : colStab t) : Perm (Fin (nOf μ))) : ℤ)
        = - (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) := by
      show (Equiv.Perm.sign ((π : Perm (Fin (nOf μ))) * τ) : ℤ) = _
      rw [Equiv.Perm.sign_mul, hτ, Equiv.Perm.sign_swap hab]
      push_cast; ring
    have hof : Mtab.of (k := k)
          ((transportPerm h ((π * ⟨τ, hτcol⟩ : colStab t) : Perm (Fin (nOf μ)))) • s)
        = Mtab.of (k := k) ((transportPerm h (π : Perm (Fin (nOf μ)))) • s) := by
      apply SpechtIrreducible.mtab_of_congr
      show Tabloid.mk ((transportPerm h ((π : Perm (Fin (nOf μ))) * τ)) • s) = _
      rw [map_mul, mul_smul, ← Tabloid.smul_mk, hτrow, Tabloid.smul_mk]
    rw [hsgn, hof, neg_smul]; abel
  · intro π _ _ hcontra
    have hx1 : (⟨τ, hτcol⟩ : colStab t) = 1 :=
      mul_left_cancel (a := π) (by rw [mul_one]; exact hcontra)
    have hτ1 : τ = 1 := by
      have := congrArg (Subtype.val) hx1; simpa using this
    rw [hτ] at hτ1
    exact hab (Equiv.swap_eq_one_iff.1 hτ1)
  · intro π _; exact Finset.mem_univ _
  · intro π _
    show (π * ⟨τ, hτcol⟩) * ⟨τ, hτcol⟩ = π
    rw [mul_assoc,
      show (⟨τ, hτcol⟩ : colStab t) * ⟨τ, hτcol⟩ = 1 from by
        apply Subtype.ext; show τ * τ = 1; rw [hτ, Equiv.swap_mul_self],
      mul_one]

/-! ## 3-bis. `κ_t` is idempotent up to `|C_t|`

`κ_t κ_t = |C_t| · κ_t`, because for fixed `π` the map `ρ ↦ πρ` is a bijection
of `C_t` and `sgn(π)sgn(ρ) = sgn(πρ)`.

This is what lets the assembly of Sagan 2.4.4 skip the extension of a
homomorphism `S^μ → M^ν` to all of `M^μ`. The textbook argument writes
`θ(e_t) = θ(κ_t {t}) = κ_t θ({t})`, which needs `θ` defined on the tabloid
`{t} ∉ S^μ`, hence needs `M^μ = S^μ ⊕ (S^μ)ᗮ`. But `κ_t e_t = |C_t| e_t` stays
inside `S^μ`, so equivariance of `θ` **on `S^μ` alone** already gives
`κ_t θ(e_t) = |C_t| θ(e_t) ≠ 0`, which is all the dominance argument needs.

`SpechtIrreducible.isCompl_specht_perp` is therefore not on the critical path
for `spechtIso_imp_dom_both`; it remains as the honest orthogonal decomposition. -/

/-- `κ_t ∘ κ_t = |C_t| · κ_t`. -/
theorem kapL_kapL (μ : YoungDiagram) (t : Tableau μ) (x : Mtab (k := k) μ) :
    SpechtIrreducible.kapL (k := k) μ t (SpechtIrreducible.kapL (k := k) μ t x)
      = (Fintype.card (colStab t)) • SpechtIrreducible.kapL (k := k) μ t x := by
  classical
  rw [SpechtIrreducible.kapL_apply (x := SpechtIrreducible.kapL (k := k) μ t x)]
  have hinner : ∀ π : colStab t,
      (Equiv.Perm.sign (π : Perm (Fin (nOf μ))) : ℤ) •
          Mtab.rep μ (π : Perm (Fin (nOf μ))) (SpechtIrreducible.kapL (k := k) μ t x)
        = SpechtIrreducible.kapL (k := k) μ t x := by
    intro π
    rw [SpechtIrreducible.kapL_apply, map_sum, Finset.smul_sum]
    refine Fintype.sum_equiv (Equiv.mulLeft π) _ _ (fun ρ => ?_)
    have hcoe : ((Equiv.mulLeft π ρ : colStab t) : Perm (Fin (nOf μ)))
        = (π : Perm (Fin (nOf μ))) * (ρ : Perm (Fin (nOf μ))) := rfl
    rw [hcoe, map_zsmul, smul_smul, ← SpechtIrreducible.rep_mul_apply,
      Equiv.Perm.sign_mul]
    congr 1
  rw [Finset.sum_congr rfl (fun π _ => hinner π), Finset.sum_const, Finset.card_univ]

/-- **`κ_t e_t = |C_t| · e_t`.** The polytabloid is an eigenvector of its own
column antisymmetriser. -/
theorem kapL_polytabloid (μ : YoungDiagram) (t : Tableau μ) :
    SpechtIrreducible.kapL (k := k) μ t (polytabloid (k := k) t)
      = (Fintype.card (colStab t)) • polytabloid (k := k) t := by
  conv_lhs => rw [← SpechtIrreducible.kapL_of_self (k := k) μ t]
  rw [kapL_kapL, SpechtIrreducible.kapL_of_self]

/-- A polytabloid is never zero over a characteristic-zero field: its
self-pairing is `|C_t|`. -/
theorem polytabloid_ne_zero {K : Type} [Field K] [CharZero K] (μ : YoungDiagram)
    (t : Tableau μ) : polytabloid (k := K) t ≠ 0 := by
  intro hzero
  have h := SpechtIrreducible.bilinM_polytabloid_self (k := K) μ t
  rw [hzero, map_zero] at h
  haveI : Nonempty (colStab t) := ⟨1⟩
  exact (Nat.cast_ne_zero.mpr Fintype.card_ne_zero) h.symm

/-! ## 4. Non-vanishing forces dominance

The contrapositive of §3 is exactly the hypothesis of Sagan Lemma 2.2.6. -/

/-- **`κ_t {s} ≠ 0 ⇒ μ ⊵ ν`** — Sagan's cross-shape dominance criterion in the
form Thm 2.4.4 consumes it.

The conclusion is definitionally `SpechtClassification.partitionDom μ ν`. -/
theorem dominance_of_kapCross_ne_zero {μ ν : YoungDiagram} (h : nOf μ = nOf ν)
    (t : Tableau μ) (s : Tableau ν)
    (hne : kapCross (k := k) h t (Mtab.of s) ≠ 0) :
    ∀ i, (∑ j ∈ Finset.range i, ν.rowLen j) ≤ ∑ j ∈ Finset.range i, μ.rowLen j := by
  refine SpechtCrossDominance.dominance_of_tableau_noclash h t s (fun a b hcol hrow => ?_)
  by_contra hab
  exact hne (kapCross_of_eq_zero_of_clash (k := k) h t s a b hab hcol hrow)

end QOU.BraidKnot.SpechtCrossKappa
