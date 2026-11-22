import Mathlib.Tactic
import QOU.Mathlib.RamifiedShiftCalculusSum
import QOU.Mass.QDifferenceConfluentObstruction

/-!
# QOU.Mass.C1KernelAsShiftSum — the C1 kernel is not a derivative-only operator

`conj:qdifference-kernel-prolongation-symbol` asks that the binding kernel

  `L_K = (q²x − 1)σ² − (q − 1)σ − (q − 1)`,   `x = q^m`, `σ : x ↦ qx`,

be the symbol of the jet-prolongation operator `D_q` at a ramified pole of the colour
curve. The ramified shift calculus (`#6474`, `#6498`, `#6523`) narrowed the admissible
`D_q` from the *target properties* (residue, `(−1)^n` residual) and left one class alive
at the low body orders: a **derivative-only** mixed-shift operator — every term
annihilates constants — such as Jackson `[e+1]_q σ` + q-`d/dz` `[e+2]_q σ²`.

This module reads the kernel itself in the same calculus and asks whether such an
operator can have it as its symbol. **It cannot, in either natural dictionary.**

* Dictionary (a): `σ` = the unit `t`-shift, `x = q^e`. Then
  `L_K = shiftOp 2 (q^{e+2} − 1) − (q−1)·shiftOp 1 (1) − (q−1)·id` (`c1KernelOp`).
  The shift-2 term is derivative-like (`q^0 − 1 = 0`); the shift-1 term has the
  **constant** multiplier `−(q−1)`, which does not vanish at `e = −1`; and there is a
  zeroth-order term.
* Dictionary (b): the ramified double cover, `x^{1/2} = u^e`, `q = u²`, `σ` = the
  `t`-shift by 2 (`c1KernelOpCover`). All shifts are even; the zeroth-order term is
  `−(u² − 1)`.

The invariant is one line: a derivative-only sum **kills the constant seed**
(`sumOp_derivativeOnly_const`), and the kernel does not — its zeroth-order term
evaluates the constant seed to `−(q − 1) ≠ 0` in every dictionary
(`c1KernelOp_const_ne_zero`, `c1KernelOpCover_const_ne_zero`). Hence
`derivativeOnly_ne_c1KernelOp` / `derivativeOnly_ne_c1KernelOpCover`: **no
derivative-only shift-sum is the kernel.** If the conjecture holds, `D_q` has a
non-derivative component — the `#6474` clause reached by a third route, from the
kernel's own shape rather than from the residue or the residual.

The kernel is, on the other hand, exactly in the `#6474` admissible class under (a):
odd shift with a non-vanishing multiplier at `−1`
(`c1Kernel_shiftOne_not_annihilatesConstants`), and its residue on a power-series seed
is dead at level 1 and alive at level 2, reading the branch value and the leading
square-root coefficient: `L_K² f (−2) = (q − 1)² (f 0 − f 1)` (`c1KernelOp_residue_two`).
Under (b) the residue is alive already at level 1, `−(u² − 1) f 0`, and the operator
commutes with the covering monodromy (`c1KernelOpCover_comm_mono`), so it carries no
odd component at all.

Nothing here identifies `D_q` with `L_K`. It says what `D_q` would have to be if the
identification held.

## References

- [leitner2026] mass-theory/qdifference-kernel-prolongation-symbol
- [leitner2026] docs/audits/2026-09-04-derivative-only-dq-vs-c1-kernel.md

LaTeX label: (library module — no content block)
-/

namespace QOU.Mass.C1KernelAsShiftSum

open QOU.Brings.RamificationParityMonodromy QOU.Mathlib.RamifiedShiftCalculus
  QOU.Mathlib.RamifiedShiftCalculusSum Finset

variable {R : Type*} [CommRing R]

/-- A finite shift-sum is **derivative-only** when every term annihilates constants. -/
def DerivativeOnly (ks : Finset ℤ) (c : ℤ → ℤ → R) : Prop :=
  ∀ k ∈ ks, AnnihilatesConstants k (c k)

