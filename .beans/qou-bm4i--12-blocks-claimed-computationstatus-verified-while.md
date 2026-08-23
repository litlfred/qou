---
# qou-bm4i
title: 12 blocks claimed computation.status verified while their witness FAILED — status corrected, the mathematics is not
status: todo
type: task
priority: normal
created_at: 2026-08-23T12:22:58Z
updated_at: 2026-08-23T16:31:47Z
---

MEASURED + FIXED 2026-08-23 (`cd19e98ac8`). This bean tracks what the fix did
**not** do.

`ComputationStatus` is explicit — `"verified"` = witness matches expected values
within tolerance, `"failed"` = it does not — and **nothing compared the two**.
No Zod constraint, no sweep, no CI step. Of 166 blocks marked `verified`, **12**
cited a witness whose own top-level `allPassed` is false.

The status field is corrected on all 12 and a gate now exists
([`scripts/check-computation-status.py`](scripts/check-computation-status.py),
wired into `check-sidecars.sh`). **The mathematics is untouched**, and some of it
needs a real look:

| block | what its own witness says |
|---|---|
| `prop:he4-two-row-dominance` | computes `tr_M(β_⁴He)(q₀) = 0.16097` vs the **0.05534835** the block states, tol 5e-07 — a **factor of 3** — plus 8 more failing assertions |
| `conj:gs-graded-markov-trace-existence` | `tr_M_at_q0_archimedean` fails for **both** proton and neutron |
| `prop:h2-lp-dual-binding` | "H2 binding energy within 5% of observed (no calibration)" fails |
| `prop:gram-matrix-h3-symbolic` | `gram_h3_symbolic_matches_pyhecke` fails |
| `prop:q-beta-c-2-eq-neg-one-structural` | `alpha_q0_matches_probe_n3_witness`: 5.82e-09 against a **1e-30** tolerance |
| `rem:hadron-level-knot-table` | `LP_stable` fails for c14, o16, ne20, si28, ca40, fe56 |
| `prop:mirror-baseline-cancellation` | `slope_10A5_refuted_at_A_ge_5` |
| `conj:binding-qbeta-complex-volume` | `c2_gate`: computed 0, expected 1, tol 0 |
| `prop:markov-trace-axiomatic-closed-form` | `anti_self_reciprocal`, `symmetric_under_q_inv` |
| `prop:deuteron-fusion-frame` | assertions not in dict form; `allPassed` false |
| `prop:y-lambda-cyclotomic-factorization` | `denominator_factors_as_cyclotomic_product` |
| `conj:h2s-angle-s3-braid-holonomy` | the +2.1° residual is not bar-antisymmetric as claimed |

## What each needs, and it is not one job

Three different dispositions are mixed together here, and telling them apart is
the actual work:

1. **The block's stated number is wrong** — ⁴He is the clear case. Either the
   witness is right and the block's `0.05534835` must change, or the producer
   regressed. Either way something in the corpus is currently false.
2. **The assertion's tolerance is unreachable** — `1e-30` on a float pipeline is
   not a physics claim, it is a gate nobody can pass. Per AGENTS.md that must be
   fixed at the producer, **never** by widening the baseline.
3. **The assertion encodes an expected NEGATIVE** — `slope_10A5_refuted_at_A_ge_5`
   reads as "this is refuted", and a refutation that holds should not be an
   `allPassed` failure. That is an assertion-authoring defect, not a result.

Do **not** batch-resolve these. (1) is a correctness bug, (2) is a producer fix,
(3) is a naming fix, and only (1) changes what the paper claims.

## Why it went unnoticed

`status` is author-set metadata that reads exactly like a machine verdict.
Nothing downstream distinguished "an agent typed verified" from "a checker
concluded verified". The gate closes that.

**The semantic half stays open and is not machine-checkable**: `verified` says a
script ran and its own assertions passed — not that the script tested the
proposition the block states. Worked instance in `qou-lrnd`:
`habiro-frobenius-probe` asserts the Galois norm is an integer, while the block's
Lean assumes a constant collapse to a value that appears nowhere in the witness.


---

## ⁴He CLOSED (`a107525051`) — 11 of 12 remain

`prop:he4-two-row-dominance` is fixed end to end: block prose, producer
constants, witness, and status.

**The diagnosis, since it generalises.** Installing the missing scientific
stack and re-running the producer reproduced the committed witness
**byte-for-byte** — so the witness was current and the block stale, not the
other way round. Then, per assertion:

* Hoefsmit characters `χ^λ` **agree** with the old table to 3+ digits;
* only `y_λ` differs, by a **non-uniform** factor of 2.66–4.04.

Non-uniform rules out a normalisation — it is a **different formula**. This is
the `y_λ` / `w_λ` / `w̃_λ` conflation AGENTS.md warns about, caught in the wild.
The q₀ re-pin was also ruled out by arithmetic: 11.5 ppb cannot move a smooth
function of q by 190 %.

