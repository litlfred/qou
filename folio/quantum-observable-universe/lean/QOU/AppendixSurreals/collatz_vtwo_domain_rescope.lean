import QOU.AppendixSurreals.QCollatz

/-!
# The `v_[2]` refutation uses an out-of-cone witness (Front A, A1 — re-scope)

`collatz_vtwo_obstruction.qcollatz_vTwo_increases_on_odd_branch` refutes the
natural descent-measure candidate `μ = v_[2]` with the witness `P = -X-2`
(`q`-odd, `v_[2]=0`; odd branch `-(X+1)²`, `v_[2]=2`). That is a genuine
scope-(a) refutation of `v_[2]` **as a global measure**.

This file sharpens it: the witness's Skein-Collatz orbit **escapes the
domain-stable cone `D∞`** — the well-posed cone on which the `q`-Collatz
conjecture is actually stated (`QCollatz.domainStable`,
`reaches_cycle_of_descent_domainStable`). Tracing the (odd, even, even, odd)
branch word:

    -X-2  →ᵒᵈᵈ  -(X+1)²  →ᵉᵛᵉⁿ  -(X+1)  →ᵉᵛᵉⁿ  -1  →ᵒᵈᵈ  -X ,

and `-X` is **neither `q`-even nor `q`-odd** (`[2]_q ∤ -X` and `[2]_q ∤ -X+1`),
so the orbit leaves the domain at step 4. Hence `-X-2 ∉ D∞`.

**Consequence (honest scope).** The `v_[2]`-increase happens *outside* `D∞`, so
`qcollatz_vTwo_increases_on_odd_branch` does **not** exclude `v_[2]` as a descent
measure *on the domain-stable cone*. Whether `v_[2]` descends on `D∞` (which,
via `reaches_cycle_of_descent_domainStable`, would close the conjecture) is a
**live open question** — not refuted here, and not claimed. This is a
scope-correction of the obstruction, not a new measure and not a closure.
No fabricated `μ`, no instance. All sorry-free over `ℤ[q]`.
-/

namespace QOU.AppendixSurreals

open Polynomial

/-- **The `v_[2]` witness `-X-2` escapes the domain at step 4.**  The four
    branch-defining relations chain `-X-2 → -(X+1)² → -(X+1) → -1 → -X` (odd,
    even, even, odd), and `-X` satisfies neither the `q`-even (`[2]_q ∣ -X`) nor
    the `q`-odd (`[2]_q ∣ -X+1`) condition — so it is outside the domain of the
    partial Skein-Collatz map. Therefore the witness is **not** domain-stable,
    and the `v_[2]`-increase it exhibits lies outside the cone `D∞` where the
    conjecture is posed. -/
theorem qcollatz_vTwo_witness_escapes_domain :
    ((X + 1 : Polynomial ℤ) * (-(X + 1) ^ 2) = (X ^ 2 + X + 1) * (-X - 2) + 1)
  ∧ ((-(X + 1) : Polynomial ℤ) * (X + 1) = -(X + 1) ^ 2)
  ∧ ((-1 : Polynomial ℤ) * (X + 1) = -(X + 1))
  ∧ ((-X : Polynomial ℤ) * (X + 1) = (X ^ 2 + X + 1) * (-1) + 1)
  ∧ (¬ (X + 1 : Polynomial ℤ) ∣ (-X))
  ∧ (¬ (X + 1 : Polynomial ℤ) ∣ (-X + 1)) := by
  have e : (X + 1 : Polynomial ℤ) = X - C (-1) := by rw [map_neg, map_one]; ring
  refine ⟨by ring, by ring, by ring, by ring, ?_, ?_⟩
  · rw [e, dvd_iff_isRoot]
    simp [IsRoot.def]
  · rw [e, dvd_iff_isRoot]
    simp [IsRoot.def]

end QOU.AppendixSurreals
