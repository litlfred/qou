---
# qou-wapd
title: beta_ew_delta_I_321_and_wedderburn labels a Plancherel-weighted sum a 'Markov trace' — it sends the identity to 11.139, not 1
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T12:23:07Z
updated_at: 2026-11-16T19:05:00Z
parent: qou-rtxm
---

## Finding, measured 2026-09-05 — `probes/beta_ew_weight_is_not_markov_probe.py` (4/4)

Follow-on from `qou-oots`. That bean's consumer audit named
`beta_ew_delta_I_321_and_wedderburn.py` as the ONE live non-harness file still
on the superseded `dim_q^2/[n]_q!` weight, and the obvious next step was to
migrate it to the now-canonical Molien. Reading it first turns up a PRIOR
question that makes the migration question moot for this file.

The file computes and labels a **'Wedderburn-weighted Markov trace'**:

    tr_M(beta_EW Delta_I) = SUM_lam w_lam chi^lam,   w_lam = dim_q^2/[n]_q!

The canonical Frobenius pairing of this framework is `tr_M = SUM_lam y_lam
chi_lam` with the **Ocneanu/Markov** weights. Those are different objects, and
the difference is not a convention.

**THE DECISIVE MEASUREMENT: a Markov trace is NORMALISED, tr_M(1) = 1.**
Evaluating both weightings at the identity braid (chi^lam(1) = f^lam), n = 6,
q0, 50 dps:

    SUM_lam y_lam       chi^lam(1) = 1.000000000000000000...   <- a Markov trace
    SUM_lam (d_q^2/[n]_q!) chi^lam(1) = 11.13944754035206007   <- not one

So the object the file calls `tr_M` does not send the identity to 1. That is a
fact about the object, independent of any convention choice.

**THEY DO NOT EVEN HAVE THE SAME SUPPORT.** At n = 6, `y_lam` is **exactly
zero on 7 of the 11 partitions** — every lambda with more than 2 rows, the
SU(2) row cap — while the consumer's weight is nonzero on all 11. No
lambda-independent rescaling relates a weight that vanishes where another is
positive, so this is not two normalisations of one sum; the sums run over
different index sets.

**THE CONSEQUENCES ARE NOT CONFINED TO THE LABEL.** All six of the file's
cot(theta_W) candidates are ratios of w-weighted quantities at fixed n = 6, so
a lambda-INDEPENDENT reweighting would cancel from every one. Measured, the
ratio y/w over the shared support alone spreads **234x**, and that excludes the
7 partitions where y vanishes. So the six reported candidates are not invariant
under using the weight the name claims.

**AND IT IS NOT A q-DEFORMATION EFFECT.** The notation register says the three
partition-weight families coincide at q = 1. Control at q = 1 + 1e-25: y_lam is
**still zero on the same 7 partitions**, and the shared-support spread is still
**189**. The support difference is the row cap — a statement about N — and it
survives the classical limit. A reader taking 'the families coincide at q = 1'
to cover y_lam at N = 2 would be wrong.

### What is NOT established

Which weight this file's physics actually wants. That is a question about what
`beta_EW Delta_I` is a trace OF, and this probe does not touch it. Three
readings are open and they are not equivalent: (a) it wants the Markov trace,
and the weight is simply wrong; (b) it wants a Plancherel-weighted spectral
aggregate and only the NAME 'Markov trace' is wrong; (c) it wants something
else again. Under (b) the qou-oots migration to Molien applies and the six
candidates move; under (a) they are replaced entirely.

**Not fixed here, deliberately** — picking among (a)/(b)/(c) changes a
physics-facing cot(theta_W) search and is not mine to decide from the naming
alone.


## Corpus-grep found the corpus had ALREADY ADJUDICATED this (same day, later)

My (a)/(b)/(c) framing is SUPERSEDED.
`appendix-standard-model/sm-params-gauge-couplings.md` already rules that the
(3,2,1) block 'carries no states' at N=2 and that 'every route from such a block
to a physical number is either a Markov trace, which the row cap sends to zero,
or a spectrum, which has no states to act on'. It also states the resulting
cot(theta_W) ~ 1.8208 'must not be cited as a framework accuracy result' — its
witness records the ansatz as neither supported at 1e-3 nor falsified at 1e-2,
and the residual factor was selected as the closest of **74** candidates.

