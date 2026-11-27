/-
  γγ production generates the operator basis (categorical).

  Two independent colored photons in the 6-dimensional Iwahori–Hecke algebra H₃(q)
  (with quadratic parameter h = q - q⁻¹),
    γ₁ = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹,
    γ₂ = 𝟙 + ψ₀·σ₀ + ψ₁·σ₁ + ψ₀₁·σ₀σ₁⁻¹
  (def:photon; the fourth term is the chiral pair-production vertex σ₀σ₁⁻¹),
  multiply to a Breit–Wheeler normal form reaching every basis operator
  {𝟙, σ₀, σ₁, L₊ = σ₀σ₁, L₋ = σ₁σ₀, e⁻ = σ₀σ₁σ₀}:

  1. Because σ₁⁻¹ = σ₁ - h·𝟙, the chiral vertex satisfies σ₀·σ₁⁻¹ = L₊ - h·σ₀,
     so every single photon has zero L₋ and zero e⁻ coordinate.
  2. The 3-term product (φ₀₁ = ψ₀₁ = 0) reduces to the exact 5-channel normal
     form generating (L₊, L₋) independently via (φ₀ψ₁, φ₁ψ₀).
  3. Restoring the 4-term vertex coupling opens e⁻ via
     (σ₀·σ₁⁻¹)·σ₀ = e⁻ - h²·σ₀ - h·𝟙 with coefficient φ₀₁·ψ₀ + φ₁·ψ₀₁,
     while conjugate pure-vertex weights (qh, -q⁻¹h) factor the Borromean
     nucleon braid (σ₀·σ₁⁻¹)³.
  4. The R-linear span of two-photon products equals all of H₃(R, h) over any
     commutative ring R (proved both on `QOU.QuarkState.pairNFChiral` and inside
     the associative `R`-algebra `H3Elem R h`).

  -- Ref: [leitner2026] predicted-spectra, gamma-gamma-generates-particles
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.Tactic
import QOU.Confinement.PhotonPairNormalForm

namespace QOU.Archimedean.GammaGammaGeneration

section PairNFChiral

variable {R : Type*} [CommRing R]

/-- Coefficient of `L₊ = σ₀σ₁` in the two-photon product `γ₁·γ₂`, as a
    function of the color weights `(φ₀, φ₁)` of `γ₁` and `(ψ₀, ψ₁)` of
    `γ₂`: the cross-color product `φ₀ · ψ₁`. -/
def coeffLplus (φ0 _φ1 _ψ0 ψ1 : R) : R := φ0 * ψ1

/-- Coefficient of `L₋ = σ₁σ₀` in the two-photon product: `φ₁ · ψ₀`. -/
def coeffLminus (_φ0 φ1 ψ0 _ψ1 : R) : R := φ1 * ψ0

/-- **The chiral pair is generated independently by γγ production.**
    For any target pair `(a, b)` there exist photon color weights whose
    two-photon product has `L₊`-coefficient `a` and `L₋`-coefficient `b`
    (take `φ₀ = a, ψ₁ = 1, φ₁ = b, ψ₀ = 1`). Hence both chiral Hopf
    operators arise from `γγ` production. -/
theorem gamma_gamma_chirality_surjective (a b : R) :
    ∃ φ0 φ1 ψ0 ψ1 : R,
      coeffLplus φ0 φ1 ψ0 ψ1 = a ∧ coeffLminus φ0 φ1 ψ0 ψ1 = b :=
  ⟨a, b, 1, 1, by simp [coeffLplus], by simp [coeffLminus]⟩

/-- The `L₋ = σ₁σ₀` content of a *single* photon
    `γ = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` is zero: its normal-form support is
    `{𝟙, σ₀, σ₁, σ₀σ₁}`, which does not include `σ₁σ₀`. -/
def singlePhotonCoeffLminus : R := 0

/-- **γγ production strictly enlarges the reachable operator set.**
    There are photon color weights whose two-photon product carries a
    nonzero `L₋ = σ₁σ₀` operator — content no single photon can hold. -/
theorem gamma_gamma_reaches_Lminus [Nontrivial R] :
    ∃ φ0 φ1 ψ0 ψ1 : R,
      coeffLminus φ0 φ1 ψ0 ψ1 ≠ singlePhotonCoeffLminus := by
  refine ⟨0, 1, 1, 0, ?_⟩
  simp only [coeffLminus, singlePhotonCoeffLminus, mul_one]
  exact one_ne_zero

/-! ### On the H₃ normal form of `def:photon`

Basis order of `pairNFChiral`: `[1, σ₀, σ₁, L₋ = σ₁σ₀, L₊ = σ₀σ₁, e⁻ = σ₀σ₁σ₀]`. -/

open QOU.QuarkState in
/-- A single `def:photon` has no `L₋` and no `e⁻` component. -/
theorem single_photon_no_Lminus_no_eminus (h a0 a1 a2 : R) :
    photon h a0 a1 a2 3 = 0 ∧ photon h a0 a1 a2 5 = 0 := by
  rw [photon_eq]; simp

open QOU.QuarkState in
/-- **The chiral pair from the full product.** `γ(a, b, 0)·γ(1, 1, 0)` has
    `L₊`-coefficient `a` and `L₋`-coefficient `b`, for every `h`. -/
theorem gamma_gamma_chirality_surjective_NF (h a b : R) :
    pairNFChiral h a b 0 1 1 0 4 = a ∧ pairNFChiral h a b 0 1 1 0 3 = b := by
  rw [pairNFChiral_eq]; constructor <;> simp

