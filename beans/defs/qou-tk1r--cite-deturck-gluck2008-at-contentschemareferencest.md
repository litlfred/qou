---
# qou-tk1r
title: Cite [deturck-gluck2008] at content/schema/references.ts
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:11Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

Fix the φ₀ formula in the references.ts note (restore the −1) and give the reference a refid-keyed citation site so the H³ kernels are reachable from the dependency graph rather than only from bibliography metadata.

Source: `library/0510388v1/0510388v1.pdf` (`deturck-gluck2008`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done-partial** (commit `cd7348e30c0`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). note fixed: both phi_0 forms w/ locators; no content block cites key (citation-site ask needs an EM-linking block, not mine)

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. The verdict was done-partial, so the residual named in the note stays open: status set to todo.
