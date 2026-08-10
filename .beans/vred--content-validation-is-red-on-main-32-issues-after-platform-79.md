---
# vred
title: Content validation is RED on main — 32 issues, of which 10 are mechanical and 22 editorial
status: completed
type: bug
priority: high
tags:
    - qa
    - verification
    - content
created_at: 2026-08-08T16:35:00Z
updated_at: 2026-08-10T13:56:58Z
---

`bun run scripts/run-validate.ts content/quantum-observable-universe` on clean
`origin/main` reports **`✗ Invalid — 32 issue(s)`**. Verified on a bare
`origin/main` checkout with no local changes.

This matters beyond the count: "validate is unchanged from baseline" is the
standard verification sentence in this repo's PR bodies and the content half of
the §rule-10 gate that stands in for CI. It currently cannot be said truthfully.

## Not a regression in the corpus — a rule that stopped skipping

Earlier the same day the same command reported `✓ Valid — 10 issue(s)`. The
corpus did not change underneath it; the **checkers** did. Platform PR
litlfred/folio-assistant#79 — *"The citation check could never fire, and three
rules skipped kinds"* — began applying `uses`-resolution to block kinds that had
been silently skipped, `table` among them.

So all 32 are **true positives that were previously invisible**, and the jump is
the fix working. See `vbase` for why the same corpus commit can validate
differently in two environments at all; this is that hazard's first live
consequence.

## The split

**10 mechanical — `uses: [""]`.** Every one is a `notation-register-tableN-data`
block, `N = 1…10`:

```ts
export default table({
  label: "tbl:notation-register-table1-data",
  title: "Data table 1 from ",
  uses: [""],
  tags: ["extracted-table"],
});
```

An empty string is not a label; it resolves to nothing and always will. These
are machine-extracted table stubs whose generator failed to substitute the
source block — the truncated `title: "Data table 1 from "` is the same failure
showing through. Exactly 10 blocks carry `uses: [""]` corpus-wide, and exactly
the same 10 carry the truncated title.

**22 editorial — dangling `uses` targets.** Real labels that do not resolve:

    tm-inductive-construction          -> rem:generator-volume-decomposition
    tm-heavy-atom-examples             -> rem:generator-volume-decomposition
    term6-binding-density-table{1,2}   -> prop:term6-binding-density
    six-term-per-derivation-weights-3  -> rem:six-term-per-derivation-weights
    q-beta-form-a-n1-symbolic-table    -> prop:q-beta-form-a-n1-symbolic
    hecke-log-decomposition-table      -> prop:hecke-log-decomposition
    cyclotomic-strand-doubling-proof   -> lemma:cyclotomic-strand-doubling
    beta-decay-simulator-table         -> sim:beta-decay-half-life
    …

Each is a judgement call — the target may have been renamed, merged, or never
written — and `uses` is the **editorial** relation, so guessing a replacement
damages the signal every ordering metric is computed from (AGENTS.md is explicit
about this for the Lean direction; the same reasoning applies to inventing an
editorial edge). These want per-case triage, not a sweep.

## Recommended order

1. Drop the 10 `uses: [""]` entries. Removing an entry that is definitionally
   empty is strictly safe — the block's effective `uses` set is already empty —
   and it cannot invent an edge. It does not fix the truncated titles, which is
   a separate generator defect worth its own item.
2. Triage the 22 dangling targets individually.
3. Only then is "validate unchanged from baseline" sayable again.

## Deliberately not done here

Found while measuring an unrelated detector change (`vrfw`). Neither the 10 nor
the 22 were swept into that PR — a content fix inside a detector PR is exactly
the side-effect commit this repo has been cleaning up after.

---

## 2026-08-08 — RESOLVED. `✗ Invalid — 32` → `✓ Valid — 13`

All nine hard failures triaged and fixed. Seven were label repairs where the
target exists; two named a block that does not.

### Seven repairs — the target exists, the prefix or spelling was wrong

Each was determined from evidence in the corpus, not chosen:

| block | was | is | how it was determined |
|---|---|---|---|
| `term6-binding-density-table{1,2}-data` | `prop:term6-binding-density` | `rem:…` | only `rem:` exists |
| `cyclotomic-strand-doubling-proof` | `lemma:cyclotomic-strand-doubling` | `prop:…` | the proof block is `prf:…`; its statement is `prop:…` |
| `six-term-per-derivation-weights-table3-data` | `rem:six-term-per-derivation-weights` | `prop:…` | **siblings table1 and table2 already use `prop:` and resolve** |
| `beta-decay-simulator-table-data` | `sim:beta-decay-half-life` | `sim:beta-decay-halflife` | one hyphen; the simulator's own label |
| `tm-inductive-construction`, `tm-heavy-atom-examples` | `rem:generator-volume-decomposition` | `prop:…` | only `prop:` and `prf:` exist |

The table3 case is the cleanest evidence in the set: two sibling tables
extracted from the same source already point at `prop:`, so the third is a
straightforward copy defect rather than a judgement call.

Where a wrong label also appeared in the **title** — the generator wrote raw
labels into published prose, e.g. `"Table 3 from rem:six-term-per-derivation-weights"`
— it was corrected in the same edit. Fixing a label in one field and leaving the
same wrong label in another would be incoherent.

### Two drops — the target does not exist

`tbl:hecke-log-decomposition-table-data` → `prop:hecke-log-decomposition` and
`tbl:q-beta-form-a-n1-symbolic-table-data` → `prop:q-beta-form-a-n1-symbolic`.
Neither label exists anywhere in the corpus; the chapter manifests list only the
extracted tables.

The references were **dropped, not re-pointed.** `uses[]` is the editorial
relation — what a reader must have read — so guessing a plausible parent would
fabricate exactly the edge every ordering metric is computed from. A missing
parent is better recorded as missing.

So it *is* recorded: each block now carries an `authorNotes` caveat naming the
absent source, why the reference was dropped rather than redirected, and that
what is actually missing is the proposition the table was extracted from. The
debt is in the block, not only in this bean.

### Remaining — 13 warnings, none of them failures

Five `chap:particle-interactions` (a chapter not yet written), three "no Lean
declaration yet", one dangling remark, and four `.md` cross-references. These
predate the platform change; two surfaced with it
(`def:simple-objects-V`, `def:conway-normal-form`). They are `⚠`, so the gate is
green and *"validate unchanged from baseline"* is sayable again.

The truncated `"Data table N from "` titles on the ten `notation-register`
tables remain — the generator defect that produced them is still unfixed, and
is the one item from this bean's original list not closed.
