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

2. **Queue, do not pivot.** When a new request, review comment, or
   sibling-PR ask arrives mid-session, **append** it to the plan in
   priority order — do not abandon the in-progress task. Pivot only
   when the user explicitly says so ("stop", "drop that", "switch
   to X first"). Inferred urgency is not enough.

3. **Parallelize independent tasks.** When two queued tasks have no
   dependency between them (e.g. one Lean fix + one .md edit on
   different blocks), batch them into a single response with
   parallel tool calls. Use background `Agent(run_in_background=true)`
   for independent research / triage that does not block the
   foreground task.

4. **Work the queue while idle.** When you are waiting on a
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
      `bun run content/pipeline/qa-sweep.ts <path> --only <crit>`
      (single canonical invocation; use `/integration-audit
      <axis>` to batch a whole axis). Witnesses are stale when
      `witness.scriptCommitSha` (producer file's `git log -1
      --format=%H -- <path>`) or `witness.scriptHash` (SHA-256
      prefix of producer file content) drift; refresh by
      re-running the producer with
      `2>&1 | tee /tmp/<script>.log` per the compute-audit
      long-compute logging discipline. Cap at ≤ 10 sidecars /
      ≤ 3 witnesses per idle pass. Every refresh that changes a
      sidecar or witness gets a `chore(qa-sweep|witness)` commit
      naming the producer + criterion + count. Full discipline:
      [`.claude/skills/local/integration-watcher.md
      §0b-idle-time-backlog-policy-5-minute-trigger`](.claude/skills/local/integration-watcher.md#0b-idle-time-backlog-policy-5-minute-trigger).
      This sits above cross-cutting cleanups because stale
      sidecars mislead all four watcher children's reads.
   5. **Cross-cutting cleanups** — bare-URL `-- Ref:` upgrades,
      `validate-bib` deferred items, glossary backfills, doc
      currency. Lowest priority because they're not gated on any
      in-flight work.

   "Substantive output" means: a new commit, a meaningful chat
   response (not a TICK ack), or a tool call that advances a
   queue item. If the only thing in the window is monitor TICKs
   and "pause-mode TICK" acks, you are idle and the trigger
   fires.

5. **Update the plan when upstream lands.** The session-start hook
   arms `local/watch` on `origin/main` (and `local/coordinate`
   triages sibling PRs). Whenever a `<github-webhook-activity>` or
   watcher event reports a new commit / PR / review comment that
   affects this branch, walk the §3 watch checklist; if the result
   is "queue work", insert the new todo at the right priority slot
   (do not push to the bottom blindly, do not jump above the
   current in-progress task unless it is a blocker).

6. **End-of-session: surface the plan.** If the session ends with
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
   - **Squash** when the branch's commits are noisy / WIP
     (e.g. a draft PR with many `wip` / `oops` commits that
     don't map to logical units). Prefer fixing the branch
     locally with `git rebase -i` instead, and rebase-merging
     the cleaned-up history.
   - **Create a merge commit** when the PR is a sub-merge of
     several already-merged sibling branches and the merge
     commit serves as a navigable boundary marker.

   The standing-authorization rule for ALWAYS-PR (above) applies
   here too: agents do not need to ask "which merge method?" each
   time — default to rebase-merge unless the branch history is
   noisy (see the **Squash** exception above; check `git log
   <merge-base>..HEAD --oneline` for `wip` / `oops` / `fix typo`
   patterns before committing to a method) or the user has
   explicitly said otherwise for the PR in question.

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

Only after **all four** grep paths return empty (modulo the
originating file itself) may you declare the item open. The source
file's `## Status`, `Open math`, or `Phase 3 open` notes are
**not authoritative**: the corpus is the source of truth.

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
family this session: `dc_3/dq ≈ 4.6e6` impossible for smooth real `f`
(kills the real-q c_3 family, [PR #1821](https://github.com/litlfred/qou/pull/1821));
the PSLQ entropy bound `precision > n_terms·log10(2·height)` (kills the
12-constant basis, [PR #1805](https://github.com/litlfred/qou/pull/1805));
A is ~4 sig figs from `c_2..c_10` (no high-precision identification
possible, [PR #1805](https://github.com/litlfred/qou/pull/1805)).
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

The QOU framework derives every observable (m_p, m_n, m_He, Q_β, B_AME, lifetimes) from **3 calibration inputs** — the canonical *mathematical* triple, **three measured masses**:

| CAL | Measured input | What it fixes | DOF of H¹(Bring) = 2W |
|-----|----------------|---------------|------------------------|
| CAL-1 | m_e | the dimensional unit (scale) | W-plane scale |
| CAL-2 | m_μ | q₀ (via m_μ/m_e = Vol(4₁)/ℏ_q²) | W-plane modulus |
| CAL-3 | m_π | the orthogonal meson scale | orthogonal class |

All three are the **three real DOF of the single H¹(Bring) = 2W** (rank-2 W-plane scale + modulus + one orthogonal class; 2+1=3) — **not** three distinct degrees H⁰/H¹/H² (per `calibration-cohomology-alignment`, Lean `QOU.Mass.calibrations_eq_cohomology`). The inputs are **three masses** (m_e, m_μ, m_π). m_e sets the unit; since q₀ is dimensionless it is fixed by m_μ *in that unit* — the ratio m_μ/m_e. The exact maps:

- **q₀** ← CAL-1 + CAL-2:  `m_μ/m_e = Vol(4₁)/ℏ_q²`, `ℏ_q = 1 − q₀⁻¹`, `Vol(4₁) = 2Λ(π/3) ≈ 2.0299`  ⇒ invert for `q₀ ≈ 1.10998`.
- **Q_β** (derived, not a calibration):  `Q_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³) ≈ 0.784 MeV` (0.17% vs CODATA) — the bar-odd `sinh` partner of the bar-even `cosh` meson scale m_π; the neutron β-decay width `𝔇_β/τ_n` is Q_β's experimental face, **not** a third calibration.

m_π (139.57 MeV) is genuinely independent of (m_e, q₀) (SDP-validated, Vol(Hopf)=0).

> **Two-layer convention (owner-clarified 2026-06-16).** The table above is the canonical *mathematical* calibration. In the **Physical-Observations** layer one may anchor q₀ on a *derived* quantity with smaller experimental error: live compute (`tools/qou-substrate/python/qou_substrate/constants.py::q_at`) pins q₀ on the **proton** ratio m_p/m_e (0.06 ppb vs the muon ratio's 22 ppb; re-pin 2026-05-28), making m_μ/m_e a 9.5σ cross-check prediction (the μ–p substrate tension). This precision substitution is **not** a change to the canonical CAL-2 and **not** a fourth calibration / second-q₀-pin.

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

> **⚠ Critical framing — the mass formula is `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`; do NOT reintroduce `λ_scale` OR the `Geom_full` wrapper.** Two standing purges: (1) the factor once called `λ_scale` was **absorbed** 2026-05-23 (commit `ffdd84409`) — not a separate constant to derive; (2) the opaque `Geom_full(K)` wrapper was **PURGED 2026-06-06** (owner directive, repeated — it obscured) in favour of its explicit meaning, the **volume–density product** `Vol(K)·ρ(K)/ℏ_q²`. So the per-knot mass is `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²` (electron scale × hyperbolic volume × per-block density). Compute uses `vol_density_borromean` / `vol_density_per_block` / `vol_density` (`_li_2_q_util.py`, `mass_vol_density.py`). The Yekutieli per-cell variant was tried then PURGED 2026-05-24 (`71d674da1`). The "2.89% m_p gap" is between the current categorical `Vol(𝓑₃)·ρ` value and its exact value — **not** a "λ_scale closure" problem. **Do not write `Geom_full` in paper, audit doc, or compute — write the explicit `Vol(K)·ρ(K)/ℏ_q²`.**

> **⚠ Critical framing — Q_β `c_k` is a TRUNCATION ORDER, not a wire/un-wire gate.** The Q_β precision ladder `Q_β = Q_base·Π(1 + c_k·u^k)` with `u = b·ℏ_q² ≈ 0.00852` is a **convergent series**; `N` is the truncation order chosen by target precision (`N ≥ log₁₀(1/ε)/2.07 − 1`). `c_2 = -1` is PROVED Taylor-exact; `c_k ≥ 3` are q₀-dependent NEAR-MATCHES (e.g. `c_3 = -2 = J_Hopf(q=1)` swings up to 3.47 % at m_p-pin q₀ (≈ 3 % cross-anchor)), with the N=4 → N=5 non-monotonicity as the experimental signature. Report TIERED (`proved` / `near-match` / `fitted`), never binary wired/dropped — the four-session wire/un-wire flip-flop (#1452 ↔ #1479) came from conflating "N=3 beats 100× experimental" (true) with "c_3 = -2 is Taylor-exact" (false). **Canonical reference (read before any `c_k` wire/un-wire decision): [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).** Permanent fix is the Q_β Habiro element (parallel α_EM `[2]_q·(1−h²α)` in PR #1511). **2026-05-31 c_3 SETTLED** (PR #1580 verdict audit + flip-flop history table now at 6 entries in [`docs/coordination/1ppq-qbeta.md`](docs/coordination/1ppq-qbeta.md)); Li_2^q × spectral combiner refuted as mech #7 (PR #1609); Δtr_M bar-decomposition recorded as structural observation (PR #1615) — none of these wire to production.

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
| **L2. Per-observable accuracy** | for each predicted observable O: `σ_pred(O) ≤ σ_exp(O) / 100` | 3/7 met (m_p, m_e, m_K/m_π) — see `per-observable-100x-status.witness.json` (fresh run 2026-05-31); the 4 missing observables (m_μ, Q_β, m_n, Δ_pn) — note **m_μ misses by 963.6× post-re-pin**, see below — and the Q_β/m_n/Δ_pn trio share a single root cause documented in [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md) |

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
  (… m_μ …)"; that was stale (the q0-repin staleness class). The
  authoritative count is **3/7**, verified by a fresh
  `per_observable_100x_status.py` run on 2026-05-31.
- **"1 ppQ" by itself is ambiguous** — say "L1 compute met" or
  "L2 met for observable X" not bare "1 ppQ".
- **1 ppQ** = 1 part per quadrillion = 10⁻¹⁵ relative = 10⁻⁶ ppb.
  Upgraded from 1 ppb (2026-05-26) because the old target was noise.

**Two subgoals under L2:**

- **Subgoal-1 (achievable):** 100× targets ≥ ~780 ppb CAL-2 floor.
  Closure path: per-isotope Borromean-tower extension + operator-
  valued branching combiner.
- **Subgoal-2 (research-grade, out of scope):** 100× targets <
  CAL-2 floor (absolute m_p / m_n / m_⁴He). Requires substrate-
  derivation of q_0, which the coordination ledger explicitly
  declined on 2026-05-08. Do **not** attempt without owner reversal.
  - **Narrow owner reversal (2026-06-19, recorded 2026-06-22; PRs #2503 /
    #2524).** The owner reversed this decline **only for the s5-so3 keystone
    geometric-realization construction** — the differential-geometry /
    WRT(S³/2I) build of the `W_λ` index (see
    [`docs/coordination/s5-so3-keystone.md`](docs/coordination/s5-so3-keystone.md)).
    That specific geometric `W_λ` build is **in scope**. The reversal is
    narrow: it does **not** reopen fit-based q_0 derivation, and the `Δ_λ`
    "no seventh fit-based ansatz" rule below **still stands**; any other
    Subgoal-2 work still needs explicit owner sign-off.

**Δ_λ gate (Track A blocker).** The per-isotope binding-energy
formula `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ` requires per-partition Δ_λ
values, and six closure ansätze (Frobenius co-Casimir, Demazure-
fibre, LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov)
have all failed on the deuteron. **Do not propose a seventh fit-
based ansatz** — the three-calibration discipline review will catch
it. The productive directions are GAP-A-3 / GAP-A-4 (categorical
brane-tower level selection / ρ general rule) and Option E **via the
A=4 interface operator (PROBE 2)** + `conj:s5-so3-fiber-action`.
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
| "uploads/ status / what's pending" | `local/document-intake` | collaborator |
| "critical path / trace dependencies" | `local/critical-path-analysis` | collaborator |
| "archimedean vs categorical / context audit" | `local/critical-path-analysis` | reader |
| "what assumptions does X need" | `local/critical-path-analysis` | reader |
| "separate categorical / split statement" | `local/critical-path-analysis` + `local/content-validation` | collaborator |
| "simulator / simulation / interactive viz" | `local/simulator` + `local/content-validation` | collaborator |
| "set up lean / install lean / lean not working" | `local/lean-environment-setup` | collaborator |
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
| "QA report / .qa.json / multi-reviewer / hash staleness / per-block audit sidecar" | `content/pipeline/qa-sweep.ts` + `qa-staleness.ts` (CLI), `folio-assistant/schemas/block-qa.ts` (schema) | collaborator |
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
| `reader` | editor, content-validation, latex-validation, scientific-accuracy, readability-editing, proof-status-tracking, proof-gap-audit, todo-review, docs-generation, diff, watch, chapter-complexity-review, verify-local-substrate, remark-audit, rendering-auditor, rendering-fixes, markdown-render-check, witnessed-values, proof-integration-watcher, canonical-watcher, detangler-integration-watcher, production-vs-exploratory-discipline, proposition-consolidation-audit, q-usage-watcher, symbiotic-interaction |
| `collaborator` | All reader skills + formalizer, category-theory, lean-generation, lean-proof-review, lean-build-fix, lean-completeness-audit, lean-substantive-pass, proof-triage, proof-simplifier, proof-editor, proof-exposition-review, proof-narrative-lean-equivalence, proof-conciseness, chapter-analysis, content-block-review, ontologist, paper-importer, document-intake, test-engineer, lean-environment-setup, simulator, one-voice-audit, compute-audit, compute-author, coordinate, compute-integration-watcher, ffi-roundtrip-audit |
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
lake build           # build every paper package
lake build QOU       # single paper library
lake exe cache get   # fetch Mathlib cache for the workspace
```

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
  (`references.bib` is auto-generated — run `bun run export-bibtex` in `content/`).
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
(`content/pipeline/conjectural-propagation-audit.ts`) reports such
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
| `content/pipeline/validate.ts` | Three-level validation |
| `content/pipeline/render-latex.ts` | Block → LaTeX + AST validation |
| `content/pipeline/build.ts` | Full document build |
| `content/schema/references.ts` | **Bibliography source of truth** (CSL-JSON) |
| `content/pipeline/export-bibtex.ts` | Generates `references.bib` from CSL-JSON |
| `content/pipeline/validate-references.ts` | Bibliography + citation cross-checks |
| `content/pipeline/citations.ts` | `\cite{}` extraction from .md content |
| `content/pipeline/find-dangling-remarks.ts` | Audit: find remarks without `interprets` |

### Bibliography architecture

The bibliography is managed as **typed CSL-JSON** in
`content/schema/references.ts`. BibTeX (`references.bib`) is a downstream
render target, auto-generated by `bun run export-bibtex`.

- **Adding a reference**: use the `ref()` builder in `references.ts`
- **Block citations**: `cites: string[]` field on blocks (auto-extracted
  from `\cite{}` in .md by the pipeline, or set explicitly in .ts)
- **Chapter bibliography**: aggregated at build time from all block cites
- **Validation**: `bun run validate-refs` checks schema, uniqueness, DOIs,
  and cross-references against Lean `-- Ref:` and LaTeX `\cite{}`
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
  && tar xzf "$TGZ" -C "$ROOT" && echo "restored from lake-cache/qou-$SLUG — skip Steps 1–3"

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
| `content/pipeline/` | Validation, rendering, build pipelines |
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
| `qou-mass/` | `qou-mass` PyPI package — external-researcher facade (`predict()`, `compute_tr_M()`, `canonical_braid()`). Alpha (`v0.1.0a1`); 1 in-repo importer (the canonical wiring example `computations/qou_mass_canonical_wiring_example.py`). |
| `tools/qou-substrate/` | `qou-substrate` PyPI package — Layer 2a (q₀, mpmath precision, `WitnessBuilder`). 7 in-repo direct importers (≈67 % transitive via `pyhecke`). |
| `tools/pyhecke/` | `pyhecke` PyPI package — Layer 2b (Hecke / Gram / Markov trace). 19 in-repo direct importers. |
| `tools/pyhecke-native/` | `pyhecke-native` PyPI wheel — PyO3 bindings into `hecke-engine`. 15 in-repo direct importers. |
| `tools/witness-schema/` | `witness-schema` PyPI + `@litlfred/witness-schema` npm — cross-language `*.witness.json` interchange schemas. 1 in-repo importer (same canonical wiring example). |
| `tools/block-qa-schema/` | Cross-language QA-sidecar interchange schemas (`<block>.qa.json` block-qa/v1 + `<criterion-id>.script.json` qa-script/v1): canonical JSON Schema + Zod + Pydantic mirrors, corpus-validated. Packaged for npm (`@litlfred/block-qa-schema`) + PyPI (`block-qa-schema`); not yet published to registries. Producing types: `folio-assistant/schemas/block-qa.ts`. |
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
| `uploads/` | Document intake pipeline (raw PDFs, scans, WHO guidelines → content objects) |
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
