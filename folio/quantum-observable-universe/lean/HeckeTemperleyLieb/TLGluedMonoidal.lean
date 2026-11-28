import HeckeTemperleyLieb.TLGluedAssoc
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Preadditive
import Mathlib.CategoryTheory.Monoidal.Linear

/-!
# The `K`-linear monoidal Temperley–Lieb category on all strand counts

Bean `hkmt`. `TLGluedTensor` and `TLGluedAssoc` construct the level-independent tensor product
`tensHom` on the glued Temperley–Lieb category `GObj T hε` (objects `[a]` with `a + 1 ≥ 1` strands)
and prove naturality of the associator and the Mac Lane pentagon. Because `GObj` starts at one
through-strand (`a = 0`), the zero-strand vacuum lives in `GObj` not as a strand-count label `[a]`
but as the cup–cap idempotent `δ⁻¹ e_0 ∈ End [1]` on two strands (`TLCupCapCorner`), alongside the
higher Jones–Wenzl simple idempotents `p_m ∈ End [m]`.

Passing to the idempotent completion `TLMonObj T hε` of `GObj T hε` puts the zero-strand vacuum,
every strand-count object `[a]` (`a + 1` strands), and every Jones–Wenzl simple idempotent into a
single `K`-linear monoidal category:

* `TLMonObj T hε`: objects `(X : GObj T hε, p : X ⟶ X, p ≫ p = p)`, with `Category`,
  `Preadditive` and `Linear K` instances, and the full and faithful `K`-linear embedding
  `inclG : GObj T hε ⥤ TLMonObj T hε` sending `[a]` to `([a], 𝟙 [a])`.
* `unitObj`: the zero-strand monoidal unit `([1], δ⁻¹ e_0)`, carrying genuine Temperley–Lieb cup
  and cap morphisms to and from even strand counts.
* `uR`, `vR`, `uL`, `vL`: explicit cup/cap and zigzag partial isometries in `GObj` implementing the
  right and left unitors against `δ⁻¹ e_0`, natural on all glued morphisms (`uR_nat`, `uL_nat`)
  and satisfying the triangle identity (`triangle_gobj`).
* `MonoidalCategory (TLMonObj T hε)`, `MonoidalPreadditive (TLMonObj T hε)`, and
  `MonoidalLinear K (TLMonObj T hε)`: the complete `K`-linear monoidal structure, agreeing
  strictly with `tensObj` and `tensHom` on the image of `inclG` (`inclG_tensorObj`,
  `inclG_tensorHom`).

No empirical input; everything holds over an arbitrary field `K` with `δ * ε = 1`.

-- Ref: [jones1983] Index for subfactors, §4.
-- Ref: [kauffman1987] State models and the Jones polynomial, §3.
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

set_option autoImplicit false

namespace QOU.HeckeTemperleyLieb.TLGluedMonoidal

open CategoryTheory MonoidalCategory
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLCupCap QOU.HeckeTemperleyLieb.TLNegligible
open QOU.HeckeTemperleyLieb.TLCableBraiding QOU.HeckeTemperleyLieb.TLQuotientTensor
open QOU.HeckeTemperleyLieb.TLRectHom QOU.HeckeTemperleyLieb.TLQuotientModular
open QOU.HeckeTemperleyLieb.TLGlued QOU.HeckeTemperleyLieb.TLSlideIso
open QOU.HeckeTemperleyLieb.TLZigzag QOU.HeckeTemperleyLieb.TLGluedTensor
open QOU.HeckeTemperleyLieb.TLGluedAssoc

variable {K : Type*} [Field K]

/-! ## Bilinearity of `tensHom` on `GObj` -/

section Bilinear

variable {δ ε : K} {T : MarkovTower δ ε} {hε : δ * ε = 1}

theorem tensLvl_add_left (a b a' b' : ℕ) {n m : ℕ} (φ₁ φ₂ : Q T n) (ψ : Q T m) :
    tensLvl T a b a' b' (φ₁ + φ₂) ψ =
      tensLvl T a b a' b' φ₁ ψ + tensLvl T a b a' b' φ₂ ψ := by
  simp only [tensLvl, tensQ_add_left, mul_add, add_mul]

theorem tensLvl_add_right (a b a' b' : ℕ) {n m : ℕ} (φ : Q T n) (ψ₁ ψ₂ : Q T m) :
    tensLvl T a b a' b' φ (ψ₁ + ψ₂) =
      tensLvl T a b a' b' φ ψ₁ + tensLvl T a b a' b' φ ψ₂ := by
  simp only [tensLvl, tensQ_add_right, mul_add, add_mul]

theorem tensLvl_smul_left (a b a' b' : ℕ) {n m : ℕ} (r : K) (φ : Q T n) (ψ : Q T m) :
    tensLvl T a b a' b' (r • φ) ψ = r • tensLvl T a b a' b' φ ψ := by
  simp only [tensLvl, tensQ_smul_left, mul_smul_comm, smul_mul_assoc]

theorem tensLvl_smul_right (a b a' b' : ℕ) {n m : ℕ} (r : K) (φ : Q T n) (ψ : Q T m) :
    tensLvl T a b a' b' φ (r • ψ) = r • tensLvl T a b a' b' φ ψ := by
  simp only [tensLvl, tensQ_smul_right, mul_smul_comm, smul_mul_assoc]

theorem gl_add (N : ℕ) {a b : ℕ} (ha : a ≤ N) (pa : a % 2 = N % 2) (hb : b ≤ N)
    (pb : b % 2 = N % 2) (φ₁ : Q T N) (hφ₁ : φ₁ ∈ HomSp T N a b) (φ₂ : Q T N)
    (hφ₂ : φ₂ ∈ HomSp T N a b) :
    gl T hε N ha pa hb pb (φ₁ + φ₂) ((HomSp T N a b).add_mem hφ₁ hφ₂) =
      gl T hε N ha pa hb pb φ₁ hφ₁ + gl T hε N ha pa hb pb φ₂ hφ₂ := by
  show (Submodule.Quotient.mk _ : GHom T hε a b) =
    Submodule.Quotient.mk _ + Submodule.Quotient.mk _
  rw [← Submodule.Quotient.mk_add, mk_eq_iff]
  exact ⟨N, ext_add_ev T hε φ₁ φ₂⟩

theorem gl_smul (N : ℕ) {a b : ℕ} (ha : a ≤ N) (pa : a % 2 = N % 2) (hb : b ≤ N)
    (pb : b % 2 = N % 2) (r : K) (φ : Q T N) (hφ : φ ∈ HomSp T N a b) :
    gl T hε N ha pa hb pb (r • φ) ((HomSp T N a b).smul_mem r hφ) =
      r • gl T hε N ha pa hb pb φ hφ := by
  show (Submodule.Quotient.mk _ : GHom T hε a b) = r • Submodule.Quotient.mk _
  rw [← Submodule.Quotient.mk_smul, mk_eq_iff]
  exact ⟨N, ext_smul_ev T hε r φ⟩

theorem tensHom_add_left {X Y X' Y' : GObj T hε} (f₁ f₂ : X ⟶ Y) (g : X' ⟶ Y') :
    tensHom (f₁ + f₂) g = tensHom f₁ g + tensHom f₂ g := by
  by_cases h1 : X.a % 2 = Y.a % 2
  swap
  · rw [hom_eq_zero_of_parity h1 f₁, hom_eq_zero_of_parity h1 f₂, add_zero, tensHom_zero_left,
      add_zero]
  by_cases h2 : X'.a % 2 = Y'.a % 2
  swap
  · rw [hom_eq_zero_of_parity h2 g, tensHom_zero_right, tensHom_zero_right, tensHom_zero_right,
      add_zero]
  set n := X.a + 2 * Y.a
  set m := X'.a + 2 * Y'.a
  have hX : X.a ≤ n := by omega
  have pX : X.a % 2 = n % 2 := by omega
  have hY : Y.a ≤ n := by omega
  have pY : Y.a % 2 = n % 2 := by omega
  have hX' : X'.a ≤ m := by omega
  have pX' : X'.a % 2 = m % 2 := by omega
  have hY' : Y'.a ≤ m := by omega
  have pY' : Y'.a % 2 = m % 2 := by omega
  obtain ⟨a⟩ := X; obtain ⟨b⟩ := Y; obtain ⟨a'⟩ := X'; obtain ⟨b'⟩ := Y'
  rw [← gl_pre n hX pX hY pY f₁, ← gl_pre n hX pX hY pY f₂, ← gl_pre m hX' pX' hY' pY' g,
    ← gl_add, tensHom_gl, tensHom_gl, tensHom_gl, ← gl_add]
  exact gl_congr _ _ _ _ _ _ _ (tensLvl_add_left _ _ _ _ _ _ _)

theorem tensHom_add_right {X Y X' Y' : GObj T hε} (f : X ⟶ Y) (g₁ g₂ : X' ⟶ Y') :
    tensHom f (g₁ + g₂) = tensHom f g₁ + tensHom f g₂ := by
  by_cases h1 : X.a % 2 = Y.a % 2
  swap
  · rw [hom_eq_zero_of_parity h1 f, tensHom_zero_left, tensHom_zero_left, tensHom_zero_left,
      add_zero]
  by_cases h2 : X'.a % 2 = Y'.a % 2
  swap
  · rw [hom_eq_zero_of_parity h2 g₁, hom_eq_zero_of_parity h2 g₂, add_zero, tensHom_zero_right,
      add_zero]
  set n := X.a + 2 * Y.a
  set m := X'.a + 2 * Y'.a
  have hX : X.a ≤ n := by omega
  have pX : X.a % 2 = n % 2 := by omega
  have hY : Y.a ≤ n := by omega
  have pY : Y.a % 2 = n % 2 := by omega
  have hX' : X'.a ≤ m := by omega
  have pX' : X'.a % 2 = m % 2 := by omega
  have hY' : Y'.a ≤ m := by omega
  have pY' : Y'.a % 2 = m % 2 := by omega
  obtain ⟨a⟩ := X; obtain ⟨b⟩ := Y; obtain ⟨a'⟩ := X'; obtain ⟨b'⟩ := Y'
  rw [← gl_pre n hX pX hY pY f, ← gl_pre m hX' pX' hY' pY' g₁, ← gl_pre m hX' pX' hY' pY' g₂,
    ← gl_add, tensHom_gl, tensHom_gl, tensHom_gl, ← gl_add]
  exact gl_congr _ _ _ _ _ _ _ (tensLvl_add_right _ _ _ _ _ _ _)

