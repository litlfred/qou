# Symbiotic proof authoring — a note for autonomous formal-proof-search teams

*An informal companion piece to* **"Advancing Mathematics Research with
AI-Driven Formal Proof Search"** *(AlphaProof Nexus, Google DeepMind,
arXiv:2605.22763). It is not a paper. It sketches a complementary paradigm —
**symbiotic authoring** — implemented in a system we call **Folio**, and
highlights the capabilities a long-lived human–machine authoring partnership
needs that an autonomous solve-and-return loop does not. We admire the
Nexus results and think the two paradigms compose; this note is an invitation
to compare notes.*

---

## 1. Two paradigms, not one

**Autonomous proof search** optimizes a sharp objective: given a
`theorem … := by sorry`, return a `sorry`-free proof, and maximize
problems-solved-per-dollar. The proof is the product; the interaction ends when
the compiler is satisfied.

**Symbiotic authoring** optimizes a different objective: keep a *growing body of
mathematics* — its narrative, its formalization, and the numbers and figures
that support it — correct, mutually consistent, and legible to humans across
months of editing by many hands. A machine-checked proof is necessary but not
sufficient; the durable product is an auditable knowledge base a person can
read, trust, cite, and extend.

The two are not rivals. Autonomous search is a superb way to *close goals*;
symbiotic authoring is about *keeping a living, legible, trustworthy body of
mathematics around them*. The most interesting design space is where they
compose (§10).

| Dimension | Autonomous proof search (AlphaProof Nexus) | Symbiotic authoring (QOU / Folio) |
|---|---|---|
| Objective | `sorry`-free proof; max solves/\$ | correct, in-sync, legible corpus over time |
| Atomic unit | a Lean proof file ("sketch") | a *knowledge object* = narrative + formal + manifest |
| Interaction | query → solve → return | continuous co-authoring round-trip |
| Natural-language proof | auto-generated to mirror the Lean | authored, audited, **authoritative** |
| Unproven step | `sorry` (graded by a rater) | `sorry` **+ mandatory checkable citation** |
| Result downstream of a conjecture | not tracked | **typed**; cannot be called a "theorem" |
| Misformalization | detected reactively | audited **proactively** (narrative ↔ formal) |
| Computed numbers / figures | out of scope | **witnessed**, hash-provenanced, staleness-tracked |
| QA | generation-time (rater + verifier) | **continuous, corpus-wide**, hash-stale-tracked |
| Authority | agent acts autonomously | agent drafts; **human approves & closes** |

### Differentiators at a glance

Feature by feature — what the authoring layer adds *around* a proof-search core:

| Capability | AlphaProof Nexus (autonomous search) | QOU / Folio (symbiotic authoring) |
|---|---|---|
| **Authoritative narrative** | auto-generated NL proofs that *mirror* the Lean, not authored exposition | the prose is the audited scholarly face, co-evolved with the formalization (voice / readability / conciseness / narrative↔formal-equivalence audits) |
| **Hallucinated-lemma defense** | no citation gate; agents `sorry`-ed fabricated "known results" | every deferred step needs a citation key that resolves against a typed reference database → directly blocks failure mode (b) |
| **Offloading defense** | could not be prompted away | a conjectural-propagation type system: a result downstream of an unproved input *cannot be typed a theorem* unless it carries that input as an explicit hypothesis → structurally blocks failure mode (a) |
| **Misformalization** | *reactive* (the wrong reading is proved, then a human notices) | *proactive* narrative↔formal equivalence audit ("do they prove the same thing?") |
| **Numeric / figure provenance** | out of scope (pure-math proofs) | witness records with producing-script hash + staleness tracking; optimisation solves emit their dual |
| **Don't-redo-known-work** | n/a (open is the goal) | a backward corpus-grep before anything is declared "open" |
| **Continuous corpus QA** | QA at *generation* time only (rater + verifier) | multi-axis watchers (proof / canonical / compute / detangler / voice / regime) + per-block `.qa.json` sidecars, hash-stale-tracked |
| **Anti-overfitting firewall** | the *opposite*: value-search markers actively reward parameter search | a production-vs-exploratory firewall refuses unjustified fitted constants in the authoritative text |

The last row is the key inversion: **AlphaProof Nexus's core strength —
searching a value space — is QOU/Folio's core hazard.** Anything QOU/Folio
imports from the autonomous side (an `EVOLVE-VALUE`-style marker especially)
must land *inside* the production-vs-exploratory fence, or it becomes a
numerology generator.

---

## 2. The atomic unit: a knowledge object, not a proof file

Your unit of work is a Lean file. Ours is a **content object**: a triple of
sibling files that share a name and are validated to agree.

- **A typed manifest** — machine-readable metadata: the object's kind
  (definition / theorem / lemma / conjecture / remark / …), a stable label, its
  immediate dependencies, its citations, and rendering hints.
- **A narrative** — the human-readable statement, motivation, and
  interpretation.
- **A formalization** — the machine-checked statement and proof.

The kind drives obligations: a *definition* must have a formalization; a
*theorem* is expected to; a *conjecture* may carry an unproved placeholder by
design. Because the three faces are separate artifacts, the framework can — and
does — check that they tell the same story. The proof file is one face of the
object, not the object itself.

---

## 3. Expected mode of interaction

The defining difference is **round-trip, not solve-and-return.**

- **Human-initiated.** A mathematician edits the narrative or the formalization.
  The agent then formalizes the new gap, cross-checks narrative against formal,
  updates the manifest and dependency edges, and flags anything that drifted out
  of sync.
- **Agent-initiated.** Persistent background "watchers" continuously audit
  incoming changes *and* the standing corpus, surfacing findings as a
  **prioritized queue** the human triages — rather than the agent silently
  acting on everything.
