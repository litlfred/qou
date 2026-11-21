---
# qou-9ohz
title: 'PERF: per_generator_V_hat_3A -- one mpf coefficient forces an object-dtype O(dim^3) matmul; the word collapses to alpha*sigma+beta'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T18:57:13Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-v2om
---

MEASURED 2026-08-24, branch claude/excise-convention-c-2026-08-24.

## Symptom
`computations/binding_via_interface_knot.py` appears to hang. It does not:
`py-spy dump` on the live PID and on an independent probe caught BOTH at the
same line, in mpmath scalar arithmetic:

    per_generator_V_hat_3A (computations/mass_at_3A_proper.py:757)
        __mul__ (mpmath/ctx_mp_python.py:275)

Line 757 is `M = M @ (c * sigmas[i] + d * I_lam)`.
CPU-bound, 89 MB RSS of 16 GB, no swap. The `>12 GB RAM` comment in the file
is a 4He concern and is NOT what is happening here.

## Root cause -- dtype contamination, not algorithmic cost
The seminormal matrices are float64 and cheap: all 30 partitions of 9 build in
0.08 s, dims <= 216. The braid word coefficients are NOT uniformly typed:

    type histogram (c,d): {(int,mpf): 17, (int,int): 16, (mpf,mpf): 2}
      gen 0: steps=7 first_mpf_at=4   gen 1: steps=4 first_mpf_at=0
      gen 2: steps=1 first_mpf_at=0   gen 3: steps=7 first_mpf_at=3   ...

19 of 35 steps carry an mpf and every generator hits one by step 0-4, so
`mpf * float64_array` promotes to dtype=object and the rest of the chain is a
Python-level triple loop instead of BLAS: ~60M mpf mul+add per word-step sweep
over lambda |- 9.

Scaling check: D (n=6, sum dim^3 ~ 2e4) = 0.58 s; T (n=9, sum dim^3 ~ 6e7) is
~3000x that ~ 29 min. Observed: 20+ min and still running. Consistent.

## Fix -- exact scalar collapse, NOT a float64 cast
Within one generator every factor is a polynomial in the SAME sigma_i, so they
commute, and sigma_i obeys the Hecke quadratic relation. VERIFIED, not assumed:

    (3,2,1)     sigma^2 = (q-1/q) sigma + 1 : max|diff| = 6.661e-16   OK
    (4,3,1,1)   sigma^2 = (q-1) sigma + q   : max|diff| = 1.992e-01   NO
                eigenvalues [-0.90091828, 1.10997858] = [-1/q, q]

So the product collapses to W_i = alpha*sigma_i + beta*1 by a scalar mpf
recursion, and chi_lambda(W_i) = alpha * tr(sigma_i^lambda) + beta * dim.
tr(sigma_i^lambda) is a diagonal sum of ONE matrix, O(dim), computed once.
No matmul, no precision given up.

    (alpha,beta) * (c,d):  alpha` = alpha*c*(q-1/q) + alpha*d + beta*c
                           beta`  = alpha*c + beta*d

## Verification
    D: matmul 0.611s   reduced 0.001s   max|diff| = 9.107e-16
       matmul : +0.671385824 +1.055110319 +0.000071902 +0.551656055 +1.088367533
       reduced: +0.671385824 +1.055110319 +0.000071902 +0.551656055 +1.088367533
    T: reduced 0.099s   (vs the 20+ min matmul run)

Caveats, stated because they are not yet closed:
  * T / 3He equality is still verifying against the slow path in the
    background. D is confirmed; T is NOT yet.
  * 9.1e-16 is float64 round-off because `_cached_seminormal` returns float64
    on this path. The reduction is exact; it does not by itself make this path
    high-precision, and it must not be reported as if it did.
  * Whether this unblocks 4He (n=12) is NOT established. The reduction removes
    the matmul but still asks for sigma_i per lambda; a closed-form axial-
    distance diagonal would remove that too, and has not been checked.

