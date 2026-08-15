---
# qou-a3n3
title: 'EPIC: Gevrey persistence — does the internal q-NS dynamics keep smooth data Gevrey as q→1⁺'
status: completed
type: milestone
priority: normal
created_at: 2026-07-25T03:32:00Z
updated_at: 2026-07-25T17:42:46Z
---

GP1 landed (PR #4193): discrete Gronwall + finite-rate horizon persistence. Epic stays OPEN — next bricks: GP2 rate improvement (does the q-damping [k]_q dissipation term cut Λ_q from ε⁻¹ to finite effective G — the analytic core), GP3 radius non-collapse (track the Gevrey radius r(t) itself, not just Ω).

GP1+GP2+GP3 all landed on PR #4193 (12 sorry-free theorems). Epic's tractable tranche COMPLETE: local persistence proved ε-free (bootstrap horizon ~1/(cΩ₀)); high modes damped (q-threshold); low modes bounded (quadratic bootstrap). Honest remainder = GLOBAL persistence past the bootstrap horizon at the finite-dim low-mode block (the classical local-vs-global gap, reproduced in-QOU). Epic stays open on that single named item.

SF1 landed: unforced DN q-shell (k_n=[n]_q) shows a TRANSITION — eps≥1e-3 decays, eps=1e-4 sustains 30 turnovers (Om_max/Om0~3.9 transient). Confound flagged (viscous time >> horizon at small eps). Next bean: SF2 discriminator — horizon scaled to viscous time + classical same-nu comparison; that decides whether the sustained channel truly activates as eps→0.

SF2 DISCRIMINATOR DECIDED: at T=1.5·t_visc the q-system tracks the classical same-ν control (R=0.565/0.947/0.995 for eps=1e-1/2/3, →1 as eps→0). SF1's small-eps sustainment was the viscous timescale, NOT q-self-forcing. The unforced finite core decays at every eps on its own clock ⇒ the sustained-forcing blow-up channel requires EXTERNAL or infinite-dimensional sustainment. Hard core sharpened again: no finite unforced structure in the program blows up, in-model. Remaining: infinite-dim sustainment analysis / PDE-uniformity / large-data global.

SF3 DECIDED: N-sweep (8..24) at eps=1e-2 — survival S_q DECREASES monotonically with N (1.35e-8→1.14e-9), R(N)~0.9. The infinite-dimensional escape does NOT open at the shell-model level; unforced decay is N-uniform (improves with N). In-model conclusion: the ONLY route to the sustained channel is EXTERNAL FORCING — but the Clay problem is unforced, so in-model the program now points to global regularity for all unforced channels examined. Remaining honest gaps: shell-model fidelity (DN is a caricature of full NS transfer — no backscatter/nonlocal interactions), PDE-uniformity, large-data global proof.

## 2026-08-14: millennium-core opening brick (low_mode_block_global.lean)

Large-data global persistence AT THE FIXED BLOCK is now proved
(no smallness hypothesis): energy monotonicity + finite-block norm
equivalence give Omega_n <= kmax^2 * E_0 forever; plus the discrete
Leray inequality delta*nu*sum Omega_i <= E_0. The honest millennium
remainder is sharpened to: UNIFORMITY of these bounds as the block
widens (kmax = [m]_{1+eps}, m ~ 1/eps) into the classical limit —
the flux through the receding damping threshold. Nothing resolves that;
it is the epic's remaining open item, now precisely localized.

## 2026-08-14: eps-uniformity reduction (low_mode_block_uniformity.lean)

The millennium remainder is now ONE named spectral hypothesis:
"no enstrophy pile-up at the receding damping threshold" — the
above-fixed-band tail enstrophy Omega_{>B} uniformly bounded in eps.
Proved: split Omega <= kB^2*E + tail (banded half eps-uniform);
trivial converse (equivalence). Also proved: leray_bound_scaling —
nu_q = eps/(2(1+eps)) makes the in-QOU classical limit a
VANISHING-VISCOSITY limit (Leray control degrades ~1/eps); mapping to
the fixed-nu millennium formulation needs an explicit
substrate-to-physical rescaling (owner flag). Candidate SF5 probe:
measure the above-fixed-band enstrophy fraction as eps -> 0 in the
shell models.

## 2026-08-14: SF5 pile-up probe DECIDED — and the answer is unit-dependent

Substrate units: pile-up REAL (sup tail ~ (1/eps)^0.83 asymptotic,
fraction -> 0.99) — the Euler-type limit fills the receding dissipation
range; scope-(a) refutation of the substrate-unit tail hypothesis.
c_q-rescaled (fixed-nu) units: tail VANISHES (~eps^1.17) — the
fixed-nu-unit hypothesis HOLDS in-model. The two normalizations give
OPPOSITE answers: the rescaling decision (audit
2026-08-14-qns-model-to-pde-uniformity-decomposition.md §5, owner
brief A/B/C) is now LOAD-BEARING for the millennium framing. Epic
blocks on that owner call.

## 2026-08-14: physical-layer Leray UNIFORM (physical_layer_leray.lean)

nu_phys = 1/(2q) >= 1/4 for q <= 2, so the discrete Leray control is
eps-UNIFORM in the physical layer: (delta/4)*sum Omega_phys <= E0 and
the same for any above-band tail — the TIME-AVERAGED no-pile-up bound
is PROVED. Remainder in the physical layer now has exactly the
classical shape: energy uniform + Leray uniform + sup-in-time OPEN
(= the classical weak-vs-strong gap, discrete/graded image). That
sup-in-time bound is the epic's single remaining analytic item.

## 2026-08-15: eventual regularity FULLY COMPOSED — no unproved link

quadratic_basin_invariant (GP4's mechanism, layer-agnostic algebra) +
eventual_regularity_quadratic: Leray hypotheses + damped quadratic
step => enstrophy enters and stays in the d/c basin after an
eps-uniform entry time. The chain energy -> Leray -> epochs ->
eventual regularity now has NO unproved hypothesis. The epic's sole
remaining open item: sup-in-time behaviour INSIDE the eps-uniform
initial window [0, 4E0/(delta*theta*)] — the classical weak-vs-strong
gap at its narrowest in-QOU form.

## 2026-08-15 (2): initial window closed for ENERGY-SMALL data

bad_count_le + sup_bound_of_chaining: epochs bad-count + GP3-shaped
bootstrap hypothesis + Nbad+1 <= H (arithmetically ~ 8cE0 <~ 1, an
ENERGY-smallness condition, eps-uniform) => sup_n Omega_n <= 2*lam
EVERYWHERE — latest-good-step pigeonhole, no induction. Extends the
global class from GP4's enstrophy-small basin to energy-small data.
Honest boundary named in the docstring: in-model c is fixed; classical
supercriticality lives in c growing with resolution. Remaining open
core: large data 8cE0 > 1 inside the initial window + the exact-form
GP3 bootstrap instantiation (hboot hypothesis).

## 2026-08-15 (3): GP3 wired — energy_small_global, every link a theorem

quadratic_step_of_damped (damped => undamped step) +
hboot_of_local_bootstrap (GP3 applied to the shifted sequence from
each good step) + energy_small_global (full composition): Leray +
damped quadratic step + smallness arithmetic (4E0/delta <= Nbad*lam,
H*delta*c*lam <= 1/4, Nbad+1 <= H, i.e. ~8cE0 <~ 1) => Omega_n <=
2*lam for ALL n, eps-uniform. NO named hypothesis remains in the
chain — only the model's discrete dynamics and the smallness
arithmetic. THE open core of the epic, final form: large data
8cE0 > 1 inside the eps-uniform initial window of the physical layer.
