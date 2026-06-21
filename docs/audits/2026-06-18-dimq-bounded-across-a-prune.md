# Quantum dimension `dim_q` — killed by bounded-across-A (the last chirality-invariant magnitude candidate)

**Date:** 2026-06-18
**Probe:** [`probes/chirality_delta_lambda_binding_sweep.py`](../../computations/probes/chirality_delta_lambda_binding_sweep.py)
(print-only A-tower sweep; the `sgn·dimq` column is the candidate pruned here)
**Status:** EXPLORATORY / formalize-first prune (per `production-vs-exploratory-discipline`); asserts the
refutation. Δ_λ magnitude remains an open gate (GAP-A-3).
**Discipline:** formalize-first — a structural growth bound prunes a candidate *before* any fit.

## The candidate pruned

The companion T/³He differential diagnostic
([`2026-06-18-pauli-young-delta-lambda-the3-refutation.md`](2026-06-18-pauli-young-delta-lambda-the3-refutation.md),
`probe_chirality_delta_lambda_the3_diagnostic.py`) left the magnitude question boxed by four constraints. The
**proved sign** `Δ_λ = sgn(w₀^{S_λ'})` is icosahedral chirality
([`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md));
the open **magnitude** `|Δ_λ|` must be:

1. **chirality-invariant** (`|Δ_λ| = |Δ_λ'|`) — proved decomposition (#2416);
2. **bounded across A** — `Δ_λ = dim` is known to diverge at A≥6 (#2405);
3. **irreducibly multi-block** — single-dominant concentration refuted by the T/³He mirror ratio
   ([`2026-06-18-sparse-interface-magnitude-the3-prune.md`](2026-06-18-sparse-interface-magnitude-the3-prune.md));
4. **reproduce the T/³He differential** `+1.4947·m_e`.

Two combinatorial-dimension weights satisfy chirality-invariance: `dim` (hook-length) and `dim_q` (q-hook-length
at q₀). `dim_q` is the **best on the differential** (78 % of target vs `dim`'s 57 %), so the live question was:
**does `dim_q` survive constraint 2, or does it diverge across A like `dim`?**

## The parameter-free prune (A-tower divergence)

Evaluating `B_pred = m_e·|Σ_λ y_λ χ^λ(β_atom)·Δ_λ|` across D…⁷Li (categorical, no `C_knot` fit; cross-check
`Δ=sgn·dim` at D `= 0.3801 ≈ 0.380` MATCH):

| iso | A | B_AME | `sgn·dim` | `sgn·dimq` | `dimq` vs AME | `dimq`/`dim` |
|---|---|---|---|---|---|---|
| D   | 2 | 2.225  | 0.380   | 0.401     | undershoot 5.5× | 1.05× |
| T   | 3 | 8.482  | 1.909   | 2.504     | undershoot 3.4× | 1.31× |
| ³He | 3 | 7.718  | 2.345   | 3.100     | undershoot 2.5× | 1.32× |
| ⁴He | 4 | 28.296 | 3.038   | 5.829     | undershoot 4.9× | 1.92× |
| **⁶Li** | **6** | **31.994** | **130.9** | **1721.2** | **overshoot 54×** | **13.1×** |
| **⁷Li** | **7** | **39.245** | **421.4** | **17692.3** | **overshoot 451×** | **42.0×** |

## Verdict — refuted (constraint 2 closes the box row)

`dim_q` is **killed by bounded-across-A**, and more decisively than `dim`:

1. **It diverges at A≥6.** Both weights undershoot through ⁴He, then explode at ⁶Li/⁷Li. `dim_q` overshoots AME by
   54× (⁶Li) and 451× (⁷Li).
2. **It diverges *worse* than `dim`** — 13.1× worse at ⁶Li, 42.0× worse at ⁷Li. Structural reason: at `q₀ = 1.110 > 1`
   each `[k]_q ≈ q^{k-1}` blows up, so the q-deformed dimension grows faster than the classical one.
3. **The signed sum does not rescue it.** There is no chirality-sign cancellation that keeps `B_pred(sgn·dimq)`
   bounded; it grows monotonically.

So **no combinatorial-dimension chirality-invariant weight survives `bounded + multi-block`** — the magnitude box
row 2 reads `dim ✗, dim_q ✗`. The bounded candidates that *do* exist (`sgn`, raw `tr_M`) undershoot
catastrophically (`sgn` at ⁷Li is 666,000× too small).

## What survives — the redirect (unchanged, sharpened)

The target magnitude is squeezed to an **intermediate-growth** object: chirality-invariant, multi-block, growing
roughly linearly in A (to track ~8 MeV/nucleon saturation) — **not** a combinatorial dimension (overshoots at A≥6)
and **not** a bounded sign/trace (undershoots everywhere). This is exactly the profile of a **bounded geometric
volume**, i.e. the owner-gated categorical `conj:s5-so3-fiber-action` `Vol` question, **not** a numerical
per-partition weight. No new fit; the prune removes the last enumerated dimension candidate and reaffirms the
ledger's redirect. A fitted intermediate-growth weight would be the gated 20th ansatz.

## Cross-references

- [`2026-06-18-pauli-young-delta-lambda-the3-refutation.md`](2026-06-18-pauli-young-delta-lambda-the3-refutation.md) — sibling T/³He sign-test refutation (the box)
- [`2026-06-18-sparse-interface-magnitude-the3-prune.md`](2026-06-18-sparse-interface-magnitude-the3-prune.md) — constraint 3 (single-dominant refuted)
- [`2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md`](2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md) — the proved sign
- [`docs/coordination/gap-a-path-b-lambda.md`](../coordination/gap-a-path-b-lambda.md) — the GAP-A Path-B ledger
