> **DEPRECATED on 2026-05-24.** Undated audit document classified as workplan / status snapshot / migration-handoff / one-off investigation whose findings have been integrated into main or whose plan has been executed. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T5 for the deprecation rationale.

# Author-question queue (compute-integration-watcher)

Tracks open questions waiting on owner sign-off.  Pulled in priority
order by the skill when the foreground task is idle.

## Format

```
### Q<N> — <one-line topic>            [priority: P0|P1|P2  status: pending|answered]

- **trigger**: <commit SHA or PR# that surfaced this>
- **context**: <2–3 sentences>
- **options**:
  - (a) ...
  - (b) ...
  - (c) ...
- **session-touch**: <files / blocks that change when answered>
- **answer**: <recorded when answered>
```

## Pending

### Q7 — Lean namespace for new flavor-dressing functor     [P1  pending]

- **trigger**: Q6 answer (`braids-and-knots/`) leaves Lean namespace open
- **context**: D3 work lives in `braids-and-knots/`.  The new Lean
  decls can either join the existing `QOU.BraidKnot.*` namespace
  (alongside `DressedParticle`, `MassTowerCoefficientStratification`)
  OR get a fresh sub-namespace `QOU.FlavorDressing.*` (clearer
  organization but more decl paths to update).
- **options**:
  - (a) reuse `QOU.BraidKnot.*` — fewer rename touches, less clean
  - (b) new `QOU.FlavorDressing.*` — cleaner, isolates the new
    structural notion
  - (c) under `QOU.HadronicMass.*` (current home of `lem:nucleon-mass-splitting`)
- **session-touch**: every new `.ts` block's `lean.ref`, every new
  `.lean` file's namespace, and (depending on choice) up to 6
  existing references that point at the lemma's Lean decl

### Q8 — heavy-flavor placeholders                          [P1  pending]

- **trigger**: D3 lift scope claims "the paper proves bounds" for all
  flavors; substrate derivation currently only covers u/d
- **context**: u, d get explicit derivation from
  `prop:flavor-split-substrate`.  s, c, b, t need EITHER (i)
  `conj:` blocks with class-axiomatized placeholders per
  AGENTS.md §3b, (ii) `def:`-only entries with no derived value,
  or (iii) be excluded from D3 and added in a follow-up.
- **options**:
  - (a) all 6 flavors with `conj:` placeholders for s/c/b/t
  - (b) u/d only; s/c/b/t excluded from D3 (smallest scope)
  - (c) u/d derived + s/c/b/t as `def:`-only without `conj:`
- **session-touch**: 4 extra `conj:` blocks if (a) chosen;
  paper manifest if these need to register as a new section group

### Q9 — bound theorem statement form                       [P0  pending]

- **trigger**: D3 includes `thm:dressed-quark-mass-bounds`
- **context**: Several candidate statements:
  - (i) `0 < μ_q < M_N` for every flavor q (loose two-sided)
  - (ii) `μ_q < c · M_N` for explicit c from `mass_upper_bound`
    (quantitative)
  - (iii) `0 < μ_d − μ_u < M_N · h_q² · ℏ_q · [2]_q · ε` — bounds
    on the SPLITTING rather than per-flavor mass
- **session-touch**: `.lean` proof complexity scales with which
  bound is targeted; (i) is one-line, (ii) needs the explicit `c`,
  (iii) needs `prop:flavor-split-substrate` plumbing in Lean
- **options**:
  - (a) (i) loose two-sided — fastest
  - (b) (ii) quantitative — most useful
  - (c) (iii) splitting-only — closest to existing infra

## Answered (session 2026-05-18)

### Q1 — flavor-split-substrate wiring choice          [P0  answered]

- **trigger**: `prop:flavor-split-substrate` flagged I2 in 2026-05-18 audit
- **answer**: **A** — replace CODATA m_n−m_p input with substrate formula

### Q2 — implementation scope (where to wire it)       [P0  answered]

- **trigger**: A choice in Q1
- **answer**: **A2** — fresh sibling PR `claude/wire-flavor-split-substrate`

### Q3 — fate of `lem:nucleon-mass-splitting`          [P0  answered]

- **trigger**: A2 implementation needs predecessor-fate decision (I2-a)
- **answer**: **Delete lemma; create definitions + remarks/props as needed.**
  Dressed-quark numerology becomes derived from the new structural
  definition rather than absorbed into a lemma input.

### Q4 — structure of replacement content              [P0  answered]

- **trigger**: Q3 answer requires structural choice
- **answer**: **(D)** chapter-level functor definition; user notes
  "theoretically even more above this — paper proves bounds."

### Q5 — lift scope                                    [P0  answered]

- **trigger**: D choice in Q4 has 4 scope tiers
- **answer**: **(D3)** Full structural lift with bounds — 1 def + 2
  props + 1 thm + 1–3 remarks + meaningful Lean (~10–15 hours).

### Q6 — directory for new content                     [P0  answered]

- **trigger**: D3 authoring requires file-tree placement
- **answer**: **(L2)** `braids-and-knots/` — alongside existing
  bound props.  Lean namespace open — surfaced as Q7.
