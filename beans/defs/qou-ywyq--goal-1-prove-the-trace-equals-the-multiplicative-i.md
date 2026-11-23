---
# qou-ywyq
title: 'GOAL #1: prove the trace equals the multiplicative integral (def:mass-identity)'
status: in-progress
type: milestone
priority: critical
created_at: 2026-10-10T14:43:05Z
updated_at: 2026-11-23T23:38:35Z
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

2026-10-12 — PR #7772 (Stream 2, owner decision 1c): the mass identity is restated on braid classes. QOU/Torsion/MassTraceMarkovClass.lean (sorry-free, axioms propext/choice/Quot.sound): artinTower (Artin braid groups as a MarkovMoves.BraidTower), jonesTot_isMarkovInvariant (framing-corrected trace at w=(1,q^2) invariant under conjugation and both stabilisations), massClass (descent to Quot), exists_wordBraid (every braid is a word), massClass_wordBraid (mass identity on classes), holTrace_eq_of_markovEquiv. Content: def:mass-identity gains a braid-classes paragraph with one Alexander-Markov citation; prop:categorical-mass-markov statement and proof scope updated. The Markov's-theorem item is thereby discharged on the algebraic side per 1c (links cited only). Bean stays open: qou-0fmb, H_n/rad = TL_n, integral = counit for the actual data.

2026-10-12 (cont.) — PR #7772 commit 8decf48456: QOU.Mass.KohnoWeightedClass.massClass_kz (sorry-free): mass of a braid class = framing-corrected site-weighted trace of the KZ holonomy kzHeckeC of any representative, for q=e^{2 pi i kappa} not a root of unity.

## 2026-11-15 — PR #7990 (`f6c6c9e`, owner ruling Q-YWYQ-1 = "try 1 and 3")
- Formalised Option 1 (non-abelian ordered holonomy `hol w` in `Hom(1, A)` before applying `∫_A ∘ Ψ` or `tr(L_{hol(w)} ≫ Ψ)` in `QOU/Torsion/MassTraceIdentity.lean`, `QOU/Torsion/MassTraceMarkov.lean`, and `mass-identity.lean`) and Option 3 (Temperley–Lieb state-sum expansion of `hol q qi ℓs`, `braidTrace`, `jonesFn`, and `massClass` over generic `[CommRing R]` with `q * qi = 1` in `QOU/Torsion/MassTraceMarkov.lean` and `QOU/Torsion/MassTraceMarkovClass.lean`, including `braidTrace_wordBraid_eq_leadProd_add_tlStates` isolating the $s \equiv \mathrm{false}$ naive per-crossing scalar product from the $2^k - 1$ Temperley–Lieb cup-cap states).
- Updated `mass-identity.{md,ts,lean}` in parity while preserving the §7c wall-side acknowledgement. Kept `status: in-progress` for owner review.

## 2026-11-16 — PR #8148 (`b1cda0e`, `qou-9634` & `qou-ep0a`)
- Formalized `QOU.Mass.KZHolonomy.MultiStrandHeckeFactor` (`qou-9634`, generic `R` per §7c, `0` `sorry`) and `QOU.Torsion.MarkovTraceTowerStabilization` (`qou-ep0a`, generic `R` per §7c, `0` `sorry`), wired into `QOU.lean`. Kept `status: in-progress`.

2026-11-23 (WS2 consolidation): Opened READY PR https://github.com/litlfred/qou/pull/9187 (76a0d2e6187, Bridge A W7 Gaps 1-4) and READY PR https://github.com/litlfred/qou/pull/9197 (f5d343840a6, W8 LaurentHeckeMonodromy + HeckeModelsBridge + WtraceTwistedPositivity + 8 legacy axiom deletions).

Claimed by claude/w7-chen-mult-integral-masstrace-20261123 (Worker 17, 2026-11-23)

