import Mathlib.Algebra.Polynomial.Basic

/-!
# QOU.Archimedean.lepton_continuant_recurrence — Morgan–Voyce continuant NF

**Proposition** ([`prop:lepton-continuant-recurrence`](../../../quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md)).

*Let `h = q − q⁻¹` be the Hecke parameter and `T_{2,n} = σ₀ⁿ` the
`(2, n)`-torus knot braid in `B₂`.  Its Gröbner–Shirshov normal
form in `H₂(q)` is `NF(σ₀ⁿ) = a_n · 1 + b_n · σ₀`, where the
sequences `{a_n}` and `{b_n}` satisfy the Morgan–Voyce continuant
recurrence*

```
  a_{n+1} = b_n
  b_{n+1} = h · b_n + b_{n-1}
  b_0     = 0
  b_1     = 1
```

*The net coefficient is `net(T_{2,n}) = a_n + b_n`.*

The recurrence is encoded below over `Polynomial ℤ` with the
indeterminate `X` playing the role of the Hecke parameter
`h = q − q⁻¹` (identical convention to the Chebyshev-degree sibling
lemma `chebyshev_degree_genus`).  The statement records the
recurrence itself; downstream specialisation to specific
`n ∈ {3, 5, 7}` recovers the `e⁻/μ⁻/τ⁻` lepton-tower NF entries.

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
-/

namespace QOU.Archimedean

open Polynomial

/-- The Morgan–Voyce continuant `b_n` defined by
    `b_0 = 0`, `b_1 = 1`, `b_{n+2} = X · b_{n+1} + b_n`
    over `Polynomial ℤ`.  The coefficient symbol `X` plays the role
    of the Hecke parameter `h = q − q⁻¹`. -/
noncomputable def morganVoyceB : ℕ → Polynomial ℤ
  | 0       => 0
  | 1       => 1
  | (n + 2) => Polynomial.X * morganVoyceB (n + 1) + morganVoyceB n

/-- The companion sequence `a_n = b_{n-1}` (with `a_0 = 0`), so that
    the NF decomposition `σ₀ⁿ = a_n + b_n · σ₀` holds. -/
noncomputable def morganVoyceA : ℕ → Polynomial ℤ
  | 0       => 0
  | (n + 1) => morganVoyceB n

/-- The "net coefficient" of `T_{2,n} = σ₀ⁿ` is `a_n + b_n`. -/
noncomputable def netCoeff (n : ℕ) : Polynomial ℤ :=
  morganVoyceA n + morganVoyceB n

/-- **Recurrence identity** for `b_n` ([`prop:lepton-continuant-recurrence`]).

    Holds by definition: this is the second equation of the Morgan–
    Voyce recurrence packaged as a Lean theorem so downstream
    consumers can `rw` against it. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceB_recurrence (n : ℕ) :
    morganVoyceB (n + 2) = Polynomial.X * morganVoyceB (n + 1) + morganVoyceB n := by
  rfl

/-- **a_n = b_{n−1}** identity, packaging the first equation of the
    Morgan–Voyce recurrence. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem morganVoyceA_succ (n : ℕ) : morganVoyceA (n + 1) = morganVoyceB n := by
  rfl

/-- **Net-coefficient identity**: `net_{n+1} = b_n + b_{n+1}`.

    Discharged by unfolding `netCoeff`, `morganVoyceA`, and applying
    `morganVoyceA_succ`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem netCoeff_succ (n : ℕ) :
    netCoeff (n + 1) = morganVoyceB n + morganVoyceB (n + 1) := by
  simp [netCoeff, morganVoyceA, morganVoyceA_succ]

/-- **Lepton continuant recurrence theorem.** Bundles the Morgan–
    Voyce recurrence into a single conjunction: for every `n`, the
    sequences `a_n` and `b_n` jointly satisfy the four characterising
    relations of `prop:lepton-continuant-recurrence`. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/lepton-continuant-recurrence.md
theorem lepton_continuant_recurrence (n : ℕ) :
    morganVoyceA (n + 1) = morganVoyceB n ∧
    morganVoyceB (n + 2)
      = Polynomial.X * morganVoyceB (n + 1) + morganVoyceB n ∧
    morganVoyceB 0 = 0 ∧
    morganVoyceB 1 = 1 := by
  refine ⟨morganVoyceA_succ n, morganVoyceB_recurrence n, ?_, ?_⟩ <;> rfl

end QOU.Archimedean
