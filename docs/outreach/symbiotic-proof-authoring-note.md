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

| Dimension | Autonomous proof search | Symbiotic authoring (Folio) |
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
