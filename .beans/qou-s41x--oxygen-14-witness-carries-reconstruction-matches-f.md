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

## Step 1 done — the survey, and it refutes the framing above

Ran the cheap survey. **`false` is the NORM, not the exception: 21 false, 4 true**
across the 25 habiro witnesses that carry the flag.

    FALSE at A = 1,2,3,4,5,6,7,8,9,10,14      (21 witnesses)
    TRUE  at A = 6,12,14                      (4 witnesses)

So the "is `false` expected at A=14?" framing was wrong — the question is why
**four** files are `true`. And `tr_M_at_q0_rel_err` is `0.0` for **all 25**,
including every `false` one, so the flag is failing family-wide while the
independent numeric cross-check passes exactly everywhere. A flag that is false
in 84% of cases while the thing it supposedly guards reproduces to full
precision is not carrying the meaning its name implies.

The four `true` files are exactly `extend_even_a_mirror_pair_test.EVEN_A_OPEN`
— helium-6, boron-12, nitrogen-12, carbon-14 — **minus oxygen-14**, the fifth
member of that same list. Everything produced from
`_habiro_coefficient_extract.ATOMS` is `false`. So the split tracks the
producing RUN, not any property of the polynomial: same function
(`analyse_atom`), same code path, opposite answers.

## A real bug found on the way, though it is NOT the explanation

`computations/_habiro_coefficient_extract.py`:

    197:  coeffs = cyclotomic_expansion(p_u, u, max_m=max_m)    # 48 … 224
    205:  recon  = reconstruct(coeffs, u)                       # ← no max_m

and the imported `reconstruct` is
`habiro_coefficients_atomic.reconstruct(coeffs_data, check_q, max_m=20)`. So the
extraction runs to `max_m` (224 for oxygen-14) while the **verification
reconstructs from at most 20 terms**. That is a latent defect worth fixing on its
own — a check that silently examines a fifth of what was computed.

**Tested as the explanation and it FAILS.** Predicted `true` ⟺ highest nonzero
index ≤ 20; got 13 contradictions out of 25. `proton` has its highest nonzero
coefficient at m=8 — comfortably inside 20 — and is `false`; `carbon-14` reaches
m=34 and is `true`. Recording the refutation so nobody re-runs it. (Also
established in passing: the coefficients are contiguous — `n_nonzero` = highest
index + 1 in every one of the 25.)

## Where that leaves it

Two hypotheses down. What remains is that the flag's value depends on **when and
by which run** a witness was written, which would make it useless for comparison
and would mean the four `true` values are the anomaly rather than the 21 `false`.
Next probe: re-run one currently-`false` ATOMS atom (proton is cheapest, m≤8) and
see which value it produces today. If it comes back `true`, the committed `false`
values are stale artifacts and the whole family needs regenerating; if it stays
`false`, the difference is in how `extend_even_a_mirror_pair_test` invokes
`analyse_atom` versus the ATOMS loop, and that diff is short enough to read.

The consumer question from the original write-up is unchanged and is now more
pressing, not less: two live readers pull these coefficients and neither consults
the flag, and 21 of 25 witnesses are advertising a failed self-check.
