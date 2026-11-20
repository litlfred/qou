---
# qou-fv0s
title: 'GAP: canonical tr_M is colour-BLIND for every mixed nucleus — the sign wire format cannot carry R3'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T18:21:32Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---

## The canonical tr_M path structurally cannot honour owner ruling R3

Owner ruling 2026-08-15 (R3) makes `bring_color_weighted` the canonical p/n
convention. The canonical Markov-trace producer cannot apply it.

`canonical_braid_crossings.sign_for_ctype` says so in its own docstring:

  > ⚠ **Lossy for `averaged_weighted`, by construction.** A sign cannot carry a
  > magnitude, so both averaged interfaces collapse onto `0` — the colour-blind
  > projection. The p-n colour weighting `-h(1/2 - δ/4)` is *not* representable
  > in this format at all.

`canonical_tr_m_via_rust` wires the word to the Rust engine as signs in
{−1, 0, +1}. So **`averaged` and `averaged_weighted` both go over as 0**, and
every trace it returns is colour-blind.

## Where it bites — measured

Colour weighting is the **p–n interface** crossing: absent for a free nucleon,
exactly one per mixed nucleus.

| atom | ctypes | colour-weighted | canonical tr_M (colour-BLIND) |
|---|---|---|---|
| p | σ 6, σ⁻¹ 3, avg 2 | **0** | 1.14575969245730086935241774516176649113 |
| n | σ 5, σ⁻¹ 4, avg 2 | **0** | 0.98774368811580957144294046174148798302 |
| D | σ 11, σ⁻¹ 7, avg 4, **avg_w 1** | **1** | 0.57509087162981031565376396300046787027 |
| T | σ 16, σ⁻¹ 12, avg 6, **avg_w 1** | **1** | 0.22927766053968917795626336907991385602 |
| ³He | σ 23?, avg_w 1 | **1** | 0.40370991405397142157994463601783332536 |
| ⁴He | σ 23, σ⁻¹ 15, avg 8, **avg_w 1** | **1** | (still computing) |

**For p and n the colour-blind value is CORRECT** — a free nucleon has no p–n
interface, so there is nothing to weight. **For D and every heavier nucleus it
is not**: the one interface crossing that carries the proton-neutron colour
asymmetry is being sent over as the colour-blind `0`.

## Magnitude

δ (flavour split) = 0.001375710807027096, h = 0.20906029879563937:

    averaged           d = -h/2        = -0.10453014939781968
    averaged_weighted  d = -h(1/2-δ/4) = -0.10445824776972631
    relative difference                = 6.87855e-4

matching to the digit the `6.879e-4` that `classify_crossing`'s own comment
records. One such crossing per nucleus, so this is a ~7e-4-scale effect on one
of 23–47 crossings — **small, and not an explanation for the 42–85 % spread
among the six tr_M(p) values**. It is a correctness question, not a magnitude
one.

## `qou-gdtb` is marked COMPLETED while its own named residual is live

`sign_for_ctype`'s docstring ends: *"The representational gap itself stays open
under bean `qou-gdtb`."* That bean's status is **completed**. What it closed is
real — `classify_crossing` now returns the two labels distinctly, which is what
made this measurable — but the gap it names is demonstrably still there: the
sign format still collapses both onto 0, in code I read today.

So either the docstring is stale or the bean closed early. **The code is the
evidence**, and it says the gap is open.

## What is NOT claimed

That the Rust engine is wrong, or that the colour-blind numbers are wrong *as
colour-blind numbers*. The wire format is documented and deliberate. What is
missing is a path from `d_for_ctype` (which is exact, and carries the weighting)
to a canonical trace for mixed nuclei. Closing it means either widening the wire
format past a sign, or computing mixed-nucleus traces through the Python ctype
route instead — a design choice, not a patch.


## PRICED — 1.4149e-4 relative, and the corpus answers it both ways (2026-08-30, PR #6309)

The gap above was established but not measured. It is now measured, on the
deuteron at the proton pin, 50 dps.

**Method.** The trace is affine in the single shift the weighted crossing
carries: `tr M(d) = tr(A σ_g B) + d·tr(A B)`. Evaluating the Schur-Weyl sum at
three shift values (blind / weighted / midpoint) settles the whole effect; the
midpoint lands halfway to **1.8e-71**, the 50-dps floor, so the affine reading
is measured rather than assumed.

**1. The colour-blind arm is now CROSS-VALIDATED, not inferred.** An independent
Python route (Hoefsmit matrices + symbolic y_lambda) reproduces the canonical
Rust value to **1.909e-18** when the weighted crossing gets the *unweighted*
shift. Independent on both axes — Rust MPFR chi vs Python Hoefsmit, witness-table
y_lambda vs symbolic. So "canonical is colour-blind" no longer rests on reading
`sign_for_ctype`.

**2. Magnitude: 8.137e-5 absolute, 1.4149e-4 relative.** That is ~12000x the
mu-p substrate tension (11.54 ppb), and ~4.9x SMALLER than the per-crossing
weight difference 6.87855e-4 recorded above — the trace attenuates the
weighting, it does not amplify it.

**3. The committed witness is on the colour-WEIGHTED arm.**
`atomic-tr-m-mpfr-50dps.witness.json`'s deuteron entry is 1.48e-7 from the
weighted sum and 1.416e-4 from the blind one. (That 1.48e-7 is the q_0 pin
straddle `rho_k_h3a_residual_decomposition.py` already decomposes: 8.34e-8
straddle + 1.85e-9 witness self-inconsistency.)

