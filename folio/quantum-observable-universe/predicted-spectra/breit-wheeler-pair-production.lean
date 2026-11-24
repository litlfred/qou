/-
  Breit–Wheeler pair production (categorical), on `def:photon` and the 6D `H₃(R, h)`
  Coxeter normal-form algebra.

  The photon is `QOU.Photon.photon`:
      γ(φ) = 𝟙 + φ₀•σ₀ + φ₁•σ₁ + φ₀₁•σ₀σ₁⁻¹
  (`def:photon`: the fourth term is the chiral vertex σ₀σ₁⁻¹).

  What this file establishes over generic coefficient rings (§7c):
  1. Named linear and circular polarisation specialisations of `QOU.Photon.photon`
     (`φ₀₁ = 0`) and bare-pair fusion `γ(0)·γ(0) = 𝟙` (`breit_wheeler_pair_production`).
  2. The full 6-dimensional three-strand Iwahori–Hecke algebra `BWHecke3 R h` on the
     Coxeter normal-form basis `{1, σ₀, σ₁, L₊ = σ₀σ₁, L₋ = σ₁σ₀, Tw0 = σ₀σ₁σ₀}`:
     - 3-term Breit–Wheeler normal form (`φ₀₁ = ψ₀₁ = 0`),
     - 4-term longest-word (`e⁻ = σ₀σ₁σ₀`) channel `ce = φ₀₁·ψ₀ + φ₁·ψ₀₁`,
     - color-swap exchange symmetry and bosonic photon-exchange symmetry of the
       chiral Hopf weight `cLp + cLm` and combined `pairThreshold`,
     - non-negativity of all active channels over any ordered commutative ring
       when weights and `h` are non-negative.

  Ref: [leitner2026] Chapter 6, §3b; def:photon, def:breit-wheeler-pair-production
  Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic
import QOU.StandardModel.Photon

namespace QOU.Archimedean

open QOU.Photon

section AbstractPhoton

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- Linear (symmetric) polarisation: `φ₀ = φ₁ = φ`, `φ₀₁ = 0`. -/
def linearColour (φ : R) : Colour R := ⟨φ, φ, 0⟩

/-- Circular polarisation, first photon: `φ₀ = s`, `φ₁ = φ₀₁ = 0`. -/
def circularColourFirst (s : R) : Colour R := ⟨s, 0, 0⟩

/-- Circular polarisation, second photon: `φ₁ = s`, `φ₀ = φ₀₁ = 0`. -/
def circularColourSecond (s : R) : Colour R := ⟨0, s, 0⟩

/-- The linear Breit–Wheeler photon is the `φ₀₁ = 0` specialisation of `def:photon`. -/
theorem photon_linearColour (σ₀ : A) (σ₁ : Aˣ) (φ : R) :
    photon σ₀ σ₁ (linearColour φ) = 1 + φ • σ₀ + φ • (σ₁ : A) :=
  photon_threeTerm σ₀ σ₁ (linearColour φ) rfl

/-- The circular Breit–Wheeler photons are `φ₀₁ = 0` specialisations of `def:photon`. -/
theorem photon_circularColour (σ₀ : A) (σ₁ : Aˣ) (s : R) :
    photon σ₀ σ₁ (circularColourFirst s) = 1 + s • σ₀ ∧
      photon σ₀ σ₁ (circularColourSecond s) = 1 + s • (σ₁ : A) := by
  constructor <;> simp [photon, circularColourFirst, circularColourSecond]

/-- **Breit–Wheeler pair production — bare pair.** Two bare photons fuse to the
    identity (the empty knot), so a bare photon pair carries no crossing at all. -/
-- Ref: [leitner2026] Chapter 6, §3b; def:photon
theorem breit_wheeler_pair_production (σ₀ : A) (σ₁ : Aˣ) :
    photon σ₀ σ₁ (bare : Colour R) * photon σ₀ σ₁ (bare : Colour R) = 1 := by
  simp [photon_bare]

end AbstractPhoton

/-! ### Full `H₃(R, h)` Breit–Wheeler normal-form algebra -/

/-- Elements of the 6-dimensional three-strand Iwahori–Hecke algebra `H₃(R, h)`
    on the Coxeter normal-form basis
    `{1, σ₀, σ₁, Lplus = σ₀σ₁, Lminus = σ₁σ₀, Tw0 = σ₀σ₁σ₀}` with `σᵢ² = h·σᵢ + 1`. -/
