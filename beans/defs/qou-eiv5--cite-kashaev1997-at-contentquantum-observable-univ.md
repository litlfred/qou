---
# qou-eiv5
title: Cite [kashaev1997] at folio/quantum-observable-universe/lean/QOU/LiftingDescent/tm_dilogarithm_…
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:37Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

Five Lean sites cite faddeev_kashaev1994 with DOI 10.1142/S0217732394002446 while the registry entry has 10.1142/S0217732394000447. Reconcile - either the registry DOI or the Lean docstrings are wrong, and both cannot be the 1994 'Quantum dilogarithm'.

Source: `library/arxiv-q-alg-9601025v2/9601025v2.pdf` (`kashaev1997`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `db02fb9f2`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). registry DOI correct, corroborated by held bibs; 5 Lean sites fixed

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