theorem tensHom_smul_left {X Y X' Y' : GObj T hε} (r : K) (f : X ⟶ Y) (g : X' ⟶ Y') :
    tensHom (r • f) g = r • tensHom f g := by
  by_cases h1 : X.a % 2 = Y.a % 2
  swap
  · rw [hom_eq_zero_of_parity h1 f, smul_zero, tensHom_zero_left, smul_zero]
  by_cases h2 : X'.a % 2 = Y'.a % 2
  swap
  · rw [hom_eq_zero_of_parity h2 g, tensHom_zero_right, tensHom_zero_right, smul_zero]
  set n := X.a + 2 * Y.a
  set m := X'.a + 2 * Y'.a
  have hX : X.a ≤ n := by omega
  have pX : X.a % 2 = n % 2 := by omega
  have hY : Y.a ≤ n := by omega
  have pY : Y.a % 2 = n % 2 := by omega
  have hX' : X'.a ≤ m := by omega
  have pX' : X'.a % 2 = m % 2 := by omega
  have hY' : Y'.a ≤ m := by omega
  have pY' : Y'.a % 2 = m % 2 := by omega
  obtain ⟨a⟩ := X; obtain ⟨b⟩ := Y; obtain ⟨a'⟩ := X'; obtain ⟨b'⟩ := Y'
  rw [← gl_pre n hX pX hY pY f, ← gl_pre m hX' pX' hY' pY' g, ← gl_smul, tensHom_gl, tensHom_gl,
    ← gl_smul]
  exact gl_congr _ _ _ _ _ _ _ (tensLvl_smul_left _ _ _ _ _ _ _)

theorem tensHom_smul_right {X Y X' Y' : GObj T hε} (r : K) (f : X ⟶ Y) (g : X' ⟶ Y') :
    tensHom f (r • g) = r • tensHom f g := by
  by_cases h1 : X.a % 2 = Y.a % 2
  swap
  · rw [hom_eq_zero_of_parity h1 f, tensHom_zero_left, tensHom_zero_left, smul_zero]
  by_cases h2 : X'.a % 2 = Y'.a % 2
  swap
  · rw [hom_eq_zero_of_parity h2 g, smul_zero, tensHom_zero_right, smul_zero]
  set n := X.a + 2 * Y.a
  set m := X'.a + 2 * Y'.a
  have hX : X.a ≤ n := by omega
  have pX : X.a % 2 = n % 2 := by omega
  have hY : Y.a ≤ n := by omega
  have pY : Y.a % 2 = n % 2 := by omega
  have hX' : X'.a ≤ m := by omega
  have pX' : X'.a % 2 = m % 2 := by omega
  have hY' : Y'.a ≤ m := by omega
  have pY' : Y'.a % 2 = m % 2 := by omega
  obtain ⟨a⟩ := X; obtain ⟨b⟩ := Y; obtain ⟨a'⟩ := X'; obtain ⟨b'⟩ := Y'
  rw [← gl_pre n hX pX hY pY f, ← gl_pre m hX' pX' hY' pY' g, ← gl_smul, tensHom_gl, tensHom_gl,
    ← gl_smul]
  exact gl_congr _ _ _ _ _ _ _ (tensLvl_smul_right _ _ _ _ _ _ _)

end Bilinear

/-! ## Temperley–Lieb words for the vacuum corner and unitors -/

section UnitWords

variable {δ : K}

theorem inv_mul_inv_mul_self (hδ : δ ≠ 0) : δ⁻¹ * δ⁻¹ * δ = δ⁻¹ := by
  rw [mul_assoc, inv_mul_cancel₀ hδ, mul_one]

theorem inv_sq_mul_self (hδ : δ ≠ 0) : (δ⁻¹ * δ⁻¹) * δ⁻¹ * δ = δ⁻¹ * δ⁻¹ := by
  rw [mul_assoc, inv_mul_cancel₀ hδ, mul_one]

variable (δ) in
/-- The zero-through-strand idempotent `δ⁻¹ e_0` inside `TL_2` (`N = 1`). -/
noncomputable def vacTL : TLFin K δ 1 := δ⁻¹ • gen δ 1 0

theorem vacTL_idem (hδ : δ ≠ 0) : vacTL δ * vacTL δ = vacTL δ := by
  unfold vacTL
  rw [smul_mul_smul_comm, gen_sq (by omega), smul_smul, inv_mul_inv_mul_self hδ]

/-- Tensoring on the right with `δ⁻¹ e_0` is the cup map `capEmb`. -/
theorem tens_vacTL_right {n : ℕ} (x : TLFin K δ n) :
    tens δ x (vacTL δ) = capEmb δ n x := by
  rw [vacTL, tens_smul_right, TLQuotientBraiding.tens_eq_pl, pl_gen _ (by omega), add_zero,
    ← pl_zero_self (L := n + 1 + 1) (by omega) (capEmb δ n x), pl_capEmb]
  congr 2
  exact congrArg (gen δ (n + 1 + 1)) (by omega)

theorem recast_gen {N N' : ℕ} (h : N = N') (i : ℕ) :
    recast δ h (gen δ N i) = gen δ N' i := by
  subst h; rfl

theorem recast_tens_vacTL_left {m : ℕ} (y : TLFin K δ m) :
    recast δ (show 1 + m + 1 = m + 1 + 1 by omega) (tens δ (vacTL δ) y) =
      δ⁻¹ • (gen δ (m + 1 + 1) 0 * pl δ 2 m (by omega) y) := by
  rw [vacTL, tens_smul_left, TLQuotientBraiding.tens_eq_pl, pl_gen _ (by omega), Nat.zero_add,
    map_smul, map_mul, recast_gen, TLQuotientBraiding.recast_pl]

theorem recast_tens_vacTL_left_one (b : ℕ) :
    recast δ (show 1 + b + 1 = b + 1 + 1 by omega) (tens δ (vacTL δ) (1 : TLFin K δ b)) =
      δ⁻¹ • gen δ (b + 1 + 1) 0 := by
  rw [recast_tens_vacTL_left, map_one, mul_one]

theorem p_four (a : ℕ) :
    P δ a (a + 1 + 1 + 1 + 1) =
      (δ⁻¹ * δ⁻¹) • (gen δ (a + 1 + 1 + 1 + 1) (a + 1) * gen δ (a + 1 + 1 + 1 + 1) (a + 3)) := by
  rw [P_succ_succ δ (by omega), P_two, ← pl_zero_self (L := a + 1 + 1 + 1 + 1) (by omega)
    (capEmb δ _ _), pl_capEmb, map_smul, pl_gen _ (by omega), smul_mul_assoc, smul_smul,
    Nat.zero_add]
  congr 2
  exact congrArg (gen δ _) (by omega)

theorem p_four_mul_zig (hδ : δ ≠ 0) (a : ℕ) :
    P δ a (a + 1 + 1 + 1 + 1) * (δ⁻¹ • zig δ (a + 1 + 1 + 1 + 1) (a + 1) 3) =
      P δ a (a + 1 + 1 + 1 + 1) := by
  set N := a + 1 + 1 + 1 + 1
  have hz : zig δ N (a + 1) 3 = gen δ N (a + 1) * gen δ N (a + 2) * gen δ N (a + 3) := by
    simp only [zig, one_mul]
  have hc : gen δ N (a + 3) * gen δ N (a + 1) = gen δ N (a + 1) * gen δ N (a + 3) :=
    (commute_gen (Or.inr (by omega))).eq
  rw [p_four, hz, smul_mul_smul_comm]
  have key : gen δ N (a + 1) * gen δ N (a + 3) *
      (gen δ N (a + 1) * gen δ N (a + 2) * gen δ N (a + 3)) =
      δ • (gen δ N (a + 1) * gen δ N (a + 3)) := by
    calc gen δ N (a + 1) * gen δ N (a + 3) *
          (gen δ N (a + 1) * gen δ N (a + 2) * gen δ N (a + 3))
        = gen δ N (a + 1) * (gen δ N (a + 3) * gen δ N (a + 1)) * gen δ N (a + 2) *
            gen δ N (a + 3) := by simp only [mul_assoc]
      _ = (gen δ N (a + 1) * gen δ N (a + 1)) *
            (gen δ N (a + 3) * gen δ N (a + 2) * gen δ N (a + 3)) := by
          rw [hc]; simp only [mul_assoc]
      _ = δ • (gen δ N (a + 1) * gen δ N (a + 3)) := by
          rw [gen_sq (by omega), show a + 3 = (a + 2) + 1 by omega, gen_adj_down (by omega),
            smul_mul_assoc]
  rw [key, smul_smul, inv_sq_mul_self hδ]

theorem zag_mul_p_four (hδ : δ ≠ 0) (a : ℕ) :
    (δ⁻¹ • zag δ (a + 1 + 1 + 1 + 1) (a + 1) 3) * P δ a (a + 1 + 1 + 1 + 1) =
      P δ a (a + 1 + 1 + 1 + 1) := by
  set N := a + 1 + 1 + 1 + 1
  have hz : zag δ N (a + 1) 3 = gen δ N (a + 3) * (gen δ N (a + 2) * gen δ N (a + 1)) := by
    simp only [zag, mul_one]
  have hc : gen δ N (a + 1) * gen δ N (a + 3) = gen δ N (a + 3) * gen δ N (a + 1) :=
    (commute_gen (Or.inl (by omega))).eq
  rw [p_four, hz, smul_mul_smul_comm]
  have key : gen δ N (a + 3) * (gen δ N (a + 2) * gen δ N (a + 1)) *
      (gen δ N (a + 1) * gen δ N (a + 3)) =
      δ • (gen δ N (a + 1) * gen δ N (a + 3)) := by
    calc gen δ N (a + 3) * (gen δ N (a + 2) * gen δ N (a + 1)) *
          (gen δ N (a + 1) * gen δ N (a + 3))
        = gen δ N (a + 3) * gen δ N (a + 2) * (gen δ N (a + 1) * gen δ N (a + 1)) *
            gen δ N (a + 3) := by simp only [mul_assoc]
      _ = δ • ((gen δ N (a + 3) * gen δ N (a + 2) * gen δ N (a + 3)) * gen δ N (a + 1)) := by
          rw [gen_sq (by omega), mul_smul_comm, smul_mul_assoc, mul_assoc _ (gen δ N (a + 1)), hc,
            ← mul_assoc]
      _ = δ • (gen δ N (a + 1) * gen δ N (a + 3)) := by
          rw [show a + 3 = (a + 2) + 1 by omega, gen_adj_down (by omega), ← hc]
  rw [key, smul_smul, ← mul_assoc, inv_sq_mul_self hδ]