@[ext]
structure BWHecke3 (R : Type*) (h : R) where
  c1  : R
  c0  : R
  c1s : R
  cLp : R
  cLm : R
  ce  : R

namespace BWHecke3

section RingAlgebra

variable {R : Type*} [CommRing R] {h : R}

instance : Zero (BWHecke3 R h) := ⟨⟨0, 0, 0, 0, 0, 0⟩⟩
instance : One (BWHecke3 R h) := ⟨⟨1, 0, 0, 0, 0, 0⟩⟩
instance : Add (BWHecke3 R h) :=
  ⟨fun x y => ⟨x.c1 + y.c1, x.c0 + y.c0, x.c1s + y.c1s,
               x.cLp + y.cLp, x.cLm + y.cLm, x.ce + y.ce⟩⟩
instance : Neg (BWHecke3 R h) :=
  ⟨fun x => ⟨-x.c1, -x.c0, -x.c1s, -x.cLp, -x.cLm, -x.ce⟩⟩
instance : Sub (BWHecke3 R h) :=
  ⟨fun x y => ⟨x.c1 - y.c1, x.c0 - y.c0, x.c1s - y.c1s,
               x.cLp - y.cLp, x.cLm - y.cLm, x.ce - y.ce⟩⟩
instance : SMul R (BWHecke3 R h) :=
  ⟨fun r x => ⟨r * x.c1, r * x.c0, r * x.c1s, r * x.cLp, r * x.cLm, r * x.ce⟩⟩
instance : NatCast (BWHecke3 R h) := ⟨fun n => ⟨n, 0, 0, 0, 0, 0⟩⟩
instance : IntCast (BWHecke3 R h) := ⟨fun n => ⟨n, 0, 0, 0, 0, 0⟩⟩

@[simp] lemma natCast_c1  (n : ℕ) : (n : BWHecke3 R h).c1  = n := rfl
@[simp] lemma natCast_c0  (n : ℕ) : (n : BWHecke3 R h).c0  = 0 := rfl
@[simp] lemma natCast_c1s (n : ℕ) : (n : BWHecke3 R h).c1s = 0 := rfl
@[simp] lemma natCast_cLp (n : ℕ) : (n : BWHecke3 R h).cLp = 0 := rfl
@[simp] lemma natCast_cLm (n : ℕ) : (n : BWHecke3 R h).cLm = 0 := rfl
@[simp] lemma natCast_ce  (n : ℕ) : (n : BWHecke3 R h).ce  = 0 := rfl

@[simp] lemma intCast_c1  (n : ℤ) : (n : BWHecke3 R h).c1  = n := rfl
@[simp] lemma intCast_c0  (n : ℤ) : (n : BWHecke3 R h).c0  = 0 := rfl
@[simp] lemma intCast_c1s (n : ℤ) : (n : BWHecke3 R h).c1s = 0 := rfl
@[simp] lemma intCast_cLp (n : ℤ) : (n : BWHecke3 R h).cLp = 0 := rfl
@[simp] lemma intCast_cLm (n : ℤ) : (n : BWHecke3 R h).cLm = 0 := rfl
@[simp] lemma intCast_ce  (n : ℤ) : (n : BWHecke3 R h).ce  = 0 := rfl

@[simp] lemma zero_c1  : (0 : BWHecke3 R h).c1  = 0 := rfl
@[simp] lemma zero_c0  : (0 : BWHecke3 R h).c0  = 0 := rfl
@[simp] lemma zero_c1s : (0 : BWHecke3 R h).c1s = 0 := rfl
@[simp] lemma zero_cLp : (0 : BWHecke3 R h).cLp = 0 := rfl
@[simp] lemma zero_cLm : (0 : BWHecke3 R h).cLm = 0 := rfl
@[simp] lemma zero_ce  : (0 : BWHecke3 R h).ce  = 0 := rfl

@[simp] lemma one_c1  : (1 : BWHecke3 R h).c1  = 1 := rfl
@[simp] lemma one_c0  : (1 : BWHecke3 R h).c0  = 0 := rfl
@[simp] lemma one_c1s : (1 : BWHecke3 R h).c1s = 0 := rfl
@[simp] lemma one_cLp : (1 : BWHecke3 R h).cLp = 0 := rfl
@[simp] lemma one_cLm : (1 : BWHecke3 R h).cLm = 0 := rfl
@[simp] lemma one_ce  : (1 : BWHecke3 R h).ce  = 0 := rfl

