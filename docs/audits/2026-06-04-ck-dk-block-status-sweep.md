# c_k / d_k block-status sweep — align paper blocks to the registry

**Date:** 2026-06-04
**PR:** (this branch — `claude/ck-dk-block-status-sweep-2026-06-04`)
**Status:** PLAN
**Registry (authoritative):** [`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)

## Why

Follow-up to the c_k / d_k consolidation (PR #1813). The registry is now the
single source of truth for canonical-vs-empirical status. This sweep aligns
the **paper content blocks** whose c_k / d_k status language contradicts it,
so the paper and the registry agree.

## Findings (contradictions to align)

| block | claim | registry tier | action |
|---|---|---|---|
| `stochastic-mechanics/q-beta-categorical-precision-ladder-table1-data.md` | `c_5 = −(b²+1/2)` "Closed form **derived**", 99.9% | c_5 **open**; 99.9% = near-match | soften "derived" → near-match + registry xref |
| `mass-theory/qbeta-c4-from-c3-c8-product-identity.md` | c_4 "**derived** from c_3, c_8" | c_4 **empirical** (fit/artifact); c_8 itself open | note conditional-on-open-c_8 + registry tier |
| blocks with `6/7` / `4/7` dashboard counts | stale beats-100× count | live **3/7** | correct to 3/7 (verify each) |
| `index-of-definitions/definition-index.md` (conj entry) | `c_3 = −2 = J_Hopf(q=1)` near-match | c_3 near-match **+ REFUTED real-q** | add refutation note |
| `stochastic-mechanics/c5-involution-leibniz-decomposition.md` | `c_5(q=1) = −5/4` proved | (q=1 classical limit — verify vs q₀ claim) | verify; align if conflated |

## Discipline

- **No mathematical rewrite.** Align *status language* (derived/canonical →
  empirical/near-match/open) + add a registry cross-reference; do not touch
  the formulae or proofs.
- **Verify before editing** — distinguish a genuine q=1 classical-limit proof
  from a stale q₀ "derived" overclaim; only the latter is misaligned.
- **Status → `authorNotes`** where a banner is status-tracking (CLAUDE.md §4d);
  scholarly caveats stay in prose.
- Run `content-validation` after edits.
- Where "derived vs empirical" is genuinely contested (c_4 product identity),
  align to the registry tier AND surface to the author rather than silently
  flipping the paper's claim.

## Deliverable

Aligned blocks + this catalog; the registry stays authoritative.
