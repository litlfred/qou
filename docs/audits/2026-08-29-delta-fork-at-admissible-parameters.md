# The admissible-parameter route does not discriminate the Δ fork

`qou-bg3w` / `qou-99qc` / `qou-cds1`. **Scope-(a): a negative.** It decides
nothing, proposes no `c_k`, wires nothing — it closes off a route.

## Why this was worth measuring

[`ConventionDAdmissibleRoots.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ConventionDAdmissibleRoots.lean)
(sorry-free, `84489c2f5`) proves the `(1³)`-block weight numerator factors over
any commutative ring,

```
N(q,z) = (q²+1)z² − (2q³+q)z + q⁴ = (z − q)·((q²+1)z − q³),
```

so under convention D **exactly two** Markov parameters descend to the two-row
quotient: `z = q` (where `tr_M` is the augmentation) and `z = z_D = q³/(q²+1)`.
Its `one_not_root` proves `z = 1` is not a root on `1 < q <` the plastic number.

The coordinate sum `net` **is** `tr_M` at `z = 1`. So every comparison the Δ
fork has been argued at — `epsNPq = h²/2 − h` for the short element,
`delta_net = −0.188291` for the long one — sits at an **inadmissible**
parameter. The obvious next question is what the two elements do at the
admissible ones.

## The grid, completed

`Q_β = |tr_M^z(Δ)|·E₀` with `E₀ = m_e/(q(q−1)) = 4.185981363294476` MeV at the
proton pin, against `Q_NEUTRON_MEV = 0.7823334093099085`. Exact sympy over
`ℚ(q)`, `q → q₀` as an exact `Rational`, 60-dps mpmath readout — no float64.

| | `z = 1` (**excluded**) | `z = q` (augmentation) | `z = z_D` (Markov, D) |
|---|---|---|---|
| **Δ_S** — the NF vector | **+0.168 %** | +12.470 % | −43.157 % |
| **Δ_L** — the 11-crossing words | +24.776 % | **+39.324 %** | −15.451 % |

Symbolically, confirming #5897's affine/quadratic split independently:

```
tr_M(Δ_S)(z) = q²/2 − q·z − 1 + z/q + 1/(2q²)                    degree 1
tr_M(Δ_L)(z) = −(q−1)(q+1)(q⁴z² + 2q³z + 2q² − 2q·z + z²)/(4q³)  degree 2
```

`Δ_L`'s trace carries the factor `(q−1)(q+1) = q·h` explicitly — the same
bar-odd factor `Δ(net)` carries.

**Calibration, run before concluding.** Four of these six are already in the
corpus and all four reproduce exactly: `qou-99qc`'s three-row table
(`+0.168 %`, `+12.470 %`, `−43.157 %`, all on the NF vector) and
`qbeta-d-frame-trace-baseline`'s `−15.451 %` on the exhibited words. The two
**new** cells are the `Δ_L` row's `z = 1` and `z = q`.

## The result: it does not discriminate, and it removes an argument

`qou-99qc` observes that the two admissible functionals **bracket** `Q_β`, and
names the trap — *"the bracket means some convex combination hits Q_codata
exactly. That is a one-parameter fit against a single anchor."*

**Measured here: `Δ_L` brackets it too.** `[0.6615, 1.0900]` MeV contains
`0.7823`, exactly as `Δ_S`'s `[0.4447, 0.8799]` does. So bracketing is a
property of *both* elements and therefore evidence for **neither**. Any
argument of the form "the admissible values straddle the measured value"
applies verbatim to the model it was meant to exclude.

Nor does closeness discriminate. The best admissible cell in the whole grid is
`Δ_S` at `z = q`, **+12.470 %**; `Δ_L`'s best is **−15.451 %**. Both are two
orders of magnitude worse than the excluded `+0.168 %`. Choosing between +12.5 %
and −15.5 % on proximity to a single anchor is the one-parameter fit the bean
already refuses.

## What is actually established

- **The admissible-parameter route is closed as a discriminator.** It was the
  natural next measurement and it returns nothing. Recorded so it is not run
  again.
- **The `z = 1` near-hit is `Δ_S`-specific.** `Δ_L` at `z = 1` is `+24.776 %`,
  not a near-hit. So the famous `+0.168 %` is a property of the short element
  *and* the excluded functional together — neither alone.
- **`qou-99qc`'s central finding survives and widens.** *"The functional that
  reproduces the measured Q-value is precisely the one the canonical convention
  forbids"* is true on the short element and now also true in the sense that no
  admissible cell, on **either** element, comes near.

## What is NOT established

- Nothing about which element is canonical. `qou-bg3w` stays open.
- No claim that either element is refuted. Scope-(a): these are numbers at
  particular functionals, not an exclusion of an ingredient.
- The probe itself is not committed here. It extends
  `qbeta_delta_element_fork_pricing_probe` (PR #5897, unmerged) and imports its
  reduction; duplicating that machinery onto another branch would create a
  second copy of exactly the code whose divergence produced this fork. It
  belongs beside its parent once #5897 settles.
