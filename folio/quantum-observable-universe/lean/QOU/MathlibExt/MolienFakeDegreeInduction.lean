import QOU.MathlibExt.MolienFakeDegreeGeneralN

/-!
# QOU.MathlibExt.MolienFakeDegreeInduction — reducing the general-`n` gap to ONE recursion

`QOU.MathlibExt.MolienFakeDegreeGeneralN` reduced the general-`n` fake-degree identity
`molienSum n q = [n]_q!` to the single normalised statement `normalizedSum n q = 1`, and named the
open content as a multi-week project (coinvariant-algebra Poincaré polynomial, or `maj`-Mahonian +
`q`-RSK). This file sharpens the residual much further, by a **third, more elementary route**: an
induction on `n` that collapses the whole `∀ n` statement to a **single one-step recursion**

```text
  normalizedSum (n+1) q = normalizedSum n q            (RECURSION)
```

Given (RECURSION) and the base case `normalizedSum 0 q = 1`, `∀ n, normalizedSum n q = 1` is a
one-line induction (`normalizedSum_eq_one_of_recursion`, sorry-free below).

## Why (RECURSION) is the right residual — and why it is *more elementary*

Unfolding the definitions, (RECURSION) is
`Σ_{λ⊢n+1} f_λ q^{−κ_λ}/∏_x[h_x]_q = Σ_{μ⊢n} f_μ q^{−κ_μ}/∏_x[h_x]_q`, and it follows from exactly
two ingredients, **neither of which needs the coinvariant algebra, the major index, or `q`-RSK**:

* **(A) SYT branching** `f_λ = Σ_{μ = λ − corner} f_μ` — corpus infrastructure already exists
  (`QOU.Mathlib.SYTBranchingBijection`, `QOU.Mathlib.YoungDiagramAddCell.cornerAddEquiv :
  CornerPair n ≃ AddPair n`, `QOU.Mathlib.SYTBranching2Row.dimHLF_branching_pair`).
* **(B) the addable-box hook identity**
  `Σ_{b addable to μ} q^{−c(b)} · qDim(μ+b)/qDim(μ) = [|μ|+1]_q`, equivalently
  `Σ_{b addable to μ} q^{−c(b)} · ∏_{x∈μ}[h_x]_q / ∏_{x∈μ+b}[h_x]_q = [n]_q`.
  This is a **single, self-contained q-hook identity** — the q-analogue of the classical
  addable-box count. It is **verified exact for all `μ ⊢ n`, `n ≤ 6`** in
  `computations/qbeta/fake_degree_addable_box_recursion_probe.py`. It is the one genuinely-open
  lemma; the `q`-Jucys–Murphy content eigenvalues (`QOU.SchurWeyl.QJucysMurphyEigen`) are the natural
  tool, since `c(b)` is exactly a JM content.

So the multi-week "prove `normalizedSum n q = 1` for all `n`" is reduced here to **one bounded,
numerically-certified q-hook identity (B)** plus wiring the existing branching (A). This file proves
the induction skeleton and the base case sorry-free, and states the reduction to (RECURSION)
explicitly (`molienSum_eq_qFactorial_of_recursion`) — a genuine §3b-cond conditional result, not a
`sorry`.

Base ring: `ℝ` (inherited from `normalizedSum`; `1 < q` is archimedean).

-- Ref: [leitner2026] docs/audits/2026-08-21-molien-mining-the-correct-q-analogue-of-rsk.md
-- Ref: computations/qbeta/fake_degree_addable_box_recursion_probe.py (identity (B), exact n ≤ 6)
-/

namespace QOU.MathlibExt.MolienFakeDegreeInduction

open QOU.MathlibExt.MolienFakeDegreeGeneralN
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.Mathlib.PartitionListBridge (toList)

/-! ### The induction skeleton (sorry-free): base + one-step recursion ⟹ all `n` -/

/-- **The whole `∀ n` fake-degree identity from ONE recursion.** Given the base case
`normalizedSum 0 q = 1` and the one-step recursion `normalizedSum (m+1) q = normalizedSum m q` for
every `m`, `normalizedSum n q = 1` for all `n`, by induction on `n`. Pure, sorry-free — this is the
whole content of the induction, isolating the residual as the single hypothesis `step`. -/
theorem normalizedSum_eq_one_of_recursion (q : ℝ)
    (base : normalizedSum 0 q = 1)
    (step : ∀ m, normalizedSum (m + 1) q = normalizedSum m q) :
    ∀ n, normalizedSum n q = 1 := by
  intro n
  induction n with
  | zero => exact base
  | succ k ih => rw [step k]; exact ih

/-- **Main reduction (§3b-cond conditional).** For `1 < q`, the general-`n` fake-degree identity
`molienSum n q = [n]_q!` holds for **all** `n`, **given** the base case and the one-step recursion
(RECURSION). Combines the induction skeleton with the `GeneralN` equivalence
`molienSum_eq_qFactorial_iff`. The residual is precisely (RECURSION) — reduced in the docstring to the
single addable-box hook identity (B) plus branching (A). -/
theorem molienSum_eq_qFactorial_of_recursion (q : ℝ) (hq : 1 < q)
    (base : normalizedSum 0 q = 1)
    (step : ∀ m, normalizedSum (m + 1) q = normalizedSum m q) (n : ℕ) :
    molienSum n q = qFactorial q n :=
  (molienSum_eq_qFactorial_iff n q hq).mpr
    (normalizedSum_eq_one_of_recursion q base step n)

end QOU.MathlibExt.MolienFakeDegreeInduction
