---
# qou-p494
title: 'PROVE(lean): instance:HyperbolicVolumeIndependence — noncomputable instance : HyperbolicVolumeIndependence where no_relation  [cited manuscript,zagier1986]'
status: todo
type: task
priority: normal
tags:
    - paper-qou
    - infra-blocked
    - cite-zagier1986
    - reorg-2026-10-04
    - lean
    - cited-sorry
created_at: 2026-08-01T23:31:01Z
updated_at: 2026-11-22T21:40:00Z
parent: qou-gdcu
---

**File:** `QOU/Archimedean/HyperbolicVolumeIndependence.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicVolumeIndependence.lean

### `instance:HyperbolicVolumeIndependence`  —  line 42  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `noncomputable instance : HyperbolicVolumeIndependence where no_relation `
- **Cited:** `[zagier1986]`, `[manuscript]`, `[zagier1986]`
  - [zagier1986] Zagier (1986), *Hyperbolic Manifolds and Special Values of Dedekind Zeta-Functions* — https://doi.org/10.1007/BFb0084581
  - [manuscript] quantum-observable-universe/predicted-spectra/hyperbolic-volume-transcendence.md
- **Tractability:** ℚ-linear independence of hyperbolic volumes (Bloch–Wigner dilogarithm); Mathlib has no Bloch group / dilog transcendence infrastructure.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.

## Verdict CONFIRMED 2026-08-31 (audit: docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md)

Individuated with the other thirteen. For THIS item the boilerplate verdict is right: the named
theory is genuinely absent from Mathlib and is genuinely required. Kept as-is.

Recorded because the same verdict was WRONG on several siblings; "confirmed" here means checked,
not merely un-revisited.

## Claim reset and applicability review 2026-11-22T21:40:00Z

Reset in-progress -> todo on owner card 2026-11-22 ("Do all three", analytic-conjectures drain thread). No bean update or main commit was carrying this claim. Re-claim with `bun run beans:claim` if you pick it up.

Applicability check against the rulings in force on 2026-11-22 (docs/coordination/owner-rulings.md): strand colour states, the rescaled generator b = -qX, convention D, photon norm 1, block-level U(1)_em charge, the photon/electron words. Verdict: Still applies. Q-linear independence of hyperbolic volumes; the Mathlib gap is real (confirmed 2026-08-31). On main the instance is conditional on `HyperbolicVolumeIndependenceAxiom` (HyperbolicVolumeIndependence.lean:41), which is the honest open state.