@[simp] lemma add_c1  (x y : BWHecke3 R h) : (x + y).c1  = x.c1  + y.c1  := rfl
@[simp] lemma add_c0  (x y : BWHecke3 R h) : (x + y).c0  = x.c0  + y.c0  := rfl
@[simp] lemma add_c1s (x y : BWHecke3 R h) : (x + y).c1s = x.c1s + y.c1s := rfl
@[simp] lemma add_cLp (x y : BWHecke3 R h) : (x + y).cLp = x.cLp + y.cLp := rfl
@[simp] lemma add_cLm (x y : BWHecke3 R h) : (x + y).cLm = x.cLm + y.cLm := rfl
@[simp] lemma add_ce  (x y : BWHecke3 R h) : (x + y).ce  = x.ce  + y.ce  := rfl

@[simp] lemma neg_c1  (x : BWHecke3 R h) : (-x).c1  = -x.c1  := rfl
@[simp] lemma neg_c0  (x : BWHecke3 R h) : (-x).c0  = -x.c0  := rfl
@[simp] lemma neg_c1s (x : BWHecke3 R h) : (-x).c1s = -x.c1s := rfl
@[simp] lemma neg_cLp (x : BWHecke3 R h) : (-x).cLp = -x.cLp := rfl
@[simp] lemma neg_cLm (x : BWHecke3 R h) : (-x).cLm = -x.cLm := rfl
@[simp] lemma neg_ce  (x : BWHecke3 R h) : (-x).ce  = -x.ce  := rfl

@[simp] lemma sub_c1  (x y : BWHecke3 R h) : (x - y).c1  = x.c1  - y.c1  := rfl
@[simp] lemma sub_c0  (x y : BWHecke3 R h) : (x - y).c0  = x.c0  - y.c0  := rfl
@[simp] lemma sub_c1s (x y : BWHecke3 R h) : (x - y).c1s = x.c1s - y.c1s := rfl
@[simp] lemma sub_cLp (x y : BWHecke3 R h) : (x - y).cLp = x.cLp - y.cLp := rfl
@[simp] lemma sub_cLm (x y : BWHecke3 R h) : (x - y).cLm = x.cLm - y.cLm := rfl
@[simp] lemma sub_ce  (x y : BWHecke3 R h) : (x - y).ce  = x.ce  - y.ce  := rfl

@[simp] lemma smul_c1  (r : R) (x : BWHecke3 R h) : (r • x).c1  = r * x.c1  := rfl
@[simp] lemma smul_c0  (r : R) (x : BWHecke3 R h) : (r • x).c0  = r * x.c0  := rfl
@[simp] lemma smul_c1s (r : R) (x : BWHecke3 R h) : (r • x).c1s = r * x.c1s := rfl
@[simp] lemma smul_cLp (r : R) (x : BWHecke3 R h) : (r • x).cLp = r * x.cLp := rfl
@[simp] lemma smul_cLm (r : R) (x : BWHecke3 R h) : (r • x).cLm = r * x.cLm := rfl
@[simp] lemma smul_ce  (r : R) (x : BWHecke3 R h) : (r • x).ce  = r * x.ce  := rfl

def mulRightS0 (x : BWHecke3 R h) : BWHecke3 R h :=
  ⟨x.c0, x.c1 + h * x.c0, x.cLm, x.ce, x.c1s + h * x.cLm, x.cLp + h * x.ce⟩

def mulRightS1 (x : BWHecke3 R h) : BWHecke3 R h :=
  ⟨x.c1s, x.cLp, x.c1 + h * x.c1s, x.c0 + h * x.cLp, x.ce, x.cLm + h * x.ce⟩

def mul (x y : BWHecke3 R h) : BWHecke3 R h :=
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

instance : Mul (BWHecke3 R h) := ⟨mul⟩

