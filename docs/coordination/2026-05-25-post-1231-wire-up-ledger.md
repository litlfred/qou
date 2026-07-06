# Coordination ledger — post-PR #1231 wire-up + H_3/H_{3A} bug fix

**Owner branch:** `claude/h4-wedderburn-knot-atlas-2026-05-25` + follow-ups
**Started:** 2026-05-25
**Goal:** address author directives following PR [#1231](https://github.com/litlfred/qou/pull/1231) (crystal-Yekutieli correspondence audit) + PR [#1233](https://github.com/litlfred/qou/pull/1233) (probes A-D):

> *"fill compute gaps. wire all up. /coordinate"*
> *"please make sure using the common audit / coord doc"*

**Parent context:**
- PR [#1231](https://github.com/litlfred/qou/pull/1231) — crystal-Yekutieli correspondence audit + Mostow-Prasad + Epstein-Penner
- PR [#1233](https://github.com/litlfred/qou/pull/1233) — probes A-D follow-up (mixed: A ✓ B ✓ C ✗ D inconclusive)
- PR [#1238](https://github.com/litlfred/qou/pull/1238) — H_4 atlas + bug audit + A-polynomial audit (THIS LEDGER'S FIRST SHIP)

## Author directive queue (in order received)

| # | Item | Tier | Status | PR |
|---|---|---|---|---|
| Q1 | Correct Mostow-Prasad framing (q_0 ↔ m_μ/m_e via CAL-2, not m_p) | 0 | DONE (noted in audit + workplan) | #1238 |
| Q2 | H_3 vs H_{3A} legacy bug audit (background-agent flagged) | 1 | AUDIT DONE | #1238 |
| Q2b | H_3 vs H_{3A} pyhecke fix (runtime deprecation warn + migration plan) | 1 | IN FLIGHT | this ledger |
| Q3 | Hoefsmit (2,1) symbolic χ for β_Bor — proved in paper/Lean? | 0 | TODO | |
| Q4 | Bring-surface tessellation explicit table (ED, color tubes) | 1 | TODO | |
| Q5 | Yekutieli 2^k vs 4^k clarification (info-theory on Bring at Planck) | 1 | TODO | |
| Q6 | Categorical derivation of Markov-trace coefficients (rescoped Path B) | 2 | SCAFFOLD | A-polynomial audit |
| Q7 | Character variety + A-polynomial framework roles | 1 | AUDIT DONE | #1238 |
| Q8 | Recursive knot atlas extension (H_4 ✓, H_5 next) | 1 | H_4 DONE | #1238 |
| Q9 | Probe D redo with matching framing convention | 1 | TODO | |
| Q10 | Wire all up — fill compute gaps | 1-2 | IN FLIGHT | this ledger |
| Q11 | q_0 → X(K) explicit mapping + minimal-archimedean formulation (Q4 from new directives) | 1 | AUDIT DONE | this branch |
| Q12 | AJ conjecture (Garoufalidis) crosses archimedean wall — algebraic Jones tower | 1 | AUDIT DONE | this branch |

## Deliverables shipped this session

### PR [#1238](https://github.com/litlfred/qou/pull/1238) — merged 2026-05-25

**Code:**
- [`computations/alpha/alpha_k_jones_markov_h4.py`](../../computations/alpha/alpha_k_jones_markov_h4.py) — production H_4 Wedderburn atlas
- [`computations/alpha-k-jones-markov-h4.witness.json`](../../computations/alpha-k-jones-markov-h4.witness.json) — y_λ at H_4 substrate

**Audits:**
- [`docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md`](../audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md) — Q2
- [`docs/audits/2026-05-25-character-variety-a-polynomial-framework-roles.md`](../audits/2026-05-25-character-variety-a-polynomial-framework-roles.md) — Q7
- [`docs/audits/2026-05-25-q0-into-character-variety-minimal-archimedean.md`](../audits/2026-05-25-q0-into-character-variety-minimal-archimedean.md) — Q11 + Q12 (q_0 explicit mapping, minimal-archimedean, AJ conjecture algebraic)

**Workplan (NOW SUPERSEDED by THIS ledger):**
- [`docs/workplans/2026-05-25-post-pr1231-followup-workplan.md`](../workplans/2026-05-25-post-pr1231-followup-workplan.md) — superseded; this ledger is the authoritative tracker

### In-flight (this branch `claude/pyhecke-h3a-fix-2026-05-25`)

**Code changes:**
- [`tools/pyhecke/python/pyhecke/atom.py`](../../tools/pyhecke/python/pyhecke/atom.py) — added DeprecationWarning + canonical replacement pointer in `atom_per_generator_volumes`

## Cross-PR coordination posted

| Sibling PR | Relationship | Comment |
|---|---|---|
| [#1214](https://github.com/litlfred/qou/pull/1214) | OVERLAP — wiring-status taxonomy (0/17 canonically wired) | [comment](https://github.com/litlfred/qou/pull/1214#issuecomment-4531039619) |
| [#1220](https://github.com/litlfred/qou/pull/1220) | DOWNSTREAM — α-cluster recursion bug likely from H_3/H_{3A} | [comment](https://github.com/litlfred/qou/pull/1220#issuecomment-4531057403) |
| [#1211](https://github.com/litlfred/qou/pull/1211) | UPSTREAM — Q_borromean = 0 Lean proof | [comment](https://github.com/litlfred/qou/pull/1211#issuecomment-4530543819) from earlier session |
| [#1241](https://github.com/litlfred/qou/pull/1241) | DIRECT FILE OVERLAP — wires `atom_per_generator_volumes` into pyhecke public API; my PR #1240 added DeprecationWarning to same function | [comment](https://github.com/litlfred/qou/pull/1241#issuecomment-4531185437) — 2026-05-25 sweep |
| [#1228](https://github.com/litlfred/qou/pull/1228) | DOWNSTREAM — vol-density-derivation §9 cites PR #1211 + commit `68e51f80e` (my ⋈_K bar-sym); my AJ-conjecture algebraic identity supplies additional structural anchor | [comment](https://github.com/litlfred/qou/pull/1228#issuecomment-4531186638) — 2026-05-25 sweep |
| [#1127](https://github.com/litlfred/qou/pull/1127) | UPSTREAM CITED — their `prop:q-zero-complex-extension` + `prop:lusztig-vs-hermitian-bar` cited in my audit §10 (don't assume q_0 real) | [comment](https://github.com/litlfred/qou/pull/1127#issuecomment-4531187667) — 2026-05-25 sweep |

## H_3 vs H_{3A} fix — design + risk

**Bug:** `tools/pyhecke/python/pyhecke/atom.py:555-569` hardcodes H_3 Wedderburn weights for ALL atoms. Affects 15+ production scripts.

**Canonical replacement:** `computations/mass_at_3A_proper.py::per_generator_V_hat_3A` — sums over all partitions of 3A with proper Plancherel/Jones-Wenzl weights. Returns DIFFERENT shape: `{"full": V̂_i}` (1 channel) vs the buggy `{"std", "sym", "alt", "full"}` (4 channels).

**Why this session does NOT do the full migration:**
1. 15+ callers all use the 4-channel return shape
2. Per-call migration requires reasoning about each script's mass formula structure
3. Many witnesses would be invalidated; before/after sweep needed
4. High-risk if done in haste

**What this session DOES:**
1. ✅ AUDIT FLAG (PR #1238) — bug documented, callers identified
2. ✅ DEPRECATION WARNING (this branch) — runtime signal for A > 1 callers
3. ✅ MIGRATION POINTER in docstring — caller knows the canonical replacement
4. ❌ Full migration sweep — DEFERRED to dedicated PR with witness-comparison

## Honest scope assessment

Items DONE this session (Q1, Q2 audit, Q7, Q8): structural/audit work — high value, low regression risk.

Items DEFERRED (Q2b full fix, Q3, Q4, Q5, Q6 closure, Q9): require either:
- Specialist knowledge (Q3 Lean audit)
- Compute infrastructure not in flight (Q4 explicit Bring tessellation)
- Research-grade work (Q6 categorical derivation, Q5 info-theory)

The "wire all up" directive is BOUNDED by:
- This session's compute window (~hours, not weeks)
- Regression risk (touching pyhecke breaks 15+ scripts at once)
- Coordination overhead with 14+ open sibling PRs

## Next 2-3 concrete actions

1. Commit the pyhecke deprecation-warning fix to this branch + PR + merge
2. Q3: search repo for Hoefsmit (2,1) Lean theorems; surface gaps
3. Q9: redo Probe D with matching framing convention (Wedderburn re-derive)

## Open after this ledger

- Q4: Bring-surface tessellation (research-grade visualization work)
- Q5: Yekutieli 2^k vs 4^k + Bring-at-Planck (research-grade)
- Q6: categorical derivation of Markov-trace coefficients (rescoped Path B, research-grade)
- pyhecke FULL migration sweep (dedicated PR, ~1 week)

## Cross-reference back to this ledger

Any audit, content block, or compute file added during this work
tranche **should link back to this ledger** as the authoritative
session-context document. Avoid scattering new audits into
`docs/audits/` without a ledger entry here.
