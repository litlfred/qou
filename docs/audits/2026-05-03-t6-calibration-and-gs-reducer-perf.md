# 2026-05-03 — T6 Calibration & GS-Reducer Performance Audit

## Summary

This audit records two related lines of work landed on
`claude/verify-binding-proton-fix-oF97P` (PR #536):

1. **T6 (Mittag-Leffler polar sum at non-zero roots of unity)** — full
   spectrum proton..⁵Li computed via partial-fraction split on the
   u-plane lift `tr_M(u²)`.  Replaced the prior per-pole `sp.residue`
   path (timeout > 30 min on deuteron) with a fully symbolic
   `sp.div + power_series_invert` pipeline.

2. **GS reduction in `H_n(q)`** — replaced sympy `Expr` coefficients
   in the Hecke / Markov-peel hot loop with a sparse Laurent
   polynomial class (`LaurentQ`).  Coupled with `tr_M_atomic` now
   routing through this fast path by default, atomic Markov traces
   for A ≤ 5 went from infeasible-or-30+min to seconds-to-minutes.

The T6 → MeV calibration question — pre-existing in
`six_term_consumer.assemble_ame_comparison`'s docstring — remains
**open**; this audit documents the empirical data points collected
and the upstream blocker (tower-scale miscalibration) that prevents
a clean reading.

## Pipeline performance after the work

End-to-end `term6_residues_at_roots.compute_atom` timings:

| atom    | A | sp.residue path | partial-fraction split | + LaurentQ peel |
|---------|--:|-----------------|------------------------|-----------------|
| proton  | 1 | 30 s            | 0.42 s                 | **0.1 s**       |
| neutron | 1 | 30 s            | 0.31 s                 | **0.1 s**       |
| deuteron| 2 | > 30 min        | 8.1 s                  | **0.6 s**       |
| tritium | 3 | infeasible      | 12.0 s                 | **3.7 s**       |
| helium-3| 3 | infeasible      | 5.6 s                  | **2.1 s**       |
| helium-4| 4 | infeasible      | 50.5 s                 | **17 s**        |
| **lithium-5** | **5** | infeasible | infeasible        | **85 s** ← new  |

`tr_M_atomic` standalone (just the symbolic Markov peel, no T6
post-processing), fast vs slow path:

| atom    | fast    | slow    | speedup |
|---------|--------:|--------:|--------:|
| proton  |  0.07 s |  0.04 s |   0.6×  |
| neutron |  0.00 s |  0.03 s |   8.7×  |
| deuteron|  0.07 s |  1.72 s |  23×    |
| tritium |  1.32 s |  3.20 s |   2.4×  |
| helium-3|  0.52 s |  2.48 s |   4.8×  |

Proton runs slightly slower in the fast path because the LaurentQ
import + setup overhead exceeds the rule-loop savings on a 4-term
unreduced product.  Net win for every other caller.

## R4 quotient ideal — explicitly *not* ported to LaurentQ

The slow `markov_peel.incremental_reduced_element` interleaves R4
(whole-atom / sub-word quotient folding via
`SymbolicHeckeDivision._try_*_quotient`) into each fixpoint pass to
keep intermediate sympy term counts bounded.  We prototyped the
R4 port via a sympy round-trip per iteration and benchmarked:

| atom    | no R4   | with R4 | R4 speedup |
|---------|--------:|--------:|----------:|
| proton  |  0.10 s |  0.16 s |  0.62×    |
| deuteron|  0.34 s |  1.20 s |  0.28×    |
| tritium |  1.29 s |  1.97 s |  0.65×    |
| ³He     |  0.53 s |  1.46 s |  0.36×    |
| ⁴He     |  9.51 s | 11.82 s |  0.80×    |

R4 is 0.28-0.80× across the spectrum — **slower on every atom**.
Reason: with the LaurentQ rule loop already 5-25× faster than
sympy, the per-iteration LaurentQ↔sympy round-trip cost exceeds
the term-count savings from quotient folding.  The prototype is
reverted; only the (proven slower) sympy R4 path in
`markov_peel.tr_M_atomic` remains for legacy callers via
`use_fast=False`.  Revisit only if A ≥ 6 atoms hit a LaurentQ
rule-loop wall that R4 could amortise.

## T6 → MeV calibration data (3 of 4 atoms)

`binding_full(Z, N, kahler_order=0)` table at q₀ = 1.10998:

| atom | A | T6 (raw)  | canon (MeV) | tower (MeV) | B_pred (MeV) | B_AME (MeV) | residual    | residual/T6 |
|------|--:|----------:|------------:|------------:|-------------:|------------:|------------:|------------:|
| D    | 2 | +109.25   | +0.4657     | +28 828.85  | +28 829.32   | +2.2245     | −28 827.10  | **−263.87** |
| T    | 3 | −41 831   | +0.6290     |+765 378.87  |+765 379.50   | +8.4818     |−765 371.01  | **+18.30**  |
| ³He  | 3 | −37 110   | +0.6581     |+765 457.44  |+765 458.10   | +7.7180     |−765 450.38  | **+20.63**  |

⁴He row not collected (script blew the 600 s budget on the kahler
build; not a regression — this is pre-existing in `binding_full`,
unrelated to T6).

### Reading

T and ³He produce a **consistent residual/T6 ≈ 19 MeV per cat unit**
— suggesting a clean linear T6 → MeV calibration on A = 3 atoms.
Deuteron (A = 2) is a wild outlier at −264, suggesting either
**T6 enters non-multiplicatively** or **the upstream tower term
contaminates the residual non-trivially**.

The bigger story is in the `tower (MeV)` column: **tower itself is
uncalibrated**, ranging 28-765 GeV vs experimental binding 2-30 MeV.
That's three orders of magnitude off at A = 2 and five orders off
at A = 3.  The "residual" is therefore dominated by tower's
miscalibration, not by genuine T6 contribution.

### Conclusion

T6 → MeV calibration **cannot be empirically determined** from the
current `binding_full` pipeline because the tower component is
itself uncalibrated.  The upstream theoretical work to nail down
the tower's MeV scaling (Φ_q tower × ℏ_q² × E_0 normalisation, or
whatever the right combination is) must land before T6 calibration
becomes a meaningful empirical question.