variable (δ) in
/-- Source word for the left unitor on `[b]`: `δ⁻¹ zig 0 (b+2)` in `TL_{b+3}`. -/
noncomputable def zU (b : ℕ) : TLFin K δ (b + 1 + 1) :=
  δ⁻¹ • zig δ (b + 1 + 1) 0 (b + 2)

variable (δ) in
/-- Target word for the left unitor on `[b]`: `δ⁻¹ zag 0 (b+2)` in `TL_{b+3}`. -/
noncomputable def zV (b : ℕ) : TLFin K δ (b + 1 + 1) :=
  δ⁻¹ • zag δ (b + 1 + 1) 0 (b + 2)

theorem p_mul_zV (hδ : δ ≠ 0) (b : ℕ) : P δ b (b + 1 + 1) * zV δ b = zV δ b := by
  rw [P_two, zV, smul_mul_smul_comm, show b + 1 = 0 + (b + 1) by omega,
    show b + 2 = (b + 1) + 1 from rfl, gen_mul_zag (by omega), smul_smul,
    inv_mul_inv_mul_self hδ]

theorem zU_mul_p (hδ : δ ≠ 0) (b : ℕ) : zU δ b * P δ b (b + 1 + 1) = zU δ b := by
  rw [P_two, zU, smul_mul_smul_comm, show b + 1 = 0 + (b + 1) by omega,
    show b + 2 = (b + 1) + 1 from rfl, zig_mul_gen (by omega), smul_smul,
    inv_mul_inv_mul_self hδ]

theorem zV_mul_zU (hδ : δ ≠ 0) (b : ℕ) : zV δ b * zU δ b = P δ b (b + 1 + 1) := by
  rw [zV, zU, P_two, smul_mul_smul_comm, show b + 2 = (b + 1) + 1 from rfl,
    zag_mul_zig (b + 1) (by omega), Nat.zero_add, smul_smul, inv_mul_inv_mul_self hδ]

theorem zU_mul_zV (hδ : δ ≠ 0) (b : ℕ) :
    zU δ b * zV δ b =
      recast δ (show 1 + b + 1 = b + 1 + 1 by omega) (tens δ (vacTL δ) (1 : TLFin K δ b)) := by
  rw [zU, zV, recast_tens_vacTL_left_one, smul_mul_smul_comm, show b + 2 = (b + 1) + 1 from rfl,
    zig_mul_zag_succ (by omega), smul_smul, inv_mul_inv_mul_self hδ]

theorem zV_mul_tens_base {b : ℕ} (y : TLFin K δ b) :
    zV δ b * recast δ (show 1 + b + 1 = b + 1 + 1 by omega) (tens δ (vacTL δ) y) =
      capEmb δ b y * zV δ b := by
  rw [recast_tens_vacTL_left, zV, smul_mul_smul_comm, ← mul_assoc,
    zag_mul_gen (by omega), smul_mul_assoc,
    pl_shift_zag (t := 0) (M := b) (p := 0) (k := b + 1) (by omega) (by omega) le_rfl (by omega)
      (by omega) y,
    ← pl_zero_self (L := b + 1 + 1) (by omega) (capEmb δ b y), pl_capEmb,
    show gen δ (b + 1 + 1) (0 + b + 1) = gen δ (b + 1 + 1) (0 + (b + 1)) from
      congrArg (gen δ _) (by omega),
    smul_mul_smul_comm, mul_assoc, gen_mul_zag (k := b + 1) (by omega), mul_smul_comm]

theorem capEmb_zV (b : ℕ) :
    capEmb δ (b + 1 + 1) (zV δ b) =
      (δ⁻¹ * δ⁻¹) • (zag δ (b + 1 + 1 + 1 + 1) 0 (b + 2) *
        gen δ (b + 1 + 1 + 1 + 1) (b + 3)) := by
  rw [← pl_zero_self (L := b + 1 + 1 + 1 + 1) (by omega) (capEmb δ _ _), pl_capEmb, zV, map_smul,
    pl_zag _ (b + 2) (by omega), smul_mul_assoc, smul_smul, Nat.zero_add]
  congr 2
  exact congrArg (gen δ _) (by omega)

theorem zV_mul_tens_cup (hδ : δ ≠ 0) (b : ℕ) :
    zV δ (b + 1 + 1) *
      recast δ (show 1 + (b + 1 + 1) + 1 = b + 1 + 1 + 1 + 1 by omega)
        (tens δ (vacTL δ) (P δ b (b + 1 + 1))) =
      capEmb δ (b + 1 + 1) (zV δ b) := by
  set N := b + 1 + 1 + 1 + 1
  have hP : pl δ 2 (b + 1 + 1) (N := N) (by omega) (P δ b (b + 1 + 1)) =
      δ⁻¹ • gen δ N (b + 3) := by
    rw [P_two, map_smul, pl_gen _ (by omega)]
    congr 2
    omega
  have hz : zag δ N 0 (b + 1 + 1 + 2) =
      gen δ N (b + 3) * (gen δ N (b + 2) * zag δ N 0 (b + 2)) := by
    rw [zag_succ (k := b + 1 + 1 + 1), zag_succ (k := b + 1 + 1)]
    simp only [Nat.zero_add]
  have hc : zag δ N 0 (b + 2) * gen δ N (b + 3) = gen δ N (b + 3) * zag δ N 0 (b + 2) :=
    (commute_zag (b + 2) (Or.inr (by omega))).eq.symm
  rw [capEmb_zV]
  simp only [recast_tens_vacTL_left, hP, zV, smul_mul_assoc, mul_smul_comm, smul_smul]
  rw [← mul_assoc (zag δ N 0 (b + 1 + 1 + 2)), zag_mul_gen (by omega), smul_mul_assoc, smul_smul,
    hz]
  have key : gen δ N (b + 3) * (gen δ N (b + 2) * zag δ N 0 (b + 2)) * gen δ N (b + 3) =
      zag δ N 0 (b + 2) * gen δ N (b + 3) := by
    calc gen δ N (b + 3) * (gen δ N (b + 2) * zag δ N 0 (b + 2)) * gen δ N (b + 3)
        = gen δ N (b + 3) * gen δ N (b + 2) * (zag δ N 0 (b + 2) * gen δ N (b + 3)) := by
          simp only [mul_assoc]
      _ = (gen δ N (b + 3) * gen δ N (b + 2) * gen δ N (b + 3)) * zag δ N 0 (b + 2) := by
          rw [hc]; simp only [mul_assoc]
      _ = zag δ N 0 (b + 2) * gen δ N (b + 3) := by
          rw [show b + 3 = (b + 2) + 1 by omega, gen_adj_down (by omega),
            ← show b + 3 = (b + 2) + 1 by omega, ← hc]
  rw [key]
  congr 1
  exact inv_sq_mul_self hδ

