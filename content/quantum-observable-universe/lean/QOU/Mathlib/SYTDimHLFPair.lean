import QOU.Mathlib.SYTHookFormulaRows

/-!
# QOU.Mathlib.SYTDimHLFPair — the two-row hook-length dimension is the ballot number

`dimHLF` is the Frame–Robinson–Thrall dimension `(∑l)! / ∏h_c` as a **floor** `ℕ`-division, so it
cannot be manipulated algebraically until its exactness is pinned.  This file pins it on two rows:

    dimHLF [a, b]  =  C(a+b, b) − C(a+b, b−1)          (`dimHLF_pair`,  a ≥ b ≥ 1)

the classical **ballot number** — a manifest `ℕ` (a difference of binomial coefficients), with **no
division**.  This is the integrality infrastructure the two-row case of the corner-removal recursion
(A) `dimHLF_branching` needs: once the dimension is a binomial difference, the branching
`dimHLF[a,b] = dimHLF[a−1,b] + dimHLF[a,b−1]` is just **Pascal's rule** (no `ℕ`-division to fight).

Proof route: from the two-row hook product `prodHooks[a,b]·(a+1−b)! = (a+1)!·(a−b)!·b!`
(`SYTHookRows.prodHooks_pair_mul`) and `Nat.choose_mul_factorial_mul_factorial`, show
`(C(a+b,b) − C(a+b,b−1)) · prodHooks[a,b] = (a+b)!`, then read off the floor-division via
`Nat.div_eq_of_eq_mul_left`.  Pure ℕ; nothing archimedean.
-/

namespace QOU.Mathlib.SYTHookRows

open QOU.BraidKnot.IdentityI (prodHooks dimHLF sz)

/-- **Two-row hook-length dimension as a ballot number (sorry-free).**
`dimHLF [a, b] = C(a+b, b) − C(a+b, b−1)` for `a ≥ b ≥ 1` — a binomial difference, so a manifest `ℕ`
with no floor-division.  Pins the exactness of `dimHLF` on two rows. -/
theorem dimHLF_pair (a b : ℕ) (hab : b ≤ a) (hb : 1 ≤ b) :
    dimHLF [a, b] = Nat.choose (a + b) b - Nat.choose (a + b) (b - 1) := by
  set Cb := Nat.choose (a + b) b with hCb
  set Cb1 := Nat.choose (a + b) (b - 1) with hCb1
  set M := Nat.factorial (a + 1) * Nat.factorial (a - b) * Nat.factorial b with hM
  have e1 : Cb * Nat.factorial b * Nat.factorial a = Nat.factorial (a + b) := by
    have := Nat.choose_mul_factorial_mul_factorial (n := a + b) (k := b) (by omega)
    simpa [hCb, Nat.add_sub_cancel_left, show a + b - b = a from by omega] using this
  have e2 : Cb1 * Nat.factorial (b - 1) * Nat.factorial (a + 1) = Nat.factorial (a + b) := by
    have := Nat.choose_mul_factorial_mul_factorial (n := a + b) (k := b - 1) (by omega)
    simpa [hCb1, show a + b - (b - 1) = a + 1 from by omega] using this
  have ht1 : Cb * M = (a + 1) * Nat.factorial (a - b) * Nat.factorial (a + b) := by
    rw [hM, Nat.factorial_succ a, ← e1]; ring
  have ht2 : Cb1 * M = b * Nat.factorial (a - b) * Nat.factorial (a + b) := by
    rw [hM, ← Nat.mul_factorial_pred (show b ≠ 0 by omega), ← e2]; ring
  have hfac : Nat.factorial (a + 1 - b) = (a + 1 - b) * Nat.factorial (a - b) := by
    rw [show a + 1 - b = (a - b) + 1 from by omega, Nat.factorial_succ]
  have hadd : Cb * M = Nat.factorial (a + b) * Nat.factorial (a + 1 - b) + Cb1 * M := by
    rw [ht1, ht2, hfac]
    have hbb : a + 1 - b + b = a + 1 := by omega
    calc (a + 1) * Nat.factorial (a - b) * Nat.factorial (a + b)
        = (a + 1) * (Nat.factorial (a - b) * Nat.factorial (a + b)) := by ring
      _ = (a + 1 - b + b) * (Nat.factorial (a - b) * Nat.factorial (a + b)) := by rw [hbb]
      _ = Nat.factorial (a + b) * ((a + 1 - b) * Nat.factorial (a - b))
            + b * Nat.factorial (a - b) * Nat.factorial (a + b) := by ring
  have star : (Cb - Cb1) * M = Nat.factorial (a + b) * Nat.factorial (a + 1 - b) := by
    rw [Nat.sub_mul, hadd, Nat.add_sub_cancel]
  have hpp := prodHooks_pair_mul a b hab hb
  have key : (Cb - Cb1) * prodHooks [a, b] = Nat.factorial (a + b) := by
    have h0 : 0 < Nat.factorial (a + 1 - b) := Nat.factorial_pos _
    apply Nat.eq_of_mul_eq_mul_right h0
    calc (Cb - Cb1) * prodHooks [a, b] * Nat.factorial (a + 1 - b)
        = (Cb - Cb1) * (prodHooks [a, b] * Nat.factorial (a + 1 - b)) := by ring
      _ = (Cb - Cb1) * M := by rw [hpp, hM]
      _ = Nat.factorial (a + b) * Nat.factorial (a + 1 - b) := star
  unfold dimHLF
  have hpos : 0 < prodHooks [a, b] := by
    rcases Nat.eq_zero_or_pos (prodHooks [a, b]) with h | h
    · rw [h, Nat.mul_zero] at key; exact absurd key.symm (Nat.factorial_ne_zero _)
    · exact h
  have hsz : sz [a, b] = a + b := by simp [sz]
  rw [hsz]
  exact Nat.div_eq_of_eq_mul_left hpos key.symm

end QOU.Mathlib.SYTHookRows
