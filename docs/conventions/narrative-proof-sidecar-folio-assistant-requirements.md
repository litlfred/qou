# Requirements — `.proof.md` sidecar wiring (for the `litlfred/folio-assistant` agent)

**Audience:** an agent working in the **`litlfred/folio-assistant`** repo
(the platform: schemas, content pipeline, render, QA registry). The
**`litlfred/qou`** repo has already shipped the file convention, the audit
tool, the convention spec, and seed content (PR #2687). This document is
the contract for the platform side. Read alongside
[`narrative-proof-sidecar.md`](narrative-proof-sidecar.md) (the convention)
in the qou repo.

**Goal.** Make a provable content block's narrative proof a first-class,
separately-tracked artifact: a `<root>.proof.md` sibling that is
(a) schema-aware, (b) rendered into the paper, and (c) gated by a QA
criterion — so "does this block have a paper proof?" is answered by file
presence, not prose heuristics.

---

## R1 — Schema + builder

**File:** `folio-assistant/schemas/types.ts`, `…/constraints.ts`,
`…/builders.ts` (and the qou re-exports in `content/schema/` resolve
through these).

1. Add an **optional** field to the provable-block base
   (`theorem` / `lemma` / `proposition` / `corollary`):

   ```ts
   /** Disposition of the narrative proof for this provable block. */
   proof?: "external" | "definitional";
   ```

   - **unset** → a narrative proof is **required**: a non-trivial
     `<root>.proof.md` sibling must exist.
   - **`"external"`** → proof deferred to a cited external/axiomatic
     source; no `.proof.md` expected. (The block's `.md` should carry the
     citation, e.g. `thm:jones-markov-trace` → Jones 1987.)
   - **`"definitional"`** → true by definition/immediate; no proof needed.

2. Do **not** add a `proof` field to non-provable kinds
   (`definition` / `conjecture` / `remark` / `prose` / `example` /
   `simulator` / `equation` / `diagram`). A `conjecture` is unproved by
   construction; a `definition` names a construction. Validation should
   **reject** `proof` on those kinds.

3. The field is **metadata only** — it does not store proof status the way
   `.lean`-derived formalization status is forbidden from `.ts` (AGENTS.md
   §4). Presence/non-triviality of `.proof.md` is the source of truth;
   `proof` only records the *exemption*.

## R2 — File resolution + constraint rules

**File:** `folio-assistant/.../content pipeline` (the resolver that maps a
`.ts` manifest to its `.md` / `.lean` siblings).

1. Resolve `<root>.proof.md` as a recognized sibling of every provable
   block (same root name, `.proof.md` suffix). It must **not** be reported
   as an orphan/unexpected file by any "no stray files" check. (This is
   the immediate CI risk for qou PR #2687 — confirm the validator ignores
   or recognizes `.proof.md` before merge.)

2. New constraint rules (mirror the existing rule style in
   `constraints.ts`):

   | Rule id | Severity | Check |
   |---|---|---|
   | `proof-sidecar-required` | **warning** | provable block, `proof` unset, no non-trivial `<root>.proof.md` ⇒ warn (this is the backlog signal; keep it **warning** until the drain completes, then consider promoting to error) |
   | `proof-sidecar-exempt-no-file` | **info** | `proof: "external"\|"definitional"` **and** a `<root>.proof.md` exists ⇒ info (redundant: either drop the file or drop the exemption) |
   | `proof-field-kind` | **error** | `proof` field present on a non-provable kind |
   | `proof-sidecar-nontrivial` | **warning** | `<root>.proof.md` exists but is empty/stub (< ~20 chars of prose) |

   "Non-trivial" = same test the qou audit uses
   (`audit-narrative-proof-presence.ts::nonTrivial`): collapsed whitespace
   length > 20.

## R3 — Render pipeline

**File:** `folio-assistant/.../render-latex.ts` + block render path.

1. When rendering a provable block, after emitting the statement body
   (from `<root>.md`), if a non-trivial `<root>.proof.md` exists, append
   it **inside a `proof` environment**:

   ```latex
   \begin{proof}
   <rendered .proof.md>
   \end{proof}
   ```

   Use the same markdown→LaTeX conversion + AST validation path as `.md`
   (inline `$…$`, display `$$…$$`, fenced ```tex, cross-refs
   `[text](#label)` → `\hyperref`). The `.proof.md` is authored with the
   identical conventions (AGENTS.md §"Markdown content convention" /
   "TeX authoring patterns").

2. The `proof` environment goes **immediately after** the statement and
   before the next block. Preserve existing numbering/label anchors of the
   statement (the proof shares the statement's label context).

3. `proof: "external"` blocks render no `proof` environment (the citation
   already lives in the statement `.md`). `proof: "definitional"` likewise.

4. Author-notes / draft flags: respect the existing `WITH_AUTHOR_NOTES`
   convention; `.proof.md` is normal published prose (not author notes).

## R4 — QA criterion `proof-narrative-present`

**File:** `folio-assistant/.../qa-criteria-registry.ts §PROOF` +
`qa-checkers-proof*.ts`.

1. Register a **script** criterion `proof-narrative-present` on the
   `proof` axis. `pass` iff:
   - a non-trivial `<root>.proof.md` exists, **or**
   - the manifest sets `proof: "external" | "definitional"`.

   Else `fail`. (It is a *presence* check — orthogonal to the existing
   `proof-narrative-lean-equiv`, which is an *equivalence* check gated on
   `.lean` existing.)

2. Wire it into the per-block `.qa.json` sidecar like the other proof
   criteria (`reviewer.kind: "script"`, `id`, `version`, `script_hash`,
   `script_commit_sha`, hashed `source_hashes` covering `.proof.md`). The
   sidecar's `source_hashes` must include the `.proof.md` hash so staleness
   detection fires when the proof changes.

3. Route `fail` to the proof-authoring backlog so
   `/integration-backlog proof` and `proof-integration-watcher` pick it up
   (add a row to the proof-integration-watcher dispatch table:
   `proof-narrative-present → proof-authoring`).

4. Update `proof-integration-watcher.md` Slot C ("The N proof criteria")
   count and the registry §PROOF docstring.

## R5 — Migration + docs

1. The qou repo will migrate inline proofs into `.proof.md` and drain
   gaps incrementally (PR #2687 follow-ups). Coordinate so the render step
   (R3) lands **before or with** the qou migration that *removes* proofs
   from `.md` — otherwise migrated proofs vanish from the PDF in the
   interim. (Newly-authored gap proofs are additive and safe either order.)

2. Update AGENTS.md §"Content-object architecture" / §"Type system" table
   to list `<root>.proof.md` as a recognized sibling and the `proof` field
   as the exemption marker, citing
   `docs/conventions/narrative-proof-sidecar.md`.

## Acceptance

- [ ] `proof?` field accepted on provable kinds, rejected elsewhere (R1).
- [ ] `.proof.md` resolved as a sibling; no orphan-file failure (R2).
- [ ] 4 constraint rules live with the severities above (R2).
- [ ] `.proof.md` renders inside `\begin{proof}…\end{proof}` after the
      statement; AST-validates (R3).
- [ ] `proof-narrative-present` registered, writes `.qa.json`, routed in
      the watcher (R4).
- [ ] `qa-sweep --axis proof` reports the new criterion across the corpus;
      counts match the qou `audit-narrative-proof-presence.ts` output (R4).
- [ ] AGENTS.md + watcher docs updated (R5).
