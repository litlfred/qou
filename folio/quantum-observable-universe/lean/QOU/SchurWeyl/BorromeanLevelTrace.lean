/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.WenzlMarkovTraceInstance

/-!
# The Borromean braid under the level-`r` Markov traces

`β_Bor = (σ₁ σ₂⁻¹)³ ∈ H₃(q)`.  This file computes `tr(β_Bor)` for **every** Markov trace family on
the Hecke tower, as an explicit quadratic polynomial in the Markov parameter `z`, and specialises it
to the level-`2` and level-`3` Wenzl traces.

## Results

* `borromean_eq_nf` — the normal form of `β_Bor` in the basis `1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁` of
  `H₃(q)`, over any commutative ring with `q · qi = 1`.  The `σ₁σ₂σ₁` coefficient is `0`.
* `tr_borromean` — for any Markov trace family with parameter `z`, `h = q − qi`,
  `tr(β_Bor) = 1 − h⁴ − h⁵ z + h⁴ z²`.
  Level-free: no weight, no seminormal matrix.
* `wenzl_borromean_three_sub_two` — over a field, with `q` not a root of unity,
  `tr⁽³⁾(β_Bor) − tr⁽²⁾(β_Bor) = −(q−1)⁴(q+1)⁴ Φ₁₀ Φ₅ / (q² (q²+1)² Φ₆² Φ₃²)`,
  where `tr⁽ʳ⁾` is the level-`r` Wenzl trace `wenzlMarkovTrace`.  Together with
  `wenzl_borromean_two` and `wenzl_borromean_three` (the two values separately).

## Scope

This is a statement about the single element `β_Bor`.  It is the exact identity of
`docs/audits/2026-10-10-level3-su3-channel-test.md` §5.2, now proved from the trace objects rather
than evaluated in sympy.  It says nothing about the order in `h = q − q⁻¹` at which the level-3
(three-row) weights differ from zero: `y_{(1³)}` at level 3 is `1/27` at `q = 1`, so the three-row
block is present at order zero; it is the *Borromean* trace difference that starts at `(q−1)⁴`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-- Ref: [leitner2026] docs/audits/2026-10-10-level3-su3-channel-test.md §5.2; bean qou-qs4c
-/

namespace QOU.SchurWeyl.BorromeanLevelTrace

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion

section NormalForm

variable {K : Type*} [CommRing K] (q qi : K)

local notation "s0" => Hecke.σ K q qi 2 0
local notation "s1" => Hecke.σ K q qi 2 1

/-- `σ₂⁻¹ = σ₂ − (q − qi)` in `H₃`. -/
noncomputable def s1inv : Hecke K q qi 2 := s1 - (q - qi) • 1

/-- **The Borromean braid** `β_Bor = (σ₁ σ₂⁻¹)³` in `H₃(q)` (generators indexed `0, 1`). -/
noncomputable def betaBor : Hecke K q qi 2 :=
  (s0 * s1inv q qi) * (s0 * s1inv q qi) * (s0 * s1inv q qi)

/-- An element of `H₃` written in the basis `1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁`. -/
noncomputable def nf (a b c d e f : K) : Hecke K q qi 2 :=
  a • 1 + b • s0 + c • s1 + d • (s0 * s1) + e • (s1 * s0) + f • (s0 * s1 * s0)

variable {q qi}

theorem sq0 (hqi : q * qi = 1) : s0 * s0 = (q - qi) • s0 + 1 :=
  Hecke.σ_quadratic_qou K q qi 2 hqi 0

theorem sq1 (hqi : q * qi = 1) : s1 * s1 = (q - qi) • s1 + 1 :=
  Hecke.σ_quadratic_qou K q qi 2 hqi 1

theorem braid01 : s0 * s1 * s0 = s1 * s0 * s1 :=
  Hecke.σ_braid K q qi 2 0 (by norm_num)

theorem nf_mul_s0 (hqi : q * qi = 1) (a b c d e f : K) :
    nf q qi a b c d e f * s0
      = nf q qi b (a + (q - qi) * b) e f (c + (q - qi) * e) (d + (q - qi) * f) := by
  have h1 : s1 * s0 * s0 = (q - qi) • (s1 * s0) + s1 := by
    rw [mul_assoc, sq0 hqi, mul_add, mul_smul_comm, mul_one]
  have h2 : s0 * s1 * s0 * s0 = (q - qi) • (s0 * s1 * s0) + s0 * s1 := by
    rw [mul_assoc, sq0 hqi, mul_add, mul_smul_comm, mul_one]
  simp only [nf, add_mul, smul_mul_assoc, one_mul, sq0 hqi, h1, h2]
  module

