import QOU.SchurWeyl.SeminormalParam

/-!
# `QOU.SchurWeyl.Orbit3Braid` — the size-`3` `S₃`-orbit braid identity (bean `qou-gjg6`)

The braid relation for the general-`λ` seminormal representation reduces to one identity
per `⟨s_k, s_{k+1}⟩`-orbit of `SYT λ`.  Orbits come in sizes `1`, `2`, `3` and `6`; the
generic size-`6` case is `Orbit6Braid`, the size-`1` and size-`2` cases reduce to the
scalar eigenvalues and the `2 × 2` template, and **this file covers size `3`**.

## What a size-`3` orbit is

The standard fillings of a **domino together with a disjoint cell**.  The domino's two
cells are adjacent, which forces their relative order, so only `3!/2! = 3` of the six
assignments are standard.  Writing the domino as `A, B` and the disjoint cell as `C`, the
three fillings of `{k, k+1, k+2}` with `entry A < entry B` are

  `0 : A=k,   B=k+1, C=k+2`   `1 : A=k,   B=k+2, C=k+1`   `2 : A=k+1, B=k+2, C=k`

and the two generators act as

* `σ_k`     — fixes filling `0` with the **scalar** `sc`, and a `2 × 2` block on `{1,2}`;
* `σ_{k+1}` — a `2 × 2` block on `{0,1}`, and fixes filling `2` with the same scalar `sc`.

Each generator is therefore (scalar) ⊕ (`2 × 2` block) — but *on different summands*,
which is exactly why the orbit is `3`-dimensional and not reducible to the `2 × 2` case,
the same phenomenon as at size `6`.

The scalar is the size-`1` eigenvalue of the domino: `q` when the domino lies in a row
(axial distance `+1`) and `-q⁻¹` when it lies in a column (`-1`), per
`axialDist_of_sameRow` / `axialDist_of_sameCol` and `seminormalParam_one` / `_neg_one`.

## The two hypotheses, and why both are needed

`hsc : sc * sc = c * sc + 1` — the scalar must itself satisfy the Hecke quadratic, i.e.
`sc` is a root of `X² - cX - 1`, which for `c = q - q⁻¹` means exactly `sc ∈ {q, -q⁻¹}`.
Without it even the *quadratic* relation fails, since the scalar block would not satisfy
`σ² = cσ + 1`.

`hrel : a₂ * (sc * (sc - a₁)) = a₁` — the two block parameters are not independent.  They
are `a(d)` and `a(d ∓ 1)` for the same underlying axial distance `d` (the domino shifts the
distance by one), and eliminating `d` leaves exactly this relation.  It is uniform across
both domino orientations once written in terms of `sc`.

Both were found by exact-rational search, and both are **derived** at the foot of this
file (`hsc_row` / `hsc_col`, `hrel_row` / `hrel_col`) for the actual seminormal
parameters — the role `seminormalParam_mul_rel` plays for `Orbit6Braid`.  So the identity
is a statement about the Hoefsmit matrices, not about abstract `3 × 3` arrays.

## Scope

This is the identity for one orbit, in an explicit basis ordering, exactly as
`Orbit6Braid` is.  Assembling the orbits of `SYT λ` into the representation — the
enumeration, the orbit-size classification, and the per-orbit basis correspondence — is
step (ii) of the general construction and remains open under bean `qou-gjg6`.

Refs:
- [hoefsmit1974] Hoefsmit, PhD thesis (UBC 1974) — the seminormal form.
- [ram1997] Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  https://doi.org/10.1112/S0024611597000373 — the axial-distance formulas.
-/

set_option maxHeartbeats 800000

namespace QOU.SchurWeyl

open Matrix

namespace Orbit3

variable (c sc a₁ a₂ : ℝ)

/-- `ρ(σ_k)` on a size-`3` orbit: the scalar `sc` on filling `0`, a `2 × 2` block on
`{1,2}` with parameter `a₁`.  Defined by a match on the index values rather than as a
`!![…]` literal — see the performance note in `Orbit6Braid`. -/
noncomputable def genA : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.of fun i j =>
    match (i : ℕ), (j : ℕ) with
    | 0, 0 => sc
    | 1, 1 => a₁
    | 1, 2 => 1
    | 2, 1 => 1 + a₁ * (c - a₁)
    | 2, 2 => c - a₁
    | _, _ => 0

/-- `ρ(σ_{k+1})` on the same orbit: a `2 × 2` block on `{0,1}` with parameter `a₂`, and the
scalar `sc` on filling `2`.  The block sits on a **different** summand from `genA`'s — that
is what makes the orbit irreducible to the `2 × 2` case. -/
noncomputable def genB : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.of fun i j =>
    match (i : ℕ), (j : ℕ) with
    | 0, 0 => a₂
    | 0, 1 => 1
    | 1, 0 => 1 + a₂ * (c - a₂)
    | 1, 1 => c - a₂
    | 2, 2 => sc
    | _, _ => 0

/-- **The size-`3` orbit braid identity (Yang–Baxter).**

