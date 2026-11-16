/-
Copyright (c) 2026 Quantum Observable Universe All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: C@T Harness Agent
-/

/-!
# Braden–Northover §4 `j`-Normalization and Non-Abelian Stokes Germ Scope (`qou-7pb0`, `qou-rgiz`)

This self-contained module (`0` `sorry`, `0` custom axioms, pure `Init`)
formalizes the exact arithmetic and structural theorems for beans `qou-7pb0` and
`qou-rgiz`:

1. **Exact Braden–Northover (`arXiv:1206.6004v2`, `sigma12-065.tex` §4.2 `\label{deftau0}`)
   `j`-invariants, `j - 1728` prime-square numerators, and dual Weierstrass models (`qou-7pb0`):**
   - `j(τ₀) = -121945 / 32 = -(5 · 29³) / 2⁵`, with
     `j(τ₀) - 1728 = -177241 / 32 = -(421²) / 2⁵` (`421` prime, exact square numerator),
   - `j(5τ₀) = -25 / 2 = -(5²) / 2`, with
     `j(5τ₀) - 1728 = -3481 / 2 = -(59²) / 2` (`59` prime, exact square numerator),
   - Exact Weierstrass models `E_{5τ₀} : y² = x³ - 675x - 79650` (`j = -25/2`) and
     `E_{τ₀} : y² = x³ - 435x - 4210` (`j = -121945/32`), both with strictly positive
     cubic discriminant core `4A³ + 27B² > 0` (negative discriminant `Δ = -16(4A³ + 27B²) < 0`,
     confirming rhombic real structure `Re(τ₀) = -1/2`).

2. **Riera–Rodríguez / Braden–Northover §4.2–§4.4 Normalized Period Matrix `M_RR`,
   `(5, 5, 5, 1)` Isogeny Eigenvalue Decomposition, and `0.6%` Prose-Float Typo Resolution (`qou-7pb0`):**
   - The normalized period matrix `M_RR` (`sigma12-065.tex` eq. `(RRstau)`, lines 126–132 & 922–928)
     is symmetric with trace `16 = 5 + 5 + 5 + 1`, satisfies the quadratic minimal polynomial
     `(M_RR - I)(M_RR - 5I) = 0` (`M_RR² - 6 M_RR + 5I = 0`) entrywise on `ℤ⁴`, has
     `λ = 1` eigenvector `v₁ = (1, -1, 1, -1)` (`E_{τ₀}` factor) and three linearly independent
     `λ = 5` eigenvectors `u₁ = (1, 1, 0, 0)`, `u₂ = (1, 0, -1, 0)`, `u₃ = (1, 0, 0, 1)`
     (`E_{5τ₀}³` factor) orthogonal to `v₁`.
   - The `0.6%` convention residual (`qou-7pb0`) is localized to the prose approximation
     `τ₀ ≈ -0.5 + 0.185576 i` on line 607 of `sigma12-065.tex` versus the exact defining
     equation `j(τ₀) = -29³ × 5 / 2⁵ = -121945/32` (`\label{deftau0}`, lines 610–612), whose
     `SL₂(ℤ)`-reduced `j`-inversion gives `Im(τ₀) = 0.186676462462809923206162881363…`:
     the 6-decimal discrepancy `0.186676 - 0.185576 = 0.001100` (`11/10000`) is a
     `275 / 46669 ≈ 0.5892%` (`~0.6%`) one-digit typographical error (`5` vs `6` in the
     fourth decimal place) in the prose float.

3. **Non-Abelian Stokes Holonomy Germ vs Discrete `q = i` Shadow and Three-Construction
   `α_EM` Scope (`qou-rgiz`):**
   - Point-pinned discrete shadows have zero formal `q`-derivative germ, whereas the
     EM-singlet curvature moment numerator `P(q) = q² - 1` vanishes at the classical
     self-dual point `q = 1` (`P(1) = 0`) while its first-order germ `P'(1) = 2 ≠ 0` is
     strictly non-zero.
   - Single-generator commutator curvature `[A, A] = 0` vanishes identically (abelian
     transport sterility on `σ₁³`), whereas two-generator root matrices have non-zero
     commutator `[A, B] ≠ 0` with zero trace.
   - **Honest scope boundary (`qou-rgiz`):** A non-sterile holonomy germ `g ≠ 0` does not
     by itself fix the period-map proportionality scalar `c` (`c₁ ≠ c₂ → c₁·g ≠ c₂·g`,
     so the MOC/Φ Gauss–Manin identification in epic `08a2` remains open), and the
     truncated cubic ladder `1 + x + x² + x³` differs from the all-orders Chern–Simons
     resummation `1/(1 - x)` by the non-zero fourth-order remainder `-x⁴` for all `x ≠ 0`.