- **Authority boundaries are explicit.** Agents may draft, branch, open pull
  requests, and run audits; **humans approve merges and close work items.** An
  agent never marks its own work "done," and capabilities are gated by a
  reader / collaborator / owner role hierarchy.
- **Every agent action yields an auditable artifact** — a citation, a QA
  sidecar, a provenance record, a typed status — never an opaque "trust me."

Culturally: the agent is a **co-author and continuous reviewer**, not a solver
you query and walk away from.

### The loop, concretely

A tranche of work runs as a five-step round-trip:

1. **The author sets a terse, high-level milestone** — "adopt these methods,"
   "extend the baseline audit to every chapter," "prepare this for merge,"
   "drain the new findings." The agent decomposes it into a prioritized
   work-plan and executes.
2. **The agent works autonomously _within standing constraints_** and
   **surfaces** two things: *findings* (what it discovered) and *genuine
   decision-points* (forks only the author can resolve) — the latter as options
   with full evidence attached, never a bare yes/no.
3. **The author decides at the forks.** The agent never merges, nor takes any
   irreversible or outward-facing action, without explicit authorization.
4. **The change lands in the co-authored corpus**, all faces kept in sync
   (narrative + formal + manifest + witness), with an auditable artifact for
   every step.
5. **Reviewers and continuous QA close the loop** (§4–§5); the agent
   dispositions every review comment — fix it, or explain on the record why a
   suggestion is incorrect or conflicts with a house convention.

### The author's role — the *what*, not the *how*

The human owns intent and constraints; the agent owns decomposition, execution,
and QA. Concretely the author supplies:

| The author sets… | …and the agent does |
|---|---|
| **Milestones** — goals and their order | decomposes into a work-plan; executes; reports |
| **Conjectures & proof strategies** — the mathematical direction (which results to pursue, which closure ansätze to test or refute) | formalizes, refutes, wires the compute, surfaces what holds |
| **Constraints** — a large standing body of rules (calibration discipline / "no post-hoc fits"; the formal-vs-numerical regime split; numeric literals pinned to a computed witness so they cannot drift; tiered—not binary—reporting of near-results; merge discipline; accessibility) | acts autonomously *inside* the guardrails; flags anything that would cross one |
| **Decisions & authorization** — the call at each fork; explicit sign-off for merges, CI overrides, outward sends | presents options with evidence; waits; then acts |
| **Ground truth** — source material (papers, measured constants) and final adjudication of correctness | cites it, checks against it, never invents it |

The constraints are the load-bearing part: they are what let the agent run a
long way unattended *safely*, and they are the precise **inverse** of an
autonomous searcher's reward signal — fences that forbid, not markers that
reward exploration.

### Context engineering — the author's primary lever

The single most load-bearing human contribution is not any individual
decision but the **context architecture** the agent works inside. The
corpus is deliberately factored into typed, atomic knowledge objects
(manifest + narrative + formalization) and a library of task-scoped
*skills*, so that the slice of corpus an agent needs for a given task —
together with its constraints and conventions — fits inside a model
context window and arrives already typed, current, and
provenance-carrying. Setting context is not preamble to the
methodology; it **is** the methodology's human half. The standing
constraints of the table above are one face of it; the
retrieval-sized factoring of content and skills is the other. An
autonomous solve-and-return loop has no analogue of this lever,
because its unit of work (one goal) never outlives one context.

### Socratic steering — known-answer questions as a root-finding scheme

A second pattern the session transcripts show: the author frequently
asks questions whose answers he knows or nearly knows — not to obtain
the answer, but to steer the agent's search toward the intended
target. The dynamic is that of a damped root-finding iteration: the
agent proposes, the author's question supplies a correction *near the
truth*, and convergence is fast precisely because the initial
corrections are good. Crucially, the same channel carries the
opposite case with an honest marker — the author flags genuine
knowledge gaps as such ("I don't recall…", "is X true?") so the agent
can distinguish steering from sincere inquiry and raise its evidence
threshold accordingly. The discussion-corpus meta-analysis (a planned
companion artifact over the archived sessions) can classify these
question types and measure their effect on convergence — turning an
anecdotal methodology claim into a measurable one.

We adopt this leg formally from **coactive learning** [2, 3]: the
author's question is α-informative feedback — an improvement toward
the target, deliberately not the gold standard — and the regret bounds
scale with correction quality α, which is exactly the "good initial
corrections" clause. A recent line applies the same model to LLMs
directly [4]. The surrounding field runs the *dual* direction (agents
strategically questioning humans to converge on intent [5, 6]), which
leaves the human-as-Socrates direction, with measured convergence,
unoccupied. The gap-marker leg sits in the sycophancy and pragmatics
literature: user-stated beliefs act as injected evidence that shifts
model confidence [7, 8, 10], and models systematically under-challenge
user presuppositions [9] — the honest-gap convention is a deliberate
de-weighting of that presupposition channel. The classical antecedents
are the classroom-discourse literature's display questions and
scaffolding [13, 14, 16], and the ur-text is the slave-boy episode of
the *Meno* [15]. The planned measurement: per-arc α̂ and
turns-to-convergence T, estimated from the archived transcripts.

### Intuition seeding — tenuous identifications, rapidly rigorized

