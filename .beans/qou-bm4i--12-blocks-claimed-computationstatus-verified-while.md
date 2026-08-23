---
# qou-bm4i
title: 12 blocks claimed computation.status verified while their witness FAILED — status corrected, the mathematics is not
status: todo
type: task
priority: normal
created_at: 2026-08-23T12:22:58Z
updated_at: 2026-08-23T13:38:29Z
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
