---
# qou-onfk
title: 'Promote bond saturation to a model parameter: f(type, coordination) as the natural relaxation'
status: in-progress
pr: 8295
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T06:48:03Z
updated_at: 2026-10-04T15:22:14Z
parent: qou-v2om
---


Opened 2026-09-04. The natural relaxation of the scalar bond constant, and the
owner's pick to push alongside the tower test (`qou-oooq`).

## The idea

The current model is `L = sum over bonds of f(type)`, a per-type scalar. Every
obstruction found in `qou-mu1h` and `qou-bygw` follows from that shape:
additivity makes `B` linear in `Z` for the chain and convex in `Z` for all-pairs,
and in both cases the maximum sits at an endpoint. The relaxation is

    f(type)  ->  f(type, coordination)

so the bond constant depends on how many neighbours the pair already has.

## Why this one and not the others

**It is already half-measured.** `all_pairs_bonds_and_saturation_probe` found
that a long-range bond delivers only a fraction of its isolated value once the
adjacent bonds are present:

| configuration | marginal / isolated |
|---|---|
| far p-p | 0.659916 |
| far p-n (ppn) | 0.650555 |
| far p-n (pnn) | 0.640829 |
| far n-n | 0.625186 |

The saturation is **flavour-dependent**, which is exactly the freedom the
convexity obstruction needs, and it is **non-linear in Z**, which is what breaks
the endpoint-maximum result. Promoting it to a model parameter invents no new
machinery; it names something already measured.

## The obvious objection, recorded up front

This is a fit wearing a measurement's clothes. The saturation numbers are real,
but turning them into `f(type, coordination)` means introducing a function with
no derivation — precisely the move this probe series has refused elsewhere. If
it is taken, it must be taken with that stated, and the derivation owed.

- [ ] Re-measure saturation at 200 bits. The existing numbers are float64
      (`np.asarray(m, dtype=float)` in the saturation probe), which is forbidden
      by `docs/precision-goals.md` and was the subject of the `qou-wx83`
      remediation. Do this FIRST; the whole bean rests on these four numbers.
- [ ] Check whether a coordination-dependent `f` can produce an interior maximum
      in `Z` at all, or whether saturation is too weak to overcome the
      `-1.747` MeV/proton drift.
- [ ] If it can: does it survive the `A = 2` test, where coordination is 1 and
      `f(type, 1) = f(type)`? At `A = 2` this relaxation reduces to the model
      already falsified in `qou-mu1h`, so it CANNOT fix the two-body inversion.
      That is a hard ceiling on what this bean can deliver and it should be
      stated before any effort goes in.
- [ ] Derive the saturation, or concede it is fitted.