theorem nf_mul_s1 (hqi : q * qi = 1) (a b c d e f : K) :
    nf q qi a b c d e f * s1
      = nf q qi c d (a + (q - qi) * c) (b + (q - qi) * d) f (e + (q - qi) * f) := by
  have h1 : s0 * s1 * s1 = (q - qi) • (s0 * s1) + s0 := by
    rw [mul_assoc, sq1 hqi, mul_add, mul_smul_comm, mul_one]
  have h2 : s1 * s0 * s1 = s0 * s1 * s0 := braid01.symm
  have h3 : s0 * s1 * s0 * s1 = (q - qi) • (s0 * s1 * s0) + s1 * s0 := by
    calc s0 * s1 * s0 * s1 = s0 * (s1 * s0 * s1) := by simp only [mul_assoc]
      _ = s0 * (s0 * s1 * s0) := by rw [braid01]
      _ = (s0 * s0) * (s1 * s0) := by simp only [mul_assoc]
      _ = _ := by rw [sq0 hqi, add_mul, smul_mul_assoc, one_mul, ← mul_assoc]
  simp only [nf, add_mul, smul_mul_assoc, one_mul, sq1 hqi, h1, h2, h3]
  module

theorem nf_mul_s1inv (hqi : q * qi = 1) (a b c d e f : K) :
    nf q qi a b c d e f * s1inv q qi
      = nf q qi (c - (q - qi) * a) (d - (q - qi) * b) a b (f - (q - qi) * e) e := by
  rw [s1inv, mul_sub, nf_mul_s1 hqi, mul_smul_comm, mul_one]
  simp only [nf]
  module

/-- **Normal form of the Borromean braid.**  Over any commutative ring with `q · qi = 1`, writing
`h = q − qi`:
`β_Bor = (1 − h⁴) − (h⁵ + h³) σ₁ + h³ σ₂ + (h⁴ + h²) σ₁σ₂ − h² σ₂σ₁ + 0 · σ₁σ₂σ₁`. -/
theorem borromean_eq_nf (hqi : q * qi = 1) :
    betaBor q qi = nf q qi (1 - (q - qi) ^ 4) (-(q - qi) ^ 5 - (q - qi) ^ 3) ((q - qi) ^ 3)
      ((q - qi) ^ 4 + (q - qi) ^ 2) (-(q - qi) ^ 2) 0 := by
  have e0 : s0 = nf q qi 0 1 0 0 0 0 := by simp only [nf]; module
  have e : betaBor q qi =
      nf q qi 0 1 0 0 0 0 * s1inv q qi * s0 * s1inv q qi * s0 * s1inv q qi := by
    rw [betaBor, ← e0]; simp only [mul_assoc]
  rw [e, nf_mul_s1inv hqi, nf_mul_s0 hqi, nf_mul_s1inv hqi, nf_mul_s0 hqi, nf_mul_s1inv hqi]
  congr 1 <;> ring

end NormalForm

section Trace

variable {K : Type*} [CommRing K] {q qi z : K}

theorem tr2_one (T : HeckeCoset.MarkovTraceFamily K q qi z) : T.tr 2 1 = 1 := T.tr_one 2

theorem tr2_s0 (T : HeckeCoset.MarkovTraceFamily K q qi z) : T.tr 2 (Hecke.σ K q qi 2 0) = z := by
  have h := T.tr_incl 1 (Hecke.σ K q qi 1 0)
  rw [heckeIncl_σ] at h
  rw [show (0 : Fin 2) = (0 : Fin 1).castSucc from rfl, h]
  exact T.param_eq

theorem tr2_s1 (T : HeckeCoset.MarkovTraceFamily K q qi z) : T.tr 2 (Hecke.σ K q qi 2 1) = z := by
  have h := T.tr_markov 1 1
  rw [map_one, one_mul, T.tr_one, mul_one] at h
  exact h

