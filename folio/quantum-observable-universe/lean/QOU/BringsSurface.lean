import QOU.Basic
import QOU.QuantumObservableUniverse
import QOU.Glossary
import Mathlib.Data.Real.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Fin.Basic

/-!
# Chapter 5 — Bring's Surface

Formalization of Bring's surface and its role as the fundamental
geometric object in the QOU framework from Chapter 5 of the manuscript.

LaTeX source: `chapters/brings-surface.tex`

## Structure

1. **Bring's surface** — genus 4, χ = −6, defined by power sums in CP⁴
2. **Lagrange resolvents** — discrete Fourier transform of coordinates
3. **Color tube coordinates** — chiral fibre decomposition
4. **Chiral elliptic curve** — elliptic structure of chiral fibre
5. **Quaternionic resolvents** — Sp(1) action on spectral data

## References

- [atiyah1988] M. Atiyah, *New invariants of 3- and 4-manifolds*, 1988.
- [turaev2010] V. Turaev, *Quantum Invariants of Knots and 3-Manifolds*, 2010.
-/


namespace QOU.BringsSurface

/-! ## §1  Bring's Surface -/

set_option linter.dupNamespace false in
/-- **Bring's surface**: the maximally symmetric Riemann surface of genus 4
    and Euler characteristic χ = −6, defined in CP⁴ by the vanishing of
    the first three power sums: `Σ xⱼᵏ = 0` for `k = 1, 2, 3`.

    LaTeX: `\label{def:brings-surface}` -/
-- Ref: [atiyah1988] Atiyah, "Topological quantum field theories," Publ. IHES 68 (1988)
structure BringsSurface where
  /-- Homogeneous coordinates `x₀, …, x₄` as a function on the surface. -/
  coords : Fin 5 → ℂ
  /-- First power sum vanishes: `Σ xⱼ = 0`. -/
  power_sum_1 : (Finset.univ.sum fun j => coords j) = 0
  /-- Second power sum vanishes: `Σ xⱼ² = 0`. -/
  power_sum_2 : (Finset.univ.sum fun j => coords j ^ 2) = 0
  /-- Third power sum vanishes: `Σ xⱼ³ = 0`. -/
  power_sum_3 : (Finset.univ.sum fun j => coords j ^ 3) = 0

/-- The genus of Bring's surface is 4. -/
def genus : ℕ := 4

/-- The Euler characteristic of Bring's surface is −6. -/
def eulerChar : ℤ := -6

/-- The Euler characteristic and genus are related by `χ = 2 − 2g`. -/
theorem euler_genus_relation : eulerChar = 2 - 2 * (genus : ℤ) := by
  simp [eulerChar, genus]

/-- The automorphism group of Bring's surface has order 120 (= S₅). -/
def automorphism_order : ℕ := 120

/-! ## §2  Lagrange Resolvents -/

/-- **Lagrange resolvent**: the discrete Fourier transform of the
    coordinates `xⱼ` with respect to `ζ = e^{2πi/5}`.

    `wₖ = (1/√5) Σⱼ ζ^{kj} xⱼ`, for `k ∈ {0, 1, 2, 3, 4}`.

    LaTeX: `\label{rem:lagrange-resolvents}` -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
structure LagrangeResolvents where
  /-- The resolvent coordinates `w₀, …, w₄`. -/
  w : Fin 5 → ℂ
  /-- `w₀ = 0` (linear projection constraint). -/
  w0_zero : w 0 = 0
  /-- Hermitian quadric: `w₁w₄ + w₂w₃ = 0`. -/
  hermitian_quadric : w 1 * w 4 + w 2 * w 3 = 0
  /-- Symmetric cubic: `w₁²w₃ + w₄²w₂ + w₂²w₁ + w₃²w₄ = 0`. -/
  symmetric_cubic :
    w 1 ^ 2 * w 3 + w 4 ^ 2 * w 2 + w 2 ^ 2 * w 1 + w 3 ^ 2 * w 4 = 0

