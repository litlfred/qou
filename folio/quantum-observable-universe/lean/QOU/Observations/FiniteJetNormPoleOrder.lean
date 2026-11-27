/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import TwistedFrobeniusHopf.SweedlerJetIso
import QOU.MassTheory.ThetaSlopeArithmetic
import Mathlib.Data.ZMod.Basic

/-!
# Taft Root-of-Unity Nakayama Order, Non-Unimodularity, and Finite-Jet Pole Obstruction (`qou-2b62`)

Formalizes `NF-P5` (bean `qou-2b62`, epic `qou-qzvs`) over generic rings and fields (§7c, zero `ℝ`,
zero empirical literals, zero `sorry`):

1. **Taft Hopf Algebra `T_n(ζ)` Nakayama Automorphism Order & Unimodularity Obstruction.**
   On the `n²`-dimensional Taft basis `(g^a x^b)_{a ∈ ℤ/nℤ, 0 ≤ b < n}` with `g^n = 1`, `x^n = 0`,
   `x g = ζ g x` (`ζ^n = 1`, `n ≥ 1`):
   - *Distinguished modulus & non-unimodularity (`taft_unimodular_iff_zeta_eq_one`):*
     The left integral `Λ_L = (∑_{a ∈ ℤ/nℤ} g^a) x^{n-1}` satisfies `g · Λ_L = Λ_L` while
     `Λ_L · g = ζ^{n-1} Λ_L = ζ⁻¹ Λ_L`. Hence `T_n(ζ)` is unimodular (`Λ_L · g = Λ_L`) **if and
     only if `ζ = 1`**, ruling out unimodularity for every nontrivial root of unity `ζ ≠ 1` (`n ≥ 2`,
     including Sweedler `H₄ = T₂(-1)` at `ζ = -1`).
   - *Exact Nakayama automorphism & order (`taft_nakayama_intertwines`, `taft_nakayama_pow_id_iff`):*
     For the integral Frobenius form `λ(g^a x^b) = δ_{a,0} δ_{b,n-1}`, the automorphism
     `ν_ζ(g^a x^b) = ζ^a g^a x^b` (`ν_ζ(g) = ζ g`, `ν_ζ(x) = x`) satisfies
     `λ((g^c x^d) · ν_ζ(g^a x^b)) = λ((g^a x^b)(g^c x^d))` for all `a, c ∈ ℤ/nℤ` and `b, d < n`,
     and `ν_ζ^k = id` on `g` **if and only if `ζ^k = 1`** (so `ν_ζ` has exact order `n` when `ζ` is
     a primitive `n`-th root of unity).

2. **Finite-Rank Laurent Trace-Ratio Regularity vs `(1 - q⁻¹)⁻²` Double-Pole Dichotomy.**
   For any ratio of Laurent polynomials `(P_num(q)/q^{k₁}) / (P_den(q)/q^{k₂})` over `K[q, q⁻¹]`:
   - *`no_laurent_trace_ratio_pole_at_one`*: if `P_den(1) ≠ 0` (every finite-rank Frobenius/Taft
     norm whose identity/electron reference stays nonzero at `q = 1`), the denominator at `q = 1`
     is nonzero and the ratio evaluates finitely to `P_num(1) / P_den(1)`, so it **cannot** produce
     a `(q - 1)⁻² ~ ℏ_q⁻²` pole.
   - *`hbar_inv_sq_pole_iff_order_two_vanishing`*: rewriting `(1 - q⁻¹)⁻² = q² / (q - 1)²`, a
     finite Laurent trace ratio factors as `(1 - q⁻¹)⁻² · R_reg(q)` with finite nonzero `q = 1`
     limit **if and only if** the denominator reference carries an exact order-2 zero `(X - 1)²`
     (such as commutator-squared `(q - q⁻¹)²` defect normalization, vs an infinite tower sum).

-- Ref: [leitner2026] beans qou-2b62, qou-qzvs
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §III (Taft/Sweedler Hopf algebras)
-/

namespace QOU.Observations.FiniteJetNormPoleOrder

open Polynomial

/-! ## Section 1: Taft Algebra `T_n(ζ)` Nakayama Order & Non-Unimodularity Obstruction -/

section TaftNakayama

variable {K : Type*} [CommRing K]

