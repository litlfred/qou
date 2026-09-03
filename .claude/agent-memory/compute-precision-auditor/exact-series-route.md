# Exact leading-order coefficients without extrapolation (2026-09-03, qou-pdg9)

## STABLE — the duck-typed exact pipeline runs over power series

`computations/probes/exact_rational_chi_gauge_probe.py` evaluates `χ^λ` (and so
the convention-D Markov trace, with the symbolic `y_lambda_at`) in exact
`Fraction` at any rational `q` via the asymmetric seminormal gauge. Its
`blocks_at` / `chi_at` / `factors_for` use only `+ − × ÷ **` on `q`, so they run
unchanged over ANY scalar type with those operators. Run them over truncated
power series in `ε = q − 1` and the trace comes back as exact rational Taylor
coefficients — no Richardson, no `limit_denominator`. Worked example:
`computations/probes/c1_leading_coefficient_derived_probe.py` (`Ser` class),
which reproduced six Richardson-measured dyadic rationals by `Fraction ==`.

Two things the series scalar MUST do:

- **Track a valuation.** The seminormal entries `h/(1 − q^{−2ρ})` are `0/0` at
  `ε = 0`; a plain truncated polynomial ring cannot divide there. Store
  `(valuation, coeffs, absolute precision)`; a quotient of two valuation-1
  series costs exactly one order of precision, nothing else does.
- **Never allocate to the precision of an exact constant.** The pipeline mixes
  `Fraction` constants in; if "exact" is modelled as `p = 10⁹`, then
  `const × const` or `1/const` asks for 10⁹ coefficients. Measured: exit 137
  (OOM-killed) and then `MemoryError`, before the fix. Cap allocations at the
  stored list lengths.

Cost, measured: two-row partitions only (row cap is exact in `y_λ`), ⁴He
(`n = 12`, dims ≤ 297) at order-3 series ≈ 4 min per word in pure Python;
`A = 5` would be hours. For the cross-check at a rational point use the
`Fraction` pipeline directly (no series) — ⁴He at `q = 8/7` took ~90 s.

## TRAP — `reject_float64_q` rejects SHORT DECIMALS, not just floats

`tr_m_atom_zn(q=mp.mpf("1.1"))` at 50 dps is refused as "mpf holding only
float64 information": the guard keys on whether the value round-trips through
a double, and `1.1` does. So a rational cross-check point must be a
non-terminating decimal — `mp.mpf(8)/7` passes, `mp.mpf("1.1")` does not. A
run that dies here after the expensive part has already finished loses that
work; put the cross-check FIRST or checkpoint before it.

## TRAP — a background run that dies mid-way still returns exit 0 through `tee`

`python3 -u probe.py 2>&1 | tee log` reports tee's exit code. Read the log for
the traceback; the harness notification said "completed (exit code 0)" for a
run that had raised.