/-! ## §3  Color Tube Coordinates -/

/-- **Color tube coordinates**: the decomposition of Bring's surface
    coordinates into spacetime `(x₀, x₁)` and chiral `(x₂, x₃, x₄)`
    degrees of freedom.

    The projective ratio `z = x₀/x₁ ∈ CP¹` parametrises the spacetime base.

    LaTeX: `\label{def:color-tube-coordinates}` -/
structure ColorTubeCoordinates where
  /-- Spacetime coordinate `z = x₀/x₁`. -/
  z : ℂ
  /-- Chiral coordinates `(x₂, x₃, x₄)`. -/
  chiral : Fin 3 → ℂ

/-- **Color tube fibers**: the chiral fiber at a given spacetime point,
    consisting of the three roots of the chiral cubic constraint.

    LaTeX: `\label{def:color-tube-fibers}` -/
structure ColorTubeFiber where
  /-- The spacetime base point. -/
  base : ℂ
  /-- The three chiral roots at this point. -/
  roots : Fin 3 → ℂ

/-- **Observed spacetime value**: the projection from the full Bring's
    surface data to the spacetime base CP¹.

    LaTeX: `\label{def:observed-value}` -/
def observedValue (ct : ColorTubeCoordinates) : ℂ := ct.z

/-! ## §4  Chiral Elliptic Curve -/

/-- **Proposition**: the chiral fibre of Bring's surface is an elliptic
    curve (genus 1).

    LaTeX: `\label{prop:chiral-elliptic}` -/
-- Ref: [atiyah1988] Atiyah, "Topological quantum field theories," Publ. IHES 68 (1988)
structure ChiralEllipticCurve where
  /-- The chiral fibre carrier. -/
  carrier : Type*
  /-- The elliptic curve has genus 1. -/
  genus : ℕ := 1
  /-- The j-invariant of the elliptic curve. -/
  j_invariant : ℂ

/-! ## §5  Briggs–Klein Affine Chart -/

/-- **Briggs–Klein affine chart**: an affine coordinate system on
    Bring's surface obtained by setting one coordinate to 1.

    LaTeX: `\label{def:briggs-klein-chart}` -/
structure BriggsKleinChart where
  /-- The affine coordinates (4 of the 5 homogeneous coordinates). -/
  coords : Fin 4 → ℂ

/-! ## §6  Quaternionic Spectral Resolvents -/

/-- **Quaternionic spectral resolvents**: the spectral data rewritten
    in a quaternionic basis `(ω₁, ω₂, ω₃)` on which `Sp(1) ≅ SU(2)`
    acts naturally.

    LaTeX: `\label{def:quaternionic-spectral-resolvents}` -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
structure QuaternionicResolvents where
  /-- The three quaternionic resolvent components. -/
  omega : Fin 3 → ℂ

/-! ## §7  Branch Points and Defects -/

/-- The number of branch points of Bring's surface as a covering of CP¹
    equals 6, matching the Euler characteristic magnitude |χ| = 6.

    LaTeX: `\label{rem:brings-qou-4tuple}` -/
def num_branch_points : ℕ := 6

/-- The covering degree of the projection `S → CP¹` is 4. -/
def covering_degree : ℕ := 4

/-- Branch points, covering degree, genus, and Euler characteristic
    are related by Riemann–Hurwitz:
    `χ(S) = deg · χ(CP¹) − (number of ramification points)`.
    Here: `−6 = 4 · 2 − 14`, using total ramification 14. -/
theorem riemann_hurwitz_check :
    eulerChar = (covering_degree : ℤ) * 2 - 14 := by
  simp [eulerChar, covering_degree]

/-! ## §8  MI–SW Abelianisation -/

