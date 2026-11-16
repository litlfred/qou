import QOU.Archimedean.BlochRigidity.Derivative
import Mathlib.Analysis.Analytic.Constructions
import Mathlib.Analysis.Calculus.FDeriv.Analytic
import Mathlib.Analysis.NormedSpace.Connected
import QOU.Archimedean.BlochRigidity.Growth
import QOU.Archimedean.BlochRigidity.Vanishing
import QOU.Archimedean.BlochSuslinComplex

/-!
# Bloch–Suslin rigidity against an abstract Dolbeault structure

The structure: a cotangent fibre `M` (a `ℂ`-vector space) with a complex structure `J`,
`J² = -1`, and a frame `e = dz`, `ē = dz̄` of its `±i` eigenlines; a class of functions
(`mem z f`: "`f` belongs to the class near `z`") and a point derivation `d f z ∈ M`
satisfying Leibniz, the chain rule along holomorphic maps, a real structure, and
commutation of `∂`, `∂̄`. The operators `∂ = c₁ ∘ d` and `∂̄ = c₂ ∘ d` are the coordinates of
the `+i` and `-i` parts `(1 ∓ iJ)/2` of `d`; they are not primitive.

Only three axioms are analytic: members are continuous (`cont`), Cauchy–Riemann at a point
(`cauchyRiemann`), and a function with `d f = 0` on a connected open set is constant
(`const`).
-/

open Complex Filter Topology

namespace QOU.Archimedean.BlochRigidity

/-- **Abstract Dolbeault structure on the plane.** -/
structure DolbeaultStructure where
  /-- The cotangent fibre. -/
  M : Type
  [acg : AddCommGroup M]
  [mod : Module ℂ M]
  /-- The complex structure. -/
  J : M →ₗ[ℂ] M
  J_sq : ∀ m, J (J m) = -m
  /-- `dz`, spanning the `+i` eigenline. -/
  e : M
  /-- `dz̄`, spanning the `-i` eigenline. -/
  ebar : M
  J_e : J e = I • e
  J_ebar : J ebar = -(I • ebar)
  e_ne : e ≠ 0
  ebar_ne : ebar ≠ 0
  /-- Coordinates of the `±i` parts. -/
  c₁ : M →ₗ[ℂ] ℂ
  c₂ : M →ₗ[ℂ] ℂ
  proj₁ : ∀ m, (1 / 2 : ℂ) • (m - I • J m) = c₁ m • e
  proj₂ : ∀ m, (1 / 2 : ℂ) • (m + I • J m) = c₂ m • ebar
  /-- The function class, as a germ predicate. -/
  mem : ℂ → (ℂ → ℂ) → Prop
  /-- The point derivation. -/
  d : (ℂ → ℂ) → ℂ → M
  mem_congr : ∀ {z f g}, mem z f → f =ᶠ[𝓝 z] g → mem z g
  mem_nhds : ∀ {z f}, mem z f → ∀ᶠ w in 𝓝 z, mem w f
  mem_add : ∀ {z f g}, mem z f → mem z g → mem z (fun w => f w + g w)
  mem_mul : ∀ {z f g}, mem z f → mem z g → mem z (fun w => f w * g w)
  mem_holo : ∀ {z h}, AnalyticAt ℂ h z → mem z h
  mem_comp : ∀ {z f g}, AnalyticAt ℂ g z → mem (g z) f → mem z (fun w => f (g w))
  mem_conj : ∀ {z f}, mem z f → mem z (fun w => (starRingEnd ℂ) (f w))
  mem_dz : ∀ {z f}, mem z f → mem z (fun w => c₁ (d f w))
  d_congr : ∀ {z f g}, f =ᶠ[𝓝 z] g → d f z = d g z
  d_add : ∀ {z f g}, mem z f → mem z g → d (fun w => f w + g w) z = d f z + d g z
  d_mul : ∀ {z f g}, mem z f → mem z g →
    d (fun w => f w * g w) z = f z • d g z + g z • d f z
  d_holo : ∀ {z h}, AnalyticAt ℂ h z → d h z = deriv h z • e
  d_comp : ∀ {z f g}, AnalyticAt ℂ g z → mem (g z) f →
    d (fun w => f (g w)) z = (deriv g z * c₁ (d f (g z))) • e
      + ((starRingEnd ℂ) (deriv g z) * c₂ (d f (g z))) • ebar
  d_conj : ∀ {z f}, mem z f →
    d (fun w => (starRingEnd ℂ) (f w)) z
      = (starRingEnd ℂ) (c₂ (d f z)) • e + (starRingEnd ℂ) (c₁ (d f z)) • ebar
  d_comm : ∀ {z f}, mem z f →
    c₂ (d (fun w => c₁ (d f w)) z) = c₁ (d (fun w => c₂ (d f w)) z)
  /-- Analytic axiom 1: members are continuous. -/
  cont : ∀ {z f}, mem z f → ContinuousAt f z
  /-- Analytic axiom 2: Cauchy–Riemann at a point. -/
  cauchyRiemann : ∀ {z f}, mem z f → c₂ (d f z) = 0 → DifferentiableAt ℂ f z
  /-- Analytic axiom 3: `d f = 0` on a connected open set makes `f` constant there. This is
  unit simplicity (flat sections of the trivial object are constants, `H⁰ = ℂ`). It is dual to
  non-degenerate integration plus exactness of compactly supported top forms; see
  `eq_smul_one_of_stokes` in `IntegrationBridge`. -/
  const : ∀ {U : Set ℂ} {f}, IsOpen U → IsPreconnected U →
    (∀ z ∈ U, mem z f ∧ d f z = 0) → ∀ z ∈ U, ∀ w ∈ U, f z = f w

namespace DolbeaultStructure

attribute [instance] acg mod

variable (S : DolbeaultStructure)

/-- `∂f`, the `dz`-coordinate of `d f`. -/
def dz (f : ℂ → ℂ) (z : ℂ) : ℂ := S.c₁ (S.d f z)

/-- `∂̄f`, the `dz̄`-coordinate of `d f`. -/
def dzb (f : ℂ → ℂ) (z : ℂ) : ℂ := S.c₂ (S.d f z)

