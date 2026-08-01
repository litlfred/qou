---
# qou-apcl
title: 'PROVE(lean): ConfinementSDP — theorem ConfinementSDP (n : ℕ) [HasConfinementSDPData n] (h : slaterStrict n) [HasConfinem [cited boyd-vandenberghe-2004,manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-boyd-vandenberghe-2004
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-08-01T23:31:05Z
parent: qou-k1mq
---

**File:** `QOU/Interactions/ConfinementSDP.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Interactions/ConfinementSDP.lean

### `ConfinementSDP`  —  line 144  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem ConfinementSDP (n : ℕ) [HasConfinementSDPData n] (h : slaterStrict n) [HasConfinementSDPStrongDuality n h] : primalOpt n = nTarget n * y0Star n `
- **Cited:** `[manuscript]`, `[boyd-vandenberghe-2004]`, `[boyd-vandenberghe-2004]`
  - [manuscript] particle-interactions/confinement-sdp
  - [boyd-vandenberghe-2004] Boyd, Vandenberghe (2004), *Convex Optimization* — (no DOI/URL)
- **Tractability:** SDP strong duality primalOpt = nTarget·y0Star under Slater; Mathlib has no SDP/conic strong-duality library.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.
