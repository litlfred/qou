---
# qou-usol
title: 'Construct wedderburnEmbed: block-diagonal is constructive, only the RSK count needs Fin (n!)'
status: completed
type: task
priority: normal
created_at: 2026-09-05T16:47:01Z
updated_at: 2026-09-05T16:56:01Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Owner: "construct
wedderburnEmbed", following `qou-qb7p` which measured the opaque axiom's cost.

## Result: constructed, with the obstruction narrowed to one named identity

**The stated blocker was wider than the real one.** `Wedderburn.lean` deferred
on two grounds — "careful index arithmetic" and the RSK dimension identity. The
first is not a blocker at all: on the natural index type

    RegIndex n := Sigma (lam : Nat.Partition n), Fin (f^lam) x Fin (f^lam)

— the regular representation, `V_lam` with multiplicity `f^lam` — the
block-diagonal assembly is an ordinary `def`, and it is **injective**. RSK is
needed only to land in `Fin (n!)`.

`content/quantum-observable-universe/lean/QOU/HeckeAlgebra/WedderburnConstruction.lean`,
7 declarations:

| declaration | content |
|---|---|
| `blockDiagonal` | the assembly, constructed |
| `blockDiagonal_same` | the on-block read-off |
| `blockDiagonal_injective` | it is an **embedding**, not merely a map |
| `card_regIndex` | `Fintype.card (RegIndex n) = Sum_lam (f^lam)^2` |
| `RSKDimIdentity` | the one missing ingredient, as a `Prop` |
| `wedderburnEmbedOf` | the embedding into `Fin (n!)`, given RSK |
| `wedderburnEmbedOf_injective` | and it is injective |

## THE GATE THAT MATTERS

Every one of the seven reports

    [propext, Classical.choice, Quot.sound]

with **no `wedderburnEmbed`**. So the construction genuinely replaces the axiom
rather than wrapping it — which was the whole point, and it is checkable.

## The RSK hypothesis is NOT a new statement — cite the corpus's

`QOU.BraidKnot.OVTopAssembly.sum_numSYT_sq_eq_factorial` already carries it, and
its status is worth quoting exactly. `scripts/lean-axiom-guard.py` lists it
first as `sorryAx` under *"known-BAD: the RSK identity and everything reindexed
from it"*, then later as `clean` — with the guard's own warning that `clean` was
reached *"by moving its obligation into a class binder, which is the §3b-cond
pattern and is exactly what 'conditional-proved ≠ premise-established' warns
about"*, and was *"treated as a RED FLAG and checked three ways"*.

So the identity is available **only conditionally**. `RSKDimIdentity` states the
same obligation as an **explicit hypothesis on the theorem** rather than inside
an ambient class binder — which is precisely the distinction the guard is
complaining about. Discharging it here would additionally need the
`numSYT` <-> `dimSYT` bridge (`QOU/BraidKnot/SYTEncodingBridge.lean`); that is
its own work and is not attempted.

## 🛑 A stale-snapshot finding, and why the statement looks the way it does

`blockDiagonal_injective` takes positivity as an **explicit argument**
(`hpos : forall lam, 0 < seminormalDim lam`) rather than invoking it. Current
source proves it unconditionally — `Hoefsmit.seminormalDim_pos'`, added
2026-09-03 — but **this container's restored olean snapshot predates that
change**: it carries only the older `seminormalDim_pos`, which needs a `0 < n`
hypothesis the statement does not (the empty diagram has one standard tableau).

Bolting `0 < n` on to satisfy a stale cache would have put a decoy hypothesis in
a shipped statement, in a repo with a `lean-decoy-hypothesis-audit.py`. Naming
the real hypothesis instead keeps it honest and verifiable here; the caller
discharges it in one line against current source. **This is a live instance of
the lean-verifier memory's TRAP: `lean`-direct exit 0 certifies against the
oleans ON DISK, which after a restore are a snapshot.**

## Two incidental defects, both fixed

- `Wedderburn.lean`'s module doc advertised `wedderburnEmbed_posSemidef`
  ("block-diagonal-of-PSD-blocks is PSD on the whole"). **No such theorem exists
  in the file.** The claim is removed rather than left standing.
- Its "Open Lean port" note is now marked partly superseded, pointing at the
  construction.

## Follow-up

Delete `opaque wedderburnEmbed` in favour of `wedderburnEmbedOf`. Its only
remaining references are two doc comments in `MarkovTrace.lean`, so the change
is small — but it removes the unconditional form, which is a deliberate scoping
decision and belongs in its own change rather than smuggled into this one.
