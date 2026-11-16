---
# qou-ztod
title: 'FIBRE-A: bridge CyclicFaddeevPhi at N=4 to the zeta4 analytic model -- the two sorry-free zeta4 artifacts do not touch'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T14:21:19Z
updated_at: 2026-11-16T19:56:51Z
parent: qou-avtq
---

FINDING: grep -rl CyclicFaddeevPhi over the whole QOU tree returns its OWN FILE AND NOTHING ELSE. Two sorry-free zeta4 objects exist and do not touch: (1) QOU/Mass/ComplexVolumeZeta4Partner.lean -- analytic model vModel z = cosh z + i sinh z over C, with the zeta4 orbit, vanishing trivial/sign isotypes, and IsZeta4Faithful as a PROVED falsifier; (2) QOU/QBeta/FaddeevPhiFibreBranch.lean -- algebraic CyclicFaddeevPhi zeta N D over a generic field, discharged unconditionally at every primitive N-th root of unity by the finite q-Pochhammer. zeta4 = i is primitive 4th, so CyclicFaddeevPhi zeta 4 sits exactly where the model rotation acts. frakV_descent_zeta4_partner_probe.py records single_fibre_V OPEN, "Missing: both fibre kernels AND their assembly"; one kernel may already be built and merely unconnected. HONEST CAVEAT from the fibre-branch file itself: there is NO sorry-free bridge making the cyclic dilog an instance of the exact C-FaddeevPhi class -- the correspondence is a genuine DEGENERATION of the functional equation. So bridge to the zeta4 ACTION on vModel, not to FaddeevPhi. Falsifiable at once: nonzero zeta4 orbit sum or nonzero sign isotype refutes the assembly. Doc: option A.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Unchanged since filing. CyclicFaddeevPhi is still referenced only by its own file, and no bridge exists.

Evidence: `grep -rl CyclicFaddeevPhi folio/.../lean/QOU` → only `QBeta/FaddeevPhiFibreBranch.lean`. The finding still holds: the two ζ₄ artifacts do not touch. Both files are sorry-free (the "sorry" hits are docstring text).

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Round 50 Formalization & 50-dps Witness (PR #8177)
- **Lean 4 Module (`0 sorry`, `0 axiom`, `0 vacuity`):** `folio/quantum-observable-universe/lean/QOU/QBeta/CyclicFaddeevZeta4Bridge.lean`
  - `cyclicDenomFour_collapse`: $(1 - x)(1 - \zeta_4 x)(1 - \zeta_4^2 x)(1 - \zeta_4^3 x) = 1 - x^4$ when $\zeta_4^2 = -1$.
  - `cyclicDenomFour_periodic`: $D_4(\zeta_4, \zeta_4 x) = D_4(\zeta_4, x)$.
  - `cyclicCarrier_not_zeta4Faithful_of_ne_zero`: any `CyclicFaddeevPhiFour` carrier $D$ is strictly $\zeta_4$-periodic with 4-step $\zeta_4$-orbit sum $4 D(x)$, so it cannot be `IsZeta4Faithful` whenever $D(x) \neq 0$.
  - `bridgedAssembly_isZeta4Faithful`: multiplying any `IsZeta4Faithful` analytic model $V$ (`vModel`) by any `CyclicFaddeevPhiFour` carrier $D$ yields a bridged assembly $B_k(x) = V_k \cdot D(x)$ that satisfies both $\zeta_4^2 = -1$ and `IsZeta4Faithful`.
- **50-dps Witness:** `computations/probes/round50-zeta4-bridge-and-alpha-em-cs-tower.witness.json` (`scriptHash: e7bf4a93b887`, `scriptCommitSha: cf283b8e199f4643fb9e0259ec0a2702096bdd9b`).
- **PR:** `litlfred/qou#8177` (`https://github.com/litlfred/qou/pull/8177`, head SHA `3fdbeeb87a6b1821ff8d57a95f95d4d20cf72628`).
- **Status:** Kept at `status: in-progress` per reviewer-separated closure discipline.
