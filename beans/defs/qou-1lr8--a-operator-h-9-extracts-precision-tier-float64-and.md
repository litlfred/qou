---
# qou-1lr8
title: 'A-operator H_9 extracts: precision_tier float64 — and the two wrong reachability answers I gave first'
status: in-progress
pr: 8190
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T07:32:44Z
updated_at: 2026-11-16T20:28:40Z
parent: qou-9nnz
---

## The question

The four H_9 A-operator witnesses are 80,578 raw float64 fields — 63 % of the
live backlog after the 2026-08-28/29 drain arc took the corpus from 487,597 to
127,388. They are `engine: numpy`, `np.linalg.lstsq` on dense complex systems
with residual ~1e-14: a genuine float64 COMPUTATION, not a float64 exit.

    A-operator-extract-h9-pp                22,750
    A-operator-extract-h9-pn                22,738
    sublemma-2-1-A-operator-extract-h9-pn   17,559
    sublemma-2-1-A-operator-extract-h9-nn   17,531

## An mpmath rewrite is not available at any budget — measured

`mp.qr_solve` at 50 dps on complex matrices:

    n_unknowns   64     96    128    192
    seconds    2.62   8.91  21.32  76.65

Fitted exponent **3.07** (clean cubic, as QR should be). Real block sizes come
from the witness: 30 blocks, largest **3,390** unknowns. Extrapolated:
**~145 h for one block**, upper bound ~17,000 h across 30 blocks x 4 witnesses.
Robust to the exponent — even at n^2 it is ~500 h.

## I gave TWO WRONG reachability answers before the right one

This is the part worth keeping. The question "does anything scored against
experiment depend on these" got three different answers from three different
instruments, and the first two were mine and wrong.

**Wrong answer 1 — grep, too weak.** `grep -lE "B_AME|M_AME|_MeV"` across the
three consumers returned nothing, and I concluded "nothing scored depends on
these". A grep answers *does this file mention that string*. It cannot see a
dependency arriving through an import.

**Wrong answer 2 — import cone, too strong.** A BFS over import edges (3,352
modules, seven production seeds) found

    canonical_mass_table_extended -> canonical_tr_m_via_branching

a DIRECT import, one hop, into a file with 31 AME/MeV references that the
corpus calls canonical for A >= 2. I concluded the opposite: two of the four
are live inputs to a scored mass table. **Module reachability is not code-path
reachability**, and I over-read it exactly as far in one direction as the grep
had in the other.

**The right instrument was reading the control flow**, and bean `qou-8chw`
had already done it. Confirmed on TODAY's code rather than taken from the
record:

    n = 3 * A
    if A < 2:  return ... "branching combiner inapplicable"
    if A >= 3: ... return via the fine-Bratteli transfer   # <-- before the load
    ...
    extract = build_A_extract_at_q(n, iface, q_val)        # line ~584

The extract load is reached only when `A == 2`, so `n` is ALWAYS 6 there. **No
H_9 entry is reachable from `compute_tr_m_via_branching` at all** — only the
H_6 pn deuteron. The mass table cannot see these four.

## qou-8chw's surviving item, now closed

That bean left one thing open: *"the unstamped file IS consumed by
`sublemma_2_1_h9_tritium_verify.py` and `sublemma_2_1_h12_helium_4_framework.py`.
Whether either threads q or is anchor-only is unexamined."*

Measured: **both are anchor-only.** Neither file contains `q_val`, `q0`,
`Q_MP` or `Q_50_DIGIT` anywhere — zero q-threading. They read `A_per_pair` and
use it as stamped. So the hybrid-off-anchor failure mode `qou-8chw` fixed for
the deuteron (+0.0332 vs the transfer's -0.00148, *"not even the same sign,
and it degenerated to the right answer exactly at q_0, so it failed TOWARD
agreement where it is tested"*) cannot arise in either consumer.

`sublemma-2-1-h12-helium-4-framework`'s own witness is a PLAN, not a result:
its data keys are `prerequisite_witnesses`, `all_prerequisites_present`,
`deferred_compute_plan`, `lean_uniqueness_ref`.

## Disposition

`precision_tier: "float64"` + `deprecated`, per the ratchet's own opt-in. The
gate's comment states the test — *"a producer that reaches none of the named
production locations ... is EXPLORATORY"* — and the control-flow trace above
is exactly the `not_production` evidence it asks be put on the record rather
than taken on faith.

NOT `float64-integrator`: that tier means f64 by construction with no
higher-precision source. Here a 50-dps source exists and numpy was simply
cheaper for the matrix algebra, which is the blur that carve-out's own comment
says it must be designed against.

## What I am NOT doing, and why the premise dissolved

I had proposed extending `build_A_extract_at_q` to cover `pp` and `nn` — it
covers only `pn` (`if interface != "pn" or n_outer % 3 != 0: return None`,
line 154). Under wrong answer 2 that looked like the real fix: kill 40,281
live float64 fields and retire a known-bad frozen path.

It is unmotivated. H_9 is unreachable from the mass table whatever the
interface, and the two real consumers are anchor-only, so extending the closed
form would serve no reachable code path. Recorded so the next reader does not
re-derive the idea and act on it.

## Progress Update (2026-11-16, PR #8190)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/Float64EngineReachabilityAndGramInverse.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/float64_engine_reachability_and_gram_inverse_probe.py` and stamped witness `computations/probes/float64-engine-reachability-and-gram-inverse.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 2ed61761fb447e7b912df4f3ef73e8603236969a`).
- [ ] Awaiting merge of PR [`litlfred/qou#8190`](https://github.com/litlfred/qou/pull/8190) (`345a3f9ff4ba913bb465b8884e861bfccde997ca`).

