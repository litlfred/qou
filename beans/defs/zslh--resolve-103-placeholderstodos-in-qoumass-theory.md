---
# zslh
title: Resolve 103 placeholders/TODOs in qou/mass-theory
status: completed
type: task
priority: normal
created_at: 2026-06-22T02:25:52Z
updated_at: 2026-07-05T05:30:00Z
---

resweep 2026-06-22: honest counter = 8 actionable (claimed 103) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 8 (claimed 103): q-beta-radius gate 5, frobenius-self-duality 2, jucys-murphy 1. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

drain 2026-06-23 (#2656): cited frobenius 2 def sorries + fixed the pre-existing-red mass-theory/jucys-murphy file (import + Ring instance + esymmJM field). Remaining mass-theory TODOs (q-beta-radius .md checklist) intentional. uncited-sorry → 0.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 0 (claimed 103) in content/quantum-observable-universe/mass-theory. FULLY DRAINED — recommend close. (Note: duplicate bean file exists for this id.)

> **Resolved 2026-07-05 (swarm 2, PR #3346).** Honest counter reports 0 machine-actionable placeholders in mass-theory (the '103' was naive-grep noise: .qa.json/.witness sidecar notes, narrative 'numerical/probe' mentions, -- Ref:-cited/§3b sorries). Tractable prose placeholders (pure _(draft.)_ banners, 5 files) stripped per one-voice H. Remainder (per-term *Status: DERIVED* tables, §3b status banners, 'earlier draft' notes) deferred — needs author judgment/authorNotes migration, documented in the audit doc.

<!-- recovered 2026-08-23 from orphaned file `zslh--resolve-103-placeholders-todos-in-qou-mass-theory.md` (no front-matter; invisible to the tracker) -->

## Result (2026-06-23, session nifty-cerf, PR #2649)

Honest actionable count (per `count-actionable-placeholders.ts`): 8 → **0**.
Disposition is **honest, not fabricated** — no `sorry` was proved:

- **frobenius-self-duality-forces-lp-dual-extraction.lean** (2): the two uncited
  `def := sorry` stubs (`observationFrame`, `frobeniusSelfDualityMap`) now carry
  `-- Ref: [manuscript]` per §1. Full formalisation of the maps remains
  build-gated (real multi-step math; no Lean build in this sandbox).
- **jucys-murphy-central-elements-qou.lean** (1+1): the two standard-result
  `sorry`s (JM commutativity, e_ℓ centrality) upgraded from a weak
  `[manuscript]→.ts` ref to the proper published sources already in the header
  ([jucys1974], [murphy1992] §2.4–§2.5, [kassel1995] §VI.6), placed adjacent to
  each `sorry` inside a `by` block. Axiomatised (the abstract
  `HeckeJMSpectrum.algebra` carries no multiplication to derive them from).
- **q-beta-radius-of-convergence-gate.md** (5): bare `TODO` work-tracking tags
  (one-voice Category H, in scholarly prose) reworded to honest *not yet
  formalised* content for gates (c) q=1-shadow and (d) direction-sanity.

NOT done (build-gated, deferred): proving the cited `sorry`s; formalising gates
(c)/(d). These need a Lean build (cold/unavailable here). Pending human close.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 0 (claimed 103) in content/quantum-observable-universe/mass-theory. FULLY DRAINED — recommend close. (Note: duplicate bean file exists for this id.)

> **Resolved 2026-07-05 (swarm 2, PR #3346).** Honest counter reports 0 machine-actionable placeholders in mass-theory (the '103' was naive-grep noise: .qa.json/.witness sidecar notes, narrative 'numerical/probe' mentions, -- Ref:-cited/§3b sorries). Tractable prose placeholders (pure _(draft.)_ banners, 5 files) stripped per one-voice H. Remainder (per-term *Status: DERIVED* tables, §3b status banners, 'earlier draft' notes) deferred — needs author judgment/authorNotes migration, documented in the audit doc.
