# Claude Code — Quantum Observable Universe

## CRITICAL: READ SKILLS BEFORE ACTING (Anti-Guessing Rule)

**DO NOT GUESS WORKFLOWS.** This repository has highly customized, non-standard workflows for building Lean, preparing merges, syncing with siblings, and validating. 
When the user asks you to perform a task (e.g., "run prepare-merge", "set up lean", "audit compute"), **you MUST FIRST read the corresponding skill file in `.claude/skills/local/*.md`** before taking any action.

**Why this is strictly enforced:** Agents frequently fail in this repository by running standard commands (like `lake build` from scratch) instead of following the explicit repo skills (which use custom caches and scripts). This wastes the user's time.

**Required Action:** Before executing any multi-step task or slash command, run `ls .claude/skills/local/` and `view_file` on the relevant `.md` file. Follow its instructions exactly. NEVER guess.

## User accessibility

The repo owner is physically disabled and types with difficulty.
Adapt ALL responses accordingly:
- **Short answers.** One-liners when possible.
- **Offer choices as numbered lists** so the user can reply "1" or "2".
- **Run commands proactively** — don't ask "shall I run X?", just run it.
- **Branch/commit/push without asking** unless destructive.
- **Interpret terse/misspelled input charitably** — infer intent, don't ask for clarification on typos.
- **Mirror every `AskUserQuestion` to chat BEFORE calling the tool (STRICT, 2026-06-09).** Write the question text, every option label, and every option description (with full evidence + trade-offs + math context) as plain chat prose *immediately above* the `AskUserQuestion` tool call. The structured tool call must mirror what is already in the chat — it does not replace it. Reasons:
  - **Cancellation/dismissal safety.** If the user dismisses the structured UI, accidentally cancels, or the question component fails to render, the full context survives in the transcript. No round-trip needed to re-state options.
  - **Chat log = durable record.** The transcript is what sub-agents, future sessions, and the user re-reading later all consume. The structured UI is ephemeral; if it isn't in the chat, it didn't happen.
  - **Math / LaTeX legibility.** Inline math (`$...$`), display math (`$$...$$`), tikzcd, multi-line equations, and fenced code blocks render correctly in markdown chat but are mangled inside the `description` field of structured options. Put the math in the chat prose, keep the structured `description` short.
  - **Shorter structured options.** With full context already in chat, structured option labels + descriptions can be tight 1-line summaries — easier to scan, fewer accidental mis-picks, the multiSelect chip UI stays usable.
- **Give rich context for every `AskUserQuestion`.** A label and one-line description is not enough. Each question must include (primarily in the chat mirror above, with only essential summaries or preview fields inside the structured options):
  - **Evidence** — exact file paths, line numbers, counts, current state vs proposed state. Quote the failing line, name the offending witness, link the blob URL.
  - **Per-option trade-offs** — cost (time, lines changed), risk (reversibility, blast radius), scope (this branch vs follow-up branch). State what the choice actually buys and gives up, not just what it does.
  - **Concrete consequences** — "if you pick this, X happens; you'll then need Y" — so the user can pick without scrolling back through context.
  - **`preview` content** for options that benefit from side-by-side comparison (diff snippets, file-tree mockups, code samples, before/after numbers).

  This rule exists because terse questions force the user to type follow-ups asking for the context that should have been provided up front, which is the most painful kind of friction. When in doubt, err toward more context in the chat mirror (where math + multi-paragraph evidence render correctly), less in the structured-option `description` field (which mangles math and gets clipped in the chip UI).
- **Default `AskUserQuestion` to `multiSelect: true` + 🟡 marker (2026-05-19).** The repo owner is physically disabled and types with difficulty (see top-of-section reminder). Single-select questions force the user to either pick exactly one option or type "1, 2" as free text — neither is accessibility-friendly. Default rules:
  - **Always set `multiSelect: true`** unless the choices are strictly mutually exclusive (e.g. "switch branch to X" vs "switch branch to Y" — picking both is incoherent). 80% of decision points are not mutually exclusive ("which of these should I do?" — answer is usually "1 and 3"), so multi-select is the safer default.
  - **Prefix the question with 🟡** to mark the agent as waiting / blocked on input ("🟡 [Yellow Circle] Waiting on user — …"). The yellow circle is the agent-state symbol for "blocked, needs user input"; using it consistently lets the user scan the chat history and find every pending decision point.
  - **Allow optional notes** in the question phrasing ("Pick all that apply; add 'Other' with a free-text note if needed.") so the user can amend a chosen option without typing follow-ups.
  - Single-select is OK only when the chosen options describe genuinely mutually-exclusive actions (e.g. "merge approach: rebase OR merge-commit"). Even then, prefer multi-select if "do both later" is a reasonable answer.
- **Coordinate intent with sibling branches on every new workplan (2026-05-19).** When opening a new branch or starting a substantive new tranche of work:
  - **List active sibling branches** via `mcp__github__list_pull_requests` (open PRs) + `mcp__github__list_branches` (active claude/* branches), filtered to recently-updated.
  - **Post a brief intent comment** on each PR whose scope overlaps your planned work (same chapter / same Python or Lean file / same domain). 1-3 sentences max — "Starting <theme> on <branch>; will touch <file>; flag conflicts to me." Don't post on every sibling — only the genuinely-overlapping ones, and don't make too much noise on the PR.
  - **When critical findings land in your branch** that a sibling is waiting on (e.g. you discover the upload branch should use force-with-lease, and another sibling is about to push to a similar branch), proactively comment on the sibling PR with the finding. Don't wait for them to step on the rake.
  - **During idle (per the 5-min idle trigger)**, also check sibling PRs for coordination updates / relevant commits. Use `mcp__github__pull_request_read get_comments` on the active siblings; new comments addressed to "all watchers" or referencing your branch's scope are actionable backlog.
  - **Measured research-overlap is PERMITTED (owner relaxation, 2026-07-18).** The "don't double-build" rule below is relaxed for **genuinely open research topics** — an unsolved math/physics question where the *outcome is unknown and multiple routes are viable* (e.g. the α_EM per-loop measure derivation, a Stokes-constant extraction, a Δ_λ closure, a c_k identification). A **different agent context may reach the solution by a different route**, so it is acceptable to work such a topic even when a sibling is already on it. This is **a small relax, not a licence to duplicate**:
    - **Only open-outcome research qualifies.** *Mechanical / settled* work — sweeps, sidecar/witness regeneration, refactors, wiring an already-derived result, doc-currency, migrations — has one right answer and **one owner**; do **not** overlap it. The test: is the answer *unknown* (research) or merely *not-yet-typed* (mechanical)? Only the former may overlap.
    - **Still post intent, and state your distinct angle.** Comment on the overlapping sibling PR naming the parallel attempt and *how your route differs* ("you're on the torsion-determinant route; I'm testing the Bloch-group lift") so the overlap is deliberate and visible, never accidental.
    - **Converge on landing.** When one route lands a result, the other re-scopes to *verify / extend / refute* it rather than re-deriving — and cites it. Two independent confirmations of an open result are valuable; two identical re-derivations are waste.
- **Structured branch names (2026-05-19).** All new branches follow the existing pattern:
      claude/<theme>-<utc-ymd>
  Theme is hyphenated, lowercase, ≤ 40 chars, descriptive of the work-tranche scope (e.g. `detangler-bib-followup-batch`, `i12-cluster-a-audit-regex-unique-decls`, `upload-bib-papers`). Date is the start day. Don't deviate from this pattern — it's what `coordinate.md` and the upload-branch idempotency rely on.
- **Combine related work into one branch / one PR. Minimize their creation.** Default to stacking commits on an existing in-flight branch when the new work shares a theme (detangler structural cleanup, watcher infrastructure, doc currency, etc.) with what's already there. Before creating a new branch, check whether the active branches host related scope — if yes, switch to that branch and add a commit there. Only spin a new branch when the work is genuinely unrelated (different domain) or when the existing branch is already large enough that adding more would hurt reviewer comprehension. Reviewers prefer one coherent 6-commit PR to six 1-commit PRs covering the same theme. Mirrors `.claude/skills/local/integration-watcher.md` §0a item 1 and item 3 ("cluster aggressively", "group a lot").
- **Small-moderate fixes for related bugs ride on the active PR.** When working on PR X surfaces a bug in adjacent code (a sibling probe, an upstream stale witness, a producer-vs-manifest mismatch, an invalid Hecke representation in a related script, etc.), default to fixing it inline on PR X — do **not** spawn a new branch / PR Y unless the fix is large or in a clearly unrelated domain. The reviewer is already loaded on the area; an extra 1-3 commit fix is far cheaper to review than a separate PR that re-establishes the context. State the bug + chosen scope in the PR description or a top comment so the reviewer sees the rationale; file the lower-priority leftover (e.g. "centralise the Hoefsmit utility module") as a follow-up. This rule complements "combine related work into one branch" above, applying it specifically to bugs surfaced mid-review.

This repository is a formal mathematics paper with:
- **Content objects** (`.ts` + `.md` + `.lean` file triples) as authoritative source
- **LaTeX** as a rendering target (generated from content objects)
- **Lean 4** formalization linked to content objects

## Critical-distance license (standing red-team permission, 2026-06-10)

Agents have standing permission — and, when asked for assessment, an
affirmative duty — to:

- **Challenge the framework's physical claims on the merits.**
- **Flag suspected numerology, overfitting, hidden degrees of freedom,
  or post-hoc rationalization plainly** ("this looks fitted") — in
  chat, without ceremony.
- **Give outside-view forecasts of reception, publishability, and
  rigor without softening.** Flattery is a disservice to the author;
  the hard part said early is cheaper than the hard part said by a
  referee.
- **Voice skeptical assessments in chat WITHOUT first running the
  corpus-grep checklist** (defined under §Before declaring "open"
  math / questions / gaps (STRICT) below). That
  checklist gates formal "open item" declarations in durable
  artifacts (audit docs, content blocks, Lean comments, PR
  descriptions) and factual "X is open in the corpus" claims; it
  does not gate critical discussion.

Read the author's *messages* charitably (per User accessibility
above); read the framework's *claims* adversarially. The two rules
do not conflict — one governs input interpretation, the other
governs assessment.

## Parallel exploration is valuable — cross-agent duplication is NOT waste (owner directive, 2026-07-17)

**It is explicitly OK to work a problem in parallel with, and even to
duplicate, what another agent (sibling branch / prior session) is doing
or has done.** A different agent carries a different context — different
files loaded, different framing, different corpus paths walked — and
that difference is exactly what finds the solution the other agent
missed. Redundant independent attacks on the same open problem are a
*feature* of the multi-agent workflow, not a coordination failure.

Concretely:

- **Do not decline a probe/derivation solely because a sibling is on the
  same front.** Coordinate (post intent, per the sibling-branch rules)
  and then attack it with your own context. Two independent derivations
  of the same result strengthen it; two independent *failures* on the
  same route strengthen the negative.
- **This does NOT loosen the anti-laundering / corpus-grep disciplines.**
  Before declaring an item "open" you still run the corpus-grep checklist
  (a prior agent may have *closed* it — duplicating *effort* is fine,
  but re-declaring a closed item open is still a flag). "OK to duplicate"
  means it is fine to *re-derive, re-test, or re-attack* — not fine to
  ignore an existing proof and pass a fresh fit off as new.
- **This is distinct from "combine related work into one branch."** That
  rule governs a *single* agent not fragmenting *its own* in-flight work
  across many branches. It does not tell you to stand down because
  *another* agent is nearby. When in doubt: coordinate intent, then
  proceed in parallel.
- **Scope note.** This complements the Critical-distance license above:
  independent parallel assessment — like independent adversarial
  assessment — is a source of robustness. The cheapest way to catch a
  wrong turn is a second agent walking in from a different direction.

## Agent work-plan policy (STRICT)

Every session must run from a **prioritized work-plan** maintained
as **beans** — the [`beans`](https://github.com/hmans/beans) CLI
flat-file issue tracker (data under `.beans/`; install via
[`scripts/install-beans.sh`](scripts/install-beans.sh)). See
[`.claude/skills/local/todo-manager.md`](.claude/skills/local/todo-manager.md)
and [`.claude/skills/local/bean-coordination.md`](.claude/skills/local/bean-coordination.md).
The plan is the agent's source of truth for "what next" — not the
user's last message, not the most recently mentioned file.

> **Migration note (2026-06-19).** Beans **supersede** the older
> `TodoWrite`-tool / `todos/*.json` work-plan mechanism. Wherever this
> document still says *"TodoWrite list"* / *"todo list"* below, read it
> as *"create / maintain beans"* (`beans create "<title>" --type task`,
> `beans update <id> --status in-progress|completed`). The
> `beans ≠ sidecars` rule holds: QA / `.qa.json` / `.witness.json`
> queues are **not** converted into beans. (Part of the qou side of
> the Folio-Assistant Infrastructure Migration — the `miga` epic.)

1. **Start a bean list at session start.** As soon as you have
   enough context (after reading the user's first request, the
   SessionStart hooks, and the current branch / PR state), create a
   session milestone bean plus child task beans decomposing the
   requested work (`beans create "Session: <branch/goal>" --type
   milestone`; one `--type task` per concrete step). If the request
   is one trivial task, you may skip — but any time there are ≥ 2
   distinct steps, create the beans.

   **Check before you create (STRICT).** `beans create` is **not**
   idempotent — it mints a fresh ID on every call and dedupes on
   nothing, so re-entering this step duplicates the entire plan
   instead of no-op'ing. Before **every** `beans create`, including
   the session milestone, run the exact-title existence check in
   [`local/todo-manager` §Check before you
   create](.claude/skills/local/todo-manager.md); on a match, claim
   the existing bean with `beans update <id> --status in-progress`
   rather than creating a second one. History: an unguarded re-run of
   this very step ~980 times on 2026-08-04 produced **14,688**
   duplicate beans — 92 % of every open bean — which starved the
   §4 idle-backlog policy of signal, left an already-proved core at
   `todo`, collided with the IDs of 15 real beans, and corrupted a
   later agent's corpus-grep badly enough to nearly land a false
   correction in a PR body (bean `qou-2ryn`).

2. **Queue, do not pivot.** When a new request, review comment, or
   sibling-PR ask arrives mid-session, **append** it to the plan in
   priority order — do not abandon the in-progress task. Pivot only
   when the user explicitly says so ("stop", "drop that", "switch
   to X first"). Inferred urgency is not enough.

   > **Stalled-claim takeover (standing policy, 2026-08-15).** Assume
   > agents can stall — a container is reclaimed, a session dies, a
   > branch is abandoned mid-task. A bean at `in-progress` whose
   > **backing branch has had no new commit for > 3 h** is presumed
   > abandoned and MAY be taken over. **Scope (read or you will clobber
   > live work):** this applies ONLY to the branch backing a *live
   > in-progress bean* — NOT to the thousands of long-idle `claude/*`
   > branches, which are permanently stale and are never takeover
   > targets by age alone. Before taking over: confirm the branch is
   > genuinely stale (last commit > 3 h AND no newer PR activity / no
   > in-flight CI — a long build is not a stall), re-claim the bean with
   > a `--body-append` noting the takeover + the stale branch's last
   > SHA, and continue from that branch's tip or from `main` — **never
   > force-push over a sibling's branch.** This is the one sanctioned
   > exception to "never touch a sibling's claim". Protocol:
   > [`local/todo-manager` §Stalled-claim takeover](.claude/skills/local/todo-manager.md).

3. **Say which bean you are on — every turn.** Claiming a bean records
   the work; *reporting* it is what lets the user steer and a sibling
   session avoid you. Both are required.

   **When you begin work on a bean**, open that turn by naming it and
   what you are attempting — before the first tool call, not after the
   work lands:

   > **Starting `fwr7`** — retargeting the seven edges the forward-ref
   > arc left alone, because the edge is wrong rather than the block's
   > position.

   **End every turn** with the beans you touched and what is next. One
   line each, **up to 50 words** — enough to act on without opening the
   file:

   > **Beans**
   > - **worked** `fwr8` — Re-baselined both endpoints with the fixed
   >   parser: the arc is 274 → 195, not 274 → 192. Corrected my own
   >   claim that the start was understated; only post-mid-arc figures
   >   are short by 3.
   > - **next** `fwr7` — Retarget seven mis-aimed edges. Two are now
   >   confirmed detangler findings rather than reader reports, which
   >   raises their priority.

   What makes the report worth reading:

   - **A name and five words is not a synopsis.** Say what changed, or
     why the next item is next. "Retarget seven edges" is a title;
     "two are now confirmed findings, which raises their priority" is
     a reason.
   - **"Next" is your judgement, not a fact.** Beans carry no priority
     order beyond what an agent asserts — so say why, and expect to be
     overruled.
   - **Prefix across repos** (`qou/fwr7`, `fa/fsl7`) when a turn spans
     both this repo and folio-assistant.
   - **Report unclaimed work as unclaimed.** If you did durable work
     without a bean, say so and open one. That omission is the failure
     this exists to catch — a manifest-parser bug was found, fixed,
     tested and merged before anyone noticed it had never been claimed.

4. **Parallelize independent tasks.** When two queued tasks have no
   dependency between them (e.g. one Lean fix + one .md edit on
   different blocks), batch them into a single response with
   parallel tool calls. Use background `Agent(run_in_background=true)`
   for independent research / triage that does not block the
   foreground task.

5. **Work the queue while idle.** When you are waiting on a
   long-running script, a background agent, a Lean build, or a CI
   run, pull the next pending todo and work on it. Never just sleep
   or poll. (Exception: if the only remaining todos depend on the
   in-flight task, idle and wait for the notification.)

   **Long-compute logging discipline (2026-05-20):** any background
   Python script expected to run > 5 minutes (mass table beyond
   ⁴He, A-operator extracts at H_9+, joint-tower SDP, PSLQ basis
   > 30, anything calling `markov_peel.tr_M_atomic` with A ≥ 4)
   **must** be launched with progress logging enabled and a teed
   log file:

   ```bash
   python3 -u script.py 2>&1 | tee /tmp/<script>.log
   ```

   `-u` defeats stdout buffering; `tee` captures the log for
   post-hoc bottleneck inspection. The script itself must emit
   periodic progress lines (every ~10 sec or ~5% of work) including
   wall elapsed + ETA. **When the script ends silently with 0-byte
   output and no completion notification within expected window**,
   assume it crashed — re-launch with stricter logging, do not
   silently abandon. Always report bottlenecks in the end-of-task
   summary ("⁶Li at H_{18} took 18 min wall, dominated by
   markov_peel.tr_M_atomic"). Full discipline:
   [`.claude/skills/local/compute-audit.md §Long-compute logging
   discipline`](.claude/skills/local/compute-audit.md).

   **5-minute idle trigger (2026-05-19).** If you have produced no
   substantive output for > 5 minutes (just TICK heartbeats or
   empty acks), start processing backlog automatically — do not
   wait for the user to prompt. Walk this priority order:

   1. **Current session todos** (TodoWrite list for this session).
      Top of the queue first.
   2. **Current PR todos** — the open PR's body checklist + any
      unresolved review-comment threads on the branch's PR.
      `mcp__github__pull_request_read get_review_comments` is the
      authoritative source; `mcp__github__pull_request_read get`
      gives the body's test-plan items.
   3. **Integration-watcher requirements** — the active watchers'
      queue items (`.beans/proof-integration-watcher-queue.json`,
      `.beans/canonical-watcher-queue.json`,
      `.beans/compute-integration-watcher-queue.json`,
      `.beans/detangler-integration-watcher-queue.json`). Prefer
      items whose `block_or_script` overlaps the current PR's
      scope (e.g. the same chapter or the same Python/Lean file).
   4. **Refresh stale sidecars + witnesses** (added 2026-06-03).
      The QA pipeline depends on `*.qa.json` sidecars and
      `computations/*.witness.json` files staying
      in sync with the source they audit. Sidecars are stale
      when `source_hashes.{md,ts,lean}` or
      `criteria.<crit>[-1].reviewer.script_hash` (both 12-char
      SHA-256 prefixes) drift from the current file contents;
      refresh by deleting the stale `criteria.<crit>` entry from
      the `.qa.json` and running
      `bun run folio-assistant/content/pipeline/qa-sweep.ts <path> --only <crit>`
      (single canonical invocation; use `/integration-audit
      <axis>` to batch a whole axis). Witnesses are stale when
      `witness.scriptHash` (SHA-256 prefix of producer file
      content) drifts from a freshly-computed hash of the current
      producer. **Do NOT treat `witness.scriptCommitSha` drift as
      staleness** — rebase-merge (rule 8) rewrites every branch
      commit sha, so that field is stale-on-arrival for any
      producer committed on a branch and no branch-side refresh
      can fix it (the merge *is* the rewrite). It is informational
      provenance only; the enforcement paths already ignore it
      (`witness_dependency_drift.py` keys self-staleness on
      `scriptHash` alone; `witness.py` masks `scriptCommitSha` in
      `_EPHEMERAL_META_FIELDS`). Measured cost of the old wording:
      two false positives and zero true positives on the
      reliably-measurable sample — i.e. it spent the idle-pass
      witness budget on producer re-runs that fix nothing. Never
      mass-refresh the field; it would be correct only until the
      next merge (bean `qou-wsha`). Refresh genuine `scriptHash`
      staleness by re-running the producer with
      `2>&1 | tee /tmp/<script>.log` per the compute-audit
      long-compute logging discipline. **Diff the producer first**
      (`git diff <witness.commitSha> -- <producer>`): `scriptHash`
      is a whole-file hash, so a comment- or docstring-only edit
      drifts it while the recomputed payload is byte-identical.
      This is a far weaker false-positive class than
      `scriptCommitSha` — it needs a real edit, not merely a merge —
      but it is the same waste when the producer is expensive. Cheap
      probes: just re-run. Long-compute producer with a comment-only
      diff: claim it as a bean rather than spend the idle pass
      recomputing numbers that cannot change. Worked case:
      `canonical-ordering-dof` drifted `87418d646ff1` →
      `894cafe018ee` on +21 lines that are **all comment**
      (bean `qou-zv2l`). Cap at ≤ 10 sidecars /
      ≤ 3 witnesses per idle pass. Every refresh that changes a
      sidecar or witness gets a `chore(qa-sweep|witness)` commit
      naming the producer + criterion + count. Full discipline:
      [`.claude/skills/local/integration-watcher.md
      §0b-idle-time-backlog-policy-5-minute-trigger`](.claude/skills/local/integration-watcher.md#0b-idle-time-backlog-policy-5-minute-trigger).
      This sits above cross-cutting cleanups because stale
      sidecars mislead all four watcher children's reads.

      **Before spending the witness half of that budget, run
      [`witness_staleness_triage.py`](computations/witness_staleness_triage.py)
      — measured, the answer is usually "spend it on sidecars instead."**
      It normalises both producer versions through `ast.unparse` (comments,
      docstrings and formatting gone) and reports which drifts can actually
      move a number. Re-measured three times across 1564 commits of `main`,
      **zero** of ~700 self-stale witnesses were safe to refresh. Source-
      identical is necessary but not sufficient, and the two extra gates are
      the ones that bite:

      - **Import-cone drift — the one that actually bites.** A producer's own
        source can be byte-stable while the module it *calls* changed.
        Measured: `binding_canonical.py` is source-stable across its drift
        window, yet `tr_M_atom` moved `0.388 -> 0.575` (48 %) because
        `tr_m_atom_via_transfer.py`, which computes that quantity, changed.
        A file-local `git diff` cannot see this — use
        [`witness_import_cone_staleness_audit.py`](computations/witness_import_cone_staleness_audit.py),
        or the one-hop check the triage script now runs.
      - **Environment (hazard, not yet measured here).** A producer *may*
        branch on what is installed. I originally reported the
        `binding_canonical` 48 % as an instance of this; **that was wrong** —
        re-run with `pyhecke_native 0.9.0` and every recorded package matched,
        it reproduces the committed value byte-identically. Still worth
        checking the witness's `environment` block before re-running, but this
        corpus has not yet produced a confirmed case.
      - **Bare producers.** Some producers never emit provenance; the
        `scriptHash` / `commitSha` on disk was added downstream. Re-running
        one *deletes the field this audit keys on* (measured: 15 keys in, 7
        and 9 out). Fix the producer to emit provenance first.

      **A `substantive` verdict over-flags — but by ~27 %, not the 61 % this
      text used to claim. CORRECTED 2026-08-23.** The old figure (39 % move,
      28 of 72) was measured PER WITNESS, and the queue was then 268 witnesses
      over only 146 producers with **119 of them from one producer**. So one
      "did not move" fact was counted ~119 times and dragged the rate down.
      **Do not quote 39 %.**

      **MEASURED, third attempt: 58 % move, so `substantive` over-flags by
      ~41 %.** Full sweep, all **152 producers**, baselined from git and
      calibrated against three hand-verified answers before it was trusted:

          completed (rate denominator)   128
            moved, substantive field      74   -> 58 %
            moved, noise only              2
            identical                     52
          excluded: 14 crashed, 10 timed out

      **Both earlier figures were wrong, in opposite directions, and both were
      mine.** 39 % (implying 61 % over-flag) came from PER-WITNESS sampling when
      119 of 268 witnesses shared one producer, so a single "did not move" fact
      counted ~119 times. 73 % (implying 27 % over-flag) came from a
      CONTAMINATED BASELINE: the sweep snapshotted `before` from the working
      tree it was itself mutating, and producers write sibling witnesses. Two of
      three spot-checked MOVED verdicts under that method were false.

      **Baseline from git** (`git show origin/main:<witness>`), never from a
      tree your own sweep writes to. That single change turned both known false
      positives back to IDENTICAL while leaving the known true positive intact.

      **CORRECTED 2026-08-24: 2 producers are genuinely broken, not 14.** This
      text said "16 % cannot complete at all — 14 crash". That figure was my
      harness, not the corpus, and it took six separate defects to unwind:

      - **2 needed `computations/` on `PYTHONPATH`**; one exits 0 with it.
      - **1 passed only in isolation** — a sweep that already set `PYTHONPATH`
        still misclassified it, so the runner carried order-dependence.
      - **1 uses REPO-ROOT-relative paths**; the sweep ran everything with
        `cwd=<producer dir>`, so any root-relative producer looked broken.
      - **4 exit non-zero BY DESIGN**, and this is the one worth internalising:
        a non-zero exit is not a defect. `low_isotope_mass_table` refuses when
        precision would fall below the committed `target_dps`;
        `qbeta_braid_nf_sdp_offset_probe` refuses because `mp.lu_solve` would
        *not* raise and running on "would publish laundered numbers". Both are
        guards working correctly, and both explain themselves on **stdout** —
        which a stderr-only harness never sees. Two more
        (`alpha_em_b2_bring_period_matrix_probe`, `rho_k_h3a_refinement`)
        **write their witness successfully** and only then exit non-zero, on an
        environment check and on DeprecationWarnings respectively.
      - **2 were real and are fixed** (mpf-formatting, PR #5615).

      - **1 raises its guard instead of exiting** — `qbeta_habiro_phase5q_dn`
        `_refactorize` dies on `AmDifferenceInvalid`, a `ValueError` subclass
        `habiro_coefficients_atomic` defines for exactly this: *"raised when
        a_m-differencing would silently build the wrong object"*. The message
        even names the correct route (`trace_diff_numerator`) and the beans
        (`qou-0ndb` / `qou-lnog`). **A traceback is not proof of a defect
        either** — a refusal implemented as a raised domain exception is
        indistinguishable from a crash by shape alone. The discriminator is
        whether the exception type is one the producer's own cone defines.
        This one cost me a wrong entry in the list below, in the very text
        warning that a non-zero exit is not a defect.
      - **2 were real and are fixed** (mpf-formatting, PR #5615).

      So a producer-runner must: set `PYTHONPATH`; skip scripts declaring
      required positionals; clean the tree **before** each run as well as after;
      try **both** `cwd=<producer dir>` and `cwd=<repo root>`; capture
      **stdout as well as stderr**; check for a **traceback** rather than
      trusting the exit code; and then check whether that traceback's exception
      type is a **guard the corpus defines**. Without all seven its verdicts are
      about itself.

      **The 2 real defects**, re-verified against `main` on 2026-08-24:
      `su4_1111_markov_trace_probe` (`scipy.sparse` rejects `dtype object` — an
      `mpf` reaching a sparse matrix) and `qbeta_habiro_element_probe`
      (`TypeError: 'NoneType' object is not subscriptable`). `hadron_knot_table`
      was on this list and **is fixed on `main`** by the sibling `qou-n7ue` arc;
      it now runs, slowly, which is the "honest cost" that bean records. The 10
      timeouts are a 240 s budget artifact and may simply be long-compute;
      re-run with a real budget before calling any of them broken.

      Two lessons in the measurement itself, both worth more than the number:
      **mask volatile keys or you measure your own harness** — `timestamp`,
      `elapsed_seconds`, `measured_at`, `start_time_monotonic` and the
      `/invocation/*` block all change every run; and **record WHICH fields
      moved**, so a mask gap is re-classifiable from the checkpoint instead of
      costing another full sweep. Both errors were made here before being
      caught, the first one twice.

      So re-run to decide, and expect roughly 1 in 4 to be a false alarm rather
      than 3 in 5. Sample is 49 of 152 producers; timeouts and crashes are
      excluded from the rate.

      **Producers write SIBLING witnesses.** The isotope producer rewrote 21
      `canonical-isotope-witness-Z*.json` files that the sampler never targeted.
      Anything that re-runs producers to compare must restore the whole
      `computations/` tree afterwards, not the one file it was looking at, or it
      leaves a dirty tree that reads as real work.

      And ~49 % of the backlog is `rewritten` — the recorded `commitSha`
      resolves to nothing. **This text previously named rebase-merge as the
      cause; that is confirmed for only 46 of 376.** Agent clones here are
      **shallow**, so a sha can be missing merely because the history was never
      fetched. Split on the shallow-boundary date, 46 witnesses were computed
      after it (sha was in the fetched window ⇒ genuinely rewritten) and 330
      before it (**cause undetermined**). Do not repeat the stronger claim, and
      note a direct `git fetch origin <sha>` cannot settle it — GitHub refuses
      arbitrary-sha fetches regardless of whether the object exists. This is
      the same effect the
      `scriptCommitSha` ruling above describes, one field over: **"diff the
      producer first" is unrunnable for half the queue**, and hand-patching
      the sha (13 such commits on `main` in one 8-day window) buys only the
      interval until the next merge.
   5. **Cross-cutting cleanups** — bare-URL `-- Ref:` upgrades,
      `validate-bib` deferred items, glossary backfills, doc
      currency. Lowest priority because they're not gated on any
      in-flight work.

   "Substantive output" means: a new commit, a meaningful chat
   response (not a TICK ack), or a tool call that advances a
   queue item. If the only thing in the window is monitor TICKs
   and "pause-mode TICK" acks, you are idle and the trigger
   fires.

6. **Update the plan when upstream lands.** The session-start hook
   arms `local/watch` on `origin/main` (and `local/coordinate`
   triages sibling PRs). Whenever a `<github-webhook-activity>` or
   watcher event reports a new commit / PR / review comment that
   affects this branch, walk the §3 watch checklist; if the result
   is "queue work", insert the new todo at the right priority slot
   (do not push to the bottom blindly, do not jump above the
   current in-progress task unless it is a blocker).

7. **End-of-session: surface the plan.** If the session ends with
   pending todos and the next step is **not unambiguous**, show the
   remaining todo list to the author before closing — even if the
   user said "we're done". Use a numbered list so they can reply
   "1, 2" to pick what's next. If the next step *is* unambiguous
   (one todo, clearly the user's stated goal), skip the prompt.

This policy makes the agent durable to interruptions, sibling-PR
churn, and long async waits. It is enforced by review tooling: a
session that pivots without a `TodoWrite` update or that idles
without pulling the queue is an audit flag.

## Branch + PR workflow (STRICT — supersedes default "no auto-PR" guidance for this repo)

**Always create a branch and open a PR at the start of every work
tranche.** Don't accumulate uncommitted work on `main` or on a stale
branch — push intent visibility to the PR layer from the first
commit. The PR is the durable artifact; the chat session is
ephemeral.

> **Supersession note.** Default agent system prompts often include
> *"Do NOT create a pull request unless the user explicitly asks for
> one."* That guidance is **overridden for this repo** by the rules
> below. The author has explicitly directed (multiple sessions,
> 2026-05-20+) that ALWAYS-PR is the working norm. Agents should
> create a branch + PR for every substantive work tranche without
> waiting for explicit "open a PR" wording — the standing
> authorization is in this section.

### Rules

0. **Commit early, commit often, push to GitHub (standing guidance,
   2026-07-27).** Every meaningful unit of work — a probe result, a
   Lean lemma, a coordination doc, a bean update — gets its own
   commit and push. Do NOT accumulate uncommitted work. The GitHub
   history is the durable record; the chat is ephemeral. If the
   session crashes, the commits survive. This applies to all agents.

1. **Start every work tranche on a fresh branch.** Naming convention:
   `claude/<theme>-<utc-ymd>` (per the existing user-accessibility
   section). The theme is the WORK, not the request — e.g.
   `claude/laurent-q-trace-optimization-2026-05-20`, not
   `claude/respond-to-user-2026-05-20`.

2. **Open the PR FIRST — ASAP, and NEVER ask permission.** The PR
   is the very first action after the first commit — before any
   further work. Create the branch, make the first commit (even a
   stub), open the PR immediately. Then continue working. The PR body
   is a living document; update it as work progresses. **Never
   accumulate multiple commits before opening the PR** — the PR is
   the visibility artifact, not the code.

   **Do NOT ask "want me to open the PR?" / "should I open a PR?".**
   Asking is itself a policy violation: branch + PR creation carries a
   standing authorization (supersession note above), so just do it.
   The branch, the commits, the push, and the PR are **all
   pre-authorized** — the only git action that ever requires explicit
   user permission is the **merge** (rule 7). If you catch yourself
   about to ask whether to open a PR, open it instead and move on.
   (Added 2026-05-29 after an agent asked "want me to open the PR?"
   despite the standing authorization — the question wastes a
   round-trip for a physically-disabled author, see User
   accessibility.)

3. **Commit early, commit often — microcommit.** Each logically
   distinct change gets its own commit. Prefer many small commits
   over few large ones. A single file rename, a single block move,
   a single bug fix — each is its own commit. Push after each
   commit (or every 2-3 if moving fast). Examples of good
   commit granularity:

   - "scaffold module X" (skeleton + types)
   - "implement X.foo() — basic case"
   - "implement X.foo() — case B (braid relation)"
   - "implement X.foo() — cache for cycle-equivalent words"
   - "tests: cross-check X.foo() vs reference at 50-dps"
   - "address Gemini review (5 comments)"
   - "bench results doc — empirical numbers"

   Bad granularity: one giant "implement X" commit that mixes
   scaffold + implementation + tests + review fixes.

4. **Small structured commits beat one big commit.** Reasons:

   - **Cherry-picking.** If a sibling PR needs ONE of your changes
     (e.g. the cache-key fix but not the algorithm port), small
     commits make cherry-pick trivial. Big commits force "all or
     nothing".
   - **Review attention.** Gemini + Copilot review LANDED commits;
     a 10-line commit gets a focused review, a 500-line commit
     gets a glancing one.
   - **Bisection.** When a regression lands, `git bisect` walks
     commit-by-commit. Granularity = debug speed.
   - **Rollback.** Reverting one commit is safer than reverting a
     batch.

5. **Commit messages: terse-but-complete.** First line is the
   verb + object ("scaffold module X"); body explains why if
   non-obvious. Match the existing commit-message style in this
   repo (see recent merges to `main` for examples).

6. **Push frequently.** After each commit (or every 2-3 if you're
   moving fast): `git push -u origin <branch>`. This is what makes
   the PR + CI visible to siblings.

7. **ALWAYS `/prepare-merge` before merging.** Never call
   `mcp__github__merge_pull_request` directly — always run the
   `/prepare-merge` skill first (rebase, integrate, one-voice
   review, Lean check, request Gemini + Copilot reviews). Only
   merge after `/prepare-merge` completes AND the author gives
   **explicit** merge permission. Interpret that permission
   **strictly**: "looks good" is NOT merge permission; "merge it"
   or "ship it" IS. When in doubt, ask.

8. **Default merge method: "Rebase and merge".** When a PR is
   ready and the user authorizes the merge, use
   `mcp__github__merge_pull_request` with `merge_method: "rebase"`
   (equivalently the "Rebase and merge" button in the GitHub UI).
   This applies the branch's structured commits to `main` as a
   linear sequence — no merge commit, no squash. Rationale:

   - **Preserves the per-cluster commits** that rule 4 above
     mandates. A 6-commit PR addressing 3 review passes stays as
     6 cherry-pickable commits on `main`; squash would collapse
     them.
   - **Bisection stays meaningful.** Each commit is a coherent
     unit; `git bisect` lands on the actual offending change.
   - **No empty merge-commit noise** on `main`. The branch
     terminates cleanly; future readers see the work, not the
     branch ceremony.

   Exceptions (require explicit user instruction at merge time):
   - **Squash** — **NEVER squash onto main unless the user gives
     explicit per-PR permission** (owner directive, 2026-07-29).
     "The branch looks noisy" is NOT sufficient justification —
     clean the branch locally with `git rebase -i` and
     rebase-merge the cleaned-up history instead. The only
     acceptable trigger for squash is an explicit user message
     like "squash this one" or "squash OK" on the specific PR.
   - **Create a merge commit** when the PR is a sub-merge of
     several already-merged sibling branches and the merge
     commit serves as a navigable boundary marker.

   The standing-authorization rule for ALWAYS-PR (above) applies
   here too: agents do not need to ask "which merge method?" each
   time — default to rebase-merge. Do NOT auto-squash.

   **Supersedes older guidance.** This rule overrides any
   conflicting merge-method recommendation that appears in
   `.claude/skills/local/*.md` skill documents. Where a skill
   (e.g. `integration-backlog.md`) historically suggested
   `merge_method: "merge"` or `"squash"` as a default, those
   options now apply only as the exceptions described above.
   Skill authors updating skill docs should refer to this rule
   rather than restating the policy in their own words.

9. **Never delete closed/merged feature branches** (owner
   directive, 2026-06-12). Do not run `git push origin --delete
   <branch>`, do not enable auto-delete-on-merge, and do not offer
   branch deletion as a "cleanup" option in end-of-session menus.
   Closed branches are part of the historical record: PR head SHAs
   stay resolvable, session links and coordination-ledger
   references stay live, and `lake-cache/*` orphan branches are
   load-bearing infrastructure. This applies to every `claude/*`
   work branch after its PR is merged or closed.

10. **NEVER merge to main without running the full
    `/prepare-merge` pipeline** (owner directive, 2026-07-29).
    Every merge to `main` — no matter how small ("just one file",
    "just a policy change", "just a docstring fix") — MUST go
    through the `/prepare-merge-auto` skill
    (`.claude/skills/local/prepare-merge-auto.md`). This means:

    - **Phase 0:** sibling coordination (notify overlapping PRs)
    - **Phase 1:** rebase onto main, build, push
    - **Phase 1b:** request review; wait for **Copilot** (up to 15 min)
    - **Phase 2:** resolve review comments
    - **Phase 3:** escalate to user if blocked
    - **Phase 4:** merge only after reviews resolved + the
      **verification gate** below is satisfied

    > **🛑 Two of the three original gates no longer exist — do NOT
    > block on them (recorded 2026-08-07).** An agent following the
    > older wording waits forever on reviewers and a CI run that can
    > never arrive:
    >
    > | Original gate | Actual state |
    > |---|---|
    > | CI green | **Unavailable.** Auto-triggers are disabled repo-wide — [`build.yml`](.github/workflows/build.yml) is `workflow_dispatch`-only ("CI auto-triggers disabled (owner directive 2026-06-30)": Actions billing). There is **no** `lean_ci.yml` in the tree. Feature branches routinely show **zero** workflow runs / zero check runs. |
    > | Gemini review | **Gone.** "The consumer version of Gemini Code Assist on GitHub has been sunset. All code review activity has officially ceased." (bot notice, PR #4514, 2026-08-01). |
    > | Copilot review | **Does not arrive.** Measured n=5 (bean `qou-gwe9`): requested explicitly via `request_copilot_review` on #5474, #5495, #5411, #5459, #5482 — **zero** reviews every time, and `get_check_runs` returns `total_count: 0` rather than a queued `copilot-pull-request-reviewer` run, so nothing is ever enqueued. Re-requesting after a force-push does not help; the cases span new Lean, a 20-file revert and a beans-only change, so it is not file-type-conditional. |
    >
    > **🛑 So the Phase-4 gate table now has ZERO live external gates, not
    > one.** All three original gates are gone. The agent's own verification
    > is not the last gate standing — it is the *only* gate. Act accordingly:
    > state the verification you actually ran, and do **not** wait on Copilot.
    > `prepare-merge-auto` Phase 1b still prescribes a 15-minute poll for a
    > check run that is never created; that wait can only expire, so skip it
    > and record why (citing `qou-gwe9`) rather than burning the window.
    >
    > **Phase-4 verification gate (replaces "CI green").** Because CI
    > is unavailable, the agent's own verification *is* the gate — this
    > is the merge-time application of §"QA is agent-owned; CI is a
    > backup". Before merging, state the evidence explicitly in the PR:
    >
    > - **Lean changed** → `lean`-direct **exit 0** on every changed
    >   file, built against its **real import cone** (not a stubbed
    >   harness), plus `#print axioms` on the new declarations showing
    >   no `sorryAx`. Note that a **library** file under
    >   `content/<paper>/lean/QOU/**` has no `.qa.json` sidecar and is
    >   **not** covered by `lean-content-siblings.yml` (which gates
    >   content-block siblings only) — nothing but the agent checks it.
    > - **Content blocks changed** → [`scripts/check-sidecars.sh`](scripts/check-sidecars.sh)
    >   clean + `qa-sweep` on the touched criteria; math-bearing `.md`
    >   also needs the render-QA gate.
    > - **Compute changed** → the producer re-run + witness refreshed.
    >
    > Do **not** write "CI green" in a PR or merge rationale unless a
    > run actually exists — say which verification you ran instead.
    > If a workflow *is* wanted for a specific PR, it must be kicked
    > manually (`workflow_dispatch`).

    **No shortcuts.** Do NOT `gh pr merge` immediately after
    creating a PR. Do NOT skip reviews because "the change is
    trivial". Do NOT merge on an *unverified* branch — the pipeline
    exists to catch mistakes that the author's own session missed,
    and with CI down the verification gate above is the only thing
    standing in for it, so skipping it defeats the purpose entirely.

    The only exception is if the user explicitly says "merge now,
    skip reviews" on the specific PR.

### Exception: batch audit-job runs

When an integration-watcher (`compute-integration-watcher`,
`canonical-watcher`, `proof-integration-watcher`,
`detangler-integration-watcher`, `one-voice-integration-watcher`)
runs a **mechanical sweep** across many blocks / scripts /
witnesses, a single bulk commit ("regenerate N sidecars after
checker fix") is acceptable and preferred:

- The mechanical change is uniform; granular commits would just
  fragment the same fix.
- Cherry-pick is rarely useful for sweep results (you want all or
  none).
- The audit-doc + the bulk commit together convey the intent.

If you find yourself making a single commit that's > 50 files OR
> 1000 lines and the change is NOT a mechanical sweep, that's a
signal to break it up.

### Why this matters

The repository has had merge churn in the past where one branch
held weeks of uncommitted work; when it finally pushed, sibling
agents had stepped on the same files. Early-branch-and-PR makes
intent visible from minute 1.

PR-level visibility also activates the integration-watcher infra
(`.claude/skills/local/integration-watch.md`) and the
coordinate-skill sweep (§7-§8 of `coordinate.md`), so sibling
agents triage your work automatically.

## QA is agent-owned; CI is a backup (STRICT, 2026-06-25)

Every agent runs the QA checks relevant to its **own** PR **by hand,
before committing** — CI is a safety-net that catches what the agent
missed, **not** the primary gate. Do **not** block on CI or wait for it
to go green to proceed: verify locally and move (a PR with local
`lean`-direct exit 0 + a clean `qa-sweep` on the touched blocks is
merge-ready on the agent's own verification). This matters because the
reactive post-commit `qa-sweep` does **not** cover everything — a
**standalone library Lean file** (`content/**/lean/QOU/**/*.lean` with no
`.ts`/`.md` sibling) has no `<block>.qa.json` sidecar and escapes every
per-block checker (`q-usage-*`, `wall-side-correct`, one-voice, …) — and
CI billing flakiness (below) makes CI unreliable as a gate anyway.

**Preflight helper — run before every commit:**
[`scripts/check-sidecars.sh`](scripts/check-sidecars.sh) maps the files
you changed → the QA sidecar criteria that apply, and runs the §7c
base-ring check on un-sidecar'd library Lean. Act on its ⚠ lines (refresh
stale sidecars via `qa-sweep`; resolve gratuitous `ℝ` per §7c). The Lean
authoring gate is [`local/formalizer.md` §Pre-commit base-ring
GATE](.claude/skills/local/formalizer.md). History: added 2026-06-25 after
a gratuitous `(q : ℝ)` / `SL₂(ℝ)` landed on a purely-algebraic τ-kernel
lemma in a library file (no sidecar ⇒ unswept); the owner caught it by eye.

**Precision preflight — run before every commit that touches a witness or a
`computations/` script (STRICT, 2026-08-09).**
[`scripts/precision-gates.sh`](scripts/precision-gates.sh) runs the whole
NO-FLOAT64 family in one pass — the two ratchets (raw-float64, float64-padding),
the three source-level gates (`mpf(<float>)`, `mp.dps` no-op, module-const), the
q₀ anchor-flip and drift gates, plus the no-free-parameter certificate as
advisory. Use `--changed` to make it a no-op when nothing precision-relevant was
touched. It exits 1 on any blocking red and does **not** stop at the first
failure.

Why it is a hand-run preflight and not "CI will catch it": these gates *were*
already strict in `.github/workflows/witness-staleness.yml`, and three dirty
witnesses reached `main` anyway (bean `qou-mnrd`). That workflow is
`workflow_dispatch:` only under the 2026-06-30 Actions-billing directive, so on
a push it never runs. **Asked and answered (owner, 2026-08-09): leave it
dispatch-only** — the directive was reaffirmed with that failure cost on the
table, against a path-filtered trigger and against full push+PR triggers. So
this script is not a stopgap until CI returns; it *is* the gate. Treat a skipped
run the way you would treat a skipped CI check, and do not re-propose enabling
the trigger without a new reason.

**Never make a red run green by widening a baseline.** Fix at the producer —
carry the value as `mpmath.mpf` from its source and serialize with
`_precision.fmt`. Adding a file to `raw-float64-baseline.json`, `--rebaseline`,
or hand-editing a number defeats the mechanism. Baselines drain, never grow.

**PROBES ARE NOT EXEMPT. "It emits no witness" is not an exemption (STRICT,
owner directive 2026-08-18).** A probe is a `computations/` script and is
covered by every gate above. The reasoning *"no witness by design, so precision
does not matter"* is **wrong and is banned** — it inverts the actual risk. A
witness is a number that gets re-derived; a probe conclusion is an **argument**
that gets written into a bean, an audit doc, a PR body and a content block,
where nothing re-derives it. Float64 in a probe corrupts *analysis*, which is
the expensive kind of wrong.

Concretely, in any `computations/` script including probes:

1. **Never compute in `float`.** Carry `mpmath.mpf` end to end. `float(x)` is
   permitted **only** inside an f-string for display, and even then prefer
   `mp.nstr`. `hf = float(G.h)` followed by arithmetic against it is a
   computation, not a display, and is a defect.
2. **Never aggregate with `statistics` / `math` over floats.** `st.mean`,
   `st.pstdev`, `math.sqrt`, `sum()` over a list of `float` all accumulate
   error across a large sample. Use `mpmath` equivalents, or `Fraction` when
   the quantity is exact.
3. **A float64 input poisons the whole result.** If a probe reads a float64
   table (e.g. `pyhecke.trace.TR_M`), the output resolves to ~1e-16 **no matter
   what is true**. Do not "note it as a limitation" and ship — either find the
   exact-arithmetic route (symbolic `ℚ(q)`, `Fraction`, the NF/GS basis over an
   exact ring) or state that the question is **unanswered**, not answered with a
   caveat.
4. **Never report a float64 agreement as "exact", "identical", or "to N
   digits".** Agreement at 1e-16 in float64 is the *floor* of the arithmetic,
   not evidence about the mathematics. The honest phrasing is "agrees to the
   limit of the arithmetic used, which cannot distinguish X from Y".
5. **Run [`scripts/precision-gates.sh`](scripts/precision-gates.sh) before
   committing a probe**, exactly as for a producer. `--changed` makes it cheap.

History: added 2026-08-18 after an agent shipped eight probes on the L2 binding
axis with `float(G.h)` in the Coulomb-charge arithmetic and `statistics.mean`
over 3519 float64 rows, and — the case that prompted the directive — ran a
Markov-trace multiplicativity test against the **float64** `TR_M` table, wrote
"the product formula is exact ... interleaved − product = 7.4e-17", and recorded
the float64 resolution as a scope caveat rather than as a reason the test could
not answer the question. The owner had asked for no-float multiple times before
this.

**Render-QA gate for math-bearing `.md` (STRICT, 2026-06-30).** Any commit
that creates or edits a `.md` content block containing math (`$…$`,
`$$…$$`, or fenced ` ```tex ` blocks) **must** be render-QA'd before commit
— do **not** rely on CI or the author's eyes to catch a broken equation.
Run the full markdown render check
([`local/markdown-render-check`](.claude/skills/local/markdown-render-check.md)):
the pipeline render where available
(`bun run folio-assistant/content/pipeline/render-latex.ts …` after
[`scripts/setup-folio-assistant.sh`](scripts/setup-folio-assistant.sh)),
**and always** the preflight grep battery — balanced `$`/`$$`/`{}`/
`\bigl`-`\bigr`/`\begin`-`\end`; no `\operatorname{}` (KaTeX rejects → use
`\mathrm{}`); no line starting with `+`/`-`/`*` inside `$$…$$` (markdown
list-parser hijack); align-family environments (`aligned`, `align`) fenced as
` ```tex `, not inline `$$`.

> **Fencing an align-family env is only HALF the rule — the other half
> is build-fatal (2026-08-16).** `aligned`/`gathered`/`split`/`cases`/
> the matrix family/`array` are **inner** environments: legal only
> *inside* math mode. A ` ```tex ` fence is raw passthrough, so a fence
> that opens directly with `\begin{aligned}` lands in horizontal mode
> and aborts pdflatex — `! Package amsmath Error: \begin{aligned}
> allowed only in math mode` plus two `! Missing $ inserted`, three
> errors from one slip. Wrap it in `\[ … \]`, or use the **outer**
> `align`/`gather` form. This is now the mechanical criterion
> **`render-math-mode-envelope`** (severity critical) — run
> `qa-sweep … --only render-math-mode-envelope` rather than grepping by
> hand: `\begin{align` is a *prefix* of `\begin{aligned}`, so the
> obvious guard matches the very thing it should catch (a scan written
> that way reported 0 hits against a true 2). Recurring class — fixed in
> `afdf60d667`, returned in two further blocks.
>
> **Companion rule — unicode.** *"Unmapped" ≠ "crashes"*: LaTeX's own
> `utf8.def` declares a large set, so `↑` is fine while `∇`/`ˣ` abort.
> Inline **and** fenced code are transliterated as of
> folio-assistant#129, so the residual risk is a crash-class char in
> plain **prose** or a `.ts` **`title:`**, where nothing transliterates.
>
> **A char can be safe in prose and still break in math — the two
> questions are separate.** "Crash-class" above is about chars `utf8.def`
> never declares at all. A char it *does* declare can still fail, because
> what it declares may be **text-mode only**: every accented Latin letter
> maps to a text accent (`ï` → `\"i`), and `\"` is invalid in math. So
> `naïve` in prose is fine while `$y^{\mathrm{naïve}}$` emits *"Command
> `\"` invalid in math mode"* and then **drops the glyph** — a hole in the
> typeset page, from markdown that looks correct. Fixed at the preamble as
> of folio-assistant#129 (`\unitextsafe`, U+00C0–U+017F, all 161 verified
> in text *and* math), so no authoring rule is needed for accented names —
> recorded because the fix is easy to undo by "tidying" the block away.

