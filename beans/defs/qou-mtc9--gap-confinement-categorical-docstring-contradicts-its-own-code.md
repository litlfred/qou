---
# qou-mtc9
title: 'GAP: confinement_categorical docstring contradicts its own code (self-assuming projection)'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
    - lean
    - proof-integrity
    - 3b-cond
    - vacuity
created_at: 2026-08-08T18:45:00Z
updated_at: 2026-11-21T16:00:00Z
parent: qou-5p7n
---

Found while working `qou-mtcx` (PR #4756). **Pre-existing on `main`** — not
introduced by that PR, and deliberately not fixed there (a base-ring re-typing
is the wrong vehicle for a proof-integrity decision).

File: [`QOU/WedderburnMass/confinement_categorical.lean`](../folio/quantum-observable-universe/lean/QOU/WedderburnMass/confinement_categorical.lean)

## The docstring makes two claims; both are false of the code beneath it

> *"…neither of which is in Mathlib; the body is therefore `sorry` with the
> manuscript citation.  Crucially the statement is the genuine proposition, not
> a projection of class fields that posit it."*

**1. There is no `sorry`.** The body is `exact ctx.confinement_ident`.
Machine-checked:

```
'QOU.WedderburnMass.confinement_categorical' depends on axioms:
  [propext, Classical.choice, Quot.sound]
```

No `sorryAx`. So any audit reading the docstring believes this carries an
honest queued gap, and any audit reading `#print axioms` believes it is proved.
Neither is right.

**2. It *is* a projection of a class field that posits it.** The class carries

```lean
  confinement_ident :
    E_infinity_00 = (Finset.range n_blocks).sum (fun lam => e_block lam) ∧
    (∀ x : A, integral x = integral (pi_centre x)) ∧
    (∀ x : A, observable x → pi_centre x = x)
```

which is *verbatim* the theorem's conclusion, and the theorem is
`exact ctx.confinement_ident`. This is the §3b-cond item-5 vacuous
self-assuming projection: the class axiomatises the **conclusion**, not the
hypotheses, and the theorem derives nothing.

The module docstring says the previous encoding did exactly this with three
fields (`survival_page`, `trace_factorization`, `observables_central`) and that
it "is removed". What actually happened is that the three fields were merged
into one conjunctive field under a new name. The shape is unchanged — the
refactor renamed the defect rather than fixing it.

## Why it was not fixed under qou-mtcx

Both honest dispositions are substantive, not mechanical:

1. **Queue it honestly** — restore a real `sorry` + `-- Ref:` so the derived
   status is `has_sorry`, matching what the docstring already claims. Cheap,
   truthful, and immediately makes the axiom audit agree with the prose.
2. **Restructure per §3b-cond item 5** — have the class carry the genuine
   *inputs* (semisimple Hochschild vanishing `HH^k(A) = 0` for `k ≥ 1`,
   Whitehead's lemma, the Wedderburn decomposition of `A`) and have the theorem
   *derive* the three clauses from them. This is the real fix and needs the
   Hochschild input the docstring names as missing from Mathlib.

Option 1 is the minimum; option 2 is the target. Either way the docstring must
end up describing the code.

## Note

`qou-mtcx` re-typed `e_block` / `E_infinity_00` / `integral` from `ℝ` to the
inherited `R` in this file (the proposition's own statement names that ring:
`E_∞^{0,0} = Z(A) = ⊕_λ R·e_λ`). That change is orthogonal to this gap and does
not affect it — the projection was there before and is there after.

---

## 2026-08-08 — option 1 applied (the minimum), option 2 still open

Done: `confinement_ident` **deleted** from the class, so it no longer carries the
theorem's conclusion; the theorem body is an honest `sorry` + `-- Ref:`. The
docstring now describes the code — including the history of the merge-not-removal
— and states the invariant a future reader can check: `#print axioms` **must**
report `sorryAx`, and if it stops doing so without the docstring changing, the
projection has returned.

Nothing consumed `confinement_ident` (grepped across `content/`), so the deletion
is contained to this file. `lean -DautoImplicit=false` compiles; the only
diagnostic is the expected `declaration uses 'sorry'`.

**Still open — the target.** The §3b-cond restructure: class carries the genuine
inputs (semisimple Hochschild vanishing `HH^k(A)=0` for `k ≥ 1`, Whitehead's
lemma, the Wedderburn decomposition), theorem *derives* the three clauses. Not
attempted, because it needs the Hochschild input this file names as absent from
Mathlib, and inventing a plausible-looking substitute would reproduce the exact
defect this bean exists to record. Bean stays open at `in-progress`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- **Regressed on main 2ae54ab40.** The option-1 fix of 2026-08-08 is undone: `ConfinementCategoricalContext` again carries `confinement_ident` (labelled "Missing input: confinement categorical ident"), stating the theorem's three-clause conclusion verbatim, and `confinement_categorical` returns `ctx.confinement_ident`. The file's own docstring (2026-09-03 section) records the tripwire firing. So the self-assuming projection is back and `#print axioms` shows no `sorryAx` (per that docstring; not re-run here, no Lean cache in this session).
- Disclosed, not fixed: caveat authorNote on `mass-theory/confinement-categorical.ts` (commit be175f860). Restoring the honest `sorry` (option 1) changes proof content, so it is asked of the owner. Option 2 (derive from HH^k vanishing + Wedderburn) still needs Mathlib input.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md): none found in this bean or the files it names.

## 2026-11-21 (honesty-audits sibling)

Honest `sorry` restored (owner ruling 2026-11-21, PR #8888, commit 863f384b9b4). Field `confinement_ident` deleted. lean-direct -DautoImplicit=false exit 0; #print axioms = [propext, sorryAx, Classical.choice, Quot.sound]. Statement unchanged; the theorem is now stated-not-proved. Stays open: the proof (semisimple HH vanishing + Wedderburn) is not formalised.
