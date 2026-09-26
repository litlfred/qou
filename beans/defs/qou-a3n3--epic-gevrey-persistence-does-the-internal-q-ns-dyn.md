---
# qou-a3n3
title: 'EPIC: Gevrey persistence — does the internal q-NS dynamics keep smooth data Gevrey as q→1⁺'
status: in-progress
type: epic
priority: normal
created_at: 2026-07-25T03:32:00Z
updated_at: 2026-09-08T04:00:00Z
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

## 2026-08-15 (4): energy-drain route proved — and the core is INFRARED

energy_geometric_decay: discrete Poincare (g*E <= Omega, g = kmin^2)
turns the dissipation step into geometric decay E_n <= (1-delta*nu*g)^n E0.
Honest scaling: the physical-layer gap is kmin = eps (def:qns-unit-layers),
so the rate ~delta*eps^2/4 is eps-NON-uniform — entry into the
energy-small class diverges as q -> 1+. Correct discrete image of the
classical no-Poincare-on-unbounded-domain fact (the physical domain
grows like c_q). LOCALIZATION COMPLETE: UV side tamed (tail Leray,
epochs, chaining, all eps-uniform); the surviving large-data
obstruction is INFRARED — the continuum limit's vanishing spectral
gap. Open core, sharpest form: large data, eps-uniformly in time,
against a spectral gap closing like eps.

## 2026-08-15 (5): the damped-forced tail bound — the arc's synthesis

tail_damped_forced_bound: seen from above the fixed band, the tail is
a strongly damped system (rate nu*kB^2, eps-FREE — the band is fixed)
forced through a fixed boundary (amplitudes eps-uniformly controlled
by the banded bound). With ONE named hypothesis — boundary flux <= Phi
uniform — the invariant gives sup_t Omega_tail <= max(Omega_tail_0,
Phi/(nu*kB^2)) for ALL data, eps-uniform: the sup-in-time tail bound,
closed in-model conditional on Phi. The flux hypothesis carries ALL
remaining uncertainty: in-model it reduces to local shell transfer +
the band bound (follow-up algebra, not assumed); for full NS it is
EXACTLY the nonlocal-transfer caveat the SF arc named. One hypothesis,
one caveat, one place. Epic state: everything proved except (a) the
in-model Phi derivation (algebra follow-up) and (b) full-NS transfer
locality (the standing fidelity caveat = the honest research frontier).

## 2026-08-15 (6): Phi chip — constant-flux hypothesis discharged

sqrt_forced_to_damped_forced (AM-GM on squares, no sqrt — generic
field kept): the amplitude-form flux F*a(n) (the DN boundary coupling,
F band-controlled, kB2*a^2 <= Omega_tail) absorbs into half the
damping. boundary_flux_tail_bound composes with the invariant:
sup_t Omega_tail <= max(Omega_tail_0, F^2/(D^2*kB2)) — all data,
eps-uniform, explicit equilibrium. FINAL epic remainder: (a) the
amplitude-form step IS the DN tail evolution (model-specific,
probe-able); (b) full-NS transfer nonlocality (the standing caveat).
The Lean chain is otherwise complete end to end.

## 2026-08-15 (7): SF6 — the amplitude-form step is REFUTED for small eps

Honest negative, the arc's first: D_eff = (F*a - dOmt/dt)/Omt holds at
eps=1e-1 (min +14.8, 0 violations) but goes to -22/-23 at eps=1e-2 and
1e-3 during the cascade-front transient (t~0.32; 19% of steps at
1e-3): interior tail production beats dissipation + boundary
accounting. Scope (a): this step form, this band, alone. The
boundary_flux_tail_bound Lean theorem STANDS as a conditional; its
in-model instantiation via the naive single-amplitude form is refuted.
Epic honest state: the final link's instantiation is genuinely open —
the correct effective step must account interior cascade production
(candidate routes: front-following band; production-vs-dissipation
Grashof condition; time-integrated form only). Full-NS nonlocality
caveat unchanged.

