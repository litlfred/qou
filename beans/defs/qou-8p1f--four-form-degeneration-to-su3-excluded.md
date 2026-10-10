---
# qou-8p1f
title: "qou-8p1x/f: 'perhaps the 4-form degenerates' -> SU(3) — EXCLUDED by dimension count"
status: completed
type: task
created_at: 2026-08-07T12:40:00Z
updated_at: 2026-08-07T12:40:00Z
---

Parent: `qou-8p1x`. Tests the proposal that a tetraplectic / generic 4-form
degenerates down `Spin(7) -> G_2 -> SU(3)`.

## Result: it does not, and the count is decisive

`computations/form_stabilizer_genericity_su3_routes.py`, exact integers, all
checks pass.

| structure | dim `Lambda^k` | dim `GL(n)` | orbit | codim | generic? |
|---|---|---|---|---|---|
| `G_2` from a 3-form on `R^7` | 35 | 49 | 35 | **0** | **OPEN ORBIT** |
| `Spin(7)` from a 4-form on `R^8` | 70 | 64 | 43 | **27** | special stratum |

And the blunter fact: `dim GL(8) = 64 < dim Lambda^4(R^8) = 70`, so **no**
4-form on `R^8` has an open orbit at all. Four-forms in dimension 8 have
moduli; "generic 4-form" does not single out `Spin(7)` or anything else.

**So there is nothing for the 4-form to degenerate INTO.** Reaching `Spin(7)`
means imposing the Cayley form by hand — precisely the octonionic import the
route was meant to avoid, and one level *higher* than the status quo, since
`Spin(7)` contains `G_2`.

**Scope-(b)** for the specific claim tested, licensed by a dimension count.

## The constructive half

The same count says the generic-form route runs through **3-forms in dimension
7**, not 4-forms in dimension 8. So of the chain's two links, the upper one
fails genericity and the lower one — `G_2 -> SU(3)` via `S^6 = G_2/SU(3)` — is
untouched, and is already **eightfold open-problem item 3**. That is where
form-stabilizer effort belongs.

## Not excluded

* imposing a Cayley form by hand: consistent, just not a derivation;
* the `G_2 -> SU(3)` link;
* tetraplectic geometry generally — see `qou-8p1g` for the separate and more
  damaging `m = 1` observation;
* routes not going through generic-form stabilizers (`qou-8p1h`, `qou-8p1i`).
