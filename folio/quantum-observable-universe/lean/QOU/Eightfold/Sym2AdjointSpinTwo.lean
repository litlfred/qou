import QOU.Eightfold.Sym2GateParity
import QOU.QuantumObservableUniverse.Structures

/-!
# QOU.Eightfold.Sym2AdjointSpinTwo — `V₂ = Sym²(V₁) ⊖ V₀` for the gauge `SU(2)`

For the gauge group `G = Aut^⊗(τ) ≅ SU(2)`, Clebsch–Gordan gives

  `Sym²(V₁) = V₀ ⊕ V₂`      (dims `1 + 5 = 6 = 3·4/2`),

for the adjoint `V₁ = Ad(A)`, where `V₀` is the trace part and `V₂` is the
traceless part.

**What is and is not formalised.** The decomposition itself is *not* proved
here. It enters through the index model `Sym2GateParity.sym2Indices`, a
definition (`k ≤ 2j` with `k ≡ 2j mod 2`) that encodes the Clebsch–Gordan
answer and is cited, not derived. What this file proves is the bookkeeping on
that model: for `2j = 2` the index set is `{0, 2}`, removing the singlet leaves
`{2}`, the remaining index carries the `SpinLabels` label `twice_j = 4`, and the
dimensions add up to `6`. These are finite checks; they would fail if the index
model, the label convention or the dimension rule were changed.

**What is reused, not re-derived.**

* `Sym2GateParity.sym2Indices` — the Clebsch–Gordan/parity description of the
  summands `V_k` of `Sym²(V_j)` (index `k` is the spin, `dim V_k = 2k + 1`);
* `Sym2GateParity.adjoint_fails_gate` — the singlet `k = 0` *is* in
  `Sym²(V₁)` (this is the trace summand that `⊖ V₀` removes);
* `Sym2GateParity.sym2_dim_twoJ_two` — `dim Sym²(V₁) = 6`;
* `QOU.SpinLabels` / `QOU.adjoint_dim` — the `twice_j` convention, under which
  the adjoint is `twice_j = 2` (`adjoint_is_one` of `prop:spin-labels`) and the
  new label is `twice_j = 4` (the spin-`2` row of `ex:spin-labels-su2`).

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

/-- **Removing the trace leaves exactly spin `2`.** In the index model, the
traceless part `Sym²(V₁) ⊖ V₀` — the summands of `Sym²(V₁)` other than the
singlet — is the single index `k = 2`. -/
theorem traceless_sym2_adjoint_eq : (sym2Indices 2).erase 0 = {2} := by
  ext k
  rw [Finset.mem_erase, mem_sym2Indices_adjoint, Finset.mem_singleton]
  omega

/-- **Uniqueness by dimension.** Among the summands of `Sym²(V₁)`, the only one
of dimension `5` is `k = 2`; the other (the singlet) has dimension `1`. -/
theorem sym2_adjoint_dim_five_iff (k : ℕ) (hk : k ∈ sym2Indices 2) :
    2 * k + 1 = 5 ↔ k = 2 := by
  rcases (mem_sym2Indices_adjoint k).1 hk with rfl | rfl <;> decide

/-- **Theorem (`V₂ = Sym²(V₁) ⊖ V₀`, index model).** For the gauge `SU(2)`, in
the Clebsch–Gordan index model `sym2Indices` of `Sym2GateParity`:

1. the singlet index `0` occurs in `Sym²(V₁)` (`adjoint_fails_gate`);
2. removing it leaves exactly the index `k = 2`;
3. the `SpinLabels` label of every remaining summand, `twice_j = 2k`, is
   `spinTwo` (`twice_j = 4`, `cat_dim = 5`);
4. the dimensions close: `dim Sym²(V₁) = 6 = 1 + dim V₂`.

The decomposition `Sym²(V₁) ≅ V₀ ⊕ V₂` is not proved here; it is encoded in
`sym2Indices` and cited. This is a statement about the gauge group
`Aut^⊗(τ)` only. -/
theorem adjoint_sym2_traceless_is_spin_two :
    0 ∈ sym2Indices 2 ∧
    (sym2Indices 2).erase 0 = {2} ∧
    (∀ k ∈ (sym2Indices 2).erase 0, ({ twice_j := 2 * k } : QOU.SpinLabels) = spinTwo) ∧
    (sym2Indices 2).sum (fun k => 2 * k + 1) = 1 + spinTwo.cat_dim := by
  refine ⟨adjoint_fails_gate, traceless_sym2_adjoint_eq, ?_, ?_⟩
  · intro k hk
    rw [traceless_sym2_adjoint_eq, Finset.mem_singleton] at hk
    subst hk
    rfl
  · rw [sym2_dim_twoJ_two]
    rfl

end QOU.Eightfold.Sym2AdjointSpinTwo
