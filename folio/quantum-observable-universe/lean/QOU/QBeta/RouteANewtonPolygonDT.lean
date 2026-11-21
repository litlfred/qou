import Init.Data.Int.Basic
import Init.Omega

/-!
# QOU.QBeta.RouteANewtonPolygonDT — the Route-A Newton-polygon readings of the DT spectrum, and the cross-knot refutation

Lean formalization of the assertions of the Route-A probe
(`computations/probes/qbeta_g3_aomega_route_a_newton_polygon.py`; audit
`docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md` §5).
Everything here is **decidable integer lattice geometry** — the Newton polygons in
question are 3- and 4-vertex integer polygons, so the probe's numerics are
promoted to proofs rather than merely re-run.

## What is proved

For the figure-eight `4₁`, from the A-polynomial
`A_{4₁}(M,L) = −M⁴ + L(1 − M² − 2M⁴ − M⁶ + M⁸) − L²M⁴` (geometric component):

* `a41_edge_slopes_pm_four` — every non-vertical Newton-polygon edge has slope
  `±4` (the boundary slopes of `4₁`);
* `a41_full_L_degree_eq_three` — the full A-polynomial (geometric `×` the abelian
  `(L−1)`) has `L`-degree `3` = the number of boundary-parabolic `SL₂(ℂ)`
  connections `{0, g, ḡ}`.

Both `3` and `4` are members of the certified DT spectrum `{3,4}`
(`StokesQZeroDTCount`, `FiveTwoDTSpectrumSplit`), which is what made the Newton
polygon look like the internal handle. Two **negative** results decide the matter:

* `c1_slope_ne_a41_slope` — the QOU C1 binding carrier
  `[m+2]_q b_{m+2} = b_{m+1} + b_m` has Newton slopes `±1/2`, **not** `±4`, so C1
  is *not* the quantum A-polynomial of `4₁`; Route A needs the true colored-Jones
  recursion `Â_K`.
* `r2_slope_reading_refuted` — the slope reading (`DT integer = boundary slope`)
  **fails the `5₂` cross-knot gate**: `5₂`'s maximal boundary slope is `10 ∉ {3,4}`.
  The `4₁` coincidence `4 = |slope|` is single-knot only.
* `r1_connection_reading_survives` — the `L`-degree / connection-count reading
  survives both knots (`4₁ ↦ 3`, `5₂ ↦ 4`, both in `{3,4}`).

The surviving reading `R1` is an Euler-characteristic-type datum, which is why the
audit pivots to Route C; and by
`FiveTwoDTSpectrumSplit.symmetric_scalar_blind_to_chirality` even `R1`, being a
scalar, cannot equal the chirality-split datum. Nothing here derives `A_ω`.

**Caveat retired 2026-09-07.** The `5₂` boundary-slope datum (`{0,−4,−10}`)
and connection count (`4`) were *literature-recalled* `def`s (bean `qou-52sn`).
They are now derived from the corpus's own `A_{5₂}` (#6985, Farey word `RL`):
`a52_edge_slopes_in_0_m4_m10`, `fiveTwoMaxAbsSlope_derived`,
`fiveTwoConnections_eq_four`. The section *The mirror* proves both Route-A
inputs mirror-invariant, so the derived frame's sign information — the one
thing #6985 adds beyond the recalled table — is invisible to Route A by
construction.

-- Ref: [leitner2026] docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md (Route A)
-/

namespace QOU.QBeta.RouteANewtonPolygonDT

/-! ## Lattice-geometry vocabulary (core `Int`, no archimedean structure) -/

/-- A Newton-polygon lattice point `(M-exponent, L-exponent)`. -/
abbrev Pt := Int × Int

/-- The edge vector `(dM, dL)` between two lattice points. -/
def edgeVec (p q : Pt) : Pt := (q.1 - p.1, q.2 - p.2)

