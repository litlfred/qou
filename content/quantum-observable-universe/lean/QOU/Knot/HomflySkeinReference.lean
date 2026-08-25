import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum

set_option autoImplicit false

/-!
# QOU.Knot.HomflySkeinReference — the 2-strand skein reference, and a mirror

Bean `qou-7ue5`. Two places in `computations/` disagree about the HOMFLY of the
same braid closure, and this file settles *what kind* of disagreement it is.

* `homflypt_reference_qa._torus_homfly` derives `closure(σ₁ᵏ)` from the skein
  relation by hand and gives `P(σ₁³) = 2v² − v⁴ + v²z²` for the right trefoil.
* `homflypt_engine.homflypt_2strand` is a hardcoded table returning
  `−v⁻⁴ + 2v⁻² + v⁻²z²`, under the label "Right-hand trefoil".

## What is proved here

`skein` is the reference recurrence. `skein_two` and `skein_three` give its
closed forms, and `engine_k2_is_mirror`/`engine_k3_is_mirror` show that the
engine's two table entries are **exactly the reference evaluated at the HOMFLY
mirror substitution** `(v, z) ↦ (v⁻¹, −z)`.

So the engine is not wrong about the polynomial — it computes the *left*
trefoil and the *negative* Hopf link, while labelling them "Right-hand" and
"(positive)". The discrepancy is a crossing-sign convention, nothing deeper.

**The `z`-sign is the part that is easy to get wrong, and this file exists
partly because I did.** At `k = 3` the two agree under plain `v ↦ v⁻¹`,
because `z` occurs there only as `z²`; that coincidence does not survive to
`k = 2`, where the reference's `+vz` must become `−v⁻¹z`.
`plain_inversion_ne_mirror` exhibits a concrete rational point at which the
naive substitution and the true mirror differ, so the accident cannot be
mistaken for a rule.

## What is NOT proved

Everything geometric. That switching a crossing of `σ₁ᵏ` yields `σ₁ᵏ⁻²` and
smoothing it yields `σ₁ᵏ⁻¹`; that `closure(σ₁⁰)` is the 2-component unlink and
`closure(σ₁¹)` the unknot; and that HOMFLY exists and is an ambient-isotopy
invariant at all — all of these are *built into* the definition of `skein`
rather than derived. This file proves the algebra downstream of the skein
relation, which is precisely the layer the two `computations/` files disagree
on. It says nothing about which convention the corpus *should* adopt; that
remains an owner call on `qou-7ue5`.

Base ring is a generic field per §7c — the content is algebraic and no
archimedean construct appears, so nothing here mentions `ℝ`. The concrete
counterexample is over `ℚ`.

## References

- [lickorish1997] W. B. R. Lickorish, *An Introduction to Knot Theory*, ch. 15. https://doi.org/10.1007/978-1-4612-0691-0
- [manuscript] `computations/homflypt_reference_qa.py` (`_torus_homfly`), `computations/homflypt_engine.py` (`homflypt_2strand`).
-/

namespace QOU.Knot.HomflySkeinReference

variable {R : Type*} [Field R]

/-- The 2-strand skein recurrence for `P(closure(σ₁ⁿ))`, in the Lickorish
convention `v⁻¹P(L₊) − vP(L₋) = zP(L₀)`. Resolving one positive crossing gives
`P(L₊) = v²P(L₋) + vzP(L₀)`; on `σ₁ⁿ` the switched diagram is `σ₁ⁿ⁻²` and the
smoothed one is `σ₁ⁿ⁻¹`. Seeds are the 2-component unlink and the unknot. -/
noncomputable def skein (v z : R) : ℕ → R
  | 0 => (v⁻¹ - v) / z
  | 1 => 1
  | (n + 2) => v ^ 2 * skein v z n + v * z * skein v z (n + 1)

variable (v z : R)

/-- The positive Hopf link. -/
theorem skein_two (hz : z ≠ 0) :
    skein v z 2 = v * z + (v - v ^ 3) / z := by
  show v ^ 2 * skein v z 0 + v * z * skein v z 1 = _
  show v ^ 2 * ((v⁻¹ - v) / z) + v * z * 1 = _
  field_simp
  ring

/-- The right-handed trefoil. Note `v⁻¹` has vanished: the closed form is a
genuine polynomial, which is why `hv` is needed to get there. -/
theorem skein_three (hv : v ≠ 0) (hz : z ≠ 0) :
    skein v z 3 = 2 * v ^ 2 - v ^ 4 + v ^ 2 * z ^ 2 := by
  show v ^ 2 * skein v z 1 + v * z * skein v z 2 = _
  rw [skein_two v z hz]
  show v ^ 2 * 1 + v * z * (v * z + (v - v ^ 3) / z) = _
  field_simp
  ring

/-- **The engine's `k = 2` entry is the reference at the mirror.**
`homflypt_2strand` returns `v⁻³z⁻¹ − v⁻¹z⁻¹ − v⁻¹z` labelled "Hopf link
(positive)"; that is `skein` evaluated at `(v⁻¹, −z)`, i.e. the *negative*
Hopf link. -/
theorem engine_k2_is_mirror (hv : v ≠ 0) (hz : z ≠ 0) :
    v⁻¹ ^ 3 / z - v⁻¹ / z - v⁻¹ * z = skein v⁻¹ (-z) 2 := by
  rw [skein_two v⁻¹ (-z) (neg_ne_zero.mpr hz)]
  field_simp
  ring

/-- **The engine's `k = 3` entry is the reference at the mirror.**
`homflypt_2strand` returns `−v⁻⁴ + 2v⁻² + v⁻²z²` labelled "Right-hand
trefoil"; that is `skein` at `(v⁻¹, −z)`, i.e. the *left*-handed trefoil. -/
theorem engine_k3_is_mirror (hv : v ≠ 0) (hz : z ≠ 0) :
    -(v⁻¹ ^ 4) + 2 * v⁻¹ ^ 2 + v⁻¹ ^ 2 * z ^ 2 = skein v⁻¹ (-z) 3 := by
  rw [skein_three v⁻¹ (-z) (inv_ne_zero hv) (neg_ne_zero.mpr hz)]
  ring

/-- **The `z`-sign is not optional.** Inverting `v` alone is *not* the mirror:
at `v = 2, z = 1` the naive substitution and the true mirror disagree already
at `k = 2`. The agreement one sees at `k = 3` is an artefact of `z` occurring
there only as `z²`, and must not be read as a rule. -/
theorem plain_inversion_ne_mirror :
    skein ((2 : ℚ)⁻¹) 1 2 ≠ skein ((2 : ℚ)⁻¹) (-1) 2 := by
  rw [skein_two _ _ one_ne_zero, skein_two _ _ (by norm_num : (-1 : ℚ) ≠ 0)]
  norm_num

/-- At `k = 3`, by contrast, they *do* agree — the accident, stated so it is
on the record next to the `k = 2` refutation rather than discovered again. -/
theorem plain_inversion_eq_mirror_at_three :
    skein ((2 : ℚ)⁻¹) 1 3 = skein ((2 : ℚ)⁻¹) (-1) 3 := by
  rw [skein_three _ _ (by norm_num) one_ne_zero,
      skein_three _ _ (by norm_num) (by norm_num : (-1 : ℚ) ≠ 0)]
  norm_num

end QOU.Knot.HomflySkeinReference
