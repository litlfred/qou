import Mathlib.Logic.Equiv.Defs
import Mathlib.Tactic

/-!
# Rotating an interval of `Fin n`

`intervalRotate a m k` rotates the block `[a, a+m)` of `Fin n` by `k` and fixes
everything outside it.

## Why this exists

The Garnir tableau `g_{ij}` of Mathas §3 is *defined* procedurally — "place
`a, a+1, …, b` in increasing order into the remaining cells, first along row
`i+1`, then along row `i`" — and formalising a procedure means discharging a
surjectivity obligation for a bespoke map.

It is not a procedure. Measured in
`computations/hecke/garnir_permutation_is_rotation_probe.py` (108 Garnir
tableaux, all partitions of `n = 3..7`, zero mismatches), the induced
permutation of labels is exactly a **cyclic rotation of the interval `[a,b]` by
`j+1`**.  A rotation is invertible by construction, so building `g_{ij}` on this
gives bijectivity for free.

Nothing here mentions tableaux; it is ordinary arithmetic on `Fin n`.
-/

namespace QOU.BraidKnot.IntervalRotate

/-- Rotate `[a, a+m)` by `k`, as a map on `ℕ`; the identity off that block. -/
def rotNat (a m k x : ℕ) : ℕ :=
  if a ≤ x ∧ x < a + m then a + (x - a + k) % m else x

theorem rotNat_of_not_mem {a m k x : ℕ} (h : ¬(a ≤ x ∧ x < a + m)) :
    rotNat a m k x = x := if_neg h

theorem rotNat_of_mem {a m k x : ℕ} (h : a ≤ x ∧ x < a + m) :
    rotNat a m k x = a + (x - a + k) % m := if_pos h

/-- A rotation maps the block into itself, so it never leaves `[0, n)`. -/
theorem rotNat_lt {a m k x n : ℕ} (hx : x < n) (hb : a + m ≤ n) :
    rotNat a m k x < n := by
  unfold rotNat
  split_ifs with h
  · have hm : 0 < m := by omega
    have := Nat.mod_lt (x - a + k) hm
    omega
  · exact hx

/-- A zero-width block rotates to nothing. -/
@[simp] theorem rotNat_zero_width (a k x : ℕ) : rotNat a 0 k x = x :=
  rotNat_of_not_mem (by omega)

/-- **Rotations compose by adding their shifts.**  This is the whole content of
the file: both inverse directions fall out of it. -/
theorem rotNat_add {a m k k' x : ℕ} (hm : 0 < m) :
    rotNat a m k' (rotNat a m k x) = rotNat a m (k + k') x := by
  unfold rotNat
  by_cases hx : a ≤ x ∧ x < a + m
  · have hlt : (x - a + k) % m < m := Nat.mod_lt _ hm
    rw [if_pos hx, if_pos (⟨by omega, by omega⟩ : a ≤ a + (x - a + k) % m ∧ _), if_pos hx]
    congr 1
    have hsimp : a + (x - a + k) % m - a = (x - a + k) % m := by omega
    rw [hsimp, Nat.mod_add_mod]
    congr 1
    omega
  · rw [if_neg hx, if_neg hx, if_neg hx]

/-- A shift that is a multiple of the width does nothing. -/
theorem rotNat_of_mod_eq_zero {a m k x : ℕ} (hk : k % m = 0) :
    rotNat a m k x = x := by
  unfold rotNat
  split_ifs with h
  · have hxa : x - a < m := by omega
    have : (x - a + k) % m = (x - a) % m := by
      simp [Nat.add_mod, hk]
    rw [this, Nat.mod_eq_of_lt hxa]
    omega
  · rfl

/-- The complementary shift: `k + (m - k % m)` is a multiple of `m`. -/
theorem add_compl_mod_eq_zero {m k : ℕ} (hm : 0 < m) :
    (k + (m - k % m)) % m = 0 := by
  have hmod : m * (k / m) + k % m = k := Nat.div_add_mod k m
  have hlt : k % m < m := Nat.mod_lt _ hm
  have hEq : k + (m - k % m) = m * (k / m + 1) := by
    have : m * (k / m + 1) = m * (k / m) + m := by ring
    omega
  rw [hEq, Nat.mul_mod_right]

/-- **Rotation of the block `[a, a+m)` as a permutation of `Fin n`.** -/
def intervalRotate {n : ℕ} (a m k : ℕ) (hb : a + m ≤ n) : Equiv.Perm (Fin n) where
  toFun x := ⟨rotNat a m k x, rotNat_lt x.2 hb⟩
  invFun x := ⟨rotNat a m (m - k % m) x, rotNat_lt x.2 hb⟩
  left_inv x := by
    rcases Nat.eq_zero_or_pos m with hm | hm
    · subst hm; exact Fin.ext (by simp)
    · refine Fin.ext ?_
      show rotNat a m (m - k % m) (rotNat a m k x) = x
      rw [rotNat_add hm]
      exact rotNat_of_mod_eq_zero (add_compl_mod_eq_zero hm)
  right_inv x := by
    rcases Nat.eq_zero_or_pos m with hm | hm
    · subst hm; exact Fin.ext (by simp)
    · refine Fin.ext ?_
      show rotNat a m k (rotNat a m (m - k % m) x) = x
      rw [rotNat_add hm]
      refine rotNat_of_mod_eq_zero ?_
      rw [show m - k % m + k = k + (m - k % m) by omega]
      exact add_compl_mod_eq_zero hm

@[simp] theorem intervalRotate_apply {n : ℕ} (a m k : ℕ) (hb : a + m ≤ n) (x : Fin n) :
    ((intervalRotate a m k hb x : Fin n) : ℕ) = rotNat a m k x := rfl

/-- Outside the block, the rotation is the identity. -/
theorem intervalRotate_eq_self {n : ℕ} {a m k : ℕ} (hb : a + m ≤ n) {x : Fin n}
    (h : ¬((a : ℕ) ≤ x ∧ (x : ℕ) < a + m)) : intervalRotate a m k hb x = x :=
  Fin.ext (rotNat_of_not_mem h)

/-- A zero-width block gives the identity permutation. -/
@[simp] theorem intervalRotate_zero {n : ℕ} (a k : ℕ) (hb : a + 0 ≤ n) :
    intervalRotate (n := n) a 0 k hb = 1 := by
  refine Equiv.ext fun x => Fin.ext ?_
  show rotNat a 0 k x = x
  simp

/-! ### Non-vacuity

A rotation must actually MOVE things, or every lemma above is satisfied by the
identity.  Concrete witnesses, checked by `decide`: -/

section NonVacuity

/-- Rotating `[1,4)` of `Fin 6` by `1` sends `1 ↦ 2`: the map is not the identity. -/
example : (intervalRotate (n := 6) 1 3 1 (by omega)) 1 = 2 := by decide

/-- It wraps: the top of the block returns to the bottom. -/
example : (intervalRotate (n := 6) 1 3 1 (by omega)) 3 = 1 := by decide

/-- It fixes everything outside the block. -/
example : (intervalRotate (n := 6) 1 3 1 (by omega)) 5 = 5 := by decide

/-- A full-width shift is the identity, but a partial one is not — so the
`k % m = 0` hypothesis in `rotNat_of_mod_eq_zero` is doing real work. -/
example : (intervalRotate (n := 6) 1 3 3 (by omega)) 1 = 1 := by decide

end NonVacuity

end QOU.BraidKnot.IntervalRotate
