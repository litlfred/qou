---
# qou-s41x
title: 'oxygen-14 witness carries reconstruction_matches: false — pre-existing, undecided, two live readers'
status: todo
type: task
created_at: 2026-08-10T02:36:17Z
updated_at: 2026-08-10T02:36:17Z
---


## The finding

`computations/habiro-coefficients-oxygen-14.witness.json` carries

    reconstruction_matches: false
    n_nonzero:              34
    all_integral:           true

`reconstruction_matches` is the producer's own check that the extracted Habiro
coefficients rebuild the polynomial they came from: p(u) =? Σ a_m·(u;u)_m. It
says they do not.

## What is established, and what is not

**Established:** it is *not* a regression from the 2026-08-10 regeneration. Both
the committed (2026-06-29) and regenerated copies carry `false`, with identical
`n_nonzero` (34) and `all_integral` (true). Whatever it is, it predates the
sympify-locals fix and survived it unchanged.

**Also established:** the OTHER cross-check in the same witness now passes
*exactly*. `tr_M_at_q0` computed directly and `tr_M_at_q0_via_u_poly` computed
through the reconstructed u-polynomial agree to `rel_err = 0.0`. So the
reconstruction is good enough to reproduce tr_M at q₀ to full precision while
failing an exact polynomial-identity test — which points at a truncation
(`max_m = 224` for A=14) rather than at a wrong extraction, but that is a
hypothesis, not a result.

**Not established:** whether `false` is expected at A=14. Nobody has checked what
the flag reads for the other 26 `habiro-coefficients-*` witnesses. That survey is
the first thing to do and it is cheap — if `false` appears only at the largest A,
the truncation reading is supported; if it appears across the family, the flag
means something else or is broken.

## Why it is worth a bean rather than a shrug

Two live scripts read this witness and neither looks at the flag:

    extend_even_a_mirror_pair_test.py:117        load_a_m("oxygen-14")
    topic2_mirror_pair_phi8_boundary_scan.py:76  load_a_m("oxygen-14")

Both pull `habiro_coefficients` straight out and compose them into a mirror
difference, then read off a Φ₈ cyclotomic multiplicity. If the coefficients do
not reconstruct their own polynomial, a multiplicity computed from them is
resting on something the producer already flagged as not matching — and the
consumer never sees the flag.

So the decision is not only "is false expected", it is "should `load_a_m` refuse,
or at least warn, on a witness whose own reconstruction check failed". A
published `false` that every reader ignores is the same shape as the
`Q0_ANCHOR_MISSING` problem on `qou-po7i`: the file records the caveat and
nothing downstream consults it.

## Suggested order

  1. survey `reconstruction_matches` across all 27 `habiro-coefficients-*`
     witnesses — cheap, and it decides whether this is A=14-specific;
  2. if truncation-specific, check whether `max_m` for A=14 (224) is actually
     sufficient, and record the answer in the witness rather than the flag alone;
  3. decide whether the two readers should guard on it.

Not investigated here — it surfaced during the oxygen-14 regeneration
(bean `qou-mnrd`) and is deliberately not that arc's to answer.
