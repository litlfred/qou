---
# qou-ypq6
title: The unified-iterative-correction table block has no live producer -- its numbers reproduce from nothing in the tree
status: todo
type: task
priority: normal
created_at: 2026-09-12T23:18:05Z
updated_at: 2026-09-19T06:16:01Z
---


## Found while dropping the Pass-2 sign gate (`qou-21oc`, PR #7253)

Work item: check content blocks citing `prop:unified-iterative-correction` for
quoted numbers the gate drop moves. Nine blocks cite it; one carries numbers.

`content/quantum-observable-universe/mass-theory/unified-iterative-correction-table-data.md`:

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


## 2026-09-19 — hunted, and the finding is stronger than "not found"

Owner selected both "hunt the producer" and "scope as historical"; run as a
sequence. **No producer is findable by the six paths, AND there is positive
evidence the table was never machine-generated.** The second half does not
depend on search coverage.

### The lead resolved the COLUMNS, not the producer

This bean said `-16.45` appears "in no audit". It appears in exactly one:
`docs/audits/2026-09-05-binding-route-consolidation-no-knot-selection.md:70`,
which names the column semantics and nothing else — `B_dedi` = the dedicated
per-`A` knot-factor route, `B_unif` = the unified accumulator. Its "misses
²⁰⁸Pb by 58 %" checks out against the table (`2592/1636 = 1.584`). It names no
emitting script, and none exists.

### Evidence of hand assembly — properties of the TABLE, not of the search

**Three of seven `B_AME` cells do not round to AME2020** (`ame2020.json` via
`ame_binding_mev`; verified independently by the parent session):

| atom | published | AME2020 | diff |
|---|---:|---:|---:|
| ¹⁴C | **105.7** | **105.2845** | **+0.4155** |
| ²⁰Ne | 160.7 | 160.6448 | rounds to 160.6 |
| ²H | 2.224 | 2.2246 | rounds to 2.225 |

A producer reading that table **cannot emit 105.7**, and it is no neighbouring
nuclide (¹⁴N 104.659, ¹³C 97.108).

**The column identity closes on 3 of 7 rows.** `B_dedi + Σ_λ B_λ` vs published
`B_unif`: exact at ⁴⁰Ca, within display rounding at ²⁰Ne and ²⁸Si, and off by
−2.224 / +2.150 / +9.600 / **+163.000** at ²H / ⁴He / ¹⁴C / ²⁰⁸Pb. One pass of
one program does neither.

### 🛑 THREE `unified`-named objects, and the corpus's own correction points at the wrong one

| # | object | why not this table's `B_unif` |
|---|---|---|
| 1 | `hecke_core_legacy.unified_iterative_correction` | ungated ²H = −17.6908290020795 at `k_exact = k_max = 11`, gated −9.14773623102088; published −16.45 is neither |
| 2 | `probes/strong_unified_binding_probe.py::B_unified` | **anchor-inverted** (`w_2 = AME_B["D"]/…`); returns 2.2246 at A=2 *by construction*; four atoms, not seven |
| 3 | `_deprecated/unified_binding.py` | magic-anchor dispatch on `Q_NEUTRON_MEV`; 8 of 9 values absent from its witness |

`mba-step09b-per-isotope-binding.md:44-48` carries a correction (PR #5765,
2026-08-25) naming **(2)** as where "the `B_unified` model lives". True of a
different object; **not** a pointer to this table's producer. Wiring it would
attach a published −16.45 to a script returning +2.2246. One grep from
happening. Follow-up bean warranted.

### 🛑 `git log --follow` is unusable here — shallow clone

All four commits it reports for the `.md` appear in `.git/shallow`. The oldest,
`0d62fe2a23b`, shows the file as `A` while changing **28,153 files / 9.9M
insertions** — the graft presenting the whole tree as new — and its subject
("honest convergence guard — multi-cut certificate") is an unrelated arc.
**Do not date the table to it.** `git diff 0d62fe2a23b HEAD` on the `.md` is
empty: byte-identical across the fetched window.

**Discriminator for a graft:** `git show --name-only --format='' <sha> | wc -l`
— a four-figure count is a graft boundary, not a commit.

### Disposition landed

`.ts` gains an `authorNotes` status entry; `.md` gains a reader-facing
provenance caveat (authorNotes are skipped by default in the LaTeX render, so
an authorNotes-only disposition would leave the published paper unchanged).
**No `computation` field wired** — there is no producer to point at, and
choosing settings that reproduce the numbers is selection against the target.

### STAYS OPEN (rule 13a)

The origin is still unidentified. Settling it needs a **full-history clone** and
`git log -S'-16.45' --all`, unavailable here — every commit reachable for this
file is a shallow boundary. That is the one open step.

### Side-finding: AGENTS.md §4d is stale by one pin bump

§4d's 🛑 box says `authorNotes` on a `table` block is silently dropped against
pin `428ca5c`. **The pin is `df28d02` (bumped 2026-09-07)**, and
`.folio-assistant-pin`'s own bump note records that this bump restores exactly
those fields, naming `tm-interaction-completeness` — a `table` block — among
the three warnings that clear. So `authorNotes` here is kept. §4d is a
correction that was itself overtaken.
