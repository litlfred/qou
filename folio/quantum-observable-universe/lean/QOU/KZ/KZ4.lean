import QOU.KZ.KZComplex
import Mathlib.Analysis.Calculus.Deriv.Prod
import Mathlib.Analysis.Calculus.Deriv.Inv

/-!
# The four-point KZ system on the triangle `0 < x < y < 1`

The KZ connection with poles at `0, x, y, 1` is `d − Ω_x dx − Ω_y dy` with

  `Ω_x = t₁₂/x + t₂₃/(x−y) + t₂₄/(x−1)`,   `Ω_y = t₁₃/y + t₂₃/(y−x) + t₃₄/(y−1)`,

and it is flat iff `[Ω_x, Ω_y] = 0`, which follows from the six infinitesimal pure-braid
relations `Res.Rel` (`comm_Ωx_Ωy`).

The real triangle `Δ = {0 < x < y < 1}` has five boundary divisors, met in cyclic order
`x = 0`, `x = y = 0`, `x = y`, `x = y = 1`, `y = 1`, with residues `t₁₂`, `T₁₂₃`, `t₂₃`, `T₂₃₄`,
`t₃₄`.  For each divisor there is a chart `ψᵢ : (0,1)² → Δ`, `(s, ε) ↦ (x, y)`, in which the
divisor is `ε = 0` and the two adjacent corners are `s = 0` and `s = 1`; in every chart the
pulled-back connection has the same shape (the `Chart` fields, `chart1` … `chart5`):

  `Ω_s = P/s + Q/(s−1) − ε/(1 − ε(1−s)) · B`,   `Ω_ε = E/ε + A/(ε−1) + (1−s)/(1 − ε(1−s)) · B`,

so at `ε = 0` the `s`-equation is the three-point KZ equation with residues `P, Q`, and `E`
commutes with `P` and `Q`.  Consecutive charts agree at the corners
(`KZPentagon.corner12` … `KZPentagon.corner51`).

-- Ref: [drinfeld1990] Leningrad Math. J. 1 (1990) 1419–1457, §2
-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1
-/
namespace QOU.KZ.KZ4
open Set

variable {R : Type*} [NormedRing R]

/-- The five residues of the four-point KZ system with poles at `0, x, y, 1`. -/
structure Res (R : Type*) where
  t12 : R
  t13 : R
  t23 : R
  t24 : R
  t34 : R

namespace Res

variable (t : Res R)

/-- `T₁₂₃ = t₁₂ + t₁₃ + t₂₃`. -/
def T123 : R := t.t12 + t.t13 + t.t23

/-- `T₂₃₄ = t₂₃ + t₂₄ + t₃₄`. -/
def T234 : R := t.t23 + t.t24 + t.t34

/-- The infinitesimal pure-braid relations needed for flatness. -/
structure Rel : Prop where
  r1 : Commute t.t12 t.t34
  r2 : Commute t.t13 t.t24
  r3 : Commute t.t12 (t.t13 + t.t23)
  r4 : Commute t.t23 (t.t12 + t.t13)
  r5 : Commute t.t23 (t.t24 + t.t34)
  r6 : Commute t.t24 (t.t23 + t.t34)

variable {t}

theorem Rel.c1 (h : t.Rel) : Commute t.t12 t.T123 := by
  unfold T123; rw [add_assoc]; exact (Commute.refl _).add_right h.r3

theorem Rel.c2 (h : t.Rel) : Commute t.T123 t.t23 := by
  unfold T123; exact h.r4.symm.add_left (Commute.refl _)

theorem Rel.c3 (h : t.Rel) : Commute t.t23 t.T234 := by
  unfold T234; rw [add_assoc]; exact (Commute.refl _).add_right h.r5

theorem Rel.c4 (h : t.Rel) : Commute t.T234 t.t34 := by
  have h5 := h.r5.eq
  have h6 := h.r6.eq
  simp only [mul_add, add_mul] at h5 h6
  unfold T234 Commute SemiconjBy
  simp only [mul_add, add_mul]
  calc t.t23 * t.t34 + t.t24 * t.t34 + t.t34 * t.t34
      = (t.t23 * t.t24 + t.t23 * t.t34) + (t.t24 * t.t23 + t.t24 * t.t34)
          - t.t23 * t.t24 - t.t24 * t.t23 + t.t34 * t.t34 := by abel
    _ = (t.t24 * t.t23 + t.t34 * t.t23) + (t.t23 * t.t24 + t.t34 * t.t24)
          - t.t23 * t.t24 - t.t24 * t.t23 + t.t34 * t.t34 := by rw [h5, h6]
    _ = _ := by abel

