import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# QOU.BraidKnot.ColoredJonesRecurrence — the order-(N+1) colored-Jones recurrence

The general form of `KnotOperatorRecurrence` (the twist-knot 2×2 case): a knot operator that
is a power of a fixed braiding element acts on a **finite-dimensional** module — for colored
Jones at colour `N` this module is `(N+1)`-dimensional — so it satisfies a monic degree-`d`
polynomial relation (**Cayley–Hamilton**, `d = N+1`), and its powers therefore obey an
**order-`d` linear recurrence**. Applying the Markov trace / closure (a linear functional)
carries the recurrence to the knot invariants: the resulting recurrence operator is the
**quantum A-polynomial** (the AJ structure).

This file proves the inheritance step in full generality, decoupled from any particular
Cayley–Hamilton coefficient formula: *whatever* monic relation
`M^d = ∑_{k<d} c_k · M^k` the operator satisfies, the power sequence and its trace obey the
same order-`d` recurrence. The `d = 2` instance is `KnotOperatorRecurrence.trace_two_step`
(the twist-knot Jones recurrence); `d = N+1` is colour `N`.

* `pow_recurrence_of_relation` — `M^{n+d} = ∑_{k<d} c_k · M^{n+k}`;
* `trace_recurrence_of_relation` — `tr(M^{n+d}) = ∑_{k<d} c_k · tr(M^{n+k})` (the closure /
  colored-Jones recurrence).

Generic `CommRing` (§7c); the existence of such a relation for a colour-`N` knot operator is
Cayley–Hamilton on its `(N+1)`-dimensional module (cited, not re-proved here). The bar-odd
`Q_β` D-ladder has **no** such finite recurrence — proven non-`q`-holonomic (KC22) — which is
exactly its escape from this machinery (audit
`docs/audits/2026-07-18-knot-operator-gram-recurrence.md`).
-/

namespace QOU.BraidKnot.ColoredJonesRecurrence

open Matrix Finset

variable {R : Type*} [CommRing R] {m : ℕ}

/-- **Power recurrence from a monic relation.** If a knot operator `M` satisfies
`M^d = ∑_{k<d} c_k · M^k` (its degree-`d` Cayley–Hamilton relation), then its powers obey the
order-`d` linear recurrence `M^{n+d} = ∑_{k<d} c_k · M^{n+k}`. -/
theorem pow_recurrence_of_relation {d : ℕ} {M : Matrix (Fin m) (Fin m) R} {c : ℕ → R}
    (h : M ^ d = ∑ k ∈ range d, c k • M ^ k) (n : ℕ) :
    M ^ (n + d) = ∑ k ∈ range d, c k • M ^ (n + k) := by
  have hstep : M ^ (n + d) = M ^ n * M ^ d := by rw [pow_add]
  rw [hstep, h, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k _
  rw [mul_smul_comm, ← pow_add]

/-- **Colored-Jones / closure recurrence.** Applying the (linear) Markov trace — the closure
of the tangle, i.e. the knot invariant — to `pow_recurrence_of_relation` gives the
invariant's order-`d` recurrence: `tr(M^{n+d}) = ∑_{k<d} c_k · tr(M^{n+k})`. The recurrence
operator is the quantum A-polynomial (AJ). -/
theorem trace_recurrence_of_relation {d : ℕ} {M : Matrix (Fin m) (Fin m) R} {c : ℕ → R}
    (h : M ^ d = ∑ k ∈ range d, c k • M ^ k) (n : ℕ) :
    (M ^ (n + d)).trace = ∑ k ∈ range d, c k * (M ^ (n + k)).trace := by
  rw [pow_recurrence_of_relation h n, Matrix.trace_sum]
  apply Finset.sum_congr rfl
  intro k _
  rw [Matrix.trace_smul, smul_eq_mul]

/-- Subtracting the linear combination of lower power traces from the shifted power trace cancels to zero (`qou-gjkv`). -/
theorem trace_recurrence_of_relation_sub_eq_zero {d : ℕ} {M : Matrix (Fin m) (Fin m) R} {c : ℕ → R}
    (h : M ^ d = ∑ k ∈ range d, c k • M ^ k) (n : ℕ) :
    (M ^ (n + d)).trace - ∑ k ∈ range d, c k * (M ^ (n + k)).trace = 0 := by
  rw [trace_recurrence_of_relation h n, sub_self]

end QOU.BraidKnot.ColoredJonesRecurrence
