---
# qou-bid3
title: 'GAP: the two-nucleon energy scale alpha is ~2.7x too large, and that is now the only surviving direction'
status: completed
type: task
priority: normal
created_at: 2026-08-16T13:57:06Z
updated_at: 2026-08-16T15:15:49Z
---

Successor to qou-brg3, which closed the last two-nucleon repair route (T-odd
ribbon twist) on a framing-invariant floor. What that closure leaves standing:

**The measurement.** `B(T=1)+B(T=0) ≥ α·log 4` for any convex channel pair. At
α = E₀ = 4.1859814 MeV the floor is 5.8030 MeV; nature's two-nucleon total is
2.1510 MeV. Every interface-side repair is excluded (the floor is independent of
z, convention, offset, crossing assignment, framing, and normalisation ≤ 1), so
the only free object left in `B = −α log μ` is α.

**The requirement.** Satisfying the floor needs α ≤ 2.1510/log 4 = 1.5516 MeV,
i.e. E₀ is ~2.70x too large *for the two-nucleon sector*.

**Why this is a GAP and not a fit target.** Rescaling α to 1.55 to fit the
deuteron is exactly the move the anti-fit discipline blocks — α = E₀ is the
framework's derived energy quantum and feeds every other binding. Three honest
questions instead:

1. Is E₀ the right scale for a *two-nucleon interface* at all, or does the
   interface carry a derived fraction of it? A derived fraction ≈ 0.37 would be
   a result; a fitted one would not.
2. Does the same 2.70x appear in the many-body sum `B_sym`? If the A≥24 band is
   also over-bound by ~2.7x, this is one scale error, not a two-nucleon defect.
   If not, the two-nucleon channel is special and the floor argument does not
   generalise. **Measure this before theorising** — it is cheap and decisive.
3. Is the binding law `−α log μ` right? The floor is a consequence of the log,
   and a different functional form would not have it.

**Do not** propose an α-rescaling ansatz before (2) is measured. That is the
seventh-Δ_λ-ansatz failure mode in a new place.


## 2026-08-16 — CLOSED as stated. NEGATIVE: it is not one scale error.

The gate this bean carried ('measure whether the same 2.70x appears in the
many-body sum BEFORE proposing any alpha ansatz') has been run. Answer: no, and
the two constraints point in opposite directions.

Chain closed form vs AME2020 at the current alpha (production _bond_type_L,
convention D, proton pin — from collective_term_budget_probe):

    2H     1.27x OVER      12C    0.35x under
    3H     0.72x under     56Fe   0.33x under
    4He    0.31x under     208Pb  0.38x under

**The chain over-binds exactly ONE nucleus — the deuteron — and under-binds
every other by ~3x.** The sign flips between A=2 and A=3.

B_chain is LINEAR in alpha, so a uniform rescale moves every row together:

    two-nucleon floor  needs  alpha <= 1.5516 MeV
    many-body A >= 12  needs  alpha LARGER

At alpha = 1.5516 the 56Fe under-binding goes 3.03x -> 8.18x. **The admissible
interval for a uniform alpha is empty.**

So the 2.70x two-nucleon over-binding is NOT a global miscalibration of E_0. It
is specific to the two-nucleon sector, where the sign structure is also wrong —
the two defects are the same defect.

The gate earned its keep: proposing alpha ~ 1.55 to fit the deuteron would have
multiplied the many-body error by 2.7x somewhere the two-nucleon probe does not
look.

Scope-(a). Excluded: a UNIFORM alpha rescale. Not excluded: a channel- or
A-dependent alpha (a function, not a constant — strictly harder than what it
replaces); a binding law other than -alpha log mu; the many-body collective term
(R/alpha = 1.3240 per nucleon, mixed-sign in A), which is its own open item.

Probe: computations/probes/alpha_direction_two_sided_squeeze_probe.py
