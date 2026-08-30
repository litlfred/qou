# cds1: the two-row cap cannot produce a D-frame ladder — the admissible set is exhausted

**Date:** 2026-08-30 · **Bean:** `qou-cds1` (§"Remaining piece") · **Scope: (a)**

## What this closes

`qou-cds1` recorded the two-row cap as the one piece not yet folded in:

> *"WenzlWeightVanishing.lean landed 2026-08-16 (sorry-free, all n; z_D is Wenzl
> level r=2 exactly) … Under D the ≥3-row blocks are annihilated, so χ_(1,1,1)
> drops from the H_3 decomposition. NOT folded in yet."*

It is now closed as a route, and **without running a search** — which is what the
bean's own Discipline section demands.

## The argument

The cap is the condition `y_(1³) = 0`. Its admissible set is **proved complete**
by `qou-06wh` (`ConventionDAdmissibleRoots.lean`, sorry-free, any `Field`):

    N(q,z) = (q²+1)z² − (2q³+q)z + q⁴  =  (z − q)·((q²+1)z − q³)
    admissible_markov_param_iff :  N(q,z) = 0  ↔  z = q  ∨  z = z_D

Verified symbolically here: `y_(1³)(z_D) = 0` **exactly**, and nonzero at `z_C`.

So the cap does not merely *permit* `z_D` — it permits **exactly two** bases, and
only `z_D` had ever been phase-tested. Testing the other one exhausts the set.

## Measurement (proton anchor, 50 dps)

    alpha_required = -0.052358683519      window (|c3| <= 1) = +/- 1.09189e-5

    z_C   sqrt(q)/(q+1)     alpha = -0.0523361202682    2.07 windows
    z_D   q^3/(q^2+1)       alpha = -0.0404857773406    1087.37 windows
    z=q   2nd admissible    alpha = +0.0114960776856    5848.10 windows

`z = q` is not merely far — it has the **WRONG SIGN**. The required phase is
negative; `z = q` gives a positive α. That is a qualitative exclusion, not a
magnitude shortfall, and it does not depend on the window's exact width.

## Result

**The two-row cap cannot produce a viable D-frame ladder in the
`α = (z−1)h/2` form.** The admissible set is closed (proved) and both of its
members are excluded (measured, 1087 and 5848 window-widths).

This **strengthens** the prune already in `qou-cds1`, which established that
`z_D` fails and inferred the one-parameter class was pruned. The prune is now
**exhaustive over the admissible set** rather than resting on one member — and
that is the stronger statement, because the cap was the only structural
constraint that selected members of that class in the first place.

## Scope — read before citing

- **Scope (a).** This excludes the two-row cap *as a route to a D-frame ladder in
  this functional form*. It does **not** exclude convention D, and it does not
  exclude a D-frame ladder derived some other way.
- It is consistent with, and does not supersede, `qou-cds1`'s finding that the
  **functional form must change**. It removes the last structural candidate for
  keeping the form.
- **Neither frame's α is derived** — that finding of `qou-cds1` is untouched. C's
  closeness remains a transversal crossing of two curves with different
  q-dependence, not a functional identity.

## What this does NOT license

Do not read "both admissible bases fail" as licence to search for a third. The
admissible set is **proved** to have exactly two members; a third base would have
to come from dropping the two-row cap, which is the constraint under the ruling.
Searching outside it for a value that lands near the required phase is a fit.
