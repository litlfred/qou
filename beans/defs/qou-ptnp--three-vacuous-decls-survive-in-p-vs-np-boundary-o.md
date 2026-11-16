---
# qou-ptnp
title: Three vacuous decls survive in p-vs-np-boundary.lean; one is cited as the warrant for the intractability input
status: in-progress
type: task
priority: normal
tags:
    - anti-laundering
    - reorg-2026-10-04
    - lean
    - vacuity
created_at: 2026-08-22T06:05:00Z
updated_at: 2026-11-16T20:00:34Z
parent: qou-6qbv
---

Found while scanning the Lean tree for the `qou-rhax` shape (an axiom whose
right-hand side is trivially inhabited). `rhax` did not generalise — it is the
only inconsistent axiom — but the scan surfaced a different, live class in
[`information-theory/p-vs-np-boundary.lean`](../folio/quantum-observable-universe/information-theory/p-vs-np-boundary.lean).

Three declarations there prove nothing their names or docstrings claim. Each
statement is quoted verbatim from the current file.

**1. `finite_field_always_decidable` (line 170)**

```lean
theorem finite_field_always_decidable (p : ℕ) (hp : p > 1) (c : ℕ) :
    ∃ (steps : ℕ), steps = p * 3 ^ c ∧ steps > 0
```

Inhabited by `⟨p * 3 ^ c, rfl, _⟩`. It asserts that a positive natural equals a
given positive expression. Nothing in it mentions a field, a lookup table, or
decidability — `p` is used only as a natural number, never as a field size. The
docstring's claim ("the obstruction ALWAYS vanishes over finite fields because
the computation can be done by lookup table") is not what is proved.

**2. `finite_field_p_eq_np` (line 182)**

```lean
theorem finite_field_p_eq_np (c : ℕ) : ∃ bound : ℕ, 3 ^ c ≤ bound
```

Inhabited by `⟨3 ^ c, le_refl _⟩`. Every natural has a natural above it; this is
true for every `c` under any hypothesis whatsoever. The name asserts a
complexity-class collapse.

**3. `nontorsion_full_tree` (line 220) — this is the load-bearing one**

```lean
theorem nontorsion_full_tree (_qt : NonTorsionReal) (c : ℕ) (hc : c > 0) :
    ∀ (effective : ℕ), effective = 3 ^ c → effective ≥ 3
```

The `NonTorsionReal` argument is unused (underscore-prefixed), so semisimplicity
plays no role in the proof. And `NonTorsionReal` carries only `q : R_q` — both
of its defining properties (`q > 1`, `∀ k ≥ 1, q ^ k ≠ 1`) are commented out as
archimedean — so the structure is inhabited by any `q` at all. What is proved is
`3 ^ c ≥ 3` for `c ≥ 1`.

It is **cited as a corpus result** in
[`QOU/Information/PhysicalIntractability.lean:175`](../folio/quantum-observable-universe/lean/QOU/Information/PhysicalIntractability.lean):

> At a **non-torsion** substrate `q₀` the Hecke algebra is semisimple, so **no
> paths cancel**: the full `3^c` tree survives (corpus `nontorsion_full_tree`).

The cited theorem does not say that. "No paths cancel" is the premise that fixes
`info(n) = 3^{3n}`, which is the physical input to the intractability argument
in that file. So a quantitative input is warranted by a citation to a tautology
— "sorry-free ≠ derived", one file over.

## Why this is worth a bean rather than a quiet fix

The same file already excised an identical defect, **with a written rationale**,
at lines 211–219:

> The former `torsion_effective_tree_bounded (t) (n) : ∃ bound : ℕ, bound =
> t.order ^ n := ⟨t.order ^ n, rfl⟩` was removed. Two problems, neither
> repairable in place: 1. `∃ bound, bound = e` is provable by `⟨e, rfl⟩` for any
> `e`, so the declaration asserted nothing […] 2. Its docstring claimed […]

Item 1 is verbatim the defect in `finite_field_always_decidable`, eight lines
above it in the same file. Whoever wrote that excision had the criterion in hand
and applied it to one declaration. The remaining three were not swept, and none
appear in
[`docs/audits/2026-08-07-lean-vacuous-existential-audit.md`](../docs/audits/2026-08-07-lean-vacuous-existential-audit.md),
which that comment points at.

## Honest disposition

Per AGENTS.md §1a the options are prove / queue / demote — not delete-and-move-on
for (3), because something downstream is relying on it.

- **(1) and (2)**: delete, following the precedent already set in the file. State
  the real proposition if one is wanted; a lookup-table bound needs a cost model
  the file does not define, exactly as the excision comment says of the tree
  bound.
- **(3)**: the honest statement needs a cancellation/effective-tree-size
  function to be non-trivial, and `NonTorsionReal` needs its properties back
  (they are commented out as "archimedean; not meaningful over `R_q`" — which is
  the real obstruction, and is itself worth recording). Until then the citation
  in `PhysicalIntractability.lean` should say the premise is **assumed**, not
  that the corpus proves it.

Not attempted here: this is a statement-design decision about what the
non-torsion premise is allowed to assume, and it belongs to whoever owns the
intractability chain.

## Round 49 Progress (`litlfred/qou#8180`, `75360a145951a3e9bdb50b79e4a7ca2a9c94a813`)

- Replaced the vacuous `: True` conjunct in `classP` (`folio/quantum-observable-universe/information-theory/p-vs-np-boundary.lean`) with the polynomial upper bound `c ≤ (c + 1) ^ d`.
- Defined `FiniteFieldLookupTable (p c : ℕ) : Type := Fin p × Fin (3 ^ c)` and `ResolutionTreeBranch (c : ℕ) : Type := Fin c → Fin 3`, and replaced the three vacuous declarations `finite_field_always_decidable`, `finite_field_p_eq_np`, and `nontorsion_full_tree` with non-vacuous `Fintype.card` and non-torsion (`qt.q ^ c ≠ 1`) theorems consuming `hp`, `qt.not_root_of_unity`, and `hc`.
- Clarified the citation of `nontorsion_full_tree` in `folio/quantum-observable-universe/lean/QOU/Information/PhysicalIntractability.lean` and fixed the unused `hB` compiler warning.
- Verified with `lean -DautoImplicit=false -s 65536` (`0` errors, `0` warnings, `0` `sorry`) and all static vacuity audits (`0` findings).
