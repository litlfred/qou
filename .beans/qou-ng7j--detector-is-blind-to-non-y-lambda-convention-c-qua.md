---
# qou-ng7j
title: Detector is blind to non-y_lambda convention-C quantities (tr_M, z); Schur-Weyl is the real per-weight test
status: todo
type: task
created_at: 2026-08-10T18:42:38Z
updated_at: 2026-08-10T18:42:38Z
---


## The question this answers

From `qou-y6h7`: *is the `1e-40` shadow-price identity supposed to hold under
convention D at all, given it was established under C where every channel is
live?*

**Yes — it is not a convention-C artifact, it is the definition.**
`rho_k_h3a_lp_dual.py:340` computes

```python
sw_err = abs(sw_sum - tr_M)        # sw_sum = Σ_λ y_λ(q₀) · χ^λ(β_D)
```

which is the Schur–Weyl / Frobenius identity `tr = Σ_λ y_λ χ^λ`. That identity
is exactly *what makes* `y_λ` the Wedderburn weights of the trace. It has to
hold for whichever weights are correct, under any convention.

## So why does it fail under D — and it is not (yet) the weights

`tr_M` comes from `load_deuteron_tr_M()`
(`rho_k_h3a_refinement.py:276`), which reads
**`atomic-tr-m-mpfr-50dps.witness.json`**. The Markov trace is
convention-dependent — it is the trace with parameter `z` — so under D it must
be recomputed at `z_D = q³/(q²+1)`. It has not been:

- last touched by an unrelated commit; **never regenerated** in PR #4928;
- producer `atomic_tr_m_mpfr_50dps.py` exists, so it is regenerable;
- **it is not in the convention-C work list at all**.

Both sides of the identity are therefore in different conventions, and it must
fail. That is diagnostic of a stale `tr_M`, not of the identity being C-specific.
It does not exonerate the shipped weights either — the identity simply cannot be
used as a test of them until both sides are the same convention.

## The blind spot, which is the real finding

`_is_convention_c` fires on (a) known convention-C decimals, or (b) a nonzero
`y_λ` on a three-or-more-row partition. **Both tests key on `y_λ` tables.** A
convention-C quantity that is not a `y_λ` table is invisible:

| quantity | convention-dependent? | detector sees it? |
|---|---|---|
| `y_λ` table, numeric | yes | yes (structural) |
| `y_λ` table, symbolic strings | yes | only after the PR #4928 fix |
| `tr_M(β)` — trace at parameter `z` | **yes** | **no** |
| `z` itself | **yes** | only if it happens to match a listed decimal |
| anything derived from these (ρ, Δρ, binding, mass) | **yes** | **no** |

This is the same shape as the symbolic-root miss: the detector finds convention
C only where it takes the one syntactic form it was taught. So **"47 witnesses
still convention C" is an undercount of unknown size**, and the campaign cannot
be called complete on that number.

## What to do

1. **Regenerate `atomic-tr-m-mpfr-50dps` under `z_D`** and check whether
   `atomic_tr_m_mpfr_50dps.py` computes the trace from a `z` at all, or inherits
   it from a witness — if the latter, follow it up the chain as was done for
   `y-lambda-wenzl-bridge-symbolic`.
2. **Re-run `rho_k_h3a_lp_dual` afterwards.** If `sw_err` returns below `1e-40`,
   that is a *strong per-weight confirmation* of the shipped convention-D
   weights — far stronger than `tr(1) = 1`, which is one scalar per `n` and
   cannot separate individual weights (`qou-smtg` item 4 asks for exactly this
   kind of check).
   If it does **not** return, the weights are implicated and `qou-smtg` becomes
   urgent rather than tidy-up.
3. **Extend the detector** to trace/scalar quantities, or accept and document
   that the work list bounds only the `y_λ` layer.

## Close condition

`atomic-tr-m` regenerated under D; `rho_k_h3a_lp_dual` exits 0 with `sw_err`
below tolerance, or the failure is traced to a named cause; and the detector
either covers non-`y_λ` convention-C quantities or says in its docstring that it
does not.
