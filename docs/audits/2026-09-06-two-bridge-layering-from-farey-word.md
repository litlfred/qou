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

## 3f. Option 2: the pretzel's Stokes data, as far as they are derivable here (2026-09-07)

**Producer:** [`computations/probes/aomega_m3_rotated_index_three_knots_probe.py`](../../computations/probes/aomega_m3_rotated_index_three_knots_probe.py)
(17/17; the corpus GHHR/GHRS 3D-index engine `borromean_3d_index.IndexTriangulation` on SnapPy's
triangulations `m004`, `m015`, `m016`).

**What GGM actually give** (`arxiv-2012.00062v3` §1.4, held): the rotated 3D-index
`Ind^rot_K(m, ζ; q) = Σ_e I_K(m,e)(q) ζ^e` and Conjecture 4, `S⁺(x;q) ≐ (Ind^rot_K(j−i, q^{(j+i)/2}x; q))_{ij}`
**up to left and right multiplication by `GL(r, ℤ(x,q))`**, with `S⁺_{σ₁σ₁}(x;q) = Ind^rot_K(0,x;q)`
exact (their (21); `arxiv-2007.10190v2` (102) prints it for 5₂). So the rotated-index family is the
invariant, derivable content; the printed q→0 integer matrices — the `{3,4}` this arc has been
working with — sit in GGM's holomorphic-block normalisation, which fixes that `GL` freedom.

**Gate.** Total index (`m = 0`, `ζ = 1`), computed two orders beyond the read order: 5₂ gives
`1 − 12q + 3q² + 74q³ + 90q⁴`, GGM (102) exactly; 4₁ gives `1 − 8q − 9q² + 18q³ + 46q⁴`, the DGG
index (recalled, not held). The gate also fixes the convention: `e` multiplies the meridian, `m` the
longitude. (Read at its own top order a `q⁴` run gave `91`, not `90`; the top orders of a truncated
lattice sum are unreliable, hence the margin.)

**Derived: the pretzel family** `Ind^rot_{(−2,3,7)}(m, ζ; q)`, `m ∈ {−2,…,2}`, exact integers to
`q³`; the `m = 0` member, i.e. `S⁺_{σ₁σ₁}(x;q)` exactly:

    1 − q(2ζ + 4 + 2ζ⁻¹) + q²(ζ² + ζ − 1 + ζ⁻¹ + ζ⁻²) + q³(5ζ² + 12ζ + 16 + 12ζ⁻¹ + 5ζ⁻²) + …

**In the adjoint variable** `s = ζ + 1 + ζ⁻¹` (every `m = 0` coefficient is `ζ ↔ ζ⁻¹` symmetric, hence
a polynomial in `s`):

| order | 4₁ | 5₂ | (−2,3,7) |
|---|---|---|---|
| `q¹` | `−(s−1)(s+1)` | `−s(s+1)` | `−2(s+1)` |
| `q²` | `−s²` | `s(s²−2s−2)` | `s² − s − 3` |
| `q³` | `s²(s²−2s−1)` | `s⁴ − 2s − 1` | `5s² + 2s − 1` |

Recorded, not interpreted: the first-order coefficient carries a common factor `(s+1) =
(ζ^{1/2} + ζ^{−1/2})²` on all three knots; at second order 4₁'s is `−s²`, so the factor is not
universal. No half-integer powers of `q` appear in the pretzel's `m = 0` index to `q³` (its level-2
structure is not visible there at this order).

