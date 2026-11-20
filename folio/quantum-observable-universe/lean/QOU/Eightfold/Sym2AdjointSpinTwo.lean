import QOU.Eightfold.Sym2GateParity
import QOU.QuantumObservableUniverse.Structures

/-!
# QOU.Eightfold.Sym2AdjointSpinTwo — `V₂ = Sym²(V₁) ⊖ V₀` for the gauge `SU(2)`

The spin-`2` label of the gauge group `G = Aut^⊗(τ) ≅ SU(2)` is the **unique
traceless symmetric summand** of the tensor square of the adjoint `V₁ = Ad(A)`:

  `Sym²(V₁) = V₀ ⊕ V₂`      (dims `1 + 5 = 6 = 3·4/2`),

where `V₀` is the trace part (the invariant symmetric form on the orthogonal,
odd-dimensional adjoint) and `V₂` is what remains after removing it.

**What is reused, not re-derived.**

* `Sym2GateParity.sym2Indices` — the Clebsch–Gordan/parity description of the
  summands `V_k` of `Sym²(V_j)` (index `k` is the spin, `dim V_k = 2k + 1`);
* `Sym2GateParity.adjoint_fails_gate` — the singlet `k = 0` *is* in
  `Sym²(V₁)` (this is the trace summand that `⊖ V₀` removes);
* `Sym2GateParity.sym2_dim_twoJ_two` — `dim Sym²(V₁) = 6`;
* `QOU.SpinLabels` / `QOU.adjoint_dim` — the `twice_j` convention, under which
  the adjoint is `twice_j = 2` (`adjoint_is_one` of `prop:spin-labels`) and the
  new label is `twice_j = 4`, matching `QOU.Examples.su2_dim_spin_two`.

**Scope.** Every statement here is about the representation theory of the
*gauge* `SU(2) = Aut^⊗(τ)`. Nothing in this file identifies that group with a
rotation or Lorentz group of spacetime, so nothing here says that `V₂` is a
spin-`2` field *in spacetime*. That identification is the missing step for any
graviton reading; see `rem:sym2-adjoint-spin-two-gauge-not-lorentz`.

-- Ref: [fulton-harris1991] §11 (Clebsch–Gordan for `sl₂`).
-/

namespace QOU.Eightfold.Sym2AdjointSpinTwo

open QOU.Eightfold.Sym2GateParity

/-- The spin-`2` label `V₂` in the `twice_j` convention of `QOU.SpinLabels`. -/
def spinTwo : QOU.SpinLabels := { twice_j := 4 }

/-- `dim V₂ = 2·2 + 1 = 5` (the same value as `QOU.Examples.su2_dim_spin_two`). -/
theorem spinTwo_cat_dim : spinTwo.cat_dim = 5 := rfl

/-- **The summands of `Sym²(V₁)`.** For the adjoint (`2j = 2`) the symmetric
square contains exactly the spins `k = 0` and `k = 2`; the antisymmetric spin
`k = 1` is absent (it lives in `Λ²(V₁) ≅ V₁`). -/
theorem mem_sym2Indices_adjoint (k : ℕ) :
    k ∈ sym2Indices 2 ↔ k = 0 ∨ k = 2 := by
  unfold sym2Indices
  rw [Finset.mem_filter, Finset.mem_range]
  constructor
  · rintro ⟨h1, h2⟩
    omega
  · rintro (rfl | rfl) <;> decide

/-- **Removing the trace leaves exactly spin `2`.** The traceless part
`Sym²(V₁) ⊖ V₀` — the summands of `Sym²(V₁)` other than the singlet — consists
of the single index `k = 2`. -/
theorem mem_traceless_sym2_adjoint_iff (k : ℕ) :
    k ∈ (sym2Indices 2).erase 0 ↔ k = 2 := by
  rw [Finset.mem_erase, mem_sym2Indices_adjoint]
  constructor
  · rintro ⟨h0, h | h⟩
    · exact absurd h h0
    · exact h
  · rintro rfl
    exact ⟨by decide, Or.inr rfl⟩

/-- **Uniqueness by dimension.** Among the summands of `Sym²(V₁)`, the only one
of dimension `5` is `k = 2`; the other (the singlet) has dimension `1`. -/
theorem sym2_adjoint_dim_five_iff (k : ℕ) (hk : k ∈ sym2Indices 2) :
    2 * k + 1 = 5 ↔ k = 2 := by
  rcases (mem_sym2Indices_adjoint k).1 hk with rfl | rfl <;> decide

/-- **Theorem (`V₂ = Sym²(V₁) ⊖ V₀`).** For the gauge `SU(2)`:

1. the singlet `V₀` occurs in `Sym²(V₁)` (`adjoint_fails_gate`);
2. after removing it, exactly one summand is left, of spin `k = 2`;
3. its label is `spinTwo` (`twice_j = 2·2 = 4`) and its dimension is `5`;
4. the dimension count closes: `dim Sym²(V₁) = 6 = 1 + dim V₂`
   (`sym2_dim_twoJ_two`).

This is a statement about the gauge group `Aut^⊗(τ)` only. -/
theorem adjoint_sym2_traceless_is_spin_two :
    0 ∈ sym2Indices 2 ∧
    (∀ k, k ∈ (sym2Indices 2).erase 0 ↔ k = 2) ∧
    spinTwo.twice_j = 2 * 2 ∧
    spinTwo.cat_dim = 5 ∧
    (sym2Indices 2).sum (fun k => 2 * k + 1) = 1 + spinTwo.cat_dim := by
  refine ⟨adjoint_fails_gate, mem_traceless_sym2_adjoint_iff, rfl, spinTwo_cat_dim, ?_⟩
  rw [sym2_dim_twoJ_two]
  rfl

end QOU.Eightfold.Sym2AdjointSpinTwo
