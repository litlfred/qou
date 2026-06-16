# Recursive ρ_ξ for A ≥ 3 is blocked by underdetermined H_9+ extracts

**Date:** 2026-05-18
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Context:** user requested "implement recursive ρ_ξ for A >=3 as infra"; this audit documents why the naive direct-eval implementation fails and what real closure looks like.

## TL;DR

The naive recursive ρ_ξ via `evaluate_word_matrix_np` on the (A-1)-nucleon prefix DOES NOT close — the A^λ_{ξν}(I) extracts at H_9, H_12, H_15, H_18 are **rank-deficient least-squares fits**, not universal interface operators. They work for A=2 (deuteron) because the H_6 extract is full-rank (rank == n_unknowns for every λ ⊢ 6). They fail for A≥3 because the H_9 extracts are far from full rank.

| Hecke level | λ representative | n_unknowns | rank | full rank? |
|------------|-----------------|-----------:|------:|------------|
| H_6 (deuteron, inner = H_3 single nucleon) | (3,2,1) | 32 | **32** | ✓ |
| H_9 (A=3, inner = H_6 deuteron) | [4,3,1,1] | 3390 | 66 | ✗ |
| H_9 | [5,3,1] | 2516 | 65 | ✗ |
| H_9 | [3,2,2,1,1] | 3000+ | 66 | ✗ |

Empirically:

| Atom | Direct-eval |tr_M| | markov_peel reference | rel_err |
|------|---:|---:|---:|
| D | 0.388286471547710 | 0.388286471547713 | **7×10⁻¹⁵** ✓ |
| T | 0.060205 | 0.104052 | **42 %** ✗ |
| ³He | 0.163198 | 0.206541 | **21 %** ✗ |

## Root cause

The H_9 extracts are produced by `A_operator_extract_at_level.py`:

1. Generate ~144 test words at H_3 covering the **single-nucleon-block** family.
2. For each (λ, ξ, ν), build a bilinear system M·vec(A) = b from those test words.
3. Solve by least-squares; report `rank` and `max_relative_residual`.

When `rank < n_unknowns`, the system is **underdetermined**: many A matrices give the same χ^λ over the test set. The least-squares solver returns the min-norm solution, which IS valid for the test family (H_3 single-nucleon inners) but is NOT the unique universal interface operator.

When we use the same A^λ_{ξν}(I_9_{nn}) with a different inner family — specifically, a 2-nucleon deuteron at H_6 — the min-norm A predicts a different χ^λ than the universal A would. That's the 21-42 % error on T and ³He.

H_6 extracts are full-rank because the underlying 144-test-word set fully determines them — H_3 inner family has small representation dimensions.

## Why this matters for Track B

The v6 workplan / canonical_tr_m_via_branching.py docstring assumes the H_9 extracts are universal. The 0b/M_N workplan and #708 PR refer to this combiner as a fast path for A≥3. **The combiner is only validated for A=2.**

The pre-existing comment in `canonical_tr_m_via_branching.py` line 218 said "extending to A ≥ 3 requires a recursive branching pass" — but the issue is upstream of that: even a *non-recursive* direct-eval ρ_ξ at H_6 plus the existing H_9 extract gives wrong answers, because the H_9 A^λ matrices are not universal.

## Closure paths (concrete)

### (a) Regenerate H_9+ extracts with adequate test-word coverage

For each (λ, ξ, ν) triple at H_n, the bilinear system has n_unknowns = d_ξ · d_ν · K (where K is the support size). To make it full-rank, generate ≥ n_unknowns test words **that span the inner-family structure** (specifically, 2-nucleon deuteron-like words at H_{n_inner}, not just H_3 single-nucleon words).

| Hecke | Max n_unknowns | Test words needed |
|-------|---:|---:|
| H_9 | ~3390 (λ=[4,3,1,1]) | ≥3500 |
| H_12 | exponentially larger | ≥10000+ |
| H_15 | astronomical | infeasible |

Cost grows fast. **Practical for H_9, marginal for H_12, intractable for H_15+.**