/-- A derivative-only sum kills the constant seed `t⁰`. -/
theorem sumOp_derivativeOnly_const (ks : Finset ℤ) (c : ℤ → ℤ → R)
    (h : DerivativeOnly ks c) : sumOp ks c (monomialCoeff 0) = 0 := by
  funext e
  simp only [sumOp_apply, Pi.zero_apply]
  apply sum_eq_zero
  intro k hk
  by_cases he : e + k = 0
  · have he' : e = -k := by omega
    subst he'
    have hc : c k (-k) = 0 := h k hk
    simp [monomialCoeff, hc]
  · simp [monomialCoeff, he]

section Field
variable {K : Type*} [Field K]

/-! ## Dictionary (a): `σ` = unit `t`-shift, `x = q^e` -/

/-- `L_K = (q²x − 1)σ² − (q − 1)σ − (q − 1)` on the coefficient model, `x = q^e`. -/
def c1KernelOp (q : K) (f : ℤ → K) : ℤ → K :=
  shiftOp 2 (fun e => q ^ (e + 2) - 1) f + shiftOp 1 (fun _ => -(q - 1)) f
    + shiftOp 0 (fun _ => -(q - 1)) f

theorem c1KernelOp_apply (q : K) (f : ℤ → K) (e : ℤ) :
    c1KernelOp q f e = (q ^ (e + 2) - 1) * f (e + 2) - (q - 1) * f (e + 1) - (q - 1) * f e := by
  simp [c1KernelOp, shiftOp]; ring

/-- On the body-order index it is the corpus's recurrence
`[m+2]_q b_{m+2} = b_{m+1} + b_m` in the geometric q-integer `qint` of
`qlift_normalized_kernel_exists`, up to the overall factor `q − 1`. -/
theorem c1KernelOp_eq_recurrence (q : K) (f : ℤ → K) (m : ℕ) :
    c1KernelOp q f m
      = (q - 1) * (QOU.Mass.QDifferenceConfluentObstruction.qint q (m + 2) * f (m + 2)
          - f (m + 1) - f m) := by
  rw [c1KernelOp_apply]
  have hgeom : q ^ ((m : ℤ) + 2) - 1
      = (q - 1) * QOU.Mass.QDifferenceConfluentObstruction.qint q (m + 2) := by
    have h := geom_sum_mul q (m + 2)
    unfold QOU.Mass.QDifferenceConfluentObstruction.qint
    rw [mul_comm] at h
    rw [show ((m : ℤ) + 2) = ((m + 2 : ℕ) : ℤ) by push_cast; ring, zpow_natCast]
    exact h.symm
  rw [hgeom]
  ring

/-- The shift-2 term is derivative-like: `q^0 − 1 = 0`. -/
theorem c1Kernel_shiftTwo_annihilatesConstants (q : K) :
    AnnihilatesConstants 2 (fun e : ℤ => q ^ (e + 2) - 1) := by
  show q ^ ((-2 : ℤ) + 2) - 1 = 0
  norm_num

