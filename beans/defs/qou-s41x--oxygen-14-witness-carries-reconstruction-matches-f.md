---
# qou-s41x
title: 'oxygen-14 witness carries reconstruction_matches: false — pre-existing, undecided, two live readers'
status: completed
type: task
priority: normal
created_at: 2026-08-10T02:36:17Z
updated_at: 2026-08-15T12:42:37Z
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

## Step 2 — the probe, and it settles it the other way round

Ran `analyse_atom` in memory (writing nothing, so no witness moved) and compared
today's `reconstruction_matches` against the committed value.

    atom        max_m   committed   TODAY    n_nonzero   hi_m
    proton         48     false      false        9        8
    neutron        48     false      false        9        8
    deuteron       64     false      false       13       12
    helium-6       96     TRUE       false       23       22     ← reverses

The 21 `false` reproduce. But **a committed `true` comes back `false`**, with
*identical* `n_nonzero` and `hi_m`. Same inputs, same derived coefficients,
opposite verdict — so what changed is the CODE, not the data.

**Conclusion: today the check is false universally, and the four `true` values
are stale artifacts of an older code state.** That is the reverse of both earlier
framings — the original bean asked why oxygen-14 is `false`, my first correction
asked why four files are `true`, and the answer is that neither is the anomaly:
the flag regressed at some point and every witness written since records `false`.
The four `true` files are simply the ones not regenerated since.

This also means the earlier refutation needs qualifying rather than discarding.
`reconstruct(coeffs, u)` dropping `max_m` (defaults to 20 while extraction runs
to 96–224) was refuted as an explanation of the true/false SPLIT — correctly,
since the split turns out to be temporal, not structural. As an explanation of
today's UNIVERSAL false it is back in play and now fits helium-6 exactly
(hi_m=22 > 20, so a 20-term reconstruction cannot match). It still does **not**
fit proton (hi_m=8, comfortably inside 20, yet `false`), so it is at most part of
the cause. Something else fails for the small atoms.

`boron-12` (max_m=192, committed `true`) was still running when this was written;
it is a confirmation, not a decision point — helium-6 alone establishes the
reversal.

## What this changes about priority

It goes UP. Previously: "21 of 25 witnesses advertise a failed self-check that
two readers ignore." Now: **the self-check itself is broken**, so it is not
telling anyone anything about any witness, and the 4 `true` values actively
mislead — they read as "verified" when today's code would not verify them.

Next: find when it regressed. `reconstruct`'s missing `max_m` is one candidate
and fits the large atoms; the small-atom failure needs its own look. Fixing the
check must come before re-running any of the 25, or the regeneration just
rewrites `false` everywhere and buries the four remaining pieces of evidence.

## SOLVED — and it is `qou-0ndb`'s bug, biting the verifier

`habiro_coefficients_atomic.reconstruct` sympified with **one** name:

    a_m = sp.sympify(entry["a_m"], locals={"check_q": check_q})

but `cyclotomic_expansion` renders its `a_m` strings using WHATEVER SYMBOL the
caller handed it, and the two call sites hand it different ones:

    habiro_coefficients_atomic.analyse_atomic_braid   passes `check_q`  → strings say check_q
    _habiro_coefficient_extract.analyse_atom          passes `u`        → strings say u

