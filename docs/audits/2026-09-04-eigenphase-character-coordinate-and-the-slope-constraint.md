# The Q_β eigenphase in the character coordinate: what the "802 fine-tuning signature" measures, and the constraint nobody was using

**Date** 2026-09-04 · **Bean** `qou-pdix` (S1 blocker) · **PR** #6572
**Probe** [`computations/qbeta/qbeta_eigenphase_character_coordinate_probe.py`](../../computations/qbeta/qbeta_eigenphase_character_coordinate_probe.py)
· **Witness** `computations/qbeta/qbeta-eigenphase-character-coordinate.witness.json` (3/3)
**Partially corrects** [`2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md`](2026-08-30-cds1-two-row-cap-admissible-set-exhausted.md)

## Summary

Three findings, in decreasing order of how much they change what to do next.

1. **The declared candidate basket is empty against a second constraint that
   was available all along.** Matching the ladder's phase requirement in the
   character coordinate `P := tr M = 2cos α` is two numbers, not one — a value
   and a slope — and every form the corpus has declared misses the slope by
   **21× to infinitely**, while sitting within 0.7 % on the value. The entropy
   bound that makes the value match uninformative does not apply to the pair.
2. **The "802 fine-tuning signature" is coordinate-dependent**, with an exact
   closed form. It is large because the phase is small, which is forced.
3. **Finding 2 does not rescue the `(z−1)h/2` family.** That exclusion rests on
   a second, invariant argument in the same witness. What changes is what it
   rests on.

## 1 · The setup, and why the coordinate matters

The committed ladder pins the eigenphase by inversion (`c₃ = 0`):

```
α_req = u/2 − arccos( Q_codata / (Q_A·(1 + c₂u²)) ),   c₂ = −1
```

At the proton pin `q₀ = 1.10997858275138…`, `α_req = −0.05235868351898296…`,
and `dα_req/dq = +41.53` (central difference, ±1e-4 relative in q).

The object a braid word actually produces is not `α`. It is the **character**
`P = tr M`, a Laurent polynomial in `q`; `α = arccos(P/2)` is derived from it
and is bounded in `[0, π]`. Two live results are both stated in the `α`/`z`
coordinate:

- the two-row-cap audit rejects the whole `α = (z−1)h/2` family on
  `z = 0.4991044802`, `dz/dq = +400.2896759`, **slope/value 802** — "a
  fine-tuning signature, not a derivation";
- `QOU.QBeta.BraidImageEigenphaseAlgebraic.coeffs_zero_of_surjective_nonpos`
  excludes any algebraic relation, by zero-counting — **for α surjective onto
  the non-positive reals**, which the unbounded `(z−1)h/2` family supplies and
  a bounded `arccos` does not. That hypothesis is worth reading before citing
  the theorem: "it is algebraic, therefore excluded" is not what it says.

## 2 · The 802 is coordinate-dependent

For any `α(q)` with `P = 2cos α` and `z = 1 + 2α/h`:

```
(z′/z) / (P′/P)  =  −2 / (h·z·tan α)  ≈  −2/(h·z·α)
```

Measured **369.74** against the closed form **365.76** — agreeing to 1.09 %,
and that residual *is* the dropped `2αh′/h²` term in `dz/dq`. The sign matters:
`α < 0` at every substrate anchor, so the leading minus is what makes the
inflation positive.

| coordinate | value | slope | slope/value |
|---|---:|---:|---:|
| `z = 1 + 2α/h` (the audit's) | 0.4991044802 | +400.29 | **802** |
| `P = 2cos α = tr M` | 1.997259194490263 | +4.3465 | **2.176** |

The factor is large **because α is small** — and α is small by construction,
since the ladder's correction to `Q_A` is a fraction of a percent. So
slope/value in the `z` coordinate cannot discriminate between candidate phases:
every candidate with a small phase carries the same inflation. This is exact
algebra, so scope-**(b)** for the claim *"slope/value is a coordinate-invariant
measure of fine-tuning"*, which it refutes.

The probe reproduces the audit's own `z` and `dz/dq` first (`z = 0.4991044802`,
`dz/dq = 401.60` against the recorded `400.29`, 0.33 % — the two central
differences use different step sizes), as a check that it is measuring the same
object rather than a lookalike.

## 3 · What this does **not** rescue

