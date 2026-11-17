---
# qou-qneo
title: 'GAP: m_s, m_c — (n,T₃) separates s/c; the mass needs the content→hyperbolic-braid map at H₃(q) (4-C)'
status: in-progress
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-09-03T08:31:01Z
updated_at: 2026-10-10T07:15:52Z
parent: qou-8lxd
blocked_by:
    - qou-qpj9
pr: 8229
---

Per-term bean for the strange and charm masses (session qou-ggdk, bean qou-bsu0). Under the observable-vs-rendering reframing (#4602) these are scheme quantities; the honest targets are the charmed/strange hadron observables (m_D, J/ψ, η_c, kaons). Supersedes qou-dnm1 (premise void: no third flavour grade is missing, `orderedContent_injective`); qou-2udt, qou-tdrd, qou-mesont3 are done. Gate: qou-qpj9 (4-C) only — NOT 4-A (PR #5770). Owner convention ruling still owed on the b↔μ / c↔τ pairing (qou-ypl2).

## 🔥 Roast (2026-09-03)

(i) Needs a canonical, parameter-free map from the ordered content (−κ_q̄, +κ_q) to a hyperbolic braid at H₃(q) (Obstruction A, `qou-qpj9`), then ONE joint check on m_D and J/ψ + η_c.
(ii) Excluded: Y-junction 3→2 reduction (B₂ abelian ⇒ Vol = 0; scope-b, `MesonFluxTubeReduction.lean`); any symmetric function of the (n,T₃) multiset (`mass_from_graded_content_cannot_separate`) — but the ordered content is injective, so no grade is missing; charm continuant tower, composite volume, Frobenius block ratio O(1) vs O(100) (scope-a, `charm-*` witnesses); the proton family misses J/ψ at every winding (#4608).
(iii) Trap: picking a braid whose Vol lands 1865 or 3097 MeV (4 % of 196 simple braids sit in the band); "find the missing invariant".
(iv) Next: derive the map. Untried corpus lead: Giambrone Cor 1.1 bounds Vol by the colored-Jones stable coefficient, and the framework computes colored Jones as Markov traces. Not near-term.
(v) Forecast: no derived m_D before the map; the map is a research project.
Tower status [reading: qou-ggdk]: ORDER-ZERO-ONLY — T₃ is a per-crossing sign and the mass would be a leading volume; the colored-Jones-as-Markov-trace lead (J_L(q) = tr_M(ρ(β_L)) over all partitions) is the full-tower formulation, unattempted.

## Implementation Note (PR #8229)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/SkeinResolutionQuarkWritheBalanceWorpitzkyDecupletOrderedContentAndGenerationFilters.lean` and `computations/probes/skein_resolution_quark_writhe_balance_worpitzky_decuplet_ordered_content_and_generation_filters_probe.py` (witness `computations/probes/skein-resolution-quark-writhe-balance-worpitzky-decuplet-ordered-content-and-generation-filters.witness.json`, `f1cdc284e299c69db7b5cdefc55f5ba3d747a9ab`).
