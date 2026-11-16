---
# qou-c6gx
title: '2H: nucleon-nucleon interface is 2-dimensional -- B floor is alpha*ln(1/z) = 2.907 MeV, ABOVE AME 2.2246'
status: in-progress
pr: 8219
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T22:20:37Z
updated_at: 2026-10-04T15:16:03Z
parent: qou-v2om
---

Branch: claude/anchor-followups-2026-08-08. Localises the 2H +74.85% overshoot,
and shows it is NOT reachable by any choice inside the interface sector.

## The interface collapses to one scalar

σ₂ is the ONLY generator joining strand 2 (proton's 3rd quark) to strand 3
(neutron's 1st), so "the inter-nucleon sector" is literally the word at gen 2.
That subalgebra is 2-dimensional — σ² = h·σ + 1 gives span{1, σ₂} — so ANY word
there, of any length, is a·σ₂ + b·I. Combined with the Markov property
tr_M(W·σ₂) = z·tr_M(W), every interface element gives

    tr_atom = tr_free · (a·z + b)        B = −α·ln(a·z + b)

Verified against the transfer kernel at all four whitelisted crossings,
residual 4.489e-32 (uniform — the shared tr_free floor, not a per-case error).

## Consequence: the three bond constants are closed-form, and L_pp is exact

    L_XY = −ln(z + d_XY),   z = 1/(√q₀ + 1/√q₀) = 0.4993203341836944524

  σ      (pp)  d = 0                 μ = 0.499320334  L = 0.694507437  B = 2.907195
  cw     (pn)  d = −h(½ − δ/4)       μ = 0.394862086  L = 0.929218723  B = 3.889692
  avg    (pn)  d = −h/2              μ = 0.394790185  L = 0.929400833  B = 3.890455
  σ⁻¹    (nn)  d = −h                μ = 0.290260035  L = 1.236978084  B = 5.177967

L_pp = ln(1/z) EXACTLY (0.69450743692190434592) — derived, not fitted.

## The hard result: AME is below the model's floor

B over the ENTIRE admissible interface family spans [2.907195, 5.177967] MeV.
AME(2H) = 2.2245662 is **30.69% BELOW the minimum**. So no crossing sign, no
colour weight, no crossing multiplicity, and no stacking can reach the deuteron.
Stacking is worse than useless: m=2 gives μ = 1.1044 → B = −0.416 MeV.

Required μ = 0.587762445 ⇒ d = +0.088442110 = +0.42304594·h — POSITIVE, outside
the Hecke range d ∈ [−h, 0].

## Attack vectors ruled OUT (each measured, not argued)

1. tr_free missing a term / double count — NO. tr_free = tr_p·tr_n exact to
   2.417e-30, and every normalisation that could differ (the HOMFLY
   ((1−λq)/(√λ(1−q)))^(n−1) prefactor, the split-link loop factor) cancels in
   the ratio because free and atom are both n = 6.
2. Dropped writhe/framing — REAL but negligible. The Lean-derived normalisation
   Ŝ = S·(1−h)^((e−n)/2) (QOU.QBeta.WritheNormalisation.writhe_factor_sq,
   sorry-free) applies, but e_atom − e_free = 6.879e-4 because the p–n crossing
   sits at t ≈ 0.4997, i.e. essentially zero net writhe. Correction: 3.2e-4 MeV.
   Should still be wired in for rigour; it is not the error.
3. Colour weight vs colour blind — 0.00076 MeV apart. Cannot matter at 1.665 MeV.
4. SDP weights — NOT USED in the pairing at all (see below).

## Two structural constraints that FORBID adding knot content

- `chi_monotone_transfer.word_to_mpfr` requires a MONOTONE word (generator
  indices non-decreasing). Conjugated interfaces (σ₁σ₂σ₁⁻¹ to reach strands
  1↔3, σ₂σ₃σ₂⁻¹ for 2↔4) are rejected outright.
- The same function WHITELISTS exactly four crossings (σ / σ⁻¹ / averaged /
  colour-weighted p-n) and raises on anything else.

So the framework braids one quark pair out of the 3×3 available, and the fast
path cannot express any other choice. Accounting for "all knot operations"
requires leaving gen 2, which the kernel currently forbids.

## Correction to the record

The chain summary in AGENTS.md is right (pairing THEN SDP). But
`docs/audits/2026-05-25-vol-density-derivation-error-localization-and-klr-path.md:41`
says "y_λ(atom) are SDP shadow-prices from the confinement constraint" — that
describes the proposed KLR path, not the shipped code. Shipped: y_λ comes from
`wedderburn_jones_markov.y_lambda_at(n, q₀)`, the closed-form Jones–Markov
hook-length weight, a function of q₀ alone. The SDP dual `y_star` lives in a
different script family (`aK_via_lp_dual*`, `pn_alpha_lp_dual`) and never
reaches `tr_m_atom_zn`. Worth a note on that audit doc so the next reader does
not repeat the inference.

Also: the pp bond is qualitatively wrong independently of 2H. The framework
binds EVERY pp pair at exactly α·ln(1/z) = 2.907 MeV; in nature the diproton is
unbound. The floor problem is systematic, not deuteron-specific.

## Next

The deficit is a property of α and z, not of the braid. Two candidates, both
testable without touching the trace:
  (a) α is the wrong scale for the interface (α* = 3.2031 MeV, ratio 0.76519,
      would land pure-σ on AME — currently a fit, needs a derivation);
  (b) B is not −α·ln μ; the map from interface scalar to energy is the defect,
      matching the determinant form failing −58% from the other side.
Check the A-scaling first: with B = −α·Σ_bonds ln μ_k the model is exactly
additive per bond, so compare the required per-bond correction at 3H/3He/4He
against 2H's. If it is constant per bond, (a); if it scales, (b).

## A-scaling: BOTH candidates above are now REFUTED

Ran it. Under B = −α·Σ_bonds ln μ_k the model is exactly additive, so the
deficit's A-dependence discriminates. It does — decisively, against both.

Chain topology (what `atom_braid_word_3A` actually builds, A−1 bonds):

    atom  nb   B_pred    B_AME    err %    per-bond deficit   B/AME
    2H     1   3.8897    2.2246   +74.85      +1.6651         1.7485
    3H     2   9.0677    8.4818    +6.91      +0.2929         1.0691
    3He    2   6.7969    7.7180   −11.94      −0.4606         0.8806
    4He    3  11.9749   28.2957   −57.68      −5.4403         0.4232
    6Li    5  20.0600   31.9946   −37.30      −2.3869         0.6270
    7Li    6  25.2380   39.2445   −35.69      −2.3344         0.6431

The per-bond deficit CHANGES SIGN, spread 7.105 MeV/bond. Full pairing
(A(A−1)/2 bonds) also changes sign, spread 3.024. So (a) is dead: no rescaling
of α can fix a residual that is positive at A=2 and negative at A=4. Best-fit α
leaves a 178% worst residual under chain, 56.5% under full pairing — quoted only
to kill the hypothesis, NOT as a proposal.

Neither topology works either: chain has 4He at 0.42×, full pairing fixes 4He
(0.84×) but blows 6Li/7Li to 1.85×/2.20×. Small A wants fewer bonds than full
pairing, 4He wants more than chain. That is saturation plus an α-particle
enhancement, and a per-bond additive log-trace model cannot produce either.

## WORSE: the bond multiset is not well defined

`atom_braid_word_3A` hard-codes `ordering = ['p']*Z + ['n']*N`. B depends on it:

    atom   canonical   B_canon    B_min     B_max    spread   B_AME
    3He    ppn          6.7969    6.7969    7.7794   0.9825   7.7180
    4He    ppnn        11.9749   10.6866   12.9574   2.2708  28.2957
    6Li    pppnnn      20.0600   18.4660   21.0425   2.5766  31.9946
    7Li    pppnnnn     25.2380   23.3382   26.2205   2.8823  39.2445

A nucleus has no ordering — so up to 2.88 MeV here is a non-physical degree of
freedom, and the chain bond-multiset is a CHOICE, not a derivation. The
convention is not even the good choice: `3He = pnp` gives 7.7794 (+0.79% of AME)
where canonical `ppn` gives −11.9%. The mirror pair is decided by it outright:
`pnn`/`ppn` splits 2.271 MeV, `npn`/`pnp` splits EXACTLY 0 (nature 0.764).
(2H and 3H show a nonzero best/canonical difference only as a tie — reversal
gives the same multiset and the same B.)

Recorded as a correction on bean qou-h7mh, whose "bond ENERGIES are right, the
deuteron is exact" premise was measured under the since-removed Reeb override
and is now false.

## Lean status of the assertions here — NOT proved

Asked and checked, rather than assumed:

  * `σ² = h·σ + 1` (Hecke quadratic) — a STRUCTURE FIELD (`quadratic`) in
    `knot-eigenbasis-complete.lean:88`, i.e. a hypothesis, not a theorem.
  * Markov property `tr(x·T_last) = z·tr x` — a structure field
    (`markov_stab`, same file:246) and, in `jones-markov-trace.lean`, an
    `axiom jones_markov_trace_exists` carrying the file's single `sorry`,
    explicitly marking where Jones (1987) would go.
  * Writhe normalisation `Ŝ = S·(1−h)^((e−n)/2)`, `A² = 1−h` —
    `QOU/QBeta/WritheNormalisation.lean`, **0 sorries, 0 axioms**: genuinely
    proved. It is also the one piece measured to be negligible (3.2e-4 MeV).

So the closed form is conditional on an axiomatised Markov trace. That is
standard practice (Jones is a real published theorem) but "Lean proved" is the
wrong label for it, and the only fully proved ingredient is the one that does
not matter.

Repro (read-only, writes no witness):
  /tmp/.../scratchpad/interface_closed_form.py
  /tmp/.../scratchpad/attack_2h.py
  /tmp/.../scratchpad/a_scaling.py
  /tmp/.../scratchpad/ordering_dep.py


## Progress Update (PR #8219)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`ThermodynamicTemperatureAndRepinBound.lean`, `SiteVsBondVolumeFactorTwo.lean`, `TwoDimensionalInterfaceCollapseAndOrdering.lean`, `WritheSignOppositionEndpointSplit.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` probe (`computations/probes/kt_repin_octahedron_interface_writhe_probe.py`) and stamped witness (`computations/probes/kt-repin-octahedron-interface-writhe-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8219 (`ready: 0004396c02a14ba756cc43c66855073b0a08f82d`)
