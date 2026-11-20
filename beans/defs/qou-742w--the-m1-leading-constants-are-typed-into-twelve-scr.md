---
# qou-742w
title: The M1 leading constants are typed into twelve scripts, not imported
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T06:28:48Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---

Found by the `qou-psjm` hand pass over the witness-copy audit. Full taxonomy:
`docs/audits/2026-09-06-witness-copy-hand-pass-taxonomy.md`.

## The defect

Twelve sibling scripts under `computations/deltalambda/wlambda_covariance_epic_M1_*`
each TYPE IN the same three constants, every one annotated "merged #5901":

    M_INF         = mp.mpf('0.300186614161')   # IO leading (CS) margin
    SIG_RATIO_INF = mp.mpf('0.679609581496')   # sigma_D/sigma_A limit
    RHO_INF       = mp.mpf('0.979796195657')   # IO leading rho_P

Twelve digits each, twelve copies, no shared module and no witness load. Re-run
#5901's producer and twelve scripts go stale simultaneously with nothing to
detect it. Highest-value single drain in the 232-finding queue; the fix is one
shared constants module.

The twelve: CA_to_margin_conversion, constant_C_landscape, debye_CA_investigation,
delta_ratio_structure, descent_dpp_variance_rate, finite_n_cs_margin,
ingredient_envelope_convergence, margin_envelope_exponent, margin_leg_decomposition,
naive_budget_closes_probe, pointwise_shortfall_recomputed, sigmaD_leg_rate.

## A second question, NOT for this bean to answer

`margin_leg_decomposition.py:45` annotates RHO_INF as `# = 2 sqrt(6)/5`. Measured
at dps 30:

    literal   0.979796195657
    2*sqrt(6)/5  0.97979589711327123928     rel 3.05e-07

They diverge at the 6th significant digit. Three distinct values near 0.9797 sit
in the corpus (0.9797938112..., 0.979796195657, 0.979798768510...) and NONE is
2*sqrt(6)/5.

Either reading changes what the fix should be:
  - conjectured closed form  -> carry the producer's full precision, not 12 digits
  - actual identity          -> compute 2*mp.sqrt(6)/5 exactly; the literal is lossy

That is the M1 epic's own call, not an infrastructure decision. Whoever owns
#5901 should settle it before the shared module fixes the spelling of a value
whose provenance is unresolved.

## Default if nobody acts

Nothing breaks today. The twelve stay in the witness-copy baseline as class-D
findings and the audit keeps reporting them. The risk is latent and realises only
when the M1 producer is next re-run.


---

## WORKED 2026-09-07 — consolidated, and the measurement changed the question

**The 'load it from a witness' fix was never available.** No producer in this
repository computes `rho_P`, the CS margin, or the sigma ratio; all three arrive
from merged PR #5901's IO computation. Measured: `grep -rl` over the three
literals returns 12 `.py` carriers and **zero** witnesses that emit them. So a
literal is the honest representation and the fix is one shared module carrying
the provenance, not a load. Anything that told the audit to expect a load here
would have been telling it to expect something that does not exist.

**Done:** `computations/deltalambda/_m1_io_constants.py`. 24 retyped sites across
12 scripts collapse to 2 literals plus 1 derived value (see Finding 1). Every consumer compiles and runs exit 0;
two probes' full stdout was captured before and after (`delta_ratio_structure`
byte-identical, `margin_leg_decomposition` differs in exactly one column — see
below).

### Finding 1 — the three constants are NOT independent

To all twelve recorded digits, in decimal:

    0.979796195657 - 0.679609581496 = 0.300186614161      exactly

That is the arc's own definition `m_inf = rho_inf - (sigma_D/sigma_A)_inf`. It
was typed as a third literal in seven scripts, which made an identity look like a
coincidence. `M_INF` is now **derived** in the module. Two consequences:

* There are **two** free numbers here, not three, so the drain is smaller than
  the bean claimed and the identity is now enforced rather than hoped for.
* `M_INF` carries **fewer** reliable digits than either input — it is a
  difference of two numbers sharing a leading digit, so it loses one to
  cancellation on top of whatever the extrapolation had.

### Finding 2 — the `2*sqrt(6)/5` question is UNDECIDABLE at the recorded precision

I drafted 'refuted at the recorded precision' and it was wrong. Squaring is the
cleaner statement:

    RHO_INF**2   = 0.96000058502393...
    24/25        = 0.96
    relative gap = 6.09e-07     (3.05e-07 on RHO_INF itself)

The literal agrees with the candidate through **six** significant digits and
departs at the seventh. That is not a refutation — it is the signature of a
6-7-digit extrapolation written out to 12. Corroborating evidence that these
*are* extrapolations: `wlambda_covariance_epic_M1_CA_to_margin_conversion.py:92`
— `# v_A by Richardson on the measured exponent; cross-check against exact
8/pi^2.`

**So the discriminator is convergence, not the digits on the page**, and the arc
has not established it. Until it does the identification must be written with
`approx`, never `=` (AGENTS.md section 7ab). The bare `= 2 sqrt(6)/5` annotation
that stood at `margin_leg_decomposition.py:45` is gone with the assignment it
sat on; the module records the arithmetic and the open question instead.

