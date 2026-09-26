---
# qou-vexw
title: The 382-file broken-sibling list predates the v4.24 lambda reservation, so it undercounts
status: todo
type: task
priority: normal
created_at: 2026-08-16T11:50:38Z
updated_at: 2026-08-16T11:51:17Z
---

Found while trying to verify an appended section in
`content/quantum-observable-universe/mass-theory/frobenius-codim-universal.lean`
(PR on branch claude/agent-discussions-queue-gibk4e).

That file does not parse under the pinned toolchain, on `main`, unmodified:

```
main-fcu.lean:37:19: error: unexpected token 'λ'; expected '(', '[', '_', '{', '⦃' or identifier
main-fcu.lean:38:42: error: unexpected identifier; expected 'lemma'
main-fcu.lean:46:63: error: unexpected token 'λ'; ...
main-fcu.lean:112:60: error: failed to synthesize OfNat ℝ 0
```

Reproduced by `git show origin/main:<path>` into a temp file and running
lean-direct against the restored oleans — byte-identical first errors to the
working copy, so it is not branch drift.

**But it is NOT on the genuine-breakage list.**
`docs/audits/2026-06-28-content-sibling-compile-sweep.genuine.txt` has exactly
382 entries and `frobenius-codim-universal` is not among them. So the file was
green when that sweep ran and is red now.

**The cause is almost certainly the toolchain bump, not authoring drift.**
Bean `5wld` records that v4.24 made `λ` a reserved token and that
`SkewSYT.lean` uses it as the partition variable in 213 places. Same class
here: `∀ λ, …` and `(λ : Λ)` binders. The sweep was taken 2026-06-28, before
the repo moved to `lean-v4.24.0` (`lean-toolchain`), so **the 382 number is a
pre-bump census and understates today's breakage by an unmeasured amount.**

Two things to do, in order:

1. **Re-run the sweep under the current toolchain** and regenerate
   `*.genuine.txt`. Until that happens, every downstream statement keyed to
   "382" — bean `2ti7`'s attack order, the per-chapter density counts
   (mass-theory 72, quantum-observable-universes 63), and any claim that a
   given file is *not* known-broken — is reasoning from a stale census. Note
   `2ti7` is `completed`, so nobody is watching this number.
2. **Then decide the λ class as one decision, not per file.** It is mechanical
   (rename the binder) and hits an unknown number of files; `5wld` already
   scoped the identical fix for one 922-line file. Batch it.

**Why CI did not catch it:** `lean-content-siblings.yml` is diff-scoped — it
gates siblings a PR *touches*, so a toolchain bump that reddens files nobody
edits passes silently. And under the 2026-06-30 Actions-billing directive the
workflow is `workflow_dispatch`-only anyway.

**Cheap repro** (~2 s once oleans are restored; the whole-file run needs no
`lake build`):

```bash
export PATH="$HOME/.elan/bin:$PATH"; export ELAN_TOOLCHAIN=lean-v4.24.0
export LEAN_PATH=$(ls -d $PWD/.lake/packages/*/.lake/build/lib/lean | tr '\n' ':')
lean content/quantum-observable-universe/mass-theory/frobenius-codim-universal.lean
```

Note the olean dirs end in `.lake/build/lib/lean`, not `.lake/build/lib` — the
shorter path is what `AGENTS.md` implies and it silently yields
`unknown module prefix 'Mathlib'`.

**Scope note (a):** this is "the census is stale", not "the corpus is more
broken than believed" — the delta is unmeasured, and step 1 is what measures
it. It could be small.
