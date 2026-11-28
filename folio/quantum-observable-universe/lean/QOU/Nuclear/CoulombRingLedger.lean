import QOU.Nuclear.CoulombIsospinChannel

/-!
# The Coulomb term ledger on the ring-valued mass — gap G3, ranks 0, 1, 2

Bean `qou-tcl3` (under `qou-s028`). Audit `docs/audits/2026-11-27-coulomb-ring-ledger.md`.
Builds on `QOU.Nuclear.CoulombIsospinChannel` (the charge structure, PR #9691) and on the
ring-valued mass `def:mass-identity` (`m = [2]ⁿ q^{−2w} ∫_A ρ(β)`, PRs #9789, #9805; Lean
`QOU.Observations.ElectronRingMassReading`, `RingMassLinkingNumber`).

`CoulombIsospinChannel` gives the EM channel as an **energy** `ε·Z(Z − 1)/2` with a scalar pair
weight `ε`. The corpus mass is ring-valued, and an energy is a *reading* of a ring element: the
log reading `E₀·log` (binding, PR #9793) or the energy reading `U = −q ∂_q log` (PR #9789). This
file puts the EM channel on the ring first and reads it second.

## Set-up

The EM channel enters the ring mass multiplicatively, one factor `μ` per proton pair:
`m = m_s · μ^{C(Z,2)}` with `m_s` the strong (braid-channel) mass and `C(Z,2) = Z(Z − 1)/2`.
A *reading* is any map `ρ` with `ρ(x y) = ρ x + ρ y` and `ρ 1 = 0`. Both corpus readings are of
this kind: `log` on positive values, and the logarithmic derivative `−q ∂_q log` on nonzero
elements of the fraction field (`logDer_mul`, proved here for any Leibniz map).

## What is proved (generic field, no measured value)

* `reading_pow`: `ρ(μⁿ) = n·ρ(μ)`.
* `reading_ledger`: for every reading, `ρ(m_s μ^{C(Z,2)}) = ρ(m_s) + imme(εa, εb, εc, T_z)` with
  `ε = ρ(μ)` and the derived `a = A(A−2)/8`, `b = (A−1)/2`, `c = 1/2`.
  So **ranks 0, 1, 2 survive the ring**, and the ring changes only what `ε` is: one ring element
  `μ`, read by whichever reading the binding uses.
* `reading_ratio_invariant`: the ratios `b/c = A − 1`, `a/c = A(A − 2)/4` do not depend on the
  reading, nor on `μ`.
* `two_readings_one_mu`: the log-reading pair weight and the energy-reading pair weight are two
  readings of the **same** `μ`; once the channel is put on the ring, they are not independent
  constants.
* `logDer_mul`: for any Leibniz map `D`, `D(xy)/(xy) = D x/x + D y/y`. So the energy reading is a
  reading in the sense above.
* The framing factor `[2]^{3A} q^{−2w}` depends only on the strand count `3A` and the writhe,
  and the braid channel is rank 0 (`braid_rank_zero`, term-completeness ledger). So across a
  multiplet with a fixed word the framing correction adds no `T_z` dependence and cannot imitate
  an EM term. (No new theorem: it is the definition plus the cited rank-0 result.)
* `monomial_reading`: if `μ = q^s` (a unit of `K[q, q⁻¹]`, the only kind that leaves the
  `q = 1` value `m(1)` unchanged up to sign), then the energy reading is `ε = −s`, an exact
  integer, and `m(1)` is unchanged by the EM channel (`monomial_at_one`). This is a
  *consequence* of a hypothesis on `μ`, recorded so that the hypothesis is visible.
* `quark_exponent_integral`: at the quark level the pair products `Q_i Q_j` lie in `(1/9)ℤ`
  (`9·Q_iQ_j ∈ {4, −2, 1}`). So a ring factor `ν^{Q_iQ_j}` per quark pair is a ring element only
  if `ν = μ₀⁹`. The nucleon-level pair exponent is then `9` quark units. Again a consequence of a
  hypothesis (a per-quark-pair monomial), recorded.

## What is not proved, and is named

* **Which `μ`.** The corpus has no derived ring element for the photon-exchange factor. Its
  reading `ε` is the same open scale as before (`r_rms`, beans `qou-mbfv`, `qou-usft`). This file
  does not choose one, and nothing here is selected against a measured value.
* **The `T(T + 1)` piece** of the rank-0 entry (`em_rank_zero`) belongs to gap G2 (bean
  `qou-tcl2`, held by the owner). It is cited, not changed.
-/

namespace QOU.Nuclear.CoulombRingLedger

open QOU.Nuclear.CoulombIsospinChannel

section Reading

variable {M : Type*} [CommMonoid M] {K : Type*} [Field K]

/-- A reading: a map from the multiplicative ring mass to an additive energy scale. -/
structure Reading (M K : Type*) [CommMonoid M] [Field K] where
  /-- The reading map. -/
  toFun : M → K
  /-- The empty product reads `0`. -/
  map_one : toFun 1 = 0
  /-- Products read as sums. -/
  map_mul : ∀ x y, toFun (x * y) = toFun x + toFun y

/-- **`ρ(μⁿ) = n·ρ(μ)`.** -/
theorem reading_pow (ρ : Reading M K) (μ : M) (n : ℕ) : ρ.toFun (μ ^ n) = n * ρ.toFun μ := by
  induction n with
  | zero => simp [ρ.map_one]
  | succ n ih =>
    rw [pow_succ, ρ.map_mul, ih]
    push_cast
    ring

/-- The ring mass of a nucleus with `Z` protons: strong mass times one EM factor per proton
pair. -/
def ringMassEM (ms μ : M) (Z : ℕ) : M := ms * μ ^ (Z.choose 2)

theorem cast_choose_two [CharZero K] (Z : ℕ) : ((Z.choose 2 : ℕ) : K) = (Z : K) * ((Z : K) - 1) / 2 := by
  rw [Nat.choose_two_right]
  rcases Nat.even_or_odd Z with h | h
  · obtain ⟨k, rfl⟩ := h
    rcases k with _ | k
    · simp
    · have : (k + 1 + (k + 1)) * (k + 1 + (k + 1) - 1) / 2 = (k + 1) * (2 * k + 1) := by
        have e : k + 1 + (k + 1) - 1 = 2 * k + 1 := by omega
        rw [e]
        have e2 : (k + 1 + (k + 1)) * (2 * k + 1) = 2 * ((k + 1) * (2 * k + 1)) := by ring
        rw [e2, Nat.mul_div_cancel_left _ (by norm_num)]
      rw [this]
      push_cast
      field_simp
      ring
  · obtain ⟨k, rfl⟩ := h
    have : (2 * k + 1) * (2 * k + 1 - 1) / 2 = (2 * k + 1) * k := by
      have e : 2 * k + 1 - 1 = 2 * k := by omega
      rw [e]
      have e2 : (2 * k + 1) * (2 * k) = 2 * ((2 * k + 1) * k) := by ring
      rw [e2, Nat.mul_div_cancel_left _ (by norm_num)]
    rw [this]
    push_cast
    field_simp
    ring

/-- **The Coulomb term ledger on the ring.** For every reading `ρ`, the EM channel reads as the
IMME polynomial with derived coefficients and the single pair weight `ε = ρ(μ)`. -/
theorem reading_ledger [CharZero K] (ρ : Reading M K) (ms μ : M) (Z N : ℕ) :
    ρ.toFun (ringMassEM ms μ Z)
      = ρ.toFun ms + imme (ρ.toFun μ * emA ((Z : K) + N)) (ρ.toFun μ * emB ((Z : K) + N))
          (ρ.toFun μ * emC) (((Z : K) - N) / 2) := by
  rw [ringMassEM, ρ.map_mul, reading_pow, cast_choose_two]
  have h := emEnergy_imme (ρ.toFun μ) (Z : K) (N : K) ((Z : K) + N) (((Z : K) - N) / 2) rfl rfl
  rw [emEnergy] at h
  rw [← h]
  ring

/-- **The rank ratios do not depend on the reading or on `μ`.** -/
theorem reading_ratio_invariant [CharZero K] (ρ : Reading M K) (μ : M) (A : K) :
    ρ.toFun μ * emB A = (A - 1) * (ρ.toFun μ * emC)
      ∧ ρ.toFun μ * emA A = A * (A - 2) / 4 * (ρ.toFun μ * emC) := by
  constructor
  · rw [emB_eq]; ring
  · rw [emA_eq]; ring

/-- **Two readings, one `μ`.** Under any two readings the EM ledger has the same shape, and the
two pair weights are the two readings of the same ring element. -/
theorem two_readings_one_mu [CharZero K] (ρ₁ ρ₂ : Reading M K) (ms μ : M) (Z N : ℕ) :
    ρ₁.toFun (ringMassEM ms μ Z) - ρ₁.toFun ms
        = imme (ρ₁.toFun μ * emA ((Z : K) + N)) (ρ₁.toFun μ * emB ((Z : K) + N))
            (ρ₁.toFun μ * emC) (((Z : K) - N) / 2)
      ∧ ρ₂.toFun (ringMassEM ms μ Z) - ρ₂.toFun ms
        = imme (ρ₂.toFun μ * emA ((Z : K) + N)) (ρ₂.toFun μ * emB ((Z : K) + N))
            (ρ₂.toFun μ * emC) (((Z : K) - N) / 2) := by
  constructor
  · rw [reading_ledger]; ring
  · rw [reading_ledger]; ring

/-- **Mirror split on the ring.** For a mirror pair the strong factor is common (rank 0), so the
reading difference is `ε·(A − 1)·T_z`, `ε = ρ(μ)`. -/
theorem reading_mirror [CharZero K] (ρ : Reading M K) (μ : M) (A Tz : K) :
    imme (ρ.toFun μ * emA A) (ρ.toFun μ * emB A) (ρ.toFun μ * emC) Tz
        - imme (ρ.toFun μ * emA A) (ρ.toFun μ * emB A) (ρ.toFun μ * emC) (-Tz)
      = ρ.toFun μ * (A - 1) * Tz :=
  emEnergy_mirror _ _ _

end Reading

section LogDer

variable {K : Type*} [Field K]

/-- The logarithmic derivative `D x / x` for a Leibniz map `D`. -/
def logDer (D : K → K) (x : K) : K := D x / x

/-- **The energy reading is a reading.** For any `D` with `D(xy) = x D y + y D x`,
`D(xy)/(xy) = D x/x + D y/y` on nonzero `x, y`. -/
theorem logDer_mul (D : K → K) (hD : ∀ x y, D (x * y) = x * D y + y * D x) (x y : K)
    (hx : x ≠ 0) (hy : y ≠ 0) : logDer D (x * y) = logDer D x + logDer D y := by
  unfold logDer
  rw [hD]
  field_simp
  ring

/-- `D 1 = 0` for a Leibniz map, so `logDer D 1 = 0`. -/
theorem logDer_one (D : K → K) (hD : ∀ x y, D (x * y) = x * D y + y * D x) : logDer D 1 = 0 := by
  have h := hD 1 1
  simp only [mul_one, one_mul] at h
  have : D 1 = 0 := by linear_combination -h
  simp [logDer, this]

/-- The energy reading `U = −q·D/·` on the nonzero elements, as a `Reading`. -/
def energyReading (D : K → K) (hD : ∀ x y, D (x * y) = x * D y + y * D x) (q : K) :
    Reading Kˣ K where
  toFun x := -q * logDer D (x : K)
  map_one := by simp [logDer_one D hD]
  map_mul x y := by
    simp only [Units.val_mul]
    rw [logDer_mul D hD _ _ x.ne_zero y.ne_zero]
    ring

/-- **Monomial EM factor.** If `D q = 1` (so `q D` is the Euler operator `q ∂_q`) and
`μ = q^s`, the energy reading of `μ` is `−s`. -/
theorem monomial_reading (D : K → K) (hD : ∀ x y, D (x * y) = x * D y + y * D x) (q : K)
    (hq : q ≠ 0) (hDq : D q = 1) (s : ℕ) : -q * logDer D (q ^ s) = -(s : K) := by
  have hpow : ∀ n : ℕ, D (q ^ n) = n * q ^ (n - 1) := by
    intro n
    induction n with
    | zero =>
      have h := hD 1 1
      simp only [mul_one, one_mul] at h
      simp; linear_combination -h
    | succ n ih =>
      rw [pow_succ, hD, ih, hDq]
      rcases n with _ | n
      · simp
      · simp only [Nat.add_sub_cancel]
        push_cast
        rw [pow_succ]
        ring
  unfold logDer
  rw [hpow]
  rcases s with _ | s
  · simp
  · simp only [Nat.add_sub_cancel]
    rw [pow_succ]
    field_simp

/-- **At `q = 1` a monomial EM factor leaves the mass unchanged.** -/
theorem monomial_at_one {R : Type*} [CommRing R] (ms : R) (s Z : ℕ) :
    ms * ((1 : R) ^ s) ^ (Z.choose 2) = ms := by
  simp

end LogDer

section QuarkExponent

/-- **Quark pair products are ninths.** With charges `2/3` and `−1/3`, `9·Q_iQ_j ∈ {4, −2, 1}`. -/
theorem quark_exponent_integral :
    (9 : ℚ) * ((2 / 3) * (2 / 3)) = 4 ∧ (9 : ℚ) * ((2 / 3) * (-1 / 3)) = -2
      ∧ (9 : ℚ) * ((-1 / 3) * (-1 / 3)) = 1 := by
  norm_num

/-- The internal (unordered) quark-pair exponents in ninths: `uud` gives `0`, `udd` gives `−3`.
These are `9·½·pairSum` of `proton_internal` and `neutron_internal`. -/
theorem internal_exponents :
    (9 : ℚ) * (1 / 2) * 0 = 0 ∧ (9 : ℚ) * (1 / 2) * (-2 / 3) = -3 := by
  norm_num

end QuarkExponent

end QOU.Nuclear.CoulombRingLedger
