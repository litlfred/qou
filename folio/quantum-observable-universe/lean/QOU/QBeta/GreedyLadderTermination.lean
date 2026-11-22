/-
# QOU.QBeta.GreedyLadderTermination — the Q_β `c_k` extraction terminates at
# its first extracted rung, identically.

`computations/qbeta/qbeta_ck_cache.py` extracts the ladder coefficients
recursively:

    for k in range(3, 8):
        ratio_m1 = Q_codata / Q_prev - 1
        if abs(ratio_m1) < EPS_RESIDUAL: break
        ck_extracted = ratio_m1 / u ** k
        Q_next = Q_prev * (1 + ck_extracted * u ** k)

Observed at runtime (proton anchor, convention D):

    c_3 (extracted) =   -974.4318877
    c_4: residual below compute precision (0.00e+00) — ladder converged

The residual at the next rung is not *small*, it is **exactly zero**, and the
theorems below say why: the extracted rung is defined by inverting the target,
so applying it reproduces the target identically. `c_4 … c_7` are therefore
never computed at all — the guard fires — and the `structural_candidates`
entries for `k ≥ 4` in that producer are unreachable.

**What this does and does not say.** It is a statement about the *extraction
procedure*, not about physics: a greedy one-step inversion is exact by
construction. It gives no support to any value of `c_3`, and it is not
evidence that the ladder converges. On the contrary — it says the ladder
cannot have more than one extracted rung, so "truncation order chosen by
target precision" does not describe this producer.

Base ring: a generic `Field`, per §7c. The claim is pure algebra — no
ordering, no `Real.sqrt`, no archimedean content — so it is stated over
`{R : Type*} [Field R]` and specialises to `ℝ` for free.

-- Ref: [leitner2026] `computations/qbeta/qbeta_ck_cache.py`, extraction loop;
-- bean `qou-cwin` T0.5; PR #5235.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

variable {R : Type*} [Field R]

/-- **The extracted rung reproduces the target exactly.**

`rung` is the coefficient the producer extracts at scale `x` (there `x = uᵏ`):
it is *defined* as the relative shortfall divided by `x`. Applying it to
`Qprev` therefore lands on `Qtarget` identically, for every nonzero `Qprev`
and `x`.

This is the algebraic content of the runtime line
`c_4: residual below compute precision (0.00e+00)`. -/
theorem greedy_rung_exact (Qtarget Qprev x : R) (hQ : Qprev ≠ 0) (hx : x ≠ 0) :
    Qprev * (1 + ((Qtarget / Qprev - 1) / x) * x) = Qtarget := by
  field_simp
  ring

/-- **The residual after the extracted rung is exactly zero.**

Consequently the producer's `abs(ratio_m1) < EPS_RESIDUAL` guard fires at the
very next `k`, whatever `EPS_RESIDUAL` is — the ladder stops after one
extracted rung, not because it converged but because it was solved. -/
theorem greedy_next_residual_zero
    (Qtarget Qprev x : R) (hQ : Qprev ≠ 0) (hx : x ≠ 0) (hT : Qtarget ≠ 0) :
    Qtarget / (Qprev * (1 + ((Qtarget / Qprev - 1) / x) * x)) - 1 = 0 := by
  rw [greedy_rung_exact Qtarget Qprev x hQ hx, div_self hT, sub_self]

/-- **Any further extracted rung is zero.**

Whatever scale `y` a later rung is extracted at, its coefficient is the
residual over `y`, and the residual is zero — so every rung beyond the first
extracted one vanishes identically. `c_4 … c_7` carry no information; they are
not small, they are `0`. -/
theorem greedy_later_rungs_vanish
    (Qtarget Qprev x y : R) (hQ : Qprev ≠ 0) (hx : x ≠ 0) (hT : Qtarget ≠ 0) :
    (Qtarget / (Qprev * (1 + ((Qtarget / Qprev - 1) / x) * x)) - 1) / y = 0 := by
  rw [greedy_next_residual_zero Qtarget Qprev x hQ hx hT, zero_div]

/-- **The one-rung model is an exact interpolant, not an approximation.**

Stated without reference to the extraction: for any `Qbase` and any nonzero
scale, there is a coefficient making the model hit the target exactly. So
"the ladder reproduces CODATA" is a property of having one free coefficient,
carrying no information about the model that coefficient multiplies. -/
theorem exists_rung_hitting_target (Qtarget Qbase x : R) (hQ : Qbase ≠ 0)
    (hx : x ≠ 0) : ∃ c : R, Qbase * (1 + c * x) = Qtarget :=
  ⟨(Qtarget / Qbase - 1) / x, greedy_rung_exact Qtarget Qbase x hQ hx⟩

end QOU.QBeta
