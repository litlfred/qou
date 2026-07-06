# Forward-reference analysis — logical defects vs storytelling

## The distinction that matters

A **forward reference** is a content block in chapter N whose `uses[]`
or `interprets` field points at a block defined in chapter M > N. Not
all are equal:

- A **logical / expository forward reference** asks the reader to
  *rely on* content not yet established — the argument made *here*
  depends on a definition, proposition, or theorem proved *later*.
  This is the genuine defect: the reader cannot follow the exposition
  in order.
- A **storytelling forward reference** merely *mentions*, *motivates*,
  *interprets*, or *points at* later content. A remark that says "this
  foreshadows the mass formula of Chapter 10" imposes no logical
  burden — the reader loses nothing by reading on. Benign and expected
  in a connected work.

The headline detangler metric is the **logical-defect count**, not the
raw forward-ref count.

Authoritative classifier:
[`computations/forward_ref_classifier.py`](../computations/forward_ref_classifier.py)
→ [`forward-ref-classification.witness.json`](../computations/forward-ref-classification.witness.json).

## Current state

```
251 forward references total
   91  LOGICAL DEFECT   ← the real work
    4  logical-waived   (surreal lift + FOUNDATIONAL_LATE — sanctioned)
  124  storytelling     (motivation / interpretation / cite — benign)
   32  structural       (appendix / framing chapter — benign)
```

So **62% of forward refs are benign** (storytelling + structural); the
real actionable set is the **91 logical defects** — edges where a
provable/definitional block builds its argument on a later
provable/definitional block. This is larger than the old "88 actionable"
count *and more precisely scoped*: it excludes the storytelling refs the
old A-category lumped in, and includes definition-consumer (B) and some
remark→provable edges that genuinely impose logical reliance.

## The one sanctioned exception

Logical forward references into **`appendix-surreals`** are permitted.
The surreal-number lift is a deliberate terminal construction: the main
text may rely on it by forward reference because it is the universal
ambient object into which everything embeds. This is the **only**
chapter that earns a blanket logical-forward-ref waiver. Any *new*
exception requires an entry in the `FOUNDATIONAL_LATE` allowlist with
an inline justification, reviewed against the test: "is this object
genuinely used before its formal home *by design*?"

## The 91 logical defects, by chapter-pair

| Count | Source → Target | Diagnosis |
|------:|-----------------|-----------|
| 17 | mass-endomorphism → mass-theory | The Mass-Endomorphism opener (chapter *before* Particles) logically depends on the Mass-Analysis chapter (*after* Particles). The opener *states* the endomorphism; many of its blocks rely on analysis results proved later. Largest cluster — a direct consequence of the opener/analysis split. |
| 11 | particle-interactions → mass-theory | Particle blocks build arguments on mass-analysis propositions proved later. |
| 6 | particle-interactions → climax-volume-mass | Particle blocks rely on q-hyperbolic geometry results. |
| 6 | mass-theory → predicted-spectra | Mass-analysis relies on predicted-spectra propositions. |
| 4 | brings-surface → particle-interactions | Bring's geometry relies on particle definitions. |
| 4 | particle-interactions → predicted-spectra | particle blocks rely on spectra results. |
| 4 | mass-theory → observations | mass-analysis relies on observational propositions. |
| 3 | stochastic-mechanics → q-geometric-langlands | stochastic blocks rely on Langlands results. |
| ~36 | (30 scattered pairs, 1-2 each) | individual cross-chapter logical dependencies |

By source kind: 69 proposition, 19 definition, 2 corollary, 1 theorem.
By target kind: 61 proposition, 25 definition, 3 theorem, 1 proof, 1 corollary.

## Disposition strategy

For each logical defect there are exactly three correct fixes:

1. **Promote the target earlier** — if the target is genuinely
   foundational and used by multiple earlier blocks, move it upstream
   of its earliest consumer.
2. **Demote the edge to storytelling** — if the source doesn't truly
   *rely* on the target but merely references it, change the dependency
   from `uses[]` to an `interprets`/narrative mention (or move the
   reliance into a remark), making it a benign storytelling ref.
3. **Add to FOUNDATIONAL_LATE** — only if the target is, by design, an
   object used early and developed late (rare; each needs justification).

The 17 `mass-endomorphism → mass-theory` cluster is the highest-value
target: the opener/analysis split was a deliberate pedagogical choice
(state the endomorphism before particles, analyze it after), so most of
these are candidates for fix #2 — the opener should *state* the
endomorphism without logically depending on analysis results, with the
dependencies expressed as forward *narrative* pointers rather than
`uses[]` edges. Several opener blocks (`prop:mass-endomorphism`,
`prop:markov-trace-axiomatic-closed-form`, `prop:explicit-central-idempotent`)
carry `uses[]` edges into the analysis chapter that are arguably
backwards — the analysis *consumes* these foundational results, not the
reverse — so the fix is often to invert or drop the edge, not to move a
block.

## The 56-defect floor under current chapter ordering (post-#1435)

PR #1435 took the count **91 → 56** by mechanical disposition: dropped
28 over-declared edges (target absent from source's prose AND Lean,
no orphans), relabeled 2 conjectures mislabeled `prop:` (§3b
hygiene), and documented 17 irreducible foundational edges where
option-(b) "promote target to earlier chapter" was BLOCKED for each
(every target carried its own ≥1 same-chapter dependency, so a
promote would just relocate the forward edge).

The remaining **56 defects** are a structural floor under current
chapter ordering:

- The most-cited target (`prop:flavor-split-substrate` in
  observations) appears in only 3 edges; the rest of the distribution
  is a long tail of 1-2x cross-chapter dependencies. There is no
  high-fanout target that would justify a single FOUNDATIONAL_LATE
  allowlist entry to clear a large batch.
- Each remaining defect is a real cross-chapter logical reliance:
  the source chapter genuinely depends on a definition or proposition
  established in a later chapter, and that target's own dependency
  cone keeps it pinned to its current chapter.

**Further reduction requires editorial-not-mechanical decisions**:

- Restructure a chapter's position in the manifest (deliberate
  pedagogical re-ordering — owner's call).
- Split a target block to extract a foundational piece into an
  earlier chapter (real content surgery, not a `uses[]` edit).
- Promote individual targets to `FOUNDATIONAL_LATE` with explicit
  per-target rationale (the existing 5-entry allowlist is for objects
  the author deliberately uses early and develops late; adding to it
  should be a curated decision, not a mass sweep).

The mechanical-cleanup ceiling for the forward-ref severity model is
**56 logical defects** until the chapter ordering itself is revisited
or the `FOUNDATIONAL_LATE` allowlist is curated further. Future PRs
that touch the count should declare which lever they're using
(restructure / split / allowlist) so reviewers can assess the
editorial implication.

## CI integration

The classifier runs in the witness pipeline (warn-only) and emits the
witness above. The gate is the **logical-defect count** — it must not
regress. Storytelling and structural counts are reported but not gated.
