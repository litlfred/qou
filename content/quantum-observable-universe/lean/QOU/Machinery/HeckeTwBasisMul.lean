import QOU.Machinery.HeckeGeneralRankQuadratic

/-!
# QOU.Machinery.HeckeTwBasisMul — the T_w standard-basis structure constants, all ranks

`HeckeGeneralRankQuadratic.mulSimple` is the right action of the Hecke
generator `T_{sᵢ}` on the function module `W → R` of an arbitrary Coxeter
system, and `mulSimple_quadratic` proves `σᵢ² = h·σᵢ + 1` at every rank.
This file identifies that action, **on the standard basis vectors**
`e_w = Pi.single w 1`, as the classical **Iwahori–Hecke `T_w`-basis
multiplication rule** — the structure constants of `H_n(q)` for all `n` at
once:

  `T_w · T_{sᵢ} = T_{w·sᵢ}`                    if `ℓ(w·sᵢ) > ℓ(w)`   (ascent)
  `T_w · T_{sᵢ} = T_{w·sᵢ} + h · T_w`          if `ℓ(w·sᵢ) < ℓ(w)`   (descent)

(the `h` normalization of `σᵢ² = h·σᵢ + 1`; at `w = sᵢ` the descent case is
`T_{sᵢ}² = T_1 + h·T_{sᵢ} = 1 + h·σᵢ`, consistent).

Contents (all sorry-free, rank-agnostic over any `CoxeterSystem`):

* `mulSimple_single` — the combined length rule on `e_w`.
* `mulSimple_single_ascent` / `mulSimple_single_descent` — the two cases.
* `mulSimple_single_one` — `T_1 · T_{sᵢ} = T_{sᵢ}`: the generator *is* the
  basis vector at `sᵢ` (`ℓ(sᵢ) = 1 > 0`).

This names the T_w basis's structure constants uniformly; it does **not**
close the open all-ranks keystones (Gram symmetry / Tits faithfulness),
which stay honest hypotheses elsewhere.
-/

namespace QOU.Machinery.HeckeGeneral

open CoxeterSystem

variable {B W : Type*} [Group W] [DecidableEq W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)
variable {R : Type*} [CommRing R]

/-- The standard basis vector `T_w = e_w` of the Hecke function module `W → R`. -/
def tw (w : W) : W → R := Pi.single w (1 : R)

omit [Group W] in
@[simp] lemma tw_apply (w u : W) : (tw w : W → R) u = if u = w then 1 else 0 := by
  simp only [tw, Pi.single_apply]

/-- **The T_w-basis multiplication rule, every rank.** The generator action
`mulSimple` on the standard basis vector `T_w` is the classical Iwahori–Hecke
length rule: `T_w · T_{sᵢ} = T_{w·sᵢ} + [ℓ(w·sᵢ) < ℓ(w)]·h·T_w`. -/
theorem mulSimple_tw (h : R) (i : B) (w : W) :
    mulSimple cs h i (tw w)
      = tw (w * cs.simple i)
        + (if cs.length (w * cs.simple i) < cs.length w then h else 0) • (tw w : W → R) := by
  funext u
  have hs : cs.simple i * cs.simple i = 1 := cs.simple_mul_simple_self i
  have hiff : (u * cs.simple i = w) ↔ (u = w * cs.simple i) := by
    constructor
    · intro hh; rw [← hh, mul_assoc, hs, mul_one]
    · intro hh; rw [hh, mul_assoc, hs, mul_one]
  simp only [mulSimple, Pi.add_apply, Pi.smul_apply, smul_eq_mul, tw_apply]
  by_cases huw : u = w
  · subst huw
    by_cases hlen : cs.length (u * cs.simple i) < cs.length u <;>
      simp [hiff, hlen]
  · by_cases hlen : cs.length (u * cs.simple i) < cs.length u <;>
      simp [huw, hlen, hiff]

/-- **Ascent case**: if `ℓ(w·sᵢ) > ℓ(w)` then `T_w · T_{sᵢ} = T_{w·sᵢ}`. -/
theorem mulSimple_tw_ascent (h : R) (i : B) (w : W)
    (hasc : cs.length w < cs.length (w * cs.simple i)) :
    mulSimple cs h i (tw w) = (tw (w * cs.simple i) : W → R) := by
  rw [mulSimple_tw]
  have : ¬ cs.length (w * cs.simple i) < cs.length w := by omega
  simp [this]

/-- **Descent case**: if `ℓ(w·sᵢ) < ℓ(w)` then `T_w · T_{sᵢ} = T_{w·sᵢ} + h·T_w`. -/
theorem mulSimple_tw_descent (h : R) (i : B) (w : W)
    (hdesc : cs.length (w * cs.simple i) < cs.length w) :
    mulSimple cs h i (tw w)
      = tw (w * cs.simple i) + h • (tw w : W → R) := by
  rw [mulSimple_tw, if_pos hdesc]

/-- **Generator = basis vector at `sᵢ`.** `T_1 · T_{sᵢ} = T_{sᵢ}`: acting on the
identity basis vector `T_1` yields `T_{sᵢ}`, since `ℓ(sᵢ) = 1 > 0 = ℓ(1)`. -/
theorem mulSimple_tw_one (h : R) (i : B) :
    mulSimple cs h i (tw (1 : W)) = (tw (cs.simple i) : W → R) := by
  have hasc : cs.length (1 : W) < cs.length ((1 : W) * cs.simple i) := by
    rw [one_mul, cs.length_simple]
    simp [cs.length_one]
  rw [mulSimple_tw_ascent cs h i 1 hasc, one_mul]

end QOU.Machinery.HeckeGeneral