### (b) Build matrix-form recursive ρ_ξ

Instead of fitting A from data, derive A^λ_{ξν}(I) **analytically** from the Hoefsmit / seminormal embedding V_λ ↪ V_ξ ⊗ V_ν (Littlewood–Richardson coefficients + Wenzl 1988 explicit branching matrices). This makes A universal by construction.

Cost: substantial implementation work (~500 lines + verification against known A=2 deuteron). Reusable for any A.

### (c) Bypass the combiner: use `markov_peel` for inner |tr_M|

For A=3, 4 just call `markov_peel.tr_M_atomic(Z_inner, N_inner)` to get the inner |tr_M| as a symbolic expression in q, then evaluate at q_0. This works at any A but doesn't accelerate.

**This is what's already happening** — `markov_peel.tr_M_atomic(2, 2)` returns ⁴He in 8.5s at 50 dps (v6 workplan). The combiner was supposed to be faster (~1s); it isn't because A=3 is broken.

### (d) Hoefsmit direct at full H_n

For A=3 (H_9), the Hoefsmit per-partition Markov trace via `mass_at_3A_proper.markov_trace_3A` works in seconds at f64. For A=4 (H_12), 12s at f64.

This is the path the existing `mass_at_3A_proper` was designed for. The combiner was meant to replace it; until (a) or (b) lands, Hoefsmit-direct stays as the canonical A=3, 4 path.

## Implications for the v7 workplan

| Track | Status post-this-audit |
|-------|--------|
| Track B "recursive ρ_ξ for A≥3" | **BLOCKED** by underdetermined extracts; not a code-level fix |
| Operator-valued combiner usability | A=2 only (deuteron); production fast path for A≥3 not viable until (a) or (b) |
| Path-independent canonical |tr_M| for {p, n, D, T, ³He, ⁴He} | **AVAILABLE** via chi-cache (50 dps) and markov_peel; the combiner isn't on the critical path |
| Option E (Kashiwara crystal) for Δ_λ closure | **already failed** per `rho-k-h3a-crystal.witness.json` — c_λ(q) = s_λ(1, q, …, q^{n-1}) gives M_pred(D) = 2796 MeV vs 1876 target (closure_err 920 MeV; ratio −412×). Option E variants with q→1 limit also fail (171 MeV closure_err). |

## Recommendation

1. **Mark canonical_tr_m_via_branching A=2-only** in the file docstring and v7 workplan (DONE).
2. **Open issue / queue item** for closure path (a): "extract regen for H_9 with ≥3500 test words covering deuteron-inner-family". Mark as **infrastructure follow-up**, not blocking 1ppb.
3. **For Track A / per-isotope formula work**, use the chi-cache witness as the canonical |tr_M| source. The combiner does not appear on the critical path until (a) or (b) lands.
4. **For Option E (Kashiwara) revival**, don't pick up the existing `rho_k_h3a_crystal.py` path — its failure mode is structural (the crystal weight gives wrong sign and magnitude). Look instead at the Demazure subcrystal cardinality |B_w(λ)| for non-w_0 elements, or at the KL canonical basis weights — but these are **research-grade conjectural ansätze**, not closure infrastructure.

## Cross-references

- [`computations/canonical_tr_m_via_branching.py`](../../computations/canonical_tr_m_via_branching.py) — combiner, now correctly returns None for A≥3
- [`computations/a_operator/A_operator_extract_at_level.py`](../../computations/a_operator/A_operator_extract_at_level.py) — extract generator
- [`computations/markov/markov_peel.py`](../../computations/markov/markov_peel.py) — canonical inner |tr_M| (workaround)
- [`computations/rho_k_h3a_crystal.py`](../../computations/rho_k_h3a_crystal.py) — Option E (failed)
- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — Δ_λ gate + Path A/B/C/D split
- [`docs/audits/2026-05-18-1ppb-workplan-v7-100x-experimental.md`](2026-05-18-1ppb-workplan-v7-100x-experimental.md) — workplan