**The proposition got stronger, not weaker.** The two-row ratio is not 86.6 %
but **exactly 1** — all 70 partitions with more than two rows contribute 0. The
≥ 80 % claim holds and λ* = (9,3) is unchanged. Only the table was wrong.

**Method worth reusing on the other 11**, in this order:

1. Install what the witness's `environment` block records, then re-run. If the
   producer reproduces the committed witness, the *block* is stale — which
   settles the direction before any editing.
2. Compare assertion by assertion. Which quantities agree pins the fault: here
   χ agreeing and only `y_λ` moving localised it to the weight family in one
   step.
3. Check whether the ratio is uniform. Uniform ⇒ normalisation; non-uniform ⇒
   different formula. Different fixes.
4. Regenerate tables **from the witness**, never by hand.
5. Restore provenance before committing a witness. The first re-run here would
   have dropped `clarabel` and `pyhecke_native` and downgraded mpmath. Building
   `pyhecke-native` from source gave `pyhecke_native_build =
   30fd920c241a54fa`, **matching** the original — so the build is identical and
   nothing was lost.

**On CITED_* constants.** Correcting them is not the banned "widen a baseline to
make a red run green": they are the producer's snapshot of the block's *prose*,
and the check is "does the block still match the computation". Tolerances were
untouched (5e-07 on tr_M, 0.15 on the percentages) and the mismatch was fixed at
its source. If a future case tempts you to move a *tolerance* instead, that is
the banned move.


---

## `conj:gs-graded-markov-trace-existence` — diagnosed, NOT fixed. It is import-cone drift, and it is the documented one.

Second of the 12. Different failure mode from ⁴He, and the answer is "do not
touch this witness".

**First, a near-miss of my own.** The recorded tolerances read `9.2323329` and
`1.0653062`, which look enormous beside a 6.7e-8 difference — I was one step
from reporting a broken comparator. My own display had truncated the string at
9 characters and eaten the exponent: they are `9.232332971861535e-10` and
`1.065306228613167e-09`. The assertions fail honestly, by **72.9x** and
**79.2x**.

**What is actually being compared.** Two independent pipelines evaluate
`tr_M(q_0)`:

    realizer  markov-substrate-realization.witness.json   computed 2026-06-22
    term6     term6-full-pole-sum.witness.json            computed 2026-08-10

Seven weeks apart. They agree to 7.3e-8 (neutron) / 7.9e-8 (proton) against
`AGREEMENT_RTOL = 1e-9`. Both values are stored as float64, whose floor is
~1e-16, so the gap is real arithmetic disagreement, not rounding.

**Re-running the realizer makes it worse, and that is the finding.**

    atom        committed (Jun)   fresh re-run (today)    move
    proton         1.0653062          1.1457597          +7.5 %
    neutron        0.9232333          0.9877437          +7.0 %
    deuteron        (absent)          0.5751722            —

The deuteron's absence is the third failing assertion,
`no_atoms_only_in_term6 = 1`: the June realizer covered 2 atoms, term6 covers 3.

**The producer is byte-identical.** `scriptHash 23130ffe0ffc` in the committed
witness matches a fresh sha256 of `markov_substrate_realizer.py` exactly. So
nothing in the producer changed — something it *calls* did. That is
**import-cone drift**, and it is not a new instance:

    AGENTS.md: "tr_M_atom moved 0.388 -> 0.575 (48 %) because
                tr_m_atom_via_transfer.py, which computes that quantity, changed."

    measured here: term6 deuteron 0.3882864 -> realizer fresh 0.5751722, +48.1 %

Same numbers, same 48 %. The corpus already documents this drift; this witness
is one of its downstream casualties.

**Deliberately NOT committed.** The regenerated realizer witness was restored to
the committed version. Which side is correct is a research question about the
import cone, not a metadata fix, and AGENTS.md measures this class at ~39 %
actionable — re-running is a diagnosis, not a work order. `status: "failed"`
(set in `cd19e98ac8`) is correct and stays.

**One thing here IS mechanically actionable**, separately from the drift: both
witnesses declare `precisionMetadata: {compute_dps: 70, output_dps: 60}` while
storing `tr_M_at_q0` as a **bare JSON float** — 16 significant figures, not 60.
Both producers emit the `raw-float64` warning on every run
(`markov_substrate_realizer`: 7 fields; `probe_he4_...`: 108). So a comparison
advertised at `rtol = 1e-9` is being run on values serialised at ~1e-16, and the
witness's own provenance block overstates its precision by 44 digits. That is
the "carry mpmath.mpf from the source, do NOT stringify the float" rule, and it
is worth fixing before anyone tries to adjudicate the 7e-8.


---

## Precision fix landed (`fb3a4009d4`) — and it UNMASKED the disagreement

The `output_dps: 60` vs stored-float64 mismatch is fixed in both markov
producers. Three things came out of it that the bean should carry.