The `(z−1)h/2` family stays excluded. `qbeta-ladder-required-phase.witness.json`
records a second argument: `dα_req/dq = +41.53` against `dα_C/dq = −0.455`,
**opposite signs**, so the two curves cross transversally at `q₀` rather than
coincide — the 2.3e-5 rad agreement there is a point coincidence. A derivative
**sign** disagreement is invariant under this reparametrisation, so §2 leaves it
untouched.

Stated explicitly because the two are easy to conflate: §2 narrows *what the
exclusion rests on*, not the exclusion.

## 4 · The finding — the derivative empties the basket

`qbeta_d_frame_terminus_probe.py` is careful about its own value match: six
declared forms sit within 0.7 %, and it calls that "basket distance, not
isolation". That caution is correct **and it is a statement about matching one
number**. Testing the same six on both constraints:

| form | value miss | \|P′/P\| | vs required 2.176 |
|---|---:|---:|---|
| `2 − h⁴` | 0.042 % | 0.0331 | 65.7× too flat |
| `2 − h²/8` | 0.136 % | 0.0475 | 45.8× too flat |
| `2` (identity word) | 0.137 % | 0 | slope exactly 0 |
| `2 − 3h⁴` | 0.150 % | 0.0996 | 21.8× too flat |
| `χ^{(2,1)}(𝓑₃) = 2 − 3h⁴ − h⁶` | 0.154 % | 0.1018 | 21.4× too flat |
| `[2]_q = q + q⁻¹` | 0.683 % | 0.0937 | 23.2× too flat |
| `tr M_{4₁} = q⁴−2q²+1−2q⁻²+q⁻⁴` | 145.6 % | 1.7363 | 1.25× too flat |

Value alone separates the six by a factor 17. Log-slope separates the *same
six* by one to two orders and **empties the basket** — the least flat is 21×
off. The only form within 1.25× on slope is `tr M_{4₁}`, and its value is
`−0.911`.

The second constraint costs no experimental precision: it is a derivative of
the same committed ladder. So a derived candidate now has a two-number target:

```
P(q₀)      = 1.997259194490263      ± 1.14e-6   (5.7e-7 relative, from |c₃| ≤ 1)
|P′(q₀)/P(q₀)| = 2.176              (~4 figures)
```

**Precision, stated rather than implied.** `dα_req/dq` is a central difference
at ±1e-4 relative in `q`, inherited from the sibling probe, so `|P′/P|` is good
to about four figures. That is far more than a 21× discrimination needs, and
the *value* constraint is exact to the compute dps. A slope quoted to seven
digits would be a claim the central difference does not support. And `2cos` is
even, so `±α` give the same `P` and opposite `P′` — only `|P′/P|` is
branch-independent; the sign is not offered as a constraint.

## 5 · Scope

- §2 is scope-**(b)** for the coordinate-invariance claim: exact algebra.
- §4 is scope-**(a)**: it measures that no **declared** form passes. It does
  **not** prove that no Laurent polynomial meets the two constraints, and it is
  not a proposal for one — nothing here is fitted. `P` and `|P′/P|` are read
  off the committed ladder by inversion, exactly as the sibling probe reads off
  `α_req`, and the basket forms are the ones already declared in the corpus.
- Nothing here derives `α`. `qou-pdix` stays open.

## 6 · Two adjacent items found while measuring, not actioned

1. **Bean `qou-xjh4` (created 2026-09-03) is already false against `main`.** It
   asserts branch 3 is "the only remaining option" and "NOT ATTEMPTED, by
   anyone"; `0ed8fcbc61`, `4471ee72ce` and `f65a953dd3` are attempts that
   closed three named horns. It also attributes branch 1's exclusion to
   "transcendence over ℚ(q,z)" — the unproved docstring assertion the registry
   flags, rather than the zero-counting proof that exists.
2. **`qbeta_d_frame_terminus_probe.py:7-14` transfers the *mass* channel's
   two-row cap to the *decay* channel** ("DERIVED, not a ruling … so `z = z_D`
   is FORCED") and calls `qou-n1dj` resolved. That contradicts
   `QOU/QBeta/DecayFibreBarParity.lean`, whose sorry-free
   `threeRow_undetermined_by_decay` shows the decay pairing sees the weights
   only through `y_{(3)} − y_{(1³)}` and so cannot establish or refute the cap
   at any precision; it also contradicts the trace-convention registry and
   `qou-n1dj`'s own status (`todo`, "Item 1 is untouched"). The probe's headline
   verdict inherits the transfer.
