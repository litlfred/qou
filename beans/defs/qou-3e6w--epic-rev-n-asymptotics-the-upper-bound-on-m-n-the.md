---
# qou-3e6w
title: 'EPIC: REV_n asymptotics — the upper bound on M_n (the deuteron-wall q-Borel gate)'
status: in-progress
type: epic
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-10-10T07:01:20Z
updated_at: 2026-11-18T07:54:48Z
parent: qou-10v9
blocking:
    - qou-v2om
---

Arc-level container created 2026-10-10 on owner instruction ("reorganize this Arc within
the bean reorg").  Before this, the arc had **no epic** and was split across two levels
of the 2026-10-04 reorg:

| bean | was | what it is |
|---|---|---|
| `qou-hok7` | `parent: qou-v2om` (EPIC: low-isotope binding defect) | the arc's whole ledger, 1,967 lines, ~20 session appendices |
| `qou-0ie7` | `parent: qou-10v9` (PROGRAM root, directly) | one of the arc's open sub-problems |

Measured: `qou-10v9` carries **~70 direct task children** alongside 8 epics, and `qou-0ie7`
is one of them — so the reorg gave the arc two parents at two different depths and no
place of its own.  `qou-v2om`'s five fronts (F1 deuteron overshoot, F2 the n=3 term, F3
cluster substructure, F4 derive `R(q,x)`, F5 indexing) are all about `B_sym` and the
binding functional; this arc is about the **growth rate of a partition sum**, which gates
one of them rather than being one of them.  Hence a sibling epic, with the gate recorded
as a blocking edge rather than as containment.

## What the arc is

`qou-hok7` opened (2026-08-21) as *"the classical Borel transform is the wrong transform
for the deuteron wall; the substrate object `Z_n(q0)` is q-Gevrey"*.  Its open step was
the q-Borel–Laplace resummation.  Two things then happened, both recorded in that bean:

1. **The resummation was already run** and is a scope-(a) negative (correction of
   2026-09-07) — so the open item stopped being "run it".
2. The question narrowed to the one object the resummation needs and nobody has:
   **an upper bound on `M_n`** — equivalently, whether `REV_n` (the free energy over
   partition shapes: energy = excess hook length, entropy = shape multiplicity) is
   `O(√n)`.

So the arc's headline problem is a combinatorial-analysis bound, and everything since
2026-09-13 has been infrastructure for it.

## What is settled (cite, do not re-derive)

- **`REV_n`'s `Θ(√n)` coefficient is `A√2`**, where `e_∞ = A` is a k-free constant (#7294;
  an earlier verdict of mine in #7286 was withdrawn).
- **`e_∞` is a sum of three k-free pieces** (#7335):
  `e_∞ = max over (s_t, s_b) of [ Xblock(s_t) + Xrun(s_t+s_b) + Xbot(s_b) ]`, value
  `2.43929645512078402706542884314` at `(8,8)`.
- **Two of the three pieces are closed forms in `q₀`** (#7349).
- **Gap G2 is CLOSED** (#7349, merged `05eaebd6b2f`): the top edge's maximum is *certified*,
  not searched — concave relaxation + supergradient certificate, `B_cert = 2.25373556700090488296611`,
  slack `6.43e-12`, and every admissible block length covered, cutting the window `90 → 27`.
- **The `(ℓ,W)` reduction is TIGHT** (#7081), so it is *not* where the slack is.
- **The staircase leg is closed form and its asymptotic is an identity** (2026-09-13).
- **`ℓ` is padding, not a search dimension** (a caveat of mine, withdrawn 2026-09-13).

## What is open

Four items, now one bean each (see children).  The honest summary:

- The join still rests on **G1** (`Xbot(s) ≤ Xblock(s)`), which is **neither proved nor
  refuted**, and which **no enumeration can settle** — a capped maximum is a *lower* bound
  on its own supremum, so it can only refute.
- The arc's strategy is therefore to **remove G1 from the argument**, not prove it: the join
  needs a finite window, and separate certified caps on the two edges give the same cut.
- **`REV_n`'s sub-linearity is MEASURED to `n ≤ 44`, not proved.** That is the headline.
- The data **cannot yet distinguish `√n` from `n^{3/4}`** (2026-09-07).

## The gate this arc is for

`--blocking qou-v2om`: the deuteron leg of the low-isotope binding epic needs the q-Borel
resummation of `Z_n`, whose convergence needs the `M_n` bound.  Recorded as an edge so the
dependency survives either bean being re-parented again.

## Discipline carried into every child

Proton-pinned; `mpmath` end to end, no float64 (probes are **not** exempt); the arc's probes
**execute** `rev_e_infinity_edge_limit_probe.py`'s committed evaluator rather than re-deriving
it, splitting on an asserted banner rather than a line number, so the object under test is
*the* committed one.  Every "refuted" is scoped (a)/(b) with the invariant named.

**Do not close this epic, and do not close `qou-hok7`** — its subject is an open conjecture.

## Round 84 Progress (PR #8393)
- Branch: `feat/round84-colourdisc-fixedratio-comptrace-zeroslope-equidcap-43c1`
- Commit 1 (code + probe): `02a557115ca6d2779725ccfdca969ee6ef80dff4`
- Commit 2 (witness): `f21ac2e565e6a27158e92746366f1616c0d9fd98` (`scriptSha256 = 930736b7600cb1fb1ca87062021ff390088ea82549e2ac7bf6e2fad10cdf9749`)
