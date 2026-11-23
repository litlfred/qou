import QOU.Hecke.TauStructureConstants
import QOU.MathlibExt.CasimirBasisIndependence

/-!
# QOU.Hecke.TauDualBasis — the `τ`-dual of the `T_w` basis is `q^{-ℓ(w)} T_{w⁻¹}`

An immediate corollary of `tau_Tw_mul_Tw`, and the bridge every further
Schur-element result goes through.

`QOU.Hecke.TauStructureConstants.tau_Tw_mul_Tw` says
`τ(T_v T_w) = δ_{w,v⁻¹} q^{ℓ(v)}`.  Read as a pairing, that already exhibits the
dual family: scale `T_{w⁻¹}` by `q^{-ℓ(w)}` and the pairing becomes `δ_{v,w}`.

## Why this is the next brick and not a footnote

For a symmetric algebra, dual bases are what turn character theory into
computation.  The classical route to the Schur element runs

  dual basis  →  the Casimir `Σ_w b_w b_w^∨` is central  →  it acts on the
  `λ`-block by the scalar `s_λ`  →  `s_λ` as a character sum  →  (Wenzl) the
  hook-length product.

The first **two** steps are here.  The block scalar is not.  The rest is deliberately not claimed: identifying
`s_λ` with `∏_x (1 - Q^{h(x)})`-type products for **all** `n` is Wenzl's
theorem, and `computations/hecke/tau_weights_vs_wenzl_schur_probe.py` verifies
that identification exactly only for `n ≤ 3` — enough to pin the statement, not
to prove it.

## What is proved

* `TwDual` — the candidate dual family `q^{-ℓ(w)} · T_{w⁻¹}`.
* `tau_Tw_mul_TwDual` — `τ(T_v · T^∨_w) = δ_{v,w}`, for `q ≠ 0`.
* `tau_TwDual_mul_Tw` — the same on the other side, since `τ` is a trace.
* `TwDual_apply_ne` — the off-diagonal half holds with **no** hypothesis on `q`;
  only the diagonal `q^{-ℓ}·q^{ℓ} = 1` needs `q ≠ 0`.
* `TwDualBasis` — the dual family **is** a basis, for elementary reasons: it is
  `basisTwOfField` reindexed along the involution `w ↦ w⁻¹` and rescaled by
  units.  No nondegeneracy argument is needed to get it.
* `repr_eq_tau_mul_TwDual` — **coordinates are values of `τ`**: the `T_w`
  coefficient of `y` is `τ(y · T^∨_w)`.  This is the practical content of
  duality; it turns a coefficient into one evaluation of the trace.
* `sum_tau_mul_TwDual_smul_Tw` / `sum_tau_Tw_mul_smul_TwDual` — the two
  expansions, one on each family.
* `casimir` and `mul_casimir_comm` — **`Σ_w T_w T^∨_w` is central.**  Both
  sides expand to the same double sum over `(v, w)`; the coefficients agree by
  `tau_mul_comm`, which is precisely where the *trace* property is spent.
  Without it the two double sums are different objects.

`Ref: [geckpfeiffer2000]` §7.1–7.2 — attribution.
-/

namespace QOU.Hecke.TwBasis

open QOU.Hecke.SymmetricCoxeter

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-- **The `τ`-dual of `T_w`**: `q^{-ℓ(w)} · T_{w⁻¹}`. -/
noncomputable def TwDual (w : Equiv.Perm (Fin (n + 1))) :
    QOU.Hecke.IwahoriHecke K q n :=
  (q ^ (permCoxeterSystem n).length w)⁻¹ • Tw K q n w⁻¹

/-- The **off-diagonal** half of duality, with no hypothesis on `q`. -/
theorem TwDual_apply_ne {v w : Equiv.Perm (Fin (n + 1))} (h : v ≠ w) :
    tau K q n (Tw K q n v * TwDual K q n w) = 0 := by
  rw [TwDual, mul_smul_comm, map_smul, tau_Tw_mul_Tw, smul_eq_mul]
  rw [if_neg (fun hc => h (by simpa using (congrArg (·⁻¹) hc).symm)), mul_zero]

/-- **`τ(T_v · T^∨_w) = δ_{v,w}`** — the dual-basis property.

    Only the diagonal case uses `q ≠ 0`, to cancel `q^{-ℓ(w)}` against
    `q^{ℓ(w)}`; the vanishing off the diagonal is unconditional
    (`TwDual_apply_ne`). -/