Per `six_term_consumer.assemble_ame_comparison`:

> T6 (Habiro residue) is currently a symbolic / per-A object;
> its MeV translation requires nailing down whether it is
> ALREADY counted inside T1 (per the Mittag-Leffler decomposition
> of the full Markov trace) or is a separate additive correction.

This audit confirms that as the open question — and adds: even if
we resolve "ALREADY-IN" vs "SEPARATE", the upstream tower's MeV
calibration remains the *primary* blocker.

## Files affected on this branch

Code:
- `computations/term6_residues_at_roots.py` — partial-fraction polar split on u-plane lift
- `computations/laurent_q.py` — sparse Laurent polynomial class (new)
- `computations/hecke/hecke_laurent_fast.py` — LaurentQ-coefficient GS reducer + tr_M_atomic_fast (new)
- `computations/markov/markov_peel.py` — `tr_M_atomic` defaults to fast path
- `computations/binding_full_pipeline.py` — T6 wired in with module-level cache

Witnesses:
- `computations/term6-residues-at-roots.witness.json` — full A ≤ 5 spectrum

## Next steps (out of scope of this audit)

1. **⁶Li (A = 6) symbolic peel** — projected ~10 min; no longer
   structurally blocked.  Run when budget permits.
2. **Tower MeV calibration** — primary blocker for T6 → MeV.
3. **R4 in LaurentQ revisit** — only if A ≥ 6 walls the rule loop.
4. **Numeric-mode `tr_M_atomic`** — skip sympy entirely for callers
   that only need q = q₀ output (binding_full, term6_residues).
   Could cut another order of magnitude on heavy atoms.