EOS (2026-11-23, Worker 17, branch claude/w7-chen-mult-integral-masstrace-20261123, issue #9214):
- Lean 4 module folio/quantum-observable-universe/lean/QOU/Torsion/ChenMultiplicativeIntegralBridge.lean (commit 15db38d0253, 0 sorry, 0 custom axioms — [propext, Classical.choice, Quot.sound] only, zero empirical constants):
  (1) Ordered matrix product path-concatenation multiplicativity (orderedProd_append, eulerStepProd_append), gauge covariance & closed-loop trace invariance (orderedProdFin_gauge_covariant, trace_gaugeTransform_closed_loop), and units/weighted associator conjugation trace invariance (trace_eq_of_units_intertwine, weighted_trace_eq_of_commuting_intertwine).
  (2) Algebraic Chen iterated-integral tensor-coalgebra shuffle homomorphism & group-like signature stability over generic [CommAlgebra Q R] (shuffleEval_chenSigMul, shuffleEval_wordProd, isShuffleGroupLike_segmentSig, IsShuffleGroupLike.chenSigMul, isShuffleGroupLike_piecewiseLinear).
  (3) Picard contraction, linear ODE fundamental-solution uniqueness, and discrete Gronwall O(1/N) error bound + convergence of N-step Euler ordered matrix products (norm_picardOp_sub_le, IsLinearFundSol.eqOn, eulerOrderedProd_error_bound, tendsto_eulerOrderedProd_isFundSol).
  (4) Concrete non-vacuous Matrix (Fin (d+2)) (Fin (d+2)) R Frobenius-Hopf substrate instantiation of MassTraceIdentity: regular trace d * Tr(M) vs counit trace Tr(M) (matFrobHopf_frobeniusMass_eq_trace, matFrobHopf_leftTrace_eq_dim_mul_trace), inner commutator connection nablaEndo = adEndo K satisfying Leibniz and non-vanishing on KZ Casimir kzOmega01 (adEndo_leibniz, adEndo_kzOmega01_ne_zero), block-diagonal Reeb/matter decoupling (evalTraceLin_cross_zero, substrateLagrangian_normalised), and non-abelian 3x3 Borromean two-term instantiation matching twoTermCandidateBorromean (substrate_borromean_two_term_instantiation).
  (5) Explicit 2-row/hook Hecke & KZ monodromy bridge on B_3 ([2,1], dim 2) and B_4 ([2,2], dim 2; [3,1], dim 3), proving exact KZ half-turn fundamental solution, local quadratic Hecke relation, real/complex monodromy-to-Hecke trace equality, and Convention-D 2-row generator synthesis (kzHalfTurnFundReal_isFundSol, kzLocalMonodromyReal_hecke_quad, kzMonodromy_trace_eq_hecke_real, kzMonodromy_trace_eq_hecke_complex, conventionD_twoRow_generator_synthesis).
- Pre-registered 80-dps probe & witness computations/probes/w7_chen_multiplicative_integral/ (PREREGISTRATION.md cbd41d51fb5, probe 15db38d0253, witness 5978c1eb262, workDps=80, outputDps=50, q0Anchor=proton, 59/59 assertions passed, 0 float64): path-concatenation < 2.5e-80, Chen shuffle/deconcatenation < 6e-82, Gronwall O(1/N) bound + Richardson O(1/N) scaling verified, continuous KZ Yang-Baxter & far-commutativity < 4.5e-80, Klein-four V_4 symmetry P_KZ^{[2,2]}(sigma_0)=P_KZ^{[2,2]}(sigma_2) to 2.11e-81 vs [3,1] diff 3.0332, Drinfeld associator Phi_KZ conjugacy < 2.4e-80 with leading zeta(2) commutator norm (1/2)eta_0^2 = 0.0054284 verified to 3.44e-5, and |Tr(P_KZ(w)) - Tr(rho_Hecke(w))| < 1.6e-80 across all 21 knot/link sector-word pairs (3_1, 4_1, T(3,5), Borromean, T(4,3) + Markov stabilizations).

Ready PR opened: https://github.com/litlfred/qou/pull/9228 (head 5978c1eb262, Refs #9214).
