/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/

/-!
# The 3 in `−12 = −k²·3`: the proton weight space has dimension 3

The `−12` audit (`ProtonTwelveOrigin.weight_space_weight_eq_two`) reduced the `−12 m_e`
term to `τ(R_p∘R_p) = −k²·dim W_p` with `k` the Reeb weight and `W_p` the proton weight
space that `hReebP` (`CategoricalLagrangianTwoTermBridge`) traces over with the
unnormalised `Matrix.trace` on `Fin 3`. This file derives `dim W_p = 3` from the inputs
the mass pipeline already fixes, instead of reading it off the `Fin 3` in the code:

1. three strands: `β_Bor = (σ₀σ₁⁻¹)³ ∈ B₃`;
2. each strand carries `V = C²` with basis `e₁ = u`, `e₂ = d` (level-2 Jimbo braiding,
   `NucleonWeightSpaceTraces`);
3. the proton sector is the `K^{⊗3}`-eigenspace of eigenvalue `q`
   (`NucleonWeightSpaceTwoTerm.Kp = q • 1`), where `K` acts as `q` on `e₁` and `q⁻¹` on `e₂`.

A basis state of `(C²)^{⊗3}` with `d` copies of `e₂` has `K`-weight `q^(3−2d)`. For `q` not a
root of unity, weight `q` holds iff `3 − 2d = 1`, i.e. `d = 1`, and there are exactly 3 such
states (`e₁e₁e₂, e₁e₂e₁, e₂e₁e₁`), the basis the corpus uses. The same set is cut out by
electric charge `+1` with `Q = diag(2/3, −1/3)` (`charge_iff_one_d`). Lean checks the
exponent step (`weight_one_iff_one_d`); the step "`q^e = q` forces `e = 1` for `q` not a root of
unity" is standard and stays in prose. Schur–Weyl splits the space as `3 = 1 + 2`
(`V_(3) ⊕ V_(2,1)`); that decomposition is cited, and Lean checks only the arithmetic and the
transitivity of the `S₃` action (`kostka_split`, `transitive_on_proton`).

Consequence (`twelve_iff_weight_two`): with `dim W_p = 3` derived, a scalar Reeb square
`R∘R = −k²·𝟙` gives `−12` iff `k² = 4`. The Reeb weight `k` is still not derived.

Core Lean only, all by `decide`. No empirical number enters.
-/

namespace QOU.MassTheory.ProtonWeightSpaceDim

/-- Basis states of `(C²)^{⊗3}`: `true` at position `i` means `e₂ = d` on strand `i`. -/
def states : List (List Bool) :=
  [false, true].flatMap fun a => [false, true].flatMap fun b => [false, true].map fun c => [a, b, c]

theorem states_length : states.length = 8 := by decide

/-- Number of `e₂` factors. -/
def numD (s : List Bool) : Nat := (s.filter id).length

/-- `K`-weight exponent: `K^{⊗3}` acts on the state by `q ^ weightExp s`. -/
def weightExp (s : List Bool) : Int := (s.length : Int) - 2 * (numD s : Int)

/-- Three times the electric charge, `Q(u) = 2/3`, `Q(d) = −1/3`. -/
def charge3 (s : List Bool) : Int := (s.map fun x => if x then (-1 : Int) else 2).foldl (· + ·) 0

/-- The proton weight space: states of `K`-weight exponent `1`. -/
def protonStates : List (List Bool) := states.filter fun s => weightExp s = 1

/-- **`dim W_p = 3`**, and the basis is `e₁e₁e₂, e₁e₂e₁, e₂e₁e₁`. -/
theorem protonStates_eq :
    protonStates = [[false, false, true], [false, true, false], [true, false, false]] := by decide

theorem dim_proton_weight_space : protonStates.length = 3 := by decide

/-- Weight exponents occurring on `(C²)^{⊗3}` are `3, 1, −1, −3`; so `q^e = q` with `q` not a
root of unity singles out `e = 1` (the differences `e − 1` are `2, 0, −2, −4`). -/
theorem weight_exponents : states.map weightExp = [3, 1, 1, -1, 1, -1, -1, -3] := by decide

/-- Charge `+1` cuts out the same three states. -/
theorem charge_iff_one_d : states.filter (fun s => charge3 s = 3) = protonStates := by decide

/-- Neutron check: charge `0` is the weight `q⁻¹` space, also of dimension 3. -/
theorem neutron_dim : (states.filter fun s => charge3 s = 0).length = 3 ∧
    (states.filter fun s => charge3 s = 0) = states.filter (fun s => weightExp s = -1) := by
  decide

/-- On the three strand states, weight exponent `1` is exactly `d = 1`. -/
theorem weight_one_iff_one_d : ∀ s ∈ states, weightExp s = 1 ↔ numD s = 1 := by decide

/-- Swap the entries at positions `i` and `j`. -/
def swapList (s : List Bool) (i j : Nat) : List Bool :=
  (s.set i (s.getD j false)).set j (s.getD i false)

/-- `S₃` acts transitively on the proton states: any one is carried to any other by the
identity or a transposition. -/
theorem transitive_on_proton : ∀ s ∈ protonStates, ∀ t ∈ protonStates,
    ∃ p ∈ [(0, 0), (0, 1), (0, 2), (1, 2)], swapList s p.1 p.2 = t := by decide

/-- **Arithmetic only.** `dim W_p = 1·1 + 2·1`. The Schur–Weyl decomposition
`W_p = V_(3) ⊕ V_(2,1)` is cited (Kostka numbers `K_{(3),(2,1)} = K_{(2,1),(2,1)} = 1`), not
proved here. What is checked is `transitive_on_proton`: by Frobenius reciprocity (cited) a
transitive permutation module contains `V_(3)` once, which leaves a 2-dimensional complement. -/
theorem kostka_split : 1 * 1 + 2 * 1 = protonStates.length := by decide

/-- With `dim W_p = 3`, a scalar Reeb square `−k²·𝟙` traces to `−12` iff `k = ±2`. -/
theorem twelve_iff_weight_two (k : Int) (hk : -3 ≤ k ∧ k ≤ 3) :
    -(k ^ 2) * (protonStates.length : Int) = -12 ↔ k = 2 ∨ k = -2 := by
  obtain ⟨h1, h2⟩ := hk
  have : k = -3 ∨ k = -2 ∨ k = -1 ∨ k = 0 ∨ k = 1 ∨ k = 2 ∨ k = 3 := by omega
  rcases this with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> decide

/-- Outside `|k| ≤ 3` the trace is below `−12`, so the bound in `twelve_iff_weight_two`
loses nothing: `|k| ≥ 4` gives `−k²·3 ≤ −48`. -/
theorem large_weight_misses (k : Int) (hk : 4 ≤ k ∨ k ≤ -4) : -(k ^ 2) * 3 ≠ -12 := by
  intro h
  have : k ^ 2 = 4 := by omega
  rcases hk with hk | hk
  · have : 16 ≤ k ^ 2 := by
      have := Int.mul_le_mul hk hk (by decide) (by omega)
      simpa [Int.pow_succ, Int.pow_zero] using this
    omega
  · have : 16 ≤ k ^ 2 := by
      have := Int.mul_le_mul (Int.neg_le_neg hk) (Int.neg_le_neg hk) (by decide) (by omega)
      simpa [Int.pow_succ, Int.pow_zero, Int.neg_mul_neg] using this
    omega

end QOU.MassTheory.ProtonWeightSpaceDim
