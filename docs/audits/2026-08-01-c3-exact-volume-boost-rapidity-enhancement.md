# c₃ direction 1: exact figure-8 Im 𝔙₄₁ confirms the A≈2.05 gap is a boost-rapidity enhancement (2026-08-01)

**Axis:** Q_β c₃ bar-odd `S` — direction 1, the direct assault on the survivor
(`qou-iyj5`). **No c_k wired; no fit; registry untouched.** The exact figure-8 complex
volume **confirms** the `A ≈ 2.05` muon gap is a genuine boost-rapidity enhancement —
not a spin part, not higher volume terms.

## Exact Im 𝔙₄₁ (slip-safe: A-polynomial branch + √3/4-validated convention)

At a real boost `M = √q₀`, the geometric longitude branch `L(M)` lies on the unit
circle (`|L|=1`; `disc B²−4M⁸ < 0`), rotating from `−1` by `θ = arg(−L)`, with `θ ≈ √3·u`
near `u=0`. The exact bar-odd (CS) face is

```
Im 𝔙₄₁(u) = ½ ∫₀^u arg(−L(M(u'))) du' ,   M(u') = e^{u'/2} ,
```

with the `½` convention fixed empirically: it reproduces the corpus's proved leading
`(√3/4)u²` to **0.18%** at `u = ln q₀` (ratio → 1 as `u → 0`). Probe:
[`qbeta_c3_exact_volume_boost_enhancement_probe.py`](../../computations/qbeta/qbeta_c3_exact_volume_boost_enhancement_probe.py).

## Findings

| quantity | value |
|---|---|
| `Im 𝔙₄₁(real boost u = ln q₀)` exact | `0.0047229` |
| leading `(√3/4)(ln q₀)²` | `0.0047142` |
| `A(real boost, exact)` | `1.0018 ≈ 1` |
| `S(muon)` target | `0.0096830` (`A = 2.054`) |
| boost enhancement needed | `Re u = c·ln q₀`, `c = 1.4305` |
| `√A` / `√2` | `1.4332` / `1.4142` |

1. **The exact potential does NOT close the gap.** Higher-order terms of `𝔙₄₁` are
   negligible at the anchor (`A(real boost) = 1.002`), exactly as the radius
   `R = 2·log φ ≈ 0.96 ≫ u = 0.104` (#4508) predicts. The exact `Im 𝔙₄₁` at the meridian
   boost is `~half` of `S(muon)`.
2. **The gap is UNAMBIGUOUSLY a boost-rapidity enhancement.** `Im 𝔙₄₁ = (√3/4)(Re²u − Im²u)`,
   so a spin part `Im u ≠ 0` only *decreases* `Im 𝔙₄₁` — it cannot raise `A` above 1.
   Only a larger `Re u` can. So the survivor is not a spin part and not a potential-shape
   effect: it is `Re u = c·ln q₀` with `c ≈ 1.43`.
3. **`c = 1.4305 = √A`** (since exact ≈ leading quadratic at the anchor), and it is **not**
   `√2 = 1.4142` (differs 1.15%) — no clean geometric origin identified.

## Net — the survivor, maximally sharpened

The whole c₃ magnitude problem now reduces to one crisp question:

> **Why is the effective boost rapidity in the CS face `√2.05·ln q₀ ≈ 1.43·ln q₀`,
> rather than the meridian rapidity `ln q₀`?**

Everything else is closed or reframed: lattice-sum routes excluded (scope-b, #4503),
argument map smooth (radius `2 log φ`, #4508), hypersensitivity a `1/u³` extraction
artifact (#4509), spin part / higher volume terms ruled out (this doc). The open content
is a single `O(1)` enhancement factor `c = √A ≈ 1.43` of the boost rapidity — **derive it
geometrically (not fit it)**. This does not close the gap, but it is the tightest the
target has ever been stated.

-- Ref: [manuscript] docs/audits/2026-08-01-c3-uq0-radius-golden-ratio-on-anchor-singularity-refuted.md (#4508)
-- Ref: [manuscript] docs/audits/2026-08-01-c3-hypersensitivity-is-u3-extraction-artifact.md (#4509)
-- Ref: [manuscript] .beans/qou-iyj5 (the survivor: boost-enhancement A≈2.05 = c=√A≈1.43)
