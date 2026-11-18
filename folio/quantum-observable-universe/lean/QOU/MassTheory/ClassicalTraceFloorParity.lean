/-!
# Interface-Parity Generalisation of the Classical Trace Floor

Bean `qou-zrx2` (2026-09-06 follow-up). Companion to
`QOU.MassTheory.ClassicalTraceFloor` and
`computations/probes/classical_floor_derivation_probe.py`.

## Mathematical Statement

For an `A`-nucleon chain braid word on `n = 3A` strands whose `A` intra-nucleon
blocks each have `2` cycles at `q = 1` (`c_free = 2A`), each inter-nucleon
interface `k ∈ {1, …, A-1}` of crossing multiplicity `m_k` reduces to `s_{3k}^{m_k}`
at `q = 1`:
- if `m_k` is **even**, `s_{3k}^{m_k} = 1`, which merges `0` cycles;
- if `m_k` is **odd**, `s_{3k}^{m_k} = s_{3k}`, which bridges two previously
  disjoint nucleon blocks and merges `1` pair of cycles.

Let `O ∈ {0, …, A-1}` be the number of inter-nucleon interfaces of **odd**
crossing multiplicity. Then `c_atom(A, O) = 2A - O`, and the classical (`q = 1`)
Schur–Weyl trace difference is

    c₀(A, O) = 2^{c_free - 3A} - 2^{c_atom - 3A}
             = 2^{-A} - 2^{-(A + O)}
             = 2^{-A} · (1 - 2^{-O}).

Clearing the dyadic denominator `2^{3A}` gives the integer numerator

    N_floor(A, O) := 2^{3A} · c₀(A, O) = 2^{2A} - 2^{2A - O} = 2^{2A - O} · (2^O - 1),

and clearing `2^{A + O}` gives the reduced numerator `M_floor(O) := 2^O - 1`.

In particular:
1. `M_floor(O) = 0 ↔ O = 0`: the classical floor vanishes if and only if every
   inter-nucleon interface has even crossing multiplicity (e.g. `m = 2`, or
   `A = 1` where there are no interfaces).
2. At `O = A - 1` (the canonical `m = 1` chain), `M_floor(A - 1) = 2^{A - 1} - 1`,
   reproducing `0, 1, 3, 7, 15, 31` for `A = 1, 2, 3, 4, 5, 6` and
   `c₀(A) = (2^{A-1} - 1) / 2^{2A - 1} = 0, 1/8, 3/32, 7/128, 15/512, 31/2048`.

-- Ref: [leitner2026] bean qou-zrx2; QOU/MassTheory/ClassicalTraceFloor.lean
-/

namespace QOU.MassTheory

/-- Free-braid cycle count at `q = 1` for `A` uncoupled nucleons: `2A`. -/
def cFreeCount (A : Nat) : Nat := 2 * A

/-- Atom-braid cycle count at `q = 1` with `O` odd-multiplicity inter-nucleon
    interfaces: `2A - O`. -/
def cAtomParityCount (A O : Nat) : Nat := 2 * A - O

/-- Clearing `2^{3A}` from `c₀(A, O) = 2^{2A - 3A} - 2^{(2A - O) - 3A}` gives
    the unreduced dyadic numerator `2^{2A} - 2^{2A - O}`. -/
def unreducedFloorNumerator (A O : Nat) : Nat :=
  2 ^ (2 * A) - 2 ^ (2 * A - O)

/-- Clearing `2^{A + O}` from `c₀(A, O) = 2^{-A}(1 - 2^{-O})` gives the
    reduced dyadic numerator `2^O - 1`. -/
def reducedFloorNumerator (O : Nat) : Nat :=
  2 ^ O - 1

/-- Each odd-multiplicity interface merges one cycle pair:
    `cAtomParityCount A O + O = cFreeCount A` whenever `O ≤ 2A`. -/
theorem cAtomParityCount_add_odd (A O : Nat) (hO : O ≤ 2 * A) :
    cAtomParityCount A O + O = cFreeCount A := by
  unfold cAtomParityCount cFreeCount
  have hsub : 2 * A - O + O = 2 * A := Nat.sub_add_cancel hO
  have hfree : cFreeCount A = 2 * A := rfl
  exact hsub