## 2026-08-15 (8): Amplitude repair — SF6's failure was the aggregate, not the structure

The refutation dissolves at per-amplitude resolution: DN inflow to
rung n is only from below (k_n*u_{n-1}^2); the interior term
-k_{n+1}*u_n*u_{n+1} is NONPOSITIVE for nonnegative amplitudes. SF6
measured the enstrophy AGGREGATE Omega_tail, where the cascade-front
interior production shows up; the per-rung scalar has no such term.
Two new sorry-free theorems (physical_layer_leray.lean, bean
qou-2y1i): rung_equilibrium (tail_damped_forced_bound at one rung,
Phi = kn*P^2, D = nu*kn^2, equilibrium P^2/(nu*kn)) and
amplitude_ladder_collapse (beta j <= theta^j * beta 0 under the
dissipation-scale condition beta j <= theta*nu*kk j). eps-uniform
physical-layer reading: nu_phys >= 1/4, k_phys = q^n - 1 <= e-1.
Honest remainders: (a) trajectory-level sup composition across rungs
(bounds-level only so far); (b) the band-at-dissipation-scale
condition — probe-able, SF7 candidate; (c) full-NS nonlocality
(standing).

## 2026-08-15 (9): SF7 validates the repair; trajectory composition closes remainder (a)

SF7 (qns_dissipation_scale_probe, bean qou-qzh2): all 3 assertions
pass. (i) The dissipation-scale crossing B* exists at every eps once
the ladder reaches the physical dissipation scale (eps-scaled ladder,
cap 400 rungs). (ii) The crossing's physical wavenumber is bounded by
the Kolmogorov prediction 2^{3/4} eps^{1/4} and DECREASES with eps
(0.949 / 0.220 / 0.104 at 1e-1 / 1e-2 / 3e-3, ~eps^0.6) — the
condition gets EASIER toward the classical limit. (iii) The per-rung
trajectory equilibrium ratio r_n <= 1 on every excited empty-start
rung at every eps (max 0.901) — rung_equilibrium holds along actual
trajectories, empirically. Lean side (bean qou-9vk9):
trajectory_ladder_bounds (rung-by-rung induction upgrading trajectory
forcing to its uniform bound, then rung_equilibrium) +
trajectory_tail_collapse (compose with amplitude_ladder_collapse:
u n t <= theta^n * P) — sorry-free, closes remainder (a) AT THE MODEL
LEVEL. Remaining: full-NS transfer nonlocality (standing caveat) —
now the ONLY open link in the in-model chain. Witness float64 debt
beaned (qou-xwjs, joins the 4 sibling probe witnesses).

## 2026-08-15 (10): SF8 — the per-amplitude route survives second-neighbor nonlocality

The standing full-NS caveat attacked at probe + Lean level. SF8
(qns_nonlocal_transfer_probe): DN + energy-conserving second-neighbor
channel gamma (inflow gamma*k_n*u_{n-2}^2 paired with outflow
-gamma*k_{n+2}*u_n*u_{n+2}, exact telescoping — drift ~1e-5 inviscid).
3/3 assertions at gamma = 0.5 AND 1.0 (equal-strength, harsher than NS
triad decay): two-source trajectory equilibrium r_n <= 1 everywhere
(max 0.90); dissipation-scale crossing exists at every (gamma, eps)
and still decreases with eps (shifts up modestly with gamma:
0.22 -> 0.32 at 1e-2, still under the Kolmogorov bound). Lean (bean
qou-dxva, sorry-free): rung_equilibrium_two_source (Phi = kn*(P1^2 +
gamma*P2^2)); two_source_ladder_collapse (pair-maximum induction,
rate theta per pair); rungBound2 + trajectory_two_source_bounds (pair
induction on rungs — trajectory-level composition for the nonlocal
class too). Honest scope: this covers the SECOND-NEIGHBOR nonlocality
class; full NS triad structure (all k+p+q=0 interactions,
sweeping/backscatter of distant modes) remains the standing caveat —
now with evidence it is not fragile to the first nonlocal extension.

