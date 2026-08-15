import QOU.SchurWeyl.SeminormalParam

/-!
# `QOU.SchurWeyl.Orbit6Braid` — the generic size-`6` `S₃`-orbit braid identity
(bean `qou-gjg6`, step (iii))

The braid relation for the general-`λ` Hoefsmit seminormal representation reduces to one
identity per `⟨s_i, s_{i+1}⟩`-orbit of `SYT λ`.  Orbits of size `1`, `2` and `3` reduce to
the `2 × 2` template `S0_S1_braid`; the **generic orbit has size `6`** and is a genuine
`6`-dimensional identity, *not* reducible to `2 × 2` blocks — because `σ_i` and `σ_{i+1}`
pair the six tableaux differently.  That identity is proved here, sorry-free.

## The set-up

Index the six tableaux by `(x, y, z)`, the contents of the cells holding the three
consecutive entries `i, i+1, i+2`; `σ_i` swaps the first two coordinates and `σ_{i+1}` the
last two, with axial distances `y - x` and `z - y`.  In the basis order

  `(c₁,c₂,c₃), (c₁,c₃,c₂), (c₂,c₁,c₃), (c₂,c₃,c₁), (c₃,c₁,c₂), (c₃,c₂,c₁)`

`σ_i` pairs indices `{0,2}, {1,4}, {3,5}` and `σ_{i+1}` pairs `{0,1}, {2,3}, {4,5}`.  The
two pairings differ; that is the whole difficulty.

## Why the statement is polynomial

Writing `c = q - q⁻¹` and `p = c₂ - c₁`, `r = c₃ - c₂`, the three axial distances that
occur are `p`, `r` and `p + r`, with seminormal parameters (`SeminormalParam.lean`)

  `a₁ = a(p) = c/(1-u)`,  `a₂ = a(r) = c/(1-v)`,  `a₃ = a(p+r) = c/(1-uv)`

for `u = q^{-2p}`, `v = q^{-2r}`.  These are *not* independent: eliminating `u` and `v`
gives the single relation

  `a₃ · (a₁ + a₂ - c) = a₁ · a₂`     (`seminormalParam_mul_rel`)

and **that relation is exactly what the braid identity needs** — the theorem below is
stated for arbitrary reals satisfying it, with no `q`, `u`, `v` and no integer distances.
The relation is also *necessary*: perturbing `a₃` away from it breaks the identity.

Everything else about the parameters — in particular that `a(-d) = c - a(d)`, so the
partner entry of each block is `c - aᵢ` — is already proved in `SeminormalParam.lean`.

## The orientation convention

Each `s`-pair `{T, sT}` must designate one member as "first" — the one whose column carries
the plain `1` rather than `1 + a·a'` — because `seminormalBlock` is the square-root-free
(seminormal, not orthogonal) form and is not symmetric under exchanging the pair.  Here
"first" is the member with **negative** axial distance, matching the verified `(2,1)`
instance: in `[[1,2],[3]]` entry `2` has content `1` and `3` has content `-1`, so `σ₁` acts
at `d = -2 < 0` on the first basis vector, which is `S1`'s layout.

What matters is **global consistency**, not which sign is chosen.  The theorem below proves
the negative-distance convention; the positive-distance one is the same statement with the
orbit transposed.  Mixing the two — negative-first for `σ_i`, positive-first for `σ_{i+1}` —
appears to break the identity, so the convention is a real constraint rather than a
cosmetic choice; that is why it is stated here rather than left implicit.

*Evidence for the mixed case is numerical, not formal*: an exact-rational search over the
four orientation combinations (both-negative, both-positive, and the two mixed) found the
braid identity holding for the two consistent choices and failing for both mixed ones, with
`ABA - BAB` carrying six nonzero entries.  Only the consistent case is formalised here.

## Scope