/-- An edge is **vertical** (parallel to the `M`-axis, i.e. `dL = 0`); such edges
carry no boundary slope. -/
def isVertical (v : Pt) : Prop := v.2 = 0

instance (v : Pt) : Decidable (isVertical v) := by
  unfold isVertical; infer_instance

/-- Slope equality by cross-multiplication: `dM₁/dL₁ = dM₂/dL₂`. Avoids rationals
so the whole file stays in core `Int`. -/
def slopeEq (v w : Pt) : Prop := v.1 * w.2 = w.1 * v.2

instance (v w : Pt) : Decidable (slopeEq v w) := by
  unfold slopeEq; infer_instance

/-- The integer slope `s` as an edge vector `(s, 1)`. -/
def intSlope (s : Int) : Pt := (s, 1)

/-! ## The figure-eight A-polynomial Newton polygon

`A_{4₁}(M,L) = −M⁴ + L(1 − M² − 2M⁴ − M⁶ + M⁸) − L²M⁴` has monomials (in
`(M-exp, L-exp)`) `(4,0), (0,1), (2,1), (4,1), (6,1), (8,1), (4,2)`, whose convex
hull is the quadrilateral below (the interior/edge-interior points `(2,1),(4,1),
(6,1)` are not vertices). -/

/-- Convex-hull vertices of the `4₁` Newton polygon, counter-clockwise. -/
def a41Hull : List Pt := [(0, 1), (4, 0), (8, 1), (4, 2)]

/-- All monomials of `A_{4₁}` (geometric component), including the three
edge-interior points `(2,1), (4,1), (6,1)` that are not hull vertices. -/
def a41Monomials : List Pt :=
  [(4, 0), (0, 1), (2, 1), (4, 1), (6, 1), (8, 1), (4, 2)]

/-! ### Transcription check — the A-polynomial reciprocal symmetry

The `A_{4₁}` monomial data is *typed in* (it is a literature value, not something
Lean can read off a knot). It is not unchecked, however: A-polynomials satisfy a
reciprocal symmetry `(M,L) ↦ (M⁻¹, L⁻¹)`, which on the Newton polygon is the
central point-reflection about the polygon's centre — here `(4,1)`, i.e.
`(m,l) ↦ (8−m, 2−l)`. A transcription slip in any exponent would generically
break it, so the two theorems below are a genuine (if partial) integrity check on
the input, in the same spirit as the `det S± = 1` and `S⁺ᵀS⁻ = 1` identities that
certify the Stokes matrices in `FiveTwoStokesMatrixIdentities`. -/

/-- The central reflection of the `4₁` Newton polygon about its centre `(4,1)`. -/
def a41Reflect (p : Pt) : Pt := (8 - p.1, 2 - p.2)

/-- **The `4₁` Newton polygon is centrally symmetric** (hull level): the
reflection permutes the hull vertices. -/
theorem a41_hull_reciprocal_symmetric :
    ∀ p ∈ a41Hull, a41Reflect p ∈ a41Hull := by decide

/-- **The full monomial set is centrally symmetric too** — the reciprocal
symmetry `(M,L) ↦ (M⁻¹,L⁻¹)` of the A-polynomial, at the level of exponents.
This is the integrity check on the typed-in polynomial. -/
theorem a41_monomials_reciprocal_symmetric :
    ∀ p ∈ a41Monomials, a41Reflect p ∈ a41Monomials := by decide

/-- The reflection is an involution (so the symmetry above is a genuine
pairing). -/
theorem a41Reflect_involutive (p : Pt) : a41Reflect (a41Reflect p) = p := by
  cases p
  unfold a41Reflect
  refine Prod.ext ?_ ?_ <;> simp <;> omega

