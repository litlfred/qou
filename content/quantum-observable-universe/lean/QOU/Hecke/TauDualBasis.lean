import QOU.Hecke.TauStructureConstants

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

Only the first step is here.  The rest is deliberately not claimed: identifying
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

end QOU.Hecke.TwBasis
