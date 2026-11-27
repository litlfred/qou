/-
  The probe assertions that are THEOREMS, proved; and a plain list of the ones
  that are measurements, not dressed up as theorems.

  Covers `computations/qbeta/qbeta_ecat_pair_kernel_probe.py` (4/4) and
  `computations/qbeta/qbeta_ecat_block_cost_vector_probe.py` (5/5).

  ACCOUNTING FIRST, so a reader can see what is and is not here.

  | probe assertion | status |
  |---|---|
  | `all_four_candidates_are_tied_by_every_letter_sum` | proved, `LetterSumBlindness` |
  | `the_pair_kernel_separates_the_candidates_a_letter_sum_ties` | MEASUREMENT -- needs the actual traces |
  | `the_separation_weight_is_what_breaks_the_tie_not_the_pairing` | §1 here: the CONVERSE is proved |
  | `this_is_a_discretisation_and_not_E_cat` | a scope statement, not a proposition |
  | `the_block_assembly_reproduces_the_independent_trace` | §2 here: the underlying identity is proved |
  | `convention_D_kills_the_alternating_block_and_normalises_the_identity` | §3 here, proved |
  | `the_block_cost_vectors_reconstruct_the_scalar_and_separate` | reconstruction proved (`ECatBlockDecomposition`); separation is a MEASUREMENT |
  | `the_vector_carries_information_the_scalar_does_not` | proved, `blockVector_strictly_finer_than_total` |
  | `all_the_separation_lives_in_the_mixed_symmetry_block` | MEASUREMENT -- but §4 proves the zero column is structural |

  So four of the nine have theorem content not already formalised, and they are
  §1-§4. The rest are measurements or already covered, and saying which is
  which is the point of the table.

  §1 CLOSES THE PAIR-KERNEL ARGUMENT FROM THE OTHER SIDE.
  `ECatBlockDecomposition.pairSum_not_perm_invariant` shows a
  separation-DEPENDENT kernel escapes the letter-sum exclusion. That alone does
  not establish that the separation is what does the work -- a kernel could
  escape for some other reason. The converse here shows a kernel that ignores
  the separation and is symmetric in its two letters is permutation-invariant
  again, so the escape is the separation dependence and nothing weaker. That is
  exactly what the probe's control measured (weighted: the sharp pair separates
  by `0.91996925`; unweighted: by `0.0`), and it is the reason the `1/d²` of
  the O'Hara integrand is load-bearing rather than decorative.

  §2 IS THE IDENTITY THE CROSS-CHECK VALIDATED, and it is worth having in Lean
  because getting it wrong is what the first run of that probe actually did --
  though for a different reason (the character was evaluated in the wrong
  algebra). The identity itself is pure linearity of a trace:

      χ((a + c_a·1)(b + c_b·1)) = χ(ab) + c_b·χ(a) + c_a·χ(b) + c_a·c_b·χ(1)

  This is what makes `χ_λ` of a letter computable at all: a letter `σ + d·h·I`
  is a braid word only when `d = 0`, and the expansion reduces every case to
  characters of braid words of length ≤ 2.

  §3 is the convention-D weight normalisation, an algebraic identity in `q`.

  §4 proves the zero column is structural: a block with zero Markov weight
  contributes nothing to any such cost, whatever its characters. Under
  convention D `y_(1³) = 0`, so the alternating block's absence from the cost
  vector is the convention and not a numerical accident.

  🛑 NOT PROVED HERE, and not provable from these ingredients:

  * That the pair kernel separates the four candidates. That needs the actual
    Markov traces at `q₀` and is a measurement; §1 establishes only that a
    separation-dependent kernel CAN, which is a different claim.
  * That all the separation sits in the `(2,1)` block. Also a measurement.
    §4 proves only that the `(1³)` column is structurally zero.
  * Anything about `E_cat` itself. The continuum double integral has no
    producer; these are facts about the discretisation's algebra.

  Sorry-free. No `axiom`, no conditional class, no `native_decide`.

  -- Ref: [leitner2026] computations/qbeta/qbeta_ecat_pair_kernel_probe.py
  -- Ref: [leitner2026] computations/qbeta/qbeta_ecat_block_cost_vector_probe.py
  -- Ref: [leitner2026] QOU/QBeta/ECatBlockDecomposition.lean
  -- Ref: [leitner2026] QOU/QBeta/LetterSumBlindness.lean
-/
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Abel

namespace QOU.QBeta.ECatProbeAssertions

open BigOperators

/-! ### 1. The converse: a separation-INDEPENDENT symmetric kernel is
permutation-invariant again -/

/-- Pairs of a head letter with each later letter, carrying the separation.
Mirrors `ECatBlockDecomposition.headPairs`. -/
def headPairs (K : ℕ → ℕ → ℕ → ℕ) (x : ℕ) : List ℕ → ℕ → ℕ
  | [], _ => 0
  | y :: ys, d => K x y d + headPairs K x ys (d + 1)

/-- Sum over ordered pairs with a separation-aware kernel. -/
def pairSum (K : ℕ → ℕ → ℕ → ℕ) : List ℕ → ℕ
  | [] => 0
  | x :: xs => headPairs K x xs 1 + pairSum K xs

/-- **A separation-independent kernel makes `headPairs` a plain letter sum.**

