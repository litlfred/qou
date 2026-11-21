# Claude Code — Quantum Observable Universe

## CRITICAL: READ SKILLS BEFORE ACTING (Anti-Guessing Rule)

**DO NOT GUESS WORKFLOWS.** This repository has highly customized, non-standard workflows for building Lean, preparing merges, syncing with siblings, and validating. 
When the user asks you to perform a task (e.g., "run prepare-merge", "set up lean", "audit compute"), **you MUST FIRST read the corresponding skill file in `.claude/skills/local/*.md`** before taking any action.

**Why this is strictly enforced:** Agents frequently fail in this repository by running standard commands (like `lake build` from scratch) instead of following the explicit repo skills (which use custom caches and scripts). This wastes the user's time.

**Required Action:** Before executing any multi-step task or slash command, run `ls .claude/skills/local/` and `view_file` on the relevant `.md` file. Follow its instructions exactly. NEVER guess.

## 🟥 THE PHOTON IS `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (owner ruling 2026-11-20) — STRICT

**The fourth term is the chiral vertex `σ₀σ₁⁻¹`. The form with `σ₀σ₁` (`L₊`) as the
fourth term is OLD AND WRONG.** Verbatim, owner 2026-11-20: *"1 + φ₀σ₀ + φ₁σ₁ +
φ₀₁σ₀σ₁ is old and wrong. 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁^-1 is correct"*, and earlier the
same day: *"That was already decided. Why did it get changed back to the wrong form?"*

    γ(φ₀, φ₁, φ₀₁) = 1 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹      ∈ H₃(R, q)

- **This is a ruling, not a working assumption.** It was first recorded on
  2026-11-18 as "a working assumption, not a ruling to edit def:photon"; that
  classification was the recording agent's, and it is why the wrong form kept
  coming back (bean `qou-99qc`, entry 2026-11-20T14:50:40Z).
- **`def:photon` (`knots-particles-confinement/photon.md`) and `QOU/Photon.lean` state the
  correct form as of PR #8583 (merged 2026-11-20).** Copies of the old `σ₀σ₁` form
  survive in older branches, beans, audits and probes: do not copy from them, and do
  not quote, compute, formalise or propose anything on the `σ₀σ₁` form. Do not call
  the correct form "switched", "γ′" or "the qou-99qc variant" — it is simply *the
  photon*.
- **Every agent repeats this to its subagents.** A subagent does not see this file
  if it was edited mid-session (see §Subagents); put the photon form in the
  subagent's prompt whenever photons are in scope.
- Worked consequence: the Borromean core factors as
  `V³ = (σ₀σ₁⁻¹)³ = γ(0,0,qh)·γ(0,0,−q⁻¹h)`, `h = q − q⁻¹`
  (`borromeanV3A_eq_switched_photon_product` and its `B` twin, sorry-free).

## User accessibility

