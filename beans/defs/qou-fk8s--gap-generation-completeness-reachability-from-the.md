---
# qou-fk8s
title: 'GAP: generation completeness — reachability from the generator set rests on GenerationScheme.unknotting_realised (the unknotting-number axiom); no knot type is constructed in Lean'
status: in-progress
pr: 8183
type: task
priority: normal
tags:
    - lean
    - gap
    - reorg-2026-10-04
    - 8f-gen
    - 8f-open
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-10-10T12:24:00Z
parent: qou-8lxd
---

Class B (modelling) gap (SM-surface Lean sweep, bean qou-08zf, 2026-09-03). brings-surface/generation-completeness.lean previously proved nothing: isReachable held for every K (audit docs/audits/2026-08-30-generation-completeness-is-vacuous.md, bean qou-0avp). It now defines ReachableIn (exact-step reachability over a move relation) and GenerationScheme, whose field unknotting_realised : ∀ k, ReachableIn crossingChange (unknottingNumber k) unknot k is the defining property of the unknotting number (Kauffman). generation_completeness composes that field with unknot ∈ 𝒢.

OPEN: the Lean has no knot type, no actual Skein crossing-change relation and no Seifert genus — GenerationScheme is a model whose content field is the axiom. The corollary about V_phys = colim V^⊗n (spectrum completeness) has no formal carrier and was removed rather than restated vacuously.

NEXT HONEST STEP: instantiate GenerationScheme on an actual knot model (braid words modulo Markov moves with a crossing-change relation on words), prove unknotting_realised there from the definition of the unknotting number, and state the genus filter as a real predicate on that model.

## Progress Update (Round 54 — PR #8183)
- [x] Formalized non-vacuous Lean 4 theorems (`0` `sorry`, `0` vacuity candidates across all 4 static audits) in `folio/quantum-observable-universe/lean/QOU/Eightfold/CoCasimirFigureEightAndGenerationCompleteness.lean` and wired into `QOU.lean`.
- [x] Added 50-dps `mpmath` probe `computations/probes/co_casimir_figure_eight_and_generation_completeness_probe.py` and 2-commit stamped witness `computations/probes/co-casimir-figure-eight-and-generation-completeness.witness.json` (`scriptCommitSha: 0a9a3d4c2110ac1fe5749fd28e2cb610a48c9e50`, `HEAD: 531c8d4812e2909b18a4bc18eeba6be23a873d7f`).
- [x] Opened `litlfred/qou#8183` (status kept at `in-progress` per no-unilateral-closure policy).