`ρ(σ_k) ρ(σ_{k+1}) ρ(σ_k) = ρ(σ_{k+1}) ρ(σ_k) ρ(σ_{k+1})` on a size-`3` orbit — a domino
plus a disjoint cell — given that the scalar satisfies the Hecke quadratic and that the two
block parameters satisfy the relation forced by their shared axial distance. -/
theorem genA_genB_braid (hsc : sc * sc = c * sc + 1) (hs : sc * (sc - a₁) ≠ 0)
    (hrel : a₂ * (sc * (sc - a₁)) = a₁) :
    genA c sc a₁ * genB c sc a₂ * genA c sc a₁
      = genB c sc a₂ * genA c sc a₁ * genB c sc a₂ := by
  have hsc0 : sc ≠ 0 := fun h => hs (by rw [h]; ring)
  have hd : sc - a₁ ≠ 0 := fun h => hs (by rw [h]; ring)
  have hc : c = (sc * sc - 1) / sc := by field_simp; linarith [hsc]
  have ha₂ : a₂ = a₁ / (sc * (sc - a₁)) := by
    field_simp; linear_combination hrel
  subst hc
  subst ha₂
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp only [genA, genB, Matrix.mul_apply, Fin.sum_univ_three, Matrix.of_apply] <;>
    norm_num <;> field_simp <;> ring

/-- **The Hecke quadratic relation on the orbit** for `ρ(σ_k)`.  The `2 × 2` block gives it
by Cayley–Hamilton (trace `c`, determinant `-1`); the scalar entry needs `hsc`, which is
precisely the statement that `sc` is an eigenvalue of a Hecke generator. -/
theorem genA_quadratic (hsc : sc * sc = c * sc + 1) :
    genA c sc a₁ * genA c sc a₁
      = c • genA c sc a₁ + (1 : Matrix (Fin 3) (Fin 3) ℝ) := by
  have hsc' : sc ^ 2 - c * sc - 1 = 0 := by linear_combination hsc
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp only [genA, Matrix.mul_apply, Fin.sum_univ_three, Matrix.of_apply, Matrix.smul_apply,
      Matrix.one_apply, Matrix.add_apply, smul_eq_mul] <;>
    norm_num <;> linarith [hsc']

/-! ## The hypotheses, derived from `seminormalParam`

`genA_genB_braid` takes `hsc` and `hrel` as hypotheses.  This section discharges both for
the actual seminormal parameters, so the identity is a statement about the Hoefsmit
matrices rather than about abstract arrays — the same role `seminormalParam_mul_rel` plays
for `Orbit6Braid`.

Multiplicative coordinates: `x = q^{-2d}` for the axial distance `d` of the `2 × 2` block,
so `a₁ = a(d) = (q - q⁻¹)/(1 - x)`.  The domino shifts the second generator's distance by
one, giving `a₂ = a(d-1)` at `q²x` for a row-domino and `a₂ = a(d+1)` at `x/q²` for a
column one.
-/

/-- The **row-domino scalar** `q` satisfies the Hecke quadratic `sc² = c·sc + 1`. -/
theorem hsc_row (q : ℝ) (hq : q ≠ 0) : q * q = (q - q⁻¹) * q + 1 := by
  field_simp
  ring

/-- The **column-domino scalar** `-q⁻¹` satisfies the same quadratic. -/
theorem hsc_col (q : ℝ) (hq : q ≠ 0) : (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by
  field_simp
  ring

/-- **The parameter relation, row-domino.**  With `a₁ = a(d)` at `x` and `a₂ = a(d-1)` at
`q²x`, the relation `a₂ · sc · (sc - a₁) = a₁` of `genA_genB_braid` holds identically for
`sc = q`. -/
theorem hrel_row (q x : ℝ) (hq : q ≠ 0) (hx : 1 - x ≠ 0) (hx' : 1 - q ^ 2 * x ≠ 0) :
    ((q - q⁻¹) / (1 - q ^ 2 * x)) * (q * (q - (q - q⁻¹) / (1 - x)))
      = (q - q⁻¹) / (1 - x) := by
  field_simp
  ring

/-- **The parameter relation, column-domino.**  With `a₂ = a(d+1)` at `x/q²` and
`sc = -q⁻¹`, the same relation holds — which is why `genA_genB_braid` is stated through
`sc` rather than through `q`: the `q`-only form covers the row case only. -/
theorem hrel_col (q x : ℝ) (hq : q ≠ 0) (hx : 1 - x ≠ 0) (hx' : 1 - x / q ^ 2 ≠ 0) :
    ((q - q⁻¹) / (1 - x / q ^ 2)) * ((-q⁻¹) * ((-q⁻¹) - (q - q⁻¹) / (1 - x)))
      = (q - q⁻¹) / (1 - x) := by
  have h2 : q ^ 2 - x ≠ 0 := fun h => hx' (by field_simp; linarith)
  field_simp
  ring


end Orbit3

end QOU.SchurWeyl
