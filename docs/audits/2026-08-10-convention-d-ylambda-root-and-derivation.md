# The convention-C root is symbolic, has no producer, and the convention-D replacement is derivable

**Date:** 2026-08-10
**Branch:** `claude/convention-c-witness-pass2-2026-08-10` (PR #4928)
**Beans:** `qou-eea0` (campaign), `qou-v0b3` (root), `qou-u2jg` (keystone, supplies `z_D`)

## Summary

`qou-eea0` is scoped as *"the producers are all convention D; their committed
outputs are not"*, so re-running every producer should close the gap. **It
cannot.** The convention is defined in a **symbolic** witness that has **no
producer**, and every downstream number is a faithful evaluation of it.

The replacement is not an open question. Convention D's Markov parameter is
already derived and Lean-proved elsewhere in the corpus, and the corresponding
weight family follows in closed form and is verified below.

## 1. The cascade, and its root

```
y-lambda-wenzl-bridge-symbolic-witness.json      <- SYMBOLIC, convention C, NO PRODUCER
  |   regenerate_y_lambda_mpfr.py  (line 60: SOURCE — evaluates at q0, derives nothing)
  v
y-lambda-mpfr-witness.json / y-lambda-mpfr-proton-witness.json   (223 three-row hits each)
  |   tr_m_wenzl_bridge_mpfr.load_y_lambda_for_q0
  v
chi_at_q0_via_hoefsmit_mpfr.py   ->  6 chi witnesses (p, n, D, T, 3He, 4He)
  |
  v
7 producers  ->  8 more via y-lambda-at-q0.witness.json
```

The root's entry for the three-row partition `[1,1,1]` at `n = 3` is a rational
function of `q` that `sympy` confirms is **not identically zero**, and that
evaluates at the proton `q₀` to

```
0.022744942577009783454
```

which is the registry convention-C fingerprint `0.02274491`. Under convention D
every `y_λ` with `ℓ(λ) ≥ 3` vanishes identically (Schur–Weyl on a
two-dimensional fibre), so this is convention C at the source.

Independent confirmation from the other direction: bean `qou-u2jg` records that
under convention C *"`y_(1^3) = 0.0227449`"*. Two routes, same number.

## 2. Why no detector saw it

`_structural_hits` called `float()` on each `y_lambda` and swallowed the
`ValueError`. This file stores `y_lambda_symbolic` as **expression strings**, so
every entry was skipped in silence: **0 fingerprints, 0 structural hits**, for a
7 MB file that defines the convention for the whole cascade.

Fixed in this branch as a syntactic screen (any non-trivially-zero expression
string counts). The same blindness should be assumed in
`scripts/convention-c-witness-audit.py` — the "selftest 7/7" canonical detector —
until checked; its structural rule has the same shape.

## 3. Ordering was a real, separate defect

Producers read each other's witnesses, and the harness ran them **alphabetically**.
`aK_via_lp_dual` ran *first* while its upstream `chi_at_q0_via_hoefsmit_mpfr` ran
20 producers later, so downstreams re-emitted the convention-C weights they had
just read, exited 0, and were recorded as successful regenerations. That is why a
98-minute pass with 41 of 55 producers `ok` left 28 witnesses convention C, the
whole `rho_k_h3a_*` family having moved 0.5–1.2 ppm from `main`.

Fixed by `topo_order()` — 29 edges among 57 producers, Kahn with alphabetical
tie-break, verified zero order violations. **But ordering alone does not close the
campaign**, because a perfectly-ordered pass still evaluates the same
convention-C symbolic source.

## 4. The convention-D weights — derived, not chosen

`qou-u2jg` derives (Lean, sorry-free) that imposing the three Markov
normalisations on `H₃(q)` in the Wedderburn basis forces

```
y_(1^3) · (q²+1)(q⁴+q²+1) = q² (z − q) (z(q²+1) − q³)
```

so the antisymmetriser dies at exactly two values of `z`; `z = q` collapses to the
one-dimensional character, leaving

```
z_D = q³/(q² + 1)
```

as the unique non-trivial Markov trace on `H₃(q)` whose radical contains the
three-strand antisymmetriser. At the proton `q₀`:

| | value at `q₀ = 1.1099785827513808` |
|---|---|
| `z_D = q³/(q²+1)` | `0.61268803714646524365` |
| `z_C = 1/(q^{1/2}+q^{-1/2})` | `0.49932033418369445` |

The second is the registry fingerprint `0.49932033418369`.

**The weight family that goes with `z_D`**, for `λ = (n−k, k)` (at most two rows),
with `[m]_q = (q^m − q^{−m})/(q − q^{−1})`:

```
y_λ  =  [n − 2k + 1]_q / [2]_q^n              ℓ(λ) ≤ 2
y_λ  =  0                                     ℓ(λ) ≥ 3
```

### Verification

Checked symbolically with `sympy`, against quantities *not* used to construct it:

| check | result |
|---|---|
| `y_(3)` vs `qou-u2jg`'s independently-derived `(q⁴+1)/(q²+1)²` | equal |
| `y_(2,1)` vs its `q²/(q²+1)²` | equal |
| `tr(1) = y_(3) + 2y_(2,1) + y_(1³) = 1` | holds |
| `tr(σ) = q·y_(3) + (q−r)·y_(2,1) − r·y_(1³) = z_D` | holds |
| `tr(σ₀σ₁) = q²·y_(3) − y_(2,1) + r²·y_(1³) = z_D²` | holds |
| `tr(1) = Σ_λ dim_λ · y_λ = 1` for `n = 2 … 8` | holds |

The third and fifth rows are the ones that matter: `tr(σ) = z_D` is the defining
condition, and it is what distinguishes *reproducing convention D* from merely
*normalising correctly*.

> **Recorded error, because it nearly shipped.** A first pass used
> `[m]_q = (q^{m/2} − q^{−m/2})/(q^{1/2} − q^{−1/2})` — half-integer powers —
> and "confirmed" the two closed forms by comparing that bracket against
> *itself*. The check was circular and passed; the two Markov conditions then
> failed, which is what exposed it. Verify a closed form against a quantity
> derived independently of it, never against your own restatement.

## 5. What remains

The migration is a **derivation followed by a mechanical cascade**, in this order:

1. **Write a producer** for the symbolic `y_λ` witness under convention D. It
   currently has none, which is why nothing could regenerate it. Formula in §4;
   the Lean pinning `z_D` already exists (`QOU/QBeta/TemperleyLiebTower.lean`,
   section `ConventionPinning`).
2. **Re-issue** `y-lambda-wenzl-bridge-symbolic-witness.json` from that producer.
3. **Run the dependency-ordered harness**; everything downstream follows without
   further intervention.
4. **Re-audit** and report total impact with `--impact-vs-main`.

Hand-editing the symbolic file is not an acceptable route — `qou-eea0` hard
constraint: nothing hand-edited, every number comes from a producer run.

## 6. Scope note on the numbers in §4

`y_λ = [n−2k+1]_q/[2]_q^n` is verified at `n = 3` against all three Markov
conditions and at `n = 2 … 8` against the trace normalisation. It is **not**
verified against `tr(σ) = z` for `n > 3`, and the `H_n/rad = TL_n` identification
it is consistent with is itself measured (`qou-8iru`, `n = 2 … 7`, residual
`1.34e-51`) rather than proved for general `n`. So: the `n = 3` case is derived,
the general-`n` form is a well-supported extension that the producer in step 1
should re-verify per `n` as it emits, not an established theorem.