open QOU.QuarkState in
/-- **`e⁻` is reached.** `γ(0, 0, 1)·γ(1, 0, 0)` has `e⁻`-coefficient `1`: the
    vertex `σ₀σ₁⁻¹` times `σ₀` carries `σ₀σ₁σ₀`. -/
theorem gamma_gamma_reaches_eminus_NF (h : R) : pairNFChiral h 0 0 1 1 0 0 5 = 1 := by
  rw [pairNFChiral_eq]; simp

open QOU.QuarkState in
/-- **The two-photon products span `H₃(q)`.** Every coordinate vector of the
    six-word basis `[1, σ₀, σ₁, L₋, L₊, e⁻]` is an `R`-linear combination of
    normal forms `NF(γ(φ)·γ(ψ))`, so their span is the whole module `Fin 6 → R`.
    Witnesses (`P(φ; ψ)` for `pairNFChiral h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁`):
    `1 = P(0;0)`, `σ₀ = P(1,0,0;0) − 1`, `σ₁ = P(0,1,0;0) − 1`,
    `L₋ = P(0,1,0;1,0,0) − 1 − σ₀ − σ₁`, `L₊ = P(1,0,0;0,1,0) − 1 − σ₀ − σ₁`,
    `e⁻ = P(0,0,1;1,0,0) − (1 − h)·1 − (1 − h − h²)·σ₀ − L₊`. -/
theorem gamma_gamma_span_top (h : R) :
    Submodule.span R (Set.range fun p : Fin 6 → R =>
      pairNFChiral h (p 0) (p 1) (p 2) (p 3) (p 4) (p 5)) = ⊤ := by
  set S := Submodule.span R (Set.range fun p : Fin 6 → R =>
      pairNFChiral h (p 0) (p 1) (p 2) (p 3) (p 4) (p 5)) with hS
  have mem : ∀ a0 a1 a2 b0 b1 b2 : R, pairNFChiral h a0 a1 a2 b0 b1 b2 ∈ S := by
    intro a0 a1 a2 b0 b1 b2
    exact Submodule.subset_span ⟨![a0, a1, a2, b0, b1, b2], by simp⟩
  have E0 : (![1, 0, 0, 0, 0, 0] : Fin 6 → R) ∈ S := by
    have := mem 0 0 0 0 0 0
    rw [pairNFChiral_eq] at this; simpa using this
  have E1 : (![0, 1, 0, 0, 0, 0] : Fin 6 → R) ∈ S := by
    have h1 := S.sub_mem (mem 1 0 0 0 0 0) E0
    rw [pairNFChiral_eq] at h1
    convert h1 using 1; funext i; fin_cases i <;> simp
  have E2 : (![0, 0, 1, 0, 0, 0] : Fin 6 → R) ∈ S := by
    have h1 := S.sub_mem (mem 0 1 0 0 0 0) E0
    rw [pairNFChiral_eq] at h1
    convert h1 using 1; funext i; fin_cases i <;> simp
  have E3 : (![0, 0, 0, 1, 0, 0] : Fin 6 → R) ∈ S := by
    have h1 := S.sub_mem (S.sub_mem (S.sub_mem (mem 0 1 0 1 0 0) E0) E1) E2
    rw [pairNFChiral_eq] at h1
    convert h1 using 1; funext i; fin_cases i <;> simp
  have E4 : (![0, 0, 0, 0, 1, 0] : Fin 6 → R) ∈ S := by
    have h1 := S.sub_mem (S.sub_mem (S.sub_mem (mem 1 0 0 0 1 0) E0) E1) E2
    rw [pairNFChiral_eq] at h1
    convert h1 using 1; funext i; fin_cases i <;> simp
  have E5 : (![0, 0, 0, 0, 0, 1] : Fin 6 → R) ∈ S := by
    have h1 := S.sub_mem (S.sub_mem (S.sub_mem (mem 0 0 1 1 0 0)
      (S.smul_mem (1 - h) E0)) (S.smul_mem (1 - h - h ^ 2) E1)) E4
    rw [pairNFChiral_eq] at h1
    convert h1 using 1; funext i; fin_cases i <;> simp
  rw [eq_top_iff]
  intro v _
  have hv : v = v 0 • (![1, 0, 0, 0, 0, 0] : Fin 6 → R) + v 1 • ![0, 1, 0, 0, 0, 0]
      + v 2 • ![0, 0, 1, 0, 0, 0] + v 3 • ![0, 0, 0, 1, 0, 0]
      + v 4 • ![0, 0, 0, 0, 1, 0] + v 5 • ![0, 0, 0, 0, 0, 1] := by
    funext i; fin_cases i <;> simp
  rw [hv]
  exact S.add_mem (S.add_mem (S.add_mem (S.add_mem (S.add_mem
    (S.smul_mem _ E0) (S.smul_mem _ E1)) (S.smul_mem _ E2)) (S.smul_mem _ E3))
    (S.smul_mem _ E4)) (S.smul_mem _ E5)

end PairNFChiral

/-! ### Full associative `R`-algebra model `H3Elem R h` of `H₃(R, h)` -/

/-- Elements of the 6-dimensional three-strand Iwahori–Hecke algebra `H₃(R, h)`
    in the Coxeter / Gröbner–Shirshov normal-form basis
    `{1, σ₀, σ₁, Lplus = σ₀σ₁, Lminus = σ₁σ₀, eminus = σ₀σ₁σ₀}` with quadratic
    parameter `h` (`σᵢ² = h·σᵢ + 1`). -/
