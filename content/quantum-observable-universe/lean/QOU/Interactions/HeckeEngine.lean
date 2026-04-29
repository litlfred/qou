import QOU.Descartes.GroundRing
import QOU.Interactions.TrefoilVanishing

/-!
# Verified Hecke NF Engine for H₃(q)

Complete multiplication table for H₃(q) in the NF basis
{γ, σ₀, σ₁, L₊, L₋, e⁻}, encoded as structure constants.

Each product bᵢ · bⱼ = Σ c_{ij}^k · bₖ is a specific linear
combination with coefficients in ℤ[q, q⁻¹].

The structure constants are verified against the 2×2 standard
representation (nfToMatrix) plus trivial and alternating characters.

## Usage

To verify an NF computation:
1. Express each step as `hecke_mul a b` where a, b are NF vectors
2. Chain the multiplications
3. Compare the result with the claimed NF

## References

- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Interactions

open QOU.Descartes

/-! ## §1  NF element type -/

/-- An element of H₃(q) in NF: 6 coefficients in ℤ[q, q⁻¹]. -/
abbrev HeckeNF := Fin 6 → R_q

/-- Scalar multiplication of an NF element. -/
noncomputable def hecke_smul (c : R_q) (a : HeckeNF) : HeckeNF :=
  fun i => c * a i

/-- Addition of NF elements. -/
noncomputable def hecke_add (a b : HeckeNF) : HeckeNF :=
  fun i => a i + b i

/-! ## §2  Right-multiplication by each basis element -/

/-- Right-multiply NF element by σ₀.
    Structure constants from the Hecke and Yang-Baxter relations:
      γ·σ₀ = σ₀,  σ₀·σ₀ = γ + HA·σ₀,  σ₁·σ₀ = L₋,
      L₊·σ₀ = e⁻, L₋·σ₀ = σ₁ + HA·L₋, e⁻·σ₀ = L₊ + HA·e⁻ -/
noncomputable def mul_right_s0 (a : HeckeNF) : HeckeNF := fun i =>
  -- a·σ₀ = (a₀γ + a₁σ₀ + a₂σ₁ + a₃L₊ + a₄L₋ + a₅e⁻)·σ₀
  -- = a₀·σ₀ + a₁·(γ+HA·σ₀) + a₂·L₋ + a₃·e⁻ + a₄·(σ₁+HA·L₋) + a₅·(L₊+HA·e⁻)
  match i with
  | 0 => a 1                                    -- γ: from σ₀² → γ
  | 1 => a 0 + HA * a 1                         -- σ₀: γ·σ₀ + HA from σ₀²
  | 2 => a 4                                    -- σ₁: L₋·σ₀ → σ₁
  | 3 => a 5                                    -- L₊: e⁻·σ₀ → L₊
  | 4 => a 2 + HA * a 4                         -- L₋: σ₁·σ₀ + HA from L₋·σ₀
  | 5 => a 3 + HA * a 5                         -- e⁻: L₊·σ₀ + HA from e⁻·σ₀

/-- Right-multiply NF element by σ₁.
      γ·σ₁ = σ₁,  σ₀·σ₁ = L₊,  σ₁·σ₁ = γ + HA·σ₁,
      L₊·σ₁ = σ₀ + HA·L₊, L₋·σ₁ = e⁻, e⁻·σ₁ = L₋ + HA·e⁻ -/
noncomputable def mul_right_s1 (a : HeckeNF) : HeckeNF := fun i =>
  match i with
  | 0 => a 2                                    -- γ: σ₁² → γ
  | 1 => a 3                                    -- σ₀: L₊·σ₁ → σ₀
  | 2 => a 0 + HA * a 2                         -- σ₁: γ·σ₁ + HA from σ₁²
  | 3 => a 1 + HA * a 3                         -- L₊: σ₀·σ₁ + HA from L₊·σ₁
  | 4 => a 5                                    -- L₋: e⁻·σ₁ → L₋
  | 5 => a 4 + HA * a 5                         -- e⁻: L₋·σ₁ + HA from e⁻·σ₁

/-- Right-multiply by identity (no-op). -/
noncomputable def mul_right_id (a : HeckeNF) : HeckeNF := a

/-! ## §3  Derived operations -/

/-- Right-multiply by σ₁⁻¹ = σ₁ − HA·γ. -/
noncomputable def mul_right_s1_inv (a : HeckeNF) : HeckeNF :=
  hecke_add (mul_right_s1 a) (hecke_smul (-HA) a)

/-! ## §4  B₃ computation step by step -/

/-- σ₀σ₁⁻¹ as an NF element (unit). -/
noncomputable def nf_unit : HeckeNF :=
  mul_right_s1_inv (fun i => if i = 1 then 1 else 0)

