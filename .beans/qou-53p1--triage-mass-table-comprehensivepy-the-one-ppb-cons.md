---
# qou-53p1
title: Triage mass_table_comprehensive.py — the one ppb consumer that timed out unchecked
status: todo
type: task
priority: normal
created_at: 2026-08-16T01:49:31Z
updated_at: 2026-08-16T10:57:34Z
---

## Triage answer: NOT broken. Slow — and hiding something much worse.

Last unchecked consumer from the `mass_table_ppb` port (qou-3wqg / qou-hqjf).
It timed out at 120 s during the consumer sweep, so it was unknown whether it
was merely slow or broken the way the four binding-family producers were.

**It runs to completion, rc=0, 14,972 rows.** But getting that answer turned up
three findings, and the third is the one that matters.

## 1. The ppb correction never reaches it — the upstream is declared, not read

```
mt_ppb_path = _pb.witness_path("mass-table-ppb.witness.json", HERE)
mt_ppb_data = None
if mt_ppb_path.exists():
    mt_ppb_data = builder.add_upstream(mt_ppb_path)     # L406
```

`mt_ppb_data` has **two stores and zero loads** (checked by AST walk, not by
eye). Every `B_pred_MeV` in the output comes from this producer's own
`sym_binding` / `qclt_binding` / `binding_canonical` paths. So the corrected
deuteron prediction does not reach this consumer at all — the provenance edge
claims a dependency the code does not have.

The `alpha_cluster_binding` call site is also safe: it already wraps
`float(r["B_pred_MeV"])`, so qou-hqjf changing that return type to mpf does
not break it.

That closes the question this bean was opened for.

## 2. It is ~11.5x slower than its own recorded baseline

    committed witness   durationMs    57,274   (14,972 rows,  261 rows/s)
    measured today      durationMs   656,759   (14,972 rows,   23 rows/s)

Same enumeration, and the producer takes **no CLI flags**, so there is exactly
one invocation to compare. `t_start = time.monotonic()` sits at the top of
`main()` above the row loop, so the baseline covers the full computation — I
checked, because a duration that only measured the final write would have made
this a non-finding.

**Not caused by this session.** A/B at `d7274ddc0` (pre-merge) vs current main,
150 s budget each: 5663 vs 5642 rows. Noise. I had suspected my own
`set_compute_dps()` additions raising global `mp.dps` to 70 via the lazy
`alpha.alpha_cluster_recursion` import inside the row loop — measured, wrong.

`engineVersion` moved `mpmath 1.3.0 -> 1.4.1` between the two runs. That is the
best remaining candidate and it is **untested** — it would affect every mpmath
producer in the repo, not just this one, so it is worth an hour from whoever
picks it up. Bisecting the code path instead needs `git fetch --unshallow`:
the witness's own `commitSha` (85da4f43133) is not reachable in this shallow
clone.

## 3. THE ONE THAT MATTERS — the committed witness is 5 weeks stale, and every row differs

`computedAt: 2026-07-07`. Regenerating today changes **14,970 of 14,972 rows**
in both `m_symbolic_MeV` and `B_pred_MeV`. These are not precision tails:

     atom      B_AME   B_pred OLD   B_pred NEW   err% OLD   err% NEW
        D     2.2245       3.5423       2.0715    +59.239     -6.877
        T     8.4818       8.4732       5.5149     -0.102    -34.980
      7Li    39.2445      23.0623      15.0515    -41.234    -61.647
      16O   127.6190      54.6043      35.4496    -57.213    -72.222

Mixed, not a scale factor: the deuteron gets much BETTER (+59% -> -6.9%) while
everything A>=3 gets much WORSE. Tritium's error moves from -0.1% to -35%.

Two readings, and I cannot tell which from the numbers alone:
  (a) a code change since 2026-07-07 broke the binding path, and the stale
      witness has been masking it for five weeks; or
  (b) the methodology changed deliberately and nobody regenerated.

Either way the published 10 MB table is not what the code computes, and
**nothing catches it**: regeneration takes 11 minutes, no gate runs it, and the
witness-staleness workflow is dispatch-only by owner directive (2026-06-30
Actions-billing). Four audit docs cite values from the stale copy
(`2026-08-09-canonical-ordering-dof-production-impact.md`,
`2026-08-09-ordering-loose-ends-a3-helper-and-missing-he-rows.md`,
`2026-06-01-vol-density-derivation-trace.md`,
`2026-05-24-65-isotope-mass-table-audit.md`).

### I did NOT commit the regenerated witness

Deciding which of the two tables is correct is a physics call, not a triage
outcome, and it would also move this file's raw-float64 count (it is in the
qou-mnrd baseline). The regenerated file is preserved out-of-tree at:

    <session scratchpad>/mass-table-comprehensive.REGENERATED-2026-08-16.witness.json

