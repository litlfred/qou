---
# qou-6bla
title: One notation per object — consolidate the ℏ_q spelling family; the q-integer split is the literature carve-out
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T12:38:14Z
updated_at: 2026-10-04T15:11:02Z
parent: qou-lv2z
---

Owner directive, 2026-08-30: *"lets use one notation.... consolidate different
names of things unless they are already existing in the lit and the point is
to show an unknown connection."*

So the rule has two halves, and the second half is doing real work here.

## Half one — consolidate: the ℏ_q family

`ℏ_q = 1 − q⁻¹` is written under **four names** and **four equal bodies**
across **~38 sites**:

| names | bodies (all equal) |
|---|---|
| `hbar_q`, `hbarQ`, `hbar`, `hbarQc` (+ `hbarQSq`, `hbar_q_sq`, `hbarQ'`) | `(q-1)/q`, `1 - q⁻¹`, `1 - 1/q`, `1 - ↑q⁻¹` |

Nothing mathematical distinguishes them — this is the case the directive is
aimed at. Not yet done; ~38 sites spanning library and block siblings, and a
canonical spelling has to be picked first. **Recommendation:** `hbarQ` as the
identifier (camelCase matches the corpus's newer Lean naming and avoids the
`hbar_q`/`hbarQ` near-collision), body `1 - q⁻¹` (matches the notation
register's `ℏ_q = 1 − q⁻¹`, and `(q-1)/q` carries a division that `1 - q⁻¹`
does not).

**One member was not a spelling at all, and is fixed.**
`QOU/MassTheory/EmGermMomentVanishing.hbar` was `q - q⁻¹` — the Hecke
structure constant of AGENTS.md §7a, **2.11× ℏ_q** at the anchor
(0.2090602988 vs 0.0990817160 at `q₀ = 1.1099785827513808`). The docstring
always said "the bar-odd generator h"; only the identifier read as ℏ. Renamed
`barOddGen`, 18 sites, `lean`-direct exit 0.

## Half two — the carve-out: the q-integer family is NOT to be merged

`qInt` / `qIntBal` / `qIntGeo` / `qBracket` / `qIntPoly` / `qNumber` /
`quantumTwo` look like the same sprawl and are not. **Geometric**
`[n]_q = 1 + q + … + q^{n-1}` and **balanced**
`[k]_q = (q^k − q^{-k})/(q − q^{-1})` are both standard in the literature,
they are genuinely different objects, and the corpus carries a *proved* twist
between them — `QOU.Mass.QHookDimensionBalanced.qIntBal_eq_twist`:
`[k]_q^bal = q^{-(k-1)} · [k]_{q²}^geo`. That identity is exactly the
"unknown connection" the directive protects.

`qou-qint` (todo, high) already holds the plan and its guardrail: **do not
blanket-convert geometric → balanced** — a geometric site is *correct* when
its variable means `q²`, so converting it would introduce an error. The
resolution there is to put the convention **in the name** (`qIntGeo` /
`qIntBal`, never bare `qInt`), which is one-notation-per-*object* rather than
one name for two objects. Do that work in `qou-qint`, not here.

## Method note

Both halves were found by the same measurement: comparing declaration bodies
across the library / block-sibling surfaces
(`scripts/lean-name-surface-audit.py`). Sameness of *body* is what separates
half one from half two — four equal bodies under four names is sprawl; two
inequivalent bodies under one name is either a defect (`hbar`) or a
literature distinction that must be named (`qInt`).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
