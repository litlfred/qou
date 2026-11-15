import Mathlib.Tactic
import QOU.Mathlib.RamifiedShiftCalculusSum
import QOU.Mass.C1KernelAsShiftSum

/-!
# QOU.Mass.C1KernelDictionaryParity — the C1 kernel cannot carry the Door-v residual

`C1KernelAsShiftSum` (#6582) read the binding kernel

  `L_K = (q²x − 1)σ² − (q − 1)σ − (q − 1)`

in the ramified shift calculus under the two natural `σ ↔ t`-shift dictionaries and
found that they **disagree on parity**: under (a) (`σ` = unit `t`-shift) the kernel has
an odd component, under (b) (`σ` = `t`-shift 2 on the double cover) it commutes with the
covering monodromy `t ↦ −t`. The question this module answers is whether the Door-v
`(−1)^m` residual — the target property `#6474` demanded of the prolongation operator's
tower — decides between them.

**It does not decide; it kills both.** A tower whose level-`n` jet carries the monodromy
character `(−1)^n ε` from some level `n₀` on is **zero** from that level on, in either
dictionary:

* **(b), by monodromy commutation.** A monodromy-commuting homogeneous operator `T`
  transports the character of level `n` to level `n + 1` unchanged, so alternation at two
  consecutive levels forces `2 · (−1)^n ε · Tⁿ⁺¹X = 0`, hence `Tⁿ⁺¹X = 0`
  (`comm_mono_flip_kills`, no seed hypothesis). Applied to `c1KernelOpCover`:
  `c1KernelOpCover_residual_kills_tower`.
* **(a), by the `e`-dependence of the shift-2 weight.** `#6498`'s
  `residual_from_level_tower_is_odd_part` forces the even part `E` to kill both the
  level-`n₀` jet `Y` and `O Y`. Written out, `E Y = 0` is
  `(q^{e+2} − 1) Y(e+2) = (q − 1) Y(e)` and `E (O Y) = 0` is the *same* recurrence with
  `q^{e+1}` in place of `q^{e+2}`. Their difference is `q^{e+1}(q − 1) Y(e+2) = 0`, so
  `Y = 0` for `q ≠ 0, 1` (`c1E_zero_c1E_O_zero_imp`), and the tower is zero from `n₀`
  on (`c1KernelOp_residual_kills_tower`). Under (a) the jet dies at the level where the
  alternation *starts*; under (b) one level later.

The corpus's Door-v residual is the asymptotic sign alternation of the **growing** GGM
solution — nonzero at every level. So **the C1 kernel, read as a shift operator on the
jet tower, is not a carrier of the Door-v residual in either dictionary.** If the
conjecture's identification "symbol = `L_K`" holds and the prolongation operator *is*
its symbol, the `(−1)^m` twist is not produced by the prolongation's own iteration; it
must sit in the seed or in the pairing (`C1 ⊗ C1` vs GGM), not in `D_q`. And the
dictionary question W2 is **not** settled by the residual — both readings fail it the
same way.

Two invariants, both named: monodromy commutation for (b); for (a), that the shift-2
weight `q^{e+2} − 1` is not translation-invariant in `e` while the zeroth-order weight
`−(q − 1)` is. Nothing here constructs `D_q`, and an operator whose *symbol* is `L_K`
but which differs from it by lower-order terms is not excluded.

## References

- [leitner2026] mass-theory/qdifference-kernel-prolongation-symbol
- [leitner2026] mass-theory/c1-ggm-bar-parity-faces
- [leitner2026] docs/audits/2026-09-04-c1-kernel-cannot-carry-door-v-residual.md

LaTeX label: (library module — no content block)
-/

namespace QOU.Mass.C1KernelDictionaryParity

open QOU.Brings.RamificationParityMonodromy QOU.Mathlib.RamifiedShiftCalculus
  QOU.Mathlib.RamifiedShiftCalculusSum QOU.Mass.C1KernelAsShiftSum Finset

variable {R : Type*} [CommRing R] [CharZero R] [NoZeroDivisors R]

/-! ## Generic: a monodromy-commuting operator cannot alternate -/

/-- **Two consecutive alternating levels kill the tower.** If `T` commutes with the
covering monodromy and is homogeneous, the character of level `n` is transported to
level `n + 1` unchanged; alternation between the two levels then forces
`2 · (−1)^n ε · Tⁿ⁺¹X = 0`. No hypothesis on the seed. -/
theorem comm_mono_flip_kills (T : (ℤ → R) → (ℤ → R))
    (hT : ∀ f, T (mono f) = mono (T f)) (hTs : ∀ (r : R) f, T (r • f) = r • T f)
    (X : ℤ → R) (ε : R) (hε : ε ≠ 0) (n : ℕ)
    (h0 : mono (T^[n] X) = ((-1 : R) ^ n * ε) • T^[n] X)
    (h1 : mono (T^[n + 1] X) = ((-1 : R) ^ (n + 1) * ε) • T^[n + 1] X) :
    T^[n + 1] X = 0 := by
  have hA : mono (T^[n + 1] X) = ((-1 : R) ^ n * ε) • T^[n + 1] X := by
    rw [Function.iterate_succ_apply', ← hT, h0, hTs]
  rw [hA] at h1
  funext e
  have h := congrFun h1 e
  simp only [Pi.smul_apply, smul_eq_mul, Pi.zero_apply] at h ⊢
  rw [pow_succ] at h
  have h5 : (2 * ((-1 : R) ^ n * ε)) * T^[n + 1] X e = 0 := by linear_combination h
  rcases mul_eq_zero.mp h5 with h | h
  · exact absurd h (mul_ne_zero two_ne_zero
      (mul_ne_zero (pow_ne_zero _ (neg_ne_zero.mpr one_ne_zero)) hε))
  · exact h

omit [CharZero R] [NoZeroDivisors R] in
/-- A homogeneous operator sends `0` to `0`. -/
theorem map_zero_of_smul (T : (ℤ → R) → (ℤ → R)) (hTs : ∀ (r : R) f, T (r • f) = r • T f) :
    T 0 = 0 := by
  have := hTs 0 0
  simpa using this

/-- **A monodromy-commuting tower that alternates from level `n₀` on is zero from level
`n₀ + 1` on.** -/
theorem comm_mono_residual_from_level_kills_tower (T : (ℤ → R) → (ℤ → R))
    (hT : ∀ f, T (mono f) = mono (T f)) (hTs : ∀ (r : R) f, T (r • f) = r • T f)
    (X : ℤ → R) (ε : R) (hε : ε ≠ 0) (n₀ : ℕ)
    (halt : ∀ n, n₀ ≤ n → mono (T^[n] X) = ((-1 : R) ^ n * ε) • T^[n] X) (k : ℕ) :
    T^[n₀ + 1 + k] X = 0 := by
  induction k with
  | zero =>
    simpa using comm_mono_flip_kills T hT hTs X ε hε n₀ (halt n₀ le_rfl)
      (halt (n₀ + 1) (by omega))
  | succ k ih =>
    rw [show n₀ + 1 + (k + 1) = (n₀ + 1 + k) + 1 by ring, Function.iterate_succ_apply', ih]
    exact map_zero_of_smul T hTs

section Field
variable {K : Type*} [Field K]

/-! ## Dictionary (b): the double cover — killed by monodromy commutation -/

theorem c1KernelOpCover_smul (u : K) (r : K) (f : ℤ → K) :
    c1KernelOpCover u (r • f) = r • c1KernelOpCover u f := by
  funext e
  simp only [c1KernelOpCover_apply, Pi.smul_apply, smul_eq_mul]
  ring

/-- **Under the cover dictionary the kernel cannot carry the residual**: a tower
alternating from level `n₀` on is zero from level `n₀ + 1` on. -/
theorem c1KernelOpCover_residual_kills_tower [CharZero K] (u : K) (X : ℤ → K) (ε : K) (hε : ε ≠ 0)
    (n₀ : ℕ)
    (halt : ∀ n, n₀ ≤ n → mono ((c1KernelOpCover u)^[n] X)
      = ((-1 : K) ^ n * ε) • (c1KernelOpCover u)^[n] X) (k : ℕ) :
    (c1KernelOpCover u)^[n₀ + 1 + k] X = 0 :=
  comm_mono_residual_from_level_kills_tower (c1KernelOpCover u) (c1KernelOpCover_comm_mono u)
    (c1KernelOpCover_smul u) X ε hε n₀ halt k

/-! ## Dictionary (a): the unit shift — killed by the `e`-dependence of the shift-2 weight -/

/-- The even part of the kernel under (a): the shift-2 and zeroth-order terms. -/
def c1E (q : K) (f : ℤ → K) : ℤ → K :=
  shiftOp 2 (fun e => q ^ (e + 2) - 1) f + shiftOp 0 (fun _ => -(q - 1)) f

/-- The odd part of the kernel under (a): the shift-1 term, constant weight `−(q − 1)`. -/
def c1O (q : K) (f : ℤ → K) : ℤ → K :=
  shiftOp 1 (fun _ => -(q - 1)) f

theorem c1E_apply (q : K) (f : ℤ → K) (e : ℤ) :
    c1E q f e = (q ^ (e + 2) - 1) * f (e + 2) - (q - 1) * f e := by
  simp only [c1E, shiftOp, Pi.add_apply, add_zero]
  ring

theorem c1O_apply (q : K) (f : ℤ → K) (e : ℤ) :
    c1O q f e = -(q - 1) * f (e + 1) := by
  simp only [c1O, shiftOp]

theorem c1KernelOp_eq_E_add_O (q : K) (f : ℤ → K) :
    c1KernelOp q f = c1E q f + c1O q f := by
  funext e
  simp only [c1KernelOp, c1E, c1O, Pi.add_apply]
  ring

theorem c1E_comm_mono (q : K) (f : ℤ → K) : c1E q (mono f) = mono (c1E q f) := by
  unfold c1E
  rw [mono_add, shiftOp_comm_mono_of_even 2 even_two,
    shiftOp_comm_mono_of_even 0 ⟨0, by norm_num⟩]

theorem c1O_anticomm_mono (q : K) (f : ℤ → K) : c1O q (mono f) = -mono (c1O q f) :=
  shiftOp_anticomm_mono_of_odd 1 odd_one _ f

theorem c1E_smul (q : K) (r : K) (f : ℤ → K) : c1E q (r • f) = r • c1E q f := by
  funext e
  simp only [c1E_apply, Pi.smul_apply, smul_eq_mul]
  ring

theorem c1O_smul (q : K) (r : K) (f : ℤ → K) : c1O q (r • f) = r • c1O q f := by
  funext e
  simp only [c1O_apply, Pi.smul_apply, smul_eq_mul]
  ring

/-- **The two even-part constraints are jointly fatal.** `E Y = 0` reads
`(q^{e+2} − 1) Y(e+2) = (q − 1) Y(e)`; `E (O Y) = 0` reads the same with `q^{e+1}`.
Subtracting, `q^{e+1}(q − 1) Y(e+2) = 0` for every `e`, so `Y = 0`. -/
theorem c1E_zero_c1E_O_zero_imp (q : K) (hq0 : q ≠ 0) (hq1 : q ≠ 1) (Y : ℤ → K)
    (h0 : c1E q Y = 0) (h1 : c1E q (c1O q Y) = 0) : Y = 0 := by
  have hq' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have key : ∀ e : ℤ, Y (e + 2) = 0 := by
    intro e
    have a := congrFun h0 e
    have b := congrFun h1 (e - 1)
    rw [c1E_apply, Pi.zero_apply] at a
    rw [c1E_apply, c1O_apply, c1O_apply, Pi.zero_apply] at b
    rw [show e - 1 + 2 + 1 = e + 2 by ring, show e - 1 + 2 = e + 1 by ring,
      show e - 1 + 1 = e by ring] at b
    have hQ2 : q ^ (e + 2) = q ^ (e + 1) * q := by
      rw [show e + 2 = (e + 1) + 1 by ring, zpow_add_one₀ hq0]
    rw [hQ2] at a
    have h5 : (q - 1) ^ 2 * q ^ (e + 1) * Y (e + 2) = 0 := by
      linear_combination (q - 1) * a + b
    rcases mul_eq_zero.mp h5 with h | h
    · rcases mul_eq_zero.mp h with h' | h'
      · exact absurd h' (pow_ne_zero _ hq')
      · exact absurd h' (zpow_ne_zero _ hq0)
    · exact h
  funext e
  have := key (e - 2)
  rwa [show e - 2 + 2 = e by ring] at this

/-- **Under the unit-shift dictionary the kernel cannot carry the residual**: a tower
alternating from level `n₀` on has a zero jet already at level `n₀`. -/
theorem c1KernelOp_residual_kills_jet [CharZero K] (q : K) (hq0 : q ≠ 0) (hq1 : q ≠ 1)
    (X : ℤ → K) (ε : K) (hε : ε ≠ 0) (n₀ : ℕ)
    (halt : ∀ n, n₀ ≤ n → mono ((c1KernelOp q)^[n] X)
      = ((-1 : K) ^ n * ε) • (c1KernelOp q)^[n] X) :
    (c1KernelOp q)^[n₀] X = 0 := by
  have hfun : c1KernelOp q = fun f => c1E q f + c1O q f := funext (c1KernelOp_eq_E_add_O q)
  rw [hfun] at halt ⊢
  have h := residual_from_level_tower_is_odd_part (c1E q) (c1O q) (c1E_comm_mono q)
    (c1O_anticomm_mono q) (c1E_smul q) (c1O_smul q) X ε hε n₀ halt
  have h0 := (h 0).2
  have h1 := (h 1).2
  simp only [Function.iterate_zero, id_eq, Function.iterate_one] at h0 h1
  exact c1E_zero_c1E_O_zero_imp q hq0 hq1 _ h0 h1

theorem c1KernelOp_smul (q : K) (r : K) (f : ℤ → K) :
    c1KernelOp q (r • f) = r • c1KernelOp q f := by
  funext e
  simp only [c1KernelOp_apply, Pi.smul_apply, smul_eq_mul]
  ring

/-- ... and hence the whole tower is zero from level `n₀` on. -/
theorem c1KernelOp_residual_kills_tower [CharZero K] (q : K) (hq0 : q ≠ 0) (hq1 : q ≠ 1)
    (X : ℤ → K) (ε : K) (hε : ε ≠ 0) (n₀ : ℕ)
    (halt : ∀ n, n₀ ≤ n → mono ((c1KernelOp q)^[n] X)
      = ((-1 : K) ^ n * ε) • (c1KernelOp q)^[n] X) (k : ℕ) :
    (c1KernelOp q)^[n₀ + k] X = 0 := by
  induction k with
  | zero => simpa using c1KernelOp_residual_kills_jet q hq0 hq1 X ε hε n₀ halt
  | succ k ih =>
    rw [show n₀ + (k + 1) = (n₀ + k) + 1 by ring, Function.iterate_succ_apply', ih]
    exact map_zero_of_smul _ (c1KernelOp_smul q)

end Field

end QOU.Mass.C1KernelDictionaryParity
