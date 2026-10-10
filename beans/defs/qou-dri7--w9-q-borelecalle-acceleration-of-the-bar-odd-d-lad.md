---
# qou-dri7
title: 'W9: q-Borel/Ecalle acceleration of the bar-odd D-ladder (1ppq Option 1, unowned)'
status: scrapped
type: task
priority: normal
created_at: 2026-07-17T14:58:56Z
updated_at: 2026-08-14T19:46:00Z
---

**Consolidation carrier.** This bean absorbs `qou-b00b` and `qou-xuc4`, which
were the same task under three titles. All three were created 2026-07-17 with
**empty bodies** and never written to.

- `qou-b00b` — "F1: odd D-ladder Ecalle acceleration — median/Watson resummation
  via parity-split per-channel estimators"
- `qou-xuc4` — "Probe: qbeta_dladder_ecalle_acceleration (Borel-Leroy + q-Borel
  + parity-split, estimator gate)"
- `qou-dri7` (this) — "W9: q-Borel/Ecalle acceleration of the bar-odd D-ladder"

One object (the bar-odd D-ladder `D(ũ)`), one operation (q-Borel / Écalle
acceleration, median-Watson resummation), three beans.

## SCRAPPED 2026-08-14 — the premise was divergence, and the ladder converges

Every technique named in the three titles — **Écalle acceleration**,
**median/Watson resummation**, **Borel–Leroy** — exists to assign a sum to, or
extract Stokes data from, a **divergent** asymptotic series. That was the
premise when these were opened on 2026-07-17, under the then-current
[`2026-07-12-dladder-divergence-correction.md`](../docs/audits/2026-07-12-dladder-divergence-correction.md).

That premise was **withdrawn 2026-08-09**:
[`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](../docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md)
— *"the c₃ D-ladder is CONVERGENT"*, radius `ρ = ũ(q*_ρ) = 0.142799996644689…`,
the image of a `Q_b` zero the singularity search had omitted
(`k²Δ²log|d_k| → 1`, `kΔ² → 0`, so `κ = 0`).

With convergence, each stated goal is moot or already met:

| goal in the titles | state |
|---|---|
| resum the divergent ladder | nothing to resum — the series converges on `\|w\| < ρ` |
| median/Watson lateral ambiguity | no divergence ⇒ no lateral Borel ambiguity to resolve |
| accelerate / extract asymptotics | **already in hand** — KC22 gives `D(w) = φ(w)log(1−w/ρ) + ψ(w)` with algebraic `φ`,`ψ`, hence `d_k = −(1/(2h*_ρ))ρ^{−k}/k(1+O(1/k))`, **no free parameters** |

The (q-)holonomic exclusion these beans sat beside is **untouched** and still
stands — a convergent series need not be holonomic, and KC22's closed form is
exactly the sort of element that is not low-order P-finite.

## Scope — (a), not (b)

Scrapped because **the stated task's target does not exist**, not because
q-Borel methods are excluded from this function. No invariant is named
forbidding a q-Borel study of the `log(1−w/ρ)` branch point at `ρ`; that would
be a *different* task with a different motivation, and it should be opened as a
new bean with that motivation stated, not resumed under these titles.

## Do not confuse with `qou-vkg5` — different object, opposite status

`qou-vkg5` (Écalle bridge equation / C1's `∞` weight) is **live and productive**
and is **not** affected by any of the above. The two share the word "Écalle" and
nothing else:

| | object | regularity | resurgence applies? |
|---|---|---|---|
| this bean | bar-odd D-ladder `D(ũ)` | **convergent**, `ρ = 0.1428` | no — nothing to resum |
| `qou-vkg5` | C1 at `∞` | **irregular**, slope `½`, divergent | **yes** — genuinely |

Scrapping this one says nothing about that one. The recurring failure mode in
this corpus is a shared glyph or term standing for two different objects
(cf. the KC21/KC22 `q*` collision, PR #5022 §9a); this is the same shape at the
level of a *technique name*.

Follow-on: `qou-tdp0` — `docs/coordination/1ppq-qbeta.md:1055-1058` still asserts
the withdrawn resurgent/Écalle inference as live, and instructs future agents on
it. That is the doc-side remainder of this same correction.
