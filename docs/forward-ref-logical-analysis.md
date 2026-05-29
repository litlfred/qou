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
[`folio-assistant/computations/forward_ref_classifier.py`](../folio-assistant/computations/forward_ref_classifier.py)
→ [`forward-ref-classification.witness.json`](../folio-assistant/computations/forward-ref-classification.witness.json).

## Current state

```
251 forward references total
   38  LOGICAL DEFECT   ← the real work
    4  logical-waived   (surreal lift + FOUNDATIONAL_LATE — sanctioned)
  179  storytelling     (motivation / interpretation / cite — benign)
   34  structural       (appendix / framing chapter — benign)
```

So **85% of forward refs are benign**; the actionable set is 38, not 88.

## The one sanctioned exception

Logical forward references into **`appendix-surreals`** are permitted.
The surreal-number lift is a deliberate terminal construction: the main
text may rely on it by forward reference because it is the universal
ambient object into which everything embeds. This is the **only**
chapter that earns a blanket logical-forward-ref waiver. Any *new*
exception requires an entry in the `FOUNDATIONAL_LATE` allowlist with
an inline justification, reviewed against the test: "is this object
genuinely used before its formal home *by design*?"

## The 38 logical defects, by chapter-pair

| Count | Source → Target | Diagnosis |
|------:|-----------------|-----------|
| 12 | mass-endomorphism → mass-theory | The Mass-Endomorphism opener (Ch before Particles) logically depends on the Mass-Analysis chapter (Ch after Particles). The opener *states* the endomorphism; some of its blocks rely on analysis results. Largest cluster — created by the opener/analysis split. |
| 8 | particle-interactions → mass-theory | Particle blocks build arguments on mass-analysis propositions proved later. |
| 3 | climax-volume-mass → mass-theory | q-Hyperbolic geometry blocks rely on mass propositions. |
| 2 | braids-and-knots → mass-theory | early algebra relies on mass results. |
| 2 | brings-surface → mass-theory | Bring's geometry relies on mass-identity / Wedderburn. |
| 1 each | (13 scattered pairs) | individual cross-chapter logical dependencies |

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

The 12 `mass-endomorphism → mass-theory` cluster is the highest-value
target: the opener/analysis split was a deliberate pedagogical choice
(state the endomorphism before particles, analyze it after), so most of
these are candidates for fix #2 — the opener should *state* the
endomorphism without logically depending on analysis results, with the
dependencies expressed as forward *narrative* pointers rather than
`uses[]` edges.

## CI integration

The classifier runs in the witness pipeline (warn-only) and emits the
witness above. The gate is the **logical-defect count** — it must not
regress. Storytelling and structural counts are reported but not gated.
