---
# qou-wpca
title: Remark interpreting 1402.4615v3.pdf at conj:q-plancherel-asymptotic-skeleton
status: in-progress
pr: 8431
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:13:10Z
updated_at: 2026-11-18T10:40:05Z
parent: qou-aqfj
---

Not aid-proof: the Jack alpha-deformation is a different deformation from the folio's q-deformed Wedderburn weight and none of its hypotheses have been checked in that setting. The honest artifact is a remark at the q-Plancherel skeleton recording the Jack precedent and naming what would have to be checked (polynomiality of the q-character structure constants).

**From the source**
- §1.1 eq. (1) + main theorem (bulk first- and second-order asymptotics) — Under the Jack deformation P_n^(alpha)(lambda) = alpha^n n!/j_lambda^(alpha) of Plancherel measure, the bulk of a random Young diagram has a deterministic limit shape and Gaussian second-order fluctuations, extending Vershik-Kerov/Logan-Shepp and Kerov to all alpha > 0.
  Use here: A precedent theorem of exactly the shape conj:q-plancherel-asymptotic-skeleton part (3) needs, in a sibling one-parameter deformation. Cite as the method template and as evidence that the deformed-Kerov-Vershik statement is reachable; do NOT present it as covering the q-deformed weight.
- §1 (main tool: polynomiality of structure constants of Jack characters, after Lassalle) — The structure constants of Jack characters are polynomial in the deformation parameter, which is what makes the cumulant/CLT machinery go through.
  Use here: Identifies the structural input a q-analogue would have to reproduce for the folio's part (3): a polynomiality/degree bound on the structure constants of the q-deformed characters. Names the obstacle rather than removing it.

Source: `library/arxiv-1402.4615v3/1402.4615v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-1402.4615v3/  ->  [dolega-feray2014]
  Gaussian fluctuations of Young diagrams and structure constants of Jack characters

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [dolega-feray2014] as the citation key when you do it.


## Implementation Progress (PR #8431)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/AnisotropicContentHelicityOhtsukiQBorelRound72.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round72_anisotropic_content_helicity_ohtsuki_qborel_probe.py` with 2-commit witness `computations/probes/round72-anisotropic-content-helicity-ohtsuki-qborel.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8431 (`ready: 9f16804370f4cb20ca3c9ba012e7448a071f0f7c`).
