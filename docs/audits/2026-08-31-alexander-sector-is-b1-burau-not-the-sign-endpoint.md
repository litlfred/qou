# The Alexander sector is b=1 (reduced Burau), NOT the sign endpoint — correcting #6387 (qou-o6ov)

**Date:** 2026-08-31
**Directive (owner):** work the decay rate + the Schur–Weyl bridge (does the sign-rep endpoint
equal the color-`n` Alexander sector?).
**Scope:** scope-(a); corrects a prior claim; no MeV, no fit, nothing wired.
**Probe:** [`magnus_alexander_sector_check_probe.py`](../../computations/deltalambda/magnus_alexander_sector_check_probe.py)
**Corrects:** #6387 (which *suggested* the sign rep `(1ⁿ)` is "the fully-antisymmetric =
Alexander sector"). That was marked "suggestive, not established" — and it is **wrong**.

## The bridge question, answered: NO

**The sign-rep endpoint does NOT equal the Alexander sector.** There are **three distinct
Alexander appearances**, and #6387 conflated the wrong two:

| # | object | parametrization | Alexander? |
|---|---|---|---|
| (a) | colored Jones, large **color** `N`, `q→1` (Melvin–Morton–Rozansky) → `1/Δ` | the `U_q(sl₂)` **coloring** `N` | yes, as a *limit* |
| (b) | **reduced Burau** = reflection Hecke irrep `(n−1,1)` = **`b=1`**; `Δ_K(t) ∝ det(I − Burau(β))` | Hecke **strand-partition** `λ` | **yes, a fixed rep** |
| (c) | **sign rep** `(1ⁿ)` = fully-antisymmetric = **`b=n−1`** (the decay endpoint) | Hecke strand-partition `λ` | **NO** |

The user's "color-`n` Alexander sector" is **(a)** — a large-color limit. The decay endpoint
is **(c)**. They are neither equal nor even in the same parametrization. And within the Hecke
`b`-grading the genuine Alexander carrier is **(b)** at `b=1` — the decay's **peak**, not its
endpoint.

## Why (c) is information-free (verified)

In the sign rep `(1ⁿ)` every generator acts as the **scalar** `σ_i = −q⁻¹` (dim 1), so
`ρ = ∏σ_{g_i} = (−q⁻¹)^L` — a monomial carrying only the writhe/framing, **no knot
information, no Alexander polynomial**. Measured (A=2,3): `σ_i = −0.900918 = −q⁻¹` exactly;
`ρ` is a scalar; and `⁅A_a,A_{a+1}⁆=0` ⇒ `tr(ρ Ω₂)=0` (#6387's exact-zero endpoint). So the
endpoint is where the invariant **degenerates to writhe**, the opposite of the
Alexander-rich sector.

## Why (b) is the Alexander sector (verified dim + citation)

The `b=1` reflection rep `(n−1,1)` has dim `n−1` (verified: 5 at A=2, 8 at A=3), matching the
**reduced Burau representation** of `B_n`. That the reduced Burau *is* the `(n−1,1)` Hecke
irrep and yields the Alexander polynomial is standard (Jones 1987, *Hecke algebra
representations of braid groups and link polynomials*); its unitary form is
`library/squier-burau-unitary-1984` (Squier 1984). So the Alexander polynomial lives at
**`b=1`**.

## The decay runs AWAY from Alexander (verified)

`|tr(ρ_λ Ω₂)|/dim` by `b` (max-dim `λ` of each `b`):

| A | b=1 (Burau/Alexander) | b=2 | b=3 | b=4 | … | endpoint |
|---|---|---|---|---|---|---|
| 2 | **10.24** (peak) | 4.84 | 1.34 | 0.55 | | sign `b=5`: 0 |
| 3 | **46.0** (peak) | 17.9 | 4.09 | 0.38 | 0.09 (b5) | sign `b=8`: 0 |

The germ trace **peaks at `b=1`** — the Burau/Alexander sector — and **decays toward the
trivial sign endpoint**. So the Alexander structure is at the **source** of the decay, and the
decay is precisely the departure from the Alexander/Burau sector into the higher-`b` bulk and
on to the information-free sign rep.

## The rate (partial, honest)

- **Correct framing:** the rate is the fall-off of `|tr(ρ_λ Ω₂)|/dim` as `λ` moves from the
  `b=1` reduced-Burau peak toward the `b=n−1` sign zero.
- **Empirically rapid:** in the measured range `|tr|/dim` drops by ~2.6× to ~11× **per
  `b`-step** (A=3: 46 → 17.9 → 4.1 → 0.38), i.e. faster than any fixed exponential over the
  early steps — though `dim` varies with `b`, so no single closed rate is claimed.
- **Still open, and not a simple support count.** The naive "few columns ⇒ 3 strands share a
  column ⇒ `σ` scalar ⇒ commutator vanishes" intuition explains the *endpoint* (sign rep, one
  column) but **not the rate**: #6349 measured the local commutator `‖⁅σ_g,A_a⁆‖_F = Θ(√dim)`
  (it does *not* shrink), and #6354 showed the trace decay is the **trace-orthogonality**
  `⟨⁅ρ,A_a⁆,A_{a+1}⟩_F/dim → 0`, not a support collapse. The rate is governed by that
  orthogonality, which remains the open theorem.

## Bottom line

Answer to the bridge question: **NO** — the sign-rep endpoint is information-free (writhe-only)
and is *not* the Alexander sector; the Alexander carrier is the `b=1` reduced-Burau reflection
rep, the decay's **peak**, and the MMR "color-`N` Alexander" is a third, different (large-color)
limit. **This corrects #6387**, which had the direction backwards. The decay is the departure
*from* the Burau/Alexander sector; its rate is the trace-orthogonality (#6354), still open.
