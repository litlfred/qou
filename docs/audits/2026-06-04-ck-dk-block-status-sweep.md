# c_k / d_k block-status sweep — align paper blocks to the registry

**Date:** 2026-06-04
**PR:** [#1818](https://github.com/litlfred/qou/pull/1818) (`claude/ck-dk-block-status-sweep-2026-06-04`)
**Status:** DONE
**Registry (authoritative):** [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)

## Why

Follow-up to the c_k / d_k consolidation (PR #1813). The registry is now the
single source of truth for canonical-vs-empirical status. This sweep aligns
the **paper content blocks** whose c_k / d_k status language contradicts it,
so the paper and the registry agree.

## Findings — after verification

### Aligned (real contradictions, fixed in this PR)

| block | claim | registry tier | action taken |
|---|---|---|---|
| `stochastic-mechanics/q-beta-categorical-precision-ladder-table1-data.md` | `c_3` empirical match "**exact**"; `c_4`/`c_5` "Closed form **derived**" (while the adjacent column reads 99.1%/99.9%) — and the cited audit `-qbeta-all-ck-categorical-extension.md` **does not exist** (broken link) | c_3 near-match (~3%, refuted real-q); c_4 empirical; c_5 open — all near-matches, not derived | c_3 "exact" → "near-match (~3% at q₀; refuted real-q)"; c_4/c_5 "derived" → "near-match (empirical tier)" with the broken link replaced by the registry link |
| `mass-theory/qbeta-c4-from-c3-c8-product-identity.md` | c_4 "**derived** from c_3, c_8" (already internally caveated as conditional on an open c_8 proof) | c_4 **empirical** (conditional) | added a registry cross-reference clarifying the empirical tier + the "machinery-proved ≠ values-derived" distinction; no math/proof rewrite |

### Ruled out on inspection (NOT contradictions — left unchanged)

| candidate | why it is NOT a contradiction |
|---|---|
| `stochastic-mechanics/polynomial-bar-involution.md` "6" | **false positive** — `barPoly_cos_truncated_6` is a Taylor truncation order, not a dashboard count |
| `particle-interactions/q-beta-spectral-bridge.md` "cycle-6/7" | **false positive** — an audit-cycle reference, not a dashboard count |
| `stochastic-mechanics/c5-involution-leibniz-decomposition.md` | **legitimate** — proves c_5 *bar-symmetry* + the q=1 classical limit `c5_classical_limit_eq_neg_five_quarters` (sorry-free); these are structural-property proofs, NOT a q₀ "canonically-derived" overclaim. Weakening them would be wrong. |
| `index-of-definitions/definition-index.md` (conj entry) | already aligned — describes c_3 as a near-match and c_{k≥3} as cal-anchored/open; links the conjecture class. No change needed. |

**Lesson:** the "verify before editing" discipline caught two false-positive
dashboard "fixes" and one legitimate q=1-limit proof that a naive
status-sweep would have wrongly weakened.

## Discipline

- **No mathematical rewrite.** Align *status language* (derived/canonical →
  empirical/near-match/open) + add a registry cross-reference; do not touch
  the formulae or proofs.
- **Verify before editing** — distinguish a genuine q=1 classical-limit proof
  from a stale q₀ "derived" overclaim; only the latter is misaligned.
- **Status → `authorNotes`** where a banner is status-tracking (AGENTS.md §4d);
  scholarly caveats stay in prose.
- Run `content-validation` after edits.
- Where "derived vs empirical" is genuinely contested (c_4 product identity),
  align to the registry tier AND surface to the author rather than silently
  flipping the paper's claim.

## Deliverable

Aligned blocks + this catalog; the registry stays authoritative.
