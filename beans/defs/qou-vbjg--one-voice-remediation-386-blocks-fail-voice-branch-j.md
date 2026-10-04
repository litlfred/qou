---
# qou-vbjg
title: 'One-voice remediation: 386 blocks fail voice-branch-jargon'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T12:00:00Z
updated_at: 2026-10-04T15:14:59Z
parent: qou-mub3
---

Owner: *"` the binding module C1` is audit/agent-author-dicussion language...
what is C1???? use one voice pls / milnor"*, then *"dispatch agent to add agent
qa sidecar for all .md, titles for review of agentic-author discussion and audit
jargon"*.

The sweep is **done** and committed (`6f8932a0`): axis `voice-branch-jargon` on
**3362** blocks, **2976 pass / 386 fail**. Four subagents over nine directories
plus a concurrent sibling session over the rest; clean partition, one criterion
key. No prose was touched by the sweep — verdicts only, so the findings are
reviewable before editing.

**This bean is the remediation**, not the sweep.

## The rule the axis encodes

`.md` is the manuscript and `title` is published. Neither may carry a label that
names a *branch artifact* rather than a *mathematical object*: AGENTS.md section
ids, bean ids, PR numbers, tracker letters, pipeline slot names, `docs/audits/*`
paths, or instructions to a future agent. `authorNotes` is the working channel
and takes all of it.

The failure mode is not "informal prose". It is prose a reader **cannot
resolve** — `C1`, `D6`, `§3b-cond`, `Piece A`, `Avenue B` name nothing that the
paper defines.

## Buckets, largest first (a block can be in several)

| # | bucket | what the fix is |
|---|---|---|
| 143 | **A** — `**Archimedean specialisation (§7c).**` and `per AGENTS.md §7c` | drop the citation, keep the sentence. The base-ring statement is real mathematics; only the pointer to agent instructions is the defect |
| 118 | **B** — `§3b` / `§3b-cond` naming the conditional-class convention | say it in words: "conditional on a class hypothesis for which no instance is supplied" |
| 115 | **Z** — mixed: the word "audit" for a verification, `Piece A`, `Avenue A/B`, `B1` keystone shorthand | per file |
| 65 | **F** — `docs/audits/*` cited as if published | drop or replace with the block/witness the audit was about |
| 43 | **I** — Phase / Workplan / Track / Path / Piece narration | delete; it describes the branch's history, not the mathematics |
| 31 | **D** — `— section lead` suffix on published prose titles | strip the suffix; it is the pipeline slot name |
| 26 | **H** — tracker/lattice labels `D6 D7 D8 D22`, `C1–C4`, `L3` | name the object, or define the label in place where it is genuinely a lattice node |
| 16 | **E** — PR links | drop |
| 9 | **G** — bean ids in published tables | drop |
| 8 | **C** — `§7a §7b §2e §2f §2h` | as bucket A |
| 8 | **J** — instructions to a future agent, `WIP`, "deferred to follow-up PR" | delete |

## Guarded against (checked, deliberately NOT flagged)

`R1/R2/R3` (Reidemeister, and separately the Hecke defining relations);
`CAL-1/2/3` (the manuscript's own calibration anchors); bare `§7`, `§8` (the
paper's own chapters); "the arc" (arc space $\mathcal{L}(X)$); "branch"
(branch point/cut/divisor); `D_2`/`D_8` as dihedral groups; "Step 1..N" in
proofs (86 hits); "open"/"remains open"; `*.witness.json` citations, which are
data-availability references and stay.

`substrate wall` is used 108× and defined nowhere, but it is the manuscript's
own metaphor in the manuscript's own voice — underdefined, not branch jargon.
Separate issue; not part of this bean.

## Worst individual offenders (from the sweeps)

1. `brings-surface/c-from-color-flavor-swap.md` — the block **is** a work plan.
   Conjecture titled by tracker id; a `## Diagnostics` stanza addressed to a
   skill file; orders to a future agent ("Close D7 and D8 — author …").
2. `knots-particles-confinement/electroweak-higgs-torus-link-triplet.md` —
   `C1`/`C2` as conjecture-lattice nodes. **Genuinely not mathematics**: no
   $C^1$ smoothness class, no chain group. Defined only here, used bare in three
   siblings.
3. `mass-endomorphism/b1-current-status-table3-data.md` — the table is a git
   history of the branch: columns `| Round | Commit | Key contribution |`.
4. `mass-endomorphism/tau-M-asymptotic-rep-theory-interpretation.md` —
   *"Subsection content pending restoration (prior text was AI-generated filler
   removed under bean 6fib)"* is published prose.