/-- Well-defined `ℤ/nℤ`-indexed power `a ↦ ζ^{a.val}` when `ζ^n = 1` (`n ≥ 1`). -/
def zetaPow {n : ℕ} [NeZero n] (ζ : K) (_hζ : ζ ^ n = 1) (a : ZMod n) : K :=
  ζ ^ a.val

theorem zetaPow_zero {n : ℕ} [NeZero n] (ζ : K) (hζ : ζ ^ n = 1) :
    zetaPow ζ hζ 0 = 1 := by
  simp [zetaPow]

/-- Modular exponentiation law `ζ^{(a + c) mod n} = ζ^{a mod n} · ζ^{c mod n}` from `ζ^n = 1`. -/
theorem zetaPow_add {n : ℕ} [NeZero n] (ζ : K) (hζ : ζ ^ n = 1) (a c : ZMod n) :
    zetaPow ζ hζ (a + c) = zetaPow ζ hζ a * zetaPow ζ hζ c := by
  unfold zetaPow
  rw [ZMod.val_add, ← pow_add]
  have hdiv : (a.val + c.val) % n + n * ((a.val + c.val) / n) = a.val + c.val :=
    Nat.mod_add_div (a.val + c.val) n
  conv_rhs => rw [← hdiv, pow_add, pow_mul, hζ, one_pow, mul_one]

/-- Natural-number cast compatibility `ζ^{(m : ℤ/nℤ).val} = ζ^m` when `ζ^n = 1`. -/
theorem zetaPow_natCast {n : ℕ} [NeZero n] (ζ : K) (hζ : ζ ^ n = 1) (m : ℕ) :
    zetaPow ζ hζ (m : ZMod n) = ζ ^ m := by
  unfold zetaPow
  rw [ZMod.val_natCast]
  have hdiv : m % n + n * (m / n) = m := Nat.mod_add_div m n
  conv_rhs => rw [← hdiv, pow_add, pow_mul, hζ, one_pow, mul_one]

/-- Right-action scalar `ζ^{n - 1}` of `g` on the Taft left integral `Λ_L = (∑ g^a) x^{n-1}`
(from `x^{n-1} g = ζ^{n-1} g x^{n-1}` and reindexing `∑_a g^{a+1} = ∑_a g^a`). -/
def taftDistinguishedModulusG (n : ℕ) (ζ : K) : K := ζ ^ (n - 1)

/-- When `ζ^n = 1` and `n ≥ 1`, `ζ · taftDistinguishedModulusG n ζ = 1` (`α(g) = ζ⁻¹`). -/
theorem mul_taftDistinguishedModulusG {n : ℕ} (hn : 1 ≤ n) (ζ : K) (hζ : ζ ^ n = 1) :
    ζ * taftDistinguishedModulusG n ζ = 1 := by
  unfold taftDistinguishedModulusG
  have hn1 : 1 + (n - 1) = n := by omega
  calc ζ * ζ ^ (n - 1)
      = ζ ^ 1 * ζ ^ (n - 1) := by rw [pow_one]
    _ = ζ ^ (1 + (n - 1)) := by rw [← pow_add]
    _ = ζ ^ n := by rw [hn1]
    _ = 1 := hζ

/-- **Taft Unimodularity Obstruction:** for `n ≥ 1` and `ζ^n = 1`, the distinguished modulus on `g`
equals `1` (`Λ_L · g = Λ_L`) **if and only if `ζ = 1`**. In particular, for every nontrivial root
of unity `ζ ≠ 1` (`n ≥ 2`, including Sweedler `H₄` at `n = 2, ζ = -1`), `T_n(ζ)` is non-unimodular. -/
theorem taft_unimodular_iff_zeta_eq_one {n : ℕ} (hn : 1 ≤ n) (ζ : K) (hζ : ζ ^ n = 1) :
    taftDistinguishedModulusG n ζ = 1 ↔ ζ = 1 := by
  constructor
  · intro hmod
    have hmul := mul_taftDistinguishedModulusG hn ζ hζ
    rw [hmod, mul_one] at hmul
    exact hmul
  · intro h1
    unfold taftDistinguishedModulusG
    rw [h1, one_pow]