/-- **Factorisation of the unreduced dyadic numerator.**
    `2^{2A} - 2^{2A - O} = 2^{2A - O} · (2^O - 1)` for `O ≤ 2A`. -/
theorem unreducedFloorNumerator_factor (A O : Nat) (hO : O ≤ 2 * A) :
    unreducedFloorNumerator A O = 2 ^ (2 * A - O) * reducedFloorNumerator O := by
  unfold unreducedFloorNumerator reducedFloorNumerator
  rw [Nat.mul_sub_left_distrib, Nat.mul_one, ← Nat.pow_add]
  have hexp : 2 * A - O + O = 2 * A := by omega
  rw [hexp]

/-- Positive power of two: `1 ≤ 2^O` for all `O : Nat`. -/
theorem one_le_two_pow (O : Nat) : 1 ≤ 2 ^ O := by
  induction O with
  | zero => decide
  | succ k ih =>
    rw [Nat.pow_succ]
    omega

/-- Strict lower bound `2 ≤ 2^O` whenever `1 ≤ O`. -/
theorem two_le_two_pow {O : Nat} (hO : 1 ≤ O) : 2 ≤ 2 ^ O := by
  cases O with
  | zero => omega
  | succ k =>
    rw [Nat.pow_succ]
    have hk : 1 ≤ 2 ^ k := one_le_two_pow k
    omega

/-- **The reduced floor numerator is strictly positive whenever `1 ≤ O`.** -/
theorem reducedFloorNumerator_pos {O : Nat} (hO : 1 ≤ O) :
    0 < reducedFloorNumerator O := by
  unfold reducedFloorNumerator
  have h2 : 2 ≤ 2 ^ O := two_le_two_pow hO
  omega

/-- **Parity vanishing theorem (`qou-zrx2`).**
    The classical trace floor numerator `2^O - 1` vanishes if and only if the
    number of odd-multiplicity inter-nucleon interfaces is `O = 0` (i.e. every
    interface has even crossing multiplicity, or `A = 1`). -/
theorem reducedFloorNumerator_eq_zero_iff (O : Nat) :
    reducedFloorNumerator O = 0 ↔ O = 0 := by
  constructor
  · intro h
    cases O with
    | zero => rfl
    | succ k =>
      have hpos : 0 < reducedFloorNumerator (k + 1) :=
        reducedFloorNumerator_pos (by omega)
      omega
  · intro h
    subst h
    rfl

/-- **The unreduced floor numerator vanishes at `O = 0` for every `A`.** -/
theorem unreducedFloorNumerator_zero_odd (A : Nat) :
    unreducedFloorNumerator A 0 = 0 := by
  have hO : 0 ≤ 2 * A := Nat.zero_le (2 * A)
  rw [unreducedFloorNumerator_factor A 0 hO]
  have hz : reducedFloorNumerator 0 = 0 := (reducedFloorNumerator_eq_zero_iff 0).mpr rfl
  rw [hz, Nat.mul_zero]

/-- **Strict monotonicity in the odd-interface count `O`.** -/
theorem reducedFloorNumerator_lt_succ (O : Nat) :
    reducedFloorNumerator O < reducedFloorNumerator (O + 1) := by
  unfold reducedFloorNumerator
  rw [Nat.pow_succ]
  have h1 : 1 ≤ 2 ^ O := one_le_two_pow O
  omega

/-- **Canonical `m = 1` chain specialisation (`O = A - 1`).**
    At `O = A - 1` for `A = 1..6`, the reduced numerators `2^{A-1} - 1` are
    `0, 1, 3, 7, 15, 31` (matching `c₀(A) = 0, 1/8, 3/32, 7/128, 15/512, 31/2048`). -/
theorem canonical_chain_reduced_numerators :
    reducedFloorNumerator (1 - 1) = 0 ∧
    reducedFloorNumerator (2 - 1) = 1 ∧
    reducedFloorNumerator (3 - 1) = 3 ∧
    reducedFloorNumerator (4 - 1) = 7 ∧
    reducedFloorNumerator (5 - 1) = 15 ∧
    reducedFloorNumerator (6 - 1) = 31 := by
  decide

end QOU.MassTheory
