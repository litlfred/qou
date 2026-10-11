---
# qou-bje0
title: 544 beans cite the pre-rename content/ path; the rename bean closed without sweeping them
status: todo
type: task
priority: normal
created_at: 2026-10-11T07:33:48Z
updated_at: 2026-10-11T07:34:40Z
parent: qou-n4r9
---


Found 2026-10-11 while closing `qou-cxon`, whose own Lean citation was dead.

## The defect

`content/` **does not exist**. The `content/` → `folio/` rename landed as
`qou-yqko` (#7485 / #7487, merged 2026-09-29) and that bean is **`completed`** —
correctly, for the tree. It closed without sweeping the work-plan's own
citations, so the beans directory now points at a directory that is gone.

    beans naming `content/quantum-observable-universe` : 544 files

That matters more than a doc typo: `beans/defs/` is the agent work-plan and
AGENTS.md §path-6 makes it a corpus-grep path. A dead path in a bean sends the
next agent to a `No such file or directory` and invites the conclusion that the
artifact was deleted rather than moved.

## MEASURED — and a text match is NOT a verdict here, which cost me a wrong figure

Extracting with `git grep -oh 'content/quantum-observable-universe/[A-Za-z0-9_./-]*'`
gives **1700** distinct matches. My first pass judged all 1700 and reported
*"48 % resolve under folio/, 52 % resolve nowhere"*. **That was wrong**, and the
error was in the extraction, not the tree: **835 of the 1700 are artifacts** —
paths truncated by a line wrap, paths written with a `...` elision, and
directory-ish fragments with no file extension (`appendix-m`,
`appendix-mass-binding`).

Judging only the complete file paths:

    raw distinct matches             1700
      extraction artifacts            835   (truncated / elided / no extension)
      genuine file paths              865
        resolve under folio/          789   (91 %)
        do NOT resolve                 76   ( 9 %)

So `s|content/|folio/|` is the **right** rewrite for 91 %, not the 48 % my first
pass claimed — and the 9 % residue is what makes a blind sweep wrong rather than
merely incomplete. Samples of the 76: `appendix-standard-model/theta-qcd-framing-cp.lean`,
`appendix-surreals/b1-figure-8-row-theorem.lean`,
`climax-volume-mass/mobius-energy{,-proof}.lean`,
`brings-surface/mi-sw-abelianisation.lean`. Several are `.lean` files, so they
may have been renamed, moved into a different module, or genuinely retired —
each needs one reading, and rewriting them to `folio/` would turn a **dead**
path into a **wrong-looking-live** one, which is worse.

## 🟡 This is a sweep, so it asks — framed, not started

- **What it means.** Rewrite the 789 resolvable citations across ~544 bean
  files; read the 76 non-resolvers individually.
- **What it costs.** The 789 are mechanical and scriptable in one pass. The 76
  are ~an hour of reading. Beans are append-only ledgers, so per
  AGENTS.md this would collide with `main` on essentially every landing — the
  measured rate is `qou-brng` going un-mergeable about every 2.7 h — so it wants
  `scripts/bean-append-merge.py` at merge time and ideally one commit.
- **What it risks.** Touching 544 files in the tracker buries any real finding
  landing the same day under a mechanical diff — the exact cost §🟥 ASK THE
  OWNER names. And the 76 risk a wrong path that *looks* right.
- **What it commits to.** Nothing downstream; no number moves and no content
  changes.
- **Default if nothing happens.** The citations stay dead. Nothing breaks
  mechanically — no validator reads bean bodies — but every future corpus-grep
  through path 6 lands on missing files, and this is already how one agent
  (me) was misled today.

**Recommendation, my judgement not a finding:** do the **76 first and the 789
never**, or at least not as a tranche. The 76 are where the information is — a
`.lean` file that resolves nowhere is either moved, renamed or retired, and
that is worth knowing — while the 789 are legible to any reader who knows about
the rename, which a one-line note at the top of the migration status doc would
tell them more cheaply than 544 edited files.

**Precedent, and it is close:** `qou-utbr` is the same shape one directory over
(`.beans/` → `beans/defs/`) — the store moved, the instructions pointing at it
did not. It is **`completed`**, and its own closing note records the residue as
sitting in **open PR #7484**; measured today, **16** skill files still carry a
`.beans/` path. So two renames closed on the tree while their citation surfaces
stayed behind, and in that case somebody opened a PR for it.

🛑 **Corrected before shipping:** this paragraph first said *"its ~168-file
skills sweep is also still waiting on the owner"*. Both halves were wrong. The
**168** is AGENTS.md's count of further `.md` files across the whole tree, not
skills — the skills surface is **16**. And it is not waiting on the owner; it is
in a PR. The stale figure came from reading AGENTS.md's note rather than
measuring, which is the failure this whole bean is about.