The repo owner is physically disabled and types with difficulty.
Adapt ALL responses accordingly:
- **Short answers.** One-liners when possible — but read this together
  with **Terse ≠ compressed** below: "short" cuts ceremony, never
  evidence, implications, or options.
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
- **Write the question for someone who was NOT in your session (STRICT, 2026-08-24).**
  The rule above says *what* to include. This one governs *how it reads*, and it
  exists because the failure is systematic: an agent that has spent an hour
  inside one problem asks its question in the private vocabulary it built along
  the way. The author then has to reconstruct the agent's rabbit hole before
  they can answer a question that should have been answerable on its own.

  Assume the author has read **none** of your session. Before asking, apply all
  six:

  1. **Expand every identifier on first use.** Not `qou-cds2`, `y0_star`,
     `G_PINV`, `the 8 stubs` — instead "bean `qou-cds2` (the convention-D Gram
     singularity)", "`y0_star`, the shadow price of the LP's net constraint",
     "eight witness files that carry LP-dual field *names* with `null` values".
     A bean ID, a witness stem, a field name and a Lean declaration are all
     opaque without their gloss. If a term needs a definition, give it inline —
     do not link to one.
  2. **Lead with the decision, not the investigation.** One or two sentences:
     what is being decided, and why it needs the author rather than the agent.
     The narrative of how you got there goes *below* the options, or is omitted.
     The author is choosing a future action, not grading your search.
  3. **Mirror the structure.** The chat context must be laid out to match the
     questions being asked: one clearly-headed section per question, and within
     it one sub-block per option, in the same order and with the same labels as
     the structured call. The author should be able to read one option's block
     and answer without holding the others in their head. Do not write a long
     shared preamble that all the options depend on.
  4. **Give every option the same four-part frame**, so options are comparable
     rather than merely listed:
     - **What it means** — in plain language, no repo jargon.
     - **What it costs** — concrete: files touched, producers re-run, hours,
       whether a long compute is involved.
     - **What it risks** — what could break, how reversible it is, what numbers
       could move and who reads them.
     - **What it commits to** — what this forecloses or obliges later.
  5. **State the default.** What happens if the author says nothing, or picks
     none of the above? Name it explicitly ("nothing changes; the eight stay as
     they are and the audit keeps reporting them"). An author who knows the
     no-op is safe can defer with confidence.
  6. **Name the blast radius in real terms.** Not "three consumers" but
     "`bound_state_observable_validator.py`, `audit_frobenius_pairing.py` and
     `delta_lambda_master_formula_h3_probe.py` read this field; the last one
     feeds the Δ_λ master-formula probe." The author needs to know what breaks
     in terms of the *physics or the paper*, not the call graph.

  **Give a recommendation.** Say which option you would take and why, in one
  sentence, and mark it clearly as your judgement rather than a finding. An
  author overruling a stated recommendation is cheaper than an author
  reverse-engineering the agent's preference from a neutral list.

  **When you cannot make an option legible without a paragraph of background,
  that is a signal the question is premature** — go do the measurement that
  would collapse the option space, and ask a smaller question afterwards.

  History: added 2026-08-24 on owner instruction, after a question offered
  three options ("populate, needing a real LP per producer, or drop the names")
  whose meaning, cost and consequences were legible only to the agent that had
  just spent the session measuring them.

- **NAMING A DECISION IS ASKING A QUESTION — the frame above applies wherever
  you raise one, not only in `AskUserQuestion` (STRICT, 2026-08-29).**

  Every rule above says "`AskUserQuestion`", and an agent reads that as a rule
  about a *tool*. It is not. It is a rule about **handing the author a
  decision**, and the tool is one of several ways to do that. The others, all
  of which carry the same obligation:

  - an end-of-turn summary line ("the one thing waiting on you is …");
  - a `**next**` entry in the beans report;
  - a "Suggested follow-up" / "open question" section in a PR body;
  - a bean body's "still open" list;
  - a chat sentence of the form *"X is a judgement call for you"*.

  **The test is not which tool you used. It is: does this sentence require the
  author to decide something?** If yes, it owes the six-part frame — expand
  every identifier, lead with the decision, give each option its what-it-means
  / costs / risks / commits-to, state the default, name the blast radius in
  real terms — and a recommendation marked as judgement.

  **The failure mode is specifically the one-line gesture.** *"Whether the mass
  context should move to `tower_term_li2q` is a judgement about the framework"*
  names a decision and supplies none of what is needed to make it: not what the
  two options do, not that the calibration has **zero non-probe consumers**
  (which is what makes it cheap), not what happens if the author says nothing.
  The author cannot act on it, and worse, cannot tell that it is cheap to
  ignore. That is not a hand-off; it is a mention.

  **Cheapest correct move when you do not want to spend the words:** don't
  raise it. A decision you are not prepared to frame is a decision you should
  either measure further yourself or leave in the bean unmentioned — a bean the
  author can read on their own schedule is a fine home for an unframed
  question. What is not fine is putting it in front of them stripped of
  everything that would let them answer.

  History: added 2026-08-29 on owner instruction — *"Named decision, but I
  haven't described any information about it. This is a repeated habit of
  yours."* The agent had applied the six-part frame diligently inside
  `AskUserQuestion` calls all session while ending turn after turn with bare
  one-line decision gestures, because every rule it had was addressed to the
  tool rather than to the act.

- **Terse ≠ compressed: "short" governs ceremony, never content (STRICT,
  2026-08-25).** The *Short answers* rule at the top of this section is about
  **the author's typing cost**, not about how much of what you measured reaches
  them. Agents read it as licence to compress a finding into a headline and drop
  the evidence, the implications and the options — and the author then has to
  spend keystrokes asking for material the agent was already holding. In a repo
  whose owner types with difficulty, **that round-trip is the single most
  expensive failure mode there is.** A one-line answer that triggers three
  follow-up questions cost four messages; the three-paragraph answer costs one.

  **What "short" legitimately cuts** — cut all of it, always:

  - preamble, restating the request back, narrating what you are about to do;
  - status theatre, apologies, self-criticism, hedging, "great question";
  - options you have already decided not to pursue;
  - re-derivation of facts already established earlier in the session.

  **What it must NEVER cut.** Every substantive report carries the same
  four-part frame the `AskUserQuestion` rules above demand — because a finding
  and a question need the same scaffolding to be actionable:

  - **The claim**, stated flatly, with its number. Not "the tolerance moved" —
    `1.9177226708e-06 → 1.9177218447e-06, rel 4.31e-7`.
  - **The evidence.** File path and line, the exact command run, the value
    *before* as well as after, the sample size, and whether the figure was
    measured this session or carried from a prior one.
  - **The implications** — what this changes for the corpus, the paper or the
    next agent, in physics-and-paper terms rather than call-graph terms. Name
    the consumers by file, and say which of them feeds something a reader sees.
  - **The options**, each with cost / risk / what it forecloses, plus **a stated
    recommendation marked as your judgement** rather than as a finding. Include
    the no-op and say what happens if the author does nothing.

  **Two triggers where terseness is always a defect**, because the compressed
  form is not merely thin but *misleading*:

  1. **Correcting your own earlier claim.** Say what you asserted, what is
     actually true, how the new figure was measured, and — the part that gets
     dropped — **what else that error may have contaminated**: which beans, PR
     bodies, audit docs or content blocks repeated it. A bare "corrected" is
     unusable, and this corpus has repeatedly had a wrong figure survive in five
     other places after being fixed in one.
  2. **Any negative or absence-of-evidence result.** *"I found no rationale in
     the source"* and *"there is no rationale"* are different claims and only
     one of them was measured. Say which, name the surface you searched, and say
     what observation would separate them. Absence of a comment is not evidence
     of absence of a reason — and a *measurement* you already have outranks the
     silence of a source file.

  **This applies to chat, commit messages, PR bodies and bean updates alike.**
  The chat is ephemeral; the commit and the PR are what a reviewer and the next
  agent read cold. A commit message that says "migrate X" over a change whose
  whole point is that the previous recommendation was backwards is the same
  defect as the terse chat answer, with a longer half-life.

  History: added 2026-08-25 on owner instruction — *"you are as USUAL too terse
  (PLEASE update Agents.md linked directives)"* — after an agent reported that
  `aoperator_a5_crosscheck` (a probe cross-checking the A-operator at A=5)
  "carries no muon rationale in its source" and stopped there, in a session that
  had **already measured** that the producer's own assertions FAIL at the muon
  anchor and PASS at the proton one. The absent comment and the present
  measurement are not the same evidence, and only the weaker one was reported.

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

## The paper is a MATHEMATICAL MODEL by default (owner ruling, 2026-08-07)

**Every object in this paper is a mathematical object unless it is being compared
to measurement.** This is the default reading for readers and agents alike, and it
governs how claims should be stated, criticised, and defended.

- **Named terms are model terms.** `electron`, `proton`, `neutron`, `mass`,
  `binding energy`, `decay width` are *names of constructions inside the model* —
  `m_e` is a defined quantity in the framework, not an assertion about the physical
  electron. Naming a construction after a particle is expository convention, exactly
  as a topologist calls a knot "the trefoil".
- **Physics enters only at the comparison boundary.** The empirical content of the
  framework is located precisely where a model quantity is set against an
  experimental one — AME2020, CODATA, PDG. Those comparisons are the physical
  claims. Everything upstream of them is mathematics.
- **Therefore an incomplete physical derivation is not a reason to abandon the
  physics.** A mathematical model with an honest empirical-comparison section is a
  legitimate object, and the work must stand up in a **physics** venue as well as a
  mathematics one. Do **not** propose "split the math off and drop the physics" as a
  resolution to a derivation gap — the owner has ruled against that framing.

### What this does NOT license

The ruling narrows where the physical claims live; it does not weaken them.

- **The comparison points carry the full burden.** Because physics enters *only*
  at comparison, the honesty of the comparison is the whole empirical case. A
  systematic that moves a compared quantity is therefore *more* consequential under
  this framing, not less — it is attacking the one place the physics lives.
- **"It's just a model term" is not a defence of a wrong number.** If `m_p` in the
  model is compared to CODATA `m_p`, the comparison is a physical claim and is
  judged as one.
- **The anti-fit discipline is untouched.** A fitted quantity is still a fit whether
  its name is mathematical or physical.

Practical consequence for agents: when writing or reviewing, keep the register
straight — state model results as mathematics, and mark the comparison points
explicitly as where the empirical claim is being made. When criticising, aim at the
comparisons and at the systematics on them, not at the naming.

## 🟥 NO FITTING, EXCEPT CAL-1/2/3 (owner directive, 2026-09-05) — STRICT

**This is a mathematics paper, not a physics paper.** The deliverable is a
*process* and a *derivation*. The owner is building a model in order to iterate
it toward physics, and **that iteration is impossible if anything is fitted**: a
fitted model cannot be wrong in a way you can learn from, because it has already
absorbed the discrepancy that would have taught you something.

**The only admissible calibration is CAL-1/2/3** (the decay-width triple, table
below). Everything else must be *derived*. There is no fourth constant, no
"one small tuned factor", no "we only picked the cutoff".

### What counts as fitting — including the kinds agents keep missing

Continuous parameters are the obvious case and are rarely the problem. These
are the ones that recur:

- **Selection against the target.** Choosing an *object* — a knot from a census,
  a partition, a truncation order, a branch — because the choice reproduces the
  measured value. No continuous parameter is tuned and it is still a fit. The
  giveaway is a gap where no object matched: see the 2026-09-05 retirement of
  the census route, where `A ∈ {5,6,7}` had no prediction precisely because "no
  census knot/link with `Vol ≈ B_AME/m_e` yet found".
- **Sweeping a discrete parameter for accuracy.** "Empirical sweep shows `K = 6`
  is the OPTIMAL cutoff" is a fitted parameter. Optimal against what? The data.
- **Per-case dispatch.** A formula that branches on `A` (or on species, or on
  regime) with a different expression per branch has one free choice per branch.
- **Importing an empirical term.** Citing a phenomenological formula from the
  literature (an empirical Wigner energy, an SEMF coefficient) imports somebody
  else's fit.
- **A tolerance sized to its own miss.** Already flagged in
  `unified-iterative-correction-proof`: "A bound sized to its own miss is a fit."

### The ranking rule agents get backwards

**Accuracy is not evidence of correctness here, and a more accurate fitted route
is worth LESS than a less accurate derived one.** A 5.87 % miss obtained by
selecting a knot whose volume matches is weaker than a 69 % miss obtained by
computing, because only the second one can be iterated. When comparing routes,
rank by *derivational cleanliness first*, and treat accuracy as a diagnostic —
never as a tie-breaker that promotes a fitted route.

Corollary: **do not recommend consolidating onto the most accurate route.** Ask
first what each route derives and what it selects.

### What to do instead

- If a derivation is specified but not implemented, **implement the
  specification**, and report what it gives even when that is worse. A
  documented honest miss is a result; the corpus's negatives are its most
  reusable output.
- If you cannot derive a quantity, say so and leave the gap visible. A gap is
  information. A filled gap with a chosen constant is not.
- If you catch yourself reaching for a route because its numbers are better,
  that is the moment to stop and say so in the report.


## 🟥 ASK THE OWNER BEFORE CHANGING THINGS (owner directive, 2026-09-07) — STRICT

**This OVERRIDES the standing excise / sweep / drain / migrate authorisations
throughout this document.** Verbatim: *"OVERRIDE / excise guidance.... new
guidance = ask owner for changes (if changes are not increasing precision /
derived from corpus)"*.

**Default: ask first.** An agent may no longer start a corpus-wide excision,
sweep, drain, migration, rename tranche or refactor on the strength of a
directive written here. Those passages record what the owner *wanted at the
time*; they are not standing permission to begin one now. Put the change to the
owner with its measured blast radius and wait.

### The two exemptions, and they are narrow

A change proceeds without asking only if it is one of:

1. **It increases precision.** Removing a float64 path, carrying `mpf` further
   up the call chain, replacing a hardcoded literal with a derived value,
   raising `mp.dps` where it was silently truncating. The test is that the
   change makes a number *more* correct or makes a wrong number *impossible* —
   not that it tidies something near a number.
2. **It is derived from the corpus.** The corpus already fixes the answer and
   you are making the code agree with it: the file's own docstring names the
   quantity, a notation-register table publishes the value, a sorry-free Lean
   theorem states the identity, or a producer's own convention is declared and
   violated one line down. The test is that you can point at the corpus
   artifact that decides it, and that a reviewer could check your work against
   that artifact rather than against your reasoning.

Everything else asks. Notably **not** exempt: consolidating onto a "better"
route, tidying an inconsistency, mass-refreshing witnesses or sidecars,
regenerating a derived artifact that belongs to someone else's arc, or applying
a rule from this document across files you were not sent to.

### Why the exemptions are shaped this way

Both are things a reviewer can verify **without reconstructing the agent's
session**. A precision fix is checkable by running the gate; a corpus-derived
fix is checkable by opening the artifact it cites. Everything outside them
requires trusting the agent's judgement about what *should* change, and that is
the owner's call in a mathematics repository.

### Worked example, the same day

`q_int_at` / `q_int_classical_at` were added to
`qou_substrate/constants.py` with **float64 fallbacks** in the no-mpmath branch.
Excising them is exemption 1 (it removes a float64 path) *and* exemption 2 (the
file's other four fallbacks all `raise`, so the corpus already fixed the
convention) — so it proceeded without asking. Rewriting the *other* 29
classical-convention files found by the same audit does **not** qualify: it needs
a per-file basis determination, and it waits.

### Interaction with the rest of this document

- The **ALWAYS-PR** authorisation (branch, commit, push, open the PR) is
  unaffected — that is about visibility, not about changing content.
- **Run commands proactively** is unaffected. Measuring is not changing.
- The **anti-fit**, **anti-laundering** and **NO-FLOAT64** disciplines are
  unaffected and still bind; this rule adds a gate, it removes none.
- When in doubt, **measure it, report the blast radius, and ask.** A measurement
  the owner did not want costs a few minutes; a sweep they did not want costs a
  review cycle and can bury a real finding under a thousand mechanical diffs.

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

## Subagents with persistent memory (`.claude/agents/`)

Five subagents are defined under [`.claude/agents/`](.claude/agents/), each
carrying `memory: project` in its frontmatter. That gives the agent its own
directory under `.claude/agent-memory/<agent-name>/`, which it reads and writes
as it works.

> **🛑 THE INJECTION DOES NOT HAPPEN IN THIS ENVIRONMENT — measured
> 2026-09-03.** This paragraph used to state, as fact, that *"the first 200
> lines (or 25 KB) of that directory's `MEMORY.md` are injected into the
> subagent's system prompt when it starts."* **For subagents launched via the
> Agent tool in a Claude Code remote session, nothing is injected — not a
> truncated 200 lines, none of it.**
>
> Measured by asking two agents, independently, what their own system prompt
> contained: `lean-verifier` and `corpus-grepper` both reported **zero**
> `MEMORY.md` content. Objective corroboration, checkable without trusting a
> self-report: **four "see memory" / "see the memory entry" cross-references in
> three agent definitions are dangling pointers** — they reference content that
> never arrives. The frontmatter is correct (`memory: project` on all five) and
> the files exist, so this is a harness behaviour, not a misconfiguration; it
> may well work in the desktop or CLI harness, and this is a statement about
> **this** environment only.
>
> **Consequence for the 200-line cap.** The cap is now a *convention*, not a
> live constraint — nothing is being truncated because nothing is being sent.
> Keep files under it anyway (it bounds what an agent must read), but do not
> treat "under 200" as evidence an agent has the content.
>
> **The repair, and 🛑 it is UNVERIFIED — do not assume it works.** Each
> agent definition now opens with a `## FIRST ACTION — read your memory; it is
> NOT injected here` section telling the agent to `Read` its own `MEMORY.md`
> first, and to open its report with a compliance line naming the files read,
> `MEMORY.md`'s line count and its last commit sha — so a reader can tell a
> memory-informed run from a memory-less one instead of taking it on trust.
> **A report without that line should be presumed to have run without memory.**
>
> **But a third agent, launched AFTER that edit, did not receive it** — it
> quoted its own prompt going straight from the preceding bullet to `## What
> you do`, with no `## FIRST ACTION` section, while the section was plainly on
> disk. So agent definitions appear to be **snapshotted** (committed `HEAD`, or
> cached at session start), and an uncommitted edit to one does not reach a
> subagent in the same session. The fix may take effect once committed and a
> fresh session starts; that has **not** been demonstrated.
>
> **🛑 AND I WAS WRONG ABOUT THE CARRIER — corrected the same hour.** This
> paragraph first said *"this AGENTS.md note is the load-bearing carrier … it
> provably arrives in subagent prompts in full"*. It does arrive in full, but
> **the version that arrives is snapshotted at session start**: a
> `convention-auditor` launched minutes after this very edit was committed
> still received the *pre-edit* text, uncaveated. So a mid-session edit to
> `AGENTS.md` reaches no subagent either — **the same failure as the agent
> definitions, through a different file.**
>
> Three causes remain consistent with that single observation and it does not
> separate them: session-start snapshotting, a cached/differently-rooted copy,
> or an edit at a path other than the one `CLAUDE.md` `@`-includes. Snapshotting
> is the leading candidate only because definitions failed the same way.
> **The discriminator is a genuinely new top-level session**, not another
> subagent.
>
> **The practical rule, which holds whatever the cause:** nothing you write to
> `AGENTS.md` or to an agent definition reaches a subagent **in the session you
> write it**. If a subagent must know something you learned this session, **put
> it in that subagent's prompt** — that is the only channel demonstrated to
> work today. Everything here is for *later* sessions.
>
> So if you are a subagent reading this in a later session: **read
> `.claude/agent-memory/<your-name>/MEMORY.md` yourself before you start**,
> whatever your own definition does or does not say.
>
> **A figure to not repeat.** The first version of the agent-definition block
> quoted "2,520 lines across 16 files" — that is the *whole tree across all
> five agents*. Per agent it is **195–419 lines** for `MEMORY.md` and 412–657
> for the directory, i.e. ~3-7k tokens: cheap. Quoting the tree total in each
> agent's own file overstates its burden ~6× and invites exactly the wrong
> trade-off (skipping the read). Caught by the consuming agent, not by me.
>
> Tracked in bean `qou-rpgi`.
>
> **So "maintaining them is part of the work" below still holds** — the files
> are read, just deliberately rather than automatically.

| agent | owns |
|---|---|
| `lean-verifier` | olean cache restore, `lean`-direct verification, sorry/axiom status |
| `corpus-grepper` | the six-path checklist before anything is declared open / refuted |
| `compute-precision-auditor` | the NO-FLOAT64 gate family, witness staleness, producer health |
| `convention-auditor` | convention C vs D, the muon/proton q₀ pin, Λ vs Cl₂, layer straddles |
| `merge-coordinator` | branch/PR policy, sibling coordination, drive-to-green |

The point is the failure mode this document is itself a record of: an agent
spends a session measuring something, writes the number down, and the number
is quoted months later as though it were current. **Memory does not fix that
by holding better numbers — it fixes it by holding methods.** Each `MEMORY.md`
labels every entry as exactly one of:

- **STABLE** — a path, a command, a ruling, a structural fact. Trustworthy;
  verify cheaply if surprising.
- **TRAP** — a specific way the task goes wrong, with the evidence that
  established it. Durable, and the highest-value entry type.
- **BASELINE** — a measured number, stored **with the command that produced it
  and the date, and never quoted as a current answer.** A baseline tells the
  agent what to measure and how; re-run it, report fresh, then update the
  entry.

**Maintaining them is part of the work.** When a session establishes a durable
fact in one of these areas — a detector blind spot, a producer that refuses by
design, a gate that cannot fire — add it to the relevant `MEMORY.md` as a TRAP
in the same PR. When a session re-measures a BASELINE, update the entry with
the fresh number and date. A memory file that only accretes becomes the thing
it exists to prevent.

Two mechanical notes. `MEMORY.md` is the entry point an agent reads first
(**not** injected — see the block above), so keep it
under 200 lines — split detail into sibling files the agent reads on demand
(`compute-precision-auditor/producer-health.md` is the worked example). And
`memory: project` writes under `.claude/agent-memory/`, which is **committed**;
`memory: local` writes under `.claude/agent-memory-local/`, which is
gitignored, for anything genuinely per-machine.

The agents defer to `.claude/skills/local/*.md` as the source of truth on
procedure. Memory summarises; the skill governs. Where the two disagree, the
skill wins and the memory entry is wrong — fix it.

## Agent work-plan policy (STRICT)

Every session must run from a **prioritized work-plan** maintained
as **beans** — the [`beans`](https://github.com/hmans/beans) CLI
flat-file issue tracker (data under `beans/defs/`; install via
[`scripts/install-beans.sh`](scripts/install-beans.sh)). See
[`.claude/skills/local/todo-manager.md`](.claude/skills/local/todo-manager.md)
and [`.claude/skills/local/bean-coordination.md`](.claude/skills/local/bean-coordination.md).
The plan is the agent's source of truth for "what next" — not the
user's last message, not the most recently mentioned file.

> **🟧 BEANS ARE BRANCH-MOUNTED, NOT ON MAIN (owner ruling 2026-10-10,
> re-confirmed 2026-11-15; issue #7642).** `beans/` (`beans.json` + `defs/`)
> lives on the branch `cat/cat-harness/beans`, declared in `qou.json` as
> `source: {kind: branch, keyedBy: tip}`, and is gitignored on main. The
> SessionStart hook (`scripts/mount-fsh-guts.sh`) installs a light subset of
> the platform if it is absent (`scripts/mount-platform-lite.sh`: about 20 s,
> 165 MB, against 1.7 GB for the full setup) and mounts `beans/` with
> `state:mount`. Note `branch-store.ts push` has no `--dry-run`: an unknown
> flag is ignored and the push happens. There is **no read-only
> fallback** (owner, 2026-11-15). By hand:
> `./scripts/mount-platform-lite.sh && bun folio-assistant/cat-harness-tools/scripts/state-mount.ts`.
> The `beans` CLI works on the mount unchanged, because `.beans.yml` still says
> `path: beans/defs`. **A bean edit is no longer a commit in your PR.** Push it
> back with `bun folio-assistant/cat-harness-tools/scripts/branch-store.ts push
> --id beans`. That is a splice with `expect`; it never forces, and two writers
> of one file get `conflict`, so re-read and retry. The CLI never pushes, so an
> edit you have not pushed is lost when the container goes. If the mount
> failed, an empty `beans list` means the work plan is **unreachable**, not
> that there is no work. Every `beans/defs/...` path below names a file in the
> mount.

> **Migration note (2026-06-19).** Beans **supersede** the older
> `TodoWrite`-tool / `todos/*.json` work-plan mechanism. Wherever this
> document still says *"TodoWrite list"* / *"todo list"* below, read it
> as *"create / maintain beans"* (`beans create "<title>" --type task`,
> `beans update <id> --status in-progress|completed`). The
> `beans ≠ sidecars` rule holds: QA / `.qa.json` / `.witness.json`
> queues are **not** converted into beans. (Part of the qou side of
> the Folio-Assistant Infrastructure Migration — the `miga` epic.)

> **A bean is an APPEND-ONLY ledger, and concurrent appends collide on
> essentially every landing (measured 2026-09-13).** *(Since the beans
> branch mount (issue #7642), beans are no longer merged through PRs, so the
> merge-time collision below no longer happens on `main`. A concurrent write
> now surfaces as `conflict` from `branch-store.ts push --id beans`. The record
> below is kept as history, and `bean-append-merge.py` is only for a branch
> cut before the mount.)* `main` takes **169
> commits / 24 h**; `beans/defs/qou-brng--…` is touched by **9** of them and
> `beans/defs/qou-zlra--…` by **6**, so a branch that appends to `qou-brng`
> goes un-mergeable roughly **every 2.7 h**. In the #7237 / #7245 /
> #7251 / #7253 cluster, **four of the five collision surfaces were
> these two files** — no content, no Lean, no compute — and `qou-brng`
> conflicted three times in about forty minutes, twice while the
> previous resolution was being committed. Clearing them ahead of merge
> is not winnable by hand; resolve **at merge time** with
> [`scripts/bean-append-merge.py`](scripts/bean-append-merge.py), which
> keeps `main` byte-for-byte, appends the branch's note verbatim, takes
> the later `updated_at`, and asserts `len(merged) == len(main) +
> len(note)` so nothing is invented. It **refuses** (exit 2, markers left
> intact) unless BOTH sides are pure appends — an edit to existing text
> is a real conflict and stays a human's job.

1. **Start a bean list at session start.** As soon as you have
   enough context (after reading the user's first request, the
   SessionStart hooks, and the current branch / PR state), create a
   session **epic** bean plus child task beans decomposing the
   requested work (`beans create "Session: <branch/goal>" --type
   epic`; one `--type task` per concrete step). If the request
   is one trivial task, you may skip — but any time there are ≥ 2
   distinct steps, create the beans.

   **🛑 `--type epic`, NOT `--type milestone` (corrected 2026-09-26 on owner
   instruction).** This line said `milestone` until then, and following it
   ~291 times is why `milestone` stopped meaning anything here: cat-harness's
   hierarchy is `milestone -> epic -> feature -> task/bug`, where a
   **milestone is an owner-level goal** — the platform's own tracker has
   **three**, from "the owner's goals" — while a session is a work-tranche,
   which is what an `epic` is. qou had **374** milestones, 291 of them
   `Session: …`, so the roadmap had ~291 roots and `check-bean-parents`
   reported **1910 problems / 2305 open (83 %)**. The 291 were retyped to
   `epic` in the same commit as this edit (`milestone` 374 -> 49).

   **Do NOT "fix" this by using `--type task` instead.** That was the first
   instinct and it is measurably worse: `ROOT_TYPES = {milestone, epic}`, so a
   parentless task is an orphan, and `task` is not a legal parent — measured
   on the 291, a `task` retype would have created **66 new orphans** and left
   **148 open children illegally parented** (`task beans can only have
   milestone, epic, or feature as parent, not task`). `epic` costs nothing:
   children stay legally parented and the bean stays a legitimate root.

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
   - **The 50-word cap is a cap on the LEDGER, not on the turn.** It
     bounds this bean-status block so the author can scan it — it is
     never a budget for the substantive report of what you found, which
     is governed by **Terse ≠ compressed** in §User accessibility above.
     A turn that measured something puts the claim, the evidence, the
     implications and the options in the body of the reply, and uses
     these lines only to say which beans that touched.

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
      queue items (`beans/defs/proof-integration-watcher-queue.json`,
      `beans/defs/canonical-watcher-queue.json`,
      `beans/defs/compute-integration-watcher-queue.json`,
      `beans/defs/detangler-integration-watcher-queue.json`). Prefer
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
      `bun run folio-assistant/cat-harness-tools/pipeline/qa-sweep.ts <path> --only <crit>`
      (path corrected 2026-11-15: `content/pipeline/` no longer exists in the
      platform. It takes ONE path per call — extra paths are ignored silently.
      At platform pin `b61e856` it does not load at all: the pinned
      `folio-assistant-sci` layer still imports `cat-harness/schemas/kg/cat-harness`,
      which moved to `cat-harness-tools/schemas/`. See bean `qou-4jhp`)
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
      **zero** of ~700 self-stale witnesses were safe to refresh.

      > **Re-measured a FOURTH time 2026-08-30 on `main` `655a80ee84d`, and the
      > answer is unchanged where it matters: `cosmetic = 0`.** The denominator
      > and the split both moved, so quote these rather than the figures above:
      > **559 decided** (was 628 in the committed witness), **substantive 186 /
      > 33.3 %**, **rewritten 309 / 55.3 %**, **unresolvable 60**,
      > `cosmetic_import_cone_drift` **4**. So the standing advice holds on a
      > fourth independent run — **not one self-stale witness in the corpus is
      > safe to refresh**, and an idle pass should spend its budget on sidecars.
      > Recorded in `computations/witness-staleness-triage.witness.json`.
      >
      > **FIFTH run, 2026-09-07, and `cosmetic = 0` again — but one bucket
      > MORE THAN DOUBLED and it is the one that matters.** Quote these:
      > **603 decided**, **substantive 205 / 34.0 %**, **rewritten 333 /
      > 55.2 %**, **unresolvable 55**, `cosmetic_env_differs` **1**,
      > `cosmetic_import_infra_only` **0**, `cosmetic_strips_provenance` **0**,
      > `unparseable` **0** — and **`cosmetic_import_cone_drift` 4 → 9**.
      >
      > The headline is stable across five runs and ~5 weeks: **zero self-stale
      > witnesses are safe to refresh**, so an idle pass still spends its budget
      > on sidecars. The *interesting* movement is that import-cone drift is the
      > only growing bucket, and it is the one whose own label records
      > "measured 2/2 moved" — a producer whose source is byte-stable while a
      > NUMERIC-bearing module it calls changed. Those 9 are not "safe to
      > refresh"; they are the opposite, the cases where a re-run is *expected*
      > to move a number, and they are invisible to the `git diff <producer>`
      > check AGENTS.md tells you to run. Everything else held its proportion
      > (substantive 33.3 → 34.0 %, rewritten 55.3 → 55.2 %), so this is not
      > drift in the denominator.
      >
      > Bean `qou-e9pp`, whose own record stopped at the third run
      > (2026-08-19) and whose title still reads "~700 self-stale witnesses"
      > against a decided population that has been 559–628 for a month.

      Source-
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

      **🛑 But requirement one MASKS a whole defect class, and the "2 real
      defects" figure below cannot see it (added 2026-08-29, bean `qou-0e1t`).**
      Setting `PYTHONPATH` is necessary for the runner to reach the corpus's
      bare-name imports — and it is exactly what hides a script whose
      `import _path_bridge` precedes the `sys.path` bootstrap that resolves it.
      `_path_bridge` lives in `computations/`; a script in a cluster subdir has
      `sys.path[0]` set to its own directory, so that import fails unless the
      parent is already on the path. **Measured on the SAME file at the SAME
      commit, varying only the environment:** without `PYTHONPATH`,
      `ModuleNotFoundError: No module named '_path_bridge'`; with
      `PYTHONPATH=computations`, 4/4 checks pass and the witness is written.
      **Six such scripts were live on `main`** — among them
      `qbeta_d_frame_trace_baseline_probe`, whose `gap_over_ladder_ratio =
      92.1058` the Δ fork-pricing probe calibrates against — and none appears
      in the "2 real defects" list, because the runner that produced that list
      set `PYTHONPATH` by its own rule. So read that 2 as *"2 that survive a
      PYTHONPATH-equipped runner"*, not as *"2 that a user can run"*.

      The fix is at the script (move the import after the bootstrap, per
      `_path_bridge`'s documented USAGE), and the guard is
      [`computations/audits/path_bridge_bootstrap_audit.py`](computations/audits/path_bridge_bootstrap_audit.py),
      which narrows by pattern but **decides by executing each candidate with
      `PYTHONPATH` stripped**. Its own count was 28 before it was corrected to
      6: the first pass matched only `sys.path.insert(` and missed
      `sys.path[:0] = [...]` — 22 false positives from one unknown spelling,
      the same detector-blindness class as everything else in this section.

      **The 2 real defects**, re-verified against `main` on 2026-08-24:
      `su4_1111_markov_trace_probe` (`scipy.sparse` rejects `dtype object` — an
      `mpf` reaching a sparse matrix) and `qbeta_habiro_element_probe`
      (`TypeError: 'NoneType' object is not subscriptable`).

      **`hadron_knot_table` does NOT crash; it is very slow — and getting to
      that took two wrong turns of mine, in opposite directions.**

      First I wrote that it "runs, slowly" on the strength of a **timeout**
      after three `A=1` atoms with no traceback. A timeout is not proof of
      success; that claim had no evidence behind it, whatever its merits.

      Then I retracted it, on the sibling bean `qou-q7lf`, which reports a
      **second** scipy-sparse boundary in
      `hecke_core_legacy.unified_iterative_correction` reached via
      `binding_energy` at `A ≥ 2`. **That bean is stale.** Its last update is
      2026-08-23T23:08; `da645cf0f32` ("the sparse crossing loop died on mpf
      coefficients") and `46dcfc62a57` landed on 2026-08-24 and fix exactly
      that site. The live code computes `exact_chain` **before** the loop,
      routes an exact chain off scipy entirely, and accumulates over σ's
      nonzeros in COO — `O(dim·nnz)`, the same complexity the float64 branch
      gets from sparse BLAS — rather than coercing `c`/`d` to float, which its
      own comment refuses by citing this file.

      So: **a sibling's bean is not a primary source either.** The corpus-grep
      discipline this document states for source-file `## Status` notes —
      *"not authoritative: the corpus is the source of truth"* — applies to
      beans verbatim, including beans written by other agents that look
      authoritative because they are specific and recent. I applied that rule
      to my own claims all session and suspended it for someone else's.

      Measured on `main` 2026-08-24: the three `A=1` atoms complete, then
      deuterium — the first bound atom — ran for a **full 50 minutes and was
      killed by its own timeout** (`exit 124`), with **zero tracebacks**. It
      neither crashed nor finished.

      Keep the two claims separate, because this is the same signal that
      started the whole confusion. **"Does not crash" is established by the
      code**, above: an exact chain provably never reaches a scipy call, so
      there is no boundary left to die at. The 50-minute run **corroborates**
      that and is not what proves it — a timeout still could not have proved
      it, and a crash at minute 51 would not be excluded by any run. What the
      run *does* establish on its own is the **cost**: > 50 min for one bound
      atom of nineteen. Budget accordingly, and do not expect the table to
      finish.

      The 10 timeouts are a 240 s budget artifact and may simply be
      long-compute; re-run with a real budget before calling any of them
      broken — and, per the paragraph above, before calling any of them fixed.

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

      And ~49 % of the backlog is `rewritten` (**55.3 % as re-measured
      2026-08-30**; see the fourth-run note above) — the recorded `commitSha`
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

8a. **Draft → ready: ONE REST CALL, and READ THE STATUS CODE — a 403
   never clears, a 503 does. Never close-and-reopen a PR to get past
   it** (owner ruling, 2026-09-05; diagnosis corrected 2026-09-13,
   remedy measured 2026-09-14). Use

       POST /repos/{owner}/{repo}/pulls/{n}/ccr/ready_for_review

   It returns `200 {"draft": false}`. **On a `503` from that route, retry
   spaced — it is a transient CCR-family outage and it does clear; measured
   windows of ≥ 15 min. On the `403` from GraphQL, never retry — that one
   is a hard block. The status code is the discriminator; see the box.**
   `mcp__github__update_pull_request` with `draft: false` fails — often for
   hours — with

       Failed to find pull request: API rate limit already exceeded
       for user ID 662242

   while every REST path (title, body, state, create, merge, and all
   reads) keeps working.

   > **🛑 THIS RULE PREVIOUSLY SAID "SPACED RETRY ONLY", AND THAT
   > ADVICE COULD NEVER SUCCEED (corrected 2026-09-13).** It attributed
   > the failure to a rate-limited **node-ID lookup**. Measured twice,
   > independently: GraphQL is **403-BLOCKED session-wide from Claude
   > Code**, not rate-limited, so there is no limiter draining and no
   > wait to sit out. #7241 got the 403 while *supplying* the node_id
   > from a prior REST read — the lookup skipped entirely — and a
   > read-only `query { viewer { login } }`, which does no lookup at
   > all, returns the same 403. The body says so in words:
   >
   > > *"GitHub GraphQL is not available from Claude Code sessions; use
   > > the REST API. For review threads, auto-merge, and
   > > draft/ready-for-review use the CCR routes on api.github.com"*
   >
   > **🛑 THE CCR ROUTE GOES DOWN IN WINDOWS, AND A 503 IS NOT A 403 —
   > measured end-to-end on #7350, 2026-09-14.** This passage has been
   > corrected three times in two days and the final shape is the useful
   > one, so read the table rather than any one sentence:
   >
   > | time | `ccr/ready_for_review` | plain REST | GraphQL |
   > |---|---|---|---|
   > | #7230, 09-12 | **200** first try | — | — |
   > | #7350, 06:30–06:45 | **503** × 6 over ~15 min | **200** | **403** |
   > | #7350, 07:40 | **200**, flip succeeded | **200** | **403** |
   >
   > The middle row was briefly written up here as *"not dependable"* and
   > *"sustained unavailability"*. **Both overstated it**: the route came
   > back within the hour and the flip went through on the seventh attempt.
   > What is true is narrower and more useful — the **CCR family** has
   > outage windows of at least fifteen minutes during which **ordinary
   > REST answers normally**, so a 503 there says nothing about the rest of
   > the API.
   >
   > **So the two failure modes take OPPOSITE responses, and the original
   > rule paired them the wrong way round:**
   >
   > - **`403` from GraphQL — never retry.** A hard session-wide block. It
   >   was measured at every point above, an hour apart, including on a
   >   query doing no node-ID lookup at all. Nothing drains; §8a's old
   >   *"retry until it lands"* could never succeed.
   > - **`503` from a CCR route — retry, spaced.** A transient outage that
   >   clears. This is where spaced retry actually belongs.
   >
   > **Still worth doing anyway: open the PR non-draft in the first place**
   > where the work is already verified. `create_pull_request` takes `draft`
   > as a plain REST field and never touches either transport, so it cannot
   > be caught by a window at all. And if you are holding a draft while the
   > window is open, wait it out and say so; do **not** close-and-reopen,
   > which remains forbidden.
   >
   > **`PATCH` is independently confirmed as a silent no-op.** Measured here
   > with correct headers: `PATCH /pulls/7350 {"draft": false}` → **`200`**,
   > and the authoritative re-read still says `draft: true`. (A first
   > attempt returned `415` for want of `Content-Type: application/json` —
   > a 415 is *your* bug, not evidence about the field.)
   >
   > That single fact explains what four prior sessions could not: the
   > measured "windows" were ~2 h, ~4 h, ~4 h and ~10 h and never
   > agreed, because nothing was draining. **An agent following the old
   > wording waits forever**, and at least one armed a `send_later`
   > check-in to do exactly that.
   >
   > **The 403 body names four more routes, and had been discarded
   > unread across at least five sessions:**
   >
   >     GET  /repos/{owner}/{repo}/pulls/{n}/ccr/review_threads
   >     POST /repos/{owner}/{repo}/pulls/{n}/ccr/comments/{id}/resolve   (or /unresolve)
   >     PUT  /repos/{owner}/{repo}/pulls/{n}/ccr/auto_merge              (or DELETE)
   >     POST /repos/{owner}/{repo}/pulls/{n}/ccr/ready_for_review
   >     POST /repos/{owner}/{repo}/pulls/{n}/ccr/convert_to_draft
   >
   > `ccr/review_threads` is worth as much as the draft flip: "review
   > threads are GraphQL, therefore unreadable" has a direct REST answer
   > too. **Read the body of a 403 before believing its status line.**
   >
   > Also measured: `PATCH /pulls/{n}` with `{"draft": false}` returns
   > **200 and the re-read still says `draft: true`** — REST accepts the
   > field and silently discards it. So a 200 there is not evidence
   > either. Recorded in `.claude/agent-memory/merge-coordinator/`
   > (PR #7241, merged 2026-09-13).

   **Do NOT close the draft and create a replacement PR for the same
   head.** It works, which is exactly why it keeps getting
   reinvented: this session did it three times (#6526 → #6579,
   #6649 → #6674, #6723 → #6753) before the owner ruled against it.
   What it costs is not the API call but the record — the review
   threads, the Copilot request, the comment history and the PR
   number in every commit message, bean and coordination ledger that
   already cites it all stay on the abandoned PR, and a reader who
   follows that number lands on something marked "closed without
   merging" when the work in fact merged. The agent-harness PR rules
   independently forbid close-and-reopen; this ruling extends that to
   the undraft case, which those rules do not name.

   **Two measured traps, which survive the correction above.**

   - **The error is not evidence the call did nothing.** A sibling
     session measured (2026-09-05) that `update_pull_request` calls
     which set `title` / `body` *alongside* `draft: false` returned
     that same rate-limit error and **the title and body writes
     landed anyway** — only the draft flip was dropped. Always
     confirm with `pull_request_read` before re-sending a mutation,
     or you will write it twice.
   - **Send the flip ALONE, then re-READ.** Bundling other fields
     makes the partial-success case above harder to read. This applies
     to the `ccr/ready_for_review` route as much as to the old one.

   **The fix that avoids the problem entirely: open the PR non-draft
   in the first place** where the work is already verified.
   `create_pull_request` takes `draft` as a plain REST field, so
   `draft: false` at creation never touches the limiter. Rule 2 of
   this section asks for the PR immediately, at the first commit,
   which is usually before verification — so a draft is still the
   right default for a tranche that is about to grow. It is the wrong
   default for a PR you are opening at the end of the work.

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

    > **🛑 ALL THREE original gates are gone — do NOT block on any of
    > them (recorded 2026-08-07; Copilot row added later, heading
    > corrected 2026-08-28).** This heading read "Two of the three"
    > while the table beneath it and its own closing paragraph both say
    > three, so the line a skimming agent reads contradicted the body it
    > introduces. An agent following the older wording waits forever on
    > reviewers and a CI run that can never arrive:
    >
    > | Original gate | Actual state |
    > |---|---|
    > | CI green | **Unavailable.** Auto-triggers are disabled repo-wide — [`build.yml`](.github/workflows/build.yml) is `workflow_dispatch`-only ("CI auto-triggers disabled (owner directive 2026-06-30)": Actions billing). There is **no** `lean_ci.yml` in the tree. Feature branches routinely show **zero** workflow runs / zero check runs. |
    > | Gemini review | **Gone.** "The consumer version of Gemini Code Assist on GitHub has been sunset. All code review activity has officially ceased." (bot notice, PR #4514, 2026-08-01). |
    > | Copilot review | **🛑 CORRECTED 2026-08-30 — reviews DO arrive, and are RATIONED.** Measured first-hand on `qou#6122` (~3 min) and `folio-assistant#153` (~4 min), both from `copilot-pull-request-reviewer[bot]`, both with substantive findings — and on qou#6104/#6116, where the reviews landed minutes AFTER those PRs were merged on this row's old guidance, carrying six findings including a real correctness regression. **A quota exists**: five requests across two repos in ~30 min returned *"reached their quota limit"*, so do NOT re-request after every push. The mechanism for the historical zeros is UNSETTLED (three candidates weighed in [`docs/audits/2026-08-30-copilot-review-works-again.md`](docs/audits/2026-08-30-copilot-review-works-again.md), bean `qou-gwe9` **reopened**); note `get_check_runs` still returns `total_count: 0`, so that signal does not discriminate and must not be read as "no review is coming". Superseded text follows: Measured n=5 (bean `qou-gwe9`): requested explicitly via `request_copilot_review` on #5474, #5495, #5411, #5459, #5482 — **zero** reviews every time, and `get_check_runs` returns `total_count: 0` rather than a queued `copilot-pull-request-reviewer` run, so nothing is ever enqueued. Re-requesting after a force-push does not help; the cases span new Lean, a 20-file revert and a beans-only change, so it is not file-type-conditional. |
    >
    > **🛑 So the Phase-4 gate table now has ZERO live external gates, not
    > one.** All three original gates are gone. The agent's own verification
    > is not the last gate standing — it is the *only* gate. Act accordingly:
    > state the verification you actually ran. (The "do not wait on Copilot" that
> stood here is corrected above — reviews arrive, subject to quota.)
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

**A warn-only commit hook now surfaces the blocking gate (2026-08-25).** The
paragraph above was true and nothing acted on it: `core.hooksPath` was unset,
there was no `.githooks/`, and every reference to `precision-gates.sh` in the
tree was prose. A gate nobody invokes is documentation, and the cost is on the
record — beans `qou-mnrd` and `qou-82ur` reached the same finding from opposite
directions, that dirty witnesses land, get drained, and are replaced by
different dirty witnesses, each one arriving the way the last did.
[`scripts/precommit-precision-warn.sh`](scripts/precommit-precision-warn.sh) is
a `PreToolUse` hook on `Bash` that runs the **raw-float64 ratchet** when a
commit touches a witness or a `computations/` script, and prints the NEW-dirty
list. Three properties are deliberate and should not be "improved" away:

- **It warns; it never blocks.** It always exits 0. A `PreToolUse` hook exiting
  non-zero stops the tool call, and a bare container is the *default* here —
  `mpmath`/`numpy`/`scipy` are routinely absent on a fresh clone, exactly when a
  blocking hook would brick every commit in the session. Warn-on-commit was the
  owner's choice on 2026-08-25; the push-side block was offered and **declined**.
  Do not upgrade it to blocking without asking again.
- **It runs the ratchet only, not the family.** Measured on this corpus:
  the ratchet is **1.8 s**, the full `precision-gates.sh` is **3 m 12 s**. A
  hook runs *before* the tool call, so wiring the family in would add three
  minutes to every witness-touching commit — which buys avoidance, not safety.
  The advisory gates are deliberately not run here; `precision-gates.sh` remains
  the full preflight and is still yours to run by hand.
- **It is not a substitute for the preflight.** It covers one gate on the commit
  path. Everything the QA-is-agent-owned rule asks of you is unchanged.

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
`\bigl`-`\bigr`/`\begin`-`\end`; no line starting with `+`/`-`/`*` inside `$$…$$`
(markdown list-parser hijack); align-family environments (`aligned`, `align`)
fenced as ` ```tex `, not inline `$$`.

> **`\operatorname{}` is NOT a violation — the old rule was stale (corrected
> 2026-09-03, bean `qou-iars`).** This battery read *"no `\operatorname{}`
> (KaTeX rejects → use `\mathrm{}`)"*. Measured: the viewer loads **KaTeX
> 0.16.11** (`folio-assistant/{viewer,ui}/index.html`, CDN), and KaTeX has
> supported `\operatorname` since **v0.10.0 (2019)** — so the deployed renderer
> does not reject it, and pdflatex (amsmath) never did. `\operatorname{Re}`,
> `\operatorname{Im}`, `\operatorname{ord}`, `\operatorname{Area}`,
> `\operatorname{Vol}` are the *semantically correct* markup for operators
> (correct spacing), and blanket-rewriting them to `\mathrm{}` is a downgrade.
> Do **not** flag or sweep `\operatorname`. (If a KaTeX downgrade below 0.10
> ever happened it would resurface, but that is a version regression to fix at
> the CDN pin, not a content rule.)

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
rewrite shipped with `\operatorname` (believed KaTeX-breaking at the time; that
belief was itself stale — KaTeX has supported it since v0.10, see the correction
above), a `B`-vs-`𝔪` mislabel, a wrong `dim_q = [n]_q`, and a `λ` notation
collision — the latter three none machine-caught because the pipeline was
unavailable and the agent skipped the manual battery.

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

0. **`corpus_search` (MCP) — run this FIRST, because every path below
   shares one blind spot.** Paths 1-6 are greps, and a grep finds prior
   work only if it used *your* words. Prior work written in different
   words is not an edge case here; it is the case that actually costs a
   session, because the grep comes back empty and reads as a clean bill.

   The knowledge graph is the structure that survives a change of
   vocabulary: a block that never says "Temperley-Lieb" but `uses` one
   that does is one hop from the query, and `corpus_search` seeds
   lexically then expands structurally across the authored corpus and
   the ingested library at once.

   ```
   corpus_search  query: "<topic>"        # 1 hop, both directions
   corpus_search  query: "<topic>", direction: "in"   # what depends on it
   ```

   **If the MCP server is not connected, use the CLI. Never skip this step.**
   `bun scripts/corpus-search.ts "<topic>" [--direction in|out] [--hops N]
   [--limit N] [--search-text] [--provenance authored|ingested]` calls the same
   function the MCP tool calls, over the same roots. It runs on the light
   platform that the SessionStart hook installs.

   The MCP server does not start by itself: call `mcp__paper-assistant__start`
   first, then RefreshMcpTools (see §"MCP servers start on demand").

   The MCP route reported "paper-assistant: Connection closed" in every
   session from at least 2026-10-12 to 2026-11-20 (bean `qou-q261`). Two causes:
   - `.mcp.json` named `folio-assistant/cat-harness/src/index.ts`, which the
     platform restructure removed. The launcher is now
     `scripts/paper-assistant-mcp.sh`.
   - The MCP server needs the full platform (`scripts/setup-folio-assistant.sh`).
     The light one has no `@modelcontextprotocol/sdk`.

   A run that reports step 0 as "unavailable" has skipped it; the CLI was
   available. The default `--limit` is 20 seeds. At that limit, "Plancherel" returned 20
   authored seeds and 0 ingested; at `--limit 200` it returned 49 ingested
   (measured 2026-11-20). Raise `--limit` before reading "no ingested hits" as
   "not held".

   Read three things in its answer. **`why`** says whether a hit MATCHED
   or was REACHED, and by which edge — a `~` prefix means the edge ran
   backwards, so that node depends on the seed rather than the reverse.
   **`seedsByProvenance`** splits authored from ingested, and the shape
   that matters is many ingested hits with no authored ones: that means
   *cite it*, not *derive it*, which is the distinction path 5 exists to
   draw. **`emptyRoots`** names a directory that exists but holds no
   graph nodes — a corpus whose `.jsonld` siblings have never been
   generated answers every query with a silence indistinguishable from
   "nobody has done this". If it is non-empty, generate them
   (`gen-block-jsonld` / `gen-library-jsonld`) before reading any absence
   as an absence.

   It does **not** replace the paths below — it seeds on labels, titles,
   kinds and tags (add `searchText: true` for companion prose), so a
   topic named only inside a proof body is still a grep's job.

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
   grep -in <topic> library/INDEX.md              # ~513 briefs (527 lines); re-count, do not trust
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
   and re-deriving one. **576** document directories, holding **11,528**
   section files, are searchable this way (this read *"332 documents /
   7,313 sections"* until 2026-08-30 — low by 62 % — and *"542 / 10,922"*
   until 2026-09-03; the library grows, so **re-count, do not quote**).

   **Say which count you mean, or the next reader will "correct" you.**
   Three numbers describe this library and they are all different:
   `ls -d library/*/ | wc -l` gives **576** *directories* (what the grep
   above actually walks); `grep -c '^| \[' library/INDEX.md` gives **552**
   *index rows*, because the 23 known duplicate copies deliberately get no
   row of their own; and `summarize-library.py` prints that 552 as
   "documents". A grep-coverage claim wants the 576; a "how many distinct
   works do we hold" claim wants the 552. Quoting one against the other
   reads as staleness when it is a category difference.

   **🛑 And the duplicates do NOT always explain the gap — INDEX.md goes
   STALE, silently (found 2026-09-03).** On that date the index carried
   **519** rows against 576 directories, and only **23** of the 57 missing
   were marked `duplicate_of`. The other **33 were real documents with real
   sections that simply had no row** — invisible to this tier, which is the
   one the checklist tells you to read FIRST. They were not marginal: the
   volume conjecture (`0803219`), the oriented skein category
   (`arxiv-1712.08953v1`), affine-Hecke Plancherel (`arxiv-1110.6212v2`),
   knot polynomials on braid closures (`li-braid-closures`) and q-deformed
   Plancherel growth (`arxiv-2105.09342v1`) — this corpus's own subject
   matter, including the LP-Plancherel `Δ_λ` ansatz's literature.

   **So check the arithmetic before trusting tier 1** — but use the CORRECT
   invariant. This read *"`directories − index rows` should equal the duplicate
   count"* until 2026-09-07, and that is **short by the containers**: a journal
   issue carries `container: true` in its `structure.json`, gets no index line
   of its own by design, and has its constituent papers indexed separately
   (`ant-v14-n7-s` is *Algebra & Number Theory* Vol 14 No. 7 — 170 sections, no
   row, and all **ten** of its `-p01`…`-p10` children DO have rows). An agent
   applying the old form finds a gap it cannot explain and concludes the index
   is broken; I did exactly that, and wrote "`ant-v14-n7-s` carries 170 sections
   and is invisible to the tier every agent is told to read first" into a bean
   before checking the design. The invariant is

       directories − index rows  ==  duplicates + containers

   and when *that* fails the index is behind. Measured 2026-09-07 after a
   regeneration: **661 − 640 = 21 = 20 + 1**, exact.

   Both exclusions are silent, and one is silent in a worse way: `build()`
   returns `None` for a container or a duplicate with no diagnostic, so a
   directory that is neither — a genuinely un-indexed document — is
   indistinguishable from a designed exclusion without opening its
   `structure.json`. To separate them, classify the missing set by that file
   rather than by eye. The fix for a real gap is
   `python3 scripts/summarize-library.py --apply` (extractive, offline, no
   model; agent-written summaries preserved). The producer fixes it deterministically and offline —
   `python3 scripts/summarize-library.py --apply` (extractive, no model, no
   network; agent-written summaries are preserved). A clean tier-1 scan is
   evidence about the index, not about the library.

   **🛑 FOURTH TIER — `ocr/`, and the `sections/` grep above is BLIND to it
   (added 2026-08-30).** Some documents were ingested with their text in
   `library/<doc-id>/ocr/page-*.txt` and only a **stub** in `sections/`, so
   the command on the line above cannot see their mathematics at all:

   ```sh
   grep -rln <topic> library/*/ocr/     # the tier the three above miss
   ```

   Measured, not estimated: **25 of 576** directories carry an `ocr/`; ten
   of the eleven single-`sections/`-file directories hold **under 15 %** of
   their OCR bytes in `sections/`, six of them under 3 %. The worked case is
   the one that exposed it — `library/procrsoclondona92/` is **Moffatt &
   Ricca 1992, _Helicity and the Calugareanu invariant_**, whose `sections/`
   is **1,916 bytes of JSTOR download banner** against **46,511 bytes** of
   real text in `ocr/` (4.1 %). A `sections/` grep for *helicity* returns
   several other documents and **not this one** — the single most on-point
   held source for the mass/binding self-vs-mutual linking question, invisible
   to the documented path. `1992evansberger` (*A Hierarchy of Linking
   Integrals*, 2.2 %) is hidden the same way.

   So a clean `sections/` grep is **not** evidence the library lacks a topic.
   Run the `ocr/` tier before concluding a source is not held — the whole
   point of path 5 is to catch a citation, and this is exactly where the
   citations that matter have been hiding.

   This path exists only because the sources were sectioned into text.
   Before that they were 339 PDFs and grep could not see them, which is
   why the checklist historically stopped at four. Two practical notes:
   a hit's YAML front-matter names the document, section and page range,
   so it is immediately citable; and `library/<doc-id>/candidates.json`
   lists that document's extracted theorems and definitions if you want
   the claims rather than the prose.

6. **The beans** — `grep -rl <topic> beans/defs/`, **on the mount**
   (`beans/` is mounted from `cat/cat-harness/beans`; if `beans/defs` is
   missing, run `state-mount` first, or this path is an empty grep that reads
   as a clean bill). The work-plan tracker is a
   corpus in its own right (tens of thousands of files) and it is where a
   prior agent's *conclusion* most often sits before it reaches an audit
   doc or a content block. It is **not** covered by paths 1–5: `beans/`
   is not under `docs/`, `content/`, `computations/` or `library/`, and a
   coordination ledger is a different file.

   Read `status` and the whole body, not the title. A **`completed`** bean
   is the one that bites — it means the question was answered, and the
   answer may be a single sentence in the body with no artifact anywhere
   else. A **`scrapped`** bean is worth as much: it usually names the bean
   that superseded it, which is how you find the live carrier.

   History: added 2026-08-26 after one PR re-derived two results the
   corpus already held. The second was `qou-dwsh` (2026-08-03, priority
   high, `completed`), whose body states the conclusion the PR spent a
   tranche proving — *"a groupoid with inequivalent fibre objects carrying
   a 3-dim `W` whose fundamental is **not self-dual**"* — and which paths
   1–5 cannot reach, because that sentence exists nowhere but the bean.
   The trail to it ran `qou-8pl3` → `qou-8p1i` (scrapped) → `qou-dwsh`,
   i.e. through exactly the two statuses this note says to read.

Only after **all six** grep paths return empty (modulo the
originating file itself) may you declare the item open. Step 0 is not a
seventh gate — it is the step that most often stops you needing the other
six, and an empty result from it is not by itself a licence to declare
anything, because a graph that was never generated is silently empty. The source
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
> With the live anchors (`c_3(p) = -2.0693425771`, `c_3(μ) =
> -2.0202002328`, `Δq = 1.28e-8`) three independent routes agree:
> **3.8375e6** by secant, **3.8320e6** from `2.37/u³` at `u = 0.00852`,
> and `3838404.458` recorded in `rem-qstar`'s own witness as
> `S_prime_qstar`. Reaching 4.7e6 would need `u = 0.0079595`. Since
> 3.84e6 is just as impossible for a smooth real `f` as 4.6e6, the
> **prune stands and the real-q c₃ family stays killed** — only the
> quoted magnitude was wrong.
>
> **Proton `c_3` corrected 2026-10-13 (PR #7792):** it read `-2.0693425728`,
> a typed copy no producer reproduces; the canonical extraction
> (`qbeta_ck_cache.py`, `qbeta_utils.c3_proton_extracted`) gives
> `-2.06934257711516783787971951725`, and with the typed copy the N=3
> residual it is defined to zero was 2.7e-6 ppb instead of ~0. The secant
> moves by 0.34, invisible at the precision quoted. The muon `-2.0202002328`
> is the CODATA-2018-era figure (that extraction now gives `-2.0202002350`;
> the live CODATA-2022 muon pin gives `-2.0198603119`); it is kept because
> the secant is quoted as of that pin, not re-derived here.
>
> **🛑 "five other sites" was wrong by an order of magnitude, and wrong
> about WHERE (corrected 2026-08-29, bean `qou-kt8o`).** Measured on
> `origin/main`, excluding `.beans/`: the figure appears in **43 files on
> 71 lines** that also name `c₃` on the same line, and in **88 files** by a
> file-level scan that allows the figure and the `c₃` context to sit on
> adjacent lines. Either number is ~10–20× the "five" claimed here, so do
> not treat this figure as nearly drained.
>
> **The characterisation misled more than the count.** "Audit docs and
> `local/compute-author` §precedent-table" names neither of the two places
> that actually matter. By the tight line-level measure the largest group is
> **`computations/qbeta` (20 files)** — live probes, producers and witness
> `description` fields, i.e. code that *recomputes* the stale figure rather
> than merely recording it — against 8 in `docs/audits`. And there are
> **5 `.lean` files**, which this note does not mention at all; one of them
> (`FaddeevModularDouble.lean`) carried the superseded `c₃ = -2.0097`
> itself, not just the derived slope. All 5 are fixed as of #5942.
>
> **Both spellings are the same stale value.** `4.6e6` and `4.66e6` are
> one figure: the secant `|-2.0693 - (-2.0097)|/1.28e-8 = 4.65958e6`. Its
> companion `Δc₃ = 0.0596` is a third spelling. A grep for `4.6e6` alone
> finds well under half of them.
>
> **Do not sweep the remainder blind.** Most survivors are dated audit docs
> — `qou-3nva` deliberately left those as historical records of the
> analysis, and that decision stands — or witness `description` fields,
> which cannot be corrected without re-running their producer. Several use
> `4.66e6` as the *input* to a refutation whose conclusion holds under
> `3.84e6` anyway. Re-measure the specific file you are editing, and fix at
> the producer; tracked in `qou-3nva` / `qou-kt8o`.

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

> **🛑 Keep the URL under 150 characters, or the link arrives BROKEN
> (measured 2026-09-04, bean `qou-pbql`).** A link destination of **150
> characters or more** in a PR body comes back wrapped in double backticks —
> `[label](``https://…``)` — and markdown link destinations do not process
> backticks, so the destination becomes a literal string and the link is dead
> in the rendered body. 149 is clean; T149 / T150 / T151 were binary-searched
> with generator-asserted lengths. It is the **URL** length, not the line
> length (a 130-char label with a 110-char URL is clean), and it is **not** the
> author's input: the same body was rewritten twice in plain single-delimiter
> markdown and came back mangled both times.
>
> The pattern above is the problem, because a `claude/<theme>-<utc-ymd>` branch
> name spends ~43 characters of the budget. **Address a long path by short
> commit sha instead** — the same bean file is **153** characters branch-form
> and **116** sha-form:
>
> ```
> https://github.com/litlfred/qou/blob/<short-sha>/<path-to>/<block>.md
> ```
>
> A sha-form link is also more durable: rule 8 rebase-merges every branch, which
> rewrites the shas a branch-form link resolves through.
>
> **Do not "fix" this by shortening the bean's filename or blaming `--`.** The
> first three instances were all `.beans/…--….md` paths, which made both the
> dot-directory and the double hyphen look causal; tested in isolation a probe
> carrying **both** is clean at 98 characters and one carrying **neither** is
> mangled at 155. Bean filenames are `<id>--<slug>.md` with long slugs, so they
> simply clear 150 more often than `scripts/foo.py` does.

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
- **Q_β** (the CAL-2 proxy):  `Q_β = ℏ/𝔇_β = m_e·|q₀²−2q₀−1|(q₀+1)/(2q₀³) ≈ 0.784 MeV` (0.17% vs CODATA). 𝔇_β **is** CAL-2; because the modulus is overdetermined and pinned most precisely by m_μ/m_e, Q_β reproduced from q₀ is a 0.17% **cross-check**, not a fourth input.

  > **🛑 EXCISED 2026-11-15 (owner, D-W2): "Q_β is the bar-odd `sinh` partner of the
  > bar-even `cosh` meson scale m_π".** That description stood here until this date. It is
  > removed because **no Q_β functional on record has a definite bar parity** under
  > q ↦ q⁻¹: not Form A above, not the retired z = 1 trace, and not the ruled z_D trace. The
  > two traces carry only an overall factor h = q − q⁻¹ = 2 sinh λ. Measured exactly in
  > [`docs/audits/2026-11-15-one-sided-weak-vertex.md` §4](docs/audits/2026-11-15-one-sided-weak-vertex.md).
  > Nothing numeric, Lean or compute depended on the label. Do **not** reinstate it on the
  > strength of the letter-level fact that σ − σ⁻¹ = h is bar-odd; that is true of the letter
  > and was never shown of Q_β. Open question: bean `qou-hlx8`. Out of scope and untouched:
  > `prop:bar-parity-split` and `conj:binding-qbeta-complex-volume` (Q_β ↔ binding).
  >
  > **🛑 SCOPING NOTE (2026-09-05) — the route that produces this number is
  > under review; the number is unchanged and nothing here is enacted.**
  > Solving the published closed form against the ansatz shape
  > `|tr_M^z(Δ_S)|·E₀` gives **`z = 1`**, which is **not** an admissible Markov
  > parameter under convention D — the admissible roots are `z = q` and
  > `z_D = q³/(q²+1)`, and `z = 1` leaves the `χ_(1³)` coefficient
  > `c(1) = q²(q−1)(q³−q²−1)/… ≠ 0`, so it does not annihilate the block the
  > GNS/TL quotient kills (`ConventionDAdmissibleRoots.lean`, sorry-free; PRs
  > #6722 / #6763, both routes independent).
  >
  > **§NO FITTING, EXCEPT CAL-1/2/3 above counts this as selection against the
  > target** — it names *a branch* chosen because it reproduces the measured
  > value, and states that accuracy is not evidence of correctness. So the
  > 0.17 % is not a point in this route's favour under the directive.
  >
  > **The two derived alternatives, neither adopted:** `z = q` (the
  > augmentation) gives `0.8798906` MeV, **+12.470 %**; `z_D` gives
  > `0.4447004` MeV, **−43.157 %**, against CODATA `0.7823334` MeV. Choosing
  > between *them* by residual is the same defect one level down and is equally
  > forbidden — the choice turns on what `ε` **means** in `Q_β = |ε(Δ)|·E₀`,
  > which is bean `qou-99qc` and is an owner call.
  >
  > **🟧 OWNER RULING 2026-09-08 (final, same day) — ε is the MARKOV TRACE AT
  > `z_D = q³/(q²+1)`, i.e. option C; convention D governs the decay channel
  > (D7).** Sequence, for the record: the owner first selected the augmentation
  > on an option that carried the agent's recommendation; the same hour
  > `13bb8243d8` (`qbeta_augmentation_is_a_markov_trace_probe.py`, on `main`)
  > showed the augmentation IS the Markov trace at `z = q`, so the choice is
  > *which Markov parameter*, and under D7 (convention D = the two-row
  > truncation, scoped to the decay channel) the consistent point is `z_D` —
  > the augmentation is the strictly finer one-row truncation (`y_(2,1) = 0`)
  > and is **not** convention D. Put back to the owner with both options
  > framed; **the owner chose `z_D`.** Base value `0.4447004` MeV,
  > **−43.157 %** against CODATA. The published 0.17 % form is retired as the
  > base (it is the `z = 1` cell) and stays citable only as the historical
  > C-frame cross-check; the augmentation cell (+12.470 %) is the other
  > admissible point and is proportional to `z_D`'s
  > (`α = (q⁴+1)/(q²+1)²`). The c_k ladder is to be re-derived on the `z_D`
  > base (`qou-cds1`) — 🛑 **but NOT because of the phase; see the scoping note
  > at the end of this section**; the dashboard rows
  > Q_β / m_n / Δ_pn are NOT yet re-scored on it. Same day, the owner also
  > ruled that every canonical **braid word** is to be selected via γγ
  > (pair-production) construction + the confinement SDP at q₀, never by
  > census (bean `qou-ales`). Record:
  > [`docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md`](docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md) §8.
  >
  > **Until it is made, cite this number with its scope**: it is a recorded
  > cross-check whose functional is inadmissible under the canonical
  > convention, not a derived prediction. Do **not** quote the 0.17 % as
  > evidence for the framework, and do **not** replace it on your own
  > initiative — that picks the option. Full enumeration:
  > [`docs/audits/2026-09-05-qbeta-functional-decision-options.md`](docs/audits/2026-09-05-qbeta-functional-decision-options.md)
  > §6.
  >
  > **🛑 SCOPING NOTE (2026-09-14) — `qou-cds1` is NOT blocked on the phase
  > `qou-pdix`, and this document said it was in two places.** Both sites now
  > point here. The old reading is correct only for the **retired `z = 1`
  > cell**; it did not survive the 2026-09-08 ruling that made `z_D` the base,
  > and nothing re-checked it at the time.
  >
  > The ladder's N=2 factor is `F_N2(α) = cos(α − u/2)·(1 − u²)`, so
  > `cos ≤ 1` caps it at `1 − u² = 0.99992745` **for every real α** — the
  > supremum sits at `α = u/2` and is still below 1. What the ladder must
  > supply is `F_required = Q_codata / Q_base`, and on the two bases the ruling
  > actually selects that number is **above 1**:
  >
  > | base | `Q_base` (MeV) | `F_required` | vs the cap |
  > |---|---|---|---|
  > | `z = 1` (Form A) — **RETIRED** | 0.783645827375 | 0.998325241673 | reachable |
  > | `z_D`, order-zero `E₀` — **RULED** | 0.444700408522 | **1.75923699418** | **excluded** |
  > | `z = q` (augmentation) | 0.87989056126 | 0.889125812282 | reachable |
  > | dashboard scored cell — **RULED** | 0.65185631006 | **1.20016236389** | **excluded** |
  >
  > **The two cells a cosine can reach are exactly the two the ruling does not
  > select.** So no value of α unblocks `qou-cds1` on the ruled base, and an
  > agent sent to derive α as *the* `Q_β` L2 blocker is working off the
  > critical path. The live question is **what object supplies a factor above 1
  > at all** — about the base or the assembly, not the phase.
  >
  > **`qou-pdix` is NOT retired and stays open** (§13a): α is still the
  > ladder's N=1 phase and is still underived. Only its *priority* changes.
  >
  > Established twice, independently and sorry-free — PR #7355
  > (`LadderFactorBound.lean`, 4 lemmas, 7/7 probe) and PR #7262
  > (`EigenphaseQuantization.lean`, 19/19, base-independent table) — and
  > verified rather than taken on trust in
  > [`docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` §5.1](docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md)
  > (merged as #7276), which recomputed all four `F_required` at 70 dps and
  > inspected the Lean for `sorry`. **That merged audit is the corpus artifact
  > this note is derived from**; the two PRs are still open, so cite the audit,
  > not them, when checking it.
  >
  > **The two beans do not carry this yet** — `qou-cds1`'s last entry is
  > 2026-09-08 and `qou-pdix`'s 2026-09-12, both predating the result. Appended
  > alongside this note.

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

> **🟧 Mass-and-Binding-Algorithms appendix sync (STRICT).** Any PR that touches mass / binding derivations or compute infra (Steps 9a, 9b, 10, 11 of the canonical chain, or any sidecar algorithm — Δ_λ closure, c_k truncation ladder, LP/SDP dual emission, witness-JSON pipeline) **must** update the matching `alg:`-block under [`folio/quantum-observable-universe/appendix-mass-binding-algorithms/`](folio/quantum-observable-universe/appendix-mass-binding-algorithms/) in the same PR. The appendix is a maintenance contract bridging propositions ↔ Python API; its `uses[]`, `computation.script`, `computation.witness`, and `.md` *Algorithm / Correctness / Python API* sections must stay in sync with the actual compute. Enforced by `local/coordinate.md §2-bis`, `local/compute-author.md §8 pre-work checklist`, `local/compute-audit.md §verification checklist`, and `local/proof-editor.md §coordination rules`. Reviewers diff the appendix against the compute / proof change.

> **🛑 ABSOLUTE MASS EXCISED (owner ruling 2026-08-11, bean `qou-exam`).** The framework no longer claims, targets, or scores an **absolute** nucleon or atomic mass in MeV (m_p, m_n, m_⁴He) as a prediction. Absolute mass is `m_e · (dimensionless ratio)`, and m_e (CAL-1) sets the MeV scale *by fiat* — so the MeV number double-counts the calibration and carries no content beyond the ratio. **The mass-formula shape and the `canonical_mass` facade in the two banners below remain valid — but as `m_e`-scaled *realizations* of the dimensionless ratio / binding, NOT as absolute-mass predictions.** Report ratios (`m_p/m_e`, `m_μ/m_e`, `m_K/m_π`), binding `B(K)`, decay Q-values (`Q_β`), and splittings (`Δ_pn`); do **not** present `m_p ≈ 938.27 MeV` as a framework *prediction* (it remains derivable as `m_e × ratio`, but that is a rendering, not a claim). Broader than the 2026-08-02 q₀-derivation forever-gate — that closed one route; this closes the absolute-mass *target*. Full ruling: [`docs/audits/2026-08-11-excise-absolute-mass-notion.md`](docs/audits/2026-08-11-excise-absolute-mass-notion.md).

> **⚠ Critical framing — the mass formula is `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`; do NOT reintroduce `λ_scale` OR the `Geom_full` wrapper.** Two standing purges: (1) the factor once called `λ_scale` was **absorbed** 2026-05-23 (commit `ffdd84409`) — not a separate constant to derive; (2) the opaque `Geom_full(K)` wrapper was **PURGED 2026-06-06** (owner directive, repeated — it obscured) in favour of its explicit meaning, the **volume–density product** `Vol(K)·ρ(K)/ℏ_q²`. So the per-knot mass is `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²` (electron scale × hyperbolic volume × per-block density). Compute uses `vol_density_borromean` / `vol_density_per_block` / `vol_density` (`_li_2_q_util.py`, `mass_vol_density.py`). The Yekutieli per-cell variant was tried then PURGED 2026-05-24 (`71d674da1`). The "2.89% m_p gap" is between the current categorical `Vol(𝓑₃)·ρ` value and its exact value — **not** a "λ_scale closure" problem. **Do not write `Geom_full` in paper, audit doc, or compute — write the explicit `Vol(K)·ρ(K)/ℏ_q²`.**

> **🛑 CORRECTION (owner ruling 2026-06-24) — `m_e·Vol(𝓑₃)·ρ/ℏ_q²` is NOT the canonical ABSOLUTE nucleon mass. Use the muon-anchored Hecke energy via the `canonical_mass` facade.** The banner above describes the *general* volume–density shape, but read with `K = 𝓑₃` (Borromean) and `ρ ∈ {λ_A, tr_M}` it is the **wrong absolute-mass form** — it applies `1/ℏ_q² (= c_q²)` to the Borromean volume and yields **m_p ≈ 966 (+2.96%, λ_A is a CODATA-implied FIT)** or **≈ 406 (−57%, naive tr_M)**. The canonical absolute nucleon mass is the **muon-anchored** Hecke energy:
> `m_p = 2·(m_μ·F_Bor − 6·m_e)`, `m_μ = m_e·Vol(4₁)/ℏ_q²`, `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³` → **m_p ≈ 938.27, m_n ≈ 939.56 (CODATA)**. The `c_q²` belongs in the **muon** anchor `Vol(4₁)`, then dressed by the *dimensionless* `F_Bor` — not on `Vol(𝓑₃)`.
> **Route every absolute nucleon/atom mass through the single facade [`computations/canonical_mass.py`](computations/canonical_mass.py)** (`proton_mass_mev` / `neutron_mass_mev` / `nucleon_mass_mev`). `mass_vol_density` / `vol_density_borromean` / `linking_weight_family_a` (=λ_A) are **deprecated for absolute mass** (emit `DeprecationWarning`); `vol_density_per_block` stays valid for **binding ratios only** (scale cancels). Read first: [`docs/canonical-mass-formula-guardrail.md`](docs/canonical-mass-formula-guardrail.md). Why it recurred: this very banner read with `K=𝓑₃` *is* the wrong form — that's the trap the facade closes.

> **⚠ Critical framing — Q_β `c_k` is a TRUNCATION ORDER, not a wire/un-wire gate.** The Q_β precision ladder `Q_β = Q_base·Π(1 + c_k·u^k)` with `u = b·ℏ_q² ≈ 0.00852` is a **convergent series**; `N` is the truncation order chosen by target precision (`N ≥ log₁₀(1/ε)/2.07 − 1`). `c_2 = -1` is **structural** — no fit, no CODATA, no q₀ (see the correction immediately below, which restates two halves of this sentence's earlier wording); `c_k ≥ 3` are q₀-dependent NEAR-MATCHES (e.g. `c_3 = -2 = J_Hopf(q=1)` is 3.47 % from the extracted `c_3` at m_p-pin q₀ — **or 3.35 %, the same gap normalised by the extracted value rather than by `-2`; see below**), with the N=4 → N=5 non-monotonicity as the experimental signature — **but not for the reason long given here: see the correction below.**
>
> **🛑 CORRECTION (2026-09-04) — the non-monotonicity is real; its stated
> REASON is not, and its figures are convention-C.** The clause above cited
> "the N=4 → N=5 non-monotonicity" on the strength of
> [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md),
> which argued that *"a convergent series with exact `c_k` would be
> monotone."* **That is not a correct general statement.** Partial sums of a
> convergent series need not have monotonically decreasing residuals unless
> the terms are sign-definite and decreasing, which is nowhere established
> for this ladder — so as written the argument does not support its
> conclusion, even though the conclusion is right.
>
> **🛑 AND THE REPLACEMENT ARGUMENT WAS ALSO WRONG — corrected 2026-09-05, and
> it was mine.** This block replaced "monotone" with a SIZE MISMATCH: *"the N=4
> residual should sit near `|c_5·u^5| = 0.577` ppb; convention C measured it at
> 0.055 ppb, ~10× smaller — an anomalously good landing, which is the fit
> signature."* **That figure is computed on the SUPERSEDED `c_5`.**
>
> The slot is settled in
> [`qbeta_ladder_c5_slot_provenance_probe.py`](computations/qbeta/qbeta_ladder_c5_slot_provenance_probe.py)
> (bean `qou-54g5`): `c_5 = −(b²+½) = −1.2527` is **current** — six carriers,
> 2.4 % from the SDP extraction `−1.2229`; `c_5 = 3c_3²+b = +12.8676` is
> **superseded**, wrong sign, ~10× off. And `qbeta_ck_truncation_order_analysis.py`
> still carries the superseded family at **line 57**, which is the script the
> 0.577 was read from.
>
> With the **live** `c_5`, `|c_5·u^5| = 0.0561` ppb against the measured
> **0.055** ppb — **2 % apart, exactly what an exact series predicts.** The
> anomalously-good landing does not exist, and the argument points the other way.
>
> **What supports the conclusion is the residual MAGNITUDE.** Recomputed at the
> proton pin under the live family, `|residual|` runs **6.1698 → 6.2260 ppb**
> across N=4 → N=5 — it increases, so the signature holds. Under the superseded
> family it runs 6.1698 → 5.5551 and does not. So the non-monotonicity is real
> **under the correct coefficient**, while both arguments previously offered for
> it — "monotone" and the size mismatch — are unsound. Use the magnitude
> crossing, and note it is the *magnitude*: the signed column goes
> −6.1698 → −6.2260, which is *decreasing*, and reading it that way is how PR
> #6424 reached the opposite conclusion.
>
> **Caveat, load-bearing:** the crossing is only **0.91 %**, computed with `c_3`
> hardcoded at the recorded proton extraction and at the proton pin only. It is
> **not** robust to a large `c_3` move; a full settlement re-extracts `c_3` at
> both pins. Probe:
> [`qbeta_ck_c5_slot_and_size_mismatch_probe.py`](computations/qbeta/qbeta_ck_c5_slot_and_size_mismatch_probe.py)
> (4/4).
>
> **The figures `+0.055 → +0.63` ppb are CONVENTION-C.**
> `qbeta_ck_truncation_order_analysis.py` computes in whatever frame the
> substrate is on; under **D** the same table prints
> `+600999.7384 → +601000.3155`, and its hardcoded prose disagreed with its
> own computed table by six orders of magnitude until fixed (2026-09-04).
> **What survives the convention change is the STEP, not the baseline:**
> `+0.575` ppb in C against `+0.577` ppb in D — so the reversal is
> frame-robust and only the offset moves.
>
> **Do not read this ladder as a live N-selection.** Per defect 2 below,
> `qbeta_ck_cache.py` extracts ONE rung by inverting the target — verified
> 2026-09-04, it prints `c_4: residual below compute precision (0.00e+00) —
> ladder converged` and stops, because `Q_next = Q_prev·(1 + (Q_codata/Q_prev
> − 1)) = Q_codata` identically. `c_4 … c_7` are never computed there. That
> producer also **refuses to run** under convention D; the analysis script
> does not, which is how the stale prose survived.

> **🛑 CORRECTION (2026-08-16, owner-authorised; beans `qou-f09n` + `qou-cwin`).** Three claims above needed fixing, one of my own proposed fixes was itself wrong, and the two facts are worth separating.
>
> 1. **"`c_2 = -1` is PROVED Taylor-exact" — ONE half is wrong, and it is NOT the half the bean originally named.**
>    - **"Taylor" is UNDER-SPECIFIED, not false.** Bean `qou-f09n` (my own text) asserted that *"under the natural reading of 'Taylor' the `u²` coefficient is `−9/8`"*. That is **a** reading offered as **the** reading, and it is **retracted**. Measured symbolically: the `u²` coefficient of the **explicit-factor product** `Π_{k≥2}(1 + c_k u^k)` is exactly `c₂` — trivially, since there is no `k = 1` factor — so `c₂ = −1` **is** a Taylor coefficient of *that* series. It is `c̃₂ = c₂ − 1/8 = −9/8` only for the **full normalised model** `Φ(u)/Φ(0)`, i.e. with the cosine factor inside the series (`QOU.QBeta.normalisedQuadCoeff_eq`, sorry-free, and independent of the phase `α`). **So the fix is to say WHICH SERIES, never to delete the word.** Registry [§9i](docs/coordination/ck-dk-canonical-registry.md); the three live meanings (`c₂` / `c̃₂` / `c₂^even ≈ −7.4588`) are separated in §2 and in the notation register. **That third figure read `−8.006` until 2026-08-29 and was stale, not a different normalisation.** The producer's own upstream source of the exact rungs, `qbeta-c4even-exact-sseries.witness.json`, carries `−7.45876032789888019236780697835`, and a fresh run of `qbeta_c4even_ladder_reconstruction_probe` reproduces it byte-for-byte at BOTH pins — the `c_k^even` are exact s-series coefficients and are **anchor-independent** (only the `abs_ck_uk` products move, by ~4e-7). The downstream ladder witness had simply never been regenerated since it was first written: `−8.006` survived the convention C→D excision (`70d1ade383`) and a sweep whose own message claims it re-ran 154 producers (`119885a4c6`). Fixed in PR #6054, which regenerates that witness and pins the producer to proton.
>    - **"PROVED" IS wrong.** The Lean is `1 − b²ℏ⁴ = 1 − (bℏ²)²`, a one-line `ring` identity: it proves only that *re-reading* the N=2 factor in the ansatz form yields `−1`. Corpus-grepped: `N2_factor` is a bare `def` with **no** theorem deriving it — every use in `QBetaCategoricalPrecisionLadder.lean` merely `unfold`s it, and its provenance ("Kashiwara `f̃_1†f̃_1`") lives in a docstring. **"Structural" is the defensible word** (no fit, no CODATA, no q₀) and is what the source block itself claims; the compression to "PROVED" happened here, not there.
> 2. **"`N` is the truncation order chosen by target precision" does not describe the canonical producer.** `qbeta_ck_cache.py` extracts **one** rung by inverting the target; the residual at the next rung is then **exactly zero**, not merely below tolerance, so its guard fires and `c_4 … c_7` are **never computed** (`QOU.QBeta.greedy_rung_exact` / `greedy_later_rungs_vanish`, sorry-free). Whether some abstract ladder converges is a separate question this does not settle; the point is that no `N` is being *chosen* by an `ε` anywhere in the producer.
> 3. **The "3.47 %" is NOT stale — I checked, expecting it to be.** It is `|−2 − c₃|/2 = 3.4671 %`; the ladder witness's own `err_pct` field reports `3.3509 %`, which is the **same gap** normalised by the extracted `c₃ = −2.06934258` instead. Do **not** "fix" either number into the other. That this trap sits in the same banner as defect 1 is the point: **a quantity differing only by normalisation, mistaken for a discrepancy, is the exact error class this correction is about.** The cross-anchor swing quoted as "≈ 3 %" measures **2.3912 %** (proton-normalised; 2.4741 % normalised by the candidate `-2`) — **corrected 2026-08-31 from 2.3748 % / 2.4571 %, which were themselves on the superseded CODATA-2018 muon pin** (`qou-cds1`; `fca08de7d2` moved the pin to CODATA 2022 on 2026-08-22, and `1/u³ ≈ 1.6e6` turns a 1.451 ppb step on `m_μ/m_e` into 1.7e-4 on `c₃`). That "≈ 3 %" traces to a **superseded** muon `c_3 = -2.0097` (pre-#1422; today's is `-2.01986031` at the CODATA-2022 pin, `-2.02020024` at the CODATA-2018 one), and the corpus's `2.98 %` / `2.88 %` are that one stale gap under the two normalisations — resolved in [`qbeta_c3_crossanchor_swing_provenance_probe.py`](computations/qbeta/qbeta_c3_crossanchor_swing_provenance_probe.py) (3/3). Verdict unaffected. Report TIERED (`proved` / `near-match` / `fitted`), never binary wired/dropped — the four-session wire/un-wire flip-flop (#1452 ↔ #1479) came from conflating "N=3 beats 100× experimental" (true) with "c_3 = -2 is Taylor-exact" (false). **Canonical reference (read before any `c_k` wire/un-wire decision): [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).** Permanent fix is the Q_β Habiro element (parallel α_EM `[2]_q·(1−h²α)` in PR #1511). **2026-05-31 c_3 SETTLED** (PR #1580 verdict audit + flip-flop history table now at 6 entries in [`docs/coordination/1ppq-qbeta.md`](docs/coordination/1ppq-qbeta.md)); Li_2^q × spectral combiner refuted as mech #7 (PR #1609); Δtr_M bar-decomposition recorded as structural observation (PR #1615) — none of these wire to production.
>
> **🛑 CONVENTION LABEL (2026-08-15 ruling) — every number in this banner is
> CONVENTION-C-frame.** `c_2 = -1`, `c_3 = -2 = J_Hopf(q=1)`, the 3.47 % swing,
> and the whole `c_k` ladder were derived with the Markov parameter
> `z = √q/(q+1)` (convention C). The owner ruling of 2026-08-15 makes
> **convention D (`z = q³/(q²+1)`) canonical**. The values above are **correct
> for C** and are kept as recorded — they need *scoping*, not correction; do
> **not** "fix" them. **The ladder must be RE-DERIVED under D, and that is not
> a z-swap** — `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
> ([`MarkovZFullBarCondition.lean`](folio/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean),
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

> **🟧 OWNER RULING (2026-09-03, recorded from chat, verbatim):** *"The QOU should be
> on the full tower in the derivations to the standard model — should make use of the
> full tower even though what is observable is only order zero."* **Reading (agent's,
> not the owner's — see the open question below):** a derivation of an SM parameter
> must be carried on the fibre-level categorical object in full — the Hecke tower
> `H_n(q)` with the complete Frobenius pairing over all partitions, and all orders of
> the fibre-level `q`-expansion (the Habiro-element object of the fibre-vs-observable
> banner) — and the observable parameter is only its **order-zero archimedean
> rendering** at `q₀`. Consequences: (i) an attack that works only on the leading
> term, a single crossing, or a first-order ansatz is **structurally incomplete**
> under this ruling, whatever its residual; (ii) every per-term bean carries a
> *tower status* line (FULL-TOWER / ORDER-ZERO-ONLY / MIXED); (iii) the L2
> residual of an order-zero-only construction is not evidence about the tower.
> **Settled (owner, same day):** "full tower" means **both** — all `n` of the Hecke
> tower *and* all orders in `q`. Recorded in
> `docs/audits/2026-09-03-sm-26-term-status.md` §10.

## Precision goals (STRICT — read before any precision-affecting work)

The framework's headline precision goal has **two independent legs**.
Authoritative reference: [`docs/precision-goals.md`](docs/precision-goals.md).

| Leg | Target | Status |
|-----|--------|--------|
| **L1. Compute precision** | internal cross-method agreement ≤ 1 ppQ (10⁻¹⁵) at substrate q_0 | met — `_precision.py` default is **70 dps compute / 60 dps serialization** (10⁻⁶⁰ absolute truncation, guard 10). **Do not quote 65/50/10⁻⁵⁰** — that was this row until 2026-09-06 and had been stale since at least 2026-08-30 (bean `qou-0z4i`). Measure, do not quote: `python3 -c "import qou_substrate.precision as P; print(P.COMPUTE_DPS, P.OUTPUT_DPS, P.PRECISION_GUARD)"`. The change was a strict tightening — recomputed values agree with committed ones over their whole shared prefix, so no recorded result was invalidated; only this figure was wrong. It reached durable artifacts twice, most recently PR #6937, whose body names "65 dps" and "the 50-dps floor" and thereby **understates** the remaining optimisation headroom (70 → 60 is more than 65 → 50). |
| **L2. Per-observable accuracy** | for each predicted observable O: `σ_pred(O) ≤ σ_exp(O) / 100` | **1/6 scoreable met (`m_K/m_π` alone; `scoreable_total = 6` (α_em⁻¹ row added 2026-09-07, `d626761a34`; 238.3×)) — but that 1 is a truncation-fit + α_em-`sorry`-conditional, so 0/6 UNCONDITIONAL parameter-free (red-team 2026-08-22, see below)** — quote `beats_100x_scoreable`/`scoreable_total`, NOT `beats_100x_count=2`, which counts the calibration inputs `m_p` and `m_e` (corrected 2026-08-18) — see `per-observable-100x-status.witness.json` (`beats_100x_count=2`); the 5 missing observables (m_p, m_μ, Q_β, m_n, Δ_pn) — note **m_p misses by ~437× since 2026-07-04** (the fitted Habiro tower that landed it on CODATA to 0.0004 ppb was dropped; de-fitted round-trip +1.35 ppb — see [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md)) and **m_μ misses by 970.2× post-re-pin**, see below — and the Q_β/m_n/Δ_pn trio share a single root cause documented in [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md) |

**Key distinctions** (avoid agent confusion):

- **L1 ≠ L2.** A formula that is compute-stable to 50 digits (L1 met)
  can still miss its 100× experimental target by 10⁴ (L2 missed).
- **L2 is variable per observable.** Q_β target is 7.8 ppb; currently
  measured at **1.668e+8 ppb (2.139e+7× miss)** per the dashboard
  (`per-observable-100x-status.witness.json`, current with its producer at
  `scriptHash 98317bdcfb5c`) — the RULED base, `ε` = the Markov trace at
  `z_D = q³/(q²+1)`, on the **γγ-selected element `nuc11_interleaved`** and the
  canonical tower-summed `E₀`, with **zero `c_k` rungs**.

  > 🛑 **This read `4.316e+8 ppb (5.535e+7× miss)` until 2026-09-13, and that
  > figure was stale by TWO commits — the same prose-lag the element migration
  > left in the producer itself (PR #7283).** `4.316e+8` is `delta_S` at
  > **order-zero `E₀`** (−43.157 %), i.e. the cell the 2026-09-08 ruling entry
  > recorded and `22ff8a86d2` re-scored onto. Since then `173da443b6` made the
  > **tower-summed `E₀`** canonical (`delta_S` then reads 4.2594e+8 ppb,
  > −42.594 %) and `573b2ece24` migrated the scored **element** to
  > `nuc11_interleaved` (1.668e+8 ppb, −16.678 %). Net **2.588×**, and this
  > paragraph's own instruction — *"Quote the witness, not this paragraph"* —
  > is what catches it: the witness has carried 1.668e+8 since 2026-09-12.
  >
  > The three `delta_S` / `nuc11` cells differ only by which `E₀` and which
  > element, so **say both when you quote one**. The corresponding rows are
  > `m_n` **1.389e+5 ppb (2.718e+7×)** and `Δ_pn` **1.009e+8 ppb (2.327e+7×)**;
  > `m_μ` (970.2×) and `m_K/m_π` (0.195× ✓) are untouched by all of this.
  >
  > **The element is ruled in 6 of its 11 letters, not in all of them.** γγ
  > words have even length (`gammaGamma_length_even`, sorry-free) and
  > `nuc11_interleaved` is eleven letters, so the ruling reaches the 6-letter
  > core and provably not the 3-letter quark block (odd) or the 2-letter gluon
  > pair (both letters positive). Five letters remain census-derived against a
  > ruling that says not to use census (`qou-99qc`, still `todo`).
  >
  > **🟧 OWNER RULING 2026-09-13 — that is true of the γγ half ONLY, and the
  > SDP half reaches all eleven. The scored element FAILS it.** `qou-ales` has
  > two halves, and the paragraph above is about the *construction* half. The
  > scope of the *confinement SDP* half was put to the owner as a fork — does
  > it constrain only the 6 γγ core letters, or the whole word? — and the
  > answer is **(B) whole element**.
  >
  > 🛑 **THE READING NAMED HERE WAS WRONG, AND IT WAS MINE (corrected
  > 2026-09-14, bean `qou-99qc`).** This sentence read *"every Wedderburn
  > projection of the full 11-letter word must be `Matrix.PosSemidef`"*. That
  > is **reading 1**, and reading 1 is **parked**. The corpus enumerates three
  > PSD readings — 1 literal `Matrix.PosSemidef`, 2 symmetric-part PSD, 3
  > Frobenius positivity (`χ_λ(w) ≥ 0` on every block with `y_λ > 0`) — and
  > the owner selected **3** on 2026-09-12: *"try PSD condfinement 3 for now,
  > but keep 1 2 for later"* (bean `qou-ales`). The 2026-09-13 fork was
  > explicitly about **reading 3's** scope — the probe states it as *"(A)
  > reading 3 applies to the γγ-selected core only / (B) reading 3 applies to
  > the whole 11-crossing word"* — so **(B) moved the letter scope and did not
  > change the reading.** Live criterion: **reading 3, whole word.**
  >
  > **What that changes, and what it does not.** Under convention D
  > `y_(1³) = 0` — the Ocneanu weight of every shape with a third row vanishes
  > at `z = q³/(q²+1)`, unconditionally over any field with `q² + 1 ≠ 0`
  > (`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`,
  > sorry-free, general `n`; at `n = 3` specifically it is
  > `QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser`, which
  > derives `y₁₃ = 0` from the D pin plus the three moment equations) — so
  > reading 3 does **not** constrain the alternating block at all. Any
  > exclusion resting on the `(1,1,1)` sign is a reading-**1** exclusion, not
  > a live one.
  >
  > 🛑 **This cited `markovWeights_eq_jones_of_threeRow_eq_zero` until
  > 2026-09-26, and that lemma proves the CONVERSE (bean `qou-6moa`).** Read
  > its signature (`BraidsAndKnots/MarkovTraceTLUniqueness.lean:119`):
  > `hTL : y₁₃ = 0` is a **hypothesis** and `z * (q + qi) = q ^ 2` — convention
  > D — is its **conclusion**. So it gives **TL ⟹ D**, which is the direction
  > `docs/coordination/trace-convention-registry.json` correctly cites it for,
  > and the exact opposite of what this paragraph needs. It also carries
  > `hfaith : y₂₁ ≠ 0`, and that hypothesis is load-bearing rather than
  > decorative: the same file's `markovWeights_degenerate_root` proves that
  > dropping it makes the conclusion **false**, not merely unprovable (the
  > `y = (1,0,0)` trivial character at `z = q`). A lemma that *assumes* a form
  > of faithfulness on the two-row block cannot be evidence about the
  > three-row block vanishing. **The reading in this paragraph is unaffected —
  > only its citation was**, which is why this is a citation swap and not a
  > retraction.
  >
  > **The corpus already had the sentence, one file over.**
  > `QOU.BraidsAndKnots.FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu`
  > (`:179`) is the converse in the **same variable frame** — same `q, qi`, same
  > three moment equations — and its own docstring states the distinction
  > verbatim: *"The converse direction of
  > `markovWeights_eq_jones_of_threeRow_eq_zero`: there, `y_(1³) = 0` implies
  > `z·[2] = q²`; here, `z·[2] = q²` implies `y_(1³) = 0`."* Prefer it over
  > `conventionD_kills_antisymmetriser` anywhere the site is on the **fibre /
  > generic side**, because the two differ in typeclass and it is easy to swap
  > the wrong one in:
  >
  > | forward-direction lemma | typeclass | scope |
  > |---|---|---|
  > | `ocneanuWeight_conventionD_eq_zero_of_three_rows` | `[Field R]`, one hypothesis `q²+1 ≠ 0` | general `n`, on the actual Ocneanu weight |
  > | `threeRow_eq_zero_of_jones_ocneanu` | `[CommRing R] [IsDomain R]`, division-free | `n = 3`, generic domain |
  > | `conventionD_kills_antisymmetriser` | **`[Field R] [LinearOrder R] [IsStrictOrderedRing R]`** — an ORDERED field (`section PinningOrdered`) | `n = 3`, archimedean side only |
  >
  > The third is correct *here* (the PSD / reading-3 context is archimedean) and
  > is the wrong citation at a §7c generic-`R` site. Do not propagate it into a
  > Lean docstring on the fibre side.
  >
  > **MEASURED, and the defect is a CLASS — 14 reversed citations across 9
  > files, against 49 correct ones.** Population: **81 hits / 56 files**
  > excluding `__pycache__` (82/57 if the stale `.pyc` is counted; say which).
  > The reversal is concentrated in **one arc** — the `qbeta` reading-3 / e-cat /
  > D-ladder probes, the two beans they feed (`qou-99qc`, `qou-cds1`), two audit
  > docs, and the Lean twin of this very paragraph at
  > `QOU/Mass/AltCharShiftMultiset.lean`. **Nothing reader-facing (`content/**/*.md`)
  > is affected and no validator's verdict changes**; three witness `source` /
  > `detail` fields carry it with no machine consumer. Per-site table and
  > blast radius: bean `qou-6moa`.
  >
  > **And the claim survives the citation fix**: three further files assert
  > *"that vanishing IS convention D"* with **no lemma named at all**
  > (`qbeta_knot_operator_ilp_ohara_cost_probe.py:270`,
  > `qbeta_ecat_lp_radical_pairing_probe.py:30,207`), so a sweep keyed on the
  > identifier cannot see them. **Grep the phrase, not the identifier** — the
  > same detector-blindness class as everything in
  > `docs/audits/2026-08-15-detector-blindness-taxonomy.md`.
  >
  > Measured, `nuc11_interleaved` fails on `(2,1)` and `(1,1,1)` for **both**
  > nucleons (proton block dets `1.38249446339` / `-1.02197249381` /
  > `-0.739223570776`; neutron `1.1221068216` / `-1.02197249381` /
  > `-0.910762214553`). **Only the `(2,1)` failure binds** — `y_(2,1) =
  > 0.2473 > 0` — and it binds for both nucleons, so **the element rejection
  > STANDS on `(2,1)` alone** and nothing downstream of it moves. This
  > paragraph previously called `(1,1,1)` an exclusion *"already on record"*
  > with `(2,1)` *"additional"*, which inverts which of the two is doing the
  > work. **So the
  > three L2 rows above are scored on an element the selection rule that is
  > supposed to produce it rejects** — do not quote them as though the element
  > were ruled-in, and do not read the 6-of-11 paragraph as an all-clear for
  > the other five.
  >
  > The same ruling rejects every alternative in the one-letter quark family,
  > including the bar-odd survivors that a parity constraint forces
  > (`Q_β = 0.353415698` MeV, −54.825 %). **What replaces the element is an
  > owner decision and has not been taken**; the dashboard is deliberately
  > un-re-scored. Probes
  > `qbeta_qbeta_scores_a_difference_probe.py` and
  > `qbeta_bar_parity_forces_a_unique_quark_letter_probe.py`; bean `qou-99qc`,
  > which stays `todo` with the replacement as its first open item.

  This
  read "1279 ppb (164.0× miss) per the dashboard (fresh run 2026-05-31)" until
  2026-09-12, when item (iii) of the 2026-09-08 ruling was re-scored on owner
  authorisation (`qou-99qc`); that figure was convention-C on the retired
  `z = 1` cell. **Do not quote the new figure as convention D's accuracy** —
  no ladder exists on an admissible base (`qou-cds1`; 🛑 the phase `qou-pdix`
  is **not** what blocks it — see the 🛑 SCOPING NOTE (2026-09-14) at the end
  of the Q_β ruling block in §"Canonical derivation chain", and
  [`docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md` §5.1](docs/audits/2026-09-13-formb-probe-adjudication-and-cds1-state.md)),
  and a second re-score is authorised for when one does
  (`qou-iagg`). Quote the witness, not this paragraph — the Habiro-exact 5.7 ppb result was against the
  pre-re-pin (muon-anchored) q₀ and has not been refreshed since the
  2026-05-28 proton-anchor re-pin
  (see [`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`](docs/audits/2026-05-30-q0-repin-stale-witness-audit.md)).
  Absolute m_p target is 3 ppt (research-grade, below CAL-2 floor).
- **m_μ is no longer a met goal (2026-05-31 correction).** Before the
  2026-05-28 proton-anchor re-pin, m_μ was the q₀ *anchor* (err ≈ 0).
  Post-re-pin it is a *prediction* (m_e × (m_μ/m_e)_CODATA) and misses
  the 100× target by **970.2×** (211.2 ppb vs 0.2177 ppb target) per
  the dashboard. An earlier version of this table listed "4/7 met
  (… m_μ …)"; that was stale (the q0-repin staleness class).

  > **The `963.6× / 209.8 ppb` this line carried until 2026-09-04 was
  > itself an instance of that same staleness class — one CODATA
  > edition later.** Those are the **CODATA-2018** figures. The muon
  > anchor moved to CODATA 2022 on 2026-08-22 (`fca08de7d2`, owner
  > ruling), which shifts the residual `209.755 → 211.165` ppb and the
  > miss `963.6 → 970.2×`. Live source, both fields on one row:
  > `per-observable-100x-status.witness.json`, `rows[]` where
  > `obs == "m_mu"` — `err_ppb 211.2`, `target_100x_ppb 0.2177`,
  > `miss_factor 970.2`. **Quote the witness, not this paragraph.**
  > Drained on `main` at four sites here plus `docs/precision-goals.md`
  > and two content blocks; the ~17 hits left in `docs/audits/` and
  > `docs/coordination/` are **dated records of their own analyses and
  > were deliberately left** — same decision as the `4.66e6` drain
  > (`qou-3nva`). Beans `qou-silm` (finding) / `qou-m4au` (drain).
- **m_p dropped from "met" 2026-07-04.** Through 2026-07-04 the count was
  3/7 (m_e, m_p, m_K/m_π), but m_p "met" only because a fitted Habiro
  tower `(1+46u⁴)(1+4u⁵)(1−29u⁶)` landed it on CODATA to 0.0004 ppb. That
  tower was a muon-era fit left applied to the proton-pinned q₀ (a live
  +242 ppb regression) and was **dropped**; the honest documented-pin
  round-trip is +1.35 ppb, a ~437× miss. Full analysis:
  [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md).
- **🛑 The authoritative count is 1/6 SCOREABLE, not 2/7 (corrected
  2026-08-18; 1/5 → 1/6 with `scoreable_total = 6` (α_em⁻¹ row added 2026-09-07, `d626761a34`; 238.3×)).** `beats_100x_count = 2` counts **calibration inputs**
  alongside predictions. The dashboard already excludes `m_p` from scoring
  as an anchor round-trip ("the framework content cancels"), but **scores
  `m_e`**, whose `err_ppb` is not measured but *defined* zero — `m_e` is the
  CAL-1 input that fixes the MeV unit, so its ratio to itself is 1 by
  construction. That is the same argument `m_p` is excluded for, only
  stronger. Separating inputs from predictions, **1 of 6 scoreable
  predictions meets L2, and it is `m_K/m_π`** — the only *ratio* among the
  six. Quote `beats_100x_scoreable` / `scoreable_total` from the witness,
  **never** bare `beats_100x_count`. Full analysis:
  [`docs/audits/2026-08-18-mass-binding-accuracy-what-is-closeable.md`](docs/audits/2026-08-18-mass-binding-accuracy-what-is-closeable.md).
- **🛑 Even the 1/6 is inflated — the UNCONDITIONAL parameter-free count is
  0/6 (red-team 2026-08-22; denominators 5 → 6 on 2026-09-07).** The single "scoreable win" `m_K/m_π` is itself
  **not** a parameter-free prediction. Its derived core `√([3]_q·[4]_q)` (a
  legitimate ~0.1 % categorical postdiction of the strong ratio) misses this
  observable's own — unusually loose, 264 ppb — 100× target by **385×** on its
  own; the sub-100× result is manufactured by an EM correction
  `(α_em/π)·(3q²−1)/(2q²)` whose **truncation order beats the untruncated
  series** (chosen against the data — the same fit signature the `c_k` red-team
  caught) and whose `α_em` input is **conditional on an open Lean `sorry`**
  (Witten-κ Gram determinant). So `beats_100x_scoreable = 1` is the dashboard's
  arithmetic metric; the count of **unconditional, parameter-free** sub-100×
  predictions is **0**. State it as "1/6 scoreable — and that 1 is
  truncation-fitted + α_em-`sorry`-conditional ⇒ **0/6 unconditional**". Full
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

> **🟧 Extensive-term frontier + deuteron ruling (2026-08-29/30).** The "separate
> super-pairwise additive extensive object" above is the arc's one real open
> problem. It is now bounded by four sorry-free formalize-first results — the
> *scaling* is pruned from four directions; the *coefficient/mechanism* stays
> open (`qou-brng`). Do not re-attempt the excluded routes.
>
> - **Complete-graph coordination is excluded by saturation.**
>   `QOU.Mass.CoordinationSaturation` (lean-direct sorry-free): the complete
>   graph `M = C(A,2)` (the `z = A−1` law) gives `B/A = ε·(A−1)/2`, **unbounded**
>   (no plateau); bounded-degree gives `B/A = ε·k/2`, constant. Observed
>   saturation *forces* bounded degree and refutes `z = A−1` **structurally**
>   (not merely at ⁴He). Audit:
>   [`docs/audits/2026-08-30-coordination-saturation-formalized.md`](docs/audits/2026-08-30-coordination-saturation-formalized.md).
> - **Linear-chain coordination is excluded by arrangement-dependence.**
>   `QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff` — the chain
>   bond sum is arrangement-invariant iff `L_pp = L_pn = L_nn`; a nucleus has no
>   arrangement (scope-(b), bean `qou-m07y`). The saturation lemma's uniform-`ε`
>   is exactly that order-independent (physical) regime.
> - **Body-order recurrence depth ≥ 3 is forced**, and 3 terms cannot test it
>   (`QOU.MassTheory.BodyOrderRecurrenceDepth`).
> - **The connected 3-body cumulant of the multiplicative assembly is the third
>   Mayer coefficient of a lattice gas, and it is negative for every bond
>   triple — no threshold** (owner-adopted wording, 2026-09-12, PR #7198).
>   `b₃ = −φᵀ₃` exactly, where `φᵀ₃` is the third Ursell function of the
>   hard-core lattice gas on the nucleon sites with the interface-letter traces
>   `μ_e ∈ (0,1)` as pair weights (`QOU.MassTheory.UrsellPartitionFunctionB3`,
>   sorry-free); by the Ursell alternation `φᵀ₃ > 0`, so `b₃ < 0` for every
>   `f ∈ (0,1)³` — the `fpn > 2/3` escape of `MayerThreeBodySign.lt_of_b3_pos`
>   came from leaving `P₃` free and is never met. Scope (b), invariant = the
>   alternation. The 2026-08-30 "missing `(−1)^{n−1}`" reading is withdrawn:
>   restoring it is the same expansion at negative activity. Within Mayer a
>   positive term needs a bond factor above 1 (attractive channel; none in the
>   production word — measured in #7198 and independently in #7204, whose one
>   mechanism reaching `b > 1` is 4.0× short **against the SEMF asymmetry
>   coefficient `a_A` (23.7 / 5.963), NOT against `b₃`** — that arc is the
>   `δ ≤ 2 ln q` cap of #7165, a different quantity; scope a); the log assembly
>   is exactly pairwise (`b₃ = 0`). Zero-parameter magnitudes at the live chain
>   bonds: `−1.2277` MeV (³H) vs AME `+1.8081`, `−0.7973` MeV (³He) vs
>   `+1.0443`. Audit: `docs/audits/2026-09-12-ursell-partition-function-for-b3.md`,
>   beans `qou-rwhv` / `qou-rraz`.
>
>   🛑 **Those two magnitudes, and the chain bonds `μ_e` they come from, are on a
>   SUPERSEDED word (owner, 2026-11-15).** The γγ rule now covers the nuclear bond
>   letters, so the single-crossing interface letters `g_{3k+2} + d_k` of
>   `atom_braid_word_3A` are not canonical. The figures stay as records; the Lean
>   theorems above take generic bond weights and still stand. Redo waits on a
>   γγ-selected word per nucleus (#7876). Record:
>   `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`.
>
>   🛑 **"A bond factor above 1" is NECESSARY, NOT SUFFICIENT — do not read the
>   sentence above as "find an attractive letter and the sign follows"** (owner
>   ruling 2026-09-12, PR #7226, bean `qou-q8vl`). The production `A = 3` word is
>   a **chain** (`atom_braid_word_3A` lays `A−1` interfaces in a line), so `φᵀ₃`
>   collapses to a **product**, `φᵀ₃ = g₀₁·g₁₂` — and a product does not change
>   sign when **both** factors flip. Measured: reflecting every live bond to
>   attractive leaves `b₃` **byte-identical** (`−0.293278112721` ³H,
>   `−0.190468485549` ³He). A two-bond chain needs **exactly one** bond above 1,
>   i.e. a **sign-mixed** pair (`b3corpus_chain_pos_iff`).
>
>   Two further traps on this bullet. **The chain is covered by NEITHER standing
>   theorem**: `b3corpus_neg` needs all three bonds strictly inside `(0,1)` and a
>   chain's absent bond sits at exactly `f = 1`; `wMult_b3_nonpos` is the
>   **equal-bond** case and the chain bonds differ by ~0.105 — use
>   `QOU.MassTheory.B3SignOneRoot.b3corpus_chain_neg`. And **a bond above 1 is not
>   the only escape**: `AggregatorConvexity.b3Agg_nonneg_of_convexOn` gives
>   `b₃ ≥ 0` from an aggregator convex through the origin with every bond still
>   inside `(0,1)` (bean `qou-82mc`).
>
>   **The required sign-mixed pattern is the two-nucleon spectrum.** Both `A = 3`
>   chains impose the same one — `g_pn` opposite to both like-pair bonds — which,
>   since `B = −α·log μ > 0` iff `μ < 1`, reads *the unlike pair binds and the
>   like pairs do not*: deuteron bound, diproton and dineutron unbound. The live
>   model binds all three (dineutron **most** bound), so `b₃ > 0` and the correct
>   two-body isospin structure are **one condition, not two**. Both derived bond
>   families are excluded from supplying it — production letters by `d ≤ 0`
>   (`SingleCrossingAlwaysBinds.interface_mem_Ioo`), isospin projectors by an
>   **identity**, `μ₊ + μ₋ = 1` (`InterfaceScalar.mu_sum_eq_one`), so an
>   attractive channel forces its partner to `μ < 0` where the log is not real.
>
>   **Do NOT "fix" this by adopting `σ²`.** It does reach `μ = (q⁴+1)/(q²+1) > 1`
>   for every `q > 1`, but the topological argument that selects it assigns it to
>   the *distinguishable* pair, which bean `qou-kj4v` records as running backwards
>   (it **binds the diproton and unbinds the deuteron**); choosing it because it
>   yields `b₃ > 0` is selection against the target. And **`μ(σ^m)` does not
>   alternate by parity** — measured `m = −2…+8`, `μ > 1` at `m = 2, 4, 5, 6, 7, 8`,
>   so `+5` and `+7` are odd. Audit:
>   `docs/audits/2026-09-12-b3-sign-one-root-and-the-insufficient-escape.md`.
>
> **Deuteron leg — 🟧 OWNER RULING A (2026-08-29):** the deuteron knot is the
> canonical braid closure (trefoil / Hopf, `Vol = 0`); **the deuteron binding is
> NOT a hyperbolic-volume term** (Bloch volume leg proved 0, PR #5242). The 6₂
> census assignment (`Vol = 4.40`) is retired; `qou-e5jf` unblocked. Sourcing the
> binding from the **Gram/Frobenius pairing (⟨g,g⟩) + confinement SDP** was tested
> (`deuteron_real_sdp.py`, H₆) and is a **scope-(a) negative**: the diagonal Gram
> SDP is degenerate and 0 of 6 off-diagonal encodings derive the binding — the
> only non-zero result (`2.22456607`) is the AME value fed in as the constraint
> (circular). Same intensive/extensive gap. Audits:
> [`docs/audits/2026-08-29-deuteron-knot-owner-decision.md`](docs/audits/2026-08-29-deuteron-knot-owner-decision.md),
> [`docs/audits/2026-08-29-deuteron-binding-via-gram-sdp-compute.md`](docs/audits/2026-08-29-deuteron-binding-via-gram-sdp-compute.md).
>
> **Open positive target (`qou-brng`):** the linking-vs-self-energy amplitude
> assignment — why the binding multiplier is the *mutual* (coordination) linking
> count while the mass multiplier is the *self*-linking weight `lw`. The
> exact-`ℏ_q²` saturated-fraction value is **suspect numerology** (volume-defect
> route refuted); do not chase it. Consolidated arc ledger:
> [`docs/coordination/2026-08-29-bk-crossing-mass-binding-arc-reassessment.md`](docs/coordination/2026-08-29-bk-crossing-mass-binding-arc-reassessment.md).

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

> **🛑 OWNER RULING — the muon pin is CODATA 2022. The frozen value is retired.
> RULED 2026-08-22; IMPLEMENTED 2026-08-28; re-confirmed 2026-08-30.** The
> original wording is a sibling session's record of the owner's 2026-08-22
> ruling: *"2022 CODATA better than 2018. A --> CODATA 2022."* It was put to the
> owner again on 2026-08-30, against the three-values measurement below, and
> re-confirmed — *"C."* then *"CODATA 2022 for muon"*.
>
> **🛑 The 2026-08-30 half of this block was written as though nothing had been
> done yet. It had. Corrected the same day — read this before acting on the
> paragraphs below.** The ruling was dated 2026-08-30 (it is 2026-08-22), and the
> anchor was described as still frozen at A. `fca08de7d29` (2026-08-28, *"muon
> anchor -> CODATA 2022 (owner ruling): derive it, stop the self-certification"*)
> had **already migrated it**, and that commit is an ancestor of the one carrying
> the stale description. The corpus-grep checklist would have caught it — so
> would `git log` on the named file.
>
> **What the tree actually holds, measured on `main` `3a919ad14fe`:**
>
> - `computations/q-pinning-50-digit.witness.json` carries
>   `1.109978595642739046681795129380001752700065561029011556974045769999095`
>   — that is **C**, not A.
> - `computations/audits/muon_pin_stored_vs_live_gate.py`: stored and live agree,
>   **gap 0.0 ppb** (0.0 σ against σ(q₀) = 1.22335 ppb).
> - `q0_anchor_consistency_audit.py`: **`Q0_FLIP` = 1**, and it is
>   `hadron-knot-table.witness.json` alone, still carrying **A**.
>
> **The fix was to DERIVE, not to re-freeze**, which is why it did not repeat the
> 2026-08-19 breakage: `q_parameter`'s ideal/muon branch now takes q from
> `q_muon_at()` over `constants.MASS_RATIO_MU_E_STR`, so the witness records a
> value it did not choose. Previously `q_pinning_50_digit` was listed `ideal_muon`,
> so `q_at` was rebound *for that very producer* and it wrote back the value it
> had just read — **the anchor certified itself.** A also disagreed by 1.4 ppb
> with the ratio the same witness declares in its own `calibration_inputs`.
>
> `computations/audits/muon_pin_three_values_probe.py` establishes that **three
> different numbers are all called "the muon q₀"**, diverging at the 13th
> significant digit — five orders of magnitude above the framework's own 1 ppQ L1
> target, and inside the ~11.6 ppb μ–p separation the two-pin vocabulary exists to
> keep straight. Re-derived independently 2026-08-30 at `mp.dps = 60`, with
> `Vol(4₁) = 2·Cl₂(π/3) = 2.02988321281930725004240510855`:
>
> | | `m_μ/m_e` | `q₀ = 1/(1 − √(Vol(4₁)/(m_μ/m_e)))` |
> |---|---|---|
> | **A** former frozen pin (retired) | *(none — see below)* | `1.1099785955573347…` |
> | **B** CODATA 2018 | `206.7682830` | `1.10997859555418057528159407961` |
> | **C** CODATA 2022 | `206.7682827` | `1.10997859564273904668179512938` |
>
> **The ruling's reason is the dataset constraint, and it is measured rather than
> aesthetic: CAL-1, CAL-2 and CAL-3 must come from one experimental dataset.**
> Inverting **A** through its own defining relation gives `m_μ/m_e =
> 206.768282989315111`, which matches **neither published figure** — it sits
> strictly between them (5.17e-11 relative from 2018, 1.40e-9 from 2022). So A is
> not that derivation at *any* CODATA vintage and cannot be in a common dataset
> with anything; the tempting reading *"A is just the older CODATA"* is
> **measurably false**. Between B and C, the live table already decides:
> `constants.py` serves `MASS_RATIO_MU_E_STR = 206.7682827  # CODATA 2022` from
> the same `codata.py` that supplies `M_E_MEV` for CAL-1, so **C is the only
> choice that does not also require rolling CAL-1 back**.
>
> **What is already done:** both the live derivation path *and* the
> anchor-defining witness `computations/q-pinning-50-digit.witness.json` are at C
> (`fca08de7d29`, 2026-08-28), and `cfe73b8eb5f` drained the resulting flips
> `Q0_FLIP` 83 → 34. **Do not "migrate the anchor" — that step has run.**
>
> **🛑 WHAT REMAINS IS STILL NOT A BULK SWEEP, and the reason is on the record.**
> The anchor step above was done deliberately and by derivation. Re-pinning that
> witness *as a step in a bulk pass* is a different act, and it is what took
> `main` red on 2026-08-19: both anchors
> collapsed to one string, **262 correctly-stamped muon witnesses flipped to
> `Q0_FLIP`** (`Q0_OK` 654 → 392), and every `ideal_muon` producer hard-failed —
> including, circularly, the one that regenerates the anchor. `q0_repin_sweep.py`
> carries an `ANCHOR_DEFINING` exclusion for exactly this; **do not remove it** and
> do not re-pin that file as a step in a bulk pass. Note also that C is a **live**
> derivation over a CODATA input, so unlike A it moves whenever that table is
> updated — accepted deliberately as the price of reproducibility from a published
> source. Migration scope and staging: bean `qou-tekx`.
>
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
>   **Measured surface, 2026-08-24.** The `computations/` side is no longer
  unmeasured: `scripts/convention-c-producer-audit.py` reports **26 actionable**
  sites after the `regime_scanner` fix — 14 live producers, 11 probes, 1 in the
  **generated** `qou-mass/_internal/` mirror — against 14 further sites that are
  *deliberately* C-named comparisons and are not defects. Two cautions for
  whoever drains it. First, the mirror site
  (`qou-mass/src/qou_mass/_internal/_li_2_q_util.py:312`) must **not** be
  hand-edited; its source is `computations/_li_2_q_util.py`, which carries the
  same C at lines **302 and 312** and is load-bearing (`vol_density_*`), so
  changing it moves real numbers. Second, the detector labels `qou-mass` a
  **"SHIPPED PACKAGE"**, which contradicts this document's own measured row
  above — it is **not on PyPI** (404) — so do not treat that label as a reason
  to leave the site alone. The `content/` side was measured the same day:
  of 12 grep matches only **5** carried live unscoped C, the other 7 being
  correct records; 4 of the 5 are migrated and the fifth is a refutation whose
  scope under D is being established separately.

  **Status 2026-08-16, corrected 2026-08-24.** The detector now scans return
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
>   this correction did **not** identify it.
>
>   **IDENTIFIED AND CLOSED 2026-08-24.** It is
>   `tools/pyhecke/python/pyhecke/regime_scanner.py:94`, inside `scan_h2_molecule`'s
>   `v_std`: `z = mp.mpf(1.0) / (mp.sqrt(q) + mp.sqrt(qi))`, which is
>   `√q/(q+1) = z_C` — unlabelled, no comparison rationale, no registry row.
>   Migrated to `z_D = q³/(q²+1)`; the detector now reports **26** actionable
>   sites and no `tools/pyhecke` row. The migration is behaviour-safe rather
>   than merely believed to be: the module has **zero importers** in the repo
>   (the only other hit is a sibling worktree's copy of itself) and **no
>   committed witness** references `scan_h2_molecule` or `rank_drop`, so the
>   crossings it reports change without invalidating any recorded number.
>
>   **The `.lean` surface has never been counted, by this or any other tool
>   (measured 2026-08-26, bean `qou-cxjq`).**
>   [`scripts/convention-c-producer-audit.py`](scripts/convention-c-producer-audit.py)
>   walks the tree four times and every one is `rglob("*.py")` — lines 635, 760,
>   785, 930. There is no `.lean` path in it. Its numbers are correct and
>   correctly scoped; they are simply not *about* Lean, and nothing else covers
>   Lean either. So do not read any figure in this section as an `.lean`
>   all-clear. **Nor is there one elsewhere in this document:** the single
>   "**0** in `.lean`/`.ts`" claim above belongs to the **Λ vs Cl₂ naming**
>   guard (`qou-zdz5`), a different defect class — the two were conflated once,
>   by shape rather than subject, in a bean about detector blindness.
>
>   Measured directly with
>   [`scripts/lean-markov-convention-audit.py`](scripts/lean-markov-convention-audit.py)
>   (which the producer audit structurally cannot do), the Lean
>   Markov-parameter surface is **22 convention-C *definitions* across 18 files,
>   under 3 spellings**, against **24** in convention D — roughly half the
>   Markov-parameter definitions in the Lean tree. **Quote `defs`, not total
>   sites:** the scanner reports 150 sites, but a `q³/(q²+1)` inside a proof
>   *mentions* a convention while one inside a `def` body *defines* it, and
>   conflating them inflates the count several-fold. **Not all 22 are defects**: the same script triages
>   them **14 actionable / 8 deliberate**, where deliberate means the site
>   announces itself (a `_legacy` name, an `@[deprecated]`, or a docstring saying
>   convention-C / comparison / historical). That is evidence of *intent*, not a
>   clean bill — a deliberate C object can still be cited as though it were D. An earlier hand-verified pass in
>   the audit below reported 7 across 6 files and was an undercount. And **`markovZ` is five
>   declarations spanning both conventions** — three C (`markov-trace-factorization`,
>   `QBetaCategoricalPrecisionLadder`, `HoefsmitV21CosSymmetrization`) against two
>   D (`MarkovBondRule`, `y-lambda-recipe-from-partition`). Same name, opposite
>   values: `z_C(q₀) = 0.49932…` vs `z_D(q₀) = 0.61268…`. Only **3** of the 7 use
>   the square-root-variable disguise (`u/(u²+1)` or `s/(s²+1)` with `u² = q`);
>   the other **4 write `Real.sqrt q` in plain sight** and are trivially
>   greppable — the surface is unscanned, not invisible-in-principle. Note also
>   that the Tier-2 migration which replaced `Real.sqrt` with a generic
>   `markovZ (u : R)` **did not change the convention**: it removed the square
>   root, which was its stated goal, and left C harder to see. Table and
>   per-site verdicts:
>   [`docs/audits/2026-08-26-convention-c-in-lean-and-the-markovz-overload.md`](docs/audits/2026-08-26-convention-c-in-lean-and-the-markovz-overload.md).
>
>   **🛑 RE-MEASURED 2026-08-29 (PR #5972) — every figure in the paragraph above
>   has moved, and one has moved in a direction worth noticing.** Run the same
>   two scripts before quoting any of them.
>
>   | quantity | recorded above | measured 2026-08-29 |
>   |---|---|---|
>   | `.lean` convention-C **defs** | 22 across 18 files | **14** |
>   | of those, actionable / deliberate | 14 / 8 | **0 / 14** |
>   | `.lean` convention-D defs | 24 | **38** |
>   | `computations/` actionable (shape audit) | 26 | **9** (7 registry-blocked on `qou-cds1`) |
>   | `markovZ` declarations | 5 (3 C, 2 D) | **13** (3 C, 10 D) |
>   | `content/` live unscoped C | 5 of 12 grep matches | **3** |
>
>   **The Lean surface reaching 0 actionable is real progress, not a detector
>   getting weaker** — the C defs that remain all announce themselves. But
>   `markovZ` went the OTHER way: 5 declarations became **13**, still spanning
>   both conventions. The paragraph above names `markov-trace-factorization` and
>   `QBetaCategoricalPrecisionLadder` as two of the three C `markovZ`; **both are
>   now D**. The live C three are `HoefsmitV21CosSymmetrization` (the
>   convention-neutral kernel), `EigenphaseCarrierVacuity`, and
>   `q-beta-cos-resummation`. So a name that spans two conventions keeps
>   accreting declarations while the convention question underneath it is being
>   settled — the overload is a naming defect that migration does not fix, and
>   it is tracked as bean `qou-961o` with the rename proposal and the
>   `lean`-direct verification recipe.
>
>   **RESOLVED 2026-08-29 (session tender-keller).** The three C `markovZ` were
>   renamed so bare `markovZ` now means convention D uniformly:
>   `EigenphaseCarrierVacuity` and `q-beta-cos-resummation` → `markovZC`;
>   `HoefsmitV21CosSymmetrization`'s convention-neutral kernel → `cosKernel`.
>   All three are file-local (no cross-file consumers) and `lean`-direct clean;
>   the 10 D declarations keep the `markovZ` name (one convention for the bare
>   name — re-measured 2026-08-29: **9 bare `markovZ`, all D**).
>
>   **But "no collision" is wrong, and the rename is what created the new one.**
>   `markovZC` (**upper** C) is convention C; `markovZc` (**lower** c), at
>   `categorical-chain-convergence-mechanisms.lean:83`, is convention **D**.
>   They differ by one letter's case and mean opposite things — `0.4993203342`
>   vs `0.6126880371` at the proton q₀, 0.113 apart. A case-insensitive grep
>   cannot separate them. Resolve any `markovZ*` to its definition body before
>   reasoning about its value; the suffix is now actively misleading rather
>   than merely absent. Bean `qou-961o` (reopened scope).
>
>   **RESOLVED 2026-08-29 (#6015), and the docstring was the worse half.**
>   `markovZc` is renamed to bare `markovZ` (convention D, matching the other
>   ten), so `markovZC` has no case twin. Underneath the collision its
>   **docstring** read *"z = 1 / (√q + 1/√q)"* — convention C — above a body
>   computing `q³/(q²+1)`. Name and docstring agreed with each other and both
>   were wrong; only the body was right. Docstring corrected to the body.
>   **Agreement between two labels is not evidence about the third thing.**
>
>   **And the `computations/` figure is NOT a measurement of the C surface.**
>   26 → 9 is real drain, but both numbers count only what a shape-matcher can
>   see. Measured by VALUE with
>   [`scripts/convention-c-value-audit.py`](scripts/convention-c-value-audit.py)
>   (new, PR #5972 — it evaluates each binding at two sample points instead of
>   matching its shape), `computations/` holds **85 confirmed convention-C
>   bindings**, of which **21 are reported by the shape audit NOWHERE** — not
>   actionable, not deliberate, not at all. All 21 use the sqrt-variable
>   spelling (`1/(sq + 1/sq)` or `u/(u²+1)` with the variable equal to `√q`).
>   That is the 14th entry for the blindness taxonomy and it hides BOTH buckets
>   at once, so draining the shape audit to zero would not end the excision.
>   Confirmed from the other side: five of those sites were registered in
>   `blocked_on_rederivation` on 2026-08-29 and the audit's printed count did
>   **not** move, because it never counted them. Live per-tree value counts —
>   `computations/` 85, `qou-mass/` 1 (the generated mirror of the deliberate
>   `_wenzl_constants_convention_C_HISTORICAL`), `tools/` **0**, `content/` 0.
>   Remainder tracked as `qou-t9r1`; the four sites that cannot be migrated by
>   substituting `z_D` at all are `qou-pmkh`.
>
>   **The posture below still does not change**, and the remaining 26 are the
>   reason. Closing one shape does not
>   close the class —
>   [`docs/audits/2026-08-15-detector-blindness-taxonomy.md`](docs/audits/2026-08-15-detector-blindness-taxonomy.md)
>   catalogues **fifty-eight** rows (re-counted 2026-10-12 with the anchored regex after #7583 merged as row 57 and #7734 as row 58, both renumbered on merge; previously fifty-six, re-counted 2026-10-10, twice in one day as `main` appended a row each time; 46 landed 2026-09-14
>   in `81a8ac98b9` after this line last said forty-five, then 47 and 48 landed,
>   49 is PR #7401's — which arrived numbered 46 and had to be renumbered on
>   merge — then PR #7318's two merged in at 50-51, main took 52-54, and **55 is
>   PR #7553's**, the prediction path that does no arithmetic, which arrived
>   numbered 50 and had to be renumbered on merge for the same reason #7401 did.
>   So **re-count before citing any number here, including this one.**
>   **Measure it with `grep -cE '^\| [0-9]+ \|'`, anchored.** A naive
>   `^\| [0-9]` reads **57**, because it also matches a second table's two rows
>   — and the trap is sharper than a two-row overcount: on `main` before this
>   merge the naive regex read 51, which was exactly the true count at an
>   earlier moment, so the wrong command and the right one have each been
>   correct at different times and neither can be checked against this sentence.
>   🛑 **And main's own version of this line read "fifty-one" against a table
>   that already held 54** — measured at the merge, anchored: main 54, resolved
>   55. A count line stating the lesson about count lines was itself three
>   behind, which is the fourth time this sentence has gone stale while warning
>   you not to quote it. 🛑 **Then it went stale AGAIN the same day, on the same
>   branch, for the same reason** — `main` appended a 55th row while the branch
>   held a 55th of its own, so the branch row became 56: measured at that merge,
>   anchored main 55 / resolved 56 (naive 57 / 58), and `main`'s own tail line in
>   `docs/audits/2026-08-15-detector-blindness-taxonomy.md` read **49**. Twice in
>   one day is the signal: this is not a number that goes stale occasionally, it
>   is a number that is stale by default. And the
>   groups
>   below split the FIRST THIRTY-FOUR seven ways — only the first group is
>   about conventions at all. **Rows 35-51 are NOT in this list**, and the
>   notes that follow describe only 35-46; 47-51 are in the table and are
>   unsummarised here: 35 (the
>   identifier's alphabet), 36 (the direction of the cast), 37 (the numerator
>   is an applied argument), 38 (the value audit's variable resolution),
>   39 (the freshness is on the wrong object), 40, which is the first row
>   in the table whose failure runs the OTHER way — an over-matching grep that
>   fails to a false **COVERED** rather than a false all-clear, so it ends the
>   search instead of prolonging it — 41 (the query's character encoding), and
>   **42-44, which are one arc and the sharpest group in the table**: 42 is the
>   body SHAPE of a self-assuming projection (an applied SINGLE field was
>   unseen, so the case where the conclusion is universally quantified — the
>   NORMAL case — was invisible by construction, 26 → 42 hits), and 43 is scan
>   SCOPE on the `--review-ledger` write path, found while fixing 42 and
>   **destroying 106 of 329 committed adjudications in the process**. Both are
>   repeats of a repair the corpus had already made once: 42's fix exists one
>   arity over as `APPLIED_TUPLE_PROJECTION`, and 43 is row 33 a second time on
>   the same API, where the `--json` path refuses a partial scan and the ledger
>   path never got the rule. **44 is the third**, and it is the one to
>   internalise: the ledger seeds only candidates whose exemption text matches
>   the literal `triage pending`, and a sibling emit site spells its reason
>   `derivation pending` — so 34 candidates were exempted into silence rather
>   than queued, while a code comment eight lines above the bug asserted they
>   "still enter the review ledger". Rows 33, 43 and 44 are one lesson said
>   three times: **a queue is only a queue on the paths that actually write to
>   it, and an exemption is only a deferral if the thing it defers to can see
>   it.** Do not read an empty ledger, or a clean `--check-ledger`, as evidence
>   about the corpus.
>
>   **46** is the newest — **the PROOF TERM'S GRAMMAR**: `lean-self-assuming-audit.py`
>   had a rule for a bare binder and one for a single qualified projection, and
>   the character `⟨` occurred NOWHERE in the file, so every CONJUNCTIVE form of
>   a self-assuming projection — Lean's anonymous constructor — was invisible.
>   Landed by a sibling in `81a8ac98b9`; see
>   [`2026-09-14-conjunctive-self-assuming-blind-spot.md`](docs/audits/2026-09-14-conjunctive-self-assuming-blind-spot.md).
>
>   **45** is about an ALGEBRAIC signature rather than a
>   spelling: `q**2 - 2*q - 1`, the factor identifying the retired Q_β base,
>   is also written with the **absolute value pre-resolved**
>   (`2*q + 1 - q**2`, legitimate since `q₀²−2q₀−1 < 0`, so no `abs()`
>   appears) and in **Horner form** (`q*(q - 2) - 1`) — a 45 % undercount,
>   29 → 42 files, the corrected set including `qbeta_ck_cache.py`, the
>   canonical `c_k` producer. Its reusable half is a rule about AUDITS and it
>   is row 44's twin from the other side: 44 is an exemption the queue cannot
>   see, 45 is a **calibration check that certifies itself**. The audit's was
>   a hardcoded `check(..., True, ...)`; replacing it with one that resolves
>   known consumers to their actual bucket and FAILS on a miss is what exposed
>   the blindness. **An audit that self-certifies its calibration cannot
>   discover its own blind spot** — 29 would otherwise have shipped with a
>   clean 3/3 beside it.
>
>   **46-47** are the newest and are one pair: *what a clean float64 signal
>   does NOT tell you.* **46** is the one to internalise, because it is a
>   blind spot in GREP rather than in an audit — reviewing `mpf(str(Q))` /
>   `mpf(Q)` by pattern, where `Q` is assumed to be the float64
>   `q_parameter.Q`. **`from q_parameter import Q_MP as Q` rebinds that
>   name**, so byte-identical call text is a float64 cap in one file and a
>   harmless decimal round-trip in another: measured, 3 of 8 casimir sites
>   were never caps, and the round-trip loss is **4.406e-70** against a cap's
>   **2.725e-17**. `f64_into_mpmath_audit.py` gets this RIGHT — it tracks the
>   import `asname` — and I was one step from filing a blind spot against a
>   `completed` bean (`qou-tj98`) and the ledger resting on its tier exiting
>   0. **The audit reads bindings; grep reads spellings.** **47** is the
>   corollary on the other gate: the **raw-float64 ratchet is evidence about
>   the RECORDED value, never about the computation** —
>   `casimir-macdonald-probe` read **0** on it while its producer computed
>   every value from a double, and fixing that moved 183 of 405 fields.
>   Corollary for ranking: its baseline says 196 and its live count was 0, so
>   **rank off disk, never off the baseline**, which never moves down by
>   design. Beans `qou-lz8f` / `qou-840k`, PR #7318:
>
>   - **1-16** — detector-blind *spellings* of convention C.
>   - **17-21** — the `qou-t9r1` family. These blind an *exemption* or a guard
>     rather than a detector: a labelled two-arm comparison whose D arm is a
>     call, a sibling scope, a derived closed form, a Lean declaration, or
>     unreachable to an mpmath-only guard, so each is reported as a leak
>     forever.
>   - **23-24** — `qou-4lbh`, the Lean statement-carrier arc: a defect that is
>     an **absent** field rather than a wrong one, and a carrier written as
>     `def … : Prop` instead of a `class`/`structure`.
>   - **22, 25, 26** — the NO-FLOAT64 / witness arc, and the three of them are
>     ONE root worth naming: *the interesting text is assumed to be a `str` in
>     the AST, at the call.* 22 read a call's operands positionally and so
>     examined 13 % of a corpus that writes 87 % of its calls with keywords
>     (`MEASURED: 0` against a true 56). 26 could not see a witness key written
>     as a keyword argument, because that key is an identifier. 25 could not see
>     a literal reaching an assertion through a **list slot** two hundred lines
>     up. Two different audits, two days apart, same assumption.
>   - **27-32** — `qou-dke6` / `qou-sof3`, and unlike every group above these
>     are **six blind spots in ONE detector**, found one at a time while it was
>     used. All six are about the SHAPE of the data around the fields, never
>     the fields themselves: a hoisted **wrapper** (54 of 241 matches, each
>     solve counted twice and the hoisted copy manufacturing a phantom
>     "no primal"), a **column-wise aggregate** whose `y0_star` is a list not a
>     scalar, a **prefixed key** (`lp_x_star_str`) reported as absent while the
>     record carried two primals, a **numeric proxy for a structural fact**
>     (`duality_gap != 0` taken to mean a solve happened — wrong on 6 of 9,
>     since a closed-form dual's gap is 0 by construction and four producers
>     never call a solver at all), an **SDP matrix primal** where a vector was
>     assumed, and a **threshold cliff** (62 flagged at 0.96, 7 at 0.98, with
>     the one confirmed positive ranking 59 of 146). The corrections ran
>     105 → 56 and 84 → 44 → 15 → 3 → 0, **every one making the problem
>     smaller**, and one of them nearly reached the owner as a contract change
>     that would have turned 29 correct records into violations.
>   - **33** — `qou-3ral`, and it is its own group: the guard is installed on
>     one of an API's several **write paths**. `WitnessBuilder` has three
>     routes into the anchor vocabulary — `stamp_staleness_metadata`
>     (guarded), `save(extra)` (a bare `witness.update`), and `wrap_legacy`
>     (payload keys emitted verbatim by `build()`) — and the one live
>     off-vocabulary producer travels the third. Not about data shape at all,
>     which is why it is not in the 27-32 family.
>   - **34** — `qou-t0wm`, and its own group because it blinds a detector by
>     what an author **NAMED** a quantity rather than by shape or write path.
>     An identifier matching `delta`/`err`/`resid` that also reaches both sides
>     of a comparison was taken to mean the quantity IS the residual. An
>     **error-propagation formula** mentions the measured quantities for
>     exactly the same reason the residual does —
>     `borromean_mass_MeV_err = sqrt((ratio_err·m_e)² + (ratio·m_e_err)²)` is a
>     1σ propagated uncertainty and entirely correct. The discriminator is that
>     **a residual is a difference**: requiring a `Sub` in the provenance keeps
>     the `qou-tol0` positive (`delta = M_derived − M_obs`) and drops the class.
>     Two things make it worth its own row. It was found by running the audit
>     **on a fix made with that audit** — the repaired producer was still
>     reported blocking. And the tier had fired on **nothing** on `main`, so
>     the false positive was latent: **zero hits is not the same as verified
>     sound**, and the audit doc asserted the second having measured only the
>     first.
>
>   Several were found *by* detectors written to catch the previous blind spot —
>   row 26 in the output of the audit that introduced it. Quote the split, not
>   the total, because folding the last ten into the C figure inflates exactly
>   the number this note exists to keep honest.
>   (This line has been stale SIX times — *thirteen* at 15 rows, *sixteen*
>   at 17, *eighteen* at 21, *twenty-two* at 26, *thirty-five* at 39 — and on
>   the fourth fix I first
>   wrote "twenty are spellings", miscounting the very split I was adding. On
>   the fifth, the agent adding rows 25-26 called them "the 17th and 18th"
>   in a commit, a bean and a PR comment before re-counting. On the sixth the
>   agent adding row 40 wrote "they split EIGHT ways" in the same edit that
>   fixed the row count — inventing a group count while correcting a row count,
>   when the group list had in fact stopped covering the table at row 34.
>   **Re-count the table; do not trust this sentence, including this
>   parenthesis.**) So: **treat
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
> the μ₃ Fréchet probe took `y_λ` from the then-muon-built cache while
> evaluating `χ_λ` at the proton `q₀` — an 11.54 ppb layer separation (=
> the μ–p substrate tension itself), ~1e-7 relative on the result. See
> [`computations/deltalambda/mu3_anchor_consistency_probe.py`](computations/deltalambda/mu3_anchor_consistency_probe.py)
> and [`docs/audits/2026-08-07-mu3-door-status-consolidated.md` §4ter](docs/audits/2026-08-07-mu3-door-status-consolidated.md).
> *"then-"* is load-bearing: that cache was re-derived and re-pinned to proton
> in the 2026-08-09 convention-D cascade, so the incident is history and the
> **discipline** is what generalises. See the closed-case note below.
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
>
> **Two producers bypass the accessor and read the cache file directly** —
> `probe_theta_carry_binding.py` and `delta_lambda_empirical_tabulation.py`.
> They get D-at-proton, which is correct; noting them so a future reader does
> not conclude the accessor is the only path to that file.
> Independent evidence for the same correction:
> [`docs/audits/2026-08-23-y-lambda-cache-agents-md-staleness.md`](docs/audits/2026-08-23-y-lambda-cache-agents-md-staleness.md).

The substrate modulus q₀ has **one** value but **two** documented pins
(authoritative corpus:
[`observations/three-calibration-discipline.md` §3](folio/quantum-observable-universe/observations/three-calibration-discipline.md),
[`observations/epistemic-status-of-calibrations.md`](folio/quantum-observable-universe/observations/epistemic-status-of-calibrations.md),
[`mass-theory/rem-qstar-decay-sector-q0.md`](folio/quantum-observable-universe/mass-theory/rem-qstar-decay-sector-q0.md) — the decay-sector point `q*`, which is **conditional on (H1)** and is **NOT** an independent third determination; see registry §9f):

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
| **Experimental / Physical-Observations** | **m_p/m_e** (0.017 ppb; re-pin 2026-05-28) | **9.49σ on the RATIO / 9.70σ on the MASS** — say which (see the note below); misses L2 100× by **970.2×** (211.2 ppb) — the μ–p substrate tension |

> **🛑 "9.5σ" and "9.70σ" are the SAME residual against DIFFERENT σ, and
> neither is stale — do NOT sweep one into the other (measured 2026-09-14).**
> The residual is one number, `err_ppb = 211.20`. It is divided by two
> different published uncertainties, and this table cell used to carry one of
> each with no label, which is what makes the sweep look obviously right:
>
> | denominator | σ | t | source |
> |---|---:|---:|---|
> | **σ on the RATIO** `m_μ/m_e` | 22.247 ppb | **9.4934σ** | `qou_substrate.constants.MASS_RATIO_MU_E_ERR = 4.6e-6` over `206.7682827` |
> | **σ on the MASS** `m_μ` | 21.768 ppb | **9.7022σ** | `per-observable-100x-status.witness.json` row `m_mu`: `sigma_exp_MeV 2.30000e-6` over `codata_MeV 105.658375496`, published as `sigma_exp_ppb 21.77` |
>
> **The ratio σ is the right denominator for a residual on the ratio
> relation** `m_μ/m_e = Vol(4₁)/ℏ_q²`, which is what CAL-2 actually asserts;
> the mass σ is what the L2 dashboard scores against, and every *dashboard*
> figure — `211.2`, `21.77`, `target_100x_ppb 0.2177`, `miss_factor 970.2` —
> is mass-denominated. So a cell quoting `970.2×` alongside a bare `9.5σ` is
> mixing frames, even though both halves are individually correct. Quote the
> denominator, or quote both.
>
> **This was already adjudicated and the adjudication was already durable** —
> `epistemic-status-of-calibrations.ts`, `authorNotes` (bean `qou-silm`):
> *"Different denominators, not a stale figure — do not 'reconcile' them."*
> It was invisible from here, which is why it is restated here.
>
> **It is also not a CODATA-edition artifact**, the other tempting reading:
> at CODATA 2018 the ratio figure was **9.534σ** (recorded in
> `mu-p-residual-two-readings.ts`), at CODATA 2022 it is **9.4934σ**. The
> 2026-08-22 re-pin moved it by 0.04σ and it rounds to 9.5 on both sides, so
> the edition change did not make `9.5σ` wrong.
>
> Every live content block that says `9.5σ` says it of the **ratio**, in a
> sentence that names the ratio or the 22 ppb, and is correct as written:
> `epistemic-status-of-calibrations.md`, `mu-p-residual-two-readings.md`
> (which shows `σ_exp ≈ 2.2e-8` inline), `three-calibration-inputs-context.md`.
> Leave them.

The proton re-pin is a **precision substitution within the same
overdetermined H¹ datum — NOT a 4th calibration and NOT a change to
CAL-2.** (CAL-1 = m_e; CAL-2 = 𝔇_β, proxy m_μ/m_e; CAL-3 = 𝔇_π, proxy
m_π; Q_β = ℏ/𝔇_β is the **CAL-2 proxy**, not CAL-3 — see the decay-width
cheat-sheet ruling above.) Pin on the most precise ratio so the unavoidable ~11.6 ppb
theory residual lands where least significant (proton-anchor → 9.49σ on the
muon ratio; muon-anchor → ~1.4e4 σ on the proton ratio — that figure read "~4000σ" until
2026-09-04 and was the CODATA-2018 one, computed against σ(m_p/m_e) = 0.06 ppb;
at the live 0.017 ppb the same 243.86 ppb miss is 1.4e4 σ, and the two-line rule
above already carries the tighter σ).

**STRICT rules:**

1. **Every precision / accuracy / prediction artifact** — the L2 100×
   dashboard, `per-observable-100x-status`, accuracy audit docs,
   "N/7 met" counts — **must report m_μ as the proton-anchored
   prediction (970.2×, FAIL), never "exact / ~0 ppb / MET".** An m_μ
   value ≈ CODATA computed at the muon q₀ is the CAL-2 calibration
   tautology ("equality by construction"), **not** an accuracy win.
   **The same rule applies at CAL-1, and was not being applied.** `m_e` is
   the CAL-1 input that fixes the MeV unit; its `err_ppb` is *defined*
   zero, not measured. Scoring it as a "beat" is the identical tautology
   this rule forbids one line above. The canonical L2 count is therefore
   **1/6 scoreable** — `m_K/m_π` alone; `scoreable_total = 6` (α_em⁻¹ row added 2026-09-07, `d626761a34`; 238.3×) — **not** 1/5, 2/7, 3/7 or 4/7.
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
     **`1.1099785956427390466817…`** (−11.6 ppb) — see the 🛑 correction
     below; this read `1.10997859555733471…` until 2026-08-30 and that
     value has been **retired since 2026-08-22**. The **counts below are
     still the counts**: they describe witnesses computed under the OLD
     anchor, which is exactly the population the migration is about — do
     not read them as counts of the live value. It fed ~72 producers /
     **870** witnesses — the canonical 3-CAL (muon) derivation witnesses.
     (Re-measured 2026-08-15 and again 2026-08-16 over the 2941 tracked
     `computations/*.witness.json`: **870** carry the muon fingerprint —
     **801 muon-only** and **69 also carrying the proton pin**. The
     previous figure here was "~840"; the error was **low, not
     stale-high**. A both-pin witness is either a deliberate comparison
     or a layer straddle — see the straddling hazard above; triage is
     bean `qou-cds3`.)

     > **State the METHOD when you quote this number, or the next reader
     > will "correct" it downward (added 2026-08-26).** "Carries the muon
     > fingerprint" is ambiguous *in this corpus specifically*, because
     > [`muon_pin_three_values_probe.py`](computations/audits/muon_pin_three_values_probe.py)
     > establishes that **three different values are all called "the muon
     > q₀"** — the then-canonical frozen pin `1.1099785955573347…`
     > (**retired 2026-08-28**; C is canonical now), and the
     > lepton-tower derivation at CODATA 2018 (`…55541805…`) and 2022
     > (`…56427390…`). They diverge at the **13th significant digit**, so
     > the choice of prefix length silently selects which of the three you
     > are counting:
     >
     > | match on | counts | at 2026-08-16 | at 2026-08-26 |
     > |---|---|---|---|
     > | `1.109978595` (10 digits) | **all three** | **871** | **477** |
     > | `1.1099785955573347` (full) | ~~the canonical pin only~~ **the RETIRED pin — see below** | 468 | 149 |
     >
     > 🛑 **The second row's label is now WRONG, and the table is missing its
     > largest population (corrected 2026-08-30; found by bean `qou-silm`,
     > which did the diagnosis and deliberately did not edit this file —
     > the CODATA-2018 row below is the one part it does not carry).** On an
     > owner ruling — *"2022 CODATA better than 2018. A → CODATA 2022"* —
     > commit **`fca08de7d2` (2026-08-22)** re-derived the anchor witness, so
     > *(A sibling correction on `main` dated this **2026-08-28**. That is the
     > `computedAt` of a LATER regeneration, `83bab99730`; the VALUE changed on
     > 2026-08-22, verified with `git log -- <file>`. Bean `qou-silm` made and
     > corrected the same slip. Do not revert the date — reading a `computedAt`
     > stamp as the date a value changed is the same error class as reading a
     > `scriptCommitSha` as provenance.)*
     > `1.1099785955573347…` has been the **retired** pin for eight days and
     > the live canonical value is **`1.1099785956427390466817…`**. The row
     > above tells you to count the retired literal *while calling it
     > canonical*, which inverts its own warning: an agent following it counts
     > a dead value and reports it as the live one.
     >
     > **Re-measured 2026-08-30 with the recorded method** (`git ls-tree` on
     > `origin/main`, 3237 tracked `computations/*.witness.json`):
     >
     > | match on | is | count |
     > |---|---|---|
     > | `1.109978595` (10 digits) | all muon spellings | **403** |
     > | `1.1099785955541805` | **CODATA 2018** | **257** |
     > | `1.1099785956427390` | **CODATA 2022 — the LIVE canonical anchor** | **96** |
     > | `1.1099785955573347` | the **retired** self-certified pin | **40** |
     > | 10-digit hit, no full muon literal | unaccounted spellings | 17 |
     >
     > **That 40 is a count of FILES CONTAINING THE STRING, not of stale
     > pins — do not read it as 40 stale witnesses.** Bean `qou-silm`
     > independently reports *"exactly one witness"* still on the old pin, and
     > **both are right about different questions**: of the 40, only **4**
     > carry the literal in a `q0Value`/`q` *field*, and only **one**
     > (`hadron-knot-table.witness.json`) as the top-level `q0Value`. The
     > other three are payload data — a `scan[]` point, a cross-anchor
     > `residual_evaluations/muon_q0`, an `across_q[]` array — i.e.
     > deliberate multi-q records, not stale pins; the remaining 36 carry it
     > in prose, `description` or provenance. This is the same
     > string-match-vs-semantics gap the row above it warns about, one level
     > down, and it is why every row here names its method.
     >
     > **CODATA 2018 is 64 % of the muon population and the two-row table
     > cannot see it at all** — it is neither "the canonical pin" nor
     > distinguishable from the rest under a 10-digit match. That is the
     > sharper defect here: the old table's two rows do not partition what
     > they are counting, so *both* readings under-describe the tree. Quote
     > four rows, or say which single literal you matched.
     >
     > **The shift itself is small; do not confuse it with the μ–p tension.**
     > retired → live is **0.0769 ppb**, and it moves μ–p from 11.5371 to
     > **11.6141 ppb**. The witness drain for it is *already scoped* under
     > bean **`qou-3f7a`** /
     > [`2026-08-29-q0-muon-anchor-repin-drain.md`](docs/audits/2026-08-29-q0-muon-anchor-repin-drain.md)
     > (83 `Q0_FLIP` + 165 NEW drift sites, all at that same −0.0769 ppb) —
     > **do not duplicate it.** That audit cites this document nine times and
     > never flags that this passage is itself stale, which is why the
     > correction lands here rather than there.
     >
     > **This does NOT weaken rule 1 of the sweep constraints** ("NEVER re-pin
     > an anchor-defining witness"). That rule binds *agents*; the owner
     > re-pinned it deliberately, by ruling, having established that the old
     > value was **self-certifying** — `q_pinning_50_digit` is listed
     > `ideal_muon`, so `q_parameter` rebound `q_at` for that very producer and
     > it wrote back the value it had just read.
     >
     > The **870** above is the ten-digit reading and is correct. Measured
     > with the same script at both ends (`git ls-tree` on each revision,
     > so the denominator moves with the tree: 2947 → 3102 tracked). The
     > migration has genuinely run — **871 → 477 under the recorded
     > definition** — but it has *not* fallen to ~149, and an agent
     > measuring only the canonical literal will think it has.
     >
     > Recorded because that is exactly what happened on 2026-08-26: this
     > figure was measured at 149, called "stale by 5.8×", and was one
     > edit away from being replaced by a number answering a different
     > question. Quote the number **with its prefix**, or re-measure and
     > say which you used.
     These remain **valid as recorded** (they are what they say they are)
     but are **no longer the default an agent should reach for**; see
     rule 4 for the migration posture.
3. **Recurring bug to watch (bean `tnjb`):** a dashboard/witness that
   reads a **muon-q₀** `muon_check.m_mu_pred_MeV` (≈ CODATA, ~0 ppb)
   and scores it as the m_μ *prediction* silently flips m_μ FAIL→MET.
   The committed `per-observable-100x-status.witness.json`
   (m_μ ≈ 105.6583978, 970.2×) is the **canonical** value; a fresh run
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
   > **🟧 REAFFIRMED AND SHARPENED 2026-08-30, for the `qou-p77d` tranche
   > specifically.** The 32 q-dependent producers of `qou-p77d` had been held
   > as "an owner decision, 32 times". They are not. The owner ruled, in these
   > words:
   >
   > > *"it should be proton unless it is an explicit comparison / discussion
   > > on CAL 123 math ideal or so."*
   >
   > This is the 2026-08-15 directive restated, with the exception set made
   > explicit. **Proton is the default; there are exactly two exceptions**, and
   > a producer qualifies only if it can be shown to be one of them:
   >
   > - **(E1) An explicit proton-vs-muon comparison** — the producer's PURPOSE
   >   is to measure the difference between the two pins (the μ–p substrate
   >   tension). `mu_substrate_tension_audit_100dps` is the type case. Such a
   >   producer needs BOTH pins and belongs under `physical_proton` with a
   >   per-process override, per constraint 3 below.
   > - **(E2) The ideal CAL-1/2/3 mathematical layer** — the producer is
   >   *about* the canonical calibration triple as mathematics (CAL-2 = 𝔇_β
   >   with proxy `m_μ/m_e`), not about evaluating an observable. The muon pin
   >   is what that layer MEANS, so pinning it to proton would not migrate the
   >   producer, it would misstate the calibration. `q_pinning_50_digit` is the
   >   type case and is anchor-DEFINING besides (constraint 1).
   >
   > **The burden is on the exception, not on the default.** A producer is
   > proton unless someone can name which of E1/E2 it is and why. "It has
   > always been muon", "its witness says muon", and "it is in the
   > `ideal_muon` list" are NOT reasons — that list is what is being migrated.
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
   - **Do NOT do it by emptying `ideal_muon` in the manifest.** The
     tempting one-line version of this migration is to move every stem
     from `ideal_muon` to `physical_proton` in
     [`computations/q0_anchor_manifest.json`](computations/q0_anchor_manifest.json)
     and declare the end state reached. **That is not a migration, it is a
     disabling.** `q_parameter.py` selects the anchor by
     `if _stem in _man.get("ideal_muon", [])`, so an empty `ideal_muon`
     means no producer ever resolves to the muon anchor again — and the
     anti-corruption guard that hard-fails when the muon anchor cannot be
     established (`"Refusing to fall back to proton silently"`) can no
     longer fire for any of them, because none of them ask for it. The
     relabel also decouples the declaration from reality across every
     listed producer at once: every witness they have already emitted was
     computed at the muon pin and stays that way, now labelled proton.
     Proposed in PR #5049 and deliberately NOT merged (#5315).
     **And the list does not end at zero.** Measured 2026-08-24: three
     producers refuse a proton run *by design* — `atomic_tr_m_mpfr_50dps`
     (dual-layer, emits one witness per layer),
     `he4_stage2_ranking_seminormal_xcheck` (asserts the muon prefix off
     the anchor-defining witness), and `cross_check_trM_1ppb` ("L1
     cross-check must run under the MUON q0 pin") — several more hold the
     muon value as a deliberate reference, and `q_pinning_50_digit`
     defines the anchor. A run that drove `ideal_muon` to zero would be a
     bug, not a completed migration.
   - **Measured cost of getting this wrong, 2026-08-19.** The sweep ran
     producer-by-producer, as it should — and still took main RED, because
     it regenerated `computations/q-pinning-50-digit.witness.json` at the
     proton pin. That witness is not a *consumer* of the muon anchor, it
     **is** the anchor: `witness._q0_value_for_anchor("muon")` reads
     `derived_50_digit.q` out of it. Both anchors collapsed to the same
     string, 262 correctly-stamped muon witnesses flipped to `Q0_FLIP`
     (`Q0_OK` 654 → 392), and every `ideal_muon` producer hard-failed —
     including, circularly, the one that would regenerate the anchor. Fixed
     in `2e4745448d` by restoring the witness and adding an
     `ANCHOR_DEFINING` exclusion list to `q0_repin_sweep.py`. The guard did
     its job; what was missing was an exclusion list. Read that commit
     before touching this sweep.
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
| "QA report / .qa.json / multi-reviewer / hash staleness / per-block audit sidecar" | `folio-assistant/cat-harness-tools/pipeline/qa-sweep.ts` + `qa-staleness.ts` (CLI), `folio-assistant/cat-harness-tools/schemas/sdlc/block-qa.ts` (schema) | collaborator |
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
| `qou` | `folio/quantum-observable-universe/lean/` | `QOU` |
| `ugb` | `folio/unital-groebner-bases/lean/` | `UGB` |
| `fred2005` | `folio/fred2005-formal-groups/lean/` | `Fred2005` |

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

- The `[key]` must match a bibliography key exactly (case-sensitive): a
  `folio/references/<key>.json` file, loaded by `folio/schema/references.ts`.
  (`references.bib` is auto-generated from `references.ts` — the `export-bibtex`
  shortcut was dropped in the miga migration, pending re-wiring).
- If no published reference exists, use `[leitner2026]` (the self-citation) and cite chapter/section. The legacy `[manuscript]` key was renamed to `leitner2026` at every site on owner ruling 2026-11-15.
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
  ([`folio/pipeline/lean-vacuity-axiom-audit.ts`](folio/pipeline/lean-vacuity-axiom-audit.ts)).
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
   [`QOU/FluidDynamics/q_bkm_criterion.lean`](folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_bkm_criterion.lean).

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
[`ConditionalClasses.lean`](folio/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean)),
never a bare `True` or an empty body. An unproved primary is honestly
represented by a **content-bearing class with no instance** (the open
state); do not fabricate a trivial instance to "close" it.

**Enforcement.** `folio/pipeline/lean-vacuity-axiom-audit.ts` adds
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
[`ReebEpsilon.lean`](folio/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/ReebEpsilon.lean)
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

The `TodoItem` type is defined in `folio-assistant/cat-harness/schemas/types.ts` for reuse,
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

`BlockBase.authorNotes?: AuthorNote[]`.

> **✅ LIVE STATE (verified 2026-09-05): all four kinds accept every base
> field. `authorNotes` on a `prose` / `table` / `equation` / `diagram` block
> WORKS — write it.** The rest of this box is the history of a defect that is
> now closed in the product; read it for the mechanism, not for the state.
>
> Verified by **parse**, not by grep: `ProseSchema` / `EquationSchema` /
> `DiagramSchema` / `TableSchema` each `safeParse` a block carrying
> `authorNotes`, `defines`, `cites` and `computation` and **retain** every one.
> The fix is `folio-assistant` **`a117daa`** (2026-09-03, *"Four block kinds
> restated BlockBase instead of extending it"*), confirmed an ancestor of that
> repo's `main`.
>
> **🛑 Why this box opened for months with the opposite claim, and why the
> ordering matters.** The two paragraphs that used to lead were a 🛑 asserting
> *"every block kind accepts it is FALSE, and the field is dropped in
> silence"*, retracted nine lines below. An agent reading top-down met the
> false claim first and stopped — the same *heading-contradicts-its-own-body*
> defect this document already had to fix once, in the Phase-4 merge-gate
> table. **The live state now leads; the history follows.** Superseded text,
> kept because the mechanism is still worth reading: four content-block kinds
> had zod schemas declared as standalone `z.object({...})` rather than
> `BlockBaseSchema.extend({...})`, so they restated a *subset* of the base
> fields; a zod object is non-strict, so a note written on one of those blocks
> validated clean and **vanished**. `folio-assistant` granted `authorNotes` to
> all four by hand on 2026-08-24 (bean `folio-assistant-5nle`), which fixed
> that one field and left the mechanism — see the structural note below.
>
> **🛑 And the "fixed" rows in the table below were written AHEAD of the
> evidence.** That table is dated 2026-09-03 and states its basis as
> `folio-assistant` `93e476b`. `93e476b` is dated **2026-08-31** and does
> **not** contain `a117daa` — so at the moment those rows were written, the
> fix they call *"fixed — folio-assistant#164"* had not landed. The rows are
> true **today**, and this line is not a retraction of them; it is a note that
> they were forward-looking claims about an unmerged PR, which is precisely
> the *"fixed on a branch, not in the product"* move that bean `qou-3v8h`
> refused to close on. State what has landed, or say it has not.
>
> **This document could not have known, and that is the reusable lesson: the
> validator you ran is the validator in the clone.** The count that produced
> the table below was taken against a `folio-assistant` checkout at
> `e1030e8` — itself already behind `main`. The same qou tree, validated
> against `main`, reports **six** warnings of which **five are invented field
> names** and exactly **one** is a schema gap. Re-measure with
> [`scripts/setup-folio-assistant.sh`](scripts/setup-folio-assistant.sh) and
> `git -C folio-assistant log --oneline -1` before quoting any figure here.
>
> **Live state, measured 2026-09-03 against `folio-assistant` `93e476b`:**
>
> | class | count | status |
> |---|---|---|
> | invented field names (`is_mathematics` ×3, `probe`, `consumers`) | 5 | **fixed** — qou #6501 |
> | schema gap: `prose:knot-periodic-table` drops `computation` | 1 | **fixed** — folio-assistant#164 |
> | `authorNotes` dropped | **0** | fixed upstream 2026-08-24 |
>
> 🛑 **That table measured a platform THIS REPO DOES NOT RUN, and the row above
> is not true here (corrected 2026-09-06, bean `qou-lq8g`).** `93e476b` is
> unpinned `folio-assistant` `main`. The platform this repo actually validates
> against is the SHA in
> [`.folio-assistant-pin`](.folio-assistant-pin) — **`428ca5c`, dated
> 2026-08-23 09:52** — and the upstream grant `affcec4` (*"schema: grant
> `authorNotes` to prose, equation, diagram and table"*) landed **after** it.
>
> Measured against the pin on 2026-09-06, on a clone
> `scripts/setup-folio-assistant.sh` had just created:
>
> | class | count against the PIN |
> |---|---|
> | `authorNotes` dropped | **5** |
> | `computation` dropped (`prose:knot-periodic-table`) | **1** |
>
> — the same six fields, in the same blocks, that the superseded text below
> lists. Both halves are true and describe different platforms.
>
> **The re-measure instruction three lines up is what produces the
> disagreement, not what resolves it.** It says to re-run
> `scripts/setup-folio-assistant.sh` before quoting any figure — and that
> script installs the **pinned** platform, so an agent following it lands on
> `428ca5c` and sees five warnings a corpus-grep tells them were fixed.
>
> **Do NOT "fix" this by pointing the setup script at `main`.** The pin is
> deliberate, and its rationale is in that script's own header: the checkers
> live in the platform repo, so every count this repo quotes is a function of
> **two** inputs, and defaulting to `main` let two agents on the same corpus
> commit measure different numbers and each be right (bean `vbase`). Moving the
> platform is meant to be a reviewable one-line commit to
> `.folio-assistant-pin`, not a silent consequence of when you cloned.
>
> **So the useful rule is: name the platform whenever you quote a count.**
> "validate: N issues" is meaningless without it, and this row is what that
> looks like when it goes wrong — the same class as everything else this
> section documents, one level up.
>
> Advancing the pin past `affcec4` would make the all-clear true here, and is
> its own PR: 169 commits of checker changes move every count this repo quotes,
> which is exactly the reviewable decision the pin exists to force.
>
> Of the six, only one has a downstream consumer: `knot-periodic-table`'s
> `computation`, its link to its producer. The other five are author-facing
> prose.
>
> Superseded — the five `authorNotes` rows the table below names
> (`fine-structure-data`, `tm-interaction-completeness`,
> `millennium-bounds-via-surreals-intro`,
> `hecke-log-decomposition-table-data`,
> `q-beta-form-a-n1-symbolic-table-data`) were described here as *"no longer
> dropped"*. Against the pin they still are.
>
> **The structural cause outlived the one-field fix, which is why it is worth
> reading the rest of this box.** That grant added `authorNotes` to the four
> schemas *by hand* and left them restating the base. Measured a week later:
> `defines` was still absent from all four, and `cites`, `simulator` and
> `computation` from three. `defines` is the sharp one — §4c *mandates* it for
> every glossary term and the `defterm-declared` rule reads that array, so on
> those kinds a term could not be declared at all. folio-assistant#164 makes
> the four **extend `BlockBaseSchema`** and adds a guard
> (`scripts/tests/block-base-fields.test.ts`) that fails when any block schema
> falls behind the base, so the next field cannot be forgotten one kind at a
> time.
>
> Superseded text follows.
>
> **Six authored fields are being dropped in this corpus right now**, and two
> of them are substantive:
>
> | block | field | what is lost |
> |---|---|---|
> | `braids-and-knots/hecke-log-decomposition-table-data` | `authorNotes` | multi-paragraph caveat recording that the table has **no source block** and why the dangling `uses[]` was dropped rather than guessed |
> | `nuclear-interactions/q-beta-form-a-n1-symbolic-table-data` | `authorNotes` | — |
> | `observations/fine-structure-data` | `authorNotes` | — |
> | `appendix-surreals/millennium-bounds-via-surreals-intro` | `authorNotes` | — |
> | `appendix-transfer-matrices/tm-interaction-completeness` | `authorNotes` | — |
> | `appendix-knot-periodic-table/knot-periodic-table` | `computation` | the block's link to its producer |
>
> **The wider hazard is not `authorNotes`.** Those same four kinds also drop
> **`defines`** and (all but `prose`) **`cites`**. No block hits those today,
> but §4c *mandates* `defines` for every glossary term, so the first `prose`
> or `table` block to register one will have it silently discarded and the
> glossary gate will not fire. `cites` dropping means bibliography extraction
> would silently miss those kinds.
>
> **A second class, same symptom, different cause.** The validator also
> reports five *invented* field names no schema declares anywhere —
> `is_mathematics` (×3), `probe`, `consumers`. Those are authoring errors
> rather than a schema gap, and they are dropped just as quietly.
>
> **You only see any of this if the validator is current.** These warnings
> come from an "Unknown field" check that a stale `folio-assistant` clone does
> not have; the same tree reported **1** issue before the clone was
> fast-forwarded and **14** after. Run
> [`scripts/setup-folio-assistant.sh`](scripts/setup-folio-assistant.sh) and
> check the clone is not behind before trusting a clean validate.
>
> **The fix was in `folio-assistant`, not here, and it has LANDED** — all four
> schemas now extend `BlockBaseSchema` like the other eleven (`a117daa`, on
> that repo's `main`). The advice this paragraph used to give — *"do not put an
> author note on a `prose`, `table`, `equation` or `diagram` block"* — is
> **withdrawn and inverted**: write the note, it is kept. Verified by parse on
> 2026-09-05, and locked upstream by two regression tests
> (`scripts/tests/block-base-fields.test.ts`, which fails when any block schema
> falls behind the base, and `scripts/tests/schema-ts-zod-parity.test.ts`), so
> the next field cannot be forgotten one kind at a time the way `defines`,
> `cites`, `simulator` and `computation` were.
>
> **The one thing that still bites is the CLONE, not the schema.** Everything
> above is a statement about `folio-assistant` `main`; your validator is the
> validator in *your* checkout. Measured this session: a qou tree validated
> against a clone **169 commits behind** reported all six of these fields as
> dropped — a defect that no longer exists. Before quoting any figure from this
> box, or filing anything from a validate run, refresh and say what you ran
> against:
>
> ```sh
> bash scripts/setup-folio-assistant.sh
> git -C folio-assistant fetch origin main && git -C folio-assistant log --oneline -1
> ```

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
  [`folio/quantum-observable-universe/notation/notation-register.md`](folio/quantum-observable-universe/notation/notation-register.md)
- **Collision avoidances + conventions**:
  [`folio/quantum-observable-universe/notation/notation-collisions.md`](folio/quantum-observable-universe/notation/notation-collisions.md)

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
- Three partition-weight families — Markov `$y_\lambda$`, q-deformed Wedderburn `$w_\lambda(q)$`, classical Plancherel `$w_\lambda(1)$` — are **distinct** at `$q \neq 1$` and coincide at `$q = 1$`; never conflate. (**`$\tilde w_\lambda$` is RETIRED** by owner ruling 2026-08-16: bare `$w_\lambda$` now means `$w_\lambda(q)$`, and the classical measure is its specialisation `$w_\lambda(1)$`, not a separate symbol. This line said `$\tilde w_\lambda$` until 2026-09-05.) **Never write a normalisation claim on bare `$w_\lambda$`**: `$\sum_\lambda w_\lambda(1) = 1$` is exact, and `$\sum_\lambda w_\lambda(q)$` is **not** — measured 0.987 / 0.982 / 0.982 / 0.991 / 1.111 / **1.517** at `$n = 3/4/5/6/9/12$` at the proton `$q_0$`. That defect is **structural, not a q-integer-convention artifact** (the deformation breaks Burnside `$\sum_\lambda (f^\lambda)^2 = n!$`; the asymmetric convention is *worse* at five of those six `$n$`), so it does not cancel across different `$n$` and distorts any **cross-atom** metric — `$n = 3A$`. Cross-atom consumers need a **self-normalised** family and must **declare which one they used**. **🛑 For Φ_k that family is NOT `$d_q^2/D^2$`, and the choice is NOT open.** This line read *"Cross-atom consumers use the self-normalised `$d_q^2/D^2$` (Reshetikhin–Turaev/Verlinde). Whether `$\dim_q^2$` is even the right numerator … is **open**, bean `qou-oots`"* until 2026-11-15 (correction written 2026-09-14 on PR #7402, ported to the current layout on this date). **The owner RULED on it 2026-09-05** — verbatim *'molien. do the two arm reporting'* — and **re-affirmed it 2026-09-08**: the canonical **Φ_k** weight is **Molien** `$f^\lambda q^{-\kappa}\dim_q(\lambda)/[n]_q!$`, and `$d_q^2/D^2$` is kept as a **labelled comparison arm** — not a fallback, and not what an undecided consumer should reach for. **The arms disagree materially:** under Molien the Frobenius-reciprocity mechanism gains **+21.4 %** over its own baseline with best knot `$5_2$`, where `$d_q^2/D^2$` gives **+1.7 %** with best knot `$6_1$` (bean `qou-oots`). **Scope — do not widen it:** the ruling is about **Φ_k**; outside it the family is a **declared choice**, never an implicit `$d_q^2/D^2$`. **The `$\dim_q$` convention is dragged along:** the Molien identity holds under the **fake-degree** convention and **fails** under the symmetric one (measured `$n = 2..5$`, [`confinement_filtration_vs_gbdepth_probe.py`](computations/audits/confinement_filtration_vs_gbdepth_probe.py) §0), so `$\dim_q$` alone is ambiguous. Ruling record: bean `qou-oots`; [`2026-09-08-l2-1ppq-research-program-gaps.md`](docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md) row D2, which records that listing the choice as open *"was written as open by mistake"*. **What is still open in `qou-oots` is the α_EM-axis triage, not the choice.** The identity's own status: 🛑 **That identity is NOT `$\sum_\lambda f^\lambda \dim_q(\lambda)$` — this clause said so until 2026-10-11. It IS now proved for every `$n$`** (`QOU.MathlibExt.NormalizedSumUnconditional.molienSum_eq_qFactorial`, general `$n$`, `$1 < q$`, no `sorryAx`; via `MolienFakeDegreeGeneralN`). The scope paragraph below describes the earlier explicit-`$n$` file and is kept as history. The Lean is [`QOU/MathlibExt/MolienFakeDegree.lean`](folio/quantum-observable-universe/lean/QOU/MathlibExt/MolienFakeDegree.lean) (sorry-free; the only `sorry` in it is the word inside a docstring), and it states `$\sum_{\lambda \vdash n} f^\lambda \, q^{-\kappa_\lambda} \dim_q(\lambda) = [n]_q!$` — **with a per-partition `$q^{-\kappa_\lambda}$` factor** that the old wording dropped. At `$n=3$` the theorem writes those weights out as `$q^{-3}, 1, q^{3}$` on `$[3], [2,1], [1^3]$`. Verified symbolically against `computations/substrate/young_qdim.py`: **with** the factor `LHS − RHS` simplifies to **0**; **without** it, as the old clause stated, the ratio is **8/15 at `$q=2$`**. And the scope is `$n = 2, 3, 4$` — three separate explicit theorems (`molien_qanalogue_n2/_n3/_n4`), not a `Finset.sum`; the general-`$n$` case was then **open** (closed since by `molienSum_eq_qFactorial`), needing *"the graded decomposition of the coinvariant algebra (Chevalley/Steinberg) plus an induction over `Finset`-many partitions"*, tracked as bean `qou-3quc`. The same file also **proves the contrast** — `sum_qDim_sq_ne_qFactorial_n3_at_two`: `$\sum_\lambda \dim_q(\lambda)^2 \neq [n]_q!$`, which is the `$\sum_\lambda w_\lambda(q) \neq 1$` defect above, proved rather than merely measured (`$22/35$` at `$n=3, q=2$`; bean `qou-zmw4`). Register: [`notation-collisions.md`](folio/quantum-observable-universe/notation/notation-collisions.md); measurement: [`2026-09-04-plancherel-convention-gap.md`](docs/audits/2026-09-04-plancherel-convention-gap.md) **Mechanical check (2026-09-13):** [`computations/audits/y_lambda_conflation_audit.py`](computations/audits/y_lambda_conflation_audit.py), wired blocking into `scripts/precision-gates.sh`. It flags the name `y_lambda` attached to the quantum Plancherel measure `$d_q(\lambda)^2/[n]_q!$` — in prose, in an AST assignment, in a producer's own name, and (as a draining ratchet) in a witness column that declares no `weight_family`. It exists because this rule lived only in prose and was broken in four probes at once, and there it was **not cosmetic**: re-weighting the Magnus $\Omega_2$ probes' own committed traces with the real Wenzl bridge FLIPS the sign of $P_\text{total}$ at $A=3$ and $A=4$ (Plancherel $-,+,+$ over $A=2,3,4$; Wenzl $-,-,-$), so the programme's target $A$-dependent sign change is present under one name and absent under the other — bean `qou-za3q`, decision 1 still OPEN.
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
| `folio-assistant/cat-harness/schemas/types.ts` | TypeScript types (discriminated unions) |
| `folio-assistant/cat-harness/schemas/constraints.ts` | Zod schemas + constraint rules |
| `folio/schema/builders.ts` | `definition()`, `theorem()`, `prose()`, etc. |
| `folio-assistant/content/pipeline/validate.ts` | Three-level validation |
| `folio-assistant/content/pipeline/render-latex.ts` | Block → LaTeX + AST validation |
| `folio-assistant/content/pipeline/build.ts` | Full document build |
| `folio/references/<id>.json` | **Bibliography source of truth** (CSL-JSON, one entry per file) |
| `folio/schema/references.ts` | Loads `folio/references/` in `ORDER`; exports the registry |
| `folio-assistant/content/pipeline/export-bibtex.ts` | Generates `references.bib` from CSL-JSON |
| `folio-assistant/content/pipeline/validate-references.ts` | Bibliography + citation cross-checks |
| `folio-assistant/content/pipeline/citations.ts` | `\cite{}` extraction from .md content |
| `folio-assistant/content/pipeline/find-dangling-remarks.ts` | Audit: find remarks without `interprets` |

### Bibliography architecture

The bibliography is managed as **typed CSL-JSON**, one entry per file in
`folio/references/<id>.json` (bean `qou-l7pj`, owner 2026-10-14 "1 + 2").
`folio/schema/references.ts` loads those files in the order its `ORDER` list
gives, validates each with `ref()`, and exports the registry (`references`,
`referenceMap`, `getRef`) that every consumer imports. BibTeX
(`references.bib`) is a downstream render target, generated in `ORDER`
(`bun run scripts/check-references-bib.ts` checks the committed copy).

- **Adding a reference**: write `folio/references/<id>.json` with
  `"$schema": "folio-reference/v1"` first, then add a `{ id: <id> }` line to
  `ORDER` in `references.ts` (the loader refuses a file `ORDER` does not list).
  Only an entry whose values are computed stays inline as a `ref({...})`
  call (today `leitner2026`).
- **Do not regex `references.ts` for entry fields** — it holds no entry
  bodies. Python reads the entries through `scripts/lib/references_dir.py`.
  Its `{ id: ... }` lines are kept so key-only scanners
  (`bib-cite-resolves`, `check-citation-keys.py`) keep working.
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

Each paper in `folio/folio.ts` has an optional `url` field for
viewer routing. CSL-JSON entries in `folio/schema/references.ts`
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

## MCP servers start on demand (owner directive, 2026-11-20)

Owner, verbatim: *"MCP should only start up if an agent needs the tools. The
agent should look at the process and what it needs and then make a decision."*

Every server in `.mcp.json` runs through
[`scripts/mcp-lazy.py`](scripts/mcp-lazy.py). At session start it connects in
under 0.1 s and exposes **one** tool, `start`; the real server is not running.
Its description says what the server provides, when it is worth starting, what
it costs, and the cheaper route that needs no MCP. The commands and those texts
live in [`scripts/mcp-lazy.json`](scripts/mcp-lazy.json).

**Decide before you start one.** Look at the task. If it needs the tools, call
`mcp__<server>__start` (pass a one-line `reason`), then call `RefreshMcpTools`
to load the real tools. If a cheaper route covers it, use that instead:

| server | provides | cheaper route without MCP |
|---|---|---|
| `paper-assistant` | `corpus_search` and the platform tools (~74) | `bun scripts/corpus-search.ts "<topic>"` |
| `lean-lsp` | goal states, diagnostics, Mathlib search | `lean -DautoImplicit=false -s 65536 <file>` (lean-direct) |
| `paper-search-mcp` | external paper search and PDF download | `library/INDEX.md` and `library/*/sections` |
| `openalex-paper-search` | OpenAlex author and work metadata | `folio/references/` for cited works |

Why. Measured 2026-11-20 on a fresh container: all four eager servers hit the
30 s connect timeout at session start. Run by hand, two of them could never
start: `paper-search-mcp` was unpinned and broke on mcp 2.x (now pinned
`mcp<2`), and `alex-mcp` needs `OPENALEX_MAILTO`, which is not set here. A
failed `start` now returns the backend's stderr tail as the tool result.


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
trap 'rm -f "$TGZ"' EXIT INT TERM   # ~2.4G scratch tarball; NOTHING else reaps it
SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)   # v4.24.0 -> v4-24-0
. "$ROOT/scripts/lib/lake-cache-family.sh"   # branch name comes from qou.json
BR=$(lake_cache_read_branch "qou-$SLUG")     # cat/folio-assistant-sci/lake-cache/qou-v4-24-0
git fetch --depth=1 origin "$BR" \
  && C=$(git rev-parse FETCH_HEAD) \
  && git ls-tree --name-only "$C" | grep '^lake-oleans\.tgz\.part' | sort \
     | while read -r p; do git show "$C:$p"; done > "$TGZ" \
  && tar xzf "$TGZ" -C "$ROOT" --transform 's,^content/,folio/,' \
  && bash "$ROOT/scripts/lake-restore-trace-check.sh" "$ROOT" \
  && echo "restored from $BR — skip Steps 1–3"

# 🛑 The branch NAME is declared, not written here (corrected 2026-11-15). The
# family moved to `cat/folio-assistant-sci/lake-cache/<member>` (bean `qou-hb5v`,
# declared in qou.json `storage.branchPrefix`), and the legacy
# `refs/heads/lake-cache/*` refs no longer exist on origin — measured with
# `git ls-remote origin 'refs/heads/lake-cache/*'`, which returns nothing. This
# recipe hardcoded `lake-cache/qou-$SLUG` and so failed at the fetch. Every
# literal `lake-cache/qou-...` branch name elsewhere in this file is now the
# member name under that prefix; resolve it with `lake_cache_read_branch`.

# 🛑 The `--transform` is load-bearing too, and it is NOT cosmetic. The seeded
# tarball stores PAPER paths as `content/<paper>/lean/...` — MEASURED 2026-10-10 by
# streaming all 20 parts through `tar tzf`: **13,670 `content/` members, 0 `folio/`**.
# It was seeded before the `content/` -> `folio/` tree rename (#7485), and `content/`
# does not exist on main at all now. Without the transform every paper olean lands in
# a directory nothing reads — `LEAN_PATH` is built from `folio/*/lean/...` — so a
# restore "succeeds", reports its olean count, and leaves the paper cone unbuilt. The
# ~3,480 Mathlib oleans under `.lake/` are unaffected, which is exactly why this is
# easy to miss: a Mathlib-only file verifies fine and the gap only shows on a file
# that imports the paper library. Drop the transform once the branch is re-seeded
# from a `folio/` tree; until then it is required, and it is a no-op afterwards.

# 🛑 The `trap` above is load-bearing, not boilerplate. This recipe streams every
# `lake-oleans.tgz.part` into ONE temp file before untarring, so `$TGZ` reaches
# ~1.8G (20 parts — reseeded 2026-09-06; was ~2.4G/27 parts on 2026-09-04, and ~1.6G/18 parts
# before the 2026-08-31 reseed added own-package oleans), and until 2026-08-28
# nothing deleted it — not the recipe, not a reaper.
# Measured: a single leaked `/tmp/tmp.4JEBENOn9G` from 2026-08-15 was still on
# disk thirteen days later and was a direct contributor to this container
# reaching **92K free**, at which point the Bash harness cannot write its own
# output capture and EVERY command fails, including the `rm` that would fix it.
# Note the disk reads deceptively: `df` shows 252G nominal at 100% with only 38G
# used, because the real limit is a per-session quota near 38G.

# 🛑 MEASURE the traces; do NOT assume them either way. This block used to state
# flatly that "a RESTORED tree has oleans but NO .trace files". That WAS true and
# is now FALSE for this branch: `lake-cache/qou-v4-24-0` was RESEEDED AGAIN
# 2026-09-06 from a full `lake build QOU UGB Fred2005`, then GAP-FILLED the same
# day. Measured on the branch head `a792c46d01b` (part19 of a 20-part seed
# stamped "fresh f897ebc"; parts 00-19 are 19x94371840 + 28770096 B = 1.70 GiB):
# **6492 oleans / 6492 PAIRED traces = 100.0% coverage**, 32461 tar entries,
# 1 orphan trace. Per tree: mathlib 3480, QOU 2702, Aesop 129, Batteries 85,
# ProofWidgets 34, UGB 28, Qq 12, Plausible 8, LeanSearchClient 3, ImportGraph 2.
#
# 🛑 The figures this line carried until 2026-09-06 — seed `1c496980587`,
# 6483 oleans / 6484 traces, mathlib 3471, 32416 tar entries — are STALE, and
# the way they went stale is the point. They are the PRE-GAP-FILL seed. The
# deltas are exactly +9 oleans and +45 tar entries = **9 modules x 5 files**
# (.olean/.ilean/.trace + 2 build artifacts): the four content-corpus imports
# that were missing (Topology.FiberBundle.Basic, RingTheory.HopfAlgebra.Basic,
# Analysis.Complex.UpperHalfPlane.Basic, Analysis.Real.Pi.Bounds) plus five
# transitive deps. All four verified PRESENT at the head above. So the branch
# was re-pushed after the figures were written, and the doc silently understated
# it by 9 — quote the head sha with any count here, and re-measure.
#
# 🛑 VERIFYING THIS COSTS ~1.7 GiB OF GIT OBJECTS PER RUN, and that is enough to
# brick a session. The round-trip check streams the parts (no tarball on disk),
# but the FETCH is the cost, not the stream: two verification fetches into the
# repo's own .git took it to 9.0G and the container to 402M free / 99%, where
# the Bash harness cannot write its output capture and every command fails.
# Fetch into a THROWAWAY repo so `rm -rf` reclaims it with no gc:
#   T=/tmp/cachecheck; rm -rf $T; git init -q $T
#   git -C $T remote add origin https://github.com/litlfred/qou
#   git -C $T fetch --depth=1 -q origin cat/folio-assistant-sci/lake-cache/qou-v4-24-0
#   C=$(git -C $T rev-parse FETCH_HEAD)
#   git -C $T ls-tree --name-only $C | grep '^lake-oleans\.tgz\.part' | sort \
#     | while read -r p; do git -C $T show "$C:$p"; done | tar tzf - > /tmp/listing.txt
#   rm -rf $T          # <- reclaims fully; a fetch into .git does NOT
# raw.githubusercontent.com is NOT an alternative: the repo is private, so an
# unauthenticated raw fetch 404s (measured, not assumed).
#
# The prior figures — the 2026-08-31 seed, 6170 of 6172 oleans, 27 parts — are
# superseded; note that seed was NOT measured before being replaced, so no
# before/after comparison exists (see lean-environment-setup.md §PRESERVE THE BUILD).
# Measured by stream-listing the parts; the seeders have refused a sub-90% seed since
# 2026-08-07. So the unconditional `touch` the recipe used to do now asserts
# something false in the BLOCKING direction, which is why the line above runs
# scripts/lake-restore-trace-check.sh instead: it sets the marker from the
# measurement, and cannot go stale the way the assertion did.
#
# Count PAIRED traces, never total ones — a Lake tree carries many traces
# belonging to no olean (cache.trace, lake.trace, *.c.o.export.trace); the naive
# ratio read 192% on a 13-olean tree.
#
# WHAT THAT DOES NOT MEAN. Traces are NECESSARY for Lake to accept a restored
# olean; they are NOT shown to be sufficient. A trace records input hashes, so
# Lake can still rebuild if the tree it hashes differs. The eviction below was
# real and is NOT retracted — only its premise has changed, and whether a
# `lake build` on a traced restore still evicts is UNTESTED (testing it costs a
# real build and risks the cache). Keep preferring lean-direct.
#
# The eviction, measured 2026-08-15 (bean qou-r13s) running `lake build QOU UGB
# Fred2005` at the root against an UNTRACED restore: root mathlib oleans
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

> **🛑 A BARE `lean` IS A WEAKER CHECK THAN `lake build` — pass
> `-DautoImplicit=false` (measured 2026-09-05, bean `qou-56qy`).** `lean`
> invoked directly does **not** read the lakefile, so it does not apply its
> `[leanOptions]`. `autoImplicit` defaults **true** in `lean` and is set
> **false** in both the root and paper lakefiles, and with it on Lean silently
> auto-binds an unbound identifier as an implicit argument rather than erroring.
> Same file, same `LEAN_PATH`, on `QOU/MassTheory/AtomWordShadow.lean`:
>
> ```
> lean                        ->  exit 0,  0 errors
> lean -DautoImplicit=false   ->  exit 1,  6 errors      (lake agrees: 20)
> ```
>
> That file was **red on `main`**, and it was called clean by a bare
> `lean`-direct run *and* by both sweep scripts before they were fixed. Pass
> `-s 65536` too, mirroring the paper lakefile's `moreLeanArgs`: one generated
> module overflows the default elaboration stack and aborts as a bare `exit 134`
> with no source error. So the recipe above is
> `lean -DautoImplicit=false -s 65536 <file>`, never bare `lean`.
>
> **This is the sharper of the two defects on this line.** The snapshot problem
> below makes a green *go stale*; this one makes a green *wrong from the start*,
> on any tree, however fresh.

> **🛑 `exit 0` here is a claim about the SNAPSHOT, not about the library
> source (measured 2026-09-05, bean `qou-56qy`).** The restored cache is a
> point-in-time tree. When a library signature moves after it was taken, a file
> calling the old signature compiles clean *and* is red against the source it
> names — both at once, with no signal. Realised, not hypothetical:
> `descartesWtrace` recorded `lean`-direct `exit 0` and **landed on `main`
> red**, because the cache was built 2026-08-30 while `794c34897d7`
> (2026-09-03) retyped `SeminormalRep.wtrace`'s genericity hypothesis and
> ported the seven consumers *inside* the package. The library half was done
> correctly; a content-block sibling was simply not in it (#6751).
>
> **So on a branch that touches `.lean`, run the sweep rather than bare
> `lean`-direct.** Each builds a shadow tree, rebuilds from source only the
> modules whose own olean predates their own last source commit, and compiles
> against that — never invoking `lake`, so the restored cache is not evicted:
>
> ```bash
> scripts/lean-content-sweep.sh [file.lean ...]   # content-block siblings
> scripts/lean-library-sweep.py                   # library dirty closure
> ```
>
> Whole corpus 2026-09-06: **938** content blocks and 74 dirty library modules;
> library sweep 122 s, content sweep ~55 min (pass the changed files, and
> `SHADOW=`/`--shadow` to reuse the ~2.3 GB shadow). Wired into
> `/prepare-merge` §4 and `prepare-merge-auto` Phases 1 and 4.
>
> **This read "261 content blocks and 74 dirty library modules, 0 red" until
> 2026-09-06, and BOTH halves misled.** The 261 was the pre-coverage-fix
> population: the sweep once filtered on an `import QOU` line, which reaches
> **262** of the **938** content-block `.lean` files — the other 675 import only
> Mathlib, are compiled by nothing else in the repo, and carry the same
> auto-implicit vacuity class the sweep exists to catch. The script's own header
> records the fix and calls the old form what it was: *"a 28%-coverage sweep
> reporting 0 red is the kind of green this whole bean is about."* Quote the
> figure the script prints, not this line.
>
> **🛑 And "0 red" is not the current result — at full scope it is 8 RED, of which
> ZERO are corpus defects.** All 8 are one class: a **missing Mathlib olean**,
> named at the block's own `import` line. Absent from the
> **paper and root trees alike**, and reproducible with **no shadow and no sweep**
> on a plain restored cache, so it is the cache branch, not the gate and not the
> source. So read the corpus result as **930 of 938 verifiable and green, 8
> unverifiable here**, and do NOT "fix" those blocks: their imports are fine, the
> cache is short.
>
> **🟩 THE GAP IS CLOSED, and it was 3 targets / 7 modules, not 4 (2026-09-07).**
> This paragraph named four absent modules. Measured: **`Analysis.Real.Pi.Bounds`
> is PRESENT.** The real gap is three targets whose transitive cones are seven
> modules — `HopfAlgebra.Basic` (+ `Bialgebra.Basic`, `Coalgebra.Basic`,
> `TensorProduct.Finiteness`), `FiberBundle.Basic` (+ `FiberBundle.Trivialization`)
> and `UpperHalfPlane.Basic`. All seven build from source with `lean`-direct in a
> few minutes and package to **2.3 MB**.
>
> Seeded to the addon orphan branch **`lake-cache/qou-v4-24-0-mathlib-gap-modules`**;
> restore with [`scripts/lean-restore-gap-oleans.sh`](scripts/lean-restore-gap-oleans.sh).
> With them restored, the seven blocks that import them compile **plain
> `lean`-direct, no shadow, exit 0** — confirming the diagnosis above exactly.
>
> **🟩 THAT BRANCH IS NOW 7 → 86 OLEANS (2026-09-11, commit `d7e3ae8c662`), and the
> 79 added are what make the LIBRARY ROOT verifiable.** The seven above unblock
> seven content blocks. They do **not** cover
> `Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree`, which
> `QOU.Eightfold.ObstructionH2Mathlib` needs — and the library root `QOU` is
> **SKIPPED behind that module**, so the single module `lake build QOU` gates on
> could not be checked in a stock container at all. That was attributed to a
> container resource limit (bean `qou-ed8a`, repeated in a sibling's merged audit);
> **it is not one** — it is 79 missing oleans, 188 s to build, 22 MB to fetch.
>
> **How the set was identified, and it is NOT by mtime** (an `mtime` discriminator
> fails here: `shutil.copy2` and a restore both preserve it). An olean in the paper
> mathlib tree with **no paired `.trace`** is exactly one the main cache did not
> provide, because `lake-cache/qou-v4-24-0` is 100 % trace-paired while both this
> branch's restore and a `lean`-direct build write plain oleans. That found **87**;
> one — `Mathlib/Data/Multiset/ZeroCons.olean`, mtime 2026-08-28, eleven days before
> the cone was built — is an untraced leftover from an earlier session and is
> **deliberately excluded**, so the 86 are exactly the 7 + the 79-module cone.
>
> **Verify with the SWEEP, not bare `lean`-direct, and the reason is instructive.**
> Two attempts to verify `ObstructionH2Mathlib` by hand both failed for reasons
> that were about the command rather than the cache: `lean-direct-env.sh` pins the
> **ROOT** tree (1298 oleans here against the paper tree's 3563), so it reported a
> missing *Mathlib* olean; re-pinned to the **paper** tree it reported a missing
> **QOU** olean (`QOU.Eightfold.ObstructionH2`), which is a sibling library module
> the sweep builds into its shadow and a bare `lean` never does. Neither was
> evidence about the gap. `scripts/lean-library-sweep.py --all --only-exact QOU`
> is the gate.
>
> **Seven, not eight, and the difference is NOT settled.** The 8 above came from a
> full content sweep; the 7 from grepping `import` lines, so a block blocked
> *transitively* through a `QOU` module would not appear in it. One block remains
> unaccounted for. Do not read 7 as a correction of 8.
>
> Restoring is **not** a Lake restore: these are plain oleans with no `.trace`, so
> `lake build` would evict them with the rest of the cache. Write-up:
> [`docs/audits/2026-09-07-mathlib-cache-gap-closed.md`](docs/audits/2026-09-07-mathlib-cache-gap-closed.md).
>
> **🛑 QUIESCE THE SESSIONSTART BUILD BEFORE TRUSTING THE SAFETY INVARIANT.** Both
> sweeps assert that the hardlinked shadow never writes through into the real
> olean tree, checked by snapshotting it before and after. Measured 2026-09-06 the
> QOU tree went **2660 → 2713** across a content sweep — 53 new, 62 rewritten —
> and **neither sweep did it**: `lean-shadow-verify.sh` writes only inside
> `$SHADOW` and unlinks first, while `scripts/lean-build-bg.sh`, re-fired by this
> session's *compaction*, ran `lake build` concurrently (status stamped mid-sweep,
> `attempts: 5`) and every changed path is under `QOU/`, `QOU.olean` included.
> Read naively that diff accuses the gate under review of the one thing that would
> make it worse than the bug. A concurrent `lake build` is also the eviction
> hazard documented above, so this is not merely a measurement nuisance.
>
> **A `lake build` log you did not commission may already hold the answer.**
> `/tmp/qou-lake-build.log` is the background build's full output and it is kept
> (only the `/tmp/qou-lean-build-bg.log` *timing report* discards the error
> bodies it counts). On 2026-09-06 it independently confirmed #6909 from the
> canonical path — `✖ [6459/6460] QOU.Eightfold.ObstructionClassForcesComplexType`
> with the same six source positions, sole failure in 6459 modules — on a branch
> carrying no `.lean` change. Read it before running any build of your own.
>
> Full measurement, both count coincidences, and what is NOT established:
> [`docs/audits/2026-09-06-full-content-sweep-938-and-the-cache-gap.md`](docs/audits/2026-09-06-full-content-sweep-938-and-the-cache-gap.md).
>
> **Two limits — do not write either out of a PR.** The dirty closure is
> computed against *this* container's olean tree, so a result is
> **container-scoped**: two sessions measured the same dependency as stale and
> as current, and both were right. And neither script sweeps the **UGB** or
> **Fred2005** packages.
>
> **A source-change count is the wrong population.** Six of those 74 have no
> olean at all — a *new* file inherits its dependencies' staleness without ever
> appearing in a drift count keyed on changed sources. Use the closure.
>
> This block is an owner-reviewable wording change to the repo's primary
> verification guidance, added on the evidence above; revert the wording if you
> disagree — the measurement stands either way.

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
| `folio/schema/` | Type system, Zod schemas, builder functions (re-exports from `folio-assistant/schemas/`) |
| `content/pipeline/` | qou-side audit scripts only (vacuity/axiom, clarity, orphan, trace-convention, …). Validation / rendering / build moved to `folio-assistant/content/pipeline/` in the miga migration — check which side a script is on before invoking it |
| `content/<paper>/` | Paper manifest + chapter directories |
| `content/<paper>/fluid-dynamics/` | Ch 7: Fluid dynamics of the brane (q-NS, NS obstruction) |
| `folio-assistant/` | **Platform package** — MCP server, auth, UI, blocks, viewer |
| `folio-assistant/src/` | Generic core (server, types, routes, tools, blocks registry) |
| `folio-assistant/adapters/paper/` | Paper content adapter (implements `ContentAdapter`) |
| `folio-assistant/schemas/` | Shared TypeScript types (proof-objects, glossary, etc.) |
| `folio-assistant/viewer/` | Paper viewer SPA + Pyodide cache Service Worker |
| `folio-assistant/ui/` | Assistant chat SPA |
| `folio-assistant/feedback/` | User feedback (TypeScript files, committed to main) |
| `simulators/` | Interactive HTML simulators |
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
| `references.bib` | BibTeX database (auto-generated from `folio/schema/references.ts`) |
| `lakefile.toml`, `lean-toolchain` | **Root Lake workspace** — aggregates every paper package; `lake build` here builds all |
| `folio/quantum-observable-universe/lean/` | `qou` Lake package (lib: `QOU`) |
| `folio/unital-groebner-bases/lean/` | `ugb` Lake package (lib: `UGB`) |
| `folio/fred2005-formal-groups/lean/` | `fred2005` Lake package (lib: `Fred2005`) |
| `folio-assistant/schemas/lean-packages.ts` | Registry mapping `lean.ref` URI prefixes → Lake packages |
| `blueprint/src/` | LeanBlueprint source (content.tex, preamble.tex, web.tex, print.tex) |
| `home_page/` | Jekyll landing page for GitHub Pages |
| `.github/workflows/` | CI/CD pipelines |
| `.github/scripts/` | Python orchestration (ontologist, extraction, stub generation) |
| `.claude/skills/local/` | Repo-specific review skills |
| `.claude/skills/<pkg>/` | Synced external skill packages |
| `library/` | **Ingested sources**, one directory per document: `library/<doc-id>/` holds the PDF, `structure.json` (metadata + TOC + section index), `sections/*.md` (**greppable** section text — corpus-grep path 5), and `candidates.json` (extracted claims, *proposals only*). `<doc-id>` is derived from the page-1 arXiv stamp (`arxiv-0706.2213v3`) or the slugified filename, and is the join key to the source ledger (`test/attestations/bib-verification/`). Produced by folio-assistant's `scripts/pdf-structure.py` + `extract-candidates.py`. |
| `uploads/` | **Incoming queue** — raw PDFs as dropped, not yet ingested. `uploads/` and `library/` are **two stages of one pipeline, not the same directory renamed**: a file sits in `uploads/` until it is processed into `library/<doc-id>/`, and `uploads/` stays live for the next drop. **Corpus-grep path 5 searches `library/` only**, so anything still in `uploads/` is invisible to it — an un-ingested paper will not be found by any "has the corpus got this?" check, which is exactly how a held source gets re-derived. `scripts/migrate-uploads-to-library.py` moves one across. (Corrected 2026-08-25 on owner instruction: this row previously read *"renamed from `uploads/` 2026-08-15"*, which described the one-time migration of the then-existing backlog as though it had retired the incoming path. It had not, and reading it that way makes an agent treat a live queue as a dead alias.) |
| `beans/` | **Session work-plans as beans** — the [`beans`](https://github.com/hmans/beans) CLI flat-file issue tracker (install via `scripts/install-beans.sh`). Agent work-plan source of truth; see `.claude/skills/local/todo-manager.md` |
| | 🛑 **The path is `beans/defs/`, NOT `.beans/` — and the old spelling made this document's own corpus-grep gate UNRUNNABLE (corrected 2026-09-27).** Commit `58a1f3231c` (*"qou-utbr: .beans/ -> beans/defs/ + beans/beans.json, matching the platform layout"*) moved the store; `.beans/` **does not exist** and `beans/defs/` holds **5364** beans. Eleven operative sites in this file said `.beans/`, and the sharpest was §"Before declaring open" **path 6**, whose literal command `grep -rl <topic> .beans/` therefore returned **empty every single time** — a false all-clear over the whole tracker, on the one path that section adds because *"it is where a prior agent's conclusion most often sits"*. Its own history note says it was added after a PR re-derived two results the corpus already held; as written it could not have found them. **This is the migration plan's own governing principle** (`cat-harness/docs/architecture/migration-plan.md:20`): *"Move wiring and script together"* — the store moved, the wiring did not, and `qou-utbr` is still `in-progress`. **Two `.beans/` mentions survive here on purpose** (lines ~2184, ~2266): both are records of what a *past* measurement scoped or sampled, and rewriting a path inside a dated finding falsifies the record — same call as the `4.66e6` drain, which deliberately left audit docs alone. **NOT swept:** 168 further `.md` files (mostly `.claude/skills/local/`) plus 66 code **comments** and 100 bean bodies. Measured, and no live code is broken — **4** runtime `.beans/` paths exist and all four are in `fsh-guts/deprecated/root-scratch/`, one carrying a hardcoded `/Users/litlfred/…` path that never resolved in this container. The skills sweep is a ~168-file change and waits on the owner per §🟥 ASK THE OWNER. |
| `todos/` | Legacy work-tracking queues (`*-queue.json`), gitignored; being migrated into `beans/defs/` per the Folio-Assistant Infrastructure Migration (`miga` epic) |
| `docs/` | Planning documents, migration plans, dependency graphs |
| `scripts/` | Setup and health-check scripts (Lean MCP, etc.) |
| `lean-mcp.config.json` | MCP server config (domain, image, auth, ports) |
| `deploy/` | Remote MCP server deployment (Docker Compose, auth, auto-update) |
| `skills-config.json` | Skill package subscriptions |

## Build output (gh-pages) — 🛑 THE RENDERED SITE IS DEPRECATED, AND THIS SECTION DESCRIBED THREE WORKFLOWS THAT DO NOT EXIST

**Owner, 2026-09-27: *"depcecate/remove the githubpage"*.** The rendered
GitHub Pages site at `litlfred.github.io/qou/` is deprecated. The `gh-pages`
**branch is NOT removed** — it stays as a file store, and every
`github.com/.../blob/gh-pages/...` link in `README.md` keeps working. The
deprecation stops at the rendering.

**This section previously opened *"Three workflows deploy to the `gh-pages`
branch"* and tabulated `blueprint.yml`, `lean_ci.yml` and `publish.yml`. The
location attribution was stale — it reads as a list of files in THIS repo, and
none of the three is here. But 🛑 "absent" is the WRONG correction, and it has
now been made twice by two different sessions:**

| workflow | qou `.github/workflows/` | platform `.github/workflows/` | what it actually is |
|---|---|---|---|
| `publish.yml` | absent | **PRESENT** | **LIVE on dispatch** — qou reaches it from `.github/workflows/build.yml:27`, `uses: litlfred/folio-assistant/.github/workflows/publish.yml@37a36ce9296…` (pinned to `.folio-assistant-pin`) |
| `blueprint.yml` | absent | absent | a **TEMPLATE** at `cat-harness/templates/paper/github/workflows/blueprint.yml` — scaffolding for a new paper repo, runnable nowhere |
| `lean_ci.yml` | absent | absent | same: a template, runnable nowhere |

**So the heavy render is live, not gone**, and the `gh-pages` site is dormant
because nobody has **dispatched** `build.yml` since 2026-06-30 — not because its
producer disappeared. Two sessions in two days got this wrong in opposite
directions: 2026-09-26 reported all three ABSENT, corrected itself to *"they
MOVED — all three exist in the platform"* (bean `qou-w5av`), and 2026-09-27
repeated the original ABSENT claim without reading that bean. **Both
corrections were over-broad**: one of the three is live, two are templates.
The lesson is the one the detector-blindness taxonomy keeps recording — *measure
the right tree, and say which tree you measured.*

**Do NOT "clean up" `build.yml` or `paper-builder-image.yml` on the strength of
this.** `build.yml` is qou's only render entry point and is what produces the
paper PDFs that README's chapter table links; `paper-builder-image.yml` builds
the TeX image `build.yml` passes in as `builder_image:`, which the platform's
`publish.yml` consumes at three job sites while hardcoding it nowhere. Whether
the PDF output goes away at all is an owner decision, framed in `qou-w5av`.

### What actually runs on qou — measured, per workflow, not read off YAML

All **14** workflows are `workflow_dispatch`-only (owner directive 2026-06-30,
Actions billing). Run counts and last conclusions:

| workflow | runs | last conclusion | date |
|---|---:|---|---|
| `docs-site` | 5 | **success** | 2026-09-26 |
| `kg-vocabulary-gate` | 2 | failure | 2026-09-27 |
| `build` | 3531 | failure | **2026-06-30** |
| `lean-content-siblings` | 1216 | failure | **2026-06-30** |
| `witness-staleness` | 953 | failure | **2026-06-30** |
| `doc-gen4` *(now deprecated)* | 461 | failure | **2026-06-30** |
| `lean-axiom-guard` | **0** | never ran | — |
| `lp-dual-gate` | **0** | never ran | — |
| `probe-float64-gate` | **0** | never ran | — |
| `lean-orphan-gate` | **0** | never ran | — |
| `word-provenance-gate` | **0** | never ran | — |
| `lake-cache-refresh` | **0** | never ran | — |

Two facts worth internalising. **Four high-volume workflows last failed on the
same day**, 2026-06-30 — they were not merely switched to dispatch-only, their
final run *failed* and then the triggers were removed. And **six workflows have
never run at all**, among them `lp-dual-gate`, `probe-float64-gate`,
`word-provenance-gate` and `lean-axiom-guard`, which this document describes as
enforcement. A gate with zero runs is documentation, which is the same lesson
§"QA is agent-owned" records for `precision-gates.sh`.

**`docs-site` is the only workflow that has succeeded since 2026-06-30 — and
it has never published.** Its gh-pages write was gated `if: inputs.publish`
with `default: false`; `git ls-tree` on the branch head confirms **no `docs/`
directory has ever existed there**. That step is now removed and the workflow
uploads an artifact only.

**There is no STAGING pipeline on qou.** The word `STAGING` in `docs-site.yml`
names a local directory used for front-matter injection. The
`litlfred.github.io/folio-assistant/STAGING/<branch>/` previews that appear on
PR comments are the **platform** repo's, and that repo is push-triggered
because its billing is not in this state.

### What is on the branch, and how stale

`gh-pages` head is **2026-07-08** — *"deploy: update PDF with \pm error
formatting"*. Contents: `lean/` (~9,500 files), `drafts/` (~7,300),
`rust-api/` (783), `schema-docs/` (206), `python-api/` (20), `papers/` (14),
plus `qou.pdf`, `main.pdf`, `paper.html`, `visualizer.html`, `axiom-report.txt`,
`dependency-graph.svg`, `proof-objects.json`, `glossary.json`.

🛑 **An earlier version of this paragraph said "every producer of every one of
those is absent or dead, so the snapshot cannot be refreshed". That is wrong.**
The paper-build half of it — `papers/`, `index.html`, the PDFs, `schema-docs/`,
`drafts/` — comes from the platform's `publish.yml`, which is **live and
callable today** via `build.yml`. The snapshot is stale because that workflow
has not been **dispatched** since 2026-06-30, which is a different fact with a
different remedy. The `lean/` subtree is the part whose producer really is gone
(`doc-gen4.yml`, now deprecated below). Treat the site as dormant-but-revivable,
not as an unrefreshable archive.

### Deprecated, and where it went

`doc-gen4.yml` is moved to
[`fsh-guts/deprecated/workflows/doc-gen4.yml`](fsh-guts/deprecated/workflows/doc-gen4.yml)
— its only job was `peaceiris/actions-gh-pages` into `gh-pages/lean`, and it has
not succeeded since 2026-06-30. **The `doc-gen4` Lake dependency is a different
thing and stays**: it is in `lake-manifest.json` and `scripts/lean-build-bg.sh`,
and is the Lean doc generator itself rather than a publishing workflow. Do not
conflate them.

**The rule for agents.** Do not write "published at `litlfred.github.io/qou/…`"
anywhere, and do not restore a `push:` trigger to make any of this automatic.
If a rendered artifact is genuinely wanted, that is a new decision about a new
pipeline, not a repair of this one.

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
13a. **NEVER close a bean whose subject is an open conjecture (owner
    directive, 2026-09-06, verbatim: *"Don't close beans with open
    conjectures!!!"*).** A bean that tracks a conjecture, a
    conditional-class hypothesis, a literature-unsupported identification
    (e.g. `A_ω → S`, bean `qou-q3np`), or the epistemic tier of a bridge
    stays `todo` / `in-progress` until the mathematics closes — not until
    the *recording* of its openness is done. "The scoping sentence is now
    in the content block" is a body-append, not a completion. Only beans
    whose whole task is mechanical (a citation key added, a file renamed)
    may be completed while the conjecture they touch remains open.
14. **Do NOT try to please.** The owner is a physicist. Fake progress
    is worse than no progress — it wastes time, pollutes the corpus,
    and erodes trust. If the math doesn't work, say so. If a
    derivation dead-ends, report the negative. If you don't know,
    say "I don't know." The user would rather see "this is open
    (bean `qou-XXXX`)" than a sorry-laden scaffold dressed up as a
    result. **Honesty is the only acceptable output.**
