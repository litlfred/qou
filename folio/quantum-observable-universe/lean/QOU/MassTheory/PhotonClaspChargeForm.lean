import Mathlib.Tactic

/-!
# Photon clasps on the Borromean core: the charge-weighted quadratic form

Formalize-first scaffold for the "Compton subtraction" proposal assessed in
`computations/probes/compton_clasp/RESULT.md`. The proposal adjoins a fourth
strand to the three-strand Borromean core `B = (σ₀σ₁⁻¹)³ ∈ H₃(q)`, lets it clasp
quark strand `i` (or strands `i` and `j`), closes it with the convention-D
Markov conditional expectation `E₄ : H₄(q) → H₃(q)`, and weights the resulting
traces `D_ij = tr_D(B · E₄(L_ij))` by quark charges.

## What is proved here (unconditional, generic field)

* `chargeForm_symCore` — on a strand-symmetric matrix (`D_ii = a`, `D_ij = b`)
  the charge form is `b·Q_tot² + (a − b)·ΣQᵢ²` (the "Thomson + subtraction"
  split of the proposal).
* `pMinusN_general` — for ANY symmetric 3×3 matrix and the odd strand in
  position 2, `F(uud) − F(ddu) = (a₀ + a₁ − a₂)/3 + (2/3)·b₀₁`. Only the pair
  of like-flavour strands enters the off-diagonal part.
* `pMinusN_symCore` — on a strand-symmetric matrix, `p − n = a/3 + 2b/3`
  (agrees with `ChargeQuadraticSumRule.pn_energy_gap` at `A = a`, `B = 2b`).
* `merScalar_eq` — the single-strand clasp scalar `1 + (q − q⁻¹)·z_D`
  equals `(q⁴ + 1)/(q² + 1)`, and `merScalar_one` — it is `1` at `q = 1`.
* `pMinusN_factorised` / `pMinusN_connected` — if the diagonal entries equal
  `m·t` and the like-flavour pair entry equals `m²·t + c`, then
  `p − n = t·(m/3 + 2m²/3) + (2/3)·c`, and the connected part (with the
  disconnected `m·t`, `m²·t` removed) is exactly `(2/3)·c`.
* `pMinusN_at_classical_point` — at `t = m = 1`, `c = 0` the split is `1`,
  i.e. `Q_p² − Q_n²`: only the total-charge (Thomson) piece survives.

## What is NOT proved here (probe-measured, exact symbolic)

The values of `t = tr_D(B)`, the clasp scalar on `B`, and the connected pair
terms `c_ij` are computed by the exact rational-function probe
`computations/probes/compton_clasp/compton_clasp_probe.py` in `H₄(q)` with
`σ² = (q − q⁻¹)σ + 1` and `z_D = q³/(q² + 1)`. They are recorded below as the
closed forms `trBor`, `connK` and are NOT derived in Lean; deriving them from
a Lean Hecke-algebra model is follow-up work.

No empirical value enters this file. Quark charges `2/3`, `−1/3` are the
quantum numbers already used in `NeutronProtonEMSign` and
`ChargeQuadraticSumRule`.

## Ruling caveat

Closing the fourth strand is a photon emitted and reabsorbed: a virtual loop,
which the owner ruling of 2026-11-16 excludes. The algebra here is stated about
the Markov conditional expectation, not about virtual photons; a physical
reading must go through prior entangled photons or unseen intermediary
emitters, and none is constructed here. The fourth strand is also not the
ruled photon `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`.

-- Ref: [leitner2026] computations/probes/compton_clasp/RESULT.md
-/

namespace QOU.MassTheory.PhotonClaspChargeForm

variable {R : Type*} [Field R]

/-- The charge-weighted quadratic form `Σ_{i,j} Qᵢ Qⱼ D_ij` of a symmetric
3×3 matrix with diagonal `a₀ a₁ a₂` and off-diagonal `b₀₁ b₀₂ b₁₂`. -/
def chargeForm (Q0 Q1 Q2 a0 a1 a2 b01 b02 b12 : R) : R :=
  Q0 ^ 2 * a0 + Q1 ^ 2 * a1 + Q2 ^ 2 * a2
    + 2 * (Q0 * Q1 * b01 + Q0 * Q2 * b02 + Q1 * Q2 * b12)

/-- **Thomson + subtraction split.** On a strand-symmetric matrix the charge form
is `b·Q_tot² + (a − b)·ΣQᵢ²`. -/
theorem chargeForm_symCore (Q0 Q1 Q2 a b : R) :
    chargeForm Q0 Q1 Q2 a a a b b b
      = b * (Q0 + Q1 + Q2) ^ 2 + (a - b) * (Q0 ^ 2 + Q1 ^ 2 + Q2 ^ 2) := by
  unfold chargeForm; ring

