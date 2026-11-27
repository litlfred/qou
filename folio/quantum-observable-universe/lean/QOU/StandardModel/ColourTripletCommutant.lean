import QOU.StandardModel.OctonionCubeRootPhase

/-!
# QOU.StandardModel.ColourTripletCommutant — the octonion triple has no room for flavour

Bean `qou-x08k` (flavour fundamental `W` from the aether), follow-up to
`OctonionCubeRootPhase`: is the octonionic cube-root phase the **flavour** phase?

## Results (base ring `ℚ`, exact linear algebra)

* `D₁_isDer`, `S₁`, `T₁_apply` — a third explicit element of the colour stabiliser
  `𝔰𝔲(3) ⊂ Der(𝕆)` of `e₁`, beside `S₀, S₄` from `OctonionColourTripletComplexType`.
* `commutant_matrix` — **the commutant of colour is `ℚ[J]`.**  A `6 × 6` rational matrix that
  commutes with the three colour generators `T₀, T₁, T₄` is `a·1 + b·J6`.
* `commutant_end` — the same statement for linear endomorphisms, against the actual
  `su3ToEndTriplet` images.
* `commutant_commutative` — any two operators commuting with colour commute with each other.
  So a **non-abelian** flavour algebra (in particular `𝔰𝔲(3)_f`) cannot act on the octonionic
  colour triple commuting with colour.
* `no_cubeRoot_phase_in_commutant` — over `ℚ` the commutant contains no nontrivial cube root of
  unity at all (combines `commutant_end` with `colourTriple_no_rational_cubeRoot_phase`).

## Answer to the question

The phase `Ω = ½(√3·J − 1)` of `OctonionCubeRootPhase` lies in the commutant, so it is a
function of `J`, i.e. of **colour's own** complex structure: it is the centre (`N`-ality) of
colour `SU(3)`, not of a second group.  A flavour `SU(3)` commuting with colour cannot live on
the same six-dimensional carrier, since the commutant there is the commutative field `ℚ(J)`.
So, **on this carrier, the octonion phase is the colour phase, and flavour needs a different
carrier** (a tensor factor or another fibre, i.e. the multi-fibre route).  What the two share is
only the abstract `ℤ/3` grading forced by any degree-3 volume form
(`FlavourCentralPhase.phase_pow_of_volume`), not an operator.

Scope: commuting with colour is the standard requirement that flavour and colour be
independent symmetries; a flavour action that does not commute with colour is not excluded here.
-/

namespace QOU.StandardModel.ColourTripletCommutant

open QOU.MathlibExt.OctonionDerivations QOU.StandardModel
  QOU.StandardModel.ColourTripletComplexType QOU.StandardModel.OctonionCubeRootPhase

/-! ## A third colour generator -/

/-- Third stabiliser element (support on `e₂ … e₇`). -/
def D₁ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(0 : ℚ), 0, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 0, 0, 0;
    0, 0, 0, -1, 0, 0, 0, 0;
    0, 0, 1, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 0, 0, -1;
    0, 0, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 0, 0, 0, 0;
    0, 0, 0, 0, 1, 0, 0, 0]

theorem D₁_isDer (u v : Fin 8 → ℚ) :
    D₁.mulVec (octMul u v) = octMul (D₁.mulVec u) v + octMul u (D₁.mulVec v) := by
  funext k
  fin_cases k <;> simp [D₁, octMul, Matrix.mulVec, dotProduct, Fin.sum_univ_eight] <;> ring

/-- `D₁` as an element of `su3 stdIm`. -/
def S₁ : ↥(su3 stdIm) :=
  ⟨⟨Matrix.mulVecLin D₁, mem_Der𝕆_of_isDer D₁_isDer⟩, by
    rw [mem_su3_iff]
    funext k
    fin_cases k <;> simp [D₁, stdIm, Matrix.mulVec, dotProduct, Fin.sum_univ_eight]⟩

/-- The triplet restriction of `S₁`. -/
def T₁ : Module.End ℚ (Fin 6 → ℚ) := su3ToEndTriplet S₁

theorem T₁_apply (x : Fin 6 → ℚ) : T₁ x = ![-x 1, x 0, -x 5, 0, 0, x 2] := by
  funext k
  fin_cases k <;>
    simp [T₁, S₁, D₁, su3ToEndTriplet_apply, π6, emb6, Matrix.mulVec, dotProduct,
      Fin.sum_univ_eight]

/-! ## Matrices of the three generators and of `J6` -/

