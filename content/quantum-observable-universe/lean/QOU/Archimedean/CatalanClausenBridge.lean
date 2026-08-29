import QOU.Archimedean.ClausenFunctionMathlibFiller
import QOU.Archimedean.HyperbolicVolumeTranscendence

/-!
# QOU.Archimedean.CatalanClausenBridge — the two Catalan definitions agree

This repo defines Catalan's constant **twice**, in two files that do not import each
other, and until now nothing connected them:

* `QOU.Archimedean.HyperbolicVolumeTranscendence.catalan_G`
  `:= ∑' k, (-1)^k / (2k+1)^2` — the alternating series;
* `QOU.Archimedean.ClausenFunctionMathlibFiller.Catalan_constant`
  `:= Cl_2 (π/2)`, where `Cl_2 θ := ∑' k, sin((k+1)θ) / (k+1)^2` — the Clausen value.

The filler's `catalan_constant_eq_cl_2_pi_over_2` is `rfl`: it restates a *definition*
and carries no content. The mathematical claim — that the alternating series and the
Clausen value are the same real number — was **unproved**, and a corpus grep found no
cross-reference between `catalan_G` and `Cl_2` anywhere in the tree. Two unbridged
definitions of one constant is a live hazard: a downstream result proved about one is
not a result about the other.

`catalan_G_eq_Cl_2_pi_div_two` closes that. The proof is elementary — no analysis, no
integrals — because at `θ = π/2` the Clausen series *is* the alternating series with
its zero terms removed:

* `sin((2k+2)·π/2) = sin((k+1)π) = 0`, so every odd-index term vanishes;
* `sin((2k+1)·π/2) = cos(kπ) = (-1)^k`, so the even-index terms are the Catalan summand.

`tsum_even_add_odd` then splits the sum. `Real.cos_nat_mul_pi` is not in Mathlib at this
toolchain, so `cos_nat_mul_pi'` proves it by induction via `Real.cos_add_pi`.

**Scope.** This says nothing about the `lobachevsky (π/4) = catalan_G / 2` axiom in
`BorromeanVolumeCatalan`. That one relates an *integral* to the series and needs the
Clausen integral representation (`Cl_2' θ = -log|2 sin(θ/2)|`) — genuine analysis over an
improper integrand, and still correctly classified External by
`docs/audits/2026-06-03-lean-axiom-tractability-triage.md`. What this file does supply is
the *other* half of that identity's bridge, so the residual gap is now exactly the
integral representation and nothing else.
-/

open Real QOU.Archimedean

namespace QOU.Archimedean


theorem cos_nat_mul_pi' (k : Nat) : Real.cos ((k : Real) * Real.pi) = (-1)^k := by
  induction k with
  | zero => simp
  | succ n ih =>
      have : ((n+1 : Nat) : Real) * Real.pi = (n : Real) * Real.pi + Real.pi := by
        push_cast; ring
      rw [this, Real.cos_add_pi, ih]; ring

-- summability of the Catalan summand, as its own step
theorem summable_catalan_summand :
    Summable (fun k : Nat => (-1 : Real)^k / (2*(k : Real)+1)^2) := by
  have hbase : Summable (fun n : Nat => 1 / ((n + 1 : Nat) : Real) ^ 2) :=
    (summable_nat_add_iff 1).mpr (Real.summable_one_div_nat_pow.mpr one_lt_two)
  refine Summable.of_abs ?_
  refine Summable.of_nonneg_of_le (fun k => abs_nonneg _) (fun k => ?_) hbase
  have hk : (0 : Real) <= (k : Real) := k.cast_nonneg
  have hpos : (0 : Real) < ((k : Real) + 1)^2 := by positivity
  have h1 : |(-1 : Real)^k / (2*(k : Real)+1)^2| = 1 / (2*(k : Real)+1)^2 := by
    rw [abs_div, abs_pow, abs_neg, abs_one, one_pow,
        abs_of_nonneg (by positivity : (0:Real) <= (2*(k : Real)+1)^2)]
  rw [h1]
  have h2 : (1 : Real) / (((k : Nat) + 1 : Nat) : Real)^2 = 1 / ((k : Real)+1)^2 := by
    push_cast; ring
  rw [h2]
  apply one_div_le_one_div_of_le hpos
  nlinarith [hk]

theorem catalan_G_eq_Cl_2_pi_div_two : catalan_G = Cl_2 (Real.pi / 2) := by
  set f : Nat -> Real := fun k => Real.sin (((k : Real) + 1) * (Real.pi/2)) / ((k : Real) + 1)^2
    with hf
  have hodd : (fun k : Nat => f (2*k+1)) = fun _ => (0 : Real) := by
    funext k
    simp only [hf]
    have h : ((2*k+1 : Nat) : Real) + 1 = ((k+1 : Nat) : Real) * 2 := by push_cast; ring
    rw [h]
    have h2 : ((k+1 : Nat) : Real) * 2 * (Real.pi/2) = ((k+1 : Nat) : Real) * Real.pi := by ring
    rw [h2, Real.sin_nat_mul_pi, zero_div]
  have heven : forall k : Nat, f (2*k) = (-1 : Real)^k / (2*(k : Real)+1)^2 := by
    intro k
    simp only [hf]
    have h : ((2*k : Nat) : Real) + 1 = 2*(k : Real) + 1 := by push_cast; ring
    rw [h]
    have h2 : (2*(k : Real) + 1) * (Real.pi/2) = (k : Real) * Real.pi + Real.pi/2 := by ring
    rw [h2, Real.sin_add, Real.sin_nat_mul_pi, cos_nat_mul_pi']
    simp
  have hEvenFun : (fun k : Nat => f (2*k))
      = (fun k : Nat => (-1 : Real)^k / (2*(k : Real)+1)^2) := funext heven
  have hEven : Summable (fun k : Nat => f (2*k)) := by
    rw [hEvenFun]; exact summable_catalan_summand
  have hOdd : Summable (fun k : Nat => f (2*k+1)) := by rw [hodd]; exact summable_zero
  have hsplit := tsum_even_add_odd hEven hOdd
  rw [hodd] at hsplit
  simp only [tsum_zero, add_zero] at hsplit
  have hE : (∑' k : Nat, f (2*k)) = catalan_G := by
    rw [hEvenFun]
    unfold catalan_G
    exact tsum_congr (fun k => by ring)
  rw [hE] at hsplit
  have hCl : Cl_2 (Real.pi/2) = ∑' k : Nat, f k := rfl
  rw [hCl]
  exact hsplit

end QOU.Archimedean
