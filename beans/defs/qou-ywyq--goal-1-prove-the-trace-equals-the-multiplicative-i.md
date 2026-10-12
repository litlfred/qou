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


2026-10-12 — ∫=ε survey (Stream 2, owner pick 2a): VERDICT undetermined / not well-posed. For the data where mass is computed (A = H_n(q), ∫ = convention-D Markov trace) the corpus names no Δ and no ε. Lean carries ∫=ε only as hypothesis (MassTraceIdentity _of_frobeniusForm_eq_counit). General: Ψ = left mult by u = (∫⊗id)Δ(1), ∫ = ε(u·−); over a field ∫=ε ⇔ u=1 ⇔ Ψ=id ⇔ Δ(1)=coev, i.e. ∫=ε holds exactly when Δ is the ∫-induced coproduct (a choice of definition). SU(2) example: ∫ (Haar) ≠ ε (ev_e), but ∫∘Ψ = ∫ so m = ‖∫ϱ‖ anyway. Side findings beaned: qou-aj49 (content axiom 2 multiplicative counit forces A trivial), qou-5hbo (su2 example m=1 vs orthogonality). Owner decision pending on how to fix Δ.
