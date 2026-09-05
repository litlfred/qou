# The bound's looseness is κ, not Cauchy–Schwarz — and that corrects my own mechanism

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — n=9, 14 shapes with both κ and slack measured. Nothing wired, no witness, no fit.

## The measurement

#6754's link-1 loss, `slack = √(dim·‖X‖_F²) / |tr|`, factors **exactly**:

```
slack  =  (1/κ)  ×  ( √(dim·‖X‖_F²) / Σ|eig| )
          ^^^^^     ^^^^^^^^^^^^^^^^^^^^^^^^^
          cancellation      Cauchy–Schwarz
```

since `|tr| = κ·Σ|eig|` by definition of `κ = |Σ eig| / Σ|eig|`. Measured over the 14 n=9 shapes
where both factors are now known:

| λ | dim | slack | 1/κ | CS part | family |
|---|---|---|---|---|---|
| `(4,3,2)` | 168 | 307.10 | **85.45** | 3.59 | non-hook |
| `(4,3,1,1)` | 216 | 295.30 | **74.74** | 3.95 | non-hook |
| `(5,2,2)` | 120 | 186.30 | **53.42** | 3.49 | non-hook |
| `(5,2,1,1)` | 189 | 74.34 | 20.19 | 3.68 | non-hook |
| `(5,1⁴)` | 70 | 44.98 | 10.19 | 4.41 | hook |
| `(6,1,1,1)` | 56 | 30.97 | 9.59 | 3.23 | hook |
| `(4,4,1)` | 84 | 25.96 | 7.90 | 3.29 | non-hook |
| `(5,3,1)` | 162 | 20.82 | 6.60 | 3.16 | non-hook |
| `(5,4)` | 42 | 18.42 | 6.47 | 2.85 | non-hook |
| `(6,2,1)` | 105 | 12.75 | 4.39 | 2.91 | non-hook |
| `(6,3)` | 48 | 9.68 | 3.63 | 2.67 | non-hook |
| `(7,2)` | 27 | 6.10 | 2.45 | 2.49 | non-hook |
| `(7,1,1)` | 28 | 4.45 | 1.86 | 2.39 | hook |
| `(8,1)` | 8 | 2.04 | 1.07 | 1.91 | hook |

```
1/κ  spans  1.07 … 85.45      (80×)
CS   spans  1.91 …  4.41      (2.3×, essentially constant)
```

**The Cauchy–Schwarz factor is uniform at ~2–4× across every shape and every family.** Virtually all
the variation in the bound's looseness — and most of its magnitude — is `κ`.

## What this corrects

**#6785's mechanism is wrong.** That correction said hooks are better-bounded because their spectrum
collapses *uniformly*, keeping Cauchy–Schwarz honest, while the fat non-hook shapes *"keep a spread
spectrum"*. The CS column refutes it: spectral spread is uniform across all 14 shapes, hooks and
non-hooks alike. Hooks are better bounded because they have **less cancellation** (higher `κ`) at the
levels sampled — nothing to do with spread.

**#6785's headline survives.** The hook split still does not transfer to bound tightness, and
non-hooks are still the worse-bounded family. Only the explanation was wrong.

**#6754's redirect is vindicated and made concrete.** That PR said "a quantitatively useful bound
must keep the sign information", which was right but unquantified. It is now specific: the norm
relaxation's loss *is* the `κ` factor, to within a uniform 2–4×.

## Consequence: the sub-problem is bounding κ

Improving the Cauchy–Schwarz step cannot buy more than ~4× anywhere, so it is not worth attacking.
The whole 550× lives in `κ`, so:

- an upper bound on `κ(λ)` that decays with `b` would give a bound tight to within a uniform 2–4×;
- conversely, **no bound that discards `κ` can be better than ~85× loose** at n=9, since that is the
  measured `1/κ` at `(4,3,2)` — and the census still has fatter shapes to report.

That is the sharpest statement this arc has produced about *where* a bound must do its work, and it
is the first time the loss has been attributed to a named factor with numbers rather than argued.

## What is NOT established

- **14 of 30 shapes**, those where the κ census had reported by the time of writing; the remaining
  16 are the fatter ones and could extend the `1/κ` range upward but cannot narrow it.
- **n=9, this atom word.** Nothing proved for general `n`.
- **No bound on κ is offered here.** This says where a bound must act, not how.
- The factorisation itself is an identity, not a finding; what is measured is the *split of
  magnitudes* between its two halves.

## Correction-chain note

Three of my claims in this arc have now been corrected by later measurement — the majorant route
carrying the size (#6754), the hook split transferring to tightness (#6785), and the spread-spectrum
mechanism (here). Each was caught by measuring something the previous claim implied but had not
tested. The pattern worth keeping: an explanation that has not been decomposed into factors with
numbers attached is a story, and this arc has produced three wrong ones.
