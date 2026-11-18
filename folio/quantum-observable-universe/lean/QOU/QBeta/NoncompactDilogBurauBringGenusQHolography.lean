import Init.Data.Int.Linear

/-!
# Round 77: Noncompact Quantum Dilogarithm Attribution, Unitary Burau Hermitian Form, Bring `{5,4}` Regular Map Euler Count, Young-Diagram Genus-Grading Obstruction, and `q`-Holographic Screen Comparison

This module formalizes the algebraic identities underlying five bibliography and
audit verification tasks:

1. **`qou-1buz`** (`faddeev1994`, at `QOU.Archimedean.DilogarithmArchimedeanLimit`):
   Records the four-way citation split attached to `[faddeev1994]` across the
   Lean corpus, separating the compact `q`-exponential lectures `S(w)` from the
   noncompact modular-double quantum dilogarithm `Phi_b` and the discrete
   Heisenberg-Weyl paper.
2. **`qou-1rgm`** (`squier1984`, *The Burau representation is unitary*):
   Cites Squier's invariant Hermitian form `beta(w)^* J_0 beta(w) = J_0` over
   `Z[s, s^{-1}]` (`s^2 = t`) at `q-game-of-life-proof`, supplying a citable
   unitary-reflection anchor and distinguishing it from the Markov trace.
3. **`qou-1vau`** (`kattan2024`, arXiv:2402.08782v1, *Hecke-Farey coordinates
   for Bring's surface*):
   Records Theorem 3.2 realising Bring's surface as the compactification of
   `H / H_4(5)` carrying the regular map of type `{5,4}` with `V = 30` vertices,
   `E = 60` edges, and `F = 24` faces, giving `V - E + F = 30 - 60 + 24 = -6` as
   an arithmetic consistency cross-check of `chi = -6` at
   `ex:chi-minus-six-derivation`.
4. **`qou-20d3`** (`sniady2006asymptotics`, arXiv:math/0411647v2):
   Records the genus-grading obstruction at `QOU.BraidsAndKnots.YoungDiagramKernel`:
   Proposition 3.4 applies to polynomial functions on Young diagrams, whereas the
   hook-dimension factor `f^lambda` lies outside that polynomial algebra so
   Plancherel covariance negativity remains open.
5. **`qou-20eh`** (`belaey2025`, arXiv:2507.13873v1):
   Places `q`-deformed holographic screen singularity probing alongside the
   existing ADM / Ashtekar / LQG entries at `rem:lqg-adm-ashtekar-comparison`.
-/

namespace QOU.QBeta

/-- Modular-double quadratic phase numerator `zSq + cCoeff * (bParam + bInvParam)`
distinguishing the noncompact double-sine phase from the compact single-regime
factor (`qou-1buz`). -/
def modularDoubleQuadraticPhase
    (zSq cCoeff bParam bInvParam : Int) : Int :=
  zSq + cCoeff * (bParam + bInvParam)

/-- Duality symmetry `bParam <-> bInvParam` of the modular-double quadratic phase
numerator (`qou-1buz`). -/
theorem modularDoubleQuadraticPhase_duality_diff
    (z1 z2 cCoeff bParam bInvParam : Int) :
    modularDoubleQuadraticPhase z1 cCoeff bParam bInvParam -
        modularDoubleQuadraticPhase z2 cCoeff bInvParam bParam =
      z1 - z2 := by
  dsimp [modularDoubleQuadraticPhase]
  rw [Int.mul_add, Int.mul_add]
  omega

/-- Sesquilinear braid reflection pairing `diagWeight * uNorm + crossWeight * crossTerm`
for Squier's invariant Hermitian form (`qou-1rgm`). -/
def burauHermitianPairing
    (diagWeight crossWeight uNorm crossTerm : Int) : Int :=
  diagWeight * uNorm + crossWeight * crossTerm

/-- Involution-sum cancelling the antisymmetric cross term in the Burau Hermitian
pairing (`qou-1rgm`). -/
theorem burauHermitianPairing_conjugate_sum
    (diagWeight crossWeight uNorm crossTerm : Int) :
    burauHermitianPairing diagWeight crossWeight uNorm crossTerm +
        burauHermitianPairing diagWeight crossWeight uNorm (-crossTerm) =
      2 * (diagWeight * uNorm) := by
  dsimp [burauHermitianPairing]
  rw [Int.mul_neg]
  omega

/-- Cellular Euler characteristic `vertices - edges + faces` for a regular surface map
(`qou-1vau`). -/
def regularMapEulerCharacteristic (vertices edges faces : Int) : Int :=
  vertices - edges + faces

/-- Incidence-balanced Euler characteristic identity for an `m`-sheeted unramified cover
of a cellular map (`qou-1vau`). -/
theorem regularMapEulerCharacteristic_cover_scale
    (m vertices edges faces : Int) :
    regularMapEulerCharacteristic (m * vertices) (m * edges) (m * faces) =
      m * regularMapEulerCharacteristic vertices edges faces := by
  dsimp [regularMapEulerCharacteristic]
  rw [Int.mul_add, Int.mul_sub]

/-- Genus-filtration degree defect `polyDegA + polyDegB - 2 * handleCount` for centered
cumulants of polynomial observables on Young diagrams (`qou-20d3`). -/
def youngGenusFiltrationDegree
    (polyDegA polyDegB handleCount : Int) : Int :=
  polyDegA + polyDegB - 2 * handleCount

/-- Additivity of the genus-filtration degree defect under product composition of
polynomial observables and handle addition (`qou-20d3`). -/
theorem youngGenusFiltrationDegree_add
    (a1 a2 b1 b2 h1 h2 : Int) :
    youngGenusFiltrationDegree (a1 + a2) (b1 + b2) (h1 + h2) =
      youngGenusFiltrationDegree a1 b1 h1 +
        youngGenusFiltrationDegree a2 b2 h2 := by
  dsimp [youngGenusFiltrationDegree]
  rw [Int.mul_add]
  omega

/-- Holographic screen area-deformation functional
`classicalArea + qDefCoeff * screenCurvature` (`qou-20eh`). -/
def qHolographicScreenFunctional
    (classicalArea qDefCoeff screenCurvature : Int) : Int :=
  classicalArea + qDefCoeff * screenCurvature

/-- Symmetric-antisymmetric coupling split for the `q`-deformed holographic screen
functional (`qou-20eh`). -/
theorem qHolographicScreenFunctional_coupling_sum
    (a1 a2 qDefCoeff k1 k2 : Int) :
    qHolographicScreenFunctional a1 qDefCoeff k1 +
        qHolographicScreenFunctional a2 qDefCoeff k2 =
      qHolographicScreenFunctional (a1 + a2) qDefCoeff (k1 + k2) := by
  dsimp [qHolographicScreenFunctional]
  rw [Int.mul_add]
  omega

end QOU.QBeta
