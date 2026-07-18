# α_EM per-loop measure is a Gauss–Bonnet object, not a b₁-object (2026-07-18)

**Tier:** distinct-route measurement on the α_EM per-loop measure (research-overlap
relaxation, 2026-07-18; posted as the discriminant on #3864). Audit-only; no
`α_k` wired; no fit; `1/(8π)` stays a phase-4 identification. scope-(a).
**Branch:** `claude/alpha-em-gauss-bonnet-measure-2026-07-18`.

## The tension this resolves

The spectral-determinant route (#1552 / #3870 / #3864) reads the per-loop measure
as `1/(π·b₁) = 1/(8π)` and hunts for a ζ-determinant on `Jac(Bring) ~ T⁸` that is
area-free + bare-π + **reciprocal in b₁**. The channel-split route (#3810) reaches
`1/(8π) = ½·(1/(4π))` (two Hecke channels × the gauge loop unit), with the `b₁`
form a **genus-4 coincidence**. The two are numerically identical at `g=4` but
predict opposite genus-scaling. This probe settles the discriminant.

## The identity (verified symbolically for all g)

Hyperbolic Gauss–Bonnet gives `Area = −2π·χ = 2π·|χ|`, so:

| quantity | geometric form | scaling |
|---|---|---|
| gauge loop unit | `1/(4π) = |χ|/(2·Area)` | genus-independent |
| **per-loop measure** | **`1/(8π) = |χ|/(4·Area)`** | **genus-independent** |
| b₁ reading | `1/(π·b₁) = 1/(2π·g)` | scales as `1/g` |

`|χ|/(4·Area) = |χ|/(4·2π|χ|) = 1/(8π)` for **every** genus. The b₁ reading
equals it **only at `g=4`** (`b₁=8`, `|χ|=6`: `6/(4·12π) = 1/(8π) = 1/(π·8)`);
at `g=5` they diverge (`1/(8π)` vs `1/(10π)`).

## Consequence

- **The measure is a Gauss–Bonnet invariant `|χ|/(4·Area)`, not a Betti (b₁)
  object.** The `b₁` appearance at `g=4` is coincidental (`b₁=8`, `|χ|=6`, and
  `6/(4·Area)=1/(π·8)` holds only there). A spectral object with genuine `b₁^{-1}`
  scaling would be the wrong shape — Gauss–Bonnet ties `Area` to `|χ|`, forcing
  genus-independence.
- **The channel-split's one imported input is closed geometrically:** the
  "standard gauge loop unit `1/(4π)`" **is** `|χ|/(2·Area)` on any hyperbolic
  surface — no QFT correspondence assumption needed.

## Honest tier — re-scope, not full closure

This makes genus-independence manifest and geometrizes the loop unit; it does
**not** independently derive the factor `½` (two braiding channels) or the `1/4`
grouping — those are the #3810 channel-split structure. What is new: the measure
is a `(χ, Area)` invariant, answering the #3864 tension in favour of
genus-independence. Bring: `(2,4,5)`-tiling, `g=4`, `χ=−6`, `Area=12π` (=
`4π(g−1)`); see the merged `EmCouplingBringZeroMode` Lean. No fit; no `α_k`
wired; `1/(8π)` stays phase-4.
