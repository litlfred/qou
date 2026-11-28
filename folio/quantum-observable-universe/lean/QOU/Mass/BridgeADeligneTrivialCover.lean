import QOU.Mass.BridgeADeligneGauge

/-!
# Bridge A: the `FundamentalSolution` hypothesis does not pin the monodromy

`BridgeADeligneGauge.FundamentalSolution` carries the monodromy `M` as data. This file shows the
structure alone cannot be what ties `M` to the connection: on the ring `Γ → S₀` (one copy of a
local ring `S₀` per sheet, deck group acting by right translation of the sheet label), **every**
local solution `Φ₀` and **every** homomorphism `M : Γ →* GL_N(K)` give a `FundamentalSolution`
with monodromy `M` (`trivialCover_fundamentalSolution`).

So removing the `FundamentalSolution` hypothesis of `lagrangian_gauge_to_KZ` by a packaging of
this kind proves nothing: the KZ and Lagrangian monodromies would be inputs again, and on this
ring `DeligneFullyFaithful` is not Deligne's theorem (a deck-invariant `h` is any local horizontal
section, algebraic or not). The constraint "the monodromy is the analytic continuation of `Φ₀`"
has to come from a ring `S` of functions on the genuine universal cover, where the deck action is
analytic continuation. That construction is the open part; it is not attempted here.

Base ring (§7c): generic commutative rings; no `ℝ`/`ℂ`.
-/

set_option linter.unusedSectionVars false

namespace QOU.Mass.BridgeADeligneTrivialCover

open Matrix QOU.Mass.BridgeADeligneGauge

variable {S₀ : Type*} [CommRing S₀] {Γ : Type*} [Group Γ]

/-- Right translation of the sheet label: `(γ • f) δ = f (δ * γ)`. -/
instance sheetAction : MulSemiringAction Γ (Γ → S₀) where
  smul γ f := fun δ => f (δ * γ)
  one_smul f := by funext δ; show f (δ * 1) = f δ; rw [mul_one]
  mul_smul γ₁ γ₂ f := by funext δ; show f (δ * (γ₁ * γ₂)) = f (δ * γ₁ * γ₂); rw [mul_assoc]
  smul_zero _ := rfl
  smul_add _ _ _ := rfl
  smul_one _ := rfl
  smul_mul _ _ _ := rfl

theorem smul_apply (γ : Γ) (f : Γ → S₀) (δ : Γ) : (γ • f) δ = f (δ * γ) := rfl