theorem tr2_s0s1 (T : HeckeCoset.MarkovTraceFamily K q qi z) :
    T.tr 2 (Hecke.σ K q qi 2 0 * Hecke.σ K q qi 2 1) = z ^ 2 := by
  have hp : T.tr 1 (Hecke.σ K q qi 1 0) = z := T.param_eq
  have h := T.tr_markov 1 (Hecke.σ K q qi 1 0)
  rw [heckeIncl_σ, hp] at h
  rw [sq, ← h]
  rfl

theorem tr2_s1s0 (T : HeckeCoset.MarkovTraceFamily K q qi z) :
    T.tr 2 (Hecke.σ K q qi 2 1 * Hecke.σ K q qi 2 0) = z ^ 2 := by
  rw [T.tr_cyclic, tr2_s0s1]

/-- The trace of a normal-form element whose `σ₁σ₂σ₁` coefficient vanishes. -/
theorem tr_nf (T : HeckeCoset.MarkovTraceFamily K q qi z) (a b c d e : K) :
    T.tr 2 (nf q qi a b c d e 0) = a + (b + c) * z + (d + e) * z ^ 2 := by
  simp only [nf, zero_smul, add_zero, map_add, map_smul, smul_eq_mul, tr2_one, tr2_s0, tr2_s1,
    tr2_s0s1, tr2_s1s0]
  ring

/-- **The trace of the Borromean braid under any Markov trace family**, as a polynomial in the
Markov parameter `z`, `h = q − qi`:  `tr(β_Bor) = 1 − h⁴ − h⁵ z + h⁴ z²`. -/
theorem tr_borromean (hqi : q * qi = 1) (T : HeckeCoset.MarkovTraceFamily K q qi z) :
    T.tr 2 (betaBor q qi) = 1 - (q - qi) ^ 4 - (q - qi) ^ 5 * z + (q - qi) ^ 4 * z ^ 2 := by
  rw [borromean_eq_nf hqi, tr_nf]
  ring

end Trace

section Levels

open SeminormalRep

variable {K : Type*} [Field K]

