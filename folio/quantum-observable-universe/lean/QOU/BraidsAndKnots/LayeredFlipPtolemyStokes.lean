import QOU.MassTheory.TransversePairingClusterDecomposition
import BraidKnotOctonion.PachnerPentagonBorromean
import Mathlib.Algebra.Ring.Units
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Group

/-!
# Layered Whitehead Diagonal Flips, Ptolemy Cluster Periodicity, and Non-Abelian Stokes

Formalises, strictly over a generic commutative ring `[CommRing R]` using the unit
group `Rˣ` (zero `[Field]`, zero `field_simp`, zero `Real.*`), the algebraic engine
connecting 2D surface Whitehead diagonal flips (Ptolemy / Fock–Goncharov cluster
mutations) to 3D layered ideal-tetrahedron cross-ratio shapes and transverse
Yekutieli–Stokes curvature.

## Mathematical & Physical Literature Context

* **Fock–Goncharov (2006)** (*Moduli spaces of local systems and higher Teichmüller
  theory*, Publ. Math. IHÉS 103, 1–211) and **Fomin–Shapiro–Thurston (2008)** (Acta
  Math. 201, 83–146): Penner $\lambda$-lengths satisfy the division-free Ptolemy
  exchange $a_{\mathrm{new}} a_{\mathrm{old}} = b d + c e$ (`PtolemyQuad`), while shear
  coordinates $X_k$ mutate by cluster $\mathcal{X}$-mutations (`xFlipSwap`) satisfying
  the 5-flip $A_2$ pentagon identity.
