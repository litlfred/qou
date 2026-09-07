# Two-bridge knot complements from the Farey word — NZ data for 4₁ and 5₂ (2026-09-06)

**Bean:** `qou-yvyd` (follow-on to `qou-n2cl`; the A_ω cross-knot gate now has derived data on both sides).
**Producer:** [`computations/probes/two_bridge_layered_nz_probe.py`](../../computations/probes/two_bridge_layered_nz_probe.py)
(14/14 assertions, `q0Anchor: independent`, no `q`, no Markov parameter).
**Lean:** `QOU/Mass/FiveTwoGluingFromFareyWord.lean` (sorry-free; the four 5₂ rows at the cubic shape).
**Owner request:** *"Work qou-yvyd foreground."*

## 1. Construction

The complement of a two-bridge link `K(Ω)` contains a product region `S × I`, `S` the 4-punctured
sphere, layered by the Farey word `Ω` (Futer–Kalfagianni–Purcell §2.4, held as
`library/arxiv-0808.2716v4`). Modelled here as `S = T₄/ι` with `T₄` the torus minus its four
half-integer points and `ι = −1`: for a Farey pair `(a, b)` the lines of slopes `a, b` through the
punctures cut `T₄` into four parallelograms that `ι` pairs into the pillowcase's front and back
squares, each with all four punctures as vertices. A diagonal exchange is one flip tetrahedron per
square, so **two tetrahedra per letter**; consecutive layers glue by ι-canonical face keys; a
tetrahedron vertex's cusp identity is its puncture (which ι fixes).

**The fold is found, not transcribed.** Guéritaud's fold rule is not held. Each end surface must
be "folded onto itself, identifying its four ideal triangles in pairs" (FKP); the probe enumerates
every pairing of the four end faces with every orientation-reversing simplicial identification
(27 per end, 729 in all) and keeps candidates that are (i) manifolds with torus cusps, (ii)
one-cusped, (iii) `H₁ = ℤ` (Smith normal form on the dual spine), (iv) geometric — a complete
structure with all `Im z > 0`, every dual cycle developing with derivative 1 and every edge's
corner arguments summing to 2π. The survivors are then compared to a reference volume that the
search never sees.

**Word length is c − 3.** The first run used two letters for 4₁ and found eleven distinct
one-cusped geometric manifolds with four tetrahedra (volumes 2.7818, 2.9441, 3.2529, 3.3621,
3.4030, 3.6087, 3.6639, 3.7506, 3.7588, 3.8217) but not 4₁; the single-letter word gave 4₁ at
once. So the two clasps and one further crossing are absorbed by the folds: 4₁ (c = 4) ← `R`,
5₂ (c = 5) ← `RL`.

## 2. Results