/-- The four edges of the `4₁` Newton polygon. -/
def a41Edges : List Pt :=
  [ edgeVec (0, 1) (4, 0)      -- ( 4, -1)  slope -4
  , edgeVec (4, 0) (8, 1)      -- ( 4,  1)  slope  4
  , edgeVec (8, 1) (4, 2)      -- (-4,  1)  slope -4
  , edgeVec (4, 2) (0, 1) ]    -- (-4, -1)  slope  4

/-- **Every `4₁` Newton edge has boundary slope `±4`.** No edge is vertical, and
each is slope-equal to `+4` or `−4`. -/
theorem a41_edge_slopes_pm_four :
    ∀ v ∈ a41Edges, ¬ isVertical v ∧ (slopeEq v (intSlope 4) ∨ slopeEq v (intSlope (-4))) := by
  decide

/-- The maximal absolute boundary slope of `4₁` is `4` — a member of the certified
DT spectrum `{3,4}`, which is what motivated the slope reading `R2`. -/
def a41MaxAbsSlope : Int := 4

/-- `L`-degree of the **geometric** component (`L²` is its top power). -/
def a41GeomLDegree : Int := 2

/-- `L`-degree of the **full** A-polynomial: the geometric component times the
abelian factor `(L − 1)`. -/
def a41FullLDegree : Int := a41GeomLDegree + 1

/-- **The full `4₁` A-polynomial has `L`-degree `3`** — the number of
boundary-parabolic `SL₂(ℂ)` connections `{0, g, ḡ}`, and the other DT integer. -/
theorem a41_full_L_degree_eq_three : a41FullLDegree = 3 := by decide

/-! ## The QOU C1 binding carrier is not the quantum A-polynomial

`[m+2]_q · b_{m+2} = b_{m+1} + b_m` with `M = q^m` and `L` the shift, in balanced
form `(q²M − q⁻²M⁻¹)L² − (q − q⁻¹)(L + 1) = 0`, has monomials
`(1,2), (−1,2), (0,1), (0,0)` and hull `(−1,2), (0,0), (1,2)`. -/

/-- Convex-hull vertices of the C1 Newton polygon. -/
def c1Hull : List Pt := [(-1, 2), (0, 0), (1, 2)]

/-- The non-vertical C1 edges (the edge `(1,2) → (−1,2)` is vertical). -/
def c1NonVerticalEdges : List Pt :=
  [ edgeVec (-1, 2) (0, 0)     -- ( 1, -2)  slope -1/2
  , edgeVec (0, 0) (1, 2) ]    -- ( 1,  2)  slope  1/2

/-- **C1's Newton slopes are `±1/2`.** -/
theorem c1_edge_slopes_pm_half :
    ∀ v ∈ c1NonVerticalEdges,
      slopeEq v (1, 2) ∨ slopeEq v (-1, 2) := by
  decide

/-- **C1 is not the quantum A-polynomial of `4₁`.** Its Newton slope `1/2` is not
the `4₁` boundary slope `4`: cross-multiplying, `1 * 1 ≠ 4 * 2`. Route A therefore
requires the genuine colored-Jones recursion `Â_K`, not the binding carrier. -/
theorem c1_slope_ne_a41_slope : ¬ slopeEq (1, 2) (intSlope 4) := by decide

/-! ## The `5₂` Newton polygon from the DERIVED A-polynomial (added 2026-09-07)

Until 2026-09-07 the `5₂` inputs below were literature-recalled `def`s (bean
`qou-52sn`). They are now read off the A-polynomial **derived in this corpus**
from the Farey word `RL` — `two_bridge_cusp_rows_apoly_probe.py` (#6985; the
meridian pinned by the Dehn-filling test, the polynomial fitted on a continuation
grid and verified on fresh samples) — and carried as a polynomial in
`FiveTwoAPolynomialFromFareyWord.A`:

    A_{5₂} = L³ + L²(M¹⁰ − M⁸ + 2M⁴ + 2M² − 1) + L(−M¹⁴ + 2M¹² + 2M¹⁰ − M⁶ + M⁴) + M¹⁴

