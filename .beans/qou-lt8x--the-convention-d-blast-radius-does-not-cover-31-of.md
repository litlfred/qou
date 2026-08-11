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
