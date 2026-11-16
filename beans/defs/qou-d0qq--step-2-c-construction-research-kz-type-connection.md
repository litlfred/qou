---
# qou-d0qq
title: 'Step-2 option C (research): the sl2 KZ connection on Conf3(C) pulled back along the colour cubic''s root map, at the level FIXED BY q0 (q0 is input; forever-gate) — does its monodromy reproduce the Hecke quadratic and z_D = q^3/(q^2+1)?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T08:13:53Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-wp3h
---

2026-09-06 first measurement (exact, mpmath 40 dps at the proton pin): KZ at REAL level cannot give q0 (unit modulus, Lean KZUnitModulusPrune); at IMAGINARY level it can — with q = e^{2πi/(k+2)}, k+2 = 2πi/ln q0 = 60.2179598524791980753 i (ln q0 = 0.10434072031951951232); with q = e^{iπ/(k+2)}, k+2 = 30.1089799262395990377 i. So the prune does not kill C; it fixes the level to be non-unitary. Next: write the KZ connection on Conf of the six branch points at that level and compute its monodromy exactly (Kohno–Drinfeld gives Hecke; the question is whether the framework's connection IS this one).



2026-09-07 claimed (session route-c / step-2 arc). Planning agent dispatched (label kz-level) for the initial plan; q₀ is INPUT only (forever-gate respected). Plan to be filed by the parent session.



2026-09-07 PLAN FILED: docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md §B (agent kz-level, parent-verified). The bean's stated next step is ill-posed: the six branch points are fixed, so the base is C∖{6 points} (π₁ = F₆), and the only meaningful construction is the sl₂ KZ connection on Conf₃(C) pulled back along the root map. Queue: B1 = braid word of each lasso (half-twist or not), B2 = Lean z_D = U_q(sl₂) quantum trace (already numerically confirmed, diff 5e-31) and z_3 ≠ z_D, B3 = flatness is level-independent + reword the three 'flat at q₀' prose sites, B5 = retitle this bean (the title's 'does any level reproduce q0' is gate-violating wording; q₀ is INPUT). Registry key correction: drinfeld1985, not 1990.



2026-09-07 EXECUTED: P2 (SL2QuantumTraceIsZD: z_D is the sl2 quantum trace, sl3 never equals it over any field), P3 (KZFlatnessLevelIndependent + two prose sites reworded), P5 (colour_cubic_braid_monodromy_probe, parent re-run 13/13: all six lassos are positive half-twists, conjugacy ESTABLISHED, product = Δ² = loop at infinity). Remaining: plan step 5 (carry the named hypothesis — substrate connection = sl2 KZ on Conf3 pulled back along the root map at level k+2 = iπ/ln q0 — as a field of conj:hecke-monodromy-step-two) and step 6 (ingest Kohno 1987 / Drinfeld 1985). Audit §0b. PR #7035.