@[ext]
structure H3Elem (R : Type*) (h : R) where
  c1  : R
  c0  : R
  c1s : R
  cLp : R
  cLm : R
  ce  : R
  deriving DecidableEq

namespace H3Elem

section Instances

variable {R : Type*} [CommRing R] {h : R}

instance : Zero (H3Elem R h) := ⟨⟨0, 0, 0, 0, 0, 0⟩⟩
instance : One (H3Elem R h) := ⟨⟨1, 0, 0, 0, 0, 0⟩⟩
instance : Add (H3Elem R h) :=
  ⟨fun x y => ⟨x.c1 + y.c1, x.c0 + y.c0, x.c1s + y.c1s,
               x.cLp + y.cLp, x.cLm + y.cLm, x.ce + y.ce⟩⟩
instance : Neg (H3Elem R h) :=
  ⟨fun x => ⟨-x.c1, -x.c0, -x.c1s, -x.cLp, -x.cLm, -x.ce⟩⟩
instance : Sub (H3Elem R h) :=
  ⟨fun x y => ⟨x.c1 - y.c1, x.c0 - y.c0, x.c1s - y.c1s,
               x.cLp - y.cLp, x.cLm - y.cLm, x.ce - y.ce⟩⟩
instance : SMul R (H3Elem R h) :=
  ⟨fun r x => ⟨r * x.c1, r * x.c0, r * x.c1s, r * x.cLp, r * x.cLm, r * x.ce⟩⟩
instance : NatCast (H3Elem R h) := ⟨fun n => ⟨n, 0, 0, 0, 0, 0⟩⟩
instance : IntCast (H3Elem R h) := ⟨fun n => ⟨n, 0, 0, 0, 0, 0⟩⟩

@[simp] lemma natCast_c1  (n : ℕ) : (n : H3Elem R h).c1  = n := rfl
@[simp] lemma natCast_c0  (n : ℕ) : (n : H3Elem R h).c0  = 0 := rfl
@[simp] lemma natCast_c1s (n : ℕ) : (n : H3Elem R h).c1s = 0 := rfl
@[simp] lemma natCast_cLp (n : ℕ) : (n : H3Elem R h).cLp = 0 := rfl
@[simp] lemma natCast_cLm (n : ℕ) : (n : H3Elem R h).cLm = 0 := rfl
@[simp] lemma natCast_ce  (n : ℕ) : (n : H3Elem R h).ce  = 0 := rfl

@[simp] lemma intCast_c1  (n : ℤ) : (n : H3Elem R h).c1  = n := rfl
@[simp] lemma intCast_c0  (n : ℤ) : (n : H3Elem R h).c0  = 0 := rfl
@[simp] lemma intCast_c1s (n : ℤ) : (n : H3Elem R h).c1s = 0 := rfl
@[simp] lemma intCast_cLp (n : ℤ) : (n : H3Elem R h).cLp = 0 := rfl
@[simp] lemma intCast_cLm (n : ℤ) : (n : H3Elem R h).cLm = 0 := rfl
@[simp] lemma intCast_ce  (n : ℤ) : (n : H3Elem R h).ce  = 0 := rfl

@[simp] lemma zero_c1  : (0 : H3Elem R h).c1  = 0 := rfl
@[simp] lemma zero_c0  : (0 : H3Elem R h).c0  = 0 := rfl
@[simp] lemma zero_c1s : (0 : H3Elem R h).c1s = 0 := rfl
@[simp] lemma zero_cLp : (0 : H3Elem R h).cLp = 0 := rfl
@[simp] lemma zero_cLm : (0 : H3Elem R h).cLm = 0 := rfl
@[simp] lemma zero_ce  : (0 : H3Elem R h).ce  = 0 := rfl

@[simp] lemma one_c1  : (1 : H3Elem R h).c1  = 1 := rfl
@[simp] lemma one_c0  : (1 : H3Elem R h).c0  = 0 := rfl
@[simp] lemma one_c1s : (1 : H3Elem R h).c1s = 0 := rfl
@[simp] lemma one_cLp : (1 : H3Elem R h).cLp = 0 := rfl
@[simp] lemma one_cLm : (1 : H3Elem R h).cLm = 0 := rfl
@[simp] lemma one_ce  : (1 : H3Elem R h).ce  = 0 := rfl

@[simp] lemma add_c1  (x y : H3Elem R h) : (x + y).c1  = x.c1  + y.c1  := rfl
@[simp] lemma add_c0  (x y : H3Elem R h) : (x + y).c0  = x.c0  + y.c0  := rfl
@[simp] lemma add_c1s (x y : H3Elem R h) : (x + y).c1s = x.c1s + y.c1s := rfl
@[simp] lemma add_cLp (x y : H3Elem R h) : (x + y).cLp = x.cLp + y.cLp := rfl
@[simp] lemma add_cLm (x y : H3Elem R h) : (x + y).cLm = x.cLm + y.cLm := rfl
@[simp] lemma add_ce  (x y : H3Elem R h) : (x + y).ce  = x.ce  + y.ce  := rfl

