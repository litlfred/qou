# c₃ direction 1: exact figure-8 Im 𝔙₄₁ confirms the A≈2.05 gap is a boost-rapidity enhancement (2026-08-01)

> **Resolution landed on main (cross-ref, cherry-picked 2026-08-07).** This note's open
> content — "derive the boost factor `c = √A ≈ 1.4305`" — is **reduced** by a merged
> sibling result: `A = 2` (`c = √2`) is Lean-exact = the Neumann–Zagier ½ normalization
> `κ_shape/κ_pot = 2` (`QOU/QBeta/BoostFactorNZNormalization.lean`; audit
> [`2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md`](2026-08-01-c3-boost-factor-nz-half-normalization-and-precision-ceiling.md)),
> and the residual `2.0 → 2.054` is amplification noise below a `σ_A ≈ 40 %` precision
> ceiling (`c` cannot be *identified*, only reduced). Verdict **REDUCED** (scope-a).
> This file is the complementary **exact-CS-integral origin** of `c = √A`; the structural
> reason + ceiling live in that sibling audit. Open content tracked in bean `qou-yh67`
> (this bean `qou-iyj5` marked REDUCED).

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
is a single `O(1)` enhancement factor `c ≈ 1.4305` (exact solve; leading-quadratic proxy
`√A ≈ 1.4332`) of the boost rapidity — **derive it
geometrically (not fit it)**. This does not close the gap, but it is the tightest the
target has ever been stated.

-- Ref: [manuscript] docs/audits/2026-08-01-c3-uq0-radius-golden-ratio-on-anchor-singularity-refuted.md (#4508)
-- Ref: [manuscript] docs/audits/2026-08-01-c3-hypersensitivity-is-u3-extraction-artifact.md (#4509)
-- Ref: [manuscript] .beans/qou-iyj5 (the survivor: boost-enhancement A≈2.05, c≈1.4305)

## Addendum — A is consistent with EXACTLY 2 (c=√2), within the amplification uncertainty

Testing the clean hypothesis `A = 2` (`c = √2`, a candidate two-tetrahedra /
log-holonomy `u = 2·log M` doubling) against the data:

| `c` | `Im𝔙₄₁` | `A` | miss vs `S(muon)` |
|---|---|---|---|
| `1` (meridian boost) | `0.004723` | `1.002` | `−51%` |
| **`√2` (A=2)** | **`0.009463`** | **`2.007`** | **`−2.27%`** |
| `1.4305` (fits A=2.054) | `0.009683` | `2.054` | `0.001%` |
| `2` | `0.018996` | `4.03` | `+96%` |

The `c=√2` (A=2) miss of `2.27%` corresponds to a q₀-shift of only
**`Δq = 5.7×10⁻¹¹`** — **20× smaller than the q₀ pin precision (~`10⁻⁹`)**. Because
`S(muon)` is a `1/u³`-amplified near-threshold quantity (#4509, `dS/dq ≈ 4×10⁶`), its
value is uncertain at the ~2–3% level from the q₀-pin definition alone. **The data
therefore cannot distinguish `A = 2` from `A = 2.054`.**

**Reframed survivor (hopeful).** The boost-enhancement is **consistent with the clean
factor `c = √2` (`A = 2` exactly)** — the apparent `2.054` is plausibly the amplified
image of an underlying `A = 2`. If `A = 2` is a *derived* doubling (the figure-8's two
ideal tetrahedra, or the `u = 2·log M` log-holonomy convention), the survivor closes:
the effective boost is `√2·ln q₀` and the `0.054` excess is amplification noise, not
open physics. **This is a consistency result, not a proof** — deriving the factor-2
mechanism (two-tetrahedra / holonomy doubling) is the concrete remaining task, and must
be a *derivation*, not a fit. Next probe (`qou-iyj5`): derive the `A = 2` doubling from
the figure-8 tetrahedron count / the log-holonomy convention.