5. `braids-and-knots/braid-link-types.ts` — title begins "Track C Step A:".
6. `nuclear-interactions/cpt-d6-d7-d8-closure.*` — ids frozen into the filename,
   the title and the class name, though the block defines $C$, $P$, $T$ itself.
7. `mass-endomorphism/{hecke-algebra-type-scaffold,markov-trace-operator-construction}.ts`
   — titles end "(forward-reference to WIP-scaffolding audit)".
8. `eightfold-way/eightfold-open-problems.md` — bean ids in a published table.
9. `mass-endomorphism/b1-{figure-8-row-theorem,soft-sharpness-theorem}.ts` —
   `B1` in published titles; it is branch shorthand for
   `conj:gb-depth-period-collapse`.

## Order of work

Mechanical bulk first (A, C, D), then the semi-mechanical phrase substitution
(B), then per-file (F, I, H, E, G, J, Z).

## Progress

**Done (`379b45db`, pushed).** Buckets A, C, D and the title half of H:

* 150 `.md` files — every AGENTS.md section id out of published prose, the
  attached sentence kept. The `mba-*` chapter's quoted-rule citations restated
  as what they assert; one instruction to a future agent rewritten as an
  argument.
* 35 prose blocks — `title` field dropped entirely (287 of 388 prose blocks
  already carry none, and the section above each one has the same title).
* 26 published titles — `B1` → "the depth correspondence", `Track C Step A/B`,
  `Path A`, `Atom 1`, `(forward-reference to WIP-scaffolding audit)`,
  `(L2 precision-goal)`, `(L3)`, `PR #1253`, an inline audit link.
* `D6 + D7 + D8` → the three symmetries by name; Lean class `CPTD6D7D8Closure`
  → `CPTClosure` (self-contained rename).
* Four sections titled `Reconnected orphan blocks (Phase 7)` retitled by
  contents; two of their lead paragraphs rewritten from branch narration.

Validation held at `✓ Valid — 10 issue(s)` throughout — the same 10 as before.

**Two chapters are now clear of every detector** — `mass-theory` and
`mass-endomorphism`, the two largest, together 199 of the 386 failures.

Subagents did bucket F there (46 sites / 31 files and 22 sites / 17 files
respectively, all three outcomes used). I then took the rest by hand:

* **A second standing boilerplate** turned up that the first pass missed —
  `> **SUPERSEDED-$\rho_q$ note .**` in 12 blocks. Rewritten as
  `> **Superseded.**`, which also **fixed a broken link**: it pointed at
  `../braids-and-knots/mass-endomorphism-tower.md` (the file is in
  `mass-theory/`) with a `§SUPERSEDED` anchor that does not exist.
* **The duality tracker.** `docs/duality-tracker.md` calls itself "coord doc"
  in its own first line and cites a PR for its rationale, so it is the same
  class as `docs/audits/*`. Its D-numbers had propagated into conjecture
  *titles* — `**Conjecture (D7 parity closure).**`, `(D16 …)`, `(D15 …)`,
  `(D21 …)`, `(D17 …)` — and through the bodies. Each D-number names a
  conjecture that already has a name, so each was replaced by it.
* **A `## Diagnostics` stanza addressed to an agent skill file** —
  `Per [.claude/skills/local/canonical-watcher.md](…) §Slot J:` — in 5 blocks.
  The three bullets under it (GB filtration level, jet order, bar-symmetry
  status) are real structural data and stay; the heading became
  `## Structural invariants` and the skill-file line is gone. `## Open R&D`
  became `## What remains open`.
* `B1` throughout the bodies, `L2`/`L3` roadmap tiers, `Phase 3`/`Phase 5g`/
  `Track C`/`Path A`, remaining PR links, one bean id, `§3b-cond` in two
  published `.ts` titles, and the 33 non-boilerplate `this block` uses.
* In the keystone `conj:qdifference-kernel-prolongation-symbol` itself: the
  bare labels `(B)`, `(C)`, `(D)`, `(L3)`, none defined in the block, and a
  garbled tail ("not searched canonical" → "not fitted numerically").