@[simp] lemma neg_c1  (x : H3Elem R h) : (-x).c1  = -x.c1  := rfl
@[simp] lemma neg_c0  (x : H3Elem R h) : (-x).c0  = -x.c0  := rfl
@[simp] lemma neg_c1s (x : H3Elem R h) : (-x).c1s = -x.c1s := rfl
@[simp] lemma neg_cLp (x : H3Elem R h) : (-x).cLp = -x.cLp := rfl
@[simp] lemma neg_cLm (x : H3Elem R h) : (-x).cLm = -x.cLm := rfl
@[simp] lemma neg_ce  (x : H3Elem R h) : (-x).ce  = -x.ce  := rfl

@[simp] lemma sub_c1  (x y : H3Elem R h) : (x - y).c1  = x.c1  - y.c1  := rfl
@[simp] lemma sub_c0  (x y : H3Elem R h) : (x - y).c0  = x.c0  - y.c0  := rfl
@[simp] lemma sub_c1s (x y : H3Elem R h) : (x - y).c1s = x.c1s - y.c1s := rfl
@[simp] lemma sub_cLp (x y : H3Elem R h) : (x - y).cLp = x.cLp - y.cLp := rfl
@[simp] lemma sub_cLm (x y : H3Elem R h) : (x - y).cLm = x.cLm - y.cLm := rfl
@[simp] lemma sub_ce  (x y : H3Elem R h) : (x - y).ce  = x.ce  - y.ce  := rfl

@[simp] lemma smul_c1  (r : R) (x : H3Elem R h) : (r • x).c1  = r * x.c1  := rfl
@[simp] lemma smul_c0  (r : R) (x : H3Elem R h) : (r • x).c0  = r * x.c0  := rfl
@[simp] lemma smul_c1s (r : R) (x : H3Elem R h) : (r • x).c1s = r * x.c1s := rfl
@[simp] lemma smul_cLp (r : R) (x : H3Elem R h) : (r • x).cLp = r * x.cLp := rfl
@[simp] lemma smul_cLm (r : R) (x : H3Elem R h) : (r • x).cLm = r * x.cLm := rfl
@[simp] lemma smul_ce  (r : R) (x : H3Elem R h) : (r • x).ce  = r * x.ce  := rfl

/-- Right multiplication by `σ₀` in the normal-form basis
    `{1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}` under `σ₀² = h·σ₀ + 1` and
    `σ₁σ₀σ₁ = σ₀σ₁σ₀`. -/
def mulRightS0 (x : H3Elem R h) : H3Elem R h :=
  ⟨x.c0, x.c1 + h * x.c0, x.cLm, x.ce, x.c1s + h * x.cLm, x.cLp + h * x.ce⟩

/-- Right multiplication by `σ₁` in the normal-form basis
    `{1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}` under `σ₁² = h·σ₁ + 1` and
    `σ₁σ₀σ₁ = σ₀σ₁σ₀`. -/
def mulRightS1 (x : H3Elem R h) : H3Elem R h :=
  ⟨x.c1s, x.cLp, x.c1 + h * x.c1s, x.c0 + h * x.cLp, x.ce, x.cLm + h * x.ce⟩

/-- Multiplication in `H₃(R, h)` obtained by composing right generator actions
    along the Coxeter reduced words `(), (0), (1), (0,1), (1,0), (0,1,0)`. -/
def mul (x y : H3Elem R h) : H3Elem R h :=
  let r0   := mulRightS0 x
  let r1   := mulRightS1 x
  let r01  := mulRightS1 r0
  let r10  := mulRightS0 r1
  let r010 := mulRightS0 r01
  ⟨y.c1 * x.c1  + y.c0 * r0.c1  + y.c1s * r1.c1  + y.cLp * r01.c1  + y.cLm * r10.c1  + y.ce * r010.c1,
   y.c1 * x.c0  + y.c0 * r0.c0  + y.c1s * r1.c0  + y.cLp * r01.c0  + y.cLm * r10.c0  + y.ce * r010.c0,
   y.c1 * x.c1s + y.c0 * r0.c1s + y.c1s * r1.c1s + y.cLp * r01.c1s + y.cLm * r10.c1s + y.ce * r010.c1s,
   y.c1 * x.cLp + y.c0 * r0.cLp + y.c1s * r1.cLp + y.cLp * r01.cLp + y.cLm * r10.cLp + y.ce * r010.cLp,
   y.c1 * x.cLm + y.c0 * r0.cLm + y.c1s * r1.cLm + y.cLp * r01.cLm + y.cLm * r10.cLm + y.ce * r010.cLm,
   y.c1 * x.ce  + y.c0 * r0.ce  + y.c1s * r1.ce  + y.cLp * r01.ce  + y.cLm * r10.ce  + y.ce * r010.ce⟩

instance : Mul (H3Elem R h) := ⟨mul⟩

@[simp] lemma mul_c1  (x y : H3Elem R h) : (x * y).c1  = (mul x y).c1  := rfl
@[simp] lemma mul_c0  (x y : H3Elem R h) : (x * y).c0  = (mul x y).c0  := rfl
@[simp] lemma mul_c1s (x y : H3Elem R h) : (x * y).c1s = (mul x y).c1s := rfl
@[simp] lemma mul_cLp (x y : H3Elem R h) : (x * y).cLp = (mul x y).cLp := rfl
@[simp] lemma mul_cLm (x y : H3Elem R h) : (x * y).cLm = (mul x y).cLm := rfl
@[simp] lemma mul_ce  (x y : H3Elem R h) : (x * y).ce  = (mul x y).ce  := rfl