so whoever adjudicates does not have to spend another 11 minutes.

## Smaller things found in passing, none fixed

- **All upstream provenance is discarded.** The output has no
  `upstream_witness_hashes` key at all, despite `add_upstream(mt_ppb_path)` at
  L406 and ~15,000 `record_upstream(...)` calls at L205.
  `builder.add_upstream_records(_UPSTREAM_RECORDS)` runs at **L363**, before
  the row loop that fills `_UPSTREAM_RECORDS`. Checked whether this ordering
  bug was systemic across the `record_upstream` port (453b2a868, 86a218eb3):
  a textual-order scan found 0 other producers, but textual order is the wrong
  test here (collection happens inside a function called later), so that scan
  proves nothing and a real check is still owed.
- **Stale description.** Claims "all nuclei from proton (A=1) through 12C
  (A=12) ... A >= 5 flagged as 'not yet computed'". The data is 14,972 rows,
  A=1..418, Z=0..118.
- **Every row emits a DeprecationWarning** — `atom_per_generator_volumes` uses
  H_3 Wedderburn weights where H_{3A} are correct
  (docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md). ~15,000 warnings per
  run, and it affects every published row.

## Next

Finding 3 needs an owner decision before anything is committed. Findings 1 and
the L363 ordering bug are both small, mechanical, and safe to fix — but fixing
1 means deciding whether the ppb upstream should be *read* or the declaration
*dropped*, which is again not mine to pick unilaterally.


---

## Root cause of the 11.5x: FOUND, and it is not what I guessed four times

`efcaf79ed` (2026-08-08) — *"NO FLOAT64: the braid word was f64 at source;
dashboards re-anchored"* — moved the braid-word arithmetic inside
`pyhecke.atom.atom_per_generator_volumes` from float64 to mpmath.

Measured directly, not inferred. Same commit, same everything, only
`tools/pyhecke/python/pyhecke/atom.py` swapped for its pre-`efcaf79ed` content,
150 s budget each:

    atom.py at efcaf79ed^   14,972 rows   (the FULL table, finished inside 150 s)
    atom.py at HEAD          5,615 rows

That is the whole regression, and it matches the 57 s baseline.

The profile says why. `atom_per_generator_volumes` is **80% of total runtime**
(20.6 s of 25.7 s over 400 rows), and underneath it:

    2,724,573  mpmath __mul__        per 400 rows  (~6,800/row)
    1,753,032  mpmath convert
    1,126,208  mpf from_float        (~2,800/row — floats converted every op)

Every one of those was a C double multiply before. The precision fix is
correct; its cost was never advertised.

### Blast radius is not this producer

**31 files** call `atom_per_generator_volumes`, including `canonical_tower.py`,
`substrate/hecke_core.py`, `pn_alpha_lp_dual.py` and the brane-tower probes.
Anything on that path took the same hit. This bean measured one of them because
it happened to have a committed `durationMs` to compare against.

### Four hypotheses this killed, recorded so nobody re-runs them

1. **My own `set_compute_dps()` additions** (qou-hqjf) raising global `mp.dps`
   via the lazy `alpha.alpha_cluster_recursion` import inside the row loop.
   A/B at `d7274ddc0` vs current main: 5663 vs 5642 rows. Noise.
2. **`record_upstream` in the row loop** re-reading and hashing an upstream per
   row. The file is 2,931 bytes and `record_upstream` is a bare `append` —
   ~0.15 s total.
3. **mpmath 1.3.0 -> 1.4.1.** Real but small: 6568 vs 5638 rows, **1.16x**.
   Tested by shadowing 1.3.0 through `pip --target`, everything else identical.
4. **Global `mp.dps` 15 -> 70.** Importing the producer really does raise dps to
   70 (COMPUTE_DPS) — but at dps 18 the run gives 5707 rows vs 5615. **1.6%.**
   It is the NUMBER of mpf ops that costs, not their precision.

## Correction: `efcaf79ed` does NOT explain the value change

I expected the same commit to account for finding 3. It does not. The
pre-`efcaf79ed` run prints **today's** values, not July's:

           PRE-efcaf79ed run    today (current atom.py)    committed (July)
      D         2.071536              2.071536                 3.542303
      T         5.514920              5.514920                 8.473201
    7Li        15.051502             15.051502                23.062339
    16O        35.449573             35.449573                54.604288

So these are **two independent regressions**. The speed one is identified and
measured. The value one — 14,970 of 14,972 rows, tritium -0.10% -> -34.98% —
happened somewhere between 2026-07-07 and 2026-08-08 and is **still
unattributed**. Bisecting it needs `git fetch --unshallow`; the witness's own
`commitSha` (85da4f43133) is unreachable in this shallow clone.

