---
# qou-k7ra
title: 'GAP: vacuous carriers part A — residuals after PR #8691'
status: todo
type: task
priority: normal
created_at: 2026-11-20T21:28:46Z
updated_at: 2026-11-20T21:28:46Z
parent: qou-dx7g
---

PR #8691 repaired the part-A carriers where an object to tie them to exists. These stay open,
each needing an object neither the corpus nor Mathlib has:

1. **MassCoefficientShadowPrice** — no program to be the dual of. Needs a partition-indexed
   operator-selection LP carrying (Z,N,A), with uStar its certified dual (reuse
   HasFiniteLPDuality) and S_λ derived. Related qou-wg3c.
2. **SaturatedShellConjecture** — needs Φ_n as an element of a concrete H_n(q) and Δ_n² as the
   genuine full twist. Blocked on mass-endomorphism-conjecture.
3. **CosimplicialCrossedGroupoid** (content + library twin) — no tower, no indexed cofaces.
   Rebuild on Mathlib CosimplicialObject with [n] ↦ 𝔊_n, cofaces from jet prolongation.
4. **QouObstructionReductionContext** — HH dims are free numbers; needs Hochschild (co)homology
   of an actual U_q(su₂) with adjoint coefficients; κ₀ = χ(A) currently assumed via hattori_stallings.
5. **QCollatz** — cone  is free; pin Skein := LaurentPolynomial ℤ, define pos, port ~15
   consumers off generic Skein.
6. **DoubleMagicConjecture** — define LR coefficients (count of LR tableaux on YoungDiagram).
7. **confinement-nf-partial-proof.lean** keeps its own vacuous copy of HasFiniteLPDuality.
8. UGB file: GroebnerBasis.has_representation and SPolynomial are still True/TODO placeholders.