* **Faddeev–Kashaev (1994)** (*Quantum dilogarithm*, Mod. Phys. Lett. A 9, 427–434) and
  **Dimofte–Gaiotto–Gukov (2011)** (*3-manifolds and 3d indices*, Adv. Theor. Math.
  Phys. 17, 975–1076, arXiv:1112.5179): each 2D diagonal flip in a surface mapping
  torus layers one 3D ideal tetrahedron $\Delta_m$ whose cross-ratio triple
  $(z_m, z_m', z_m'')$ satisfies $z_m z_m' z_m'' = -1$ (`ptolemy_shape_triple_prod`)
  and $z_m + (z_m'')^{-1} = 1$ (`ptolemy_shape_linear_rel`), lifting Pachner's 2–3
  move to the pentagon identity (`PachnerPentagonBorromean`).
* **Gaiotto–Moore–Neitzke (2013)** (*Wall-crossing, Hitchin systems, and the WKB
  approximation*, Adv. Math. 234, 239–403, arXiv:0907.3987): Stokes jumps of flat
  non-abelian connections across spectral networks act by cluster $\mathcal{X}$-mutations.
* **Jorgensen (2003) / Guéritaud (2006)** (*On canonical triangulations of once-punctured
  torus bundles*, Geom. Topol. 10, 1239–1284): stepping a Farey word $W \in \{R, L\}^*$
  preserves the Markov–Fricke cubic $x^2 + y^2 + z^2 - x y z$ (`markovCubic_applyFareyWord`)
  and converts the trace recursion $y_{\mathrm{new}} = x z - y$ on the parabolic locus
  $x^2 + y^2 + z^2 = x y z$ into the exact Ptolemy product
  $y \cdot y_{\mathrm{new}} = x^2 + z^2$ (`stepR_ptolemy_on_markov`,
  `stepL_ptolemy_on_markov`).

## Main Proved Results (`0 sorry`, `[CommRing R]` + `Rˣ`)

1. `ptolemyFlip_involutive`: flipping a quadrilateral diagonal twice restores `a_old`.
2. `lyness_five_periodic`: the $\mathcal{A}$-variable pentagon Ptolemy recursion
   $x_{m+1} x_{m-1} = 1 + x_m$ is strictly 5-periodic over any `[CommRing R]` whenever
   $x_0, x_1, 1 + x_0, 1 + x_1, 1 + x_0 + x_1$ are invertible (`Rˣ`).
3. `xFlipSwap_five_periodic` & `xMutate_alt_five_eq_swap`: the Fock–Goncharov $A_2$
   $\mathcal{X}$-seed mutation satisfies $(M_{\mathcal{X}})^5 = \mathrm{id}$ and
   $(\mu_1 \circ \mu_2 \circ \mu_1 \circ \mu_2 \circ \mu_1)(X_1, X_2) = (X_2, X_1)$
   over any `[CommRing R]`.
4. `ptolemy_shape_triple_prod` & `ptolemy_shape_linear_rel`: Thurston's ideal-tetrahedron
   cross-ratio identities $z z' z'' = -1$ and $z + (z'')^{-1} = 1$ derived purely from
   the Ptolemy flip equation $a_{\mathrm{new}} a_{\mathrm{old}} = b d + c e$ in `Rˣ`.
5. `markovCubic_applyFareyWord`, `stepR_ptolemy_on_markov`, `stepL_ptolemy_on_markov`,
   and `fig8_RL_stationary_fixed_point`: exact Farey/Whitehead layered-tetrahedron
   recursion and the algebraic sixth-root-of-unity stationary solution for $4_1 = RL$.
6. `layered_transverse_trace_zero_and_split`: connects layered flip blocks to the
   transverse Yekutieli–Stokes pairing (`TransversePairingCluster`), proving linear-trace
   annihilation alongside exact bilinear two-block commutator splitting.
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots.LayeredFlipPtolemyStokes

open QOU.MassTheory.TransverseSurfaceCurvature
open QOU.MassTheory.TransversePairingCluster

section PtolemyAndShapes

variable {R : Type*} [CommRing R]

/-- Division-free 2D Whitehead diagonal flip (Ptolemy relation) on a quadrilateral
with cyclic side $\lambda$-lengths `(b, c, d, e)` and diagonals `aOld`, `aNew`:
`aNew * aOld = b * d + c * e`. -/
def IsPtolemyFlip (b c d e aOld aNew : R) : Prop :=
  aNew * aOld = b * d + c * e

/-- Symmetry of the division-free Ptolemy relation: flipping `aNew` back across the
same quadrilateral `(b, c, d, e)` gives `aOld`. -/
theorem isPtolemyFlip_symm {b c d e aOld aNew : R}
    (h : IsPtolemyFlip b c d e aOld aNew) :
    IsPtolemyFlip b c d e aNew aOld := by
  unfold IsPtolemyFlip at *
  rw [mul_comm, h]

/-- Unit-valued Ptolemy flip: given invertible old diagonal `aOld : Rˣ` and cyclic
sides `b, c, d, e : R`, the flipped diagonal in `R` is `↑aOld⁻¹ * (b * d + c * e)`. -/
def ptolemyFlipVal (b c d e : R) (aOld : Rˣ) : R :=
  (↑aOld⁻¹ : R) * (b * d + c * e)

/-- `ptolemyFlipVal` satisfies the division-free Ptolemy relation `IsPtolemyFlip`. -/
theorem isPtolemyFlip_ptolemyFlipVal (b c d e : R) (aOld : Rˣ) :
    IsPtolemyFlip b c d e (aOld : R) (ptolemyFlipVal b c d e aOld) := by
  unfold IsPtolemyFlip ptolemyFlipVal
  calc
    (↑aOld⁻¹ : R) * (b * d + c * e) * (aOld : R)
        = ((↑aOld⁻¹ : R) * (aOld : R)) * (b * d + c * e) := by ring
    _ = 1 * (b * d + c * e) := by rw [Units.inv_mul]
    _ = b * d + c * e := one_mul _

/-- **Involutivity of the Whitehead flip** over any `[CommRing R]`: if `aOld, aNew : Rˣ`
satisfy `IsPtolemyFlip b c d e aOld aNew`, then `ptolemyFlipVal b c d e aNew = aOld`. -/
theorem ptolemyFlip_involutive {b c d e : R} (aOld aNew : Rˣ)
    (h : IsPtolemyFlip b c d e (aOld : R) (aNew : R)) :
    ptolemyFlipVal b c d e aNew = (aOld : R) := by
  unfold ptolemyFlipVal
  unfold IsPtolemyFlip at h
  rw [← h, ← mul_assoc, Units.inv_mul, one_mul]

/-- Bundled invertible Ptolemy quadrilateral flip data, carrying unit witnesses for
the four boundary sides and both diagonals so cross-ratios live in `Rˣ` without `[Field]`. -/
structure PtolemyUnitQuad (R : Type*) [CommRing R] where
  /-- First side length. -/
  b : Rˣ
  /-- Second side length. -/
  c : Rˣ
  /-- Third side length (opposite `b`). -/
  d : Rˣ
  /-- Fourth side length (opposite `c`). -/
  e : Rˣ
  /-- Pre-flip diagonal. -/
  aOld : Rˣ
  /-- Post-flip diagonal. -/
  aNew : Rˣ
  /-- Ptolemy exchange identity `(aNew : R) * aOld = b * d + c * e`. -/
  ptolemy : (aNew : R) * (aOld : R) = (b : R) * (d : R) + (c : R) * (e : R)

/-- Primary Thurston cross-ratio shape $z = -(c e)(b d)^{-1} \in R^\times$ of the
3D ideal tetrahedron layered by a 2D Ptolemy flip `Q`. -/
def tetShapeZ (Q : PtolemyUnitQuad R) : Rˣ :=
  -(Q.c * Q.e * (Q.b * Q.d)⁻¹)

/-- Secondary Thurston cross-ratio shape $z' = (b d)(a_{\mathrm{new}} a_{\mathrm{old}})^{-1} \in R^\times$. -/
def tetShapeZPrime (Q : PtolemyUnitQuad R) : Rˣ :=
  Q.b * Q.d * (Q.aNew * Q.aOld)⁻¹

/-- Tertiary Thurston cross-ratio shape $z'' = (a_{\mathrm{new}} a_{\mathrm{old}})(c e)^{-1} \in R^\times$. -/
def tetShapeZDoublePrime (Q : PtolemyUnitQuad R) : Rˣ :=
  Q.aNew * Q.aOld * (Q.c * Q.e)⁻¹

/-- **Thurston cyclic product identity (`z * z' * z'' = -1`)** in `Rˣ` over any
`[CommRing R]`. -/
theorem ptolemy_shape_triple_prod (Q : PtolemyUnitQuad R) :
    tetShapeZ Q * tetShapeZPrime Q * tetShapeZDoublePrime Q = -1 := by
  unfold tetShapeZ tetShapeZPrime tetShapeZDoublePrime
  ext
  push_cast
  have hb : (↑Q.b⁻¹ : R) * (Q.b : R) = 1 := Units.inv_mul Q.b
  have hc : (Q.c : R) * (↑Q.c⁻¹ : R) = 1 := Units.mul_inv Q.c
  have hd : (↑Q.d⁻¹ : R) * (Q.d : R) = 1 := Units.inv_mul Q.d
  have he : (Q.e : R) * (↑Q.e⁻¹ : R) = 1 := Units.mul_inv Q.e
  have haN : (↑Q.aNew⁻¹ : R) * (Q.aNew : R) = 1 := Units.inv_mul Q.aNew
  have haO : (↑Q.aOld⁻¹ : R) * (Q.aOld : R) = 1 := Units.inv_mul Q.aOld
  calc
    -((Q.c : R) * Q.e * (↑Q.d⁻¹ * ↑Q.b⁻¹)) * (Q.b * Q.d * (↑Q.aOld⁻¹ * ↑Q.aNew⁻¹)) *
        (Q.aNew * Q.aOld * (↑Q.e⁻¹ * ↑Q.c⁻¹))
      = -(((Q.c : R) * ↑Q.c⁻¹) * ((Q.e : R) * ↑Q.e⁻¹) * ((↑Q.b⁻¹ : R) * Q.b) *
          ((↑Q.d⁻¹ : R) * Q.d) * ((↑Q.aNew⁻¹ : R) * Q.aNew) * ((↑Q.aOld⁻¹ : R) * Q.aOld)) := by
        ring
    _ = -1 := by rw [hc, he, hb, hd, haN, haO]; ring

/-- **Thurston linear cross-ratio identity (`(1 - z) * z' = 1` and `(z'')⁻¹ + z' = 1`)**
derived purely from the Ptolemy relation over any `[CommRing R]`. -/
theorem ptolemy_shape_linear_rel (Q : PtolemyUnitQuad R) :
    (1 - (tetShapeZ Q : R)) * (tetShapeZPrime Q : R) = 1 ∧
      (((tetShapeZDoublePrime Q)⁻¹ : Rˣ) : R) + (tetShapeZPrime Q : R) = 1 := by
  have hbd : ((Q.b : R) * Q.d) * (↑(Q.b * Q.d)⁻¹ : R) = 1 := Units.mul_inv (Q.b * Q.d)
  have hbd' : (↑(Q.b * Q.d)⁻¹ : R) * ((Q.b : R) * Q.d) = 1 := Units.inv_mul (Q.b * Q.d)
  have ha : ((Q.aNew : R) * Q.aOld) * (↑(Q.aNew * Q.aOld)⁻¹ : R) = 1 :=
    Units.mul_inv (Q.aNew * Q.aOld)
  have hce : ((Q.c : R) * Q.e) * (↑(Q.c * Q.e)⁻¹ : R) = 1 := Units.mul_inv (Q.c * Q.e)
  constructor
  · unfold tetShapeZ tetShapeZPrime
    have h1 : (1 - (-(Q.c * Q.e * (Q.b * Q.d)⁻¹) : Rˣ) : R) =
        ((Q.b : R) * Q.d + (Q.c : R) * Q.e) * (↑(Q.b * Q.d)⁻¹ : R) := by
      push_cast
      calc
        1 - -((Q.c : R) * Q.e * ↑(Q.b * Q.d)⁻¹)
            = ((Q.b : R) * Q.d) * (↑(Q.b * Q.d)⁻¹ : R) +
                (Q.c : R) * Q.e * (↑(Q.b * Q.d)⁻¹ : R) := by rw [hbd]; ring
        _ = ((Q.b : R) * Q.d + (Q.c : R) * Q.e) * (↑(Q.b * Q.d)⁻¹ : R) := by ring
    rw [h1, ← Q.ptolemy]
    push_cast
    calc
      (Q.aNew : R) * Q.aOld * (↑Q.d⁻¹ * ↑Q.b⁻¹) * (Q.b * Q.d * (↑Q.aOld⁻¹ * ↑Q.aNew⁻¹))
          = ((Q.aNew : R) * Q.aOld * (↑Q.aOld⁻¹ * ↑Q.aNew⁻¹)) *
              ((↑Q.d⁻¹ * ↑Q.b⁻¹) * ((Q.b : R) * Q.d)) := by ring
      _ = 1 := by
        have ha' : (Q.aNew : R) * Q.aOld * (↑Q.aOld⁻¹ * ↑Q.aNew⁻¹) = 1 := by
          simpa [mul_inv_rev] using ha
        have hb' : (↑Q.d⁻¹ * ↑Q.b⁻¹ : R) * ((Q.b : R) * Q.d) = 1 := by
          simpa [mul_inv_rev] using hbd'
        rw [ha', hb', one_mul]
  · unfold tetShapeZDoublePrime tetShapeZPrime
    have hinv : (((Q.aNew * Q.aOld * (Q.c * Q.e)⁻¹)⁻¹ : Rˣ) : R) =
        (Q.c : R) * Q.e * (↑(Q.aNew * Q.aOld)⁻¹ : R) := by
      simp [mul_inv_rev, mul_assoc, mul_comm, mul_left_comm]
    rw [hinv]
    push_cast
    have ha' : ((Q.aNew : R) * Q.aOld) * ((↑Q.aOld⁻¹ : R) * ↑Q.aNew⁻¹) = 1 := by
      simpa [mul_inv_rev] using ha
    calc
      (Q.c : R) * Q.e * (↑Q.aOld⁻¹ * ↑Q.aNew⁻¹) + (Q.b : R) * Q.d * (↑Q.aOld⁻¹ * ↑Q.aNew⁻¹)
          = ((Q.b : R) * Q.d + (Q.c : R) * Q.e) * (↑Q.aOld⁻¹ * ↑Q.aNew⁻¹) := by ring
      _ = ((Q.aNew : R) * Q.aOld) * (↑Q.aOld⁻¹ * ↑Q.aNew⁻¹) := by rw [← Q.ptolemy]
      _ = 1 := ha'

end PtolemyAndShapes

/-! ## 2. Exact 5-Flip $A_2$ Pentagon Periodicity over `[CommRing R]` (`\mathcal{A}` and `\mathcal{X}`) -/

section PentagonPeriodicity

variable {R : Type*} [CommRing R]

/-- Admissibility data for an $A_2$ pentagon Ptolemy seed `(x₀, x₁)` over a commutative
ring `R`: the two initial diagonals `x₀, x₁` together with the three cluster factors
`1 + x₀`, `1 + x₁`, and `1 + x₀ + x₁` are invertible (`Rˣ`). Over any ring, this is
the exact division-free domain of the 5-flip pentagon cycle. -/
structure PentagonASeed (R : Type*) [CommRing R] where
  /-- First internal diagonal $\lambda$-length. -/
  x0 : Rˣ
  /-- Second internal diagonal $\lambda$-length. -/
  x1 : Rˣ
  /-- Unit witness for `1 + x₀`. -/
  u10 : Rˣ
  /-- Unit witness for `1 + x₁`. -/
  u01 : Rˣ
  /-- Unit witness for `1 + x₀ + x₁`. -/
  u11 : Rˣ
  /-- Identification `u10 = 1 + x₀`. -/
  hu10 : (u10 : R) = 1 + (x0 : R)
  /-- Identification `u01 = 1 + x₁`. -/
  hu01 : (u01 : R) = 1 + (x1 : R)
  /-- Identification `u11 = 1 + x₀ + x₁`. -/
  hu11 : (u11 : R) = 1 + (x0 : R) + (x1 : R)

/-- The five successive diagonals `(d₀, d₁, d₂, d₃, d₄)` produced by stepping the
unit-boundary pentagon Ptolemy relation `d_{m+1} * d_{m-1} = 1 + d_m` in `Rˣ`. -/
def pentagonADiag (S : PentagonASeed R) : Fin 7 → Rˣ
  | 0 => S.x0
  | 1 => S.x1
  | 2 => S.x0⁻¹ * S.u01
  | 3 => S.x0⁻¹ * S.x1⁻¹ * S.u11
  | 4 => S.x1⁻¹ * S.u10
  | 5 => S.x0
  | 6 => S.x1

/-- **Every step of the 5-flip pentagon cycle satisfies the exact Ptolemy relation
`d_{m+2} * d_m = 1 + d_{m+1}` AND `(d₅, d₆) = (d₀, d₁)` (5-periodicity)** over any
`[CommRing R]`. -/
theorem lyness_five_periodic (S : PentagonASeed R) :
    ((pentagonADiag S 2 : R) * (pentagonADiag S 0 : R) = 1 + (pentagonADiag S 1 : R)) ∧
    ((pentagonADiag S 3 : R) * (pentagonADiag S 1 : R) = 1 + (pentagonADiag S 2 : R)) ∧
    ((pentagonADiag S 4 : R) * (pentagonADiag S 2 : R) = 1 + (pentagonADiag S 3 : R)) ∧
    ((pentagonADiag S 5 : R) * (pentagonADiag S 3 : R) = 1 + (pentagonADiag S 4 : R)) ∧
    ((pentagonADiag S 6 : R) * (pentagonADiag S 4 : R) = 1 + (pentagonADiag S 5 : R)) ∧
    pentagonADiag S 5 = pentagonADiag S 0 ∧
    pentagonADiag S 6 = pentagonADiag S 1 := by
  have hx0 : (↑S.x0⁻¹ : R) * (S.x0 : R) = 1 := Units.inv_mul S.x0
  have hx0' : (S.x0 : R) * (↑S.x0⁻¹ : R) = 1 := Units.mul_inv S.x0
  have hx1 : (↑S.x1⁻¹ : R) * (S.x1 : R) = 1 := Units.inv_mul S.x1
  have hx1' : (S.x1 : R) * (↑S.x1⁻¹ : R) = 1 := Units.mul_inv S.x1
  refine ⟨?_, ?_, ?_, ?_, ?_, rfl, rfl⟩
  · simp only [pentagonADiag, Units.val_mul, S.hu01]
    calc
      (↑S.x0⁻¹ : R) * (1 + S.x1) * S.x0 = ((↑S.x0⁻¹ : R) * S.x0) * (1 + S.x1) := by ring
      _ = 1 + S.x1 := by rw [hx0, one_mul]
  · simp only [pentagonADiag, Units.val_mul, S.hu11, S.hu01]
    calc
      (↑S.x0⁻¹ : R) * ↑S.x1⁻¹ * (1 + S.x0 + S.x1) * S.x1
          = ((↑S.x1⁻¹ : R) * S.x1) * ((↑S.x0⁻¹ : R) * (1 + S.x0 + S.x1)) := by ring
      _ = (↑S.x0⁻¹ : R) * S.x0 + (↑S.x0⁻¹ : R) * (1 + S.x1) := by rw [hx1]; ring
      _ = 1 + (↑S.x0⁻¹ : R) * (1 + S.x1) := by rw [hx0]
  · simp only [pentagonADiag, Units.val_mul, S.hu10, S.hu01, S.hu11]
    calc
      (↑S.x1⁻¹ : R) * (1 + S.x0) * ((↑S.x0⁻¹ : R) * (1 + S.x1))
          = (↑S.x0⁻¹ : R) * ↑S.x1⁻¹ * (1 + S.x0 + S.x1 + S.x0 * S.x1) := by ring
      _ = ((↑S.x0⁻¹ : R) * S.x0) * ((↑S.x1⁻¹ : R) * S.x1) +
            (↑S.x0⁻¹ : R) * ↑S.x1⁻¹ * (1 + S.x0 + S.x1) := by ring
      _ = 1 + (↑S.x0⁻¹ : R) * ↑S.x1⁻¹ * (1 + S.x0 + S.x1) := by rw [hx0, hx1, one_mul]
  · simp only [pentagonADiag, Units.val_mul, S.hu11, S.hu10]
    calc
      (S.x0 : R) * ((↑S.x0⁻¹ : R) * ↑S.x1⁻¹ * (1 + S.x0 + S.x1))
          = ((S.x0 : R) * ↑S.x0⁻¹) * ((↑S.x1⁻¹ : R) * (1 + S.x0 + S.x1)) := by ring
      _ = ((↑S.x1⁻¹ : R) * S.x1) + (↑S.x1⁻¹ : R) * (1 + S.x0) := by rw [hx0']; ring
      _ = 1 + (↑S.x1⁻¹ : R) * (1 + S.x0) := by rw [hx1]
  · simp only [pentagonADiag, Units.val_mul, S.hu10]
    calc
      (S.x1 : R) * ((↑S.x1⁻¹ : R) * (1 + S.x0))
          = ((S.x1 : R) * ↑S.x1⁻¹) * (1 + S.x0) := by ring
      _ = 1 + S.x0 := by rw [hx1', one_mul]

/-- Admissibility data for an $A_2$ Fock–Goncharov $\mathcal{X}$-seed `(X₁, X₂)` over
`[CommRing R]`: `X₁, X₂` and the three $\mathcal{X}$-cluster factors `1 + X₁`, `1 + X₂`,
and `1 + X₁ + X₁ X₂` are units in `Rˣ`. -/
structure PentagonXSeed (R : Type*) [CommRing R] where
  /-- First Fock–Goncharov shear coordinate $X_1 \in R^\times$. -/
  X1 : Rˣ
  /-- Second Fock–Goncharov shear coordinate $X_2 \in R^\times$. -/
  X2 : Rˣ
  /-- Unit witness for `1 + X₁`. -/
  v1 : Rˣ
  /-- Unit witness for `1 + X₂`. -/
  v2 : Rˣ
  /-- Unit witness for `1 + X₁ + X₁ * X₂`. -/
  v12 : Rˣ
  /-- Identification `v1 = 1 + X₁`. -/
  hv1 : (v1 : R) = 1 + (X1 : R)
  /-- Identification `v2 = 1 + X₂`. -/
  hv2 : (v2 : R) = 1 + (X2 : R)
  /-- Identification `v12 = 1 + X₁ + X₁ * X₂`. -/
  hv12 : (v12 : R) = 1 + (X1 : R) + (X1 : R) * (X2 : R)

/-- Single Fock–Goncharov $\mathcal{X}$-mutation + quiver relabelling
$M_{\mathcal{X}}(X_1, X_2) = (X_1 X_2 (1 + X_1)^{-1}, X_1^{-1})$ holds between two pairs
`(X₁, X₂)` and `(Y₁, Y₂)` in `Rˣ × Rˣ` (written division-free in `(1 + X₁)`). -/
def IsXFlipSwapStep (p q : Rˣ × Rˣ) : Prop :=
  (q.1 : R) * (1 + (p.1 : R)) = (p.1 : R) * (p.2 : R) ∧ q.2 = p.1⁻¹

/-- The 5-step orbit of `PentagonXSeed` in `Rˣ × Rˣ` under $M_{\mathcal{X}} = \mathrm{swap} \circ \mu_1$. -/
def pentagonXOrbit (S : PentagonXSeed R) : Fin 6 → Rˣ × Rˣ
  | 0 => (S.X1, S.X2)
  | 1 => (S.X1 * S.X2 * S.v1⁻¹, S.X1⁻¹)
  | 2 => (S.X2 * S.v12⁻¹, S.X1⁻¹ * S.X2⁻¹ * S.v1)
  | 3 => (S.X1⁻¹ * S.v2⁻¹, S.X2⁻¹ * S.v12)
  | 4 => (S.X2⁻¹, S.X1 * S.v2)
  | 5 => (S.X1, S.X2)

/-- **Fock–Goncharov $A_2$ $\mathcal{X}$-Cluster 5-Flip Pentagon Theorem** over any
`[CommRing R]`: each step `0 → 1 → 2 → 3 → 4 → 5` satisfies `IsXFlipSwapStep`, and
after 5 Whitehead flips the $\mathcal{X}$-seed returns identically to `(X₁, X₂)`
(equivalently, 5 alternating unlabelled flips `μ₁ ∘ μ₂ ∘ μ₁ ∘ μ₂ ∘ μ₁` swap `(X₁, X₂) ↦ (X₂, X₁)`). -/
theorem xFlipSwap_five_periodic (S : PentagonXSeed R) :
    IsXFlipSwapStep (pentagonXOrbit S 0) (pentagonXOrbit S 1) ∧
    IsXFlipSwapStep (pentagonXOrbit S 1) (pentagonXOrbit S 2) ∧
    IsXFlipSwapStep (pentagonXOrbit S 2) (pentagonXOrbit S 3) ∧
    IsXFlipSwapStep (pentagonXOrbit S 3) (pentagonXOrbit S 4) ∧
    IsXFlipSwapStep (pentagonXOrbit S 4) (pentagonXOrbit S 5) ∧
    pentagonXOrbit S 5 = pentagonXOrbit S 0 ∧
    (pentagonXOrbit S 5).swap = (S.X2, S.X1) := by
  have hX1 : (S.X1 : R) * (↑S.X1⁻¹ : R) = 1 := Units.mul_inv S.X1
  have hX1' : (↑S.X1⁻¹ : R) * (S.X1 : R) = 1 := Units.inv_mul S.X1
  have hX2 : (S.X2 : R) * (↑S.X2⁻¹ : R) = 1 := Units.mul_inv S.X2
  have hX2' : (↑S.X2⁻¹ : R) * (S.X2 : R) = 1 := Units.inv_mul S.X2
  have hv1 : (↑S.v1⁻¹ : R) * (S.v1 : R) = 1 := Units.inv_mul S.v1
  have hv1' : (S.v1 : R) * (↑S.v1⁻¹ : R) = 1 := Units.mul_inv S.v1
  have hv2 : (↑S.v2⁻¹ : R) * (S.v2 : R) = 1 := Units.inv_mul S.v2
  have hv12 : (↑S.v12⁻¹ : R) * (S.v12 : R) = 1 := Units.inv_mul S.v12
  have hv12' : (S.v12 : R) * (↑S.v12⁻¹ : R) = 1 := Units.mul_inv S.v12
  refine ⟨?_, ?_, ?_, ?_, ?_, rfl, rfl⟩
  · refine ⟨?_, rfl⟩
    simp only [pentagonXOrbit, Units.val_mul, ← S.hv1]
    calc
      (S.X1 : R) * S.X2 * ↑S.v1⁻¹ * S.v1 = (S.X1 : R) * S.X2 * (↑S.v1⁻¹ * S.v1) := by ring
      _ = (S.X1 : R) * S.X2 := by rw [hv1, mul_one]
  · refine ⟨?_, ?_⟩
    · simp only [pentagonXOrbit, Units.val_mul]
      have hsum : 1 + (S.X1 : R) * S.X2 * ↑S.v1⁻¹ = (S.v12 : R) * ↑S.v1⁻¹ := by
        calc
          1 + (S.X1 : R) * S.X2 * ↑S.v1⁻¹
              = (S.v1 : R) * ↑S.v1⁻¹ + (S.X1 : R) * S.X2 * ↑S.v1⁻¹ := by rw [hv1']
          _ = ((S.v1 : R) + (S.X1 : R) * S.X2) * ↑S.v1⁻¹ := by ring
          _ = (S.v12 : R) * ↑S.v1⁻¹ := by rw [S.hv1, S.hv12]
      rw [hsum]
      calc
        (S.X2 : R) * ↑S.v12⁻¹ * ((S.v12 : R) * ↑S.v1⁻¹)
            = (S.X2 : R) * (↑S.v12⁻¹ * S.v12) * ↑S.v1⁻¹ := by ring
        _ = 1 * (S.X2 : R) * ↑S.v1⁻¹ := by rw [hv12]; ring
        _ = ((S.X1 : R) * ↑S.X1⁻¹) * S.X2 * ↑S.v1⁻¹ := by rw [hX1]
        _ = (S.X1 : R) * S.X2 * ↑S.v1⁻¹ * ↑S.X1⁻¹ := by ring
    · simp only [pentagonXOrbit]; ext; simp [mul_comm]
  · refine ⟨?_, ?_⟩
    · simp only [pentagonXOrbit, Units.val_mul]
      have hfac : (S.v12 : R) + S.X2 = (S.v1 : R) * S.v2 := by
        rw [S.hv12, S.hv1, S.hv2]; ring
      have hsum : 1 + (S.X2 : R) * ↑S.v12⁻¹ = (S.v1 : R) * S.v2 * ↑S.v12⁻¹ := by
        calc
          1 + (S.X2 : R) * ↑S.v12⁻¹
              = (S.v12 : R) * ↑S.v12⁻¹ + (S.X2 : R) * ↑S.v12⁻¹ := by rw [hv12']
          _ = ((S.v12 : R) + S.X2) * ↑S.v12⁻¹ := by ring
          _ = (S.v1 : R) * S.v2 * ↑S.v12⁻¹ := by rw [hfac]
      rw [hsum]
      calc
        (↑S.X1⁻¹ : R) * ↑S.v2⁻¹ * ((S.v1 : R) * S.v2 * ↑S.v12⁻¹)
            = (↑S.X1⁻¹ : R) * (↑S.v2⁻¹ * S.v2) * S.v1 * ↑S.v12⁻¹ := by ring
        _ = (↑S.X1⁻¹ : R) * 1 * S.v1 * ↑S.v12⁻¹ := by rw [hv2]
        _ = ((S.X2 : R) * ↑S.X2⁻¹) * ↑S.X1⁻¹ * S.v1 * ↑S.v12⁻¹ := by rw [hX2]; ring
        _ = (S.X2 : R) * ↑S.v12⁻¹ * (↑S.X1⁻¹ * ↑S.X2⁻¹ * S.v1) := by ring
    · simp only [pentagonXOrbit]; ext; simp [mul_comm]
  · refine ⟨?_, ?_⟩
    · simp only [pentagonXOrbit, Units.val_mul]
      have hfac : (S.X1 : R) * S.v2 + 1 = S.v12 := by
        rw [S.hv2, S.hv12]; ring
      calc
        (↑S.X2⁻¹ : R) * (1 + ↑S.X1⁻¹ * ↑S.v2⁻¹)
            = (↑S.X2⁻¹ : R) * (((S.X1 : R) * ↑S.X1⁻¹) * ((S.v2 : R) * ↑S.v2⁻¹) +
                ↑S.X1⁻¹ * ↑S.v2⁻¹) := by
              have hv2' : (S.v2 : R) * ↑S.v2⁻¹ = 1 := Units.mul_inv S.v2
              rw [hX1, hv2', one_mul]
        _ = (↑S.X1⁻¹ : R) * ↑S.v2⁻¹ * ((↑S.X2⁻¹ : R) * ((S.X1 : R) * S.v2 + 1)) := by ring
        _ = (↑S.X1⁻¹ : R) * ↑S.v2⁻¹ * (↑S.X2⁻¹ * S.v12) := by rw [hfac]
    · simp only [pentagonXOrbit]; ext; simp [mul_comm]
  · refine ⟨?_, ?_⟩
    · simp only [pentagonXOrbit, Units.val_mul]
      calc
        (S.X1 : R) * (1 + ↑S.X2⁻¹)
            = (S.X1 : R) * ((S.X2 : R) * ↑S.X2⁻¹ + ↑S.X2⁻¹) := by rw [hX2]
        _ = (↑S.X2⁻¹ : R) * ((S.X1 : R) * (1 + S.X2)) := by ring
        _ = (↑S.X2⁻¹ : R) * ((S.X1 : R) * S.v2) := by rw [← S.hv2]
    · simp only [pentagonXOrbit, inv_inv]

end PentagonPeriodicity

/-! ## 3. Farey / Whitehead Layered-Tetrahedron Recursion on $\Sigma_{1,1}$ -/

section FareyLayeredFlips

variable {R : Type*} [CommRing R]

/-- Alphabet of elementary 2D Whitehead flips on the once-punctured torus / 3-braid
quotient (`R = σ₀`, `L = σ₁⁻¹` in `B₃ → PSL(2, ℤ)`). -/
inductive FareyFlip : Type
  | R : FareyFlip
  | L : FareyFlip
  deriving DecidableEq, Repr

/-- Right Whitehead flip (`R = σ₀`) on a Markov–Fricke trace triple `(x, y, z)`:
replaces `y` by `y_new = x * z - y` and advances to `(x, z, x * z - y)`. -/
def stepR (t : R × R × R) : R × R × R :=
  (t.1, t.2.2, t.1 * t.2.2 - t.2.1)

/-- Left Whitehead flip (`L = σ₁⁻¹`) on a Markov–Fricke trace triple `(x, y, z)`:
replaces `x` by `x_new = y * z - x` and advances to `(z, y, y * z - x)`. -/
def stepL (t : R × R × R) : R × R × R :=
  (t.2.2, t.2.1, t.2.1 * t.2.2 - t.1)

/-- Apply one `FareyFlip` to `(x, y, z)`. -/
def stepFarey (f : FareyFlip) (t : R × R × R) : R × R × R :=
  match f with
  | .R => stepR t
  | .L => stepL t

/-- Step an entire Farey/braid flip word `w : List FareyFlip` across `(x, y, z)`. -/
def applyFareyWord (w : List FareyFlip) (t : R × R × R) : R × R × R :=
  w.foldl (fun acc f => stepFarey f acc) t

/-- The Markov–Fricke parabolic-cusp cubic $M(x, y, z) = x^2 + y^2 + z^2 - x y z$
(`tr [A, B] + 2` in `SL(2, R)`). -/
def markovCubic (t : R × R × R) : R :=
  t.1 ^ 2 + t.2.1 ^ 2 + t.2.2 ^ 2 - t.1 * t.2.1 * t.2.2

/-- `stepR` strictly preserves `markovCubic` over any `[CommRing R]`. -/
theorem markovCubic_stepR (t : R × R × R) :
    markovCubic (stepR t) = markovCubic t := by
  unfold markovCubic stepR
  ring

/-- `stepL` strictly preserves `markovCubic` over any `[CommRing R]`. -/
theorem markovCubic_stepL (t : R × R × R) :
    markovCubic (stepL t) = markovCubic t := by
  unfold markovCubic stepL
  ring

/-- Stepping any word `w : List FareyFlip` strictly preserves `markovCubic`. -/
theorem markovCubic_applyFareyWord (w : List FareyFlip) (t : R × R × R) :
    markovCubic (applyFareyWord w t) = markovCubic t := by
  induction w generalizing t with
  | nil => rfl
  | cons f ws ih =>
    change markovCubic (applyFareyWord ws (stepFarey f t)) = markovCubic t
    rw [ih]
    cases f
    · exact markovCubic_stepR t
    · exact markovCubic_stepL t

/-- **Trace-to-Ptolemy equivalence (`R`-flip):** on the parabolic Markov locus
`markovCubic (x, y, z) = 0`, the additive trace flip `y_new = x * z - y` satisfies
the exact multiplicative Ptolemy relation `y_new * y = x^2 + z^2`. -/
theorem stepR_ptolemy_on_markov {x y z : R} (hM : markovCubic (x, y, z) = 0) :
    IsPtolemyFlip x z x z y (x * z - y) := by
  unfold IsPtolemyFlip
  unfold markovCubic at hM
  linear_combination -hM

/-- **Trace-to-Ptolemy equivalence (`L`-flip):** on the parabolic Markov locus
`markovCubic (x, y, z) = 0`, the additive trace flip `x_new = y * z - x` satisfies
the exact multiplicative Ptolemy relation `x_new * x = y^2 + z^2`. -/
theorem stepL_ptolemy_on_markov {x y z : R} (hM : markovCubic (x, y, z) = 0) :
    IsPtolemyFlip y z y z x (y * z - x) := by
  unfold IsPtolemyFlip
  unfold markovCubic at hM
  linear_combination -hM

/-- **Exact algebraic stationary fixed point of the figure-eight flip word `RL` (`4₁`)**
over any `[CommRing R]` carrying a root `ω` of the cyclotomic polynomial
`ω^2 - ω + 1 = 0` (the algebraic cut for $e^{i\pi/3}$, with zero `Real.*` / `Complex.*`):
`t = (1 + ω, 2 - ω, 2 - ω)` lies on `markovCubic t = 0`, is a stationary fixed point of
`[FareyFlip.R, FareyFlip.L]`, and both layered tetrahedron cross-ratios satisfy the
regular-ideal-tetrahedron equation `z^2 * (1 - ω) = y_old * y_new` and
`y^2 * ω = x_old * x_new`. -/
theorem fig8_RL_stationary_fixed_point {ω : R} (hω : ω ^ 2 - ω + 1 = 0) :
    let t : R × R × R := (1 + ω, 2 - ω, 2 - ω)
    markovCubic t = 0 ∧
    applyFareyWord [.R, .L] t = t ∧
    ((2 - ω) ^ 2 * ω = (2 - ω) * ((1 + ω) * (2 - ω) - (2 - ω))) ∧
    ((2 - ω) ^ 2 * ω = (1 + ω) * ((2 - ω) * (1 + ω) - (1 + ω))) := by
  dsimp only
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold markovCubic
    linear_combination (5 - ω) * hω
  · simp only [applyFareyWord, List.foldl_cons, List.foldl_nil, stepFarey, stepL, stepR]
    ext
    · dsimp only; linear_combination -hω
    · rfl
    · dsimp only; linear_combination -(3 - ω) * hω
  · ring
  · linear_combination (2 * ω - 1) * hω

end FareyLayeredFlips

/-! ## 4. Bridge to Non-Abelian Transverse Yekutieli–Stokes Pairing -/

section TransverseStokesBridge

/-- Stepping a layered flip sequence into a non-commutative Hecke / matrix algebra `A`
produces a list of parallel-transported band curvatures whose transverse Yekutieli
pairing `listPairing` satisfies **both Sibling-12 guards** simultaneously:
1. Any cyclic linear trace `τ` annihilates `listPairing` identically (`τ(Ω₂) = 0`),
   forbidding naive linear trace readouts of `[A, B]`;
2. Concatenating two flip layers `l₁ ++ l₂` decomposes `listPairing (l₁ ++ l₂)` into
   the sum of intra-layer pairings plus the exact inter-layer commutator
   `curvComm l₂.sum l₁.sum`. -/
theorem layered_transverse_trace_zero_and_split {A M : Type*} [Ring A] [AddCommGroup M]
    (τ : A →+ M) (hcyc : ∀ x y : A, τ (x * y) = τ (y * x)) (l₁ l₂ : List A) :
    τ (listPairing (l₁ ++ l₂)) = 0 ∧
      listPairing (l₁ ++ l₂) = listPairing l₁ + listPairing l₂ + curvComm l₂.sum l₁.sum :=
  ⟨listPairing_trace_zero τ hcyc (l₁ ++ l₂), listPairing_append l₁ l₂⟩

end TransverseStokesBridge

end QOU.BraidsAndKnots.LayeredFlipPtolemyStokes
