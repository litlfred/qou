---
# qou-x0aa
title: Cite [ramis-sauloy2006] at QOU/MathlibExt/QBorelKernel.lean — Thm 3.8/3.9 tie the level-δ q-Borel invariants to the alien derivations by theta multiplication
status: todo
pr: 8431
type: task
priority: normal
tags:
    - paper-relevance-triage
    - qdiff-stokes
    - reorg-2026-10-04
created_at: 2026-09-07T08:35:56Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1qhv
---

Source: library/arxiv-math-0611521v1/0611521v1.pdf -> [ramis-sauloy2006]. Relevance: **core** — agent assessment, not yet adjudicated. Raised by local/paper-relevance-triage 2026-09-07.

QOU/MathlibExt/QBorelKernel.lean (level-1 kernel t_n = q^{C(n,2)}) and QBorelKernelLevel.lean (closed form of the RSZ level-d recurrence) cite [ramis-sauloy-zhang2013] §3.3 only. Ramis–Sauloy §3.2 is the paper that says what the q-Borel transform of level δ is FOR:

- Thm 3.8 — with the notations of §2.3, the inhomogeneous equation (8) has a convergent solution iff B_q^{(δ)} U(jL) = 0 for all j in the level-δ index set, and the family of these q-Borel invariants is a complete set of analytic invariants within the formal class M0.
- Thm 3.9 — the automorphism Φ_a (left multiplication by θ^{−δ}(…) on each (α,β) block) sends the q-Borel invariant to the alien-derivation invariant Δ̇^{(δ)}_ξ(M).

So the kernel file's object and the alien-derivation file's object are the same invariant read through a theta power.

What to do: add the `-- Ref:` line with the locators (§3.2, Thm 3.8, Thm 3.9) to QBorelKernel.lean and QBorelKernelLevel.lean.

Caveat carried over from docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md: Ramis–Sauloy §2.3 "case of one level" assumes TWO integral slopes μ < ν with δ = ν − μ; C1 at ∞ is pure isoclinic (one slope), so these theorems constrain the kernel's meaning — they do not supply C1 Stokes data.


## Implementation Progress (PR #8431)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/AnisotropicContentHelicityOhtsukiQBorelRound72.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round72_anisotropic_content_helicity_ohtsuki_qborel_probe.py` with 2-commit witness `computations/probes/round72-anisotropic-content-helicity-ohtsuki-qborel.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8431 (`ready: 9f16804370f4cb20ca3c9ba012e7448a071f0f7c`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8431, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
