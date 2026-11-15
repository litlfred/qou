import Mathlib.Algebra.GeomSum
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.MathlibExt.QIntegerFactorial — quantum integers, q-factorial, genericity

Mathlib has Coxeter groups and `IsSemisimpleRing` but **no quantum
integers** and **no Iwahori–Hecke algebra**.  This file supplies the
first infrastructure brick of the Hecke-semisimplicity attack (bean
`qou-6566`, epic `qou-hnhg`): the quantum integer `[n]_q`, the quantum
factorial `[n]_q!` (the Poincaré polynomial of `H_n(q)`), and the
**genericity equivalence**

  `[n]_q! ≠ 0  ⟺  q` is not a `k`-th root of unity for any `2 ≤ k ≤ n`,

for `q ≠ 1` over a field.  This is exactly the *parameter-side*
condition of Wenzl's semisimplicity criterion
([`WenzlSchurElement.WenzlGeneric`](WenzlSchurElement.lean),
[`wenzl1988`]): `H_n(q)` is semisimple iff `[n]_q! ≠ 0`.  The **hard**
half — `[n]_q! ≠ 0 ⟹ H_n(q)` semisimple — needs the Hecke algebra +
Gram/Schur machinery (beans `qou-phir`/`qou-0y6h`/`qou-q5bp`); this
brick discharges the arithmetic side, sorry-free, over a generic field
(§7c: no archimedean input until the real `1 < q` corollary).
-/

namespace QOU.MathlibExt

open Finset

section Field

variable {K : Type*} [Field K]

/-- The **quantum integer** `[n]_q = 1 + q + ⋯ + q^{n-1} = ∑_{i<n} q^i`. -/
def qInt (q : K) (n : ℕ) : K := ∑ i ∈ range n, q ^ i

/-- **Bridge to the canonical geometric bracket.**

`qInt` is kept rather than aliased: `qInt_eq_div` below does
`rw [qInt, geom_sum_eq hq]`, which needs the `Finset.sum` to be the literal
body. The two are definitionally the same object, so the consolidation here is
this equation — checked, not asserted. -/
theorem qInt_eq_canonical (q : K) (n : ℕ) : qInt q n = QOU.QInteger.qIntGeo q n := rfl

@[simp] theorem qInt_zero (q : K) : qInt q 0 = 0 := by simp [qInt]

@[simp] theorem qInt_one (q : K) : qInt q 1 = 1 := by simp [qInt]

/-- Closed form `[n]_q = (q^n - 1)/(q - 1)` for `q ≠ 1`. -/
theorem qInt_eq_div {q : K} (hq : q ≠ 1) (n : ℕ) :
    qInt q n = (q ^ n - 1) / (q - 1) := by
  rw [qInt, geom_sum_eq hq]

/-- **Vanishing of a quantum integer.**  For `q ≠ 1`,
    `[k]_q = 0 ⟺ q^k = 1` — i.e. `q` is a `k`-th root of unity. -/
theorem qInt_eq_zero_iff {q : K} (hq : q ≠ 1) (k : ℕ) :
    qInt q k = 0 ↔ q ^ k = 1 := by
  rw [qInt_eq_div hq, div_eq_zero_iff, sub_eq_zero, sub_eq_zero]
  constructor
  · rintro (h | h)
    · exact h
    · exact absurd h hq
  · intro h; exact Or.inl h

/-- **Quantum-integer recursion** `[n+1]_q = [n]_q + q^n` (sorry-free). -/
theorem qInt_succ (q : K) (n : ℕ) : qInt q (n + 1) = qInt q n + q ^ n := by
  rw [qInt, qInt, Finset.sum_range_succ]

/-- The **quantum factorial** `[n]_q! = ∏_{k=1}^{n} [k]_q` — the Poincaré
    polynomial of the Iwahori–Hecke algebra `H_n(q)`. -/
def qFactorial (q : K) (n : ℕ) : K := ∏ k ∈ range n, qInt q (k + 1)

@[simp] theorem qFactorial_zero (q : K) : qFactorial q 0 = 1 := by
  simp [qFactorial]

@[simp] theorem qFactorial_one (q : K) : qFactorial q 1 = 1 := by
  simp [qFactorial]