@[simp] lemma mul_c1  (x y : BWHecke3 R h) : (x * y).c1  = (mul x y).c1  := rfl
@[simp] lemma mul_c0  (x y : BWHecke3 R h) : (x * y).c0  = (mul x y).c0  := rfl
@[simp] lemma mul_c1s (x y : BWHecke3 R h) : (x * y).c1s = (mul x y).c1s := rfl
@[simp] lemma mul_cLp (x y : BWHecke3 R h) : (x * y).cLp = (mul x y).cLp := rfl
@[simp] lemma mul_cLm (x y : BWHecke3 R h) : (x * y).cLm = (mul x y).cLm := rfl
@[simp] lemma mul_ce  (x y : BWHecke3 R h) : (x * y).ce  = (mul x y).ce  := rfl

private lemma mul_assoc' (a b c : BWHecke3 R h) : a * b * c = a * (b * c) := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma one_mul' (a : BWHecke3 R h) : (1 : BWHecke3 R h) * a = a := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma mul_one' (a : BWHecke3 R h) : a * (1 : BWHecke3 R h) = a := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma left_distrib' (a b c : BWHecke3 R h) : a * (b + c) = a * b + a * c := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma right_distrib' (a b c : BWHecke3 R h) : (a + b) * c = a * c + b * c := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma zero_mul' (a : BWHecke3 R h) : (0 : BWHecke3 R h) * a = 0 := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma mul_zero' (a : BWHecke3 R h) : a * (0 : BWHecke3 R h) = 0 := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

instance : Ring (BWHecke3 R h) where
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

instance : Module R (BWHecke3 R h) where
  one_smul x := by ext <;> exact one_mul _
  mul_smul r s x := by ext <;> exact mul_assoc _ _ _
  smul_zero r := by ext <;> exact mul_zero _
  smul_add r x y := by ext <;> exact mul_add _ _ _
  add_smul r s x := by ext <;> exact add_mul _ _ _
  zero_smul x := by ext <;> exact zero_mul _

private lemma smul_mul_assoc' (r : R) (x y : BWHecke3 R h) : (r • x) * y = r • (x * y) := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

private lemma mul_smul_comm' (r : R) (x y : BWHecke3 R h) : x * (r • y) = r • (x * y) := by
  ext <;> dsimp [mul, mulRightS0, mulRightS1] <;> ring

instance : Algebra R (BWHecke3 R h) :=
  Algebra.ofModule smul_mul_assoc' mul_smul_comm'

end RingAlgebra

section Generators

variable {R : Type*} [CommRing R]

def σ₀ {h : R} : BWHecke3 R h := ⟨0, 1, 0, 0, 0, 0⟩
def σ₁ {h : R} : BWHecke3 R h := ⟨0, 0, 1, 0, 0, 0⟩
def Lplus {h : R} : BWHecke3 R h := ⟨0, 0, 0, 1, 0, 0⟩
def Lminus {h : R} : BWHecke3 R h := ⟨0, 0, 0, 0, 1, 0⟩
def Tw0 {h : R} : BWHecke3 R h := ⟨0, 0, 0, 0, 0, 1⟩
def σ₁Inv {h : R} : BWHecke3 R h := σ₁ - h • 1

theorem sigma0_sq (h : R) : (σ₀ : BWHecke3 R h) * σ₀ = h • σ₀ + 1 := by
  ext <;> dsimp [σ₀, mul, mulRightS0, mulRightS1] <;> ring

theorem sigma1_sq (h : R) : (σ₁ : BWHecke3 R h) * σ₁ = h • σ₁ + 1 := by
  ext <;> dsimp [σ₁, mul, mulRightS0, mulRightS1] <;> ring

theorem braid_rel (h : R) : (σ₀ : BWHecke3 R h) * σ₁ * σ₀ = σ₁ * σ₀ * σ₁ := by
  ext <;> dsimp [σ₀, σ₁, mul, mulRightS0, mulRightS1] <;> ring

theorem sigma1_mul_inv (h : R) : (σ₁ : BWHecke3 R h) * σ₁Inv = 1 := by
  ext <;> dsimp [σ₁, σ₁Inv, mul, mulRightS0, mulRightS1] <;> ring

theorem borromeanStep_eq (h : R) : (σ₀ : BWHecke3 R h) * σ₁Inv = Lplus - h • σ₀ := by
  ext <;> dsimp [σ₀, σ₁, σ₁Inv, Lplus, mul, mulRightS0, mulRightS1] <;> ring

