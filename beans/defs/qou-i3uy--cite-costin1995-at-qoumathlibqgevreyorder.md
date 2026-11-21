---
# qou-i3uy
title: Cite [costin1995] at QOU.Mathlib.QGevreyOrder
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:14Z
updated_at: 2026-11-21T12:26:55Z
parent: qou-1qhv
---

The Borel-summability/Stokes files carry no classical-ODE anchor; this reference already exists in references.ts and is exactly that anchor. Cite it as the classical leg, explicitly marked as the analogy's source and NOT as a transfer of the theorem to the q-difference setting.

**From the source**
- main theorem (abstract statement) — For analytic nonlinear systems of ODEs at a rank-one irregular singularity, under non-degeneracy and integrability conditions the formal exponential (trans-)series solutions are Borel summable in Ecalle's sense, and the resummed functions are exactly the solutions decaying in a specified sector; the correspondence's dependence on the ray gives the local Stokes phenomenon.
  Use here: It is the classical-side anchor for 'trans-series are Borel summable and the ray-dependence IS the Stokes phenomenon', which is the pattern the q-difference Stokes work assumes. Citing it would make the analogy's classical leg explicit rather than tacit.

Source: `library/arxiv-math-0608414v1/0608414v1.pdf` (`costin1995`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **declined** (no commit). QGevreyOrder.lean defines q-Gevrey growth order (Gaussian exponent of coefficient growth) and its slope algebra; it states nothing about Borel summability or Stokes phenomena. Costin 1995 (Borel summability of transseries for rank-one ODE systems) supports no statement in it.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status set to scrapped.
