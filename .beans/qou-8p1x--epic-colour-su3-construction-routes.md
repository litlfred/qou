---
# qou-8p1x
title: 'EPIC: routes to a 3-dimensional fibre / colour SU(3) — assessed and roasted'
status: in-progress
type: milestone
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-08-07T12:40:00Z
---

Umbrella for every proposed route to colour `SU(3)`, old and new, after the
Bring -> Klein bridge was excluded (`qou-8p1b`, scope-(b)).

## The gap, stated once, precisely

**NOT** "why `N = 3`" — that is DONE. `RowCapObstruction.lean` already proves
the Weyl arithmetic (`weylDimAlt N = N.choose 3`, `no_singlet_of_lt_three`,
`singlet_forces_three`). Do **not** re-derive it.
`a2-from-three-strands.md` explicitly disclaims supplying it (its `A_2` is the
Coxeter group on three *strands*, not the `sl_3` acting on the fibre).

The gap is upstream of all of that:

> **The single-fibre construction supplies `dim V = 2`. Colour needs a
> 3-dimensional fibre.**

Every route below is judged on one question: **does it produce that object?**

## Scoreboard

| # | Route | Bean | Produces a 3-dim fibre? | Verdict |
|---|---|---|---|---|
| 1 | Multi-fibre groupoid (T3b) | `qou-8p1i` | count of objects, not a fibre dim | **live, untested** — weakest content, cheapest to state |
| 2 | Bruhat / `GL_n(F_q)` realisation of `H_n(q)` | `qou-8p1h` | group natively; fibre via complex **3** of `PSL(2,7)` | **live, gated** on `qou-8p1j` |
| 3 | char-2 justification (gate for #2) | `qou-8p1j` | — | **the load-bearing unknown** |
| 4 | Octonionic `G_2` (status quo, direction 2) | — | yes, by import | **works, but unearned** — substrate bridge dead, `qou-8fl1` |
| 5 | Tetraplectic / quaternionic (Foth, Foth–Leitner) | `qou-8p1g` | supplies `SU(2)`, already spent on electroweak | **does not reach `SU(3)` as instantiated** |
| 6 | "4-form degenerates" -> `Spin(7)` -> `G_2` -> `SU(3)` | `qou-8p1f` | — | **EXCLUDED scope-(b)**, dimension count |
| 7 | `G_2 -> SU(3)` via `S^6 = G_2/SU(3)` | open-problem item 3 | yes, if `G_2` granted | **surviving form-stabilizer link** |

## The roast, route by route

**#1 multi-fibre groupoid.** It is a *name*, not a construction. Nobody has
exhibited the inequivalent fibre objects or shown their interaction space is
three-dimensional. It relocates "why is `dim V = 3`" to "why are there exactly
3 inequivalent fibres" — the same question wearing a hat. Its virtue is that it
is the only route that is both substrate-native and completely untouched by the
Klein exclusion.

**#2 Bruhat.** The strongest *idea*: `H_n(q)` IS the Iwahori–Hecke algebra of
`GL_n(F_q)` by origin, so this is the framework's own core object's defining
realisation, not an import. At `n = 3, q = 2` everything lands
(`21` flags, Fano `= PG(2,F_2)`, `Aut = GL(3,F_2) = PSL(2,7)`, order `168`).
Three things to be honest about: (a) **`q = 2` is the whole ballgame** — the
framework's `q` is a deformation parameter and `q_0` is a *locally observed,
varying* value; jumping to `q = 2` because it yields `168` is textbook
numerology absent a derivation, see `qou-8p1j`; (b) `F_2^3` is **not** a
`C`-fibre, so the fibre still comes from the complex **3** of `PSL(2,7)` —
rep theory you would have had anyway, which weakens the "native" claim;
(c) the Iwahori–Hecke algebra only sees the `B`-bi-invariant part, so
recovering the *group* needs the building, not just `H_3(q)`.

**#4 octonionic `G_2` (status quo).** It works and it is standard mathematics.
The problem is not correctness, it is provenance: `prop:color-su3-from-g2` has
an **empty `uses[]`** and there is no `def:octonion-algebra` in the corpus at
all. After the Klein exclusion this is the section's sole foundation, undefined
and unconstructed (`qou-8fl1`, and see the dependency audit).

**#5 tetraplectic.** In-corpus, owner's own paper, Lean-formalised sorry-free —
and it still does not get to `SU(3)`. Three problems, in increasing severity:
the Bring-cone instantiation is at `m = 1` where the tetraplectic condition is
*vacuous*; its output is `SU(2)`; and that `SU(2)` is already spent on
electroweak. Full detail in `qou-8p1g`.

**#6 "4-form degenerates".** Excluded, and cleanly — `qou-8p1f`. There is
nothing for the 4-form to degenerate *into*.

## Reading of the board

The two live routes are **#1 (native, weak)** and **#2 (strong, gated on
#3)**. If `qou-8p1j` fails to justify characteristic 2 on structural grounds,
#2 collapses into numerology and #1 is all that is left — at which point the
honest position is that colour is an **imported** symmetry and the corpus
should say so plainly.