theorem Rel.c5 (h : t.Rel) : Commute t.t34 t.t12 := h.r1.symm

variable [NormedAlgebra ℂ R] (t)

/-- `Ω_x(x, y) = t₁₂/x + t₂₃/(x−y) + t₂₄/(x−1)`. -/
noncomputable def Ωx (p : ℝ × ℝ) : R :=
  (p.1)⁻¹ • t.t12 + (p.1 - p.2)⁻¹ • t.t23 + (p.1 - 1)⁻¹ • t.t24

/-- `Ω_y(x, y) = t₁₃/y + t₂₃/(y−x) + t₃₄/(y−1)`. -/
noncomputable def Ωy (p : ℝ × ℝ) : R :=
  (p.2)⁻¹ • t.t13 + (p.2 - p.1)⁻¹ • t.t23 + (p.2 - 1)⁻¹ • t.t34

end Res

/-- The open triangle `0 < x < y < 1`. -/
def Δ : Set (ℝ × ℝ) := {p | 0 < p.1 ∧ p.1 < p.2 ∧ p.2 < 1}

open Res

variable [NormedAlgebra ℂ R] {t : Res R}

/-- **Flatness**: `[Ω_x, Ω_y] = 0` on the triangle. -/
theorem Res.Rel.comm_Ωx_Ωy (h : t.Rel) {p : ℝ × ℝ} (hp : p ∈ Δ) :
    t.Ωx p * t.Ωy p = t.Ωy p * t.Ωx p := by
  obtain ⟨h0, h01, h1⟩ := hp
  have hx : p.1 ≠ 0 := h0.ne'
  have hy : p.2 ≠ 0 := (h0.trans h01).ne'
  have hxy : p.1 - p.2 ≠ 0 := (sub_neg.mpr h01).ne
  have hyx : p.2 - p.1 ≠ 0 := (sub_pos.mpr h01).ne'
  have hx1 : p.1 - 1 ≠ 0 := (sub_neg.mpr (h01.trans h1)).ne
  have hy1 : p.2 - 1 ≠ 0 := (sub_neg.mpr h1).ne
  have e1 := h.r1.eq
  have e2 := h.r2.eq
  have e3 := h.r3.eq
  have e4 := h.r4.eq
  have e5 := h.r5.eq
  have e6 := h.r6.eq
  simp only [mul_add, add_mul] at e3 e4 e5 e6
  simp only [Ωx, Ωy, mul_add, add_mul, smul_mul_smul_comm]
  set a := (p.1)⁻¹
  set b := (p.1 - p.2)⁻¹
  set c := (p.1 - 1)⁻¹
  set d := (p.2)⁻¹
  set b' := (p.2 - p.1)⁻¹
  set e := (p.2 - 1)⁻¹
  linear_combination (norm := skip) (a * e) • e1 + (-(c * d)) • e2 + (a * d) • e3
    + (b * d) • e4 + (b * e) • e5 + (c * e) • e6
  match_scalars <;> simp only [a, b, c, d, b', e] <;> field_simp <;> ring

theorem isOpen_Δ : IsOpen Δ :=
  (isOpen_lt continuous_const continuous_fst).inter
    ((isOpen_lt continuous_fst continuous_snd).inter (isOpen_lt continuous_snd continuous_const))

theorem combo_lt {a b u u' v v' : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1)
    (hu : u < u') (hv : v < v') : a * u + b * v < a * u' + b * v' := by
  rcases ha.lt_or_eq with ha | rfl
  · nlinarith [mul_lt_mul_of_pos_left hu ha, mul_le_mul_of_nonneg_left hv.le hb]
  · simp at hab; subst hab; simpa using hv

theorem convex_Δ : Convex ℝ Δ := by
  intro p hp q hq a b ha hb hab
  obtain ⟨hp0, hp1, hp2⟩ := hp
  obtain ⟨hq0, hq1, hq2⟩ := hq
  refine ⟨?_, ?_, ?_⟩ <;> simp only [Prod.fst_add, Prod.snd_add, Prod.smul_fst,
    Prod.smul_snd, smul_eq_mul]
  · simpa using combo_lt ha hb hab hp0 hq0
  · exact combo_lt ha hb hab hp1 hq1
  · simpa [hab] using combo_lt ha hb hab hp2 hq2

theorem mem_Δ_center : ((1 / 3 : ℝ), (2 / 3 : ℝ)) ∈ Δ := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

section Smooth

variable (t)

theorem contDiffAt_Ωx {p : ℝ × ℝ} (hp : p ∈ Δ) : ContDiffAt ℝ 1 t.Ωx p := by
  obtain ⟨h0, h01, h1⟩ := hp
  unfold Ωx
  refine ((((contDiffAt_fst.inv h0.ne').smul contDiffAt_const).add
    (((contDiffAt_fst.sub contDiffAt_snd).inv (sub_neg.mpr h01).ne).smul contDiffAt_const)).add
    (((contDiffAt_fst.sub contDiffAt_const).inv (sub_neg.mpr (h01.trans h1)).ne).smul
      contDiffAt_const))

theorem contDiffAt_Ωy {p : ℝ × ℝ} (hp : p ∈ Δ) : ContDiffAt ℝ 1 t.Ωy p := by
  obtain ⟨h0, h01, h1⟩ := hp
  unfold Ωy
  refine ((((contDiffAt_snd.inv (h0.trans h01).ne').smul contDiffAt_const).add
    (((contDiffAt_snd.sub contDiffAt_fst).inv (sub_pos.mpr h01).ne').smul contDiffAt_const)).add
    (((contDiffAt_snd.sub contDiffAt_const).inv (sub_neg.mpr h1).ne).smul contDiffAt_const))

theorem hasFDerivAt_Ωx {p : ℝ × ℝ} (hp : p ∈ Δ) : HasFDerivAt t.Ωx (fderiv ℝ t.Ωx p) p :=
  ((contDiffAt_Ωx t hp).differentiableAt le_rfl).hasFDerivAt

theorem hasFDerivAt_Ωy {p : ℝ × ℝ} (hp : p ∈ Δ) : HasFDerivAt t.Ωy (fderiv ℝ t.Ωy p) p :=
  ((contDiffAt_Ωy t hp).differentiableAt le_rfl).hasFDerivAt

theorem continuousOn_fderiv_Ωx : ContinuousOn (fderiv ℝ t.Ωx) Δ :=
  (ContDiffOn.continuousOn_fderiv_of_isOpen (fun _ hp => (contDiffAt_Ωx t hp).contDiffWithinAt)
    isOpen_Δ le_rfl)

theorem continuousOn_fderiv_Ωy : ContinuousOn (fderiv ℝ t.Ωy) Δ :=
  (ContDiffOn.continuousOn_fderiv_of_isOpen (fun _ hp => (contDiffAt_Ωy t hp).contDiffWithinAt)
    isOpen_Δ le_rfl)

/-- `∂_y Ω_x = t₂₃/(x−y)²`. -/
theorem fderiv_Ωx_snd {p : ℝ × ℝ} (hp : p ∈ Δ) :
    fderiv ℝ t.Ωx p (0, 1) = ((p.1 - p.2) ^ 2)⁻¹ • t.t23 := by
  obtain ⟨h0, h01, h1⟩ := hp
  have hl : HasDerivAt (fun b : ℝ => ((p.1, b) : ℝ × ℝ)) (0, 1) p.2 :=
    (hasDerivAt_const _ _).prodMk (hasDerivAt_id _)
  have h1' := (hasFDerivAt_Ωx t ⟨h0, h01, h1⟩).comp_hasDerivAt p.2 hl
  have hne : p.1 - p.2 ≠ 0 := (sub_neg.mpr h01).ne
  have h2 : HasDerivAt (fun b : ℝ => t.Ωx (p.1, b)) (((p.1 - p.2) ^ 2)⁻¹ • t.t23) p.2 := by
    have := (((hasDerivAt_id p.2).const_sub p.1).inv hne).smul_const t.t23
    have := ((hasDerivAt_const p.2 ((p.1)⁻¹ • t.t12)).add this).add
      (hasDerivAt_const p.2 ((p.1 - 1)⁻¹ • t.t24))
    convert this using 1
    simp [div_eq_mul_inv]
  exact h1'.unique h2

/-- `∂_x Ω_y = t₂₃/(y−x)²`. -/
theorem fderiv_Ωy_fst {p : ℝ × ℝ} (hp : p ∈ Δ) :
    fderiv ℝ t.Ωy p (1, 0) = ((p.2 - p.1) ^ 2)⁻¹ • t.t23 := by
  obtain ⟨h0, h01, h1⟩ := hp
  have hl : HasDerivAt (fun a : ℝ => ((a, p.2) : ℝ × ℝ)) (1, 0) p.1 :=
    (hasDerivAt_id _).prodMk (hasDerivAt_const _ _)
  have h1' := (hasFDerivAt_Ωy t ⟨h0, h01, h1⟩).comp_hasDerivAt p.1 hl
  have hne : p.2 - p.1 ≠ 0 := (sub_pos.mpr h01).ne'
  have h2 : HasDerivAt (fun a : ℝ => t.Ωy (a, p.2)) (((p.2 - p.1) ^ 2)⁻¹ • t.t23) p.1 := by
    have := (((hasDerivAt_id p.1).const_sub p.2).inv hne).smul_const t.t23
    have := ((hasDerivAt_const p.1 ((p.2)⁻¹ • t.t13)).add this).add
      (hasDerivAt_const p.1 ((p.2 - 1)⁻¹ • t.t34))
    convert this using 1
    simp [div_eq_mul_inv]
  exact h1'.unique h2

/-- **Zero curvature** of the four-point KZ connection on the triangle. -/
theorem Res.Rel.curvature (h : t.Rel) {p : ℝ × ℝ} (hp : p ∈ Δ) :
    fderiv ℝ t.Ωy p (1, 0) - fderiv ℝ t.Ωx p (0, 1) = t.Ωx p * t.Ωy p - t.Ωy p * t.Ωx p := by
  rw [fderiv_Ωx_snd t hp, fderiv_Ωy_fst t hp, h.comm_Ωx_Ωy hp, sub_self,
    show (p.2 - p.1) ^ 2 = (p.1 - p.2) ^ 2 by ring, sub_self]

end Smooth

/-! ### Edge charts -/

/-- The common shape of the `s`-component of the connection in an edge chart. -/
noncomputable def Ωs (P Q B : R) (s e : ℂ) : R :=
  s⁻¹ • P + (s - 1)⁻¹ • Q - (e / (1 - e * (1 - s))) • B

/-- The common shape of the `ε`-component of the connection in an edge chart. -/
noncomputable def Ωe (E A B : R) (s e : ℂ) : R :=
  e⁻¹ • E + (e - 1)⁻¹ • A + ((1 - s) / (1 - e * (1 - s))) • B

theorem Ωs_ofReal (P Q B : R) (s e : ℝ) :
    Ωs P Q B s e = s⁻¹ • P + (s - 1)⁻¹ • Q - (e / (1 - e * (1 - s))) • B := by
  simp only [Ωs, ← Complex.coe_smul]; push_cast; rfl

theorem Ωe_ofReal (E A B : R) (s e : ℝ) :
    Ωe E A B s e = e⁻¹ • E + (e - 1)⁻¹ • A + ((1 - s) / (1 - e * (1 - s))) • B := by
  simp only [Ωe, ← Complex.coe_smul]; push_cast; rfl

/-- The open unit square `(0,1)²`, the domain of every edge chart. -/
def sq : Set (ℝ × ℝ) := Ioo 0 1 ×ˢ Ioo 0 1

/-- An edge chart `ψ : (0,1)² → Δ` with its partial derivatives, in which the connection takes
the shape `Ω_s = Ωs P Q B`, `Ω_ε = Ωe E A B`. -/
structure Chart (t : Res R) where
  ψ : ℝ × ℝ → ℝ × ℝ
  ψa : ℝ × ℝ → ℝ × ℝ
  ψb : ℝ × ℝ → ℝ × ℝ
  P : R
  Q : R
  E : R
  A : R
  B : R
  maps : ∀ q ∈ sq, ψ q ∈ Δ
  da : ∀ q ∈ sq, HasDerivAt (fun a => ψ (a, q.2)) (ψa q) q.1
  db : ∀ q ∈ sq, HasDerivAt (fun b => ψ (q.1, b)) (ψb q) q.2
  pa : ∀ q ∈ sq, (ψa q).1 • t.Ωx (ψ q) + (ψa q).2 • t.Ωy (ψ q) = Ωs P Q B q.1 q.2
  pb : ∀ q ∈ sq, (ψb q).1 • t.Ωx (ψ q) + (ψb q).2 • t.Ωy (ψ q) = Ωe E A B q.1 q.2

theorem w_pos {s e : ℝ} (hs : s ∈ Ioo (0 : ℝ) 1) (he : e ∈ Ioo (0 : ℝ) 1) :
    0 < 1 - e * (1 - s) := by
  obtain ⟨hs0, hs1⟩ := hs; obtain ⟨he0, he1⟩ := he; nlinarith

set_option hygiene false in
/-- Closes a scalar chart identity after `match_scalars`, once every inverse sits on one of the
atoms `s, ε, 1 − s, 1 − ε, 1 − ε(1 − s)` whose nonvanishing is in context as `hs he ha hb hw`.
`ring_nf` puts goal and hypotheses in the same normal form, so `field_simp` can find them. -/
macro "chart_scalars" : tactic =>
  `(tactic| first
    | ring1
    | (generalize hwdef : 1 - q.2 * (1 - q.1) = w at hw ⊢
       field_simp <;> (subst hwdef; ring1))
    | (field_simp <;> ring1))

set_option hygiene false in
/-- Proves `x⁻¹ = X` by checking `x * X = 1`. -/
macro "chart_inv" : tactic =>
  `(tactic| (apply inv_eq_of_mul_eq_one_right
             first
             | (generalize hwdef : 1 - q.2 * (1 - q.1) = w at hw ⊢
                field_simp <;> (subst hwdef; ring1))
             | (field_simp <;> ring1)))

variable (t)

/-- `Ω_s` with every inverse on one of the atoms `s, 1 − s, 1 − ε(1 − s)`. -/
theorem Ωs_atoms (P Q B : R) (s e : ℝ) :
    Ωs P Q B s e = s⁻¹ • P + (-(1 - s)⁻¹) • Q + (-(e * (1 - e * (1 - s))⁻¹)) • B := by
  rw [Ωs_ofReal, div_eq_mul_inv, show (s - 1)⁻¹ = -(1 - s)⁻¹ by rw [← inv_neg, neg_sub]]
  module

/-- `Ω_ε` with every inverse on one of the atoms `ε, 1 − ε, 1 − ε(1 − s)`. -/
theorem Ωe_atoms (E A B : R) (s e : ℝ) :
    Ωe E A B s e = e⁻¹ • E + (-(1 - e)⁻¹) • A + ((1 - s) * (1 - e * (1 - s))⁻¹) • B := by
  rw [Ωe_ofReal, div_eq_mul_inv, show (e - 1)⁻¹ = -(1 - e)⁻¹ by rw [← inv_neg, neg_sub]]

/-- Pulling the connection back along a direction `(a, b)` at a point `(x, y)`, with the six
inverses supplied in whatever form is convenient. -/
theorem pull {a b x y X₁ X₂ X₃ Y₁ Y₂ Y₃ : ℝ} (h₁ : x⁻¹ = X₁) (h₂ : (x - y)⁻¹ = X₂)
    (h₃ : (x - 1)⁻¹ = X₃) (h₄ : y⁻¹ = Y₁) (h₅ : (y - x)⁻¹ = Y₂) (h₆ : (y - 1)⁻¹ = Y₃) :
    a • t.Ωx (x, y) + b • t.Ωy (x, y) = (a * X₁) • t.t12 + (b * Y₁) • t.t13 +
      (a * X₂ + b * Y₂) • t.t23 + (a * X₃) • t.t24 + (b * Y₃) • t.t34 := by
  simp only [Res.Ωx, Res.Ωy, h₁, h₂, h₃, h₄, h₅, h₆]
  module

theorem hasDerivAt_w_s (e a : ℝ) : HasDerivAt (fun a => 1 - e * (1 - a)) e a := by
  simpa using (((hasDerivAt_id' a).const_sub 1).const_mul e).const_sub 1

theorem hasDerivAt_w_e (s b : ℝ) : HasDerivAt (fun b => 1 - b * (1 - s)) (-(1 - s)) b := by
  simpa using ((hasDerivAt_id' b).mul_const (1 - s)).const_sub 1

set_option hygiene false in
/-- Closes the strict inequalities placing a chart's image in `Δ`, with `0 < w` in context. -/
macro "chart_ineq" : tactic =>
  `(tactic| first
    | nlinarith [mul_pos hs0 he0, mul_pos (sub_pos.2 hs1) (sub_pos.2 he1), mul_pos (mul_pos he0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 he1)]
    | (apply div_pos <;> nlinarith [mul_pos hs0 he0, mul_pos (sub_pos.2 hs1) (sub_pos.2 he1), mul_pos (mul_pos he0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 he1)])
    | (rw [div_lt_iff₀ hW]; nlinarith [mul_pos hs0 he0, mul_pos (sub_pos.2 hs1) (sub_pos.2 he1), mul_pos (mul_pos he0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 he1)])
    | (rw [lt_div_iff₀ hW]; nlinarith [mul_pos hs0 he0, mul_pos (sub_pos.2 hs1) (sub_pos.2 he1), mul_pos (mul_pos he0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 he1)])
    | (rw [div_lt_div_iff_of_pos_right hW]; nlinarith [mul_pos hs0 he0, mul_pos (sub_pos.2 hs1) (sub_pos.2 he1), mul_pos (mul_pos he0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 (sub_pos.2 he1)) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 hs1), mul_pos (mul_pos hs0 he0) (sub_pos.2 he1)]))

/-- Chart at the divisor `x = 0` (residue `t₁₂`): `(x, y) = (ε(1−s), 1−s)`. -/
noncomputable def chart1 : Chart t where
  ψ q := (q.2 * (1 - q.1), 1 - q.1)
  ψa q := (-q.2, -1)
  ψb q := (1 - q.1, 0)
  P := t.t34
  Q := t.T123
  E := t.t12
  A := t.t23
  B := -t.t24
  maps q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine ⟨?_, ?_, ?_⟩ <;> dsimp only <;> chart_ineq
  da q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := (((hasDerivAt_id' q.1).const_sub 1).const_mul q.2).prodMk ((hasDerivAt_id' q.1).const_sub 1)
    convert this using 1
    all_goals (try ext)
    all_goals (try dsimp only)
    all_goals chart_scalars
  db q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := ((hasDerivAt_id' q.2).mul_const (1 - q.1)).prodMk (hasDerivAt_const q.2 (1 - q.1))
    convert this using 1
    all_goals (try ext)
    all_goals (try dsimp only)
    all_goals chart_scalars
  pa q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := q.2⁻¹ * (1 - q.1)⁻¹) (X₂ := -((1 - q.2)⁻¹ * (1 - q.1)⁻¹))
      (X₃ := -(1 - q.2 * (1 - q.1))⁻¹) (Y₁ := (1 - q.1)⁻¹)
      (Y₂ := (1 - q.2)⁻¹ * (1 - q.1)⁻¹) (Y₃ := -q.1⁻¹)
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωs_atoms]; simp only [T123]
    match_scalars <;> chart_scalars
    all_goals chart_inv
  pb q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := q.2⁻¹ * (1 - q.1)⁻¹) (X₂ := -((1 - q.2)⁻¹ * (1 - q.1)⁻¹))
      (X₃ := -(1 - q.2 * (1 - q.1))⁻¹) (Y₁ := (1 - q.1)⁻¹)
      (Y₂ := (1 - q.2)⁻¹ * (1 - q.1)⁻¹) (Y₃ := -q.1⁻¹)
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωe_atoms]
    match_scalars <;> chart_scalars
    all_goals chart_inv

/-- Chart at the divisor `x = y = 0` (residue `T₁₂₃`): `(x, y) = (sε/w, ε)`. -/
noncomputable def chart2 : Chart t where
  ψ q := (q.1 * q.2 / (1 - q.2 * (1 - q.1)), q.2)
  ψa q := (q.2 * (1 - q.2) / (1 - q.2 * (1 - q.1)) ^ 2, 0)
  ψb q := (q.1 / (1 - q.2 * (1 - q.1)) ^ 2, 1)
  P := t.t12
  Q := t.t23
  E := t.T123
  A := t.T234
  B := t.t12 + t.t23 + t.t24
  maps q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine ⟨?_, ?_, ?_⟩ <;> dsimp only <;> chart_ineq
  da q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := (((hasDerivAt_id' q.1).mul_const q.2).div (hasDerivAt_w_s q.2 q.1) hw).prodMk (hasDerivAt_const q.1 q.2)
    convert this using 1
    all_goals (try ext)
    all_goals (try dsimp only)
    all_goals chart_scalars
  db q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := (((hasDerivAt_id' q.2).const_mul q.1).div (hasDerivAt_w_e q.1 q.2) hw).prodMk ((hasDerivAt_id' q.2))
    convert this using 1
    all_goals (try ext)
    all_goals (try dsimp only)
    all_goals chart_scalars
  pa q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := (1 - q.2 * (1 - q.1)) * q.1⁻¹ * q.2⁻¹) (X₂ := -((1 - q.2 * (1 - q.1)) * q.2⁻¹ * (1 - q.2)⁻¹ * (1 - q.1)⁻¹))
      (X₃ := -((1 - q.2 * (1 - q.1)) * (1 - q.2)⁻¹)) (Y₁ := q.2⁻¹)
      (Y₂ := (1 - q.2 * (1 - q.1)) * q.2⁻¹ * (1 - q.2)⁻¹ * (1 - q.1)⁻¹) (Y₃ := -(1 - q.2)⁻¹)
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωs_atoms]
    match_scalars <;> chart_scalars
    all_goals chart_inv
  pb q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := (1 - q.2 * (1 - q.1)) * q.1⁻¹ * q.2⁻¹) (X₂ := -((1 - q.2 * (1 - q.1)) * q.2⁻¹ * (1 - q.2)⁻¹ * (1 - q.1)⁻¹))
      (X₃ := -((1 - q.2 * (1 - q.1)) * (1 - q.2)⁻¹)) (Y₁ := q.2⁻¹)
      (Y₂ := (1 - q.2 * (1 - q.1)) * q.2⁻¹ * (1 - q.2)⁻¹ * (1 - q.1)⁻¹) (Y₃ := -(1 - q.2)⁻¹)
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωe_atoms]; simp only [T123, T234]
    match_scalars <;> chart_scalars
    all_goals chart_inv

/-- Chart at the divisor `x = y` (residue `t₂₃`): `(x, y) = (s, s/w)`. -/
noncomputable def chart3 : Chart t where
  ψ q := (q.1, q.1 / (1 - q.2 * (1 - q.1)))
  ψa q := (1, (1 - q.2) / (1 - q.2 * (1 - q.1)) ^ 2)
  ψb q := (0, q.1 * (1 - q.1) / (1 - q.2 * (1 - q.1)) ^ 2)
  P := t.T123
  Q := t.T234
  E := t.t23
  A := t.t34
  B := t.t13 + t.t23 + t.t34
  maps q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine ⟨?_, ?_, ?_⟩ <;> dsimp only <;> chart_ineq
  da q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := ((hasDerivAt_id' q.1)).prodMk ((hasDerivAt_id' q.1).div (hasDerivAt_w_s q.2 q.1) hw)
    convert this using 1
    all_goals (try ext)
    all_goals (try dsimp only)
    all_goals chart_scalars
  db q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := (hasDerivAt_const q.2 q.1).prodMk ((hasDerivAt_const q.2 q.1).div (hasDerivAt_w_e q.1 q.2) hw)
    convert this using 1
    all_goals (try ext)
    all_goals (try dsimp only)
    all_goals chart_scalars
  pa q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := q.1⁻¹) (X₂ := -((1 - q.2 * (1 - q.1)) * q.2⁻¹ * q.1⁻¹ * (1 - q.1)⁻¹))
      (X₃ := -(1 - q.1)⁻¹) (Y₁ := (1 - q.2 * (1 - q.1)) * q.1⁻¹)
      (Y₂ := (1 - q.2 * (1 - q.1)) * q.2⁻¹ * q.1⁻¹ * (1 - q.1)⁻¹) (Y₃ := -((1 - q.2 * (1 - q.1)) * (1 - q.2)⁻¹ * (1 - q.1)⁻¹))
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωs_atoms]; simp only [T123, T234]
    match_scalars <;> chart_scalars
    all_goals chart_inv
  pb q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := q.1⁻¹) (X₂ := -((1 - q.2 * (1 - q.1)) * q.2⁻¹ * q.1⁻¹ * (1 - q.1)⁻¹))
      (X₃ := -(1 - q.1)⁻¹) (Y₁ := (1 - q.2 * (1 - q.1)) * q.1⁻¹)
      (Y₂ := (1 - q.2 * (1 - q.1)) * q.2⁻¹ * q.1⁻¹ * (1 - q.1)⁻¹) (Y₃ := -((1 - q.2 * (1 - q.1)) * (1 - q.2)⁻¹ * (1 - q.1)⁻¹))
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωe_atoms]
    match_scalars <;> chart_scalars
    all_goals chart_inv

/-- Chart at the divisor `x = y = 1` (residue `T₂₃₄`): `(x, y) = (1−ε, 1−ε(1−s))`. -/
noncomputable def chart4 : Chart t where
  ψ q := (1 - q.2, 1 - q.2 * (1 - q.1))
  ψa q := (0, q.2)
  ψb q := (-1, -(1 - q.1))
  P := t.t23
  Q := t.t34
  E := t.T234
  A := t.t12
  B := -t.t13
  maps q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine ⟨?_, ?_, ?_⟩ <;> dsimp only <;> chart_ineq
  da q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := (hasDerivAt_const q.1 (1 - q.2)).prodMk ((hasDerivAt_w_s q.2 q.1))
    convert this using 1
  db q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := ((hasDerivAt_id' q.2).const_sub 1).prodMk ((hasDerivAt_w_e q.1 q.2))
    convert this using 1
  pa q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := (1 - q.2)⁻¹) (X₂ := -(q.2⁻¹ * q.1⁻¹))
      (X₃ := -q.2⁻¹) (Y₁ := (1 - q.2 * (1 - q.1))⁻¹)
      (Y₂ := q.2⁻¹ * q.1⁻¹) (Y₃ := -(q.2⁻¹ * (1 - q.1)⁻¹))
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωs_atoms]
    match_scalars <;> chart_scalars
    all_goals chart_inv
  pb q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := (1 - q.2)⁻¹) (X₂ := -(q.2⁻¹ * q.1⁻¹))
      (X₃ := -q.2⁻¹) (Y₁ := (1 - q.2 * (1 - q.1))⁻¹)
      (Y₂ := q.2⁻¹ * q.1⁻¹) (Y₃ := -(q.2⁻¹ * (1 - q.1)⁻¹))
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωe_atoms]; simp only [T234]
    match_scalars <;> chart_scalars
    all_goals chart_inv

/-- Chart at the divisor `y = 1` (residue `t₃₄`): `(x, y) = ((1−s)(1−ε)/w, (1−ε)/w)`. -/
noncomputable def chart5 : Chart t where
  ψ q := ((1 - q.1) * (1 - q.2) / (1 - q.2 * (1 - q.1)), (1 - q.2) / (1 - q.2 * (1 - q.1)))
  ψa q := (-(1 - q.2) / (1 - q.2 * (1 - q.1)) ^ 2, -(q.2 * (1 - q.2)) / (1 - q.2 * (1 - q.1)) ^ 2)
  ψb q := (-(q.1 * (1 - q.1)) / (1 - q.2 * (1 - q.1)) ^ 2, -q.1 / (1 - q.2 * (1 - q.1)) ^ 2)
  P := t.T234
  Q := t.t12
  E := t.t34
  A := t.T123
  B := t.t12 + t.t13 + t.t23 + t.t24 + t.t34
  maps q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine ⟨?_, ?_, ?_⟩ <;> dsimp only <;> chart_ineq
  da q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := ((((hasDerivAt_id' q.1).const_sub 1).mul_const (1 - q.2)).div (hasDerivAt_w_s q.2 q.1) hw).prodMk ((hasDerivAt_const q.1 (1 - q.2)).div (hasDerivAt_w_s q.2 q.1) hw)
    convert this using 1
    all_goals (try ext)
    all_goals (try dsimp only)
    all_goals chart_scalars
  db q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    have := ((((hasDerivAt_id' q.2).const_sub 1).const_mul (1 - q.1)).div (hasDerivAt_w_e q.1 q.2) hw).prodMk (((hasDerivAt_id' q.2).const_sub 1).div (hasDerivAt_w_e q.1 q.2) hw)
    convert this using 1
    all_goals (try ext)
    all_goals (try dsimp only)
    all_goals chart_scalars
  pa q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := (1 - q.2 * (1 - q.1)) * (1 - q.1)⁻¹ * (1 - q.2)⁻¹) (X₂ := -((1 - q.2 * (1 - q.1)) * q.1⁻¹ * (1 - q.2)⁻¹))
      (X₃ := -((1 - q.2 * (1 - q.1)) * q.1⁻¹)) (Y₁ := (1 - q.2 * (1 - q.1)) * (1 - q.2)⁻¹)
      (Y₂ := (1 - q.2 * (1 - q.1)) * q.1⁻¹ * (1 - q.2)⁻¹) (Y₃ := -((1 - q.2 * (1 - q.1)) * q.2⁻¹ * q.1⁻¹))
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωs_atoms]; simp only [T234]
    match_scalars <;> chart_scalars
    all_goals chart_inv
  pb q hq := by
    obtain ⟨⟨hs0, hs1⟩, he0, he1⟩ := hq
    have hW : 0 < 1 - q.2 * (1 - q.1) := w_pos ⟨hs0, hs1⟩ ⟨he0, he1⟩
    have hs : q.1 ≠ 0 := hs0.ne'
    have he : q.2 ≠ 0 := he0.ne'
    have ha : 1 - q.1 ≠ 0 := by linarith
    have hb : 1 - q.2 ≠ 0 := by linarith
    have hw : 1 - q.2 * (1 - q.1) ≠ 0 := hW.ne'
    refine (pull t (X₁ := (1 - q.2 * (1 - q.1)) * (1 - q.1)⁻¹ * (1 - q.2)⁻¹) (X₂ := -((1 - q.2 * (1 - q.1)) * q.1⁻¹ * (1 - q.2)⁻¹))
      (X₃ := -((1 - q.2 * (1 - q.1)) * q.1⁻¹)) (Y₁ := (1 - q.2 * (1 - q.1)) * (1 - q.2)⁻¹)
      (Y₂ := (1 - q.2 * (1 - q.1)) * q.1⁻¹ * (1 - q.2)⁻¹) (Y₃ := -((1 - q.2 * (1 - q.1)) * q.2⁻¹ * q.1⁻¹))
      ?_ ?_ ?_ ?_ ?_ ?_).trans ?_
    rotate_left 6
    rw [Ωe_atoms]; simp only [T123]
    match_scalars <;> chart_scalars
    all_goals chart_inv