in the frame `(μ by the filling test, λ homological, Im(t_λ/t_μ) > 0)`. Its
monomials in `(M-exp, L-exp)` are listed in `a52Monomials`; the hull vertices in
`a52Hull`. The transcription is checked the same way as for `4₁`: the reciprocal
symmetry `(M,L) ↦ (M⁻¹,L⁻¹)` — proved on the polynomial itself as
`FiveTwoAPolynomialFromFareyWord.A_involution`, `L³M¹⁴·A(L⁻¹,M⁻¹) = A(L,M)` —
is the central reflection `(m,l) ↦ (14−m, 3−l)` on exponents. -/

/-- Convex-hull vertices of the `5₂` Newton polygon, counter-clockwise, in
`(M-exp, L-exp)`. (The producer records them as `(deg_L, deg_M)`:
`(0,14),(1,4),(2,0),(3,0),(2,10),(1,14)`.) -/
def a52Hull : List Pt := [(0, 3), (0, 2), (4, 1), (14, 0), (14, 1), (10, 2)]

/-- All twelve monomials of the derived `A_{5₂}`, in `(M-exp, L-exp)`. -/
def a52Monomials : List Pt :=
  [ (0, 3)
  , (10, 2), (8, 2), (4, 2), (2, 2), (0, 2)
  , (14, 1), (12, 1), (10, 1), (6, 1), (4, 1)
  , (14, 0) ]

/-- The central reflection of the `5₂` Newton polygon about `(7, 3/2)`. -/
def a52Reflect (p : Pt) : Pt := (14 - p.1, 3 - p.2)

/-- **The `5₂` hull is centrally symmetric.** -/
theorem a52_hull_reciprocal_symmetric :
    ∀ p ∈ a52Hull, a52Reflect p ∈ a52Hull := by decide

/-- **The `5₂` monomial set is centrally symmetric** — the exponent-level shadow
of `A_involution`, and the transcription check on the list. -/
theorem a52_monomials_reciprocal_symmetric :
    ∀ p ∈ a52Monomials, a52Reflect p ∈ a52Monomials := by decide

theorem a52Reflect_involutive (p : Pt) : a52Reflect (a52Reflect p) = p := by
  cases p
  unfold a52Reflect
  refine Prod.ext ?_ ?_ <;> simp <;> omega

/-- Every hull vertex is a monomial. -/
theorem a52_hull_subset_monomials : ∀ p ∈ a52Hull, p ∈ a52Monomials := by decide

/-- The six edges of the `5₂` Newton polygon (counter-clockwise). -/
def a52Edges : List Pt :=
  [ edgeVec (0, 3) (0, 2)       -- (  0, -1)  slope   0
  , edgeVec (0, 2) (4, 1)       -- (  4, -1)  slope  -4
  , edgeVec (4, 1) (14, 0)      -- ( 10, -1)  slope -10
  , edgeVec (14, 0) (14, 1)     -- (  0,  1)  slope   0
  , edgeVec (14, 1) (10, 2)     -- ( -4,  1)  slope  -4
  , edgeVec (10, 2) (0, 3) ]    -- (-10,  1)  slope -10

/-- **Every `5₂` Newton edge has boundary slope in `{0, −4, −10}`**, and none is
vertical — the derived boundary-slope set, in the derived frame. -/
theorem a52_edge_slopes_in_0_m4_m10 :
    ∀ v ∈ a52Edges, ¬ isVertical v ∧
      (slopeEq v (intSlope 0) ∨ slopeEq v (intSlope (-4)) ∨ slopeEq v (intSlope (-10))) := by
  decide

/-- Each of the three slopes is attained. -/
theorem a52_slopes_attained :
    (∃ v ∈ a52Edges, slopeEq v (intSlope 0)) ∧
    (∃ v ∈ a52Edges, slopeEq v (intSlope (-4))) ∧
    (∃ v ∈ a52Edges, slopeEq v (intSlope (-10))) := by
  decide