/-- The shift-1 term is **not**: its multiplier is the constant `−(q − 1)`. -/
theorem c1Kernel_shiftOne_not_annihilatesConstants (q : K) (hq : q ≠ 1) :
    ¬ AnnihilatesConstants 1 (fun _ : ℤ => (-(q - 1) : K)) := by
  intro h
  have h' : -(q - 1) = (0 : K) := h
  exact hq (sub_eq_zero.mp (neg_eq_zero.mp h'))

/-- The kernel does not kill the constant seed: its value at `e = 0` is `−(q − 1)`. -/
theorem c1KernelOp_const_ne_zero (q : K) (hq : q ≠ 1) :
    c1KernelOp q (monomialCoeff 0) ≠ 0 := by
  intro h
  have h0 := congrFun h 0
  simp [c1KernelOp_apply, monomialCoeff] at h0
  exact hq (sub_eq_zero.mp h0).symm

/-- **No derivative-only shift-sum is the C1 kernel** (dictionary (a)). -/
theorem derivativeOnly_ne_c1KernelOp (q : K) (hq : q ≠ 1) (ks : Finset ℤ)
    (c : ℤ → ℤ → K) (h : DerivativeOnly ks c) : sumOp ks c ≠ c1KernelOp q := by
  intro heq
  apply c1KernelOp_const_ne_zero q hq
  rw [← heq]
  exact sumOp_derivativeOnly_const ks c h

/-- Level 1: the kernel's residue slot is dead on a power-series seed. -/
theorem c1KernelOp_residue_one (q : K) (f : ℤ → K) (hf : PowerSeriesSupported f) :
    c1KernelOp q f (-2) = 0 := by
  rw [c1KernelOp_apply]
  have h1 := hf (-1) (by norm_num)
  have h2 := hf (-2) (by norm_num)
  norm_num [h1, h2]

/-- Level 2: the kernel's residue reads the branch value and the leading square-root
coefficient, `(q − 1)² (f 0 − f 1)`. -/
theorem c1KernelOp_residue_two (q : K) (f : ℤ → K) (hf : PowerSeriesSupported f) :
    c1KernelOp q (c1KernelOp q f) (-2) = (q - 1) ^ 2 * (f 0 - f 1) := by
  simp only [c1KernelOp_apply]
  have h1 := hf (-1) (by norm_num)
  have h2 := hf (-2) (by norm_num)
  norm_num [h1, h2]
  ring

/-! ## Dictionary (b): the ramified double cover, `x^{1/2} = u^e`, `q = u²`, `σ` = shift 2 -/

/-- `L_K` on the double cover: `q²x − 1 = u^{2e+4} − 1`, `σ` the `t`-shift by 2. -/
def c1KernelOpCover (u : K) (f : ℤ → K) : ℤ → K :=
  shiftOp 4 (fun e => u ^ (2 * e + 4) - 1) f + shiftOp 2 (fun _ => -(u ^ 2 - 1)) f
    + shiftOp 0 (fun _ => -(u ^ 2 - 1)) f

theorem c1KernelOpCover_apply (u : K) (f : ℤ → K) (e : ℤ) :
    c1KernelOpCover u f e
      = (u ^ (2 * e + 4) - 1) * f (e + 4) - (u ^ 2 - 1) * f (e + 2) - (u ^ 2 - 1) * f e := by
  simp [c1KernelOpCover, shiftOp]; ring

theorem c1KernelOpCover_const_ne_zero (u : K) (hu : u ^ 2 ≠ 1) :
    c1KernelOpCover u (monomialCoeff 0) ≠ 0 := by
  intro h
  have h0 := congrFun h 0
  simp [c1KernelOpCover_apply, monomialCoeff] at h0
  exact hu (sub_eq_zero.mp h0).symm

/-- **No derivative-only shift-sum is the C1 kernel** (dictionary (b)). -/
theorem derivativeOnly_ne_c1KernelOpCover (u : K) (hu : u ^ 2 ≠ 1) (ks : Finset ℤ)
    (c : ℤ → ℤ → K) (h : DerivativeOnly ks c) : sumOp ks c ≠ c1KernelOpCover u := by
  intro heq
  apply c1KernelOpCover_const_ne_zero u hu
  rw [← heq]
  exact sumOp_derivativeOnly_const ks c h

/-- Under the cover dictionary every shift is even, so the kernel commutes with the
covering monodromy: it has no odd component. -/
theorem c1KernelOpCover_comm_mono (u : K) (f : ℤ → K) :
    c1KernelOpCover u (mono f) = mono (c1KernelOpCover u f) := by
  unfold c1KernelOpCover
  rw [mono_add, mono_add,
    shiftOp_comm_mono_of_even 4 ⟨2, by norm_num⟩,
    shiftOp_comm_mono_of_even 2 even_two,
    shiftOp_comm_mono_of_even 0 ⟨0, by norm_num⟩]

/-- Under the cover dictionary the residue is alive already at level 1, from the branch
value: `−(u² − 1) f 0`. -/
theorem c1KernelOpCover_residue_one (u : K) (f : ℤ → K) (hf : PowerSeriesSupported f) :
    c1KernelOpCover u f (-2) = -(u ^ 2 - 1) * f 0 := by
  rw [c1KernelOpCover_apply]
  have h2 := hf (-2) (by norm_num)
  norm_num [h2]
  ring

end Field

end QOU.Mass.C1KernelAsShiftSum
