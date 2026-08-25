# Covariance-kernel epic (qou-x631) — A1 ELIMINATED; the unifying dim²→dim³ threshold

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-attack-all-2026-07-25` · **Tier:**
route-elimination (A1) + synthesis · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`;
L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-4hq0` (A1).

## A1 — exact evaluation of `T₃`: ELIMINATED (route #12)

A paper-mining + compute agent (Okounkov–Olshanski `9608020`, Ivanov–Olshanski `0304010`, Śniady
`0411647`) settled it: **`T₃(n) = Σ_λ (dim λ)² χ^λ(3-cycle)` has no usable closed form**, and no
manifestly-negative expression. Confirmed: OEIS-absent, not P-recursive; ratio/product/hypergeometric
families all miss. The simplest exact finite forms are `T₃(n) = Σ_{w∈S_n} χ^{sh(w)}(σ₃)` (RSK) and the
content moment `(3/[n(n−1)(n−2)])·Σ_λ (dim λ)³(Σc²−C(n,2))` — neither closed nor manifestly signed.

## The unifying obstruction — the dim²→dim³ threshold

The decisive finding is *why*, and it **unifies A1 with A5**. Since `χ^λ(σ₃) = dim λ · ω₃(λ)` with
`ω₃` a shifted-symmetric function of degree 3 (Plancherel mean 0), weight `ω₃` by `(dim λ)^k`
(verified, `n ≤ 12`):

| weight | sum | value | status |
|---|---|---|---|
| `k=2` | `Σ_λ (dim)² ω₃` | **`0`** exactly | CLOSED — Plancherel expectation of a positive-degree shifted-symmetric function (IO Prop 5.1) |
| `k=3` | `Σ_λ (dim)³ ω₃ = cov(n)` | `≠ 0` | **non-holonomic** — one extra `dim` factor (`= χ^λ(e)`, *not* shifted-symmetric) |

Even the positive envelope `Σ_λ (dim)³ = 10, 64, 596, 8056, …` (triples of SYT of common shape) has no
closed form. **The `dim²→dim³` step is exactly where tractability is lost.**

**Every framework tried is blind to the same extra `dim`:**

- **A1 (exact eval / shifted-symmetric):** `Σ (dim)² F = poly(n)` for shifted-symmetric `F`; the extra
  `dim` makes `Σ (dim)³ ω₃` non-holonomic. → eliminated.
- **A5 (Śniady genus):** the grading lives on the algebra `A` of polynomial functions on Young
  diagrams; `dim λ ∉ A`, so `dim³·ω₃` has no genus / leading term. → eliminated (route #11).
- **A2 (leading term):** `Cov_Planch(ln f, ω₃)` involves `ln dim λ`, also `∉ A`. → same wall.

So the kernel is hard for **exactly one reason**: it requires evaluating a **non-shifted-symmetric
dimension functional** (`dim λ` or `ln dim λ`) against the Plancherel measure. The one missing tool is
a **dimension-functional expansion** — Vershik–Kerov `ln dim` functional, Schur-measure, or a
hook-content generating function — **not** the character / shifted-symmetric machinery. This is the
sharpest characterization of the open problem to date, and it tells the next attempt exactly what to
build.

## Correction (A1 agent's illustrative table)

The agent's `k=1` row (`Σ dim·ω₃ = 0` "by column orthogonality") is **wrong**: `Σ dim·ω₃ =
|C₃|·Σ_λ χ^λ(σ₃) = 2, 8, 40, 160, …` (nonzero). The agent conflated it with `Σ dim·χ(σ₃) = 0`. The
load-bearing facts (`k=2` vanishes, `k=3` non-holonomic) are correct and re-verified here.

## Conjugation bijection infra (A4 general form) — feasible but deferred

The general `∀`-sorted-`l` conjugation-invariance (`contentSq (conj l) = contentSq l`) reduces to one
lemma — the sorted-`countP` cell bijection `[j < (conj l).getD i 0] ↔ [i < l.getD j 0]` — then
`Cross(conj l) = Cross(l)` by a double-sum reindex. The needed Mathlib modules (`Data.List.Sort`,
`Data.List.Count`) **are** in the restored olean cache (only `Tactic.Omega` is missing, workable with
`Nat` lemmas / `Nat.lt` API). So it is **feasible**, but a genuine multi-iteration Lean proof, and
blind iteration (no lean-lsp; ~2–4 min/compile) is expensive for a non-load-bearing scaffold lemma —
deferred to a dedicated pass. The instance-level result (all `λ ⊢ k`, `k ≤ 6`, `decide`) is already on
`main` (`contentSq_conj_invariant_of_le_six`), establishing the mathematical point.

## Net

A1 eliminated (#12). The attack round's payoff is the **unifying dim²→dim³ characterization**: the
kernel needs a dimension-functional expansion against Plancherel, the one tool outside every
character/shifted-symmetric/genus framework. Remaining live route: **A2** (log-covariance leg), now
sharpened to "expand `ln dim` against Plancherel." Kernel stays an open §3b conjecture.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_dim_threshold.py`](../../computations/deltalambda/wlambda_covariance_epic_dim_threshold.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-dim-threshold.witness.json`

## Cross-references

- A5 (genus eliminated) + A4 (Lean): [`2026-07-25-covariance-kernel-A5-genus-eliminated-A4-lean.md`](2026-07-25-covariance-kernel-A5-genus-eliminated-A4-lean.md)
- A3 (CM refuted): [`2026-07-25-covariance-kernel-complete-monotonicity-target.md`](2026-07-25-covariance-kernel-complete-monotonicity-target.md)
- Attack plan: bean `qou-v8t7`; Okounkov–Olshanski `9608020`, IO `0304010`, Śniady `0411647` (`library/`)
