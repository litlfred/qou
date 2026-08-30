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

**Caveat carried from the probe.** The `5₂` boundary-slope datum (`{0,−4,−10}`)
and connection count (`4`) are *literature-recalled* values (bean `qou-52sn`
tracks verifying them with SnapPy). They enter as explicit `def`s below, so the
refutation `r2_slope_reading_refuted` is exactly as strong as that input and no
stronger.

-- Ref: [manuscript] docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md (Route A)
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

/-! ## The `5₂` cross-knot gate

Literature-recalled `5₂` boundary data (bean `qou-52sn` tracks SnapPy
verification); the certified DT spectrum of both knots is `{3,4}`. -/

/-- The certified DT spectrum (both `4₁` and `5₂`; chirality-split at `5₂`). -/
def dtSpectrum : List Int := [3, 4]

/-- `5₂` maximal absolute boundary slope (literature: slopes `{0, −4, −10}`). -/
def fiveTwoMaxAbsSlope : Int := 10

/-- `5₂` number of boundary-parabolic connections (literature: abelian + three). -/
def fiveTwoConnections : Int := 4

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
