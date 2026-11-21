import Mathlib.Algebra.Group.Nat.Defs

/-!
# QOU.Molecular.ElectronShellCapacity

## Why this is a `def` and not a `theorem`

An earlier revision read

```lean
theorem electron_shell_capacity_2n2 (n : ℕ) : Prop :=
  ∃ capacity : ℕ → ℕ, capacity n = 2 * n^2
```

with the same two defects as `QOU.Information.DispersionSuppressionScale`:

1. **It proved nothing** — its *type* is `Prop`, so it is a proposition, not a
   proof of one; `theorem` claimed a proof that does not exist (AGENTS.md §1a).
2. **The proposition was content-free** — the existential is witnessed by
   `fun k => 2 * k ^ 2` for every `n`, so it is provable outright and says
   nothing about electron shells.

Restated as a predicate on a given capacity function, and quantified over all
`n` rather than asserted at a single one.

Note this module is *not* the substantive treatment of shell capacity; see
[`electron-shell-braid-capacity`](../../../quantum-observable-universe/molecular-construction/electron-shell-braid-capacity.lean)
for the braid-theoretic content. Nothing in the corpus referenced this
declaration.

-- Ref: [leitner2026] quantum-observable-universe/molecular-construction/electron-shell-2n2-capacity.md
-/

namespace QOU.Molecular.ElectronShellCapacity

/-- **The `2n²` shell-capacity rule.**

    `electron_shell_capacity_2n2 capacity` holds when `capacity n = 2n²` for
    every shell index `n`. A predicate on the capacity function, not an
    existential over it — the existential form is discharged by
    `fun k => 2 * k ^ 2` and therefore asserts nothing. -/
def electron_shell_capacity_2n2 (capacity : ℕ → ℕ) : Prop :=
  ∀ n : ℕ, capacity n = 2 * n ^ 2

end QOU.Molecular.ElectronShellCapacity
