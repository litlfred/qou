
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
