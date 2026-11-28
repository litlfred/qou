# The 5₂ Stokes constants 4 and 3 read from the 3d index (2026-11-28)

**Bean:** `qou-vr3q` (G3 monodromy / Stokes-constant keystone), the cross-knot
test named in [`2026-11-27-aomega-stokes-constant-from-3d-index.md`](2026-11-27-aomega-stokes-constant-from-3d-index.md) §"Still open" 3.
**Probe:** [`computations/probes/qbeta_g3_stokes_from_3d_index_52.py`](../../computations/probes/qbeta_g3_stokes_from_3d_index_52.py),
witness `qbeta-g3-stokes-from-3d-index-52.witness.json` (9/9).
**Lean:** [`QOU/Nuclear/StokesIndexCount52.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/StokesIndexCount52.lean): the 3×3 gauge (`gaugeL_spec`, `gaugeR_spec`), `stokes11_eq_index`, and the q⁰ factorisation with the `4, −3, −9` (`splus_qzero_factorisation`). `lean`-direct exit 0, no `sorry`, axioms `propext`, `Classical.choice`, `Quot.sound` only.

## Result

The 5₂ Stokes matrix `S⁺(x;q)` of Garoufalidis–Gu–Mariño (2012.00062) is assembled
from the 3d index of the SnapPy triangulation m015 alone:

    S⁺ = L · E·N·E⁻¹ · R,   N_{ij} = Ind^rot(j−i, q^{(i+j)/2}x; q),   E = diag((−q^k x²)^k),

with `L = P·K(x⁻¹;q⁻¹)⁻¹·M₀(x⁻¹;q⁻¹)⁻¹` and `R = M₀(x;q)⁻ᵀ·K(x;q)⁻ᵀ·Q` from GGM's
eqs (Sp-52), (Wmatrec), (W52xm). At `q → 0`:

    S⁺(x;0) = [[1, s+1, 0], [0, 1, 0], [−s, −s², 1]],   s = x + x⁻¹ + 1     (GGM eq S0px52)

so at `x = 1` the Stokes constants are `4`, `−3` (and `−9 = −3²`).

## How the normalisation was fixed (not chosen)

GGM give two forms of the block-to-index dictionary (main text eq WW52 and a
footnote for Beem's conventions). With the 4₁ prefactor or the footnote form the
q⁰ matrix came out wrong. Instead of trying further conventions against the
printed target, the probe evaluates GGM's own holomorphic blocks `A₀, B₀, C₀`
(eqs Am, Bm, Cm, H52p, H52n) numerically at 40 digits and compares the block
bilinear with the m015 index. They agree to `2·10⁻⁴⁰` at three `(x,q)` points
once `E` is included. `E` is GGM's main-text form up to a diagonal conjugation,
which is a change of block normalisation, so `S⁺₁₁` is untouched (GGM's remark
after eq WW52). A second numeric check, independent of the index, confirms the
gauge: `L·Bil·R` equals GGM's W-route `P·W₋₁(x⁻¹;q⁻¹)·W₋₁(x;q)ᵀ·Q` to `2·10⁻³⁸`.

## Checks

| check | through |
|---|---|
| B1 block bilinear = E·N·E⁻¹ (numeric, GGM's blocks vs m015 index) | 40 digits |
| B2 L·Bil·R = GGM W-route, det = 1 (numeric, index-free) | 38 digits |
| C1 `S⁺(x;0)` = GGM eq S0px52 | exact |
| C2 `S⁺₁₁ = Ind^rot(0,x;q)` | q⁶ |
| C3 printed `𝒮⁺_{σ₁σ₁}(x;q)` | q² |
| C4 `det S⁺(x;q) = 1` | q⁶ |
| C5 x = 1: equal to the W-route `S⁺(q)` of `qbeta_g3_5two_stokes_sandwich` (GGM 2007.10190), all nine entries | q⁶ |
| C6 no half-integer q-powers survive | q⁶ |
| C7 stable under a larger charge cutoff (`E_MAX` 22 → 26) | q⁶ |

Cutoff note: at `E_MAX = 16` the q⁵ and q⁶ coefficients of `S⁺₂₂`, `S⁺₃₂` were
short by 1 or 2 and det failed at q⁵. C7 at 22 vs 26 is what certifies the table.

## Which index coefficients carry the 4 and the 3

Row 1 of `L` is `(1,0,0)` and the first column of `R` is `(1,0,0)ᵀ`, so only
finitely many index coefficients reach q⁰. For `S⁺₁₂(x;0) = x⁻¹ + 2 + x`:

| flux m | charge e | q-power | I(m,e) | contributes |
|---|---|---|---|---|
| 0 | 0 | q⁰ | 1 | `1 + x` (vacuum, gauge weight) |
| 1 | −1 | q^{1/2} | 1 | `−x⁻¹` |
| 1 | 0 | q¹ | 2 | `+2x⁻¹` |
| 1 | 1 | q^{1/2} | 1 | `+1` |
| 1 | −3 | q^{5/2} | −1 | `−x⁻⁴` |
| 1 | −2 | q² | −2 | `−2x⁻³` |
| 2 | −4 | q⁴ | −1 | `+x⁻⁴` |
| 2 | −3 | q³ | −2 | `+2x⁻³` |

At `x = 1`: `4 = 2 + (−1 + 2 + 1) + (−1 − 2) + (1 + 2)`. The last two groups
cancel between flux 1 and flux 2. `S⁺₃₁(x;0) = −s` is carried the same way by the
vacuum (`−x`), flux −1 at `e = −1, −2` (`−1`, `−x⁻¹`), and cancelling pairs at
`x⁻², x⁻⁴, x⁻⁵` (full list in the witness).

**Honest reading.** For 4₁ the 3 was `2·1 + 1`, no cancellation. For 5₂ the 4
and the 3 are still finite read-offs of the index, but they are signed sums with
cancellations between flux sectors, not a positive count of states. In the
x-graded form, each surviving power of x is carried by one to three coefficients
of absolute value at most 2.

## Still open

1. GGM's conjecture for the 5₂ region matrices (behind eq Sp-52). The W-route
   rests on it too.
2. The block-to-index identity is measured to 40 digits, not proved.
3. ~~The Lean minimal-degree bound for the tetrahedron index.~~ Done for 4₁, see
   the next section. The same bound applies to 5₂, but the 5₂ attribution needs
   the m015 gluing data in Lean, which is not there yet.

## Addendum: the 4₁ inputs are now theorems (Lean)

[`QOU/Nuclear/TetIndexDegree.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/TetIndexDegree.lean)
defines `[t^k] I_Δ(m,e)` (`t = q^{1/2}`) as an honest finite sum: partition counts
for `1/(q)_n`, with the `n`-sum cut where every later summand starts above `t^k`
(`summand_start_gt`). It proves:

- `tet_cone_lead`, `tet_cone_zero`: in the cone `m ≤ 0 ≤ e`, the lowest term is
  `1·t^{-me}` (1208.1663, proof of Lemma lem.degID).
- `tet_degree_bound`: in every cone, `[t^k] I_Δ(m,e) = 0` below
  `deg2 = m₊(m+e)₊ + (−m)₊e₊ + (−e)₊(−e−m)₊ + max{0,m,−e}`, given triality.
- `fourone_N11_support`, `fourone_N12_support`: in the DGG sum
  `I₄₁(m,e) = Σ_{e₂} I_Δ(m−e₂, m+e−e₂)·I_Δ(e−e₂, −e₂)`, the only term reaching
  q⁰ in `N₁₁` is `e = e₂ = 0`, and in `N₁₂` it is `e = −2, e₂ = 0`.
- `fourone_i00 = 1`, `fourone_i1 = −1`, `stokes41_inputs_proved`,
  `stokes41_three_from_tetrahedra`: the 3 is `2·1 − (−1)` in tetrahedron-index
  coefficients.

The one cited input is triality, `I_Δ(m,e) = (−q^{1/2})^{−e} I_Δ(e, −e−m)`
(1208.1663 Prop prop.S3(b)), stated as a hypothesis `Triality` on the concrete
coefficients. It was checked on the exact index for `|m|,|e| ≤ 5`, `k ≤ 24`
(3025 coefficients, 0 failures). Proving it in Lean needs the two q-recursions of
`I_Δ` and the rank-1 uniqueness of their solution space (1208.1663 §4.2–4.4).
`lean`-direct exit 0, no `sorry`, axioms `propext`, `Classical.choice`,
`Quot.sound` only.

### Triality, proved (`QOU/Nuclear/TetIndexTriality.lean`)

The cited input above is now a theorem, `triality_holds : Triality`, so every
4₁ statement holds with no hypothesis (`tet_degree_bound_proved`,
`fourone_N11_support_proved`, `fourone_N12_support_proved`,
`stokes41_inputs_unconditional`, `stokes41_three_unconditional`). The route is
elementary and stays coefficientwise in `ℤ[[q]]`:

- Write `I_Δ(m,e) = q^{−em/2} F(m,e)`, `F(m,e) = Σ_n (−1)ⁿ q^{n(n+1)/2 − nm}/((q)_n (q)_{n+e})`,
  and let `Fc m e j = [q^j] F(m,e)`, with `1/(q)_n` the Mathlib power-series inverse.
