---
# qou-k6a4
title: Cite 0206161v1.pdf at content/quantum-observable-universe/bring_tetraplectic.md
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:01Z
updated_at: 2026-08-24T18:59:49Z
---

bring_tetraplectic.md Sect. 3 attributes the Young-tableaux fixed-point classification to Nekrasov by name without a citation.

**From the source**
- Sects. 3.5-3.6 — The fixed points of the maximal-torus action on the (compactified) instanton moduli space are labelled by N-tuples of Young diagrams with k boxes in total, and the localisation integral reduces to a residue sum over them.
  Use here: Supplies the source for the uncited 'Nekrasov localization / Young tableaux' attribution that motivates the S_5-partition fibre decomposition in bring_tetraplectic.md Sect. 3 and the N = 5 choice in the cyclotomic fibre-reduction probe.

Source: `library/arxiv-hep-th-0206161v1/0206161v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-hep-th-0206161v1/  ->  [nekrasov2002]
  SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [nekrasov2002] as the citation key when you do it.

## CLOSED 2026-08-24 — cited, at the block the material became

The citation site named in the title no longer exists: `bring_tetraplectic.md`
was incorporated into `brings-surface/` (bean `qou-wy6d`, owner ruling). Its
Sect. 3 — the Nekrasov attribution this bean is about — is now
`conj:tetraplectic-sw-localisation-bridge`, which cites `[nekrasov2002]` in both
`cites[]` and the prose, exactly as the 2026-08-21 line instructed. The block
also states what the citation is *for*: the fixed points of the torus action on
instanton moduli are labelled by tuples of Young diagrams, which is the
localization index the conjecture would have to identify with the `S_5` index.

The ledger row in `content/bib-qa-verifications.json` still names the old path.
That is left alone on purpose — it records what paper-relevance-triage saw on
2026-08-08, nothing reads the `target` field, and editing a past verification
would falsify the record.
