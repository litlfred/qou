---
# qou-bje0
title: 544 beans cite the pre-rename content/ path; the rename bean closed without sweeping them
status: todo
type: task
priority: normal
created_at: 2026-10-11T07:33:48Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---


Found 2026-10-11 while closing `qou-cxon`, whose own Lean citation was dead.

## The defect

`content/` **does not exist**. The `content/` → `folio/` rename landed as
`qou-yqko` (#7485 / #7487, merged 2026-09-29) and that bean is **`completed`** —
correctly, for the tree. It closed without sweeping the work-plan's own
citations, so the beans directory now points at a directory that is gone.

    beans naming `folio/quantum-observable-universe` : 544 files

That matters more than a doc typo: `beans/defs/` is the agent work-plan and
AGENTS.md §path-6 makes it a corpus-grep path. A dead path in a bean sends the
next agent to a `No such file or directory` and invites the conclusion that the
artifact was deleted rather than moved.

## MEASURED — and a text match is NOT a verdict here, which cost me a wrong figure

Extracting with `git grep -oh 'folio/quantum-observable-universe/[A-Za-z0-9_./-]*'`
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

## 2026-10-11 — owner authorised "sweep the 76". DONE, and the 76 were not what this bean said

The sweep is applied, and reading each path changed the shape of the problem
twice. Neither change is in the framing above.

### Change 1: the dead paths are NOT mostly in bean bodies — they are in the WATCHER QUEUES

My rewrite over `beans/defs/*.md` retargeted **2** occurrences. The other 36
distinct paths live in `beans/defs/*-watcher-queue.json` — the integration
watchers' work queues, which are **machine-consumed data**, not prose, and which
the `beans ≠ sidecars` rule says are not beans at all despite sitting in
`beans/defs/`. A `.md`-only glob cannot see them, which is how I measured "544
beans" and then retargeted two files.

### Change 2: the right discriminator is the entry's STATUS, not the path

    queue                                     dead-path entries   status
    canonical-watcher-queue.json                      1           wontfix
    compute-integration-watcher-queue.json           30           wontfix
    detangler-integration-watcher-queue.json         21           wontfix
    proof-integration-watcher-queue.json             43           resolved
    devils-advocate-watcher-queue.json               40           needs-author

**95 of 135 are CLOSED** — `wontfix` or `resolved`. Those are records of what
was audited at the time, and rewriting their paths would falsify the record.
**Left untouched**, same call as the `4.66e6` drain precedent.

**All 46 entries of `devils-advocate-watcher-queue.json` are `needs-author`** —
open items awaiting the author, citing files that do not exist. *That* is where
the dead path is a live defect, and it is a sharper finding than this bean's
original framing: not "544 beans have stale citations" but **46 open work items
pointing at nothing**, in a queue AGENTS.md §4 lists as idle-backlog priority 3.

### Applied

Of the **71** distinct paths those 46 entries cite, **65 resolved to a unique
file** and were retargeted; **6** were left, for a reason below. Verified after:
all five queues still parse, `items` counts unchanged, **every entry's `status`
unchanged**, and all 65 new paths exist on disk (0 missing).

**The moves are two-stage, which is why a prefix rewrite would have failed.**
The dominant pattern is not `content/` → `folio/` alone but the old
`particle-interactions/` chapter splitting into `nuclear-interactions/` (28) and
`knots-particles-confinement/` (9), plus `mass-endomorphism.ts` moving into its
own directory. A blind `s|content/|folio/|` fixes **none** of those — it would
produce `folio/…/particle-interactions/…`, a path that has never existed. This
is the 9 % residue the framing above warned about, and it turned out to be the
*majority* of the 76.

### The 6 left, and they are NOT defects

All six name a **`.lean` sibling** of a block that exists. Resolved properly —
my first attempt was wrong, see below — every one of the six has a `lean.ref`
that resolves to a **library** declaration:

    b1-figure-8-row-theorem            -> QOU/AppendixSurreals/B1Figure8RowTheorem.lean   b1_figure_8_row
    depth-2-identification-bloch-suslin-> QOU/AppendixSurreals/Depth2IdentificationBlochSuslin.lean
    knot-factor-frobenius-pairing      -> QOU/BraidKnot/KnotFactorFrobeniusPairing.lean
    flavor-split-substrate             -> QOU/HadronicMass.lean                           flavor_split_substrate
    cyclotomic-l-value-decomposition   -> QOU/BraidKnot/CyclotomicLValueDecomposition.lean
    confinement-topological            -> QOU/Interactions/GramIndefinite.lean:201        gram_indefinite_witness

So the **absent sibling is CORRECT** — AGENTS.md §0a's "no shadowing stubs" rule
forbids creating one when the library declaration exists. Rewriting these to a
`folio/…/<block>.lean` would invent a path that must not exist. Left as-is
deliberately.

🛑 **Two of my own resolution errors, caught by checking rather than by review.**
First, I built the library path by `tr '.' '/'` on the whole `lean.ref`, which
turns the *declaration name* into a path segment — that reported 5 of 6 as
"library file ABSENT too", pure artifact. Fixed by trying each dotted **prefix**
as the module. Second, even then `confinement-topological` read as missing,
because the prefix search found the `QOU/Interactions.lean` aggregator and
stopped; the declaration is in `QOU/Interactions/GramIndefinite.lean`. One grep
settled it. Had I reported either, I would have filed a dangling-`lean.ref`
defect against a corpus that is correct.

### What is left, and the recommendation above is now obsolete

The framing above recommended *"the 76 first and the 789 never"*. The 76 are
done. The **789** are unchanged, and the case for leaving them is now stronger
than when I wrote it: the 95 closed queue entries are records that *should* keep
their historical paths, and most of the rest are prose in bean bodies that no
tool reads. **Status: `todo`**, holding only the 789 question, which nothing
depends on.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Unchanged: only the 789-path question remains, which this bean already recommends leaving. Nothing depends on it.
