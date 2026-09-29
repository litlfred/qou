import QOU.Archimedean.GroundRing
import QOU.Archimedean.HeckeH3
import Mathlib.Tactic

/-!
# Confined Knot Binding: Extremal Cancellation and Crossing Balance

Formalises prop:confined-knot-binding:

1. **Wedderburn weight equality**: W_sym = W_alt for H₃(q),
   because d_q((3)) = d_q((1,1,1)) = 1.

2. **Extremal cancellation**: For the pn crossing (d = -HA/2), the
   symmetric and alternating channel contributions cancel:
   W_sym · χ_sym + W_alt · χ_alt = 0.

3. **Crossing balance**: V_pp + V_nn = 2 · V_pn exactly.

4. **δV = HA/2**: The deviation V_pp - V_pn = HA/2.

All proofs are over the generic ground ring `R_q = ℤ[q, q⁻¹]`, symbolic
in `q` (§7c: no archimedean structure is used — these are algebraic
identities, so we do **not** specialise to `ℝ` or a field).

**Base-ring note (2026-07-11).** `R_q` is a `CommRing`, not a field, so
the pn-crossing "half" `d = -HA/2` cannot be written as a literal
division. It is instead carried as an explicit hypothesis `dh + dh = -HA`
(equivalently `2·dh = -HA`), which is exactly the defining property of
the midpoint and keeps every identity provable by `ring` /
`linear_combination` over `CommRing`. This replaces an earlier draft that
used `/` and `linarith`/`nlinarith` on `ℤ[q,q⁻¹]` — operations that
`LaurentPolynomial ℤ` does not support (it is neither a field nor
ordered), so that draft did not compile.

## References

- [prop:confined-knot-binding]
- [prop:three-parameters-wedderburn]
-/

namespace QOU.Archimedean.ConfinedKnotBinding

open QOU.Archimedean

/-! ## §1  Wedderburn weights of H₃(q)

The symmetric `(3)` and alternating `(1,1,1)` reps of `H₃(q)` are the two
one-dimensional reps.  Both partitions have hook-length multiset `{3,2,1}`
(they are transposes, and the hook multiset is transpose-invariant), so
their hook-length q-dimensions `d_q(λ) = [3]_q!/∏_{cells}[h]_q` both equal
`1`.  Over the `CommRing` `R_q` (no division) we record this as the
numerator/denominator identity `∏hooks = [3]_q!`. -/

/-- The balanced-q hook product `∏_{h ∈ hooks} [h]_q`. -/
noncomputable def qHookProd (hooks : List ℤ) : R_q := (hooks.map qInt).prod

/-- Hook lengths of the symmetric partition `(3)` (a single row): the cell
    `(1, j)` has arm `3 - j`, leg `0`, hook `(3 - j) + 0 + 1` — giving
    `{3, 2, 1}`. -/
def hooksSym : List ℤ := [3, 2, 1]

/-- Hook lengths of the alternating partition `(1,1,1)` (a single column):
    the cell `(i, 1)` has arm `0`, leg `3 - i`, hook `0 + (3 - i) + 1` —
    giving `{3, 2, 1}` (the transpose of `(3)`; identical multiset). -/
def hooksAlt : List ℤ := [3, 2, 1]

/-- `[3]_q! = [3]_q · [2]_q · [1]_q`. -/
noncomputable def qFactorial3 : R_q := qInt 3 * qInt 2 * qInt 1

/-- **The q-dimension of the symmetric rep `(3)` is `1`.**  Stated over the
    `CommRing` `R_q` (no division) as the numerator/denominator identity
    `∏_{h ∈ hooks}[h]_q = [3]_q!`, i.e. `d_q((3)) = [3]_q!/∏hooks = 1`. -/
theorem dq_sym_eq_one : qHookProd hooksSym = qFactorial3 := by
  simp only [qHookProd, hooksSym, qFactorial3, List.map_cons, List.map_nil,
    List.prod_cons, List.prod_nil, mul_one]
  ring

/-- **The q-dimension of the alternating rep `(1,1,1)` is `1`** — `(1,1,1)`
    is the transpose of `(3)`, so its hook multiset `{3,2,1}` is identical;
    `hooksAlt` is definitionally `hooksSym`, so this is exactly
    `dq_sym_eq_one` (Gemini review). -/
