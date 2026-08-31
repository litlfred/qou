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

`z = q` is not merely far — it has the **WRONG SIGN**, and that exclusion has a
form needing **no anchor, no window and no numerics at all**:

    alpha = (z - 1)*h/2  with  h = q - 1/q > 0  for all q > 1
    =>  alpha < 0  <=>  z < 1

The required phase is negative, so the form **forces z < 1**. And `z = q > 1`
for every `q > 1`. So `z = q` is excluded structurally, for the whole substrate
range at once — the 5848-window figure above is an illustration of it at one
anchor, not the argument.

    z_C = 0.4993203342  < 1   admissible by sign
    z_D = 0.6126880371  < 1   admissible by sign
    z=q = 1.109978583   > 1   EXCLUDED

This is the stronger statement and is what should be cited: the two-row cap's
admissible set has exactly two members, and one of them cannot satisfy the
form's own sign requirement at any q > 1.

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

---

# Addendum: the two-constraint filter — what any candidate `z` must satisfy

The exclusion above is a *sign* argument. There is a sharper one, and it prunes
the whole family rather than its two admissible members. It is stated here so the
next tranche can test a candidate **before** running any search, per the bean's
Discipline section.

## The filter

`α_required` is measured at two anchors that share their experimental input
**exactly** — `Q_codata_MeV = 0.78233340999999999999999999999999` for both — so
the difference between them is a genuine `q`-derivative and not a confound
between two experimental values. That was checked, not assumed.

    alpha_required(q0)      = -0.052358683519
    d(alpha_required)/dq    = +41.388615        (secant over the two anchors)

Imposing both on `α = (z−1)·h/2`, `h = q − 1/q`:

    z(q0)   = 1 + 2*alpha/h                     =   0.4991044802
    z'(q0)  = (slope - (z-1)*h'/2) * 2/h        = +400.2896759

## What the candidates give

| | `z(q₀)` | `z′(q₀)` |
|---|---|---|
| **required** | **0.4991044802** | **+400.2896759** |
| `z_C` | 0.4993203342 | −0.01172370089 |
| `z_D` | 0.6126880371 | 1.046577629 |
| `z = q` | 1.109978583 | 1.0 |

## Reading

**`z_C` matches the VALUE to four decimals and misses the DERIVATIVE by a factor
of −34,144**, sign included. That is the "transversal crossing" `qou-cds1`
already reported, now quantified: the two curves agree in position at `q₀` and
disagree in slope by four and a half orders of magnitude.

**For constant `z` the two constraints are outright contradictory.** Matching the
value needs `z ≈ 0.4991`; matching the slope needs `z = 46.69`, which would give
`α = +4.78` — wrong sign and ~91× too large.

## The prune this supplies

A viable `z` must sit at **≈ 0.499** while having derivative **≈ +400**. No
rational function of `q` of the kind the corpus uses behaves that way near `q₀`
without a near-pole or a steep engineered feature sitting exactly there — which
is a fine-tuning signature, not a derivation.

So this is independent evidence for `qou-cds1`'s existing conclusion that **the
functional form must change**: the problem is not that the wrong `z` was picked,
it is that no well-behaved `z` can carry a slope two orders of magnitude above
its own scale.

## Scope

Scope-(a), and it is a **filter, not a refutation**: it says what a candidate
must satisfy, and that the natural candidates fail. It does not prove no `z`
exists. A candidate presented in future should be checked against **both** rows
of the table above — passing the value alone is what `z_C` already does, and is
not evidence.

## Red-team of the filter's own load-bearing number

The slope above is a **secant over `dq = 1.29e-8`, from exactly two points**. Two
points cannot distinguish a derivative from an artifact, and the whole ×34,144
claim rests on it — so it was checked before being left in place.

`α_required` has a closed form (`qbeta_eigenphase_branch_and_barodd_projection_probe.py:91`):

    alpha_required = -arccos( Q_codata / (Q_A * (1 - u^2)) )

with `Q_A` and `u` functions of `q`. Reconstructed independently and
differentiated exactly:

    witness secant (2 anchors)   41.388615
    my secant (same 2 anchors)   41.31873053
    my EXACT derivative at q0    41.31853588

Three routes, agreeing to **0.17 %**. The slope is a genuine derivative.

**Caveat on the reconstruction, stated rather than hidden:** my `α_required`
sits a *constant* −0.004259 from the witness at BOTH anchors, so my `Q_A` or
`m_e` differs slightly from the producer's. A constant offset leaves the
derivative intact — which is why the slopes agree while the values do not — but
it means the absolute figures here are the witness's, not mine. Quote the slope
as **≈ +41.3–41.4**, not to six digits.

**Smoothness**, exact derivative at increasing offsets from `q₀`:

    q0        41.31853588
    q0+1e-8   41.31883786
    q0+1e-6   41.34876716
    q0+1e-4   44.71506597

Slowly varying near the anchor; the two-anchor secant is a fair estimate.

**Independent corroboration of a separate `qou-cds1` claim.** At `q₀ + 1e-3`
(~0.09 %) the reconstruction returns a COMPLEX α (`0.0 − 0.0384j`) — the arccos
argument has left `[−1,1]`. That reproduces, from a different direction, the
bean's note that *"past ±0.1 % in q the ladder has no real phase at all"*. Two
independent constructions landing on the same window is worth more than either
alone.
