import QOU.Descartes.GroundRing
import QOU.Descartes.TorusKnot
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic.Ring

/-!
# Transfer Matrices over ℤ[q, q⁻¹]

The 2×2 transfer matrices for the three nuclear vertex types
(proton–proton, neutron–neutron, proton–neutron), the inductive
chain construction, and the traced volume (Skein polynomial factor).

**Note to reader**: all definitions and proofs over `ℤ[q, q⁻¹]`.
Transfer matrices live in `M₂(ℤ[q, q⁻¹])` (not over ℝ).

## References

- [beta-decay-transfer-matrix] Prop: beta decay as universal matrix polynomial.
- [shell-closure-normal-form] Prop: palindromic Poincaré distribution.
-/

namespace QOU.Descartes

open Matrix

/-! ## §1  Ground ring `ℤ[t, t⁻¹]` (where `t² = q`)

The skein weights for `nn` and `pn` vertices involve `q^{1/2}`.
The transfer matrices therefore live in `M₂(ℤ[q^{1/2}, q^{-1/2}])`,
which is a degree-2 extension of `ℤ[q, q⁻¹]`.

For formal proofs, we can either:
1. Work in `ℤ[t, t⁻¹]` where `t = q^{1/2}` and `q = t²`
2. Work with `2 · 𝔴⁺` and `2 · 𝔴⁰` to clear denominators

We adopt option (1): set `t = q^{1/2}` and define everything
in `ℤ[t, t⁻¹]`. -/

/-- Extended ground ring: `ℤ[t, t⁻¹]` where `t² = q`. -/
abbrev R_t := LaurentPolynomial ℤ

/-- `t` (= q^{1/2}) in `ℤ[t, t⁻¹]`. -/
noncomputable def t : R_t := LaurentPolynomial.T 1

/-- `t⁻¹` (= q^{-1/2}) in `ℤ[t, t⁻¹]`. -/
noncomputable def t_inv : R_t := LaurentPolynomial.T (-1)

/-- `q = t²` in `ℤ[t, t⁻¹]`. -/
noncomputable def q_from_t : R_t := t * t

/-- `q⁻¹ = t⁻²` in `ℤ[t, t⁻¹]`. -/
noncomputable def q_inv_from_t : R_t := t_inv * t_inv

/-- The skein amplitude `s = t − t⁻¹ = q^{1/2} − q^{-1/2}`. -/
noncomputable def s_skein : R_t := t - t_inv

/-- Hecke amplitude over `ℤ[t, t⁻¹]`: `HA = q − q⁻¹ = t² − t⁻²`. -/
noncomputable def HA_t : R_t := q_from_t - q_inv_from_t

/-! ## §2  Skein weights (vertex amplitudes) -/

/-- A vertex type: the crossing between two nucleons. -/
inductive VertexType where
  | pp  -- proton ⁱ⋈_j proton
  | nn  -- neutron _j⋈ⁱ neutron
  | pn  -- proton ⁱ⋈_j neutron
  deriving DecidableEq, Repr

/-- Nucleon type. -/
inductive NucleonType where
  | proton
  | neutron
  deriving DecidableEq, Repr, Inhabited

/-- Determine vertex type from two nucleon types. -/
def vertexType : NucleonType → NucleonType → VertexType
  | .proton, .proton => .pp
  | .neutron, .neutron => .nn
  | _, _ => .pn

/-- The crossing amplitude `𝔴⁺(q)` at a vertex (coefficient on σ).
    From the Hecke relation σ⁻¹ = σ - (q - q⁻¹):
    - pp: 1  (positive crossing = σ)
    - nn: 1  (negative crossing = σ⁻¹ = σ - HA)
    - pn: 1  (mixed = ½(σ + σ⁻¹), DOUBLED below to avoid ½) -/
noncomputable def w_plus_t (v : VertexType) : R_t :=
  match v with
  | .pp => 1
  | .nn => 1                                -- σ⁻¹ has coeff 1 on σ
  | .pn => 2                                -- DOUBLED: actual is ½ of this

/-- The smoothing amplitude `𝔴⁰(q)` at a vertex (coefficient on 𝟏).
    From the Hecke relation σ⁻¹ = σ - (q - q⁻¹):
    - pp: 0
    - nn: −(q − q⁻¹) = −HA
    - pn: −(q − q⁻¹)  (DOUBLED: actual is −HA/2) -/
noncomputable def w_zero_t (v : VertexType) : R_t :=
  match v with
  | .pp => 0
  | .nn => -HA_t                             -- −(q − q⁻¹)
  | .pn => -HA_t                             -- −(q − q⁻¹) (DOUBLED)

/-! **Convention**: for `pn` vertices, `w_plus_t` and `w_zero_t`
    return the DOUBLED values `2𝔴⁺` and `2𝔴⁰`.  The factor of 2
    is tracked through the computation and cancels in the Q ratio
    (same number of pn crossings in parent and daughter). -/

/-! ## §3  Transfer matrix (over ℤ[t, t⁻¹]) -/