So the question was never which weight; it is whether the block is in the
carrier. **The Molien migration is moot for these files and was NOT done** —
migrating would move a physics-facing number inside a construction the paper has
already placed outside the carrier.

## Done

Documentation only, no production number moves:
- both consumer files carry a docstring note (not a Markov trace; block
  unoccupied at N=2; deliberately not migrated; what stays open);
- user-visible labels no longer say 'Markov trace';
- audit doc `docs/audits/2026-09-05-beta-ew-321-weight-and-the-row-cap.md`.

## Spun out

`qou-yk03` — the N=3 second-trace route, with its first measurement attached.

## A DEFECT IN MY OWN qou-oots AUDIT, found by this work

`w_lambda_family_consumer_audit.py` reported the Molien blast radius as
**4 of 36**. It is at least **5**. `close_321_weinberg_gap.py` builds
`w_lam = d_q_lam ** 2 / fact_n` — the identical superseded weight — and my
classifier filed it **NAME-ONLY** ('token present, no construction') because the
pattern expected `dim_q**2` and the variable is named `d_q_lam`; the `_lam`
suffix defeated the match. NAME-ONLY is a LOWER BOUND on 'computes no weight',
exactly as that audit's own limits section says, and this is the first measured
instance. Do not quote the 4; re-derive it.

## RE-DERIVED 2026-09-05 (PR #6840): it is 11 of 37, and 'at least 5' was far
## too generous

Measured with a detector keyed on PROVENANCE — what each operand was assigned
FROM — rather than on the local variable's spelling. SEVEN files build
`dim_q(...)^2 / q_factorial(...)` and NONE was visible to the regex:

    dim_q_num(...)  ** 2   call: '(' stops \w*
    q_dimension(...)** 2   word order — no 'dim_q' substring at all
    _q_dimension(...)**2   word order + leading underscore
    d_q_lam         ** 2   suffix after d_q — the instance found above
    dq[l]           ** 2   subscript between the name and **
    d               ** 2   single-letter local, from dim_q_via_hooks
    dim_q(part)     ** 2   a CALL to dim_q itself

The last is the actual defect and it reframes the diagnosis above. `dim_?q\w*`
cannot cross a '(', so the pattern could only ever match a VARIABLE named dim_q,
never a CALL to the function it is named after — the ordinary spelling, not an
exotic alias. So '_lam suffix' is right about its own instance and WRONG as a
characterisation: the detector was not too narrow, it was looking at the wrong
syntactic category.

THREE OF THE SEVEN ARE ON THE alpha_EM AXIS (alpha_5_jucys_murphy_central,
alpha_em_b2_scalar_c_probe, alpha_em_b2_canonical_scale_ratio_probe) — hidden
entirely by the 4-of-36 figure. NOT triaged whether Molien moves a
physics-facing number there.

Also fixed: the evidence field was sorted(...)[:8] and `q_factorial` sorts NINTH
in its own provenance set, so the witness recorded a provenance list not
containing the name that decided the match — a true positive reading as a false
one.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Row-Capped Ocneanu/Markov vs Uncapped Plancherel Obstruction in Lean (PR #8157)
- Formalized `row_capped_contribution_vanishes`, `no_uniform_rescale_between_uncapped_and_row_capped`, and the concrete `n = 6, λ = (3,2,1)` witness `n6_partition_321_row_cap_obstruction` (`ℓ(3,2,1) = 3 > 2`, `f^{(3,2,1)} = 16`, `(f^{(3,2,1)})² = 256 ≠ 0`, full Burnside sum `720 = 6!`, `ℓ(λ) ≤ 2` row-capped sum `132`, killed `ℓ(λ) ≥ 3` sector `588`) in `folio/quantum-observable-universe/lean/QOU/Foundations/FrobeniusHopfMarkovBridge.lean` (wired into `QOU.lean`, 0 `sorry`, generic `CommRingOps R` per §7c).
- PR: https://github.com/litlfred/qou/pull/8157 (commit `16f8c01498462170d1ad98f5b5426233d3feea7d`). Status kept `in-progress`.
