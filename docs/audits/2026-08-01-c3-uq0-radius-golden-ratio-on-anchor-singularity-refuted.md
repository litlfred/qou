# c₃ argument map u(q₀): radius of convergence is 2·log φ ≈ 0.962 — on-anchor-singularity REFUTED (2026-08-01)

**Axis:** Q_β c₃ bar-odd `S` — the argument map `u(q₀)` (`qou-82w7` / `qou-iyj5`,
the survivor after the sum-branch closure). **No c_k wired; no fit; registry
untouched; no `SDeformedVolumeChannel` instance fabricated.** This is the **decisive
test** the `qou-iyj5` bean called for, and it comes back with a clear, validated
answer.

## The question

After this session closed all lattice-sum routes to the c₃ magnitude (scope-(b) via
Thurston, [PR #4503](https://github.com/litlfred/qou/pull/4503)), the sole survivor is
the single geometric structure `u(q₀)`. The muon anchor is `2.05×` the leading
supremum `(√3/4)(ln q₀)²` under the pinned boost `Re u = ln q₀`; closing that gap
under the exact `𝔙₄₁` would need its NZ Taylor to have quartic/quadratic `≈ 97`, i.e.
**radius `R ≈ 0.10 ≈ u`** — a transcendental singularity *at* the anchor (the
resurgence / hypersensitivity reading). The decisive test: **compute `R` directly.**

## The computation (slip-safe: algebraic + validated against the proved √3/4)

The singularities of the geometric complex volume `𝔙₄₁(u)` are the branch points of
the figure-8 A-polynomial's longitude branch — roots of `disc_L A = 0` — in the
`u = log(M²) = log q₀` plane. No NZ integration needed.

**A-polynomial** (textbook, Cooper–Culler–Gillet–Long–Shalen):
`A(M,L) = M⁴L² − (M⁸−M⁶−2M⁴−M²+1)L + M⁴`, with `A(1,L) = (L+1)²` (completeness,
longitude `−1`, ✓ figure-8 framing).

```
disc_L A = (M−1)²(M+1)²(M²+1)² · (M²−M−1)(M²+M−1)(M²−M+1)(M²+M+1)
```

The first three factors are the M-coordinate artifact at the complete structure
(`𝔙(u)` is analytic there — `u` is the good coordinate). The **geometric** branch
points are the last four: `x = M² ∈ {φ², φ⁻², e^{±2πi/3}}`.

| branch point `x = M²` | `|u| = |log x|` |
|---|---|
| `φ² = (3+√5)/2` and `φ⁻²` | **`2·log φ ≈ 0.96242`** ← nearest |
| `e^{±2πi/3}` | `2π/3 ≈ 2.09440` |

So `R = 2·log φ ≈ 0.9624` (φ = golden ratio): **the figure-8 geometric structure
degenerates when the meridian eigenvalue `M` reaches the golden ratio `φ`.**

**Validation of the A-poly + convention.** Puiseux expansion at `u=0`:
`A = (1+2u+2u²)(L+1)² − 3u²L + O(u³)`, so `(L+1)² = −3u²`, `L ≈ −1 ± i√3·u`, cusp
shape `τ = ∓i√3`, and leading `Im 𝔙₄₁(u) = (√3/4)u²` — **exactly** the corpus's proved
coefficient (`FigureEightComplexVolume.lean`). The A-polynomial and the
`u = log q₀` convention are therefore correct.

**Anchor position:** `u = ln q₀ ≈ 0.1043 = 0.108·R` — deep inside the disc.

Probe: [`qbeta_c3_uq0_radius_branchpoint_probe.py`](../../computations/qbeta/qbeta_c3_uq0_radius_branchpoint_probe.py)
(exit 0), witness
[`qbeta-c3-uq0-radius-branchpoint.witness.json`](../../computations/qbeta/qbeta-c3-uq0-radius-branchpoint.witness.json).

## Verdict — on-anchor-singularity REFUTED

`R ≈ 0.962 = O(1)`, **not `~0.1`**. The argument map `u(q₀)` is analytic with an O(1)
radius; there is **no singularity near the anchor** to source the `2.05×` muon
boost-enhancement or a `dc₃/dq` hypersensitivity. This decides the two live readings
of `qou-iyj5`:

- **(rejected) on-anchor-singularity / resurgence-at-anchor.** Would require `R ≈ 0.1`.
  It is `0.96`. The `dc₃/dq ≈ 4.7×10⁶` hypersensitivity **cannot** be an analytic
  near-singularity of a single `u(q₀)` — the nearest singularity is 9× farther away
  than the anchor.
- **(favored) either geometric boost-enhancement or the [W] discrete-winding reframe.**
  Since `u(q₀)` is smoothly analytic near the anchor, the `2.05×` gap and the
  muon/proton sign flip cannot come from hypersensitive analytic variation of a single
  `u(q₀)`. This **favors the [W] picture** (direction 4): the muon/proton difference is
  a *discrete winding/channel* datum, not a `10⁻⁸`-gap hypersensitivity — consistent
  with `sign Im 𝔙₄₁ = sign G(m,ℓ)` being arithmetic. Alternatively the boost `Re u` is
  geometrically enhanced beyond `ln q₀` (factor `≈ 1.43`; note `1.43` is *not* `√2`, so
  no clean doubling), a mechanism that is now constrained to be **smooth/geometric, not
  singular**.

## Bearing on the directions

- **Direction 1 (this doc):** the decisive `qou-iyj5` test is **done** — `R = 2 log φ`,
  on-anchor-singularity refuted, A-poly validated against the proved `√3/4`.
- **Direction 4 (reconcile [W]):** materially advanced — the refutation of on-anchor
  hypersensitivity **removes the main tension** and favors the discrete-winding reading.
  The remaining reconciliation is to identify the muon/proton windings (still open).
- **Direction 5 (Q_β Habiro `F(q)`):** untouched — this is an *archimedean-level* result
  about the analyticity of the observable map `u(q₀)`; the *fibre-level* Habiro element
  remains the deeper open object (AGENTS.md Im(q) fibre-vs-observable framing).

## What stays open

The value of `u(q₀)` (equivalently the boost-enhancement `A ≈ 2.05` / the muon/proton
winding assignment) is still open — but the search is now sharply constrained: **it is
a smooth/geometric or discrete-arithmetic effect, NOT an analytic on-anchor
singularity.** Do not route a c₃ closure through a resurgence-at-anchor / essential-
singularity hypothesis for the single-structure `u(q₀)` — its radius is `O(1)`.

-- Ref: [manuscript] .beans/qou-iyj5 (single-structure survivor; this is its decisive test)
-- Ref: [manuscript] docs/audits/2026-08-01-c3-magnitude-full-volume-thurston-sum-exclusion.md (#4503)
-- Ref: [manuscript] docs/coordination/udeform-spin-part-derivation.md ([W] discrete-winding reframe)
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md (qou-82w7)
