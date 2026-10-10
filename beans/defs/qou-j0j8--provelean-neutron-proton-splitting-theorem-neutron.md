---
# qou-j0j8
title: 'PROVE(lean): neutron_proton_splitting — theorem neutron_proton_splitting [ctx : NeutronProtonSplittingContext] : (ctx.m_n - ctx.m_ [cited faddeev1994,manuscript]'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-faddeev1994
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:09Z
updated_at: 2026-10-04T15:22:40Z
parent: qou-qqyb
---

**File:** `QOU/Torsion/neutron_proton_splitting.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Torsion/neutron_proton_splitting.lean

### `neutron_proton_splitting`  —  line 96  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem neutron_proton_splitting [ctx : NeutronProtonSplittingContext] : (ctx.m_n - ctx.m_p = ctx.α * |ctx.Φ_udd - ctx.Φ_uud|) ∧ (|ctx.m_n - ctx.m_p - codataNeutronProtonSplittingMeV| ≤ 0.01 * codataNeutronProtonSplittingMeV) `
- **Cited:** `[manuscript]`, `[faddeev1994]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/particle-interactions/neutron-proton-splitting.md
  - [faddeev1994] Faddeev, Kashaev (1994), *Current-like variables in massive and massless integrable models* — https://doi.org/10.1007/BF02101594
- **Tractability:** m_n−m_p = α·|Φ_udd−Φ_uud| within 1% of CODATA; compute-backed numeric (Faddeev current variables), not a pure Lean theorem.
- **Next step:** Compute-backed numeric — the value lives in the Hecke/GS engine (witness JSON). Needs that compute formalized in Lean before the goal is provable; not a Mathlib gap.