**What this settles and what it does not — CORRECTED 2026-09-07, same day.** The paragraph that
stood here (and the title of PR #7101, and `qou-m3ad` Part 7 as first written) said item 1 is "not
GL-invariant as posed". That overstates it. The Stokes matrix `S⁺(x;q)` is a canonical invariant of
the knot once the Borel rays are ordered by volume; its q→0 entries are well-defined integers and
`s(x)`-polynomials, and "are they built from `s(x)`?" is a well-posed question about them. What is
**not** invariant is the *identification* in GGM's Conjecture 4: the rotated-index matrix determines
`S⁺` only up to `GL(r, ℤ(x,q))` on both sides, and for a unipotent `S⁺` every determinantal (Fitting)
invariant is trivial, so the index family fixes nothing of `S⁺` beyond the exact `σ₁σ₁` entry. So the
correct statement is: **the question is well-posed; the index route cannot answer it.** The route
that does is the holomorphic-block one, `Ind^rot(m,ζ;q) = Σ_α B^α(q^{m/2}ζ;q) B^α(q^{m/2}ζ⁻¹;q⁻¹)`
(GGM (19)), whose blocks come from the state integral of the triangulation — for `m016` a
2-dimensional integral at level 2, which GZ §4.2 declined to evaluate in closed form. The library
holds the method (Garoufalidis–Kashaev, *From state integrals to q-series*, `arxiv-1304.2705v1`;
*Evaluation of state integrals at rational points*, `arxiv-1411.6062v2`), and the corpus holds a
4₁ instance (`qbeta_m1_rotated_index_from_blocks.py`); the pretzel instance is the tranche
`qou-m3ad` Part 8 names. The `s`-polynomial table above is the exact `σ₁σ₁` entry and stands.

## 3g. The sister hypothesis, tested and refuted in its natural configuration (2026-09-08)

**Producer:** [`computations/probes/aomega_m3_sister_i13_block_index_certification_probe.py`](../../computations/probes/aomega_m3_sister_i13_block_index_certification_probe.py)
(bean `qou-x3iv`; owner: "compute the pretzel's state-integral asymptotics in-sandbox").

**The hypothesis (H-I13).** GK `arxiv-1304.2705v1` §1.3: `I_{1,2} = I_{4₁}`, `I_{2,3} = I_{5₂}`. The
pretzel (−2,3,7) is the 5₂ *sister* (same volume, same trace field), so the natural candidate is the
other member `(A,B) = (1,3)` of the same one-dimensional family, i.e. the same two q-series towers
with the roles of `q` and `q̃` exchanged. If true, GGM `arxiv-2012.00062v3` Theorem 28 gives the
pretzel's holomorphic blocks explicitly and item 1 runs.

**The test, entirely from held text.** GGM (315)–(316): `S⁺₁₁(x;q) = Σ_k H_k(x;q)·H_k(x⁻¹;q⁻¹)`
over the three 5₂ blocks `H(x,y,z;q) = Σ_n q^{n(n+1)} zⁿ (q^{1+n}x;q)_∞ (q^{1+n}y;q)_∞ / (q;q)_n`
(pinned by their (270) `lim_{z→0} H = (qx)_∞(qy)_∞`; it is `G_{2,3}` of (325) at `y₃ = 1`), block
arguments from (326) with `x = (1,x,1/x)`, `w = 1`; the `q⁻¹` side by their (106)
`(u;q⁻¹)_∞ = (qu;q)_∞⁻¹`. Gates: the (106) rule reproduces their printed `J₋` from `J₊`
(4₁, (127a/b)); the `(2,3)` bilinear reproduces their printed (316) to q² and the **derived** 5₂
index (§3f) to q³. The `(1,3)` candidate is the same construction with `A = 1`.

**Result.** The `(1,3)` bilinear is **identical** to the `(2,3)` bilinear at every order computed
(to q³, symbolically in `x`): `1 − (x⁻²+3x⁻¹+4+3x+x²)q + (x⁻³+x⁻²−1+x²+x³)q² + (s⁴−2s−1)q³`, i.e.
the 5₂ index, `1 − 12q + 3q² + 74q³` at `x = 1`; the pretzel's derived index is
`1 − (2x+4+2/x)q + …`, `1 − 8q + 3q² + 50q³`. So **H-I13 is refuted in the 5₂ configuration**
`u = (0,u,−u)`, `t = 0`, and the mechanism is structural rather than numerical: the `A ↔ r−A`
exchange (the `q ↔ q̃` swap) is invisible in the `σ₁σ₁` entry — GK Lemma 1.5(a),
`F_{A,B}(q⁻¹,x) = F_{B−A,B}(q,x)`, is exactly the symmetry that makes the two bilinears
coincide. Hence no member of the one-dimensional family *with this `u`-configuration* can
separate the pretzel from 5₂ in `σ₁σ₁`, and the pretzel is not the "`q ↔ q̃` sister" of 5₂
inside the GK family. Scope-(a) with respect to the configuration only: a `(1,3)` or other
one-dimensional integral with a *different* `u`-configuration is not excluded by this test, and the
three-dimensional DG (5.2) integral for `m016` is untouched.

**What this leaves.** The derived pretzel index is now known to be *not* reproducible by the
one-dimensional sister construction, so the honest route to the pretzel's blocks is the
three-dimensional state integral of `m016` (DG `arxiv-1202.6268v2` eq (5.2)) evaluated by
residues, or a one-dimensional reduction derived (not guessed) from its NZ datum. Both are
research computations with the same certificate: the derived index family of §3f.

## 3h. The pretzel's state integral IS one-dimensional — with one dilogarithm at doubled argument (2026-09-13)

**Producer:** [`computations/probes/aomega_m3_pretzel_nz_rank_one_probe.py`](../../computations/probes/aomega_m3_pretzel_nz_rank_one_probe.py)
(8/8; bean `qou-x3iv`, Part 10). Derived, not guessed: DG `arxiv-1202.6268v2` (2.7)–(2.8) give the
Neumann–Zagier matrices `A = G − G'`, `B = G'' − G'` (first `N−1` edges plus the meridian, `Z'`
eliminated), and (5.2) gives the state integral's inter-tetrahedron Gaussian as the symmetric
`B⁻¹A`; SnapPy's `gluing_equations()` docstring fixes the column convention (interleaved `z, z', z''`
per tetrahedron); a quad-type change is a cyclic relabelling per tetrahedron, all `3^N` enumerated.

**The criterion.** If `B⁻¹A = c·v vᵀ` has rank one, a Hubbard–Stratonovich transform on the single
direction `v` reduces the `N`-dimensional integral to one dimension, in which tetrahedron `i` enters
through the Fourier transform of its dilogarithm at `v_i` times the auxiliary variable (DG (C.18),
(C.25): the S-type generator acts by Fourier transform and the transform of the quantum dilogarithm is
again a quantum dilogarithm times a Gaussian). So rank one with `v = (1,…,1)` is the unit-coefficient
family `∫ Π_j Φ_b(t + u_j) e^{−Aπit²…}` of GK / GGM Theorem 28, and `A = 1/c`.

> **Corrected 2026-09-13 (§3i).** `A = 1/c` is wrong as the Gaussian coefficient of the reduced integral: the
> exact reduction gives `A = Σ v_i² − 1/c` (4₁: 1, 5₂: **1**, pretzel: 2), and `1/c` is the coefficient of the
> *orientation-reversed* integral (`A_mirror = Σ v_i² − A = 1/c`). The two agree for 4₁ only because it is
> amphichiral; the 5₂ row's "A = 2 ✓" was read off the printed form, not derived. The gates of the Part 10
> probe test only `v` and `c`, so its 8/8 stands; its docstring and gate labels carried the same wrong clause and
> are corrected in the same commit, as is bean `qou-x3iv` Part 10 and the PR #7152 table.

| knot | rank-one quads | `v` | `c` | printed form |
|---|---|---|---|---|
| 4₁ | 3 of 9 | (1,1) | 1 | GK `I_{1,2}`, A = 1 ✓ |
| 5₂ | 1 of 27 | (1,1,1) | 1/2 | GK `I_{2,3}` / GGM (240), A = 2 ✓ — **corrected in §3i: the reduction gives A = 1 (`I_{1,3}`, the mirror); A = 2 is `A_mirror = 1/c`** |
| (−2,3,7) | 1 of 27 | **(1,1,2)** | 1/4 | — |

The two gates reproduce the printed one-dimensional forms exactly. **The pretzel's state integral is
one-dimensional, but one of its three quantum dilogarithms enters at *doubled* argument**, which is
outside both unit-coefficient families. That is why the `(1,3)` sister candidate of §3g failed (every
unit-coefficient member with the 5₂ configuration gives 5₂'s index), and it is the mechanism behind
GGM's "level 2": the doubled argument halves that factor's pole spacing, so the residue sum runs in
`q^{1/2}`. The (2.9) symplectic identity `ABᵀ = BAᵀ` holds for every quad choice of all three knots
(a check that the convention was read correctly).

**Not yet done.** The exact linear shifts and prefactor of the reduced integral (from `ν`, the
flattening `f`, and the Fourier-transform constants; DG (C.20)–(C.23), (C.25) are held), then the
residue evaluation to `q^{1/2}`-series blocks, then the certificate: GGM (19) against the derived
index of §3f. The `qou-x3iv` plan is re-scoped to this route; the three-dimensional DG (5.2)
integral is no longer needed.

## 3i. The exact one-dimensional reduction, and what it says about 5₂'s orientation (2026-09-13)

**Producer:** [`computations/probes/aomega_m3_pretzel_one_dim_reduction_probe.py`](../../computations/probes/aomega_m3_pretzel_one_dim_reduction_probe.py)
(bean `qou-x3iv`, Part 11). Every step is a held equation except one, which is checked numerically.

**Inputs, all held.** DG `arxiv-1202.6268v2` (5.2) at `u = 0`; its (5.5)–(5.6) definition of `ψ_ℏ`; the
Fourier transform (C.18); the single-tetrahedron transform identity (C.25); the normalisation ambiguity
(5.4). GK `arxiv-1304.2705v1` (1) for `Φ_b`, its functional equation and `I_{A,B}`; GGM `arxiv-2012.00062v3`
(125), (240) at `u = m = μ = 0`.

**D1 — dictionary.** Matching the two product formulas term by term (numerator `(q e^{−Z};q)_∞` against
`(−q^{1/2}e^{2πbx};q)_∞`, denominator `(e^{−LZ};q̃)_∞` against `(−q̃^{1/2}e^{2πb⁻¹x};q̃)_∞`, using
`e^{2πb c_b} = −q^{1/2}` and `Lq⁻¹ = q̃`) gives

$$
\psi_\hbar(Z) = \Phi_b\!\Bigl(c_b - \frac{Z}{2\pi b}\Bigr),\qquad \hbar = 2\pi i b^2,\qquad i\pi + \tfrac{\hbar}{2} = 2\pi b\,c_b .
$$

The recurrent DG shift `iπ + ℏ/2` is `2πb c_b`; that is why every shift below is a multiple of `c_b`.

**D2 — the Fourier transform of one dilogarithm.** (C.25) says the (C.18) transform of
`e^{(Z² − (2πi+ℏ)Z)/2ℏ} ψ_ℏ(Z)` is `C·ψ_ℏ(Z')`. The (C.18) transform applied twice is reflection
(`ℏ` pure imaginary), so inverting,

$$
\widehat{\psi_\hbar}(P) = C^{-1}\, e^{(P^2 + (2\pi i+\hbar)P)/2\hbar}\;\psi_\hbar(-P)
$$

up to a (5.4)-class constant. This is the one step not printed in held text; the probe checks it
numerically (the ratio of the two sides is independent of `P` to `7·10⁻⁹` across three frequencies, and equals the (5.4)-class unit `e^{5πi/6}` at the test point; the residual is tanh-sinh quadrature error at 22 digits).

**D3 — the reduction.** With `B⁻¹A = c·vvᵀ` (§3h) and `w := B⁻¹ν`, the exponent of (5.2) is
`(1/ℏ)[½c(v·Z)² − (iπ+ℏ/2) w·Z] + const`. A Hubbard–Stratonovich transform on `s = v·Z` makes every `Z_i`
appear linearly, `e^{P_i Z_i/ℏ}` with `P_i = c v_i W − (iπ+ℏ/2) w_i`, and (C.18) turns each `Z_i` integral
into `√(2πiℏ)·ψ̂(P_i)`. Substituting D2 and `t = −cW`, then `t = −2πb x`, and completing the square:

$$
Z_{\mathcal T} \;\propto\; \int e^{-\pi i A x^2}\;\prod_{i=1}^{N}\Phi_b\bigl(v_i x + \sigma_i c_b\bigr)\,dx,
\qquad A = \sum_i v_i^2 - \frac1c,\qquad
\sigma_i = 1 - w_i - v_i\,\frac{\Lambda}{A},\quad \Lambda = \sum_i v_i(1-w_i).
$$

The probe verifies `A` and `Λ` by expanding the exponent symbolically (`sympy.Poly`), and records the
constant prefactor (all of it (5.4)-class apart from the `ℏ`-power). Two measured facts make the shifts
this clean for the three knots: `w ∥ v` (`κ = 1, 1, ½`), and `c Σv_i² + κ = 1 + c Σ v_i`, which is exactly
the statement that every unit-coefficient factor is unshifted. **Neither is general**: in the one-cusped
census with 2–4 tetrahedra there are 17 rank-one quads, 10 collinear, and the identity holds for 9 of those
(it fails at m019, `c = −1`). Rank one alone gives one dimension; collinearity is what puts all the shift on
the doubled factor.

| knot | `c` | `v` | `w = B⁻¹ν` | `A` | reduced integral (SnapPy orientation) | `A_mirror = 1/c` |
|---|---|---|---|---|---|---|
| 4₁ | 1 | (1,1) | (1,1) | 1 | `∫ Φ_b(x)² e^{−πix²}` = GK `I_{1,2}` = GGM (125) ✓ | 1 |
| 5₂ | ½ | (1,1,1) | (1,1,1) | **1** | `∫ Φ_b(x)³ e^{−πix²}` = GK `I_{1,3}` | 2 |
| (−2,3,7) | ¼ | (1,1,2) | (½,½,1) | 2 | `∫ Φ_b(x)² Φ_b(2x − c_b) e^{−2πix²}` | 4 |

**The 5₂ gate lands on `I_{1,3}`, not the printed `I_{2,3}` — and that is orientation, measured.**
Numerically (mpmath, GK's contour `ℝ + iε`), `I_{1,3}(b)` and `I_{2,3}(b)` are *different* functions: their
ratio is not a (5.4)-class constant and its modulus varies with `b` (`1.000` at `|b| = 1`, `0.787` at
`|b| = 0.8`). But at `|b| = 1` they satisfy `I_{1,3} = u · conj(Φ_b(0)⁶ I_{2,3})` with `u` a (5.4)-class unit
(`(q̃/q)^{n/24} e^{iπm/4}`, found at both unit-modulus `b` tested). Complex conjugation of a state integral is
the state integral of the orientation-reversed manifold; so DG (5.2) on SnapPy's m015 datum is the 5₂ state
integral with the *opposite* orientation to KLV/AK's, and the printed `A = 2` is recovered as
`A_mirror = Σv² − A = 1/c` (the `x → −x` + functional-equation image, then conjugation). The reduction is
exact; the gate passes as "mirror". The interpretive step (conjugation = orientation reversal) is standard
but the held sources do not print it — GK cite [AK] for `I_{2,3} = I_{5₂}` and that paper is not held.

**This closes §3g's loose end.** The `(1,3)` and `(2,3)` block bilinears coincided because they are the two
orientations of the same knot, and the `σ₁σ₁` index does not see orientation. H-I13 was not a distinct
hypothesis; it was 5₂ again.

**Held precedent, found after the derivation (2026-09-13, corpus-grep for the doubled argument).** Garoufalidis–Kashaev,
*Evaluation of state integrals at rational points*, `arxiv-1411.6062v2` §2.3 eq. (56), prints
`I_{(−2,3,7)}(b) = ∫ Φ_b(x)² Φ_b(2x − c_b) e^{−2πix²} dx` — character for character the form derived here — and attributes
it to *"the second author computed the state-integral invariant … the result of the long computation"*, taken there as
input. So the four-line reduction from the Neumann–Zagier datum (rank one, `w ∥ v`, one Fourier transform per
tetrahedron) reproduces Kashaev's unpublished computation, and fixes the orientation question of the previous paragraph
in GK's favour: my pretzel integral **is** GK's, with no mirror. The same paper (§2.2) assigns `(A,B) = (1,3)` to 5₂ —
the `I_{1,3}` this reduction lands on — while their 2013 paper assigns `I_{2,3}`; the two GK conventions are the two
orientations, exactly as measured above. Their (57b)–(57c) also give the rational-point building blocks
`g_k(x,q) = q^{k(k+1)}x^{2k}/((qx;q)_k²(qx²;q)_{2k})`, `g(x) = x²/((1−x)²(1−x²)²)`, whose equation `g(x) = 1` has **six**
solutions in two cubic fields (discriminants −23 and 49) matching the six nonabelian parabolic representations — so the
pretzel has six blocks, which is what §3k's residue sum has (two unit families plus four parity classes).

**The pretzel, explicit.** In SnapPy's orientation
$$
Z_{m016} \;\propto\; \int \Phi_b(x)^2\,\Phi_b(2x - c_b)\,e^{-2\pi i x^2}\,dx,
$$
and its mirror carries the same three dilogarithms with `e^{−4πix² + 4πic_b x}`. The doubled factor is the
only one shifted, by `−c_b`; its poles sit at `c_b + (ibm + ib⁻¹n)/2`, halving the lattice spacing, and the
Gaussian cross term at those points is `e^{πimn}` instead of `1` — the `q`- and `q̃`-halves of the residue
sum are coupled by the parity of `(m,n)`. That is GGM's "level 2" as a mechanism rather than an observation.
Which of the two orientations is GGM/GZ's pretzel is **not settled here** (open; recorded in the bean).

**Part 12, as now scoped.** Residues at the half-lattice: triple poles where `m, n` are both even (from
`Φ_b(x)²` and the doubled factor together), simple otherwise; the parity coupling should split the sum into a
`2 × 2` block structure in `q^{1/2}`. Then the `σ₁σ₁` block against the derived rotated index of §3f. Both
orientations must be carried until one is matched.

## 3j. The meridian deformation, and one dictionary for all three knots (2026-09-13)

**Producer:** [`computations/probes/aomega_m3_pretzel_u_deformed_reduction_probe.py`](../../computations/probes/aomega_m3_pretzel_u_deformed_reduction_probe.py)
(3/3; bean `qou-x3iv`, Part 12a). DG (C.21)/(C.23) add one term to the exponent at meridian parameter `u`
(`u_vec = (0,…,0,u)`, `m = e^u` the meridian eigenvalue): `−(2/ℏ) Z·B⁻¹u_vec`. Through §3i's reduction it
shifts tetrahedron `i` by `−2β_i ū`, `β = B⁻¹e_N`, `ū = u/2πb`, and the cross terms add a `u`-linear term in
`x`. The `u`-only constants of (C.23) (which need the completion `(C, D)`) are overall factors and are not
derived here.

| knot | `β = B⁻¹e_N` | `u`-deformed reduced integral (SnapPy orientation), `u_G := −2ū` |
|---|---|---|
| 4₁ | (2, 1) | `∫ Φ_b(x + u_G) Φ_b(x) e^{−πix² − 4πi u_G x}` |
| 5₂ | (1, 0, −1) | `∫ Φ_b(x + u_G) Φ_b(x) Φ_b(x − u_G) e^{−πix²}` |
| (−2,3,7) | (½, −½, 0) | `∫ Φ_b(x + u_G/2) Φ_b(x − u_G/2) Φ_b(2x − c_b) e^{−2πix²}` |

**One dictionary serves both gates.** With `u_G = −2ū`, i.e. `x_G = e^{2πb u_G} = m^{−2}`, the 4₁ row is
GGM (125)/(322) *including its `u`-dependence* — shifts `(u, 0)` and the linear term `w = −2u` — and the 5₂
row is (240)/(323): shifts `(0, u, −u)`, no linear term. So GGM's block variable is the inverse square of DG's
meridian eigenvalue (the square is the SL₂ vs PSL₂ holonomy; the inverse is the orientation of §3i).

**The pretzel's deformation sits on the two unit factors at half the meridian variable**, `±u_G/2`
(`x_G^{1/2} = m^{−1}`), and the doubled factor is undeformed. That is a second level-2 signature, now in `x`
rather than `q`: the unit factors' pole families are `c_b ∓ u_G/2 + ibm + ib⁻¹n`, the doubled factor's is
`c_b + (ibm + ib⁻¹n)/2`, and the residue sum will carry `x_G^{1/2}` and `q^{1/2}` together. Whether the
`σ₁σ₁` bilinear closes to integer powers of `ζ = x_G` (as the derived index of §3f has) is exactly what Part
12b must decide.

## 3k. Residues: the 5₂ index certified from the state integral alone; the pretzel's level-2 pairing is the open item (2026-09-13)

**Producer:** [`computations/probes/aomega_m3_pretzel_residue_blocks_probe.py`](../../computations/probes/aomega_m3_pretzel_residue_blocks_probe.py)
(bean `qou-x3iv`, Part 12b). Three failing tests are kept deliberately; they record a scope-(a) negative.

**The residue calculus, derived and validated.** GK `arxiv-1304.2705v1` Lemma 2.1 gives `Φ_b` near a pole
`x_{m,n} = c_b + ibm + ib⁻¹n` as `K_{m,n}·φ_m·φ̃_n/(1 − e^{2πb⁻¹x})`. Applied to the reduced integrals of §3i–§3j,
every pole family contributes

$$
{-}\frac{b}{2\pi}\,\frac{(q;q)_\infty}{(\tilde q;\tilde q)_\infty}\;e^{-A\pi i(u_F-c_b)^2}\;w_F\;
\Bigl(\sum_m S_F(m;q,x)\Bigr)\Bigl(\sum_n S_F(n;\tilde q^{-1},\tilde x)\Bigr),
$$

with **one** summand function `S_F` per family (the `q̃`-side is the same summand at `(q̃⁻¹, x̃)`, made
convergent by GGM (106)), and the *same* constant for every family — the powers of `(q)_∞/(q̃)_∞` from `K`
cancel against the `φ`'s however many dilogarithms there are. `w_F = 1` for a unit factor's poles. For the
pretzel's doubled factor `Φ_b(2x − c_b)` the residue is halved (`w = ½`), its lattice `c_b + (ibm + ib⁻¹n)/2`
splits by the parities `(ε, δ)` of `(m, n)`, the Gaussian cross term is `e^{πimn} = (−1)^{εδ}`, the `q`-side
carries `q^{3ε/4}` with products shifted by `q^{ε/2}` and evaluated at `ξ = (−1)^δ x^{1/2}`, and the `q̃`-side
mirrors this at `(−1)^ε x̃^{1/2}`:

| knot | family | `S_F(m)` |
|---|---|---|
| 5₂ (`I_{1,3}(u)`) | pole of `Φ_b(x + u_k)`, `u_k ∈ (u,0,−u)` | `(−1)^m q^{m(m+1)/2} x_k^{−m} Π_{j≠k}(q^{m+1}x_j/x_k;q)_∞/(q;q)_m` |
| pretzel | `Φ_b(x ± u/2)` | `q^{m(m+1)} x^{∓m} (q^{m+1}x^{∓1};q)_∞ (q^{2m+1}x^{∓1};q)_∞/(q;q)_m` |
| pretzel | `Φ_b(2x − c_b)`, parity `ε` | `(−1)^ε q^{m'(m'+1)+εm'+3ε/4} (q^{m'+1+ε/2}ξ;q)_∞ (q^{m'+1+ε/2}ξ⁻¹;q)_∞/(q;q)_{2m'+ε}` |

Validated numerically against the integrals themselves (mpmath, GK's contour, fractional nome powers taken from
the *defining* logarithm — at `b = e^{iπ/6}` the nome is a negative real and a principal `q^{3/4}` picks the wrong
root): relative error `5.6·10⁻²⁰` for 5₂ and `7.8·10⁻¹⁹` for the pretzel, and every individual pole of every
family checked by a small contour integral. Dropping the `(−1)^{εδ}` coupling moves the pretzel sum by `2·10⁻⁴`;
it is load-bearing. (The pretzel integral converges on `ℝ + iε` only for `ε > Im c_b/2`, because the doubled
factor's `−c_b` shift makes it grow like `e^{2π(b+b⁻¹)x}`.)

**5₂: the index, certified from DG (5.2) alone.** The bare-block fusion `Σ_k S_k(x;q)·S_k(x⁻¹;q⁻¹)` (no θ's, no
Gaussians; the `q⁻¹` evaluation by (106) and `(q;q⁻¹)_n = (−1)^n q^{−n(n+1)/2}(q;q)_n`) equals the derived
`σ₁σ₁` rotated index of §3f **exactly to `q³`** at `ζ = x`:
`1 − (ζ² + 3ζ + 4 + 3/ζ + 1/ζ²) q + (ζ³ + ζ² − 1 + ζ⁻² + ζ⁻³) q² + (ζ⁴ + 4ζ³ + 10ζ² + 14ζ + 16 + …) q³`. This is
GGM (21) for 5₂ reproduced from the Neumann–Zagier datum and residues, not transcribed from their (316) — and it
holds on the *mirror* integral `I_{1,3}`, confirming that the index does not see orientation. That the θ-factors
of the Gaussians cancel in the fusion is derived, not assumed: by GGM (111a)/(112) the family Gaussians are
`θ(X;q)^{−2}θ(X̃;q̃⁻¹)^{−2}·X^{∓1}X̃^{∓1}` relative to family 3, and `θ(X;q)^{−2}θ(X⁻¹;q⁻¹)^{−2} = 1` by (109).

**The pretzel: a scope-(a) negative, with the obstruction exhibited.** The same bare-block fusion, with the
θ-consistent family weights `1, 1, ½(−1)^{εδ}`, does **not** give the derived pretzel index — for any of the
eight level-2 branches of the fusion (`q̃^{1/4} ↦ ω q^{−1/4}`, `ω⁴ = 1`; `x̃^{1/2} ↦ σ x^{−1/2}`), at `ζ ∈ {x, x^{1/2}}`
or their mirrors. Fractional `q`-powers survive (`q^{3/4}, q^{5/4}, …`), and the obstruction is already at order
`q⁰`: the three families contribute

$$
\frac{1}{(1-X^2)^2},\qquad \frac{X^4}{(1-X^2)^2},\qquad -\frac{X}{2(1-X)^2},\qquad X = x^{1/2},
$$

which sum to `(2X² + 3X + 2)/(2(1+X)²)`, and **no constant reweighting** `α, β, γ` of these three pieces equals `1`
(the `X` and `X³` terms of `(1 − X²)²` cannot be produced; checked as a linear system). So the level-2 pairing of
the parity-split blocks is not a reweighting of the naive families: the true holomorphic blocks of a level-2 knot
must pair the `(ε, δ)` pieces differently (plausibly through the two branches `±X` of `x^{1/2}`), and the held
sources do not print that rule — BDP14, which GGM cite for (19), is not in the library.

**What this fixes and what it leaves.** Fixed: the pretzel state integral as an explicit sum of six
`(q^{1/4}, x^{1/2})`-series bilinears, exact and validated. Open: the fusion rule at level 2, hence the
`σ₁σ₁` certification and, downstream, `qou-m3ad` item 1 for the pretzel. The 5₂ certification is the
positive result of this part and is independent of GGM's printed blocks.

## 4. What it does not do

It does not transcribe Guéritaud; the fold is a search result, stated as such, and a reader who
wants the rule as a theorem should read it off the recorded gluings and prove it, or ingest
Guéritaud 2006. It does not compute the 3d-index or Stokes constants of 5₂, and it does not decide which chirality the Rolfsen 5₂ is in the derived frame (no held source). It does not settle
A_ω (`qou-arc1` terminus unchanged; `qou-q3np` open).
