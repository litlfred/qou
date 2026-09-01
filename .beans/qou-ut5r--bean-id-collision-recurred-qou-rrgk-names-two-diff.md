---
# qou-ut5r
title: 'Bean ID collision RECURRED: qou-rrgk names two different beans; `beans show` silently serves the wrong one'
status: completed
type: task
priority: normal
created_at: 2026-08-29T18:58:12Z
updated_at: 2026-08-30T07:51:34Z
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


---

**RESOLVED 2026-08-30 — PR #6090** (`claude/bean-id-collision-guard-2026-08-30`).

Collision fixed: the **drain** bean renamed `qou-rrgk` → `qou-q0dr`, chosen by
measurement — the germ bean's ID is cited in four tracked files, the drain
bean's nowhere outside `.beans/`, with no intra-beans refs and no parent/child
links. `beans show qou-rrgk` now serves the germ bean, which is what all four
citations mean. Corpus-wide collisions **1 → 0**.

**The finding worth keeping is not the collision.** `scripts/check-beans.sh`
**already detected this** — failure shape 4 in its own header, exits 1 on a
duplicate, verified by reconstructing the collision in a temp tree. Nothing ever
ran it. Same finding `precommit-precision-warn.sh` records for
`precision-gates.sh`: a gate nobody invokes is documentation.

Wired as `scripts/precommit-bean-id-warn.sh`, warn-only `PreToolUse` beside the
precision hook. Duplicate-ID pass only: measured on 4332 bean files,
`check-beans.sh` is **40.4 s** against **0.024 s** for the narrow pass (1670×),
and bean commits are the most frequent kind here — the full validator in a
pre-tool hook would buy avoidance, not safety.

Deliberately **warn-only and never blocking**, matching the owner's 2026-08-25
choice for the precision hook (a push-side block was offered and declined). Do
not upgrade without asking.
