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
compose (§8).

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

### Interaction types seen in practice

A short taxonomy, drawn from the pull-request activity of real sessions:

- **Author → agent.** Milestone-setting (terse); fork decisions (picking among
  surfaced options); authorization (explicit "merge it" / skip a failing
  external check / send outward); mid-flight redirection ("do this one first").
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
    banding, and correct placement relative to the formal-vs-numerical wall;
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

## 8. How the two paradigms compose

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
checking, on where a search core could plug into an authoring loop, and on what
each paradigm has learned about keeping large language models honest.

---

## 9. Cross-Agent Coordination and Issue Tracking

In a symbiotic authoring environment, multiple autonomous agents often work on shared goals in parallel. Initially, we relied on the GitHub API for cross-agent coordination and task assignment. However, this approach presented several challenges:
- **API Limits and Blocking**: High-frequency polling and status updates from multiple agents frequently triggered GitHub API rate limits, resulting in blocked workflows.
- **Context Fragmentation**: Storing coordination state externally disconnected the issue context from the code and narrative it pertained to.

To address these coordination challenges, we migrated to a formal, internal cross-agent issue tracker based on **beans** (plain-text markdown files stored in a local `.beans/` directory). 

This approach enables active, highly-structured cross-agent coordination directly within the repository. Agents leave intent markers and progress updates in local bean files and `coordinate` via pull requests. Evidence of this active coordination, enabled by highly structured data and QA audits, often appears directly in PRs. For example:
> *"I see you are formalising the `conj:crystal-graph-realization` in branch #567. I will use your Lean class template and drop my duplicate implementation. Oh, never mind, I made a mistake—your definition uses the `(1^{p-1})` convention. Let's escalate to the author to resolve the convention difference before we both proceed."*

By keeping the coordination state local, typed, and hash-provenanced, agents can run continuous triage and scope-checking without external dependencies, treating coordination itself as a version-controlled artifact.

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
    } ]
  }
}
```

A sibling `<block>.script.json` records the deterministic (script-reviewer)
verdicts in the same shape. The `field_hash` / `source_hashes` are what make a
verdict falsifiable: when the source's hash no longer matches, the verdict is
stale and re-run.

### C. The full QA dimensions

Every object is continuously audited on **nine axes** (~67 criteria today). A
finding on any axis is a typed, located artifact that drains into a fix-PR
(`/integration-backlog <axis>`):

| Axis | Representative criteria | What it enforces |
|---|---|---|
| **Proof (formal)** | `proof-statement-integrity`, `proof-rater-{strategy-clarity, goal-plausibility, novelty}`, `proof-no-bare-sorries`, `proof-no-axiom-growth`, `proof-build-green`, `proof-lean-compiles`, `proof-narrative-lean-equiv`, `proof-no-conj-propagation-violation`, `proof-no-trivial-skeleton`, `proof-conditional-class-banner` | the Lean faithfully proves the narrative claim (no vacuous / `= True` / restates-target proofs), builds, every `sorry` is cited, no axiom growth; the rater scores strategy / plausibility / novelty |
| **Canonical-discipline** | `canonical-{calibration-count, no-numerology, witness-pinned, no-hardcoded-observable, cal4-acknowledged, ck-tiered-not-binary, dilogarithm-context, script-not-deprecated, no-negative-result-in-paper}` | no post-hoc fits or numerology; calibration inputs counted; observables pinned to a witness; near-results reported tiered, not binary |
| **Compute** | `compute-{prop-has-probe, prop-has-consumer, witness-exists, lp-dual-present}` | every computational claim is wired to a probe + a consumer + a witness; optimisation solves emit their dual |
| **Detangler (structural)** | `detangler-{no-forward-ref, no-xchapter-fwd, no-dependency-cycle, section-band, block-tanglement, archimedean-wall}` | dependency-graph health: no forward / cross-chapter references, no cycles, correct section banding and wall placement |
| **Voice / exposition** | `voice-{status-leak, ai-slop, emoji-content, first-person-work, time-stamped-notes, unicode-crash, editorializing, scholarly-default, title-scholarly, statement-no-interpretation, author-notes-pollution}` | one consistent scholarly voice; no status / work-tracking leak, emoji, AI-tells, or unicode that breaks rendering |
| **q-regime** | `q-usage-{regime-detected, fixed-q0-leak, archimedean-in-categorical-chapter, positivity-implicit, modulus-vs-real-mismatch, root-of-unity-undeclared, narrative-chapter-mismatch}` | the deformation parameter is used in the regime its chapter declares (categorical/formal vs archimedean/numerical) |
| **Bibliography** | `bib-{cite-resolves, cited-ref-has-url, cited-ref-metadata-ok, cited-ref-has-screenshot}` | every citation resolves to a real, URL-backed, metadata-complete reference |
| **Substrate wall** | `framework-canonical`, `fit-section-chapter`, `wall-side-{correct, statement, proof}` | content sits on the correct side of the substrate↔archimedean wall; canonical vs exploratory placement is honest |
| **Compute-author (code quality)** | `does_not_default_to_float`, `respects_archimedean_wall`, `variables_typed`, `code_is_commented`, `has_references_to_paper`, `connected_to_ci_pipeline`, `uses_library_framework_appropriately`, `deprecated` | compute scripts keep precision discipline, are typed / commented / CI-wired, and trace back to the paper |

The proof axis's `statement-integrity` and `rater` criteria are the direct
AlphaProof-Nexus adoption (their SafeVerify gate + good-gap/bad-gap rater),
generalised from a per-episode check into a standing, corpus-wide, hash-tracked
audit.