def A₀ : Matrix (Fin 6) (Fin 6) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (-1 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (-1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

def A₁ : Matrix (Fin 6) (Fin 6) ℚ :=
  !![(0 : ℚ), (-1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (-1 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

def A₄ : Matrix (Fin 6) (Fin 6) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (-1 : ℚ); (-1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

def AJ : Matrix (Fin 6) (Fin 6) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (-1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (-1 : ℚ); (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (-1 : ℚ), (0 : ℚ); (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ); (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-! ## The commutant, in matrices -/

set_option maxHeartbeats 4000000 in
/-- **The commutant of colour is `ℚ[J]`** (matrix form). -/
theorem commutant_matrix (X : Matrix (Fin 6) (Fin 6) ℚ)
    (h0 : X * A₀ = A₀ * X) (h1 : X * A₁ = A₁ * X) (h4 : X * A₄ = A₄ * X) :
    X = X 0 0 • (1 : Matrix (Fin 6) (Fin 6) ℚ) + X 2 0 • AJ := by
  have e0 : X 0 4 + X 4 0 = 0 := by
    have := congrFun (congrFun h0 0) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e1 : X 4 1 = 0 := by
    have := congrFun (congrFun h0 0) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e2 : -X 0 3 + X 4 2 = 0 := by
    have := congrFun (congrFun h0 0) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e3 : X 0 2 + X 4 3 = 0 := by
    have := congrFun (congrFun h0 0) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e4 : -X 0 0 + X 4 4 = 0 := by
    have := congrFun (congrFun h0 0) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e5 : X 4 5 = 0 := by
    have := congrFun (congrFun h0 0) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e6 : X 1 4 = 0 := by
    have := congrFun (congrFun h0 1) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e7 : -X 1 3 = 0 := by
    have := congrFun (congrFun h0 1) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e8 : X 1 2 = 0 := by
    have := congrFun (congrFun h0 1) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e9 : -X 1 0 = 0 := by
    have := congrFun (congrFun h0 1) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e10 : X 2 4 - X 3 0 = 0 := by
    have := congrFun (congrFun h0 2) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e11 : -X 3 1 = 0 := by
    have := congrFun (congrFun h0 2) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e12 : -X 2 3 - X 3 2 = 0 := by
    have := congrFun (congrFun h0 2) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e13 : X 2 2 - X 3 3 = 0 := by
    have := congrFun (congrFun h0 2) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e14 : -X 2 0 - X 3 4 = 0 := by
    have := congrFun (congrFun h0 2) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e15 : -X 3 5 = 0 := by
    have := congrFun (congrFun h0 2) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e16 : X 2 0 + X 3 4 = 0 := by
    have := congrFun (congrFun h0 3) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e17 : X 2 1 = 0 := by
    have := congrFun (congrFun h0 3) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e18 : X 2 2 - X 3 3 = 0 := by
    have := congrFun (congrFun h0 3) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e19 : X 2 3 + X 3 2 = 0 := by
    have := congrFun (congrFun h0 3) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e20 : X 2 4 - X 3 0 = 0 := by
    have := congrFun (congrFun h0 3) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e21 : X 2 5 = 0 := by
    have := congrFun (congrFun h0 3) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e22 : -X 0 0 + X 4 4 = 0 := by
    have := congrFun (congrFun h0 4) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e23 : -X 0 1 = 0 := by
    have := congrFun (congrFun h0 4) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e24 : -X 0 2 - X 4 3 = 0 := by
    have := congrFun (congrFun h0 4) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e25 : -X 0 3 + X 4 2 = 0 := by
    have := congrFun (congrFun h0 4) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e26 : -X 0 4 - X 4 0 = 0 := by
    have := congrFun (congrFun h0 4) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e27 : -X 0 5 = 0 := by
    have := congrFun (congrFun h0 4) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e28 : X 5 4 = 0 := by
    have := congrFun (congrFun h0 5) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e29 : -X 5 3 = 0 := by
    have := congrFun (congrFun h0 5) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e30 : X 5 2 = 0 := by
    have := congrFun (congrFun h0 5) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e31 : -X 5 0 = 0 := by
    have := congrFun (congrFun h0 5) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₀] at this; linarith
  have e32 : X 0 1 + X 1 0 = 0 := by
    have := congrFun (congrFun h1 0) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e33 : -X 0 0 + X 1 1 = 0 := by
    have := congrFun (congrFun h1 0) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e34 : X 0 5 + X 1 2 = 0 := by
    have := congrFun (congrFun h1 0) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e35 : X 1 3 = 0 := by
    have := congrFun (congrFun h1 0) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e36 : X 1 4 = 0 := by
    have := congrFun (congrFun h1 0) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e37 : -X 0 2 + X 1 5 = 0 := by
    have := congrFun (congrFun h1 0) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e38 : -X 0 0 + X 1 1 = 0 := by
    have := congrFun (congrFun h1 1) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e39 : -X 0 1 - X 1 0 = 0 := by
    have := congrFun (congrFun h1 1) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e40 : -X 0 2 + X 1 5 = 0 := by
    have := congrFun (congrFun h1 1) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e41 : -X 0 3 = 0 := by
    have := congrFun (congrFun h1 1) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e42 : -X 0 4 = 0 := by
    have := congrFun (congrFun h1 1) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e43 : -X 0 5 - X 1 2 = 0 := by
    have := congrFun (congrFun h1 1) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e44 : X 2 1 + X 5 0 = 0 := by
    have := congrFun (congrFun h1 2) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e45 : -X 2 0 + X 5 1 = 0 := by
    have := congrFun (congrFun h1 2) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e46 : X 2 5 + X 5 2 = 0 := by
    have := congrFun (congrFun h1 2) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e47 : X 5 3 = 0 := by
    have := congrFun (congrFun h1 2) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e48 : X 5 4 = 0 := by
    have := congrFun (congrFun h1 2) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e49 : -X 2 2 + X 5 5 = 0 := by
    have := congrFun (congrFun h1 2) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e50 : X 3 1 = 0 := by
    have := congrFun (congrFun h1 3) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e51 : -X 3 0 = 0 := by
    have := congrFun (congrFun h1 3) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e52 : X 3 5 = 0 := by
    have := congrFun (congrFun h1 3) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e53 : -X 3 2 = 0 := by
    have := congrFun (congrFun h1 3) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e54 : X 4 1 = 0 := by
    have := congrFun (congrFun h1 4) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e55 : -X 4 0 = 0 := by
    have := congrFun (congrFun h1 4) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e56 : X 4 5 = 0 := by
    have := congrFun (congrFun h1 4) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e57 : -X 4 2 = 0 := by
    have := congrFun (congrFun h1 4) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e58 : -X 2 0 + X 5 1 = 0 := by
    have := congrFun (congrFun h1 5) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e59 : -X 2 1 - X 5 0 = 0 := by
    have := congrFun (congrFun h1 5) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e60 : -X 2 2 + X 5 5 = 0 := by
    have := congrFun (congrFun h1 5) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e61 : -X 2 3 = 0 := by
    have := congrFun (congrFun h1 5) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e62 : -X 2 4 = 0 := by
    have := congrFun (congrFun h1 5) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e63 : -X 2 5 - X 5 2 = 0 := by
    have := congrFun (congrFun h1 5) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₁] at this; linarith
  have e64 : -X 0 2 - X 2 0 = 0 := by
    have := congrFun (congrFun h4 0) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e65 : X 0 5 - X 2 1 = 0 := by
    have := congrFun (congrFun h4 0) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e66 : X 0 0 - X 2 2 = 0 := by
    have := congrFun (congrFun h4 0) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e67 : -X 2 3 = 0 := by
    have := congrFun (congrFun h4 0) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e68 : -X 2 4 = 0 := by
    have := congrFun (congrFun h4 0) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e69 : -X 0 1 - X 2 5 = 0 := by
    have := congrFun (congrFun h4 0) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e70 : -X 1 2 + X 5 0 = 0 := by
    have := congrFun (congrFun h4 1) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e71 : X 1 5 + X 5 1 = 0 := by
    have := congrFun (congrFun h4 1) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e72 : X 1 0 + X 5 2 = 0 := by
    have := congrFun (congrFun h4 1) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e73 : X 5 3 = 0 := by
    have := congrFun (congrFun h4 1) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e74 : X 5 4 = 0 := by
    have := congrFun (congrFun h4 1) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e75 : -X 1 1 + X 5 5 = 0 := by
    have := congrFun (congrFun h4 1) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e76 : X 0 0 - X 2 2 = 0 := by
    have := congrFun (congrFun h4 2) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e77 : X 0 1 + X 2 5 = 0 := by
    have := congrFun (congrFun h4 2) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e78 : X 0 2 + X 2 0 = 0 := by
    have := congrFun (congrFun h4 2) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e79 : X 0 3 = 0 := by
    have := congrFun (congrFun h4 2) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e80 : X 0 4 = 0 := by
    have := congrFun (congrFun h4 2) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e81 : X 0 5 - X 2 1 = 0 := by
    have := congrFun (congrFun h4 2) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e82 : -X 3 2 = 0 := by
    have := congrFun (congrFun h4 3) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e83 : X 3 5 = 0 := by
    have := congrFun (congrFun h4 3) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e84 : X 3 0 = 0 := by
    have := congrFun (congrFun h4 3) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e85 : -X 3 1 = 0 := by
    have := congrFun (congrFun h4 3) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e86 : -X 4 2 = 0 := by
    have := congrFun (congrFun h4 4) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e87 : X 4 5 = 0 := by
    have := congrFun (congrFun h4 4) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e88 : X 4 0 = 0 := by
    have := congrFun (congrFun h4 4) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e89 : -X 4 1 = 0 := by
    have := congrFun (congrFun h4 4) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e90 : -X 1 0 - X 5 2 = 0 := by
    have := congrFun (congrFun h4 5) 0
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e91 : -X 1 1 + X 5 5 = 0 := by
    have := congrFun (congrFun h4 5) 1
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e92 : -X 1 2 + X 5 0 = 0 := by
    have := congrFun (congrFun h4 5) 2
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e93 : -X 1 3 = 0 := by
    have := congrFun (congrFun h4 5) 3
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e94 : -X 1 4 = 0 := by
    have := congrFun (congrFun h4 5) 4
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  have e95 : -X 1 5 - X 5 1 = 0 := by
    have := congrFun (congrFun h4 5) 5
    simp [Matrix.mul_apply, Fin.sum_univ_six, A₄] at this; linarith
  ext i j
  fin_cases i <;> fin_cases j <;> simp [AJ] <;> linarith

/-! ## Bridge to the actual colour action -/

theorem toMatrix'_T₀ : LinearMap.toMatrix' T₀ = A₀ := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [LinearMap.toMatrix'_apply, T₀_apply, A₀]

theorem toMatrix'_T₁ : LinearMap.toMatrix' T₁ = A₁ := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [LinearMap.toMatrix'_apply, T₁_apply, A₁]

theorem toMatrix'_T₄ : LinearMap.toMatrix' T₄ = A₄ := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [LinearMap.toMatrix'_apply, T₄_apply, A₄]

theorem toMatrix'_J6 : LinearMap.toMatrix' J6 = AJ := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [LinearMap.toMatrix'_apply, J6_apply, AJ]

/-- **The commutant of colour is `ℚ[J6]`** (operator form): an endomorphism of the colour
triple commuting with the colour generators `T₀, T₁, T₄` is `a • 1 + b • J6`. -/
theorem commutant_end (M : Module.End ℚ (Fin 6 → ℚ))
    (h0 : M * T₀ = T₀ * M) (h1 : M * T₁ = T₁ * M) (h4 : M * T₄ = T₄ * M) :
    ∃ a b : ℚ, M = a • 1 + b • J6 := by
  have m0 := congrArg LinearMap.toMatrix' h0
  have m1 := congrArg LinearMap.toMatrix' h1
  have m4 := congrArg LinearMap.toMatrix' h4
  simp only [LinearMap.toMatrix'_mul, toMatrix'_T₀, toMatrix'_T₁, toMatrix'_T₄] at m0 m1 m4
  have key := commutant_matrix _ m0 m1 m4
  refine ⟨LinearMap.toMatrix' M 0 0, LinearMap.toMatrix' M 2 0,
    LinearMap.toMatrix'.injective ?_⟩
  rw [map_add, map_smul, map_smul, show (1 : Module.End ℚ (Fin 6 → ℚ)) = LinearMap.id from rfl,
    LinearMap.toMatrix'_id, toMatrix'_J6]
  exact key

/-- **Operators commuting with colour commute with each other.**  The commutant is
commutative, so no non-abelian flavour algebra acts on the octonionic colour triple
commuting with colour. -/
theorem commutant_commutative (M N : Module.End ℚ (Fin 6 → ℚ))
    (hM0 : M * T₀ = T₀ * M) (hM1 : M * T₁ = T₁ * M) (hM4 : M * T₄ = T₄ * M)
    (hN0 : N * T₀ = T₀ * N) (hN1 : N * T₁ = T₁ * N) (hN4 : N * T₄ = T₄ * N) :
    M * N = N * M := by
  obtain ⟨a, b, rfl⟩ := commutant_end M hM0 hM1 hM4
  obtain ⟨c, d, rfl⟩ := commutant_end N hN0 hN1 hN4
  have hJ : Commute J6 J6 := Commute.refl _
  apply Commute.eq
  apply Commute.add_left <;> apply Commute.add_right <;>
    first
    | exact ((Commute.one_left _).smul_left _).smul_right _
    | exact ((Commute.one_right _).smul_left _).smul_right _
    | exact (hJ.smul_left _).smul_right _

/-- **No cube-root phase commutes with colour over `ℚ`.** -/
theorem no_cubeRoot_phase_in_commutant (M : Module.End ℚ (Fin 6 → ℚ))
    (h0 : M * T₀ = T₀ * M) (h1 : M * T₁ = T₁ * M) (h4 : M * T₄ = T₄ * M) :
    M * M + M + 1 ≠ 0 := by
  obtain ⟨a, b, rfl⟩ := commutant_end M h0 h1 h4
  exact colourTriple_no_rational_cubeRoot_phase a b

end QOU.StandardModel.ColourTripletCommutant
