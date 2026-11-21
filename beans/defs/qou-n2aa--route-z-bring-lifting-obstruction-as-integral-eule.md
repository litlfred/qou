---
# qou-n2aa
title: 'Route Z: Bring lifting obstruction as integral Euler class; derive kappa_0 = e'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:30:20Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-vo9t
---

Route 2 of qou-lx8f (owner, 2026-10-12: pursue in parallel; band deferred).

**Reading.** The obstruction is integral, kappa_0 = e(xi) = -6 in H^2(Sigma_4, Z) = Z. That is nonzero, so persistence is at least consistent.

**Problem.** An integral Euler class obstructs a nowhere-zero section (trivialising an SO(2)-bundle). It is NOT the obstruction to lifting through a central extension by a finite or discrete-abelian kernel. The natural central extension with Z kernel is Z -> R -> U(1) (or the universal cover). Making this a Yekutieli lifting problem needs that extension identified explicitly, and kappa_0 = e derived. Today kappa_0 = e is asserted (thm:qu-to-qou item 2, "via the Gysin sequence") and is a structure field in every Lean file (trace_map, kappa_zero_euler, hattori_stallings).

**Next honest step.** Identify the Z-kernel central extension the tower uses, then derive kappa_0 = e from it. Lean needs Euler classes, which Mathlib lacks; the group-level shadow is T1 with A = Z.

## Progress (2026-11-16, PR `litlfred/qou#8150` — `status: in-progress`)
- **Lean 4 formalization (`0` `sorry`, `0` custom axioms):** Added `folio/quantum-observable-universe/lean/QOU/Brings/BringLiftingObstructionRoutes.lean` (wired into `QOU.lean`, verified with Lean v4.24.0 `-DautoImplicit=false`), proving:
  - `integral_euler_zero_iff_torus`: `χ(Σ_g) = 2 - 2g = 0 ↔ g = 1` (the torus `𝕋²`).
  - `bring_integral_euler_nonzero` and `bring_z_persists_while_z2_vanishes`: at `g = 4`, the integral Euler / Chern class under `0 → ℤ → ℝ → U(1) → 1` is `κ₀(Σ₄) = -6 ≠ 0` (`|κ₀(Σ₄)| = 6`, matching `H₁(UT(Σ₄))_tors ≅ ℤ/6ℤ` and chiral Seifert linking residue `∓1/6 ∈ ℚ/ℤ`), while its mod-2 Stiefel–Whitney reduction `ρ₂(-6) = 0` vanishes identically.
  - `bring_admissible_kummer_levels` and `bring_kummer_fibre_torsion_orders`: under the Kummer sequence `1 → ℤ/nℤ → U(1) → U(1) → 1`, the admissible `n`-th root levels in `{1..6}` are `{1, 2, 3, 6}` (with `n = 4, 5` obstructed) and the fibre torsion orders are `|-6/n| ∈ {6, 3, 2, 1}`.
- **50-dps / Exact Probe + Witness:** `computations/probes/bring_lifting_obstruction_routes_z2_vs_z_probe.py` and `.witness.json` (12/12 assertions passed).

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
Same PR #8150 as qou-2a2o, same verification and the same caveat: bring_integral_euler_nonzero is surfaceEulerChar 4 = −6 by rfl; kappa_0 = e is still not derived from a Z-kernel central extension. The cochain-level derivation that exists is CechChernClass (expExtension Z → R → U(1), chernClass, kummer_obstruction obs_n = c_1 mod n), merged earlier; what is missing is (i) local real lifts (IsRealLift is a hypothesis) and (ii) deg c_1(TΣ₄) = χ. Bean stays open.