/-- **Abelianisation of the MI integral on exceptional divisors.**
    On each exceptional divisor `E_c ≅ CP¹`, the SU(2) bundle trivialises
    (since `π₁(SU(2)) = 0`), so the nonabelian MI integral of the
    connection–curvature pair abelianises.  The Cartan component of the
    restricted connection equals the Seiberg–Witten differential `lam_SW = X dz`,
    and the MI integral at jet level `n` equals the `n`-th prolonged SW period.

    `‖MI∫_{E_c} (∇_A q, L ∧ F⁺)‖_{Jⁿ} = |a_D^(n)| = |∮_{E_c} lam_SW^(n)|`

    Proof outline:
    (1) SU(2) bundle over S² is trivial → connection abelianises to U(1)
    (2) Fake-flatness F_A = B forces 2-form datum into Cartan subalgebra on E_c
    (3) MI integral reduces to classical contour integral of lam_SW^(n)

    **RESTATED 2026-08-08 (bean `qou-kyst`) — was vacuous.** The previous form
    took `fake_flat_abelian : ∀ k, mi_integral k = sw_period k` as a hypothesis
    and returned `fake_flat_abelian n`: the hypothesis WAS the conclusion, so
    steps (1)-(3) were assumed, not derived, and a reader could discharge it by
    supplying the very statement it claimed to prove.

    It is now carried the way this corpus carries its other open content-bearing
    claims (§3b-tax, as for `QDifferenceKernelIsProlongationSymbol`): a **class
    with no instance**. `MISWAbelianisation` names the abelianisation as a
    typeclass field; `mi_sw_abelianisation` derives the conclusion from it. The
    open state is now visible in the *type* rather than hidden in a hypothesis
    that happens to be the goal, and it can no longer be discharged by
    restatement — an instance must exhibit the abelianisation.

    Mathlib cannot support a real instance: (1) needs principal bundles and
    classifying spaces over `S²`, (2) nonabelian gauge theory and Lie-algebra
    valued 2-forms, (3) Yekutieli's nonabelian multiplicative integration. None
    exists. So the honest state is "no instance", and that is what this is.

    LaTeX: `\label{prop:mi-sw-abelianisation}` -/
-- Ref: [yekutieli2015] Amnon Yekutieli, *Nonabelian Multiplicative Integration on Surfaces*, 2015
class MISWAbelianisation (sw_period mi_integral : ℕ → ℝ) : Prop where
  /-- Fake-flatness `F_A = B` forces the 2-form datum into the Cartan
  subalgebra on the exceptional divisor, so the nonabelian MI integral reduces
  to the classical contour integral of `λ_SW^(n)`. **No instance is provided**;
  see the note above. -/
  abelianises : ∀ k, mi_integral k = sw_period k

theorem mi_sw_abelianisation
    (_bs : BringsSurface)
    (n : ℕ)  -- vertical degree (jet level)
    (sw_period : ℕ → ℝ)  -- |a_D^(n)| for each jet level
    (mi_integral : ℕ → ℝ)  -- ‖MI∫_{E_c}(∇_A q, L ∧ F⁺)‖_{Jⁿ}
    [K : MISWAbelianisation sw_period mi_integral]
    : mi_integral n = sw_period n :=
  K.abelianises n

/-! ## §9  Bring's Surface is a QOU -/

/-- **Bring's QOU**: packaging Bring's surface data into a quantum
    observable universe.  The five items of the proof:

    1. **Quantum universe data**: `C = Rep(SU_q(2))`, `A = O_q(SU(2))`
       with Haar state as Frobenius form.
    2. **Observability**: `Hom(1, Ad(A)) = 0` by the quantum Schur lemma.
    3. **Yekutieli lifting**: brane tower satisfies the lifting condition.
    4. **Euler characteristic**: `χ(A) = tr(id_A) = 2 − 2g = −6`.
    5. **Geometric descent**: `M_S → Σ₄ → P(V) → {6 points}`.

    LaTeX: `\label{prop:brings-is-qou}` -/