- `Fc_rec2`: `F(m,e) = q^e F(m−1,e) + F(m,e−1)` (1208.1663 eq rec2), term by term.
- `Fc_rec1`: `F(m,e) = F(m+1,e) + q^{−m} F(m,e+1)` (eq rec1), by telescoping with
  certificate `G(n) = (−1)^{n+1} q^{n(n+1)/2 − nm − n}/((q)_{n−1}(q)_{n+e})`.
- `unique_of_rec`: a solution of both recursions that vanishes at `(0,0)` and
  `(0,1)` vanishes everywhere. The `m = 0` column obeys
  `h(0,e+1) = 2h(0,e) − q^e h(0,e) − h(0,e−1)` in both directions, and the other
  columns follow from the recursions.
- `S_R1`, `S_R2`: the transform `(SF)(m,e) = (−1)^e q^{e(e−1)/2 + em} F(e,−e−m)`
  maps solutions to solutions.
- `Fc_one_neg`: every solution has `F(1,−1) = −F(0,1)`, so `SF` and `F` agree at
  `(0,0)` and `(0,1)`; hence `Fc_triality`: `SF = F`.
- `pc_eq`, `conv_eq`, `tetCoeff_eq`: the partition-count coefficients of
  `TetIndexDegree` are the power-series coefficients, and
  `tetCoeff m e k = [k + em even]·Fc m e ((k+em)/2)`. Parity and the shift
  `σ(m,e)` match, giving `triality_holds`.

`lean`-direct exit 0, no `sorry`; `#print axioms triality_holds` and
`stokes41_three_unconditional`: `propext`, `Classical.choice`, `Quot.sound` only.

No measured value enters any step, and nothing is fitted.

## Addendum: the 4 and the 3 computed in Lean from tetrahedron indices

[`QOU/Nuclear/FiveTwoStokesIndex.lean`](../../folio/quantum-observable-universe/lean/QOU/Nuclear/FiveTwoStokesIndex.lean)
(with `FiveTwoIndexBase.lean` and `FiveTwoDegree0/1/2.lean`) computes
`[q⁰] S⁺₁₂(1;q) = 4` (`stokes52_12_from_index`) and `[q⁰] S⁺₃₁(1;q) = −3`
(`stokes52_31_from_index`) from tetrahedron-index coefficients by exact finite
arithmetic, and checks them against GGM's q⁰ matrix (`stokes52_matches_S0px52`).

- **The m015 index as a tetrahedron sum.** Substituting the two GHRS edge weights
  `(2a, 2b+m)` in SnapPy's m015 gluing rows makes every half-integral triple
  integral:
  `I(m,e) = Σ_{a,b} (−1)^{b+m} t^{−b} I_Δ(b−m, e−a) I_Δ(b, 2a−e−b) I_Δ(b+m, −a)`,
  `t = q^{1/2}`. The probe's engine agrees for `|m| ≤ 2`, `|e| ≤ 4` through `t⁸`
  (45 charge pairs, 0 mismatches).
- **Finiteness.** The `(a,b)` summand starts at t-degree
  `fdeg = −b + Σ deg2` (tetrahedron degree, proved with triality in
  `TetIndexTriality`). `fdeg_quad0/1/2`: `12·fdeg ≥ a² + b² + e²` at flux 0 and 1
  and `≥ a² + b² + e² − 36` at flux 2, each from the 27 cone cases by `nlinarith`.
  A flux reflection, `fdeg(−m,e,a,b) = fdeg(m,−e,a−e,b)`, covers flux −1 and −2.
  So `idx m e p` (`[t^p] I(m,e)`) and `rot m s n` (`[t^n] Ind^rot(m, t^s)` at `x = 1`)
  are honest finite sums (`idx_eq`, `rot_eq`, `rot_eq_idx`, `rot_low`).
- **Which summands reach q⁰.** For each of the five rotated indices that enter,
  the summands that can reach the needed degree are confined to a box and then
  listed by `decide`: 1, 7, 4, 6 and 3 points `(e,a,b)`.
- **Gauge at x = 1.** The six entries of `gaugeR`/`gaugeL` that enter are
  `num/den` in `q` (`R12_at1` … `L33_at1`, over any field). `serC` is the
  q-expansion, characterised by `serC_rec` (its Cauchy product with `den` is `num`).

Still named inputs, unchanged: GGM's region-matrix conjecture behind eq Sp-52,
and the block-to-index identity (measured to 40 digits). `lean`-direct exit 0,
no `sorry`; axioms `propext`, `Classical.choice`, `Quot.sound` only.
