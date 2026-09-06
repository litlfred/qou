---
# qou-hft3
title: He-4 disjoint-product identity fails 5.94x once the 480s timeout stops masking it
status: in-progress
type: bug
priority: normal
created_at: 2026-09-06T10:41:05Z
updated_at: 2026-09-06T10:41:32Z
---

## What happened

`computations/atomic_tr_m_helium4.py` cross-checks two routes to |tr_M(⁴He)| on
H₁₂:

- **(A) disjoint product** — `|tr_M(⁴He)| = |tr_M(p)|² · |tr_M(n)|²`, read from
  `atomic-tr-m-mpfr-50dps-proton.witness.json`
- **(B) direct recursion** — `markov_trace_recursive.markov_trace_of_word(12, word)`

The **committed** witness records (B) as having never run:

    direct_recursion.error                          = "timeout_after_480s"
    direct_recursion.elapsed_sec                    = 480.00026202201843
    direct_recursion.abs_tr_M_50dps                 = null
    direct_recursion.matches_disjoint_product_within_1ppb = null

On 2026-09-06 it completed in **16.54 s** and the two routes disagree:

    (A) disjoint product   |tr_M(⁴He)| = 1.280783151528646
    (B) direct recursion   |tr_M(⁴He)| = 7.610469960740114
        ratio  (B)/(A)                 = 5.9420
        Δ                              = 4.94204

The producer prints `✗ MISMATCH — investigate disjoint-product application on
H_12` and then **exits 0** ("0 assertions, all passed"). The mismatch is
printed, not asserted, so nothing downstream notices.

So the identity has never once been verified. `matches_..._within_1ppb: null`
reads as "not checked"; it was in fact "checked and cannot pass", and the
timeout hid which.

## Why it suddenly completes

Not the row-cap optimisation landed in the same pass (`qou-fq0f`, ~100x on the
Wenzl bridge): this producer uses `markov_trace_of_word`, an independent
recursion, and imports the bridge nowhere. It went from >480 s to 16.5 s for
some other reason — a sibling's merged work today, or machine variance. Worth
confirming, because if it is variance the timeout can come back and re-hide
this.

## Three things to separate before fixing

1. **Which arm is wrong.** A factor of 5.942 is not a precision artefact. Note
   the disjoint-product arm squares values it did not compute.
2. **The word is not the canonical one.** It is hand-specified —
   `σ₁⁷σ₂⁴ · σ₄⁷σ₅⁴ · σ₇⁶σ₈⁴σ₇⁻¹ · σ₁₀⁶σ₁₁⁴σ₁₀⁻¹`, 44 crossings — not
   `atom_braid_word_3A(2,2)`, so this "helium-4" is a different braid from the
   one the intra-ordering ruling (`qou-hu1f`) governs. Its inputs are also
   grouped-era: `abs_tr_p = 1.1457596924573` is the **superseded grouped**
   proton value; the ruling gives 0.62932842249. Whatever (A) and (B) are
   comparing, it is not the production ⁴He.
3. **A printed ✗ must not exit 0.** That is the defect that let this sit.

## Now reachable, which changes the options

`qou-fq0f` made the Wenzl bridge run at H₁₂ in **19.4 s** (previously
unreachable), and `atomic_tr_m_helium4.py`'s own header already anticipates
this: line 25 says it should move to `tr_M_via_wenzl_bridge_mpfr.py` "once the
y-lambda witness is extended". It is extended and the bridge is fast. A **third,
independent** value for |tr_M(⁴He)| is now cheap to obtain, which is the natural
way to settle which of (A) and (B) is wrong rather than arguing from the two
that disagree.

Direct bridge evaluation on the canonical word `atom_braid_word_3A(2,2)` gives
`0.01123741765976742156419955` in 19.37 s — but that is the canonical borromean
word, so it is not directly comparable to either arm above until item 2 is
resolved. Recorded here as the starting point, not as the answer.

## Also

`atomic-tr-m-helium4.witness.json` emits 2 raw-float64 fields
(`direct_recursion.budget_sec`, `.elapsed_sec`) — flagged by the raw-float64
gate on every run, and inert only because they are timings.
