import QOU.BraidKnot.HeckeStableScalarCascade

/-!
# The bounded Hecke presentation, and the Jucys–Murphy spectral half at `n = 3`

`HeckeStableScalarCascade.lean` proved that `HeckeGenerators` — whose relations are quantified over
**all** `i : ℕ`, i.e. the stable algebra `H_∞(q)` — cannot host an irreducible representation, and
that a bounded-index variant is therefore the only route to a `dim > 1` witness for `IsJMWeight`.

This file builds that variant and cashes it out at `n = 3`.

## What is here

* `HeckeGeneratorsBelow R A q n` — the relations required **only** for the generator indices that
  actually occur in `H_n(q)`, namely `σ₀ … σ_{n-2}`.  At `n = 3` this is exactly *two* generators
  with one braid relation and no far-commutation at all.
* `hecke_mul_sub_eq_one` / `sub_mul_hecke_eq_one` — the Hecke relation **already supplies the
  inverse**, `σ⁻¹ = σ − (q − q⁻¹)`.  So the `σinv` / `mul_σinv` / `σinv_mul` fields of the unbounded
  `HeckeGenerators` are redundant data, and the bounded class does not carry them.
* `stdTwoBelow3` — the 2-dimensional `(2,1)` representation as an instance.  Its Hecke and braid
  relations are the ones already proved in `HeckeStableScalarCascade.lean`; nothing new is assumed.
* `stdTwoBelow3_jm_content` — **the payload.**  The Jucys–Murphy elements act on the seminormal
  vector `e₀ = (1,0)` by `q^{2c}` with `c = 0, 1, −1`.

## Why the payload matters

`HeckeJucysMurphyElements.lean` splits `JucysMurphySpectrum` into a *structural* half (the `Lᵢ`
exist, commute, multiply to the full twist) and a *spectral* half, and says of the latter:

> The spectral half — that `Lᵢ` acts on the seminormal basis by `q^{2·content}`.  Untouched here.
> It needs Young's seminormal form, which the corpus does not carry.

This file gives that spectral half its **first instance**.  The three eigenvalues `q^0, q^2, q^{-2}`
are `q^{2c}` for the contents `c = 0, 1, −1` of the cells `(0,0), (0,1), (1,0)` — i.e. of the
standard Young tableau

```
1 2
3
```

on `λ = (2,1)`, read in the order the JM elements index.  It is one tableau at one `n`, not Young's
theorem; what it establishes is that the content spectrum is **realised**, on a genuinely
2-dimensional module, rather than only conjectured.

Refs:
- [jones1987] V. Jones, Hecke algebra representations of braid groups and link polynomials.
- [wenzl1988] H. Wenzl, Hecke algebras of type A_n and subfactors.
-/

namespace QOU.BraidKnot.Hecke

open Matrix

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-! ## §1  The Hecke relation supplies the inverse -/

/-- `X · (X − (q − q⁻¹)) = 1` for any Hecke-quadratic `X`.  Scalars are central, so this is pure
rearrangement — no invertibility hypothesis is needed. -/
theorem hecke_mul_sub_eq_one {X : A} (h : X * X = algebraMap R A (q - q⁻¹) * X + 1) :
    X * (X - algebraMap R A (q - q⁻¹)) = 1 := by
  rw [mul_sub, h, Algebra.commutes]
  abel

/-- The other side: `(X − (q − q⁻¹)) · X = 1`. -/
theorem sub_mul_hecke_eq_one {X : A} (h : X * X = algebraMap R A (q - q⁻¹) * X + 1) :
    (X - algebraMap R A (q - q⁻¹)) * X = 1 := by
  rw [sub_mul, h]
  abel

/-! ## §2  The bounded presentation -/

/-- **Bounded Hecke presentation.**  The relations of `H_n(q)`, required only for the generator
indices that actually occur there: `σ₀ … σ_{n-2}`, i.e. `i + 1 < n`.

