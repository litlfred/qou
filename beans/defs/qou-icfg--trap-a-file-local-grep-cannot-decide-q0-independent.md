---
# qou-icfg
title: 'TRAP: a file-local grep cannot decide `q0Anchor: independent` — 52 of 81 candidates read q0 through the import cone'
status: completed
type: task
priority: high
created_at: 2026-09-03T05:40:00Z
updated_at: 2026-09-03T05:40:00Z
---

Recorded while triaging the q0-anchor refill (150 unstamped witnesses; the
refill itself is `qou-q0rf`, carried on PR #6456, unmerged at the time of
writing).

## The trap

`q0Anchor: "independent"` is a **producer-declared assertion** that no
substrate pin enters the computation. The obvious way to decide it is to grep
the producer for `q_at` / `q_muon_at` / `Q_50_DIGIT_STR` / `q_parameter` /
`resolve_q0_anchor`. **That test is wrong, and it is wrong most of the time.**

Measured on the 150-witness refill, 2026-09-03, `main` `62c0f17dead`:

| test | verdict "q0-free" |
|---|---|
| file-local grep, comments stripped | **81** of 149 resolved producers |
| the same, then a transitive AST import-cone walk inside `computations/` | **29** |

**52 of the 81 — 64 % — read q0 through a module they import.** A file-local
grep would have stamped every one of them `independent`, which is not a
missing stamp but a **false assertion in a durable artifact**: it states that
no pin applies to a number that was computed at one.

This is the same class as the import-cone drift already recorded in AGENTS.md
for witness staleness (`binding_canonical.py` is source-stable while
`tr_M_atom` moved 48 % because a module it calls changed). The lesson
generalises: **for any question of the form "does this producer touch X",
a file-local answer is not an answer.**

## The measurement

`ast.parse` each producer, collect top-level module names from `Import` /
`ImportFrom`, resolve them against `computations/**/*.py` by stem, recurse
with a seen-set, and treat `q_parameter` (any depth) as a terminal yes.
Comment lines are stripped before the pattern match, because several
producers discuss `q = psi` in a module docstring while computing nothing of
the kind — `h3_gram_degeneracy_is_wedderburn_weight_vanishing.py` has 13 such
docstring hits and is genuinely q0-free.

Script: `/tmp/.../cone.json` was produced ad hoc; the walk is ~30 lines and is
reproduced in the PR body. It has NOT been committed as an audit — if a future
agent wants this as a gate rather than a one-off, that is worth doing, and is
the honest follow-up.

## Scope of the claim

The walk resolves imports **by stem within `computations/`**. It treats
`qou_substrate` and `pyhecke` as opaque (they are packages, and a producer
importing `qou_substrate.witness` for `WitnessBuilder` is not thereby reading
a pin). So a producer that reaches a pin *through a package helper other than
`q_parameter`* would still be missed. That is a real residual blind spot and
is stated rather than papered over: the 29 are **candidates confirmed against
this walk**, not proved q0-free in the absolute.

Each of the 29 therefore carries a `q0AnchorReason` that names the method and
its date, so a later reader can tell what was actually checked:

> "No substrate pin enters this computation: neither the producer nor its
> transitive import cone inside computations/ references q_at, q_muon_at,
> Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST
> import-cone walk, 2026-09-03). The probe computes: …"

## Related

- `qou-q0rf` — the refill itself (PR #6456).
- `qou-fl0a` — manifest `ambiguous` declarations whose stamp is discarded.
- `qou-5le1` — the q0 classifier is blind to inline q0 re-derivation.