end Generators

end BWHecke3

section FusionNormalForm

/-- Embed a `Colour R` photon (`γ = 1 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·(σ₀·σ₁⁻¹)`) into `BWHecke3 R h`. -/
def colourToH3 {R : Type*} [CommRing R] (h : R) (φ : Colour R) : BWHecke3 R h :=
  1 + φ.phi0 • BWHecke3.σ₀ + φ.phi1 • BWHecke3.σ₁ +
    φ.phi01 • (BWHecke3.σ₀ * BWHecke3.σ₁Inv)

/-- The 3-term projection (`φ₀₁ = 0`) of a `Colour R`. -/
def threeTermColour {R : Type*} [CommRing R] (φ : Colour R) : Colour R :=
  ⟨φ.phi0, φ.phi1, 0⟩

/-- Color-conjugate swap `(φ₀, φ₁, φ₀₁) ↦ (φ₁, φ₀, φ₀₁)`. -/
def swapColour {R : Type*} (φ : Colour R) : Colour R :=
  ⟨φ.phi1, φ.phi0, φ.phi01⟩

theorem colourToH3_no_Lm_or_Tw0 {R : Type*} [CommRing R] (h : R) (φ : Colour R) :
    (colourToH3 h φ).cLm = 0 ∧ (colourToH3 h φ).ce = 0 := by
  dsimp [colourToH3, BWHecke3.σ₀, BWHecke3.σ₁, BWHecke3.σ₁Inv,
    BWHecke3.mul, BWHecke3.mulRightS0, BWHecke3.mulRightS1]
  constructor <;> ring

/-- **Breit–Wheeler fusion product** `(γ₁, γ₂) ↦ NF(γ₁ · γ₂)` in `BWHecke3 R h`. -/
def breitWheelerProduct {R : Type*} [CommRing R] (h : R) (φ ψ : Colour R) :
    BWHecke3 R h :=
  colourToH3 h φ * colourToH3 h ψ

/-- **Exact 3-term Breit–Wheeler normal form** (`φ₀₁ = ψ₀₁ = 0`):
    `NF(γ₁ · γ₂) = (1 + φ₀ψ₀ + φ₁ψ₁)·1 + (φ₀ + ψ₀ + φ₀ψ₀h)·σ₀
     + (φ₁ + ψ₁ + φ₁ψ₁h)·σ₁ + φ₀ψ₁·L₊ + φ₁ψ₀·L₋`. -/
theorem breitWheelerProduct_threeTerm {R : Type*} [CommRing R] (h : R) (φ ψ : Colour R)
    (h₁ : φ.phi01 = 0) (h₂ : ψ.phi01 = 0) :
    breitWheelerProduct h φ ψ =
      ⟨1 + φ.phi0 * ψ.phi0 + φ.phi1 * ψ.phi1,
       φ.phi0 + ψ.phi0 + φ.phi0 * ψ.phi0 * h,
       φ.phi1 + ψ.phi1 + φ.phi1 * ψ.phi1 * h,
       φ.phi0 * ψ.phi1,
       φ.phi1 * ψ.phi0,
       0⟩ := by
  ext <;> dsimp [breitWheelerProduct, colourToH3,
    BWHecke3.σ₀, BWHecke3.σ₁, BWHecke3.σ₁Inv,
    BWHecke3.mul, BWHecke3.mulRightS0, BWHecke3.mulRightS1] <;>
    rw [h₁, h₂] <;> ring

/-- **4-term longest-word (`e⁻ = σ₀σ₁σ₀`) channel opening:**
    the vertex square `(σ₀·σ₁⁻¹)²` contributes zero to `Tw0`, leaving
    the exact coefficient `ce = φ₀₁·ψ₀ + φ₁·ψ₀₁`. -/
theorem breitWheelerProduct_ce {R : Type*} [CommRing R] (h : R) (φ ψ : Colour R) :
    (breitWheelerProduct h φ ψ).ce = φ.phi01 * ψ.phi0 + φ.phi1 * ψ.phi01 := by
  dsimp [breitWheelerProduct, colourToH3,
    BWHecke3.σ₀, BWHecke3.σ₁, BWHecke3.σ₁Inv,
    BWHecke3.mul, BWHecke3.mulRightS0, BWHecke3.mulRightS1]
  ring

