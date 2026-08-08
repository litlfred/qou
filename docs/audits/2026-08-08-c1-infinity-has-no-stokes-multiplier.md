# There is no Stokes multiplier at C1's `∞` — I mis-stated the open item

**Date:** 2026-08-08 · **Axis:** C1 `∞`-residual (`qou-vkg5`) · **Tier:** correction
of my own claim + one Lean instance. **No fit, nothing wired, no Stokes multiplier
computed — because there is none to compute.**

## The claim being retracted

Across PRs #4771 and #4783 I repeatedly wrote that the remaining open item was
*"compute C1's Stokes multiplier at `∞`"*, most recently as a scoreboard row:

> | **Stokes multiplier** | **OPEN — the only remaining item** |

**That item does not exist.** C1 at `∞` is **pure isoclinic**, and a pure
isoclinic module has no local q-Stokes phenomenon. Not "hard to compute" —
*nonexistent*.

## Why, from RSZ

Two independent statements, both already in the corpus:

**1. The dimension formula.** RSZ Thm 3.3.5,
`dim F(P₁,…,P_k) = Σ_{i<j} rᵢrⱼ(μⱼ − μᵢ)`. At `k = 1` the index set `{i < j}` is
empty, so the isoformal space is a point. Formalized in
[`RSZIsoformalInterface.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/RSZIsoformalInterface.lean)
as `rszIsoformalDim_one`, whose docstring I wrote in #4721 and which says, verbatim:

> *"A pure isoclinic module has no isoformal moduli, hence no Stokes data to
> extract."*

**2. The Stokes sheaf.** Per
[`2026-07-20-qlift-doorI-analytic-summation.md` §1](2026-07-20-qlift-doorI-analytic-summation.md)
reading RSZ §5.5.2 / Thm 5.5.7 / §4.4 directly: the q-Stokes matrices
`St_{λ₀}(λ;A)` are **upper-triangular unipotent** automorphisms inducing the
**identity on `gr M₀`**, and the phenomenon *is* the ambiguity between generic
divisor partitions among the slope pieces. With one slope there is no
strictly-upper-triangular part and nothing to partition: the Stokes group is
trivial.

Both say the same thing by different routes.

## That C1 is pure isoclinic at `∞` was settled three weeks before I started

[`2026-07-20-qlift-routeA-rsz-invariants.md` §2](2026-07-20-qlift-routeA-rsz-invariants.md):
the `∞` Newton polygon of `L1` has the single edge `(r,d) = (2,1)`, slope **½
with multiplicity 2** — *pure isoclinic, non-integral*, the irreducible rank-2
`E(2,1,·)` of RSZ §2.2.2.2 (restriction of scalars of a rank-1 slope-1 line on
the 2-cover). Machine-cross-checked there by an mpmath lower-hull script.

So the premise was in the corpus on 2026-07-20, I re-derived the same single edge
independently in #4721, wrote the dim-0 consequence into a Lean docstring in that
same PR — and then stated the opposite three times.

## How it happened

Not a computation error; a **framing** error, and the same shape as the one #4721
was written to fix. The 2026-08-01 chain said "slope ½ ⇒ two Stokes multipliers
`U ∈ ℂ²`". #4721 killed the *derivation* of that number, showing §3.3 does not
apply and `dim = 0` at `k = 1`. But I kept the *noun* — "the Stokes multiplier" —
as the name of the residual, and never re-asked whether the object survived its
own refutation. The corpus-grep checklist would have caught it: I grepped for
`{0,1,∞}`, for existing beans, for overlapping declaration names, but never for
`pure isoclinic`, which is the phrase that decides it and which returns six hits
across three prior audits.

## What is actually true about C1's `∞`

| item | status |
|---|---|
| formal class at `∞` | pure isoclinic, `E(2,1,c)`, slope ½ mult 2 |
| the class parameter `c` | determined: edge equation `q²t² = q−1`, product fixed by `det A`, residual freedom exactly the deck sign |
| weight lattice | `q^{½ℤ}`, up to deck sign |
| **analytic moduli within that formal class** | **a point — `dim = 0`. No Stokes data.** |

The local story at `∞` is therefore **closed**, not open. The "residual freedom"
I characterised in #4771/#4783 as constraining an unknown multiplier is in fact
the *whole* local invariant, and it is computed.

## What, if anything, remains

**Not** a local Stokes multiplier. The candidates are genuinely different objects
and each needs its own justification before being called open:

1. **Global connection data between `0` and `∞`** — the q-analogue of monodromy,
   the Birkhoff connection matrix, theta/elliptic-valued. This is *not* local
   Stokes data and is not excluded by anything above. It is the honest successor
   target. **Not started, and not claimed to be needed for anything downstream.**
2. **The `q^{½ℤ}` lattice's role downstream** — whether the deck sign or the
   half-integral weight feeds any Q_β / c_k object at all. Unexamined.

Both are stated as *questions*, not as open items with an expected answer. Per
AGENTS.md §"Before declaring 'open'", promoting either to a tracked open item
requires the corpus-grep checklist first — which is precisely the step whose
omission produced this retraction.

## Landed with this correction

`c1_infinity_isoformalDim_eq_zero` in
[`RSZIsoformalInterface.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/RSZIsoformalInterface.lean):
the *instance*, not just the general lemma — C1's own `∞` data after the forced
ramified pullback (`k = 1`, `r = 2`, slope `1`) has isoformal dimension `0`. The
general fact was already there and got restated wrongly anyway; a named instance
mentioning C1 is harder to walk past.

-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853 (Thm 3.3.5, §4.4, Thm 5.5.7, §2.2.2.2)
-- Ref: [manuscript] docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md
-- Ref: [manuscript] docs/audits/2026-07-20-qlift-doorI-analytic-summation.md
-- Ref: [manuscript] docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md