This closes step (iii) — the braid identity — of the general-`λ` construction, in the
generic size-`6` case.  It does **not** by itself close `hoefsmit_seminormal_rep`.  Step
(i) (the tableau layer: `cellOf`, the axial distance, the `s_k`-action, far commutation)
is complete in `TableauCells.lean`; **step (ii)** — classifying the `⟨s_k, s_{k+1}⟩`-orbits
of `SYT λ` and assembling the block-diagonal generators, which includes mapping each orbit
onto the explicit index ordering its identity is stated in — remains open (bean
`qou-gjg6`).

Refs:
- [hoefsmit1974] Hoefsmit, PhD thesis (UBC 1974) — the seminormal form.
- [ram1997] Ram, *Seminormal representations of Weyl groups and Iwahori–Hecke algebras*,
  https://doi.org/10.1112/S0024611597000373 — the axial-distance formulas.
-/

set_option maxHeartbeats 1600000

namespace QOU.SchurWeyl

open Matrix

namespace Orbit6

variable (c a₁ a₂ a₃ : ℝ)

/-- `ρ(σ_i)` on a size-`6` orbit: pairs `{0,2}`, `{1,4}`, `{3,5}` with parameters
`a₁`, `a₃`, `a₂`.  The partner entry of a block is `c - a`, per `seminormalParam_add_neg`;
the lower-left entry is `1 + a·(c-a)`, per `seminormalBlock`.

Defined by a match on the index values rather than as a `!![…]` literal: entry lookup is
then a single iota reduction, where the literal form forces `simp` through a chain of
`vecCons` unfoldings and blows up (the `6 × 6` triple product has 1296 scalar terms). -/
noncomputable def genA : Matrix (Fin 6) (Fin 6) ℝ :=
  Matrix.of fun i j =>
    match (i : ℕ), (j : ℕ) with
    | 0, 0 => a₁
    | 0, 2 => 1 + (c - a₁) * a₁
    | 1, 1 => a₃
    | 1, 4 => 1 + (c - a₃) * a₃
    | 2, 0 => 1
    | 2, 2 => c - a₁
    | 3, 3 => a₂
    | 3, 5 => 1 + (c - a₂) * a₂
    | 4, 1 => 1
    | 4, 4 => c - a₃
    | 5, 3 => 1
    | 5, 5 => c - a₂
    | _, _ => 0

/-- `ρ(σ_{i+1})` on the same orbit: pairs `{0,1}`, `{2,3}`, `{4,5}` with parameters
`a₂`, `a₃`, `a₁`.  A **different** pairing from `genA` — this is what makes the orbit
irreducible to `2 × 2` blocks. -/
noncomputable def genB : Matrix (Fin 6) (Fin 6) ℝ :=
  Matrix.of fun i j =>
    match (i : ℕ), (j : ℕ) with
    | 0, 0 => a₂
    | 0, 1 => 1 + (c - a₂) * a₂
    | 1, 0 => 1
    | 1, 1 => c - a₂
    | 2, 2 => a₃
    | 2, 3 => 1 + (c - a₃) * a₃
    | 3, 2 => 1
    | 3, 3 => c - a₃
    | 4, 4 => a₁
    | 4, 5 => 1 + (c - a₁) * a₁
    | 5, 4 => 1
    | 5, 5 => c - a₁
    | _, _ => 0

/-- **The size-`6` orbit braid identity (Yang–Baxter).**

`ρ(σ_i) ρ(σ_{i+1}) ρ(σ_i) = ρ(σ_{i+1}) ρ(σ_i) ρ(σ_{i+1})` on a generic
`⟨s_i, s_{i+1}⟩`-orbit, given only the relation `a₃ (a₁ + a₂ - c) = a₁ a₂` that the
seminormal parameters satisfy (`seminormalParam_mul_rel`).  This is the `6`-dimensional
case that does not reduce to the `2 × 2` template, and it is the mathematical core of the
braid relation for arbitrary `λ`. -/
theorem genA_genB_braid (hs : a₁ + a₂ - c ≠ 0) (hrel : a₃ * (a₁ + a₂ - c) = a₁ * a₂) :
    genA c a₁ a₂ a₃ * genB c a₁ a₂ a₃ * genA c a₁ a₂ a₃
      = genB c a₁ a₂ a₃ * genA c a₁ a₂ a₃ * genB c a₁ a₂ a₃ := by
  have ha₃ : a₃ = a₁ * a₂ / (a₁ + a₂ - c) := by
    field_simp
    linarith [hrel]
  subst ha₃
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp only [genA, genB, Matrix.mul_apply, Fin.sum_univ_six, Matrix.of_apply] <;>
    norm_num <;> field_simp <;> ring

