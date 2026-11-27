/-
Copyright (c) 2026 QOU contributors. Released under CC BY 4.0.

# Σ(2,3,5): the period-60 character and its Borel-sector actions

Bean `qou-6gf9` (option 2, resummation). Formalize-first scaffold for
`computations/mu_p_sigma235_borel_resummation_probe.py`.

The Ohtsuki series of the unified WRT invariant `I(Σ(2,3,5); q)` is the `q → 1`
asymptotic expansion of `(½·A(q) − 1)/(q(1 − q))` with the Lawrence–Zagier
false theta `A(q) = Σ_{n ≥ 1} χ₊(n) q^{(n² − 1)/120}` (`lovejoy2026`, eq. (1.3)
and `[LZ]`; the probe checks the coefficient match through order 9 exactly).
Its Borel transform in `t = −log q` is a finite-type sum over `j ≥ 1` of
`(s(j)/j)·(1 − 30ξ/(π² j²))^{−1/2}`, where `s(j)` is the sine-Gauss sum of `χ₊`
and is non-zero exactly on `dualSupport` below. So the Borel singularities sit
at `ξ_j = π² j² / 30` and the trans-series sectors are `exp(−π² j² /(30 |t|))`.

This file proves, over `ℕ`/`ℤ` and with no imports, the two finite facts the
probe's sector table rests on:

* `chiPlus` is odd and supported on `n² ≡ 1 (mod 120)` (so the exponent
  `(n² − 1)/120` is an integer);
* the sector actions `j²` for `j ∈ dualSupport` take no value strictly between
  `1` and `49` (`dualSupport_action_gap`).

Nothing empirical enters this file. The comparison of any sector size with a
measured residual is done only in the probe's comparison block.
-/

namespace QOU.BraidsAndKnots.PoincareSphereBorelSectors

/-- The Lawrence–Zagier period-60 character of `Σ(2,3,5)` (sign convention of the
probe: `A(1) = L(0, χ₊) = 2`, `H(1) = ½A(1) = 1`). -/
def chiPlus (n : Nat) : Int :=
  match n % 60 with
  | 1 | 11 | 19 | 29 => 1
  | 31 | 41 | 49 | 59 => -1
  | _ => 0

/-- Residues carrying a non-zero dual (sine-Gauss) coefficient `s(j)`:
`j² ≡ 1` or `j² ≡ 49 (mod 120)`. These are the Chern–Simons values
`−1/120` and `−49/120` of the two irreducible flat `SU(2)` connections. -/
def dualSupport (j : Nat) : Bool :=
  (j * j) % 120 == 1 || (j * j) % 120 == 49

/-- `χ₊` is odd on residues: `χ₊(60 − r) = −χ₊(r)` for `0 < r < 60`. -/
theorem chiPlus_odd : ∀ r : Fin 60, r.val ≠ 0 → chiPlus (60 - r.val) = - chiPlus r.val := by
  decide

/-- `χ₊` is supported on `n² ≡ 1 (mod 120)` (checked on one period of 120). -/
theorem chiPlus_support_sq : ∀ n : Fin 120, chiPlus n.val ≠ 0 → (n.val * n.val) % 120 = 1 := by
  decide

/-- `χ₊` has period 60 (definitional, recorded for the probe's Bernoulli sums). -/
theorem chiPlus_periodic (n : Nat) : chiPlus (n + 60) = chiPlus n := by
  simp [chiPlus, Nat.add_mod_right]

/-- Only `j = 1` lies in `dualSupport` below `7`. -/
theorem dualSupport_lt_seven : ∀ j : Fin 7, dualSupport j.val = true → j.val = 1 := by
  decide

/-- **Action gap.** For every `j` in the dual support, the sector action `j²`
is either `1` or at least `49`: no Borel sector of this series has action ratio
strictly between `1` and `49` relative to the first. -/
theorem dualSupport_action_gap (j : Nat) (h : dualSupport j = true) :
    j * j = 1 ∨ 49 ≤ j * j := by
  by_cases hj : j < 7
  · left
    have := dualSupport_lt_seven ⟨j, hj⟩ h
    simp at this
    subst this
    rfl
  · right
    have h7 : 7 ≤ j := Nat.le_of_not_lt hj
    exact Nat.mul_le_mul h7 h7

end QOU.BraidsAndKnots.PoincareSphereBorelSectors