## Still owner's call

Nothing here changes what I said about finding 3: which table is correct is a
physics decision, and the regenerated witness stays out-of-tree until someone
makes it. The speed regression is a separate question — whether an 11.5x cost
on 31 call sites is the accepted price of the braid-word precision fix is also
not mine to decide, but it should be decided knowingly rather than by nobody
noticing for eight days.


---

# Finding 3 RESOLVED: convention C -> D, owner-ruled, and already queued

Owner called it: this is the trace convention. Confirmed by A/B, not inferred.

`33a6c7aa4` (2026-08-09) *"excise convention C from the binding channel — the
trace is now D everywhere"*, step 3 of 3 of the owner ruling:

    closed_form_tau_M::markov_z    1/(sqrt q + 1/sqrt q)  ->  q^3/(q^2+1)
    wedderburn_jones_markov::y_lambda_at    C weights -> D (SU(2) quantum dims)

Reverting **only** those two files to `33a6c7aa4^` and recomputing the symbolic
channel directly (no witness write):

           markov_z(q0)      D        T      3He      4He      7Li      16O
    D  (now)   0.6126880   2.0715   5.5149   3.3964   6.8398  15.0515  35.4496
    C  (pre)   0.4993203   3.0168   7.6948   5.1078   9.7858  21.2329  50.4001
    JULY witness            3.5423   8.4732   absent   absent  23.0623  54.6043

The D column reproduces today's regenerated witness **exactly**. So C->D is the
dominant cause and it is settled.

### It is not the ONLY cause — a residual remains

Convention C does not restore July: D is 3.0168 vs July's 3.5423 (~17%), 16O is
50.40 vs 54.60 (~8%). Non-constant, so a second real change. It is **not** in
`closed_form_tau_M.py`, `wedderburn_jones_markov.py` or `binding_canonical.py`
— reverting all three together to `d156e8d50` gives the same C column. Since
`d156e8d50` is 2026-08-02 and the witness is 2026-07-07, the residual lives in
the Jul 7 -> Aug 2 gap in some other file. Unattributed, and smaller than the
convention effect.

(The July witness also has **no 3He and no 4He rows** at all — bean qou-48is.
The old table was structurally different too, not just numerically.)

### The degradation was known and recorded AT THE TIME

`markov_z`'s own docstring says it outright:

> "NOT decided by which value matches experiment. For the record it does NOT
> flatter the binding table: mean |err| over {2H,3H,3He,4He,6Li,7Li} moves
> 37.39% -> 43.85%. It does fix 2H (+74.85% -> +27.36%)"

My independent measurement over 61 measured rows — median |B_err| 57.6% ->
72.1%, deuteron +59.2% -> -6.9%, 60 of 61 rows worse — is the same phenomenon
on a wider row set. Nothing here is a surprise to the ruling.

The selection is **forced**, not fitted: `lem:feynman-eigenbasis-decomposition`
puts the row cap ell(lambda) <= 2 in the mass channel's own decomposition, and
`markovWeights_eq_jones_of_threeRow_eq_zero` (sorry-free) then makes the
faithful normalised Markov trace unique and equal to q^3/(q^2+1).

## CORRECTION to what I filed earlier

I wrote "nothing catches this". **Wrong** — it was caught, queued, and simply
not done:

- `33a6c7aa4`'s own message: *"96 witnesses still need regenerating; that is
  the next step, not done here."*
- `.work/convention-d-blast-radius.json` lists `mass_table_comprehensive.py` as
  **producer #93 of 146**, reading `y-lambda-mpfr-witness.json` and
  `y-lambda-wenzl-bridge-symbolic-witness.json`, writing this witness.

So this is a **known item on an existing regeneration queue** (qou-c6xo wave-4
sweep, qou-lt8x blast-radius gap), not an undetected regression. What is new
here is only the measurement of how far this particular one moved.

Worth flagging to qou-c6xo: that sweep ran `--timeout 900`, and this producer
now takes **657 s**. It is inside the timeout but no longer comfortably, and
the cause is the 11.5x above — the two findings interact.

## "Are other masses that bad?" — NO. Masses are fine; this is one crude channel

The 70% figure is the **symbolic binding** column only. Everything else:

    m_p, m_n in THIS SAME TABLE      938.272089 / 939.565423 vs CODATA
                                     938.27208943 / 939.56542194   -> ~ppb
    canonical-mass-table-extended    D +1.09%, T -0.156%, 3He -2.97%, 4He +5.87%
    this table, MASS err% (symbolic) 0.53%  -> 0.66%
    this table, MASS err% (q-CLT)    UNCHANGED — bit-identical, 0 of 63 rows moved
    this table, BINDING err% (sym)   57.6% -> 72.1%     <- the only 70% anywhere