theorem zV_mul_tens_cap (hδ : δ ≠ 0) (b : ℕ) :
    capEmb δ (b + 1 + 1) (zV δ b) *
      recast δ (show 1 + (b + 1 + 1) + 1 = b + 1 + 1 + 1 + 1 by omega)
        (tens δ (vacTL δ) (P δ b (b + 1 + 1))) =
      P δ b (b + 1 + 1 + 1 + 1) * zV δ (b + 1 + 1) := by
  set N := b + 1 + 1 + 1 + 1
  have hP : pl δ 2 (b + 1 + 1) (N := N) (by omega) (P δ b (b + 1 + 1)) =
      δ⁻¹ • gen δ N (b + 3) := by
    rw [P_two, map_smul, pl_gen _ (by omega)]
    congr 2
    omega
  have hc0 : gen δ N (b + 3) * gen δ N 0 = gen δ N 0 * gen δ N (b + 3) :=
    (commute_gen (Or.inr (by omega))).eq
  have hc1 : gen δ N (b + 1) * gen δ N (b + 3) = gen δ N (b + 3) * gen δ N (b + 1) :=
    (commute_gen (Or.inl (by omega))).eq
  have hcZ : zag δ N 0 (b + 2) * gen δ N (b + 3) = gen δ N (b + 3) * zag δ N 0 (b + 2) :=
    (commute_zag (b + 2) (Or.inr (by omega))).eq.symm
  have hLHS : capEmb δ (b + 1 + 1) (zV δ b) *
      recast δ (show 1 + (b + 1 + 1) + 1 = N by omega) (tens δ (vacTL δ) (P δ b (b + 1 + 1))) =
      (δ⁻¹ * δ⁻¹) • (zag δ N 0 (b + 2) * gen δ N (b + 3)) := by
    simp only [capEmb_zV, recast_tens_vacTL_left, hP, smul_mul_assoc, mul_smul_comm, smul_smul]
    have k1 : zag δ N 0 (b + 2) * gen δ N (b + 3) * (gen δ N 0 * gen δ N (b + 3)) =
        (δ * δ) • (zag δ N 0 (b + 2) * gen δ N (b + 3)) := by
      calc zag δ N 0 (b + 2) * gen δ N (b + 3) * (gen δ N 0 * gen δ N (b + 3))
          = zag δ N 0 (b + 2) * (gen δ N (b + 3) * gen δ N 0) * gen δ N (b + 3) := by
            simp only [mul_assoc]
        _ = (zag δ N 0 (b + 2) * gen δ N 0) * (gen δ N (b + 3) * gen δ N (b + 3)) := by
            rw [hc0]; simp only [mul_assoc]
        _ = (δ * δ) • (zag δ N 0 (b + 2) * gen δ N (b + 3)) := by
            rw [zag_mul_gen (by omega), gen_sq (by omega), smul_mul_smul_comm]
    rw [k1, smul_smul]
    congr 1
    calc δ⁻¹ * δ⁻¹ * (δ⁻¹ * δ⁻¹) * (δ * δ)
        = (δ⁻¹ * δ⁻¹) * (δ⁻¹ * (δ⁻¹ * δ) * δ) := by ring
      _ = δ⁻¹ * δ⁻¹ := by rw [inv_mul_cancel₀ hδ, mul_one, inv_mul_cancel₀ hδ, mul_one]
  have hRHS : P δ b N * zV δ (b + 1 + 1) =
      (δ⁻¹ * δ⁻¹) • (zag δ N 0 (b + 2) * gen δ N (b + 3)) := by
    have hz : zag δ N 0 (b + 1 + 1 + 2) =
        gen δ N (b + 3) * (gen δ N (b + 2) * (gen δ N (b + 1) * zag δ N 0 (b + 1))) := by
      rw [zag_succ (k := b + 1 + 1 + 1), zag_succ (k := b + 1 + 1), zag_succ (k := b + 1)]
      simp only [Nat.zero_add]
    rw [p_four, zV, hz, smul_mul_smul_comm]
    have k2 : gen δ N (b + 1) * gen δ N (b + 3) *
        (gen δ N (b + 3) * (gen δ N (b + 2) * (gen δ N (b + 1) * zag δ N 0 (b + 1)))) =
        δ • (zag δ N 0 (b + 2) * gen δ N (b + 3)) := by
      calc gen δ N (b + 1) * gen δ N (b + 3) *
            (gen δ N (b + 3) * (gen δ N (b + 2) * (gen δ N (b + 1) * zag δ N 0 (b + 1))))
          = gen δ N (b + 1) * (gen δ N (b + 3) * gen δ N (b + 3)) *
              (gen δ N (b + 2) * (gen δ N (b + 1) * zag δ N 0 (b + 1))) := by
            simp only [mul_assoc]
        _ = δ • (gen δ N (b + 3) * (gen δ N (b + 1) * gen δ N (b + 2) * gen δ N (b + 1)) *
              zag δ N 0 (b + 1)) := by
            rw [gen_sq (by omega), mul_smul_comm, smul_mul_assoc, hc1]
            simp only [mul_assoc]
        _ = δ • (zag δ N 0 (b + 2) * gen δ N (b + 3)) := by
            rw [gen_adj_up (by omega), mul_assoc, ← show gen δ N (0 + (b + 1)) *
                zag δ N 0 (b + 1) = gen δ N (b + 1) * zag δ N 0 (b + 1) from
              congrArg (· * _) (congrArg (gen δ N) (by omega)), ← zag_succ, ← hcZ]
    rw [k2, smul_smul, inv_sq_mul_self hδ]
  rw [hLHS, hRHS]

end UnitWords

/-! ## Unitor morphisms and coherence in `GObj` -/

section GluedUnitors

variable {δ ε : K} {T : MarkovTower δ ε} {hε : δ * ε = 1}

/-- The zero-strand idempotent in `Q T 1`. -/
noncomputable def vacQ : Q T 1 := (vacTL δ : Q T 1)

include hε in
theorem vacQ_idem : vacQ (T := T) * vacQ (T := T) = vacQ (T := T) := by
  rw [vacQ, ← RingCon.coe_mul, vacTL_idem (left_ne_zero_of_mul_eq_one hε)]

/-- **The zero-strand idempotent in `GObj`**, living as `δ⁻¹ e_0` on `[1]` (two strands). -/
noncomputable def vacIdem : (GObj.mk 1 : GObj T hε) ⟶ GObj.mk 1 :=
  gl T hε 1 le_rfl rfl le_rfl rfl (vacQ (T := T)) (mem_top 1 _)

theorem vacIdem_idem : vacIdem (T := T) (hε := hε) ≫ vacIdem = vacIdem := by
  unfold vacIdem
  rw [gl_comp 1]
  exact gl_congr 1 _ _ _ _ _ _ (vacQ_idem (hε := hε))

theorem tensQ_vacQ_right {n : ℕ} (φ : Q T n) :
    tensQ T φ (vacQ (T := T)) = capQ T hε n φ := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  rw [vacQ, tensQ_coe, capQ_coe, tens_vacTL_right]

/-- Right-unitor forward partial isometry `[a] ⊗ [1] = [a+2] ⟶ [a]`. -/
noncomputable def uR (a : ℕ) :
    tensObj (GObj.mk a : GObj T hε) (GObj.mk 1) ⟶ GObj.mk a :=
  gl T hε (a + 1 + 1) le_rfl rfl (by omega) (by omega) (PQ T a (a + 1 + 1))
    (PQ_mem_down (hε := hε) a _)

/-- Right-unitor inverse partial isometry `[a] ⟶ [a+2] = [a] ⊗ [1]`. -/
noncomputable def vR (a : ℕ) :
    (GObj.mk a : GObj T hε) ⟶ tensObj (GObj.mk a) (GObj.mk 1) :=
  gl T hε (a + 1 + 1) (by omega) (by omega) le_rfl rfl (PQ T a (a + 1 + 1))
    (PQ_mem_up (hε := hε) a _)

theorem vR_comp_uR (a : ℕ) : vR (T := T) (hε := hε) a ≫ uR a = 𝟙 (GObj.mk a) := by
  unfold vR uR
  rw [gl_comp (a + 1 + 1), ← gl_id a, gl_lift a]
  refine gl_congr (a + 1 + 1) _ _ _ _ _ _ ?_
  rw [PQ_idem T hε, ← PQ_self T a, capQ_PQ T hε (by omega)]

theorem uR_comp_vR (a : ℕ) :
    uR (T := T) (hε := hε) a ≫ vR a = tensHom (𝟙 (GObj.mk a)) vacIdem := by
  unfold uR vR vacIdem
  rw [gl_comp (a + 1 + 1), ← gl_id a, tensHom_gl]
  refine gl_congr (a + 1 + 1) _ _ _ _ _ _ ?_
  rw [PQ_idem T hε, tensLvl_base T _ (mem_top 1 _), tensQ_vacQ_right (hε := hε),
    ← PQ_self T a, capQ_PQ T hε (by omega)]

/-- Right-unitor naturality predicate on `GObj`. -/
def GoodR {A B : GObj T hε} (h : A ⟶ B) : Prop :=
  tensHom h vacIdem ≫ uR B.a = uR A.a ≫ h

/-- **Naturality of the right-unitor partial isometry** on every morphism of `GObj`. -/
theorem uR_nat {X Y : GObj T hε} (f : X ⟶ Y) :
    tensHom f vacIdem ≫ uR Y.a = uR X.a ≫ f := by
  refine glued_induction (@GoodR _ _ _ _ T hε)
    (fun ⟨a⟩ => by
      unfold GoodR
      rw [← uR_comp_vR a, Category.assoc, vR_comp_uR, Category.comp_id])
    (fun {A B} => by
      unfold GoodR
      rw [tensHom_zero_left, Limits.zero_comp, Limits.comp_zero])
    (fun {A B C} {f₁ f₂} h1 h2 => by
      unfold GoodR at *
      rw [← vacIdem_idem, tensHom_comp, Category.assoc, h2, ← Category.assoc, h1, Category.assoc])
    (fun a => ?_) (fun a => ?_) (fun a φ => ?_) f
  · -- cup `[a] → [a+2]`
    unfold GoodR
    have hvR : gl T hε (a + 1 + 1) (a := a) (b := a + 1 + 1) (by omega) (by omega) le_rfl rfl
        (PQ T a (a + 1 + 1)) (PQ_mem_up (hε := hε) a _) = vR a := rfl
    rw [hvR, uR_comp_vR]
    unfold vR vacIdem uR
    rw [← gl_id a, tensHom_gl, tensHom_gl, gl_comp (a + 1 + 1 + 1 + 1), gl_lift (a + 1 + 1)]
    refine gl_congr (a + 1 + 1 + 1 + 1) _ _ _ _ _ _ ?_
    have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
    rw [tensLvl_base T (1 : Q T a) (mem_top 1 _), tensQ_vacQ_right (hε := hε), ← PQ_self T a,
      capQ_PQ T hε (by omega), capQ_PQ T hε (by omega)]
    unfold tensLvl sUQ sVQ
    rw [P_self, slideV_base, tens_one, RingCon.coe_one, one_mul,
      slideU_one' hδ (show a + 1 + 1 = a + 2 by omega), tensQ_vacQ_right (hε := hε),
      capQ_PQ T hε (by omega), ← mul_assoc, PQ_cup_mul (hε := hε) a (a + 1 + 1) (by omega), PQ,
      ← RingCon.coe_mul, p_four_mul_zig hδ a]
  · -- cap `[a+2] → [a]`
    unfold GoodR vacIdem uR
    dsimp only
    rw [tensHom_gl, gl_lift (a + 1 + 1) (a := a + 1 + 1) (b := a), gl_comp (a + 1 + 1 + 1 + 1),
      gl_comp (a + 1 + 1 + 1 + 1)]
    refine gl_congr (a + 1 + 1 + 1 + 1) _ _ _ _ _ _ ?_
    have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
    rw [capQ_PQ T hε (by omega), PQ_mul_cap (hε := hε) a (a + 1 + 1) (by omega)]
    unfold tensLvl sUQ sVQ
    rw [P_self, slideU_base, tens_one, RingCon.coe_one, mul_one,
      slideV_one' hδ (show a + 1 + 1 = a + 2 by omega), tensQ_vacQ_right (hε := hε),
      capQ_PQ T hε (by omega), PQ, ← RingCon.coe_mul _ (δ⁻¹ • _), zag_mul_p_four hδ a, ← PQ,
      PQ_idem T hε]
  · -- base `[a] → [a]`
    unfold GoodR vacIdem uR
    dsimp only
    rw [tensHom_gl, gl_comp (a + 1 + 1), gl_lift a le_rfl rfl le_rfl rfl φ, gl_comp (a + 1 + 1)]
    refine gl_congr (a + 1 + 1) _ _ _ _ _ _ ?_
    rw [tensLvl_base T φ (mem_top 1 _), tensQ_vacQ_right (hε := hε),
      ← capQ_PQ T hε (n := a) (by omega), ← capQ_mul, ← capQ_mul, PQ_self, one_mul, mul_one]

