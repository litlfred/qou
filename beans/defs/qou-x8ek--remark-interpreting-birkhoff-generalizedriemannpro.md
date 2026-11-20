---
# qou-x8ek
title: Remark interpreting Birkhoff-GeneralizedRiemannProblem-1913.pdf at content/quantum-observable-uni…
status: todo
pr: 8431
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:29Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-vva9
---

Record the scope boundary explicitly so the primary source is not over-read: the connection-matrix formulation is the regular-singular q-difference setting, whereas C1's obstruction at infinity is irregular and pure isoclinic. Adding the reference must not be taken to reopen the RSZ route the 2026-08-08 audit closed.

**From the source**
- the q-difference sections of the 1913 memoir (the 'allied problems') — For a linear q-difference system, the analytic solution is characterized by connection constants relating canonical solutions at 0 and at infinity -- the Birkhoff connection matrix -- and the associated Riemann problem asks for those constants to be prescribed at will.
  Use here: The primary source for the global object BirkhoffAmplitudeWellPosed.lean reasons about (P = (X^infty)^{-1} X^0 and the gauge freedom of the canonical local solutions), which currently cites only the modern RSZ treatment.

Source: `library/birkhoff-generalizedriemannproblem-1913/Birkhoff-GeneralizedRiemannProblem-1913.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/birkhoff-generalizedriemannproblem-1913/  ->  [birkhoff1913]
  The Generalized Riemann Problem for Linear Differential Equations and the Allied Problems for Linear Difference and q-Difference Equations

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [birkhoff1913] as the citation key when you do it.


## Implementation Progress (PR #8431)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/AnisotropicContentHelicityOhtsukiQBorelRound72.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round72_anisotropic_content_helicity_ohtsuki_qborel_probe.py` with 2-commit witness `computations/probes/round72-anisotropic-content-helicity-ohtsuki-qborel.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8431 (`ready: 9f16804370f4cb20ca3c9ba012e7448a071f0f7c`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8431, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
