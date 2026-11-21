---
# qou-xiaj
title: Cite 2402.04839v2 (1).pdf at fundamental-knots-operator-basis
status: completed
pr: 8435
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:51Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

Once the entry exists, the fundamental-knots table and the three-calibration proof should cite it at the exact points where they say 'simplest hyperbolic knot', replacing an informal appeal with the minimality statement.

**From the source**
- Example 2.1 — volt(S^3) = 2 v_0 ~ 2.02988, where v_0 is the volume of the ideal regular tetrahedron, with the figure-eight knot complement realising the minimum among hyperbolic link complements in the three-sphere.
  Use here: Sources and sharpens the corpus's repeated but uncited 'simplest hyperbolic knot' justification for the figure-eight anchor, turning an informal appeal into a minimality theorem about the very number the corpus already uses.
- Cor. 2.11 and the surrounding discussion of universal links — The Borromean rings are a universal link -- every closed orientable 3-manifold is a cover of the three-sphere branched over them -- and for a hyperbolic universal link L, volt(M) <= d_L(M) volH(L).
  Use here: A structural fact about the corpus's nucleon knot that is absent from the corpus: the Borromean complement is not merely a convenient hyperbolic link but a universal one, which is the kind of no-choice selection argument the framework's knot assignments otherwise lack.

Source: `library/arxiv-2402.04839v2/2402.04839v2 (1).pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2402.04839v2/  ->  [kegel2024]
  On a volume invariant of 3–manifolds

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [kegel2024] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8435, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — expo-cite-xcheck drain

`\cite{kegel2024}` added at three-calibration-inputs-proof.md 'simplest hyperbolic knot invariant' (figure-eight unique minimiser, held text). The table in fundamental-knots-operator-basis does not use the phrase, so no cite there. Universal-link fact not added (new exposition, owner's call). Completes on merge. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.

## 2026-11-21: merged

Completed: PR #8852 merged (merge 4d8767a1c).
