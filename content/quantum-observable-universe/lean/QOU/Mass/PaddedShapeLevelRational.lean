import QOU.MathlibExt.QPartitionCombinatorics
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Mass.PaddedShapeLevelRational — level-rationality of padded-shape q-dimensions

Lean face of the §8/§10 decisive probe of
`docs/audits/2026-07-03-parabolic-cylinder-channel-interpolation.md`
(`computations/deligne_stable_range_binding_period_probe.py`, 99/99 exact): for a fixed
shape `μ`, the padded family `n ↦ dim_q(μ[n])`, `μ[n] = (n − |μ|, μ)`, is a fixed
rational function of `(q, qⁿ)` — the per-shape restriction property of the Deligne/TL
interpolated level.

The identity factors into two inputs of different kinds, and this file formalizes the
division of labor explicitly:

* **Algebraic content (proved here, sorry-free).** The q-factorial telescope
  `[n]_q! = [n−K]_q! · ∏_{i<K} [n−i]_q` (`qFactorial_telescope`, induction on `K`) and
  its division form (`qFactorial_div_telescope`, at `1 < q` where `[·]_q! ≠ 0`).
* **Combinatorial input (probe-verified, carried as an explicit hypothesis).** The hook
  multiset of the padded shape splits as
  `hooks(μ[n]) = {1, …, n−|μ|−μ₁} ⊎ {n − c_j}_{j ≤ μ₁} ⊎ hooks(μ)` with
  `c_j = |μ| + j − 1 − leg_j(μ)` — equivalently `hookProd q (μ[n]) = [n−K]_q! · D` with
  `K = |μ| + μ₁` and `D` the fixed shifted-bracket × `H_q(μ)` factor. This is the
  99/99-verified combinatorial fact; `qdim_level_rational_of_hook_split` consumes it as
  the named hypothesis `hsplit` (honest §3b-style conditionality — no `sorry`, no
  hidden assumption). Its general combinatorial proof (a fold decomposition over
  `Partition.hookLength`) is queued follow-up work.

Together: `qDim q (μ[n]) = ∏_{i<K} [n−i]_q / D` — numerator a fixed window of
`K = |μ|+μ₁` brackets sliding with the level, denominator level-independent. Each
`[n−i]_q` is Laurent in `qⁿ`, so the family is rational in `(q, qⁿ)` of degree bounded
by `K` — "polynomial in the level", the q-dimension face of Deligne interpolation
\cite{deligne2007}.

Ground ring: `ℝ`, matching the canonical `QPartitionCombinatorics` infrastructure this
file consumes (its nonvanishing lemmas live at `1 < q`); the telescope itself is
ordering-free and would state over any field — kept here to avoid duplicating the
q-bracket stack (§7c note).
-/

namespace QOU.Mass.PaddedShapeLevelRational

open QOU.MathlibExt.QPartitionCombinatorics

/-- The hook product `∏_{x ∈ λ} [h_x]_q` — the denominator fold of `qDim`, named. -/
noncomputable def hookProd (q : ℝ) (lam : Partition) : ℝ :=
  (List.range lam.length).foldl
    (fun acc i =>
      acc * (List.range ((lam.get? i).getD 0)).foldl
        (fun a j => a * qBracket q (Partition.hookLength lam i j))
        1)
    1

/-- `qDim` is definitionally the q-factorial over the named hook product. -/
theorem qDim_eq_fact_div_hookProd (q : ℝ) (lam : Partition) :
    qDim q lam = qFactorial q lam.size / hookProd q lam := rfl

/-- **q-factorial telescope**: `[n]_q! = [n−k]_q! · ∏_{i<k} [n−i]_q` for `k ≤ n`.
The algebraic heart of padded-shape level-rationality: the last `k` brackets of the
q-factorial form a fixed-size window sliding with `n`. -/
theorem qFactorial_telescope (q : ℝ) (n : ℕ) :
    ∀ k : ℕ, k ≤ n →
      qFactorial q n = qFactorial q (n - k) * ∏ i ∈ Finset.range k, qBracket q (n - i) := by
  intro k
  induction k with
  | zero => intro _; simp
  | succ k ih =>
    intro h
    have hk : k ≤ n := Nat.le_of_succ_le h
    rw [ih hk, Finset.prod_range_succ,
      show n - k = n - (k + 1) + 1 from by omega, qFactorial_succ]
    ring

/-- Division-free form of the telescope, for downstream `rw` without nonzero
hypotheses. -/
theorem qFactorial_mul_telescope (q : ℝ) (n K : ℕ) (h : K ≤ n) (D : ℝ) :
    qFactorial q n * D =
      qFactorial q (n - K) * ((∏ i ∈ Finset.range K, qBracket q (n - i)) * D) := by
  rw [qFactorial_telescope q n K h]; ring

/-- Division form at `1 < q` (where `[n−K]_q! ≠ 0`):
`[n]_q! / ([n−K]_q! · D) = ∏_{i<K} [n−i]_q / D`. -/
theorem qFactorial_div_telescope {q : ℝ} (hq : 1 < q) (n K : ℕ) (h : K ≤ n) (D : ℝ) :
    qFactorial q n / (qFactorial q (n - K) * D) =
      (∏ i ∈ Finset.range K, qBracket q (n - i)) / D := by
  rw [qFactorial_telescope q n K h,
    mul_div_mul_left _ _ (qFactorial_ne_zero hq (n - K))]

/-- **Level-rationality of the padded q-dimension** (conditional on the hook split).
If the hook product of `λ = μ[n]` splits off the tail q-factorial —
`hookProd q λ = [|λ|−K]_q! · D` with `K = |μ|+μ₁` and `D` the level-independent
shifted-bracket × `H_q(μ)` factor (the probe-verified combinatorial input, 99/99 exact
for `|μ| ≤ 4`, `n ≤ 12`) — then

  `qDim q λ = ∏_{i<K} [|λ|−i]_q / D`,

a fixed rational function of `(q, q^{|λ|})`: the per-shape Deligne/TL restriction
property. The interpolation-vs-feasibility verdict (audit §10): this per-shape
rationality is exact, while the *sum* over the growing shape set escapes it — the
stable truncation captures a collapsing fraction of `T_q(n)` at `q₀`. -/
theorem qdim_level_rational_of_hook_split {q : ℝ} (hq : 1 < q) (lam : Partition)
    (K : ℕ) (hK : K ≤ lam.size) (D : ℝ)
    (hsplit : hookProd q lam = qFactorial q (lam.size - K) * D) :
    qDim q lam = (∏ i ∈ Finset.range K, qBracket q (lam.size - i)) / D := by
  rw [qDim_eq_fact_div_hookProd, hsplit,
    qFactorial_div_telescope hq lam.size K hK D]

end QOU.Mass.PaddedShapeLevelRational
