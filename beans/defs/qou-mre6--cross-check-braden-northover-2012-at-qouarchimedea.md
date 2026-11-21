---
# qou-mre6
title: Cross-check [braden-northover-2012] at QOU.Archimedean.BringHauptmodulGate
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:52Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

This document gives tau_0 ~ -0.5 + 0.185576i while BringHauptmodulGate.lean:41 records -0.5 + 0.186676i from braden-disney-hogg-2022. Determine which is the corrected value and note the supersession in the Lean, so the gate's numeric context does not silently carry two different tau_0.

**From the source**
- eq. (4.3) + footnote 5, §4 — tau_0 is defined by j(tau_0) = -29^3 x 5/2^5 = -121945/32 and j(5 tau_0) = -25/2; the earlier literature swaps these two equations, which the authors believe to be a typographical error.
  Use here: The corrected labelling the Bring hauptmodul gate depends on, and the source of the -121945/32 constant in its exact-rational sextic-root theorem.

Source: `library/sigma12-065/sigma12-065.pdf` (`braden-northover-2012`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `6358cf6eb22`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). BN2012 0.185576 is a misprint (J off); BDH 0.186676 verified mpmath; noted in Lean

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences. The τ₀ check is literature arithmetic on Bring's modulus; no particle form involved.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