/-- The level-`r` Wenzl trace of `β_Bor`. -/
noncomputable def trLevel (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (r : ℕ) :
    K :=
  wtraceW q hq0 hq2 (wenzlWeight r (q ^ 2)) 2 (betaBor q q⁻¹)

theorem trLevel_eq (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) {r : ℕ}
    (hr : r ≠ 0) :
    trLevel q hq0 hq2 r
      = 1 - (q - q⁻¹) ^ 4 - (q - q⁻¹) ^ 5 * ((q ^ 2) ^ r / (q * levelBracket r (q ^ 2)))
        + (q - q⁻¹) ^ 4 * ((q ^ 2) ^ r / (q * levelBracket r (q ^ 2))) ^ 2 := by
  rw [trLevel, ← wenzlMarkovTrace_tr q hq0 hq2 (gen_of_notRootOfUnity hq2) hr]
  exact tr_borromean (mul_inv_cancel₀ hq0) _

theorem q21_ne_zero {q : K} (hq2 : GenericParameter.NotRootOfUnity q) : q ^ 2 + 1 ≠ 0 := by
  have h := levelBracket_ne_zero_of_gen (gen_of_notRootOfUnity hq2) (r := 2) (by norm_num)
  rw [levelBracket_two] at h
  rwa [add_comm]

theorem levelBracket_two_sq (q : K) : levelBracket 2 (q ^ 2) = q ^ 2 + 1 := by
  rw [levelBracket_two, add_comm]

theorem levelBracket_three_sq (q : K) : levelBracket 3 (q ^ 2) = q ^ 4 + q ^ 2 + 1 := by
  simp only [levelBracket, Finset.sum_range_succ, Finset.sum_range_zero]; ring

theorem q421_ne_zero {q : K} (hq2 : GenericParameter.NotRootOfUnity q) :
    q ^ 4 + q ^ 2 + 1 ≠ 0 := by
  have h := levelBracket_ne_zero_of_gen (gen_of_notRootOfUnity hq2) (r := 3) (by norm_num)
  rwa [levelBracket_three_sq] at h

/-- **Level 2** (convention D): `tr⁽²⁾(β_Bor) = −(q¹² − 3q¹⁰ + 2q⁸ − 4q⁶ + 2q⁴ − 3q² + 1) /
(q⁴ (q² + 1)²)`. -/
theorem wenzl_borromean_two (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) :
    trLevel q hq0 hq2 2
      = -(q ^ 12 - 3 * q ^ 10 + 2 * q ^ 8 - 4 * q ^ 6 + 2 * q ^ 4 - 3 * q ^ 2 + 1)
          / (q ^ 4 * (q ^ 2 + 1) ^ 2) := by
  have h1 := q21_ne_zero hq2
  rw [trLevel_eq q hq0 hq2 (by norm_num), levelBracket_two_sq]
  field_simp
  ring

/-- **Level 3**: `tr⁽³⁾(β_Bor) = −(q¹⁶ − 2q¹⁴ − q¹² − 5q⁸ − q⁴ − 2q² + 1) / (q⁴ Φ₆² Φ₃²)`,
`Φ₃ = q² + q + 1`, `Φ₆ = q² − q + 1`. -/
theorem wenzl_borromean_three (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) :
    trLevel q hq0 hq2 3
      = -(q ^ 16 - 2 * q ^ 14 - q ^ 12 - 5 * q ^ 8 - q ^ 4 - 2 * q ^ 2 + 1)
          / (q ^ 4 * (q ^ 2 - q + 1) ^ 2 * (q ^ 2 + q + 1) ^ 2) := by
  have h3 := q421_ne_zero hq2
  have h63 : (q ^ 2 - q + 1) * (q ^ 2 + q + 1) = q ^ 4 + q ^ 2 + 1 := by ring
  have h6 : q ^ 2 - q + 1 ≠ 0 := fun h => h3 (by rw [← h63, h, zero_mul])
  have h3' : q ^ 2 + q + 1 ≠ 0 := fun h => h3 (by rw [← h63, h, mul_zero])
  rw [trLevel_eq q hq0 hq2 (by norm_num), levelBracket_three_sq, mul_assoc, ← mul_pow, h63]
  generalize hD : q ^ 4 + q ^ 2 + 1 = D at h3 ⊢
  field_simp
  subst hD
  ring

/-- **The level-3 minus level-2 Borromean trace** (`docs/audits/2026-10-10-level3-su3-channel-test.md`
§5.2), over any field with `q` not a root of unity:

`tr⁽³⁾(β_Bor) − tr⁽²⁾(β_Bor) = −(q−1)⁴ (q+1)⁴ Φ₁₀ Φ₅ / (q² (q²+1)² Φ₆² Φ₃²)`,

`Φ₅ = q⁴+q³+q²+q+1`, `Φ₁₀ = q⁴−q³+q²−q+1`.  A statement about `β_Bor` only. -/
theorem wenzl_borromean_three_sub_two (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) :
    trLevel q hq0 hq2 3 - trLevel q hq0 hq2 2
      = -((q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 4 - q ^ 3 + q ^ 2 - q + 1)
            * (q ^ 4 + q ^ 3 + q ^ 2 + q + 1))
          / (q ^ 2 * (q ^ 2 + 1) ^ 2 * (q ^ 2 - q + 1) ^ 2 * (q ^ 2 + q + 1) ^ 2) := by
  have h1 := q21_ne_zero hq2
  have h3 := q421_ne_zero hq2
  have h63 : (q ^ 2 - q + 1) * (q ^ 2 + q + 1) = q ^ 4 + q ^ 2 + 1 := by ring
  have h6 : q ^ 2 - q + 1 ≠ 0 := fun h => h3 (by rw [← h63, h, zero_mul])
  have h3' : q ^ 2 + q + 1 ≠ 0 := fun h => h3 (by rw [← h63, h, mul_zero])
  rw [wenzl_borromean_three, wenzl_borromean_two,
    show q ^ 2 * (q ^ 2 + 1) ^ 2 * (q ^ 2 - q + 1) ^ 2 * (q ^ 2 + q + 1) ^ 2
      = q ^ 2 * (q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) ^ 2 by rw [← h63]; ring,
    mul_assoc (q ^ 4), ← mul_pow, h63]
  generalize hD : q ^ 4 + q ^ 2 + 1 = D at h3 ⊢
  field_simp
  subst hD
  ring

end Levels

end QOU.SchurWeyl.BorromeanLevelTrace