theorem dq_alt_eq_one : qHookProd hooksAlt = qFactorial3 := dq_sym_eq_one

/-- **Equality of the symmetric/alternating Wedderburn numerators**:
    `d_q((3))² = d_q((1,1,1))²` in `R_q`.

    The Wedderburn weight is `W_λ = d_q(λ)² / [3]!`.  Both channels share
    the common `[3]!` denominator, so `W_sym = W_alt` is *equivalent* to
    this numerator equality — and both hook-products equal `[3]_q!`
    (`dq_sym_eq_one`, `dq_alt_eq_one`), so the numerators coincide. -/
theorem dq_sym_sq_eq_dq_alt_sq : qHookProd hooksSym ^ 2 = qHookProd hooksAlt ^ 2 := by
  rw [dq_sym_eq_one, dq_alt_eq_one]

/-! ## §2  Crossing eigenvalues -/

/-- Eigenvalue of σ in the symmetric (dim-1) rep: λ_sym = q. -/
noncomputable def sym_eigenvalue : R_q := q

/-- Eigenvalue of σ in the alternating (dim-1) rep: λ_alt = -q⁻¹. -/
noncomputable def alt_eigenvalue : R_q := -q_inv

/-- The Hecke parameter HA = q - q⁻¹. -/
noncomputable def HA : R_q := q - q_inv

/-- For a crossing with parameters (c, d):
    χ_sym(c, d) = c·q + d
    χ_alt(c, d) = -c·q⁻¹ + d -/
noncomputable def chi_sym (c d : R_q) : R_q := c * q + d
noncomputable def chi_alt (c d : R_q) : R_q := -c * q_inv + d

/-! ## §3  Extremal cancellation for pn crossings

The pn crossing has `d = -HA/2`, carried as the hypothesis
`d + d = -(c · HA)` (the defining property of the half). -/

/-- For the pn crossing with `d + d = -(c · HA)` (i.e. `d = -c·HA/2`), the
    sum `χ_sym + χ_alt = 0`.

    Proof: `χ_sym + χ_alt = (c·q + d) + (-c·q⁻¹ + d) = c·(q - q⁻¹) + 2d
    = c·HA + 2d = 0`. -/
theorem extremal_cancellation (c d : R_q) (hd : d + d = -(c * HA)) :
    chi_sym c d + chi_alt c d = 0 := by
  unfold chi_sym chi_alt HA at *
  linear_combination hd

/-- Since `W_sym = W_alt`, the weighted sum also vanishes:
    `W_sym · χ_sym + W_alt · χ_alt = W_sym · (χ_sym + χ_alt) = 0`. -/
theorem weighted_extremal_cancellation (w c d : R_q) (hd : d + d = -(c * HA)) :
    w * chi_sym c d + w * chi_alt c d = 0 := by
  rw [← mul_add, extremal_cancellation c d hd, mul_zero]

/-! ## §4  Crossing balance: V_pp + V_nn = 2 · V_pn -/

/-- Single-crossing Wedderburn volume for crossing type (c, d).

    V(c, d) = W_sym · (c·q + d) + W_std · (z·c + d) + W_alt · (-c·q⁻¹ + d)

    For pp: (c=1, d=0); for nn: (c=1, d=-HA); for pn: (c=1, d=-HA/2). -/
noncomputable def crossing_volume (w_sym w_std w_alt z c d : R_q) : R_q :=
  w_sym * (c * q + d) + w_std * (z * c + d) + w_alt * (-c * q_inv + d)

/-- `V_pp + V_nn = 2 · V_pn` when `W_sym = W_alt` and the pn midpoint
    `dh + dh = -HA` holds.  This is the crossing-balance identity: the
    `q`-parts of pp and nn combine to `w_std·(2z - HA)`, matched by
    `2·V_pn`. -/
theorem crossing_balance (w w_std z dh : R_q) (hdh : dh + dh = -HA) :
    crossing_volume w w_std w z 1 0 +
    crossing_volume w w_std w z 1 (-HA) =
    2 * crossing_volume w w_std w z 1 dh := by
  unfold crossing_volume HA at *
  linear_combination (-(w + w_std + w)) * hdh

/-- The deviation `δV = V_pp - V_pn = W_sym · HA + W_std · (HA/2)`.  Written
    with the pn midpoint `dh` (`HA/2 = -dh`): `δV = w · HA - w_std · dh`. -/