theorem smul_e_inj {a b : ℂ} (h : a • S.e = b • S.e) : a = b := by
  have : (a - b) • S.e = 0 := by rw [sub_smul, h, sub_self]
  rcases smul_eq_zero.1 this with h' | h'
  · exact sub_eq_zero.1 h'
  · exact absurd h' S.e_ne

theorem smul_ebar_inj {a b : ℂ} (h : a • S.ebar = b • S.ebar) : a = b := by
  have : (a - b) • S.ebar = 0 := by rw [sub_smul, h, sub_self]
  rcases smul_eq_zero.1 this with h' | h'
  · exact sub_eq_zero.1 h'
  · exact absurd h' S.ebar_ne

theorem I_smul_I_smul (m : S.M) : I • I • m = -m := by
  rw [smul_smul, I_mul_I, neg_one_smul]

theorem c₁_e : S.c₁ S.e = 1 := by
  apply S.smul_e_inj
  rw [← S.proj₁, S.J_e, S.I_smul_I_smul, sub_neg_eq_add, ← two_smul ℂ, smul_smul, one_smul]
  norm_num

theorem c₂_e : S.c₂ S.e = 0 := by
  apply S.smul_ebar_inj
  rw [← S.proj₂, S.J_e, S.I_smul_I_smul, add_neg_cancel, smul_zero, zero_smul]

theorem c₁_ebar : S.c₁ S.ebar = 0 := by
  apply S.smul_e_inj
  rw [← S.proj₁, S.J_ebar, smul_neg, S.I_smul_I_smul, neg_neg, sub_self, smul_zero, zero_smul]

theorem c₂_ebar : S.c₂ S.ebar = 1 := by
  apply S.smul_ebar_inj
  rw [← S.proj₂, S.J_ebar, smul_neg, S.I_smul_I_smul, neg_neg, ← two_smul ℂ, smul_smul,
    one_smul]
  norm_num

@[simp] theorem c₁_frame (a b : ℂ) : S.c₁ (a • S.e + b • S.ebar) = a := by
  simp [S.c₁_e, S.c₁_ebar]

@[simp] theorem c₂_frame (a b : ℂ) : S.c₂ (a • S.e + b • S.ebar) = b := by
  simp [S.c₂_e, S.c₂_ebar]

/-- Every covector is the sum of its `±i` parts. -/
theorem decomp (m : S.M) : m = S.c₁ m • S.e + S.c₂ m • S.ebar := by
  rw [← S.proj₁, ← S.proj₂, ← smul_add]
  rw [show m - I • S.J m + (m + I • S.J m) = (2 : ℂ) • m by rw [two_smul]; abel, smul_smul]
  norm_num

