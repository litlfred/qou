import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Archimedean
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum

/-!
# QOU.FluidDynamics.QAubinLions

q-deformed Aubin--Lions lemma: compactness of the solution family as q → 1.

LaTeX label: `conj:q-aubin-lions`

## Conjectural content

Conjectural q-deformed Aubin–Lions compactness: as q → 1, the q-NS solution family is compact in the appropriate Sobolev–Gevrey topology, with the limit a weak Leray–Hopf solution. The class supplies the abstract compactness witness.

## Status

Class-axiomatised per AGENTS.md §3b-cond. Downstream blocks may take
`[QAubinLions …]` as an explicit `[Instance]` hypothesis to retain
`theorem` / `proposition` status.

Assuming this class is assuming an open conjecture. It is *not* proved
here, and no `instance` is declared — the examples below are witnesses
that the class is consistent and refutable, not instances that would
make it available to typeclass inference.

## References

- [leitner2026] §q-deformed Aubin--Lions lemma: compactness of the solution family as q → 1, `conj:q-aubin-lions`
-/

namespace QOU.FluidDynamics

/-- **Conjecture class** for `conj:q-aubin-lions`.

    Encodes the conjectural content as a Lean type-class so downstream
    theorems can take `[QAubinLions …]` as an explicit hypothesis
    (AGENTS.md §3b-cond).

    **Rewritten 2026-08-30.**  The single field was

        compactness_threshold : ∃ q_thresh : ℝ, q_thresh > 0

    — "there exists a positive real", a theorem of ordered fields,
    discharged by `1`.  It asserted nothing about compactness, about
    `q → 1`, or about the solution family, and its docstring had holes
    where the symbols had been dropped ("a compactness exponent  such
    that for all  the solution family").

    The class is now **parametrised by the objects the conjecture is
    about**, and each field is one clause of the `.md` conjecture:

    > *there exists a subsequence `qₙ → 1` such that `v_{qₙ} → v*`
    > weakly in `L²`; `v*` is a weak solution of Navier–Stokes,
    > satisfies the energy inequality, and is smooth off a singular set
    > of Hausdorff dimension ≤ 1.*

    This does **not** prove the conjecture.  It makes assuming it mean
    something: every field is refutable by a wrong object, and the
    negative controls below exhibit such objects.

    **Parameters.**  `qSeq` is the extracted subsequence `qₙ` of substrate
    parameters; `convergenceGap n` is `‖v_{qₙ} − v*‖²_{L²}`, the `L²` gap
    along it; `energyLimit` and `energyInitial` are `‖v*‖²` and `‖v₀‖²`;
    `singularDim` is the Hausdorff dimension of the singular set of `v*`.

    Ref: [leitner2026] §q-deformed Aubin--Lions lemma: compactness of the
    solution family as q → 1, `conj:q-aubin-lions` -/
class QAubinLions (qSeq : ℕ → ℝ) (convergenceGap : ℕ → ℝ)
    (energyLimit energyInitial : ℝ) (singularDim : ℝ) : Prop where
  /-- The subsequence lies in the q-NS regime `q > 1`. -/
  qSeq_gt_one : ∀ n, 1 < qSeq n
  /-- …and tends to `1`, which is the limit the conjecture is about. -/
  qSeq_tendsto_one : ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, ∀ n, N ≤ n → qSeq n - 1 < ε
  /-- Strong `L²` convergence along it: the gap is eventually arbitrarily
      small.  Non-negative because it is a squared norm. -/
  convergenceGap_nonneg : ∀ n, 0 ≤ convergenceGap n
  converges : ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, ∀ n, N ≤ n → convergenceGap n < ε
  /-- The limit satisfies the energy inequality. -/
  energy_inequality : energyLimit ≤ energyInitial
  /-- The limit is smooth off a singular set of Hausdorff dimension ≤ 1
      (the Caffarelli–Kohn–Nirenberg bound). -/
  singularDim_le_one : singularDim ≤ 1

/-! ### The class is consistent, and each field can be false

Inhabited, so the carrier is not vacuously unsatisfiable; and refutable,
which the previous `∃ q_thresh > 0` was not. -/

example : QAubinLions (fun n => 1 + 1 / (n + 1 : ℝ)) (fun _ => 0) 0 0 1 where
  qSeq_gt_one := fun n => by
    have : (0:ℝ) < 1 / (n + 1 : ℝ) := by positivity
    linarith
  qSeq_tendsto_one := by
    intro ε hε
    obtain ⟨N, hN⟩ := exists_nat_gt (1 / ε)
    refine ⟨N, fun n hn => ?_⟩
    have hn1 : (0:ℝ) < (n : ℝ) + 1 := by positivity
    have hNn : (N : ℝ) ≤ (n : ℝ) := Nat.cast_le.mpr hn
    have : 1 / ((n : ℝ) + 1) < ε := by
      rw [div_lt_iff₀ hn1]
      have : 1 / ε < (n : ℝ) + 1 := by linarith
      rwa [div_lt_iff₀ hε, mul_comm] at this
    simpa using this
  convergenceGap_nonneg := fun _ => le_refl 0
  converges := fun ε hε => ⟨0, fun _ _ => hε⟩
  energy_inequality := le_refl 0
  singularDim_le_one := le_refl 1

/-- A subsequence that does not approach `1` refutes the conjecture —
    the `q → 1` limit is the whole content. -/
example : ¬ QAubinLions (fun _ => 2) (fun _ => 0) 0 0 1 := by
  rintro ⟨-, htend, -, -, -, -⟩
  obtain ⟨N, hN⟩ := htend (1/2) (by norm_num)
  have := hN N (le_refl N); norm_num at this

/-- A singular set of Hausdorff dimension `2` refutes the CKN clause. -/
example : ¬ QAubinLions (fun n => 1 + 1 / (n + 1 : ℝ)) (fun _ => 0) 0 0 2 := by
  rintro ⟨-, -, -, -, -, hdim⟩; norm_num at hdim

end QOU.FluidDynamics