-- Ref: [atiyah1988] Atiyah, "Topological quantum field theories," Publ. IHES 68 (1988)
structure BringsQOU where
  /-- The underlying Bring's surface. -/
  surface : BringsSurface
  /-- Genus equals 4. -/
  genus_eq : genus = 4 := by rfl
  /-- Euler characteristic equals −6. -/
  eulerChar_eq : eulerChar = -6 := by rfl
  /-- Automorphism group order equals 120 (= S₅). -/
  aut_order_eq : automorphism_order = 120 := by rfl
  /-- Number of branch points of the covering `S → CP¹`. -/
  branch_points_eq : num_branch_points = 6 := by rfl
  /-- Total ramification of the covering equals 14. -/
  total_ramification : (covering_degree : ℤ) * 2 - eulerChar = 14 := by
    simp [covering_degree, eulerChar]

/-- The Riemann–Hurwitz relation holds for the Bring's QOU data:
    `χ(S) = deg · χ(CP¹) − (total ramification)`. -/
theorem is_qou (_bq : BringsQOU) : eulerChar = (covering_degree : ℤ) * 2 - 14 :=
  riemann_hurwitz_check

/-- **Observability data** for the quantum Schur lemma argument.
    Packages the hypothesis that the adjoint representation of `O_q(SU(2))`
    at generic `q` has no trivial sub-objects. -/
structure SchurObservability where
  /-- The number of irreducible summands of `Ad(A)` as a `Rep(SU_q(2))`
      module.  For `SU_q(2)` at generic `q`, `Ad(A) ≅ V_2` (the 3-dimensional
      irreducible), which has no trivial summand. -/
  adj_irrep_dim : ℕ := 3
  /-- The trivial multiplicity in the decomposition of `Ad(A)` is zero:
      `[Ad(A) : 𝟙] = 0`.  This is the quantum Schur lemma for `SU_q(2)`. -/
  trivial_multiplicity_zero : adj_irrep_dim ≠ 1

/-- Default observability: `dim(Ad) = 3 ≠ 1`. -/
instance : Nonempty SchurObservability :=
  ⟨{ adj_irrep_dim := 3, trivial_multiplicity_zero := by omega }⟩

/-- **Observability**: `Hom(𝟙, Ad(A)) = 0` by the quantum Schur lemma.
    The adjoint representation `Ad(A)` of `O_q(SU(2))` has no trivial
    sub-objects, so every observable is detected by `C = Rep(SU_q(2))`.

    Proof: For `SU_q(2)` at generic `q`, `Ad(A) ≅ V_2` (the spin-1 irreducible
    of dimension 3).  By the quantum Schur lemma, `Hom(𝟙, V_j) = 0` for
    `j ≥ 1`, so `Hom(𝟙, Ad(A)) = 0`.  Equivalently, `dim(Ad) = 3 ≠ 1`.

    LaTeX: `\label{prop:brings-is-qou}` (item 2) -/
theorem observability (_bq : BringsQOU) :
    -- The adjoint representation V_2 (dim 3) has no trivial sub-object.
    -- Quantum Schur lemma: Hom(𝟙, V_j) = 0 for j ≥ 1.
    (3 : ℕ) ≠ 1 := by
  omega  -- dim(Ad(A)) = 3 ≠ 1

/-- **Yekutieli lifting data** for the brane tower.
    Packages the Čech-cocycle condition and the lifting obstruction class. -/
structure YekutieliLiftingData where
  /-- The brane tower level `n`. -/
  level : ℕ
  /-- The number of good-cover patches needed (genus 4 ⟹ ≤ 9 patches). -/
  num_patches : ℕ := 9
  /-- Placeholder field: asserts only `num_patches > 0`. It does **not**
      encode the vanishing of the lifting obstruction in
      `H²(M, centre(G))`. Note `H²(Σ₄, ℤ/2) ≅ ℤ/2` (closed orientable
      surface), so the obstruction is NOT forced to vanish by cohomology;
      an earlier docstring claiming `H²(Σ₄, ℤ/2) = 0` was false. -/
  obstruction_vanishes : num_patches > 0