Then run the **expository pass**: every symbol
and term is introduced before first use, and no symbol is silently reused for
two meanings (e.g. `λ = ln q` vs the partition `λ ⊢ n`; rename one). When the
pipeline render cannot run (e.g. the `folio-assistant` clone is firewalled in
a sandbox), run the grep battery + expository pass by hand and **state
explicitly in the commit/PR that the change was not machine-validated** — never
report a math edit as render-checked when only CI (which may be billing-flaky)
would have caught it. History: added 2026-06-30 after a mass-derivation survey
rewrite shipped with `\operatorname` (KaTeX-breaking), a `B`-vs-`𝔪` mislabel, a
wrong `dim_q = [n]_q`, and a `λ` notation collision — none machine-caught
because the pipeline was unavailable and the agent skipped the manual battery.

## CI billing failures — distinguish from real failures (STRICT)

GitHub Actions workflows may fail in **2-3 seconds across multiple
jobs simultaneously** with no logs reaching the validate / build /
test step. When this happens the cause is almost always a GitHub
Actions billing issue, NOT a problem with the code:

> *"The job was not started because recent account payments have
>  failed or your spending limit needs to be increased. Please check
>  the 'Billing & plans' section in your settings."*

### How to recognize it

- **Setup-phase failure timing.** All failing jobs complete in
  ≤ 5 seconds (setup-phase only — checkout / pip install alone
  take longer). Real validate/build failures take ≥ 30 seconds.
- **Multiple jobs fail together.** Same `started_at` timestamp
  across `validate`, `Content pipeline`, `Build all papers + commit
  sidecar`, etc.
- **Local reproduction passes.** `bun run scripts/run-validate.ts content/<paper>` exits 0,
  witness-pipeline Python scripts exit 0, no `.lean` changes.
- **Webhook payload says `conclusion: failure`** but no error log
  exists because the job never actually started.

### What to do

1. **Do NOT diagnose as a code issue.** The MCP API does not expose
   job-startup-phase error reasons; treat the unexplained 2-3s
   failure as billing UNLESS the user shares a different error.
2. **Do NOT push retrigger commits** — billing doesn't clear on retry.
3. **Notify the user briefly** and ask whether to (a) skip CI and
   proceed (`/prepare-merge` step 6+, request reviews on the green
   local validate), or (b) wait for billing to clear.
4. **Document the skip in the PR** when proceeding — e.g.
   `[skip-ci: GitHub Actions billing; local validate exit 0]` in
   the comment requesting reviews.

History note (2026-05-29): this rule added after PR #1435 hit
3 consecutive failures with this exact pattern; the user confirmed
"job was not started because recent account payments have failed"
and instructed "skip CI". Local validate had been exit 0 throughout.

## Before declaring "open" math / questions / gaps (STRICT)

Before any agent declares an item "open", "Open Math X", "TODO",
"pending derivation", "open problem", or any equivalent phrasing in
an audit doc, content block, Lean comment, or PR description — or
asserts as fact in chat that an item is open/unresolved in the
corpus — run the **corpus-grep checklist**:

1. `grep -rln <topic> docs/audits/` — owner-authorised resolutions
   typically land as audit docs; the originating source file's
   status note may lag the audit by weeks or months.
2. `grep -rln <topic> content/` (whole tree, not just the chapter
   you started in) — related conjectures/propositions cross-cut
   chapters (e.g. `brings-surface/inter-nucleon-channel-color-tube`
   answers a `mass-theory/` p/n asymmetry question).
3. `grep -rln <topic> computations/` — implemented
   Python may already realise the categorical content the source
   file says is "open" (e.g. `pn_convention="bring_color_weighted"`
   in `closed_form_tau_M.py`).
4. Check the relevant coordination ledger
   `docs/coordination/<theme>.md` — prior agents may have closed
   the item already.
5. **The library — walk three tiers, cheapest first.** The ingested
   sources are 24.7 M characters; do not grep straight into them when a
   line will do.

   ```sh
   grep -in <topic> library/INDEX.md              # 320 briefs, ~14k tokens total
   cat library/<doc-id>/summary.json              # ~300 tokens: is it worth opening?
   grep -rln <topic> library/<doc-id>/sections/   # the text itself
   ```

   `INDEX.md` is one line per document and is the right first read — it
   costs about as much as a single paper's abstract to scan the entire
   library. Each section file also carries a `doc_brief` in its
   front-matter, so a hit found by the third command is interpretable
   without opening anything else (contextual retrieval: a chunk in
   isolation otherwise loses what makes it mean anything).

   **One line per *work*, not per file.** The library holds 19 works more
   than once — a preprint beside its published version, or the same PDF
   ingested under two names — and Neumann–Zagier three times. The extra
   copies keep their text on disk, so a full-text grep still lands in
   them; each carries `duplicate_of` in its section front-matter naming
   the copy to prefer. **Do not read two hits on one work as two
   sources.** Adjudicated in
   [`docs/audits/library-duplicate-ledger.json`](docs/audits/library-duplicate-ledger.json);
   `scripts/library-find-duplicates.py` proposes, but its same-work and
   different-work score ranges overlap, so a proposal is not a verdict —
   a sequel sharing its setup sections outscores four true duplicates.

   Briefs and summaries are **extractive** — assembled from each
   document's own abstract, section titles and extracted claims, nothing
   written by a model — so a brief is only as good as the abstract it came
   from. Regenerate with `scripts/summarize-library.py --apply`; a
   hand-written summary marked `provenance.kind: "agent"` survives
   regeneration.

   The full-text grep, for when you want it directly:
   `grep -rln <topic> library/*/sections/` — the **ingested sources**.
   An item can be open *in this corpus* and settled in a paper we
   already hold; that is a citation, not a derivation, but it changes
   what "open" means and it is the difference between deriving a result
   and re-deriving one. 332 documents / 7,313 sections / 24.7 M
   characters are searchable this way.

   This path exists only because the sources were sectioned into text.
   Before that they were 339 PDFs and grep could not see them, which is
   why the checklist historically stopped at four. Two practical notes:
   a hit's YAML front-matter names the document, section and page range,
   so it is immediately citable; and `library/<doc-id>/candidates.json`
   lists that document's extracted theorems and definitions if you want
   the claims rather than the prose.

