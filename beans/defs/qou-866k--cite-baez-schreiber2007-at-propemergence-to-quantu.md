---
# qou-866k
title: Cite [baez-schreiber2007] at prop:emergence-to-quantum-flat
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:27Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

prop:emergence-to-quantum-flat cites baez2004 for fake-curvature/2-connection content that lives in this paper instead. Cite baez-schreiber2007 there, which simultaneously fixes the miscitation and retires this bib orphan.

**From the source**
- Abstract; and the vanishing-fake-curvature discussion in the body — A 2-connection on a principal 2-bundle gives parametrisation-independent parallel transport along surfaces exactly when the fake curvature vanishes; this is the condition matching Breen-Messing connections on nonabelian gerbes.
  Use here: This is the actual source for the flatness condition that prop:emergence-to-quantum-flat currently attributes to baez2004; citing it fixes a wrong-source citation and gives the F = B / F^- = 0 discussion a real 2-gauge-theoretic footing.

Source: `library/arxiv-math-0511710v2/0511710v2.pdf` (`baez-schreiber2007`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `7d4bc51ac`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). Baez-Schreiber §4 (pp.19-27) vanishing fake curvature; cite in .md/.ts/.lean.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