/-- **The Hecke quadratic relation on the orbit** for `ρ(σ_i)`.  Unlike the braid this is
pair-local — it needs no relation among the parameters, and indeed holds for *every* `c`,
since each block has trace `c` and determinant `-1` and Cayley–Hamilton does the rest.
Instantiating `c = q - q⁻¹` (with `q * q⁻¹ = 1`) gives the Hecke relation
`σ² = (q - q⁻¹)σ + (q·q⁻¹)·1` in the normalisation of `Hecke.σ_quadratic`.  (`genB`
satisfies the same statement with the pairing permuted.) -/
theorem genA_quadratic :
    genA c a₁ a₂ a₃ * genA c a₁ a₂ a₃
      = c • genA c a₁ a₂ a₃ + (1 : Matrix (Fin 6) (Fin 6) ℝ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp only [genA, Matrix.mul_apply, Fin.sum_univ_six, Matrix.of_apply, Matrix.smul_apply,
      Matrix.one_apply, Matrix.add_apply, smul_eq_mul] <;>
    norm_num <;> ring

/-- The Hecke-normalised form of `genA_quadratic`: with `c = q - q⁻¹` and `q ≠ 0` this is
exactly the relation `Hecke.σ_quadratic` imposes on a generator. -/
theorem genA_quadratic_hecke (q : ℝ) (hq : q ≠ 0) :
    genA (q - q⁻¹) a₁ a₂ a₃ * genA (q - q⁻¹) a₁ a₂ a₃
      = (q - q⁻¹) • genA (q - q⁻¹) a₁ a₂ a₃
        + (q * q⁻¹) • (1 : Matrix (Fin 6) (Fin 6) ℝ) := by
  rw [mul_inv_cancel₀ hq, one_smul]
  exact genA_quadratic _ a₁ a₂ a₃

/-! ## Tying the abstract parameters back to the seminormal form -/

open Seminormal in
/-- **The seminormal parameters satisfy the braid relation's hypothesis.**  With
`a₁ = a(p)`, `a₂ = a(r)`, `a₃ = a(p+r)` — the three axial distances of a size-`6` orbit,
written multiplicatively as `x = q^{-2p}`, `y = q^{-2r}`, so that the third is at the
*product* `x*y` — the relation `a₃ (a₁ + a₂ - c) = a₁ a₂` holds identically.

This is what makes `genA_genB_braid` a statement about the actual Hoefsmit matrices rather
than about abstract `6 × 6` arrays. -/
theorem seminormalParam_mul_rel (q x y : ℝ) (hx : x ≠ 1) (hy : y ≠ 1) (hxy : x * y ≠ 1) :
    ((q - q⁻¹) / (1 - x * y)) * ((q - q⁻¹) / (1 - x) + (q - q⁻¹) / (1 - y) - (q - q⁻¹))
      = ((q - q⁻¹) / (1 - x)) * ((q - q⁻¹) / (1 - y)) := by
  have h1 : (1 : ℝ) - x ≠ 0 := sub_ne_zero.mpr (Ne.symm hx)
  have h2 : (1 : ℝ) - y ≠ 0 := sub_ne_zero.mpr (Ne.symm hy)
  have h3 : (1 : ℝ) - x * y ≠ 0 := sub_ne_zero.mpr (Ne.symm hxy)
  field_simp
  ring

end Orbit6

end QOU.SchurWeyl
