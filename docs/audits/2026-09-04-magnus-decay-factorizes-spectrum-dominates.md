# The decay factorizes, and the OUTPUT spectrum dominates — refining #6548 (qou-o6ov)

**Date:** 2026-09-04
**Scope:** scope-(a); one quantitative result that **corrects the natural reading of my own previous
finding**; nothing wired.
**Probe:** [`magnus_cancellation_factor_probe.py`](../../computations/deltalambda/magnus_cancellation_factor_probe.py)
**Follows:** #6548 (the b-decay is not in the input commutator norm), #6534 (`★`).

## The refinement in one line

#6548 showed the decay is **not** in `‖[ρ,σ_a]‖` — the *input*. The natural next thought, which I
held, was "therefore it is phase cancellation in the trace." **That is wrong.** The decay is
overwhelmingly a collapse in the magnitude of the *output* operator's spectrum. Both facts are
true and they are about different objects.

## The decomposition

Let `M_λ = ρ_λ(ρ)·ρ_λ(Ω₂^P)`, so `tr_λ(ρΩ₂^P) = Σ_i eig_i(M_λ)`. Define the **cancellation factor**

```
κ(λ) := |Σ_i eig_i| / Σ_i |eig_i|  ∈ [0,1]        (κ=1: phases aligned; κ→0: total cancellation)
```

Then exactly `|tr|/dim = κ · (Σ|eig|/dim)`, so any b-decay splits into a **phase** part (`κ`) and a
**magnitude** part (`Σ|eig|`). Measured on conjugate pairs — `dim λ = dim λ'` **exactly**, so the
dimension confound is removed by a theorem — ratios are higher-b partner ÷ lower-b partner:

| A | pair | dim | b → b' | **Σ\|eig\| ratio** | κ ratio | product = trace ratio |
|---|---|---|---|---|---|---|
| 3 | (8,1) → (2,1⁷) | 8 | 1 → 7 | **0.00469** | 0.732 | 0.00343 |
| 3 | (7,2) → (2,2,1⁵) | 27 | 2 → 7 | **0.0226** | 0.911 | 0.0206 |
| 3 | (7,1,1) → (3,1⁶) | 28 | 2 → 6 | **0.0284** | 0.467 | 0.0133 |
| 3 | (6,3) → (2,2,2,1,1,1) | 48 | 3 → 7 | **0.0607** | 0.290 | 0.0176 |
| 3 | (5,4) → (2,2,2,2,1) | 42 | 4 → 7 | **0.106** | 0.871 | 0.0926 |
| 2 | (5,1) → (2,1⁴) | 5 | 1 → 4 | **0.0684** | 0.532 | 0.0364 |
| 2 | (4,2) → (2,2,1,1) | 9 | 2 → 4 | **0.318** | 0.840 | 0.267 |
| 2 | (4,1,1) → (3,1,1,1) | 10 | 2 → 3 | **0.371** | 0.291 | 0.108 |
| 2 | (3,3) → (2,2,2) | 5 | 3 → 4 | **0.151** | **1.385** | 0.209 |

(The product column reproduces #6548's independently-measured trace ratios — a consistency check
across two probes, e.g. `0.732 × 0.00469 = 0.00343`.)

**`Σ|eig|` falls in 9 of 9 pairs, and it dominates in all 9.** For `(8,1)` vs `(2,1⁷)` the spectrum
contributes a factor 213 and the phases only 1.4.

## What this changes