2026-09-07 plan step 5 DONE: QOU/Mass/KZPullbackHypothesis.lean — class KZPullbackGenerators (each substrate generator is conjugate in the tower to a KZ generator satisfying the Hecke quadratic with the level's q; Kohno–Drinfeld cited); quad_of_kz DERIVES HeckeMonodromy.quad from it, heckeMonodromy_of_kz assembles the Step-2 instance given braid / far_comm / shadow (which per-generator conjugacy does not supply — the measured conjugators differ per lasso). No instance provided: constructing the connection is the open remainder. conj:hecke-monodromy-step-two .md names the hypothesis and the three results. Remaining on this bean: plan step 6 (ingest Kohno 1987 / Drinfeld 1985), and the construction itself.



2026-09-07 CONSTRUCTION HALF, as far as computable (kz_pullback_monodromy_exact_probe.py, 13/13; Lean KZLevelFromHeckeNormalisation, sorry-free): (1) the level is fixed convention-free by the eigenvalue RATIO of the KZ half-twist — split Casimir 1/4 on Sym², −3/4 on Λ² ⇒ ratio −e^{iπħ}; matching the Hecke ratio −q² gives q² = e^{iπħ}, i.e. ħ = (2/iπ) ln q, purely imaginary at the real pin (ħ = −0.0664i; k+2 = 15.05i or 30.10i under ħ = 1/(k+2) or 2/(k+2) — the two levels previously on this bean are those two conventions; the route-5 probe's 'ħ = 2 ln q' is the same relation with iπħ renamed). (2) The pulled-back representation ϱ: F₆ → B₃ → End(V^{⊗3}) is explicit from the six measured lasso words: each ϱ(w_j) satisfies the Hecke quadratic and has pivotal trace z_D; image = image of B₃; ϱ(w₁⋯w₆) = ϱ(Δ²), central, eigenvalue q⁶ on the spin-3/2 block and 1 on both spin-1/2 blocks. (3) The framework side has no connection object to compare (cheat-sheet §2a); KZPullbackGenerators is the interface. STATUS: the KZ side of option C is done; what is open is Step 2 itself — a connection on the framework side. Stays open (rule 13a).



2026-09-07 (owner pick 2): #7044 merged. Planning agent dispatched (label fw-conn) for the FRAMEWORK-side connection — which framework object can carry a flat connection on C∖Δ whose monodromy generators are conjugate to the KZ half-twists (the KZPullbackGenerators interface); the natural candidate to assess is the Gauss–Manin connection of the colour-cubic family and where its q-deformation comes from. q₀ input only.



2026-09-07 fw-conn PLAN FILED (audit §C) and steps 1–2 EXECUTED by the parent: UntwistedMonodromyPrune.lean (finite-order / quasi-unipotent eigenvalues are never > 1 — C1/C2 dead, scope (b)); colour_cubic_abelian_twist_holonomy_probe.py 8/8 (A⁰ = X dz has trivial push-down and trivial holonomy around every ramification point — C3 dead, scope (b)). Survivor C3′: external twist exponent μ with e^{2πiμ} = −q₀², i.e. the KZ level. CONCLUSION: no framework geometry in the corpus produces 1 ↦ q₀; the deformation is an input (forever-gate-consistent). Remaining plan steps 3–5. PR #7088.



2026-09-07 CORRECTION (qou-99qc review on #7088): q² = e^{iπħ} is conditional on Skein normalisation (H) — under (J) the ratio is −q and ħ halves; and the level mapping is k+2 = 15.05 i / 30.1 i / 60.2 i for ħ = 1/(k+2), 2/(k+2), 4/(k+2) (the earlier '60.2 i ↔ 2/(k+2), 30.1 i ↔ 1/(k+2)' was off by two; the probe's numbers were right). Fixed in KZLevelFromHeckeNormalisation.lean, the kz_pullback probe and audit §B′.



2026-09-13 claimed (branch claude/d0qq-twisted-period-eigenvalue-2026-09-13): §C step 4 of docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md — Lean QOU/Mass/TwistedPeriodEigenvalueRatio.lean: for μ : ℂ, exp(2πiμ) = −q² with real q > 1 forces Im μ = −ln q/π ≠ 0 (the twist exponent is never real: no real-exponent twisted period gives the Hecke ratio), and the pseudo-reflection pair {1, e^{2πiμ}} rescales to {q, −q⁻¹}. Then §C step 5 (prose rewrite of hecke-monodromy-step-two §What remains conjectural) if time allows. Kohno/Drinfeld ingestion (§B step 6) stays on qou-denm.



### 2026-09-13 RESULT — §C step 4 landed: the twist exponent is never real (Lean, sorry-free)

QOU/Mass/TwistedPeriodEigenvalueRatio.lean, lean-direct exit 0, axioms propext/Classical.choice/Quot.sound. norm_exp_two_pi_I_mul: ‖e^{2πiμ}‖ = e^{−2π Im μ}. im_eq_of_exp_eq_neg_sq: e^{2πiμ} = −q², real q > 0 ⇒ Im μ = −ln q/π — the exponent's imaginary part IS the level (same ln q as ħ = (2/iπ) ln q). im_ne_zero_of_exp_eq_neg_sq / not_exp_eq_neg_sq_of_im_eq_zero: for q > 1, Im μ ≠ 0 — no twisted period with a REAL exponent (unitary, rational, root-of-unity twist) gives the Hecke ratio; scope-(b), invariant = modulus of the monodromy eigenvalue. rescaled_pair: {1, e^{2πiμ}} rescaled to product −1 is {±q, ∓q⁻¹} via KZLevelFromHeckeNormalisation.eigen_sq_of_product_ratio. NOT established: that the substrate connection is a twisted period, or any derivation of μ (q₀ is an input under the forever-gate; §C step 2 measured zero twist from the framework's own connection). Next: §C step 5 (prose rewrite of hecke-monodromy-step-two §What remains conjectural, render-QA) — separate PR.



### 2026-09-13 — §C step 5 landed on the same PR (#7277): the twisted-period route is written into the conjecture block

conj:hecke-monodromy-step-two §'What remains conjectural' now carries the second route and its negative: A^0 = X dz (the Seiberg-Witten differential, the framework's one candidate connection on this family) supplies NO twist (push-down exact by Vieta, every lasso holonomy 1; colour_cubic_abelian_twist_holonomy_probe 8/8, 1e-30 at 50 dps); untwisted Gauss-Manin is quasi-unipotent so never has a real eigenvalue > 1 (UntwistedMonodromyPrune); what survives is a TWISTED period whose exponent is forced non-real by step 4 (TwistedPeriodEigenvalueRatio). The exponent is where q0 enters, as an INPUT. The existing KZ paragraph was EXTENDED, not replaced -- KZPullbackGenerators is a separate landed route and both constructions stay open. Render-QA: grep battery clean; expository pass removed a k-for-level vs k-for-order collision with the preceding paragraph. qa-sweep on the block: 99 criteria, 0 findings; the 10 residual stale criteria were already stale at HEAD. REMAINING on this bean: §B step 6 / qou-denm (ingest Kohno 1987 + Drinfeld 1985 -- cited in this block's cites[] but NOT held in library/, so path 5 cannot verify any 'Kohno-Drinfeld gives...' sentence), and the construction itself on either route. Bean stays OPEN.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-10-10 — now also gates the continuous mass identity (qou-ywyq)
The discrete mass identity tr_M(β) = (1+q²)^{-n}·Tr(K^{⊗n}·Hol(β)) is proved (QOU.Torsion.MassTraceMarkov, PR #7632). Promoting Hol to a continuous KZ holonomy at the real pin q₀ needs the imaginary level this bean studies; the real-level route is pruned (qou-74ip). Cross-link only; no new work done here.

## 2026-10-11 — Drinfeld–Kohno holds at the real pin; what remains is the framework connection
Kohno 1987 Remark 1.3.14 (library/kohno1987-aif, p.150): Theorem 1.2.8 holds at any complex coupling λ for which the R-side images φ(γ_k), γ_k=(σ1…σ_{k−1})^k, are diagonalizable, which holds when φ is completely reducible. At real q0>1 (not a root of unity) the U_q(sl2) tensor powers are semisimple and γ_k acts by ribbon scalars, so the theorem holds at the imaginary coupling λ0 = ln q0/(iπ) ≈ −0.0332i. The weight-preserving intertwiner argument (PR #7632) needs only q not a root of unity, so the weighted trace Tr(K^{⊗n}·) transports there too. Numerical check computations/kz_real_q0_pure_braid_monodromy_probe.py (mpmath 40 dps, n=3, pure braids incl. products): per-weight-sector traces agree to 1e-15, residual ∝ h^4, wrong orientation q→1/q fails by 0.70. Branch claude/kz-real-q0-2026-10-11. Cited, not proved in Lean. STILL OPEN (do not close): whether the framework's substrate connection IS this KZ connection (KZPullbackGenerators), and n>3 / full braid group only by citation.

2026-10-11: (a) Framework-connection check: as the corpus stands its connection is not the KZ connection. QFlatConnection is := trivial in its content sibling, and the library structure's flatness is an optional Prop-valued field (not an obligation) beside a tautological total_curvature equation. The Hecke 'curvature' F(σ)=σ²−(q−q⁻¹)σ−1 is a hypothesis class (QOU.Mass.HeckeMonodromy), stipulated, not computed from a connection form. A⁰ = X dz is rank 1, has zero residues and trivial holonomy. (b) Added def:kz-connection-sl2 (mass-endomorphism/kz-connection-sl2.lean), whose flatness is the infinitesimal pure braid relations, proved sorry-free, with a non-flat example. (c) The EMVZ route to sl2 at any ℏ∉ℚ is in docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md (our adaptation, unrefereed; 3 checks owed). The open question here is unchanged: whether the substrate connection IS this one.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

- **Round 56 Progress (`2026-11-16T21:20:58Z`)**: Opened [`litlfred/qou#8207`](https://github.com/litlfred/qou/pull/8207) (`cfc03c4131df1ea758c17554768f2274e708f38b`, Commit 1 `0a9d3f269d6c23f614dc40aac55d5f0a7b2baafd`). Keeping bean at `status: in-progress` pending owner review.