/-- The `L`-exponent profile of a monomial list. -/
def lProfile (l : List Pt) : List Int := l.map Prod.snd

/-- `L`-degree of the derived geometric `A_{5₂}`: the largest `L`-exponent. -/
def a52GeomLDegree : Int := (lProfile a52Monomials).foldl max 0

theorem a52_geom_L_degree_eq_three : a52GeomLDegree = 3 := by decide

/-- Full `A_{5₂}` = geometric × the abelian factor `(L − 1)`. -/
def a52FullLDegree : Int := a52GeomLDegree + 1

/-! ### The mirror, and what the Newton polygon cannot see

The mirror image `K̄` has `A_{K̄}(L, M) = A_K(L, M⁻¹)` up to a unit, so on exponents
it is `(m, l) ↦ (−m, l)`: every boundary slope changes sign, and the `L`-profile
is untouched. The two Route-A inputs — the maximal **absolute** slope (`R2`) and
the `L`-degree (`R1`) — are therefore invariant under the mirror. The `5₂` DT
datum is the *ordered* pair `(4 ∈ S⁺, 3 ∈ S⁻)` whose bar-odd part is nonzero
(`FiveTwoDTSpectrumSplit.chirality_odd_datum_ne_zero`); a quantity that cannot
tell `5₂` from its mirror cannot carry it. This sharpens
`FiveTwoDTSpectrumSplit.symmetric_scalar_blind_to_chirality` from "no symmetric
scalar" to "no Newton-polygon slope-magnitude or degree datum", and it is the
reason the derived frame (#6985, which fixes the *sign* of the slopes) adds
nothing to Route A: the sign is exactly what Route A discards. -/

/-- The mirror on exponents: `M ↦ M⁻¹`. -/
def mirrorPt (p : Pt) : Pt := (-p.1, p.2)

/-- The mirror negates every slope: `v` has slope `s` iff `mirrorPt v` has slope
`−s`. -/
theorem slopeEq_mirror (v : Pt) (s : Int) :
    slopeEq (mirrorPt v) (intSlope (-s)) ↔ slopeEq v (intSlope s) := by
  cases v
  unfold slopeEq mirrorPt intSlope
  constructor <;> intro h <;> simp [Int.neg_mul] at * <;> omega

/-- Verticality is mirror-invariant. -/
theorem isVertical_mirror (v : Pt) : isVertical (mirrorPt v) ↔ isVertical v := by
  cases v; unfold isVertical mirrorPt; exact Iff.rfl

/-- Absolute slope `|s|`, as the disjunction "slope `s` or slope `−s`". -/
def absSlopeEq (v : Pt) (s : Int) : Prop :=
  slopeEq v (intSlope s) ∨ slopeEq v (intSlope (-s))

instance (v : Pt) (s : Int) : Decidable (absSlopeEq v s) := by
  unfold absSlopeEq; infer_instance

/-- **The absolute boundary slope is mirror-invariant** — so the `R2` input is. -/
theorem absSlopeEq_mirror (v : Pt) (s : Int) :
    absSlopeEq (mirrorPt v) s ↔ absSlopeEq v s := by
  cases v
  unfold absSlopeEq slopeEq mirrorPt intSlope
  constructor <;> intro h <;> simp [Int.neg_mul] at * <;> omega

/-- **The `L`-profile is mirror-invariant** — so the `L`-degree (`R1`) is. -/
theorem lProfile_mirror (l : List Pt) : lProfile (l.map mirrorPt) = lProfile l := by
  unfold lProfile
  induction l with
  | nil => rfl
  | cons p t ih => simp [List.map, mirrorPt, ih]

/-- The mirrored `5₂` edges carry slopes `{0, 4, 10}` — the literature set as
usually printed, i.e. the derived triangulation is the mirror of *that*
convention's `5₂` (which of the two is Rolfsen's is a convention no held source
settles). -/
theorem a52_mirror_edge_slopes_in_0_4_10 :
    ∀ v ∈ a52Edges.map mirrorPt,
      slopeEq v (intSlope 0) ∨ slopeEq v (intSlope 4) ∨ slopeEq v (intSlope 10) := by
  decide