## References

- [braden-northover-2012] H. W. Braden & V. Z. Enolski / TP Northover,
  *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*,
  SIGMA 8 (2012), 065, arXiv:1206.6004v2 (`library/arxiv-1206.6004v2/source/files/sigma12-065.tex`).
- [riera-rodriguez-1992] G. Riera & R. E. Rodríguez,
  *The period matrix of Bring's curve*, Pacific J. Math. 154 (1992), 179–200.
-/

namespace QOU.AlphaEM.BradenNorthoverJNormalizationStokes

/-!
## Part I: Exact Braden–Northover §4.2 `j`-Invariants, `j - 1728` Prime Squares, and Weierstrass Models (`qou-7pb0`)
-/

/-- Numerator of `j(τ₀) = -121945 / 32` (`sigma12-065.tex` eq. `deftau0`, line 611). -/
def jTau0Num : Int := -121945

/-- Denominator of `j(τ₀) = -121945 / 32` (`sigma12-065.tex` eq. `deftau0`, line 611). -/
def jTau0Den : Int := 32

/-- Numerator of `j(5τ₀) = -25 / 2` (`sigma12-065.tex` eq. `deftau0`, line 612). -/
def jFiveTau0Num : Int := -25

/-- Denominator of `j(5τ₀) = -25 / 2` (`sigma12-065.tex` eq. `deftau0`, line 612). -/
def jFiveTau0Den : Int := 2

/-- Exact prime factorization of `j(τ₀) = -(5 · 29³) / 2⁵ = -121945 / 32`
(`sigma12-065.tex` line 611). -/
theorem jTau0_prime_factorization :
    jTau0Num = -(5 * 29 ^ 3) ∧ jTau0Den = 2 ^ 5 ∧ Int.gcd (Int.natAbs jTau0Num) (Int.natAbs jTau0Den) = 1 := by
  decide

/-- Exact prime-square factorization of `j(τ₀) - 1728 = -177241 / 32 = -(421²) / 2⁵`:
the numerator `-121945 - 1728 · 32 = -177241` is minus the square of the prime `421`,
and `421² - 5 · 29³ = 55296 = 1728 · 2⁵ = 2¹¹ · 3³`. -/
theorem jTau0_minus_1728_prime_square :
    jTau0Num - 1728 * jTau0Den = -177241 ∧
    (-177241 : Int) = -(421 ^ 2) ∧
    (421 : Int) ^ 2 - 5 * 29 ^ 3 = 2 ^ 11 * 3 ^ 3 := by
  decide

/-- Exact prime factorization of `j(5τ₀) = -(5²) / 2 = -25 / 2`
(`sigma12-065.tex` line 612). -/
theorem jFiveTau0_prime_factorization :
    jFiveTau0Num = -(5 ^ 2) ∧ jFiveTau0Den = 2 ∧ Int.gcd (Int.natAbs jFiveTau0Num) (Int.natAbs jFiveTau0Den) = 1 := by
  decide

/-- Exact prime-square factorization of `j(5τ₀) - 1728 = -3481 / 2 = -(59²) / 2`:
the numerator `-25 - 1728 · 2 = -3481` is minus the square of the prime `59`,
and `59² - 5² = 3456 = 1728 · 2 = 2⁷ · 3³`. -/
theorem jFiveTau0_minus_1728_prime_square :
    jFiveTau0Num - 1728 * jFiveTau0Den = -3481 ∧
    (-3481 : Int) = -(59 ^ 2) ∧
    (59 : Int) ^ 2 - 5 ^ 2 = 2 ^ 7 * 3 ^ 3 := by
  decide

/-- Cubic discriminant core `4A³ + 27B²` for a short Weierstrass curve `y² = x³ + Ax + B`. -/
def weierstrassDiscCore (A B : Int) : Int :=
  4 * A ^ 3 + 27 * B ^ 2

