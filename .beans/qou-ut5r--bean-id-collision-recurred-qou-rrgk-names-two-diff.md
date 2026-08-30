---
# qou-ut5r
title: 'Bean ID collision RECURRED: qou-rrgk names two different beans; `beans show` silently serves the wrong one'
status: todo
type: task
priority: normal
created_at: 2026-08-29T18:58:12Z
updated_at: 2026-08-29T18:58:44Z
---

**Measured on `origin/main` 2026-08-29.** Exactly one bean ID is carried by two
different files:

```
.beans/qou-rrgk--germ-viability-probe-is-the-em-word-holonomy-germ.md   (completed)
.beans/qou-rrgk--drain-329-stale-q-0-anchors-across-witnesses-ratch.md  (todo)
```

They are unrelated beans: one is the α_EM germ-viability decision closed
2026-08-29T17:36Z, the other a q₀-anchor drain.

**Why it matters — the failure is silent.** `beans show qou-rrgk` resolves to
the **drain** bean and prints nothing about the other, so the germ bean is
unreachable from the CLI by its own ID. An agent handed the ID "qou-rrgk" reads
a q₀ drain task and has no signal that it is looking at the wrong bean. That
happened in this session: commit `13cb825068` says "Decides bean qou-rrgk" and
`beans show qou-rrgk` shows a `todo` drain bean, which reads as a commit
claiming to close something it never touched.

**Why this is a REGRESSION, not a leftover.** `qou-xqno` (completed) measured
the duplicate-ID population at 2 (`qou-x4qm`, `sp06`) and drained it. This
collision was **created 2026-08-29T16:24Z**, i.e. after that cleanup. So the
create-guard added under `qou-2ryn` does not close this class: per AGENTS.md the
guard is an **exact-title existence check**, and these two beans have completely
different titles. Nothing checks the *ID*.

**Suggested fix (not done here — this bean is the report).**
1. Rename one file's ID. The germ bean is `completed` and its ID is cited in a
   landed commit message and an audit doc, so renaming the **drain** bean (still
   `todo`, no landed citations found) is the lower-blast-radius choice.
2. Add an ID-uniqueness check next to the title guard, so `beans create` cannot
   mint an ID that an existing file already carries. A title guard cannot catch
   this; the collision is in the random ID, not the slug.

**Blast radius if left.** Low but sharp: any agent citing `qou-rrgk` gets the
wrong bean with no error. Two audit docs
(`2026-08-29-alpha-em-germ-viability-live.md`,
`2026-08-29-alpha-em-measure-arc-workplan-update.md`) and at least one commit
cite the ambiguous ID.

Found while picking up the germ work on branch
`claude/standard-panel-qou-derivation-ixuolx`; recorded in the header of
`QOU/MassTheory/EmGermMomentVanishing.lean` so a reader of that file is warned.