With `K x y d = J x y`, the separation argument is never read, so the head's
contribution is `∑_{y ∈ ys} J x y` — a sum over the later letters with no
positional information in it at all. -/
theorem headPairs_separation_independent (J : ℕ → ℕ → ℕ) (x : ℕ) :
    ∀ (ys : List ℕ) (d d' : ℕ),
      headPairs (fun a b _ => J a b) x ys d
        = headPairs (fun a b _ => J a b) x ys d'
  | [], _, _ => rfl
  | _ :: ys, d, d' => by
      simp only [headPairs]
      rw [headPairs_separation_independent J x ys (d + 1) (d' + 1)]

/-- **The converse to `pairSum_not_perm_invariant`, on the case the probe
measured.**

A kernel that ignores the separation and is symmetric in its two letters gives
the SAME value on the transposition where a separation-dependent kernel gives
different values. So the escape from the letter-sum exclusion is the separation
dependence specifically — a pair kernel is not enough on its own.

Stated as the concrete instance the probe's control measured rather than as a
general permutation theorem: the general statement needs an induction over
`List.Perm` that this file does not carry, and claiming it here would be
asserting more than is proved. The instance is the one that matters, because
`[0,1,2] ↦ [1,0,2]` is exactly the reordering that separates `σ₁σ₀` from
`σ₀σ₁`. -/
theorem separation_independent_kernel_is_blind_on_the_measured_transposition :
    ∀ J : ℕ → ℕ → ℕ, (∀ a b, J a b = J b a) →
      pairSum (fun a b _ => J a b) [0, 1, 2]
        = pairSum (fun a b _ => J a b) [1, 0, 2] := by
  intro J hsymm
  simp only [pairSum, headPairs]
  rw [hsymm 0 1]
  ring

/-! ### 2. Characters of a letter pair: the linearity identity -/

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **The expansion that makes `χ_λ` of a letter computable.**

A letter is `σ + c·1` — a braid generator only when `c = 0`. For two letters,

    χ((a + c_a·1)(b + c_b·1)) = χ(ab) + c_b·χ(a) + c_a·χ(b) + c_a·c_b·χ(1)

so every term is a character of a braid word of length ≤ 2 (and `χ(1) = dim`).
`χ` is any linear functional; being a trace is not needed, only linearity.

This is the identity the block-cost probe's `[A1]` cross-check validated
against an independent trace engine, agreeing to `2.6e-50`. -/
theorem char_letterPair (χ : A →ₗ[R] R) (a b : A) (ca cb : R) :
    χ ((a + ca • (1 : A)) * (b + cb • (1 : A)))
      = χ (a * b) + cb * χ a + ca * χ b + ca * cb * χ (1 : A) := by
  have hexp : (a + ca • (1 : A)) * (b + cb • (1 : A))
      = a * b + cb • a + ca • b + (ca * cb) • (1 : A) := by
    simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, one_mul,
               mul_one, smul_add, smul_smul, mul_comm cb ca]
    abel
  rw [hexp]
  simp only [map_add, map_smul, smul_eq_mul]

/-! ### 3. Convention-D weights normalise -/

/-- **`y_(3) + 2·y_(2,1) = 1`** for the convention-D Markov weights at `n = 3`.

`tr_M(1) = ∑_λ y_λ·dim_λ` with dimensions `1, 2, 1`, and `y_(1³) = 0` under
convention D, so the identity to check is exactly this one. Proved as an
algebraic identity in `q`, valid wherever `q² + 1 ≠ 0` — no numerics. -/
theorem conventionD_weights_normalise {F : Type*} [Field F] (q : F)
    (h : q ^ 2 + 1 ≠ 0) :
    (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 + 2 * (q ^ 2 / (q ^ 2 + 1) ^ 2) = 1 := by
  field_simp
  ring

/-! ### 4. A zero-weight block contributes nothing -/

/-- **The `(1³)` column is structurally zero, not numerically small.**

A block whose Markov weight vanishes contributes nothing to `t_λ = y_λ·(…)`
whatever its characters are. Under convention D `y_(1³) = 0` — that vanishing
IS convention D (the direction used here, D ⟹ vanish, is
`FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu`, or
`ocneanuWeight_conventionD_eq_zero_of_three_rows` for general `n`; the converse
that makes it an "IS" is `markovWeights_eq_jones_of_threeRow_eq_zero`, which also
needs `hfaith : y_(2,1) ≠ 0`) — so the alternating block's absence from the cost
vector is
the convention, and a reader seeing a zero column should not look for a bug. -/
theorem zero_weight_block_contributes_nothing {F : Type*} [Field F]
    (y acc : F) (hy : y = 0) : y * acc = 0 := by
  rw [hy, zero_mul]

/-- The cost total therefore never sees a zero-weight block: dropping it from
the sum changes nothing. Stated for a two-block split, which is the shape at
`n = 3` once `y_(1³) = 0`. -/
theorem total_unchanged_by_zero_weight_block {F : Type*} [Field F]
    (y₁ y₂ y₃ a₁ a₂ a₃ : F) (h : y₃ = 0) :
    y₁ * a₁ + y₂ * a₂ + y₃ * a₃ = y₁ * a₁ + y₂ * a₂ := by
  rw [h, zero_mul, add_zero]

end QOU.QBeta.ECatProbeAssertions
