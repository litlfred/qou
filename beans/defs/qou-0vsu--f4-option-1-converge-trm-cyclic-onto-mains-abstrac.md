---
# qou-0vsu
title: 'F4 option-1: converge trM_cyclic onto main''s abstract MarkovStabilization cyclic-trace lemma (no duplicate derivation)'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T03:00:12Z
updated_at: 2026-10-04T15:19:05Z
---


## Scope (option 1 — RECOMMENDED: converge, do not duplicate)
Close F4 `trM_cyclic` (QOU.Machinery.H4, PR #4046) by having it discharged from
the ABSTRACT cyclic-trace lemma that main's algebra framework is heading toward
— NOT by re-deriving cyclicity in the concrete Fin-24 encoding (proven a
value-independent whnf dead-end; audit 2026-07-19-h4-cyclicity-whnf-explosion.md).
Main already has the vehicle:
- `HeckeBraidedCategoryScaffold.MarkovStabilization` (class, general-n, OPEN)
- `HeckeH2AlgebraInstance` / `HeckeH3AlgebraInstance` — NF module as Ring/Algebra
  (mul = mulNF), `HeckeH3AlgebraLaws` (mulNF bilinear+assoc+unit sorry-free)
- `HeckeH4StabilizationRung` — n=4 mulσ/TRM4/trM4 + Hecke/braid/far-commute/
  stabilization/markov_σ₂ (but NO mulNF and NO cyclicity)
My module contributes the concrete n=4 `mulNF` those files lack.

## Non-duplication / anti-laundering guards
- Do NOT re-attempt Fin-24 computation of cyclicity (dead-end, confirmed).
- Do NOT wire a conditional-class instance that assumes cyclicity as a field
  (self-assuming projection = vacuous; §"Axiomatization is NOT a Proof").
- trM_cyclic stays an honest cited sorry until a GENUINE abstract lemma exists.

## Plan of attack
1. Identify the owner/PR of the MarkovStabilization framework (git log/PR search
   on HeckeBraidedCategoryScaffold, HeckeH2/H3AlgebraInstance). Post intent:
   "my H4 mulNF is the concrete n=4 rung; trM_cyclic should be an instance of
   the abstract cyclic-trace lemma; flag naming reconciliation."
2. Reconcile duplication: my `mulσ0/1/2`+`TRM`+`trM`+`mulNF` vs main's
   `mulσ₀/₁/₂`+`TRM4`+`trM4` (HeckeH4StabilizationRung). Either (a) rename mine
   to the subscript-glyph convention and re-express in terms of the shared defs,
   or (b) have my module `import` the rung and reuse its mulσ/TRM4, defining only
   the missing `mulNF` on top. Prefer (b) — dedupes, keeps one operator table.
   Verify with lean-direct (no full build); no Fin-24 grind needed for reuse.
3. Once main's abstract `MarkovStabilization` carries a proved
   `trace_cyclic : trn (a*b) = trn (b*a)` (regular-rep or Ocneanu-induction),
   replace the trM_cyclic sorry with the instance application (H4A : the n=4
   algebra instance — build it if main only did H2A/H3A, mirroring H3A).
4. Update the audit + this bean; drop the sorry only when the instance genuinely
   type-checks (lean-direct exit 0), never via a stub.

## Definition of done
trM_cyclic is either (a) discharged by an abstract instance (sorry gone), or
(b) still a documented sorry BUT the duplication with HeckeH4StabilizationRung is
reconciled and the intent is posted so the upstream lemma lands it. Either is a
clean, non-duplicative state.

## Coordination done (2026-07-19)
No ACTIVE sibling PR is working the abstract MarkovStabilization cyclic-trace
lemma — the framework (HeckeBraidedCategoryScaffold, H2A/H3A) is all merged to
main; the general-n abstract lemma is the OPEN class nobody has a live branch for.
So option-1 coordination = make my contribution discoverable from the canonical
open-item-A home and record the convergence:
- Added a convergence note to docs/audits/2026-07-18-tau-functor-construction-
  reduction.md (F3 general-n section): the n=4 rung now has a sorry-free cyclicity
  REDUCTION (trM_cyclic_of_gram_symm, from option 2 / qou-svnb); the abstract
  MarkovStabilization lemma supplies it generically and discharges gram_symm.
- Noted the MarkovTraceH4 (mulNF+reduction) vs HeckeH4StabilizationRung
  (mulσ/TRM4, no mulNF) duplication — complementary, reconcile when abstract
  lemma lands.
Definition-of-done (b) met: documented residual sorry + duplication noted +
convergence/intent recorded in the canonical doc. Full closure (a) awaits the
abstract lemma (no live owner yet). Bean stays open pending that.



## Reasons for Scrapping

Duplicate of `qou-bhrx` (work-plan reorganisation 2026-10-04). Evidence: both F4 option-1: Ocneanu cyclic-trace lemma on MarkovStabilization; 1 main commits
Content is untouched; only this work item is closed.