theorem vR_nat {X Y : GObj T hε} (f : X ⟶ Y) :
    vR X.a ≫ tensHom f vacIdem = f ≫ vR Y.a := by
  have hf : tensHom f vacIdem = tensHom f vacIdem ≫ tensHom (𝟙 Y) vacIdem := by
    rw [← tensHom_comp, Category.comp_id, vacIdem_idem]
  rw [hf, ← uR_comp_vR Y.a, ← Category.assoc (tensHom f vacIdem), uR_nat f,
    ← Category.assoc, ← Category.assoc, vR_comp_uR, Category.id_comp]

include hε in
theorem zVQ_mem (b : ℕ) : (zV δ b : Q T (b + 1 + 1)) ∈ HomSp T (b + 1 + 1) (b + 1 + 1) b := by
  rw [mem_Hom, PQ_self, mul_one, PQ, ← RingCon.coe_mul,
    p_mul_zV (left_ne_zero_of_mul_eq_one hε)]

include hε in
theorem zUQ_mem (b : ℕ) : (zU δ b : Q T (b + 1 + 1)) ∈ HomSp T (b + 1 + 1) b (b + 1 + 1) := by
  rw [mem_Hom, PQ_self, one_mul, PQ, ← RingCon.coe_mul,
    zU_mul_p (left_ne_zero_of_mul_eq_one hε)]

/-- Auxiliary left-unitor forward map `[b+2] ⟶ [b]` at level `b + 2`. -/
noncomputable def uL' (b : ℕ) : (GObj.mk (b + 1 + 1) : GObj T hε) ⟶ GObj.mk b :=
  gl T hε (b + 1 + 1) le_rfl rfl (by omega) (by omega) (zV δ b : Q T (b + 1 + 1))
    (zVQ_mem (hε := hε) b)

/-- Auxiliary left-unitor inverse map `[b] ⟶ [b+2]` at level `b + 2`. -/
noncomputable def vL' (b : ℕ) : (GObj.mk b : GObj T hε) ⟶ GObj.mk (b + 1 + 1) :=
  gl T hε (b + 1 + 1) (by omega) (by omega) le_rfl rfl (zU δ b : Q T (b + 1 + 1))
    (zUQ_mem (hε := hε) b)

/-- Left-unitor forward partial isometry `[1] ⊗ [b] = [1+b+1] ⟶ [b]`. -/
noncomputable def uL (b : ℕ) :
    tensObj (GObj.mk 1 : GObj T hε) (GObj.mk b) ⟶ GObj.mk b :=
  eqToHom (congrArg GObj.mk (by omega : 1 + b + 1 = b + 1 + 1)) ≫ uL' b

/-- Left-unitor inverse partial isometry `[b] ⟶ [1+b+1] = [1] ⊗ [b]`. -/
noncomputable def vL (b : ℕ) :
    (GObj.mk b : GObj T hε) ⟶ tensObj (GObj.mk 1) (GObj.mk b) :=
  vL' b ≫ eqToHom (congrArg GObj.mk (by omega : b + 1 + 1 = 1 + b + 1))

theorem vL_comp_uL (b : ℕ) : vL (T := T) (hε := hε) b ≫ uL b = 𝟙 (GObj.mk b) := by
  unfold vL uL vL' uL'
  rw [Category.assoc, ← Category.assoc (eqToHom _), eqToHom_trans, eqToHom_refl, Category.id_comp,
    gl_comp (b + 1 + 1), ← gl_id b, gl_lift b]
  refine gl_congr (b + 1 + 1) _ _ _ _ _ _ ?_
  rw [← RingCon.coe_mul, zV_mul_zU (left_ne_zero_of_mul_eq_one hε), ← PQ, ← PQ_self T b,
    capQ_PQ T hε (by omega)]

theorem recastQ_mul {N N' : ℕ} (h : N = N') (φ ψ : Q T N) :
    recastQ T h (φ * ψ) = recastQ T h φ * recastQ T h ψ := by
  subst h; rfl

theorem recastQ_PQ {N N' : ℕ} (h : N = N') (c c' : ℕ) (hc : c = c') :
    recastQ T h (PQ T c N) = PQ T c' N' := by
  subst h; subst hc; rfl

