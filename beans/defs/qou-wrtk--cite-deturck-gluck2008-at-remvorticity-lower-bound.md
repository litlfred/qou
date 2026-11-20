---
# qou-wrtk
title: Cite [deturck-gluck2008] at rem:vorticity-lower-bound-argument
status: todo
pr: 8431
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:26Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-1qhv
---

A registered reference giving helicity bounds and a Biot-Savart formula in hyperbolic 3-space is uncited while three fluid-dynamics remarks argue about helicity and Biot-Savart strain. Cite it where the ambient-geometry dependence of the helicity bound is discussed.

**From the source**
- front matter, bullets 1 and 3 — Explicit isometry-invariant integral formulas for linking, twisting, writhing and helicity in S^3 and H^3, with the Biot-Savart formula yielding upper bounds for helicity and lower bounds for the first eigenvalue of curl on subdomains.
  Use here: The hyperbolic-space version is the setting the framework actually works in; a helicity upper bound in H^3 is the natural comparison for the vorticity lower-bound argument, which currently argues in the Euclidean setting.

Source: `library/0406276v1/0406276v1.pdf` (`deturck-gluck2008`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Implementation Progress (PR #8431)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/AnisotropicContentHelicityOhtsukiQBorelRound72.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round72_anisotropic_content_helicity_ohtsuki_qborel_probe.py` with 2-commit witness `computations/probes/round72-anisotropic-content-helicity-ohtsuki-qborel.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8431 (`ready: 9f16804370f4cb20ca3c9ba012e7448a071f0f7c`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8431, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
