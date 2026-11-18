---
# qou-qmoh
title: 'Lean-prove NucleonWeightSpaceTwoTerm: Gell-Mann-Nishijima hypercharge intertwiner breaking & two-term QCD+QED trace on (2,1) vs (1,2)'
status: completed
type: task
priority: high
tags:
    - lean
    - convention-d
created_at: 2026-11-18T19:52:23Z
updated_at: 2026-11-18T20:19:50Z
parent: qou-7xl8
---

In `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean` (importing `QOU.BraidsAndKnots.NucleonWeightSpaceTraces` and `QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder` over generic `[Field R]`):
1. Define the 3×3 restriction matrices on `(2,1)` (proton `uud`) and `(1,2)` (neutron `udd`) of:
   - Cartan quantum-trace weight `Kp q = q • 1`, `Kn q = q⁻¹ • 1`,
   - Diagonal self-energy charge-squared sum `QSelfP = 1`, `QSelfN = (2/3) • 1`,
   - Total pairwise Coulomb-Compton operator `QPairP = 0`, `QPairN = (-1/3) • 1`,
   - Local crossing-coupled two-photon operators `Q12p, Q23p` and `Q12n, Q23n`.
2. Prove over `[Field R]` (`0 sorry`, `0 axiom`, verified via `scripts/lean-verify.sh`):
   - `P(q)` does NOT intertwine `Q12p` and `Q12n` (`P q * Q12p ≠ Q12n * P q`),
   - Exact decomposition of `Q12, Q23` into an ω-swapped part (intertwined by `P q`) and a hypercharge-asymmetric defect,
   - Exact two-term quantum-trace difference `tr(O_n * word B1 B2 w) - tr(O_p * word A1 A2 w)` for every braid word `w : List Bool` and specifically on the Borromean nucleon `V³ = (σ₁σ₂⁻¹)³`.
3. Link claim-level citations (`library/<doc-id>/blocks/<block-id>`) for `borsanyi-et-al-2015`, `gasser-leutwyler-rusetsky-2020-epjc`, `walker-loud-carlson-miller-2012`, and `can-qcdsf-2025`.



## Completion & Adversarial Verification Record (2026-11-18)
- **Lean Module:** `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean`
- **Verification:**
  - `bash scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean`: `✓ exit 0 — checks` (`0` sorries, `0` warnings)
  - `python3 scripts/lean-borrowed-name-audit.py --strict`: `0 CRITICAL, 0 major, 0 advisory`
  - `python3 scripts/lean-definition-collapsed-audit.py --strict`: `0 CRITICAL, 0 advisory`
  - Adversarial review (`qou-gt6w`, `lane-7b4f`): **PASS** (`#print axioms`: strictly `[propext, Classical.choice, Quot.sound]`).
