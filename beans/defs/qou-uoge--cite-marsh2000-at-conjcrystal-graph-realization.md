---
# qou-uoge
title: Cite [marsh2000] at conj:crystal-graph-realization
status: completed
pr: 8412
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:25Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

Either drop marsh2000 (and khovanovlauda2009) from the cites array as unused, or add the sentence they are meant to support - the rectangle-diagram parametrisation of Lusztig-cone spanning vectors would naturally back the 'crystal highest-weight vertices are in bijection with GS irreducible forms' clause.

Source: `library/arxiv-math-0008040v1/0008040v1.pdf` (`marsh2000`)
Relevance: **tangential** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Implementation Progress (PR #8412)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/ModularSixJNormalSurfaceTripleLinkingRound69.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round69_modular_sixj_normal_surface_triple_linking_probe.py` with 2-commit witness `computations/probes/round69-modular-sixj-normal-surface-triple-linking.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8412 (`ready: 83afa66fc31cdd276e7404f29767f2f41edefe60`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8412, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `4056b68fdc1`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). dropped unused khovanovlauda2009+marsh2000 from cites[]

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