A third register completes the picture, and it is the inverse of
steering. Some of the author's inputs are **cross-domain
identifications that exist in neither the literature nor the model's
usable priors** — offered *flagged as tenuous* ("could the Reeb flow
be linked to the Julia-set dynamics here?"). For these the agent's job
is not convergence toward a known target but **cheap decisive
(in)validation followed by rigorization of survivors**: a corpus check
(is it already resolved here?), then the least expensive structural
argument or probe that can kill or confirm the identification, then —
only for survivors — formal development. The division of labor is the
point: the human generates low-probability, high-value hypotheses that
no retrieval process would surface; the machine validates in minutes
what would once have cost the author weeks, which is precisely what
makes tenuous identifications *rational to voice*. The meta-analysis
inventories these events with a literature-absence check, so novelty
attribution (which identifications originated as author intuition) is
auditable rather than anecdotal. The three registers — steer, honest
gap, seed — and the corresponding agent protocols are codified as a
platform skill (`symbiotic-interaction`).

### Interaction types seen in practice

A short taxonomy, drawn from the pull-request activity of real sessions:

- **Author → agent.** Milestone-setting (terse); fork decisions (picking among
  surfaced options); authorization (explicit "merge it" / skip a failing
  external check / send outward); mid-flight redirection ("do this one first");
  Socratic steering (known/nearly-known-answer questions as course
  corrections, with genuine knowledge gaps flagged as such).
- **Reviewer (automated) → agent.** Bot reviewers comment on landed commits; the
  agent dispositions each as **fix** (valid), **decline with rationale** (e.g. a
  relative-link suggestion that conflicts with the repo's stable-URL convention),
  or **refute** (a false positive the agent verifies is absent) — the
  disposition is recorded, not silent.
- **Agent → sub-agent.** A lead agent dispatches background workers (corpus-wide
  audits, environment-setup-and-fix) and integrates their reported findings;
  workers emit only auditable artifacts and never merge.
- **System → agent.** CI / webhook signals are **diagnosed, not blindly
  chased** — an infrastructure (billing) failure is distinguished from a code
  failure and handled by proceeding on a green local check rather than pushing
  retrigger commits; lifecycle hooks (watch upstream, coordinate sibling PRs,
  check uncommitted state) keep the agent durable across interruptions.

The through-line: the agent **asks only when genuinely blocked on a call that is
the author's to make**, and otherwise turns its work into reviewable artifacts
rather than acting opaquely.

---

## 4. Safeguards aimed squarely at the failure modes you reported

Your paper names two failure modes of autonomous search. We treat both as
first-class, *enforced* invariants rather than behaviors to prompt against.

**(a) "Offloading the core difficulty into a single `sorry` in a helper lemma
that restates the target."**
→ **Typed conjectural propagation.** A claim that depends (transitively) on an
unproved input *cannot be typed as a theorem*. It must be either an honest
conjecture, or a **conditional result that carries the unproved input as an
explicit hypothesis** (formally, a typeclass instance the downstream proof
consumes). You cannot launder an open assumption into a "proved" theorem by
hiding it in a helper lemma — a propagation audit walks the dependency cone and
rejects it. The honest options remain open; the dishonest one is unspellable.

**(b) "`sorry`-ing lemmas the agent claims are established literature, which turn
out to be hallucinations."**
→ **Mandatory checkable provenance.** Every deferred step must carry a citation
key that resolves against a typed reference database; an *uncited* deferral is
an automatic review failure, and the bibliography is cross-checked for real
identifiers (DOIs, etc.). A hallucinated "well-known result" cannot pass unless
it names a registered, resolvable reference — which a fabricated one does not.

And a third safeguard, for a problem you handle reactively:

**Misformalization → narrative ↔ formal equivalence audit.** Because the prose
statement and the formal statement are *separate artifacts that must agree*, the
framework audits that they assert the **same** claim. A quantifier that flipped,
or a definition sense that drifted (your "density" → "lower/upper density"
example), is caught **by design, before** a proof of the wrong reading is ever
attempted — not discovered after a human notices the agent proved the wrong
thing.

---

## 5. Provenance and continuous QA

- **Multi-reviewer QA sidecars.** Each object carries a sidecar recording which
  automated reviewers examined it and against which **content hash**. When the
  source drifts, the affected audits are auto-invalidated and re-run. QA is
  continuous and corpus-wide, not only at the moment of generation.
- **A dependency graph.** A `uses` relation across objects, combined with the
  formal import graph, forms a DAG used to scope re-validation after an edit,
  compute the downstream blast radius of a change, and prioritize formalization
  by number of dependents. (Where your global goal-cache reuses *goal states*,
  this is a *semantic* graph spanning narrative and formal.)
- **Witnessed values.** Any computed or empirical number that enters the text is
  backed by a witness record carrying the producing script's hash and commit,
  and is staleness-tracked: if the script changes, the value is flagged for
  refresh. Reproducibility of the **non-proof** parts of a result is enforced
  too — a concern that simply doesn't arise for pure proof search, but is
  central whenever mathematics meets computation or data.
- **The QA is multi-axis, not a single rater.** The same per-object sidecar
  carries *several independent audit axes*, each a mix of deterministic
  script-checkers and agentic raters:
  - **formal / proof** — a multi-criterion proof rater (strategy clarity, goal
    plausibility, novelty) plus a hard **statement-integrity** check (a vacuous
    `⟨_, rfl⟩` "proof," a `= True` restatement, or a Lean statement that does not
    match its narrative is *failed*), and structural checks (no bare `sorry`, no
    axiom growth, the Lean builds);
  - **structural / detangler** — dependency-graph heuristics: forward-reference
    and dependency-cycle detection, cross-chapter reference limits, section
    banding, per-chapter topic coherence, a within-section graph-energy measure
    of reading order, and correct placement relative to the formal-vs-numerical
    wall — each verdict carrying a snapshot of the block's graph position
    (degree, dependency-cone size, edge span, PageRank);
  - **canonical-discipline** — no numerology, no undisclosed fitted constants,
    calibration-count and tiered-reporting checks;
  - **compute** — every computational claim has a witness; optimisation solves
    emit their dual; producers are not stale;
  - **voice / exposition** — consistent authorial voice, no status-leak or
    work-tracking residue in scholarly prose, notation-register compliance;
  - **parameter-regime** and **bibliography** — domain-specific regime and
    citation-resolution checks.

  Each criterion stores an array of reviewer results under one shared schema;
  each result records its **outcome** (pass / warn / fail), a **severity**, an
  **optional score**, the **reviewer** (a script or an agent, with its id), the
  **content hash** of the `.md` / `.ts` / `.lean` it judged, a **timestamp**, and
  **quoted evidence**. The content hash makes every verdict falsifiable and
  auto-stale on edit: a verdict whose hash no longer matches the source is re-run.
- **Findings drain back into the loop.** Because every verdict is a typed,
  located artifact, the failing ones cluster automatically into review-sized
  fix-batches — each becomes a pull request that is prepared, reviewed, and
  merged — so "audit the corpus" and "improve the corpus" are the same machine,
  run continuously rather than as a one-off pass.

---

## 6. A discipline against overfitting

One inversion is worth flagging, because it is a genuine difference in values.

Your `EVOLVE-VALUE` markers *reward* searching a parameter space — exactly the
right move for discovering, say, a better step-size schedule. In a long-lived
corpus the same freedom is a **hazard**: a fitted constant can quietly
masquerade as a derived one, and "the search found a number that works" is not
the same as "we understand why." We therefore keep an explicit
**production-vs-exploratory firewall** that separates canonical derivations from
exploratory fits and refuses to let an unjustified fitted parameter enter the
authoritative text.

This is not a rejection of your idea — we would happily adopt an
`EVOLVE-VALUE`-style marker — but as a **fence that labels the few legitimately
tunable knobs**, not as open license. Conversely, your rater's
**good-gap / bad-gap** rubric (routine/technical gaps are acceptable to defer;
core-insight "miracle" gaps are not; an honest gap beats a no-gap dead end) is a
sharp articulation we are adopting into our own gap-triage discipline. Credit
where due.

---

## 7. Exposition as a first-class artifact

Your results repository pairs Lean with natural-language proofs that *mirror* the
formal structure. In a symbiotic setting the narrative is the **authoritative
human face** of the work and is itself audited: a consistent authorial voice, a
controlled notation register, terminology and glossary checks, and conciseness
passes. The single source then renders to multiple targets — typeset PDF, HTML,
a formal "blueprint," and dependency-graph visualizations. The reader engages
with the mathematics, not the manifest.

This matters because the bottleneck symbiotic authoring targets is not "can a
proof be found" but "can a human quickly *understand, trust, and build on* what
was found." Formal verification answers the first; audited exposition plus
provenance answers the second.

---

## 8. Many agents, one adjudicator

In practice the loop of §3 is rarely a single agent. The working method that
emerged over months of daily use is **deliberately redundant**: several agent
sessions are pointed at the *same* problem from *different* perspectives — a
different framing of the question, a different skill profile, a different
branch — while the human author holds the three roles no agent holds:
**adjudicator** (which answer survives), **priority-setter** (which line gets
the next session), and **source of intuition** (which approach is worth
pursuing, and which two distant-looking things are secretly the same thing).

The obvious reading of this — parallelism as speedup — is the wrong one.
Running one iterative scheme on more workers makes the same answer arrive
sooner; that is Newton's method with a larger budget. The value of redundant
*perspectives* is **evidential, not computational**:

- **Agreement amplifies.** When approaches with genuinely different failure
  modes — a structural derivation, an independent high-precision numerical
  probe, a formalization attempt — converge on the same answer, the
  convergence is evidence of a kind that no single method's internal
  confidence can supply. (Internal cross-method agreement is a standing
  target of the framework's compute discipline for exactly this reason.)
- **Disagreement localizes.** When two approaches diverge, the divergence is
  a pointer: the error lives in an assumption they do not share. In one
  episode, six independently conceived closure ansätze for the same
  per-partition quantity all failed on the simplest test nucleus — which
  condemned the framing they shared, not the six implementations.
- **Hallucination decorrelates.** A single session can confabulate fluently
  and consistently *with itself*. It is much harder for several sessions,
  primed differently, to confabulate the *same* fabrication. This is
  independent-witness logic, and it is the cheapest hedge against model
  hallucination we have found.

The machine-learning literature reaches nearby conclusions from inside a
single model: sampling diverse reasoning paths and keeping the consensus
answer (self-consistency; Wang et al. 2023), letting several model instances
debate (Du et al. 2023), and reading divergence across stochastic samples as
a hallucination signal (Manakul et al. 2023). Our practice differs in two
ways. The diversity is **engineered at the level of method and framing**, not
sampled from one prompt — different skills, different starting documents,
different branches. And the aggregation is **not a vote**: the author
adjudicates, because the witnesses are not exchangeable — a one-line
structural refutation outweighs three numerical probes that agree, and
knowing which is which is precisely the intuition the human contributes. The
division of labor that machine-assisted mathematics keeps arriving at —
machine breadth, human judgment (Tao 2025) — is, in our experience, not a
transitional arrangement but the design.

Mechanically, the redundancy is cheap because the infrastructure assumes it:

| Mechanism | Role in the independent-witness scheme |
|---|---|
| Several sessions on one problem, differently framed | the witnesses themselves |
| Sibling-PR coordination (a standing skill: intent comments posted on branches with overlapping scope) | witnesses *know of each other*; overlap surfaces at the first commit, not at merge time |
| Coordination ledgers (one shared markdown ledger per theme, under `docs/coordination/`) | adjudication memory — what was decided, by whom, on what evidence |
| Standing integration watchers | auditors that re-examine everyone's landed work on every QA axis of §5 |
| Cross-model review on every pull request | each PR is reviewed by automated reviewers from *different model families* (currently Gemini Code Assist and GitHub Copilot) in addition to the authoring agent — heterogeneous models as decorrelated error channels |

The ledger row deserves emphasis, because redundancy has a failure mode of
its own: **oscillation**. Independent sessions that share no memory can each
re-derive a defensible-looking but opposite conclusion. Our canonical example
is a precision-affecting coefficient that was wired into the production
formula and un-wired again four times by different sessions over five days —
each flip locally well argued. The oscillation itself was the diagnostic: two
true facts ("truncating the series at this order beats the experimental bar"
and "the coefficient equals this exact constant") had been conflated into one
claim. The repair was **adjudication memory**: a ledger that records every
flip with its commit, its argument, and its error mode, and that any new
session must read before re-litigating; the question was then settled once,
with a tiered verdict (proved / near-match / fitted) rather than a binary
one. The flip-flop table for that coefficient holds six entries and has
stopped growing.

Human adjudication is what makes redundancy converge instead of oscillate;
the ledgers are what make the adjudication durable.

---

## 9. An honest limitation: the corpus no longer fits in the window

Symbiotic authoring has a structural weakness that autonomous, per-problem
search does not, and it deserves to be stated plainly.

The corpus long ago exceeded every available context window. The content tree
alone is roughly nine megabytes of narrative markdown across some three
thousand files, alongside roughly four thousand typed manifests and a
dependency graph of several thousand edges. Even the dependency DAG *by itself* — every
object's label, kind, and edges, with no bodies at all — no longer fits in a
single window. No session, however long, sees the whole corpus; every agent
works from a window-sized slice of it.

The recurrent symptom is **failure to recall that a result already exists.**
The author's most common intervention, across months of sessions, is some
variant of *"didn't we prove that already?"* — and it resolves in two
distinct modes that are worth separating, because only one of them is even
partially a solved problem.

**Mode 1 — retrieval failure.** The result exists, verbatim or nearly; the
agent simply did not look where it lives. A representative exchange:

> **Author:** Why are you deriving the selection rules from scratch? We
> proved that already — the partition shapes give the rules. See the
> molecular-angles analysis.
>
> **Agent:** I don't have that in context — searching the corpus for it now.
> […] Found it: the symmetric-block analysis derives the bond-angle table
> from the partition data, and the rule I was about to re-derive is a special
> case of its master table. Citing that instead.

The agent's "memory" of the corpus is whatever it greps during the session;
the pointer had to come from the author. In the worst observed run of this
failure, three consecutive audit items were declared "open" against a single
source file's stale status note, each later found to be already resolved
elsewhere in the corpus; the post-mortem traced all three to the same scoping
error — trusting one file's self-description instead of searching the whole
tree.

**Mode 2 — the analogy the system could not surface.** Sometimes *"didn't we
prove that already?"* is not about a missed search hit but about the author's
intuition that two superficially different concepts are the same concept — a
connection no string search would return, because the two passages share no
vocabulary (one phrased in knot diagrams, say, the other in representation
data). These are the productive ones: once stated, the connection often
collapses a planned derivation into a citation plus a translation lemma. The
system has no mechanism that produces these. The author does.

Our current mitigations are **search discipline, not learned retrieval**: a
mandatory backward corpus-grep before any agent may declare an item "open"
(four search paths — the audit record, the whole content tree, the
computation scripts, the coordination ledgers — must all come back empty);
the content-hash-pinned QA sidecars of §5, which at least keep what *has*
been audited from silently drifting; the standing watchers, which re-walk the
corpus continuously; and, candidly, the author's episodic memory, which
functions as the de-facto retrieval index of the project. These measures have
substantially reduced mode-1 failures. They do nothing for mode 2.

The honest gap, then: the project uses **no retrieval-augmented generation
and no knowledge-graph memory layer.** Retrieval-augmented architectures are
well established (Lewis et al. 2020), and the strongest current practice for
grounding language-model agents in a large structured corpus comes from
biomedicine — e.g. PrimeKG, a multimodal precision-medicine knowledge graph
(Chandak, Huang & Zitnik 2023), and the knowledge-grounded agents built over
such resources by the same group (Gao et al. 2025). We have nothing
comparable, and we feel the absence weekly. The irony is that a typed
knowledge graph already implicitly exists here: the `uses` / `interprets`
dependency DAG over typed content objects *is* one — typed nodes (definition
/ theorem / conjecture / …), typed edges (dependency, interpretation,
citation), each node carrying a narrative face well suited to embedding.
Grounding agent retrieval in that graph, rather than in the author's memory
plus a grep, is the most obvious next step this project has not taken. The
constraint any such layer must respect is the one this note keeps returning
to: retrieval may *propose*, but provenance still *disposes* — a recalled
claim enters the text only with its citation, hash, and typed status intact.

---

## 10. How the two paradigms compose

We see autonomous search and symbiotic authoring as **layers, not competitors.**

- **Your search core is a natural tool inside our loop.** Once a gap has been
  classified as "routine," an autonomous prover — yours, or an open one — is
  exactly what should discharge it. A returned **disproof** is just as valuable:
  it refutes a candidate lemma and prunes a line of attack.
- **Our layer supplies what a durable corpus needs around that core:**
  provenance, audited narrative, continuous corpus-wide QA, dependency tracking,
  and human authority boundaries.
- **Disciplines flow both ways.** Your good-gap/bad-gap rubric and EVOLVE
  markers flow *upstream* into our authoring guidance; our citation and
  conjectural-propagation invariants flow *downstream* as guardrails on what any
  search agent is permitted to call "proved."

A one-line summary:

> **Autonomous search closes goals; symbiotic authoring keeps a living,
> legible, trustworthy body of mathematics around them.**

We would genuinely enjoy comparing notes — on the gap taxonomy, on integrity
checking, on where a search core could plug into an authoring loop, on memory
and retrieval over corpora that no longer fit a context window (§9), and on
what each paradigm has learned about keeping large language models honest.

---

## Appendix: content blocks, sidecars, and the full QA dimensions

A concrete look at the data structures the workflow above operates on.

### A. Content-block kinds (the atomic unit)

Each knowledge object's *kind* drives its formal obligation and its label prefix:

| Kind | Lean formalization | Label prefix |
|---|---|---|
| `definition` | **required** (enforced at type level) | `def:` |
| `theorem` / `lemma` / `proposition` / `corollary` | expected (warning if missing) | `thm:` / `lem:` / `prop:` / `cor:` |
| `conjecture` / `example` / `remark` | optional (a conjecture may carry an unproved placeholder by design) | `conj:` / `ex:` / `rem:` |
| `simulator` | n/a | `sim:` |
| `prose` / `equation` / `diagram` | n/a | — |

A `theorem`/`lemma`/`proposition`/`corollary` whose dependency cone touches a
`conjecture` cannot stay a provable kind: it is demoted, or made conditional on
the conjecture as an explicit hypothesis (typed conjectural propagation, §4).

The manifest face of the triple (§2) is a TypeScript **discriminated union**:
`kind` is the discriminant, and the type system is what turns editorial policy
into compile-time obligations — a `definition` without a Lean reference does
not validate. Abridged from the production schema:

```ts
/** Fields shared by every block kind. */
interface BlockBase {
  label: string;        // kind-prefixed, stable, unique ("def:quantum-universe")
  title?: string;
  uses?: string[];      // IMMEDIATE dependencies only — the DAG edges; bare
                        //   label, "paper-dir:label", or cross-folio URL
  cites?: string[];     // bibliography keys (auto-extracted from \cite{})
  tags?: string[];
  authorNotes?: AuthorNote[]; // status / caveat / deprecation metadata, kept
                              //   out of the scholarly prose and skipped by
                              //   the default render (one-voice discipline)
}

/** A definition MUST be formalized — enforced by the type. */
interface DefinitionBlock extends BlockBase {
  kind: "definition";
  lean: LeanRef;        // package-qualified: "qou:QOU.Torsion.lifting_exists"
  examples?: string[];
}

/** Provable kinds: Lean expected but may be in flight. */
interface ProvableBase extends BlockBase {
  lean?: LeanRef;       // missing ⇒ pipeline warning, not error
  proofs?: string[];    // labels of proof blocks
  examples?: string[];
}

/** A remark must name the formal object it glosses. */
interface RemarkBlock extends BlockBase {
  kind: "remark";
  interprets?: string;  // the provable block this remark explains — a remark
                        //   with claims but no interprets is "dangling"
  computation?: Computation; // optional computational witness backing
}

type Block =
  | DefinitionBlock | TheoremBlock | LemmaBlock | PropositionBlock
  | CorollaryBlock | AlgorithmBlock | ConjectureBlock | ExampleBlock
  | RemarkBlock | ProofBlock | SimulatorBlock | ProseBlock
  | EquationBlock | DiagramBlock | TableBlock;
```

Three fields do the structural work. `kind` is the policy discriminant:
validation, label prefix, and formal obligation all dispatch on it (the table
above). `uses` declares *immediate* dependencies only, so the corpus-wide
dependency DAG is the transitive closure of locally asserted edges — this,
together with `interprets`, is the typed graph that conjectural propagation
(§4), the watchers (§5), and the implicit knowledge graph of §9 traverse. And
`lean` is a package-qualified reference into the Lake workspace, which is what
lets a hash-pinned QA verdict (below) assert not merely that *a* proof exists,
but that *this* proof, of *this* statement, at *this* content hash, compiles.

### B. The QA sidecar (`<block>.qa.json`)

One sidecar per object. Under each criterion id sits an append-only array of
reviewer verdicts (script, agent, or human), each pinned to the content hash it
judged so it auto-stales on edit:

```jsonc
// <block>.qa.json   —   criteria: { "<criterion-id>": QaCriterionEntry[] }
{
  "kind": "theorem",
  "source_hashes": { "ts": "<sha12>", "md": "<sha12>", "lean": "<sha12>" },
  "criteria": {
    "proof-statement-integrity": [ {
      "field_hash":   { "md": "<sha12>", "ts": "<sha12>", "lean": "<sha12>" },
      "result":       "fail",                  // pass | warn | fail | n/a
      "severity":     "critical",              // critical | major | minor (optional)
      "reviewer":     { "kind": "agent", "id": "local/lean-proof-review" },
      "reviewed_at":  "2026-06-07T...Z",
      "reviewed_sha": "<commit>",
      "evidence":     "Lean is `<_, rfl>` — a vacuous existence tautology, not the md claim"
    } ],
    "proof-rater-goal-plausibility": [ {
      "field_hash":   { "md": "<sha12>", "ts": "<sha12>", "lean": "<sha12>" },
      "result":       "fail",
      "score":        { "value": 0.3, "max": 1 },   // scored raters carry a 0..1 score
      "reviewer":     { "kind": "agent", "id": "local/proof-integration-watcher" },
      "reviewed_at":  "2026-06-07T...Z",
      "reviewed_sha": "<commit>",
      "evidence":     "core gap: the key step is an axiom"
    } ],
    "detangler-block-tanglement": [ {
      "field_hash":   { "md": "<sha12>", "ts": "<sha12>" },
      "result":       "pass",
      "reviewer":     { "kind": "script", "id": "content/pipeline/qa-checkers-extended.ts",
                        "script_hash": "<sha12>" },   // the checker's own hash — a
                                                      //   checker bug fix auto-stales
                                                      //   every verdict it ever wrote
      "reviewed_at":  "2026-06-12T...Z",
      "reviewed_sha": "<commit>",
      "metrics":      { "tanglement_score": 0, "out_degree": 1, "in_degree": 0,
                        "cone_size": 1, "edge_span_max": 16, "pagerank": 0.0001 }
    } ]
  }
}
```

Three details carry the staleness and trust semantics. *Content staleness:*
the `field_hash` / `source_hashes` make a verdict falsifiable — when the
judged source's hash no longer matches, the verdict is stale and re-run.
*Checker staleness:* a script reviewer's entry also pins the checker's own
source hash (plus a hash of any extra inputs it consulted, e.g. the reference
database), and a per-criterion sidecar (`<criterion-id>.script.json`) records
the same triple globally — so a bug fix to a checker auto-invalidates every
verdict that checker ever wrote, corpus-wide, and the next sweep re-runs them.
*Reviewer provenance:* agent verdicts record the model id, session, and
dispatching skill, so heterogeneous models can audit one another's verdicts —
the same decorrelation logic as the cross-model pull-request review of §8.
Structural checkers additionally persist a descriptive `metrics` snapshot (the
detangler entry above), so the sidecar corpus doubles as a longitudinal record
of the dependency graph's health, not just a pass/fail ledger.

These schemas are deliberately small and language-agnostic. The witness
counterpart already ships as a dual npm + PyPI interchange package
(`witness-schema`) so that non-TypeScript producers emit identical records;
the QA-sidecar schema is the same kind of artifact and could be published the
same way. We would gladly share it as a concrete basis for comparing
QA-and-provenance notes across systems.

### C. The full QA dimensions

Every object is continuously audited on **nine axes**. Measured 2026-06-12:
the corpus holds 2,255 sidecars carrying 62 block-level criteria and 109,815
recorded verdicts — 84,837 script, 24,975 agent, and 3 human (human
adjudication is the reserve tier, spent only on genuine forks); the ninth
axis (compute-script code quality) is audited on the scripts themselves
rather than in block sidecars. A finding on any axis is a typed, located
artifact that drains into a fix-PR (`/integration-backlog <axis>`):

| Axis | Representative criteria | What it enforces |
|---|---|---|
| **Proof (formal)** | `proof-statement-integrity`, `proof-rater-{strategy-clarity, goal-plausibility, novelty}`, `proof-no-bare-sorries`, `proof-no-axiom-growth`, `proof-build-green`, `proof-lean-compiles`, `proof-narrative-lean-equiv`, `proof-no-conj-propagation-violation`, `proof-no-trivial-skeleton`, `proof-conditional-class-banner` | the Lean faithfully proves the narrative claim (no vacuous / `= True` / restates-target proofs), builds, every `sorry` is cited, no axiom growth; the rater scores strategy / plausibility / novelty |
| **Canonical-discipline** | `canonical-{calibration-count, no-numerology, witness-pinned, no-hardcoded-observable, cal4-acknowledged, ck-tiered-not-binary, dilogarithm-context, script-not-deprecated, no-negative-result-in-paper}` | no post-hoc fits or numerology; calibration inputs counted; observables pinned to a witness; near-results reported tiered, not binary |
| **Compute** | `compute-{prop-has-probe, prop-has-consumer, witness-exists, lp-dual-present}` | every computational claim is wired to a probe + a consumer + a witness; optimisation solves emit their dual |
| **Detangler (structural)** | `detangler-{no-forward-ref, no-xchapter-fwd, no-dependency-cycle, section-band, block-tanglement, topic-coherence, graph-energy, archimedean-wall}` | dependency-graph health: no forward / cross-chapter references, no cycles, correct section banding and wall placement, per-chapter topic coherence, and a within-section graph-energy measure of reading order |
| **Voice / exposition** | `voice-{status-leak, ai-slop, emoji-content, first-person-work, time-stamped-notes, unicode-crash, editorializing, scholarly-default, title-scholarly, statement-no-interpretation, author-notes-pollution}` | one consistent scholarly voice; no status / work-tracking leak, emoji, AI-tells, or unicode that breaks rendering |
| **q-regime** | `q-usage-{regime-detected, fixed-q0-leak, archimedean-in-categorical-chapter, positivity-implicit, modulus-vs-real-mismatch, root-of-unity-undeclared, narrative-chapter-mismatch}` | the deformation parameter is used in the regime its chapter declares (categorical/formal vs archimedean/numerical) |
| **Bibliography** | `bib-{cite-resolves, cited-ref-has-url, cited-ref-metadata-ok, cited-ref-has-screenshot}` | every citation resolves to a real, URL-backed, metadata-complete reference |
| **Substrate wall** | `framework-canonical`, `fit-section-chapter`, `wall-side-{correct, statement, proof}` | content sits on the correct side of the substrate↔archimedean wall; canonical vs exploratory placement is honest |
| **Compute-author (code quality)** | `does_not_default_to_float`, `respects_archimedean_wall`, `variables_typed`, `code_is_commented`, `has_references_to_paper`, `connected_to_ci_pipeline`, `uses_library_framework_appropriately`, `deprecated` | compute scripts keep precision discipline, are typed / commented / CI-wired, and trace back to the paper |

The proof axis's `statement-integrity` and `rater` criteria are the direct
AlphaProof-Nexus adoption (their SafeVerify gate + good-gap/bad-gap rater),
generalised from a per-episode check into a standing, corpus-wide, hash-tracked
audit.

### D. Heuristics in practice — a detangler vignette

How a heuristic axis, author adjudication, and the checkers themselves
co-evolve, in one episode:

- **Heuristics emit measures, not just verdicts.** Each block's detangler
  entries record its dependency-graph position — forward references emitted
  and received (computed from declared `uses` edges only, never inferred from
  prose), in/out-degree, dependency-cone size, edge span in reading order,
  PageRank, and a per-section graph-energy aggregate (the `metrics` of
  Appendix B).
- **Findings triage into mechanical fixes vs. judgment calls.** For a flagged
  block, relocation to just after its latest dependency is provably safe iff
  its earliest dependent sits later still; that calculus split one chapter's
  45 graph-energy findings into 12 provably-safe single-block moves, 20
  genuine tangles (a block both used early and using late — only the author
  can split it, drop an edge, or accept it), and the rest incomputable.
- **Adjudication refines the criterion, not just the corpus.** On review, the
  author ruled the flagged cross-section forward edges *intentional* — the
  chapter's deliberate face ordering (algebraic → geometric → archimedean →
  physical → open). The ruling was committed back into the checker, which now
  counts within-section edges only; the entire false-positive class vanished
  (45 → 0) for every future sweep, and no blocks were moved. A parallel
  topic-coherence triage taught the checker that cross-cutting chapters
  legitimately host other chapters' constructions: of 23 flags, 4 were real
  relocations.

This is the §3 loop applied to the QA layer itself: the agent proposes a
heuristic, sweeps the corpus, and surfaces the borderline class; the author
adjudicates it once; the adjudication lands as checker logic — and the next
hundred-thousand verdicts inherit the judgment.

---

## References

Web-verified entries carry links; entries marked **[from memory]** are
confidence-labeled per house sourcing discipline and must be verified
against primary editions before any formal submission.

### Cited by number (§3)

1. *Advancing Mathematics Research with AI-Driven Formal Proof Search*
   (AlphaProof Nexus), Google DeepMind, arXiv:2605.22763.
2. P. Shivaswamy, T. Joachims, *Online Structured Prediction via
   Coactive Learning*, ICML 2012.
   <https://icml.cc/2012/papers/717.pdf>
3. P. Shivaswamy, T. Joachims, *Coactive Learning*, JMLR 16 (2015).
   <https://www.cs.cornell.edu/people/tj/publications/shivaswamy_joachims_15a.pdf>
4. *Coactive Learning for Large Language Models using Implicit User
   Feedback*. <https://openreview.net/pdf?id=Q7cwVnRWAs>
5. *Closing the Expression Gap in LLM Instructions via Socratic
   Questioning*, arXiv:2510.27410.
6. *The Art of Socratic Questioning: Recursive Thinking with Large
   Language Models*, arXiv:2305.14999.
7. *BASIL: Bayesian Assessment of Sycophancy in LLMs*,
   arXiv:2508.16846.
8. *Social Sycophancy: A Broader Understanding of LLM Sycophancy*,
   arXiv:2505.13995.
9. *Accommodation and Epistemic Vigilance: A Pragmatic Account of Why
   LLMs Fail to Challenge Harmful Beliefs*, arXiv:2601.04435.
10. *Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect
    Intrinsic Confidence?*, arXiv:2605.28778.
11. S. Ross, G. Gordon, D. Bagnell, *A Reduction of Imitation Learning
    and Structured Prediction to No-Regret Online Learning* (DAgger),
    AISTATS 2011. **[from memory]**
12. R. Dembo, S. Eisenstat, T. Steihaug, *Inexact Newton Methods*,
    SIAM J. Numer. Anal. 19 (1982). **[from memory]**
13. H. Mehan, *Learning Lessons: Social Organization in the
    Classroom*, Harvard UP, 1979 (display / known-answer questions,
    IRE sequences). **[from memory]**
14. D. Wood, J. Bruner, G. Ross, *The Role of Tutoring in Problem
    Solving*, J. Child Psychol. Psychiatry 17 (1976) (scaffolding).
    **[from memory]**
15. Plato, *Meno* 82b–85b (the slave-boy episode — the original
    known-answer-question convergence demonstration). **[primary;
    edition to be fixed]**
16. H. Lightman et al., *Let's Verify Step by Step*, arXiv:2305.20050
    (process supervision: step-level feedback beats outcome-level).
    **[from memory]**

### Cited by author–year (§8–§9)

- Chandak, P., Huang, K., and Zitnik, M. *Building a knowledge graph to
  enable precision medicine.* Scientific Data **10**, 67 (2023).
  doi:10.1038/s41597-023-01960-3.
- Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., and Mordatch, I. *Improving
  Factuality and Reasoning in Language Models through Multiagent Debate.*
  arXiv:2305.14325 (2023); ICML 2024.
- Gao, S., et al. *TxAgent: An AI Agent for Therapeutic Reasoning Across a
  Universe of Tools.* arXiv:2503.10970 (2025).
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N.,
  Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., and Kiela, D.
  *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.*
  Advances in Neural Information Processing Systems 33 (NeurIPS 2020).
  arXiv:2005.11401.
- Manakul, P., Liusie, A., and Gales, M. J. F. *SelfCheckGPT: Zero-Resource
  Black-Box Hallucination Detection for Generative Large Language Models.*
  EMNLP 2023. arXiv:2303.08896.
- Tao, T. *Machine-Assisted Proof.* Notices of the American Mathematical
  Society **72**(1) (2025).
- Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery,
  A., and Zhou, D. *Self-Consistency Improves Chain of Thought Reasoning in
  Language Models.* ICLR 2023. arXiv:2203.11171.
