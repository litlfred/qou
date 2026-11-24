import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Data.Fin.Basic

/-!
# Jimbo's `gl₃` braiding and the colour singlet (working assumption, issue #9106)

`HopfColourTensorBraid` takes two facts about Jimbo's braiding on colour `V = K³` as cited
inputs. This file proves both, concretely, over any field `K` and any `q ≠ 0` (so in particular
over `ℚ(q)`, i.e. at generic `q`), with no numerical input.

**Conventions** (the ones `computations/probes/hopf_colour_singlet/singlet_eigen_probe.py` uses).
Tensors in `V^{⊗2}` and `V^{⊗3}` are functions on index tuples. Jimbo's braiding is
`Ř(e_x ⊗ e_x) = q·e_x ⊗ e_x`, and for `x ≠ y`, `Ř(e_x ⊗ e_y) = e_y ⊗ e_x + [x > y](q − q⁻¹)·e_x ⊗ e_y`.
`U_q(gl₃)` acts on `V` by `E_i = e_{i,i+1}`, `F_i = e_{i+1,i}`, `K_i = q^{e_{ii} − e_{i+1,i+1}}`,
`L_j = q^{e_{jj}}`, with coproduct `Δ E = E ⊗ K + 1 ⊗ E`, `Δ F = F ⊗ 1 + K⁻¹ ⊗ F`,
`Δ L = L ⊗ L` (iterated coassociatively on `V^{⊗3}`).

**Proved here.**
* `hecke`: `(Ř − q)(Ř + q⁻¹) = 0` on `V ⊗ V`.
* `braid`: `Ř₁₂ Ř₂₃ Ř₁₂ = Ř₂₃ Ř₁₂ Ř₂₃` on `V^{⊗3}`.
* `comm_E`, `comm_F`, `comm_L`: `Ř` commutes with `Δ E_i`, `Δ F_i`, `Δ L_j` on `V ⊗ V`.
  This is the "colour action commutes with `Ř_c`" input, for the generators.
* `R12_eps`, `R23_eps`: both braid generators act on the `q`-antisymmetric vector `ε_q` by `−q⁻¹`.
  This is the "`Ř` acts on `ε` by `−q⁻¹`" input.
* `E_eps`, `F_eps`, `L_eps`: `Δ²E_i ε_q = 0`, `Δ²F_i ε_q = 0`, `Δ²L_j ε_q = q·ε_q`. So the line
  `K·ε_q` is a `U_q(gl₃)`-submodule (the `q`-determinant), and on it `U_q(sl₃)` acts trivially.
* `singlet_unique`: if `q² + 1 ≠ 0` and `q⁴ + q² + 1 ≠ 0`, every `w` with `Ř₁₂ w = −q⁻¹ w` and
  `Ř₂₃ w = −q⁻¹ w` is a multiple of `ε_q`. So the colour singlet is one-dimensional.

What is **not** claimed: anything about flavour, masses or measurement. Those enter downstream
of `HopfColourTensorBraid`, never here.
-/

namespace QOU.Braiding.JimboGl3Singlet

variable {K : Type*} [Field K]

/-- Two-fold tensors on `K³`. -/
abbrev T2 (K : Type*) := Fin 3 → Fin 3 → K
/-- Three-fold tensors on `K³`. -/
abbrev T3 (K : Type*) := Fin 3 → Fin 3 → Fin 3 → K

/-- Jimbo's braiding on `V ⊗ V`, component form: `(Ř v)(a, b)`. -/
def R (q : K) (v : T2 K) : T2 K := fun a b =>
  if a = b then q * v a a else v b a + (if b < a then (q - q⁻¹) * v a b else 0)

/-- `Ř` on the first two factors of `V^{⊗3}`. -/
def R12 (q : K) (w : T3 K) : T3 K := fun a b c => R q (fun x y => w x y c) a b

/-- `Ř` on the last two factors of `V^{⊗3}`. -/
def R23 (q : K) (w : T3 K) : T3 K := fun a b c => R q (fun x y => w a x y) b c