include hε in
theorem recast_vacQ_tens_mem {m b b' : ℕ} (hb : b ≤ m) (pb : b % 2 = m % 2) (hb' : b' ≤ m)
    (pb' : b' % 2 = m % 2) {ψ : Q T m} (hψ : ψ ∈ HomSp T m b b') :
    recastQ T (show 1 + m + 1 = m + 1 + 1 by omega) (tensQ T (vacQ (T := T)) ψ) ∈
      HomSp T (m + 1 + 1) (b + 1 + 1) (b' + 1 + 1) := by
  have hmem := tensLvl_mem T hε (a := 1) (a' := 1) (n := 1) le_rfl rfl hb pb.symm le_rfl
    rfl hb' pb'.symm (mem_top 1 (vacQ (T := T))) hψ
  rw [tensLvl_base T _ hψ, mem_Hom] at hmem
  rw [mem_Hom]
  have hr := congrArg (recastQ T (show 1 + m + 1 = m + 1 + 1 by omega)) hmem
  rwa [recastQ_mul, recastQ_mul, recastQ_PQ _ (1 + b' + 1) (b' + 1 + 1) (by omega),
    recastQ_PQ _ (1 + b + 1) (b + 1 + 1) (by omega)] at hr

theorem tensHom_vacIdem_gl {m b b' : ℕ} (hb : b ≤ m) (pb : b % 2 = m % 2) (hb' : b' ≤ m)
    (pb' : b' % 2 = m % 2) (ψ : Q T m) (hψ : ψ ∈ HomSp T m b b') :
    tensHom (vacIdem (T := T) (hε := hε)) (gl T hε m hb pb hb' pb' ψ hψ) ≫
      eqToHom (congrArg GObj.mk (by omega : 1 + b' + 1 = b' + 1 + 1)) =
    eqToHom (congrArg GObj.mk (by omega : 1 + b + 1 = b + 1 + 1)) ≫
      gl T hε (m + 1 + 1) (by omega) (by omega) (by omega) (by omega)
        (recastQ T (by omega) (tensQ T (vacQ (T := T)) ψ))
        (recast_vacQ_tens_mem (hε := hε) hb pb hb' pb' hψ) := by
  unfold vacIdem
  rw [tensHom_gl]
  refine gl_eqToHom (by omega) (by omega) (by omega) _ _ _ _ _ _ _ _ _ _ _ _ ?_
  rw [tensLvl_base T _ hψ]

theorem uL_comp_vL (b : ℕ) :
    uL (T := T) (hε := hε) b ≫ vL b = tensHom vacIdem (𝟙 (GObj.mk b)) := by
  have heq : tensHom (vacIdem (T := T) (hε := hε)) (𝟙 (GObj.mk b)) ≫
      eqToHom (congrArg GObj.mk (by omega : 1 + b + 1 = b + 1 + 1)) =
      eqToHom (congrArg GObj.mk (by omega : 1 + b + 1 = b + 1 + 1)) ≫
        (uL' (T := T) (hε := hε) b ≫ vL' b) := by
    rw [← gl_id b, tensHom_vacIdem_gl]
    congr 1
    unfold uL' vL'
    rw [gl_comp (b + 1 + 1)]
    refine gl_congr (b + 1 + 1) _ _ _ _ _ _ ?_
    rw [vacQ, ← RingCon.coe_one, tensQ_coe, recastQ_coe, ← RingCon.coe_mul,
      zU_mul_zV (left_ne_zero_of_mul_eq_one hε)]
  have h2 := congrArg (· ≫ eqToHom (congrArg GObj.mk (by omega : b + 1 + 1 = 1 + b + 1))) heq
  simp only [Category.assoc, eqToHom_trans, eqToHom_refl, Category.comp_id] at h2
  unfold uL vL
  simpa only [Category.assoc] using h2.symm

/-- Left-unitor naturality predicate on `GObj`. -/
def GoodL {A B : GObj T hε} (h : A ⟶ B) : Prop :=
  tensHom vacIdem h ≫ uL B.a = uL A.a ≫ h

/-- **Naturality of the left-unitor partial isometry** on every morphism of `GObj`. -/
theorem uL_nat {X Y : GObj T hε} (g : X ⟶ Y) :
    tensHom vacIdem g ≫ uL Y.a = uL X.a ≫ g := by
  refine glued_induction (@GoodL _ _ _ _ T hε)
    (fun ⟨b⟩ => by
      unfold GoodL
      rw [← uL_comp_vL b, Category.assoc, vL_comp_uL, Category.comp_id])
    (fun {A B} => by
      unfold GoodL
      rw [tensHom_zero_right, Limits.zero_comp, Limits.comp_zero])
    (fun {A B C} {g₁ g₂} h1 h2 => by
      unfold GoodL at *
      rw [← vacIdem_idem, tensHom_comp, Category.assoc, h2, ← Category.assoc, h1, Category.assoc])
    (fun b => ?_) (fun b => ?_) (fun b ψ => ?_) g
  · -- cup `[b] → [b+2]`
    unfold GoodL uL
    dsimp only
    rw [← Category.assoc, tensHom_vacIdem_gl, Category.assoc, Category.assoc]
    congr 1
    unfold uL'
    rw [gl_comp (b + 1 + 1 + 1 + 1), gl_comp (b + 1 + 1), gl_lift (b + 1 + 1)]
    refine gl_congr (b + 1 + 1 + 1 + 1) _ _ _ _ _ _ ?_
    rw [vacQ, PQ, tensQ_coe, recastQ_coe, ← RingCon.coe_mul,
      zV_mul_tens_cup (left_ne_zero_of_mul_eq_one hε) b, ← RingCon.coe_mul,
      p_mul_zV (left_ne_zero_of_mul_eq_one hε) b, capQ_coe]
  · -- cap `[b+2] → [b]`
    unfold GoodL uL
    dsimp only
    rw [← Category.assoc, tensHom_vacIdem_gl, Category.assoc, Category.assoc]
    congr 1
    unfold uL'
    rw [gl_lift (b + 1 + 1) (a := b + 1 + 1) (b := b),
      gl_lift (b + 1 + 1) (a := b + 1 + 1) (b := b) le_rfl rfl (by omega) (by omega)
        (PQ T b (b + 1 + 1)),
      gl_comp (b + 1 + 1 + 1 + 1), gl_comp (b + 1 + 1 + 1 + 1)]
    refine gl_congr (b + 1 + 1 + 1 + 1) _ _ _ _ _ _ ?_
    rw [vacQ, PQ, tensQ_coe, recastQ_coe, capQ_coe, ← RingCon.coe_mul,
      zV_mul_tens_cap (left_ne_zero_of_mul_eq_one hε) b, ← PQ, capQ_PQ T hε (by omega), PQ,
      RingCon.coe_mul]
  · -- base `[b] → [b]`
    obtain ⟨y, rfl⟩ := coe_surj T ψ
    unfold GoodL uL
    dsimp only
    rw [← Category.assoc, tensHom_vacIdem_gl, Category.assoc, Category.assoc]
    congr 1
    unfold uL'
    rw [gl_lift b le_rfl rfl le_rfl rfl (y : Q T b), gl_comp (b + 1 + 1), gl_comp (b + 1 + 1)]
    refine gl_congr (b + 1 + 1) _ _ _ _ _ _ ?_
    rw [vacQ, tensQ_coe, recastQ_coe, capQ_coe, ← RingCon.coe_mul, ← RingCon.coe_mul,
      zV_mul_tens_base y]

theorem vL_nat {X Y : GObj T hε} (g : X ⟶ Y) :
    vL X.a ≫ tensHom vacIdem g = g ≫ vL Y.a := by
  have hg : tensHom vacIdem g = tensHom vacIdem g ≫ tensHom vacIdem (𝟙 Y) := by
    rw [← tensHom_comp, Category.comp_id, vacIdem_idem]
  rw [hg, ← uL_comp_vL Y.a, ← Category.assoc (tensHom vacIdem g), uL_nat g,
    ← Category.assoc, ← Category.assoc, vL_comp_uL, Category.id_comp]

/-- **The Mac Lane triangle identity** in `GObj` for `uR`, `uL` and `eqToHom (tensObj_assoc · · ·)`. -/
theorem triangle_gobj (a b : ℕ) :
    eqToHom (tensObj_assoc (GObj.mk a : GObj T hε) (GObj.mk 1) (GObj.mk b)) ≫
      tensHom (𝟙 (GObj.mk a)) (uL b) =
    tensHom (uR a) (𝟙 (GObj.mk b)) := by
  unfold uL
  rw [← Category.id_comp (𝟙 (GObj.mk a)), tensHom_comp, tensHom_eqToHom_right,
    ← Category.assoc, eqToHom_trans]
  unfold uL' uR
  rw [← gl_id a, ← gl_id b, tensHom_gl, tensHom_gl]
  have h := gl_eqToHom (T := T) (hε := hε)
    (hN := (by omega : (a + 1 + 1) + b + 1 = a + (b + 1 + 1) + 1))
    (hA := (by omega : (a + 1 + 1) + b + 1 = a + (b + 1 + 1) + 1))
    (hB := (rfl : a + b + 1 = a + b + 1))
    (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
    (tensLvl T (a + 1 + 1) b a b (PQ T a (a + 1 + 1)) (1 : Q T b))
    (tensLvl_mem T hε le_rfl rfl le_rfl rfl (by omega) (by omega) le_rfl rfl
      (PQ_mem_down (hε := hε) a _) (mem_top b 1))
    (tensLvl T a (b + 1 + 1) a b (1 : Q T a) (zV δ b : Q T (b + 1 + 1)))
    (tensLvl_mem T hε le_rfl rfl le_rfl rfl le_rfl rfl (by omega) (by omega)
      (mem_top a 1) (zVQ_mem (hε := hε) b))
    (by
      rw [PQ, tensLvl_cap T hε (show a + 1 + 1 = a + 2 by omega), zag_mul_cap,
        tensLvl_base T (1 : Q T a) (zVQ_mem (hε := hε) b), tensQ_one_coe, tens_one_left, zV,
        map_smul, pl_zag _ (b + 2) (by omega), add_zero, recastQ_coe, map_smul, recast_zag])
  rw [eqToHom_refl, Category.comp_id] at h
  exact h.symm

end GluedUnitors

/-! ## The idempotent-completed category `TLMonObj` and its `MonoidalCategory` structure -/

section Monoidal

variable {δ ε : K} (T : MarkovTower δ ε) (hε : δ * ε = 1)

/-- **Objects of the monoidal Temperley–Lieb category**: idempotent corners `(X, p)` of the glued
category `GObj T hε`. This includes `[a]` (`a + 1` strands) as `([a], 𝟙 [a])`, the zero-strand
monoidal unit as `([1], δ⁻¹ e_0)`, and every Jones–Wenzl simple object `([m], p_m)`. -/
structure TLMonObj where
  /-- Ambient glued strand-count object. -/
  X : GObj T hε
  /-- Defining idempotent endomorphism. -/
  p : X ⟶ X
  /-- Idempotence `p ≫ p = p`. -/
  idem : p ≫ p = p

variable {T hε}

/-- Morphisms between idempotent corners `(X, p)` and `(Y, q)`. -/
@[ext]
structure TLMonHom (P Q : TLMonObj T hε) where
  /-- Underlying glued morphism. -/
  f : P.X ⟶ Q.X
  /-- Corner compatibility `p ≫ (f ≫ q) = f`. -/
  comm : P.p ≫ f ≫ Q.p = f

theorem TLMonHom.comm_left {P Q : TLMonObj T hε} (φ : TLMonHom P Q) : P.p ≫ φ.f = φ.f := by
  conv_lhs => rw [← φ.comm]
  rw [← Category.assoc, P.idem, φ.comm]

theorem TLMonHom.comm_right {P Q : TLMonObj T hε} (φ : TLMonHom P Q) : φ.f ≫ Q.p = φ.f := by
  conv_lhs => rw [← φ.comm]
  rw [Category.assoc, Category.assoc, Q.idem, φ.comm]

noncomputable instance : Category (TLMonObj T hε) where
  Hom P Q := TLMonHom P Q
  id P := ⟨P.p, by rw [P.idem, P.idem]⟩
  comp φ ψ := ⟨φ.f ≫ ψ.f, by
    rw [Category.assoc φ.f, ψ.comm_right, ← Category.assoc, φ.comm_left]⟩
  id_comp φ := TLMonHom.ext φ.comm_left
  comp_id φ := TLMonHom.ext φ.comm_right
  assoc _ _ _ := TLMonHom.ext (Category.assoc _ _ _)

@[simp] theorem id_f (P : TLMonObj T hε) : (𝟙 P : P ⟶ P).f = P.p := rfl
@[simp] theorem comp_f {P Q R : TLMonObj T hε} (φ : P ⟶ Q) (ψ : Q ⟶ R) :
    (φ ≫ ψ).f = φ.f ≫ ψ.f := rfl

noncomputable instance (P Q : TLMonObj T hε) : AddCommGroup (P ⟶ Q) where
  zero := ⟨0, by simp⟩
  add φ ψ := ⟨φ.f + ψ.f, by rw [Preadditive.add_comp, Preadditive.comp_add, φ.comm, ψ.comm]⟩
  neg φ := ⟨-φ.f, by rw [Preadditive.neg_comp, Preadditive.comp_neg, φ.comm]⟩
  sub φ ψ := ⟨φ.f - ψ.f, by rw [Preadditive.sub_comp, Preadditive.comp_sub, φ.comm, ψ.comm]⟩
  nsmul n φ := ⟨n • φ.f, by rw [Preadditive.nsmul_comp, Preadditive.comp_nsmul, φ.comm]⟩
  zsmul z φ := ⟨z • φ.f, by rw [Preadditive.zsmul_comp, Preadditive.comp_zsmul, φ.comm]⟩
  add_assoc _ _ _ := TLMonHom.ext (add_assoc _ _ _)
  zero_add _ := TLMonHom.ext (zero_add _)
  add_zero _ := TLMonHom.ext (add_zero _)
  nsmul_zero _ := TLMonHom.ext (zero_smul ℕ _)
  nsmul_succ n φ := TLMonHom.ext (succ_nsmul φ.f n)
  sub_eq_add_neg _ _ := TLMonHom.ext (sub_eq_add_neg _ _)
  zsmul_zero' _ := TLMonHom.ext (zero_smul ℤ _)
  zsmul_succ' n φ := TLMonHom.ext (SubNegMonoid.zsmul_succ' n φ.f)
  zsmul_neg' n φ := TLMonHom.ext (SubNegMonoid.zsmul_neg' n φ.f)
  neg_add_cancel _ := TLMonHom.ext (neg_add_cancel _)
  add_comm _ _ := TLMonHom.ext (add_comm _ _)

@[simp] theorem zero_f {P Q : TLMonObj T hε} : (0 : P ⟶ Q).f = 0 := rfl
@[simp] theorem add_f {P Q : TLMonObj T hε} (φ ψ : P ⟶ Q) : (φ + ψ).f = φ.f + ψ.f := rfl

noncomputable instance : Preadditive (TLMonObj T hε) where
  homGroup _ _ := inferInstance
  add_comp _ _ _ _ _ _ := TLMonHom.ext (Preadditive.add_comp _ _ _ _ _ _)
  comp_add _ _ _ _ _ _ := TLMonHom.ext (Preadditive.comp_add _ _ _ _ _ _)

noncomputable instance (P Q : TLMonObj T hε) : Module K (P ⟶ Q) where
  smul r φ := ⟨r • φ.f, by rw [Linear.smul_comp, Linear.comp_smul, φ.comm]⟩
  one_smul _ := TLMonHom.ext (one_smul K _)
  mul_smul _ _ _ := TLMonHom.ext (mul_smul _ _ _)
  smul_zero _ := TLMonHom.ext (smul_zero _)
  smul_add _ _ _ := TLMonHom.ext (smul_add _ _ _)
  add_smul _ _ _ := TLMonHom.ext (add_smul _ _ _)
  zero_smul _ := TLMonHom.ext (zero_smul K _)

@[simp] theorem smul_f {P Q : TLMonObj T hε} (r : K) (φ : P ⟶ Q) : (r • φ).f = r • φ.f := rfl

noncomputable instance : Linear K (TLMonObj T hε) where
  homModule _ _ := inferInstance
  smul_comp _ _ _ r φ ψ := TLMonHom.ext (Linear.smul_comp _ _ _ r φ.f ψ.f)
  comp_smul _ _ _ φ r ψ := TLMonHom.ext (Linear.comp_smul _ _ _ φ.f r ψ.f)

/-- **The zero-strand monoidal unit** `([1], δ⁻¹ e_0)`. -/
noncomputable def unitObj : TLMonObj T hε :=
  ⟨GObj.mk 1, vacIdem, vacIdem_idem⟩

@[simp] theorem unitObj_X : (unitObj (T := T) (hε := hε)).X = GObj.mk 1 := rfl
@[simp] theorem unitObj_p : (unitObj (T := T) (hε := hε)).p = vacIdem := rfl

/-- Tensor product of objects in `TLMonObj`. -/
noncomputable def mTensObj (P Q : TLMonObj T hε) : TLMonObj T hε :=
  ⟨tensObj P.X Q.X, tensHom P.p Q.p, by rw [← tensHom_comp, P.idem, Q.idem]⟩

@[simp] theorem mTensObj_X (P Q : TLMonObj T hε) : (mTensObj P Q).X = tensObj P.X Q.X := rfl
@[simp] theorem mTensObj_p (P Q : TLMonObj T hε) : (mTensObj P Q).p = tensHom P.p Q.p := rfl

/-- Tensor product of morphisms in `TLMonObj`. -/
noncomputable def mTensHom {P₁ Q₁ P₂ Q₂ : TLMonObj T hε} (φ : P₁ ⟶ Q₁) (ψ : P₂ ⟶ Q₂) :
    mTensObj P₁ P₂ ⟶ mTensObj Q₁ Q₂ :=
  ⟨tensHom φ.f ψ.f, by
    dsimp only [mTensObj_X, mTensObj_p]
    rw [← tensHom_comp, ← tensHom_comp, φ.comm, ψ.comm]⟩

@[simp] theorem mTensHom_f {P₁ Q₁ P₂ Q₂ : TLMonObj T hε} (φ : P₁ ⟶ Q₁) (ψ : P₂ ⟶ Q₂) :
    (mTensHom φ ψ).f = tensHom φ.f ψ.f := rfl

/-- Associator isomorphism `(P ⊗ Q) ⊗ R ≅ P ⊗ (Q ⊗ R)` in `TLMonObj`. -/
noncomputable def mAssoc (P Q R : TLMonObj T hε) :
    mTensObj (mTensObj P Q) R ≅ mTensObj P (mTensObj Q R) where
  hom := ⟨tensHom (tensHom P.p Q.p) R.p ≫ eqToHom (tensObj_assoc P.X Q.X R.X), by
    dsimp only [mTensObj_X, mTensObj_p]
    set L := tensHom (tensHom P.p Q.p) R.p
    set R' := tensHom P.p (tensHom Q.p R.p)
    set e := eqToHom (tensObj_assoc P.X Q.X R.X)
    have hL : L ≫ L = L := by
      simp only [L, ← tensHom_comp, P.idem, Q.idem, R.idem]
    calc L ≫ (L ≫ e) ≫ R'
        = L ≫ L ≫ (e ≫ R') := by rw [Category.assoc L e R']
      _ = L ≫ L ≫ (L ≫ e) := by rw [← assoc_nat P.p Q.p R.p]
      _ = (L ≫ L) ≫ (L ≫ e) := by rw [← Category.assoc L L (L ≫ e)]
      _ = L ≫ e := by rw [hL, ← Category.assoc L L e, hL]⟩
  inv := ⟨tensHom P.p (tensHom Q.p R.p) ≫ eqToHom (tensObj_assoc P.X Q.X R.X).symm, by
    dsimp only [mTensObj_X, mTensObj_p]
    set L := tensHom (tensHom P.p Q.p) R.p
    set R' := tensHom P.p (tensHom Q.p R.p)
    set e := eqToHom (tensObj_assoc P.X Q.X R.X)
    set e' := eqToHom (tensObj_assoc P.X Q.X R.X).symm
    have hR : R' ≫ R' = R' := by
      simp only [R', ← tensHom_comp, P.idem, Q.idem, R.idem]
    have hee' : e ≫ e' = 𝟙 _ := by simp [e, e']
    have he'e : e' ≫ e = 𝟙 _ := by simp [e, e']
    have hinv : e' ≫ L = R' ≫ e' := by
      calc e' ≫ L
          = e' ≫ L ≫ (e ≫ e') := by rw [hee', Category.comp_id]
        _ = e' ≫ (L ≫ e) ≫ e' := by rw [← Category.assoc L e e']
        _ = e' ≫ (e ≫ R') ≫ e' := by rw [assoc_nat P.p Q.p R.p]
        _ = (e' ≫ e) ≫ (R' ≫ e') := by rw [Category.assoc e R' e', ← Category.assoc e' e (R' ≫ e')]
        _ = R' ≫ e' := by rw [he'e, Category.id_comp]
    calc R' ≫ (R' ≫ e') ≫ L
        = R' ≫ R' ≫ (e' ≫ L) := by rw [Category.assoc R' e' L]
      _ = R' ≫ R' ≫ (R' ≫ e') := by rw [hinv]
      _ = (R' ≫ R') ≫ (R' ≫ e') := by rw [← Category.assoc R' R' (R' ≫ e')]
      _ = R' ≫ e' := by rw [hR, ← Category.assoc R' R' e', hR]⟩
  hom_inv_id := TLMonHom.ext (by
    dsimp only [comp_f, id_f, mTensObj_p]
    have hL : tensHom (tensHom P.p Q.p) R.p ≫ tensHom (tensHom P.p Q.p) R.p =
        tensHom (tensHom P.p Q.p) R.p := by
      rw [← tensHom_comp, ← tensHom_comp, P.idem, Q.idem, R.idem]
    rw [Category.assoc, ← Category.assoc (eqToHom _), ← assoc_nat P.p Q.p R.p, Category.assoc,
      eqToHom_trans, eqToHom_refl, Category.comp_id, hL])
  inv_hom_id := TLMonHom.ext (by
    dsimp only [comp_f, id_f, mTensObj_p]
    have hR : tensHom P.p (tensHom Q.p R.p) ≫ tensHom P.p (tensHom Q.p R.p) =
        tensHom P.p (tensHom Q.p R.p) := by
      rw [← tensHom_comp, ← tensHom_comp, P.idem, Q.idem, R.idem]
    rw [Category.assoc, assoc_nat P.p Q.p R.p, ← Category.assoc (eqToHom _), eqToHom_trans,
      eqToHom_refl, Category.id_comp, hR])

/-- Left unitor isomorphism `𝟙_ ⊗ P ≅ P` in `TLMonObj`. -/
noncomputable def mLeftUnitor (P : TLMonObj T hε) : mTensObj unitObj P ≅ P where
  hom := ⟨uL P.X.a ≫ P.p, by
    dsimp only [mTensObj_X, mTensObj_p, unitObj_X, unitObj_p]
    rw [Category.assoc, P.idem, ← Category.assoc, uL_nat P.p, Category.assoc, P.idem]⟩
  inv := ⟨P.p ≫ vL P.X.a, by
    dsimp only [mTensObj_X, mTensObj_p, unitObj_X, unitObj_p]
    rw [Category.assoc, vL_nat P.p, ← Category.assoc, P.idem, ← Category.assoc, P.idem]⟩
  hom_inv_id := TLMonHom.ext (by
    dsimp only [comp_f, id_f, mTensObj_p, unitObj_p]
    rw [Category.assoc, ← Category.assoc P.p, P.idem, ← Category.assoc, ← uL_nat P.p,
      Category.assoc, uL_comp_vL, ← tensHom_comp, vacIdem_idem, Category.comp_id])
  inv_hom_id := TLMonHom.ext (by
    dsimp only [comp_f, id_f]
    rw [Category.assoc, ← Category.assoc (vL _), vL_comp_uL, Category.id_comp, P.idem])

/-- Right unitor isomorphism `P ⊗ 𝟙_ ≅ P` in `TLMonObj`. -/
noncomputable def mRightUnitor (P : TLMonObj T hε) : mTensObj P unitObj ≅ P where
  hom := ⟨uR P.X.a ≫ P.p, by
    dsimp only [mTensObj_X, mTensObj_p, unitObj_X, unitObj_p]
    rw [Category.assoc, P.idem, ← Category.assoc, uR_nat P.p, Category.assoc, P.idem]⟩
  inv := ⟨P.p ≫ vR P.X.a, by
    dsimp only [mTensObj_X, mTensObj_p, unitObj_X, unitObj_p]
    rw [Category.assoc, vR_nat P.p, ← Category.assoc, P.idem, ← Category.assoc, P.idem]⟩
  hom_inv_id := TLMonHom.ext (by
    dsimp only [comp_f, id_f, mTensObj_p, unitObj_p]
    rw [Category.assoc, ← Category.assoc P.p, P.idem, ← Category.assoc, ← uR_nat P.p,
      Category.assoc, uR_comp_vR, ← tensHom_comp, Category.comp_id, vacIdem_idem])
  inv_hom_id := TLMonHom.ext (by
    dsimp only [comp_f, id_f]
    rw [Category.assoc, ← Category.assoc (vR _), vR_comp_uR, Category.id_comp, P.idem])

noncomputable instance : MonoidalCategoryStruct (TLMonObj T hε) where
  tensorObj := mTensObj
  whiskerLeft X _ _ g := mTensHom (𝟙 X) g
  whiskerRight f Y := mTensHom f (𝟙 Y)
  tensorHom := mTensHom
  tensorUnit := unitObj
  associator := mAssoc
  leftUnitor := mLeftUnitor
  rightUnitor := mRightUnitor

/-- **The monoidal category structure on the idempotent-completed glued Temperley–Lieb category.** -/
noncomputable instance : MonoidalCategory (TLMonObj T hε) :=
  MonoidalCategory.ofTensorHom
    (id_tensorHom_id := fun _ _ => TLMonHom.ext rfl)
    (id_tensorHom := fun _ {_ _} _ => rfl)
    (tensorHom_id := fun {_ _} _ _ => rfl)
    (tensorHom_comp_tensorHom := fun f₁ f₂ g₁ g₂ =>
      TLMonHom.ext (tensHom_comp f₁.f g₁.f f₂.f g₂.f).symm)
    (associator_naturality := fun {X₁ X₂ X₃ Y₁ Y₂ Y₃} f₁ f₂ f₃ => TLMonHom.ext (by
      show tensHom (tensHom f₁.f f₂.f) f₃.f ≫
          (tensHom (tensHom Y₁.p Y₂.p) Y₃.p ≫ eqToHom (tensObj_assoc Y₁.X Y₂.X Y₃.X)) =
        (tensHom (tensHom X₁.p X₂.p) X₃.p ≫ eqToHom (tensObj_assoc X₁.X X₂.X X₃.X)) ≫
          tensHom f₁.f (tensHom f₂.f f₃.f)
      rw [← Category.assoc, ← tensHom_comp, ← tensHom_comp, f₁.comm_right, f₂.comm_right,
        f₃.comm_right, assoc_nat X₁.p X₂.p X₃.p, Category.assoc, ← tensHom_comp, ← tensHom_comp,
        f₁.comm_left, f₂.comm_left, f₃.comm_left, assoc_nat f₁.f f₂.f f₃.f]))
    (leftUnitor_naturality := fun {P Q} φ => TLMonHom.ext (by
      show tensHom vacIdem φ.f ≫ (uL Q.X.a ≫ Q.p) = (uL P.X.a ≫ P.p) ≫ φ.f
      rw [← Category.assoc, uL_nat φ.f, Category.assoc, φ.comm_right, Category.assoc,
        φ.comm_left]))
    (rightUnitor_naturality := fun {P Q} φ => TLMonHom.ext (by
      show tensHom φ.f vacIdem ≫ (uR Q.X.a ≫ Q.p) = (uR P.X.a ≫ P.p) ≫ φ.f
      rw [← Category.assoc, uR_nat φ.f, Category.assoc, φ.comm_right, Category.assoc,
        φ.comm_left]))
    (pentagon := fun W X Y Z => TLMonHom.ext (by
      show tensHom (tensHom (tensHom W.p X.p) Y.p ≫ eqToHom (tensObj_assoc W.X X.X Y.X)) Z.p ≫
          ((tensHom (tensHom W.p (tensHom X.p Y.p)) Z.p ≫
              eqToHom (tensObj_assoc W.X (tensObj X.X Y.X) Z.X)) ≫
            tensHom W.p (tensHom (tensHom X.p Y.p) Z.p ≫ eqToHom (tensObj_assoc X.X Y.X Z.X))) =
        (tensHom (tensHom (tensHom W.p X.p) Y.p) Z.p ≫
            eqToHom (tensObj_assoc (tensObj W.X X.X) Y.X Z.X)) ≫
          (tensHom (tensHom W.p X.p) (tensHom Y.p Z.p) ≫
            eqToHom (tensObj_assoc W.X X.X (tensObj Y.X Z.X)))
      set IdL := tensHom (tensHom (tensHom W.p X.p) Y.p) Z.p
      set M2 := tensHom (tensHom W.p (tensHom X.p Y.p)) Z.p
      have hIdL : IdL ≫ IdL = IdL := by
        simp only [IdL, ← tensHom_comp, W.idem, X.idem, Y.idem, Z.idem]
      have hM2 : M2 ≫ M2 = M2 := by
        simp only [M2, ← tensHom_comp, W.idem, X.idem, Y.idem, Z.idem]
      have h1 : tensHom (tensHom (tensHom W.p X.p) Y.p ≫ eqToHom (tensObj_assoc W.X X.X Y.X))
          Z.p = IdL ≫ tensHom (eqToHom (tensObj_assoc W.X X.X Y.X)) (𝟙 Z.X) := by
        conv_lhs => rw [← Category.comp_id Z.p]
        rw [tensHom_comp]
      have h1' : tensHom (eqToHom (tensObj_assoc W.X X.X Y.X)) (𝟙 Z.X) ≫ M2 =
          IdL ≫ tensHom (eqToHom (tensObj_assoc W.X X.X Y.X)) (𝟙 Z.X) := by
        simp only [M2, IdL]
        conv_lhs =>
          rw [← tensHom_comp, ← assoc_nat W.p X.p Y.p, Category.id_comp, ← Category.comp_id Z.p,
            tensHom_comp]
      have h3 : tensHom W.p (tensHom (tensHom X.p Y.p) Z.p ≫ eqToHom (tensObj_assoc X.X Y.X Z.X)) =
          tensHom W.p (tensHom (tensHom X.p Y.p) Z.p) ≫
            tensHom (𝟙 W.X) (eqToHom (tensObj_assoc X.X Y.X Z.X)) := by
        conv_lhs => rw [← Category.comp_id W.p]
        rw [tensHom_comp]
      have h23 : eqToHom (tensObj_assoc W.X (tensObj X.X Y.X) Z.X) ≫
          tensHom W.p (tensHom (tensHom X.p Y.p) Z.p) =
          M2 ≫ eqToHom (tensObj_assoc W.X (tensObj X.X Y.X) Z.X) :=
        (assoc_nat W.p (tensHom X.p Y.p) Z.p).symm
      have hRHS : (IdL ≫ eqToHom (tensObj_assoc (tensObj W.X X.X) Y.X Z.X)) ≫
          (tensHom (tensHom W.p X.p) (tensHom Y.p Z.p) ≫
            eqToHom (tensObj_assoc W.X X.X (tensObj Y.X Z.X))) =
          IdL ≫ (eqToHom (tensObj_assoc (tensObj W.X X.X) Y.X Z.X) ≫
            eqToHom (tensObj_assoc W.X X.X (tensObj Y.X Z.X))) := by
        rw [Category.assoc, ← Category.assoc (eqToHom _), ← assoc_nat (tensHom W.p X.p) Y.p Z.p,
          ← Category.assoc, ← Category.assoc, hIdL, Category.assoc]
      rw [hRHS, h1, h3]
      simp only [Category.assoc]
      rw [← Category.assoc (eqToHom (tensObj_assoc W.X (tensObj X.X Y.X) Z.X)), h23,
        Category.assoc M2, ← Category.assoc M2 M2, hM2,
        ← Category.assoc (tensHom (eqToHom (tensObj_assoc W.X X.X Y.X)) (𝟙 Z.X)) M2, h1']
      simp only [Category.assoc]
      rw [← Category.assoc IdL IdL, hIdL, tensHom_pentagon W.X X.X Y.X Z.X]))
    (triangle := fun P Q => TLMonHom.ext (by
      show (tensHom (tensHom P.p vacIdem) Q.p ≫ eqToHom (tensObj_assoc P.X (GObj.mk 1) Q.X)) ≫
          tensHom P.p (uL Q.X.a ≫ Q.p) =
        tensHom (uR P.X.a ≫ P.p) Q.p
      have hPQ : tensHom P.p (uL Q.X.a ≫ Q.p) =
          tensHom (𝟙 P.X) (uL Q.X.a) ≫ tensHom P.p Q.p := by
        conv_lhs => rw [← Category.id_comp P.p]
        rw [tensHom_comp]
      rw [hPQ, Category.assoc, ← Category.assoc (eqToHom _), triangle_gobj P.X.a Q.X.a,
        ← Category.assoc, ← tensHom_comp, ← tensHom_comp, uR_nat P.p, Category.assoc, P.idem,
        Category.comp_id, Q.idem]))

noncomputable instance : MonoidalPreadditive (TLMonObj T hε) where
  whiskerLeft_zero := TLMonHom.ext (tensHom_zero_right _)
  zero_whiskerRight := TLMonHom.ext (tensHom_zero_left _)
  whiskerLeft_add f g := TLMonHom.ext (tensHom_add_right _ f.f g.f)
  add_whiskerRight f g := TLMonHom.ext (tensHom_add_left f.f g.f _)

noncomputable instance : MonoidalLinear K (TLMonObj T hε) where
  whiskerLeft_smul X {_ _} r f := TLMonHom.ext (tensHom_smul_right r X.p f.f)
  smul_whiskerRight r {_ _} f X := TLMonHom.ext (tensHom_smul_left r f.f X.p)

variable (T hε) in
/-- **The full and faithful `K`-linear embedding** of the positive-strand glued category `GObj`
into its monoidal idempotent completion `TLMonObj`. -/
noncomputable def inclG : GObj T hε ⥤ TLMonObj T hε where
  obj X := ⟨X, 𝟙 X, Category.id_comp _⟩
  map f := ⟨f, by simp⟩
  map_id _ := rfl
  map_comp _ _ := rfl

instance inclG_faithful : (inclG T hε).Faithful where
  map_injective h := congrArg TLMonHom.f h

instance inclG_full : (inclG T hε).Full where
  map_surjective φ := ⟨φ.f, TLMonHom.ext rfl⟩

instance inclG_additive : (inclG T hε).Additive where
  map_add := rfl

instance inclG_linear : (inclG T hε).Linear K where
  map_smul _ _ := rfl

theorem inclG_tensorObj (X Y : GObj T hε) :
    (inclG T hε).obj (tensObj X Y) = ((inclG T hε).obj X ⊗ (inclG T hε).obj Y) := by
  show TLMonObj.mk (tensObj X Y) (𝟙 (tensObj X Y)) _ =
    TLMonObj.mk (tensObj X Y) (tensHom (𝟙 X) (𝟙 Y)) _
  congr 1
  exact (tensHom_id X Y).symm

theorem inclG_tensorHom {X Y X' Y' : GObj T hε} (f : X ⟶ Y) (g : X' ⟶ Y') :
    ((inclG T hε).map f ⊗ₘ (inclG T hε).map g).f = tensHom f g :=
  rfl

end Monoidal

end QOU.HeckeTemperleyLieb.TLGluedMonoidal
