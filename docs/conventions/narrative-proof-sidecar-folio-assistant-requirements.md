# Requirements — `proof-narrative-present` QA criterion (for the `litlfred/folio-assistant` agent)

**Audience:** an agent in the **`litlfred/folio-assistant`** repo (schemas,
content pipeline, render, QA registry).

**Context correction (2026-06-24).** The narrative-proof mechanism the
qou author asked for — a separate `.md` proof, part of the content block —
**already exists** as the `proof` block kind (`<name>-proof.ts` +
`<name>-proof.md`, parent `proofs: [...]`, chapter-manifest entry; ~170 in
use, rendered into the PDF). So the schema, resolver, and render work are
**already done**. The only genuinely-new platform work is a QA criterion
that makes proof-block *presence* trackable in the `.qa.json` sidecars,
plus a small optional schema marker for deliberate exemptions.

See [`narrative-proof-sidecar.md`](narrative-proof-sidecar.md) (qou) for
the mechanism.

---

## R1 — `proof-narrative-present` QA criterion (the main ask)

**File:** `qa-criteria-registry.ts §PROOF` + a `qa-checkers-proof*.ts`.

1. Register a **script** criterion `proof-narrative-present` on the
   `proof` axis, evaluated for every provable block
   (`theorem`/`lemma`/`proposition`/`corollary`). `pass` iff **either**:
   - the block has a linked, non-trivial `proof` block — detected from the
     parent's `proofs: [...]` field referencing a `prf:` block whose
     `.md` is non-trivial, **or** from a `proof` block whose `uses: [...]`
     names the parent label; **or**
   - the block is marked exempt via the R2 manifest field.

   Else `fail`. (This is a *presence* check — orthogonal to the existing
   `proof-narrative-lean-equiv` *equivalence* check, which is gated on
   `.lean` existing.)

   Reference implementation of the detection logic:
   `litlfred/qou` → `content/pipeline/audit-narrative-proof-presence.ts`
   (`prfOk` / `provesParent` two-pass). "Non-trivial" = collapsed
   whitespace length > 20.

2. Write the result into each provable block's `.qa.json` like the other
   proof criteria (`reviewer.kind: "script"`, `id`, `version`,
   `script_hash`, `script_commit_sha`). The sidecar `source_hashes` for
   this criterion must cover the linked `<name>-proof.md` so staleness
   fires when the proof text changes.

3. Route `fail` to the proof-authoring backlog and add a row to the
   `proof-integration-watcher.md` Slot C dispatch table:
   `proof-narrative-present → proof-authoring`. Bump the registry §PROOF
   criterion count + docstring.

## R2 — optional exemption marker (small schema add)

**File:** `schemas/types.ts`, `constraints.ts`, `builders.ts`.

1. Add an **optional** field to the provable-block base:

   ```ts
   /** Why this provable block has no internal proof block. */
   proof?: "external" | "definitional";
   ```

   - **unset** → a proof block is required (else `proof-narrative-present`
     fails — the backlog signal).
   - **`"external"`** → proof deferred to a cited external/axiomatic
     source (e.g. `thm:jones-markov-trace`); no proof block expected.
   - **`"definitional"`** → immediate/by-definition; no proof block.

2. Reject `proof` on non-provable kinds (`definition` / `conjecture` /
   `remark` / `prose` / `example` / `simulator` / `equation` / `diagram`)
   — constraint rule `proof-field-kind` (**error**). A `conjecture` is
   unproved by construction; a `definition` names a construction.

3. `proof-narrative-present` (R1) treats either marker as `pass`.

## R3 — docs

Update AGENTS.md §"Content-object architecture" / §"Type system" to note
that a provable block's proof lives in a linked `proof` block
(`<name>-proof.{ts,md}`, parent `proofs`), and the `proof?` exemption
marker, citing `docs/conventions/narrative-proof-sidecar.md`.

## Acceptance

- [ ] `proof-narrative-present` registered on the `proof` axis; writes
      `.qa.json`; routed in the watcher (R1).
- [ ] `qa-sweep --axis proof` corpus counts match the qou
      `audit-narrative-proof-presence.ts` output (currently 167 pass /
      492 fail) (R1).
- [ ] `proof?` field accepted on provable kinds, rejected elsewhere; both
      values count as `pass` (R2).
- [ ] AGENTS.md + watcher docs updated (R3).

## Non-requirements (already implemented — do not redo)

- The `proof` block kind, the `proofs: [...]` parent field, sibling
  resolution of `<name>-proof.{ts,md}`, and rendering the proof `.md`
  into a proof environment after the statement. All in use today.