/-- **Quantum-factorial recursion** `[n+1]_q! = [n]_q! · [n+1]_q`
    (sorry-free) — the induction step for Schur-element / Gram
    computations over `H_n(q)`. -/
theorem qFactorial_succ (q : K) (n : ℕ) :
    qFactorial q (n + 1) = qFactorial q n * qInt q (n + 1) := by
  rw [qFactorial, qFactorial, Finset.prod_range_succ]

/-- **Parameter genericity** (field form of `WenzlSchurElement.WenzlGeneric`):
    `q` is not a `k`-th root of unity for any `2 ≤ k ≤ n`. -/
def QGeneric (q : K) (n : ℕ) : Prop := ∀ k, 2 ≤ k → k ≤ n → q ^ k ≠ 1

/-- **The genericity equivalence (sorry-free).**  For `q ≠ 1` over a
    field, the quantum factorial is nonzero iff `q` is generic at rank
    `n`:

      `[n]_q! ≠ 0  ⟺  ∀ k ∈ [2, n], q^k ≠ 1`.

    This is the arithmetic (parameter) half of Wenzl's semisimplicity
    criterion for `H_n(q)`. -/
theorem qFactorial_ne_zero_iff {q : K} (hq : q ≠ 1) (n : ℕ) :
    qFactorial q n ≠ 0 ↔ QGeneric q n := by
  rw [qFactorial, Finset.prod_ne_zero_iff]
  constructor
  · intro h k hk2 hkn
    have hmem : k - 1 ∈ range n := by rw [mem_range]; omega
    have hk := h (k - 1) hmem
    rw [show k - 1 + 1 = k by omega, ne_eq, qInt_eq_zero_iff hq] at hk
    exact hk
  · intro hgen j hj
    rw [mem_range] at hj
    rw [ne_eq, qInt_eq_zero_iff hq]
    rcases Nat.eq_zero_or_pos j with hj0 | hjpos
    · subst hj0; simpa using hq
    · exact hgen (j + 1) (by omega) (by omega)

end Field

section Real

/-- **Quantum integers are positive for `q > 0` (sorry-free).**  `[n]_q`
    is a sum of positive powers, hence strictly positive for `n ≥ 1`. -/
theorem qInt_pos {q : ℝ} (hq : 0 < q) {n : ℕ} (hn : 0 < n) : 0 < qInt q n := by
  rw [qInt]
  apply Finset.sum_pos
  · intro i _; exact pow_pos hq i
  · exact ⟨0, mem_range.mpr hn⟩

/-- **The quantum factorial is positive for `q > 0` (sorry-free).**  A
    product of positive quantum integers.  In particular it is nonzero,
    strengthening the genericity fact in the archimedean substrate
    regime. -/
theorem qFactorial_pos {q : ℝ} (hq : 0 < q) (n : ℕ) : 0 < qFactorial q n := by
  rw [qFactorial]
  apply Finset.prod_pos
  intro k _
  exact qInt_pos hq (Nat.succ_pos k)

/-- **The real substrate is generic at every rank (sorry-free).**  Any
    real `q > 1` — in particular the substrate `q₀ ≈ 1.10998` — has
    `[n]_q! ≠ 0` for every `n` (indeed `> 0` by `qFactorial_pos`): no
    quantum integer vanishes, so the parameter-side hypothesis of
    Wenzl's criterion is discharged.  Bridges to
    `WenzlSchurElement.wenzlGeneric_of_one_lt`. -/
theorem qFactorial_ne_zero_of_one_lt {q : ℝ} (hq : 1 < q) (n : ℕ) :
    qFactorial q n ≠ 0 :=
  ne_of_gt (qFactorial_pos (lt_trans one_pos hq) n)

/-- **Genericity from positivity (sorry-free).**  For real `q > 1`, the
    parameter genericity `QGeneric q n` holds — the form Wenzl's
    criterion consumes — recovered here from the quantum-factorial
    route (`qFactorial_ne_zero_of_one_lt` + `qFactorial_ne_zero_iff`),
    agreeing with the direct order-arithmetic proof in
    `WenzlSchurElement`. -/
theorem qGeneric_of_one_lt {q : ℝ} (hq : 1 < q) (n : ℕ) : QGeneric q n :=
  (qFactorial_ne_zero_iff hq.ne' n).mp (qFactorial_ne_zero_of_one_lt hq n)

end Real

end QOU.MathlibExt
