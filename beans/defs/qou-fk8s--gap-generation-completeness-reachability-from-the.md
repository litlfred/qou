---
# qou-fk8s
title: 'GAP: generation completeness — reachability from the generator set rests on GenerationScheme.unknotting_realised (the unknotting-number axiom); no knot type is constructed in Lean'
status: todo
type: task
priority: normal
tags:
    - lean
    - gap
    - reorg-2026-10-04
    - 8f-gen
created_at: 2026-09-03T09:08:30Z
updated_at: 2026-10-10T07:16:04Z
parent: qou-8lxd
---

Class B (modelling) gap (SM-surface Lean sweep, bean qou-08zf, 2026-09-03). brings-surface/generation-completeness.lean previously proved nothing: isReachable held for every K (audit docs/audits/2026-08-30-generation-completeness-is-vacuous.md, bean qou-0avp). It now defines ReachableIn (exact-step reachability over a move relation) and GenerationScheme, whose field unknotting_realised : ∀ k, ReachableIn crossingChange (unknottingNumber k) unknot k is the defining property of the unknotting number (Kauffman). generation_completeness composes that field with unknot ∈ 𝒢.

OPEN: the Lean has no knot type, no actual Skein crossing-change relation and no Seifert genus — GenerationScheme is a model whose content field is the axiom. The corollary about V_phys = colim V^⊗n (spectrum completeness) has no formal carrier and was removed rather than restated vacuously.

NEXT HONEST STEP: instantiate GenerationScheme on an actual knot model (braid words modulo Markov moves with a crossing-change relation on words), prove unknotting_realised there from the definition of the unknotting number, and state the genus filter as a real predicate on that model.
