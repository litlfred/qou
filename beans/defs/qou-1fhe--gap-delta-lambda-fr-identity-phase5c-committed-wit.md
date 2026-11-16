---
# qou-1fhe
title: 'GAP: delta-lambda-fr-identity-phase5c committed witness disagrees with a fresh run by ~3.85x and the cause is NOT y_lambda'
status: in-progress
pr: 8190
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:15:05Z
updated_at: 2026-11-16T20:28:40Z
parent: qou-9nnz
---

## What is measured

`computations/delta-lambda-fr-identity-phase5c.witness.json` on `main` records values that a fresh run of its own producer does not reproduce. The disagreement is large — a factor of ~3.85 on the `y_λ`-weighted quantities — not a rounding difference.

**The committed witness is self-stale**, by the corpus's own definition: it records `witness.scriptHash 7f4542540f92`, the live producer hashes to `11711368bfb6`, and its `computedAt` is `2026-08-10T01:46:03Z`.

**The move splits cleanly along one line**, and that split is the most useful thing here:

| quantity | depends on `y_λ`? | committed vs fresh |
|---|---|---|
| `z_ratio_tests.empirical_ratio`, `.predicted` | **no** — `τ_M(FULL)/τ_M(CONSTIT)`, `y_λ` cancels | **strict extensions**, 8/8 |
| `z_ratio_tests.tau_M_full`, `.tau_M_constit` | yes | moved |
| `fr_identity_tests.tr_M_Z1`, `.abs_ratio` | yes | moved (D FULL `1.018275 → 0.264566`, ×3.85) |
| `dominant_block_tests.dom_ratio` | yes | moved (`0.502636 → 0.358754`) |

So **the proposition's actual content is unaffected**: the Markov-axiom interface identity `τ_M(β^FULL)/τ_M(β^CONSTIT) = z^(#pos)·(z−h)^(#neg)` is a ratio in which the weights cancel, and its empirical values are strict extensions of the committed float64.

## The obvious cause is REFUTED — do not repeat it

The producer's own docstring records that `load_y_lambda_at_q0` was changed from reading the muon-built `y-lambda-at-q0.witness.json` to calling `y_lambda_at_q0_mpmath` live, as a layer-straddle fix. That is the natural explanation for a `y`-weighted move, and I wrote it down before testing it. **It is wrong.**

Measured, cached witness against a live call at the same `q₀`:

```
y_lambda, SIGNIFICANT entries only (|y| >= 1e-30):
  47 compared, 0 differ by more than 1e-40 relative
  (223 further entries are numerical zero on both sides —
   the cache writes 0.0, the live call writes ~1e-72)
```

The naive comparison reports "223 of 270 differ" and means nothing: those are the numerical zeros. **Do not quote that number.** On every entry that carries magnitude, the cache and the live closed form agree to better than 1e-40. Whatever moved the values, it was not `y_λ`.

## What remains open

The cause is **unidentified**. Remaining candidates, none tested:

- `atom_braid_word_3A` in `mass_at_3A_proper` — the braid word itself. Note that a braid-ordering hypothesis (`qou-hu1f`) was raised for the six-term isotope sweep earlier and **refuted there**; that says nothing about this producer.
- The `(c, d, gen)` → `(sign, gen)` marshalling in `compute_tr_M_decomposition`.
- `partitions_of`, or the `chi_lambdas_braid` batch path itself.
- Import-cone drift generally — the producer's source is only one input; see `witness_import_cone_staleness_audit.py`.

**The usual archaeology cannot settle it here.** This clone is shallow (see `qou-kfeg`): the boundary commit is credited with 45,567 files, so `git log -- <path>` and `git log -S` both return the boundary and nothing else. The question has to be answered by bisecting the producer's import cone against the current tree, not by reading history.

## Status of the record

PR #7104 commits the **fresh** values, because they are what the current producer computes and because the same values arrive from both the f64 and the MPFR paths. That replaces an unexplained old number with a reproducible new one; it does not explain the old one. This bean holds the unexplained part.

## Progress Update (2026-11-16, PR #8190)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/Float64EngineReachabilityAndGramInverse.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/float64_engine_reachability_and_gram_inverse_probe.py` and stamped witness `computations/probes/float64-engine-reachability-and-gram-inverse.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 2ed61761fb447e7b912df4f3ef73e8603236969a`).
- [ ] Awaiting merge of PR [`litlfred/qou#8190`](https://github.com/litlfred/qou/pull/8190) (`345a3f9ff4ba913bb465b8884e861bfccde997ca`).