/-- **Proton minus neutron, any symmetric matrix** (odd strand in position 2).
Only the like-flavour pair `b₀₁` enters off the diagonal. -/
theorem pMinusN_general (a0 a1 a2 b01 b02 b12 : R) :
    chargeForm (2 / 3) (2 / 3) (-1 / 3) a0 a1 a2 b01 b02 b12
      - chargeForm (-1 / 3) (-1 / 3) (2 / 3) a0 a1 a2 b01 b02 b12
      = (a0 + a1 - a2) / 3 + 2 * b01 / 3 := by
  unfold chargeForm; ring

/-- **Proton minus neutron, strand-symmetric matrix:** `a/3 + 2b/3`. -/
theorem pMinusN_symCore (a b : R) :
    chargeForm (2 / 3) (2 / 3) (-1 / 3) a a a b b b
      - chargeForm (-1 / 3) (-1 / 3) (2 / 3) a a a b b b
      = a / 3 + 2 * b / 3 := by
  rw [pMinusN_general]; ring

/-- Total charges: proton `1`, neutron `0`. -/
theorem totalCharge_proton : ((2 : R) / 3 + 2 / 3 + -1 / 3) = 1 := by ring
theorem totalCharge_neutron : ((-1 : R) / 3 + -1 / 3 + 2 / 3) = 0 := by ring

/-- The convention-D Markov parameter. -/
noncomputable def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The single-strand clasp scalar `E₄(σ₃²) = 1 + (q − q⁻¹)·z_D`. -/
noncomputable def merScalar (q : R) : R := 1 + (q - q⁻¹) * zD q

theorem merScalar_eq (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    merScalar q = (q ^ 4 + 1) / (q ^ 2 + 1) := by
  unfold merScalar zD
  field_simp
  ring

theorem merScalar_one [CharZero R] : merScalar (1 : R) = 1 := by
  unfold merScalar zD; norm_num

/-- **Factorised clasps.** Diagonal `m·t`, like-flavour pair `m²·t + c`. -/
theorem pMinusN_factorised (t m c b02 b12 : R) :
    chargeForm (2 / 3) (2 / 3) (-1 / 3) (m * t) (m * t) (m * t) (m ^ 2 * t + c) b02 b12
      - chargeForm (-1 / 3) (-1 / 3) (2 / 3) (m * t) (m * t) (m * t) (m ^ 2 * t + c) b02 b12
      = t * (m / 3 + 2 * m ^ 2 / 3) + 2 * c / 3 := by
  rw [pMinusN_general]; ring

/-- **Connected part.** With the disconnected pieces removed (diagonal `0`), only
`(2/3)·c` survives: the Thomson piece is exactly what the subtraction removes. -/
theorem pMinusN_connected (c b02 b12 : R) :
    chargeForm (2 / 3) (2 / 3) (-1 / 3) 0 0 0 c b02 b12
      - chargeForm (-1 / 3) (-1 / 3) (2 / 3) 0 0 0 c b02 b12
      = 2 * c / 3 := by
  rw [pMinusN_general]; ring

/-- **Classical point.** At `t = m = 1`, `c = 0` the split is `1 = Q_p² − Q_n²`. -/
theorem pMinusN_at_classical_point (b02 b12 : R) :
    chargeForm (2 / 3) (2 / 3) (-1 / 3) (1 * 1) (1 * 1) (1 * 1) (1 ^ 2 * 1 + 0) b02 b12
      - chargeForm (-1 / 3) (-1 / 3) (2 / 3) (1 * 1) (1 * 1) (1 * 1) (1 ^ 2 * 1 + 0) b02 b12
      = 1 := by
  rw [pMinusN_factorised]; ring

/-- Probe-measured closed form of `tr_D((σ₀σ₁⁻¹)³)` (not derived here). -/
noncomputable def trBor (q : R) : R :=
  1 - (q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (q ^ 4 * (q ^ 2 + 1) ^ 2)

theorem trBor_one [CharZero R] : trBor (1 : R) = 1 := by unfold trBor; norm_num

/-- Probe-measured numerator scale of the connected pair term (not derived
here): the symmetrised connected pair terms are `−connK q / q⁸` for the pairs
`(0,1)`, `(0,2)` and `+connK q / q⁶` for `(1,2)`. -/
noncomputable def connK (q : R) : R :=
  (q ^ 2 - 1) ^ 5 * (q ^ 4 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) / (2 * (q ^ 2 + 1) ^ 4)

theorem connK_one : connK (1 : R) = 0 := by unfold connK; norm_num

end QOU.MassTheory.PhotonClaspChargeForm