Only after **all five** grep paths return empty (modulo the
originating file itself) may you declare the item open. The source
file's `## Status`, `Open math`, or `Phase 3 open` notes are
**not authoritative**: the corpus is the source of truth.

### Grep the claim SHAPE, not only the topic (STRICT, 2026-08-15)

The four paths above answer *"has anyone worked this topic?"*. They do
**not** answer *"does the corpus actually assert the proposition I am
about to reason from?"* — and that second question is where a whole
class of errors lives. Before writing any equivalence, identification,
or exclusion into a durable artifact, resolve the symbols to their Lean
declarations and check the **arity**:

1. **One proposition, or a family?** Read the declaration's type.
   `kappa_vanishes : ℕ → Prop` is a *level-indexed family*; there is no
   single truth value to be faithful to.
2. **Pointwise, or the universal closure?** `∀ P, v ↔ Pred P` and
   `v ↔ ∀ P, Pred P` are different claims, and the second is
   **trivially inhabited**. Refuting the first says nothing about it.
3. **Shared type, or shared instance?** A theorem fixing one `sys` and
   one `P` couples two questions *within one instance*; it says nothing
   about two legs instantiated as different values — and the other
   instance may not even satisfy the hypothesis.
4. **Set-level premise, truth-value conclusion?** "Undecidable", "not
   cut out by an ideal", "cofinite locus" are facts about sets or loci,
   logically independent of whether a scalar is equivalent to a single
   proposition.

History: four separate instances of this one conflation reached durable
artifacts in a single session (2026-08-15) — a retracted "the corpus is
inconsistent" claim, a "no scalar can be faithful to halting"
over-claim, a "q-NS blow-up witness *is* a q-Collatz divergence
witness" cross-leg identification, and a set-level-to-truth-value
inference written into a content block *while the audit doc three files
away named that exact fallacy*. Each survived a topic-grep. Recorded as
the `da-arity-conflation` criterion in
[`local/devils-advocate-watcher`](.claude/skills/local/devils-advocate-watcher.md),
which carries the worked examples and the measured reason a machine
checker cannot do this for you.

**Scope note (2026-06-10):** this checklist gates *factual
corpus-status claims*. Skeptical assessments — "this looks fitted",
outside-view critique of a derivation, reception/publishability
forecasts — are not open-item declarations and are never gated by
it; see §Critical-distance license above.

