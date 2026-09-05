# The per-dim majorant is blocked by ONE pair, not by a dead statistic class — and my premise for this probe was wrong

**Date:** 2026-09-04 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — measured at A=2 and A=3, dim ≤ 50. Nothing wired, no witness, no fit.

## Summary

Three results, in decreasing order of how much they change the arc:

1. **One blocking pair, not a diffuse failure.** Of the seventeen statistics now tested against
   `tr_λ(X*X)/dim_λ`, five come within a single inversion at A=3 — and **all five fail on the same
   pair**, `(7,1,1)` vs `(7,2)`. That pair is a hook against a two-row at the same `b=2`, i.e. it
   sits exactly at the intersection of the two columns that already have derived closed forms.
2. **My premise for this probe was refuted by its own control.** I built it on the observation that
   all seven of #6587's dead candidates are `q`-independent. The `q`-independent control
   `n(λ')−n(λ)` matches the best `q`-content statistic exactly at A=3 (1 inversion, 0 ties, 55
   pairs). `q`-independence was not the defect.
3. **A correction to my characterisation of #6587**, not to its numbers. Its probe reproduces
   exactly on re-run. "All seven second-statistic candidates dead" is true read as *"none is a
   strict orderer"* and false read as *"none is close"* — three of the seven miss by one pair.

## 1. The measurement

Probe: [`magnus_q_content_statistic_probe.py`](../../computations/deltalambda/magnus_q_content_statistic_probe.py).
A=3, `n=9`, 11 interior shapes surviving the `dim ≤ 50` cap, 55 pairs. Exact `mpf`, `dps 140`.

Candidates are the Jucys–Murphy `q`-contents `x_□ = q^{2(j−i)}` and their symmetric functions —
what a *central* character of `H_n(q)` is built from. `X*X` is **not** central, so this is a reason
to look, not a derivation.

| statistic | inversions | ties w/ differing per-dim |
|---|---|---|
| `P₁ = Σ q^{2c}` | 1 | 0 |
| `P₋₁ = Σ q^{−2c}` | 1 | 0 |
| `P₁−P₋₁` | 1 | 0 |
| `P₁/n` | 1 | 0 |
| `P₂ = Σ q^{4c}` | 3 | 0 |
| `P₁+P₋₁` | 26 | 3 |
| `Σ|2c·ln q|` | 26 | 2 |
| `b(λ)` **[control]** | 2 | 8 |
| `n(λ')−n(λ)` **[control]** | **1** | **0** |

Both controls are computed **in this table**. #6587 used a different dim cap and a different
counting rule (this one also charges ties, and tests both monotone directions), so quoting its
count against one produced here would be a cross-run comparison and would mean nothing.

### The `q=1` collapse control

At `q=1` every `q`-content power sum equals `|λ| = n` **exactly** and `P₁−P₋₁ ≡ 0`, so these
candidates carry zero combinatorial content and any ordering they produce is a pure `q`-effect. The
probe verifies this numerically (`worst |dev| = 0.0` at both sizes) rather than asserting it.

## 2. The blocking pair

```
(7,1,1)   dim 28   per-dim 3478.285      hook,    j = b = 2
(7,2)     dim 27   per-dim 2793.099      two-row, k = b = 2
```

Every one of `P₁`, `P₋₁`, `P₁−P₋₁`, `P₁/n`, `n(λ')−n(λ)` ranks these two the wrong way round, and
**none of them fails anywhere else.** `b(λ)` fails on a *different* pair — `(3,1⁶)` against the two
`b=7` shapes, the inversion already recorded in #6587 — and additionally carries 8 ties, which is
the structural point about `b`: it takes few values, so it cannot be a strict orderer at all and
its inversion count alone flatters it.

**Why this is the useful finding.** "No statistic works" invites an eighth candidate. "Five
statistics work except on one pair, and that pair is a hook against a two-row" does not — because
**both of those columns already have derived closed forms**: the reduced-Burau closed form for the
hook majorant (#6556) and the exact sector difference `‖X|_{W_k}‖_F² − ‖X|_{W_{k−1}}‖_F²` for the
two-row (#6587). So this obstruction is *analytically accessible* in a way the general question is
not — the comparison at `b=2` can be settled from the two closed forms rather than measured.

## 3. The independence check, and why it matters

`P₁−P₋₁ = 2Σ sinh(2c·ln q)`, whose leading term is `4·ln q·Σc = 4·ln q·(n(λ')−n(λ))`. So the
best `q`-candidate is the *`q`-deformation of the control*, not a different idea, and two
statistics agreeing means nothing if one is a deformation of the other. Tested directly:

- **A=3: identical ordering, 0 disagreements over 11 shapes.** The `q`-content near-miss is
  therefore **not independent evidence** — it is the control wearing a `q`.
- **A=2: they differ on one pair** (`(3,1,1,1)` vs `(2,2,2)`), so they are not the same statistic;
  the deformation is real, it just buys nothing on the sample where the near-miss occurs.

Both halves are recorded because only the first is convenient.

## 4. Correction to my characterisation of #6587

#6587's probe was re-run on this sample and reproduces exactly: at A=3 it reports `n(λ)` 1/1,
`n(λ)−n(λ')` **1/0**, `b+ℓ` 1/2, `b(λ)` 2/8, `ℓ(λ)` 3/8, `n(λ')` 53/1, `dim_λ` 25/7. **There is no
counting defect in #6587 and its verdict "no single candidate orders the sample" is correct.**

What was wrong is how I *reported* it — as "all 7 candidates are dead", which reads as "none is
close" when three miss by exactly one pair. The distinction is not cosmetic: a class that fails
diffusely says stop looking, and a class that fails on one identified pair says look at that pair.
I spent this probe testing a new statistic family on the strength of the first reading.

The `dim_λ` null control still fails hard (25 inversions, 7 ties), so the original conclusion that
the ordering is about shape rather than dimension is untouched.

## 5. What is NOT established

- **A=2 and A=3 only**, and the `dim ≤ 50` cap skips 17 of 28 shapes at `n=9`. Those are **not
  run**, not evidence — the blocking-pair claim is a statement about the 11 shapes measured.
- **A statistic that orders a sample is neither a bound nor a proof.** Nothing here bounds
  anything.
- **The envelope `max_{b(λ)=b}` remains the only surviving global monotone form** (#6587),
  unchanged by this work.
- Whether the two closed forms actually cross at `b=2` is the **next** question, not one answered
  here.
