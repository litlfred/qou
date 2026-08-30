---
# qou-6vu3
title: The count channel's canonical carriers sit exactly on the b3 = 0 locus
status: completed
type: task
priority: normal
created_at: 2026-08-30T14:50:54Z
updated_at: 2026-08-30T14:50:54Z
---

Tests `qou-brng`'s **surviving route** — `QOU.Mass.BrunnianBindingChannel`'s
unsigned count channel — against the number `b₃` pins it to. It fails, and the
way it fails is specific enough to be useful.

## The result

Write `μ = ½(n₊+n₋)` for a carrier's count multiplicity, so its binding is
`s·μ·h` with `h = q − q⁻¹` and `s` the MeV scale. Then `b₃ = s·h·(μ_t − 3·μ_p)`,
which vanishes **iff `μ_t = 3·μ_p`** — the pair-local condition, so
`CrossingModelPairLocality.b3_eq_zero_of_pairLocal` applies.

**The canonical carriers satisfy it exactly:**

| carrier | `n₊` | `n₋` | `μ` |
|---|---|---|---|
| deuteron, Hopf clasp | 2 | 0 | **1** |
| A = 3, Borromean `L6a4` | 3 | 3 | **3** |

and `3 = 3 · 1`. So the count channel predicts **`b₃ = 0`** against a measured
`b₃/b₂ = 0.6411239316`. **The miss is total, not partial.**

**The scale cancels** (`b3_over_b2_eq`): `b₃/b₂ = μ_t/μ_p − 3` involves neither
`s` nor `h`, so this is zero-parameter — no reparametrisation and no choice of
`q₀` rescues it.

This is the same degeneracy `BrunnianBindingChannel`'s sub-question-1 answer
states for general `A`: *"one coordination unit per bonded pair, `C(A,2)` for a
cluster"* is `μ(A) = C(A,2)·μ_pair`, pair-local by construction. It is also the
second site of the defect already recorded against
`CoordinationBinding.BondExtensiveBinding` in `qou-w6vh`.

## A negative I nearly reported and had to withdraw

The first thing that suggests itself is a **quantisation obstruction**: `μ` is a
half-integer, the required ratio `μ_t/μ_p = 3.6411239316` is not, so no carrier
can work. **That argument is wrong** and is recorded here so it is not
re-attempted. It silently assumes `μ_p = 1`. With `μ_p` free, small half-integers
get close:

| `n(pair)` | `n(triple)` | `b₃/b₂` | rel err |
|---|---|---|---|
| 14 | 51 | 0.642857 | **0.270 %** |
| 11 | 40 | 0.636364 | 0.742 % |
| 17 | 62 | 0.647059 | 0.926 % |

I also computed the exact-match counts (`n_pair = 1483044`, `n_triple = 5399947`)
and they are absurd — but that is an **artifact of the quoted AME digits**, not a
physical statement, so it proves nothing either. Both dead ends are in the probe's
caveats.

## What this actually establishes

**The count channel is not obstructed — the carrier assignment is what fails.**
That makes the remaining burden *sharper*, not lighter: the channel has ample
freedom, so two free crossing integers matched against one measured ratio is a
**fit**. A carrier that reaches `b₃` earns nothing unless its crossing numbers are
**derived**. That is exactly `qou-brng`'s open item, now stated as a one-line test
(`carrier_must_break_three_to_one`): *any* replacement must break `μ_t = 3·μ_p`.

## Scope — (a), and it excludes no ingredient

The count channel survives. `brunnian_binding_survives` is untouched, and the
Brunnian mechanism remains the only thing that lets binding exist at `lk = 0` —
which was the point of the route and is not in question. What is excluded is that
**these two carriers with this channel** reproduce `b₃`.

Note the two carriers are of **different types**: the deuteron is a clasp and is
**not** Brunnian (`Vol = 0`, 2026-08-29 owner ruling), while `L6a4` is. That is
what makes the exact 3-to-1 coincidence a coincidence rather than a theorem — and
it is why a derived carrier assignment could in principle escape.

## Artifacts

* `QOU/Mass/CountChannelCarrierLocus.lean` — 7 declarations, sorry-free,
  `lean`-direct exit 0, axioms `[propext, Classical.choice, Quot.sound]`.
* `computations/probes/count_channel_carrier_locus_probe.py` — 5/5, exact
  `Fraction` arithmetic for every ratio, zero free parameters in the verdict.

## Related

`qou-brng` (the parent), `qou-w6vh` (pair-locality, the theorem this leans on),
`qou-82mc` (the convexity dichotomy), `qou-bsfg`.
