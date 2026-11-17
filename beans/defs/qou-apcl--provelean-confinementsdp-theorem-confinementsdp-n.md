---
# qou-apcl
title: 'PROVE(lean): ConfinementSDP — theorem ConfinementSDP (n : ℕ) [HasConfinementSDPData n] (h : slaterStrict n) [HasConfinem [cited boyd-vandenberghe-2004,manuscript]'
status: in-progress
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-boyd-vandenberghe-2004
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:05Z
updated_at: 2026-10-04T15:22:26Z
parent: qou-l2vh
---

**File:** `QOU/Interactions/ConfinementSDP.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/Interactions/ConfinementSDP.lean

### `ConfinementSDP`  —  line 144  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem ConfinementSDP (n : ℕ) [HasConfinementSDPData n] (h : slaterStrict n) [HasConfinementSDPStrongDuality n h] : primalOpt n = nTarget n * y0Star n `
- **Cited:** `[manuscript]`, `[boyd-vandenberghe-2004]`, `[boyd-vandenberghe-2004]`
  - [manuscript] particle-interactions/confinement-sdp
  - [boyd-vandenberghe-2004] Boyd, Vandenberghe (2004), *Convex Optimization* — (no DOI/URL)
- **Tractability:** SDP strong duality primalOpt = nTarget·y0Star under Slater; Mathlib has no SDP/conic strong-duality library.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.


## RE-CHECKED 2026-08-31 — verdict CONFIRMED, and the file is already honest about it

Mathlib genuinely has no SDP/conic-duality API, and that IS the required input (cited to
Boyd-Vandenberghe section-5.3). So the boilerplate verdict is right here.

Worth recording separately: this file **already carried the conclusion-carrier defect and a
prior agent already fixed it.** Its own in-body comment says the proof "previously read
`exact HasConfinementSDPData.strong_duality`, projecting a `strong_duality` field the DATA
class carried (doc-labelled 'conclusion'), while this docstring said the conic-duality step
'is discharged by `sorry` here' ... **Both were false**."

That field is deleted. `ConfinementSDP` now takes the Slater condition `h` as a real argument
plus a SEPARATE `[HasConfinementSDPStrongDuality n h]` — a legitimate section-3b-cond
hypothesis, with a `Fact`-backed default instance so a caller with a solver-verified identity
can supply it.

So this is the honest pattern, not a defect, and the corpus self-corrected it here without the
bean being touched. Third independent instance of the same defect class found in this arc.
