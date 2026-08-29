---
# qou-mdlv
title: '`.md` vs `.lean` formula divergence is a CLASS, not a singleton — two confirmed, and the grep that finds them is a lower bound'
status: completed
type: task
priority: high
created_at: 2026-08-29T00:45:00Z
updated_at: 2026-08-29T07:10:00Z
---

Follow-on to `qou-aemx`. PR #5931 found that `em-coupling-chern-simons`'s
`.lean` states a formula its own `.md` names as superseded. The obvious next
question — singleton or class? — is answered: **class**, and this is how to
find more.

## The detector

Blocks whose `.md` *announces* its own supersession are greppable:

```sh
grep -rlniE "previously displayed|previously stated|superseded (form|version)|\
earlier form of this|this (proposition|theorem|lemma|definition) previously" \
  content/ --include=*.md
```

Six hits on `main` at 2026-08-29. Triaged:

| block | Lean | verdict |
|---|---|---|
| `em-coupling-chern-simons` | sibling | **divergent** — PR #5931 |
| `centered-hecke-variance-positive` | library decl | **divergent** — PR #5936 |
| `y-lambda-recipe-from-partition` | sibling | migrated to D, migration documented in the file — the good exemplar |
| `birthday-axioms-do-not-pin-the-birthday` | library decl | different class (an assertion became a check, no formula moved) |
| `mba-step09a-mass-identity` | none | no Lean to diverge from |
| `st-is-median-resummation` | none | no Lean to diverge from |

**2 of 4 blocks that have Lean are divergent.**

## This is a LOWER BOUND, and that is the important part

The grep only finds blocks whose prose *says* it was superseded. A block
silently corrected — no "previously read" sentence — will not match, and
nothing in the pipeline compares an `.md`'s mathematical content against its
`.lean`'s. So the true count is unknown and is at least 2.

Note also that "no sibling `.lean`" does **not** mean "no Lean": per AGENTS.md
§0a the `lean.ref` resolves to a library file when no sibling exists. Both
`centered-hecke-variance-positive` and `birthday-axioms…` are that shape. A
sweep keyed on sibling files alone would have missed the second confirmed case.

## Why it survives

`centered-hecke-variance-positive` shows the mechanism cleanly:

1. The module is an **orphan** (`qou-orph`) — `lake build QOU` never compiled
   it, so nobody had reason to open it.
2. But a compile would **not** have caught it either. The stale file type-checked
   fine; it was *internally* consistent and only *externally* wrong.
3. There is no automated `.md` ↔ `.lean` content comparison. The
   `proof-statement-integrity` criterion is the right home for one and does not
   currently do this.

So the drift is invisible to every existing gate. It ran 19 days here and
across at least two merges in the `em-coupling` case.

## What would actually close it

Not another grep. A criterion that extracts the displayed formula from an
`.md` and the stated proposition from its resolved `.lean` and compares them —
or, much cheaper and probably sufficient: flag any block whose `.md` was
modified more recently than its resolved `.lean` **and** whose `.md` diff
touched a `$$…$$` display block. That is mechanical and needs no semantics.

Not attempted here. Recorded as the honest next step rather than done badly.

## The cheap heuristic above is REFUTED — measured, 0 of 2 (2026-08-29)

I proposed it in this bean two hours before testing it. It does not work, and
the reason is worth more than the proposal was.

Measured over all 931 content blocks that have a sibling `.lean`: 100 have an
`.md` committed after their `.lean`. **Neither known positive is among them.**

| known positive | why the heuristic misses it |
|---|---|
| `em-coupling-chern-simons` | `.lean` last commit **2026-08-28**, `.md` **2026-08-22** — the `.lean` is NEWER. It was touched in an earlier tranche of this very arc (an annotation commit) without its staleness being fixed, which reset its timestamp. |
| `centered-hecke-variance-positive` | **no sibling `.lean`** — the decl is a library file reached via `lean.ref`, so the block is not in the 931 population at all. |

**The generalisable failure: commit order measures who was edited last, not
whether the two agree.** Any unrelated touch to a stale `.lean` — a lint pass,
an import fix, a rename, an added docstring — resets its timestamp and makes it
invisible. So the heuristic is *anti*-correlated with what it should find: the
more a stale file is churned, the less likely it flags. Case 1 is exactly that,
and the churn was mine.

Scope of this refutation, per AGENTS.md: **scope-(a)**, this construction alone
does not detect the class. It does not structurally exclude timestamp-based
approaches — only *last-commit ordering* as the signal.

(A harness bug also inflated the first run: `git show --format= -- <path>
<commit>` puts the commit after `--`, so git reads it as a path and emits
nothing, reporting 0 of 100 diffs as math-touching. Caught because 0 of 100 is
not a plausible number. Fixed before the conclusion above was drawn — the
0-of-2 result does not depend on it.)

## Open

- [ ] A detector for this class has to compare **content**, not metadata. The
      minimum viable version: extract the displayed formula(s) from the `.md`
      and the stated proposition from its **resolved** `.lean` (sibling OR
      library, per §0a — half the known positives are the library shape) and
      compare. That is real work, not a one-liner.
- [ ] A far cheaper partial: flag any `.md` containing a supersession sentence
      (the grep at the top of this bean) whose block has Lean at all, and
      require an agent verdict. Catches 2/2 known positives by construction,
      6 candidates corpus-wide today, and is honest about being a lower bound.
      This is what I would build first.
- [ ] Decide whether `proof-statement-integrity` should carry either as a
      mechanical criterion. Author call — it would flag existing blocks.


---

## CLOSED 2026-08-29 — detector built, and the class is smaller than feared

Owner approved building it. `content/pipeline/superseded-block-lean-audit.ts`
implements the cheap half recommended above: find blocks whose `.md` *announces*
a supersession, resolve their Lean, and hand the verdict to an agent. It does not
compare content and does not pretend to.

Both design points come from defects this arc actually hit. It **resolves library
`lean.ref`s**, not only siblings — half the known positives are that shape, so a
sibling-only scan misses them outright. And it prints **"this is a LOWER BOUND"**
in its own output, because a silently-corrected block carries no such sentence.

The refuted timestamp heuristic is recorded in the script's docstring so it is
not re-attempted from scratch.

### Result on `main`

**8 candidates → 4 with Lean:**

| block | verdict |
|---|---|
| `em-coupling-chern-simons` | **divergent** — fixed (#5931, #5946) |
| `centered-hecke-variance-positive` | **divergent** — fixed (#5936); library-resolved |
| `y-lambda-recipe-from-partition` | clean — migrated to D, migration documented in-file |
| `qdifference-kernel-prolongation-symbol` | **clean** — new candidate, checked |

The wider regex (`previously read`, `conjecture previously`) finds **8** where the
hand-grep in this bean found 6. The new one is the sharpest possible version of
this defect — its `.md` removes a clause it calls **"false as an identification of
q-difference modules"** — and its `.lean` never carried it. A negative, and worth
having as one.

So the class is **2 confirmed, both now fixed**, with a standing detector for
recurrence. What remains unmeasured is the silent-correction population, which by
construction this cannot reach; the real content comparison stays the open item
and is not attempted here.