theorem tau_Tw_mul_TwDual (hq : q ≠ 0) (v w : Equiv.Perm (Fin (n + 1))) :
    tau K q n (Tw K q n v * TwDual K q n w) = if v = w then 1 else 0 := by
  by_cases h : v = w
  · subst h
    rw [TwDual, mul_smul_comm, map_smul, tau_Tw_mul_Tw, smul_eq_mul, if_pos rfl,
      if_pos rfl]
    exact inv_mul_cancel₀ (pow_ne_zero _ hq)
  · rw [if_neg h]
    exact TwDual_apply_ne K q n h

/-- The mirror statement, from `tau_mul_comm`. -/
theorem tau_TwDual_mul_Tw (hq : q ≠ 0) (v w : Equiv.Perm (Fin (n + 1))) :
    tau K q n (TwDual K q n w * Tw K q n v) = if v = w then 1 else 0 := by
  rw [tau_mul_comm, tau_Tw_mul_TwDual K q n hq]

/-! ### It is a basis, and it computes coordinates

`T^∨` is the `T_w` basis reindexed by `w ↦ w⁻¹` and rescaled by units, so it is
a basis for elementary reasons — no nondegeneracy argument is needed.  What the
duality then buys is that the `T_w`-coordinates of any element are *values of
`τ`*, which is what makes character computations finite. -/

/-- **The dual family is a basis.**  `Basis.reindex` along `w ↦ w⁻¹` (an
    involution, so its own inverse) followed by `Basis.unitsSMul`. -/
noncomputable def TwDualBasis (hq : q ≠ 0) :
    Module.Basis (Equiv.Perm (Fin (n + 1))) K (QOU.Hecke.IwahoriHecke K q n) :=
  ((basisTwOfField K q n).reindex (Equiv.inv (Equiv.Perm (Fin (n + 1))))).unitsSMul
    fun w => (Units.mk0 (q ^ (permCoxeterSystem n).length w) (pow_ne_zero _ hq))⁻¹

@[simp] theorem coe_TwDualBasis (hq : q ≠ 0) :
    ⇑(TwDualBasis K q n hq) = TwDual K q n := by
  funext w
  rw [TwDualBasis, Module.Basis.unitsSMul_apply, Module.Basis.reindex_apply,
    coe_basisTwOfField, TwDual]
  simp [Units.smul_def]

/-- **Coordinates are values of `τ`**: the `T_w`-coordinate of `y` is
    `τ(y · T^∨_w)`.

    This is the practical content of duality — it turns "what is the coefficient
    of `T_w` in `y`" into a single evaluation of the trace. -/
theorem repr_eq_tau_mul_TwDual (hq : q ≠ 0) (y : QOU.Hecke.IwahoriHecke K q n)
    (w : Equiv.Perm (Fin (n + 1))) :
    (basisTwOfField K q n).repr y w = tau K q n (y * TwDual K q n w) := by
  classical
  conv_rhs =>
    rw [← Module.Basis.sum_repr (basisTwOfField K q n) y]
  rw [Finset.sum_mul, map_sum]
  rw [Finset.sum_eq_single w]
  · rw [coe_basisTwOfField, smul_mul_assoc, map_smul, smul_eq_mul,
      tau_Tw_mul_TwDual K q n hq, if_pos rfl, mul_one]
  · intro v _ hv
    rw [coe_basisTwOfField, smul_mul_assoc, map_smul, smul_eq_mul,
      tau_Tw_mul_TwDual K q n hq, if_neg hv, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ w) h

/-- **The expansion.**  Every element is its `τ`-coordinates against the dual
    family, on the `T_w` basis. -/
theorem sum_tau_mul_TwDual_smul_Tw (hq : q ≠ 0) (y : QOU.Hecke.IwahoriHecke K q n) :
    ∑ w, tau K q n (y * TwDual K q n w) • Tw K q n w = y := by
  conv_rhs => rw [← Module.Basis.sum_repr (basisTwOfField K q n) y]
  exact Finset.sum_congr rfl fun w _ => by
    rw [repr_eq_tau_mul_TwDual K q n hq, coe_basisTwOfField]

/-- The dual-side coordinates: expanding on `T^∨` reads off `τ(T_w · y)`. -/
theorem TwDualBasis_repr (hq : q ≠ 0) (y : QOU.Hecke.IwahoriHecke K q n)
    (w : Equiv.Perm (Fin (n + 1))) :
    (TwDualBasis K q n hq).repr y w = tau K q n (Tw K q n w * y) := by
  classical
  conv_rhs => rw [← Module.Basis.sum_repr (TwDualBasis K q n hq) y]
  rw [Finset.mul_sum, map_sum, Finset.sum_eq_single w]
  · rw [coe_TwDualBasis, mul_smul_comm, map_smul, smul_eq_mul,
      tau_Tw_mul_TwDual K q n hq, if_pos rfl, mul_one]
  · intro v _ hv
    rw [coe_TwDualBasis, mul_smul_comm, map_smul, smul_eq_mul,
      tau_Tw_mul_TwDual K q n hq, if_neg (Ne.symm hv), mul_zero]
  · intro h
    exact absurd (Finset.mem_univ w) h

