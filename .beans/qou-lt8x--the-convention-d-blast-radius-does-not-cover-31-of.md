---
# qou-lt8x
title: 'The convention-D blast radius does NOT cover 31 of the 43 structurally-C witnesses: read-set != write-set'
status: in-progress
type: task
priority: normal
created_at: 2026-08-11T01:13:43Z
updated_at: 2026-08-11T01:14:12Z
---



## The gap

`.work/convention-d-blast-radius.json` was built by one question — *which
producers **read** one of the four witnesses the D migration moved?* (146
producers, 188 witnesses). The campaign then treated that queue as the
convention-C work list.

It is not. Measured against the content detector:

| | |
|---|---|
| structurally-C witnesses (`convention-c-witness-audit.py --list`) | 43 |
| of those, written by a blast-radius producer | **12** |
| **not reachable by the sweep at all** | **31** |

Reading a moved witness and *being* convention C are different properties.
A producer can carry convention C entirely on its own — the `chi-*-at-q0-50dps`
family, the `rho-k-h3a-*` siblings, `a-K-via-lp-dual` — without reading any of
the four. The sweep cannot fix what it never visits, and it exits reporting
success.

This is the same shape of error as the two that came before it, one level out:

- fingerprint list ⇒ finds only `n = 3` (reopened `qou-eea0`);
- content tests ⇒ miss derived-value witnesses (`qou-8x1l`, fourth class);
- **read-set queue ⇒ misses producers that are C on their own.**

Each detector was correct about the property it tested and was then used to
answer a question it does not answer.

## Complement, resolved

`.work/convention-c-complement.json` — 31 witnesses, producer resolution
attempted for each. 18 resolve to a live producer and are runnable:

    aK_via_lp_dual{,_full}, alpha/alpha_k_jones_markov_h12,
    binding_a3plus_{full_theta_assembly,joint_ji_combiner},
    categorical_bypass_volmatch_demo, chi_4he_binding_lossless,
    chi_at_q0_via_hoefsmit_mpfr (x3), derived_chi_catalogue_build,
    habiro/habiro_h9_spectral_decomposition, probe_1b_li6_orthogonality,
    probe_option_e_phase2_crystal_vertex_candidates,
    probe_pauli_young_delta_lambda_the3_signtest,
    rho_k_h3a_{co_casimir,counit_canonical_integral,frobenius_pairing}

13 do not, in three kinds:

| kind | count | witnesses |
|---|---|---|
| **Rust binary** | 4 | `rust-chi-q-via-gp-lossless`, `matrix-m-chi-q-via-gp` — the layer `qou-j6il` found returning C while its source read D. Do not regenerate before the convention gate reaches the binary. |
| producer in `_deprecated/` | 6 | the `y-lambda-*` / `wenzl-y-lambda-h{9,12}` family — `qou-8x1l` already showed "retire it" is unsafe here, since six live producers read them |
| no `scriptFile` at all | 3 | `chi-dineutron-h6`, `chi-diproton-h6`, `rho-w-crystal-vertex-trace` |

## To close

1. Run the 18 resolvable producers (serially, same harness, own journal).
2. Re-run `--list`; the 13 should be all that remains, each with a recorded
   reason rather than an omission.
3. Fix the queue-construction defect itself: the work list should be the
   **union** of (reads a moved witness) and (fails a content test), not either
   alone. Both are already computable.

## The native work list already asks the right question (2026-08-11)

The harness's own `work_list()` is keyed on **being** convention C — the
three content tests — not on reachability. The `--from blast-radius` override
is what substituted the wrong question; the default was correct all along.

Measured programmatically (importing `work_list()`, not grepping `--plan`):

| | |
|---|---|
| native `work_list()` | **67** witnesses — 41 with a producer, 26 orphan |
| this bean's complement | 31 |
| complement already in native | **27 / 31** |
| in complement, NOT native | **4** |

So the resolution is not to merge two queues: it is to **drop `--from` and run
the harness natively**. The complement was a symptom of the override, and 27
of its 31 entries were never outside the real list.

The four genuinely outside it need explaining before any sweep claims
completeness — a structurally-C witness absent from a convention-C-keyed work
list is either a `_deprecated/` exclusion, an unparseable doc, or a detector
disagreement:

    computations/binding-a3plus-full-theta-assembly.witness.json
    computations/binding-a3plus-joint-ji-combiner.witness.json
    computations/chi-helium-4-h12-numeric.witness.json
    computations/probe-option-e-phase2-crystal-vertex-candidates.witness.json

(`chi-helium-4-h12-numeric` is already documented in
`computations/_deprecated/README.md` as a live input with no producer — the
mis-filed-orphan case — so at least one of the four has a known cause.)

### A measurement error worth recording

First attempt at this comparison grepped the `--plan` stdout and reported
"16 of 31 missing". That was wrong: `--plan` prints producers as
`producer -> N witness(es)` and names witnesses **only** on ORPHAN lines, so
any witness owned by a producer was invisible to the grep. The real number is
4. Same shape as the defects this bean is about — measuring the artifact
instead of the property — which is why it is written down rather than quietly
fixed.

## Roots vs derived — what re-running can and cannot fix (2026-08-11)

The sweep's negative (11/41, not one witness moved C -> D) has a structural
explanation. Splitting the 44 producer-owned convention-C witnesses by whether
their producer READS another convention-C witness:

| | |
|---|---|
| ROOTS — producer reads no C witness | **29** |
| DERIVED — producer reads C | **15** |

Re-running can only fix a ROOT. A derived witness reproduces C faithfully
however many times its producer runs, because the C enters through its input.
That is why 41 green `ok`s would not have been a migration.

The 29 roots are the actual front:

    all-nuclides-wedderburn-spectral-v2   alpha-k-jones-markov-h12/h3
    binding-k-enumerator                  bond-extensivity-equal-weight
    categorical-bypass-volmatch-demo      chi-helium-4-h12-at-q0-50dps-binding
    chi-lithium-5-h15 / -6-h18            chi-tritium-h9-at-q0-50dps-matrix-m
    derived-chi-catalogue                 deuteron-tower-fusion-frame-probe
    e0-lambda-composite                   entanglement-orders
    gram-matrix-dual                      h2o-bond-angle-magnitude-vsepr
    markov-z-fibre-rank-bar-covariance    option-e-phase1-h3-cross-check
    pentagon-to-borromean-h4-probe        per-irrep-pole-deuteron-h6 / -proton-h3
    probe-1b-li6-orthogonality            q-hecke-seminormal-character-closure-probe
    qbeta-c3-barodd-binding-sdp-dual      qbeta-counit-substrate-consistency
    rho-k-h3a-refinement                  tr-m-q-hecke-seminormal
    v-hat-z-transfer-phase5d-4            weight-factor-audit

But note the sweep already re-ran several of these (alpha-k-jones-markov-h3,
bond-extensivity-equal-weight, weight-factor-audit, all-nuclides-...) and they
stayed C. So being a root is necessary, not sufficient: those producers carry
convention C **in their own code**, not in an input. Fixing them is a source
edit, like the `z_sym` one-liner in `y_lambda_wenzl_bridge_extended.py`, not a
re-run.

The correct sequencing is therefore: fix root PRODUCERS at the source, re-run
them, then let dependency ordering carry it to the 15 derived. A sweep that
re-runs everything in place cannot do this and should not be launched again as
though it could.
