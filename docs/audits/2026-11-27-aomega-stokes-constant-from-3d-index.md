# The 4₁ Stokes constant 3 read from the 3d index (2026-11-27)

**Bean:** `qou-vr3q` (G3 monodromy / Stokes-constant keystone).
**Probe:** [`computations/probes/qbeta_g3_stokes_from_3d_index_41.py`](../../computations/probes/qbeta_g3_stokes_from_3d_index_41.py),
witness `qbeta-g3-stokes-from-3d-index-41.witness.json` (8/8 exact assertions).
**Lean:** [`QOU/Nuclear/StokesIndexCount41.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/StokesIndexCount41.lean),
`lean`-direct exit 0, no `sorry`, axioms `propext`, `Classical.choice`, `Quot.sound` only.

## Result

The figure-eight Stokes matrix `S⁺(x;q)` of Garoufalidis–Gu–Mariño is assembled
from the Dimofte–Gaiotto–Gukov 3d index alone. No `W₋₁` q-hypergeometric series
enters. Write `s = q^{1/2}` and let

    N_{ij}(x;q) = (−s)^{j−i} · Ind^rot(j−i, s^{i+j}x; q),   Ind^rot(m,ζ;q) = Σ_e I₄₁(m,e)(q) ζ^e,

with `I₄₁(m,e)` the bare two-tetrahedron sum (DGG eq 4.18, certified in
`qbeta_g3_fourone_index_assembly.py`). Then `S⁺ = L·N·R`, with

    L = [[−1, 0], [−x⁻¹(1−qx²−qx³)u, qx·u]],   R = [[−1, −(1+x−qx³)u], [0, −x·u]],   u = 1/(1−qx²).

`L` and `R` are not chosen. They come from GGM's own relations: the Stokes
formula eq (Sp-41), the recursion eq (W41rec) at `m = −1`, the Wronskian
relation eq (W41xm) at `m = 0`, and the block factorisation eq (WW41) of the
index. The Lean file proves that the closed forms are that gauge
(`gaugeL_spec`, `gaugeR_spec`, over any field).

At `q → 0`:

    S⁺(x;0) = [[1, x⁻¹ + 1 + x], [0, 1]]       (GGM eq S0x41)

and only two index coefficients carry the off-diagonal entry:

    S⁺₁₂(x;0) = (1+x)·[I₄₁(0,0)]_{q⁰} + x·x⁻²·(−[I₄₁(1,−2)]_{q^{1/2}}) = (1+x)·1 + x⁻¹·1.

At `x = 1` this is **3**: the vacuum, weighted by the gauge factor `1+x = 2`,
plus one BPS state at magnetic flux 1 and electric charge −2. The Lean theorem
`stokes_constant_three_from_index` checks that this equals the W-route value
`StokesQZeroDTCount.Splus0 0 1 = 3`.

## Checks (all exact integer arithmetic)

| check | through |
|---|---|
| `S⁺(x;0) = [[1, x⁻¹+1+x],[0,1]]` | exact |
| `S⁺₁₁(x;q) = Ind^rot(0,x;q)` (GGM eq S3Dx; forced by the gauge shape, Lean `stokes11_eq_index`) | q¹⁰ |
| GGM's printed x-deformed `𝒮⁺` entries | q² (all four) |
| `det S⁺(x;q) = 1` | q¹⁰ |
| GGM symmetry `𝒮⁺₁₂ = −𝒮⁺₂₁`, i.e. `S⁺₁₂ + S⁺₂₁ = (x⁻¹+1+x)·S⁺₁₁` | q¹⁰ |
| x = 1: printed towers GGM (61)–(64) | q⁶ |
| x = 1: equal to the W-route `S⁺(q)` coefficient by coefficient | q¹⁰ |
| stability under a larger charge cutoff and order | q¹⁰ |

## What this changes

- **Corrects** [`2026-07-14-g3-stokes-via-3d-index.md`](2026-07-14-g3-stokes-via-3d-index.md)
  §4, which said *"A_ω is not a coefficient read-off of I_41"* and that the index is
  *"an independent face, not the A_ω input"*. For 4₁ it is the input: through the
  fixed gauge the whole Stokes matrix is the index, and the `3` is two index
  coefficients.
- **Index-engine fix.** `qbeta_g3_fourone_index_assembly.I41` stopped its flux
  scan after five empty shells even when the contributing shells lay further
  out. At truncation degree 30 it returned `I₄₁(0,10) = I₄₁(1,10) = 0` while
  the mirror charges were non-zero (a broken DGG eq 4.19 symmetry). Small charges
  were never affected, so the certified anchors and that witness's payload are
  unchanged. The scan now counts empty shells only outside the charge window
  `|e₂| ≤ |m|+|e|+2`; the symmetry holds for `|e| ≤ 13`, `m ≤ 2`. PR #9778 fixed
  the same bug class in `borromean_3d_index.py`.
- **GGM misprint.** The display GGM eq (S11v) gives the q-coefficient of
  `S⁺₁₁(x;q)` as `−(2x⁻²+x⁻¹+2+x+2x²)`. The index gives
  `−(x⁻²+2x⁻¹+2+2x+x²)`, as in GGM's other display (after eq S0x41), because
  `I₄₁(0,±1) = −2q` and `I₄₁(0,±2) = −q`. *(Correction 2026-11-28: this is not
  new. [`2026-08-11-m1-adjudicated-erratum-and-the-three.md`](2026-08-11-m1-adjudicated-erratum-and-the-three.md)
  line 33 recorded the same erratum; the index route confirms it independently.)*

## Still open (named, not hidden)

1. GGM Conjecture `conj.41M` (the region matrices behind eq Sp-41). The
   W-route brick rests on it too, so both routes share this input.
2. A Lean proof of the two index coefficients `[I₄₁(0,0)]_{q⁰} = 1`,
   `[I₄₁(1,−2)]_{q^{1/2}} = −1`, and that nothing else reaches q-degree 0.
   This needs the minimal-degree bound for the tetrahedron index `I_Δ(m,e)`
   (Garoufalidis 1208.1663, held in `library/`).
   *(Done 2026-11-28: [`QOU/Nuclear/TetIndexDegree.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/TetIndexDegree.lean)
   proves both coefficients and that no other term reaches q⁰ in the first row of
   the index matrix, given triality (1208.1663 Prop prop.S3) as a cited input.)*
3. 5₂: GGM eq (WW52) has the same shape with a 3×3 index matrix. Repeating this
   for 5₂ is the cross-knot test (the `{3,4}` chirality split) that the
   anti-numerology rule asks for.
   *(Done 2026-11-28: [`2026-11-28-fivetwo-stokes-from-3d-index.md`](2026-11-28-fivetwo-stokes-from-3d-index.md).)*
4. The internal QOU derivation (Hecke / Markov-trace data → index) is unchanged:
   this result moves the 3 onto the triangulation index, not onto the QOU drivers.

No measured value enters any step, and nothing is fitted.
