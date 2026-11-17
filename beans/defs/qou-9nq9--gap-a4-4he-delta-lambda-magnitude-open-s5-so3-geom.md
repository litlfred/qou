---
# qou-9nq9
title: 'GAP: A=4 (4He) Delta_lambda magnitude OPEN — s5-so3 geometric W_lambda brackets but does not close'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:11:09Z
updated_at: 2026-11-17T07:28:00Z
parent: qou-v2om
---

## What is open

The A=4 (⁴He) Δ_λ binding magnitude. SIGN is settled (#4378: τ_L₄>1 ⇒ c₄<0 compatible
with μ₄=−4.591<0). MAGNITUDE is open: no 0-fit construction supplies it.

## What was tried (this branch, PR TBD)

Option-E PROBE 2 = A=4 interface operator + `conj:s5-so3-fiber-action`. The s5-so3 fiber
action supplies a NORMALIZED color-tube weight (Σ W_λ=1); geometric measure W_geom=d_q²/D²
(Beasley–Witten, same as #4392 at A=3). Forward 0-fit on the canonical b0vf ⁴He H₁₂
per-block table (chi-helium-4-h12-at-q0-50dps, 77 λ⊢12), E₀=4.18598 MeV:

- production E₀·Σ y_λ|χ_λ| = 0.243 MeV  → undershoots B(⁴He)=28.30 by 117×
- geometric E₀·Σ W_geom|χ_λ| = 60.33 MeV → overshoots by 2.13× (r_geom=248.5)
- bound E₀·max|χ_λ| = 266 MeV (max|χ|=63.6 at λ=(6,3,3))

The two 0-fit endpoints BRACKET both targets (B(⁴He)=28.30, |μ₄|=4.591) but neither lands.
Bound is above target ⇒ NOT a scope-(b) exclusion — reachable in span, exact hit = FIT.

## Verdict: WALL(scope-(a)). Nothing wired; free_parameters=0.

## Next honest step

The missing object is a DERIVED weight between production y_λ and geometric d_q²/D², or a
derived per-block coefficient — NOT a tuned intermediate (that would be a fit). Candidates:
(i) an interface-operator block-diagonal compression A^λ_{ξν}(I) that fixes the per-block
weight from the bridge generator I=c·σ_{n-4}+d·𝟙 (InterfaceOperatorBlockDiagonal.lean is
proved but the c,d and the resulting weight are not pinned for ⁴He);
(ii) the bare cabled-H₁₂ Brunnian deficit route (#4378: c₄=−0.0582, 79× short of μ₄) —
a DIFFERENT object (deficit-vs-unlink, not full-trace reweight), also short.
Both are 0-fit endpoints on opposite sides; the derivation that pins the physical weight is open.

## Artifacts
- audit docs/audits/2026-08-01-deltalambda-a4-helium-interface-operator.md
- probe computations/deltalambda/s5so3_geometric_wlambda_a4_helium_probe.py
- lean QOU/MassTheory/GeometricWLambdaA4Helium.lean (sorry-free, lean-direct exit 0)
- option-e.md ledger row 2026-08-01

## Round 62 Update (PR #8255)
- Formalized in PR https://github.com/litlfred/qou/pull/8255 (head `b4ec4b15ca43f486c66d8f53b0eeb216293fc6aa`, Commit 1 `c715790dad2efe16f1713c8a17825e912524e641`, `scriptHash: e2eb499467fc`).
