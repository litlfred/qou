# There are two content graphs, and they read different fields

Generated 2026-08-10. Correction to §1 of PR #4921 (bean `fwr11`), found
while working `prn1` tranche 2. Bean: `fwr11`.

PR #4921 §1 argued that the `of:` / `proofOf:` fields are dead, and cited
`content-graph.ts` as the authority for "the editorial graph comes from
`uses[]`". Two things about that citation were wrong. The finding survives
both, but the evidence behind it was not what the PR said it was.

## The two graphs

| | `qa-checkers-extended.ts` | `content-graph-analysis.py` |
|---|---|---|
| location | `folio-assistant/content/pipeline/` | `folio-assistant/content/pipeline/` |
| edge sources | **`uses[]` only** | `uses` + `interprets` + `proofs` + `examples` |
| powers | `detangler-no-forward-ref`, `detangler-no-xchapter-fwd`, `uses-editorial-hygiene`, `detangler-graph-energy` | the H1–H7 editorial heuristics (forward refs, coupling, isolated blocks) |
| authority | `:1491` — *"only the uses array — NOT cites/interprets/own-label"* | `:282–290` |

`content-graph.ts` in `.claude/skills/local/` is neither of these. It is a
**skill descriptor** — an id, a description string, routing patterns, and a
pointer to the script that does the work. Its description ("builds a full
content dependency graph from uses[], interprets, proofs, and examples") is
an accurate description *of the Python script*, but the descriptor itself
reads no content. Citing it as the authority for what the graph reads was a
category error: it is a manifest, not an implementation.

The script it points at, `content/pipeline/content-graph-analysis.py`, is
**not** at that path in this repo — the miga migration moved it to
`folio-assistant/content/pipeline/`. The descriptor's `scripts[].path` was
not updated to match. A path check against this repo alone reports it
missing; it resolves only against the platform clone.

## What this corrects

PR #4921 §1 said of the parent's `proofs[]` field:

> `proofs[]` on the parent *is* validated, but is read only for navigation,
> never by `content-graph.ts` — so it does not put the edge in the graph
> either.

"Never by `content-graph.ts`" is wrong: line 287 appends a `proof` edge for
every entry. Checked against the six proof blocks whose parent edge landed
in that PR — **five of six parents declare `proofs[]` naming the child**
(`observation-energy` is the exception, which declares none).

But the edge it appends runs the other way:

```python
for p in b.proofs:                       # b is the PARENT
    edges.append((b.label, p, "proof"))  # parent -> proof-child
```

The dependency the proof block has *on* its parent — child → parent — is
recorded by neither graph until it is declared in the child's `uses[]`.
So the PR's *substance* stands ("read only for navigation"), and the six
additions still added an edge that was genuinely absent in that direction.
Only the sentence claiming `proofs[]` never reaches the graph was wrong.

## What it does not change

`of:` and `proofOf:` remain dead in both graphs. Neither field appears in
`content-graph-analysis.py`'s extracted set
(`"uses", "interprets", "proofs", "examples"`, line 71) nor in
`qa-checkers-extended.ts`. The 12 blocks that declare a parent through them
declare it to nothing. That was the finding, and it is unaffected.

## Consequence for restoration work

`interprets` **does** produce a child → parent edge in the editorial graph
(line 285). A block that already declares `interprets: "conj:X"` has
therefore already declared that dependency, in the field the schema
provides for it. Copying the same label into `uses[]` to make the
QA-checker graph see it would be duplicating an authorial declaration to
satisfy a checker.

Two such candidates were dropped from `prn1` tranche 2 on these grounds:

| block | already declared via | dropped `uses[]` candidate |
|---|---|---|
| `rem:bsd-surreal-bound` | `interprets: "conj:q-birch-swinnerton-dyer"` | `conj:q-birch-swinnerton-dyer` |
| `rem:rh-surreal-bound` | `interprets: "thm:quantum-gap-collapse"` | `thm:quantum-gap-collapse` |

This asymmetry is worth stating plainly, because it is the kind of thing
that reads as inconsistency: a proof block's `uses[]` → parent **is** added
(the parent's `proofs[]` points the other way, so the dependency is
genuinely unrecorded), while a remark's `uses[]` → interpreted-block is
**not** (the `interprets` field already records it in the right direction).
The rule is the direction of the existing edge, not the existence of one.
