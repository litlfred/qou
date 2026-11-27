import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import BraidKnotOctonion.BorromeanMarkovTrace

/-!
# The neutron's own identity: the convention-D proton identity is isospin-blind

Coordinator brief 2026-11-21, item (2) "m_n by its own identity". Pre-registration:
`computations/probes/mn_own_identity/PREREGISTRATION.md`.

The production proton identity (convention D) is

  `m_p / m_e = 2 (Vol(4₁)/ℏ_q²) F_Bor(q) − 12`,  `F_Bor = tr_M(β_Bor) · [3]_q! / q³`,

with `tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶)/(h² + 4)`, `h = q − q⁻¹` (`BorromeanMarkovTrace`).
`β_Bor = V³ = (σ₁σ₂⁻¹)³` is the two-photon product of the ruled photon
`γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` (`borromeanV3A_eq_switched_photon_product`).

## What is proved

1. `wholeTrace_eq_trM`: `tr_M(β_Bor)` is the whole-space convention-D quantum trace
   `Tr(K^{⊗3} V³)/[2]³` on `(C²)^{⊗3}`, i.e. the sum over the FOUR `T³` sectors
   `uuu` (`K = q³`), `uud = W_p` (`K = q`), `udd = W_n` (`K = q⁻¹`), `ddd` (`K = q⁻³`):
   `tr_M(β_Bor) = (q³·1 + q·tr_{W_p}(V³) + q⁻¹·tr_{W_n}(V³) + q⁻³·1)/[2]³`.
   The proton identity therefore reads a trace over the whole isospin multiplet, not the
   proton's own weight space.
2. `wholeTrace_reflect`: the weight reflection `K ↦ K⁻¹` (equivalently `u ↔ d`, which carries
   `W_p` to `W_n`) leaves this trace unchanged.