**False positives correctly left alone.** `c_k^{L2}` in
`t-beta-markov-frobenius-collapse.md` is the Euclidean $L^2$ norm, named in the
sentence above it — the notation was tightened to `c_k^{\,L^2}` so it stops
reading as the roadmap tier. `Markov-trace audit on ${}^3$He` in
`mass-endomorphism-conjecture.md` is "audit" in the ordinary sense.
`BindingPerRepReebPhase` is a Lean class name.

**One subagent flag was wrong, checked and dismissed:** it reported
`witness qbeta-ck-sseries-operator-match` as dangling and now the sole support
for a sentence. The witness exists —
`computations/qbeta/qbeta-ck-sseries-operator-match.witness.json`; the search
missed the subdirectory.

**Still in flight.** One subagent on bucket F (`docs/audits/*` and
`docs/coordination/*` cited as published sources): 137 sites across 73 files,
partitioned `mass-theory` / `mass-endomorphism` / the other fourteen chapters.
They also carry the worst individual offenders in their patches
(`c-from-color-flavor-swap.md`, `b1-current-status-table3-data.md`,
`tau-M-asymptotic-rep-theory-interpretation.md`).

## Do NOT flip the verdicts mechanically

Tried and rejected. The plan was to mark a sidecar `pass` once the defect span
its note quoted no longer appeared in the file. Measured against the *pre-fix*
text at `6f8932a0`, only **19%** of quoted spans matched — the notes elide with
`…` and paraphrase, so "span absent" mostly means "never was a literal quote",
not "fixed". Flipping on that test would have marked ~267 blocks `pass` on no
evidence.

The verdicts came from agents reading the files; only re-reading can honestly
change them. **Re-review is a separate pass**, to be run after the prose work
lands, using the same `voice-branch-jargon` key.

Where things actually stand, measured on the *published surface only* (`.md`
bodies in full, `.ts` `title:` fields; `authorNotes` and `//` comments are the
working channel and are exempt by the rule):

| detector | blocks still matching |
|---|---|
| `docs/audits`, `docs/coordination` | 73 |
| Phase / Workplan / Track / Piece / Avenue / Path / Round | 24 |
| PR links | 14 |
| `D6 D7 D8 D22`, duality tracker, conjecture lattice | 8 |
| bean ids | 6 |
| AGENTS.md ids | 4 |
| `WIP`, "pending restoration", "AI-generated filler" | 2 |

105 distinct blocks. The other 281 of the 386 no longer trip any detector, but
that is not the same as being clean — their notes flagged things no regex
catches (the word "audit" for a verification, `Piece A`, `Avenue B`, work-plan
narration). Those need the re-review pass, not a flip.

**Also done, uncommitted while the subagents run.**

* `This block …` → `What follows …` in the standing archimedean note, **101
  sites**. "Block" is the authoring pipeline's unit of content; a paper does
  not say "this block". That template was 102 of the 134 uses in the corpus —
  the other 33 vary and need individual reading, so they go to the re-review.
* `PieceASpechtCharacter.md`, `PieceACornerInduction.md` — titled `Piece A: …`
  and opening "This file provides the narrative counterpart to the … route for
  Piece A". Retitled by their mathematics (the central Jucys–Murphy element on
  Specht modules; corner-removal induction for hook lengths) with real lead
  paragraphs.
* `eightfold-open-problems.md` — bean ids out of the published evidence column.
* `definition-index.md` — `(L3)` out of the Wigner-SU(4) row, matching the
  title fix.
* `intro-ns-obstruction-tower-mtc.md` — `(Track B)` → "the second track", which
  the same sentence had already defined.
* `cpt-d6-d7-d8-closure.lean` — docstrings finished to match the `CPTClosure`
  rename (they still named D6/D7/D8 and cited §3b-cond).

**Correctly NOT flagged** (checked, left alone): `fluid-dynamics/p5-counterexample.md`
uses "**Phase 1:** $q$-deformed evolution" / "**Phase 2:** the $q \to 1$ limit"
— phases of a physical argument, not branch phases.

## OWNER DECISION NEEDED — 18 blocks carry an opt-out from this very rule

`tags: ["non-scholarly-voice-exception"]` is, per
`.claude/skills/local/one-voice-audit.md`, an **explicit author marker** that
exempts a block from the scholarly-voice default. Eighteen blocks carry it:

