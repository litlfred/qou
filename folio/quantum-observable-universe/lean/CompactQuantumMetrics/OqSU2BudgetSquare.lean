import CompactQuantumMetrics.OqSU2Star

/-!
# The Cartan-field budget integrand is minus a square

Bean `qou-q3dc`. `OqSU2Star.lean` showed that for self-adjoint `a` the integrand
`Xa · Xa` is minus a *twisted* square, `−(T_{u⁻¹,u}(Xa))* · Xa`. This file removes
the twist. Write `u = s²`. For any linear functional `φ` that is invariant under
the torus scaling `T_{s⁻¹,s}`,

  `φ(Xa · Xa) = −φ(w* · w)`,  with `w = T_{s⁻¹,s}(Xa)`.

The twist `T_{u⁻¹,u}` splits as `T_{s⁻¹,s} ∘ T_{s⁻¹,s}`. One half moves through
the star, and the invariance of `φ` absorbs the other half.

## Results (sorry-free)

* `torusScale_inv_comp`: `T_{s⁻¹,s} ∘ T_{s,s⁻¹} = id`.
* `cartanField_sq_eq_neg_square`: the identity above, for any `s : Rˣ`, any
  `cinv`, any `a` with `a* = a`, and any `T_{s⁻¹,s}`-invariant `φ`.

## Consequence (conditional)

Two further facts are needed, and neither is proved here:

1. the Haar state `h` is `T_{s⁻¹,s}`-invariant;
2. `h` is positive, `h(w* w) ≥ 0`.

If both hold, then `h(Xa · Xa) ≤ 0` for every self-adjoint `a`. The budget
`−c·h(Du·Du)` then has the sign of `c`. For Woronowicz's Cartan field, `u = q⁻²`,
so `s = q⁻¹` is available, and `c = 1 − q⁻²`. No modular property of `h` is used.

## Not established

* Facts 1 and 2 above, which belong to the Haar-state work.
* The two off-diagonal directions (twist `q⁻¹`).
* Part A of `conj:regularity-breakdown` (bean `qou-pa7n`).

## References

- [woronowicz1987-twisted-su2] Woronowicz, *Twisted SU(2) group. An example of a
  non-commutative differential calculus*, Publ. RIMS 23 (1987) 117–181,
  Section 2, eqs. (2.1)–(2.8).
-/

namespace QOU.AlgebraicSubstrate.OqSU2

variable {R : Type*} [CommRing R] (q : Rˣ)

theorem torusScale_one : torusScaleAlgHom (R := R) q 1 1 = AlgHom.id R (OqSU2 R q) := by
  apply algHom_ext <;> simp [torusScaleAlgHom]

theorem torusScale_inv_comp (s : Rˣ) (x : OqSU2 R q) :
    torusScaleAlgHom q s⁻¹ s (torusScaleAlgHom q s s⁻¹ x) = x := by
  have h := AlgHom.congr_fun (torusScaleAlgHom_comp (R := R) q s⁻¹ s s s⁻¹) x
  rw [AlgHom.comp_apply, mul_inv_cancel, inv_mul_cancel, torusScale_one] at h
  exact h

theorem torusScale_sq (s : Rˣ) (x : OqSU2 R q) :
    torusScaleAlgHom q (s ^ 2)⁻¹ (s ^ 2) x =
      torusScaleAlgHom q s⁻¹ s (torusScaleAlgHom q s⁻¹ s x) := by
  have h := AlgHom.congr_fun (torusScaleAlgHom_comp (R := R) q s⁻¹ s s⁻¹ s) x
  rw [AlgHom.comp_apply] at h
  rw [h, ← mul_inv, ← pow_two]

/-- **The budget integrand is minus a square.** For `u = s²`, self-adjoint `a`, and a
functional `φ` invariant under `T_{s⁻¹,s}`, `φ(Xa · Xa) = −φ(w* w)` with
`w = T_{s⁻¹,s}(Xa)`. -/
theorem cartanField_sq_eq_neg_square (s : Rˣ) (cinv : R) (a : OqSU2 R q)
    (ha : compactStar q a = a) (φ : OqSU2 R q →ₗ[R] R)
    (hφ : ∀ x, φ (torusScaleAlgHom q s⁻¹ s x) = φ x) :
    φ (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q (s ^ 2)).toLinearMap)) a *
        leftInvOp q (cinv • ((counit q).toLinearMap -
          (diagCharAlgHom q (s ^ 2)).toLinearMap)) a) =
      -φ (compactStar q (torusScaleAlgHom q s⁻¹ s (leftInvOp q (cinv • ((counit q).toLinearMap -
          (diagCharAlgHom q (s ^ 2)).toLinearMap)) a)) *
        torusScaleAlgHom q s⁻¹ s (leftInvOp q (cinv • ((counit q).toLinearMap -
          (diagCharAlgHom q (s ^ 2)).toLinearMap)) a)) := by
  set X := leftInvOp q (cinv • ((counit q).toLinearMap -
    (diagCharAlgHom q (s ^ 2)).toLinearMap)) a
  set w := torusScaleAlgHom q s⁻¹ s X
  have hsq := cartanField_sq_selfAdjoint q (s ^ 2) cinv a ha
  -- the twisted factor: (T_{u⁻¹,u} X)* = T_{s,s⁻¹}(w*)
  have hstar : compactStar q (torusScaleAlgHom q (s ^ 2)⁻¹ (s ^ 2) X) =
      torusScaleAlgHom q s s⁻¹ (compactStar q w) := by
    rw [torusScale_sq, compactStar_torusScale, inv_inv]
  rw [hstar] at hsq
  have key : φ (torusScaleAlgHom q s s⁻¹ (compactStar q w) * X) = φ (compactStar q w * w) := by
    rw [← hφ, map_mul, torusScale_inv_comp]
  calc φ (X * X) = φ (-(torusScaleAlgHom q s s⁻¹ (compactStar q w) * X)) := by rw [hsq]
    _ = -φ (torusScaleAlgHom q s s⁻¹ (compactStar q w) * X) := by exact map_neg φ _
    _ = -φ (compactStar q w * w) := by rw [key]

end QOU.AlgebraicSubstrate.OqSU2
