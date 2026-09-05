---
# qou-sv7h
title: 'Binding compute cannot scale: sparse path unreachable, zero Rust, float64 straddle'
status: in-progress
type: task
priority: high
created_at: 2026-08-30T15:41:58Z
updated_at: 2026-09-05T06:36:07Z
---

Full measured analysis: `docs/audits/2026-08-30-binding-compute-scaling-bottleneck.md`.

Blocks `qou-i7ju` (hadron-knot-table regeneration). The regeneration is not the
problem; the producer cannot finish its second atom.

## Localisation

Every stage of `compute_atom` is sub-millisecond except `binding_energy`.
Inside it, `unified_iterative_correction` is the whole cost. 11/11 py-spy
samples on `hecke_core_legacy.py:1102` = `np.asarray(A) @ np.asarray(B)`.

## The six findings

1. **The O(dim*nnz) sparse path is unreachable.** Guard is
   `if s['sparse'] and not exact_chain:`, and `exact_chain` is True for EVERY
   physical chain (measured over all nucleon/prev/n_gens combos). Coefficient
   histogram: ('int','int') 132, ('int','mpf') 132, ('float','float') 48 -- the
   mpf are real 50-dps values, and `c` is int 1 which is not a float. So both
   inner branches are dead, INCLUDING the COO object accumulator written for
   exactly this case. Everything runs O(dim^3) at dims up to 2310.
   Deuterium ~40 days; Fe-56 ~16 years.
2. **Zero Rust in the hot file.** grep pyhecke_native|hecke_engine in
   hecke_core_legacy.py -> 0 hits.
3. **The Rust MPFR matmul exists and is not exported.**
   `dense_dense_mul_mpfr` in dense_la_mpfr.rs, called 16+ times inside Rust,
   has no #[pyfunction]. Python gets inverse/kron/nullspace but not multiply.
   Measured Rust speed >=24x the Python path at dim 16 (401us vs 9600us), and
   that is a lower bound (includes PyO3 + seminormal construction).
4. **Half the matmuls are float64.** Counter recorded
   {'float64': 275, 'object': 271}. Measured relative error vs an all-mpf
   reference: 1.40268e-16 = float64 eps, in a 50-dps producer. Also
   `q_parameter.Q` and `h` are Python floats; intra-nucleon coefficients are
   50-dps mpf but the inter-nucleon nn crossing carries float64 -h. A straddle
   inside one product.
5. **The `dim >= 8` numpy branch is a pessimization.** Its docstring claims a
   speedup; measured at dim 16 it is 31% SLOWER than the Python loop
   (0.0126s vs 0.0096s). object dtype has no BLAS.
6. **The q-Gaussian tier is dead.** k_exact defaults to k_max, so
   active_gaussian is empty (measured: 193 exact, 0 gaussian).

## The one-line fix is necessary but NOT sufficient -- TESTED

`if s['sparse']:` was applied and run. py-spy confirms it takes the COO path
(lines 1495/1500, no _matmul_dim). Deuterium STILL had not completed after
11 minutes. Complexity drops ~500x at dim 2310 but every scalar op is still a
Python-level mpmath call. Both layers must be fixed.

**Patch was reverted, not committed.** With neither version completing there is
no way to verify it preserves the number, and this is a binding-energy producer.
Landing it needs a value-equality check on a subset that completes both ways
(use k_exact to shrink the partition set; do NOT use deuterium).

## Order of work

1. Fix the guard (one line, ~500x) -- with the equality check above.
2. Export dense_dense_mul_mpfr via PyO3, route _matmul_dim + the COO
   accumulator through it (>=24x, on top of 1). This is what makes higher
   isotopes reachable.
3. Fix the precision straddle: Q and h as mpf from Q_50_DIGIT_STR; stop
   seeding accumulators with np.eye / 0.0. Correctness, independent of 1-2.
4. Delete the dim>=8 numpy branch.
5. Decide the q-Gaussian tier: real default below k_max, or delete.

## Scaling law

Partition set is FIXED (193 at k<=11, dims 1..2310; 37s just to materialise) --
it does not grow with A. Crossings grow O(A^2). Cost ~ A^2 * sum_lambda f(dim),
f = dim^3 today, dim*nnz after fix 1. Relative to deuterium: Li-7 ~5x,
O-16 ~17x, Fe-56 ~144x.


---

## CLAIMED 2026-09-05 — branch claude/rag-document-ingestion-options-orasrw

Taking the SIGN question specifically, on owner direction. The prior session
(`session_01Cb9sX3NisBDY4WN4z5wJL4`) last committed 2026-09-03; this bean is
still `todo`, so this is a claim on an unclaimed item rather than a takeover.

**Scope I am taking:** why `unified_iterative_correction` is negative. Its own
commit `815b2a46a0` says "nothing here says WHY the sign is wrong -- that is the
physics question this measurement opens and does not answer."

**Scope I am NOT taking**, so it stays available: 6Li / A>=6, which
`aaa2ef9c51` names as the discriminating measurement for the extensive term's
SHAPE. That is a different question from the sign and ~5x deuterium's cost.

**Route:** formalize-first, per AGENTS.md STRICT — locate where the sign is
DETERMINED in term 1 and ask whether it is forced, rather than scanning. The
strongest existing evidence that it is structural is this bean's own: the
accumulator is negative on BOTH matrix families (old braid-violating: -0.0319
at k=4 to -2.1955 at k=8; corrected: -0.0896 to -2.0200), so it survives a
change of the underlying representation.

**Falsifier stated in advance:** if the sign traces to a free choice — an
orientation, a w_0 convention, an ordering of the LP objective — then it is not
structural and this framing is wrong.
