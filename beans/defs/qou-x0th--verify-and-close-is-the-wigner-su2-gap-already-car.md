---
# qou-x0th
title: 'Verify-and-close: is the ''Wigner SU(2) gap'' already carried by WignerSU4FromSpinIsospin.lean + WignerSU4RowBoundInactive.lean? (split from nmib)'
status: todo
type: task
priority: normal
tags:
    - 8f-lean
    - reorg-2026-10-04
    - split-from-nmib
created_at: 2026-10-10T08:27:45Z
updated_at: 2026-10-10T08:28:04Z
parent: qou-8lxd
---

Split out of `qou-nmib` on 2026-10-10. **Probably a verify-and-close, not a
formalisation** — read the two files below before writing any Lean.

`qou-nmib` asked, in one title, for "H3 Delta baryon map **and** Wigner SU(2)
gap resolution". The second half appears already carried. Two substantive
sorry-free Lean files exist on the live tree, neither a stub:

**1. `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/WignerSU4FromSpinIsospin.lean`**
The D11 carrier for `conj:wigner-su4-from-spin-isospin` — `SU(4) = SU(2)_S ×
SU(2)_I` as the combined classical limit of the spin `SO(3)` fibre action (D10)
and the canonical isospin `ℤ/2` swap (D9).

- `class WignerSU4FromSpinIsospin` (line 100), **no instance provided** — the
  honest open state for a conjecture per §3b.
- `wignerSU4_occupancy_via_plancherel` (127).
- `wignerSU4FromSpinIsospin_refutable` (139) / `_satisfiable` (152). **This pair
  is the part worth not losing**: without it, a conjecture class is
  indistinguishable from one that is vacuously unsatisfiable, and this file's own
  history is exactly that failure — see below.

**2. `folio/quantum-observable-universe/lean/QOU/Mass/WignerSU4RowBoundInactive.lean`**
The row-cap side: `rows`, `rows_le`, `SU4Admissible p := rows p ≤ 4`,
`su4_inactive_of_le_four`, `su4_filter_eq_univ`, `su4_restricted_sum_eq`,
`su4_no_magic_enhancement`, and `su4_active_at_five` as the non-vacuity witness
(the bound bites only from `n = 5`, so the earlier theorems are applicable rather
than conditionally empty).

## The trap this file already fell into, recorded so it is not re-introduced

Per that file's own docstring: its two content-bearing fields once read

```lean
dynamic_capacity_from_plancherel_weight (A Z N : ℕ) (S W_lam E_gate E_0 : ℝ) :
  E_gate = E_0 * Real.log (1 / W_lam)
```

— an equation between **four unrelated reals with no hypothesis linking them**.
Instantiating `E_gate := 1`, `E_0 := 0` gives `1 = 0`, so
`¬ Nonempty WignerSU4FromSpinIsospin` was **provable**: the class had no instance
*and could not have one*. Repaired on an owner ruling, together with a `.ts` ref
that resolved to a **different**, vacuous `holds : Prop` stub — so the block was
reading a carrier that asserted nothing while the one asserting something had no
reader.

## What this bean actually needs

1. **State what "the gap" was.** `qou-nmib` never said; its title is the only
   record. Candidates: the `SU(2)_S × SU(2)_I` factorisation itself, the
   `su4_inactive_of_le_four` vacuity window (`n ≤ 4`), or the occupancy weight.
   Corpus-grep `conj:wigner-su4-from-spin-isospin`'s consumers first.
2. **Check it against the two files**, including `#print axioms` on the named
   declarations.
3. **Close with evidence, or re-scope to whatever is genuinely missing.**

**Default if unanswered: nothing happens** — the two files stay as they are and
remain correct; only the ledger stays unclear about whether the item is done.

**Blast radius:** read-only unless step 3 finds a gap. No compute, no witness.
