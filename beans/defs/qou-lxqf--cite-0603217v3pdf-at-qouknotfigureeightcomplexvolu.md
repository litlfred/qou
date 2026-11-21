---
# qou-lxqf
title: Cite 0603217v3.pdf at QOU.Knot.FigureEightComplexVolume (docstring) and docs/audits/2026-07-26-sd…
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:50Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-19m0
---

The audit doc's literature-object paragraph and the Lean file's docstring both assert the deformed VC for 4_1 without a citable source.

Source: `library/arxiv-math-0603217v3/0603217v3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0603217v3/  ->  [murakami2006]
  A version of the volume conjecture

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [murakami2006] as the citation key when you do it.

## 2026-11-21 — expo-cite-xcheck drain

`[murakami2006] §1` added to FigureEightComplexVolume.lean and the 2026-07-26 audit. Finding F2: both write J_N → 𝔙(u) without log/N and call it a theorem without the r-near-1 scope. Completes on merge. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.