| knot | word | tetrahedra | shapes | volume vs reference | cusp modulus | H₁ |
|---|---|---|---|---|---|---|
| 4₁ = S(5,2) | `R` | 2 | `e^{iπ/3}, e^{iπ/3}` | `2·Cl₂(π/3)`, equal to 1e-40 | `2√3 i` — same as the bundle route (#6935) | ℤ |
| 5₂ = S(7,3) | `RL` | 4 | `θ, θ, θ²−1, θ²−1`, `θ³ − θ + 1 = 0` | corpus `2.8281220883307831627…`, equal to 5e-50 | `0.49024… + 2.97945… i` | ℤ |

**Rows (rect form `Π z^a(1−z)^b = ±1`).**
4₁: `(1,−2 | −2,1)` and its inverse — a different labelling of the same two-tetrahedron
triangulation as the bundle route's `(1,1 | 1,1)`; both are solved by `ω`.
5₂: `(1,1,−1,−1 | 1,1,1,1 ; +)`, `(0,0,−1,−1 | −2,−2,−1,−1 ; +)`, `(−1,0,1,1 | 1,0,0,0 ; −)`,
`(0,−1,1,1 | 0,1,0,0 ; −)`; edge rows isotropic under the NZ form.

**Shape field of 5₂.** The integer relation found by PSLQ on the real projection and verified on
the complex number is `θ³ − θ + 1 = 0`, discriminant `−23`: the cubic trace field of 5₂, not an
input. The other two shapes are `θ² − 1`. Every row reduces to **exactly zero** modulo the cubic
in `ℚ[θ]`, and the same identities are theorems over any commutative ring
(`FiveTwoGluingFromFareyWord.all_rows`, e.g. row 3 cleared: `−(1−θ)(θ²−1)² = θ`).

**The fold, as found.** Every fold pair identifies a **front-square face with a back-square
face** (never two faces of one tetrahedron) by an orientation-reversing map; for 5₂ all four
pairs fix two punctures pointwise (a reflection across an arc); for 4₁ two of four do. Search
statistics for `RL`: 718 candidates, 202 with torus cusps, 132 with `H₁ = ℤ`, 23 geometric; the
23rd matched Vol(5₂). The competing geometric folds are other knot complements (by volume,
several census manifolds), so the reference volume — never an input — is what selects.

## 3. Cusp rows, the meridian, and the A-polynomial (added 2026-09-07)

**Producer:** [`computations/probes/two_bridge_cusp_rows_apoly_probe.py`](../../computations/probes/two_bridge_cusp_rows_apoly_probe.py);
**Lean:** `QOU/Mass/FiveTwoAPolynomialFromFareyWord.lean` (sorry-free, standard axioms).

**λ is homological; μ is not.** The longitude is the primitive cusp class dying in `H₁(M) = ℤ`,
read off a functional on the dual spine of the triangulation. The meridian is *not* determined by
homology: every `μ₀ + kλ` kills the same class, and the Bézout complement measured against the
known `A₄₁` on the 4₁ control came out as `μ + λ`. The loop around a puncture in a layer surface is
not available either — in these triangulations the front and back squares of a layer do not share
their side edges (on 4₁ the side `(0,0)–(0,½)` of the front square is edge class 1, the back
square's is class 2; the folds, found by search, identify the sides otherwise).

**The meridian is pinned by the Dehn-filling test.** A nondegenerate solution of the gluing
equations is a representation `ρ : π₁(M) → PSL₂(ℂ)`. If `H(μ₀+kλ) = 1` while `H(λ) ≠ 1`, the cusp
subgroup's image is abelian with a loxodromic element, so `μ₀+kλ`, of eigenvalue `±1`, is the
identity: `ρ` factors through the filling `M(μ₀+kλ)`, whose `π₁` is therefore nontrivial. The
meridian filling is `S³`, so the meridian is the unique frame with no such point (Property P,
`kronheimer2004`, supplies existence and uniqueness of that frame; the certificates for every other
frame are explicit solutions). The absence at `k*` is then checked exactly on the fitted polynomial:
`A(L, ±1)` must vanish only at `L = ±1`.

**Finding the certificates took four attempts, each failure measured.** Random Newton starts on
four shapes (0–4 hits per frame, seven surviving frames on 5₂); seeds near the complete structure
(every frame fell onto it); a deflated secant target (the iteration converged to the deflator's own
zero — at `ℓ = ∞` for `1/(ℓ−1)²`, linearly at `ℓ = −3.7` for `((ℓ+3.7)/(ℓ−1))²` — while the genuine
`k = 0` points of 4₁, the roots of `A₄₁(L,1/L)·L⁷ = (L+1)²(L⁶−2L⁵+2L⁴−3L³+2L²−2L+1)`, sit at
`ℓ = 0.374, 2.675` and four points on the unit circle); and a continuation grid over the curve on
the sheet of the complete structure, which certified every frame *except* `k*−1, k*, k*+1` (the
count grows with `|k − k*|`: 2, 2, 4, 4, 6, 6, 8, 8). What works: seed further sheets of the
`ℓ = H(λ)` projection at `ℓ = 1` (the conjugate structure, random-start solutions of
`{edge rows, H(λ) = 1}`) and multiply them by monodromy loops once around `|ℓ| = r`; grid every
sheet; run an undeflated complex secant in `s = log ℓ` along the curve from the grid points where
`|H(μ₀)H(λ)^k − 1|` is smallest. Continuing a *found* point back to `ℓ = 1` never leaves its own
sheet, so that route is circular.

| knot | sheets / grid points | frames certified (loxodromic points) | `k*` | cusp shape `t_λ/t_μ` |
|---|---|---|---|---|
| 4₁ | 8 / 4928 | all `k ≠ −1` in `[−8, 8]`: 4, 4 at `k = −2, 0`, then 9–10 | `−1` (unique) | `2√3 i` |
| 5₂ | 12 / 7026 | all `k ≠ 0` in `[−8, 8]`: 7, 8 at `k = ∓1`, then 10 | `0` (unique) | `2.49024… + 2.97945… i` (recorded modulus mod 1) |

**A-polynomials.** Fitted directly in `(L, M²)` from the continuation grid on the sheet of the
complete structure (rows scaled to unit max entry; a one-dimensional nullspace by a gap criterion;
integer rounding verified on fresh samples), with the lift-free product `P(L², M²) = c·A(L,M)A(−L,M)`
kept as a fallback — measured, the product box (3,14) is conditioned to ~1e-31 against ~1e-16
for the direct box (3,7) on the same samples. Every 4₁ fit failure in the search history traced to
one inverted exponent in the frame transform (`M² = M₀²·L^{2k*}`, not `/`), invisible on 5₂
because its `k* = 0`:

- 4₁: `−A₄₁(L,M)` exactly, `A(L,±1) = (L+1)²`, fresh-sample residual `1.6e-49`, slopes `{−4, 4}` —
  the control against #6935's elimination route.
- 5₂: `A = L³ + L²(M¹⁰ − M⁸ + 2M⁴ + 2M² − 1) + L(−M¹⁴ + 2M¹² + 2M¹⁰ − M⁶ + M⁴) + M¹⁴`, fresh-sample
  residual `2.3e-43`, `A(L,±1) = (L+1)³` exactly (Lean: `A_at_M_one`, `A_at_M_neg_one`); the
  involution `L³M¹⁴·A(L⁻¹,M⁻¹) = A(L,M)` holds (Lean: `A_involution`). Newton hull
  `(0,14),(1,4),(2,0),(3,0),(2,10),(1,14)`; **boundary slopes `{−10, −4, 0}`**.

**Chirality.** The frame is `λ` oriented so `Im(t_λ/t_μ) > 0` for the `Im z > 0` solution. The
slopes `{−10, −4, 0}` are the literature set `{0, 4, 10}` for the mirror; under `L ↦ 1/L` the
polynomial is the standard `A_{5₂}` as usually printed. So the derived triangulation is the
chirality whose slopes are negative in this frame — the same sign as the corpus's recalled
`{0, −4, −10}` (`qbeta_g3_aomega_route_a_newton_polygon.py`, the 2026-08-11 memo). Which of the
two the Rolfsen `5₂` is, in this frame, is a convention question a held source would settle; the
library holds none, and the corpus's recall carries the same unverified sign. What is settled is
that `S⁺`/`S⁻` claims can now be tied to a definite triangulation with a definite `(μ, λ)` and a
definite `A`, with the mirror obtained by conjugating the shapes.

**What this buys for the A_ω arc.** Both sides of the cross-knot gate have derived NZ data *and*
derived cusp rows: 4₁ twice (bundle and two-bridge routes agreeing on volume, cusp modulus and
`A₄₁`) and 5₂ once, with its A-polynomial reproduced from the word alone. The chirality split
`{3, 4}` at 5₂ can be tested on this data with the orientation fixed by the frame above.

## 3b. The A_ω Route-A gate re-run on the derived 5₂ data (2026-09-07)

**Producer:** [`computations/probes/qbeta_g3_aomega_route_a_newton_polygon.py`](../../computations/probes/qbeta_g3_aomega_route_a_newton_polygon.py)
(7/8, the FAIL is the intended falsification); **Lean:** `QOU/QBeta/RouteANewtonPolygonDT.lean`
(core-only, `decide`; the new `a52_*` and `*_mirror` theorems, no axioms beyond `propext` /
`Quot.sound` on the two `simp`-closed ones).

Route A (`docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md`) asked whether the
DT spectrum `{3, 4}` is Newton-polygon data of the A-polynomial. Its 5₂ half ran on
literature-recalled inputs — slopes `{0, −4, −10}`, four boundary-parabolic connections — and bean
`qou-52sn` asked for them to be hardened with SnapPy. **They are now derived here instead**, from
§3's `A_{5₂}`: the probe reads `two-bridge-cusp-rows-apoly.witness.json`, recomputes the Newton
polygon with the same lattice geometry it uses for 4₁, and asserts

| quantity | derived | recalled |
|---|---|---|
| boundary slopes (derived frame) | `{−10, −4, 0}` | `{0, −4, −10}` |
| geometric `L`-degree / full (`× (L−1)`) | `3` / `4` | — / `4` |
| `|max slope|` (R2 input) | `10 ∉ {3,4}` | same |

So the verdict is unchanged and no longer conditional: **R2 (DT integer = boundary slope) is
refuted on 5₂, R1 (DT integer = connection count) survives both knots** — now as strong as #6985's
derivation, not as strong as a recalled table. In Lean the two `5₂` `def`s that carried the literal
values are theorems about `a52Monomials` (`fiveTwoMaxAbsSlope_derived`, `fiveTwoConnections_eq_four`),
and the hull's central symmetry `(m,l) ↦ (14−m, 3−l)` — the exponent shadow of `A_involution` — is
the transcription check.

**What the pinned frame adds to Route A: nothing, and that is a theorem.** The one thing §3 supplies
beyond the recalled table is the *sign* of the slopes, i.e. the chirality of the triangulated
manifold. The mirror acts on exponents by `(m, l) ↦ (−m, l)`: every slope changes sign
(`slopeEq_mirror`), the absolute slope is invariant (`absSlopeEq_mirror`), and the `L`-profile is
untouched (`lProfile_mirror`). Both Route-A inputs are therefore mirror-invariant, and the mirrored
`5₂` edges carry exactly the literature's `{0, 4, 10}` (`a52_mirror_edge_slopes_in_0_4_10`). The 5₂
DT datum is the *ordered* pair `(4 ∈ S⁺, 3 ∈ S⁻)` with nonzero bar-odd part
(`FiveTwoDTSpectrumSplit.chirality_odd_datum_ne_zero`); a quantity that cannot tell 5₂ from its
mirror cannot carry it. This sharpens `symmetric_scalar_blind_to_chirality` (no *symmetric scalar*
serves the split) to: no Newton-polygon slope-magnitude or degree datum serves it — the split is
not Route-A data in any frame. The attack-options memo's falsifier for Route A ("check the slopes
match its `{3,4}` chirality split") is thereby answered in the negative on structural grounds, not
merely by the `10 ∉ {3,4}` miss.

**Still open, unchanged.** Which chirality GGM's `S⁺`/`S⁻` (the `(96)`/`(97)` factorisations) belong
to, in the derived `(μ, λ)` frame, is the same convention question as which 5₂ is Rolfsen's; no held
source settles it, and nothing here needs it. `qou-q3np` and the Route-C programme are untouched.

## 3c. Route C, M3: `H_floor`'s remainder from the derived shape fields (2026-09-07)

**Producer:** [`computations/probes/aomega_m3_floor_remainder_from_derived_shape_fields_probe.py`](../../computations/probes/aomega_m3_floor_remainder_from_derived_shape_fields_probe.py)
(13/13); **Lean:** `QOU/QBeta/FloorRemainderFromDerivedShapeFields.lean` (sorry-free; the
real-root theorems over `ℝ`).

Bean `qou-m3ad` Part 4 found that the rival hypothesis `H_floor` — knot-independent core
`{trivial, geometric, conjugate}`, knot-dependent remainder = number of real embeddings of the
trace field — reproduces Garoufalidis–Zagier's `|P_K| = 3, 4, 7` and derives the "+1" of 5₂ from
arithmetic. Its inputs were a transcribed table (`AdjointIndexSetM3.realEmbeddings`). On the two
knots this corpus derives, they no longer need to be: §2's shape fields are `x² − x + 1` for 4₁
(no real root, `fourOneShapePoly_ne_zero`) and `θ³ − θ + 1` for 5₂ (exactly one real root,
`fiveTwoShapeCubic_existsUnique_root`: IVT on `(−2, −1)` for existence; every root lies below
`−1`, where the cubic is strictly increasing, for uniqueness). So the signatures `(0,1)`, `(1,1)`,
the sizes `|P_K| = 3, 4` and the remainders `0, 1` follow, and Part 1's forced unit remainder has
a derived source (`floor_remainders_from_derived_fields`).

The probe adds the piece `H_floor` grades by: every tetrahedron shape pushed through every
embedding of the field and summed under the Bloch–Wigner dilogarithm gives the Chern–Simons value
set of the Galois-conjugate structures — `{+V, −V}` for 4₁ (`V = 2·Cl₂(π/3)`, to 1e-40) and
`{0, +V, −V}` for 5₂ (`V = 2.82812208833…`, the corpus value to 1e-18; the real embedding
`θ ≈ −1.3247` has real shapes and volume exactly `0`).

**What this does not do.** It does not separate `H_Ad` from `H_floor` — the core is `3` under both
(`core_is_three_on_all_three`) and Part 3's meridian grading remains `H_Ad`'s only distinct
content. It does not reach `(−2,3,7)`: that field is not derived here, so the prediction `7` stays
a prediction. Nothing about `A_ω` is derived; the Hecke-side origin of the extra 5₂ ray
(`qou-rtec` M3) is untouched.

## 3d. The chirality convention, settled against SnapPy's Rolfsen table (2026-09-07, bean `qou-lrvc`)

**Producer:** [`computations/probes/fivetwo_chirality_frame_vs_snappy_probe.py`](../../computations/probes/fivetwo_chirality_frame_vs_snappy_probe.py)
(8/8; SnapPy 3.3.2 from PyPI, route 2 of `sandbox-egress.md`, and Culler's census tarball
`library/A_census.tgz`, already held).

§3 left open which chirality the Rolfsen 5₂ is in the derived frame. Two held sources answer it,
and they agree to every digit compared:

| source | its 5₂ | relation to the derived frame |
|---|---|---|
| Culler's census `A_{K3_2}` (SnapPy framing) | `1 + L(M¹⁰−M⁸+2M⁴+2M²−1) + L²(−M¹⁴+2M¹²+2M¹⁰−M⁶+M⁴) + L³M¹⁴` | **exactly** `L³·A(1/L, M)` — the mirror; the 4₁ control `K2_1` is identical to the derived `A₄₁` |
| SnapPy `Manifold('5_2')` (= `m015` = `K3_2` = `K5a1`) | cusp shape `−2.49024466750661447990098220728294261621078676… + 2.97944706647897694637268171441756946896065234… i`, slopes `{0, 4, 10}` | `−conj(τ_derived)` to 38 digits; slopes negated. `reverse_orientation()` reproduces the derived shape and `{−10, −4, 0}` exactly |

So **the derived Farey-word triangulation `RL` of `K(7,3)` is the mirror of the Rolfsen-table 5₂
as SnapPy digitises it**, and its A-polynomial is the mirror's. "Rolfsen's 5₂" here means the
digitised table (SnapPy's `LinkExteriors`, triangulations by Joe Christy); the book itself is not
held, and the identification of SnapPy's table with the book's diagrams is SnapPy's claim, recorded
as such. The mirror is obtained by conjugating the shapes, as §3 said.

**Two more held sources, same answer (owner uploads of 2026-09-07).** Dunfield's revised
Hatcher–Oertel table (`library/arxiv-math-9901120v3` §2, *notation follows [HO] and [Rol]*) gives
`5₂ = K(3/7) : 0, 4, 10` — the negatives of the derived slopes, from a source independent of SnapPy
and in Rolfsen's own notation (probe assertion 9/9). And Garoufalidis–Zagier state their convention
outright (`arxiv-2111.06645v3` §10, *Orientation conventions*): *"We will be using the consistent
orientation convention for `M_K` of the SnapPy program"*, with the trace field and complex volume
taken from SnapPy — so every `5₂` quantity in GZ (the `Φ^{(5₂,σ)}` series, the Habiro-like functions,
Appendix A's numerics) refers to SnapPy's `5_2`, i.e. the **mirror** of the derived triangulation.
SnapPy's complex volume of `5_2` is `2.82812… − 3.02413… i` and of its mirror `+3.02413… i`; that
sign is the invariant a source has to print to be pinned.

**What remains open on the bean.** Which of GGM's `S⁺`/`S⁻` (the `(96)`/`(97)` factorisations,
`FiveTwoDTSpectrumSplit`) attaches to which chirality. GGM build on GZ and cite their conventions,
but none of the four held GGM papers (`arxiv-2007.10190v2`, `arxiv-2012.00062v3`,
`arxiv-2111.04763v2`, `arxiv-2208.14188v2`) states an orientation or prints a signed complex volume
or an A-polynomial for `5₂` in its sectioned text; inheritance by citation is not a held statement.
What would close it: a signed `v(5₂)` or an `A_{5₂}(x, y)` in a GGM text, matched against SnapPy's
`5_2` (`−3.02413… i`; Culler's `A_{K3_2}`) — one line, if a source carries it.

## 3e. Route C, M3: the third knot's `H_floor` inputs, from the solved Ptolemy varieties (2026-09-07)

**Producer:** [`computations/probes/aomega_m3_pretzel_remainder_from_ptolemy_probe.py`](../../computations/probes/aomega_m3_pretzel_remainder_from_ptolemy_probe.py)
(10/10); **Lean:** `QOU/QBeta/PretzelRemainderFromPtolemy.lean` (sorry-free).

`qou-m3ad` Part 4 had the `(−2,3,7)` row of Garoufalidis–Zagier's table as a transcription and called
the count `7` *a prediction, not a check*, the Ptolemy database being firewalled. The variety is small
enough to solve here. SnapPy's census `m016` (= `K12n242` = `(−2,3,7)` = Culler's `K3_1`; 3
tetrahedra; the volume `2.82812…` it shares with `5₂`) has two `N = 2` obstruction classes, each with
three Ptolemy coordinates and four equations; a lex Gröbner basis (sympy, exact) reduces each to one
cubic:

| class | cubic | disc | real roots | field |
|---|---|---|---|---|
| 1 | `c³ − c − 1` | `−23` | 1 | `ℚ(ξ)` — the `5₂` shape cubic in `−c` |
| 0 | `c³ + 4c² + 3c − 1` | `49` | 3 | splits over `ℚ(η)`, `η³ + η² − 2η − 1 = 0` (checked by factoring over that field) |

Boundary-unipotent representations are the nontrivial elements of `P_K`, one per solution, so
`|P_K| = 1 + 3 + 3 = 7`, real embeddings `1 + 3 = 4`, one complex pair, `H_floor` remainder `4` —
GZ §2.1 reproduced from a held triangulation and exact algebra, and `R1`'s count `7` matched by
Culler's `A_{K3_1}` (geometric `L`-degree `6`, irreducible over `ℚ`: one curve carries both fields).
The real-root counts are theorems (`geoCubic_existsUnique_root` inherits the `5₂` proof;
`realCubic_three_real_roots` by IVT on `(−3,−2)`, `(−2,−1)`, `(−1,1)`), linked to the transcribed
`realEmbeddings pretzel237 = 4`.

**Honest scoring.** This is the third knot's *provenance*, not a discriminator: the core is `3` under
both `H_Ad` and `H_floor`, and the pretzel's `q → 0` Stokes matrix — the one datum that could test
`H_Ad`'s polynomial one-sidedly — is in no held source (GGM 2012.00062 §1.5 record that the pretzel
has *level 2*, entries in `q^{1/2}`, so even that test would need the level-2 form of the claim). The
triangulation is SnapPy's, not a Farey-word derivation: the pretzel is not two-bridge.

**On the plan that prompted this** (a suggested attack, taken critically): GZ do *not* print the
pretzel's Habiro-like matrix — §4.2 says explicitly that for `(−2,3,7)` they *"cannot give even
conjectural explicit formulas"*; what they print is the seven-term modularity relation (4.3) with the
periodic functions `Q_j` at roots of unity and Appendix A's series coefficients, which are not a
`q → 0` Stokes matrix. The pretzel has six non-abelian boundary-parabolic representations, not
five (`rank 6`, `|P_K| = 7`). Retrieving Ptolemy solutions from the database is blocked, but solving
the variety is not, as above. And `H_Ad` versus `H_floor` is not decided by any count — they agree on
every count — only by whether the Stokes entries are built from `s(x) = x + 1 + x⁻¹`.

## 4. What it does not do

It does not transcribe Guéritaud; the fold is a search result, stated as such, and a reader who
wants the rule as a theorem should read it off the recorded gluings and prove it, or ingest
Guéritaud 2006. It does not compute the 3d-index or Stokes constants of 5₂, and it does not decide which chirality the Rolfsen 5₂ is in the derived frame (no held source). It does not settle
A_ω (`qou-arc1` terminus unchanged; `qou-q3np` open).
