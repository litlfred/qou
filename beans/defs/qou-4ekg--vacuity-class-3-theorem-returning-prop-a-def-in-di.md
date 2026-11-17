---
# qou-4ekg
title: 'VACUITY class 3: theorem-returning-Prop — a def in disguise that proves nothing'
status: in-progress
pr: 8259
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T11:54:19Z
updated_at: 2026-10-04T15:25:24Z
parent: qou-6qbv
---


## Finding

Two declarations were written as

```lean
theorem electron_shell_capacity_2n2 (n : ℕ) : Prop :=
  ∃ capacity : ℕ → ℕ, capacity n = 2 * n^2

theorem dispersion_suppression_scale (q : ℝ) (E_QG : ℝ) : Prop :=
  ∃ fractional_variation : ℝ → ℝ, ∀ E : ℝ, E > 0 → fractional_variation E ≤ E / E_QG
```

Two *independent* defects in each:

1. **The declaration proves nothing.** Its *type* is `Prop`, so the term is a
   proposition, not a proof of one. Calling it `theorem` claims a proof that
   does not exist — AGENTS.md §1a. This is a `def` wearing a `theorem` label,
   the mirror image of the `def`-disguised-`True` case the vacuity audit
   already catches.
2. **The proposition it named was content-free.** Both existentials are
   outright provable — `capacity := fun k => 2 * k ^ 2` witnesses the first for
   every `n`; any negative constant witnesses the second. Quantifying the
   *subject* of the claim existentially is what destroyed the content. `q` was
   unused in the second.

Both carried the docstring marker "**Pattern C — named proposition**", so
naming a proposition *was* the intent — the `theorem` kind and the existential
wrapper were the errors.

## Scope

**Two instances corpus-wide** (`grep -rn "^theorem .*: Prop :="`), both fixed.
Contained, not systemic. Recording it anyway because the shape is invisible to
every existing checker and cheap to re-introduce.

## Resolution

Restated as content-bearing predicates on the subject, quantified properly:

```lean
def dispersion_suppression_scale (fractionalVariation : ℝ → ℝ) (E_QG : ℝ) : Prop :=
  ∀ E : ℝ, 0 < E → fractionalVariation E ≤ E / E_QG

def electron_shell_capacity_2n2 (capacity : ℕ → ℕ) : Prop :=
  ∀ n : ℕ, capacity n = 2 * n ^ 2
```

Names preserved: `dispersion_suppression_scale` is the `lean.ref` target of the
`conj:dispersion-suppression-scale` content block, so renaming would break the
manifest. `electron_shell_capacity_2n2` had **no** references anywhere in the
corpus (the substantive treatment is `electron-shell-braid-capacity.lean`).

Imports narrowed from `import Mathlib` to `Mathlib.Data.Real.Basic` /
`Mathlib.Algebra.Group.Nat.Defs` — which also closes bean `qou-iww3`: these were
the two modules that could not be verified from the olean cache at all, because
the cache carries per-module oleans but not the aggregate `Mathlib.olean`.
Both now verify. Narrowing was the preferred fix regardless (AGENTS.md §8).

## Follow-up worth considering

`conj:dispersion-suppression-scale` is a **`conjecture`** block. Per §3b-tax the
fully-compliant carrier is a content-bearing `class` with no instance, not a
bare predicate `def`. A predicate is strictly better than what was there and is
non-controversial; promoting it to a class interacts with the block's `uses[]`
and is an owner-facing design call, so it is left open here rather than decided
unilaterally.

Also: add `^theorem .* : Prop :=` to the vacuity audit's detector set. One
regex, and it is a hard error rather than a heuristic — a theorem whose type is
`Prop` is *always* miskinded.

- **Round 55 update (in-progress):** De-vacuified in PR `litlfred/qou#8259` (HEAD `1be723e4c3e702d48db833cb3bedc75e89004822`), verified with Lean 4.24.0 (`0` `sorry`, `0` vacuity hits) and 80-dps `mpmath` witness.