Contrast `HeckeGenerators`, which quantifies over every `i : ℕ` and so presents `H_∞(q)`.  That
difference is not cosmetic — `stdTwo_no_stable_extension` shows the unbounded version excludes the
2-dimensional representation outright.

No `σinv` field: §1 derives the inverse from `hecke`. -/
class HeckeGeneratorsBelow (R : Type*) [Field R] (A : Type*) [Ring A] [Algebra R A] (q : R)
    (n : ℕ) where
  /-- The braid generators; only `σ i` for `i + 1 < n` is constrained. -/
  σ : ℕ → A
  /-- **Hecke relation**, for each generator of `H_n(q)`. -/
  hecke : ∀ i, i + 1 < n → σ i * σ i = algebraMap R A (q - q⁻¹) * σ i + 1
  /-- **Braid relation**, whenever both `σ i` and `σ (i+1)` are generators of `H_n(q)`. -/
  braid : ∀ i, i + 2 < n → σ i * σ (i + 1) * σ i = σ (i + 1) * σ i * σ (i + 1)
  /-- **Far commutation**, whenever both indices are generators of `H_n(q)`. -/
  far : ∀ i j, i + 1 < j → j + 1 < n → σ i * σ j = σ j * σ i

variable {n : ℕ}

/-- **Unnormalized JM elements** on the bounded presentation: `L₀ = 1`, `L_{i+1} = σᵢ Lᵢ σᵢ`.
Same recursion as `jmRaw`; `jmRawB H k` for `k < n` touches only `σ₀ … σ_{k-1}`. -/
def jmRawB (H : HeckeGeneratorsBelow R A q n) : ℕ → A
  | 0 => 1
  | (i + 1) => H.σ i * jmRawB H i * H.σ i

@[simp] theorem jmRawB_zero (H : HeckeGeneratorsBelow R A q n) : jmRawB H 0 = 1 := rfl

theorem jmRawB_succ (H : HeckeGeneratorsBelow R A q n) (i : ℕ) :
    jmRawB H (i + 1) = H.σ i * jmRawB H i * H.σ i := rfl

/-! ## §3  The 2-dimensional `(2,1)` representation as a bounded instance -/

section StdThree

variable {K : Type*} [Field K]

/-- The generator family: `σ₀ = stdTwo0`, and every later index `stdTwo1`.  Only `σ₀` and `σ₁` are
constrained at `n = 3`, so the tail is free. -/
noncomputable def stdTwoσ (q : K) : ℕ → Matrix (Fin 2) (Fin 2) K
  | 0 => stdTwo0 q
  | _ => stdTwo1 q

@[simp] theorem stdTwoσ_zero (q : K) : stdTwoσ q 0 = stdTwo0 q := rfl
@[simp] theorem stdTwoσ_one (q : K) : stdTwoσ q 1 = stdTwo1 q := rfl

/-- **The `dim > 1` instance.**  At `n = 3` the bounded presentation asks for exactly two
Hecke-quadratic generators and one braid relation — all three already proved for the Young
seminormal pair.  Far-commutation is vacuous: it would need `i + 1 < j` with `j + 1 < 3`.

This is precisely what `HeckeGenerators` cannot admit (`stdTwo_no_stable_extension`). -/
noncomputable def stdTwoBelow3 (q : K) (hq : q ≠ 0) :
    HeckeGeneratorsBelow K (Matrix (Fin 2) (Fin 2) K) q 3 where
  σ := stdTwoσ q
  hecke i hi := by
    have h : i = 0 ∨ i = 1 := by omega
    rcases h with rfl | rfl
    · exact stdTwo_hecke0_algebraMap hq
    · exact stdTwo_hecke1_algebraMap hq
  braid i hi := by
    have h : i = 0 := by omega
    subst h
    exact stdTwo_braid hq
  far i j hij hj := by exfalso; omega

