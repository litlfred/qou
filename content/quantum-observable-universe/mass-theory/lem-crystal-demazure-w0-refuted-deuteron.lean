import Mathlib.Data.Rat.Defs
import Mathlib.Tactic

/-!
# Crystal / Demazure-w₀ principal-specialisation Δ_λ ansatz — refuted at the deuteron

Formalised refutation (per `compute-author.md §3.4`, *formalize-the-refutation*)
of the **principal-specialisation crystal-graph weight**
`c_λ(q) := s_λ(1, q, …, qⁿ⁻¹)` used as the per-block binding density `Δ_λ` in
the Path-D `ρ_K` density formula.  At the principal specialisation this weight
equals the Demazure character `D_{w₀}(λ)` (Macdonald hook-content; verified by
`demazure-markov-trace.witness.json`), so this single lemma simultaneously
refutes the **Option C (Demazure-fibre)** and the **Option E
principal-specialisation (crystal-graph weight)** closure attempts of the Δ_λ
gate.

**Scope (STRICT).** This refutes ONLY the principal-specialisation weight.  It
does NOT bear on the bar-symmetric / isospin Option-E *v9* Kashiwara-crystal
variants (`option-e-v9-bar-symmetric-test-probe`, `option-e-isospin-probe`),
which remain open, nor on the *successful* free-subtracted Frobenius co-Casimir
+ Wigner deuteron closure (`prop:deuteron-binding-frobenius-codim`, +0.19 %),
which uses a different functional.

Numbers pinned (50 dps) from
`computations/rho-k-h3a-crystal.witness.json`: the
crystal / Demazure Δ_λ sum at the deuteron is `≈ +1796.735` (m_e units) versus
the empirical target `−B_D/m_e ≈ −4.353` — wrong sign and off by a factor
`≈ 412` (gap `≈ 1801.089`, = the witness `residual_target_minus_sum`).

## References
- [manuscript] rho-k-h3a-crystal.witness.json (Option E principal specialisation)
- [manuscript] demazure-markov-trace.witness.json (c_λ = D_{w₀} identity)
- [manuscript] docs/audits/2026-05-18-delta-lambda-gating-context.md (Options C, E)
-/

namespace QOU.WedderburnMass

/-- Crystal / Demazure-w₀ predicted `Σ_λ y_λ χ^λ Δ_λ` at the deuteron (m_e
    units), 13 sig figs from `rho-k-h3a-crystal.witness.json` (= target −
    `residual_target_minus_sum`). -/
def crystalDeuteronSum : ℚ := 1796735360023 / 1000000000        -- ≈ +1796.735360023

/-- Empirical `−B_D/m_e` (m_e units), from the same witness
    (`target_sum_y_chi_Delta`). -/
def deuteronTargetSigned : ℚ := -4353367281870 / 1000000000000  -- ≈ −4.353367281870

/-- Viability tolerance (m_e units): a candidate Δ_λ closure must land within
    `1` m_e unit of the target.  The crystal / Demazure weight misses by
    `≈ 1801`. -/
def deuteronTol : ℚ := 1

/-- **Refutation.**  The principal-specialisation crystal-graph / Demazure-w₀
    weight, used as the per-block binding density `Δ_λ`, overshoots the deuteron
    target by more than the viability tolerance (gap `≈ 1801` m_e units; wrong
    sign, `≈ 412×` the target magnitude).  Hence it is not the categorical
    `Δ_λ`.  Proof is a decidable rational comparison.
    -- Ref: [manuscript] rho-k-h3a-crystal.witness.json -/
theorem crystal_demazure_refuted_deuteron :
    deuteronTol < crystalDeuteronSum - deuteronTargetSigned := by
  unfold deuteronTol crystalDeuteronSum deuteronTargetSigned
  norm_num

end QOU.WedderburnMass