## 2026-08-15 (11): SF9 — the route survives ALL-PAIRS geometric nonlocality

The closest shell image of full NS triads: every pair (m,n) coupled
with weight lam^{n-m-1}, per-pair energy-conserving; the geometric
structure telescopes into O(N) recursions so no truncation anywhere.
3/3 assertions at lam = 0.5 AND 0.9 (10 rungs at >38% weight — far
more delocalized than NS): all-source equilibrium r_n <= 1 everywhere
(max 0.84 over 363 excited rungs at 3e-3); crossing exists and still
decreases with eps (0.27 at 3e-3 for lam=0.9). Lean (sorry-free):
rung_equilibrium_forced (arbitrary nonneg forcing — subsumes the P^2,
two-source, and geometric-sum instances); multi_source_ladder_uniform
(strong induction + sum_range_reflect + geom_sum_mul: uniform
theta-suppression under B <= theta*(1-lam)*nu*k_n). Honest remainders:
geometric-decay version of the all-pairs collapse (the pair-maximum
argument does not lift verbatim — follow-up); sweeping/phase
decorrelation — NOT representable in any real-amplitude shell model,
now the irreducible caveat of the whole SF arc.

## 2026-08-15 (12): SF10 — phases: route survives, naive comparison refuted

Complex Sabra q-shell (per-triad exact conservation derived and
Lean-free-verified in the docstring: c_{n+2} = a_n + b_{n+1}; first
draft had the c-sign wrong -> 133% drift, caught and fixed, both
recorded). POSITIVE: the modulus damped-forced form holds along
trajectories at every (seed, eps) — r_n <= 1 (max 0.957) with the
triangle forcing; B* exists everywhere, k_phys(B*) decreasing
(0.77/0.20/0.094) — the per-amplitude route (the
rung_equilibrium_forced instance, no new Lean needed) SURVIVES in the
phase-dynamical class. HONEST NEGATIVE: the coherence ratio
sup|u_n|(Sabra)/sup u_n(DN) > 1 at every (seed, eps) (~1.2-1.4x at
eps <= 1e-2; huge at 1e-1 where both tails are sub-dissipation) — the
naive "phases weaken the tail" hypothesis is REFUTED in this
cross-model comparison, scope (a). Named confound: Sabra triads
include inflow-from-above, so c_n mixes phase dynamics with
triad-structure difference. Follow-up beaned (qou-ougq): Sabra vs
phase-scrambled Sabra isolates the phase effect.

## 2026-08-15 (13): SF11 — decorrelation weakens; coherence is the worst case

The clean phase-only comparison (Sabra vs itself, hash-scrambled
phases, moduli untouched): s_n = sup|u_n|(scr)/sup|u_n|(coh) <= 0.25
at EVERY (cadence, eps) — full-cadence scrambling suppresses the tail
40-90x, partial (0.1 eddy) 4-7x. r_n <= 1 on scrambled runs too (the
triangle bound is phase-free, as predicted). Resolution of SF10's
confound: the cross-model amplification was TRIAD STRUCTURE, not
phase coherence; the coherent evolution is the in-model worst case,
so the SF arc's fully-coherent real-amplitude models are CONSERVATIVE
w.r.t. sweeping/decorrelation. Epic caveat state after SF8-SF11: the
irreducible remainder is SPATIAL ADVECTION (sweeping moves structures
in space — no shell model represents it), with in-model evidence that
both delocalized transfer AND phase decorrelation only ever weaken
the tail relative to the proved coherent bounds.

## 2026-08-15 (14): the arc is citable content

prop:qns-shell-tail-collapse (four clauses: equilibrium, trajectory
composition, geometric collapse, nonlocal stability; lean.ref ->
trajectory_tail_collapse library decl, six declarations listed) +
rem:qns-shell-tail-collapse-interpretation (eps-free physical-layer
reading, five probe witnesses, spatial-advection boundary). Wired
into sec:ns-approaches after def:qns-unit-layers. PR #5095.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.
