---
# qou-0a0n
title: Remark interpreting phys-rep09.pdf at prop:mi-sw-abelianisation
status: in-progress
pr: 8445
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:24Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-aqfj
---

Record the path-ordered Magnus representation and its convergence criterion next to prop:mi-sw-abelianisation's no-instance note, stating plainly that Magnus covers the one-dimensional case only and that the surface-ordered case the corpus needs is not addressed here. Deliberately not aid-proof: the dimension mismatch is exactly the unchecked hypothesis.

**From the source**
- Sects. 2.7.2-2.7.3 — Existence of the Magnus exponent and convergence of the Magnus series, with an improved radius of convergence in terms of the integrated operator norm.
  Use here: A proved convergence criterion for the exponential representation of a path-ordered transport -- the kind of statement that could make a Lean-tractable sub-case of the MI machinery, in contrast to the current position that no instance is expected. What would need checking: whether the corpus's connection-curvature pair restricted to a path in the exceptional divisor satisfies the norm bound.

Source: `library/phys-rep09/phys-rep09.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/phys-rep09/  ->  [blanes-casas-oteo-ros2009]
  The Magnus expansion and some of its applications

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [blanes-casas-oteo-ros2009] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8445, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T13:00:00Z expo-remarks drain (session_01Qmmkt7Gng13BtVDyQLMYQT)

Remark written: commit 61007fbba on branch claude/expo-remarks-2026-11-21, draft PR #8832 (issue #8803). Exposition only: no new claim, no new number. Superseded-premise check (owner 2026-11-21 list: L-plus/minus in the photon, virtual photons, pre-Nov-15 gamma-gamma interface letters, T(2,n_s), convention C, single-term trace, trefoil as primary electron, 'c_2=-1 PROVED', chi_(2,1)=2-h^4, fitted alpha/CODATA in proofs, project memory): none found in the edited text. Status kept in-progress until #8832 merges; close as completed then.