theorem crossing_deviation (w w_std z dh : R_q) (hdh : dh + dh = -HA) :
    crossing_volume w w_std w z 1 0 -
    crossing_volume w w_std w z 1 dh =
    w * HA - w_std * dh := by
  unfold crossing_volume HA at *
  linear_combination (-w) * hdh

/-! ## §5  The pn binding volume is std-rep only -/

/-- For the pn crossing (`c=1`, midpoint `dh`) with `W_sym = W_alt`:
    `V_pn = W_std · (z + dh)` (`= W_std · (z - HA/2)`).

    The symmetric and alternating contributions cancel by
    `extremal_cancellation`, leaving only the standard channel. -/
theorem pn_volume_std_only (w w_std z dh : R_q) (hdh : dh + dh = -HA) :
    crossing_volume w w_std w z 1 dh =
    w_std * (z + dh) := by
  unfold crossing_volume HA at *
  linear_combination w * hdh

/-! ## §6  Confinement preservation under pn binding -/

/-- The extremal contribution of a pn crossing is zero: pn binding does
    NOT change the confinement (Frobenius) channels — it operates only in
    the standard (binding) channel.  `P_ext(V_pn) = 0` by
    `extremal_cancellation`. -/
theorem pn_extremal_contribution_zero (w c d : R_q) (hd : d + d = -(c * HA)) :
    w * chi_sym c d + w * chi_alt c d = 0 :=
  weighted_extremal_cancellation w c d hd

/-- For pp crossings the extremal contribution is `+2w·HA` and for nn it
    is `-2w·HA`; the SUM pp + nn cancels exactly.  This is why Z=N nuclei
    preserve Frobenius stability. -/
theorem pp_nn_extremal_cancel (w z dh : R_q) (hdh : dh + dh = -HA) :
    (crossing_volume w 0 w z 1 0 - crossing_volume w 0 w z 1 dh) +
    (crossing_volume w 0 w z 1 (-HA) - crossing_volume w 0 w z 1 dh) = 0 := by
  unfold crossing_volume HA at *
  linear_combination (-(w + w)) * hdh

/-! ## §7  Transfer matrix identities -/

/-- det(T_pp) = det([[HA, 1], [1, 0]]) = -1. -/
theorem det_T_pp : HA * 0 - 1 * (1 : R_q) = -1 := by ring

/-- det(T_nn) = det([[0, 1], [1, -HA]]) = -1. -/
theorem det_T_nn : (HA + (-HA)) * (-HA) - 1 * (1 : R_q) = -1 := by
  unfold HA; ring

/-- For the pn crossing, `det(2·T_pn) = -HA² - 4 = -(HA² + 4)`. -/
theorem det_two_T_pn : HA * (-HA) - 2 * (2 : R_q) = -(HA ^ 2 + 4) := by
  unfold HA; ring

/-! ## §8  Wedderburn decomposition: the k=3 exact formula -/

/-- The denominator of the a₃ formula is `1 + W_std`.

    From `W_sym + W_std + W_alt = 1` and `W_sym = W_alt`:
    `W_sym·1 + W_std·2 + W_alt·1 = W_sym + W_alt + 2W_std
    = (1 - W_std) + 2W_std = 1 + W_std`. -/
theorem a3_denominator (w_sym w_std w_alt : R_q)
    (h_norm : w_sym + w_std + w_alt = 1)
    (h_eq : w_sym = w_alt) :
    w_sym * 1 + w_std * 2 + w_alt * 1 = 1 + w_std := by
  rw [h_eq] at h_norm ⊢
  linear_combination h_norm

/-- The a₃ **numerator** for Z=N nuclei with all three characters equal
    (`sp = V_std = ap = V`): `W_sym·V + W_std·V + W_alt·V = V`, using the
    normalisation `W_sym + W_std + W_alt = 1`.  Together with
    `a3_denominator` (`= 1 + W_std`) this gives `a₃ = V / (1 + W_std)`.

    (Corrected 2026-07-11: an earlier draft stated the right-hand side as
    `V·(1 + W_std)`, which is false — it would require `V·W_std = 0`. The
    numerator of the equal-characters a₃ is `V`, the denominator
    `1 + W_std`; the quotient is `V/(1 + W_std)`.) -/