### 1. It was worse than float64

    q_0 = float(CANONICAL_Q)                                   50-digit -> f64
    u_0 = sp.sqrt(sp.Rational(q_0).limit_denominator(10**12))   -> ~12 digits
    float(sp.N(p_val / d_val, 30))                              30-digit eval
                                                                of a 12-digit
                                                                input, then f64

`limit_denominator(10**12)` is the binding loss — it caps the INPUT, so nothing
downstream can recover it. The witness advertised 60 digits and carried ~12.
Now mpf end to end (Horner over exact `domain="ZZ"` coefficients, `fmt` out),
with `set_compute_dps()` in `main` — without that call the conversion is
cosmetic, since `_precision` leaves `mp.dps` at 15 on import.

### 2. The ratchets caught two of MY attempts

* `mp.mpf(q_parameter.Q)` faithfully lifts a **float64** — `Q` is one — so `fmt`
  padded its binary expansion to 60 digits. The float64-padding ratchet flagged
  it as NEW. Fixed with `Q_50_DIGIT_STR`.
* The mixed-arithmetic audit then caught `AGREEMENT_RTOL = 1e-9` as the last
  float in the path. It is a string now.

Neither was baselined or annotated away. Worth recording because the obvious
"lift it with mpf" move is exactly the trap: **`mp.mpf(<float>)` launders a
float64 into something that reads as high precision.**

### 3. The stale witness was MASKING the disagreement

The precision fix does **not** move the value — mpf agrees with the float64 run
on every float64 digit. But re-running with current inputs does, and the
cross-validation goes from an apparent near-agreement to the truth:

    before (Jun realizer vs Aug term6)   7.3e-08 / 7.9e-08
    after  (both current)                6.53e-02  n
                                         7.02e-02  p
                                         3.25e-01  D

The witness was stale on **three independent axes**, which is why:

    q_0 pin     1.1099785955573347 (MUON) -> proton 50-digit. It predates the
                producer's own switch to canonical Q — the exact staleness the
                producer's comment describes.
    precision   ~12 digits -> 60
    inputs      import-cone drift (deuteron 0.388 -> 0.575, +48.1 %)

So the earlier "they agree to 7e-8" was an artifact of comparing two different
epochs. **Two pipelines that exist to cross-validate each other disagree by 7 %
to 32 %.** That is the real state, it is now recorded, and adjudicating it is
research — not attempted here.

Also newly visible: term6 serialises as `0.3882864240747888000000…`. The
trailing zeros are its own float64 deficit, exposed by the realizer's full
width. term6 is the next producer to give this treatment.


---

## RESOLVED (`cb2e2d0ec2`) — and it CORRECTS what this bean said two entries ago

term6 got the same treatment as the realizer. Same root cause: `Q_0` is
`q_parameter.Q`, a float64, and the load-bearing field went through
`float(complex(sp.N(tr_M_expr.subs(q, Q_0))).real)` — where `sp.N` also
defaults to 15 digits, so the loss was independent of the `float()`.

**With BOTH sides exact, the pipelines agree byte-for-byte at 60 digits.**

    markov_pipeline_cross_validator: PASS
      D  realizer=0.5751722439  term6=0.5751722439  rel_diff = 0
      n  realizer=0.9877436881  term6=0.9877436881  rel_diff = 0
      p  realizer=1.1457596925  term6=1.1457596925  rel_diff = 0

`rel_diff` is **exactly 0**, not merely inside `rtol = 1e-9`, and far past the
~16-digit float64 floor. Two independently implemented pipelines agreeing to 60
digits is a genuine cross-validation result — and it was invisible for as long
as either side was truncated.

### Retracting the "7–32 % disagreement"

The entry above says these pipelines "disagree by 6.5 % to 32.5 %" and calls it
"the real state". **That was wrong**, and wrong in an instructive way: it was
measured with the realizer fixed and term6 still stale. The whole history was
epochs, not mathematics:

    7.3e-08    Jun realizer (muon q₀, ~12 digits) vs Aug term6 (float64)
               — two stale values that happened to land close.
    6.5–32.5%  current realizer vs Aug term6. One side fixed.
    0          both current, both exact. The truth.

Every intermediate reading was an artifact. The lesson is narrower than "check
staleness": **fixing ONE side of a cross-validation makes the comparison worse
before it makes it better, and the intermediate number looks like a finding.**
I published that intermediate as a finding. Do not repeat it — fix both sides,
then read.

### The status gate fired in its other direction, correctly

`check-computation-status.py` flagged `conj:gs-graded-markov-trace-existence`
as "failed but every cited witness all-passed" and I flipped it back to
`verified`. First time that arm has fired. Note this block round-tripped
verified → failed → verified inside one day, and each state was correct when
set — which is an argument for the gate, not against it.

### Score

    ⁴He                          block's number was wrong          FIXED
    gs-graded-markov             staleness both sides              FIXED
    remaining                    10 blocks                         open

Both resolved cases were **stale artifacts**, not mathematical errors in the
framework. That is worth knowing before triaging the other ten: the prior
should be "something drifted", not "the physics is wrong".
