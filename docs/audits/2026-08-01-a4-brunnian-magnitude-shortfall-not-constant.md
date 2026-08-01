# A=4 Brunnian magnitude — the shortfall is NOT constant in A

**Date:** 2026-08-01
**Bean:** `qou-g3e1` (the magnitude leg left open by the A=4 sign/order derivation)
**Verdict:** **scope-(a) NEGATIVE, and a decision-relevant one.** Compare-and-report
only: no re-weighting, no fit, no tuning, nothing wired.

## The question

PR #4458 derived the A=4 Brunnian cluster's **sign and order** exactly (leading
`(q−1)`-order 6, leading coefficient `−96`), promoting the A=4 leg of the
Milnor-parity law from *measured* to *derived*. What it explicitly did **not**
close is the **magnitude**: whether the derived cluster
`c_A = E₀·(1 − τ_A)` is the right *size* to supply the forward residual `μ_A`
(AME − model, never inverted).

The bean's instruction was to compare and report the ratio — and to **not**
re-weight to close it, since that is the fitted route.

## What was computed

[`computations/deltalambda/a4_brunnian_magnitude_vs_mu4.py`](../../computations/deltalambda/a4_brunnian_magnitude_vs_mu4.py)
· witness `a4-brunnian-magnitude-vs-mu4.witness.json`. All inputs read from
committed witnesses; no new physics. `E₀ = 4.18598136329 MeV`,
`μ₃ = +0.47076896`, `μ₄ = −4.591048`.

Both known `A`, at both levels, so the comparison is like-for-like:

| A | level | `c_A` (MeV) | `μ_A` (MeV) | `c_A/μ_A` | shortfall | sign |
|---|---|---|---|---|---|---|
| 3 | base `n=3` | `+0.0068372874` | `+0.470769` | `0.0145237` | `68.85×` | ✓ |
| 3 | cabled `H₉` | `+0.29695751` | `+0.470769` | `0.630792` | **`1.585×`** | ✓ |
| 4 | base `n=4` | `−0.00061072463` | `−4.59105` | `0.000133025` | `7517×` | ✓ |
| 4 | cabled `H₁₂` | `−0.058244099` | `−4.59105` | `0.0126864` | **`78.82×`** | ✓ |

## The finding

**The shortfall is not constant in `A` — it diverges sharply.**

```
base level :  A=3 short 68.85×  ,  A=4 short 7517×    ->  diverge by 109.2×
cabled     :  A=3 short 1.585×  ,  A=4 short 78.82×   ->  diverge by  49.7×
```

If a single missing normalisation explained both `A`, that divergence would be
`1`. It is ~50 (cabled) / ~109 (base).

**Why this is decision-relevant.** It closes off the most tempting next move.
The A=3 cabled cluster is a `1.59×` near-miss — close enough that "find the
missing `O(1)` factor" looks like the obvious programme. This result shows that
programme cannot work as stated: **any constant re-weight tuned to close A=4
would blow up the A=3 near-miss by the same ~50×**. The two cannot be closed by
one normalisation. That independently confirms the anti-fit guard the bean
carried, rather than merely restating it as policy.

**What survives.** The **sign is correct at both `A` and both levels** (4/4) —
the parity law derived in #4458 holds against the forward residual. So the
derived Brunnian cluster is contributing with the right chirality at both known
orders; it is *only* the magnitude that fails, and it fails in an `A`-dependent
way. Per the "scope-limited negative" discipline this is a **(a)** finding: it
constrains magnitudes and combinations, **not** the ingredient. The Brunnian
cluster is not excluded — a multi-term closure in which it is one contribution
among several remains open, and indeed is now the *only* shape consistent with
these numbers.

## What is NOT claimed

* **Not a refutation of the Brunnian route.** Scope-(a): the cluster alone is
  the wrong size, and the shortfall's `A`-dependence rules out a *constant*
  re-weight. It does not rule out the cluster appearing in a closure with an
  `A`-dependent or additional term — that would need its own derivation.
* **No re-weighting attempted.** No normalisation was searched for, and none is
  proposed. Inventing an `A`-dependent factor to absorb the 50× would be a fit
  with a free function, which is strictly worse than the constant it replaces.
* **Nothing wired**; no dashboard or mass/binding path consumes this.

## Note on the witness

The first version recorded the finding as a deliberately-failing assertion
(`shortfall_not_constant ≟ 1`) so the divergence would be machine-visible. That
was wrong hygiene: `allPassed: false` signals a **broken compute**, not a
result, and would trip witness-health tooling. The assertion now states what is
actually true (`divergence > 10×`) and carries the measured values in its
`source`, leaving the witness green while keeping the finding machine-readable.

## Cross-references

- [`2026-08-01-a4-brunnian-deficit-closed-form.md`](2026-08-01-a4-brunnian-deficit-closed-form.md) — the sign/order derivation this completes.
- [`2026-07-27-deltalambda-s5so3-geometric-wlambda.md`](2026-07-27-deltalambda-s5so3-geometric-wlambda.md) — the A=3 geometric `W_λ` re-weight, which overshot by ~30× (an independent instance of "re-weighting does not close it").
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — the Δ_λ magnitude gate, still open.
