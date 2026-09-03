---
# qou-1lb8
title: main is RED at QOU.Mathlib.Summary — triv_hecke/triv_wedderburn demoted to def, inferInstance left behind
status: in-progress
type: bug
created_at: 2026-08-24T15:00:40Z
updated_at: 2026-08-24T15:00:40Z
---

`lake build QOU` fails on origin/main (8367fafb26) at QOU/Mathlib/Summary.lean:100 — `failed to synthesize IwahoriHeckeAlgebra R 2 q`. Surfaced by /prepare-merge on claude/fivetwo-level7-ladder-numerators; inherited, not merge damage.

## The finding

`lake build QOU` **fails on `origin/main`** (8367fafb26):

```
✖ [5791/5797] Building QOU.Mathlib.Summary (4.0s)
error: QOU/Mathlib/Summary.lean:100:21: failed to synthesize
  IwahoriHeckeAlgebra R 2 q
```

Line 100 is inside `inventory_check`, whose proof term is
`⟨⟨inferInstance⟩, ⟨inferInstance⟩, ⟨inferInstance⟩, …⟩`.

## Cause

Commit **9a41a7ca57** — *"lean(HeckeAlgebra): demote triv_hecke and triv_wedderburn to `def` —
they discharged two chain steps globally"* — removed the two instances that those
`inferInstance` calls resolved against. `Summary.lean` was not updated in the same commit.

⚠ **Do not fix by handing `inventory_check` the trivial witnesses explicitly.** That would
reinstate precisely what 9a41a7ca57 removed, and it removed them for a stated reason: they
"discharged two chain steps globally", i.e. they were a vacuity. `inventory_check`'s
`Nonempty (IwahoriHeckeAlgebra R 2 q)` conjunct is asserting that a Hecke algebra structure
*exists* for arbitrary `R`, `q` — which, with the trivial instance gone, may simply no longer
be true at that generality. The right repair is a decision about what `inventory_check` should
claim, and it belongs to whoever owns the Hecke work, not to a passing branch.

## How it was found, and that it is inherited

Surfaced by `/prepare-merge` on `claude/fivetwo-level7-ladder-numerators` (the Roth arc), after
merging `origin/main` (420 commits). Confirmed inherited rather than merge damage:

- `Summary.lean` and `HeckeAlgebra.lean` are **byte-identical to `origin/main`** on the merged
  branch (`git diff origin/main -- <both>` empty);
- `Summary.lean`'s **82-module transitive QOU import closure has zero overlap** with the
  branch's seven changed `.lean` files (all Roth/Wronskian modules);
- `Summary.lean` itself did not change in `dd6565ba51..origin/main`, so the breakage arrived
  through its dependency.

## Why this keeps happening

Same shape as `qou-mnrd` (main red on its own float64 ratchet) and as the `lean-orphan-gate`
header's story of 37 modules silently ceasing to compile: **every workflow in this repo is
`workflow_dispatch`-only**, so nothing builds `main` unless a human or an agent asks. A
demotion from `instance` to `def` is exactly the change that breaks a distant `inferInstance`
and nothing local, which is what an unrun build is worst at catching.

The branch that found it is green in its own modules: all seven rebuilt with `.olean`s deleted,
exit 0, no errors, no warnings.