/-- Diagonal of `K_i = q^{e_{ii} − e_{i+1,i+1}}` (here `i : Fin 2`). -/
def kd (q : K) (i : Fin 2) (x : Fin 3) : K :=
  if x = i.castSucc then q else if x = i.succ then q⁻¹ else 1

/-- Diagonal of `L_j = q^{e_{jj}}`. -/
def ld (q : K) (j x : Fin 3) : K := if x = j then q else 1

/-- `E_i = e_{i,i+1}` on `V`: `(E u) a = [a = i] u (i+1)`. -/
def E1 (i : Fin 2) (u : Fin 3 → K) : Fin 3 → K := fun a => if a = i.castSucc then u i.succ else 0

/-- `F_i = e_{i+1,i}` on `V`. -/
def F1 (i : Fin 2) (u : Fin 3 → K) : Fin 3 → K := fun a => if a = i.succ then u i.castSucc else 0

/-- `Δ E_i = E_i ⊗ K_i + 1 ⊗ E_i` on `V ⊗ V`. -/
def DE (q : K) (i : Fin 2) (v : T2 K) : T2 K := fun a b =>
  (if a = i.castSucc then kd q i b * v i.succ b else 0) + (if b = i.castSucc then v a i.succ else 0)

/-- `Δ F_i = F_i ⊗ 1 + K_i⁻¹ ⊗ F_i` on `V ⊗ V`. -/
def DF (q : K) (i : Fin 2) (v : T2 K) : T2 K := fun a b =>
  (if a = i.succ then v i.castSucc b else 0) + (if b = i.succ then (kd q i a)⁻¹ * v a i.castSucc else 0)

/-- `Δ L_j = L_j ⊗ L_j` on `V ⊗ V`. -/
def DL (q : K) (j : Fin 3) (v : T2 K) : T2 K := fun a b => ld q j a * ld q j b * v a b

/-- `Δ² E_i = E_i ⊗ K_i ⊗ K_i + 1 ⊗ E_i ⊗ K_i + 1 ⊗ 1 ⊗ E_i` on `V^{⊗3}`. -/
def DE3 (q : K) (i : Fin 2) (w : T3 K) : T3 K := fun a b c =>
  (if a = i.castSucc then kd q i b * kd q i c * w i.succ b c else 0)
  + (if b = i.castSucc then kd q i c * w a i.succ c else 0)
  + (if c = i.castSucc then w a b i.succ else 0)

/-- `Δ² F_i = F_i ⊗ 1 ⊗ 1 + K_i⁻¹ ⊗ F_i ⊗ 1 + K_i⁻¹ ⊗ K_i⁻¹ ⊗ F_i` on `V^{⊗3}`. -/
def DF3 (q : K) (i : Fin 2) (w : T3 K) : T3 K := fun a b c =>
  (if a = i.succ then w i.castSucc b c else 0)
  + (if b = i.succ then (kd q i a)⁻¹ * w a i.castSucc c else 0)
  + (if c = i.succ then (kd q i a)⁻¹ * (kd q i b)⁻¹ * w a b i.castSucc else 0)

/-- `Δ² L_j = L_j ⊗ L_j ⊗ L_j` on `V^{⊗3}`. -/
def DL3 (q : K) (j : Fin 3) (w : T3 K) : T3 K := fun a b c =>
  ld q j a * ld q j b * ld q j c * w a b c

/-- The `q`-antisymmetric colour vector
`ε_q = e₁₂₃ − q⁻¹e₁₃₂ − q⁻¹e₂₁₃ + q⁻²e₂₃₁ + q⁻²e₃₁₂ − q⁻³e₃₂₁` (0-indexed below). -/
def eps (q : K) : T3 K := fun a b c =>
  if a = 0 ∧ b = 1 ∧ c = 2 then 1
  else if a = 0 ∧ b = 2 ∧ c = 1 then -q⁻¹
  else if a = 1 ∧ b = 0 ∧ c = 2 then -q⁻¹
  else if a = 1 ∧ b = 2 ∧ c = 0 then q⁻¹ ^ 2
  else if a = 2 ∧ b = 0 ∧ c = 1 then q⁻¹ ^ 2
  else if a = 2 ∧ b = 1 ∧ c = 0 then -q⁻¹ ^ 3
  else 0