## Overlap
Main`s qou-fmoi sparse-chi_lambda work (97-186x) does not touch
mass_at_3A_proper.py. Commit 6b21956c23 hit the same mpf-contamination class in
chi_lambda_of_word. Adjacent, not duplicate.

## Next
Patch mass_at_3A_proper.py:746-763 once the T/3He confirmation lands. Worth
doing before the qou-37xc baseline campaign resumes -- that campaign is itself
paying this cost.

VERIFIED at A=3 (2026-08-24). Not via the timing harness — via the producer itself.

delta_lambda_v_hat_z_transfer_phase5d_4 calls per_generator_V_hat_3A at A=3 and
was the branch's longest pole: PR #5622 lists it as '2.5h+ per measurement', and
a run of it was killed at 2h47m. Under the patch it completes in **1 second**.

The A=3 correctness check falls out for free: the committed C baseline witness
(34b068f197) was produced by the UNPATCHED code in that 2.5h run; re-running the
same C source under the PATCHED code reproduces it across 171 non-volatile
fields, 42 of them V_hat values, with ZERO differing beyond 1e-12 relative.
Worst 1.448e-13 — the same tiny-denominator artifact as A=2 (one V_hat is
7.19e-05, so 9e-16 absolute reads large relative).

Stronger than the planned harness comparison, which would have measured a
reimplementation of the call rather than the call as producers actually make it.


---

## Independent confirmation on a SECOND consumer (2026-08-25, branch claude/gram-norm-threshold-investigation-v8ck94)

Reached this bean's mechanism from the other end — a stalled probe, not
`per_generator_V_hat_3A` — and it reproduces exactly. Recording it because the
second consumer changes the scope estimate: this is not one function's bug.

**Consumer:** `computations/probes/gram_norm_binding_probe.py::_letters`, line
`out.append(c * sig + d * eye)`. Same word builder (`atom_braid_word_3A`), same
contamination, independent code path.

Measured type histogram matches this bean's exactly: `{(int,int), (int,mpf),
(mpf,mpf)}`.

**Quantified at the matmul, λ=(4,3,1,1), d=216:**

    one matmul   float64 = 0.74 ms      object dtype = 13270 ms      1.8e4x

**Symptom as seen from outside:** the probe ran >2131 s on ³H (n=9) and was on
track to consume a 7200 s budget on that one isotope, against 0.8 s for ²H
(n=6). A prior session read that as a "threshold effect in the underlying
trace/Gram computation as the Hecke dimension grows" and proposed more budget
plus per-unit instrumentation. **That hypothesis is wrong and is retracted
here:** there is no threshold. The cost is smooth in Σ_λ dim³ with a ~1.8e4
constant from object dtype; Σdim³ itself jumps ~6300x from n=6 to n=9, which is
what makes it *look* like a cliff.

**This bean's scalar-collapse fix does NOT apply to this consumer.** The
collapse relies on every factor within one generator being a polynomial in the
same σ_i, hence commuting. `gram_norm_binding_probe` multiplies a general braid
word with interleaved *different* generators, which do not commute, so the
matmul chain is genuinely required. Fixed instead by coercing the coefficients
to float in `_letters`, which is sound *only* because on this path
`build_seminormal_matrices` already returns float64 — the mpf is multiplying an
operand that has already been truncated, so it carries precision that cannot
survive the product. Verified at ²H: object-dtype vs coerced agree to 9e-16
(rel), the float64 floor. Post-fix the whole default probe runs in 1.9 s.

This is the same caveat this bean already states ("9.1e-16 is float64 round-off
because `_cached_seminormal` returns float64 on this path ... it must not be
reported as if it did [make it high-precision]"). Neither fix makes either path
high-precision. The deeper item — that the seminormal path is float64 at all —
is untouched by both and is not claimed closed by either.

**Side finding, tracked separately:** the committed
`gram-norm-binding-probe.witness.json` on `main` is stale — see the bean for it.



**Correction to the note above (same session):** it ended by citing a
raw-float64 drain of 248 -> 148 for the regenerated witness. That 148 came from
a three-isotope run without `--with-4he`, compared against a four-isotope
baseline. The like-for-like figure is **248, flat** — ratchet-neutral, not
draining. See `qou-wlaf`.


---

## The "deeper item" is now PARTLY answerable — measured 2026-08-25

Both notes above end by saying the real item, that the seminormal path is
float64 at all, is untouched by either fix. As of `a7aacec54` on `main` that is
no longer quite true: `hecke_characters.build_seminormal_matrices_mp(shape, q)`
now exists as an exact-arithmetic twin returning `mp.matrix` (landed via
[#5763](https://github.com/litlfred/qou/pull/5763), diagnosed as bean
`qou-8xb1`). It is **additive** — the float64 builder is untouched, so nothing
existing changed behaviour.

Measured here, at 50 dps, for what it would cost the *gram-norm* consumer,
which is matmul-bound rather than construction-bound:

    lam=(3,2,1)    d=16    construct 0.00 s   one matmul  f64 0.15 ms   mp    4.5 ms    29x
    lam=(4,3,1,1)  d=216   construct 0.42 s   one matmul  f64 12.3 ms   mp 6883.8 ms   561x

Consistent with the 642x-at-d=162 figure `qou-d8gq` recorded, and the ratio
clearly **grows with dimension** rather than sitting at a constant.

Consequence for `gram_norm_binding_probe`, which runs 2x(word length) matmuls
per lambda:

  * **Up to 3H / 3He (d <= 216): viable.** 0.45 s x ~561 is roughly 4 minutes
    for a genuinely multiprecision run. That is a real option and would retire
    the float64 caveat for the light isotopes.
  * **4He (d up to 7700): not viable.** 418 s x 561 is ~65 hours, and since the
    ratio grows with d that is a **lower bound**, not an estimate. Do not quote
    65 h as the cost; quote it as "at least tens of hours".

So the honest status is no longer "open" and not "closed": the exact route
exists, it is affordable for the small-dimension consumers, and it is out of
reach for the one this probe most wanted it for. Recording the numbers so the
next agent does not have to re-derive them before deciding.

Not doing the upgrade on PR #5775 — that probe declares itself float64 and
audit-only, the change would move every number it reports, and it belongs in a
scoped PR against `qou-8xb1` rather than riding on a perf fix.


### CORRECTION to the note above: the "~4 minutes for 3H" figure is WRONG

That note said the exact route made 3H/3He "viable" at roughly four minutes.
Measured: a 3H `_gram_and_trace_mp` run has exceeded **30 minutes** without
finishing. Do not quote 4 minutes.

The error was in the extrapolation, and it is instructive. I took the float64
whole-isotope time (0.45 s) and multiplied by the per-matmul ratio at the
largest dimension (561x) to get 252 s. That step assumes the float64 time is
matmul-dominated at d=216. **It is not.** One float64 matmul at d=216 already
costs 12.3 ms, and the probe does ~70 of them per lambda, so the largest lambda
alone would be ~0.86 s — nearly twice the measured whole-isotope total. The
float64 path is getting a large speedup the timing did not account for (sparse
dispatch on the big blocks), which the mpmath path cannot use: every entry
there is a Python object and every product is a Python loop.

So the ratio measured on ONE dense matmul is a **lower bound** on the aggregate
ratio, not an estimate of it, and multiplying a whole-pipeline time by it
understates the cost — here by at least an order of magnitude.

Revised status, stated as measurement rather than extrapolation:

  * **2H (d <= 16): confirmed, ~2 s.** Exact and float64 agreed to 2.13e-14.
  * **3H / 3He (d <= 216): UNMEASURED, exceeds 30 min.** Not "viable"; not
    established as infeasible either. Someone should let one finish and record
    the number instead of extrapolating, as I did.
  * **4He (d up to 7700): out of reach**, unchanged.

The same caution applies to the 4He figure in the note above: ">= tens of
hours" was reached the same way, so treat it as a lower bound that is probably
much too low, which is the direction that keeps it honest.


---

## The patch IS landed — correcting my own repeated claim (2026-08-25)

I stated three times, in this bean, in PR #5775, and to the owner, that the
`per_generator_V_hat_3A` scalar-collapse patch had **not** landed and that the
`qou-wlaf` re-run campaign was gated behind it. **That was wrong the whole
time.**

The collapse is on `main`. Measured on today's `main`:

    per_generator_V_hat_3A(1, 2)   # 3H, A=3   ->  0.21 s

against the 2.5 h+ this bean records for the unpatched path. The source
carries the `# Per-generator SCALAR collapse, replacing a per-λ matrix
product.` comment at line 883.

**Why I missed it, because the failure mode generalises.** I checked with
`git log -3 origin/main -- computations/mass_at_3A_proper.py`, saw only a
language-cleanup commit and an old merge, and concluded "not landed". The
collapse arrived under a commit named for something else entirely —
`89d94187b9 probe: per-block-magnitude binding for A=3 (operator-valued, no
Δ_λ)` — and was further back than three commits. The original
`23b9c4f5ba perf(qou-9ohz): ...` is **not** an ancestor of `main`; its content
was re-landed by another route, so searching for the commit finds nothing while
the change is present.

**A cherry-pick confirmed it independently and by accident:**
`git cherry-pick --no-commit 23b9c4f5ba` auto-merged to an **empty diff**. A
no-op cherry-pick is a positive result — it says the content is already there.

Two rules worth keeping:

  * **Test the behaviour, not the commit log.** `git log -N -- <file>` answers
    "what recently touched this file", which is not "does this change exist".
    One timing call settled in 0.2 s what the log had answered wrongly for
    hours.
  * **A no-op cherry-pick is evidence.** If a patch you believe is missing
    cherry-picks to an empty diff, stop and check whether it landed by another
    route before concluding the cherry-pick failed.

**Consequence: the `qou-wlaf` residue is NOT gated.** Every place that says it
waits on this patch — this bean, `qou-wlaf`, and PR #5775's body — is stale on
that point.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-25 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8308, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). No superseded premise for the fix itself (an exact Hecke-quadratic scalar collapse; the word it is applied to may be old-letter, which does not affect the code).

**Completed.** The per-generator scalar collapse is on main: `computations/mass_at_3A_proper.py` line ~1082 ("σ_i, so the factors commute, and σ_i obeys the Hecke quadratic relation"). The bean's own 2026-08-25 section already records 3H in 0.21 s against 2.5 h unpatched.