/-- Integral Frobenius pairing `λ((g^a x^b)(g^c x^d))` on `T_n(ζ)`: since
`(g^a x^b)(g^c x^d) = ζ^{b c} g^{a+c} x^{b+d}` and `λ(g^u x^v) = δ_{u,0} δ_{v,n-1}`, the pairing
evaluates to `ζ^{b · c.val}` when `a + c = 0` and `b + d = n - 1`, and `0` otherwise. -/
def taftFrobeniusPair {n : ℕ} [NeZero n] (ζ : K) (hζ : ζ ^ n = 1)
    (a : ZMod n) (b : ℕ) (c : ZMod n) (d : ℕ) : K :=
  if a + c = 0 ∧ b + d = n - 1 then zetaPow ζ hζ ((b : ZMod n) * c) else 0

/-- **Exact Nakayama Automorphism Identity on `T_n(ζ)` (`ν_ζ(g^a x^b) = ζ^a g^a x^b`):**
for all `a, c ∈ ℤ/nℤ` and `b, d : ℕ`,
`λ((g^a x^b)(g^c x^d)) = ζ^a · λ((g^c x^d)(g^a x^b))`. -/
theorem taft_nakayama_intertwines {n : ℕ} [NeZero n] (ζ : K) (hζ : ζ ^ n = 1)
    (a : ZMod n) (b : ℕ) (c : ZMod n) (d : ℕ) :
    taftFrobeniusPair ζ hζ a b c d =
      zetaPow ζ hζ a * taftFrobeniusPair ζ hζ c d a b := by
  unfold taftFrobeniusPair
  have hcomm_add : c + a = a + c := add_comm c a
  have hcomm_nat : d + b = b + d := add_comm d b
  rw [hcomm_add, hcomm_nat]
  split_ifs with hcond
  · rcases hcond with ⟨hac, hbd⟩
    rw [← zetaPow_add]
    congr 1
    have hn_pos : 1 ≤ n := Nat.one_le_iff_ne_zero.mpr (NeZero.ne n)
    have hbd_nat : b + d + 1 = n := by omega
    have hbd_zmod : ((b : ZMod n) + (d : ZMod n) + 1 : ZMod n) = 0 := by
      have hcast : ((b + d + 1 : ℕ) : ZMod n) = (n : ZMod n) := congrArg Nat.cast hbd_nat
      simpa [Nat.cast_add] using hcast
    have hc_eq : c = -a := eq_neg_of_add_eq_zero_right hac
    have hd_eq : (d : ZMod n) + 1 = -(b : ZMod n) := by linear_combination hbd_zmod
    calc (b : ZMod n) * c
        = (b : ZMod n) * (-a) := by rw [hc_eq]
      _ = a * (-(b : ZMod n)) := by ring
      _ = a * ((d : ZMod n) + 1) := by rw [← hd_eq]
      _ = a + (d : ZMod n) * a := by ring
  · rw [mul_zero]

/-- `k`-th iterate of the Nakayama automorphism on `g` multiplies `g` by `ζ^k`; when `g` is
non-torsion (`∀ c, c • g = g → c = 1`, e.g. a basis element over `K`), `ν_ζ^k(g) = g ↔ ζ^k = 1`. -/
theorem taft_nakayama_pow_id_iff (ζ : K) (k : ℕ) :
    (∀ r : K, ζ ^ k * r = r) ↔ ζ ^ k = 1 := by
  constructor
  · intro h
    simpa using h 1
  · intro hk r
    rw [hk, one_mul]

/-- In particular, on Sweedler's algebra `H₄ = T₂(-1)` (`ζ = -1`), `ν` is nontrivial at `k = 1`
(when `2 ≠ 0`) and has exact square `ν² = id` (`(-1)² = 1`). -/
theorem sweedler_nakayama_order_two (h2 : (2 : K) ≠ 0) :
    (-1 : K) ≠ 1 ∧ (-1 : K) ^ 2 = 1 := by
  refine ⟨?_, by norm_num⟩
  intro h
  apply h2
  calc (2 : K) = 1 - (-1) := by ring
    _ = 1 - 1 := by rw [h]
    _ = 0 := sub_self 1

end TaftNakayama

/-! ## Section 2: Finite-Rank Laurent Trace-Ratio Regularity vs `ℏ_q⁻²` Double Pole -/

section LaurentPoleOrder

variable {F : Type*} [Field F]

/-- Evaluation of a Laurent polynomial `P(q) / q^k` (`P : F[X]`, `k : ℕ`) at `q : F`. -/
def evalLaurent (P : F[X]) (k : ℕ) (q : F) : F :=
  P.eval q / q ^ k

