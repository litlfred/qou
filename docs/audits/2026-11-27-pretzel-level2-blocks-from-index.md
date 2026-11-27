# The (−2,3,7) pretzel's holomorphic blocks, derived from its 1-dim index and certified at every flux (2026-11-27)

**Beans** `qou-x3iv` (Part 18), `qou-m3ad`, `qou-gz37`. **Producer**
[`computations/probes/aomega_m3_pretzel_index_factorisation_blocks_probe.py`](../../computations/probes/aomega_m3_pretzel_index_factorisation_blocks_probe.py).
**Lean** `QOU/Nuclear/PretzelLevelTwoBlockFactorization.lean` (exponent and sign bookkeeping, 0 sorry).
**Prior arcs** [`2026-09-06-two-bridge-layering-from-farey-word.md`](2026-09-06-two-bridge-layering-from-farey-word.md) §3g–3p,
[`2026-09-13-pretzel-level2-stokes-matrix.md`](2026-09-13-pretzel-level2-stokes-matrix.md) (`qou-lzzi`).
**Convention** `e` = meridian, `m` = longitude (GGM (S3Dx); PR #9739 for 4₁, `qou-m3ad` Part 7 for 5₂).

## 0. Result

1. **The 1-dim state integral IS the pretzel's index.** Read as a `U(1)` theory with
   tetrahedron chirals of gauge charge `(1,1,2)` at Chern–Simons level `A = 2`, the
   integral `∫ Φ_b(v+u/2) Φ_b(v−u/2) Φ_b(2v−c_b) e^{−2πiv²} dv` has 3D index

   ```
   I(m,ζ) = Σ_n q^{−n} CT_z [ z^{2n} I_Δ(n+m, zζ) I_Δ(n−m, z/ζ) I_Δ(2n, z²) ]
   ```

   and this equals SnapPy `m016`'s triangulation index on **every** cell
   `m ∈ [−2,2]`, `e ∈ [−6,6]` to `q³`, and Garoufalidis–Zagier's printed total index
   `1 − 8q + 3q² + 50q³ + 58q⁴ + 13q⁵ − 196q⁶ − 456q⁷` (Obs 3.9) to `q⁷`.
2. **Six blocks, in closed form.** Closing the contour factorises the index into
   the GGM eq (19) shape `Σ_α B^α(q^{m/2}ζ; q) B^α(q^{m/2}ζ^{−1}; q^{−1})`, with

   ```
   B_U(x;q)       = Σ_{j≥0} q^{j(j+1)} x^{2j} (q^{1+j}x²; q)_∞ (q^{1+2j}x²; q)_∞ / (q;q)_j        (×2: x and 1/x)
   B_{σ,ε}(x;q)   = Σ_{j≡ε (2)} q^{j(j+2)/4} (σ q^{1+j/2} x; q)_∞ (σ q^{1+j/2}/x; q)_∞ / (q;q)_j   (σ = ±1, ε = 0,1; weight 1/2)
   ```

   plus the theta monomials `ζ^{2m}q^{±m}` on the unit pair. The fusion equals the
   index at **every** flux `m ∈ [−2,2]`, not only at `m = 0`.
3. **The level-2 pairing rule** — what `qou-x3iv` Parts 12b–17 searched for — is
   *same sign, same parity*: on a doubled pole `s = σq^{−j/2}`, `s̃ = σ'q^{i/2}` with
   `ss̃ = qⁿ`, so `σ' = σ` and `i ≡ j (mod 2)`, with the branch `(q^{−1})^{1/2} := q^{−1/2}`.
   Part 12b's eight "branch twists" were the eight ways to break this.

## 1. The dictionary, fixed on 4₁ and 5₂

The state-integral → index rule has three discrete choices. They are **fixed on
4₁ and 5₂, where the integrands are derived** (`qou-x3iv` Parts 11, 12a), and then
applied unchanged to the pretzel.

| choice | 4₁ (`A=1`) | 5₂ (`A=1`) | (−2,3,7) (`A=2`) |
|---|---|---|---|
| gauge CS level `K` | 1 | 1 | **2** (= `A`) |
| weight `(−q^{1/2})^{t n}` | `t = −1` | `t = −1` | **`t = −2`** (= `−A`) |
| fugacity charge per meridian shift | 1 per `u` | 1 per `u` | **1/2 per `u/2`** |
| flux charge per meridian flux | 2 | 2 | **1** |
| longitude framing `c` (`I(m,e) → I(m,e+cm)`) | −2 | 0 | 1 |

5₂ also passes with `(K,t) = (2,−2)`: that is the mirror `I_{2,3}`, consistent with
Part 11's finding that the two GK labels are the two orientations.

The pretzel's flux and fugacity scales are not chosen. They are Part 12a's
half-meridian placement (`±u/2` on the unit chirals, none on the doubled one), and
they produce **integer** `ζ_tri` powers only because the gauge constraint
`E₁ + E₂ + 2E₃ + 2n = 0` forces `E₁ − E₂` even. That is level 2 seen in the
charge lattice.

**The one per-knot integer.** The framing `c` is a `T`-transformation of the
longitude. It comes from the `u`-only Gaussian constants that Part 12a dropped,
and it never touches the `m = 0` row, so the `σ₁σ₁` entry (GGM (S3Dx), exact) is
independent of it. It is recorded, not interpreted.

**The `−c_b` shift needs no separate R-charge.** Under the gated rule the doubled
chiral enters with R-charge shift 0. The `−c_b` is absorbed by the `(−q^{1/2})^{−An}`
weight, which is the same rule 4₁ and 5₂ fixed.

## 2. A corpus engine bug, found and fixed

`borromean_3d_index.IndexTriangulation.admissible_lattice` stopped after three
consecutive empty `ℓ∞` shells **counted from the origin**. For a large peripheral
class the admissible set sits away from the origin, so the first shells are empty
and the sum was cut short. Example: `m004` gave `I(4,1) = 0`, but `I(−4,−1) = q + O(q⁴)`,
which breaks the symmetry `I(b) = I(−b)`.

The fix counts an empty shell only once the shell's minimum degree has stopped
falling. It agrees with a brute stop-after-20 reference on every cell of the
4₁ and 5₂ grids.

**Contamination.** The `m ≠ 0` rows of
`aomega-m3-rotated-index-three-knots.witness.json` (`qou-m3ad` Part 7) are
incomplete. Its `m = 0` rows, its GGM (102) gate and its verdict are unaffected,
because they only use classes near the origin. The witness is regenerated in this change (17/17); for example `m004` `m = 1` at `q¹` is now `ζ⁴ + ζ⁻⁴`, where before it was only `ζ⁻⁴`.

## 3. H_Ad versus H_floor, at block level

The meridian enters the six blocks in two different ways. In the block formulas
of §0 the argument at `m = 0` is `ζ`, the **meridian eigenvalue** `μ` (one half of
the triangulation's meridian charge, §1), and `H_Ad`'s variable is `x_Ad = μ²`.

* **Unit blocks `B_U(μ)`, `B_U(1/μ)`**: they depend on `μ` only through `μ² = x_Ad`,
  and the pair is swapped by `x_Ad ↔ 1/x_Ad`. To first order,
  `B_U = 1 − 2q·x_Ad + O(q²)`.
* **Doubled blocks `B_{σ,ε}`**: they depend on `μ` only through `σ·(μ + μ⁻¹)`.
  That is the **fundamental** character `χ_V`, not the adjoint, and
  `χ_V² = s(x_Ad) + 1` (`fundamental_sq_eq_adjoint_add_one`). To first order,
  `B_{σ,0} = 1 − σq(μ + μ⁻¹) + O(q²)`, and `B_{σ,1}` starts at `q^{3/4}`.

So:

* `σ`-even combinations (`B_{+,ε} ± B_{−,ε}` with the matching parity) lie in `ℤ[s(x)]`.
* `σ`-odd ones carry `χ_V` and do not.
* The `σ`-grading is tied to the `q^{1/2}` grading: an odd `j` gives both a
  half-integer `j/2` inside the products and the `q^{3/4}` offset.

This is the same ring verdict as the operator route (`qou-lzzi` §5: `σ² = s+1`,
integer-`q` sector in `ℤ[s]`, half-integer sector not), now **from explicit blocks**
instead of from `q → 0` characteristic roots. Two independent derivations agree.

**Against `H_floor`.** `H_floor` grades the core by Chern–Simons value and predicts
no meridian structure. Every one of the six blocks carries an explicit meridian
character (`x` for the unit pair, `χ_V` for the doubled four). That is evidence for
a meridian grading. It does **not** exclude `H_floor`, because `H_floor` was never a
statement about blocks. It also does **not** confirm `H_Ad` as stated: the pretzel's
natural grading is by `χ_V`, and the adjoint appears only as `χ_V² − 1`.

## 4. What is still not established

**The integer matrix `S⁺(x;0)`.** GGM's Conjecture 4 fixes `S⁺` only up to
`GL(r, ℤ(x,q))` on each side. For 4₁ and 5₂ the normalisation comes from the four
region matrices `M_R(x;q)` (GGM (186), (94)). For the pretzel these are still
missing. They are now the **only** missing input: the blocks exist, are explicit,
and are certified. Two routes to them:

* the asymptotics of the six certified blocks as `q → e^{2πi·0}` from the four
  regions, matched to the perturbative series `Φ_σ` (GGM §3); this is numerical
  resurgence, so its output would be integers certified numerically, not proved;
* Garoufalidis–Zagier's quadratic relation (§3.5), lifted to `x ≠ 1` with these
  blocks; this is pure `q`-series.

Until then the ring statement of §3 is the H_Ad answer, and the explicit analogue of
GGM's `[[1,4,0],[0,1,0],[−3,−9,1]]` is not claimed.

**Numerical part.** Gate G5 is a high-precision numerical identity at two values of
`q` and two of `ζ`. Its residual scales as `q⁸`, the first omitted order of the
exact `q⁷` series (ratio `≈ 4⁸` between `q = 0.02` and `q = 0.005`). That certifies
the coefficients through `q⁷`. It is not a symbolic proof of the factorisation. The
contour argument (all poles at `|z| ≥ 1`, closing outward) is not formalised.