/-- Conjugate color-swap exchange symmetry of the `e⁻` channel:
    swapping color indices `0 ↔ 1` reverses photon order in `ce`. -/
theorem breitWheelerProduct_ce_colorSwap_symm {R : Type*} [CommRing R]
    (h : R) (φ ψ : Colour R) :
    (breitWheelerProduct h (swapColour φ) (swapColour ψ)).ce =
      (breitWheelerProduct h ψ φ).ce := by
  simp only [breitWheelerProduct_ce, swapColour]
  ring

/-- Total chiral Hopf-link weight `cLp + cLm = φ₀·ψ₁ + φ₁·ψ₀` from the 3-term
    projection of the Breit–Wheeler product. -/
def chiralHopfWeight {R : Type*} [CommRing R] (h : R) (φ ψ : Colour R) : R :=
  (breitWheelerProduct h (threeTermColour φ) (threeTermColour ψ)).cLp +
    (breitWheelerProduct h (threeTermColour φ) (threeTermColour ψ)).cLm

theorem chiralHopfWeight_eq {R : Type*} [CommRing R] (h : R) (φ ψ : Colour R) :
    chiralHopfWeight h φ ψ = φ.phi0 * ψ.phi1 + φ.phi1 * ψ.phi0 := by
  have h3 := breitWheelerProduct_threeTerm h (threeTermColour φ) (threeTermColour ψ) rfl rfl
  unfold chiralHopfWeight
  rw [h3]
  simp [threeTermColour]

theorem chiralHopfWeight_symm {R : Type*} [CommRing R] (h : R) (φ ψ : Colour R) :
    chiralHopfWeight h φ ψ = chiralHopfWeight h ψ φ := by
  simp only [chiralHopfWeight_eq]
  ring

/-- Combined bosonic pair-threshold weight extracted from the Breit–Wheeler
    Hecke normal form: the total chiral Hopf-link weight `cLp + cLm` plus the
    symmetrized longest-word (`e⁻ = σ₀σ₁σ₀`) channel weight. -/
def pairThreshold {R : Type*} [CommRing R] (h : R) (φ ψ : Colour R) : R :=
  chiralHopfWeight h φ ψ +
    ((breitWheelerProduct h φ ψ).ce + (breitWheelerProduct h ψ φ).ce)

/-- Bosonic exchange symmetry (`φ ↔ ψ`) of `pairThreshold` over any commutative ring. -/
theorem pairThreshold_symm {R : Type*} [CommRing R] (h : R) (φ ψ : Colour R) :
    pairThreshold h φ ψ = pairThreshold h ψ φ := by
  simp only [pairThreshold, chiralHopfWeight_symm h φ ψ]
  ring

/-- Over any ordered commutative ring, non-negative photon color weights give
    non-negative `e⁻` channel and non-negative `pairThreshold`. -/
theorem pairThreshold_nonneg {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R]
    (h : R) {φ ψ : Colour R}
    (hφ0 : 0 ≤ φ.phi0) (hφ1 : 0 ≤ φ.phi1) (hφ01 : 0 ≤ φ.phi01)
    (hψ0 : 0 ≤ ψ.phi0) (hψ1 : 0 ≤ ψ.phi1) (hψ01 : 0 ≤ ψ.phi01) :
    0 ≤ (breitWheelerProduct h φ ψ).ce ∧ 0 ≤ pairThreshold h φ ψ := by
  have hce12 : 0 ≤ (breitWheelerProduct h φ ψ).ce := by
    rw [breitWheelerProduct_ce]
    exact add_nonneg (mul_nonneg hφ01 hψ0) (mul_nonneg hφ1 hψ01)
  have hce21 : 0 ≤ (breitWheelerProduct h ψ φ).ce := by
    rw [breitWheelerProduct_ce]
    exact add_nonneg (mul_nonneg hψ01 hφ0) (mul_nonneg hψ1 hφ01)
  have hhopf : 0 ≤ chiralHopfWeight h φ ψ := by
    rw [chiralHopfWeight_eq]
    exact add_nonneg (mul_nonneg hφ0 hψ1) (mul_nonneg hφ1 hψ0)
  exact ⟨hce12, add_nonneg hhopf (add_nonneg hce12 hce21)⟩

end FusionNormalForm

end QOU.Archimedean
