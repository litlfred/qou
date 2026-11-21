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
updated_at: 2026-11-21T13:00:00Z
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

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8431, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T13:00:00Z expo-remarks drain (session_01Qmmkt7Gng13BtVDyQLMYQT)

Remark written: commit 8218d5028 on branch claude/expo-remarks-2026-11-21, draft PR #8832 (issue #8803). Exposition only: no new claim, no new number. Superseded-premise check (owner 2026-11-21 list: L-plus/minus in the photon, virtual photons, pre-Nov-15 gamma-gamma interface letters, T(2,n_s), convention C, single-term trace, trefoil as primary electron, 'c_2=-1 PROVED', chi_(2,1)=2-h^4, fitted alpha/CODATA in proofs, project memory): none found in the edited text. Status kept in-progress until #8832 merges; close as completed then.
