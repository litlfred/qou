import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# The q-Casimir pair coupling gives pp = nn at generic q, for every braid core

Setting (audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §28). Two nucleon blocks
`A = {0,1,2}`, `B = {3,4,5}` of the Jimbo `Ř` braid. The readout of an operator `X` in the
block-charge sector `(n_A, n_B)` is `T_X(n_A, n_B) = Σ_{s} K_s (core · X)_{ss}`, the sum over basis
states with `n_A`, `n_B` up-strands, where the core is any product of `Ř^{±1}` inside the blocks.
The pair coupling is the `U_q(sl₂)` Casimir with the `Ř`-compatible coproduct
`Δe = e ⊗ K + 1 ⊗ e`, `Δf = f ⊗ 1 + K⁻¹ ⊗ f`, scaled by `h² = (q - q⁻¹)²`:
`X = h²C_{AB} - h²C_A - h²C_B`, with `h²C = h²·fe + qK + q⁻¹K⁻¹`.

**Reduction to block data (hypotheses, not proved here).** The terms of `X` that move charge
between the blocks (`f_A ⊗ e_B`, `K_A⁻¹e_A ⊗ f_B K_B`) have zero sector trace
(`QOU.QBeta.WeightShiftZeroTrace.sectorTrace_eq_zero_of_shift`). What is left is
`h²f_Ae_A ⊗ (K_B - 1) + (K_A⁻¹ - 1) ⊗ h²f_Be_B + q(K_AK_B - K_A - K_B) + q⁻¹(...)⁻¹`,
in which `K` on a block with `n` up-strands is the scalar `k(n) = q^{2n-3}`, so `k(2) = q` and
`k(1) = q⁻¹`. The core commutes with the `U_q` action on each block (Jimbo `Ř` intertwines the
coproduct; checked identically in `q` by `np_gaudin_generic_q_probe.py`), and the block Casimir is a
scalar `λ_j` on each irreducible summand. Since the weights `±½` occur once in every summand of
`V^{⊗3} = V_{3/2} ⊕ 2V_{1/2}`, the block traces in the charge-1 and charge-2 sectors are
* `a(n) = k(n)·τ` with `τ = Σ_j tr(core on the multiplicity space of j)`,
* `h²c(n) = k(n)·(μ − (q k(n) + (q k(n))⁻¹)·τ)` with `μ = Σ_j λ_j·tr(...)`,
where `c(n)` is the trace with `fe` inserted. The two hypotheses `ha`, `hc` below are exactly these
two lines. They are hypotheses of this file. They are proved elsewhere: the reduction from the
two-block trace to `a`, `c` is `PairReadoutTensorReduction.readout_eq_pairReadout`, and the equality
of `τ`, `μ` on the two charge sectors of a three-strand block is
`BlockChargeSectorTrace.sectorTrace_eq` / `feTrace_eq` (audit §32, §33). The link between the
8-dimensional block space and its 3×3 sector matrices is checked by `block_sector_matrices_probe.py`.

**What is proved here, over any field and for every `τ`, `μ`.** pp = nn
(`pairReadout_pp_eq_nn_of_blockData`), and the interaction `pp − pn − np + nn = h²·[2]_q`
(`pairDE_interaction_of_blockData`). Since `τ`, `μ` are arbitrary, the conclusion holds for every
weight-preserving `U_q`-commuting core, not only `V = σ₀σ₁⁻¹`. A Coulomb shape `c + κ Q_A Q_B`
with `Q = n − 1` and pp = nn forces `κ = 0` (`WeylSymmetricPairNotCoulomb.coulomb_kappa_zero_of_pp_eq_nn`).

No empirical input. Tower status: the three-strand block only.
-/

namespace QOU.QBeta.QCasimirPairGenericQ

variable {R : Type*} [Field R]

/-- The surviving (charge-preserving) part of the scaled q-Casimir pair readout in sector
`(n_A, n_B)`, written through the block data `a`, `cH = h²c` and the block K-scalars `kA`, `kB`. -/
def pairReadout (q aA aB cA cB kA kB : R) : R :=
  cA * (kB - 1) * aB + (kA⁻¹ - 1) * aA * cB
    + (q * (kA * kB - kA - kB) + q⁻¹ * ((kA * kB)⁻¹ - kA⁻¹ - kB⁻¹)) * aA * aB

/-- Block trace of the core in a charge sector with K-scalar `k` (hypothesis `ha`). -/
def blockA (τ k : R) : R := k * τ

/-- `h²·` block trace with `fe` inserted (hypothesis `hc`). -/
def blockC (q τ μ k : R) : R := k * (μ - (q * k + (q * k)⁻¹) * τ)

/-- Readout in sector `(n_A, n_B)` from the K-scalars, under the block-data hypotheses. -/
def sectorReadout (q τ μ kA kB : R) : R :=
  pairReadout q (blockA τ kA) (blockA τ kB) (blockC q τ μ kA) (blockC q τ μ kB) kA kB

/-- Identity readout in sector `(n_A, n_B)`. -/
def sectorNorm (τ kA kB : R) : R := blockA τ kA * blockA τ kB

/-- pp = nn for the q-Casimir pair coupling, at generic `q`, for every core: the energy shifts
`T_X/T_1` agree, stated cross-multiplied so no nonvanishing of `τ` is needed. -/
theorem pairReadout_pp_eq_nn_of_blockData (q τ μ : R) (hq : q ≠ 0) :
    sectorReadout q τ μ q q * sectorNorm τ q⁻¹ q⁻¹
      = sectorReadout q τ μ q⁻¹ q⁻¹ * sectorNorm τ q q := by
  unfold sectorReadout pairReadout sectorNorm blockA blockC
  field_simp
  ring

/-- The energy shift `T_X/T_1` in sector `(kA, kB)`. -/
def pairDE (q τ μ kA kB : R) : R := sectorReadout q τ μ kA kB / sectorNorm τ kA kB

/-- The pair interaction is `h²·[2]_q`, independent of the core: pp − pn − np + nn. -/
theorem pairDE_interaction_of_blockData (q τ μ : R) (hq : q ≠ 0) (hτ : τ ≠ 0) :
    pairDE q τ μ q q - pairDE q τ μ q q⁻¹ - pairDE q τ μ q⁻¹ q + pairDE q τ μ q⁻¹ q⁻¹
      = (q - q⁻¹) ^ 2 * (q + q⁻¹) := by
  unfold pairDE sectorReadout pairReadout sectorNorm blockA blockC
  field_simp
  ring

/-- pp = nn as energy shifts. -/
theorem pairDE_pp_eq_nn_of_blockData (q τ μ : R) (hq : q ≠ 0) (hτ : τ ≠ 0) :
    pairDE q τ μ q q = pairDE q τ μ q⁻¹ q⁻¹ := by
  unfold pairDE sectorReadout pairReadout sectorNorm blockA blockC
  field_simp
  ring

end QOU.QBeta.QCasimirPairGenericQ
