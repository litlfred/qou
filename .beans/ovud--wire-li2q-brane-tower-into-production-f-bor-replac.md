---
# ovud
title: Wire Li2q brane-tower into production F_Bor (replace /q3 normalization)
status: todo
type: task
created_at: 2026-06-24T03:48:33Z
updated_at: 2026-06-24T03:48:33Z
---


## Method (owner-specified, 2026-06-24): expansion-truncation, not raw tower

Replace the /q³ monomial normalization in F_Bor with a c_k-style
truncated expansion of the bounded brane-tower:

1. Bounded object: −Li₂^q(−V) = Σ_{n≥1} (−1)^{n+1} V^n / [n]_q.
2. Expand in u = b·ℏ_q² ≈ 0.0085 (or h² = (q−q⁻¹)²).
3. Truncate at order N: N ≥ log₁₀(1/ε)/2.07 − 1 (same rule as Q_β ladder).
4. Error control: truncation residual ~ u^{N+1} (vs /q³ = order-0, no
   error control).

DISCIPLINE: principled only to the order whose coefficients are DERIVED
symbolically from the q-dilog series (no CODATA fit). Unlike the refuted
Q_β c_k≥4 classes, these coefficients come from a known function
(Li₂^q), so low orders are genuinely derivable. Tier each order
proved/derived/fitted per the c_k framing (AGENTS.md).

Cross-ref: docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md
