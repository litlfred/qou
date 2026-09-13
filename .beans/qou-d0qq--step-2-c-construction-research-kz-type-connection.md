---
# qou-d0qq
title: 'Step-2 option C (research): the sl2 KZ connection on Conf3(C) pulled back along the colour cubic''s root map, at the level FIXED BY q0 (q0 is input; forever-gate) — does its monodromy reproduce the Hecke quadratic and z_D = q^3/(q^2+1)?'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T08:13:53Z
updated_at: 2026-09-07T18:13:25Z
parent: qou-2akx
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
