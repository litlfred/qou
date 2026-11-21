---
# qou-nzyr
title: Redefine NS(A) on a non-degenerate invariant (owner option 2)
status: in-progress
type: task
priority: normal
created_at: 2026-10-13T00:10:17Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-vo9t
---

Owner option 2 (2026-10-13): redefine NS(A) on an invariant that is not automatically zero.

The current NS(A) = κ₀|_Σ lies in H²(Σ) = 0. Candidates: an invariant of the vorticity line field ξ = ω/|ω| (ns-v1 audit: the Levi scalar ξ·curl ξ; Constantin–Fefferman bounds it only from above); the Beirão da Veiga–Berselli ½-Hölder seminorm of ξ on the high-vorticity set.

Constraint: it must be defined on objects the model actually has (ξ is currently undefined in the corpus), and it must not be chosen to produce a verdict.

## 2026-11-15 — Owner ruling `Q-VO9T-2 = 1` implemented (PR `litlfred/qou#7982`, commit `f67322a50a`)

Redefined `NS(A)` in `def:ns-regular-qou` (`fluid-dynamics/ns-regular-qou.{md,ts,lean}`), `def:ns-obstruction` (`fluid-dynamics/ns-obstruction.{md,ts,lean}`), and `QOU/GaugeFieldFluidDynamics.lean` as the **global** surface Euler class `e(ξ) ∈ H²(S, ℤ) ≅ ℤ` of degree `χ(A)` (matching `qou_ns_in_qou.lean` and `thm:ns-singularity-descartes` item 1), removing the degenerate 1D curve restriction `κ₀|_Σ ∈ H²(Σ, ℤ) = 0` while explicitly scoping the 3D classical Navier–Stokes regularity bridge as open per `qou-hjl0` (Tao averaged-NS barrier). Updated consumers `ns-obstruction-computation-interpretation.{md,ts}`, `leray-profile.{md,ts}`, `torus-ns-regular.{md,ts}`, `torus-ns-regular-table-data.{md,ts}`, and `observability-independent-motivation.{md,ts}`. Both Lean files verified sorry-free (`lean -DautoImplicit=false -s 65536`, exit 0).

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
The redefinition landed with PR #7982 (merged 2026-11-15). Nothing further pending in this bean except confirmation; candidate for completion (owner's call).