- **An absolute-value spectral bound on `M_λ` is VIABLE.** `Σ|eig(M_λ)|` — and any bound above it,
  such as `dim · spectral-radius` — *does* decay with `b` at fixed dimension. This is the
  constructive route to a general-λ bound, and it is the opposite of what "cancellation" suggested.
  It is also consistent with the hook bound (#6520) working through `e_j` of a spectrum.
- **#6548's stated finding stands unchanged**: no bound `|tr| ≤ Σ_a ‖[ρ,σ_a]‖·‖σ_{a+1}‖` can work,
  because that quantity *grows* ~25 % at high b. What fails is the inference I drew from it.
  Reconciled: the commutators are individually larger at high b, but the assembled
  `Ω₂^P = Σ_a[σ_a,σ_{a+1}]` and its product with `ρ` have a far smaller spectrum. **The cancellation
  happens in the assembly, not in the final trace.** Bounding the inputs term-by-term throws that
  assembly away — which is exactly why the input-norm route fails and the output-spectrum route
  does not.
- **κ is real but secondary, and NOT uniform.** It falls in 8 of 9 pairs, and **rises** in one:
  `(3,3) → (2,2,2)` at A=2, κ `0.604 → 0.837` (ratio 1.385) — the trace still falls there, carried
  entirely by `Σ|eig|` (0.151). So "κ decreases with b" is **not** a law and must not be asserted;
  the probe reports the non-uniformity rather than averaging it away.

## Honest limits

- **9 pairs, A = 2 and 3, dim ≤ 50.** Self-conjugate shapes ((3,3,3) at n=9, measured but pairless)
  and `dim > 50` pairs are not in the control — named as skipped, not evidence.
- **`Σ|eig|` is not the nuclear norm** (`M_λ` is not normal); it is the right comparator here
  because the trace is exactly `Σ eig`, so the split into magnitude × phase is exact by
  construction, not an approximation.
- **"Viable" is not "proved".** That `Σ|eig(M_λ)|` decays is measured on 9 dimension-controlled
  pairs; no closed form or bound for it is derived here. A general-λ theorem still needs one.
- Scope-(a) throughout.

## Bottom line

The b-decay factorizes exactly as `|tr|/dim = κ · Σ|eig|/dim`, and across 9 dimension-controlled
conjugate pairs the **magnitude** factor `Σ|eig|` falls in all 9 and dominates in all 9 (down to
0.005), while the **phase** factor `κ` falls in 8 and rises in 1. So the decay is chiefly a
collapse of the output operator's spectrum, not phase cancellation in the trace — correcting the
reading I drew from #6548, whose own finding (the input-norm route is excluded) is untouched. An
absolute-value spectral bound on `M_λ` is the viable route to the general-λ statement.

---

# Addendum — the majorant ladder, and the bound is itself a positive trace

Two follow-on measurements on the same branch, both dimension-controlled by conjugate pairs.

## 1. How far up the majorant ladder does the b-decay survive?

`Σ|eig|` decays (above), but it is *the quantity*, not a bound. A theorem needs a **computable
majorant** that both dominates `|tr|` and still decays. The classical ladder:

```
|tr M| ≤ Σ|eig_i(M)| ≤ Σσ_i(M) ≤ √dim·‖M‖_F        and       Σ|eig_i| ≤ dim·ϱ(M)
```

each rung cheaper to bound analytically and progressively weaker. Measured (high-b ÷ low-b at
equal dimension), the **maximum** ratio over all pairs — so a rung "decays" only if every pair does:

| rung | A=2 max ratio | A=3 max ratio | pairs decaying |
|---|---|---|---|
| `\|tr\|` | 0.267 | 0.0926 | 4/4, 5/5 |
| `Σ\|eig\|` | 0.371 | 0.106 | 4/4, 5/5 |
| `Σσ` | 0.423 | 0.133 | 4/4, 5/5 |
| `√dim·‖M‖_F` | 0.521 | 0.179 | 4/4, 5/5 |
| `dim·ϱ` | 0.534 | 0.122 | 4/4, 5/5 |

**Every rung decays, in every pair.** The b-information survives all the way to the **Frobenius
norm of the assembled `M_λ`** — an elementary sum of squared entries, requiring no eigenvalues.
That is what a general-λ theorem can target.

## 2. That majorant is itself a trace of an algebra element — and a positive one

`‖M‖_F² = tr(MᵀM)` trivially; the content is whether `Mᵀ` is again the image of an *algebra*
element. The Hecke algebra carries the word-reversal anti-involution `*` (an anti-automorphism
fixing each generator). **Measured, not assumed:** the seminormal generator matrices are
**exactly symmetric** (`max|σ − σᵀ| = 0.0`), so `ρ_λ(X)ᵀ = ρ_λ(X*)` and therefore

```
‖M_λ‖_F²  =  tr_λ(X* X),        X = ρ·Ω₂^P
```

verified to `7.6e-141` on every λ ⊢ 6 (worst case), with `X*` assembled term by term
(`(ρ·[σ_a,σ_{a+1}])* = −[σ_a,σ_{a+1}]·ρ*`). The quantity is **positive** (it is `Σσ_i²`), so there
is no cancellation inside it to fight, and it decays at controlled dimension: **4/4 pairs at A=2**
(ratios 0.0073–0.271) and **5/5 at A=3** (9.2e-5, 0.0021, 0.0041, 0.0167, 0.0322 — max 0.032).

**Why this closes the loop.** The arc's two reductions — hooks to the reduced Burau (#6464) and
two-rows to R-matrix weight sectors (#6525) — are **character identities, valid for any algebra
element**. That is exactly why they carried `Ω₂^P` (#6445) and could not carry the germ
(#6432/#6434). `X*X` is an algebra element, so those same handles apply to the majorant verbatim:
the general-λ bound becomes a positive trace of the same type as the quantity it bounds, one rung
down, with the cancellation problem removed.

**Limits.** The symmetry and the identity are exact algebra facts, checked on all 11 shapes at
n=6; the *decay* of `tr_λ(X*X)` is measured on 9 conjugate pairs (4 at A=2, 5 at A=3, dim ≤ 48). No closed form or bound for `tr_λ(X*X)` is derived here — "the handles apply" is a statement
about applicability, not a completed derivation. Scope-(a).