Why this matters: pattern observed in PRs #1515, #1532, #1543 —
three consecutive items declared open against the source-file
status note, each found in subsequent reanalysis to be already
implemented (Track B Gap #2 in `canonical_tr_m_via_branching.py`;
α_shift A=4 in `lightNucleiForceCarrierKnot`; ρ_F derivation in
`conj:kashaev-density-equals-sdp-multiplicity`; p/n asymmetry in
`closed_form_tau_M.py::bring_color_weighted`). Post-mortem in
[`docs/audits/2026-05-31-binding-magic-A-wireup.md` §"Why was the
resolution missed?"](docs/audits/2026-05-31-binding-magic-A-wireup.md).

Skill cross-reference: `local/proof-gap-audit` §K codifies this
checklist for proof-gap declarations specifically.

## Before declaring "refuted" / "ruled out" / "dead end" (STRICT)

The mirror image of the "open" over-claim: an agent tests a single
parameter-free construction **alone, as the sole mechanism**, gets a
bad number, and writes "REFUTED" / "ruled out" / "dead end" /
"cannot" / "impossible" in a durable artifact (audit doc, content
block, ledger, witness `verdict`, PR description). This **over-narrows
the search** — later agents avoid an ingredient that was never
actually excluded. (Calibration audit 2026-06-23 found 6 such
over-claims live in the corpus: c_k method-class map, Bratteli /
Markov-trace H₃→H₄, signed-crossing binding, q-Bessel smoothness.)

Before writing a refutation in a durable artifact, classify the claim
into exactly one of two scopes and use the matching phrasing:

- **(a) Scope-limited negative** — "this construction, *alone*, does
  not reproduce the numbers as-is." This is what a failed numerical
  probe actually shows. Use this phrasing by default. It constrains
  *magnitudes and combinations*, not *ingredients*.
- **(b) Structural exclusion** — "this ingredient cannot appear in any
  closure." Only permitted when a **proved invariant** forbids it:
  parity / sign (e.g. a mixed-sign target vs a provably non-negative
  weight — the KL-positivity prune), a dimension / orbit-count / degree
  bound, a Lean-proved impossibility, or an entropy/precision bound.
  **Cite the invariant.** Without one, you may not write (b).

Two permanence principles that make most "(b)" claims wrong:

1. **A Lean-proved or structurally-exact piece is a permanent, correct
   contribution** even while the current *total* is inaccurate.
   "Inaccurate alone" ≠ "excluded." A proved per-bond / per-block
   factor stays valid; a missing term *adds to / re-weights* it.
2. **A compositional / additive / trace object is already many-body.**
   Showing a term is insufficient *by itself* says nothing about
   whether it belongs in a multi-term closure. In particular a
   multiplicative/trace object (e.g. `1 − ∏ᵢ fᵢ`) expands to cross
   terms — a "pairwise can't do it" argument against it is a category
   error; the probe *measures the size of the missing higher term*, it
   does not exclude the factor.

**Scope note.** As with the "open" checklist, this gates *durable
"refuted" declarations*, not chat-level skepticism. Saying "this looks
fitted" or "I doubt this closes" in chat is the Critical-distance
license and is never gated. What is gated: writing "REFUTED" /
"ruled out" in an audit doc / witness / ledger without the (a)/(b)
classification, and asserting in chat as *fact* that an ingredient is
excluded from the corpus.

When you find an existing over-claimed "(b)" in the corpus, **re-scope
it to (a)** (do not silently delete the finding — the numerical result
stands; only the scope was wrong), and note the calibration in the
commit. Worked example + the 6-item live list:
[`docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md` §"Calibration note"](docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md).

Skill cross-reference: `local/canonical-watcher` flags durable
refutations missing the (a)/(b) scope; `local/compute-author`
§formalize-first is the forward complement (prove the invariant that
*would* justify a (b) before running the wide search).

## Defined residual ≠ derived decomposition (STRICT, 2026-08-08)

A third member of the family with "sorry-free ≠ derived" and
"conditional-proved ≠ premise-established": **`X_resid := X − C` is a
definition, not a decomposition.** Writing a residual with `:=` and then
reasoning about it as though it were *the* bar-odd part (or *the*
anomalous part, or *the* non-perturbative part) of `X` smuggles in an
unproved identification — that `X`'s complementary part *is* `C`.

Before treating any residual as a decomposition, check all three:

1. **Is the split empirically accessible at all?** A bar-decomposition
   `X^even(q) = (X(q) + X(1/q))/2` needs `X` at **both** `q` and `1/q`.
   Every substrate anchor sits at `q ≈ 1.10998`; none supplies
   `q ≈ 0.901`. So no amount of anchor data determines a bar-split — it
   always comes from an assumed structural form. Say which form.
2. **Is the offset *forced*, or merely *in range*?** If the interesting
   feature is a sign change across two anchors, it is produced by **any**
   constant strictly between the two values. Compute that window and
   report its width before claiming the feature is evidence for your
   particular `C`. Worked case: `S_leak := c₃ + Vol(4₁)` sign-flips
   across the anchors — but so does `c₃ + V` for **every** `V` in a
   window of width 0.049, including `2 + 1/36`, `63/31`, and `e^{0.708}`
   ([`sleak_offset_genericity_check.py`](computations/qbeta/sleak_offset_genericity_check.py)).
   The flip restates "`c₃` differs between anchors"; it says nothing
   about `Vol(4₁)`.
3. **Does the corpus already carry a *different* split of the same
   object?** Two inequivalent "bar-even part of `X`" claims mean at most
   one is the canonical split. Grep before building on either. (Same
   worked case: `c₃`'s bar-even part is given as an exact `ℚ(√3)`
   ũ-ladder in one audit and as `−Vol(4₁)` in another; the two are not
   the same object, and a symbol-collision guard separating the two `S`s
   does **not** reconcile the two *even* parts.)

Theorems stated for a *generic* function with the residual's signs as
**hypotheses** are unaffected and remain valid — the defect is never in
that Lean, it is in the interpretive step that the residual *is* the
named part of `X`. Keep the two separate when you cite such a result.

History: added after an agent (this repo, PR #4724) built a c₃ candidate
filter on `S_leak` without checking whether the `−Vol(4₁)` identification
was derived, published it to a sibling PR, and had to retract it. The
author caught it with one question: *"this is not derived?"*. Full
retraction + the three checks worked through:
[`docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md` §RETRACTED](docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md).

## Conditional-proved ≠ premise-established (STRICT, 2026-07-07)

The sibling of "sorry-free ≠ derived" (registry §1): a **hypothesis-carrying
Lean lemma proves the implication, never the premise.** Do not restate a
conditional lemma's antecedent as established fact in constraint lists,
audit docs, ledgers, or chat ("a₁ bar-odd" when the Lean says "IF c₃ is
odd THEN a₁ is odd"). Rules:

1. **Constraint lists carry per-row epistemic tiers** (`proved-lean` /
   `symbolic-exact` / `conditional` + named hypothesis / `empirical` /
   `gate`). For kernel/f-map constraints the authoritative table is
   [`ck-dk-canonical-registry.md` §9](docs/coordination/ck-dk-canonical-registry.md)
   + JSON twin + validator (`kernel_constraints_registry_validate.py`,
   `--lint-docs --strict` for CI); update the registry, not a new scatter
   of status notes.
2. **Conditional lemmas wear their hypothesis in the name** (Mathlib `_of_`
   style) — see `local/formalizer.md` §Conditional-lemma naming.
3. **Machine-checked contradiction rule:** `parity: exactly-odd` together
   with a nonzero q=1 shadow is impossible
   (`QOU.QBeta.fixed_eval_two_mul_kills_bar_odd`) and fails the validator.
4. **Attributes do not transfer across overloaded symbols** — check registry
   §2 before asserting a property of `a₁`/`Φ₂`/`c_k`-like symbols; distinct
   objects sharing a glyph is a recurring root cause.

History: the a₁ parity-shadow incident,
[`docs/audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md`](docs/audits/2026-07-07-a1-bar-odd-parity-shadow-investigation.md).

## Formalize-first policy (STRICT)

For any new math or physics derivation, agents MUST begin by writing the Lean structure, class, or proof scaffold in `.lean` files. Explicitly forbidden: agents must NOT start with Python fitting scripts or prose `.md` files until the Lean axioms compile.

## Formalize-first probe discipline (STRICT — narrow the search before running it)

**Too much time is lost chasing numerical rainbows that a one-line
structural argument — or a small Lean lemma — would have eliminated up
front.** Before launching a *wide / expensive* numerical search over a
hypothesis class (candidate closed forms, a PSLQ basis, a partition /
character / root-of-unity enumeration, a recursion-kernel fit), STOP and
ask whether a **formalizable structural claim prunes the class first**:

1. **State the hypothesis class** you would probe.
2. **Find the invariant the whole class must satisfy** — parity, bar-
   symmetry, a degree / anchor bound, cross-anchor rigidity, search-space
   entropy vs available precision, a Lean-provable constraint.
3. **Formalize it** — a Lean lemma (even *conditional* / `sorry` +
   `-- Ref:` per §3b-cond), or a rigorous symbolic argument.
4. **Let the result narrow the probe** — refuted class ⇒ do not run the
   scan; constrained class ⇒ probe only the survivors; brute-enumerate
   only what formalization cannot prune.

This is the **forward** complement to the corpus-grep checklist above
(which prunes *backward* against already-known results). Worked
precedents where one structural argument killed an entire numerical
family this session: `dc_3/dq ≈ 3.84e6` impossible for smooth real `f`
(kills the real-q c_3 family, [PR #1821](https://github.com/litlfred/qou/pull/1821));
the PSLQ entropy bound `precision > n_terms·log10(2·height)` (kills the
12-constant basis, [PR #1805](https://github.com/litlfred/qou/pull/1805));
A is ~4 sig figs from `c_2..c_10` (no high-precision identification
possible, [PR #1805](https://github.com/litlfred/qou/pull/1805)).

> **Figure corrected 2026-08-22 — the conclusion is untouched.** This read
> `≈ 4.6e6` here and in five other places. That value is the **stale-c₃
> twin** of the "≈ 3 %" swing this document already corrects two sections
> up: both were computed from the pre-#1422 muon `c_3 = -2.0097` and its
> 2.88 % swing, and both should have been re-derived at the same time.
> With the live anchors (`c_3(p) = -2.0693425728`, `c_3(μ) =
> -2.0202002328`, `Δq = 1.28e-8`) three independent routes agree:
> **3.8375e6** by secant, **3.8320e6** from `2.37/u³` at `u = 0.00852`,
> and `3838404.458` recorded in `rem-qstar`'s own witness as
> `S_prime_qstar`. Reaching 4.7e6 would need `u = 0.0079595`. Since
> 3.84e6 is just as impossible for a smooth real `f` as 4.6e6, the
> **prune stands and the real-q c₃ family stays killed** — only the
> quoted magnitude was wrong. The five other sites are audit docs and
> `local/compute-author` §precedent-table; tracked in `qou-3nva`.

**Caveat:** if the formalization is harder than the probe AND the probe
is cheap and decisive, just run the probe — this rule targets
wide/expensive searches, not every one-off check. Full protocol +
precedent table:
[`.claude/skills/local/compute-author.md §3.3`](.claude/skills/local/compute-author.md#formalize-first).

## Always provide GitHub links — default to `.md`

Whenever a skill or agent creates or modifies a file, the reply **must**
include a clickable GitHub blob URL for every affected file on the
pushed branch. This applies to all file kinds: `.md`, `.ts`, `.lean`,
`.tex`, config files, scripts, etc.

**Default link target for content blocks is always the `.md` file.**
When citing a content block (definition, proposition, remark, etc.) in
chat replies, reviews, or summaries, the primary clickable link
**must** point to the `.md` sibling — never to `.ts` or `.lean` as the
primary link.

Rationale: `.md` is the narrative/authoritative human-readable face of a
content block. `.ts` is manifest metadata; `.lean` is formalization.
Users want to read the statement, not the manifest.

Pattern (always):

```
https://github.com/litlfred/qou/blob/<branch>/<path-to>/<block>.md
```

**When to link siblings (`.ts`, `.lean`, `.tex`):**
- Only in delivery summaries for **modified** files (see
  `.claude/skills/local/delivery-summary.md`) — list every sibling that
  actually changed.
- When the user explicitly asks about the Lean formalization or TS
  manifest.
- Never as the primary citation link for a block reference.

If the branch is not yet pushed, say so explicitly and do not fabricate
URLs.

## Canonical derivation chain — cheat sheet (READ THIS FIRST for math work)

**Authoritative cross-link**: [`docs/canonical-derivation-cheat-sheet.md`](docs/canonical-derivation-cheat-sheet.md).

The QOU framework derives every observable (m_p, m_n, m_He, Q_β, B_AME, lifetimes) from **3 calibration inputs** — the canonical *mathematical* triple, **three weak-sector observables** (a leptonic mass scale and two decay widths; their numerical proxies are masses):

| CAL | Canonical observable | What it fixes | Numerical proxy | DOF of H¹(Bring) = 2W |
|-----|----------------|---------------|-----------------|------------------------|
| CAL-1 | m_e (leptonic mass scale, h⁰) | the dimensional unit (scale) | m_e (CODATA) | W-plane scale |
| CAL-2 | 𝔇_β (neutron β-decay width, h²) | q₀ (via m_μ/m_e = Vol(4₁)/ℏ_q²) | Q_β = ℏ/𝔇_β; modulus pinned most precisely by m_μ/m_e | W-plane modulus |
| CAL-3 | 𝔇_π (pion decay width, h³) | the orthogonal meson scale | m_π (PDG) | orthogonal class |

> **🟧 Owner ruling (2026-06-26): the ideal *mathematical* canonical is the decay-width triple (m_e, 𝔇_β, 𝔇_π), NOT three masses.** Masses (m_e, m_μ/m_e, m_π) and Q_β are the *numerical proxies*; **Q_β is the proxy for CAL-2 (𝔇_β), not "derived, not a calibration".** This supersedes the prior "three measured masses / Q_β derived" wording. (PR #2866, Stage 1 + Stage 2: the two Propositions + their `.ts`/`.lean` siblings, `epistemic-status-of-calibrations`, and the §"q₀ anchor convention" STRICT section below are relabeled. The Lean witness `calibrations_eq_cohomology` is a count/alignment claim — 3 calibrations = 3 H¹ DOF — unchanged by the relabel.) **Read-first anti-flip-flop record (history + ideal-vs-experimental m_μ + the fitted-proton-q₀-solver caveat): [`docs/audits/2026-06-28-calibration-canon-decay-width-ruling.md`](docs/audits/2026-06-28-calibration-canon-decay-width-ruling.md).**

All three are the **three real DOF of the single H¹(Bring) = 2W** (rank-2 W-plane scale + modulus + one orthogonal class; 2+1=3) — **not** three distinct degrees H⁰/H¹/H² (per `calibration-cohomology-alignment`, Lean `QOU.Mass.calibrations_eq_cohomology` — a count/alignment claim, unchanged). The canonical inputs are **weak-sector observables** (m_e, 𝔇_β, 𝔇_π); their proxies are the masses (m_e, m_π) plus the Q-value Q_β. m_e sets the unit; since q₀ is dimensionless it is pinned by m_μ *in that unit* — the ratio m_μ/m_e, the most precise CAL-2 anchor. The exact maps:

- **q₀** ← CAL-2 (𝔇_β), pinned numerically via CAL-1 + the lepton ratio:  `m_μ/m_e = Vol(4₁)/ℏ_q²`, `ℏ_q = 1 − q₀⁻¹`, `Vol(4₁) = 2·Cl₂(π/3) = 6Λ(π/3) ≈ 2.0299`  ⇒ invert for `q₀ ≈ 1.10998`.
  (**Λ vs Cl₂ — do not swap the coefficient.** `Λ(θ) = Cl₂(2θ)/2`, so one regular ideal tetrahedron is `Cl₂(π/3) = 3Λ(π/3) ≈ 1.01494` and the two-tetrahedron figure-eight complement is `2·Cl₂(π/3) = 6Λ(π/3)`. The forms `2Λ(π/3) ≈ 0.6766` and `3·Cl₂(π/3) ≈ 3.0448` are **both wrong** — they arise from keeping one function's coefficient while writing the other function's name.

  **Both are still live, and this line previously said they were not.** It read "both were live in the corpus until 2026-08-10", i.e. an all-clear. The 2026-08-10 drain (#4886 → #4901 → #4917, reported as "14 sites across 12 files, corpus-wide") swept `content/` only. Measured 2026-08-15 with fixed-string grep: **54 sites across 35 files** remain — 5 in `content/`, 28 in `computations/`, 21 in `docs/` (25 `.py`, 17 `.md`, 12 `.json`; **0** in `.lean`/`.ts`, which the drain did clear). Do not read this guard as "already fixed"; assume the file you are editing still carries it, and check. Tracked as `qou-zdz5`.

  Most survivors compute the RIGHT value under the WRONG name — e.g. `VOL41 = 2*mp.clsin(2, mp.pi/3)` is `2·Cl₂(π/3) = 2.0299` ✓ annotated `# Vol(4₁) = 2Λ(π/3)` ✗. So a grep for the bad *name* does not imply a bad *number*; check the arithmetic beside it before "fixing" a value.)
- **Q_β** (the CAL-2 proxy):  `Q_β = ℏ/𝔇_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³) ≈ 0.784 MeV` (0.17% vs CODATA) — the bar-odd `sinh` partner of the bar-even `cosh` meson scale m_π. 𝔇_β **is** CAL-2; because the modulus is overdetermined and pinned most precisely by m_μ/m_e, Q_β reproduced from q₀ is a 0.17% **cross-check**, not a fourth input.

m_π (139.57 MeV) is genuinely independent of (m_e, q₀) (SDP-validated, Vol(Hopf)=0).

> **Two-layer convention (owner-clarified 2026-06-16).** The table above is the canonical *mathematical* calibration. In the **Physical-Observations** layer one may anchor q₀ on a *derived* quantity with smaller experimental error: live compute (`tools/qou-substrate/python/qou_substrate/constants.py::q_at`) pins q₀ on the **proton** ratio m_p/m_e (0.017 ppb vs the muon ratio's 22 ppb; re-pin 2026-05-28 — the figure read "0.06 ppb" until 2026-08-21; the live CODATA table, `qou_substrate.constants.MASS_RATIO_P_E_ERR = float(_P_E.uncertainty)`, carries the tighter value), making m_μ/m_e a 9.5σ cross-check prediction (the μ–p substrate tension). This precision substitution is **not** a change to the canonical CAL-2 and **not** a fourth calibration / second-q₀-pin.

The derivation chain:

```
substrate q_0 → 𝐂 categorical action → Yekutieli non-abelian Stokes → 𝐇_n(q) Hecke
             → Wedderburn decomposition (partitions λ ⊢ n)
             → Frobenius pairing tr_M = Σ_λ y_λ χ_λ
             → confinement SDP → canonical T_w → Archimedean functor at q_0
             → MeV observables
```

Read the cheat sheet for: per-step math + paper references + canonical compute scripts; Φ_q (Faddeev) vs Li_2^q (Rogers) context-sorting; current Phase 5 findings (Phase 5l: ρ_Z^constit = tr_M^3(𝓑_p) structural identity); pipeline-discipline migration backlog.

When working on math-affecting code or content, **trace the change to a step in the chain** and verify the canonical compute script is in the consumer set.

> **🟧 Mass-and-Binding-Algorithms appendix sync (STRICT).** Any PR that touches mass / binding derivations or compute infra (Steps 9a, 9b, 10, 11 of the canonical chain, or any sidecar algorithm — Δ_λ closure, c_k truncation ladder, LP/SDP dual emission, witness-JSON pipeline) **must** update the matching `alg:`-block under [`content/quantum-observable-universe/appendix-mass-binding-algorithms/`](content/quantum-observable-universe/appendix-mass-binding-algorithms/) in the same PR. The appendix is a maintenance contract bridging propositions ↔ Python API; its `uses[]`, `computation.script`, `computation.witness`, and `.md` *Algorithm / Correctness / Python API* sections must stay in sync with the actual compute. Enforced by `local/coordinate.md §2-bis`, `local/compute-author.md §8 pre-work checklist`, `local/compute-audit.md §verification checklist`, and `local/proof-editor.md §coordination rules`. Reviewers diff the appendix against the compute / proof change.

> **🛑 ABSOLUTE MASS EXCISED (owner ruling 2026-08-11, bean `qou-exam`).** The framework no longer claims, targets, or scores an **absolute** nucleon or atomic mass in MeV (m_p, m_n, m_⁴He) as a prediction. Absolute mass is `m_e · (dimensionless ratio)`, and m_e (CAL-1) sets the MeV scale *by fiat* — so the MeV number double-counts the calibration and carries no content beyond the ratio. **The mass-formula shape and the `canonical_mass` facade in the two banners below remain valid — but as `m_e`-scaled *realizations* of the dimensionless ratio / binding, NOT as absolute-mass predictions.** Report ratios (`m_p/m_e`, `m_μ/m_e`, `m_K/m_π`), binding `B(K)`, decay Q-values (`Q_β`), and splittings (`Δ_pn`); do **not** present `m_p ≈ 938.27 MeV` as a framework *prediction* (it remains derivable as `m_e × ratio`, but that is a rendering, not a claim). Broader than the 2026-08-02 q₀-derivation forever-gate — that closed one route; this closes the absolute-mass *target*. Full ruling: [`docs/audits/2026-08-11-excise-absolute-mass-notion.md`](docs/audits/2026-08-11-excise-absolute-mass-notion.md).

> **⚠ Critical framing — the mass formula is `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`; do NOT reintroduce `λ_scale` OR the `Geom_full` wrapper.** Two standing purges: (1) the factor once called `λ_scale` was **absorbed** 2026-05-23 (commit `ffdd84409`) — not a separate constant to derive; (2) the opaque `Geom_full(K)` wrapper was **PURGED 2026-06-06** (owner directive, repeated — it obscured) in favour of its explicit meaning, the **volume–density product** `Vol(K)·ρ(K)/ℏ_q²`. So the per-knot mass is `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²` (electron scale × hyperbolic volume × per-block density). Compute uses `vol_density_borromean` / `vol_density_per_block` / `vol_density` (`_li_2_q_util.py`, `mass_vol_density.py`). The Yekutieli per-cell variant was tried then PURGED 2026-05-24 (`71d674da1`). The "2.89% m_p gap" is between the current categorical `Vol(𝓑₃)·ρ` value and its exact value — **not** a "λ_scale closure" problem. **Do not write `Geom_full` in paper, audit doc, or compute — write the explicit `Vol(K)·ρ(K)/ℏ_q²`.**

> **🛑 CORRECTION (owner ruling 2026-06-24) — `m_e·Vol(𝓑₃)·ρ/ℏ_q²` is NOT the canonical ABSOLUTE nucleon mass. Use the muon-anchored Hecke energy via the `canonical_mass` facade.** The banner above describes the *general* volume–density shape, but read with `K = 𝓑₃` (Borromean) and `ρ ∈ {λ_A, tr_M}` it is the **wrong absolute-mass form** — it applies `1/ℏ_q² (= c_q²)` to the Borromean volume and yields **m_p ≈ 966 (+2.96%, λ_A is a CODATA-implied FIT)** or **≈ 406 (−57%, naive tr_M)**. The canonical absolute nucleon mass is the **muon-anchored** Hecke energy:
> `m_p = 2·(m_μ·F_Bor − 6·m_e)`, `m_μ = m_e·Vol(4₁)/ℏ_q²`, `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³` → **m_p ≈ 938.27, m_n ≈ 939.56 (CODATA)**. The `c_q²` belongs in the **muon** anchor `Vol(4₁)`, then dressed by the *dimensionless* `F_Bor` — not on `Vol(𝓑₃)`.
> **Route every absolute nucleon/atom mass through the single facade [`computations/canonical_mass.py`](computations/canonical_mass.py)** (`proton_mass_mev` / `neutron_mass_mev` / `nucleon_mass_mev`). `mass_vol_density` / `vol_density_borromean` / `linking_weight_family_a` (=λ_A) are **deprecated for absolute mass** (emit `DeprecationWarning`); `vol_density_per_block` stays valid for **binding ratios only** (scale cancels). Read first: [`docs/canonical-mass-formula-guardrail.md`](docs/canonical-mass-formula-guardrail.md). Why it recurred: this very banner read with `K=𝓑₃` *is* the wrong form — that's the trap the facade closes.

> **⚠ Critical framing — Q_β `c_k` is a TRUNCATION ORDER, not a wire/un-wire gate.** The Q_β precision ladder `Q_β = Q_base·Π(1 + c_k·u^k)` with `u = b·ℏ_q² ≈ 0.00852` is a **convergent series**; `N` is the truncation order chosen by target precision (`N ≥ log₁₀(1/ε)/2.07 − 1`). `c_2 = -1` is **structural** — no fit, no CODATA, no q₀ (see the correction immediately below, which restates two halves of this sentence's earlier wording); `c_k ≥ 3` are q₀-dependent NEAR-MATCHES (e.g. `c_3 = -2 = J_Hopf(q=1)` is 3.47 % from the extracted `c_3` at m_p-pin q₀ — **or 3.35 %, the same gap normalised by the extracted value rather than by `-2`; see below**), with the N=4 → N=5 non-monotonicity as the experimental signature.
>
> **🛑 CORRECTION (2026-08-16, owner-authorised; beans `qou-f09n` + `qou-cwin`).** Three claims above needed fixing, one of my own proposed fixes was itself wrong, and the two facts are worth separating.
>
> 1. **"`c_2 = -1` is PROVED Taylor-exact" — ONE half is wrong, and it is NOT the half the bean originally named.**
>    - **"Taylor" is UNDER-SPECIFIED, not false.** Bean `qou-f09n` (my own text) asserted that *"under the natural reading of 'Taylor' the `u²` coefficient is `−9/8`"*. That is **a** reading offered as **the** reading, and it is **retracted**. Measured symbolically: the `u²` coefficient of the **explicit-factor product** `Π_{k≥2}(1 + c_k u^k)` is exactly `c₂` — trivially, since there is no `k = 1` factor — so `c₂ = −1` **is** a Taylor coefficient of *that* series. It is `c̃₂ = c₂ − 1/8 = −9/8` only for the **full normalised model** `Φ(u)/Φ(0)`, i.e. with the cosine factor inside the series (`QOU.QBeta.normalisedQuadCoeff_eq`, sorry-free, and independent of the phase `α`). **So the fix is to say WHICH SERIES, never to delete the word.** Registry [§9i](docs/coordination/ck-dk-canonical-registry.md); the three live meanings (`c₂` / `c̃₂` / `c₂^even ≈ −8.006`) are separated in §2 and in the notation register.
>    - **"PROVED" IS wrong.** The Lean is `1 − b²ℏ⁴ = 1 − (bℏ²)²`, a one-line `ring` identity: it proves only that *re-reading* the N=2 factor in the ansatz form yields `−1`. Corpus-grepped: `N2_factor` is a bare `def` with **no** theorem deriving it — every use in `QBetaCategoricalPrecisionLadder.lean` merely `unfold`s it, and its provenance ("Kashiwara `f̃_1†f̃_1`") lives in a docstring. **"Structural" is the defensible word** (no fit, no CODATA, no q₀) and is what the source block itself claims; the compression to "PROVED" happened here, not there.
> 2. **"`N` is the truncation order chosen by target precision" does not describe the canonical producer.** `qbeta_ck_cache.py` extracts **one** rung by inverting the target; the residual at the next rung is then **exactly zero**, not merely below tolerance, so its guard fires and `c_4 … c_7` are **never computed** (`QOU.QBeta.greedy_rung_exact` / `greedy_later_rungs_vanish`, sorry-free). Whether some abstract ladder converges is a separate question this does not settle; the point is that no `N` is being *chosen* by an `ε` anywhere in the producer.
> 3. **The "3.47 %" is NOT stale — I checked, expecting it to be.** It is `|−2 − c₃|/2 = 3.4671 %`; the ladder witness's own `err_pct` field reports `3.3509 %`, which is the **same gap** normalised by the extracted `c₃ = −2.06934258` instead. Do **not** "fix" either number into the other. That this trap sits in the same banner as defect 1 is the point: **a quantity differing only by normalisation, mistaken for a discrepancy, is the exact error class this correction is about.** The cross-anchor swing quoted as "≈ 3 %" measures **2.3748 %** (proton-normalised; 2.4571 % normalised by the candidate `-2`). That "≈ 3 %" traces to a **superseded** muon `c_3 = -2.0097` (pre-#1422; today's is `-2.02020024`), and the corpus's `2.98 %` / `2.88 %` are that one stale gap under the two normalisations — resolved in [`qbeta_c3_crossanchor_swing_provenance_probe.py`](computations/qbeta/qbeta_c3_crossanchor_swing_provenance_probe.py) (3/3). Verdict unaffected. Report TIERED (`proved` / `near-match` / `fitted`), never binary wired/dropped — the four-session wire/un-wire flip-flop (#1452 ↔ #1479) came from conflating "N=3 beats 100× experimental" (true) with "c_3 = -2 is Taylor-exact" (false). **Canonical reference (read before any `c_k` wire/un-wire decision): [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).** Permanent fix is the Q_β Habiro element (parallel α_EM `[2]_q·(1−h²α)` in PR #1511). **2026-05-31 c_3 SETTLED** (PR #1580 verdict audit + flip-flop history table now at 6 entries in [`docs/coordination/1ppq-qbeta.md`](docs/coordination/1ppq-qbeta.md)); Li_2^q × spectral combiner refuted as mech #7 (PR #1609); Δtr_M bar-decomposition recorded as structural observation (PR #1615) — none of these wire to production.
>
> **🛑 CONVENTION LABEL (2026-08-15 ruling) — every number in this banner is
> CONVENTION-C-frame.** `c_2 = -1`, `c_3 = -2 = J_Hopf(q=1)`, the 3.47 % swing,
> and the whole `c_k` ladder were derived with the Markov parameter
> `z = √q/(q+1)` (convention C). The owner ruling of 2026-08-15 makes
> **convention D (`z = q³/(q²+1)`) canonical**. The values above are **correct
> for C** and are kept as recorded — they need *scoping*, not correction; do
> **not** "fix" them. **The ladder must be RE-DERIVED under D, and that is not
> a z-swap** — `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
> ([`MarkovZFullBarCondition.lean`](content/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean),
> sorry-free) makes the C-frame ladder and the mass channel's three-row forcing
> mutually exclusive, so substituting `z_D` into the existing ladder is not a
> valid move. Until the re-derivation lands, treat every `c_k` conclusion —
> including the downstream `c₃^even = −Vol(4₁)`, `[3]_q/25`, `J − ℏ²`, `S_leak`
> and `q*_S` facts — as **C-conditional**. Tranche S1, bean `qou-cds1`;
> §S1 of [`docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md`](docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md).

> **⚠ Critical framing — Im(q) at fibre vs observable level (2026-06-01).** A recurrent source of confusion in the c_k flip-flop saga and the (1+q)/2 Option-E v9 near-match: distinguish two levels of "Im(q)":
>
> | Level | Im(q) status | Where |
> |---|---|---|
> | **Observable / archimedean** (post-τ functor) | **Im(q_0) = 0** (verified — `lusztig_q_0_imaginary_part_zero` assertion in `four_unwired_theorems_regression.py`) | the MeV evaluation at substrate q_0 requires real q for real masses |
> | **Fibre / categorical** (pre-τ, formal q) | **Im(q) unconstrained** | formal variable in 𝐇_n(q); Hecke reps over ℂ; complex residues in `term6_full_pole_sum.py`; KZ/Habiro q-difference equations |
>
> **The c_k Taylor coefficients live in the FIBRE** (formal q-deformation, potentially complex). Each q_0 anchor is a different archimedean evaluation of the SAME fibre object. The "cross-anchor swing" caught as "near-match" is the **fibre object having structure beyond a real constant** — exactly what you'd expect if c_k(q) is a complex-analytic function evaluated at real q_0.
>
> **Implication for any Habiro element / Δ_λ closure attack**:
> - ❌ Looking for a REAL formula `c_3 = f(q_0_real)` that matches multiple anchors — was already known to fail
> - ✓ Looking for a **fibre-level** Habiro element `F(q) ∈ Habiro ring` whose archimedean evaluation at any q_0 reproduces the c_3 at THAT anchor — different question
>
> This is consistent with α_EM PR #1511: `[2]_q · (1 - h²α)` is a fibre-level element; its real Taylor coefficients are what get evaluated.
>
> The `lusztig_q_0_imaginary_part_zero` assertion is an **archimedean constraint** on the evaluation at the substrate anchor — NOT a categorical/fibre claim. Agents searching for c_k or Δ_λ closures must NOT conflate the two levels.

## Precision goals (STRICT — read before any precision-affecting work)

The framework's headline precision goal has **two independent legs**.
Authoritative reference: [`docs/precision-goals.md`](docs/precision-goals.md).

| Leg | Target | Status |
|-----|--------|--------|
| **L1. Compute precision** | internal cross-method agreement ≤ 1 ppQ (10⁻¹⁵) at substrate q_0 | met — `_precision.py` default is 65 dps compute / 50 dps serialization (10⁻⁵⁰ absolute truncation) |
| **L2. Per-observable accuracy** | for each predicted observable O: `σ_pred(O) ≤ σ_exp(O) / 100` | **1/5 scoreable met (`m_K/m_π` alone) — but that 1 is a truncation-fit + α_em-`sorry`-conditional, so 0/5 UNCONDITIONAL parameter-free (red-team 2026-08-22, see below)** — quote `beats_100x_scoreable`/`scoreable_total`, NOT `beats_100x_count=2`, which counts the calibration inputs `m_p` and `m_e` (corrected 2026-08-18) — see `per-observable-100x-status.witness.json` (`beats_100x_count=2`); the 5 missing observables (m_p, m_μ, Q_β, m_n, Δ_pn) — note **m_p misses by ~437× since 2026-07-04** (the fitted Habiro tower that landed it on CODATA to 0.0004 ppb was dropped; de-fitted round-trip +1.35 ppb — see [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md)) and **m_μ misses by 963.6× post-re-pin**, see below — and the Q_β/m_n/Δ_pn trio share a single root cause documented in [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md) |

**Key distinctions** (avoid agent confusion):

- **L1 ≠ L2.** A formula that is compute-stable to 50 digits (L1 met)
  can still miss its 100× experimental target by 10⁴ (L2 missed).
- **L2 is variable per observable.** Q_β target is 7.8 ppb; currently
  measured at 1279 ppb (164.0× miss) per the dashboard (fresh run
  2026-05-31) — the Habiro-exact 5.7 ppb result was against the
  pre-re-pin (muon-anchored) q₀ and has not been refreshed since the
  2026-05-28 proton-anchor re-pin
  (see [`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`](docs/audits/2026-05-30-q0-repin-stale-witness-audit.md)).
  Absolute m_p target is 3 ppt (research-grade, below CAL-2 floor).
- **m_μ is no longer a met goal (2026-05-31 correction).** Before the
  2026-05-28 proton-anchor re-pin, m_μ was the q₀ *anchor* (err ≈ 0).
  Post-re-pin it is a *prediction* (m_e × (m_μ/m_e)_CODATA) and misses
  the 100× target by **963.6×** (209.8 ppb vs 0.2177 ppb target) per
  the dashboard. An earlier version of this table listed "4/7 met
  (… m_μ …)"; that was stale (the q0-repin staleness class).
- **m_p dropped from "met" 2026-07-04.** Through 2026-07-04 the count was
  3/7 (m_e, m_p, m_K/m_π), but m_p "met" only because a fitted Habiro
  tower `(1+46u⁴)(1+4u⁵)(1−29u⁶)` landed it on CODATA to 0.0004 ppb. That
  tower was a muon-era fit left applied to the proton-pinned q₀ (a live
  +242 ppb regression) and was **dropped**; the honest documented-pin
  round-trip is +1.35 ppb, a ~437× miss. Full analysis:
  [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md).
- **🛑 The authoritative count is 1/5 SCOREABLE, not 2/7 (corrected
  2026-08-18).** `beats_100x_count = 2` counts **calibration inputs**
  alongside predictions. The dashboard already excludes `m_p` from scoring
  as an anchor round-trip ("the framework content cancels"), but **scores
  `m_e`**, whose `err_ppb` is not measured but *defined* zero — `m_e` is the
  CAL-1 input that fixes the MeV unit, so its ratio to itself is 1 by
  construction. That is the same argument `m_p` is excluded for, only
  stronger. Separating inputs from predictions, **1 of 5 scoreable
  predictions meets L2, and it is `m_K/m_π`** — the only *ratio* among the
  five. Quote `beats_100x_scoreable` / `scoreable_total` from the witness,
  **never** bare `beats_100x_count`. Full analysis:
  [`docs/audits/2026-08-18-mass-binding-accuracy-what-is-closeable.md`](docs/audits/2026-08-18-mass-binding-accuracy-what-is-closeable.md).
- **🛑 Even the 1/5 is inflated — the UNCONDITIONAL parameter-free count is
  0/5 (red-team 2026-08-22).** The single "scoreable win" `m_K/m_π` is itself
  **not** a parameter-free prediction. Its derived core `√([3]_q·[4]_q)` (a
  legitimate ~0.1 % categorical postdiction of the strong ratio) misses this
  observable's own — unusually loose, 264 ppb — 100× target by **385×** on its
  own; the sub-100× result is manufactured by an EM correction
  `(α_em/π)·(3q²−1)/(2q²)` whose **truncation order beats the untruncated
  series** (chosen against the data — the same fit signature the `c_k` red-team
  caught) and whose `α_em` input is **conditional on an open Lean `sorry`**
  (Witten-κ Gram determinant). So `beats_100x_scoreable = 1` is the dashboard's
  arithmetic metric; the count of **unconditional, parameter-free** sub-100×
  predictions is **0**. State it as "1/5 scoreable — and that 1 is
  truncation-fitted + α_em-`sorry`-conditional ⇒ **0/5 unconditional**". Full
  analysis:
  [`docs/audits/2026-08-22-mK-mpi-l2-red-team.md`](docs/audits/2026-08-22-mK-mpi-l2-red-team.md).
- **"1 ppQ" by itself is ambiguous** — say "L1 compute met" or
  "L2 met for observable X" not bare "1 ppQ".
- **1 ppQ** = 1 part per quadrillion = 10⁻¹⁵ relative = 10⁻⁶ ppb.
  Upgraded from 1 ppb (2026-05-26) because the old target was noise.

**Two subgoals under L2:**

- **Subgoal-1 (achievable):** 100× targets ≥ ~780 ppb CAL-2 floor.
  Closure path: per-isotope Borromean-tower extension + operator-
  valued branching combiner.
- **Subgoal-2 (research-grade, OPEN for all EXCEPT q₀-derivation —
  see the 🛑 gate below):** 100× targets < CAL-2 floor (absolute
  m_p / m_n / m_⁴He). These absolute-mass targets classically *require*
  substrate-derivation of q_0, which the coordination ledger declined
  on 2026-05-08, the owner **generally reversed on 2026-07-11**, and the
  owner then **PERMANENTLY RE-GATED on 2026-08-02** (bean `qou-eic1`):

  > **🛑 OWNER RULING 2026-08-02 — substrate-q₀ derivation is FOREVER
  > GATED.** No agent may pursue deriving `q₀` from the substrate, in any
  > form, ever. This is a **permanent** gate, **not** a decline awaiting
  > reversal, and it **supersedes the 2026-07-11 "open for all" reversal
  > for the q₀-derivation item ONLY.** Everything else in Subgoal-2 stays
  > open for all: `Δ_λ` magnitude, the per-isotope binding `M_n(K)`
  > closure, absolute `m_p / m_n / m_⁴He` via any route that does **not**
  > go through deriving `q₀`, and the s5-so3 keystone. If a route you are
  > considering routes through "derive `q₀`," **STOP — it is forbidden.**

  For every non-q₀ route the anti-fit / anti-laundering discipline still
  gates *how* (a fit is not a derivation), not *whether*.
  - **Narrow owner reversal (2026-06-19, recorded 2026-06-22; PRs #2503 /
    #2524).** The owner reversed this decline **only for the s5-so3 keystone
    geometric-realization construction** — the differential-geometry /
    WRT(S³/2I) build of the `W_λ` index (see
    [`docs/coordination/s5-so3-keystone.md`](docs/coordination/s5-so3-keystone.md)).
    That specific geometric `W_λ` build was the first item brought in scope.
    *(Superseded in breadth by the 2026-07-11 general reversal below.)*
  - **🟧 GENERAL owner reversal — Subgoal-2 open for all (2026-07-11).** The
    owner reversed the 2026-05-08 decline **generally**: the geometric /
    substrate-derivation routes to the Subgoal-2 targets (absolute
    m_p / m_n / m_⁴He; ~~substrate-derivation of q_0~~ **[🛑 FOREVER GATED
    2026-08-02 — q₀-derivation is permanently excluded; see the ruling
    above]**; the per-isotope binding
    `M_n(K)` edge-set / coordination-graph closure; the s5-so3 keystone) are
    now **in scope for all agents** — no longer owner-gated, no per-item
    sign-off required (**except q₀-derivation, which is permanently gated**). Context: the qou-v0yw binding-weight closure (the
    M₃/M₄ weights of `conj:binding-manybody-eq-jet-filtration`) was blocked
    *only* by this gate plus the anti-fit rule; the gate is now lifted.
    **The anti-fit / anti-laundering honesty discipline is ORTHOGONAL to this
    scope gate and STILL STANDS:** the `Δ_λ` "no seventh fit-based ansatz"
    rule (below), the §"Axiomatization is NOT a Proof" anti-laundering rule,
    and "sorry-free ≠ derived" all remain in force. "Open for all" grants
    permission to *pursue and derive*, not to pass a fit off as a derivation
    or wire an anchor-inverted `wₙ(K)` to production as canonical. Full
    ruling: [`docs/audits/2026-07-11-subgoal2-owner-reversal-open-for-all.md`](docs/audits/2026-07-11-subgoal2-owner-reversal-open-for-all.md);
    [`docs/precision-goals.md`](docs/precision-goals.md).

**Δ_λ gate (Track A blocker).** The per-isotope binding-energy
formula `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` requires per-partition Δ_λ
values. **The per-partition VALUE is now PROVED** (2026-08-02,
sorry-free, general-n): `Δ_λ = (-1)^{n(λ)}·dim V_λ` (the signed
Springer dimension; sign = jet-order valuation parity, magnitude =
Wedderburn dimension) —
`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional` (PR #4580),
wired to `computations/delta-lambda-witness.json` (value_only). **What
remains open is NOT the value — it is the many-body binding
MAGNITUDE**: the six closure ansätze (Frobenius co-Casimir, Demazure-
fibre, LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov)
all failed on the deuteron because they tried to force the magnitude
`r* ≈ 1.585` into a per-block Δ_λ, which is structurally impossible
(no per-block weight converts an intensive quantity into an extensive
one; the missing term is a separate, super-pairwise additive extensive
object — pairwise cap `ρ_A ≤ C(A,2)` proved in
`QOU.MassTheory.exchangeDet_pow_two_le_four`). **Do not propose a
seventh fit-based ansatz for the MAGNITUDE** — the three-calibration
discipline review will catch it. Full framing:
[`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md).

> **🟧 GENERAL owner reversal — the Δ_λ gate is OPEN FOR ALL (2026-07-13).**
> The owner has lifted the *direction/scope* narrowing on the Δ_λ closure:
> any **derivation** route (geometric / substrate / categorical brane-tower /
> Option E and beyond) is now **in scope for all agents**, no owner per-item
> sign-off — mirroring the 2026-07-11 Subgoal-2 general reversal. The
> "productive directions" list below is now a *starting-point suggestion*, not
> a restriction. **The anti-fit / anti-laundering discipline is ORTHOGONAL and
> STILL STANDS:** the "no seventh fit-based ansatz" rule above, §"Axiomatization
> is NOT a Proof", "sorry-free ≠ derived", and "conditional-proved ≠
> premise-established" all remain in force. "Open for all" grants permission to
> *pursue and derive* — a Δ_λ obtained by inverting the AME anchors is still a
> **fit**, must be labelled one, and may **not** be wired to production as
> canonical; only a *derived* Δ_λ may. The **Lean-proved PROBE-4 prune** below
> (KL-positivity vs the mixed-sign target) is a *proved exclusion*, not a scope
> gate — it stays pruned. Full ruling:
> [`docs/audits/2026-07-13-delta-lambda-gate-open-for-all.md`](docs/audits/2026-07-13-delta-lambda-gate-open-for-all.md).

Suggested starting points (no longer a restriction): GAP-A-3 / GAP-A-4
(categorical brane-tower level selection / ρ general rule) and Option E **via
the A=4 interface operator (PROBE 2)** + `conj:s5-so3-fiber-action`.
**Option E's Kashiwara-crystal / KL-weight sub-path (PROBE 4) is
PRUNED**, not a productive direction: the target
`Δ_λ = sgn(w_0^{S_{λ'}})·dim` is mixed-sign (n=3: 1+/2−; n=6: 6+/5−)
but KL multiplicities `n^w_λ` are non-negative (KL positivity), so a
`Σ_w n^w_λ·X_w` sum supplies at most the magnitude `|Δ_λ| = dim`,
never the chirality sign — engine-verified at S₄ (PR #2381) and the
mixed-sign premise Lean-proved sorry-free (PR #2416,
`PartitionOf5.deltaSign_mixed`). Full context:
[`docs/audits/2026-05-18-delta-lambda-gating-context.md`](docs/audits/2026-05-18-delta-lambda-gating-context.md);
Option-E ledger
[`docs/coordination/option-e.md`](docs/coordination/option-e.md);
PROBE-4 prune
[`docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md`](docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md).

**Where to check status:**

- L1: `computations/onepb-status-dashboard.witness.json`
- L2: `computations/per-observable-100x-status.witness.json`

**When writing a precision-affecting change**, run BOTH dashboards
and report the deltas. Mention which leg the change addresses.
Do not regress either.

### q₀ anchor convention — ideal CAL-2 (muon) vs experimental anchor (proton) (STRICT)

> **🛑 OWNER RULING 2026-08-15 — convention D canonical (C excised); proton pin
> canonical; colour weighting canonical.** Verbatim: *"convention D is
> convention. excise convention C."* / *"similarly, use proton pin and color
> wighting"*. Record, measured blast radius, and ordered tranche plan:
> [`docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md`](docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md).
> It supersedes the `disputed` registration of the `qbeta-decay` trace channel
> (PR #5111) and answers the trace-convention registry's one
> `owner_decision_required`.
>
> - **R1 — convention D (`z = q³/(q²+1)`) canonical; C (`z = √q/(q+1)`)
>   excised.** **Largely a RE-AFFIRMATION** — the 2026-08-09 ruling had
>   already excised C. R1's new work is the two surviving carve-outs: the
>   `qbeta-decay` channel registered `disputed` (PR #5111) and the registry's
>   one `owner_decision_required`. It removes the *convention* question from
>   `tools/pyhecke/gram.py::z` but **not** the Gram singularity under D —
>   that is a numerical blocker, bean `qou-cds2`.
>
>   **A clean detector run is NOT evidence the C surface is clear.**
>   [`scripts/convention-c-producer-audit.py`](scripts/convention-c-producer-audit.py)
>   once reported **0 actionable C producers**. That count was real but
>   **narrow**: it keyed on *assignment targets*, so a convention-C value
>   **returned from a function** was structurally invisible to it. Measured on
>   `main` 2026-08-16 — **7 files** returned `1/(√q + 1/√q)`, which is
>   `√q/(q+1) = z_C` *exactly* (`0.49932…` against D's `0.61268…`).
>
>   **Status 2026-08-16, corrected 2026-08-24.** The detector now scans return
>   forms, and those seven are migrated, so *that* spelling is closed. This then
>   named `pyhecke/gram.py:634` (`z_mp`) as **the only return-form C site left in
>   the tree** — stale in both coordinates by the time it was written. `z_mp` is
>   at **line 645** and is **convention D**: its docstring reads *"z = q³/(q² + 1)
>   … MIGRATED 2026-08-16 (bean `qou-cds2`)"*, and the module's `_Z_FRAC =
>   _Q_FRAC**3 / (_Q_FRAC**2 + 1)` is D arithmetic. The paragraph was stamped the
>   same day as the migration, which is presumably how they crossed.
>
>   **Do NOT read that as "the return-form surface is clear."** The named instance
>   is retired; the count is not. Re-run 2026-08-24, the detector still reports
>   **1 site in `tools/pyhecke` as "C with NO registry row (unexplained)"**, and
>   this correction did **not** identify it — so one pyhecke site remains
>   unaccounted for. **The posture does not change.** Closing one shape does not
>   close the class —
>   [`docs/audits/2026-08-15-detector-blindness-taxonomy.md`](docs/audits/2026-08-15-detector-blindness-taxonomy.md)
>   catalogues **thirteen** distinct detector-blind spellings, four of which were
>   found *by* detectors written to catch the previous blind spot. So: **treat
>   the remaining C surface as UNMEASURED rather than clear — and do not launch
>   a corpus-wide sweep off any of these numbers.** R1 settles which convention
>   is canonical; it does not tell you how much code still disagrees.
>
>   **The counter-move, when the result is exact and symbolic: test the ANSWER,
>   not the source.** Every detector above keys on how the convention was
>   *written*; the algebraic form of the result keys on what it *is*. The Markov
>   peel's deuteron denominator factors as `192·q²³·(q²+1)³` — one `(q²+1)` per
>   peel, because `z = q³/(q²+1)`. Convention C leaves half-integer powers and
>   cannot produce it, so *"`(q²+1)` divides the denominator"* is a complete
>   convention test needing no source, no `z` grep and no anchor
>   (`computations/markov/peel_anchor_identification_probe.py`, #5190). A value
>   cannot be stale, mislabelled, re-spelled, or inherited from a stale record
>   and still factor correctly.
>
>   Two examples of why the count is not the answer. The first has since
>   **moved, and is recorded because the moving is the point**: this named
>   `pyhecke/atom.py:691` binding a C `z_mark` consumed at `:713`. Measured
>   2026-08-24, `z_mark` occurs **once** in that file, at **line 720**, and it is
>   a **comment** — `#   local  z_mark = 1/(q^½ + q^-½) = 0.4993203  ← convention
>   **C**` — so there is no binding for a waiver to cover, and an AST-verified
>   detector cannot see it at all. Whether the binding was migrated or merely
>   re-spelled is **not** settled here. Second, a *declared* site is not a fixed
>   one — the audit's `DECLARED C in evaluators.z, R10-waived` bucket stays
>   **actionable** by design.
>
>   Three named instances in this one section have now gone stale between being
>   written and being read (`z_mp`, `z_mark`, and the `y_lambda_at` trap two
>   sections down). That rate is itself the argument for the posture above:
>   **cite the rule, re-measure the instance.**
> - **R2 — proton pin canonical.** Reaffirms the 2026-08-07 directive
>   immediately below; nothing in that directive changes. The *ideal CAL-2
>   definition* (`𝔇_β`, proxy `m_μ/m_e`) is untouched — R2 governs which pin
>   code **evaluates** at, not what the calibration **is**.
> - **R3 — `bring_color_weighted` canonical** as the p/n convention. Six live
>   non-comparison files are still off-canon (bean `qou-cds4`).
>
> **The Q_β `c_k` ladder is convention-C-frame throughout and has not been
> re-derived** (bean `qou-cds1`) — see the convention note on the `c_k`
> truncation-order banner earlier in this document before wiring or
> un-wiring any `c_k`.

> **🟧 OWNER DIRECTIVE (2026-08-07) — ALL AGENTS AND ALL PRODUCTION CODE
> DEFAULT TO THE EXPERIMENTAL (PROTON) ANCHOR.** When any code, probe,
> witness, dashboard, or agent needs a numerical `q₀`, the default is the
> **experimental / Physical-Observations** pin — proton, `m_p/m_e`,
> `q₀ ≈ 1.1099785827513808`, i.e. `q_parameter.Q` /
> `tools/qou-substrate/.../constants.py::Q`. **Do not read a muon-pinned
> value into new compute.** This supersedes the previous default in which
> the `computations/` layer silently supplied the muon pin.
>
> **What this does NOT change.** The *ideal mathematical* canonical is
> still CAL-2 = `𝔇_β` with proxy `m_μ/m_e` — that is the **definition** of
> the calibration and is unaffected. The directive is about which
> **numerical evaluation** code defaults to, not about redefining the
> 3-CAL triple. Prose describing the canonical derivation chain keeps the
> ideal framing; *compute* uses the experimental pin.
>
> **Never straddle the two layers inside one quantity.** Mixing an
> ideal-layer input with an experimental-layer input in a single computed
> number is a defect regardless of its size. Worked example + measurement:
> the μ₃ Fréchet probe took `y_λ` from the muon-built cache while
> evaluating `χ_λ` at the proton `q₀` — an 11.54 ppb layer separation (=
> the μ–p substrate tension itself), ~1e-7 relative on the result. See
> [`computations/deltalambda/mu3_anchor_consistency_probe.py`](computations/deltalambda/mu3_anchor_consistency_probe.py)
> and [`docs/audits/2026-08-07-mu3-door-status-consolidated.md` §4ter](docs/audits/2026-08-07-mu3-door-status-consolidated.md).
>
> **The shape to check for (the rule; its named instance is now closed).**
> A cached-witness accessor that serves precomputed data **when the caller's
> `q` matches the value the cache was built at** is a straddle waiting to
> happen: that gate is satisfied *trivially* when the caller passes the package
> constant itself, so an ideal-layer cache reaches an experimental-layer caller
> with **no signal that a layer boundary was crossed**. Audit any accessor with
> that shape.
>
> **🛑 The instance this rule used to name — `y_lambda_at` — no longer has the
> shape (corrected 2026-08-23, bean `qou-c1ya`/`qou-vu19`).** This paragraph
> read *"`wedderburn_jones_markov.y_lambda_at(n, q)` returns the cached
> muon-built `y-lambda-at-q0.witness.json` whenever `|q − q_parameter.Q| <
> 1e-12`"* and told you to call `y_lambda_at_q0_mpmath` instead. **That
> describes pre-2026-08-09 behaviour.** Read at the body rather than the
> docstring — the live function is five statements:
>
> ```python
> if q_val is not None:
>     return y_lambda_su_n(n, mpf(str(q_val)), 2)   # the CALLER's q
> return y_lambda_su_n_symbolic(n, Q_SYM, 2)        # symbolic, anchor-free
> ```
>
> No `.witness.json` anywhere in it, and `y_lambda_su_n` is read-only
> ("writes no witness, runs no producer") — the whole call cone is cache-free.
> The gate and the cache load moved into
> `_y_lambda_at_convention_C_HISTORICAL`, which is **dead** (convention C,
> excised 2026-08-09). So `y_lambda_at` is **anchor-neutral**: calling it says
> nothing about a producer's layer.
>
> **Do not "fix" call sites on the strength of the old wording.** Measured
> cost of trying: promoting `y_lambda_at` to a muon *identifier* check in
> `q0_producer_pin_classifier` — which is exactly what the old paragraph
> invites — reclassified **56 producers** from `proton` to `BOTH`, and `BOTH`
> shields a producer from triage as a possible deliberate comparison. It would
> have hidden 56 clean files behind an association the code no longer has.
> `y_lambda_at` has been removed from that classifier's `MUON_ARTIFACTS`.
>
> **The rule above still stands, and has been measured: zero live instances.**
> [`computations/audits/cached_accessor_shape_audit.py`](computations/audits/cached_accessor_shape_audit.py)
> keys on **provenance** (a name assigned from a file read, at module level or
> via `global` in a loader) rather than on a list of constant names, and
> requires the gate to involve a **caller argument** — without that it returns
> 34, almost all plain memoisation. Its `--selftest` fails unless the known
> dead positive is detected, so a future narrowing cannot report a clean tree
> the way a name-keyed version did. Current result: **2 hits, both the dead
> historical function and its generated `qou-mass/_internal/` mirror.**
>
> **The μ₃ Fréchet incident above is unaffected** — 11.54 ppb, `y_λ` from the
> muon-built cache against `χ_λ` at the proton `q₀`, is a real measured
> straddle and the reason the rule exists. Only the *mechanism* has changed.

The substrate modulus q₀ has **one** value but **two** documented pins
(authoritative corpus:
[`observations/three-calibration-discipline.md` §3](content/quantum-observable-universe/observations/three-calibration-discipline.md),
[`observations/epistemic-status-of-calibrations.md`](content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md),
[`mass-theory/rem-qstar-decay-sector-q0.md`](content/quantum-observable-universe/mass-theory/rem-qstar-decay-sector-q0.md) — the decay-sector point `q*`, which is **conditional on (H1)** and is **NOT** an independent third determination; see registry §9f):

> **Dead citation corrected 2026-08-11.** This list previously named
> `observations/substrate-anchor-alternatives.md`, which **does not exist**
> anywhere in `content/` or `docs/` — an authoritative pointer in this document
> resolving to nothing. Replaced with the live block covering the alternative
> (decay-sector) anchor. Found while adding the §"Which pin the numbers
> actually use" subsection to `epistemic-status-of-calibrations`.
>
> **Descriptive clause corrected 2026-08-15** (PR #5074, bean `qou-kh7e`). The
> replacement first read *"— the third, decay-sector determination of the same
> modulus"*. There is no such determination: `q*` is root-found on
> `S(q) = c₃(q) + Vol(4₁)` where `c₃ = (Q_β^exp/Q_N2 − 1)/u³` is **extracted
> from experimental Q_β**, so locating it **presupposes (H1)**
> `c₃^even = −Vol(4₁)`. It is independent of the two **mass** pins only, which
> is weaker and different. **Two** pins; μ–p is a **two-way** tension. The
> dead-citation fix above stands — only the clause describing the block was
> wrong.

| Layer | q₀ pin | m_μ status |
|---|---|---|
| **Ideal / canonical 3-CAL** | **CAL-2 = 𝔇_β**, pinned via its proxy `m_μ/m_e = Vol(4₁)/ℏ_q²` | proxy/anchor **input** — exact *by construction* when used to pin q₀ |
| **Experimental / Physical-Observations** | **m_p/m_e** (0.017 ppb; re-pin 2026-05-28) | **9.5σ prediction**; misses L2 100× by **963.6×** (~210 ppb) — the μ–p substrate tension |

The proton re-pin is a **precision substitution within the same
overdetermined H¹ datum — NOT a 4th calibration and NOT a change to
CAL-2.** (CAL-1 = m_e; CAL-2 = 𝔇_β, proxy m_μ/m_e; CAL-3 = 𝔇_π, proxy
m_π; Q_β = ℏ/𝔇_β is the **CAL-2 proxy**, not CAL-3 — see the decay-width
cheat-sheet ruling above.) Pin on the most precise ratio so the unavoidable ~11.5 ppb
theory residual lands where least significant (proton-anchor → 9.5σ on
muon; muon-anchor → ~4000σ on proton).

**STRICT rules:**

1. **Every precision / accuracy / prediction artifact** — the L2 100×
   dashboard, `per-observable-100x-status`, accuracy audit docs,
   "N/7 met" counts — **must report m_μ as the proton-anchored
   prediction (963.6×, FAIL), never "exact / ~0 ppb / MET".** An m_μ
   value ≈ CODATA computed at the muon q₀ is the CAL-2 calibration
   tautology ("equality by construction"), **not** an accuracy win.
   **The same rule applies at CAL-1, and was not being applied.** `m_e` is
   the CAL-1 input that fixes the MeV unit; its `err_ppb` is *defined*
   zero, not measured. Scoring it as a "beat" is the identical tautology
   this rule forbids one line above. The canonical L2 count is therefore
   **1/5 scoreable** — `m_K/m_π` alone — **not** 2/7, and not 3/7 or 4/7.
   Quote `beats_100x_scoreable` / `scoreable_total`; `beats_100x_count = 2`
   is retained in the witness for consumer compatibility and **must not be
   quoted as an accuracy result** (corrected 2026-08-18).
2. **Two q₀ live in the repo; do not conflate them, and default to the
   proton one (owner directive above):**
   - **Package layer** `tools/qou-substrate/.../constants.py` (`Q`,
     `q_at()`, `Q_50_DIGIT_STR`) is **proton-pinned**
     (`_solve_q_proton_f64`), q₀ ≈ 1.1099785827513808 — **this is the
     DEFAULT for all new compute and all production code**, not merely
     "for precision/prediction".
   - **`computations/` layer** historically carries **muon-q₀**
     witnesses: `…/q-pinning-50-digit.witness.json` holds the muon value
     `1.10997859555733471…` (−11.5 ppb), feeding ~72 producers /
     **870** witnesses — the canonical 3-CAL (muon) derivation witnesses.
     (Re-measured 2026-08-15 and again 2026-08-16 over the 2941 tracked
     `computations/*.witness.json`: **870** carry the muon fingerprint —
     **801 muon-only** and **69 also carrying the proton pin**. The
     previous figure here was "~840"; the error was **low, not
     stale-high**. A both-pin witness is either a deliberate comparison
     or a layer straddle — see the straddling hazard above; triage is
     bean `qou-cds3`.)
     These remain **valid as recorded** (they are what they say they are)
     but are **no longer the default an agent should reach for**; see
     rule 4 for the migration posture.
3. **Recurring bug to watch (bean `tnjb`):** a dashboard/witness that
   reads a **muon-q₀** `muon_check.m_mu_pred_MeV` (≈ CODATA, ~0 ppb)
   and scores it as the m_μ *prediction* silently flips m_μ FAIL→MET.
   The committed `per-observable-100x-status.witness.json`
   (m_μ ≈ 105.6583978, 963.6×) is the **canonical** value; a fresh run
   that reads the muon-q₀ Borromean witness (≈ 105.6583756, 1.36 ppb)
   is the symptom.
4. **Migration posture for the 870 muon-q₀ `computations/` witnesses
   (updated 2026-08-07; count re-measured 2026-08-16).** The owner
   directive above sets the *target end state*: experimental (proton)
   everywhere in compute. It does **not** authorise a bulk rewrite as an
   idle-drain — that sweep is large, is tracked under bean **`qou-1c4y`**,
   and still needs scoped sign-off before it runs. **The 2026-08-15 ruling
   (R2) does not change this.** R2 restates the end state; it does not
   scope the sweep, so the sign-off requirement stands. If the owner
   intends R2 to authorise the bulk migration, that has to be said here
   explicitly — do not infer it from R2's wording.

   > **🟧 OWNER AUTHORISATION, RECORDED 2026-08-19 (the gate above is now
   > SATISFIED — read the four constraints before running anything).**
   > The owner gave the directive in session on 2026-08-15, in these words:
   >
   > > *"we want proton unless for an explicit reason (like comparison on
   > > proton vs muon results). otherwise pin proton"*
   > > *"fix all, even if not visible."*
   >
   > It is recorded **here** because the gate above asks for exactly that
   > and a chat transcript does not satisfy it. PR #5049 held the bulk
   > reclassification back on precisely this ground, and it was right to:
   > the branch could not show the directive, only infer it.
   >
   > **The authorisation is real, and it is not a blank cheque.** The first
   > attempt at this migration broke `main` for **208 producers**
   > (`qou-m9xp`), so it carries four constraints, each one bought:
   >
   > 1. **NEVER re-pin an anchor-DEFINING witness.**
   >    `q-pinning-50-digit.witness.json` is what
   >    `qou_substrate.witness._q0_value_for_anchor("muon")` READS. Re-pinning
   >    it does not migrate a consumer — it redefines what "muon" *means*, so
   >    every muon-stamped witness in the corpus then disagrees with its own
   >    anchor (262 `Q0_FLIP`s) and `q_parameter`'s anti-corruption guard
   >    hard-fails every `ideal_muon` producer, including the one that would
   >    regenerate the anchor. `q0_repin_sweep.py` now excludes it by name
   >    (`ANCHOR_DEFINING` / `ANCHOR_DEFINITIONS`); do not remove that.
   > 2. **The muon anchor keeps its definition.** "Proton everywhere"
   >    governs what new compute *pins to*, not whether the muon layer still
   >    has a value. Something in the tree must continue to hold the muon
   >    50-digit string or the ideal/CAL-2 layer becomes unstatable.
   > 3. **A comparison producer needs BOTH pins and the manifest cannot
   >    serve it.** A per-process override supplies one. Such a producer
   >    reads `q_at()` / `q_muon_at()` by name and belongs under
   >    `physical_proton` — see `mu_substrate_tension_audit_100dps`, which
   >    understated its own subject **155×** while listed `ideal_muon`.
   > 4. **Do not split the change.** The manifest reclassification and the
   >    witnesses it re-pins are one change. #5049 merged the witnesses and
   >    held the manifest, and the half that landed is the half that broke
   >    `main`. Land them together or not at all.
   >
   > Scope: `qou-1c4y`. Rules 1–4 immediately below still apply to
   > everything the sweep does not cover.

   Concretely:

   > **Bean reference corrected 2026-08-15.** This paragraph previously
   > said the sweep is "tracked under bean `tnjb`". It is not, and the
   > mis-reference is worse than a typo: `tnjb` is *completed* and is
   > about a **dashboard** defect (`per-observable-100x-status.witness.json`
   > scoring the muon tautology as the m_μ prediction — see item 3 above,
   > where the `tnjb` citation is correct). An agent following this
   > paragraph to find the migration lands on a closed, unrelated bean and
   > can reasonably conclude the sweep has already run. The live tracker is
   > `qou-1c4y` (in-progress); its predecessor `z5vu` is completed.
   - **New / touched code: use proton.** Any probe, producer, or witness
     you write or modify defaults to the experimental pin. No sign-off
     needed — that is the standing directive.
   - **Untouched muon witnesses: leave them.** Do not mass-regenerate.
     They stay valid as recorded until the tracked migration runs.
   - **Never mix.** If you touch a producer that consumes a muon-built
     cache, move the *whole* quantity to proton rather than leaving one
     input on each layer (see the straddling hazard above).
   - **Say which pin you used.** Any new witness must record its q₀ so a
     later reader can tell which layer it belongs to without inferring it
     from a call site.


## CRITICAL: Protected Files — DO NOT MODIFY

The following files are **strictly off-limits** to all coding agents
(Claude, Copilot, etc.). Only the repo owner may edit them manually:

- `deploy/google-viewers.txt` — Google OAuth viewer whitelist
- `deploy/github-collaborators.txt` — GitHub OAuth collaborator whitelist
- `.github/CODEOWNERS` — File ownership rules

These files control authentication access to the folio deployment.
**Never** read, write, edit, or suggest changes to these files.
If asked to modify them, refuse and explain that only the repo owner
can change whitelist files manually.

## Skills

Skills are organized under `.claude/skills/`:

- **`local/`** — repo-specific skills (latex-validation, scientific-accuracy,
  readability-editing)
- **`<package-name>/`** — skills synced nightly from external packages defined
  in `skills-config.json` (mode `"sync"`)
- **Reference packages** — registered in `skills-config.json` with mode
  `"reference"`, fetched on demand via the `skill_fetch` MCP tool (not
  synced locally)

### Skill routing (quick reference)

When a user request arrives, route to the right skill(s):

| User request pattern | Primary skill(s) | Min role |
|---------------------|------------------|----------|
| "fill in / prove / remove sorry" | `local/formalizer` + `local/category-theory` | collaborator |
| "define / formalize / add structure" | `local/formalizer` + `local/lean-generation` | collaborator |
| "diagram / naturality / monoidal" | `local/category-theory` | collaborator |
| "extract / stub / from LaTeX" | `local/lean-generation` | collaborator |
| "review / check / audit Lean" | `local/lean-proof-review` | collaborator |
| "status / tracking / manifest" | `local/proof-status-tracking` | reader |
| "what next / priority / triage" | `local/proof-triage` | collaborator |
| "proof gap / missing step / unproved assertion / bridging lemma" | `local/proof-gap-audit` | reader |
| "audit proofs / review proofs / proof editor / coordinate proof review" | `local/proof-editor` | collaborator |
| "simplify exposition / revisit old proof / integrate new content" | `local/proof-exposition-review` | collaborator |
| "lean vs narrative / do they prove the same thing / equivalence audit" | `local/proof-narrative-lean-equivalence` | collaborator |
| "concise proof / tighten proof / cut verbose narrative / shorten human proof" | `local/proof-conciseness` | collaborator |
| "write / edit chapter text" | `local/scientific-accuracy` + `local/readability-editing` | reader (review) / collaborator (edit) |
| "fix lean build / lake build fails" | `local/lean-build-fix` | collaborator |
| "audit lean / completeness / coverage" | `local/lean-completeness-audit` | collaborator |
| "meat / typed sub-claims / holds:Prop placeholder / bulk-split / docstring enrichment" | `local/lean-substantive-pass` | collaborator |
| "simplify / streamline proofs" | `local/proof-simplifier` | collaborator |
| "validate LaTeX" | `local/latex-validation` | reader |
| "validate content objects" | `local/content-validation` | reader |
| "build content → LaTeX" | `local/content-validation` | reader |
| "add / edit content block" | `local/content-validation` + relevant skill | collaborator |
| "review / audit blocks" | `local/content-block-review` | collaborator |
| "glossary / terminology / naming" | `local/ontologist` + `local/content-validation` | collaborator |
| "witnessed value / drift / numerical literal / :val / hardcoded number / pin to witness" | `local/witnessed-values` + `local/content-validation` | collaborator |
| "audit compute / compute audit / what can be sped up / find slow scripts / where is sympy.simplify / LaurentQ wiring / BlockCache wiring" | `local/compute-audit` | collaborator |
| "production vs exploratory / empirical fit vs canonical / numerology vs derivation / CAL-4 / 13-driver menu / Rule 14 / which file is production / can I empirically fit this / what counts as canonical / shape-probing / where does this h^k come from" | `local/production-vs-exploratory-discipline` | reader |
| "audit ffi / ffi roundtrip / rust-python ping-pong / back-and-forth / 20% wall opportunity / find boundary-crossings in a loop / consolidate compute to rust" | `local/ffi-roundtrip-audit` | collaborator |
| "write new compute / port to Rust / before optimization / precision / 1 ppb / 1ppb / precision discipline / error / python / rust / py / optimize / optimise / memory / storage / speed / fast / symbolic / float / float64 / f64 / mpf / mpmath / mpfr / witness / BigRational vs sympy.Rational / what type to use / Python-Rust boundary / pyo3 / maturin / cargo / BigInt / orbit-sum identity / algebraic preflight / cross-check / tolerance / read before coding compute" | `local/compute-author` | collaborator |
| "audit math compute integration / is X wired in / where is prop:foo consumed / props not in compute / validate mass-table sweep" | `local/compute-integration-watcher` | collaborator |
| "coordinate / coordinate with PR / sibling PR / cherry-pick / cross-PR request" | `local/coordinate` | collaborator |
| "missing proof (narrative)" | `local/editor` §Proof workflow | collaborator |
| "missing proof (Lean)" | `local/formalizer` + `local/proof-triage` | collaborator |
| "test / unit test / coverage" | `local/test-engineer` | collaborator |
| "deploy / auth / OAuth / roles" | `local/deployment-auth` | owner |
| "import / arxiv / upload paper" | `local/paper-importer` | collaborator |
| "import + formalize" | `local/paper-importer` + `local/formalizer` | collaborator |
| "upload / scan / intake / process document" | `local/document-intake` | collaborator |
| "WHO / guideline / L1 / L2 / normative" | `local/document-intake` | collaborator |
| "library/ status / what's pending" | `local/document-intake` | collaborator |
| "is this paper relevant / triage the uploads / what can we use from X / which uploads aren't cited / source ledger" | `local/paper-relevance-triage` | collaborator |
| "critical path / trace dependencies" | `local/critical-path-analysis` | collaborator |
| "archimedean vs categorical / context audit" | `local/critical-path-analysis` | reader |
| "what assumptions does X need" | `local/critical-path-analysis` | reader |
| "separate categorical / split statement" | `local/critical-path-analysis` + `local/content-validation` | collaborator |
| "simulator / simulation / interactive viz" | `local/simulator` + `local/content-validation` | collaborator |
| "set up lean / install lean / lean not working" | `local/lean-environment-setup` | collaborator |
| "egress / 403 / blocked host / firewalled / can't download / data server unreachable / clone mirror" | `local/sandbox-egress` (route table: github clone, wheel-bundled data, env overrides) | reader |
| "generate docs / build docs / schema docs" | `local/docs-generation` | reader |
| "build paper / compile PDF / render HTML" | `local/docs-generation` | reader |
| "latex build cache / slow latex build / faster pdf / install tex / get a TeX engine / quick feature build / changed-chapter preview / why isn't the preamble or diagram cached" | `local/latex-build-cache` (findings: caches that failed + what works — install-tex, feature-build) | collaborator |
| "TypeDoc / type docs / dependency graph" | `local/docs-generation` | reader |
| "diff / changes / what changed / undo" | `local/diff` | reader |
| "watch / watch main / watch upstream / watch this PR / watch branch X / what's landing" | `local/watch` | reader |
| "watch proofs / proof watcher / proof integration / chase sorries / proof QA on incoming" | `local/proof-integration-watcher` | reader |
| "watch canonical / canonical watcher / chase numerology / canonical-derivation discipline" | `local/canonical-watcher` | reader |
| "watch wiring / compute integration watcher / is X wired in / mass-table sweep validation" | `local/compute-integration-watcher` | collaborator |
| "/integration-watch proof / canonical" | `local/integration-watch` (dispatcher) | reader |
| "/integration-watch compute / all (compute-wiring requires write access to scripts)" | `local/integration-watch` (dispatcher → compute-integration-watcher child) | collaborator |
| "/integration-audit xxx / invalidate sidecar entries / re-audit after checker fix / mark stale / repopulate" | `local/integration-audit` (sidecar maintenance — script-only) | collaborator |
| "watch shared mechanics / parent watcher / inherit-from" | `local/integration-watcher` (abstract parent of the 3 watcher children) | reader |
| "chapter complexity / reorder sections / backward edges / graph energy" | `local/chapter-complexity-review` | reader |
| "verify substrate / observations trace to U / substrate connectivity" | `local/verify-local-substrate` | reader |
| "dangling remarks / audit remarks / remark backing" | `local/remark-audit` | reader |
| "promote remark / add interprets / fix dangling" | `local/remark-audit` + `local/content-validation` | collaborator |
| "review / audit chapter or paper" | Tier 0 → Tier 1 (`peer-review`) → Tier 2 (`academic-paper-reviewer`) | reader (review) / collaborator (act) |
| "full review / devil's advocate" | `skill_fetch("academic-paper-reviewer")` (Tier 2) | collaborator |
| "publication readiness / final check" | All tiers: local + `peer-review` + `skill_fetch("academic-pipeline/integrity-verification")` | collaborator |
| "check claim / evidence quality" | `local/scientific-accuracy` → `sci-critical-thinking` → `skill_fetch("deep-research")` | reader |
| "fact-check / source verification" | `skill_fetch("deep-research")` (fact-check mode) | reader |
| "audit rendering / check rendering / rendering issues" | `local/rendering-auditor` | reader |
| "rendering QC / visual check / overfull hbox" | `local/rendering-auditor` | reader |
| "notation check / symbol audit / register compliance" | `local/rendering-auditor` (pass 2) + `local/ontologist` | reader |
| "fix rendering / rendering fix / quick fix" | `local/rendering-fixes` | reader |
| "check markdown render / GitHub view / proof markdown" | `local/markdown-render-check` | reader |
| "one voice / status leak / TODO in prose / strip emoji / scholarly voice" | `local/one-voice-audit` (sweep) + `local/one-voice-style-guide` (author voice profile) | collaborator |
| "watch one-voice / voice + AI slop + fit + framework + wall / QA reports per block / staleness map" | `local/one-voice-integration-watcher` | collaborator |
| "/integration-watch one-voice / voice" | `local/integration-watch` (dispatcher → one-voice-integration-watcher child) | collaborator |
| "similar propositions / consolidate props / corollary vs theorem / mergeable lemmas / exposition redundancy / special-case forest" | `local/proposition-consolidation-audit` | reader |
| "/integration-watch consolidation / dedupe" | `local/integration-watch` (dispatcher → proposition-consolidation-audit child) | reader |
| "q usage / q regime / fixed q_0 leak / Real.sqrt q without 0 < q / archimedean leak / |q| > 1 vs q > 1 / root of unity undeclared / chapter regime mismatch / q symbolic vs numerical / per-block q audit" | `local/q-usage-watcher` (per-block q-regime detector + chapter-mismatch flagger; emits sidecar entries under `q-usage-*` criteria) | reader |
| "/integration-watch q-usage / q" | `local/integration-watch` (dispatcher → q-usage-watcher child) | reader |
| "devils advocate / why is this wrong / what will reviewers argue / adversarial review / red team / referee objection / counterexample / break this proof / poke holes" | `local/devils-advocate-watcher` (per-block + Lean adversarial review; 4 lenses + adjudicator; emits `da-*` sidecars) | reader |
| "/integration-watch devils-advocate / da / adversarial" | `local/integration-watch` (dispatcher → devils-advocate-watcher child) | reader |
| "bold defined terms / tighten definition / no rambling / no preamble in defn / one definition per block / each thing its own definition / tight theorem/prop/lemma statement / no interpretation in a theorem-prop-lemma-conjecture / statement should be pure / interpretation should be a follow-on remark / graduate-level formal math book style / informal register / contractions / hype / rhetorical header / why-question header / consequence header / academic header register / no Why…? or Consequence. section headers / definition in the wrong block / misplaced definition / definition clarity / setup clarity audit" | `local/definition-clarity-audit` (defn+statement clarity scanner; 8 criteria — `clarity-defterm-bold` / `clarity-defn-single` / `clarity-defn-tight` / `clarity-stmt-tight` / `clarity-stmt-pure` (a theorem/prop/lemma/conjecture must carry only its claim; interpretation moves to a follow-on `remark`) / `clarity-grad-style` (graduate-level formal-math register) / `clarity-rhetorical-header` (section headers must be noun-phrase academic, not "Why…?"/"Consequence." rhetorical/colloquial) + inverse `clarity-defn-misplaced` (a non-`definition` block secretly carrying a definition); emits `clarity-*` sidecars) | reader |
| "QA report / .qa.json / multi-reviewer / hash staleness / per-block audit sidecar" | `folio-assistant/content/pipeline/qa-sweep.ts` + `qa-staleness.ts` (CLI), `folio-assistant/schemas/block-qa.ts` (schema) | collaborator |
| "session todos / work plan / what's left / track progress / beans" | `local/todo-manager` (session work-plan via the `beans` CLI) + `local/bean-coordination` | reader |
| "process feedback / review todos / triage open feedback" | `local/todo-review` (content-feedback triage) | reader |
| "prepare merge auto / auto merge / resolve and merge / ship it" | `local/prepare-merge-auto` (full autonomous merge pipeline: coordinate siblings → prepare-merge → resolve comments → merge) | collaborator |
| "socratic steering / steer vs gap / known-answer question / intuition seed / tenuous identification / coactive / α-informative / interaction registers" | `local/symbiotic-interaction` (three-register author-input protocol + arc-metrics spec) | reader |

### External skill packages

Skills come from three sources, forming a tiered escalation model:

| Tier | Source | Location | Mechanism |
|------|--------|----------|-----------|
| **0 — Local** | `.claude/skills/local/` | On disk (repo) | Always available, run on every content change |
| **1 — K-Dense** | `K-Dense-AI/claude-scientific-skills` | On disk (synced nightly) | Read `SKILL.md` from `.claude/skills/claude-scientific-skills/<skill>/` |
| **2 — Academic** | `Imbad0202/academic-research-skills` | Fetched on demand | Call `skill_fetch` MCP tool; cached for 30 min |

**Tier 1 skills** (synced, for general scientific QC): `peer-review`,
`scientific-writing`, `scientific-critical-thinking`, `citation-management`,
`literature-review`, `hypothesis-generation`, `scientific-brainstorming`,
`arxiv-database`.

**Tier 2 skills** (fetched, for deep academic review):
`academic-paper-reviewer` (7-agent multi-perspective review),
`deep-research` (13-agent evidence grading / fact-check),
`academic-pipeline` (integrity verification protocol).

See `editor.md §External Academic Review` for the full escalation protocol,
delegation flows, and review-mode mapping.

### Skill role assignments

Every skill has a `roles:` field in its YAML frontmatter listing which
user roles may invoke it. The three roles form a hierarchy:
`reader < collaborator < owner`. Each role inherits all lower-role skills.

| Role | Skills |
|------|--------|
| `reader` | editor, content-validation, latex-validation, scientific-accuracy, readability-editing, proof-status-tracking, proof-gap-audit, todo-review, docs-generation, diff, watch, chapter-complexity-review, verify-local-substrate, remark-audit, rendering-auditor, rendering-fixes, markdown-render-check, witnessed-values, proof-integration-watcher, canonical-watcher, detangler-integration-watcher, production-vs-exploratory-discipline, proposition-consolidation-audit, q-usage-watcher, symbiotic-interaction, devils-advocate-watcher, definition-clarity-audit |
| `collaborator` | All reader skills + formalizer, category-theory, lean-generation, lean-proof-review, lean-build-fix, lean-completeness-audit, lean-substantive-pass, proof-triage, proof-simplifier, proof-editor, proof-exposition-review, proof-narrative-lean-equivalence, proof-conciseness, chapter-analysis, content-block-review, ontologist, paper-importer, document-intake, paper-relevance-triage, test-engineer, lean-environment-setup, simulator, one-voice-audit, compute-audit, compute-author, coordinate, compute-integration-watcher, ffi-roundtrip-audit |
| `owner` | All collaborator skills + deployment-auth |

When a user connects via **Folio Assist** (chat), they default to `reader`
unless authenticated via GitHub OAuth (which grants `collaborator` or `owner`).
Agents coordinating sub-skills **must** check the user's role against each
skill's `roles:` list before routing.

**Decision tree**: (1) Check the user's role — only route to skills they
can access. (2) Does it touch content objects (`.ts` + `.md`)? →
`local/content-validation` + relevant content skill. (3) Does it touch `.tex`?
→ LaTeX skills. (4) Does it touch `.lean`? → Lean skills above. (5) Both
content + Lean? → also `local/lean-generation` for cross-refs. (6) Ambiguous?
→ read the skill `.md` files, then ask the user.

See **§12 Using Skills for Content Changes** in
`.github/copilot-instructions.md` for the full authoritative mapping,
including the detailed decision tree and Lean-specific routing table.

### Coding conventions

Follow the detailed rules in `.github/copilot-instructions.md` — they govern
LaTeX structure, labeling, cross-references, prose style, notation, and skill
usage for content changes.

### LP / SDP duals — first-class infra (do not skip)

Per `prop:operator-selection-lp` § *dual program*, every operator-
selection / shadow-price / knot-operator-selection compute MUST
emit BOTH primal and dual variables in its witness JSON:

| field | meaning |
|-------|---------|
| `y0_star` | shadow price of the net constraint |
| `y_star` | shadow prices of Frobenius positivity constraints (≥ 0) |
| `active_set` (or `active_constraints` / `active_channels`) | indices `i` with `y_star[i] > 0` |
| `primal_obj` | $\sum_i t_i x_i^*$ |
| `dual_obj` | $n_{\text{target}} \cdot y_0^*$ (= primal_obj by strong duality) |
| `duality_gap` | $|\text{primal\_obj} - \text{dual\_obj}|$ |

**Canonical entry point**:
[`computations/lp_dual_solver.py`](computations/lp_dual_solver.py)
exposes `solve_operator_selection_lp(t, G, n_target)` and
`solve_psd_operator_selection_sdp(t, G, n_target)`. Both return
a result whose `.to_dict()` contains all required fields.

**CI enforcement**:
[`computations/lp_dual_witness_validator.py`](computations/lp_dual_witness_validator.py)
runs in `witness-pipeline.yml` (warn-only by default; `--strict`
fails CI). Scans every `*.witness.json` whose name or
`description`/`computation` field signals an LP/SDP/operator-
selection compute and verifies the dual fields are present.

**Why this matters**: the dual variables ARE the binding-energy
shadow prices. The active demand channels (`y_star[i] > 0`) are
the "most receptive sub-braids" — they identify which Wedderburn
blocks the bound state actually saturates. Solving only the
primal loses this structural information, which has been the
historical pattern (58 of 58 LP/SDP witnesses on `main` lacked
the dual at the time this rule was added). Do not repeat this
pattern.

**Current baseline.** Run
[`lp_dual_witness_validator.py`](computations/lp_dual_witness_validator.py)
for the live count of missing-dual witnesses — do not cite a dated
baseline from AGENTS.md, as new LP/SDP witnesses land regularly.
The validator's narrowed hint list (`lp-dual` /
`operator-selection-lp` / `shadow-price` / `primal-dual` /
`lp-duality`) skips symbolic feasibility certificates and
knot-particle probes that do not compute LP duals.

**Fix per offender**: route the LP/SDP solve through
`solve_operator_selection_lp()` or
`solve_psd_operator_selection_sdp()`; the result's `.to_dict()`
carries every required field.

## Writing `.lean` proofs — rules for agents

These rules apply whenever an agent creates or modifies a `.lean` file.
Agents **must** follow all of them; violations will be caught by the
`content-block-review` skill.

### 0. Standardized root Lake workspace

The repo uses a **single root Lake workspace** (`/lakefile.toml`,
`/lean-toolchain`).  Each paper is a Lake **package** declared by
`[[require]]` with a short-form name:

| Package | Paper directory | Library module |
|---------|-----------------|----------------|
| `qou` | `content/quantum-observable-universe/lean/` | `QOU` |
| `ugb` | `content/unital-groebner-bases/lean/` | `UGB` |
| `fred2005` | `content/fred2005-formal-groups/lean/` | `Fred2005` |

**Preferred build commands** (always run from repo root):

```bash
lake build QOU UGB Fred2005   # build every paper package
lake build QOU                # single paper library
lake exe cache get            # fetch Mathlib cache for the workspace
```

**Name the targets.** A bare `lake build` at the root is a **no-op**: it exits 0
with "Build completed successfully (0 jobs)" having examined nothing. The root
package aggregates the three paper packages and declares no library of its own,
so its default target set is empty; `defaultTargets` cannot reference another
package's target, and a root aggregator module would under-build because each
paper's library is glob-declared (`globs = ["QOU", "QOU.+"]`) and a glob library
is built only by naming the library target. The root `lakefile.toml` carries the
same note.

Per-paper `cd content/<paper>/lean && lake build` still works, but
root-workspace commands are the standardized entry point used by CI
(`lean_ci.yml`, `blueprint.yml`) and the MCP server (`lean_build`).

> **🟦 Agents building Lean in a sandbox — RESTORE → build → SEED (don't
> rebuild Mathlib from scratch).** The toolchain is often already installed
> (`export PATH="$HOME/.elan/bin:$PATH"`; `lake build -R <Module>` builds a
> single module's dep cone from source — github clones work; only the
> release server + `lake exe cache get` are network-blocked, both
> sidesteppable). Cross-container preservation lives on orphan branches
> `lake-cache/<pkg>-<toolchain-slug>` (e.g. `lake-cache/qou-v4-24-0`):
> **fetch-and-extract to restore (~2 min) instead of recompiling (~30 min+),
> and SEED the branch after a successful build** so the next agent restores.
> **Caveat — the seed ROUTE depends on how you built.** `lake build` output
> seeds the monolithic branch via `lean-olean-cache-seed.sh`. A `lean`-direct
> build (`lean f.lean -o …`, which the verification guidance below tells you to
> prefer) writes no `.trace`, so that script's guard correctly **refuses** it —
> never force it past, since Lake treats untraced oleans as stale, rebuilds and
> evicts them (bean `02kc`). Preserve lean-direct output as an **addon** orphan
> branch via plain `tar` instead (e.g.
> `lake-cache/qou-v4-24-0-h4-wedderburn-cone`); restored with `tar xzf`, not by
> Lake, it is exactly what a `lean`-direct + `LEAN_PATH` consumer needs. See the
> skill's §"Rule for agents going forward" for the route table.
> Full proven recipe + restore/seed commands:
> [`.claude/skills/local/lean-environment-setup.md` §"PROVEN sandbox build
> recipe" + §"PRESERVE THE BUILD"](.claude/skills/local/lean-environment-setup.md).
> Strategy: [`docs/workplans/2026-05-24-lean-cache-strategy.md`](docs/workplans/2026-05-24-lean-cache-strategy.md).

### 0a. Content-block `lean.ref` is a package-qualified URI

Every `lean:` field on a content block uses a package-qualified URI
of the form `"<package>:<Decl.Path>"`:

```ts
// definition in the qou package
lean: { ref: "qou:QOU.Torsion.lifting_exists" }

// cross-paper reference (ugb package)
lean: { ref: "ugb:UGB.GrobnerShirshov.Basis" }
```

- **Package prefix** must be one of `qou`, `ugb`, `fred2005` — see
  `folio-assistant/schemas/lean-packages.ts` for the registry and
  `parseLeanRef()` helper.
- The legacy `decl:` / `file:` shape is **removed**.  Validation fails
  on blocks that still use it.
- The pipeline resolves a `.lean` source file by: (1) sibling
  `<rootName>.lean`, (2) `<lakeRoot>/<Decl/Path>.lean` under the
  package's Lake root, (3) grep fallback on current branch.

> **🚫 No shadowing stubs (STRICT, 2026-06-14).** Because resolution checks
> the **sibling first**, a trivial `theorem foo : True := trivial`
> content-block sibling **shadows** the real library declaration the
> `lean.ref` would otherwise resolve to (candidate 2). NEVER create or keep
> such a stub when the real formalisation exists in the library tree:
> - If the decl lives at `<lakeRoot>/<Decl/Path>.lean` (candidate 2),
>   **do not** add a sibling `.lean` — let the ref resolve to the library decl.
> - If the decl lives in a **mis-named** library file (decl-name ≠ file-name),
>   **align** it (rename the file / move the decl so candidate 2 resolves) —
>   do not paper over it with a stub.
> - A sibling `.lean` is legitimate ONLY when it carries the **real**
>   formalisation (not `: True`), for a `definition` block (sibling required),
>   or as a genuine placeholder where no library formalisation exists yet — and
>   then it must be honest (state the real proposition with `sorry` + `-- Ref:`,
>   or be a `conjecture`), never `: True := trivial` and never a
>   `: True ∧ True := ⟨…⟩` self-assuming projection.
>
> Audit + drain: [`lean-proof-vacuity-audit`](.claude/skills/local/lean-proof-vacuity-audit.md)
> + [`docs/audits/2026-06-14-lean-vacuous-proof-audit.md`](docs/audits/2026-06-14-lean-vacuous-proof-audit.md).

To register a **new paper** as a Lake package: add a `[[require]]`
stanza to the root `lakefile.toml`, append to `LEAN_PACKAGES` in
`lean-packages.ts`, and add the library name to `defaultTargets`.

### 0b. Rebasing across the `lean.ref` migration — instructions for agents

If you are an agent working on an older branch and you **rebase or
merge onto a commit that contains this standardization**, your
content blocks may still use the legacy `lean: { decl: "...", file? }`
shape.  Zod validation will fail with a message pointing at this
procedure.  **Run the migration, do not hand-edit each block** (it runs in
the external `litlfred/folio-assistant` pipeline / CI — see the currency
note below; the qou `bun run` aliases were pruned by miga):

```text
# CONCEPTUAL — runs in the folio-assistant pipeline / CI, NOT inside qou.
# miga pruned the qou aliases; invoke from a litlfred/folio-assistant
# checkout per that repo's docs (exact cwd/alias is defined there):
migrate-lean-refs        # apply (writes content blocks in place)
migrate-lean-refs --dry  # preview only (no writes)
```

The script (`migrate-lean-refs.ts`, relocated to the folio-assistant pipeline by miga)
is **idempotent** — safe to re-run after any rebase, merge, or
cherry-pick.  It rewrites every `lean: { decl: "<Decl>", file? }`
into `lean: { ref: "<pkg>:<Decl>" }` using the paper directory to
choose the Lake package prefix (see `LEAN_PACKAGES` in
`folio-assistant/schemas/lean-packages.ts`).

After the migration, re-run `bun run scripts/run-validate.ts content/<paper>`
to confirm the schema is clean before continuing your task.  **Do not add
`decl` back** to unblock a merge — that field was removed from the schema on
purpose.

> **Currency note (miga, 2026-06-23).** The content pipeline + schemas now live
> in the separate `litlfred/folio-assistant` repo, wired into this checkout by
> [`scripts/setup-folio-assistant.sh`](scripts/setup-folio-assistant.sh) (clones
> the platform as a sibling + symlinks `folio-assistant/`). Run it **once** before
> any validate / pipeline command. The former `package.json` shortcuts
> (`bun run validate`, `migrate-lean-refs`, `validate-refs`, `export-bibtex`) were
> dropped in the migration; only `scripts/run-validate.ts` has a standalone
> replacement so far — the others await re-wiring (track under the `miga` epic).
> The lean.ref migration above is corpus-complete (0 legacy `decl:` shapes
> remain), so it is now historical.

If new `.lean` files were added on your branch, their content-block
`lean.ref` URIs must use the correct `<package>:` prefix for the
paper they live under.  Agents authoring new blocks should always
consult `LEAN_PACKAGES` for the list of valid prefixes.

### 1. Every `sorry` requires a bibliographic citation

```lean
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
sorry
```

- The `[key]` must match an entry in `content/schema/references.ts` exactly (case-sensitive).
  (`references.bib` is auto-generated from `references.ts` — the `export-bibtex`
  shortcut was dropped in the miga migration, pending re-wiring).
- If no published reference exists, use `[manuscript]` and cite chapter/section.
- A `sorry` without `-- Ref:` is always a review failure.

### 1a. No audit-dodging / sorry-workarounds (STRICT, 2026-06-23)

The vacuity / sorry / axiom audits exist to surface unproved or
content-free declarations **honestly**. Agents **must not** disguise
such a declaration to slip it past a checker. Forbidden workarounds
include:

- **`theorem X : True := trivial` → `def X : True := trivial`.** Every
  vacuity detector keyed on the provable kinds
  (`theorem`/`lemma`/`proposition`/`corollary`/`example`); re-declaring
  the same vacuous body as a `def` (or `abbrev`/`instance`) hid it from
  the entire audit. Now caught as `def-disguised-true`
  ([`content/pipeline/lean-vacuity-axiom-audit.ts`](content/pipeline/lean-vacuity-axiom-audit.ts)).
- **Concluding `: True`** (or `: X = X := rfl`, or any tautology) in
  place of the real proposition.
- **`native_decide`** to mask a goal behind the kernel evaluator.
- Any equivalent move whose *only* effect is to make an audit pass
  without making the proof any less vacuous.

**Honest dispositions** (the only acceptable outcomes) — per the
self-assuming disposition rubric (PR #2477) and §3b:

1. **Prove it** — state the real proposition and discharge it.
2. **Queue it** — state the *real* proposition with `sorry` + a
   `-- Ref:` citation. The derived `has_sorry` status is the honest
   "stated, not yet proved" marker (§4); never an uncited `sorry`.
3. **Demote it** — make it a `conjecture` (kind `conjecture`, or the
   §3b class-axiomatisation `class C : Prop where …`). The vacuity
   audit's **"except conjectures"** carve-out recognises a `def : True`
   inside a `conjecture` content block, and shadow-stubs whose real
   formalisation lives elsewhere.

A `def : True := trivial` that is neither a shadow-stub nor a
conjecture-block placeholder is a **review failure**.

### 2. Naming convention: LaTeX label → Lean declaration

| LaTeX label | Lean declaration | Rule |
|---|---|---|
| `thm:lifting-exists` | `QOU.Torsion.lifting_exists` | Hyphens → underscores |
| `def:quantum-connection` | `QOU.QuantumObservableUniverse.quantum_connection` | Namespace = chapter module |
| `def:categorical-instanton` | `CategoricalInstanton` | Type-level structures use CamelCase |
| `prop:categorical-dq-squared` | `categorical_dq_squared` | Theorems/lemmas use snake_case |

All declarations live under the `QOU` root namespace.

### 3. Block kind determines Lean requirements

The authoritative `kind → Lean requirement + label prefix` mapping
is the **Type system** table in `## Content-object architecture`
(below). Summary: `definition` requires a sibling `.lean` (enforced);
`theorem`/`lemma`/`proposition`/`corollary` are expected and warn if
missing; `conjecture` may carry `sorry` (see §3b for the propagation
rule); other kinds have no Lean requirement.

### 3b. Conjectural propagation and Lean formalization of conjectures

**Conjectural propagation rule (STRICT, with conditional-class
exception per §3b-cond below):** A statement that depends on (is
downstream of) a conjecture **cannot** be a `theorem`,
`proposition`, `lemma`, or `corollary` *unless* it satisfies the
conditional-class exception (§3b-cond). Only statements proved
from established results (definitions, previously proved theorems,
axioms) — or proved from explicit conditional hypotheses — may
use provable block kinds.

- If `uses[]` contains a `conj:` label (directly or transitively),
  the block **must** be either:
  - kind `conjecture`, or
  - a provable kind satisfying the **conditional-class exception**
    (§3b-cond) — i.e. the conjecture is axiomatised as a Lean
    class and the downstream block's Lean statement carries that
    class as an explicit `[Instance]` hypothesis.
- "Proof" blocks downstream of conjectures (without conditional-
  class) become `remark` blocks with `interprets: "conj:..."`
  (proof *sketches*, not proofs).
- `remark` blocks may freely interpret conjectures (they make no
  logical claims).

#### §3b-cond — Conditional-class exception (Option B, 2026-05-02)

A `theorem`/`proposition`/`lemma`/`corollary` block whose `uses[]`
cone transitively touches a `conj:C` may keep its provable kind
**iff all of**:

1. **Class axiomatisation.** `conj:C` has a Lean
   `class C` declaration in its `.lean` file, with class fields
   encoding the conjecture's content. The class instance is
   the only `sorry` in the entire downstream chain.
2. **Explicit hypothesis on Lean side.** The downstream block's
   Lean declaration has the class as an explicit `[Instance]`
   hypothesis. Example:
   ```lean
   theorem downstream_result {M : Type*} [C M] : … := by
     -- proof uses C.field1, C.field2 as hypotheses; otherwise
     -- fully verified by Lean.
   ```
3. **Explicit conditional banner on narrative side.** The `.md`
   block opens with: **Theorem (conditional on
   [`conj:C`](path/to/C.md)).** The body cites the conjectural
   hypothesis where used.
4. **`uses[]` includes the conjecture explicitly.** The
   conditional dependency is auditable from the manifest.
5. **Non-degenerate — the class axiomatises *hypotheses*, not the
   conclusion.** The class fields must encode the conjecture's
   *inputs*; the theorem must **derive** its conclusion from them. A
   class that carries the block's own conclusion as a field, with a
   "theorem" that merely projects it (`:= ctx.claim_foo`), is a vacuous
   self-assuming projection — it satisfies the propagation audit (the
   cone *is* class-axiomatised) yet **fails `proof-statement-integrity`**
   (the Lean does not *derive* the `.md` claim). Restructure so the
   class carries the genuine sub-hypotheses / proof-chain steps and the
   theorem composes them (e.g. carry the two directions of an iff as
   hypotheses, derive it by `Iff.intro`). Verified exemplar:
   [`QOU/FluidDynamics/q_bkm_criterion.lean`](content/quantum-observable-universe/lean/QOU/FluidDynamics/q_bkm_criterion.lean).

When all five hold, the block represents a *rigorous conditional
result* — fully verified by Lean modulo a single, named,
class-axiomatised conjectural input. This pattern preserves the
distinction between rigorous-conditional and unproved-conjecture
content.

**Base ring (§7c) for conditional-class fixes.** Keep the class and
theorem over a generic `{R : Type*} [CommRing R]` — never `ℝ` unless an
archimedean construct (ordering `0 < q`, `Real.sqrt`, `Real.log`, …) is
genuinely required, and place that specialisation *after* the
substrate→archimedean wall. In particular do **not** import a chapter
`Shared` module that transitively pulls in `Mathlib.Data.Real.Basic`
(e.g. `QOU.Shared.SobolevHkRegularity`) when `Mathlib.Algebra.Ring.Defs`
suffices. Archimedean setup hypotheses that the statement does not use
(e.g. `0 < T`, `1 < q`) are **dropped** from the generic class, not
coerced into `ℝ`. Verify per-module with `lake build -R <Module>` (the
whole-library `lake build QOU` is red on pre-existing failures and is not
the gate).

**Audit treatment.** The `conjectural-propagation` audit
(`folio-assistant/content/pipeline/conjectural-propagation-audit.ts`) reports such
blocks separately as **conditional-on-class** rather than as
violations. To opt a block into this status, ensure its Lean
declaration contains a class hypothesis matching one of the
conjectures in its transitive `uses[]` cone, and confirm the
narrative banner. The audit script will detect the pattern and
classify the block accordingly.

**Definitions and conjectures (clarification):** The propagation
rule above applies to **provable claims** (`theorem`, `proposition`,
`lemma`, `corollary`). It does **not** force `definition` blocks to
become conjectures even if their `uses[]` includes a `conj:` label.
A definition names a construction; whether the named construction
is "the right one" may itself be a conjecture, but the act of naming
is not a logical claim.

However:

- A `definition` whose well-formedness genuinely depends on a
  conjecture (e.g. defining "the unique X with property P" when P's
  uniqueness is conjectural) **should** carry an explicit narrative
  note in its `.md` flagging the conjectural backing, and should
  cite any computational witnesses available
  (`computations/*.witness.json`) so empirical
  support is discoverable from the manifest.
- Any `theorem`/`proposition`/`lemma`/`corollary` whose `uses[]`
  cites such a definition **does** trigger propagation — it is
  downstream of the conjecture transitively. Track the chain via the
  definition.

Audit note: the `proof-gap-audit` skill must apply §I of its
checklist (conjectural propagation) only to provable kinds. Flagging
a definition as a propagation violation is a false positive (we have
seen this hallucinated by sub-agents). Compute the transitive cone
from any provable block; if it touches a `conj:` via any path
(including through definitions), demote the provable block.

**Lean formalization of conjectures:** Conjectures *can* (and should,
when feasible) have `.lean` files.  The convention is:

1. **The conjecture itself** is axiomatized as a Lean `class` with
   fields encoding its content.  The `sorry` in any instance is
   understood as **conjecture**, not missing proof.

2. **Downstream conjectures** (conditional on the upstream conjecture)
   take the upstream class as a `[instance]` hypothesis and prove
   the conditional result: "if the conjecture holds, then..."
   These downstream proofs are **fully verified** by Lean — the
   only unproved input is the class instance itself.

3. **The dependency chain** is visible in Lean: definitions →
   conjecture (axiom class) → downstream conjectures (conditional
   theorems).

Example pattern:
```lean
-- The conjecture (sorry = conjecture)
class MyConjecture (M : Type*) where
  functor : FooData M → BarData M
  compatibility : ∀ x, ...

-- Downstream conjecture: proved conditional on MyConjecture
theorem downstream_result {M : Type*} [MyConjecture M]
    (x : FooData M) : ... :=
  MyConjecture.compatibility x
```

#### §3b-tax — Primary vs dependent conjectures (taxonomy, derived)

Every conjecture carrier is exactly one of two kinds. **The kind is
*derived* from the Lean type — not hand-tagged** — because the
dependency is already encoded in the signature's binders:

- **Primary conjecture** — an open problem that is *not* downstream of
  another conjecture (a *root*): its signature takes **no** other
  conjecture class as a hypothesis.
- **Dependent conjecture** — a statement that holds *if* a primary (or
  another dependent) conjecture holds. It is stated conditionally — "if
  the primary conjecture is true, then …" — by taking the primary's
  class as an explicit `[Instance]` hypothesis (the §3b-cond pattern).
  That `[Instance]` binder **is** the dependency edge.

Because the edge lives in the type, `lean-vacuity-axiom-audit.ts`
computes the primary/dependent split as a graph over instance binders
(`classifyConjectures`) and records it in the audit witness
(`conjecture_graph`). **You do not annotate primary-vs-dependent** — the
compiler already knows it. (An optional `-- @conjecture: primary`
comment may be added for human readers; it is documentation only and is
not required or enforced.)

A dependent conjecture written as a *flat, unconditional* assertion is
**wrong**: it silently smuggles the primary conjecture in as if it were
established. Always thread the dependency through the type:

```lean
class PrimaryConj (M : Type*) : Prop where
  content : ∀ x : Real, 0 < x → ∃ y : Real, 0 ≤ y ∧ y ≤ x   -- real content, not `True`

-- WRONG — stated unconditionally, hides its dependence on PrimaryConj
-- (the audit classifies it as primary because nothing in the type says
--  otherwise — the dependency is lost):
class DependentBad (M : Type*) : Prop where
  consequence : ...

-- RIGHT — conditional on the primary (`if PrimaryConj then …`); the
-- `[PrimaryConj M]` binder is the derived dependency edge:
class DependentGood (M : Type*) [PrimaryConj M] : Prop where
  consequence : ...
```

**The carrier must assert something.** A conjecture axiomatised as an
**empty** marker `class C : Prop` (no fields) asserts *nothing* — any
`instance : C := ⟨⟩` discharges it, so a downstream `[C]`-conditional
"theorem" proves nothing modulo `C`. Likewise a `structure`/`class`
whose docstring *promises* defining properties (positivity,
archimedean smallness, …) while encoding only a weak `≠`
non-triviality under-delivers on its own prose. Class fields must carry
the conjecture's **content** — a parameter-quantified inequality in the
*shape* of the claim (the Round-11 pattern in
[`ConditionalClasses.lean`](content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean)),
never a bare `True` or an empty body. An unproved primary is honestly
represented by a **content-bearing class with no instance** (the open
state); do not fabricate a trivial instance to "close" it.

**Enforcement.** `content/pipeline/lean-vacuity-axiom-audit.ts` adds
four conjecture-discipline criteria (high-recall candidates,
agent-confirmed like the other vacuity classes). These close the gap
that the proof-anti-pattern detectors structurally miss — an empty or
under-specified carrier has no proof term, no `sorry`, and no `axiom`
to flag, yet asserts nothing:

| Criterion | Severity | Fires on |
|---|---|---|
| `proof-no-empty-prop-carrier` | critical | a `class`/`structure : Prop` with **zero fields** (and no `extends`); opt out a genuine opaque tag with `@marker` |
| `proof-claims-unencoded` | major | a carrier whose docstring **enumerates ≥2 named properties** that are not encoded as Prop fields; **or** (pattern `true-class-field`) a single field typed literally `: True` carrying no content — opt out a genuinely-open opaque field with `@marker` / `opaque marker` |
| `proof-dependent-conjecture-not-conditional` | critical | a carrier whose doc **explicitly claims conditionality** ("conditional on / assuming / given conj:Y") while its signature binds **no** such class — the prose says conditional, the type does not (derived, intent-vs-type mismatch) |

The high-recall trivial-true detector also annotates a `placeholder-true` /
`def-disguised-true` whose docstring carries **theorem-assertion language**
(`**Theorem**`/`**Lemma**`/`**Proposition**`) and is not a conjecture carrier —
*"docstring asserts a provable claim while the Lean concludes `True`"* — the
`q_gl_obstruction_calc` failure mode (a real claim hidden behind a tautology),
which a heuristic-only triage repeatedly mis-called "legit".

**Agent inspection is mandatory, not optional (the ledger).** These criteria are
high-recall *candidates*; the legit-vs-genuine verdict is an **agent** call.
Standalone library `.lean` files have no `<block>.qa.json` sidecar to hold that
verdict, so it lives in a committed **review ledger**
([`docs/audits/lean-vacuity-review-ledger.json`](docs/audits/lean-vacuity-review-ledger.json),
schema `lean-vacuity-review/v1`): `--review-ledger` seeds new / file-changed
candidates as `needs-agent`; `--check-ledger` exits 1 unless every non-exempt
candidate carries a **fresh** agent verdict (`genuine` / `legit` / `advisory`)
whose recorded `.lean` sha still matches. A verdict goes stale the moment the
file changes — the machine can flag, only an agent can clear. Workflow +
discipline: [`lean-proof-vacuity-audit.md` §Agent-inspection ledger](.claude/skills/local/lean-proof-vacuity-audit.md).

The primary/dependent split itself is **not a criterion** — it is the
derived `conjecture_graph` in the witness (primary count, dependent
edges). There is nothing to "drain": classification is recomputed from
the Lean each run.

Worked exemplar (the bug that motivated these checks):
[`ReebEpsilon.lean`](content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/ReebEpsilon.lean)
— `ArchimedeanInfinitesimal` was an empty marker `: Prop` that passed
every existing check; it is now a content-bearing primary-conjecture
class alongside `ReebPositive`, each classified `@conjecture: primary`.

### 3a. Remark authoring convention — no dangling remarks

Every `remark` block must have **formal backing**. The correct
authoring structure is:

```
definition / proposition / lemma / theorem   (.lean: formal statement)
  └→ proof block                             (.lean: formal proof)
       └→ remark block                       (.md: interpretation)
            └→ example / simulator           (concrete instances)
```

**Rules:**

1. **Interpretive remarks** must set `interprets: "prop:foo"` (or
   `"def:foo"`, `"thm:foo"`, etc.) linking to the provable block
   they interpret. The `.md` content provides physical interpretation,
   motivation, or examples — not new mathematical claims.

2. **Glossary remarks** (Ch 8 only) are exempt — they wrap Mathlib
   types and carry the `"glossary"` tag.

3. **Prose blocks** (`prose`) are for pure exposition with no logical
   content (intros, abstracts, transitions). Use `prose`, not `remark`,
   when there is no provable statement behind the text.

4. A remark that makes a **mathematical claim** without `interprets`
   is a **dangling remark**. Resolve by:
   - **Promoting** the claim to `proposition` / `lemma` (with Lean)
   - **Linking** via `interprets` to an existing provable block
   - **Demoting** to `prose` if there is no logical content

5. **Ambiguous physics terms** (energy, force, particle, degeneration,
   etc.) in remark `.md` files must reference the corresponding
   categorical definition via `uses[]`. Physics terms without
   categorical backing are flagged by the `remark-audit` skill.

**Audit tool:** `cd content && bun run pipeline/find-dangling-remarks.ts`

**Constraint rules:** `remark-interprets` (warns on missing
`interprets`), `interprets-resolve` (errors on broken reference).

### 4. Formalization status is derived, not stored

Formalization status (`not_started`, `stated`, `has_sorry`, `proved`,
`mathlib_ok`) is **not stored in `.ts` manifests**. It is derived at
build time by CI scripts from `.lean` file content and Lean build output,
then written to `proof-objects.json`. Agents must **never** add a `status`
field to content block `.ts` files.

### 4a. TodoItem lifecycle rules

Content TODOs are **external to paper content**. They live in `todos/`
(gitignored — survives branch switches), referencing content blocks via
`targetLabel`. This keeps the paper source clean and avoids confusion
between scholarly content and work-tracking metadata.

```
todos/                           ← gitignored
  content-todos.ts               ← content-related todos
  infra-todos.ts                 ← infrastructure todos (optional)
```

The `TodoItem` type is defined in `content/schema/types.ts` for reuse,
but no `todos` field exists on any content block type or schema.

The MCP server serves todos at `/api/todos` (JSON) and `/todos` (HTML
dashboard). The `check-todos.sh` SessionStart hook summarizes open
items at the start of each session.

| Action | Who may do it |
|--------|--------------|
| **Create** a TodoItem | Agent or human |
| **Update** status to `in_progress` | Agent or human |
| **Resolve / close** a TodoItem (`resolved`, `wontfix`) | **Human only** |
| **Remove** a TodoItem from the array | **Human only** |

Agents **must never** set a TodoItem's status to `resolved` or `wontfix`,
and **must never** delete a TodoItem. The author verifies completion —
even after a commit has been made — and closes the item themselves.
Agents may add new TodoItems and may move items to `in_progress`, but
closing is always a human action.

### 4b. Glossary block policy (Chapter 8)

Chapter 8 ("Glossary of Rigid Monoidal Terms") contains **glossary
blocks** — `remark` blocks with tag `"glossary"` — that map paper
terminology to canonical Mathlib declarations. These are light
terminological wrappers: **no semantic novelty**, just naming
conventions.

| Criterion | Glossary block | Definition block |
|-----------|---------------|-----------------|
| Semantic novelty | None (Mathlib synonym) | New mathematics |
| Block kind | `remark` | `definition` |
| Label pattern | `rem:glossary-<term>` | `def:<term>` |
| Lean file | Not required | **Required** |
| Chapter | Ch 8 | Relevant content chapter |

**Decision rule**: If the paper uses a term that is a synonym for (or
lightweight wrapper around) a Mathlib type, add a glossary block. If
the paper introduces genuinely new axioms/structure, add a definition.

### 4c. Glossary terms — `\defterm` / `\refterm` (every occurrence wrapped)

Every term registered in any block's `defines: [...]` field **must** be
wrapped at every occurrence — `\defterm` once at the canonical site,
`\refterm` everywhere else. Plain text and `\emph{}` are no longer
permitted for defined terms. See
`.github/copilot-instructions.md §11.0` for the full contract.

- **Markdown** (`.md`): use the `remark-directive` syntax
  `:defterm[Visible]{#slug}` / `:refterm[Visible]{#slug}` — short
  forms `:defterm[term]` / `:refterm[term]` use the bracket text as
  both label and slug.
- **LaTeX**: use `\defterm{slug}[{Visible}]` / `\refterm{slug}[{Visible}]`.
- **Validation**: `bun run scripts/run-validate.ts content/<paper>` enforces five rules
  (`defterm-declared`, `defterm-marked`, `refterm-resolves`,
  `defterm-unique`, plus opt-in `term-mention-coverage` via `--strict`).
  Run with `--strict` once the chapter has been backfilled.
- **Codemod**: `bun run pipeline/codemod-refterm.ts <chapter-dir>`
  (dry-run by default) wraps bare-text mentions of known glossary
  slugs in `:refterm[…]{#slug}`. Mdast-based, idempotent. Pass
  `--write` to apply.
- **Glossary build**: `bun run pipeline/build-glossary.ts <paper>`
  emits `glossary.json` (committed) + `chapters/glossary.tex`
  (gitignored). `--check` mode is the CI gate.

### 4d. Author notes vs. scholarly prose — `authorNotes` field (STRICT)

> **Implementation tracking note.** The `authorNotes` schema field,
> the `WITH_AUTHOR_NOTES=1` render flag, and the `one-voice-audit`
> Category H "Banner-in-prose" rule described below are introduced
> by **PR #1098** (banner-to-authorNotes migration). This §4d
> document landed via PR #1105 alongside it. If the referenced infra
> isn't yet on `main` (e.g., `AuthorNote` interface missing from
> `folio-assistant/schemas/types.ts`), wait for PR #1098 to merge
> before authoring against this convention. Once both PRs are on
> main, this note can be removed in a follow-up.

Author-tracking notes (status, caveats, refined-framing comments,
deprecation pointers) belong in the **`authorNotes`** metadata field
on the block's `.ts` manifest — NOT in the scholarly prose of the
`.md`. Per AGENTS.md "User accessibility" + `local/one-voice-audit`
Category H ("Banner-in-prose"): status leaks in prose are a one-voice
violation.

Schema (in `folio-assistant/schemas/types.ts`):

```ts
export interface AuthorNote {
  kind: "status" | "caveat" | "note" | "refined-framing" | "deprecated";
  date?: string;  // ISO YYYY-MM-DD recommended
  body: string;   // markdown, treated as block prose
  see?: string;   // optional link to follow-up
}
```

`BlockBase.authorNotes?: AuthorNote[]` — every block kind accepts it
(builders pass through via `Omit<XBlock, "kind">`).

**Render behavior**: SKIPPED by default in the LaTeX render
(clean publication voice). Set environment variable
`WITH_AUTHOR_NOTES=1` to include them as a small
`\begin{quote}\small\textit{Author notes (working draft):}...\end{quote}`
appendix at the end of each block. Useful for working drafts.

**When to migrate vs. keep in prose**:

| In prose looks like | Action |
|---------------------|--------|
| `> **Status: theorem (sorry-free)...**` | **Migrate** to `authorNotes: [{ kind: "status", body }]` |
| `> **Caveat (over-permissive pentagon)...**` | **Migrate** to `authorNotes: [{ kind: "caveat", body }]` |
| `> **Refined-framing note (added when promoting...)**` | **Migrate** to `authorNotes: [{ kind: "refined-framing", body }]` |
| `> **Status (May 2026):** ...` (dated) | **Migrate** with ISO date e.g. `date: "2026-05-24"` (full YYYY-MM-DD preferred per `AuthorNote.date` schema doc) |
| `> **Status: DEPRECATED — superseded by ...**` | **Migrate** to `authorNotes: [{ kind: "deprecated", body, see: "..." }]` |
| `> **Theorem (conditional on [conj:X]).**` | **KEEP IN PROSE** — §3b-cond structural banner, part of the theorem statement, not an author note. |
| `**Note:** <technical clarification of scope/applicability>` | **KEEP IN PROSE** if it's scholarly content (a real mathematical caveat about applicability); **MIGRATE** if it's author-tracking. |

**Example migration**:

`.md` before:
```markdown
**Proposition.** *X holds.*

> **Status: theorem (sorry-free, modulo gap Y).** Lean file
> [`x.lean`] proves the main statement; the residual gap Y is
> documented in `conj:y`.

## Lean structure
```

`.ts` after (banner gone from .md; metadata added):
```ts
authorNotes: [
  {
    kind: "status",
    body: "**theorem (sorry-free, modulo gap Y).** Lean file `x.lean` proves the main statement; the residual gap Y is documented in `conj:y`.",
  },
],
```

**Audit/enforcement**: `local/one-voice-audit` Category H
auto-discharges this migration (mechanical fix authorised without
author approval per the skill's §3 "Apply mechanical fixes").

**History**: this convention was established 2026-05-24 (PR #1098).
Prior to that, banners lived in prose; the migration is gradual —
new authoring should use `authorNotes` from the start.

### 5. Tactic strategy (try in order)

| Goal pattern | Try first | Then try |
|---|---|---|
| Algebraic identity (`x = y`) | `ring` | `field_simp; ring` |
| Non-negativity (`0 ≤ x`) | `positivity` | `linarith` |
| Numeric (`x < y`) | `norm_num` | `linarith` |
| Definitional equality | `rfl` | `unfold …; rfl` |
| Diagram / naturality | `aesop_cat` | `slice_lhs`, `slice_rhs` |
| Anything else | `simp` | `aesop` |

### 6. Use MCP tools, not shell commands

| Task | Use this | Not this |
|---|---|---|
| Check errors | `lean_diagnostic_messages` | `lake build` + parse |
| Read goal state | `lean_goal` | Python scripts |
| Search Mathlib | `lean_leansearch` / `lean_loogle` | grep Mathlib source |
| Try tactics | `lean_multi_attempt` | edit-build-repeat |
| Axiom audit | `lean_verify` | manual inspection |

### 7. Category theory conventions

- **Category notation**: Use bold `$\mathbf{C}$` for categories
  (Herrlich–Strecker style), never calligraphic `$\mathcal{C}$`.
  Named categories are also bold: `$\mathbf{Rep}(\mathrm{SU}_q(2))$`.
  Calligraphic letters are reserved for sheaves, sites, algebras,
  bundles, and curves (`$\mathcal{S}$` = state bundle,
  `$\mathcal{E}_q$` = elliptic curve, `$\mathcal{O}$`, `$\mathcal{A}$`).
- **Fibre functor**: Always `$\tau$` (not `$\omega$` or `$U$`).
  Minimise its appearance — write `$(\mathbf{C}, A)$` when the functor
  is not needed; write `$(\mathbf{C}, A, \tau)$` only when `$\tau$` is
  explicitly used.
- **QOU archimedean tuple**: `$(\mathbf{C}, \varTheta, G, \mathcal{S})$`.
  The old 5-tuple $(M, \varTheta, G, P, E)$ is **deprecated**.
  - $M$ (base manifold) is subordinate to $\varTheta$ (its domain).
  - $P$ (principal bundle) is subordinate to $\mathcal{S}$ (frame bundle
    of the state bundle under $G$). Mention $P$ only when discussing
    gauge structure directly.
  - $\mathcal{S} = P \times_G \mathbb{CP}^1(\mathbb{C}) \to M$ is the
    associated state bundle; replaces $E$.
- Functors are bundled: `F.obj X`, `F.map f` — never treat `F` as a function.
- Open `CategoryTheory.MonoidalCategory` for notation: `X ⊗ Y`, `𝟙_ C`,
  `α_`, `λ_`, `ρ_`, `X ◁ f`, `f ▷ X`.
- Diagram commutativity: try `aesop_cat` first, then `slice_lhs`/`slice_rhs`.
- Use `Subsingleton (X ⟶ Y)` for vanishing hom-spaces (avoids `Preadditive`).

### 7aa. Notation register (STRICT) — see content notation block

The authoritative source for every mathematical symbol used in the
paper is the front-matter **Notation** chapter, rendered into the
PDF immediately after the table of contents:

- **Per-chapter symbol tables**:
  [`content/quantum-observable-universe/notation/notation-register.md`](content/quantum-observable-universe/notation/notation-register.md)
- **Collision avoidances + conventions**:
  [`content/quantum-observable-universe/notation/notation-collisions.md`](content/quantum-observable-universe/notation/notation-collisions.md)

Agents **must** treat those `.md` files as authoritative when picking
a font/symbol for a concept. When adding a new symbol convention,
edit the content block — not this section.

**Do not mirror the per-chapter tables here.** The previous mirror
drifted three sites in Phase 5n and is removed. Open the content
block above when you need a symbol or a font.

#### Stable font-family conventions (rarely change)

These five rules cover ~95% of authoring decisions. If your usage
doesn't fit one, open `notation-register.md` before inventing a new
convention.

| Family | Use for | Examples |
|--------|---------|----------|
| **bold** `\mathbf{...}` | Categories | `$\mathbf{C}, \mathbf{Rep}$` |
| **calligraphic** `\mathcal{...}` | Sheaves, bundles, algebras, curves, braid words | `$\mathcal{S}, \mathcal{O}, \mathcal{A}, \mathcal{H}_q, \mathcal{E}_q, \mathcal{B}_K$` |
| **fraktur** `\mathfrak{...}` | Physical observables: mass, energy, bandwidth, particles | `$\mathfrak{m}, \mathfrak{E}, \mathfrak{B}, \mathfrak{p}, \mathfrak{n}, \mathfrak{H}$` |
| **Greek lowercase** | Morphisms, measures, exponents | `$\varrho, \mu, \chi, \tau, \sigma$` |
| **plain italic** | Scalars, weights, indices | `$q, z, y_\lambda, w_\lambda, c$` |

#### Top-of-mind collision rules (do not violate)

For the full list with rationale, see `notation-collisions.md`. Quick
rules of thumb:

- `$c$` = color (never charm; charm is `$\mathfrak{c}$`)
- `$p$` = brane point (never proton; proton is `$\mathfrak{p}$`, proton count is `$Z$`)
- `$\gamma$` = photon (never vortex; vortex is `$\varrho$`)
- `$H_q$` alone = **forbidden** (collision); use `$\mathcal{H}_q$` (shuffle) / `$\hat{H}_q$` (Hamiltonian) / `$H_n(q)$` (Hecke) / `$H_q(\lambda)$` (hook-length)
- `$E$` alone = **not used**; use `$\mathcal{S}_p$` (fibre), `$\mathfrak{E}$` (energy), `$\mathcal{E}_q$` (elliptic curve), or `$E_{\mathfrak{H}}$` (crossing energy with hadron subscript)
- Three partition-weight families `$y_\lambda$` / `$w_\lambda$` / `$\tilde w_\lambda$` are **distinct** at `$q \neq 1$` — never conflate
- `$q = 1.1097$` (or any specific numerical value) **must not appear** outside the introduction and Chapter 7

### 7ab. Observed / derived values — approximation convention (STRICT)

When stating a numerical value derived from the substrate parameter
`$q_0$` or compared to experimental data, **always** use `$\approx$`
(or `$\simeq$`), **never** `$=$`.

```latex
% WRONG — implies exact equality
$\mathfrak{m}_{\mathfrak{p}}(q_0) = 938.272\;\text{MeV}$

% RIGHT — derived approximation
$\mathfrak{m}_{\mathfrak{p}}(q_0) \approx 938.272\;\text{MeV}$
```

**Exception:** You may write `$=$` when an explicit error term is
present:

```latex
% OK — error term makes precision explicit
$\mathfrak{m}_{\mathfrak{p}}(q_0) = 938.272 + O(10^{-3})\;\text{MeV}$
```

This applies to all physical predictions, CODATA comparisons, and
numerical evaluations at `$q_0$`. Exact algebraic identities
(e.g. `$c_q = 1/(q-1)$`) use `$=$` since they hold for all `$q$`.

**Optional surreal-equality form (language-level, 2026-07-13).** A
derived-value statement may additionally be recorded as the surreal
equality `$X = Y + \delta$` with the remainder's leading order
`$\mathrm{ord}_\omega(\delta)$` noted, per the blow-up calculus
(`def:surreal-blowup-calculus`) and the surreal-limit-transfer block
(`conj:surreal-limit-transfer`). This is bookkeeping, not new
mathematics (all surreal narrowings are Language-tier per the
2026-06-08 transcendental-surreal narrowing ledger); it never replaces
the mandatory `$\approx$` in archimedean prose, and it must not be
used to imply extra precision. Use it when a block wants to track
*where* an approximation's error lives (infinitesimal vs finite vs
growing grade) rather than merely its magnitude.

### 7a. Hecke-Skein convention (STRICT)

The Hecke algebra generator is **$\sigma_i$** (never $T$, never $t$ or
$A$ for the Jones polynomial variable). The Iwahori–Hecke algebra
$H_n(q)$ is presented as a quotient of the braid group algebra of
$B_n$, so the same symbol $\sigma_i$ is used for the braid group
generator and its image in $H_n(q)$ — context disambiguates.

- **Hecke relation**: $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$, equivalently
  $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$.
- **Skein relation**: Multiply the Hecke relation by $\sigma_i^{-1}$ to
  get $\sigma_i - \sigma_i^{-1} = q - q^{-1}$, which is the Skein
  relation $L_+ - L_- = (q - q^{-1})\,L_0$.
- **Translation dictionary**:
  - $\sigma_i$ = positive crossing $L_+$
  - $\sigma_i^{-1}$ = negative crossing $L_-$
  - $1$ = smoothed crossing $L_0$
  - $q$ and $-q^{-1}$ are the eigenvalues of $\sigma_i$ (symmetric and
    antisymmetric channels respectively)
- **Jones polynomial**: Always $J_K(q)$, never $V_K(t)$ or bracket
  with variable $A$.  The Jones polynomial is the Markov trace
  $J_L(q) = \mathrm{tr}_M(\rho(\beta_L))$ in $H_n(q)$.
- **Braid vs Hecke**: $\sigma_i$ denotes both the braid-group generator
  in $B_n$ and its image in $H_n(q)$; the latter satisfies the Hecke
  relation above while the former satisfies only the braid relations.
  This shared notation follows the standard knot-theory convention
  (Kassel, Jones).

### 7b. Symmetric-crystal techniques (KLR / Kashiwara) — authoring guidance

When **expanding the QOU formalization** or **updating the GS / Hecke
reduction engine**, prefer these symmetric-analogue constructions over
custom combinatorial machinery. Each one is a structural shortcut that
buys a categorical guarantee for free.

1. **Type B folding for chirality / CPT.** To enforce matter–antimatter
   pairing structurally in the reduction engine, do not write custom
   $\mathbb{Z}/2\mathbb{Z}$ rules. Fold the $\mathfrak{sl}_n$ Cartan
   datum into a Type B datum; the resulting Kashiwara graph is a
   *symmetric crystal*, and its GS normal forms are bar-involution
   ($q \mapsto q^{-1}$) invariant by construction. Stable matter =
   fixed points of the folded crystal.

2. **Decategorifying to KL bases for the classical limit.** The
   transition from quantum braiding to macroscopic statistics
   (Pauli / Bose–Einstein) is the functor mapping the KLR canonical
   basis to the Kazhdan–Lusztig basis of $S_n$. Define the classical
   limit of fluid dynamics via this functor — do not abandon the
   categorical substrate to recover ordinary statistics.

3. **Demazure sub-crystals for resonances.** Unstable intermediaries
   (W/Z bosons, hadronic resonances, virtual particles) are Demazure
   sub-crystals — incomplete topological states. Their non-symmetric
   Macdonald-polynomial evaluation under the Observation Frame
   ($\tau$ / Markov trace) reproduces the broken symmetry of a
   short-lived state without ad-hoc decay machinery.

These directives are **authoring shortcuts**, not new content. Apply
them when implementing a feature whose first instinct would be a
hand-rolled combinatorial rule; the symmetric-crystal route gives the
correct algebraic answer with less code and an audit trail to the
KLR / Kashiwara literature (Brundan–Kleshchev, Kashiwara, Lecouvey).

**Audit precedent (2026-05-30):** the §7b shortcuts are **authoring
guidance, not proof-restructure triggers**. An external AI dialog
re-pitching KLR/crystal as (a) GS compute-speedup, (b) positivity-
by-construction, (c) Option E Δ_λ closure was assessed in
[`docs/audits/2026-05-30-klr-dialog-assessment.md`](docs/audits/2026-05-30-klr-dialog-assessment.md);
verdict was **0/6 candidate proofs would meaningfully shorten** with
a KLR layer (existing GS arguments are already one-line Diamond-Lemma
citations; positivity claims that appear are archimedean bounds on
real `q > 0`, not `dim Hom ≥ 0` claims). Mass-formula mis-framings
(re-introducing the purged `λ_scale`) and Bloch-Wigner / dilog-
transcendence arguments on the trefoil (non-hyperbolic → D(z) = 0)
are recurrent re-pitch failure modes — **read the audit doc first**
before re-deriving the analysis on a new KLR re-pitch.

### 7c. Base ring convention: generic `R` vs. archimedean `ℝ` (STRICT)

Every Lean declaration that holds in a generic commutative ring must
be stated over a **type variable** — never silently specialised to `ℝ`.
The substrate-to-archimedean wall is the structural cut: a definition
or theorem that uses any of `Real.sqrt`, `Real.rpow`, `Real.log`,
`Real.exp`, `Real.cos`, ordering predicates (`0 < q`, `q < 1`),
`linarith`, or any other archimedean-specific construct **must**
declare its types as `ℝ`. Everything else — categorical content,
algebraic identities, q-deformation combinatorics, Wenzl / Hecke /
Hoefsmit structural data — uses a generic `{R : Type*}` parameter
with the weakest typeclass that admits the construction:

| Construction | Typeclass | Example |
|--------------|-----------|---------|
| Polynomial identity | `[CommRing R]` | `theorem foo (x : R) : (x + 1)^2 = ...` |
| Inverse / `x⁻¹` | `[Field R]` or `[GroupWithZero R]` | `def bar (Q : R) := 1 / (1 - Q)` |
| Negative-integer powers `x^(n : ℤ)` | `[GroupWithZero R]` | `Q ^ (contentSum λ)` |
| Square root / radical | `ℝ` | `noncomputable def hoefsmitB (q : ℝ) := …` |
| Ordering `0 < q` | `ℝ` (or `[LinearOrderedField R]`) | `theorem bar_inv (q : ℝ) (hq : 0 < q) : …` |
| `Real.cos`, `Real.exp`, … | `ℝ` | `noncomputable def alpha_N1 (q : ℝ) := Real.cos …` |
| CODATA / experimental value | `ℝ` | `noncomputable def codata_proton_MeV : ℝ := 938.272` |

**When in doubt, start generic.** Refactoring `ℝ`-specialised code to
generic `R` later is cheap (parameter sweep); refactoring generic-`R`
code to `ℝ` when an archimedean construct lands is also cheap (drop
the parameter). What is *not* cheap is the downstream code that
inherits the wrong specialisation and accretes archimedean assumptions
silently. Prefer the more general signature at the point of authoring.

**Lean integer / rational literals** — `(2 : R)`, `((3 : ℕ) : R)`,
`((p / q : ℚ) : R)` — are uniformly available over any `CommRing R`
(via `Nat.cast`, `Int.cast`, `Rat.cast`), so concrete combinatorial
identities like `[2]_q = q + q⁻¹` state cleanly over generic `R` with
`q : R`.

**Archimedean specialisation** — when a generic-`R` block needs to
specialise to `ℝ` for a numerical evaluation (e.g. computing the
substrate `q ≈ 1.1097`), the specialisation lives in a *separate*
file under `descartes-universe/` or `observations/` and consumes the
generic result via a `(R := ℝ)` instantiation. The generic block
itself stays in `braids-and-knots/` or `quantum-observable-universes/`
without ever mentioning `ℝ`.

See `notation/notation-collisions.md §Base ring convention` for the
notation-table entry and the §7c row in this rule's table.

### 7d. Universe conventions (STRICT) — pinning universe-carrying structures

A structure/class with a `Type*`-valued **field** (e.g. `fibreAt : M →
Type*`, `carrier : Type*`) is *universe-carrying*: every occurrence in a
signature elaborates with a fresh universe metavariable, and a theorem
header is generalized **before** its body elaborates. Two binders
mentioning the same universe-carrying type therefore get *distinct
rigid* universes, and the body fails with
`QLocalSystem.{u_1,u_4} ≠ QLocalSystem.{u_1,u_2}`-style mismatches.
(Incidents: `Torsion/MassGap` repaired in PR #2094;
`QGeometricLanglands` repaired in PR #2125, where these rules were
surveyed and drafted.)

- **U1 — default stays `Type*`.** Leaf declarations whose types appear
  in only one binder keep `Type*`; no churn.
- **U2 — universe-carrying structures get named universes at authoring
  time.** Any structure/class with a `Type*`-valued field that is
  consumed by another structure, a class field, or a multi-binder
  theorem declares `universe u v …` and pins the field
  (`fibreAt : M → Type v`). Glossary (Ch 8) wrappers exempt.
- **U3 — tie at use sites.** A signature mentioning a universe-carrying
  type in ≥ 2 binders (instance + argument, or two arguments) whose
  body relates them must tie the universes explicitly
  (`[FibreFunctorRigidity.{u, v} M]` +
  `(es es' : QHeckeEigensheaf.{u, v} M)`).
- **U4 — ∃-repackaging as the lighter alternative.** When the relation
  is existential anyway, restate à la `MassGap`
  (`∃ ymg, ymg.q = q ∧ ymg.transferMatrix = tm`) so unification happens
  inside one binder; record which pattern was used in the docstring.
- **U5 — never positional-apply `.{…}` to an unpinned declaration.**
  Auto-bound universe order is an elaboration artifact; pin the
  declaration first, then apply.
- **U6 — naming.** `u` = base/manifold type, then `v, w, x` in order of
  first appearance for fibre/carrier families (matches
  `CategoricalFoundations`' `QuantumUniverse.{u, v} k` idiom and
  `QGeometricLanglands`).

Recorded 2026-06-11 per owner instruction on PR #2125; pending
refinements from the Gemini discussion round there land as edits to
this section.

### 8. File hygiene

- Never commit `.lake/`, `lake-packages/`, or `build/`.
- **Pin external dependencies to commit hashes** in `lakefile.toml` —
  never use branch names (`main`, `master`) or version tags (`v4.16.0`).
  Mathlib version numbers ≠ Lean version numbers; tags can resolve to
  unexpected toolchain versions.
- **All deps must agree on the same `lean-toolchain`**. Before adding or
  updating a dep, check `cat .lake/packages/<dep>/lean-toolchain` for
  every package. If any disagree, find compatible versions first.
  See `formalizer.md § Adding New Dependencies` for the full procedure.
- To recover from broken `.lake/`, use `mv .lake /tmp/...` (not `rm -rf`).
- Keep imports minimal — only import what the file actually uses.
- The `.lean` sibling file must share the same root name as its `.ts`/`.md`
  siblings (e.g., `rigid-monoidal-category.lean`).

## Content-object architecture

Content is organized as **atomic knowledge units** — each definition,
theorem, remark, etc. is a self-contained file triple:

```
content/
  <paper-name>/
    <paper-name>.ts              ← Paper manifest (references chapter URIs)
    <chapter-dir>/
      <chapter-dir>.ts           ← Chapter manifest (sections → block refs)
      <block-name>.ts            ← Typed manifest (kind, label, lean ref, status)
      <block-name>.md            ← Narrative content (markdown + TeX snippets)
      <block-name>.lean          ← Lean formalization (when required by kind)
```

### File naming convention

Sibling files share the same root name: `rigid-monoidal-category.ts`,
`rigid-monoidal-category.md`, `rigid-monoidal-category.lean`.

### Type system

| Block kind | Lean required? | Label prefix |
|-----------|---------------|-------------|
| `definition` | **Yes** (enforced at type level) | `def:` |
| `theorem`, `lemma`, `proposition`, `corollary` | Expected (warning if missing) | `thm:`, `lem:`, `prop:`, `cor:` |
| `conjecture`, `example`, `remark` | Optional | `conj:`, `ex:`, `rem:` |
| `simulator` | N/A | `sim:` |
| `prose`, `equation`, `diagram` | N/A | — |

### Pipeline

```
.ts manifests + .md content
  → Zod schema validation (shape + types)
  → Constraint rules (file existence, cross-refs, lean requirements)
  → LaTeX rendering (markdown → LaTeX conversion)
  → AST validation (unified-latex parse of rendered output)
  → chapters/*.tex output
```

### Key files

| Path | Purpose |
|------|---------|
| `content/schema/types.ts` | TypeScript types (discriminated unions) |
| `content/schema/constraints.ts` | Zod schemas + constraint rules |
| `content/schema/builders.ts` | `definition()`, `theorem()`, `prose()`, etc. |
| `folio-assistant/content/pipeline/validate.ts` | Three-level validation |
| `folio-assistant/content/pipeline/render-latex.ts` | Block → LaTeX + AST validation |
| `folio-assistant/content/pipeline/build.ts` | Full document build |
| `content/schema/references.ts` | **Bibliography source of truth** (CSL-JSON) |
| `folio-assistant/content/pipeline/export-bibtex.ts` | Generates `references.bib` from CSL-JSON |
| `folio-assistant/content/pipeline/validate-references.ts` | Bibliography + citation cross-checks |
| `folio-assistant/content/pipeline/citations.ts` | `\cite{}` extraction from .md content |
| `folio-assistant/content/pipeline/find-dangling-remarks.ts` | Audit: find remarks without `interprets` |

### Bibliography architecture

The bibliography is managed as **typed CSL-JSON** in
`content/schema/references.ts`. BibTeX (`references.bib`) is a downstream
render target, auto-generated from `references.ts` (the `bun run export-bibtex`
shortcut was dropped in the miga migration — pending re-wiring).

- **Adding a reference**: use the `ref()` builder in `references.ts`
- **Block citations**: `cites: string[]` field on blocks (auto-extracted
  from `\cite{}` in .md by the pipeline, or set explicitly in .ts)
- **Chapter bibliography**: aggregated at build time from all block cites
- **Validation**: bibliography cross-checks (schema, uniqueness, DOIs, and
  cross-references against Lean `-- Ref:` and LaTeX `\cite{}`) — the
  `bun run validate-refs` shortcut was dropped in the miga migration (pending re-wiring)
- **Never edit `references.bib` directly** — it is regenerated on build

### Dependency graph integration

The `uses[]` field lists **immediate neighbors only** — direct
dependencies, not transitive ones.  If A→B and B→C, then A lists
only B; C is reachable by walking the graph.  Run
`bun run pipeline/prune-transitive-deps.ts` to enforce this.

The `uses[]` field in content objects + Lean import graphs form a
combined dependency DAG. Editors and proof-writers use this to:

- **Track upstream changes**: when a definition changes, find all
  theorems/lemmas that `uses` it and flag them for re-validation
- **Track downstream impact**: when proposing a change, identify all
  blocks that depend on the changed block
- **Scope test runs**: only run Lean builds / AST validation for the
  changed block and its downstream dependents
- **Prioritize formalization**: find blocks with the most dependents
  that are still `not_started`

### Cross-paper references

The `uses[]` field supports three reference scopes:

| Scope | Syntax | Example |
|-------|--------|---------|
| Same paper | bare label | `"def:quantum-universe"` |
| Same folio | `"paper-dir:label"` | `"unital-groebner-bases:cor:pbw"` |
| External folio | full URL | `"https://folio.example.org/viewer/#/view/paper-id"` |

Cross-paper refs are validated at folio level, not per-paper. The
`uses-resolve` constraint skips qualified refs (those matching
`paper-dir:label` or starting with `https://`).

Each paper in `content/folio.ts` has an optional `url` field for
viewer routing. CSL-JSON entries in `content/schema/references.ts`
for folio-hosted papers include a URL field matching the viewer hash route
(e.g. `/viewer/#/view/unital-groebner-bases`).

### Markdown content convention (in .md files)

- Inline math: `$...$`
- Display math: `$$...$$`
- Complex TeX (tikzcd, align): fenced code block with `` ```tex `` tag
- Bold → `\textbf{}`, italic → `\emph{}` in LaTeX output
- Cross-refs: `[text](#label)` → `\hyperref[label]{text}`

### TeX authoring patterns for agents

These rules prevent rendering errors in the content pipeline.
Violations produce broken LaTeX in titles, captions, and body text.

**1. Math in titles is supported.** Block titles (in `.ts` manifests)
may contain inline math. The `escapeLatex()` function preserves
`$...$` segments verbatim. Always use `$...$` delimiters:

```ts
// CORRECT — math preserved in rendered \begin{example}[{...}]
title: "Reeb derivation for $\\mathrm{SU}(2)$"

// WRONG — bare LaTeX commands will be escaped to garbage
title: "Reeb derivation for \\mathrm{SU}(2)"
```

**2. Multi-line inline math is valid.** The remark-math parser handles
`$...$` spanning multiple lines. This is the standard pattern for long
inline expressions in list items:

```md
1. **Cyclicity**: $\mathrm{tr}_{\mathrm{Ad}}(f \circ g) =
   \mathrm{tr}_{\mathrm{Ad}}(g \circ f)$, inherited from the
   Frobenius relation.
```

**3. Never use raw TeX commands in prose outside `$...$`.** The markdown
→ LaTeX converter only passes through content inside math delimiters
or `` ```tex `` fenced blocks. Bare `\mathrm{...}` outside delimiters
renders as literal text.

**4. Use `$$...$$` on separate lines for display math.** The `$$`
delimiter must be alone on its line (or at the very start/end):

```md
The formula is:

$$
  \nabla^2 \phi = 0
$$
```

**5. For complex environments (tikzcd, align), use fenced tex blocks:**

````md
```tex
\begin{tikzcd}
  A \arrow[r] & B
\end{tikzcd}
```
````

**6. Ampersands in math are fine.** The `&` character inside `$...$` or
`` ```tex `` blocks is not escaped (it's a column separator in matrices
and alignments). Only `&` in prose text causes LaTeX errors.

## Lean MCP server (lean-lsp-mcp)

The [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp) server is
configured via `.mcp.json`. It provides Claude Code with:

- Diagnostics, goal states, hover docs, completions
- LeanSearch, Loogle, Lean Finder, Lean Hammer search tools
- Code actions ("Try This"), profiling, axiom verification
- Local project search (requires ripgrep)

### Setup (ChromeOS / Crostini)

Prerequisites: `git`, `curl`.

Use the `lean_setup` MCP tool (provided by paper-assistant). It installs:
uv, elan, the Lean toolchain pinned in the **root** `lean-toolchain`,
Mathlib cache, ripgrep, and runs `lake build` in the **root Lake
workspace**.

Alternatively, from the command line:

```bash
# Build every paper at once from the root workspace
lake exe cache get && lake build

# Or build a single paper package
lake build QOU        # quantum-observable-universe
lake build UGB        # unital-groebner-bases
lake build Fred2005   # fred2005-formal-groups
```

### Local Mathlib cache

To avoid re-cloning Mathlib from GitHub on every fresh `.lake/` build,
keep a persistent local clone one directory above the repo:

```bash
cd ..  # parent of the repo root
git clone https://github.com/leanprover-community/mathlib4.git
```

The build tools automatically detect this clone (configured in
`lean-mcp.config.json` → `lean.local_mathlib_path`) and set a git
`insteadOf` redirect so Lake fetches from the local clone instead of
GitHub. This is transparent — no changes to `lakefile.toml` needed.

| Config key | Default | Purpose |
|-----------|---------|---------|
| `lean.local_mathlib_path` | `../mathlib4` | Path to local clone (relative to repo root) |
| `lean.mathlib_git_url` | `https://github.com/leanprover-community/mathlib4` | Upstream URL to redirect |

The `lean_build` tool warns if the local clone is >7 days stale and
offers `update_local_mathlib: true` to fetch the latest commits.
Shell scripts use `scripts/lib/lean-env.sh` for the same logic.

#### Manual fallback when auto-detection fails (cache 403 / LSP timeout)

In sandboxed cloud environments the auto-detection sometimes does not
fire (no `lean-mcp.config.json` evaluation reaches the LSP context),
and **`lake exe cache get`** returns 403 forbidden on every shard
(typically 7335+ download failures). When this happens
**`lean_diagnostic_messages`** also times out at 60 s because no
prebuilt oleans exist.

**FASTEST FIRST (Step 0): restore prebuilt oleans from the `lake-cache/*`
orphan branch — ≈2 min vs a 30–60 min from-source build.** A full build is
preserved on `lake-cache/qou-v4-24-0` (slug matches `cat lean-toolchain`).
Only if the restore misses do Steps 1–3 (source clone + from-source build) —
and **SEED the cache branch afterwards**. Full slug/seed rules:
[`lean-environment-setup.md` §"PRESERVE THE BUILD"](.claude/skills/local/lean-environment-setup.md).

```bash
# Step 0 (FASTEST — try before Steps 1–3): restore prebuilt oleans from the
# lake-cache orphan branch whose slug is DERIVED from the pinned toolchain
# (future-proof, works from any subdir, CRLF-safe).
ROOT=$(git rev-parse --show-toplevel); TGZ=$(mktemp)
SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)   # v4.24.0 -> v4-24-0
git fetch --depth=1 origin "lake-cache/qou-$SLUG" \
  && git ls-tree --name-only FETCH_HEAD | grep '^lake-oleans\.tgz\.part' | sort \
     | while read -r p; do git show "FETCH_HEAD:$p"; done > "$TGZ" \
  && tar xzf "$TGZ" -C "$ROOT" \
  && touch "$ROOT/.lake/RESTORED-NO-TRACES" \
  && echo "restored from lake-cache/qou-$SLUG — skip Steps 1–3; lean-direct ONLY, see below"

# 🛑 A RESTORED tree has oleans but NO .trace files, so Lake treats every one as
# stale: a later `lake build` rebuilds them from source AND EVICTS THE RESTORE.
# Measured 2026-08-15 (bean qou-r13s) running `lake build QOU UGB Fred2005` at
# the root against a tree restored exactly as above: root mathlib oleans
# 6990 -> 334, and of the 536 oleans written in ten minutes, 520 were
# mathlib/aesop/batteries and ZERO were QOU/UGB/Fred2005. It is silent — the
# output reads as ordinary build progress. Verify with lean-direct instead
# (2.4 s vs 50 minutes of nothing); guard any build step with:
#     [ -f "$ROOT/.lake/RESTORED-NO-TRACES" ] && echo "restored — do NOT lake build"
# Delete the marker only once Lake has genuinely rebuilt the tree.

# Step 1: Shallow-clone mathlib locally (~144 MB).  [fallback if Step 0 misses]
cd .. && git clone --depth 1 https://github.com/leanprover-community/mathlib4.git
cd -

# Step 2: Global git insteadOf redirect so Lake's mathlib fetches
# go to the local clone instead of the network.
git config --global url."file:///home/user/mathlib4".insteadOf \
  "https://github.com/leanprover-community/mathlib4"

# Step 3: Verify by querying the LSP on a mathlib-importing file.
# First query is slow (cold workspace) but should return real
# diagnostics, not the `success: false, items: []` timeout sentinel.
```

This is also documented in
[`.claude/skills/local/lean-environment-setup.md` §"Mathlib cache 403 fallback"](.claude/skills/local/lean-environment-setup.md#mathlib-cache-403-fallback-proven-workaround-2026-06-03).
Don't iterate Lean proofs blind when the LSP is cold — establish
LSP feedback first, then iterate against real diagnostics.

**To VERIFY (not author-iterate) a changed `.lean` file, prefer
`lean`-direct over `lake build`** (2026-06-13, cost a session ~40 min):
`lake build <Module>` — even for one module — re-resolves the dep graph
and rebuilds Mathlib from source (the `import Mathlib.Tactic` closure is
~3000 modules), *and* wipes the restored oleans. Instead set `LEAN_PATH`
to the restored olean dirs and run `lean <file>` directly (`exit 0` =
checks, sorry-free). The Mathlib oleans **are reachable** — they ship on
`lake-cache/qou-<toolchain-slug>` (~2919 oleans); restore + `lean`-direct
is ~2 min vs a 40-min `lake build` storm. If a stray `lake build` already
dropped the olean count (`find .lake/packages/mathlib -name '*.olean' | wc -l` ≪ 2919),
re-restore the cache branch before `lean`-direct. Full recipe + recovery:
[`lean-environment-setup.md` §"VERIFY a single file with lean-direct"](.claude/skills/local/lean-environment-setup.md#verify-a-single-file-with-lean-direct).

> **STRICT — route, don't give up, and prefer a sub-agent.** On **any**
> Lean env/tool failure (LSP "no valid project path", `leansearch` SSL
> error, cache `get` 403, `elan toolchain install` SSL / "failed to parse
> release data", empty `~/.elan/toolchains/`, `lake build` timeout) do
> **NOT** conclude "Lean is unavailable." Most of these have documented
> workarounds (e.g. the elan host `release.lean-lang.org` is firewalled in
> some web sandboxes but the **GitHub release asset is allowlisted** — install
> the toolchain by hand). FIRST `grep -ri "<error keyword>" .claude/skills/
> AGENTS.md docs/` (a generalisation of the corpus-grep / formalize-first
> disciplines: check what's known before declaring a capability unavailable),
> then **delegate the long install to a background sub-agent** per
> [`lean-environment-setup.md` §"Delegate the install to a sub-agent"](.claude/skills/local/lean-environment-setup.md)
> so the main task isn't blocked. Only after the documented workarounds hit a
> *hard* network block may you fall back to a rigorous hand-audit — and then
> say so explicitly.

### Remote MCP server

A Docker-based remote deployment is available in `deploy/`:

```bash
cd deploy && ./setup-remote.sh
```

All settings are driven by `lean-mcp.config.json` at the repo root.

Architecture: `Client → Caddy (TLS) → auth-gateway (dual OAuth) → lean-lsp-mcp (HTTP)`

- Docker image built by CI on every push to main (`build-lean-mcp.yml`)
- All Lean deps and oleans baked into the image for fast startup (~10-20s)
- Auth: Dual OAuth — Google (viewers) + GitHub (collaborators/owner)
- Roles: viewer (read + feedback), collaborator (edit + branches), owner (commit to main)
- Whitelists: `deploy/google-viewers.txt` + `deploy/github-collaborators.txt` (manually managed)
- Auto-update: `self-update-folio.sh` polls git + GHCR every minute via cron
- Programmatic access: bearer token via `FOLIO_API_TOKEN`
- Hosting: Hetzner CX22 (~€4.50/mo), provisioned via `provision-hetzner.sh`

To switch a client to remote mode, update `.mcp.json`:

```json
{"mcpServers":{"lean-lsp":{"url":"https://folio.litlfred.org/mcp"}}}
```

To extract the deploy infrastructure for another repo, copy `deploy/`,
`lean-mcp.config.json`, `.github/docker/Dockerfile.lean-mcp`, and
`.github/workflows/build-lean-mcp.yml`, then edit `lean-mcp.config.json`.

### Session-start hook

`SessionStart` hooks in `.claude/settings.json` run, in order:
`setup-elan-symlinks.sh` + `setup-lean-toolchain.sh` (Lean toolchain setup —
output redirected to `${TMPDIR:-/tmp}/qou-setup-lean.log`), `lean-build-bg.sh`
(background build; output to `${TMPDIR:-/tmp}/qou-lean-build-bg.log`, status to
`/tmp/qou-lean-build-status.json`), and `session-start-coord-sweep.sh` (surfaces
the active bean work-plan + sibling-PR coordination). The Lean scripts source
`scripts/lib/lean-env.sh` for shared environment detection and exit quietly when
`release.lean-lang.org` is firewalled, so a sandbox without Lean does not flood
the session transcript. If Lean is unavailable and the request requires it, the
editor skill suggests the `lean_setup` MCP tool rather than silently failing.


## Project structure

| Path | Purpose |
|------|---------|
| `content/` | **Authoritative content objects** (`.ts` + `.md` + `.lean` triples) |
| `content/schema/` | Type system, Zod schemas, builder functions (re-exports from `folio-assistant/schemas/`) |
| `content/pipeline/` | qou-side audit scripts only (vacuity/axiom, clarity, orphan, trace-convention, …). Validation / rendering / build moved to `folio-assistant/content/pipeline/` in the miga migration — check which side a script is on before invoking it |
| `content/<paper>/` | Paper manifest + chapter directories |
| `content/<paper>/fluid-dynamics/` | Ch 7: Fluid dynamics of the brane (q-NS, NS obstruction) |
| `folio-assistant/` | **Platform package** — MCP server, auth, UI, blocks, viewer |
| `folio-assistant/src/` | Generic core (server, types, routes, tools, blocks registry) |
| `folio-assistant/adapters/paper/` | Paper content adapter (implements `ContentAdapter`) |
| `folio-assistant/schemas/` | Shared TypeScript types (proof-objects, glossary, etc.) |
| `folio-assistant/viewer/` | Paper viewer SPA + Pyodide cache Service Worker |
| `folio-assistant/ui/` | Assistant chat SPA |
| `folio-assistant/simulators/` | Interactive HTML simulators |
| `folio-assistant/feedback/` | User feedback (TypeScript files, committed to main) |
| `computations/` | Computation scripts and witness data (Layer 3 in-repo path; see `docs/ARCHITECTURE.md`) |
| `qou-mass/` | `qou-mass` package — external-researcher facade (`predict()`, `compute_tr_M()`, `canonical_braid()`). **v1.0.0; NOT on PyPI** (`pypi.org/pypi/qou-mass/json` → 404). 5 in-repo importers. Its `_internal/` is **generated** — see the note below. |
| `tools/qou-substrate/` | `qou-substrate` package — Layer 2a (q₀, mpmath precision, `WitnessBuilder`). **Not on PyPI** (404). 309 in-repo importers. |
| `tools/pyhecke/` | `pyhecke` — Layer 2b (Hecke / Gram / Markov trace). **Not on PyPI** (404). 70 in-repo importers. |
| `tools/pyhecke-native/` | `pyhecke-native` — PyO3 bindings into `hecke-engine`. **Not on PyPI** (404); [`pyhecke-native-wheel.yml`](.github/workflows/pyhecke-native-wheel.yml) builds a wheel but is `workflow_dispatch`-only and has no publish step. Build locally with `maturin build --release`. 89 in-repo importers. |
| `schemas/witness-schema/` | `witness-schema` PyPI + `@litlfred/witness-schema` npm — cross-language `*.witness.json` interchange schemas. **Under `schemas/`, not `tools/`** — moved back from folio-assistant by `e2ded2c607`. Install the package root (`pip install -e schemas/witness-schema`); `python/` under it holds the module but no `pyproject.toml`. |

> **Importer counts are measured, not maintained.** The five above were
> `1 / 7 / 19 / 15 / 1` and were wrong by up to two orders of magnitude
> (`qou-substrate` was 7, is 309) — a hand-kept number decays exactly like a
> hand-kept copy. Re-measure rather than trust the table:
>
> ```bash
> grep -rlnE "^\s*(from|import)\s+<pkg>(\.|\s|$)" --include=*.py . \
>   | grep -v "^./tools/<pkg-dir>/" | grep -v _deprecated | wc -l
> ```
>
> **None of `qou-mass`, `qou-substrate`, `pyhecke` or `pyhecke-native` are
> published.** All four 404 on PyPI, with no `dist/` and no publish step. Do not
> describe any of them as shipped, and do not reason about external consumers of
> their data — there are none. (`qou-mass` / `qou-substrate` checked 2026-08-15;
> the two `pyhecke` rows carried the same wrong claim until 2026-08-19 and were
> corrected the same way. `pyhecke-native` has a wheel workflow, which is
> probably how "PyPI wheel" got written, but it is `workflow_dispatch`-only and
> uploads nothing — building an artifact is not publishing it.)
>
> **Consequence for agents.** `pyhecke_native` cannot be `pip install`ed, so a
> container without it is the *default*, not an anomaly. Build it from
> `tools/pyhecke-native/` with `maturin build --release` (works: produces
> `pyhecke_native-0.9.0-cp311-...whl`) when a witness's `environment` block
> records it. **Do not cite `binding_canonical` as evidence that its absence
> changes results** — I did, and it was wrong: with the native extension
> installed the producer reproduces the same `tr_M_atom` byte-identically. That
> 48 % move was import-cone drift, not environment.
>
> **Never hand-edit `qou-mass/src/qou_mass/_internal/`.** It is generated from
> `computations/` by [`scripts/sync-qou-mass-vendor.py`](scripts/sync-qou-mass-vendor.py)
> (`--check` / `--apply` / `--list`). It was hand-copied until 2026-08-15, and
> all 14 copies had drifted — `witness_base` by 815 lines,
> `canonical_braid_crossings` by a whole generation. Worse, the drift *masked*
> a live defect: `test_ephemeral_mask_sync` exists to detect mirror divergence
> and was green only because the mirror was stale. Run `--check` after any
> change to a module in the cone; it is the gate.
| ~~`tools/block-qa-schema/`~~ | **No longer in this repo.** The QA-sidecar interchange schemas (`<block>.qa.json` block-qa/v1 + `<criterion-id>.script.json` qa-script/v1) left with the platform code in `39fc90f6d6` (miga) and live in `litlfred/folio-assistant`; producing types are `folio-assistant/schemas/block-qa.ts`, reachable here via [`scripts/setup-folio-assistant.sh`](scripts/setup-folio-assistant.sh). Do not look for it under `tools/` — this row described an in-repo path for weeks after the directory was deleted. |
| `tools/hecke-engine/` | `hecke-engine` Rust crate — Layer 1 canonical compute core (Gröbner-Shirshov reducer, Hoefsmit, Markov trace, Clarabel SDP backend). |
| `tools/hecke-engine-{wasm,node,r,jvm,c}/` | Multi-language bindings of `hecke-engine` (WASM, Node napi-rs, R/JVM/C — last three Tier-3). |
| `folio.config.json` | Adapter config (content type, adapter module, feedback dir) |
| `main.tex` | LaTeX preamble and document structure (rendering target) |
| `chapters/*.tex` | Generated LaTeX chapters (from content pipeline) |
| `references.bib` | BibTeX database (auto-generated from `content/schema/references.ts`) |
| `lakefile.toml`, `lean-toolchain` | **Root Lake workspace** — aggregates every paper package; `lake build` here builds all |
| `content/quantum-observable-universe/lean/` | `qou` Lake package (lib: `QOU`) |
| `content/unital-groebner-bases/lean/` | `ugb` Lake package (lib: `UGB`) |
| `content/fred2005-formal-groups/lean/` | `fred2005` Lake package (lib: `Fred2005`) |
| `folio-assistant/schemas/lean-packages.ts` | Registry mapping `lean.ref` URI prefixes → Lake packages |
| `blueprint/src/` | LeanBlueprint source (content.tex, preamble.tex, web.tex, print.tex) |
| `home_page/` | Jekyll landing page for GitHub Pages |
| `.github/workflows/` | CI/CD pipelines |
| `.github/scripts/` | Python orchestration (ontologist, extraction, stub generation) |
| `.claude/skills/local/` | Repo-specific review skills |
| `.claude/skills/<pkg>/` | Synced external skill packages |
| `library/` | **Ingested sources**, one directory per document: `library/<doc-id>/` holds the PDF, `structure.json` (metadata + TOC + section index), `sections/*.md` (**greppable** section text — corpus-grep path 5), and `candidates.json` (extracted claims, *proposals only*). `<doc-id>` is derived from the page-1 arXiv stamp (`arxiv-0706.2213v3`) or the slugified filename, and is the join key to `content/bib-qa-verifications.json`. Produced by folio-assistant's `scripts/pdf-structure.py` + `extract-candidates.py`; renamed from `uploads/` 2026-08-15. |
| `.beans/` | **Session work-plans as beans** — the [`beans`](https://github.com/hmans/beans) CLI flat-file issue tracker (install via `scripts/install-beans.sh`). Agent work-plan source of truth; see `.claude/skills/local/todo-manager.md` |
| `todos/` | Legacy work-tracking queues (`*-queue.json`), gitignored; being migrated into `.beans/` per the Folio-Assistant Infrastructure Migration (`miga` epic) |
| `docs/` | Planning documents, migration plans, dependency graphs |
| `scripts/` | Setup and health-check scripts (Lean MCP, etc.) |
| `lean-mcp.config.json` | MCP server config (domain, image, auth, ports) |
| `deploy/` | Remote MCP server deployment (Docker Compose, auth, auto-update) |
| `skills-config.json` | Skill package subscriptions |

## Build output (gh-pages)

Three workflows deploy to the `gh-pages` branch. GitHub Pages must be
configured to **deploy from the `gh-pages` branch** (not "GitHub Actions").

### Workflow → artifact mapping

| Workflow | Artifacts deployed to gh-pages |
|----------|-------------------------------|
| `blueprint.yml` | `blueprint/` (interactive dependency graph), `blueprint.pdf`, `docs/` (doc-gen4 API), `axiom-report.txt`, manifests |
| `lean_ci.yml` | `lean/content/<paper>/lean/` (per-paper source browsers for QOU/UGB/Fred2005), `lean/.../docs/`, `axiom-report.txt`, `dependency-graph.svg`, manifests |
| `publish.yml` | `papers/<dir>/` (per-paper viewers), `index.html` (folio), `schema-docs/` (TypeDoc), `drafts/` (feature branches) |

### Expected gh-pages contents

| Path | Source | Description |
|------|--------|-------------|
| `index.html` | publish.yml | Folio landing page (links to all papers) |
| `papers/<dir>/index.html` | publish.yml | Per-paper viewer with paper/visualizer toggle |
| `papers/<dir>/paper.html` | publish.yml | Enhanced HTML paper |
| `papers/<dir>/<dir>.pdf` | publish.yml | Compiled paper PDF |
| `papers/<dir>/<dir>.md` | publish.yml | Pandoc Markdown |
| `quantum-observable-universe.pdf` | publish.yml | Backward-compat copy of first paper PDF |
| `blueprint/` | blueprint.yml | Interactive dependency graph (plasTeX HTML) |
| `blueprint.pdf` | blueprint.yml | Print blueprint |
| `docs/` | blueprint.yml | doc-gen4 API documentation with hover definitions |
| `content/quantum-observable-universe/lean/` | lean_ci.yml | Raw Lean source files |
| `content/quantum-observable-universe/lean/docs/` | lean_ci.yml | doc-gen4 or fallback source browser |
| `axiom-report.txt` | blueprint.yml / lean_ci.yml | sorry audit, axiom dependencies |
| `dependency-graph.svg` | lean_ci.yml / publish.yml | Visual proof dependency graph |
| `schema-docs/` | publish.yml | TypeDoc content-object type reference |
| `proof-objects.json` | all | Formalization status manifest |
| `glossary.json` | all | Semantic glossary |
| `mapping.json` | all | Narrative-to-Lean identifier map |
| `drafts/<branch>/` | publish.yml | Feature branch preview builds |

### Error resilience

All workflows use `continue-on-error: true` at critical points so partial
output is still deployed even when the Lean build fails:

- **Lean build fails** → proof status updates, axiom report generates, source
  browser deploys.  `proof-objects.json` records which declarations errored.
- **doc-gen4 fails** → `lean_ci.yml` generates a fallback HTML source browser.
- **Blueprint compilation fails** → other artifacts (manifests, axiom report)
  still deploy.
- **latexdiff fails** → main PDF still publishes; diff PDF is skipped.

## Axiomatization is NOT a Proof (Anti-Laundering Rule)

Agents frequently conflate "Lean code that compiles with 0 errors" with "a mathematically proved theorem." 

1. **Axioms and Conditional Classes do not satisfy "Proved".** 
   If a user says "only do X if Y is proved," creating an `axiom`, `sorry`, or a conditional `class` (e.g., `[ZToCkMappingClass]`) to define the structure does **NOT** count as proving it. You must stop and state the math is open.
2. **Never launder empirical fits through Lean axioms.** 
   Do not use conditional classes as an excuse to wire un-derived constants into downstream dashboards or production scripts. If the closed-form math isn't proven from the 13 categorical drivers, the compute remains blocked.
3. **Formalize-First means PROVING the invariant.**
   Writing the structural scaffolding is good, but it does not unlock downstream physics code. Only a true closed-form derivation does.

## Strict Lean Discipline (owner directive 2026-07-27)

**This section consolidates and ELEVATES all Lean hygiene rules into a
single strict-enforcement block. It applies to ALL agent work —
exploratory discussions, derivation sessions, PR code, and idle-time
formalization alike. Violation of any item below is a review failure.**

### Zero-sorry default

1. **New theorems/lemmas MUST be sorry-free.** If you cannot discharge
   the goal, you have two honest options:
   - **State-and-queue:** declare the proposition with `sorry` + a
     `-- Ref:` citation (§1 above) and mark it `has_sorry` in the
     content block. This is an honest "stated, not yet proved" marker.
   - **Stop and report the gap.** Say "this is open" in chat. Do NOT
     silently leave a `sorry` hoping the user won't notice.
2. **Existing `sorry`s are NOT an invitation.** Do not add *new*
   `sorry`s to already-sorry-free files. If you touch a sorry-free
   file, it must remain sorry-free when you're done.
3. **`sorry` is never a "TODO" marker.** If the proof is too hard
   right now, state the gap explicitly in chat and in a `-- GAP:`
   comment, don't use `sorry` as a placeholder you "intend to fill
   later."

### No trivial trues, no tautologies, no laundering

4. **`theorem X : True := trivial` is ALWAYS a review failure** — in
   any declaration kind (`theorem`, `lemma`, `def`, `abbrev`,
   `instance`, `example`). The only exception is a documented
   shadow-stub or conjecture-block placeholder (§1a above).
5. **Tautological conclusions are banned:** `X = X := rfl`,
   `∀ x, x = x`, `True ∧ True`, or any proposition that is provable
   without using any hypothesis about the mathematical objects in
   question. If the *statement* doesn't say something falsifiable
   about the domain, it is not a theorem.
6. **`native_decide` laundering is banned.** Do not use `native_decide`
   or `decide` to mask a goal behind the kernel evaluator unless the
   goal is a genuinely decidable finite computation (e.g., checking a
   concrete numeric inequality). Using it to bypass an unproved
   structural claim is laundering.
7. **No axiom/class may substitute for a proof.** Creating
   `axiom myResult : P` or `class MyHyp where field : P` and then
   consuming it downstream is NOT proving `P`. It is assuming `P`.
   State it as a conjecture if it is genuinely open; do not disguise
   assumptions as infrastructure.

### Derive-then-check standard

8. **Every Lean proposition must state something falsifiable BEFORE
   the proof is attempted.** Write the `theorem` statement first.
   Read it. Ask: "could this be wrong?" If the answer is "no, it's
   true by definition / by unfolding / by `rfl`," then it is not a
   theorem — it is notation, and should be a `def` or `abbrev`, not
   dressed up as a proof.
9. **Derive, then check — never fit.** When formalizing a physical
   claim (e.g., a binding energy, a Stokes constant, a magnitude),
   the Lean statement must derive the value from upstream axioms /
   proved lemmas, not assert the value and prove `rfl`. The
   anti-fit discipline applies inside Lean exactly as it does in
   Python probes.
10. **Report honest negatives.** If the Lean proof attempt reveals
    that the proposition is *false* (e.g., a `norm_num` discharges
    the negation), that is a valuable result. Report it as a
    scope-(a) or scope-(b) refutation. Do NOT silently weaken the
    statement until it becomes trivially true.

### Applies to discussions and exploration

11. **These rules apply even in chat-only / exploratory sessions.**
    When discussing a derivation route (e.g., Δ_λ magnitude, Stokes
    constants, cusp-torus winding), any Lean code shown in chat or
    proposed for a branch must meet the same standard. "It's just
    exploratory" is not a licence for `sorry`-littered scaffolding
    or trivial-true placeholders.
12. **All agents inherit these rules.** Subagents, sibling-branch
    agents, and idle-time formalization agents are bound by the same
    discipline. A subagent that lands a `sorry` without citation or a
    trivial-true theorem is a review failure attributed to the
    parent session.

### When you can't close it — bean the gap (the honest exit)

13. **If you cannot close a derivation, CREATE A BEAN.** This is
    your exit — not a `sorry`, not a weakened statement, not a
    trivial-true placeholder. Run
    `beans create "GAP: <precise description of what's open>" --type task`
    with enough detail that the next agent (or the owner) can pick it
    up cold: what was attempted, why it failed, what the surviving
    candidates are, and what the next honest step would be. Then
    **stop** and report the gap in chat. An honest bean is always
    acceptable; a dishonest "closure" never is.
14. **Do NOT try to please.** The owner is a physicist. Fake progress
    is worse than no progress — it wastes time, pollutes the corpus,
    and erodes trust. If the math doesn't work, say so. If a
    derivation dead-ends, report the negative. If you don't know,
    say "I don't know." The user would rather see "this is open
    (bean `qou-XXXX`)" than a sorry-laden scaffold dressed up as a
    result. **Honesty is the only acceptable output.**