/-! ## The `5₂` cross-knot gate

The `5₂` inputs are now theorems about the derived data above; the literal
values the gate was first run on (bean `qou-52sn`, literature-recalled) are
recovered from them, so the refutation below is exactly as strong as #6985's
derivation and no longer conditional on a recalled table. -/

/-- The certified DT spectrum (both `4₁` and `5₂`; chirality-split at `5₂`). -/
def dtSpectrum : List Int := [3, 4]

/-- `5₂` maximal absolute boundary slope. Derived: `a52_edge_slopes_in_0_m4_m10`
+ `a52_slopes_attained` (slope `−10` is attained, nothing beyond it). -/
def fiveTwoMaxAbsSlope : Int := 10

/-- **`10` is the maximal absolute slope of the derived polygon**: every edge has
`|slope| ≤ 10` (as `|dM| ≤ 10·|dL|`) and some edge attains it. -/
theorem fiveTwoMaxAbsSlope_derived :
    (∀ v ∈ a52Edges, absSlopeEq v 0 ∨ absSlopeEq v 4 ∨ absSlopeEq v fiveTwoMaxAbsSlope) ∧
    (∃ v ∈ a52Edges, absSlopeEq v fiveTwoMaxAbsSlope) := by
  decide

/-- `5₂` number of boundary-parabolic connections `= L`-degree of the full
A-polynomial: abelian + the three of the geometric component. -/
def fiveTwoConnections : Int := a52FullLDegree

/-- **The full derived `A_{5₂}` has `L`-degree `4`** (geometric `3` + abelian `1`). -/
theorem fiveTwoConnections_eq_four : fiveTwoConnections = 4 := by decide

/-- `4₁` number of boundary-parabolic connections `= L`-degree of the full
A-polynomial. -/
def a41Connections : Int := a41FullLDegree

/-- **R2 (slope reading) is REFUTED on the cross-knot gate.** The reading holds at
`4₁` (`|slope| = 4 ∈ {3,4}`) but fails at `5₂` (`|slope| = 10 ∉ {3,4}`), so
"DT integer = boundary slope" is a single-knot coincidence. -/
theorem r2_slope_reading_refuted :
    a41MaxAbsSlope ∈ dtSpectrum ∧ fiveTwoMaxAbsSlope ∉ dtSpectrum := by
  decide

/-- **R1 (connection-count / `L`-degree reading) SURVIVES the cross-knot gate.**
Both knots' connection counts lie in the DT spectrum (`4₁ ↦ 3`, `5₂ ↦ 4`). -/
theorem r1_connection_reading_survives :
    a41Connections ∈ dtSpectrum ∧ fiveTwoConnections ∈ dtSpectrum := by
  decide

/-- **Route-A verdict, assembled.** The slope reading dies on `5₂`; the
connection-count reading survives both knots; and C1 is not the quantum
A-polynomial. (That the surviving scalar reading still cannot *equal* the
chirality-split datum is
`FiveTwoDTSpectrumSplit.symmetric_scalar_blind_to_chirality` — which is why the
programme pivots to Route C.) -/
theorem route_a_verdict :
    (a41MaxAbsSlope ∈ dtSpectrum ∧ fiveTwoMaxAbsSlope ∉ dtSpectrum) ∧
    (a41Connections ∈ dtSpectrum ∧ fiveTwoConnections ∈ dtSpectrum) ∧
    (¬ slopeEq (1, 2) (intSlope 4)) := by
  decide

end QOU.QBeta.RouteANewtonPolygonDT
