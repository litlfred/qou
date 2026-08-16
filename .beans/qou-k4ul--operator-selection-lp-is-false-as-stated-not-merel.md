---
# qou-k4ul
title: operator_selection_lp is false as stated, not merely unproved
status: completed
type: bug
priority: high
created_at: 2026-08-16T11:20:00Z
updated_at: 2026-08-16T11:20:00Z
---

**Machine-verified with a working Lean toolchain.** `False` is derivable from
`operator_selection_lp`. Its `sorry` is not an honest placeholder for missing
infrastructure — it is an obligation nobody can ever discharge, because the
statement is untrue.

## Why

`OperatorSelectionLpContext` carries **only data** and no hypotheses:

```
n, d, n_target, t, G, x_star, y_0_star
```

Nothing relates `x_star` to `n_target`, `G` or `t`. The theorem nevertheless
concludes, for **every** instance,

```
IsFeasible x_star ∧ (∀ x, IsFeasible x → objective x_star ≤ objective x)
                  ∧ objective x_star = n_target * y_0_star
```

and `IsFeasible x` requires `∑ᵢ xᵢ = n_target`. Instantiate with `d = 1`,
`n_target = 1`, `x_star = 0`: the first conjunct says `0 = 1`.

```lean
def badCtx : OperatorSelectionLpContext where
  n := 2; d := 1; n_target := 1
  t := fun _ => 0; G := fun _ _ => 0
  x_star := fun _ => 0; y_0_star := 0

theorem operator_selection_lp_is_false : False := by
  obtain ⟨⟨hsum, -⟩, -, -⟩ := @operator_selection_lp badCtx
  have hx : ∀ i, (@OperatorSelectionLpContext.x_star badCtx) i = 0 := fun _ => rfl
  simp only [hx, Finset.sum_const_zero] at hsum
  norm_num [badCtx] at hsum
```

`lean` exits **0** on this file.

**Scope of the check.** Verified against the *compiled* module in the restored
olean cache, whose `OperatorSelectionLpContext` predates the source's
generic-`R` refactor (compiled: no `R` parameter). The current source has the
identical data-only class — same seven fields, no hypotheses — so the same
counterexample applies with `R := ℝ`, but what was machine-checked is the
compiled artifact.

## How it got this way, and it is an honest mistake

The module docstring explains: an earlier version carried the optimality
conclusions as class *fields* and then projected them, which `AGENTS.md` §3b-cond
item 5 forbids as self-assumption. Removing them was right. But removing them
left **no** hypotheses at all, and a universally quantified claim over
unconstrained data is false rather than merely unproven. The fix over-corrected.

## The fix does NOT need Farkas

This matters for `kl8z`, which scoped LP duality as blocked on one closedness
lemma. That is true of `lp_strong_duality` in general — and irrelevant here.

`x_star` is a *given* candidate and `y_0_star` a *given* dual variable. To prove
optimality of an exhibited point you do not need Farkas or the simplex method;
you need the certificate, and `lp_weak_duality` — **already proved
unconditionally** — turns it into optimality. The class needs hypotheses:

- `hx_feasible : IsFeasible x_star`
- `hy_dual_feasible` : `y_0_star` satisfies the dual constraints for `(t, G)`
- `hcomplementary : objective x_star = n_target * y_0_star`

With those, all three conjuncts follow: the first by assumption, the third by
assumption, and the second from weak duality against any feasible competitor.
The `sorry` closes with no new analytic input.

Those hypotheses are *hypotheses about the data*, not the block's conclusion —
exactly the §3b-cond shape the module already uses for `MatrixFarkas`, and the
shape the docstring says it was aiming for.

## Next

- [ ] Add the three hypotheses to `OperatorSelectionLpContext`
- [ ] Discharge `operator_selection_lp` from them + `lp_weak_duality`
- [ ] Check whether the substrate instantiation can supply them (if the
      concrete `x*`/`y₀*` do not satisfy complementary slackness, that is a
      **content** finding about the claimed optimum, not a Lean one)
- [ ] Sweep for the same shape: other conditional classes that carry data with
      no hypotheses and conclude something about it

## 2026-08-16 — FIXED, and the sorry is closed

The class now carries the dual certificate as hypotheses about the data:
`s` (dual slack), `s_nonneg`, `dual_feasible` (`tⱼ = y₀ + Σᵢ sᵢGᵢⱼ`),
`x_star_feasible`, `zero_gap`. None is the block's own conclusion, so §3b-cond
item 5 is respected — this is the shape the module was already using for
`MatrixFarkas`.

`operator_selection_lp` is **proved, sorry-free**, by the weak-duality
computation inlined: for any feasible `x`,

    Σⱼ tⱼxⱼ = y₀·n_target + Σᵢ sᵢ(Gx)ᵢ ≥ y₀·n_target = Σⱼ tⱼx*ⱼ

since `sᵢ ≥ 0` and `(Gx)ᵢ ≥ 0`. `lean` exits **0** on the file; no
"declaration uses 'sorry'" warning. Imports gained
`BigOperators.Ring.Finset`, `Order.BigOperators.Group.Finset`, `Linarith`,
`Ring` — the same set `LPWeakDuality` already uses, all present in the cache.

**Farkas was never needed.** `kl8z` stands for *general* strong duality; it does
not gate this block. Verifying an exhibited certificate is not optimisation.

Stale docstring rewritten: it claimed the theorem "ends in `sorry` … requires
the LP strong-duality theorem", which was wrong on both counts.

### Still open, and it is a content question

Whether the substrate's concrete `x*`/`y₀*` actually satisfy the new
hypotheses. If they do not, the claimed optimum is wrong — a finding about the
mathematics, not the formalisation. Nothing here asserts they do.
