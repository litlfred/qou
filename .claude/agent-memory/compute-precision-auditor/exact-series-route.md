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

## TRAP — do NOT read a radius of convergence off a truncated coefficient sequence

Measured 2026-09-03 (bean `qou-i719`), and it produced two wrong conclusions in a
row before the exact rational function settled it.

The Markov trace difference `Δtr` is **exactly rational**: `Δtr·(1+q²)ⁿ` is a
Laurent polynomial (deuteron: degrees −23…33, interpolated from 57 exact
evaluations and validated on held-out points). So the only poles are `q = 0` and
`q = ±i`, and the radius in `ε = q−1` is **exactly 1**.

But the order-23 pole at `ε = −1` makes `c_k ~ C(k+22, 22)` — polynomial growth of
degree 22, indistinguishable from exponential over the first few dozen orders:

- **root test** `|c_k|^{−1/k}` at k = 26 gives **0.40**, wrong by 2.5×;
- **ratio test** gives 0.50–0.60, also wrong;
- reading the *first three* coefficients (1/8, 19/8, 357/32) suggests 0.05–0.2,
  which would say the series diverges at `ε₀ = 0.11`. It converges fine.
- the partial sums at `ε = 1/2` **grow** with k out to k = 26, which reads as
  divergence. The terms `C(k+22,22)/2^k` peak at `k ≈ 22/ln2 ≈ 32`; truncation
  sampled the rising side of a hump.

**Rule:** get the rational function (interpolate and validate on held-out points),
or bound the pole order, before asserting anything about convergence. A high-order
pole is common here — every letter contributes negative powers of `q`.

## STABLE — convergence and cost at the substrate point

At `ε₀ = 0.10997858` the A=2 series reach **1 ppb by order 16–18** and **1 ppQ by
order 26**. But the insertion expansion costs `2ⁿ·C(L, ≤k)`, and at `A = 5`
(`n = 15`, `L = 59`) order 26 is `4.1e21` subset-state pairs against `15! = 1.3e12`
for the direct trace. **Convergence is necessary and not sufficient — the
expansion is a structural tool, not a route past the A ≥ 5 barrier.**

## TRAP — `sp.nsimplify` does not always return a `Rational`

`tr_M_fraction` reduced `together(y_λ).subs(q, qv)` with `sp.nsimplify` and read
`.p`/`.q`. At `q = 3/2` the result stays an unevaluated `Mul` with a `Pow(-1)` and
`.p` raises `AttributeError`. Latent since the c1 probe merged — the two points it
used (8/7, 11/10) happened to reduce. Use `sp.cancel(...).as_numer_denom()`.