private lemma mul_assoc' (a b c : H3Elem R h) : a * b * c = a * (b * c) := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma one_mul' (a : H3Elem R h) : (1 : H3Elem R h) * a = a := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma mul_one' (a : H3Elem R h) : a * (1 : H3Elem R h) = a := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma left_distrib' (a b c : H3Elem R h) : a * (b + c) = a * b + a * c := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma right_distrib' (a b c : H3Elem R h) : (a + b) * c = a * c + b * c := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma zero_mul' (a : H3Elem R h) : (0 : H3Elem R h) * a = 0 := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma mul_zero' (a : H3Elem R h) : a * (0 : H3Elem R h) = 0 := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

instance : Ring (H3Elem R h) where
  add := (· + ·)
  add_assoc a b c := by ext <;> exact add_assoc _ _ _
  zero := 0
  zero_add a := by ext <;> exact zero_add _
  add_zero a := by ext <;> exact add_zero _
  nsmul n x := ⟨n • x.c1, n • x.c0, n • x.c1s, n • x.cLp, n • x.cLm, n • x.ce⟩
  nsmul_zero x := by ext <;> exact zero_nsmul _
  nsmul_succ n x := by ext <;> exact succ_nsmul _ n
  zsmul n x := ⟨n • x.c1, n • x.c0, n • x.c1s, n • x.cLp, n • x.cLm, n • x.ce⟩
  zsmul_zero' x := by ext <;> exact zero_zsmul _
  zsmul_succ' n x := by ext <;> exact SubNegMonoid.zsmul_succ' n _
  zsmul_neg' n x := by ext <;> exact SubNegMonoid.zsmul_neg' n _
  neg := Neg.neg
  sub := (· - ·)
  neg_add_cancel a := by ext <;> exact neg_add_cancel _
  sub_eq_add_neg a b := by ext <;> exact sub_eq_add_neg _ _
  add_comm a b := by ext <;> exact add_comm _ _
  mul := (· * ·)
  one := 1
  mul_assoc := mul_assoc'
  one_mul := one_mul'
  mul_one := mul_one'
  left_distrib := left_distrib'
  right_distrib := right_distrib'
  zero_mul := zero_mul'
  mul_zero := mul_zero'
  natCast := Nat.cast
  natCast_zero := by ext <;> simp
  natCast_succ n := by ext <;> simp
  intCast := Int.cast
  intCast_ofNat n := by ext <;> simp
  intCast_negSucc n := by ext <;> simp [Int.negSucc_eq]

instance : Module R (H3Elem R h) where
  one_smul x := by ext <;> exact one_mul _
  mul_smul r s x := by ext <;> exact mul_assoc _ _ _
  smul_zero r := by ext <;> exact mul_zero _
  smul_add r x y := by ext <;> exact mul_add _ _ _
  add_smul r s x := by ext <;> exact add_mul _ _ _
  zero_smul x := by ext <;> exact zero_mul _

private lemma smul_mul_assoc' (r : R) (x y : H3Elem R h) : (r • x) * y = r • (x * y) := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma mul_smul_comm' (r : R) (x y : H3Elem R h) : x * (r • y) = r • (x * y) := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

instance : Algebra R (H3Elem R h) :=
  Algebra.ofModule smul_mul_assoc' mul_smul_comm'

end Instances

end H3Elem

/-! ### Basis elements, Hecke relations, and the 4-term photon in `H3Elem R h` -/

section Photons

variable {R : Type*} [CommRing R]

/-- First braid generator `σ₀ ∈ H₃(R, h)`. -/
def σ₀ {h : R} : H3Elem R h := ⟨0, 1, 0, 0, 0, 0⟩

/-- Second braid generator `σ₁ ∈ H₃(R, h)`. -/
def σ₁ {h : R} : H3Elem R h := ⟨0, 0, 1, 0, 0, 0⟩

/-- Positive-chirality Hopf operator `L₊ = σ₀σ₁ ∈ H₃(R, h)`. -/
def Lplus {h : R} : H3Elem R h := ⟨0, 0, 0, 1, 0, 0⟩

/-- Negative-chirality Hopf operator `L₋ = σ₁σ₀ ∈ H₃(R, h)`. -/
def Lminus {h : R} : H3Elem R h := ⟨0, 0, 0, 0, 1, 0⟩

/-- Longest Coxeter element / electron braid operator `e⁻ = σ₀σ₁σ₀ ∈ H₃(R, h)`. -/
def eminus {h : R} : H3Elem R h := ⟨0, 0, 0, 0, 0, 1⟩

/-- Inverse generator `σ₁⁻¹ := σ₁ - h·1 ∈ H₃(R, h)`. -/
def σ₁Inv {h : R} : H3Elem R h := σ₁ - h • 1

/-- Basis decomposition of any `x : H3Elem R h`. -/
theorem decomp {h : R} (x : H3Elem R h) :
    x = x.c1 • (1 : H3Elem R h) + x.c0 • σ₀ + x.c1s • σ₁ +
        x.cLp • Lplus + x.cLm • Lminus + x.ce • eminus := by
  ext <;> simp [σ₀, σ₁, Lplus, Lminus, eminus]

