---
# qou-j28s
title: Remark interpreting 0706.2213v3.pdf at prop:cusp-shape-bar-parity
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:54Z
updated_at: 2026-11-21T13:10:00Z
parent: qou-aqfj
---

prop:cusp-shape-bar-parity calls e^{i*pi/3} 'the cusp shape of 4_1'; DHY Fact 4 defines the cusp shape as the longitude translation c in the parabolic normalisation, a different quantity. Proposing new-remark, NOT aid-proof: the Lean lemma cusp_barParity_split is a correct statement about a primitive sixth root of unity regardless, so nothing is broken -- what needs checking is only the NAME, and I have not verified which object the downstream uses intend.

**From the source**
- Eq. (10) and Remark 15 / Tables 1-2 column 3 — For a hyperbolic two-bridge knot, the cusp shape is c = n - 2*w_{1,2}*w_{2,2}; and via u = 4/(c-2) the torsion at the holonomy is a rational function of the cusp shape c.
  Use here: A published cusp-shape convention (Fact 4: mu -> [[1,1],[0,1]], lambda -> [[-1,c],[0,-1]]) that the corpus should check prop:cusp-shape-bar-parity against -- that block calls omega = e^{i*pi/3} 'the cusp shape of 4_1', which is the regular ideal tetrahedron shape parameter, whereas DHY's c is the cusp-torus modulus. These are different objects and the corpus uses the same phrase for both; worth resolving before either is cited outward.

Source: `library/arxiv-0706.2213v3/0706.2213v3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-0706.2213v3/  ->  [dubois2007]
  NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [dubois2007] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8508, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T13:00:00Z expo-remarks drain (session_01Qmmkt7Gng13BtVDyQLMYQT)

Remark written: commit e6cd04561 on branch claude/expo-remarks-2026-11-21, draft PR #8832 (issue #8803). Exposition only: no new claim, no new number. Superseded-premise check (owner 2026-11-21 list: L-plus/minus in the photon, virtual photons, pre-Nov-15 gamma-gamma interface letters, T(2,n_s), convention C, single-term trace, trefoil as primary electron, 'c_2=-1 PROVED', chi_(2,1)=2-h^4, fitted alpha/CODATA in proofs, project memory): none found in the edited text. Flag, not edited: the block title still says 'figure-eight modulus' for what the source calls the cusp shape. Status kept in-progress until #8832 merges; close as completed then.

## 2026-11-21T13:10:00Z closed

PR #8832 merged 2026-11-21T13:07Z; remark is on main.