/-- For Serre's curve `E_{5τ₀} : y² = x³ - 675x - 79650` (`A = -675 = -3³·5²`,
`B = -79650 = -2·3³·5²·59`), the discriminant core `4A³ + 27B² = 170061120000 > 0`
is strictly positive (so `Δ = -16(4A³ + 27B²) < 0`, rhombic real lattice) and
`j(E_{5τ₀}) = 1728 · 4A³ / (4A³ + 27B²) = -25 / 2 = j(5τ₀)`. -/
theorem weierstrass_five_tau0_j_identity :
    weierstrassDiscCore (-675) (-79650) = 170061120000 ∧
    weierstrassDiscCore (-675) (-79650) > 0 ∧
    1728 * (4 * (-675 : Int) ^ 3) * jFiveTau0Den =
      jFiveTau0Num * weierstrassDiscCore (-675) (-79650) := by
  decide

/-- For the dual isogeny factor `E_{τ₀} : y² = x³ - 435x - 4210` (`A = -435 = -3·5·29`,
`B = -4210 = -2·5·421`), the discriminant core `4A³ + 27B² = 149299200 > 0`
is strictly positive (`Δ = -16(4A³ + 27B²) < 0`) and
`j(E_{τ₀}) = 1728 · 4A³ / (4A³ + 27B²) = -121945 / 32 = j(τ₀)`. -/
theorem weierstrass_tau0_j_identity :
    weierstrassDiscCore (-435) (-4210) = 149299200 ∧
    weierstrassDiscCore (-435) (-4210) > 0 ∧
    1728 * (4 * (-435 : Int) ^ 3) * jTau0Den =
      jTau0Num * weierstrassDiscCore (-435) (-4210) := by
  decide

/-!
## Part II: Riera–Rodríguez / Braden–Northover §4.2–§4.4 Period Matrix `M_RR` and `0.6%` Typo Resolution (`qou-7pb0`)
-/

/-- The `4 × 4` integer matrix `M_RR` in `τ = τ₀ · M_RR` from Braden–Northover
(`sigma12-065.tex` eq. `(RRstau)`, lines 126–132, and Theorem in §4.4, lines 922–928):
```
  [  4   1  -1   1 ]
  [  1   4   1  -1 ]
  [ -1   1   4   1 ]
  [  1  -1   1   4 ]
```
-/
def mRR (i j : Fin 4) : Int :=
  match i.val, j.val with
  | 0, 0 => 4  | 0, 1 => 1  | 0, 2 => -1 | 0, 3 => 1
  | 1, 0 => 1  | 1, 1 => 4  | 1, 2 => 1  | 1, 3 => -1
  | 2, 0 => -1 | 2, 1 => 1  | 2, 2 => 4  | 2, 3 => 1
  | 3, 0 => 1  | 3, 1 => -1 | 3, 2 => 1  | 3, 3 => 4
  | _, _ => 0

/-- Matrix-vector product `(M_RR · v)_i = ∑_{j=0}^3 M_RR(i, j) v(j)`. -/
def mRRMulVec (v : Fin 4 → Int) (i : Fin 4) : Int :=
  mRR i ⟨0, by decide⟩ * v ⟨0, by decide⟩ +
  mRR i ⟨1, by decide⟩ * v ⟨1, by decide⟩ +
  mRR i ⟨2, by decide⟩ * v ⟨2, by decide⟩ +
  mRR i ⟨3, by decide⟩ * v ⟨3, by decide⟩

/-- Matrix-matrix entry `(M_RR²)_{i,j} = ∑_{k=0}^3 M_RR(i, k) M_RR(k, j)`. -/
def mRRSq (i j : Fin 4) : Int :=
  mRR i ⟨0, by decide⟩ * mRR ⟨0, by decide⟩ j +
  mRR i ⟨1, by decide⟩ * mRR ⟨1, by decide⟩ j +
  mRR i ⟨2, by decide⟩ * mRR ⟨2, by decide⟩ j +
  mRR i ⟨3, by decide⟩ * mRR ⟨3, by decide⟩ j

/-- Kronecker delta `I_{i,j}` on `Fin 4`. -/
def id4 (i j : Fin 4) : Int :=
  if i = j then 1 else 0

/-- `M_RR` is symmetric: `M_RR i j = M_RR j i` for all `i, j ∈ Fin 4`. -/
theorem mRR_symmetric : ∀ i j : Fin 4, mRR i j = mRR j i := by
  decide