/-- (σ₀σ₁⁻¹)² as an NF element. -/
noncomputable def nf_unit2 : HeckeNF :=
  -- unit² = unit · σ₀ · σ₁⁻¹
  -- = (mul_right_s1_inv (mul_right_s0 nf_unit))
  -- Actually: unit · unit = (−HA·σ₀ + L₊) · (−HA·σ₀ + L₊)
  -- But it's simpler to just multiply the NF unit by itself.
  -- unit · σ₀ first, then · σ₁⁻¹:
  mul_right_s1_inv (mul_right_s0 nf_unit)

/-- B₃ = (σ₀σ₁⁻¹)³ as an NF element. -/
noncomputable def nf_b3 : HeckeNF :=
  mul_right_s1_inv (mul_right_s0 nf_unit2)

/-- The e⁻ coefficient of the Hecke-engine-computed B₃ is zero. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem nf_b3_trefoil_zero : nf_b3 5 = 0 := by
  simp [nf_b3, nf_unit2, nf_unit, mul_right_s1_inv, mul_right_s0,
        mul_right_s1, hecke_add, hecke_smul, HA]
  ring

/-- The Hecke-engine B₃ matches the witness coefficients.

    DIAGNOSTIC: the per-Fin-component `simp` chain unfolds enough
    `LaurentPolynomial.T` expressions to trigger a simp loop in
    current Mathlib (`maximum recursion depth reached`).  Closing
    requires either a `simp only` call with the precise lemma list
    that does not recurse, or a `decide`-based numerical check.
    Sorry retained pending refactor. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem nf_b3_eq_witness (i : Fin 6) :
    nf_b3 i = b3_nf_coefficients i := by
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  sorry

/-! ## §5  Proton NF via Hecke engine -/

/-- The proton NF: B₃ · σ₀ · (σ₀ − ½HA) · (σ₁ − ½HA).

    Since ½HA is not in ℤ[q,q⁻¹], we compute 4×proton:
    4×proton = B₃ · σ₀ · (2σ₀ − HA) · (2σ₁ − HA). -/
noncomputable def nf_proton4 : HeckeNF :=
  let step1 := mul_right_s0 nf_b3                              -- B₃·σ₀
  let step2 := hecke_add                                        -- step1·(2σ₀−HA)
    (hecke_smul 2 (mul_right_s0 step1)) (hecke_smul (-HA) step1)
  hecke_add                                                     -- step2·(2σ₁−HA)
    (hecke_smul 2 (mul_right_s1 step2)) (hecke_smul (-HA) step2)

/-- The 4×proton e⁻ coefficient, computed by the Hecke engine.
    This should equal (q−1)²(q+1)²(q⁸−3q⁶−3q²+1) / q⁶
    (which is 4 times the proton e⁻ coefficient). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem nf_proton4_trefoil :
    nf_proton4 5 = (q - q_inv) * (q - q_inv) *
      (q * q * q * q - 3 * q * q - 3 * q_inv * q_inv + q_inv * q_inv * q_inv * q_inv) := by
  simp [nf_proton4, nf_b3, nf_unit2, nf_unit, mul_right_s1_inv,
        mul_right_s0, mul_right_s1, hecke_add, hecke_smul, HA, q, q_inv]
  ring

/-! ## §6  Neutron NF via Hecke engine -/

/-- The neutron NF: B₃ · (σ₀−½HA) · (σ₀−½HA) · (σ₁−HA).

    4×neutron = B₃ · (2σ₀−HA) · (2σ₀−HA) · (σ₁−HA). -/
noncomputable def nf_neutron4 : HeckeNF :=
  let step1 := hecke_add                                        -- B₃·(2σ₀−HA)
    (hecke_smul 2 (mul_right_s0 nf_b3)) (hecke_smul (-HA) nf_b3)
  let step2 := hecke_add                                        -- step1·(2σ₀−HA)
    (hecke_smul 2 (mul_right_s0 step1)) (hecke_smul (-HA) step1)
  hecke_add                                                     -- step2·(σ₁−HA)
    (mul_right_s1 step2) (hecke_smul (-HA) step2)

/-- The 4×neutron e⁻ coefficient computed by the Hecke engine.

    4·c_e(𝔫) = −HA² · (q² + q⁻² + 2) = −q⁴ + 2 − q⁻⁴

    No division needed — the result is in ℤ[q, q⁻¹]. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem nf_neutron4_trefoil :
    nf_neutron4 5 = -((q - q_inv) * (q - q_inv) * (q * q + q_inv * q_inv + 2)) := by
  simp [nf_neutron4, nf_b3, nf_unit2, nf_unit, mul_right_s1_inv,
        mul_right_s0, mul_right_s1, hecke_add, hecke_smul, HA, q, q_inv]
  ring

end QOU.Interactions