`brings-surface/{inter-nucleon-channel-color-tube,c-from-color-flavor-swap}`,
`stochastic-mechanics/lusztig-canonical-basis-q-eq-1`,
`mass-theory/{pachner-pentagon-borromean,p-from-braid-mirror,
borromean-bloch-group-element,kashaev-density-equals-sdp-multiplicity,
poincare-lefschetz-borromean,stokes-dt-bps-bridge,isospin-from-canonical-bowtie,
dim-master-pentagon}`,
`q-geometric-langlands/{quantum-langlands-dual,modular-s-transform-q-q-tilde,
mirror-3d-3d-correspondence}`,
`nuclear-interactions/{wigner-su4-from-spin-isospin,spin-from-so3-fiber,
t-from-trace-cyclicity,type-b-folding-cpt}`.

**Fourteen of them are blocks this bean has now cleaned.** They satisfy the
rule they are exempted from, so the tag is stale — and worse, it is load-bearing
in the wrong direction: a future sweep honouring the opt-out will skip them, and
they can drift straight back to where they started.

Not removed. The tag is an author marker and taking it off is the owner's call,
not a remediation agent's. But it should be taken off these fourteen, and the
remaining four (`isospin-from-canonical-bowtie`, `quantum-langlands-dual`,
`spin-from-so3-fiber`, `t-from-trace-cyclicity`) should be checked to see
whether they still need it.

## The class the detectors could not see

Re-review of every flagged block (3313 pass / 48 fail, from 2976 / 386) turned
up a defect class no regex in this bean would have caught, and that the original
sweep's buckets did not isolate: **the manuscript describing its own repository
instead of its mathematics.**

| what | example |
|---|---|
| "the corpus" as the paper's name for itself | "nothing in the corpus addresses the heavy flavour masses"; "open — no corpus content" |
| "block" as the pipeline's unit of content | "**The block** therefore qualifies as…"; a table column headed "consumer block" |
| owner governance as warrant | `**(owner ruling 2026-06-24)**`, three times in one block; "owner authorised" |
| the build system addressed directly | a `### CI enforcement` heading; "gates this on every continuous integration run" |
| work-status banners | "**Outline (future work).** We will investigate…"; "deferred to a follow-up paper" |
| dated rename history inside symbol definitions | "**Canonized 2026-07-12** from the former $\beta_K$…" in the notation register |
| effort estimates and workstream labels | "~1-2 weeks" in a published table; `Story B`, `R2-c`, `w3-w4` |
| editing to-dos | "several existing blocks should be refactored…", keyed to source paths |

This is a **different failure from the one the bean opened on**. `C1`, `D6`,
`§3b-cond` were labels a reader could not resolve. These are sentences a reader
*can* parse and that are simply not about the paper — the difference between
"open" and "open — no corpus content" is that the second tells the reader about
a repository they cannot see.

Worth keeping as the axis's definition going forward: the test is not "is this
jargon" but **"is the referent something the paper contains".**

Two findings from the reviewers were checked and are correctly *not* defects:
`analytic-obstructions.md`'s "we audit which analytic structures lift" is
ordinary English for a systematic verification, and
`electroweak-higgs-torus-link-triplet`'s `C1`/`C2` now read as hypothesis
labels because the block defines them in its own table.

## Owner ruling, 2026-08-08 — goal language is also out

Owner confirmed the repository-description class, and **added one I had
explicitly decided to keep**: *"Canonized, keystone, capstone, and other
audit/discussion goal like language."*

I had reasoned that "keystone" reads as ordinary scholarly English for a
load-bearing conjecture and left it in. That was wrong, and the reason is worth
recording: 57 uses, and essentially every one ranks a result against the
*project's programme* rather than stating a mathematical dependency. "The
keystone's discharge targets" is a plan. "The depth correspondence, on which the
four bounds below depend" is mathematics. The words differ; the fact does not.

Out, in published prose and titles:

* **keystone** (57), **capstone** (1) — name the conjecture, or say what rests
  on it.
* **canonized / canonised with a date** (4) — dated rename history inside the
  notation register's symbol definitions.
* **unblock, roadmap, closure path, discharge plan, workstream, deliverable,
  milestone** where they describe the plan rather than a dependency.
* **owner rulings as warrant** — `**(owner ruling 2026-06-24)**`.
* **the build system addressed directly** — `### CI enforcement`, "gates this on
  every continuous integration run".
* **effort estimates in published tables** — "~1-2 weeks".

**Two words split, and the split is the whole job:**

