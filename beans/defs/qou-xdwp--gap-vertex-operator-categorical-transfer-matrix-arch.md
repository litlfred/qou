---
# qou-xdwp
title: ""
status: todo
type: task
priority: normal
created_at: 2026-09-26T09:57:34Z
updated_at: 2026-09-26T11:03:26Z
---


## 🟩 BOTH architectural blockers are resolved — verified at the files (2026-09-13, bean qou-g5sp)

Both files compile: `vertex-operator.lean` and `categorical-transfer-matrix.lean`
are `exit 0`, 0 errors in the 938-target content sweep on `main` `16ccc3f7e2`
([`2026-09-13-every-content-sibling-compiles-zero-red.md`](../docs/audits/2026-09-13-every-content-sibling-compiles-zero-red.md)).

**But this bean is explicit that a compile fix is not what it was tracking** —
it separates its four mechanical fixes from "still open — architectural, one
each". So the compile result alone would not close it. Both architectural items
were checked **in the source**, not taken from `qou-e7xv`'s account of having
fixed them; AGENTS.md: *"a sibling's bean is not a primary source either."*

**`vertex-operator.lean` — "`ReebBundle` is not in scope", declared in another
content-block sibling this file structurally cannot import.** Resolved by the
route this bean listed as an option, and by the safer one: `ReebBundle` is
carried as a **type parameter `B`**, not promoted into the Lake library. The
file's own docstring at lines 45–59 records exactly the hazard this bean
predicted would bite on a naive promotion — `structure ReebBundle (q : ℝ)` is
archimedean while this file is categorical over `R_q = ℤ[q, q⁻¹]` — and names
`B := ReebBundle q₀` as the instantiation *after* the τ functor. That is the §7c
wall respected rather than crossed.

Separately: `ope_is_skein` is a **`theorem`** at line 102. This bean recorded it
as a bare `axiom`.

**`categorical-transfer-matrix.lean` — "an undetermined implicit",
`base : ExceptionalDivisor` not a parameter of the structure.** Resolved the same
way, a type parameter `B`, with the rationale at lines 84–89.

**And the axiom question this bean asked to settle in the same pass, was.** Its
closing flag: *"the declaration this blocks is `axiom
transfer_matrix_level_independence` … so this file wants the axiom question
settled at the same time, not two passes."* The file now carries
`level_independence_false_as_stated` at line 153 — a **refutation**, the axiom
was FALSE as stated — and `transfer_matrix_level_independence` as a **`theorem`**
at line 183. One pass, as asked.

Both items closed, both verified at the source. Status → completed.