3. `neutron_identity_forces_equal_mass`: the literal neutron analogue `N0` — same element `V³`
   (forced for n and p on three strands, #8636 `isoChar_eq`), the whole-space trace with the
   neutron's flavour roles (`u ↔ d`) — has `F^(n) = F_Bor`, so the proton identity and the
   `N0` neutron identity together force `m_n = m_p`. No numerical value enters.
4. `sector_ratio`: the sector-resolved reading `N1` (leading term ∝ the nucleon's own `T³`
   component, `ε_N = K_N · tr_{W_N}(V³)/[2]³`) gives `F^(n)/F^(p) = q⁻²` exactly — the
   pivot `T_p = q² T_n` of #8734.

## Two-term trace

The covariant all-pairs two-term connected part vanishes on every quark-only word
(`QOU.QBeta.BetaRoutesTwoTerm.pairSum_eq_of_total_eq`: the pair charge is a scalar on each
weight space, so its connected part is zero). Hence on `V³` the two-term trace equals the
one-term trace for the proton and for the neutron alike, and items 1–4 hold verbatim for the
two-term trace. That step is cited, not re-proved here.

## What is NOT claimed

* That `N0` or `N1` is the neutron's mass identity. Both are stated as conjectures
  (`NeutronIdentityN0`, `NeutronIdentityN1`); this file proves what each one implies.
* Anything about `Vol(4₁)`, `ℏ_q` or the muon pin: `mμ` is a free symbol.
* Every statement is over a generic `[Field R]` (§7c); nothing needs an order.
-/

namespace QOU.MassTheory.NeutronOwnIdentity

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-- `[2]_q = q + q⁻¹`. -/
def qd2 (q : R) : R := q + q⁻¹

/-- `[3]_q! = [2]_q [3]_q = (q + q⁻¹)(q² + 1 + q⁻²)`. -/
def qfact3 (q : R) : R := (q + q⁻¹) * (q ^ 2 + 1 + q⁻¹ ^ 2)

/-- `V = σ₁σ₂⁻¹` on a one-dimensional extremal sector (`uuu` or `ddd`): each crossing of two
equal labels acts by `q` (Jimbo `Ř`), so `V` acts by `q · q⁻¹`. -/
def extremalV (q : R) : R := q * q⁻¹

theorem extremalV3_eq_one (q : R) (hq : q ≠ 0) : extremalV q ^ 3 = 1 := by
  simp [extremalV, hq]

/-- The `K`-weighted sector trace of `V³` on `(C²)^{⊗3}`, with sector weights
`(k₃, k₁, k₋₁, k₋₃)` on `uuu, uud, udd, ddd`, normalised by `[2]³`. -/
def sectorTrace (q k₃ k₁ km₁ km₃ : R) : R :=
  (k₃ * extremalV q ^ 3 + k₁ * trace (borromeanV3A q) + km₁ * trace (borromeanV3B q)
    + km₃ * extremalV q ^ 3) / qd2 q ^ 3

/-- The convention-D whole-space trace: `K^{⊗3}` acts by `q^{2T³}`. -/
def wholeTrace (q : R) : R := sectorTrace q (q ^ 3) q q⁻¹ (q⁻¹ ^ 3)

/-- **Item 1.** The whole-space convention-D trace of `V³` is the Borromean Markov trace
closed form `(4 + h² − 3h⁴ − h⁶)/(h² + 4)`. -/
theorem wholeTrace_eq_trM (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    wholeTrace q =
      QOU.BraidsAndKnots.trM_borromean_num (q - q⁻¹) /
        QOU.BraidsAndKnots.trM_borromean_den (q - q⁻¹) := by
  unfold wholeTrace sectorTrace qd2
  rw [extremalV3_eq_one q hq, trace_borromeanV3A q hq, trace_borromeanV3B q hq]
  unfold QOU.BraidsAndKnots.trM_borromean_num
    QOU.BraidsAndKnots.trM_borromean_den
  have hden : (q - q⁻¹) ^ 2 + 4 = (q ^ 2 + 1) ^ 2 / q ^ 2 := by field_simp; ring
  have e2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [hden, e2]
  field_simp
  ring

/-- **Item 2.** Weight reflection `K ↦ K⁻¹` (`u ↔ d`) leaves the whole-space trace of `V³`
unchanged. -/
theorem wholeTrace_reflect (q : R) (hq : q ≠ 0) :
    sectorTrace q (q⁻¹ ^ 3) q⁻¹ q (q ^ 3) = wholeTrace q := by
  unfold wholeTrace sectorTrace
  rw [trace_borromeanV3A q hq, trace_borromeanV3B q hq]
  ring

/-- `F_Bor = tr_M(β_Bor)·[3]_q!/q³` (the production observable; the production code takes the
absolute value, which is immaterial to every statement below). -/
def FBor (q : R) : R := wholeTrace q * qfact3 q / q ^ 3

/-- The neutron's `F` under reading `N0`: the same element and the whole-space trace with the
neutron's flavour roles (`u ↔ d`, i.e. `K ↦ K⁻¹`). -/
def FNeutronN0 (q : R) : R := sectorTrace q (q⁻¹ ^ 3) q⁻¹ q (q ^ 3) * qfact3 q / q ^ 3

theorem FNeutronN0_eq_FBor (q : R) (hq : q ≠ 0) : FNeutronN0 q = FBor q := by
  unfold FNeutronN0 FBor
  rw [wholeTrace_reflect q hq]

/-- The proton identity with the muon scale `mμ` as a free symbol. -/
def ProtonIdentity (q mμ me mp : R) : Prop := mp = 2 * mμ * FBor q - 12 * me

/-- **Conjecture N0** (the literal neutron analogue). -/
def NeutronIdentityN0 (q mμ me mn : R) : Prop := mn = 2 * mμ * FNeutronN0 q - 12 * me

/-- **Item 3.** The proton identity and the `N0` neutron identity together force `m_n = m_p`.
So `N0` cannot carry the n–p mass difference. -/
theorem neutron_identity_forces_equal_mass (q mμ me mp mn : R) (hq : q ≠ 0)
    (hp : ProtonIdentity q mμ me mp) (hn : NeutronIdentityN0 q mμ me mn) : mn = mp := by
  unfold ProtonIdentity at hp
  unfold NeutronIdentityN0 at hn
  rw [hn, hp, FNeutronN0_eq_FBor q hq]

/-- Sector component of nucleon `N` with `K`-eigenvalue `k` on its own weight space. -/
def sectorF (q k : R) (M : Matrix (Fin 3) (Fin 3) R) : R := k * trace M / qd2 q ^ 3

/-- **Item 4.** Sector-resolved reading `N1`: the neutron and proton components of `V³` are in
ratio `q⁻²` exactly. -/
theorem sector_ratio (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    sectorF q q⁻¹ (borromeanV3B q) = q⁻¹ ^ 2 * sectorF q q (borromeanV3A q) := by
  unfold sectorF qd2
  rw [trace_borromeanV3A q hq, trace_borromeanV3B q hq]
  have e2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [e2]
  field_simp

/-- **Conjecture N1** (sector-resolved): the leading term scales with the nucleon's own `T³`
component, so the neutron's `F` is `q⁻² F_Bor`. -/
def NeutronIdentityN1 (q mμ me mn : R) : Prop := mn = 2 * mμ * (q⁻¹ ^ 2 * FBor q) - 12 * me

/-- Under `N1` the n–p difference is `2 mμ F_Bor (q⁻² − 1)`: the neutron is LIGHTER for
`q² > 1` whenever `mμ F_Bor > 0` (an ordered-field remark; the identity itself is generic). -/
theorem n1_difference (q mμ me mp mn : R)
    (hp : ProtonIdentity q mμ me mp) (hn : NeutronIdentityN1 q mμ me mn) :
    mn - mp = 2 * mμ * FBor q * (q⁻¹ ^ 2 - 1) := by
  unfold ProtonIdentity at hp
  unfold NeutronIdentityN1 at hn
  rw [hn, hp]
  ring

end QOU.MassTheory.NeutronOwnIdentity
