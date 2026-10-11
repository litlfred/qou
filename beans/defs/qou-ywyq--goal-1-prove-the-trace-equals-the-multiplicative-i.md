---
# qou-ywyq
title: 'GOAL #1: prove the trace equals the multiplicative integral (def:mass-identity)'
status: todo
type: milestone
priority: critical
created_at: 2026-10-10T14:43:05Z
updated_at: 2026-10-11T05:59:18Z
---

Owner goal #1 (ofri, 2026-10-10, verbatim: 'start new session focused ONLY on showing that the trace equals the multiplicative integral. THAT IS PRIMARY GOAL #1 (GOAL #2 is 1ppq L2)').

Subject: def:mass-identity (folio/quantum-observable-universe/mass-endomorphism/mass-identity.{md,ts}). The prose defines mass via multiplicative integration MI∫; the Lean applies a trace on End(A) to a map 1→A (type error, recorded by PR #7601). Until proved, the identity is carried as a named conditional hypothesis (§3b-cond, owner pick 2026-10-10).

Known constraint: tmvac (PR #7605) proved only ‖MI∫_Σ‖ ≤ Σ‖…‖, and norm_additivity_not_forced is a counterexample to norm equality, so a proof must go through the trace, not norms.

Work lives in the dedicated project thread 'Trace equals multiplicative integral'. Related history: qou-qc6s (completed 2026-08-15, ref repoint). Do not close until the identity is proved sorry-free or refuted (AGENTS.md 13a). Goal #2 is milestone qou-10v9.

## 2026-10-10 — PR #7632 (session_01HjpvdM6z2jkKWYbBfwkCZG)
- PROVED (sorry-free, library sweep 15/15): `QOU.Torsion.MassTraceMarkov.braidTrace_wordBraid` — tr_M(β_ℓ) = wi^{m+1}·Tr(K^{⊗(m+1)}·Hol(ℓ)), Hol = ordered product of R-matrix transports (Ř for +, Ř⁻¹ for −); `jonesFn_wordBraid` is the framing-corrected form.
- `def:mass-identity` retyped: m(ϱ)=‖∫_A Ψ ϱ‖, Ψ=(∫_A⊗id)Δ = id when ∫=ε (counit law).
- STILL OPEN (bean stays open): Markov's theorem (link invariance); qou-0fmb abstract Ocneanu trace; H_n/rad ≅ TL_n; ∫=ε for the actual data; continuous KZ holonomy (Drinfeld–Kohno cited only).

## 2026-10-11 — Drinfeld–Kohno holds at the real pin; what remains is the framework connection
Kohno 1987 Remark 1.3.14 (library/kohno1987-aif, p.150): Theorem 1.2.8 holds at any complex coupling λ for which the R-side images φ(γ_k), γ_k=(σ1…σ_{k−1})^k, are diagonalizable, which holds when φ is completely reducible. At real q0>1 (not a root of unity) the U_q(sl2) tensor powers are semisimple and γ_k acts by ribbon scalars, so the theorem holds at the imaginary coupling λ0 = ln q0/(iπ) ≈ −0.0332i. The weight-preserving intertwiner argument (PR #7632) needs only q not a root of unity, so the weighted trace Tr(K^{⊗n}·) transports there too. Numerical check computations/kz_real_q0_pure_braid_monodromy_probe.py (mpmath 40 dps, n=3, pure braids incl. products): per-weight-sector traces agree to 1e-15, residual ∝ h^4, wrong orientation q→1/q fails by 0.70. Branch claude/kz-real-q0-2026-10-11. Cited, not proved in Lean. STILL OPEN (do not close): whether the framework's substrate connection IS this KZ connection (KZPullbackGenerators), and n>3 / full braid group only by citation.
