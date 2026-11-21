---
# qou-hp9s
title: Remark interpreting CuspShapes.pdf at prop:cusp-shape-bar-parity
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:39Z
updated_at: 2026-11-21T13:10:00Z
parent: qou-aqfj
---

Pin down which object 'cusp shape' names in prop:cusp-shape-bar-parity -- the Teichmuller modulus of the cusp torus, or the ideal-tetrahedron shape parameter tiling it -- and confirm the figure-eight value against the standard one. Deliberately a remark and not aid-proof: I could not settle the numerical question in this session, and the downstream cusp lattice Z<1, omega> depends on the answer.

**From the source**
- sec. 3 ("Recall that the Teichmuller space of the torus is the space of similarity classes...") + Def. 2.1-2.4 — The cusp shape of a hyperbolic 3-manifold with torus boundary is the similarity class of the Euclidean structure induced on a neighbourhood of that boundary, i.e. a point of the Teichmuller space of the torus.
  Use here: Supplies the standard definition for a term the corpus uses in at least three blocks with no source, and against which its value for the figure-eight should be checked.
- Thm 1.1 — Cusp shapes of hyperbolic tunnel-number-one manifolds are dense in the Teichmuller space of the torus.
  Use here: Background only: it says the cusp shape is not constrained by low tunnel number, so no structural conclusion can be drawn from a particular knot's cusp shape being special.

Source: `library/cuspshapes/CuspShapes.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/cuspshapes/  ->  [dang-purcell]
  Cusp shape and tunnel number

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [dang-purcell] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8499, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T13:00:00Z expo-remarks drain (session_01Qmmkt7Gng13BtVDyQLMYQT)

Remark written: commit e6cd04561 on branch claude/expo-remarks-2026-11-21, draft PR #8832 (issue #8803). Exposition only: no new claim, no new number. Superseded-premise check (owner 2026-11-21 list: L-plus/minus in the photon, virtual photons, pre-Nov-15 gamma-gamma interface letters, T(2,n_s), convention C, single-term trace, trefoil as primary electron, 'c_2=-1 PROVED', chi_(2,1)=2-h^4, fitted alpha/CODATA in proofs, project memory): none found in the edited text. Flag, not edited: the block title still says 'figure-eight modulus' for what the source calls the cusp shape. Status kept in-progress until #8832 merges; close as completed then.

## 2026-11-21T13:10:00Z closed

PR #8832 merged 2026-11-21T13:07Z; remark is on main.
