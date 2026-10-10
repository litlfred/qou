import QOU.SchurWeyl.HeckeMatsumoto

/-!
# QOU.SchurWeyl.HeckeMultiplicationRule — `T_w σ_i` in the standard basis

With `T_w := stdElt m w` (well defined on reduced words by `HeckeMatsumoto.matsumoto`), the right
action of a generator is

```
T_w σ_i = T_{w s_i}                              if w(i) < w(i+1)   (ascent),
T_w σ_i = (q − qi) T_w + (q·qi) T_{w s_i}        if w(i) > w(i+1)   (descent).
```

This is the defining multiplication rule of the Iwahori–Hecke algebra in the `T_w` basis.

## Proof

The ascent case is `HeckeMatsumoto.stdElt_mul_σ_of_ascent` together with
`ninv_mul_adjT_of_lt`.  At a descent, `v := w s_i` has `v(i) < v(i+1)`, so `T_w = T_v σ_i` by the
ascent case, and the quadratic relation `σ_i² = (q − qi) σ_i + q·qi` (`Hecke.σ_quadratic`) gives
`T_w σ_i = T_v σ_i² = (q − qi) T_w + q·qi · T_v`.

## Base ring (§7c)

Generic `[CommRing K]`, with `q, qi : K` free.  Nothing archimedean.

LaTeX label: `thm:hecke-multiplication-rule`

-- Ref: [geckpfeiffer2000] https://doi.org/10.1093/oso/9780198502500.001.0001 (Thm 4.4.6: the multiplication rule of the `T_w` basis)
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke HeckeInclusion Equiv

variable {K : Type*} [CommRing K] {q qi : K}

/-- **The ascent case**: `T_w σ_i = T_{w s_i}` when `w(i) < w(i+1)`. -/
theorem stdElt_mul_σ_of_lt (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m)
    (h : w i.castSucc < w i.succ) :
    stdElt (K := K) (q := q) (qi := qi) m w * σ K q qi m i = stdElt m (w * adjT i) :=
  stdElt_mul_σ_of_ascent m w i (ninv_mul_adjT_of_lt w i h)

/-- **The descent case**: `T_w σ_i = (q − qi) T_w + (q·qi) T_{w s_i}` when `w(i) > w(i+1)`. -/
theorem stdElt_mul_σ_of_gt (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m)
    (h : w i.succ < w i.castSucc) :
    stdElt (K := K) (q := q) (qi := qi) m w * σ K q qi m i
      = (q - qi) • stdElt m w + (q * qi) • stdElt m (w * adjT i) := by
  set v := w * adjT i
  have hv : v i.castSucc < v i.succ := by
    simpa [v, adjT, Perm.mul_apply, swap_apply_left, swap_apply_right] using h
  have hvw : v * adjT i = w := by rw [mul_assoc, adjT_mul_self, mul_one]
  have hw : stdElt (K := K) (q := q) (qi := qi) m w = stdElt m v * σ K q qi m i := by
    rw [stdElt_mul_σ_of_lt m v i hv, hvw]
  rw [hw, mul_assoc, σ_quadratic, mul_add, mul_smul_comm, mul_smul_comm, mul_one]

/-- **The multiplication rule of the `T_w` basis.** -/
theorem stdElt_mul_σ (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m) :
    stdElt (K := K) (q := q) (qi := qi) m w * σ K q qi m i
      = if w i.castSucc < w i.succ then stdElt m (w * adjT i)
        else (q - qi) • stdElt m w + (q * qi) • stdElt m (w * adjT i) := by
  split_ifs with h
  · exact stdElt_mul_σ_of_lt m w i h
  · have hne : w i.castSucc ≠ w i.succ := w.injective.ne (Fin.castSucc_lt_succ i).ne
    exact stdElt_mul_σ_of_gt m w i (lt_of_le_of_ne (not_lt.mp h) hne.symm)

end HeckeCoset
end QOU.SchurWeyl
