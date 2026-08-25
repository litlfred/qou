---
# fwr11
title: 'the canonical proof-parent field `of` is dead — 12 blocks, and the upstream fix'
status: in-progress
type: task
priority: normal
created_at: 2026-08-10T10:55:00Z
updated_at: 2026-08-10T10:55:00Z
parent: fwr6
---
Branch `claude/agent-beans-stalled-ioej5d`, PR #4921. Picked up from the stalled
`fwr10` session.

**What was inherited, and what was not.** PR #4908 carries only the `fwr10` bean
claim. The 37 proposed additions and the verifier that was checking them were
lost with the session context — nothing was committed, so nothing was taken on
trust. The scoping was rebuilt from scratch and reproduces the stalled
session's figures exactly: 510 blocks with an empty `uses[]`; 41 / 69 / 400 by
prose-reference count; 37 prose, 27 remark, 22 proposition, 7 definition, 5
proof. That agreement is independent confirmation the scoping was sound; the
41-block head remains unworked.

**The `proofOf:` note was right about the defect and 6x low on its size.** The
stalled session recorded *"two blocks declare their parent via `proofOf:`, a key
nothing reads"*. Both halves hold, and the field is not the interesting part:

| field | corpus uses | in `ProofSchema`? | read anywhere? |
|---|---|---|---|
| `of` | **10** | no | no |
| `proofOf` | 2 | no | no |
| `proves` | 0 | no | no |

`of` is typed on `ProofBlock` and its docstring calls it *"Canonical field name
— use in preference to `proves`"*, but it is absent from `ProofSchema` and no
consumer reads it: not `content-graph.ts` (whose own header says the editorial
graph comes from `uses[]`), not the MCP server, not `export-json`. `proofOf` is
a variant spelling of an already-dead key. So the defect is **12 blocks**, not
2, and the canonical field named in the schema docs is the dead one.

`proofs[]` on the parent *is* a real validated field, but it is read only by the
MCP server and `export-json` for navigation — never by `content-graph.ts`. It
does not put the edge in the dependency graph, so the stalled note's "absent
from the graph" is correct as stated.

**Landed: 9 of the 10 gaps** (two of the twelve already carried the edge in
`uses[]`). Each read, not inferred from the dead field — two announce the parent
in their own first line, three run under the parent's numbered claim headings
verbatim, one restates the parent's claim as its opening sentence, one matches
the parent's wording, one concludes exactly the parent's statement, one derives
the table the parent asserts. Every added edge points **backward** (d = 1..417),
so none costs a forward reference — the check `fwr9` applied to its own
addition. Cross-check: the two candidates that scored *forward* were exactly the
two the reading had already rejected as wrong parents.

`proofOf:` normalised to the documented `of:`, kept alongside the new `uses[]`
entry. Deleting authored intent because the platform does not read it yet is the
wrong direction; `prn1` is the standing lesson on bulk removal of declarations.

**Not landed.** `prf:q-bessel-c-k-recurrence-cfinite` and
`prf:q-bessel-second-order-qdifference` both point at
`prop:q-beta-c-k-recursion-from-habiro-q-difference` — a parent their own text
never names, that declares no `proofs[]`, and that is marked scaffolding. Their
`of:` may itself be mis-aimed: the "edge is wrong, not the position" case
`fwr7` was about, where one reader is known to get it wrong.

## The second reader: 6 keep, 3 revert

Ran after the fact, briefed to refute and told explicitly that *"when in doubt,
keep"* is not an acceptable tie-break. It overturned three, and **two of the
three expose errors in my reasoning, not differences of judgement**:

- `prf:jackson-q-bessel-contiguity` — I argued it "matches the parent's wording
  of the recurrence." That is an argument for *dropping* the edge. A block that
  restates its parent has shown the reader need not leave it. The block also
  carries no argument at all, deferring to `QBesselContiguityRecurrence.lean`.
- `prf:terminal-resolution` — I argued it "derives the CODATA masses the
  parent's table asserts." Wrong on the facts: it derives only p and n, by a
  route the table does not use, and never touches the deuteron or binding-energy
  rows. See bean `trm1` — the proposition over-claims against its own proof.
- `prf:categorical-archimedean-bridge` — the proof states its own goal
  self-containedly and closes against `ex:q-ext-deriv`; its unmet prerequisites
  are the definitions of `d_q` and the weight decomposition, not the parent.

The six that survived did so on positive evidence of a lean: two point at the
parent without restating it; four are structurally parasitic on it — `α_k` in
`phi-q`, "both characterisations" in `genus-filtration`, the bare Taylor line in
`observation-energy`, and the answer-key headings in `vertex-is-exceptional-divisor`
and `transfer-matrix-level-independence`.

**The standard earned its cost.** A 3-of-9 overturn on a batch I judged the
*weakest* possible editorial claim (restating an edge the author had already
declared in a dead field) says the bar is right where the repo puts it.

**Independence flaw, mine.** I committed the nine before dispatching the reader,
so my rationale was visible in `git log` and the reader said so unprompted. It
read all eighteen `.md` files and diverged from me on two of the three on its
own reasoning, which mitigates but does not erase the leak. Dispatch before the
commit next time.

## Open

1. **The reader's other findings, unfixed** — `prf:quantum-dilogarithm-stratified`
   and `prf:phi-q-categorical-truncation` now declare *only* the parent while
   naming seven or eight other blocks in prose; `prf:terminal-resolution` has a
   raw relative-path link (`../braids-and-knots/...md`) no cross-ref check will
   resolve; `prop:transfer-matrix-level-independence` declares a §3b-cond
   conditional banner without declaring the conjecture in `uses[]` (rule 4
   violation); `prop:jackson-q-bessel-contiguity-recurrence` declares no
   `proofs[]` and its proof is named off-convention.
2. **Upstream fix, `litlfred/folio-assistant`.** Either `of` goes into
   `ProofSchema` and `content-graph.ts` reads it, or the docstring calling it
   canonical stops saying so. Until then every `of:` in the corpus is decoration.
   Not changed cross-repo unasked.
3. **The `fwr10` scoping misses a class.** It selects blocks with an *empty*
   `uses[]`. `prf:genus-filtration-ideal` has a non-empty one and still names
   four lemmas in prose while declaring one — a completeness defect no
   empty-`uses[]` scan can see. The 41-block head should be joined by a
   "declares some, names more" pass.
4. **The 41-block high-signal head is still unworked** — the original `fwr10`
   scope.