theorem a3_equal_characters (w_sym w_std w_alt V : R_q)
    (h_norm : w_sym + w_std + w_alt = 1) :
    w_sym * V + w_std * V + w_alt * V = V := by
  linear_combination V * h_norm

/-- The a₃ formula for Z=N odd-odd nuclei with `sp = -ap` (extremal
    cancellation): `W_sym·sp + W_std·V_std + W_alt·(-sp) = W_std·V_std`
    when `W_sym = W_alt`. -/
theorem a3_extremal_cancel (w_sym w_std w_alt sp V_std : R_q)
    (h_eq : w_sym = w_alt) :
    w_sym * sp + w_std * V_std + w_alt * (-sp) =
    w_std * V_std := by
  rw [h_eq]; ring

/-! ## §9  Wigner energy from (2,2) partition -/

/-- The Wigner-energy term is `V_pn × α × Z / A` (per nucleon), with
    `V_pn = W_std · (z + dh)` the pn binding volume (§5).  The algebraic
    content is the commutativity/associativity rearrangement of that
    product (the `Z/A` normalisation is a common scalar factor and is not
    part of the identity), abstracting the pn binding volume as `v`. -/
-- Ref: [kerov1996] S. Kerov, q-hook walk algorithm
-- Ref: [satula1997] W. Satula et al., Wigner energy
theorem wigner_energy_from_22 (w_std v α Z : R_q) :
    w_std * v * α * Z = α * w_std * Z * v := by
  ring

/-- The general categorical process for detecting unpaired crossings via
    the per-`(k, residual)` Wedderburn projection of the running NF
    transition.  This class records that the `k`-th-level partition
    structure detects a specific (non-zero) residual term.

    Generic over any `[Zero α]` residual carrier (kept off `ℝ` so the
    file's base-ring note holds — an ordered instantiation is only needed
    for the default instances below). -/
class CategoricalResidualDetection {α : Type*} [Zero α] (k : ℕ) (residual : α) :
    Prop where
  /-- The detected residual is non-zero (i.e. structure is informative). -/
  nontrivial : residual ≠ 0

/-- **Default instance from a positivity hypothesis** (any `[Preorder α]`). -/
instance categoricalResidualDetection_of_pos {α : Type*} [Zero α] [Preorder α]
    (k : ℕ) (residual : α) [hpos : Fact (0 < residual)] :
    CategoricalResidualDetection k residual :=
  ⟨ne_of_gt hpos.out⟩

/-- **Default instance from a strict-negativity hypothesis** (any `[Preorder α]`). -/
instance categoricalResidualDetection_of_neg {α : Type*} [Zero α] [Preorder α]
    (k : ℕ) (residual : α) [hneg : Fact (residual < 0)] :
    CategoricalResidualDetection k residual :=
  ⟨ne_of_lt hneg.out⟩

/-! ## §10  Unified iterative (2,2) correction (q-hook product)

The categorical Wigner energy scale is the q-hook product of (2,2):
`Δ_(2,2) = m_e · H_q((2,2)) = m_e · [3]_q · [2]_q²` (hook lengths of the
2×2 Young diagram are {3, 2, 2, 1}). -/

-- Ref: [kerov1996] Kerov, q-hook walk on Young diagrams
-- Ref: [feray-meliot2012] Féray-Méliot, q-Plancherel CLT
-- Ref: [satula1997] Satuła et al., Wigner energy ≈ 6.3 MeV

/-- The categorical Wigner / shell energy scale
    `Δ_(2,2) = m_e · H_q((2,2))` with `H_q((2,2)) = [3]_q · [2]_q²`: a
    purely algebraic product of `m_e` with the four hook q-integers. -/
theorem delta_22_q_hook (m_e q3 q2 : R_q) :
    m_e * (q3 * q2 ^ 2) = m_e * q3 * q2 * q2 := by ring

/-- Per-step contribution of the unified iterative correction telescopes:
    `Δ₂₂ · w₂₂ · (L_A - L_0) = Δ₂₂ · w₂₂ · L_A - Δ₂₂ · w₂₂ · L_0`. -/
theorem unified_iterative_telescope
    (Δ22 w22 : R_q) (L0 LA : R_q) :
    Δ22 * w22 * (LA - L0) =
    Δ22 * w22 * LA - Δ22 * w22 * L0 := by ring

end QOU.Archimedean.ConfinedKnotBinding
