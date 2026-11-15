---
# qou-zko1
title: 'PROVE(lean): skein_mass_from_linking — theorem skein_mass_from_linking [ctx : SkeinMassFromLinkingContext] : ctx.mass = ctx.Q * c [cited manuscript]'
status: todo
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:04Z
updated_at: 2026-10-04T15:22:46Z
parent: qou-aabg
---

**File:** `QOU/BraidsKnots/skein_mass_from_linking.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidsKnots/skein_mass_from_linking.lean

### `skein_mass_from_linking`  —  line 95  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem skein_mass_from_linking [ctx : SkeinMassFromLinkingContext] : ctx.mass = ctx.Q * ctx.mass_Hopf + (Finset.range ctx.n).sum (fun i => ctx.Vol_K i / ctx.hbar_q ^ 2) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
- **Tractability:** Skein mass = Q·mass_Hopf + Σ Vol/ℏ² identity over a context class; repo compute identity.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