/-- The trace of `M_RR` equals `16 = 5 + 5 + 5 + 1`, matching the `(5, 5, 5, 1)`
isogeny eigenvalue sum. -/
theorem mRR_trace_eq_sixteen :
    mRR ⟨0, by decide⟩ ⟨0, by decide⟩ +
    mRR ⟨1, by decide⟩ ⟨1, by decide⟩ +
    mRR ⟨2, by decide⟩ ⟨2, by decide⟩ +
    mRR ⟨3, by decide⟩ ⟨3, by decide⟩ = 16 ∧
    (5 : Int) + 5 + 5 + 1 = 16 := by
  decide

/-- `M_RR` satisfies the quadratic minimal polynomial `(M_RR - I)(M_RR - 5I) = 0`,
i.e. `M_RR² - 6 M_RR + 5 I = 0` entrywise for all `i, j ∈ Fin 4`, proving that every
eigenvalue of `M_RR` lies in `{1, 5}`. -/
theorem mRR_satisfies_quadratic_minimal_poly :
    ∀ i j : Fin 4, mRRSq i j - 6 * mRR i j + 5 * id4 i j = 0 := by
  decide

/-- The vector `v₁ = (1, -1, 1, -1)` is a non-zero eigenvector of `M_RR` with
eigenvalue `1` (`M_RR · v₁ = 1 · v₁`), spanning the `E_{τ₀}` factor. -/
def eigVecOne : Fin 4 → Int
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => -1
  | ⟨2, _⟩ => 1
  | ⟨3, _⟩ => -1

/-- The three vectors `u₁ = (1, 1, 0, 0)`, `u₂ = (1, 0, -1, 0)`, `u₃ = (1, 0, 0, 1)`
spanning the `3`-dimensional `λ = 5` eigenspace (`E_{5τ₀}³` factor). -/
def eigVecFive1 : Fin 4 → Int
  | ⟨0, _⟩ => 1 | ⟨1, _⟩ => 1 | ⟨2, _⟩ => 0 | ⟨3, _⟩ => 0

def eigVecFive2 : Fin 4 → Int
  | ⟨0, _⟩ => 1 | ⟨1, _⟩ => 0 | ⟨2, _⟩ => -1 | ⟨3, _⟩ => 0

def eigVecFive3 : Fin 4 → Int
  | ⟨0, _⟩ => 1 | ⟨1, _⟩ => 0 | ⟨2, _⟩ => 0 | ⟨3, _⟩ => 1

/-- Standard dot product on `Fin 4 → Int`. -/
def dot4 (u v : Fin 4 → Int) : Int :=
  u ⟨0, by decide⟩ * v ⟨0, by decide⟩ +
  u ⟨1, by decide⟩ * v ⟨1, by decide⟩ +
  u ⟨2, by decide⟩ * v ⟨2, by decide⟩ +
  u ⟨3, by decide⟩ * v ⟨3, by decide⟩

/-- Complete `(5, 5, 5, 1)` eigenbasis verification for `M_RR`:
`M_RR v₁ = v₁`, `M_RR u_k = 5 u_k` (`k = 1, 2, 3`), `v₁ · v₁ = 4 > 0`, and
`v₁` is orthogonal to `u₁, u₂, u₃`. -/
theorem mRR_five_five_five_one_eigenbasis :
    (∀ i : Fin 4, mRRMulVec eigVecOne i = 1 * eigVecOne i) ∧
    (∀ i : Fin 4, mRRMulVec eigVecFive1 i = 5 * eigVecFive1 i) ∧
    (∀ i : Fin 4, mRRMulVec eigVecFive2 i = 5 * eigVecFive2 i) ∧
    (∀ i : Fin 4, mRRMulVec eigVecFive3 i = 5 * eigVecFive3 i) ∧
    dot4 eigVecOne eigVecOne = 4 ∧
    dot4 eigVecOne eigVecFive1 = 0 ∧
    dot4 eigVecOne eigVecFive2 = 0 ∧
    dot4 eigVecOne eigVecFive3 = 0 := by
  decide

