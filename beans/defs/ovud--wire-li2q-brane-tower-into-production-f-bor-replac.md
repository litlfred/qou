---
# ovud
title: Wire Li2q brane-tower into production F_Bor (replace /q3 normalization)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-24T03:48:33Z
updated_at: 2026-11-16T19:04:00Z
parent: qou-2002
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

## FINDING (2026-06-24, PR #2691): premise reframed — /q³ is EXACT

Probe `computations/li2q_fbor_expansion_probe.py` proves:
- [3]_q!/q³ = 1 + 2q⁻² + 2q⁻⁴ + q⁻⁶ EXACTLY (sympy, residual 0). The
  /q³ is q-factorial balancing, NOT a fit. F_Bor is a fully exact form.
- F_Bor alone lands m_p at −242 ppb.
- The habiro_ratio (1+46u⁴)(1+4u⁵)(1−29u⁶) supplies +2.42e-7 = +242 ppb,
  cancelling that residual to 0.0004 ppb. The {46,4,29} are the genuine
  CODATA-anchored fit — THIS is the improvement target, not /q³.
- The Li₂^q brane-tower (terms 2/3) is O(1) on the proton's O(1) per-gen
  volumes (Σ −Li₂^q(−|V̂|) = 1.618) — WRONG scale by 10⁷ for the O(1e-7)
  correction. The +242 ppb closer is the term-6 Habiro residue tail.

REMAINING (the real ovud): deriving the {46,4,29} term-6 Habiro residue
is the SAME open Habiro-element problem as the Q_β c_k ladder (s5bb
keystone). NOT a Li₂^q-tower reparametrisation. Gated on s5bb.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-06-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Formalisation & Verification Update (2026-11-16, PR [`litlfred/qou#8158`](https://github.com/litlfred/qou/pull/8158), commit `75b6b451ceab7004d7b1dbd5350d3c71eff04c1c`)

- Formalised the exact Laurent balancing identity in Lean 4 at `folio/quantum-observable-universe/lean/QOU/Observations/SubstrateParameterLocality.lean` (`qfact3_eq_q3_mul_laurent_balancing` and `qfact3_expanded_laurent`, `0` `sorry`, generic `CommRing R` with `q * qi = 1`): $(q^2 + 1 + qi^2)(q + qi) = q^3(1 + 2qi^2 + 2qi^4 + qi^6) = q^3 + 2q + 2qi + qi^3$.
- Verified symbolic exactness and 50-dps logarithmic sensitivity $\frac{d\ln([3]_q!/q^3)}{d\ln q}\big|_{q_0} = -2.35361087\dots$ in `computations/probes/substrate_parameter_locality_varying_constants_probe.py`.