/-- A derivation of `S₀`, applied on every sheet. -/
def sheetDer (d : Derivation ℤ S₀ S₀) : Derivation ℤ (Γ → S₀) (Γ → S₀) :=
  Derivation.mk'
    { toFun := fun f δ => d (f δ)
      map_add' := fun f g => by funext δ; exact d.map_add (f δ) (g δ)
      map_smul' := fun c f => by funext δ; exact d.map_smul c (f δ) }
    fun f g => by
      funext δ
      show d (f δ * g δ) = f δ * d (g δ) + g δ * d (f δ)
      rw [Derivation.leibniz, smul_eq_mul, smul_eq_mul]

theorem sheetDer_apply (d : Derivation ℤ S₀ S₀) (f : Γ → S₀) (δ : Γ) :
    sheetDer d f δ = d (f δ) := rfl

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Evaluation of a matrix of sheet functions on one sheet. -/
abbrev ev (δ : Γ) (A : Matrix n n (Γ → S₀)) : Matrix n n S₀ := A.map (Pi.evalRingHom _ δ)

theorem ev_mul (δ : Γ) (A B : Matrix n n (Γ → S₀)) : ev δ (A * B) = ev δ A * ev δ B :=
  Matrix.map_mul (f := Pi.evalRingHom _ δ)

theorem ev_one (δ : Γ) : ev δ (1 : Matrix n n (Γ → S₀)) = 1 :=
  Matrix.map_one _ (map_zero _) (map_one _)

theorem ext_ev {A B : Matrix n n (Γ → S₀)} (h : ∀ δ, ev δ A = ev δ B) : A = B := by
  ext i k δ; exact congrFun (congrFun (h δ) i) k

variable {K : Type*} [CommRing K] [Algebra K S₀]

/-- The constants of `S₀`, the same on every sheet. -/
theorem ev_cst (δ : Γ) (C : Matrix n n K) :
    ev δ (cst (S := Γ → S₀) C) = C.map (algebraMap K S₀) := by
  ext i k; rfl

variable {ι : Type*} (d : ι → Derivation ℤ S₀ S₀)

/-- **Any** local fundamental solution and **any** monodromy homomorphism give a
`FundamentalSolution` on the sheet ring `Γ → S₀`. Here `Φ` is `Φ₀ · M(δ)` on sheet `δ`. -/
def trivialCover_fundamentalSolution (ω₀ : ι → Matrix n n S₀) (Φ₀ Φ₀inv : Matrix n n S₀)
    (hdK : ∀ j (c : K), d j (algebraMap K S₀ c) = 0)
    (h₁ : Φ₀ * Φ₀inv = 1) (h₂ : Φ₀inv * Φ₀ = 1) (hhoriz : ∀ j, Φ₀.map (d j) = ω₀ j * Φ₀)
    (M : Γ →* (Matrix n n K)ˣ) :
    FundamentalSolution (Γ := Γ) (K := K) (fun j => sheetDer (Γ := Γ) (d j))
      (fun j => (ω₀ j).map (algebraMap S₀ (Γ → S₀))) where
  Φ := Matrix.of fun i k δ => (Φ₀ * ((M δ : Matrix n n K)).map (algebraMap K S₀)) i k
  Φinv := Matrix.of fun i k δ => (((M δ⁻¹ : Matrix n n K)).map (algebraMap K S₀) * Φ₀inv) i k
  mul_inv := by
    apply ext_ev; intro δ
    rw [ev_mul]
    have hM : ((M δ : Matrix n n K) * (M δ⁻¹ : Matrix n n K)) = 1 := by
      rw [← Units.val_mul, ← map_mul, mul_inv_cancel, map_one, Units.val_one]
    have e1 : ev δ (Matrix.of fun i k (δ' : Γ) =>
        (Φ₀ * ((M δ' : Matrix n n K)).map (algebraMap K S₀)) i k)
        = Φ₀ * ((M δ : Matrix n n K)).map (algebraMap K S₀) := by ext; rfl
    have e2 : ev δ (Matrix.of fun i k (δ' : Γ) =>
        (((M δ'⁻¹ : Matrix n n K)).map (algebraMap K S₀) * Φ₀inv) i k)
        = ((M δ⁻¹ : Matrix n n K)).map (algebraMap K S₀) * Φ₀inv := by ext; rfl
    rw [e1, e2]
    calc Φ₀ * (M δ : Matrix n n K).map (algebraMap K S₀) *
          ((M δ⁻¹ : Matrix n n K).map (algebraMap K S₀) * Φ₀inv)
        = Φ₀ * (((M δ : Matrix n n K) * (M δ⁻¹ : Matrix n n K)).map (algebraMap K S₀)) * Φ₀inv := by
          rw [Matrix.map_mul]; simp only [Matrix.mul_assoc]
      _ = ev δ 1 := by
          rw [hM, Matrix.map_one _ (map_zero _) (map_one _), Matrix.mul_one, h₁, ev_one]
  inv_mul := by
    apply ext_ev; intro δ
    rw [ev_mul]
    have hM : ((M δ⁻¹ : Matrix n n K) * (M δ : Matrix n n K)) = 1 := by
      rw [← Units.val_mul, ← map_mul, inv_mul_cancel, map_one, Units.val_one]
    have e1 : ev δ (Matrix.of fun i k (δ' : Γ) =>
        (Φ₀ * ((M δ' : Matrix n n K)).map (algebraMap K S₀)) i k)
        = Φ₀ * ((M δ : Matrix n n K)).map (algebraMap K S₀) := by ext; rfl
    have e2 : ev δ (Matrix.of fun i k (δ' : Γ) =>
        (((M δ'⁻¹ : Matrix n n K)).map (algebraMap K S₀) * Φ₀inv) i k)
        = ((M δ⁻¹ : Matrix n n K)).map (algebraMap K S₀) * Φ₀inv := by ext; rfl
    rw [e1, e2]
    calc (M δ⁻¹ : Matrix n n K).map (algebraMap K S₀) * Φ₀inv *
          (Φ₀ * (M δ : Matrix n n K).map (algebraMap K S₀))
        = (M δ⁻¹ : Matrix n n K).map (algebraMap K S₀) * (Φ₀inv * Φ₀) *
            (M δ : Matrix n n K).map (algebraMap K S₀) := by simp only [Matrix.mul_assoc]
      _ = ev δ 1 := by
          rw [h₂, Matrix.mul_one, ← Matrix.map_mul, hM, Matrix.map_one _ (map_zero _) (map_one _),
            ev_one]
  horiz := by
    intro j
    apply ext_ev; intro δ
    have eΦ : ev δ (Matrix.of fun i k (δ' : Γ) =>
        (Φ₀ * ((M δ' : Matrix n n K)).map (algebraMap K S₀)) i k)
        = Φ₀ * ((M δ : Matrix n n K)).map (algebraMap K S₀) := by ext; rfl
    have eD : ev δ ((Matrix.of fun i k (δ' : Γ) =>
        (Φ₀ * ((M δ' : Matrix n n K)).map (algebraMap K S₀)) i k).map (sheetDer (d j)))
        = (Φ₀ * ((M δ : Matrix n n K)).map (algebraMap K S₀)).map (d j) := by ext; rfl
    have eω : ev δ ((ω₀ j).map (algebraMap S₀ (Γ → S₀))) = ω₀ j := by ext; rfl
    have hc : (((M δ : Matrix n n K)).map (algebraMap K S₀)).map (d j) = 0 := by
      ext i k; simp [hdK]
    rw [eD, ev_mul, eω, eΦ, map_mul_der, hhoriz, hc, Matrix.mul_zero, add_zero, Matrix.mul_assoc]
  M := fun γ => (M γ : Matrix n n K)
  deck := by
    intro γ
    apply ext_ev; intro δ
    have eΦ : ev δ (Matrix.of fun i k (δ' : Γ) =>
        (Φ₀ * ((M δ' : Matrix n n K)).map (algebraMap K S₀)) i k)
        = Φ₀ * ((M δ : Matrix n n K)).map (algebraMap K S₀) := by ext; rfl
    have eA : ev δ (actM γ (Matrix.of fun i k (δ' : Γ) =>
        (Φ₀ * ((M δ' : Matrix n n K)).map (algebraMap K S₀)) i k))
        = Φ₀ * ((M (δ * γ) : Matrix n n K)).map (algebraMap K S₀) := by ext; rfl
    rw [ev_mul, ev_cst, eA, eΦ, map_mul, Units.val_mul, Matrix.map_mul, Matrix.mul_assoc]

end QOU.Mass.BridgeADeligneTrivialCover