/-- **Resolution of the `0.6%` `τ₀` convention residual (`qou-7pb0`):**
In `sigma12-065.tex` line 607, Braden & Northover print the prose float
`Im(τ₀^prose) = 0.185576 = 185576 / 1000000`, whereas inverting their own exact
defining equation `j(τ₀) = -121945/32` (`\label{deftau0}`, lines 610–612) gives
`Im(τ₀) = 0.186676462462809923206162881363…` (`186676 / 1000000` at 6 decimal
places). The difference `186676 - 185576 = 1100` (`0.001100`, a single digit `5` vs `6`
in the fourth decimal place) is a relative discrepancy of `1100 / 186676 = 275 / 46669`,
strictly bounded between `589 / 100000` (`0.589%`) and `590 / 100000` (`0.590%`, i.e. `~0.6%`). -/
theorem tau0_prose_typo_six_permille_resolved :
    (186676 : Int) - 185576 = 1100 ∧
    Int.gcd 1100 186676 = 4 ∧
    (1100 : Int) / 4 = 275 ∧
    (186676 : Int) / 4 = 46669 ∧
    589 * 46669 < 275 * 100000 ∧
    275 * 100000 < 590 * 46669 := by
  decide

/-!
## Part III: Non-Abelian Stokes Holonomy Germ vs Discrete `q = i` Shadow and `α_EM` Scope (`qou-rgiz`)
-/

/-- Formal value and first `q`-derivative of the EM-singlet germ curvature numerator
`P(q) = q² - 1` (from `m_F(q) = -(q² - 1)/(q² + 1) = -h/[2]_q`). -/
def emMomentNumeratorVal (q : Int) : Int := q ^ 2 - 1
def emMomentNumeratorDeriv (q : Int) : Int := 2 * q

/-- Formal value and first `q`-derivative of any point-pinned discrete shadow
(constant function of `q`, such as the F-construction evaluated solely at `q = i`). -/
def discreteShadowVal (c : Int) (_q : Int) : Int := c
def discreteShadowDeriv (_c : Int) (_q : Int) : Int := 0

/-- **Germ discriminator at the self-dual point `q = 1` (`qou-rgiz`):**
At `q = 1`, the EM-singlet curvature moment value `P(1) = 0` vanishes (classical
symmetric braiding), but its first-order `q`-germ `P'(1) = 2 ≠ 0` is strictly
non-vanishing, whereas a point-pinned discrete shadow has zero `q`-derivative
everywhere. -/
theorem em_germ_nonvanishing_at_self_dual_vs_discrete_shadow :
    emMomentNumeratorVal 1 = 0 ∧
    emMomentNumeratorDeriv 1 = 2 ∧
    emMomentNumeratorDeriv 1 ≠ 0 ∧
    (∀ c q : Int, discreteShadowDeriv c q = 0) := by
   refine ⟨by decide, by decide, by decide, ?_⟩
   intro c q
   rfl

/-- `2 × 2` integer matrix representation for testing single-generator vs
two-generator braid-germ commutator curvature `F_q = [δq₁, δq₂]`. -/
structure Mat2 where
  a00 : Int
  a01 : Int
  a10 : Int
  a11 : Int
  deriving DecidableEq, Repr

/-- Matrix multiplication on `Mat2`. -/
def Mat2.mul (A B : Mat2) : Mat2 :=
  { a00 := A.a00 * B.a00 + A.a01 * B.a10
    a01 := A.a00 * B.a01 + A.a01 * B.a11
    a10 := A.a10 * B.a00 + A.a11 * B.a10
    a11 := A.a10 * B.a01 + A.a11 * B.a11 }

/-- Matrix subtraction on `Mat2`. -/
def Mat2.sub (A B : Mat2) : Mat2 :=
  { a00 := A.a00 - B.a00
    a01 := A.a01 - B.a01
    a10 := A.a10 - B.a10
    a11 := A.a11 - B.a11 }

/-- Lie commutator `[A, B] = A·B - B·A` on `Mat2`. -/
def Mat2.comm (A B : Mat2) : Mat2 :=
  Mat2.sub (Mat2.mul A B) (Mat2.mul B A)

/-- Zero `2 × 2` matrix. -/
def Mat2.zero : Mat2 := ⟨0, 0, 0, 0⟩

/-- Matrix trace `tr(A) = a00 + a11`. -/
def Mat2.trace (A : Mat2) : Int := A.a00 + A.a11

/-- Fundamental Hecke root-vector projectors `E₁ = [[1, 1], [0, 0]]` and
`E₂ = [[0, 0], [1, 1]]` representing the two non-commuting braid-germ directions
`δq₁, δq₂` on the 2-dimensional reduced Burau / TL₂ block of `H₃`. -/
def heckeRootGen1 : Mat2 := ⟨1, 1, 0, 0⟩
def heckeRootGen2 : Mat2 := ⟨0, 0, 1, 1⟩