`gate` — 145 hits. **Mathematics, keep:** `Toffoli gate`, `q-AND gate`, `CCNOT`,
quantum-circuit gates, "this algebraic gate". **Workplan, remove:** "the
$\Delta_\lambda$ gate remains open", "owner-gated", "wire/un-wire gate",
"inclusion/exclusion gate", "the six-ansatz gate", "gated on the order-by-order
expansion". In every workplan case the content is a dependency or an open
question and survives as one — "six ansätze have failed" keeps its count.

`lands` / `landed` — 24 hits, and mostly the *other* way. **Keep** the ordinary
mathematical sense: "lands on Wedderburn channel $\lambda$", "lands away from
$t^{-1}$", "lands in $\mathbb{Z}[q^{\pm 1}]$", "lands non-by definition at its
depth", "the exact $c_4$ that lands $m_p$ on CODATA". **Remove** only the merge
sense: "once `conj:s5-so3-fiber-action` lands".

The lesson for the axis: a word is not the unit. `gate` is a defect 40 times and
a theorem 100 times in the same corpus, and only reading the sentence tells them
apart. Any future sweep that greps a word list will get this wrong in both
directions.

## Out of scope, noted here so it is not lost

`content/schema/references.ts` carries the project's own pull requests as
bibliography entries (`type: "webpage"`, `URL: …/pull/1889`), with branch jargon
in their titles — e.g. *"Q_β bar-even kernel §4 formalize-first gate (Track A/B;
bundled into the BarEvenKernel typeclass)"*. Whether a paper may cite its own
PRs as references is an editorial question above this bean, and the bibliography
is a different surface from prose and titles. Not touched.

**461 `.lean` files reference `AGENTS.md`.** Lean source is nearer the working
channel than the manuscript is, and 461 files is a decision, not a cleanup. Left
alone deliberately — do not chip at it file by file. If it is ever done it
should be one pass with one rule, the way §7c was.

**A claim that lost its only support.** `proton-mass-substrate-identity-derivation.md`
asserted the universal $-1/12$ leading-pole coefficient on the strength of an
audit document and nothing else. Substituting the obvious witness was checked
and rejected — `ocneanu-cancellation-derivation.witness.json` is a *failing*
symbolic scaffold (`allPassed: false`) whose own description names the audit as
the verification path. The prose now says plainly that the coefficient rests on
200-dps numerical pole detection and is not symbolically derived. That is honest
but the block wants a real witness.

**A stale Lean sketch**, `c-from-color-flavor-swap.md`: it lists a
`cpt_factorisation` field that `CFromColorFlavorSwap.lean` says is deliberately
omitted because the parity and time-reversal carriers do not exist. They now do.
Left verbatim — reconciling it is a mathematics change, not a voice change.

**The validator does not check relative links.** Three dead relative paths were
found by hand in the course of this work (`bar-involution.md` and two table
refs from `brings-surface/`, plus the `SUPERSEDED` notice's wrong directory in
12 blocks). `run-validate.ts` checks `#label` cross-references only, so a
`[text](../wrong/path.md)` passes silently. Worth a checker.

`substrate wall` — 108 uses, defined nowhere. Manuscript voice, so not branch
jargon, but underdefined. Separate.

Relates: `qou-kyst` (the F1/F3 statements this started from).

## CLOSED 2026-08-08 — merged as #4672 (`4f2f03cc`)

The axis reads **3367 pass, 0 fail** on `main`, from 2976 / 386 when the sweep
landed. Every verdict that moved was re-read by an agent against the current
text; the shortcut of flipping on "the quoted span is gone" was tried and thrown
out, because measured against the pre-remediation text only 19% of those spans
matched literally.

What the exercise was actually about, in one line: the test is not *is this
jargon* but **is the referent something the paper contains**. Both failure modes
reduce to it — `C1` and `D6` name nothing a reader can look up, and "open — no
corpus content" describes a repository the reader cannot see.

Follow-ups that outlived this bean, all recorded and none silently dropped:

* the `-1/12` coefficient in `proton-mass-substrate-identity-derivation` wants a
  real witness — the obvious substitute is a *failing* scaffold, so the prose
  states what the number rests on instead;
* `run-validate.ts` checks `#label` cross-references only, so a wrong relative
  path passes silently — several dead links surfaced by hand during this work;
* `substrate wall`, 108 uses and defined nowhere. Manuscript voice, not branch
  jargon, so out of scope here — but underdefined.
