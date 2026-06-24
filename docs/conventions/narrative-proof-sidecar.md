# Convention: narrative proofs live in a `.proof.md` sidecar

**Status:** adopted 2026-06-24 (author directive). qou-side tooling +
file convention land first; the render/validation wiring is a
`litlfred/folio-assistant` follow-up (see §Rollout).

## Why

A provable content block (`theorem` / `lemma` / `proposition` /
`corollary`) is a file group sharing a root name:

```
<root>.ts      manifest (kind, label, lean.ref, uses, …)
<root>.md      narrative — the STATEMENT (+ motivation / interpretation)
<root>.lean    formalization (when required)
```

Historically the *narrative proof* was folded into `<root>.md` as inline
prose (or omitted entirely, with the only proof living in `<root>.lean`).
That made "does this block have a paper proof?" un-trackable: it required
prose heuristics, and ~50 % of provable blocks had no narrative proof at
all (audit: `docs/audits/2026-06-24-narrative-proof-presence-audit.md`).

## The convention

The narrative proof gets its **own sibling file**, part of the content
block:

```
<root>.proof.md    narrative PROOF (markdown + TeX, same conventions as .md)
```

- **`<root>.md`** holds the statement and any motivation/interpretation.
- **`<root>.proof.md`** holds the proof the human reader follows.
- **Presence is the signal.** "Has a narrative proof" ⇔ a non-trivial
  `<root>.proof.md` exists. No prose heuristics, no Lean parsing — a
  file-existence check, trivially auditable and CI-gateable.

### Deliberate exemptions

Some provable blocks intentionally have no internal proof — they cite an
external/axiomatic result (e.g. `thm:jones-markov-trace`, proved in
Jones 1987). Mark these in the manifest rather than leaving an empty
sidecar:

```ts
export default theorem({
  label: "thm:jones-markov-trace",
  proof: "external",          // ← deliberate: no .proof.md expected
  // …
});
```

`proof` field values:

| value         | meaning                                                        | `.proof.md` expected |
|---------------|----------------------------------------------------------------|----------------------|
| *(unset)*     | a narrative proof is required                                  | **yes**              |
| `"external"`  | proof deferred to a cited external/axiomatic source            | no                   |
| `"definitional"` | the statement is true by definition / immediate; no proof needed | no                |

## Authoring rules

1. A new provable block ships with `<root>.proof.md` **or** an explicit
   `proof: "external" | "definitional"` in the manifest. A provable block
   with neither is a gap (flagged by the audit).
2. `.proof.md` follows the same markdown/TeX conventions as `.md`
   (inline `$…$`, display `$$…$$`, fenced ```tex blocks; see AGENTS.md
   §"Markdown content convention").
3. Open the proof with a bold **Proof.** lead and close it with `∎`.
4. When a Lean proof exists, the `.proof.md` should be a faithful
   human-readable account of the *same* argument (the
   `proof-narrative-lean-equiv` QA criterion adjudicates drift).

## Tooling

- **Audit:** `bun run content/pipeline/audit-narrative-proof-presence.ts`
  reports, per chapter: blocks with a `.proof.md` sidecar (target),
  blocks with only an inline proof (to migrate), external/definitional
  exemptions, and remaining gaps.
- **Proposed QA criterion** `proof-narrative-present` (folio-assistant
  `qa-criteria-registry.ts §PROOF`): `pass` iff `.proof.md` exists and is
  non-trivial, or the manifest marks the block exempt. Routes failures to
  the proof-authoring backlog the same way the Lean criteria route to
  Lean skills.

## Rollout

1. **(this PR, qou)** file convention + audit tooling + this doc. ✔
2. **(folio-assistant)** add the optional `proof?: "external" |
   "definitional"` field to the provable-block schema/builders; teach the
   render pipeline to append `<root>.proof.md` after the statement inside
   a `proof` environment; register the `proof-narrative-present` QA
   criterion. *Until this lands, `.proof.md` files are authored and
   tracked but not yet rendered into the PDF — additive, no regression.*
3. **(qou, ongoing)** migrate inline proofs out of `.md` into `.proof.md`
   (do this only after step 2, so the render does not drop the proof),
   and drain the ~331 genuine gaps chapter by chapter.
