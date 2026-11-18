---
# qou-7xl8
title: "EPIC: Two-Term Categorical Mass & Splitting Decomposition (Δm_QCD + Δm_QED from ℒ_q = \U0001D49F_∇² + ψ*⊗\U0001D49F_∇ψ) — Formalize-First Lean Proofs, Cottingham Self-Energy, and 211 ppb μ–p Tension"
status: completed
type: epic
priority: critical
tags:
    - convention-d
    - 1ppq
    - cottingham
created_at: 2026-11-18T19:52:23Z
updated_at: 2026-11-18T22:13:31Z
---

Master epic for deriving, formalizing in Lean 4 (over real QOU/Mathlib types, 0 sorry, 0 axiom, adversarially checked), and auditing the downstream compute/1ppQ consequences of the two-term categorical mass and isospin-splitting decomposition:

  τ(ℒ_q(∇, ψ)) = τ(𝒟_∇²) + τ(ψ* ⊗ 𝒟_∇ψ)  ⟹  Δm_np = Δm_QCD + Δm_QED

1. **Mathematical foundation**:
   - In `QOU.BraidsAndKnots.NucleonWeightSpaceTraces` and `NucleonWeightSpaceSecondOrder`, the intertwiner `P(q)` makes every pure braid word and every ω-symmetric U_q(sl₂) insertion (`FE + EF`) identical on the proton `(2,1)` and neutron `(1,2)` weight spaces, so Term 1 (`𝒟_∇²` / Cartan weight `K^{⊗3} = q^{±1}`) sees only the strong isovector shift (`t_n / t_p = q⁻²`).
   - By the Gell-Mann–Nishijima formula `Q = (1/6)I + T³`, the electromagnetic charge operator mixes an ω-even hypercharge scalar (`1/6`) with an ω-odd isovector (`T³`). Its quadratic two-photon Cottingham / Coulomb-Compton operators (`Σ Q_i²`, `Σ_{i<j} Q_i Q_j`, and crossing-coupled `Q_{12}, Q_{23}`) break the `P(q)` intertwiner (`P(q) Q_{12}^{(p)} ≠ Q_{12}^{(n)} P(q)`), yielding the negative electromagnetic self-energy shift `Δm_QED < 0` that opposes `Δm_QCD > 0`.
2. **Claim-level citations & mandatory Lean proofs**:
   - All citations to the newly ingested Cottingham / Compton subtraction function / lattice QCD+QED papers (`borsanyi-et-al-2015`, `gasser-leutwyler-rusetsky-2020-epjc`, `gasser-leutwyler-rusetsky-2021`, `walker-loud-carlson-miller-2012`, `can-qcdsf-2025`, `horsley-et-al-2016-qcd-qed`) and Hecke idempotent / modified quantum dimension / Stokes papers (`aiston-morton-1997`, `hadji-morton-2009`, `geer-patureau-mirand-turaev-2009`, `geer-patureau-mirand-turaev-2013`, `yekutieli2015`, `broda2002`, `pimsner-popa-1986`, `jones2015vonneumann`) must link to exact `library/<doc-id>/blocks/<block-id>` claim nodes.
   - Every cited mathematical claim must be proved in Lean 4 over real `QOU.*` and `Mathlib.*` imports (`scripts/lean-verify.sh`), followed by an adversarial review pass (`lean-proof-vacuity-audit`, `lean-borrowed-name-audit.py`, `lean-definition-collapsed-audit.py`).
