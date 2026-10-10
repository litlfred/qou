---
# qou-8lxd
title: 'EPIC: eightfold way / SM derived from QOU'
status: in-progress
type: epic
priority: high
tags:
    - 8f-index
created_at: 2026-08-03T23:27:15Z
updated_at: 2026-10-10T07:18:30Z
parent: qou-0uga
---

## Reorganisation 2026-10-04

Now the epic for P4.SM under SM / eightfold way and physics scope.

---

## Index — written 2026-10-10

Entry point for the P4.SM arc. This body was **empty from 2026-08-03 to
2026-10-10**: the 2026-10-04 reorg parented 149 beans here and left no index, so
the arc had 117 open children and no way in. Parent `qou-0uga`; sibling
`qou-ddmn` (physics-claim scope audits).

**149 children — 117 todo, 30 completed, 2 scrapped.** Every one of the 117 is
now tagged with exactly one `8f-*` front, so each front is a single query:

```
beans list --tag 8f-mass --ready        # startable items, one front
beans list --parent qou-8lxd --ready    # everything startable
```

`--ready` excludes blocked and in-progress, so it *is* the chip-away list.

### What this epic is, and is not

**Is:** deriving the classical eightfold way (flavour `SU(3)` multiplets, GMO,
the decuplet relations, the octet/decuplet decompositions) and the
Standard-Model parameter set from QOU's categorical substrate.

**Is not:** a claim that any of it is derived. Per PR #4640's honesty pass, most
of the chapter's representation theory is tier **standard** — correct and
correctly applied, and true of *any* `SU(3)`, so **not evidence for the
framework**. Keep that register when adding to any front.

### Fronts

| tag | ready | front |
|---|---:|---|
| `8f-flavour` | 15 | Flavour `SU(3)`, `N = 3`, the flavour Cartan (G1-opt1..4), Bring structures. **The arc's gate.** |
| `8f-lean` | 15 | Lean scaffolds owed, vacuity/self-assuming projections, opaque carriers, float64 in `close_321_weinberg_gap.py`. |
| `8f-colour` | 13 | Colour `SU(3)` action and its construction routes (sub-epic `qou-8p1x`). |
| `8f-mass` | 10 | SM mass gaps: `m_u/m_d`, `m_s/m_c`, `m_b/m_t`, `m_tau`, neutrinos, `m_H`, the lepton tower. |
| `8f-ew` | 9 | Electroweak: `sin^2 theta_W`, Weinberg angle, vev `v`, Higgs mechanism, hypercharge `Y = B - L`, CKM + PMNS. |
| `8f-gen` | 7 | Three generations, chirality grading, what excludes `T(2,9)`. |
| `8f-qcd` | 7 | Gluon flux tube (G2-opt1..3), lattice QCD from QOU, partition-function unification. |
| `8f-lit` | 7 | Literature + the four P4.SM queues (cite / cross-check / prove-lean / remark-interpreting). |
| `8f-tseries` | 5 | `T2`–`T6` derivation spine: hypercharge via ribbon twist, twist multisets, root-of-unity freeze-out, no-free-parameter certificate. |
| `8f-atomicity` | 5 | The `qou-atsd` T0-T6 chain (`dim V = 2` crux, `Sp` rank, the hard Tannakian Mathlib gap). |
| `8f-arch` | 5 | Chapter architecture. Ch. `eightfold-way` **exists and is wired**; the restructure is owner-gated. |
| `8f-decide` | 4 | Owner decisions and owner questions. Nothing here is agent work. |
| `8f-obs` | 3 | Observational cross-checks (kilonova Sr II, Reticulum II, actinide cosmochronometry). |

### Suggested order

1. **`8f-lean`** — 15 items, mechanical, each independently landable, no research
   risk. Scaffolds, vacuity defects, one float64 producer. Cheapest real shrink.
2. **`8f-lit`** — 7 items, mostly the four queues; drains fast and unblocks
   citations other fronts need.
3. **`8f-decide`** — 4 items, zero agent effort, and `qou-j3w6` gates
   `8f-flavour`. Ask before doing flavour work.
4. **`8f-tseries`** then **`8f-colour`** — the research spine and the one front
   where several routes are already excluded, so the survivors are known.
5. **`8f-mass` / `8f-ew` / `8f-gen` / `8f-qcd`** — these are the 26-parameter gap
   map. Most are blocked on `8f-flavour` or `8f-colour` landing first; read the
   individual bean before starting, several say so explicitly.

### The gate, stated once

**`qou-j3w6` — owner decision, asked 2026-09-03, dismissed, still open.** Every
single-fibre route to flavour `SU(3)` is closed by a proved invariant. The
missing object needs `Λ³W = 1`, which condition 5 (`Λ²V = 1`, `N = 2`) forbids
for `V`. Options A (keep `N = 2`, add a second fundamental `W` — recommended in
the bean) / B (weaken to epimorphism — breaks the convention-D forcing chain, 10
consumers) / C (top-power `Λ^N V`, forces the multi-universe picture) / D
(nothing). Frame: `docs/audits/2026-09-03-eightfold-axiom-5-decision-frame.md`.

**Default if unanswered: D. Nothing changes and `8f-flavour` stays parked.**

Why it binds: `QOU/Eightfold/RowCapObstruction.lean` proves sorry-free that at
`N = 2` the alternating channel `dim V_(1³) = C(N,3)` **vanishes** — no singlet,
hence no `8 ⊕ 1` and no `η′`, for **any** `q`. Scope-(b), invariant cited
(the Schur-Weyl row cap). It excludes `N = 2` from *hosting* the decomposition;
it says nothing against a route that produces `N = 3`.

### Verified state of the chapter (2026-10-10, post-rename paths)

`folio/quantum-observable-universe/eightfold-way/` — **16 blocks, 9 sections**,
wired at `quantum-observable-universe.ts:97`. All of §1–§8 exist, which is why
five Phase beans (`lsij`, `8mgu`, `wvao`, `o7o9`, `v2aa`) were closed in this
pass with their evidence appended.

Still in place and **owner-gated**, not undone: `appendix-standard-model/` and
`brings-surface/` (**181** blocks). PR #5023 states the 8 → 4 restructure
"needs author sign-off", so `qou-akee` and `qou-ywsk` are deferred.

### Hygiene rules for this arc

- **Tag every new bean** with its `8f-*` front and set `parent: qou-8lxd`.
  Untagged beans are invisible: a title-grep for `eightfold|8-fold` finds 27 of
  these 149, and the seven beans PR #4640 spun out (`8pl1`, `8pl2`, `8pl3`,
  `mrel`, `sym2`, `sgd1`, `tup9`) contain neither word. **Never scope this arc
  by title-grep.**
- **`beans` rejects a `parent` on a `milestone`.** `qou-vwu9` sits detached by
  schema, not oversight, and is linked from here instead.
- **Session beans are ephemeral.** Four (`a0gr`, `cl94`, `1qug`, `nc56`) sat
  `in-progress` for 5-9 weeks, one of them holding `qou-d7h1` — the arc's
  largest open item — as a child. All four are now closed.
- **Re-verify on `folio/`, not `content/`.** The tree was renamed
  (`content/` → `folio/`, `.beans/` → `beans/defs/`). An earlier pass of this
  cleanup measured a checkout 1245 commits behind and got two numbers wrong in
  opposite directions: `brings-surface` read 176 (is **181**) and `uploads/`
  read 23 (is **10**, i.e. the ingest queue *drained*, it did not grow).
- Per AGENTS.md rule 13a, **nothing whose subject is an open conjecture was
  closed here.** The five closures are all mechanical, each with its evidence.
