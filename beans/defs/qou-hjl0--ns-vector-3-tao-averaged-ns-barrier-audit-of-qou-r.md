---
# qou-hjl0
title: 'NS vector 3: Tao averaged-NS barrier audit of QOU regularity claims'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:57:49Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-vo9t
---

Owner (2026-10-12): pursue NS attack vectors 1, 2, 3 and 5 (unforced NS). This bean is v3. Formalize first: a genuine Lean core lemma where one exists, honest conditional statements otherwise, and an audit doc.

## 2026-10-12 — audit landed (ns-v3 subagent)

Audit doc: `docs/audits/2026-10-12-ns-v3-tao-barrier.md` (18 claims, each with file:line). Tao, JAMS 29 (2016) 601–674, arXiv:1402.0290, verified on the web; not held in `library/`.

- **(i) consistent: 9 claims.** The `q > 1` well-posedness theorem sits outside the barrier only because the `[k]_q² ~ q^{2k}` dissipation makes it energy-subcritical. Its proof sketch has internal gaps:
  - `q-ns-proof-strategy.md:11`: `dΩ/dt ≤ −νΩ + CΩ^{3/2}` gives small-data existence only.
  - `:17–24`: the "finite-dim ODE" reduction is false as stated.
  - `q-ns-proof-details.md:3`: the advection is a scalar shell model.
  - The Lean is a class projection (`existence_uniqueness` is assumed).
- **(ii) suspect: 7 claims.** The sharpest is a corpus-internal contradiction. `thm:ns-singularity-descartes` item 3 gives `κ₀|_Σ = 0` for every 1-dim `Σ`, so `NS(A)=0` for **every** QOU. `def:ns-regular-qou` (`:17`) equates that with "classical NS globally regular", and its table (`:22–25`) is falsified by item 3. As written, the corpus derives Clay regularity from topology alone. That inference uses no property of the nonlinearity, so by Tao it cannot be a proof (scope b; assumes ℝ³; transfer to 𝕋³ not checked).
- **Surreal-rate blowup claims.** `ns-surreal-bound` and `millennium-unification` treat a scaling mismatch as a blowup proof. That is unsound: axisymmetric NS without swirl has the same scaling and is globally regular.
- **The `q → 1` limit is Euler, not NS** (`q-ns-properties.md:26`). No block transfers `q > 1` regularity to NS.
- **(iii) unclear: 2 claims** (`conj:regularity-breakdown`, which is honestly scoped; and the Hecke spectral-gap criterion).
- **Heuristic.** Of the categorical structure, Frobenius and `q`-dissipation are averaged-invariant and cannot help. Braiding / vortex-line linking (helicity) is the only plausible "finer structure", and no block derives a PDE estimate from it.

Status stays in-progress: four follow-ups need the owner (audit §4). No Lean core lemma was written in this pass.

## 2026-11-15 — Owner ruling `Q-VO9T-2 = 1` applied to `def:ns-regular-qou` and consumers (PR `litlfred/qou#7982`, commit `f67322a50a`)

Resolved the `def:ns-regular-qou` vs `thm:ns-singularity-descartes` item 3 contradiction by redefining `NS(A)` as the global surface Euler class `e(ξ) ∈ H²(S, ℤ) ≅ ℤ` of degree `χ(A)` (`def:ns-regular-qou`, `def:ns-obstruction`, `QOU/GaugeFieldFluidDynamics.lean`) and explicitly separating the 2D topological classification (`NS(A) = 0` iff `g = 1`, `NS(A_D) = -6 ≠ 0` at `g = 4`) from the open 3D classical Navier–Stokes PDE regularity / blow-up question (citing the Tao averaged-NS barrier in `ns-regular-qou`, `ns-obstruction`, `ns-obstruction-computation-interpretation`, `leray-profile`, `torus-ns-regular`, `torus-ns-regular-table-data`, and `observability-independent-motivation`).

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
Audit and PR #7982 (merged) resolved the def:ns-regular-qou contradiction. Remaining items from audit §4 (q > 1 well-posedness proof gaps; q → 1 limit is Euler, not NS; surreal-rate blowup scoping) are content edits waiting on the owner. Not touched in this pass.