/-- The **mirror expansion**, on the dual family. -/
theorem sum_tau_Tw_mul_smul_TwDual (hq : q ≠ 0) (y : QOU.Hecke.IwahoriHecke K q n) :
    ∑ w, tau K q n (Tw K q n w * y) • TwDual K q n w = y := by
  conv_rhs => rw [← Module.Basis.sum_repr (TwDualBasis K q n hq) y]
  exact Finset.sum_congr rfl fun w _ => by
    rw [TwDualBasis_repr K q n hq, coe_TwDualBasis]

/-! ### The Casimir

`c = Σ_w T_w T^∨_w`.  For a symmetric algebra this is central, and on a split
semisimple quotient it acts on the `λ`-block by the scalar `s_λ` — which is the
classical route from dual bases to Schur elements.  **Centrality is proved
here; the block scalar is not.** -/

/-- **The Casimir element** `Σ_w T_w · T^∨_w`. -/
noncomputable def casimir : QOU.Hecke.IwahoriHecke K q n :=
  ∑ w, Tw K q n w * TwDual K q n w

/-- **The Casimir is central.**

    Both sides expand to the same double sum over `(v, w)`, with coefficient
    `τ(a T_w T^∨_v)` on the left and `τ(T_w T^∨_v a)` on the right; those agree
    by `tau_mul_comm`, which is exactly where the *trace* property is spent.
    Without it the two double sums would be different objects. -/
theorem mul_casimir_comm (hq : q ≠ 0) (a : QOU.Hecke.IwahoriHecke K q n) :
    a * casimir K q n = casimir K q n * a := by
  classical
  have hL : a * casimir K q n
      = ∑ w, ∑ v, tau K q n (a * Tw K q n w * TwDual K q n v) •
          (Tw K q n v * TwDual K q n w) := by
    rw [casimir, Finset.mul_sum]
    refine Finset.sum_congr rfl fun w _ => ?_
    rw [← mul_assoc]
    conv_lhs => rw [← sum_tau_mul_TwDual_smul_Tw K q n hq (a * Tw K q n w)]
    rw [Finset.sum_mul]
    exact Finset.sum_congr rfl fun v _ => by rw [smul_mul_assoc]
  have hR : casimir K q n * a
      = ∑ w, ∑ v, tau K q n (Tw K q n v * (TwDual K q n w * a)) •
          (Tw K q n w * TwDual K q n v) := by
    rw [casimir, Finset.sum_mul]
    refine Finset.sum_congr rfl fun w _ => ?_
    rw [mul_assoc]
    conv_lhs => rw [← sum_tau_Tw_mul_smul_TwDual K q n hq (TwDual K q n w * a)]
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun v _ => by rw [mul_smul_comm]
  rw [hL, hR, Finset.sum_comm]
  refine Finset.sum_congr rfl fun w _ => Finset.sum_congr rfl fun v _ => ?_
  congr 1
  calc tau K q n (a * Tw K q n v * TwDual K q n w)
      = tau K q n (a * (Tw K q n v * TwDual K q n w)) := by rw [mul_assoc]
    _ = tau K q n (Tw K q n v * TwDual K q n w * a) := tau_mul_comm K q n _ _
    _ = tau K q n (Tw K q n v * (TwDual K q n w * a)) := by rw [mul_assoc]

/-- **Any dual pair computes the same Casimir.**

    Instantiates `QOU.MathlibExt.casimir_eq_of_expansions` with the `T_w` pair
    on one side; the caller supplies only the *other* pair's left-expansion.
    This is what makes `QOU.MathlibExt.CasimirBlockScalar` — which computes a
    Casimir in the matrix-unit basis of a product of matrix algebras — say
    something about `casimir` itself, once the matrix units are transported
    along a splitting. -/
theorem casimir_eq_of_dual_pair (hq : q ≠ 0) {κ : Type*} [Fintype κ]
    (d d' : κ → QOU.Hecke.IwahoriHecke K q n)
    (hd : ∀ y : QOU.Hecke.IwahoriHecke K q n,
      ∑ p, tau K q n (d p * y) • d' p = y) :
    ∑ p, d p * d' p = casimir K q n :=
  QOU.MathlibExt.casimir_eq_of_expansions (tau K q n) (Tw K q n) (TwDual K q n) d d'
    (sum_tau_mul_TwDual_smul_Tw K q n hq) hd

end QOU.Hecke.TwBasis
