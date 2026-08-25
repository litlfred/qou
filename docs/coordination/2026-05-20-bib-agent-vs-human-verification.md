# Coordination — bib `verified_by` agent-vs-human structure

**Goal slug:** `bib-agent-vs-human-verification`
**Opened:** 2026-05-20
**Owner branch:** `claude/pdf-build-split-O0pTu` (per-chapter PDF outputs +
README regeneration + authors-note Lean coverage stats)
**Coordinating with:** PR #820 `claude/detangler-bib-followup-batch-2026-05-19`
(45-commit bib-verification + intake-infrastructure tranche)

## Scope map

| PR / branch | Domain | Overlap with this ledger |
|---|---|---|
| **THIS — `claude/pdf-build-split-O0pTu`** | PDF post-processing (per-chapter PDFs split from `main.pdf`), README regeneration on `main` publish, authors-note refresh with live Lean coverage stats (385/567 sorry-free, 121/132 class-axiomatised conjectures) | None on bib content. Authors-note explicitly retains the "we used large language models" disclaimer; no claims about agent-verified citations. |
| **#820 — `claude/detangler-bib-followup-batch-2026-05-19`** | `content/bib-qa-verifications.json` (typed per-paper verification sidecar), `validate-bib.ts` (5 audit modes), `upload-bib-papers.sh`, 654 `-- Ref:` upgrades, `bib-qa.ts` two new tags (`has_local_pdf`, `verification_status`) | This ledger documents a question about the `verified_by` field's shape — not a request to block the PR. |

## The question

PR #820's `content/bib-qa-verifications.json` records, per reference id:

```json
{
  "id": "boyd-vandenberghe-2004",
  "status": "fixed",
  "local_pdf": "library/boyd-vandenberghe-2004-convex-optimization.pdf",
  "verified_at": "2026-05-19T06:38:00Z",
  "verified_by": "Claude (claude-opus-4-7)",
  "fixes_applied": 18,
  "fix_commit": "(this commit)",
  "note": "..."
}
```

The `verified_by` field is **free-text**, and every entry currently in the
117-entry roster reads either `Claude (claude-opus-4-7)` or
`Claude (claude-sonnet-4-6)`. The author has not personally verified any
entry yet; every "verified-clean" / "fixed" / "partial" tag is an
**agent claim** awaiting human adjudication. The schema does not record
this distinction.

For honest reporting to readers (and per the AGENTS.md "Every proof in
this paper..." authors-note now refreshed to "385 of 567 provable claims
carry full Lean proofs; **human adjudication of every line is not
complete**"), the bib QA structure should make agent-only verifications
visible as such rather than equating them with human review.

## Proposed schema refinement (follow-up — not a #820 blocker)

Replace the free-text `verified_by` with a discriminated shape:

```ts
type Verifier =
  | { kind: "agent"; agent: string; model: string; assistance?: never }
  | { kind: "human"; human: string;
      agent_assistance?: { agent: string; model: string } };

interface VerificationEntry {
  id: string;
  status:
    | "verified-clean" | "partial" | "fixed"
    | "uncited" | "paper-mismatch" | "unfetchable"
    | "pending-placement";
  verified_by: Verifier;
  // adjudication may be set independently of verified_by:
  human_adjudicated?: { who: string; at: string; note?: string };
  ...
}
```

Effects:

1. **`bib-qa.ts` rendering** — distinguish "Verified by agent (awaiting
   human review)" from "Verified by human" in the QA dashboard so the
   adjudication state is visible at a glance.
2. **`validate-bib --strict`** — refuse to count an agent-only
   verification as "clean" for any audit that claims human review.
3. **`paper-mismatch` and `uncited` decisions** — must require
   `human_adjudicated` since they trigger reference removal / metadata
   rewrite.

## Suggested split

| Item | Owner | Branch |
|---|---|---|
| Land #820 as-is (free-text `verified_by`) | @litlfred via #820 | `claude/detangler-bib-followup-batch-2026-05-19` |
| Schema refinement (`Verifier` discriminated union + `human_adjudicated`) | follow-up branch | TBD — propose `claude/bib-verifier-discriminated-union` |
| Backfill `verified_by` of all 117 existing entries to the new shape | same follow-up | (migration script — purely a shape change; values stay accurate) |

**Reason for splitting:** #820 already ships 45 commits / 6 798 additions
across 276 files and is in review. A schema refinement would invalidate
every entry in `bib-qa-verifications.json` and require migration tooling;
better to land #820's audit-trail first and refactor the schema in a
focused follow-up.

## Asks

1. **For PR #820 (Frederick / reviewer):** confirm whether the
   discriminated-union refinement should be queued as a follow-up, or
   deferred indefinitely (free-text is workable if all entries are
   uniform).
2. **For PR #820 (no merge ask):** consider adding a one-line note in
   `bib-qa-verifications.json`'s `_schema` description that
   `verified_by` is currently **agent-only**, so downstream tools and
   readers don't mistake agent claims for human adjudication.

## Cross-references

- This branch's authors-note refresh:
  [`authors-note.md@claude/pdf-build-split-O0pTu`](https://github.com/litlfred/qou/blob/claude/pdf-build-split-O0pTu/content/quantum-observable-universe/introduction/authors-note.md)
- This branch's coverage tooling:
  [`scripts/lean-coverage.ts`](https://github.com/litlfred/qou/blob/claude/pdf-build-split-O0pTu/scripts/lean-coverage.ts)
- PR #820's verification sidecar:
  [`content/bib-qa-verifications.json@claude/detangler-bib-followup-batch-2026-05-19`](https://github.com/litlfred/qou/blob/claude/detangler-bib-followup-batch-2026-05-19/content/bib-qa-verifications.json)
- PR #820's audit script:
  [`content/pipeline/validate-bib.ts@claude/detangler-bib-followup-batch-2026-05-19`](https://github.com/litlfred/qou/blob/claude/detangler-bib-followup-batch-2026-05-19/content/pipeline/validate-bib.ts)
