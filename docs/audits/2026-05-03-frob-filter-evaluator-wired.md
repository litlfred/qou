# FROB-FILTER closed-form evaluator wired into β-decay pipeline

**Date**: 2026-05-03
**Branch**: `claude/audit-math-framework-FXlp2`
**Cross-reference**: [`2026-05-02-nv-frob-filter-conjectures.md` lines 683–769](2026-05-02-nv-frob-filter-conjectures.md#L683-L769)

## Summary

This memo documents wiring the symbolic closed form of $\Sigma_{\rm all}(A)$
— the unfiltered β-decay character sum — into the β-decay /
binding-energy compute pipeline as the canonical evaluator,
replacing the catastrophic-cancellation-prone raw-config-sum route.

Per the prior audit, the raw $\Sigma_{\rm all}(A)$ enumeration sums
$4^A$ per-nucleon channel configurations of $\Delta m_e$, and the
required precision scales as $A \cdot 0.589$ decimal digits. f64 is
safe only to $A \leq 27$; the full β-decay table (up to $A = 240$)
needs 130+ dps. The closed form, with all $(q-1)^A (q+1)^A$
cancellation factors extracted symbolically, evaluates at constant
compute cost per digit and **zero** cancellation.

## What the evaluator does

Module: [`computations/sigma_all_evaluator.py`](../../computations/sigma_all_evaluator.py)

Pure mpmath, no sympy at runtime. Sympy was the bottleneck (recursion
error past $n = 12$); the symbolic compute happens once, off-line, in
[`sigma_all_symbolic_decay.py`](../../computations/sigma_all_symbolic_decay.py)
and is **not** modified by this work. The runtime evaluator just
plugs $A$ and $q$ into the explicit factored formula.

### API

| function | purpose |
|----------|---------|
| `sigma_all_closed(A, q, dps=None)` | direct evaluation of the closed-form expression at $A, q$ |
| `sigma_all_ratio(A1, A2, q, dps=None)` | uses the exact two-step identity for even $\Delta A$; falls back to ratio of two evaluations for odd $\Delta A$ |
| `sigma_all_decay_rate(q, dps=None)` | returns $\gamma(q) = \tfrac{1}{2}\log\bigl(\tfrac{8q^4}{3(q^4-1)^2}\bigr)$ |
| `frob_filter_required(A, q, target_relative_precision)` | true iff the raw config-sum's required precision exceeds the target — i.e. the closed-form path is needed |
| `precision_digits_required(A, q=None)` | digits required by the raw config-sum at this $A$ (≈ $0.589 A + 1$) |
| `a_exponent(A)`, `d_exponent(A)` | the closed-form $a(A)$ and $d(A)$ exponent sequences |

### Closed form

$$
  \Sigma_{\rm all}(A) = (-1)^{A-1} \cdot
  \frac{3^{\lfloor A/2 \rfloor}}{2^{a(A)}} \cdot
  (q-1)^A (q+1)^A \cdot (q^2+1)^{2\lfloor A/2\rfloor} \cdot
  \frac{3q^4 + 4q^2 + 3}{q^{d(A)}}
$$

with closed-form exponents

- $a(A) = (3A+1)/2$ if $A$ odd, $(3A+2)/2$ if $A$ even (verified $\{2,4,5,7,8,10\}$ for $A=1..6$);
- $d(A) = 2A+1$ if $A$ odd, $2A+2$ if $A$ even (verified $\{3,6,7,10,11,14\}$ for $A=1..6$).

Two-step ratio (exact in $\mathbb{Z}[q^{\pm 1}]$):

$$
  \frac{\Sigma_{\rm all}(A+2)}{\Sigma_{\rm all}(A)} = \frac{3(q^4-1)^2}{8q^4}.
$$

## Pipeline modules now using it

| File | Replacement |
|------|-------------|
| [`computations/full-derivation-verified.py`](../../computations/full-derivation-verified.py) line 263 | A=1 free neutron: `char_sum_n = sum_p - sum_n` → `sigma_all_closed(1, q0)` (assertion confirms agreement to $10^{-12}$) |
| [`computations/full-derivation-verified.py`](../../computations/full-derivation-verified.py) line 277 | A=3 tritium ³H→³He: 64-config sum → `sigma_all_closed(3, q0)` |
| [`computations/full-derivation-verified.py`](../../computations/full-derivation-verified.py) line 297 | A=6 ⁶He→⁶Li: 4096-config $\Sigma_{\rm all}$ sum → `sigma_all_closed(6, q0)`. The $\Sigma_{\rm FP}$ Frobenius-positivity-filtered path is genuinely different (no closed form yet) and still enumerates. |

After wiring, the script reproduces the previous Q-values exactly:
- $n \to p$: $0.781575$ MeV (vs. exp $0.782333$, error −0.10%)
- $^{3}\mathrm{H} \to {}^{3}\mathrm{He}$: $0.017933$ MeV (vs. exp $0.018610$, error −3.64%)
- $^{6}\mathrm{He} \to {}^{6}\mathrm{Li}$ (FP): $3.125958$ MeV (vs. exp $3.508$, error −10.89%)

### Intentionally not wired

- [`computations/frob_filter_cancellation_test.py`](../../computations/frob_filter_cancellation_test.py)
  — this **is** the test driver for the cancellation diagnostic;
  swapping it to the closed form would defeat its purpose
  (measuring the f64 precision-budget crossover).
- [`computations/sigma_all_symbolic_decay.py`](../../computations/sigma_all_symbolic_decay.py)
  — symbolic-derivation reference. Per the task specification, this
  file is the source of truth for the closed form and was not
  modified.

A repo-wide grep for `cartesian.*ch_names` / `product.*ch_names` /
`sigma_all` confirmed no other production callers existed in
`computations/`. (`mass_endomorphism.py`,
`binding_canonical.py`, `markov_peel.py` contain no $\Sigma_{\rm
all}$ enumeration; `markov_peel.py`'s use of `sigma` refers to the
Hecke generator $\sigma_i$, unrelated.)

## Precision claim

| property | value |
|----------|-------|
| Catastrophic cancellation | none (factors extracted symbolically) |
| Compute cost per digit | constant in $A$ |
| Multiplications per evaluation | $O(\log A)$ (mpmath integer-power binary exponentiation) |
| Valid for | any $A \geq 1$, any mpmath dps |
| Verified at $q_0$ for $A=1..6$ | matches symbolic table to f64 floor (~$3 \times 10^{-15}$ relative) |
| Verified for $A = 240$ at 200 dps | $\log_{10}|\Sigma_{\rm all}(240)| \approx -141$, matches asymptotic prediction |

The audit's precision schedule for the **raw** config-sum route
(now obsolete for production callers) is reproduced exactly by
`precision_digits_required`:

| precision | floor | max $A$ safe |
|-----------|------:|-------------:|
| f64 | $10^{-16}$ | $A \leq 27$ |
| 25 dps | $10^{-25}$ | $A \leq 42$ |
| 50 dps | $10^{-50}$ | $A \leq 84$ |
| 100 dps | $10^{-100}$ | $A \leq 169$ |
| 200 dps | $10^{-200}$ | $A \leq 339$ |

## Tests

[`computations/test_sigma_all_evaluator.py`](../../computations/test_sigma_all_evaluator.py)
— 11 tests, all passing:

1. `test_a_exponent_table` — $a(A)$ matches verified $\{2,4,5,7,8,10\}$
2. `test_d_exponent_table` — $d(A)$ matches verified $\{3,6,7,10,11,14\}$
3. `test_matches_symbolic_table_A_1_to_6` — all 6 reference values to $10^{-14}$ relative
4. `test_two_step_ratio_invariant` — exact $\Sigma(A+2)/\Sigma(A) = 3(q^4-1)^2/(8q^4)$ for $A \in \{1,2,3,4\}$ to $10^{-15}$
5. `test_two_step_ratio_via_sigma_all_ratio` — `sigma_all_ratio` returns the exact identity for even $\Delta A$
6. `test_sigma_all_ratio_odd_delta` — odd-$\Delta A$ fallback agrees with direct quotient
7. `test_decay_rate_at_q0` — $\gamma(q_0) \approx 1.357$ to $0.001$
8. `test_frob_filter_threshold_f64` — $A = 84$ exceeds f64 budget; $A = 10$ does not
9. `test_frob_filter_threshold_50dps` — $A = 240$ exceeds 50-dps budget; $A = 10$ does not
10. `test_sign_pattern` — $\Sigma_{\rm all}(A)$ alternates sign for $A=1..8$
11. `test_high_precision_evaluation` — $\Sigma_{\rm all}(240)$ at 200 dps is finite, non-zero, magnitude consistent with asymptotic

## Witness

[`computations/sigma-all-evaluator.witness.json`](../../computations/sigma-all-evaluator.witness.json)
— reference table $A=1..10$ at $q_0$, asymptotic ratios, decay rate,
precision schedule, list of pipeline callers updated and
intentionally unwired.

Builder: [`computations/build_sigma_all_evaluator_witness.py`](../../computations/build_sigma_all_evaluator_witness.py).

## Status

- Steps 1–6 complete.
- All 11 evaluator tests pass.
- All identified production callers wired (3 call sites in 1 file).
- Wired script (`full-derivation-verified.py`) reproduces previous
  Q-values exactly.
- Witness emitted. Memo written. No `sorry` / `TODO` left in the new
  evaluator code.