The nucleon masses are at ppb *inside this very witness*. The q-CLT mass column
did not move at all. The convention change touched exactly one channel: the
symbolic binding `B = -alpha * ln|tau_M|` with `alpha = m_e * 8 * G`, which is a
much cruder object than the canonical binding chain.

So "masses were improving" is correct and untouched by any of this.


---

# The 11.5x: mechanism, and the remedy options

## Mechanism

`pyhecke.atom.atom_per_generator_volumes` builds the atom's braid word and sums
per-generator Wedderburn volumes. Before `efcaf79ed` the braid word and
`pyhecke.gram.h` were Python floats, so that inner arithmetic ran as C doubles
at ~ns/op. After, they are mpf, so it runs in Python at ~us/op — and because
some operands stayed float, **every operation also pays a conversion**:

    per 400 rows            per row
    2,724,573  __mul__      ~6,800     mpmath multiplications
    1,753,032  convert
    1,126,208  from_float   ~2,800     float -> mpf conversions

80% of total runtime (20.6 s of 25.7 s over 400 rows). Confirmed by swapping
only that one file: 14,972 rows in <150 s at `efcaf79ed^`, 5,615 at HEAD.

**It is not precision.** dps 18 vs 70 is a 1.6% difference; mpmath 1.3.0 vs
1.4.1 is 1.16x. It is the op COUNT and the per-op Python overhead.

## The complication that should drive the decision

`atom_per_generator_volumes` carries a **KNOWN BUG banner** in its own
docstring: it uses hardcoded H_3 Wedderburn weights regardless of atom size,
so for every A > 1 atom the weights are systematically wrong
(docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md). The canonical
replacement `mass_at_3A_proper.per_generator_V_hat_3A` exists; the migration is
queued and not done. That is the DeprecationWarning this producer emits ~15,000
times per run.

So we are now paying an 11.5x precision premium to compute a quantity that is
already known to be wrong for every composite atom. Whatever is chosen below,
that pairing is the thing to look at first.

## Options

**A. Accept.** The precision fix is correct and the affected producers are
diagnostics. Cost: 31 call sites got ~11.5x slower, and the qou-c6xo wave-4
sweep's `--timeout 900` no longer has comfortable headroom (this producer:
657 s). Zero work, but the sweep gets fragile.

**B. Hoist the constants (free win, no value change).** 2,800 `from_float`
calls per row means float and mpf operands are mixed inside the loop. Lifting
the loop-invariant constants to mpf once at module scope removes the conversion
without changing a single value. Bounded by the profile: `from_float` +
`convert` are ~7.5 s of 25.7 s, so the ceiling is roughly 1.4x. Cheap, safe,
and it does not need a ruling — but it does not get the 11.5x back.

**C. Memoize.** 14,972 calls with only (Z, N) varying. If the per-generator
volumes depend on a coarser key than (Z, N) — braid shape, crossing count, A —
the cache collapses most of the calls. **Unmeasured**: I have not checked how
large the distinct key space actually is, and if it is ~14,972 this buys
nothing.

**D. A declared float64 tier (my recommendation for the scanning consumers).**
Add `allow_float64=True`-style opt-in so a consumer that is scanning 14,972
nuclei at 0.5% accuracy can take the f64 path, while the precision consumers
keep mpf. This is **already the idiom in this file** — `reject_float64_q` has
exactly that escape, and the raw-float64 audit already honours a declared
`precision_tier='float64-integrator'` carve-out. The NO-FLOAT64 directive
exists to stop *laundering* f64 as high precision; a declared tier is the
sanctioned opposite of laundering. Recovers the full 11.5x for the consumers
that genuinely do not need 50 dps.

**E. Vectorize with numpy.** Effectively blocked — the numpy/mpmath dtype-leak
gate exists because an mpf in a numpy array demotes it to dtype=object and
leaves BLAS (bean qou-5qwb, measured at ~4000x). Only viable after dropping to
f64, which is option D.

## Recommendation

**D for the scanning consumers, plus B as a free win**, and measure C before
building it. Not A alone: the sweep-timeout headroom is real and this producer
already sits at 657 s of a 900 s budget.

But the prior question is whether `atom_per_generator_volumes` should be on the
critical path at all, given its own H_3-vs-H_{3A} bug banner. If the
`mass_at_3A_proper` migration is going to happen, tuning the deprecated
function first would be wasted work — that ordering is an owner call, which is
why this is filed rather than fixed.
