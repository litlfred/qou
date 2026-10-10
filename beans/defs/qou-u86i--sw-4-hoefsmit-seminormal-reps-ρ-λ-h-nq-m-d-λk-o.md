---
# qou-u86i
title: 'SW-4: Hoefsmit seminormal reps ρ_λ : H_n(q) → M_{d_λ}(K) on the SYT basis (explicit σ_i matrices)'
status: completed
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-19T13:38:48Z
parent: qou-59vq
blocked_by:
    - qou-2xre
    - qou-rsbf
---

The explicit representations: σ_i acts on the SYT basis of S^λ by Hoefsmit's seminormal matrices (axial-distance formulas). Ref: [hoefsmit1974], [ram1997].

## ✅ Concrete cases LANDED (2026-08-02, background agent) — 1 honest Ref'd gap

[`QOU/SchurWeyl/HoefsmitRep.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/content/quantum-observable-universe/lean/QOU/SchurWeyl/HoefsmitRep.lean)
(EXIT=0, independently re-verified). Sorry-free:
- `rhoTriv`/`rhoSign` — the two 1-dim reps via `Hecke.lift`, **generic [CommRing K]**,
  and (surprise) the quadratic is a `ring` identity needing NO `q·qi=1`.
- `S0`,`S1` + `S0_quadratic`,`S1_quadratic`,**`S0_S1_braid`** — the λ=(2,1) 2×2
  seminormal matrices over ℝ with the **braid relation S0S1S0=S1S0S1 proved
  sorry-free for all q≠0** (square-root-free seminormal S1). Assembled as
  `seminormalRep21 : Hecke ℝ q q⁻¹ 2 →ₐ[ℝ] M₂(ℝ)`.
- `cellContent`,`axialDistance`(+row/col lemmas) — infrastructure.

**One honest gap (state-and-queue, §1-compliant):** `hoefsmit_seminormal_rep`
(general λ, non-scalar for d_λ≥2) — `sorry` + `-- Ref:[hoefsmit1974]/[ram1997]`
+ `-- GAP:`. Split off as residual bean **qou-im9l**. Wired into QOU.lean.

**SW-5 handoff:** `seminormalRep21` is the concrete irreducibility testbed —
S0 diagonal (distinct eigenvalues q,−q⁻¹) + S1 off-diagonal (b=1≠0) ⇒
irreducible for q²≠−1; no common invariant subspace.


## VERIFIED CLOSED (2026-08-19) — general lambda, not just concrete cases

`hoefsmit_seminormal_rep` is PROVED for all lambda in
`SchurWeyl/HoefsmitRepGeneral.lean` (merged #5279, bean qou-im9l). The old
`-- Ref:`-cited sorry in HoefsmitRep.lean is gone; that file now carries only a
pointer note at line 384. Verified by direct grep: 0 sorries in HoefsmitRep.lean
and HoefsmitRepGeneral.lean.

This bean's body still described the state as *'concrete cases landed, one honest
gap'*. That was true on 2026-08-02 and stale for a week.