theorem stdTwoBelow3_jmRaw_one (q : K) (hq : q ≠ 0) :
    jmRawB (stdTwoBelow3 q hq) 1 = stdTwo0 q * stdTwo0 q := by
  rw [jmRawB_succ, jmRawB_zero]
  simp [stdTwoBelow3]

theorem stdTwoBelow3_jmRaw_two (q : K) (hq : q ≠ 0) :
    jmRawB (stdTwoBelow3 q hq) 2 = stdTwo1 q * (stdTwo0 q * stdTwo0 q) * stdTwo1 q := by
  rw [jmRawB_succ, stdTwoBelow3_jmRaw_one]
  simp [stdTwoBelow3]

/-! ## §4  The seminormal vector and its content spectrum -/

/-- The seminormal vector `e₀ = (1,0)`. -/
noncomputable def seminormalE0 (K : Type*) [Field K] : Fin 2 → K := ![1, 0]

/-- `L₁ = σ₀²` acts on `e₀` by `q²`, the content-`+1` eigenvalue. -/
theorem stdTwo_jm1_smul (q : K) :
    (stdTwo0 q * stdTwo0 q).mulVec (seminormalE0 K) = (q ^ 2) • seminormalE0 K := by
  funext i
  fin_cases i <;>
    simp [seminormalE0, stdTwo0, Matrix.mulVec, Matrix.mul_apply, dotProduct,
      Fin.sum_univ_two, pow_two]

/-- `L₂ = σ₁σ₀²σ₁` acts on `e₀` by `q⁻²`, the content-`−1` eigenvalue. -/
theorem stdTwo_jm2_smul (q : K) (hq : q ≠ 0) :
    (stdTwo1 q * (stdTwo0 q * stdTwo0 q) * stdTwo1 q).mulVec (seminormalE0 K)
      = ((q ^ 2)⁻¹) • seminormalE0 K := by
  funext i
  fin_cases i <;>
    simp [seminormalE0, stdTwo0, stdTwo1, Matrix.mulVec, Matrix.mul_apply, dotProduct,
      Fin.sum_univ_two] <;> field_simp <;> ring

/-- **The Jucys–Murphy spectral half, first instance.**

On the 2-dimensional `(2,1)` representation of `H₃(q)`, the JM elements act on the seminormal
vector `e₀` by `q^{2c}` for `c = 0, 1, −1` — the contents of the cells `(0,0), (0,1), (1,0)`, i.e.
of the standard tableau `[[1,2],[3]]`.

This is the statement `HeckeJucysMurphyElements.lean` records as untouched for want of Young's
seminormal form.  It is one tableau at one `n`, so it does **not** prove the general spectral
theorem; it shows the content spectrum is realised on a genuinely multi-dimensional module. -/
theorem stdTwoBelow3_jm_content (q : K) (hq : q ≠ 0) :
    (jmRawB (stdTwoBelow3 q hq) 0).mulVec (seminormalE0 K)
        = (q ^ (2 * (0 : ℤ))) • seminormalE0 K
      ∧ (jmRawB (stdTwoBelow3 q hq) 1).mulVec (seminormalE0 K)
        = (q ^ (2 * (1 : ℤ))) • seminormalE0 K
      ∧ (jmRawB (stdTwoBelow3 q hq) 2).mulVec (seminormalE0 K)
        = (q ^ (2 * (-1 : ℤ))) • seminormalE0 K := by
  refine ⟨?_, ?_, ?_⟩
  · simp [jmRawB_zero]
  · rw [stdTwoBelow3_jmRaw_one, stdTwo_jm1_smul,
      show (2 * (1 : ℤ)) = ((2 : ℕ) : ℤ) by norm_num, zpow_natCast]
  · rw [stdTwoBelow3_jmRaw_two, stdTwo_jm2_smul q hq]
    rw [show (2 * (-1 : ℤ)) = -2 by ring, zpow_neg, ← zpow_natCast q 2]
    norm_num

end StdThree

end QOU.BraidKnot.Hecke
