---
# qou-k448
title: 'Sweep: ''X = X := rfl'' + non-compiling un-sidecar''d library Lean files'
status: todo
type: task
created_at: 2026-08-08T08:35:57Z
updated_at: 2026-08-08T08:35:57Z
---


Surfaced 2026-08-08 on PR #4727. `QOU/Eightfold/WeylInvarianceQDeformation.lean`
was **red on `main`** (two `No goals to be solved`) and its headline declaration
was `cartanMatrix_A2 = cartanMatrix_A2 := rfl` — a tautology with unused `q`
binders — while three `.md` blocks cited it as proving q-independence. It was
found **by accident** (opening the file to check an adjacent `native_decide`),
not by any checker.

Root cause is structural, not incidental: a standalone library `.lean` under
`content/**/lean/QOU/**` with no `<block>.qa.json` sidecar is not covered by
`lean-content-siblings.yml`, and with CI auto-triggers disabled repo-wide
nothing reads it at all. A file can be red indefinitely.

Both halves are mechanically detectable:

1. **`X = X := rfl` with unused binders.** The unused-variable linter already
   fires on these — the signal exists and nothing consumes it. Cross-check
   against `lean-vacuity-axiom-audit.ts`, which keys on `: True` but (as far as
   this session saw) not on reflexivity-on-a-constant.
2. **Does it compile at all?** `scripts/lean-verify.sh` over every
   un-sidecar'd library file, against the restored `lake-cache/qou-<slug>`
   oleans. This session verified 5 Eightfold files in a few minutes each, so a
   full pass is feasible but not free.

Suggested scope: run (2) first — a red file is strictly worse than a vacuous
one, and the count is the interesting number. Then (1) as a checker addition
rather than a one-off sweep, so it does not regress.

Related: bean `qou-8fl1` item 3 (`Sym2Gate.lean` vacuous — compiles, and the
chapter prose already labels it honestly) and item 4 (`native_decide`,
discharged on PR #4727).
