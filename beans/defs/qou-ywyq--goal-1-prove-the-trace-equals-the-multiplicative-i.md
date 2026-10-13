---
# qou-ywyq
title: 'GOAL #1: prove the trace equals the multiplicative integral (def:mass-identity)'
status: todo
type: milestone
priority: critical
created_at: 2026-10-10T14:43:05Z
updated_at: 2026-10-12T20:13:17Z
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

2026-10-12 — PR #7744 (Stream 2, session_01A1cKZcfvENVLgchFAKbxC4): the continuous KZ holonomy is no longer cited for the mass identity. QOU.Mass.KohnoWeighted.braidTrace_eq_kz (sorry-free): for every complex coupling kappa with q = e^{2 pi i kappa} not a root of unity, every weight w and every braid beta, braidTrace q q^-1 w wi beta = wi^{m+1} * Tr(siteWeight w * KZ(x_beta)), KZ = kzHeckeC, the Hecke-factored KZ holonomy representation on (C^2)^{tensor (m+1)} (kzBraidRep, rescaled e^{2 pi i kappa c} per crossing), x_beta = beta's image in H_{m+1}(q). Built on kz_conj_jimbo_complex + weight-space rigidity. Bean stays open: Markov's theorem, qou-0fmb, H_n/rad = TL_n, integral = counit for the actual data; roots of unity q != 1 not covered.


2026-10-12 — ∫=ε survey (Stream 2, owner pick 2a): VERDICT undetermined / not well-posed. For the data where mass is computed (A = H_n(q), ∫ = convention-D Markov trace) the corpus names no Δ and no ε. Lean carries ∫=ε only as hypothesis (MassTraceIdentity _of_frobeniusForm_eq_counit). General: Ψ = left mult by u = (∫⊗id)Δ(1), ∫ = ε(u·−); over a field ∫=ε ⇔ u=1 ⇔ Ψ=id ⇔ Δ(1)=coev, i.e. ∫=ε holds exactly when Δ is the ∫-induced coproduct (a choice of definition). SU(2) example: ∫ (Haar) ≠ ε (ev_e), but ∫∘Ψ = ∫ so m = ‖∫ϱ‖ anyway. Side findings beaned: qou-aj49 (content axiom 2 multiplicative counit forces A trivial), qou-5hbo (su2 example m=1 vs orthogonality). Owner decision pending on how to fix Δ.
