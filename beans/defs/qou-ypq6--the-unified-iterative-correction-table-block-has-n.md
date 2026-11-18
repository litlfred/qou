---
# qou-ypq6
title: The unified-iterative-correction table block has no live producer -- its numbers reproduce from nothing in the tree
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T23:18:05Z
updated_at: 2026-10-04T15:25:01Z
parent: qou-5vkl
---


## Found while dropping the Pass-2 sign gate (`qou-21oc`, PR #7253)

Work item: check content blocks citing `prop:unified-iterative-correction` for
quoted numbers the gate drop moves. Nine blocks cite it; one carries numbers.

`folio/quantum-observable-universe/mass-theory/unified-iterative-correction-table-data.md`:

| Atom | `B_dedi` | `B_unif` | `B_AME` | `Σ_λ B_λ` |
|:--|--:|--:|--:|--:|
| D | 2.224 | -16.45 | 2.224 | -16.45 |
| ⁴He | 28.19 | 16.67 | 28.30 | -13.67 |
| ¹⁴C | 102.0 | 108.1 | 105.7 | -3.50 |
| ²⁰Ne | 162.6 | 163.0 | 160.7 | +0.43 |
| ²⁸Si | 234.9 | 244.8 | 236.5 | +9.94 |
| ⁴⁰Ca | 341.3 | 366.7 | 342.1 | +25.4 |
| ²⁰⁸Pb | 1631 | 2592 | 1636 | +798 |

**No producer in the tree emits these.** `-16.45` appears in no witness, no
`computations/` script and no audit (grepped `computations/`, `docs/`, all JSON
and MD). The `.ts` sibling is a bare `table(...)` with `tags:
["extracted-table"]` and no `computation` field, and the proposition it claims
to extract from carries no table. So it is an orphaned extraction.

**This is NOT a consequence of the gate drop and was not "fixed" here.** The
numbers were already disconnected from the producer before today.

## The one thing worth noting before someone re-derives them

`Σ_λ B_λ` at D is `-16.45`. Measured at the production default
(`k_exact = k_max = K_PARTITION_MAX = 11`) with the gate **dropped**:

    ²H    ungated -17.6908290020795     gated -9.14773623102088
    ⁴He   ungated -15.9926510049258     gated -8.20155846836239

The published `-16.45` is within 7 % of today's **ungated** total and is 1.80x
the gated one. At ⁴He the published `-13.67` is 0.85x the ungated and 1.67x the
gated. That is **weak** evidence the table was computed before the gate existed
— consistent in sign and order of magnitude with the ungated sum, and far from
the gated one — but it is not a reproduction and must not be written up as one.
Two atoms, no ⁴He agreement to speak of, and the `B_unif` column does not equal
`B_dedi + Σ_λ B_λ` in either row (D: 2.224 + (-16.45) = -14.23, published
-16.45; ⁴He: 28.19 + (-13.67) = 14.52, published 16.67), so the column
definitions are not recoverable from the table either.

## What would close this

Either identify the producer (and wire `computation` into the `.ts`), or scope
the block as a historical record with no live derivation. **Do not regenerate
it by picking the settings that best reproduce the published numbers** — that
is selection against the target, and at ²⁰⁸Pb the compute is out of reach
anyway (`binding_energy` is >50 min for the SMALLEST bound atom, bean
`qou-i7ju`).

Related: `qou-21oc` (the gate drop), `qou-sv7h` (the accumulator's scaling
wall), `qou-bm4i` (blocks claiming `computation.status: verified` on failing
witnesses — same family of defect, different mechanism).