theorem Lplus_eq_mul (h : R) : (Lplus : H3Elem R h) = σ₀ * σ₁ := by
  ext <;> dsimp [Lplus, σ₀, σ₁, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

theorem Lminus_eq_mul (h : R) : (Lminus : H3Elem R h) = σ₁ * σ₀ := by
  ext <;> dsimp [Lminus, σ₀, σ₁, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

theorem eminus_eq_mul (h : R) : (eminus : H3Elem R h) = σ₀ * σ₁ * σ₀ := by
  ext <;> dsimp [eminus, σ₀, σ₁, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- Quadratic Hecke relation for `σ₀`: `σ₀² = h·σ₀ + 1`. -/
theorem sigma0_sq (h : R) : (σ₀ : H3Elem R h) * σ₀ = h • σ₀ + 1 := by
  ext <;> dsimp [σ₀, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- Quadratic Hecke relation for `σ₁`: `σ₁² = h·σ₁ + 1`. -/
theorem sigma1_sq (h : R) : (σ₁ : H3Elem R h) * σ₁ = h • σ₁ + 1 := by
  ext <;> dsimp [σ₁, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- Three-strand braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁` in `H₃(R, h)`. -/
theorem braid_rel (h : R) :
    (σ₀ : H3Elem R h) * σ₁ * σ₀ = σ₁ * σ₀ * σ₁ := by
  ext <;> dsimp [σ₀, σ₁, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- Right inverse identity `σ₁ · σ₁⁻¹ = 1`. -/
theorem sigma1_mul_inv (h : R) : (σ₁ : H3Elem R h) * σ₁Inv = 1 := by
  ext <;> dsimp [σ₁, σ₁Inv, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- Left inverse identity `σ₁⁻¹ · σ₁ = 1`. -/
theorem inv_mul_sigma1 (h : R) : (σ₁Inv : H3Elem R h) * σ₁ = 1 := by
  ext <;> dsimp [σ₁, σ₁Inv, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- **Chiral Borromean-step reduction:** `σ₀ · σ₁⁻¹ = L₊ - h·σ₀`. -/
theorem borromeanStep_eq (h : R) :
    (σ₀ : H3Elem R h) * σ₁Inv = Lplus - h • σ₀ := by
  ext <;> dsimp [σ₀, σ₁, σ₁Inv, Lplus, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- **The 4-term colored photon** (`def:photon`) in `H₃(R, h)`:
    `γ = 1 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·(σ₀·σ₁⁻¹)`. -/
def h3Photon (h φ₀ φ₁ φ₀₁ : R) : H3Elem R h :=
  1 + φ₀ • σ₀ + φ₁ • σ₁ + φ₀₁ • (σ₀ * σ₁Inv)

/-- Every single photon has zero `L₋ = σ₁σ₀` component. -/
@[simp] theorem h3Photon_cLm (h φ₀ φ₁ φ₀₁ : R) :
    (h3Photon h φ₀ φ₁ φ₀₁).cLm = 0 := by
  dsimp [h3Photon, σ₀, σ₁, σ₁Inv, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1]
  ring

/-- Every single photon has zero `e⁻ = σ₀σ₁σ₀` component. -/
@[simp] theorem h3Photon_ce (h φ₀ φ₁ φ₀₁ : R) :
    (h3Photon h φ₀ φ₁ φ₀₁).ce = 0 := by
  dsimp [h3Photon, σ₀, σ₁, σ₁Inv, H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1]
  ring

/-- **Exact 3-term normal-form formula** (`φ₀₁ = ψ₀₁ = 0`):
    `(1 + φ₀σ₀ + φ₁σ₁)(1 + ψ₀σ₀ + ψ₁σ₁)` reduces in `H₃(R, h)` to
    `(1 + φ₀ψ₀ + φ₁ψ₁)·1 + (φ₀ + ψ₀ + φ₀ψ₀h)·σ₀ + (φ₁ + ψ₁ + φ₁ψ₁h)·σ₁
     + φ₀ψ₁·L₊ + φ₁ψ₀·L₋`. -/
theorem h3Photon_mul_threeTerm (h φ₀ φ₁ ψ₀ ψ₁ : R) :
    h3Photon h φ₀ φ₁ 0 * h3Photon h ψ₀ ψ₁ 0 =
      ⟨1 + φ₀ * ψ₀ + φ₁ * ψ₁,
       φ₀ + ψ₀ + φ₀ * ψ₀ * h,
       φ₁ + ψ₁ + φ₁ * ψ₁ * h,
       φ₀ * ψ₁,
       φ₁ * ψ₀,
       0⟩ := by
  ext <;> dsimp [h3Photon, σ₀, σ₁, σ₁Inv,
    H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- **Opening of the sixth basis operator `e⁻`:**
    `(σ₀ · σ₁⁻¹) · σ₀ = e⁻ - h²·σ₀ - h·1`. -/
theorem borromeanStep_mul_sigma0 (h : R) :
    ((σ₀ : H3Elem R h) * σ₁Inv) * σ₀ = eminus - (h ^ 2) • σ₀ - h • (1 : H3Elem R h) := by
  ext <;> dsimp [σ₀, σ₁, σ₁Inv, eminus,
    H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- **Exact `e⁻` coordinate of the general 4-term photon product:**
    the `(σ₀·σ₁⁻¹)²` term carries zero `e⁻` component, so `ce = φ₀₁·ψ₀ + φ₁·ψ₀₁`. -/
theorem h3Photon_mul_ce (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R) :
    (h3Photon h φ₀ φ₁ φ₀₁ * h3Photon h ψ₀ ψ₁ ψ₀₁).ce =
      φ₀₁ * ψ₀ + φ₁ * ψ₀₁ := by
  dsimp [h3Photon, σ₀, σ₁, σ₁Inv,
    H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1]
  ring

/-- The Borromean-step operator `V = σ₀·σ₁⁻¹ ∈ H₃(R, h)`. -/
def borromeanStep (h : R) : H3Elem R h := σ₀ * σ₁Inv

theorem borromeanStep_coords (h : R) :
    borromeanStep h = ⟨0, -h, 0, 1, 0, 0⟩ := by
  ext <;> dsimp [borromeanStep, σ₀, σ₁, σ₁Inv,
    H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

theorem borromeanStep_sq_coords (h : R) :
    (borromeanStep h) ^ (2 : ℕ) = ⟨h ^ 2, h ^ 3, -h, -(h ^ 2), 1, 0⟩ := by
  rw [sq, borromeanStep_coords]
  ext <;> dsimp [H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- Cubic relation of the Borromean step `V = σ₀·σ₁⁻¹` in `H₃(R, h)`:
    `V³ = 1 + h²·V - h²·V²`. -/
theorem borromeanStep_cubed (h : R) :
    (borromeanStep h) ^ (3 : ℕ) =
      1 + (h ^ (2 : ℕ) : R) • borromeanStep h -
        (h ^ (2 : ℕ) : R) • ((borromeanStep h) ^ (2 : ℕ)) := by
  rw [show (3 : ℕ) = 2 + 1 from rfl, pow_succ, borromeanStep_sq_coords, borromeanStep_coords]
  ext <;> dsimp [H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- Product of two pure fourth-term photons `(1 + a·V)(1 + b·V)`. -/
theorem h3Photon_mul_pureFourth (h a b : R) :
    h3Photon h 0 0 a * h3Photon h 0 0 b =
      1 + (a + b) • borromeanStep h +
        (a * b) • ((borromeanStep h) ^ (2 : ℕ)) := by
  have hp : ∀ c : R, h3Photon h 0 0 c = 1 + c • borromeanStep h := fun c => by
    ext <;> simp [h3Photon, borromeanStep]
  rw [hp a, hp b, borromeanStep_sq_coords, borromeanStep_coords]
  ext <;> dsimp [H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring

/-- **Borromean nucleon braid factorization** from conjugate pure fourth-term
    photons: whenever `q * q_inv = 1`, setting `h = q - q_inv` gives
    `(1 + qh·(σ₀σ₁⁻¹)) · (1 - q⁻¹h·(σ₀σ₁⁻¹)) = (σ₀σ₁⁻¹)³`. -/
theorem borromean_braid_factorization {q q_inv : R} (hq : q * q_inv = 1) :
    h3Photon (q - q_inv) 0 0 (q * (q - q_inv)) *
      h3Photon (q - q_inv) 0 0 (-q_inv * (q - q_inv)) =
      (borromeanStep (q - q_inv)) ^ (3 : ℕ) := by
  rw [h3Photon_mul_pureFourth, borromeanStep_cubed]
  have hsum : q * (q - q_inv) + (-q_inv * (q - q_inv)) = (q - q_inv) ^ (2 : ℕ) := by ring
  have hprod : (q * (q - q_inv)) * (-q_inv * (q - q_inv)) = -((q - q_inv) ^ (2 : ℕ)) := by
    linear_combination -((q - q_inv) ^ (2 : ℕ)) * hq
  rw [hsum, hprod, neg_smul, ← sub_eq_add_neg]

/-- Set of all two-photon products `γ₁ · γ₂` in `H₃(R, h)`. -/
def twoPhotonProducts (h : R) : Set (H3Elem R h) :=
  Set.range (fun p : (R × R × R) × (R × R × R) =>
    h3Photon h p.1.1 p.1.2.1 p.1.2.2 *
      h3Photon h p.2.1 p.2.2.1 p.2.2.2)

private lemma mul_mem_span (h φ₀ φ₁ φ₀₁ ψ₀ ψ₁ ψ₀₁ : R) :
    h3Photon h φ₀ φ₁ φ₀₁ * h3Photon h ψ₀ ψ₁ ψ₀₁ ∈
      Submodule.span R (twoPhotonProducts h) :=
  Submodule.subset_span ⟨((φ₀, φ₁, φ₀₁), (ψ₀, ψ₁, ψ₀₁)), rfl⟩

theorem one_mem_twoPhoton_span (h : R) :
    (1 : H3Elem R h) ∈ Submodule.span R (twoPhotonProducts h) := by
  have hm := mul_mem_span h 0 0 0 0 0 0
  have heq : h3Photon h 0 0 0 * h3Photon h 0 0 0 = (1 : H3Elem R h) := by
    ext <;> simp [h3Photon_mul_threeTerm]
  rwa [heq] at hm

theorem sigma0_mem_twoPhoton_span (h : R) :
    (σ₀ : H3Elem R h) ∈ Submodule.span R (twoPhotonProducts h) := by
  have hm := Submodule.sub_mem _ (mul_mem_span h 1 0 0 0 0 0) (one_mem_twoPhoton_span h)
  have heq : h3Photon h 1 0 0 * h3Photon h 0 0 0 - 1 = (σ₀ : H3Elem R h) := by
    ext <;> simp [h3Photon_mul_threeTerm, σ₀]
  rwa [heq] at hm

theorem sigma1_mem_twoPhoton_span (h : R) :
    (σ₁ : H3Elem R h) ∈ Submodule.span R (twoPhotonProducts h) := by
  have hm := Submodule.sub_mem _ (mul_mem_span h 0 1 0 0 0 0) (one_mem_twoPhoton_span h)
  have heq : h3Photon h 0 1 0 * h3Photon h 0 0 0 - 1 = (σ₁ : H3Elem R h) := by
    ext <;> simp [h3Photon_mul_threeTerm, σ₁]
  rwa [heq] at hm

theorem Lplus_mem_twoPhoton_span (h : R) :
    (Lplus : H3Elem R h) ∈ Submodule.span R (twoPhotonProducts h) := by
  have hbase := Submodule.add_mem _
    (Submodule.add_mem _ (one_mem_twoPhoton_span h) (sigma0_mem_twoPhoton_span h))
    (sigma1_mem_twoPhoton_span h)
  have hm := Submodule.sub_mem _ (mul_mem_span h 1 0 0 0 1 0) hbase
  have heq :
      h3Photon h 1 0 0 * h3Photon h 0 1 0 - (1 + σ₀ + σ₁) = (Lplus : H3Elem R h) := by
    ext <;> simp [h3Photon_mul_threeTerm, σ₀, σ₁, Lplus]
  rwa [heq] at hm

theorem Lminus_mem_twoPhoton_span (h : R) :
    (Lminus : H3Elem R h) ∈ Submodule.span R (twoPhotonProducts h) := by
  have hbase := Submodule.add_mem _
    (Submodule.add_mem _ (one_mem_twoPhoton_span h) (sigma0_mem_twoPhoton_span h))
    (sigma1_mem_twoPhoton_span h)
  have hm := Submodule.sub_mem _ (mul_mem_span h 0 1 0 1 0 0) hbase
  have heq :
      h3Photon h 0 1 0 * h3Photon h 1 0 0 - (1 + σ₀ + σ₁) = (Lminus : H3Elem R h) := by
    ext <;> simp [h3Photon_mul_threeTerm, σ₀, σ₁, Lminus]
  rwa [heq] at hm

theorem eminus_mem_twoPhoton_span (h : R) :
    (eminus : H3Elem R h) ∈ Submodule.span R (twoPhotonProducts h) := by
  have hbase := Submodule.add_mem _
    (Submodule.add_mem _
      (Submodule.smul_mem _ (1 - h) (one_mem_twoPhoton_span h))
      (Submodule.smul_mem _ (1 - h - h ^ 2) (sigma0_mem_twoPhoton_span h)))
    (Lplus_mem_twoPhoton_span h)
  have hm := Submodule.sub_mem _ (mul_mem_span h 0 0 1 1 0 0) hbase
  have heq :
      h3Photon h 0 0 1 * h3Photon h 1 0 0 -
        ((1 - h) • (1 : H3Elem R h) + (1 - h - h ^ 2) • σ₀ + Lplus) =
        (eminus : H3Elem R h) := by
    ext <;> dsimp [h3Photon, σ₀, σ₁, σ₁Inv, Lplus, eminus,
      H3Elem.mul, H3Elem.mulRightS0, H3Elem.mulRightS1] <;> ring
  rwa [heq] at hm

/-- Every element of `H₃(R, h)` lies in the `R`-linear span of two-photon
    products, over any commutative ring `R` (no field or invertibility assumption). -/
theorem mem_h3Photon_pair_span (h : R) (x : H3Elem R h) :
    x ∈ Submodule.span R (Set.range (fun p : (R × R × R) × (R × R × R) =>
      h3Photon h p.1.1 p.1.2.1 p.1.2.2 *
        h3Photon h p.2.1 p.2.2.1 p.2.2.2)) := by
  let S := Submodule.span R (twoPhotonProducts h)
  change x ∈ S
  rw [decomp x]
  have h1 : x.c1 • (1 : H3Elem R h) ∈ S :=
    Submodule.smul_mem S _ (one_mem_twoPhoton_span h)
  have h2 : x.c0 • (σ₀ : H3Elem R h) ∈ S :=
    Submodule.smul_mem S _ (sigma0_mem_twoPhoton_span h)
  have h3 : x.c1s • (σ₁ : H3Elem R h) ∈ S :=
    Submodule.smul_mem S _ (sigma1_mem_twoPhoton_span h)
  have h4 : x.cLp • (Lplus : H3Elem R h) ∈ S :=
    Submodule.smul_mem S _ (Lplus_mem_twoPhoton_span h)
  have h5 : x.cLm • (Lminus : H3Elem R h) ∈ S :=
    Submodule.smul_mem S _ (Lminus_mem_twoPhoton_span h)
  have h6 : x.ce • (eminus : H3Elem R h) ∈ S :=
    Submodule.smul_mem S _ (eminus_mem_twoPhoton_span h)
  exact S.add_mem (S.add_mem (S.add_mem (S.add_mem (S.add_mem h1 h2) h3) h4) h5) h6

/-- **The `R`-linear span of two-photon products in `H3Elem R h` is all of `H₃(R, h)`.** -/
theorem h3Photon_pair_span_top (h : R) :
    Submodule.span R (Set.range (fun p : (R × R × R) × (R × R × R) =>
      h3Photon h p.1.1 p.1.2.1 p.1.2.2 *
        h3Photon h p.2.1 p.2.2.1 p.2.2.2)) = ⊤ :=
  Submodule.eq_top_iff'.mpr (mem_h3Photon_pair_span h)

end Photons

end QOU.Archimedean.GammaGammaGeneration