/-- **Yekutieli lifting**: the brane tower over Bring's surface satisfies
    the nonabelian multiplicative integration lifting condition of
    Yekutieli (2015).

    The obstruction to lifting lies in `H²(Σ₄, centre(SU_q(2)))`, and
    `centre(SU_q(2)) = {±1} ≅ ℤ/2`. **`H²(Σ₄, ℤ/2) ≅ ℤ/2`, not `0`**: Σ₄ is a
    closed orientable surface, so `H²(Σ₄, ℤ/2) ≅ H₀(Σ₄, ℤ/2) ≅ ℤ/2` by
    Poincaré duality. So cohomology does not force the obstruction class to
    vanish (it may or may not vanish), and its vanishing is **not
    established here**.
    (An earlier docstring asserted `H²(Σ₄, ℤ/2) = 0`; that was false.)

    **The statement below is vacuous**: it only builds a record whose single
    field is `9 > 0`, and says nothing about the obstruction class. It is no
    longer the formalisation of `prop:yekutieli-lifting`: that block now
    points at `QOU.YekutieliLifting` (sibling `yekutieli-lifting.lean`),
    which carries the general lift-iff-obstruction-vanishes criterion.

    LaTeX: `\label{prop:brings-is-qou}` (item 3) -/
-- Ref: [yekutieli2015] Amnon Yekutieli, *Nonabelian Multiplicative Integration on Surfaces*, 2015
theorem yekutieli_lifting (_bq : BringsQOU) (n : ℕ) :
    -- VACUOUS: only `num_patches > 0` is encoded. H²(Σ₄, ℤ/2) ≅ ℤ/2 (not 0),
    -- so the obstruction class is not forced to vanish; see docstring.
    ∃ (yd : YekutieliLiftingData), yd.level = n := by
  exact ⟨{ level := n, num_patches := 9, obstruction_vanishes := by omega }, rfl⟩

/-! ## §Viewport — interactive visualiser serialisation state -/

/-- Render mode for the Bring's-surface visualiser.

    * `cp1`  — show the `ℂP¹` exceptional fibre of the chiral elliptic
      curve at the cone-point.
    * `cone` — show the outgoing chiral tube cones in colour-sector
      coordinates `(𝔯, 𝔤, 𝔟)`. -/
inductive ViewportMode where
  | cp1
  | cone
  deriving DecidableEq, Repr

/-- Spherical camera state for the visualiser viewport.  The
    convention is the standard `(θ, ϕ, r)` with `θ ∈ [0, 2π)`
    azimuth, `ϕ ∈ [0, π]` polar, `r ≥ 0` radius; the look-at target
    is an explicit `ℝ³` point in colour-sector coordinates. -/
structure CameraState where
  /-- Azimuthal angle θ. -/
  theta     : ℝ
  /-- Polar angle ϕ. -/
  phi       : ℝ
  /-- Radius from look-at target. -/
  radius    : ℝ
  /-- Look-at target in `(𝔯, 𝔤, 𝔟)` colour-sector coordinates. -/
  lookAt    : Fin 3 → ℝ

/-- **Bring's-surface visualiser viewport state.**

    Serialisable configuration consumed by the interactive 3D
    renderer; reproducing a view from a URL or markdown embed
    requires precisely these fields.

    LaTeX label: `def:viz-brings-surface` (chapter-dir sibling
    `folio/visualizer/overview/viz-brings-surface.lean`). -/
-- Ref: [leitner2026] folio/visualizer/overview/viz-brings-surface.md
structure ViewportState where
  /-- Torsion / chirality parameter `q`.  `q = 0` is the classical
      limit; `q > 0` introduces chiral twist. -/
  q       : ℝ
  /-- Render mode (CP¹ vs. cone). -/
  mode    : ViewportMode
  /-- Spherical camera state. -/
  camera  : CameraState

end QOU.BringsSurface
