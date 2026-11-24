---
# qou-urt1
title: Remark interpreting 0110001v3.pdf at computations/gap2_borromean_triple_count.py
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:03Z
updated_at: 2026-11-24T13:03:57Z
parent: qou-aqfj
---

The GAP-2 audit's M3(K) = mu-bar-irreducible triple count is currently defined only combinatorially on the contact graph. A remark recording the geometric triple-point form of the same count would make the definition checkable on an explicit link realisation. What would need checking first: the corpus's contact graphs are not currently realised as links with Seifert surfaces, so the translation is not automatic.

**From the source**
- p. 562, remark following the Theorem — When the boundary of F is disjoint from the double-point set (possible only if all pairwise linkings vanish) mu-bar(ijk) = -t(ijk)(F), a pure signed triple-point count.
  Use here: The Brunnian-case corollary is the geometric form of the 'Milnor-irreducible triple' the GAP-2 audit uses to define M3(K); it gives a surface-level object to count rather than a braid-word Magnus coefficient.

Source: `library/0110001v3/0110001v3.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/0110001v3/  ->  [mellor-melvin2003]
  A geometric interpretation of Milnor's triple linking numbers

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [mellor-melvin2003] as the citation key when you do it.


## Implementation Progress (PR #8412)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/ModularSixJNormalSurfaceTripleLinkingRound69.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round69_modular_sixj_normal_surface_triple_linking_probe.py` with 2-commit witness `computations/probes/round69-modular-sixj-normal-surface-triple-linking.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8412 (`ready: 83afa66fc31cdd276e7404f29767f2f41edefe60`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8412, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-22 — remark drafted, PR #9127

Remark block written on branch claude/library-remarks-2026-11-22, draft PR https://github.com/litlfred/qou/pull/9127 (issue #9121). Locators read from the held PDF. Stays open until the PR merges.

Session: https://claude.ai/code/session_01Qmmkt5c8TSSh1GGk4PoPDu



## 2026-11-24 — Tranche 3 origin/main reconciliation

Verified on origin/main (acb646cc6fe): Mellor-Melvin Seifert-surface triple-point form of mu-bar remark landed in merged PR #9184 (d03be3181ff / dc8919ec7a3).
