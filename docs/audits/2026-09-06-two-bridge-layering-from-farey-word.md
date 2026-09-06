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

## 3. What this buys for the A_ω arc

Both sides of the cross-knot gate now have Neumann–Zagier data derived from a word with no SnapPy
input: 4₁ twice (bundle route and two-bridge route, agreeing on volume and cusp modulus) and 5₂
once. The chirality split `{3, 4}` at 5₂ can now be tested on derived data — with one caveat that
this audit does not resolve: **orientation.** 5₂ is chiral; the pillowcase inherits (fibre
orientation) ∧ dt and the mirror has conjugate shapes and the same volume, so which of `S⁺`/`S⁻`
the derived triangulation corresponds to must be pinned (e.g. by the sign of the Chern–Simons
invariant or by matching the derived meridian/longitude rows to a chirality-sensitive invariant)
before any `S⁺`/`S⁻` claim rests on it. The cusp rows (μ, λ) for 5₂ are computed by the same
developing-map machinery as for 4₁ but are not yet identified against an independent invariant;
that and the orientation are the next honest step (bean stays open).

## 4. What it does not do

It does not transcribe Guéritaud; the fold is a search result, stated as such, and a reader who
wants the rule as a theorem should read it off the recorded gluings and prove it, or ingest
Guéritaud 2006. It does not compute the 3d-index or Stokes constants of 5₂. It does not settle
A_ω (`qou-arc1` terminus unchanged; `qou-q3np` open).
