---
# qou-9gj9
title: 'Convention-slip sweep: reach the alpha_EM = [2]_q(1-h^2 alpha) / EM self-energy sign surface and the gravity+information channels (not reached in 2026-08-08 sweep)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T13:05:02Z
updated_at: 2026-11-16T19:01:00Z
parent: qou-3l2l
---

## Progress (2026-11-16, PR `litlfred/qou#8156` — `status: in-progress`)
- **Lean 4 formalization (`0` `sorry`, `0` custom axioms):** Added Part IV of `folio/quantum-observable-universe/lean/QOU/AlphaEM/PropagatorHodgeH3GreenAssembly.lean` (complementing `QOU.Archimedean.EmCouplingBringZeroMode` and `QOU.MassTheory.NeutronProtonEMSign`, wired into `QOU.lean`, verified with Lean v4.24.0 `-DautoImplicit=false`), proving:
  - `balanced_two_q_sq_sub_h_sq`: `(q² + 1)² - (q² - 1)² = 4 q²` (`[2]_q² - h² = 4`), confirming that `[2]_q = q + q⁻¹` and `h = q - q⁻¹` in `H = [2]_q/(8π)` and `(1 - h²α)` both live in the balanced Hecke presentation (`σ² = h σ + 1`) with no balanced/unbalanced convention slip.
  - `hecke_h_eq_q_plus_one_mul_hbar_q`: `q² - 1 = (q + 1)(q - 1)`, proving the exact ratio `h / ℏ_q = q + 1` (`= 2` at `q = 1`, `≈ 2.105` at `q₀`) separating the Hecke constant `h = q - q⁻¹` from the mass-chain parameter `ℏ_q = 1 - q⁻¹`.
  - `np_em_sign_convention_immune`: proves that the cleared pairwise quark Coulomb factor `9 ∑_{i<j} qᵢ qⱼ` is `0` on proton `uud` (`2, 2, -1`) and `-3` on neutron `udd` (`2, -1, -1`), with gap `+3 > 0`, which depends only on the signed writhe `Q = ½(n₊ - n₋)` (the sound half of `coulomb-charge.md`) and is completely immune to the negative-crossing energy sign slip.
- **50-dps / Exact Probe + Witness:** `computations/probes/h3_green_coth_saturation_probe.py` and `.witness.json` (11/11 assertions passed).
