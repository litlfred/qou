---
# qou-l1je
title: 'B2 tau-lift resolution: build explicit H1(Bring) Hodge model, reduce lift to minimal tau-dictionary core (alpha_EM per-loop)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T19:03:03Z
updated_at: 2026-11-16T19:01:00Z
parent: qou-3l2l
---


## RESULT (2026-08-02): wall reduced to ONE existence axiom (MOC); not closable this session
Audit: 2026-08-02-hodge-lift-bring-h1-model.md. Compute: computations/alpha_em/
hodge_lift_bring_model.py (10/10 PASS, re-verified).
- Bring Jac ~ E^4, E NON-CM (proved: j=-121945/32, -25/2 non-integral; tau0 not
  imag-quadratic). Jac = E_{5tau0}^3 x E_{tau0}, X0(5). CM-close route foreclosed.
- rho <-> Hodge conjugation (c=SWAP.conj, Weil real structure) is CANONICAL/automatic
  (same for any moduli) -- the holo/anti-holo "obstruction" is definitively a non-issue.
- nome equivariance tau(qbar)=-conj(tau(q)) forced. Both would-be-open ingredients AUTOMATIC.
- MINIMAL OPEN CORE (MOC): existence of the functorial holomorphic period map
  Phi: q |-> H^1(E_{tau(q)}) subset H^1(Bring), nome-normalized. Option (a), NARROWER than
  (b): loop is a rank-2 sub-object. 2-field wall collapses to 1 field (PeriodMapWeight).
- NOT closable from the model: MOC = the foundational q<->period dictionary (keystone E(q)
  Gauss-Manin). Shadow fixes a point, no germ of Phi. CM never helps (pins target, not map).
- Proposed Lean: single-field PeriodMapWeight class (described in the audit;
  reduction; unbuilt proposal, Mathlib-gated; no instance fabricated). conditional-proved
  != premise-established. Nothing wired.
Follow-up options: (1) land the PeriodMapWeight interface reduction as real Lean infra;
(2) attack MOC via the genus-1 E(q) Gauss-Manin family (foundational, multi-week).

## Progress (2026-11-16, PR `litlfred/qou#8156` — `status: in-progress`)
- **Lean 4 formalization (`0` `sorry`, `0` custom axioms):** Added Part II of `folio/quantum-observable-universe/lean/QOU/AlphaEM/PropagatorHodgeH3GreenAssembly.lean` (complementing `QOU.Archimedean.HodgeWeilRealStructure` and `QOU.Archimedean.PeriodMapWeightReduction`, wired into `QOU.lean`, verified with Lean v4.24.0 `-DautoImplicit=false`), proving:
  - `bradenNorthoverC_spectral_decomposition`: formalizes the `4 × 4` Braden–Northover / Riera–Rodríguez period matrix `C = 5 I₄ - J₄` on `V_std` (`Ω = τ₀ C`), proving `Cᵀ = C`, `tr(C) = 16`, `(C - 5 I₄)(C - I₄) = 0`, explicit eigenbasis `e₁ - e₄, e₂ - e₄, e₃ - e₄` with eigenvalue `5` (the `E_{5τ₀}³` isogeny block) and `(1, 1, 1, 1)` with eigenvalue `1` (the `S₄`-invariant `E_{τ₀}` quotient block), and `det(C) = 5³ · 1 = 125`.
  - `bring_elliptic_factors_non_cm`: proves `(-121945) % 32 ≠ 0` and `(-25) % 2 ≠ 0`, confirming neither `j(τ₀) = -121945/32` nor `j(5τ₀) = -25/2` is an integer, foreclosing CM period closure and reducing the B2 lift to the single-field `PeriodMapWeight` MOC.
- **50-dps / Exact Probe + Witness:** `computations/probes/h3_green_coth_saturation_probe.py` and `.witness.json` (11/11 assertions passed).