**What that changes about this bean.** The design choice is NOT "build the
colour-weighted route or don't" — both routes are already in the tree, and the
corpus answers R3 both ways depending on which one a consumer takes. The choice
is which of the two is canonical, and it is worth 1.4e-4.

**Still open, and still not a patch:** whether the p-n interface should carry
the flavour weighting is a physical modelling question. The probe prices it; it
does not settle it.

**Scope-(a):** deuteron only. The linear coefficient tr(A B) is word-specific —
do NOT quote 1.41e-4 for T / 3He / 4He.

Probe: `computations/probes/colour_weighting_trace_magnitude_probe.py` (5/5).


## RETRACTED — the `qou-gdtb` section above is WRONG (2026-08-30, same day)

The section headed *"qou-gdtb IS MARKED COMPLETED WHILE ITS OWN NAMED RESIDUAL IS
LIVE"* is retracted. I read `sign_for_ctype`'s docstring — which ends *"The
representational gap itself stays open under bean qou-gdtb"* — saw that gdtb is
`completed`, and concluded the bean closed early. I did not read the bean. It is
closed, and closed CORRECTLY.

Two different encodings, and only one is lossy:

    pair form  (gen_idx, ctype)  -> d_for_ctype        EXACT (2.66e-16, f64 eps)
    sign wire  {-1, 0, +1}       -> both averaged -> 0  LOSSY, by construction

`qou-gdtb` item 1 was the PAIR form. It closed on a measurement plus a scope-(b)
exclusion with the invariant cited: `I = sigma_g - (h/2)*1` is of the form
`c*sigma_g + d*1` with d SCALAR, so the pair names the generator and
`d_for_ctype` supplies d — an algebraic identity, verified symbolically-exact
over all 11 partitions of 6, independent of lambda and of the representation.
Nothing about that is stale.

The gap the docstring describes is the SIGN wire — a different encoding — and it
is THIS bean, `qou-fv0s`. The docstring was pointing at the wrong bean, and I
followed the pointer instead of reading the target.

**Do NOT reopen `qou-gdtb`.** Three sites carried the wrong pointer
(`sign_for_ctype`, and two in `chi_via_rust_lossless`); all three retargeted to
`qou-fv0s` in PR #6309, each with a note saying why, so the next reader does not
correct it back.

The rest of the section above stands — what gdtb closed IS what made this
measurable, as it says.


## UNIVERSAL — one number, and my #6309 caveat is RETRACTED (2026-08-30, PR #6319)

The PRICED section above carries a scope-(a) caveat: *"the linear coefficient
tr(A B) is word-specific — do NOT quote 1.41e-4 for T / 3He / 4He."* **That is
wrong.** The coefficient is word-specific; the RATIO is not, and nothing in
#6309 tested it.

Measured across all four mixed nuclei — H_6, H_9, H_12:

    atom  H_n  contrib  maxdim     delta_rel    rust-vs-blind
    D       6        4       9   1.414947e-04      1.909e-18
    T       9        5      48   1.414947e-04      3.420e-18
    3He     9        5      48   1.414947e-04      3.290e-18
    4He    12        7     297   1.414947e-04      4.815e-18

**The identity.** Fitting k in `tr_M ∝ (d + k)` from each nucleus's own two arms
— nothing about the Markov parameter entering the fit — gives

    k = z_D = q^3/(q^2 + 1)      |k - z_D| ~ 1e-48, spread 1.3e-47

So `tr(A σ_g B) = z_D · tr(A B)`, the Markov stabilization factor, and

    Delta_rel = (d_w - d_blind)/(d_blind + z_D) = 1.414946610628e-4

nucleus-independent. Four different braid words agreeing on a constant never put
in.

**The mechanism, with a control.** The weighted generator occurs exactly once per
canonical word (D/T at gen 2, 3He/4He at gen 5). Tested by breaking it:

    canonical beta_D                    occ=1   k - z_D = 2.3e-48
    + one sigma on the SAME generator   occ=2   k - z_D = 1.2285   <- dies
    + one sigma on ANOTHER generator    occ=1   k - z_D = 1.1e-47  <- survives

Survives lengthening elsewhere, dies on reuse. So the once-only occurrence
carries it — not word length or content — and the four-way agreement is not an
artifact of these particular words.

**What this changes for the decision.** The choice is worth a SINGLE
nucleus-independent 1.414946610628e-4 on every mixed nucleus. It does not grow
with A and needs no per-isotope re-measurement. Still not settled here: which
arm is correct is a physical modelling question.

**Scope narrowed, not widened:** no claim for words where the interface
generator repeats — the control shows it fails there, and no canonical nucleus
has that shape.

## Implementation & Witness Progress (PR #8253)
- Branch: `qou-10v9-4e5k-742w-9bei-cblw-fv0s` (`52305a7a1e7f9836f16e0d5d8d454bd72705f9b1`), PR: `litlfred/qou#8253`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/deuteron_trace_discrepancy_m1_rho_constant_sdp_zero_threshold_pn_colour_factor_and_sign_wire_loss_probe.py` -> `computations/probes/deuteron-trace-discrepancy-m1-rho-constant-sdp-zero-threshold-pn-colour-factor-and-sign-wire-loss.witness.json` (`allPassed: true`, `scriptHash: ece5f27ee4a5`, `scriptCommitSha: 1c76aa0739f7803dab0155515577d8888a08fc68`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8253, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