So every `u`-rendered string resolved to a **fresh** `Symbol('u')` — same name,
no assumptions, therefore not the caller's `Symbol('u', positive=True,
real=True)`. Demonstrated in three lines:

    sp.sympify("8 - 3*u**2", locals={"check_q": u}) - (8 - 3*u**2)
        ->  -3*u**2 + 3*u**2        # NOT 0

`diff == 0` was therefore false for every atom regardless of size — which is why
`proton` (hi_m=8) failed just as surely as `helium-6` (hi_m=22), the fact that
killed both earlier hypotheses.

Fix: `locals={"u": check_q, "check_q": check_q}`. It cannot misfire — a given
string uses one name or the other, and both now resolve to the caller's symbol.

### Verified

    atom        committed   before fix   AFTER FIX
    proton        false       false        TRUE
    neutron       false       false        TRUE
    deuteron      false       false        TRUE
    helium-6      TRUE        false        TRUE      ← the reversal, reversed back
    boron-12      TRUE        false        TRUE

So the four committed `true` values were **right all along**, and the 21 `false`
are the artifacts. Exactly opposite to this bean's opening framing, and opposite
again to my first correction. The check regressed; the witnesses recording
`true` are the ones that predate the regression.

### The expensive part: it also corrupted the Φ₈ multiplicities

`mirror_pair_diff` (`_habiro_coefficient_extract.py:382`) uses the same
`reconstruct`, then divides the result by cyclotomic polynomials in the CALLER's
`u`. With the two symbols mixed, the division is never exact, so the
multiplicity comes back 0. `habiro-coefficients-mass-table-summary.witness.json`
publishes exactly that — `phi_8_mult: 0` for all 7 mirror pairs and all 7 rows of
`phi_k_scaling_table`.

Recomputed on the committed coefficients with the fix:

    pair                            A    phi_8   2⌊(A−1)/2⌋
    proton − neutron                1      0         0
    helium-3 − tritium              3      2         2
    lithium-5 − helium-5            5      4         4
    boron-9 − beryllium-9           9      8         8
    carbon-10 − beryllium-10       10      8         8

Five for five against **the repo's own refined scaling law** (see
`docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md` and
`extend_even_a_mirror_pair_test.py`'s docstring). The published witness reports 0
for the quantity that law is about.

Why nobody caught it: `extend_even_a_mirror_pair_test.py` and
`topic2_mirror_pair_phi8_boundary_scan.py` do **not** use the shared helper —
they carry their own `load_a_m` with `locals={'u': u, 'check_q': u}` already
correct, and their own `cyc_mult`. So the two scripts whose whole purpose is
testing this law were computing it correctly, while the shared-helper path
published zeros beside them. A uniform 0 across A=1..10, for a quantity a
documented law says varies with A, was the tell.

### Correction to this bean's own earlier note

`reconstruct`'s `max_m=20` is **vestigial** — the loop iterates `coeffs_data`,
not `range(max_m)`, so it never truncated anything. The "verification examines a
fifth of what was computed" concern recorded above is withdrawn; it was wrong.
Marked as such in the code.

## Not done here

`habiro-coefficients-mass-table-summary.witness.json` still publishes the zeros.
Regenerating it means running the full ATOMS table (proton … carbon-10, max_m up
to 160) — a deliberate producer run, and one that now also has to absorb the
padding-ratchet consequence recorded on `qou-j6gb` (68 producers build their
constants at 50 dps, so latent float64 becomes visible padding). Sequence that
deliberately; do not fold it into an unrelated change.

---

## REGENERATED — the zeros are gone, and the coefficients never moved

PR #4926, stacked on #4903. The full ATOMS run took 513 s / 0 failures.

Φ_8 now matches `2⌊(A−1)/2⌋` on **all seven** mirror pairs (was 0 on all
seven):

    A    pair                            Φ_8   2⌊(A−1)/2⌋
    1    proton − neutron                 0       0
    3    helium-3 − tritium               2       2
    5    lithium-5 − helium-5             4       4
    7    beryllium-7 − lithium-7          6       6
    8    boron-8 − lithium-8              6       6
    9    boron-9 − beryllium-9            8       8
   10    carbon-10 − beryllium-10         8       8

`reconstruction_matches` is True on all 20 atoms; `tr_M_at_q0_rel_err`
stayed 0.0 throughout.

**The decisive check: all 25 per-atom witnesses carry byte-identical
`habiro_coefficients` before and after.** So this was a corrected *check*,
never corrected mathematics — which is also why nothing downstream of the
coefficients needs re-litigating.

Φ_2 came back 1 at A=1, matching the value
`docs/audits/2026-06-01-qbeta-habiro-phi8-mirror-multiplicity-scaling.md`
recorded independently from the two standalone scripts. An independent
source agreeing on a value the witness had zeroed is the strongest
confirmation available that the regenerated numbers are the real ones.

### An observation, explicitly NOT a law

Φ_2 also comes back **1 at A=8 and A=10** — even-A pairs that audit doc did
not have when it wrote that Φ_2 is "specific to A = 1". Present pattern:
Φ_2 = 1 at A ∈ {1, 8, 10}, 0 at A ∈ {3, 5, 7, 9}. That reads as "even A, plus
A=1", but three even-A points are not a scaling claim and it has not been
tested. Do not cite it as one; the doc's A=1-specific wording is now known
to be incomplete, which is a different statement from knowing the rule.

## The qou-j6gb prediction was right, in its function-scope form

`main()` had `q0_mp = mp.mpf(str(_Q_CANONICAL))` at the default 15 dps.
`analyse_atom` then raised dps to 50 and built `sp.Rational(str(q0))` — an
*exact* rational from a value whose last 34 digits were the binary64
expansion:

    1.1099785827513799496557567181298509240150451660156   was
    1.1099785827513808075916690956107688798744991218736   is

7.7e-16 relative, anchoring tr_M_at_q0 in all 20 witnesses. Fixed BEFORE the
run (sourced from `Q_50_DIGIT_STR`), so the table did not need computing
twice. Same anchor layer throughout — `parameters.q_0` unchanged at the
proton pin; no straddle.

Because it was fixed first, the ratchets did **not** go red: all blocking
precision gates green, counts identical to the pre-run baseline. Two audit
witnesses moved in the right direction — `Q0_OK` 581 → 602,
`Q0_ANCHOR_MISSING` 1888 → 1867, as the 21 regenerated witnesses now record
`q0Value` at 50 digits with `q0Anchor: "proton"`.

## oxygen-14 — this bean's original subject

It is the **only** remaining `reconstruction_matches: false` in the family,
and the reason is ordering, not anything about A=14. Its producer is
`extend_even_a_mirror_pair_test.py` (its own `EVEN_A_OPEN` list, not
`ATOMS`), and it was regenerated at `64b1389eb` — *before* the `reconstruct`
fix landed at `a417b821e`. So it missed the fix by two commits.

The remaining question this bean opened — "should `load_a_m` refuse, or at
least warn, on a witness whose own reconstruction check failed" — is
untouched and still live. It is now a smaller question (0 or 1 offenders
rather than 21), but the structural point stands: a published caveat that
every reader ignores is the `qou-po7i` shape.

## Landed on main (c16eb6dcb, via PR #4926)

Everything above is on `main`. Φ_8 matches the law on all seven pairs,
`reconstruction_matches` is True on all 26 witnesses, and oxygen-14 — this
bean's original subject — is fixed.

**Deliberately left in-progress, not completed.** The bean opened two
questions and only one is answered. The second is untouched:

> should `load_a_m` refuse, or at least warn, on a witness whose own
> reconstruction check failed?

It is now a *smaller* question — 0 offenders rather than 21 — but "there
are currently no offenders" is not an answer to "should a reader trust a
witness that flagged itself". It is a design call about consumer contracts,
and closing this bean on the strength of the count would quietly convert an
open decision into a decision nobody made. Left for the owner.

---

## Summary of Changes — COMPLETED

Verified on `main` at `ebc21d1ae`, measured rather than assumed:

    reconstruction_matches across the habiro family:  true=25  false=0
        (was true=4, false=21)

    habiro-coefficients-mass-table-summary, all 7 mirror pairs:

        pair                              A   phi_8   2⌊(A−1)/2⌋
        proton − neutron                  1     0         0
        helium-3 − tritium                3     2         2
        lithium-5 − helium-5              5     4         4
        beryllium-7 − lithium-7           7     6         6
        boron-8 − lithium-8               8     6         6
        boron-9 − beryllium-9             9     8         8
        carbon-10 − beryllium-10         10     8         8

Seven for seven, including A=7 and A=8 which were never tested while
diagnosing — those two are independent confirmation rather than a restatement
of the five pairs the fix was validated on.

**What the bean turned out to be.** Opened as "is `reconstruction_matches: false`
expected at A=14?". It was not an A=14 question, nor a "why are four files true"
question. `reconstruct` sympified the `a_m` strings with only `check_q` in
`locals`, so every `u`-rendered string resolved to a fresh `Symbol('u')` carrying
no assumptions — not the caller's `Symbol('u', positive=True, real=True)` — and
`diff == 0` was false for every atom regardless of size. Root cause is bean
`qou-0ndb`; this was its fourth and most expensive instance, because the same
`reconstruct` feeds `mirror_pair_diff`, which then divided by cyclotomic
polynomials in the caller's symbol and returned multiplicity 0 for everything.

The published witness reported `phi_8_mult: 0` across the board for the quantity
the repo's own refined scaling law is about. The two scripts whose purpose is
testing that law — `extend_even_a_mirror_pair_test.py` and
`topic2_mirror_pair_phi8_boundary_scan.py` — never used the shared helper and
had the two-name `locals` right, so they computed it correctly the whole time,
beside a summary publishing zeros.

**Two hypotheses were tested and killed on the way, both recorded above so they
are not re-run:** that the split was A=14-specific (it was not — `false` was the
norm at 21 of 25), and that `reconstruct`'s `max_m=20` truncated the check (it
does not — `max_m` is vestigial, the loop iterates `coeffs_data`).

Regeneration landed via #4926; the fix itself via #4903's commits, content-merged
into the same PR.

## Follow-ups deferred, not dropped

Both live on other beans rather than here: retiring the two-name `locals`
workaround once every witness has been regenerated (`qou-0ndb`), and the second
`to_u_polynomial` copy that emits canonical text by luck rather than by
construction (`qou-0ndb`).