/-- **Hecke relation** for Jimbo's `Ř` on `V ⊗ V`: `Ř² = (q − q⁻¹)Ř + 1`. -/
theorem hecke (q : K) (hq : q ≠ 0) (v : T2 K) :
    R q (R q v) = fun a b => (q - q⁻¹) * R q v a b + v a b := by
  funext a b
  fin_cases a <;> fin_cases b <;> simp [R] <;> field_simp <;> ring

/-- **Braid relation** for Jimbo's `Ř` on `V^{⊗3}`. -/
theorem braid (q : K) (hq : q ≠ 0) (w : T3 K) :
    R12 q (R23 q (R12 q w)) = R23 q (R12 q (R23 q w)) := by
  funext a b c
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [R12, R23, R] <;> field_simp <;> ring

/-- `Ř` commutes with `Δ E_i` on `V ⊗ V`. -/
theorem comm_E (q : K) (hq : q ≠ 0) (i : Fin 2) (v : T2 K) :
    R q (DE q i v) = DE q i (R q v) := by
  funext a b
  fin_cases i <;> fin_cases a <;> fin_cases b <;> simp [R, DE, kd] <;> field_simp <;> ring

/-- `Ř` commutes with `Δ F_i` on `V ⊗ V`. -/
theorem comm_F (q : K) (hq : q ≠ 0) (i : Fin 2) (v : T2 K) :
    R q (DF q i v) = DF q i (R q v) := by
  funext a b
  fin_cases i <;> fin_cases a <;> fin_cases b <;> simp [R, DF, kd] <;> field_simp <;> ring

/-- `Ř` commutes with `Δ L_j` on `V ⊗ V`. -/
theorem comm_L (q : K) (j : Fin 3) (v : T2 K) : R q (DL q j v) = DL q j (R q v) := by
  funext a b
  fin_cases j <;> fin_cases a <;> fin_cases b <;> simp [R, DL, ld] <;> ring

/-- **`Ř₁₂` acts on `ε_q` by `−q⁻¹`.** -/
theorem R12_eps (q : K) (hq : q ≠ 0) : R12 q (eps q) = fun a b c => -q⁻¹ * eps q a b c := by
  funext a b c
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [R12, R, eps] <;> field_simp <;> ring

/-- **`Ř₂₃` acts on `ε_q` by `−q⁻¹`.** -/
theorem R23_eps (q : K) (hq : q ≠ 0) : R23 q (eps q) = fun a b c => -q⁻¹ * eps q a b c := by
  funext a b c
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [R23, R, eps] <;> field_simp <;> ring

/-- `Δ² E_i ε_q = 0`. -/
theorem E_eps (q : K) (hq : q ≠ 0) (i : Fin 2) : DE3 q i (eps q) = 0 := by
  funext a b c
  fin_cases i <;> fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [DE3, kd, eps] <;>
    field_simp <;> ring

/-- `Δ² F_i ε_q = 0`. -/
theorem F_eps (q : K) (hq : q ≠ 0) (i : Fin 2) : DF3 q i (eps q) = 0 := by
  funext a b c
  fin_cases i <;> fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [DF3, kd, eps] <;>
    field_simp <;> ring

/-- `Δ² L_j ε_q = q·ε_q`: `ε_q` has weight `(1,1,1)`, the `q`-determinant. -/
theorem L_eps (q : K) (j : Fin 3) : DL3 q j (eps q) = fun a b c => q * eps q a b c := by
  funext a b c
  fin_cases j <;> fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [DL3, ld, eps]