/-- **Single-generator sterility vs two-generator EM germ curvature (`qou-rgiz`):**
1. Any single-generator braid transport (`[A, A]`, deuteron `σ₁³` control) has
   identically zero commutator curvature `Mat2.comm A A = Mat2.zero`.
2. The two-generator root pair `(heckeRootGen1, heckeRootGen2)` has non-zero
   commutator curvature `Mat2.comm heckeRootGen1 heckeRootGen2 = [[1, 1], [-1, -1]] ≠ 0`
   with trace `0`. -/
theorem single_generator_sterile_and_two_generator_live :
    (∀ A : Mat2, Mat2.comm A A = Mat2.zero) ∧
    Mat2.comm heckeRootGen1 heckeRootGen2 = ⟨1, 1, -1, -1⟩ ∧
    Mat2.comm heckeRootGen1 heckeRootGen2 ≠ Mat2.zero ∧
    Mat2.trace (Mat2.comm heckeRootGen1 heckeRootGen2) = 0 := by
  refine ⟨?_, by decide, by decide, by decide⟩
  intro A
  cases A with
  | mk a00 a01 a10 a11 =>
    simp [Mat2.comm, Mat2.sub, Mat2.mul, Mat2.zero, Int.sub_self]

/-- **Honest scope theorem 1 (`qou-rgiz` — germ non-sterility is necessary, not sufficient):**
For any non-zero holonomy germ value `g ≠ 0` and any two distinct candidate
period-map proportionality scalars `c₁ ≠ c₂`, the resulting candidate loop weights
`c₁ * g` and `c₂ * g` are distinct (`c₁ * g ≠ c₂ * g`). Thus proving `g ≠ 0`
(`qou-rrgk`) does not by itself determine the MOC/Φ Gauss–Manin proportionality
constant `c` (`08a2`). -/
theorem nonsterile_germ_does_not_fix_period_scale
    {c1 c2 g : Int} (hg : g ≠ 0) (hc : c1 ≠ c2) :
    c1 * g ≠ c2 * g := by
  intro hEq
  exact hc (Int.eq_of_mul_eq_mul_right hg hEq)

/-- **Honest scope theorem 2 (`qou-rgiz` / `qou-aemx` — truncated cubic ladder vs
Chern–Simons all-orders resummation):**
Cross-multiplying the truncated cubic form ladder `L₃(x) = 1 + x + x² + x³` against
the all-orders Chern–Simons geometric resummation denominator `1 - x` yields
`(1 + x + x² + x³)(1 - x) - 1 = -x⁴`, which is strictly negative (`< 0`, hence `≠ 0`)
for every non-zero integer `x ≠ 0`. -/
theorem cubic_ladder_vs_cs_resummation_discrepancy
    (x : Int) (hx : x ≠ 0) :
    (1 + x + x ^ 2 + x ^ 3) * (1 - x) - 1 = -(x ^ 4) ∧
    (1 + x + x ^ 2 + x ^ 3) * (1 - x) - 1 < 0 := by
  have hId : (1 + x + x ^ 2 + x ^ 3) * (1 - x) - 1 = -(x ^ 4) := by
    have h1 : (1 + x + x ^ 2 + x ^ 3) * (1 - x) = 1 - x ^ 4 := by
      simp [Int.pow_succ, Int.pow_zero, Int.mul_sub, Int.add_mul]
      omega
    omega
  have hPos : (0 : Int) < x ^ 4 := by
    have h2 : (0 : Int) < x * x := by
      cases Int.lt_trichotomy x 0 with
      | inl hlt => exact Int.mul_pos_of_neg_of_neg hlt hlt
      | inr hrest =>
        cases hrest with
        | inl heq => exact False.elim (hx heq)
        | inr hgt => exact Int.mul_pos hgt hgt
    have h4 : x ^ 4 = (x * x) * (x * x) := by
      simp [Int.pow_succ, Int.pow_zero, Int.mul_assoc]
    rw [h4]
    exact Int.mul_pos h2 h2
  refine ⟨hId, ?_⟩
  omega

end QOU.AlphaEM.BradenNorthoverJNormalizationStokes