/-- A 2×2 transfer matrix over `ℤ[t, t⁻¹]`. -/
abbrev TMatrix := Matrix (Fin 2) (Fin 2) R_t

/-- The transfer matrix `T(𝔴⁺, 𝔴⁰)` at a single crossing.

    T(c, d) = ⎡ c·HA + d,  c ⎤
              ⎣ c,          d ⎦

    where `c = 𝔴⁺` and `d = 𝔴⁰`. -/
noncomputable def transferMatrix (c d : R_t) : TMatrix :=
  !![c * HA_t + d, c; c, d]

/-- Transfer matrix for a proton–proton crossing: `T(1, 0)`. -/
noncomputable def T_pp : TMatrix := transferMatrix 1 0

/-- Transfer matrix for a neutron–neutron crossing: `T(1, −HA)`.
    From the Hecke relation: σ⁻¹ = σ − (q − q⁻¹). -/
noncomputable def T_nn : TMatrix :=
  transferMatrix 1 (-HA_t)

/-- Transfer matrix for a proton–neutron crossing.
    `𝔴⁺ = 1`, `𝔴⁰ = −HA/2`.

    **Note**: the factor ½ takes us to `ℤ[½][t, t⁻¹]`.
    For formal proofs, we work with `2·T_pn` to stay integral. -/
noncomputable def two_T_pn : TMatrix :=
  -- 2·T_pn has integer coefficients: 𝔴⁺ = 2, 𝔴⁰ = −HA
  transferMatrix 2 (-HA_t)

/-! ## §3  Markov parameter and traced volume -/

/-- The Markov parameter `z = 1/(t + t⁻¹) = 1/(q^{1/2} + q^{-1/2})`.

    This is NOT in `ℤ[t, t⁻¹]` — it's in the fraction field.
    For formal proofs involving `z`, we work with the denominator
    `t + t⁻¹` explicitly and clear it from equations. -/
noncomputable def markov_denom : R_t := t + t_inv

/-- The traced volume `V̂ = z · M[0][0] + M[1][0]` rewritten as
    `(t + t⁻¹) · V̂ = M[0][0] + (t + t⁻¹) · M[1][0]`.

    We work with the **cleared** form to stay in `ℤ[t, t⁻¹]`. -/
noncomputable def tracedVolCleared (M : TMatrix) : R_t :=
  M 0 0 + markov_denom * (M 1 0)

/-! ## §4  Inductive chain construction -/

/-- A nuclear configuration: a list of nucleon types. -/
abbrev NuclearConfig := List NucleonType

/-- The transfer matrix for a crossing between nucleon types `a` and `b`.

    Returns `2 · T` (doubled to stay integral for pn crossings).
    The factor of 2 is tracked and cancelled in the final Q formula. -/
noncomputable def crossingMatrix (a b : NucleonType) : TMatrix :=
  match vertexType a b with
  | .pp => 2 • T_pp           -- 2 · T_pp (scale to match doubled pn)
  | .nn => 2 • T_nn           -- 2 · T_nn
  | .pn => two_T_pn           -- already doubled

/-- Extend a chain matrix by one more crossing. -/
noncomputable def extendChain (M : TMatrix) (a b : NucleonType) : TMatrix :=
  M * crossingMatrix a b

/-- The identity 2×2 matrix (start of a new chain). -/
noncomputable def chainStart : TMatrix := 1

/-- Build all chain matrices for a nuclear configuration inductively.

    When nucleon `k` is added:
    1. Each existing chain `M_j` is extended: `M_j ← M_j · T(j, k)`
    2. A new chain `M_{k-1}` is created: `M_{k-1} = T(k-1, k)`

    Returns the list of chain matrices. -/
noncomputable def buildChains : NuclearConfig → List TMatrix
  | [] => []
  | [_] => []  -- single nucleon: no crossings
  | config =>
    let A := config.length
    -- Build chains by processing nucleons left to right
    config.foldl (fun (acc : List TMatrix × ℕ) nk =>
      let (chains, k) := acc
      if k = 0 then (chains, k + 1)
      else
        -- Extend existing chains
        let extended := chains.mapIdx fun j Mj =>
          extendChain Mj (config.get! j) nk
        -- New chain for position k-1
        let newChain := crossingMatrix (config.get! (k - 1)) nk
        (extended ++ [newChain], k + 1)
    ) ([], 0) |>.1

/-! ## §5  Skein polynomial -/

/-- The Skein polynomial `P(q)` (cleared form) as a product of
    traced volumes.  The actual `P = ∏ V̂_j`, but we compute
    `∏ ((t+t⁻¹)·V̂_j)` to stay integral.

    The power of `(t+t⁻¹)` in the denominator is `A-1`
    (one factor per chain). -/
noncomputable def skeinPolynomialCleared (config : NuclearConfig) : R_t :=
  let chains := buildChains config
  chains.foldl (fun acc M => acc * tracedVolCleared M) 1

end QOU.Descartes