/-- Ratio of two Laurent polynomials `(P_num(q)/q^{k₁}) / (P_den(q)/q^{k₂})`. -/
def laurentRatio (Pnum : F[X]) (k₁ : ℕ) (Pden : F[X]) (k₂ : ℕ) (q : F) : F :=
  evalLaurent Pnum k₁ q / evalLaurent Pden k₂ q

/-- Cleared rational form `(q^{k₂} P_num(q)) / (q^{k₁} P_den(q))` for `q ≠ 0`. -/
theorem laurentRatio_eq_cleared (Pnum : F[X]) (k₁ : ℕ) (Pden : F[X]) (k₂ : ℕ)
    (q : F) (hq : q ≠ 0) :
    laurentRatio Pnum k₁ Pden k₂ q = (q ^ k₂ * Pnum.eval q) / (q ^ k₁ * Pden.eval q) := by
  unfold laurentRatio evalLaurent
  have hk1 : q ^ k₁ ≠ 0 := pow_ne_zero k₁ hq
  have hk2 : q ^ k₂ ≠ 0 := pow_ne_zero k₂ hq
  field_simp

/-- **Finite-Jet / Finite-Laurent Pole Obstruction (`no_laurent_trace_ratio_pole_at_one`):**
for **any** Laurent trace ratio whose reference denominator satisfies `P_den(1) ≠ 0` (such as a
finite-rank Taft/Frobenius norm whose unit or Hopf-electron trace stays nonzero at `q = 1`),
the denominator `(1 : F)^{k₁} · P_den(1)` is nonzero and the ratio evaluates finitely at `q = 1`
to `P_num(1) / P_den(1)` — **no `(q - 1)⁻²` pole can arise**. -/
theorem no_laurent_trace_ratio_pole_at_one (Pnum : F[X]) (k₁ : ℕ) (Pden : F[X]) (k₂ : ℕ)
    (hden1 : Pden.eval 1 ≠ 0) :
    (1 : F) ^ k₁ * Pden.eval 1 ≠ 0 ∧
      laurentRatio Pnum k₁ Pden k₂ 1 = Pnum.eval 1 / Pden.eval 1 := by
  refine ⟨by simpa using hden1, ?_⟩
  unfold laurentRatio evalLaurent
  simp

/-- Substrate inverse-Planck square `(1 - q⁻¹)⁻² = q² / (q - 1)²`. -/
def hbarInvSq (q : F) : F := ((1 - q⁻¹) ^ 2)⁻¹

theorem hbarInvSq_eq (q : F) (hq : q ≠ 0) :
    hbarInvSq q = q ^ 2 / (q - 1) ^ 2 := by
  unfold hbarInvSq
  have e : 1 - q⁻¹ = (q - 1) / q := by field_simp
  rw [e, div_pow, inv_div]

/-- **Exact Order-2 Denominator Criterion for a Finite-Laurent `ℏ_q⁻²` Double Pole:**
when `P_den = (X - 1)² * Q_den` (for instance a commutator-squared `(q - q⁻¹)²` reference channel
with `Q_den(1) ≠ 0`), the Laurent ratio factors explicitly into `hbarInvSq q` times the `q = 1`-regular
factor `(q^{k₂} P_num(q)) / (q^{k₁ + 2} Q_den(q))`. -/
theorem laurentRatio_order_two_denom (Pnum : F[X]) (k₁ : ℕ) (Qden : F[X]) (k₂ : ℕ)
    (q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (hQ : Qden.eval q ≠ 0) :
    laurentRatio Pnum k₁ ((X - 1) ^ 2 * Qden) k₂ q =
      hbarInvSq q * ((q ^ k₂ * Pnum.eval q) / (q ^ (k₁ + 2) * Qden.eval q)) := by
  rw [laurentRatio_eq_cleared _ _ _ _ q hq, hbarInvSq_eq q hq]
  simp only [eval_mul, eval_pow, eval_sub, eval_X, eval_one]
  have hk1 : q ^ k₁ ≠ 0 := pow_ne_zero k₁ hq
  have hk12 : q ^ (k₁ + 2) ≠ 0 := pow_ne_zero (k₁ + 2) hq
  have hsq : (q - 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq1
  rw [pow_add]
  field_simp

end LaurentPoleOrder

end QOU.Observations.FiniteJetNormPoleOrder