/-- **The colour singlet is one-dimensional.** If `q ≠ 0` and `q² + 1 ≠ 0`, every
`w ∈ V^{⊗3}` on which both braid generators act by `−q⁻¹` is `w(e₁₂₃)·ε_q`. -/
theorem singlet_unique (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (w : T3 K)
    (H12 : R12 q w = fun a b c => -q⁻¹ * w a b c)
    (H23 : R23 q w = fun a b c => -q⁻¹ * w a b c) :
    w = fun a b c => w 0 1 2 * eps q a b c := by
  have e12 : ∀ a b c, R12 q w a b c = -q⁻¹ * w a b c := fun a b c => by rw [H12]
  have e23 : ∀ a b c, R23 q w a b c = -q⁻¹ * w a b c := fun a b c => by rw [H23]
  have hqq : q + q⁻¹ ≠ 0 := by
    intro h; apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  have z12 : ∀ a c, w a a c = 0 := by
    intro a c
    have h := e12 a a c
    simp only [R12, R, if_true] at h
    have h' : (q + q⁻¹) * w a a c = 0 := by linear_combination h
    exact (mul_eq_zero.mp h').resolve_left hqq
  have z23 : ∀ a b, w a b b = 0 := by
    intro a b
    have h := e23 a b b
    simp only [R23, R, if_true] at h
    have h' : (q + q⁻¹) * w a b b = 0 := by linear_combination h
    exact (mul_eq_zero.mp h').resolve_left hqq
  have z010 : w 0 1 0 = 0 := by
    have h := e12 0 1 0; simp [R12, R, z23] at h
    exact h.resolve_left hq
  have z020 : w 0 2 0 = 0 := by
    have h := e12 0 2 0; simp [R12, R, z23] at h
    exact h.resolve_left hq
  have z121 : w 1 2 1 = 0 := by
    have h := e12 1 2 1; simp [R12, R, z23] at h
    exact h.resolve_left hq
  have z101 : w 1 0 1 = 0 := by
    have h := e12 1 0 1; simp [R12, R, z23] at h
    have h' : q * w 1 0 1 = 0 := by linear_combination h
    simpa [hq] using h'
  have z202 : w 2 0 2 = 0 := by
    have h := e12 2 0 2; simp [R12, R, z23] at h
    have h' : q * w 2 0 2 = 0 := by linear_combination h
    simpa [hq] using h'
  have z212 : w 2 1 2 = 0 := by
    have h := e12 2 1 2; simp [R12, R, z23] at h
    have h' : q * w 2 1 2 = 0 := by linear_combination h
    simpa [hq] using h'
  have p102 : w 1 0 2 = -q⁻¹ * w 0 1 2 := by
    have h := e12 1 0 2; simp [R12, R] at h
    apply mul_left_cancel₀ hq
    rw [show q * w 1 0 2 = -w 0 1 2 by linear_combination h]
    field_simp
  have p021 : w 0 2 1 = -q⁻¹ * w 0 1 2 := by
    have h := e23 0 2 1; simp [R23, R] at h
    apply mul_left_cancel₀ hq
    rw [show q * w 0 2 1 = -w 0 1 2 by linear_combination h]
    field_simp
  have p120 : w 1 2 0 = q⁻¹ ^ 2 * w 0 1 2 := by
    have h := e23 1 2 0; simp [R23, R] at h
    apply mul_left_cancel₀ hq
    rw [show q * w 1 2 0 = -w 1 0 2 by linear_combination h, p102]
    field_simp
  have p201 : w 2 0 1 = q⁻¹ ^ 2 * w 0 1 2 := by
    have h := e12 2 0 1; simp [R12, R] at h
    apply mul_left_cancel₀ hq
    rw [show q * w 2 0 1 = -w 0 2 1 by linear_combination h, p021]
    field_simp
  have p210 : w 2 1 0 = -q⁻¹ ^ 3 * w 0 1 2 := by
    have h := e12 2 1 0; simp [R12, R] at h
    apply mul_left_cancel₀ hq
    rw [show q * w 2 1 0 = -w 1 2 0 by linear_combination h, p120]
    field_simp
  funext a b c
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [eps, z12, z23, z010, z020, z121, z101, z202, z212,
    p102, p021, p120, p201, p210] <;> ring

end QOU.Braiding.JimboGl3Singlet
