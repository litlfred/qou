# Design: human-validated bibliography workflow (issue-driven physical review + photo ingestion)

**Date:** 2026-06-08 · **Requested by:** owner · **Status:** design + phased build
plan (faithful capture of the owner's spec). Supersedes "work the ingestion
backlog" (queue item 5) with a *human-review-gated* bib pipeline.

## Goal

Every reference in `content/schema/references.ts` must be **human-reviewed against
its source**. Track that status; for refs not yet human-validated, drive
acquisition + review through **GitHub issues** carrying full QOU context, ending
in the author uploading a **photo of the relevant page(s)**, which then triggers
**automated formalisation + source-match ingestion**.

## 1. Human-review status (audit)

- **New audit check** (extend `validate-references` / a new `bib-human-review`
  criterion): for each reference, has a human reviewed it against the source?
  Status: `unreviewed | source-in-repo | issue-open | photo-uploaded | validated`.
- **Where stored:** a bib sidecar — e.g. `content/schema/references.review.json`
  (or per-ref `humanReviewed?: { by, date, source, page? }` field, render-skipped),
  hashed against the `references.ts` entry so it goes stale if the entry changes.
- The audit **flags every `unreviewed` ref** and every ref whose cited QOU result
  has no human-validated source.

## 2. Acquisition ladder (per unvalidated ref)

1. **Source already in `library/`** → agent identifies the relevant
   page(s)/passage (no human photo needed) → ingest (§4).
2. **Not in repo** → acquire legally for `library/` (open-access/arXiv/author
   copy), with author assistance if needed.
3. **Paywalled / not digitally available** → open a **physical-review issue**
   (§3); author photographs the page(s) at a library.

## 3. GitHub issue per ref needing physical review

One issue per non-human-validated ref needing physical acquisition. **Assigned to
`@litlfred`.** Contents (as much bibliographic data as possible, *consistently
readable*):

- **Bibliographic block:** title, authors, year, journal/volume/pages, DOI, ISBN,
  **library call number**, holding library if known.
- **QOU context:** the citing content block(s) (`.md` narrative + label), any Lean
  `-- Ref:` stub sites, the `\cite{}`/`uses[]` sites, with **blob links**.
- **What to verify:** the specific theorem/section/equation the QOU result relies
  on (so the photo targets the right page).
- **Labels:** `bib-physical-review`, `needs-photo`, plus the chapter/domain tag.
- **Action requested:** author uploads a **photo of the relevant page(s)**.

Issue template lives in `.github/ISSUE_TEMPLATE/bib-physical-review.md`; created
programmatically by the `bib-human-review` skill (one per flagged ref).

## 4. On photo upload → automated ingestion (new integration-watcher)

**New integration-watcher skill** (`bib-photo-ingestion-watcher`): subscribes to
the bib-physical-review issues. **When a photo is attached:**

1. OCR/read the page; extract the cited statement.
2. Run the **proof-authoring / ingester skills** (`paper-importer`,
   `formalizer`): formalise the cited result in **Lean** (per-paper package /
   wrapper-for-overlap, per the ingestion backlog) and **ensure the QOU usage
   matches the source** (statement-match check).
3. Begin **machine + agent bib validation**: DOI/metadata cross-check, citation
   consistency (`validate-references`), `-- Ref:` resolution.
4. On success → set the ref's review status to `validated`, record
   `humanReviewed: { by, date, source: <issue#>, page }`, refresh the bib sidecar,
   and post the result back on the issue.

## 5. Existing `library/` — same pipeline, agent-sourced

The 19+ files already in `library/` follow the **same ingest workflow**, but with
**agent-identified relevant passages** instead of human photocopies. After
identification, the **post-ingestion process is identical** (§4 steps 1–4):
formalise, source-match, validate, set status, refresh sidecar. (This subsumes the
[uploaded-paper ingestion backlog](2026-06-08-uploaded-paper-results-ingestion-backlog.md).)

## 6. Sidecar changes

- `references.review.json` (new): per-ref human-review + ingestion status, hashed
  to the `references.ts` entry.
- Extend `validate-references` output to a sidecar consumable by the audit/CI.
- `library/intake.json` gains per-file ingestion status (identified passage,
  formalised?, matched?).

## 7. Skills to add / update

| Skill | Change |
|---|---|
| **`bib-human-review`** (new) | flag unreviewed refs; build the issue (context + biblio + photo request); assign `@litlfred`; drive the acquisition ladder |
| **`bib-photo-ingestion-watcher`** (new integration-watcher) | on photo upload → OCR → formalise (Lean) + source-match + bib-validate → set status + sidecar |
| `local/paper-importer` | results-ingestion + per-paper Lean placement / wrapper (shared with the ingestion backlog) |
| `local/document-intake` | track per-upload ingestion status in `intake.json` |
| `local/validate-references` (pipeline) | add the `human-reviewed?` criterion + sidecar output; CI gate (warn → strict) |
| `local/coordinate` / `integration-watcher` | new "bib human-review" axis: every ref validated or issue-open |

## Phased build plan

1. **Status + audit** — add the `humanReviewed` status model + the
   `validate-references` check + `references.review.json` sidecar (baseline: all
   `unreviewed`).
2. **Issue template + `bib-human-review` skill** — generate one issue per flagged
   ref with full context, assign `@litlfred`.
3. **`bib-photo-ingestion-watcher`** — the on-photo automation (OCR → formalise →
   match → validate).
4. **Backfill** — run the agent-sourced path (§5) over existing `library/`.

**Note:** start with phase 1 (the status model + audit) — it is the gate
everything else hangs on, and it is buildable now (schema + pipeline check +
sidecar), no external dependencies. Phases 2–4 add the issue/photo/automation
layers incrementally.