theorem ext_coord {m m' : S.M} (h1 : S.c₁ m = S.c₁ m') (h2 : S.c₂ m = S.c₂ m') : m = m' := by
  rw [S.decomp m, S.decomp m', h1, h2]

/-! ### Derived rules -/

theorem mem_const (z c : ℂ) : S.mem z (fun _ => c) := S.mem_holo analyticAt_const

theorem d_const (z c : ℂ) : S.d (fun _ => c) z = 0 := by
  rw [S.d_holo analyticAt_const, deriv_const, zero_smul]

theorem mem_const_mul {z : ℂ} {f : ℂ → ℂ} (c : ℂ) (hf : S.mem z f) :
    S.mem z (fun w => c * f w) := S.mem_mul (S.mem_const z c) hf

theorem d_const_mul {z : ℂ} {f : ℂ → ℂ} (c : ℂ) (hf : S.mem z f) :
    S.d (fun w => c * f w) z = c • S.d f z := by
  rw [S.d_mul (S.mem_const z c) hf, S.d_const, smul_zero, add_zero]

theorem mem_sub {z : ℂ} {f g : ℂ → ℂ} (hf : S.mem z f) (hg : S.mem z g) :
    S.mem z (fun w => f w - g w) := by
  have := S.mem_add hf (S.mem_const_mul (-1) hg)
  simpa [← sub_eq_add_neg] using this

theorem d_sub {z : ℂ} {f g : ℂ → ℂ} (hf : S.mem z f) (hg : S.mem z g) :
    S.d (fun w => f w - g w) z = S.d f z - S.d g z := by
  have e : (fun w => f w - g w) = fun w => f w + (-1) * g w := by funext w; ring
  rw [e, S.d_add hf (S.mem_const_mul (-1) hg), S.d_const_mul (-1) hg, neg_one_smul,
    ← sub_eq_add_neg]

theorem dz_comp {z : ℂ} {f g : ℂ → ℂ} (hg : AnalyticAt ℂ g z) (hf : S.mem (g z) f) :
    S.dz (fun w => f (g w)) z = deriv g z * S.dz f (g z) := by
  simp [dz, S.d_comp hg hf]

theorem dzb_comp {z : ℂ} {f g : ℂ → ℂ} (hg : AnalyticAt ℂ g z) (hf : S.mem (g z) f) :
    S.dzb (fun w => f (g w)) z = (starRingEnd ℂ) (deriv g z) * S.dzb f (g z) := by
  simp [dzb, S.d_comp hg hf]

theorem dzb_holo {z : ℂ} {h : ℂ → ℂ} (hh : AnalyticAt ℂ h z) : S.dzb h z = 0 := by
  simp [dzb, S.d_holo hh, S.c₂_e]

theorem dzb_mul_holo {z : ℂ} {f h : ℂ → ℂ} (hf : S.mem z f) (hh : AnalyticAt ℂ h z) :
    S.dzb (fun w => f w * h w) z = h z * S.dzb f z := by
  simp only [dzb, S.d_mul hf (S.mem_holo hh), map_add, map_smul, smul_eq_mul]
  rw [show S.c₂ (S.d h z) = S.dzb h z from rfl, S.dzb_holo hh]
  ring

/-- **Real structure.** For a real-valued member, `∂̄f = conj (∂f)`. -/
theorem dzb_of_real {z : ℂ} {f : ℂ → ℂ} (hf : S.mem z f)
    (hr : ∀ w, (starRingEnd ℂ) (f w) = f w) : S.dzb f z = (starRingEnd ℂ) (S.dz f z) := by
  have h := S.d_conj hf
  have e : (fun w => (starRingEnd ℂ) (f w)) = f := funext hr
  rw [e] at h
  have := congrArg S.c₂ h
  simpa [dzb, dz] using this

end DolbeaultStructure
namespace DolbeaultStructure

variable (S : DolbeaultStructure)

theorem dz_five {z : ℂ} {A B C D E : ℂ → ℂ} (hA : S.mem z A) (hB : S.mem z B)
    (hC : S.mem z C) (hD : S.mem z D) (hE : S.mem z E) :
    S.dz (fun w => A w - B w + C w - D w + E w) z
      = S.dz A z - S.dz B z + S.dz C z - S.dz D z + S.dz E z := by
  simp only [dz]
  rw [S.d_add (S.mem_sub (S.mem_add (S.mem_sub hA hB) hC) hD) hE,
    S.d_sub (S.mem_add (S.mem_sub hA hB) hC) hD, S.d_add (S.mem_sub hA hB) hC, S.d_sub hA hB]
  simp only [map_add, map_sub]

theorem dzb_four {z : ℂ} {A B C D : ℂ → ℂ} (hA : S.mem z A) (hB : S.mem z B)
    (hC : S.mem z C) (hD : S.mem z D) :
    S.dzb (fun w => A w + B w - C w + D w) z
      = S.dzb A z + S.dzb B z - S.dzb C z + S.dzb D z := by
  simp only [dzb]
  rw [S.d_add (S.mem_sub (S.mem_add hA hB) hC) hD, S.d_sub (S.mem_add hA hB) hC,
    S.d_add hA hB]
  simp only [map_add, map_sub]

/-- The `∂`-form of a real function, `ω = ∂φ`. -/
def omegaS (φ : ℂ → ℝ) (z : ℂ) : ℂ := S.dz (fun w => (φ w : ℂ)) z

/-- Its antiholomorphic derivative `γ = ∂̄∂φ`. -/
def gammaS (φ : ℂ → ℝ) (z : ℂ) : ℂ := S.dzb (S.omegaS φ) z

variable {S} {φ : ℂ → ℝ}

/-- **D1a, abstract.** -/
theorem first_identityS (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    {x y : ℂ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1) (hxy : x ≠ y) :
    -S.omegaS φ y + S.omegaS φ (y / x) * (1 / x)
      - S.omegaS φ (y / x * ((1 - x) / (1 - y))) * ((1 - x) / (x * (1 - y) ^ 2))
      + S.omegaS φ ((1 - x) / (1 - y)) * ((1 - x) / (1 - y) ^ 2) = 0 := by
  have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  obtain ⟨a0, a1, b0, b1, c0, c1⟩ := args_ne hx0 hx1 hy0 hy1 hxy
  set Φ : ℂ → ℂ := fun w => (φ w : ℂ) with hΦdef
  have d1 : HasDerivAt (fun y => y / x) (1 / x) y := (hasDerivAt_id y).div_const x
  have d5 : HasDerivAt (fun y => (1 - x) / (1 - y)) ((1 - x) / (1 - y) ^ 2) y := by
    have := (hasDerivAt_const y (1 - x)).div ((hasDerivAt_const y (1 : ℂ)).sub (hasDerivAt_id y))
      h1y
    convert this using 1
    simp
  have d4 : HasDerivAt (fun y => y / x * ((1 - x) / (1 - y)))
      ((1 - x) / (x * (1 - y) ^ 2)) y := by
    convert d1.mul d5 using 1
    field_simp
    ring
  have g1 : AnalyticAt ℂ (fun y : ℂ => y / x) y := by fun_prop (disch := assumption)
  have g4 : AnalyticAt ℂ (fun y : ℂ => y / x * ((1 - x) / (1 - y))) y := by
    fun_prop (disch := assumption)
  have g5 : AnalyticAt ℂ (fun y : ℂ => (1 - x) / (1 - y)) y := by
    fun_prop (disch := assumption)
  have m1 := S.mem_comp (f := Φ) g1 (hΦ _ a0 a1)
  have m4 := S.mem_comp (f := Φ) g4 (hΦ _ b0 b1)
  have m5 := S.mem_comp (f := Φ) g5 (hΦ _ c0 c1)
  have e1 := S.dz_comp (f := Φ) g1 (hΦ _ a0 a1)
  have e4 := S.dz_comp (f := Φ) g4 (hΦ _ b0 b1)
  have e5 := S.dz_comp (f := Φ) g5 (hΦ _ c0 c1)
  rw [d1.deriv] at e1
  rw [d4.deriv] at e4
  rw [d5.deriv] at e5
  have hev : (fun y' => Φ x - Φ y' + Φ (y' / x) - Φ (y' / x * ((1 - x) / (1 - y')))
      + Φ ((1 - x) / (1 - y'))) =ᶠ[𝓝 y] fun _ => (0 : ℂ) := by
    have hV : IsOpen ({0, 1, x}ᶜ : Set ℂ) := (Set.toFinite _).isClosed.isOpen_compl
    filter_upwards [hV.mem_nhds (by simp [hy0, hy1, Ne.symm hxy])] with y' hy'
    simp only [Set.mem_compl_iff, Set.mem_insert_iff, Set.mem_singleton_iff, not_or] at hy'
    obtain ⟨h0, h1, h2⟩ := hy'
    have := h5 x y' hx0 hx1 h0 h1 (Ne.symm h2)
    rw [flip_eq hx0 h0 h1] at this
    simp only [hΦdef]
    exact_mod_cast this
  have hz : S.dz (fun y' => Φ x - Φ y' + Φ (y' / x) - Φ (y' / x * ((1 - x) / (1 - y')))
      + Φ ((1 - x) / (1 - y'))) y = 0 := by
    simp only [dz]
    rw [S.d_congr hev, S.d_const, map_zero]
  rw [S.dz_five (S.mem_const y _) (hΦ y hy0 hy1) m1 m4 m5] at hz
  simp only [dz, S.d_const, map_zero] at hz
  simp only [dz] at e1 e4 e5
  simp only [omegaS, dz]
  rw [e1, e4, e5] at hz
  linear_combination hz

/-- **`γ` is real.** -/
theorem gammaS_conj (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ))) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) : (starRingEnd ℂ) (S.gammaS φ z) = S.gammaS φ z := by
  have hm := hΦ z h0 h1
  have hω := S.mem_dz hm
  have hc := congrArg S.c₁ (S.d_conj hω)
  simp only [c₁_frame] at hc
  have hev : (fun w => (starRingEnd ℂ) (S.c₁ (S.d (fun w => (φ w : ℂ)) w)))
      =ᶠ[𝓝 z] fun w => S.c₂ (S.d (fun w => (φ w : ℂ)) w) := by
    filter_upwards [S.mem_nhds hm] with w hw
    exact (S.dzb_of_real hw (fun v => Complex.conj_ofReal _)).symm
  rw [S.d_congr hev, ← S.d_comm hm] at hc
  simp only [gammaS, dzb]
  exact hc.symm

theorem gammaS_ofReal_re (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ))) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) : (((S.gammaS φ z).re : ℝ) : ℂ) = S.gammaS φ z :=
  Complex.conj_eq_iff_re.1 (gammaS_conj hΦ h0 h1)

/-- **D1b, abstract (mixed derivative).** -/
theorem mixed_identityS (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    {x y : ℂ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1) (hxy : x ≠ y) :
    S.gammaS φ (y / x) * (starRingEnd ℂ) (-y / x ^ 2) * (1 / x)
      - S.gammaS φ (y / x * ((1 - x) / (1 - y))) * (starRingEnd ℂ) (-y / (x ^ 2 * (1 - y)))
          * ((1 - x) / (x * (1 - y) ^ 2))
      + S.gammaS φ ((1 - x) / (1 - y)) * (starRingEnd ℂ) (-1 / (1 - y))
          * ((1 - x) / (1 - y) ^ 2) = 0 := by
  have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have hxy2 : x * (1 - y) ^ 2 ≠ 0 := mul_ne_zero hx0 (pow_ne_zero 2 h1y)
  have h1y2 : (1 - y) ^ 2 ≠ 0 := pow_ne_zero 2 h1y
  obtain ⟨a0, a1, b0, b1, c0, c1⟩ := args_ne hx0 hx1 hy0 hy1 hxy
  set ω : ℂ → ℂ := S.omegaS φ with hωdef
  have mω : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z ω := fun z h0 h1 => S.mem_dz (hΦ z h0 h1)
  have g1 : HasDerivAt (fun x => y / x) (-y / x ^ 2) x := by
    convert (hasDerivAt_const x y).div (hasDerivAt_id x) hx0 using 1
    simp
  have g5 : HasDerivAt (fun x => (1 - x) / (1 - y)) (-1 / (1 - y)) x := by
    convert ((hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_id x)).div_const (1 - y) using 1
    simp
  have g4 : HasDerivAt (fun x => y / x * ((1 - x) / (1 - y))) (-y / (x ^ 2 * (1 - y))) x := by
    convert g1.mul g5 using 1
    field_simp
    ring
  have a1' : AnalyticAt ℂ (fun x : ℂ => y / x) x := by fun_prop (disch := assumption)
  have a4' : AnalyticAt ℂ (fun x : ℂ => y / x * ((1 - x) / (1 - y))) x := by
    fun_prop (disch := assumption)
  have a5' : AnalyticAt ℂ (fun x : ℂ => (1 - x) / (1 - y)) x := by
    fun_prop (disch := assumption)
  have k1 : AnalyticAt ℂ (fun x : ℂ => 1 / x) x := by fun_prop (disch := assumption)
  have k4 : AnalyticAt ℂ (fun x : ℂ => (1 - x) / (x * (1 - y) ^ 2)) x := by
    fun_prop (disch := assumption)
  have k5 : AnalyticAt ℂ (fun x : ℂ => (1 - x) / (1 - y) ^ 2) x := by
    fun_prop (disch := assumption)
  have m1 := S.mem_comp (f := ω) a1' (mω _ a0 a1)
  have m4 := S.mem_comp (f := ω) a4' (mω _ b0 b1)
  have m5 := S.mem_comp (f := ω) a5' (mω _ c0 c1)
  have t1 := S.dzb_mul_holo m1 k1
  have t4 := S.dzb_mul_holo m4 k4
  have t5 := S.dzb_mul_holo m5 k5
  have e1 := S.dzb_comp (f := ω) a1' (mω _ a0 a1)
  have e4 := S.dzb_comp (f := ω) a4' (mω _ b0 b1)
  have e5 := S.dzb_comp (f := ω) a5' (mω _ c0 c1)
  rw [g1.deriv] at e1
  rw [g4.deriv] at e4
  rw [g5.deriv] at e5
  have hev : (fun x' => -ω y + ω (y / x') * (1 / x')
      - ω (y / x' * ((1 - x') / (1 - y))) * ((1 - x') / (x' * (1 - y) ^ 2))
      + ω ((1 - x') / (1 - y)) * ((1 - x') / (1 - y) ^ 2)) =ᶠ[𝓝 x] fun _ => (0 : ℂ) := by
    have hV : IsOpen ({0, 1, y}ᶜ : Set ℂ) := (Set.toFinite _).isClosed.isOpen_compl
    filter_upwards [hV.mem_nhds (by simp [hx0, hx1, hxy])] with x' hx'
    simp only [Set.mem_compl_iff, Set.mem_insert_iff, Set.mem_singleton_iff, not_or] at hx'
    obtain ⟨h0, h1, h2⟩ := hx'
    exact first_identityS hΦ h5 h0 h1 hy0 hy1 h2
  have hz : S.dzb (fun x' => -ω y + ω (y / x') * (1 / x')
      - ω (y / x' * ((1 - x') / (1 - y))) * ((1 - x') / (x' * (1 - y) ^ 2))
      + ω ((1 - x') / (1 - y)) * ((1 - x') / (1 - y) ^ 2)) x = 0 := by
    simp only [dzb]
    rw [S.d_congr hev, S.d_const, map_zero]
  rw [S.dzb_four (S.mem_const x _) (S.mem_mul m1 (S.mem_holo k1))
    (S.mem_mul m4 (S.mem_holo k4)) (S.mem_mul m5 (S.mem_holo k5))] at hz
  rw [t1, t4, t5, e1, e4, e5, S.dzb_holo analyticAt_const] at hz
  simp only [gammaS]
  linear_combination hz

/-- **D1, abstract.** `Re γ · |z|²|1-z|² = k · Im z`. -/
theorem gammaS_normSq_eq_mul_im (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0) :
    ∃ k : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 →
      (S.gammaS φ z).re * normSq z * normSq (1 - z) = k * z.im := by
  apply mixed_eq_mul_im
  intro x y hx0 hx1 hy0 hy1 hxy
  obtain ⟨a0, a1, b0, b1, c0, c1⟩ := args_ne hx0 hx1 hy0 hy1 hxy
  rw [gammaS_ofReal_re hΦ a0 a1, gammaS_ofReal_re hΦ b0 b1, gammaS_ofReal_re hΦ c0 c1]
  exact mixed_identityS hΦ h5 hx0 hx1 hy0 hy1 hxy


/-! ### Vanishing (D2, D3) against the structure -/

/-- Differentiating `φ ∘ g = c • φ` near `z`, `g` holomorphic, gives `ω(g z)·g' = c·ω(z)`. -/
theorem omegaS_comp_of_eventuallyEq {g : ℂ → ℂ} {z : ℂ} {c : ℝ} (hg : AnalyticAt ℂ g z)
    (hmg : S.mem (g z) (fun w => (φ w : ℂ))) (hmz : S.mem z (fun w => (φ w : ℂ)))
    (hev : (fun w => φ (g w)) =ᶠ[𝓝 z] fun w => c * φ w) :
    S.omegaS φ (g z) * deriv g z = c * S.omegaS φ z := by
  have h1 := S.dz_comp hg hmg
  have hev' : (fun w => ((φ (g w) : ℝ) : ℂ)) =ᶠ[𝓝 z] fun w => (c : ℂ) * (φ w : ℂ) := by
    filter_upwards [hev] with w hw
    rw [hw]; push_cast; ring
  have h2 : S.dz (fun w => ((φ (g w) : ℝ) : ℂ)) z = c * S.omegaS φ z := by
    simp only [dz]
    rw [S.d_congr hev', S.d_const_mul _ hmz, map_smul, smul_eq_mul]
    rfl
  rw [← h2, h1]
  simp only [omegaS]
  ring

/-- Inversion: `ω(z⁻¹) = z² ω(z)`. -/
theorem omegaS_inv (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z) {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    S.omegaS φ z⁻¹ = z ^ 2 * S.omegaS φ z := by
  have hi0 : z⁻¹ ≠ 0 := inv_ne_zero hz0
  have hi1 : z⁻¹ ≠ 1 := by rwa [ne_eq, inv_eq_one]
  have hev : (fun w : ℂ => φ w⁻¹) =ᶠ[𝓝 z] fun w => (-1 : ℝ) * φ w := by
    filter_upwards [isOpen_U.mem_nhds (mem_U'.2 ⟨hz0, hz1⟩)] with w hw
    obtain ⟨h0, h1⟩ := mem_U'.1 hw
    rw [hinv w h0 h1]; ring
  have ha : AnalyticAt ℂ (fun w : ℂ => w⁻¹) z := by fun_prop (disch := assumption)
  have := omegaS_comp_of_eventuallyEq (g := fun w => w⁻¹) ha (hΦ _ hi0 hi1) (hΦ _ hz0 hz1) hev
  rw [(hasDerivAt_inv hz0).deriv] at this
  have hz2 : z ^ 2 ≠ 0 := pow_ne_zero 2 hz0
  push_cast at this
  calc S.omegaS φ z⁻¹ = (S.omegaS φ z⁻¹ * -(z ^ 2)⁻¹) * (-z ^ 2) := by field_simp
    _ = z ^ 2 * S.omegaS φ z := by rw [this]; ring

/-- Reflection: `ω(1 - z) = ω(z)`. -/
theorem omegaS_one_sub (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (hone : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ (1 - z) = -φ z) {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    S.omegaS φ (1 - z) = S.omegaS φ z := by
  have h0 : 1 - z ≠ 0 := sub_ne_zero.2 (Ne.symm hz1)
  have h1 : 1 - z ≠ 1 := by intro h; apply hz0; linear_combination -h
  have hev : (fun w : ℂ => φ (1 - w)) =ᶠ[𝓝 z] fun w => (-1 : ℝ) * φ w := by
    filter_upwards [isOpen_U.mem_nhds (mem_U'.2 ⟨hz0, hz1⟩)] with w hw
    obtain ⟨h0, h1⟩ := mem_U'.1 hw
    rw [hone w h0 h1]; ring
  have ha : AnalyticAt ℂ (fun w : ℂ => 1 - w) z := by fun_prop
  have hd : HasDerivAt (fun w : ℂ => 1 - w) (-1) z := by
    simpa using (hasDerivAt_const z (1 : ℂ)).sub (hasDerivAt_id z)
  have := omegaS_comp_of_eventuallyEq (g := fun w => 1 - w) ha (hΦ _ h0 h1) (hΦ _ hz0 hz1) hev
  rw [hd.deriv] at this
  push_cast at this
  linear_combination -this

/-- **D2, abstract.** If `γ` vanishes on `{0,1}ᶜ`, then `ω` is holomorphic there. This is the
`cauchyRiemann` axiom applied to `ω = ∂φ`. -/
theorem omegaS_holo (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (hγ : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → S.gammaS φ z = 0) :
    DifferentiableOn ℂ (S.omegaS φ) {0, 1}ᶜ := by
  intro z hz
  obtain ⟨h0, h1⟩ := mem_U'.1 hz
  exact (S.cauchyRiemann (S.mem_dz (hΦ z h0 h1)) (hγ z h0 h1)).differentiableWithinAt

theorem continuousAt_omegaS (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    {z : ℂ} (h0 : z ≠ 0) (h1 : z ≠ 1) : ContinuousAt (S.omegaS φ) z :=
  S.cont (S.mem_dz (hΦ z h0 h1))

/-- **D3a, abstract (growth at `0`).** -/
theorem omegaS_growth (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0) :
    ∃ r : ℝ, 0 < r ∧ ∃ C : ℝ, ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r →
      ‖y * S.omegaS φ y‖ * Real.sqrt ‖y‖ ≤ C := by
  set R : ℂ → ℂ := fun y => (1 - 1 / 10) / (1 - y) ^ 2 * S.omegaS φ ((1 - 1 / 10) / (1 - y))
    with hRdef
  have hRc : ContinuousAt R 0 := by
    have hc : ContinuousAt (fun y : ℂ => (1 - 1 / 10) / (1 - y)) 0 :=
      continuousAt_const.div (continuousAt_const.sub continuousAt_id) (by norm_num)
    have hω : ContinuousAt (S.omegaS φ) ((1 - 1 / 10) / (1 - 0)) :=
      continuousAt_omegaS hΦ (by norm_num) (by norm_num)
    have hcomp : ContinuousAt (fun y : ℂ => S.omegaS φ ((1 - 1 / 10) / (1 - y))) 0 :=
      ContinuousAt.comp (f := fun y : ℂ => (1 - 1 / 10) / (1 - y)) hω hc
    show ContinuousAt (fun y : ℂ => (1 - 1 / 10) / (1 - y) ^ 2
      * S.omegaS φ ((1 - 1 / 10) / (1 - y))) 0
    exact (continuousAt_const.div ((continuousAt_const.sub continuousAt_id).pow 2)
      (by norm_num)).mul hcomp
  obtain ⟨δ, hδ, hδR⟩ := Metric.continuousAt_iff.1 hRc 1 one_pos
  set r : ℝ := min (1 / 100) (δ / 2) with hr
  have hr0 : 0 < r := lt_min (by norm_num) (by linarith)
  have hr1 : r ≤ 1 / 100 := min_le_left _ _
  have hrδ : r < δ := lt_of_le_of_lt (min_le_right _ _) (by linarith)
  have hRb : ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r → ‖R y‖ ≤ ‖R 0‖ + 1 := by
    intro y _ hy
    have := hδR (x := y) (by rw [dist_zero_right]; linarith)
    rw [dist_eq_norm] at this
    have := norm_sub_norm_le (R y) (R 0)
    linarith
  set A : Set ℂ := Metric.closedBall 0 (11 * r) ∩ {w | r ≤ ‖w‖} with hA
  have hAc : IsCompact A :=
    (isCompact_closedBall 0 (11 * r)).inter_right (isClosed_le continuous_const continuous_norm)
  have hAU : ∀ w ∈ A, w ≠ 0 ∧ w ≠ 1 := by
    intro w hw
    obtain ⟨h1, h2⟩ := hw
    simp only [Metric.mem_closedBall, dist_zero_right] at h1
    simp only [Set.mem_setOf_eq] at h2
    refine ⟨fun h => by rw [h, norm_zero] at h2; linarith, fun h => ?_⟩
    rw [h, norm_one] at h1; linarith
  have hΩc : ContinuousOn (fun w => w * S.omegaS φ w) A := by
    intro w hw
    obtain ⟨h0, h1⟩ := hAU w hw
    exact (continuousAt_id.mul (continuousAt_omegaS hΦ h0 h1)).continuousWithinAt
  obtain ⟨B, hB⟩ := hAc.exists_bound_of_continuousOn hΩc
  have hrel : ∀ y : ℂ, y ≠ 0 → ‖y‖ ≤ r →
      y * S.omegaS φ y = 10 * y * S.omegaS φ (10 * y)
        - 9 * y / (1 - y) * S.omegaS φ (9 * y / (1 - y)) / (1 - y) + y * R y := by
    intro y hy0 hyr
    have hy1 : y ≠ 1 := by intro h; rw [h, norm_one] at hyr; linarith
    have hyx : (1 / 10 : ℂ) ≠ y := by
      intro h; rw [← h] at hyr; norm_num at hyr; linarith
    have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
    have hf := first_identityS hΦ h5 (x := 1 / 10) (by norm_num) (by norm_num) hy0 hy1 hyx
    have e1 : y / (1 / 10) = 10 * y := by ring
    have e2 : 10 * y * ((1 - 1 / 10) / (1 - y)) = 9 * y / (1 - y) := by ring
    rw [e1] at hf
    rw [e2] at hf
    simp only [hRdef]
    generalize S.omegaS φ y = W0 at hf ⊢
    generalize S.omegaS φ (10 * y) = W1 at hf ⊢
    generalize S.omegaS φ (9 * y / (1 - y)) = W2 at hf ⊢
    generalize S.omegaS φ ((1 - 1 / 10) / (1 - y)) = W3 at hf ⊢
    have e3 : ((1 : ℂ) - 1 / 10) / (1 / 10 * (1 - y) ^ 2) = 9 / (1 - y) ^ 2 := by
      field_simp; ring
    rw [e3] at hf
    generalize 1 - y = t at hf ⊢
    linear_combination (-y) * hf
  obtain ⟨C, hC⟩ := growth_sqrt (Ω := fun w => w * S.omegaS φ w) hr0 hr1
    (by positivity : (0 : ℝ) ≤ ‖R 0‖ + 1) hrel hRb
    (fun w h1 h2 => hB w ⟨by simpa using h2, h1⟩)
  exact ⟨r, hr0, C, hC⟩

/-- **D3c, abstract.** If `γ` vanishes, then `ω ≡ 0` on `{0,1}ᶜ`. The function
`F = z(1-z)ω` is holomorphic with the two symmetries and a growth bound; the class-free
theorem `eq_zero_of_symm_growth` (removable singularities and Liouville) kills it. -/
theorem omegaS_eq_zero (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (hone : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ (1 - z) = -φ z)
    (hγ : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → S.gammaS φ z = 0) :
    ∀ z : ℂ, z ≠ 0 → z ≠ 1 → S.omegaS φ z = 0 := by
  obtain ⟨r, hr, C, hC⟩ := omegaS_growth hΦ h5
  set F : ℂ → ℂ := fun z => z * (1 - z) * S.omegaS φ z with hF
  have hd : DifferentiableOn ℂ F {0, 1}ᶜ := by
    have hp : DifferentiableOn ℂ (fun z : ℂ => z * (1 - z)) {0, 1}ᶜ :=
      (differentiable_id.mul ((differentiable_const (1 : ℂ)).sub differentiable_id)).differentiableOn
    exact hp.mul (omegaS_holo hΦ hγ)
  have hsym : ∀ z, z ≠ 0 → z ≠ 1 → F (1 - z) = F z := by
    intro z h0 h1; simp only [hF, omegaS_one_sub hΦ hone h0 h1]; ring
  have hinvF : ∀ z, z ≠ 0 → z ≠ 1 → F z⁻¹ * z = -F z := by
    intro z h0 h1; simp only [hF, omegaS_inv hΦ hinv h0 h1]; field_simp; ring
  have hz := eq_zero_of_symm_growth hd hsym hinvF (r := min r 1) (C := 2 * max C 0)
    (lt_min hr one_pos) ?_
  · intro z h0 h1
    have h := hz z h0 h1
    simp only [hF] at h
    have h1' : (1 - z) ≠ 0 := sub_ne_zero.2 (Ne.symm h1)
    rcases mul_eq_zero.1 h with h | h
    · exact absurd h (mul_ne_zero h0 h1')
    · exact h
  intro z h0 hz
  have hzr : ‖z‖ ≤ r := hz.trans (min_le_left _ _)
  have hz1 : ‖z‖ ≤ 1 := hz.trans (min_le_right _ _)
  have h1z : ‖1 - z‖ ≤ 2 := by
    calc ‖1 - z‖ ≤ ‖(1 : ℂ)‖ + ‖z‖ := norm_sub_le _ _
      _ ≤ 2 := by rw [norm_one]; linarith
  calc ‖F z‖ * Real.sqrt ‖z‖ = ‖1 - z‖ * (‖z * S.omegaS φ z‖ * Real.sqrt ‖z‖) := by
        simp only [hF, norm_mul]; ring
    _ ≤ 2 * max C 0 := mul_le_mul h1z ((hC z h0 hzr).trans (le_max_left _ _))
        (by positivity) (by norm_num)

/-- **D3, abstract (closing).** If `γ` vanishes, then `φ ≡ 0` on `{0,1}ᶜ`. Both coordinates of
`d φ` vanish (`∂̄φ = conj ∂φ` for real `φ`), so the `const` axiom makes `φ` constant, and
inversion-oddness makes the constant `0`. -/
theorem eq_zero_of_gammaS_eq_zero (hΦ : ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ)))
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (hone : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ (1 - z) = -φ z)
    (hγ : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → S.gammaS φ z = 0) :
    ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z = 0 := by
  have hω := omegaS_eq_zero hΦ h5 hinv hone hγ
  have hrank : 1 < Module.rank ℝ ℂ := by rw [Complex.rank_real_complex]; norm_num
  have hpc : IsPathConnected ({0, 1}ᶜ : Set ℂ) :=
    (Set.toFinite _).countable.isPathConnected_compl_of_one_lt_rank hrank
  have hd : ∀ z ∈ ({0, 1}ᶜ : Set ℂ), S.mem z (fun w => (φ w : ℂ))
      ∧ S.d (fun w => (φ w : ℂ)) z = 0 := by
    intro z hz
    obtain ⟨h0, h1⟩ := mem_U'.1 hz
    refine ⟨hΦ z h0 h1, S.ext_coord ?_ ?_⟩
    · rw [map_zero]; exact hω z h0 h1
    · rw [map_zero]
      have := S.dzb_of_real (hΦ z h0 h1) (fun v => Complex.conj_ofReal _)
      simp only [dzb] at this
      rw [this]
      have h' := hω z h0 h1
      simp only [omegaS] at h'
      rw [h', map_zero]
  have h2 : (2 : ℂ) ∈ ({0, 1}ᶜ : Set ℂ) := mem_U'.2 ⟨by norm_num, by norm_num⟩
  have hc : ∀ z ∈ ({0, 1}ᶜ : Set ℂ), φ z = φ 2 := fun z hz =>
    Complex.ofReal_injective (S.const isOpen_U hpc.isConnected.isPreconnected hd z hz 2 h2)
  have hi : (2 : ℂ)⁻¹ ∈ ({0, 1}ᶜ : Set ℂ) := mem_U'.2 ⟨by norm_num, by norm_num⟩
  have h22 : φ 2 = 0 := by
    have e1 := hinv 2 (by norm_num) (by norm_num)
    rw [hc _ hi] at e1
    linarith
  intro z h0 h1
  rw [hc z (mem_U'.2 ⟨h0, h1⟩), h22]

/-! ### Rigidity conditional on the structure -/

/-- `φ` belongs to the class of `S` on `ℂ ∖ {0,1}`. -/
def InClass (S : DolbeaultStructure) (φ : ℂ → ℝ) : Prop :=
  ∀ z, z ≠ 0 → z ≠ 1 → S.mem z (fun w => (φ w : ℂ))

theorem InClass.sub_mul {φ D : ℂ → ℝ} (hφ : InClass S φ) (hD : InClass S D) (c : ℝ) :
    InClass S (fun v => φ v - c * D v) := by
  intro z h0 h1
  have := S.mem_sub (hφ z h0 h1) (S.mem_const_mul (c : ℂ) (hD z h0 h1))
  convert this using 2 with w
  push_cast; ring

/-- `ω` is linear in the function. -/
theorem omegaS_sub_mul {D : ℂ → ℝ} {w : ℂ} (c : ℝ) (hφ : S.mem w (fun v => (φ v : ℂ)))
    (hD : S.mem w (fun v => (D v : ℂ))) :
    S.omegaS (fun v => φ v - c * D v) w = S.omegaS φ w - c * S.omegaS D w := by
  have e : (fun v => (((φ v - c * D v : ℝ)) : ℂ)) = fun v => (φ v : ℂ) - (c : ℂ) * (D v : ℂ) := by
    funext v; push_cast; ring
  simp only [omegaS, dz]
  rw [e, S.d_sub hφ (S.mem_const_mul _ hD), S.d_const_mul _ hD, map_sub, map_smul, smul_eq_mul]

/-- `γ` is linear in the function. -/
theorem gammaS_sub_mul {D : ℂ → ℝ} (c : ℝ) (hφ : InClass S φ) (hD : InClass S D) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) :
    S.gammaS (fun v => φ v - c * D v) z = S.gammaS φ z - c * S.gammaS D z := by
  have hev : S.omegaS (fun v => φ v - c * D v) =ᶠ[𝓝 z]
      fun v => S.omegaS φ v - (c : ℂ) * S.omegaS D v := by
    filter_upwards [isOpen_U.mem_nhds (mem_U'.2 ⟨h0, h1⟩)] with v hv
    obtain ⟨v0, v1⟩ := mem_U'.1 hv
    exact omegaS_sub_mul c (hφ v v0 v1) (hD v v0 v1)
  have mφ : S.mem z (S.omegaS φ) := S.mem_dz (hφ z h0 h1)
  have mD : S.mem z (S.omegaS D) := S.mem_dz (hD z h0 h1)
  simp only [gammaS, dzb]
  rw [S.d_congr hev, S.d_sub mφ (S.mem_const_mul _ mD), S.d_const_mul _ mD, map_sub, map_smul,
    smul_eq_mul]

/-- A solution in the class with vanishing constant `k` vanishes. -/
theorem eq_zero_of_kS_eq_zero (hφ : InClass S φ) (hs : BlochSymmetric φ) (h5 : SuslinFiveTerm φ)
    (hk : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → (S.gammaS φ z).re * normSq z * normSq (1 - z) = 0) :
    ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z = 0 := by
  refine eq_zero_of_gammaS_eq_zero hφ h5 hs.inv
    (fun z h0 h1 => one_sub_odd hs.inv hs.conj h5 h0 h1) ?_
  intro z h0 h1
  have hN : normSq z * normSq (1 - z) ≠ 0 :=
    mul_ne_zero (normSq_eq_zero.not.2 h0) (normSq_eq_zero.not.2 (sub_ne_zero.2 (Ne.symm h1)))
  have hre : (S.gammaS φ z).re = 0 := by
    have := hk z h0 h1
    rw [mul_assoc] at this
    exact (mul_eq_zero.1 this).resolve_right hN
  rw [← gammaS_ofReal_re hφ h0 h1, hre, ofReal_zero]

/-- **Bloch–Suslin rigidity, conditional on a Dolbeault structure.** In the function class of
any `DolbeaultStructure`, every Bloch-symmetric solution of the five-term relation on
`ℂ ∖ {0,1}` is a real multiple of a fixed such solution `D` that is nonzero somewhere. -/
theorem eq_mul_of_fiveTermS {D : ℂ → ℝ} (hDc : InClass S D) (hDs : BlochSymmetric D)
    (hD5 : SuslinFiveTerm D) {z₀ : ℂ} (hz₀0 : z₀ ≠ 0) (hz₀1 : z₀ ≠ 1) (hDz : D z₀ ≠ 0)
    (hφc : InClass S φ) (hφs : BlochSymmetric φ) (hφ5 : SuslinFiveTerm φ) :
    ∃ c : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z = c * D z := by
  obtain ⟨kD, hkD⟩ := gammaS_normSq_eq_mul_im hDc hD5
  obtain ⟨kφ, hkφ⟩ := gammaS_normSq_eq_mul_im hφc hφ5
  have hkD0 : kD ≠ 0 := by
    intro h
    exact hDz (eq_zero_of_kS_eq_zero hDc hDs hD5
      (fun z h0 h1 => by rw [hkD z h0 h1, h, zero_mul]) z₀ hz₀0 hz₀1)
  set c : ℝ := kφ / kD with hc
  set ψ : ℂ → ℝ := fun v => φ v - c * D v with hψ
  have hψc : InClass S ψ := hφc.sub_mul hDc c
  have hψs : BlochSymmetric ψ :=
    ⟨fun z h0 h1 => by simp only [hψ, hφs.inv z h0 h1, hDs.inv z h0 h1]; ring,
     fun z => by simp only [hψ, hφs.conj z, hDs.conj z]; ring⟩
  have hψ5 : SuslinFiveTerm ψ := by
    intro x y hx0 hx1 hy0 hy1 hxy
    have e1 := hφ5 x y hx0 hx1 hy0 hy1 hxy
    have e2 := hD5 x y hx0 hx1 hy0 hy1 hxy
    simp only [hψ]
    linear_combination e1 - c * e2
  obtain ⟨kψ, hkψ⟩ := gammaS_normSq_eq_mul_im hψc hψ5
  have hI0 : (I : ℂ) ≠ 0 := I_ne_zero
  have hI1 : (I : ℂ) ≠ 1 := by intro h; have := congrArg Complex.im h; simp at this
  have hlin := gammaS_sub_mul c hφc hDc hI0 hI1
  have hkψ0 : kψ = 0 := by
    have a := hkψ I hI0 hI1
    have b := hkφ I hI0 hI1
    have d := hkD I hI0 hI1
    rw [show (fun v => φ v - c * D v) = ψ from rfl] at hlin
    rw [hlin] at a
    simp only [sub_re, re_ofReal_mul, I_im, mul_one] at a b d
    have hc' : c * kD = kφ := by rw [hc]; field_simp
    linear_combination -a + b - c * d - hc'
  refine ⟨c, fun z h0 h1 => ?_⟩
  have := eq_zero_of_kS_eq_zero hψc hψs hψ5
    (fun z h0 h1 => by rw [hkψ z h0 h1, hkψ0, zero_mul]) z h0 h1
  simp only [hψ] at this
  linarith

end DolbeaultStructure

end QOU.Archimedean.BlochRigidity