This closes the bean's 'second question' as **stated but not decided** — the
consolidation is correct under either answer, which is why it did not have to
wait on the M1 epic.

### The one output change, and why it is right

`margin_leg_decomposition` prints a leg-closure residual. It read exactly `0.0`
before and reads `3.9e-34` to `1.5e-33` now (it varies with n). **I first wrote in the module docstring that
deriving `M_INF` would make it exactly zero; measuring said otherwise and the
docstring is corrected.** The largest residual is ~130x BELOW that probe's own
dps-30 epsilon (1.97e-31) — quoting the worst case, not the best, and the exact `0.0` was an artifact: at dps 30 and 40 the
three decimals' binary roundings cancel identically, at dps 50 they leave one
ulp (1.34e-51). A closure column reading exactly zero for a rounding reason was
not testing the closure. The probe's own docstring claim ('closes to round-off
at every n') holds either way.

Cause: the module builds at `_DPS = 50` on purpose. Consumers set `mp.mp.dps` to
30 or 40 **after** their import block, so a module-level literal built at the
caller's ambient dps would silently be a **15-dps** value — the precision
downgrade this whole arc is auditing, reintroduced by the fix for it.

### Still open

Whether digits 7-12 of the #5901 extrapolation are converged. That is the M1
epic's call and it is a conjecture, so this bean stays open per AGENTS.md 13a.


---

## DECIDED 2026-09-07 — it IS 2*sqrt(6)/5, and my own "undecidable" verdict is superseded

Extending the ladder from theta=10240 to **theta=40960** drives the method error
below the gap and resolves the question. Same probe, same calibration, longer
ladder:

    theta=10240   method error 5.861e-7   ratio to gap 1.92x   UNDECIDABLE
    theta=20480   method error 1.189e-7
    theta=40960   method error 9.933e-8   ratio to gap 0.326x  RESOLVES

At theta=40960 the extrapolation lands at **0.9797958719839**:

    vs 2*sqrt(6)/5 = 0.9797958971133   ->  2.565e-8   INSIDE one method error (0.26x)
    vs recorded      0.979796195657    ->  3.303e-7   3.33x OUTSIDE it

One candidate sits comfortably inside the method's demonstrated error and the
other sits over three times outside it. **The closed form is supported; the
recorded 12-digit literal is wrong past roughly its sixth digit.**

So the annotation `# = 2 sqrt(6)/5` was RIGHT all along, and both of my earlier
readings were wrong in turn: first "refuted at the recorded precision" (wrong),
then "undecidable" (right for the ladder available at the time, superseded by a
longer one). The literal is the thing that was wrong, not the identification.

### The probe FAILED ON ITS OWN SUCCESS, and that is now fixed

Its third check asserted `method_error > gap` -- i.e. that the ladder CANNOT
decide. Correct while the arc's ladder was the only evidence; wrong the moment a
longer one resolved it, and the run exited 1 while printing the answer. **An
assertion that a question stays open is a prediction, not a check.** Replaced
with a determinacy check that passes in either regime and refuses the genuinely
bad middle case -- an error small enough to look decisive while the extrapolation
is ambiguous between the two. Verified on both ladders: short (undecidable) PASS,
long (decided) PASS.

### What this does NOT establish

The extrapolation supports the closed form; it does not PROVE it. `2*sqrt(6)/5 =
sqrt(24/25)` remains a numerically-supported identification, not a derivation.
Whatever makes `rho_inf^2 = 24/25` exact is still unexplained, and that is the
part worth having.

The decay-exponent spread WIDENED (2.302 vs 0.2589 pairwise, a 57x cost spread),
so the probe's forward cost projection is less reliable than before -- moot here,
since the question is answered, but do not quote that projection.

**Bean stays open** per AGENTS.md 13a: the identification is supported, the
derivation is not. What should close alongside it is the recorded literal --
`0.979796195657` should carry only the digits it has earned, or be replaced by
the closed form.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Implementation & Witness Progress (PR #8253)
- Branch: `qou-10v9-4e5k-742w-9bei-cblw-fv0s` (`52305a7a1e7f9836f16e0d5d8d454bd72705f9b1`), PR: `litlfred/qou#8253`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/DeuteronTraceDiscrepancyM1RhoConstantSdpZeroThresholdPnColourFactorAndSignWireLoss.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/deuteron_trace_discrepancy_m1_rho_constant_sdp_zero_threshold_pn_colour_factor_and_sign_wire_loss_probe.py` -> `computations/probes/deuteron-trace-discrepancy-m1-rho-constant-sdp-zero-threshold-pn-colour-factor-and-sign-wire-loss.witness.json` (`allPassed: true`, `scriptHash: ece5f27ee4a5`, `scriptCommitSha: 1c76aa0739f7803dab0155515577d8888a08fc68`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8253, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-07: "measure(qou-742w, qou-3f7a, qou-9ies): the closed form decided, a false positive that inverts a bean, and a check that c"). The work may be partly or fully done. Read the bean before you close it.
