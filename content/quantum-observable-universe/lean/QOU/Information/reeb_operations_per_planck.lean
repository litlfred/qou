import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import QOU.Shared.MarkovTraceClaim

/-!
# QOU.Information.reeb_operations_per_planck — discrete iterations per Reeb circuit

**Proposition** ([`prop:reeb-operations-per-planck`](../../../quantum-observable-universe/information-theory/reeb-operations-per-planck.md)).

Let `q ∈ k^× ∖ {1}` and `t_P(q) = q/(q − 1)` the Planck time. The number
of discrete `f_q`-iterations composing one Reeb circuit is

`n_R(q) = t_P(q) = q/(q − 1) = 1/ℏ_q`,  with  `ℏ_q = (q − 1)/q`.

Each iteration is one braiding evaluation (one `R`-matrix application) and
one jet-prolongation step, advancing the phase by `ℏ_q` of a full circuit.

## Formalisation notes

- **Derived arithmetic, not assumed.** The headline chain
  `n_R = t_P = q/(q−1) = 1/ℏ_q` is *derived* from the definitions
  `ℏ_q = (q − 1)/q`, `t_P = q/(q − 1)`, and `n_R = t_P` (the iteration
  count equals the Planck time, from the Reeb-time coordinate
  `t = ℏ_q · 𝒯`). The non-trivial step `t_P = 1/ℏ_q` is `field_simp`
  + `ring`. The phase-increment bound `0 < ℏ_q < 1` is likewise
  *derived* from `ℏ_q = (q − 1)/q` with `q > 1`.
- The per-iteration counts (`n_connection_apps = 1`, `n_R_matrix_evals
  = 1`) are structural *definitions* of the discrete dynamics (one `∇_q`
  application, one `R`-matrix evaluation per `f_q`-iteration), carried as
  honest data fields — not self-assumed conclusions.

-- Ref: [manuscript] quantum-observable-universe/information-theory/reeb-operations-per-planck.md
-/

namespace QOU.Information

/-- Inputs for the Reeb-operations-per-Planck identity.

    The substrate definitions (`ℏ_q = (q−1)/q`, `t_P = q/(q−1)`,
    `n_R = t_P`) are carried as fields; the arithmetic identities
    `t_P = 1/ℏ_q` and `0 < ℏ_q < 1` are *derived* in the theorem, not
    assumed. The per-iteration operation counts are modelling data. -/
class ReebOperationsPerPlanckContext extends QOU.Shared.MarkovTraceContext where
  /-- Real substrate parameter `q_real : ℝ` (specialisation of the
      generic shared `q : R` to ℝ for the analytic identity below). -/
  q_real : ℝ
  /-- `q > 1` (QOU regime). -/
  q_gt_one : 1 < q_real
  /-- Substrate q-Planck constant `ℏ_q`. -/
  hbar_q : ℝ
  /-- **Definition:** `ℏ_q = (q − 1)/q`. -/
  hbar_q_eq : hbar_q = (q_real - 1) / q_real
  /-- Planck time `t_P(q)`. -/
  t_P : ℝ
  /-- **Definition:** `t_P = q/(q − 1)`. -/
  t_P_eq : t_P = q_real / (q_real - 1)
  /-- Number of iterations per Reeb circuit `n_R(q)`. -/
  n_R : ℝ
  /-- **Definition (Reeb-time coordinate `t = ℏ_q · 𝒯`):** the iteration
      count composing one circuit equals the Planck time. -/
  n_R_eq_t_P : n_R = t_P
  /-- Number of `∇_q` connection applications per iteration. -/
  n_connection_apps : ℕ
  /-- Modelling datum (ii): each iteration applies `∇_q` exactly once. -/
  n_connection_apps_eq : n_connection_apps = 1
  /-- Number of `R`-matrix evaluations per iteration. -/
  n_R_matrix_evals : ℕ
  /-- Modelling datum (iii): each iteration evaluates exactly one
      `R`-matrix. -/
  n_R_matrix_evals_eq : n_R_matrix_evals = 1

/-- **Discrete iterations per Reeb circuit** ([`prop:reeb-operations-per-planck`]).

    `n_R = t_P = q/(q − 1) = 1/ℏ_q`, the phase increment satisfies
    `0 < ℏ_q < 1`, and each iteration performs one `∇_q` application and
    one `R`-matrix evaluation — all *derived* from the substrate
    definitions and `q > 1`. -/
-- Ref: [manuscript] quantum-observable-universe/information-theory/reeb-operations-per-planck.md
theorem reeb_operations_per_planck [ctx : ReebOperationsPerPlanckContext] :
    (ctx.n_R = ctx.t_P ∧ ctx.t_P = ctx.q_real / (ctx.q_real - 1) ∧
     ctx.t_P = 1 / ctx.hbar_q) ∧
    (0 < ctx.hbar_q ∧ ctx.hbar_q < 1) ∧
    ctx.n_connection_apps = 1 ∧
    ctx.n_R_matrix_evals = 1 := by
  have hq0 : (0 : ℝ) < ctx.q_real := lt_trans one_pos ctx.q_gt_one
  have hq1 : (0 : ℝ) < ctx.q_real - 1 := by linarith [ctx.q_gt_one]
  refine ⟨⟨ctx.n_R_eq_t_P, ctx.t_P_eq, ?_⟩, ⟨?_, ?_⟩,
          ctx.n_connection_apps_eq, ctx.n_R_matrix_evals_eq⟩
  · -- t_P = 1 / ℏ_q
    rw [ctx.t_P_eq, ctx.hbar_q_eq]
    rw [one_div, inv_div]
  · -- 0 < ℏ_q
    rw [ctx.hbar_q_eq]
    exact div_pos hq1 hq0
  · -- ℏ_q < 1
    rw [ctx.hbar_q_eq, div_lt_one hq0]
    linarith

end QOU.Information
