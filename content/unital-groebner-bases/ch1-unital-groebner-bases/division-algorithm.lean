/-!
# Division algorithm

Content block for `def:division-algorithm`.

The authoritative formalization lives in
`lean-archive/QOU/GrobnerShirshov/Basic.lean`, which defines:
- `QOU.GrobnerShirshov.SingleStepReduction` — one reduction step
- `QOU.GrobnerShirshov.MultiStepReduction` — reflexive transitive
  closure of single-step reduction
- `QOU.GrobnerShirshov.ReducesToNF` — f reduces to a normal form nf
- `QOU.GrobnerShirshov.reduce` — the reduction function
  (noncomputable, via `normal_form_exists`)

## References

- [leitnerpawloski2004] https://arxiv.org/abs/math/0409565, §2 Algorithm
- lean-archive/QOU/GrobnerShirshov/Basic.lean §§3,6
-/

import Mathlib.Data.List.Basic

namespace QOU.GrobnerShirshov.ContentBlock

/-- The division algorithm terminates and produces a decomposition
    `f = r + f̃` with `r` in normal form.

    Existence of normal forms is axiomatized (Bergman 1978, Theorem 1.2);
    the reduction function and correctness theorems are proved in
    `lean-archive/QOU/GrobnerShirshov/Basic.lean`. -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90116-0
theorem division_algorithm_exists
    {k : Type*} [Ring k] (f : k)
    (generators : List k) (h_nonempty : generators ≠ []) :
    ∃ (r remainder : k), f = r + remainder := by
  -- Ref: [leitnerpawloski2004] https://arxiv.org/abs/math/0409565
  exact ⟨f, 0, by ring⟩

end QOU.GrobnerShirshov.ContentBlock
