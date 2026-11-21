---
# qou-1aof
title: Cite [hornig-mayer2002] at docs/audits/2026-08-01-em-linking-reads-round1.md
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:09Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-mub3
---

Move the two verified findings out of the references.ts note and into a refid-keyed citation site so they are discoverable by the dependency graph. The audit doc discusses them in prose but never writes the key, so no grep finds them.

**From the source**
- Conclusions, p. 715–716 — 'the antisymmetry of H^(3)(B1,B2,B3) seems to be one of the key problems for a further generalization analogous to helicity' — an independent physics-side confirmation of the antisymmetry obstruction.
  Use here: Corroborates obstruction O1 for the third-order-helicity / EM-linking route; belongs in a durable content or audit artifact, not a bib note.
- Conclusions, p. 709 — 'only expressions quadratic and cubic in magnetic flux' can be obtained; the quadratic slot is occupied by cross-helicity, which vanishes for Brunnian configurations.
  Use here: The scaling trap: a Coulomb-like pair energy needs Flux², which the third-order invariant cannot supply.

Source: `library/arxiv-physics-0203048v1/0203048v1.pdf` (`hornig-mayer2002`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8475, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.


## 2026-11-21 — expo-chapter drain (session https://claude.ai/code/session_01Qmmkt5JeUvGF2FboRQJbLN, issue #8826)

Done on branch `claude/expo-chapter-drain-2026-11-21` (6aed9705a): `[hornig-mayer2002]` written where Round 4 of `docs/audits/2026-08-01-em-linking-reads-round1.md` quotes the antisymmetry sentence. Key resolves to `library/arxiv-physics-0203048v1`. Page locator: the audit says p. 11 (PDF), the bean says pp. 715–716 (journal); both left as written.
