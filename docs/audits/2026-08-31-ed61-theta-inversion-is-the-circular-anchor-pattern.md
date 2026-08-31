# `qou-ed61`'s θ_K(A) inversion is the circular-anchor pattern, and the corpus already named it

**Date:** 2026-08-31 · **Beans:** `qou-ed61` (completed), `qou-qnnq` (in-progress),
`qou-gcmn` (todo) · **Scope:** (a) throughout. Nothing refuted, nothing wired, no
compute run.

Owner asked to try `qou-ed61`'s route. The answer came out of the corpus-grep
checklist rather than a probe, which is the cheapest possible outcome and is what
the formalize-first discipline is for: **the attack it proposes has already been
run, has already been found circular, and has an audit class and a scope document
written about it.** What survives is one non-circular quantity, and that is
blocked on a bean already open.

## The proposal

`qou-ed61`'s title (the bean has no body):

> the per-pair Coulomb unit may have the `S_K` FORM, not be a constant.
> `S_K(q₀) = A_ω · cuspModulus · (ln²q₀ − θ_K²)` with `A_ω = 3` exact/q-independent
> (Stokes symmetry constant, **proved**) and `cuspModulus = √3/4` proved — the
> knot-dependence is entirely in `θ_K = Im u_K`. … **Attack: invert the series to
> extract implied `θ_K` per mirror pair and check they are real/bounded/monotone.**

## 1. That inversion is already in the corpus, and is the reason an audit exists

`computations/qbeta/qbeta_t4_stokes3_crux_probe.py` fixes `A_omega = 3`, defines

```
theta2 = ln2_q0 - S/(A_omega * kappa)
```

at each anchor, and reports "both anchors yield real theta with correct
boost/spin dominance".

`content/pipeline/circular-anchor-audit.ts` was written **because of that probe**
and names it in its own history block. Its verdict:

> Recovering `A` from those `theta` returns 3 **by construction**; the cited
> "0.6% two-anchor consistency" is rounding in the 8-digit theta values, not
> independent agreement.

The detector class is `circ-anchor-inverted-roundtrip`: *"a module-level numeric
constant C is used in a denominator/inversion to DEFINE a derived quantity D, and
the file also reports C (or D) with confirmation language."* Full analysis:
[`docs/scope/2026-08-01-t4-anchor-circularity.md`](../scope/2026-08-01-t4-anchor-circularity.md).

**The mirror-series version is the same shape.** `θ_A` would be *defined* by the
residual, so "the residual drift may BE the θ_K(A) profile" is true for **any**
residual whatsoever. It is not a finding about θ; it is the inversion restated.

## 2. Two of the three proposed checks are provably vacuous

`QOU.QBeta.ThetaRealityBound` (sorry-free, on `main`) settles this in Lean, and
its own docstring says so:

| proposed check | what the Lean says |
|---|---|
| **real** | `thetaSq_nonneg_iff` — reality is **exactly** `A ≥ S/(κ·ln²q₀)`, a one-sided lower bound **on `A`**. It binds only where `S > 0`; where `S < 0` reality is automatic (`thetaSq_pos_of_neg`). So "the θ come out real" is a statement about `A_ω`, restated — not a measurement of θ. |
| **boost/spin dominance** (the T4 companion check) | `diagonal_crossed` holds for **every** `A > 0`. *"It is therefore not evidence for any particular `A`."* |
| **monotone** | `thetaSq_nonneg_mono` already characterises monotonicity in `A`; it is an identity, not data. |

So of the three, one is vacuous by theorem, one is automatic on half the data,
and the third is a known identity.

## 3. What actually survives — and it is blocked on `qou-gcmn`

Exactly one non-circular quantity comes out of the inversion:

> the **tightest lower bound on `A_ω`** supported by the mirror series,
> `max_A S_A/(κ·ln²q₀)` over the pairs with `S_A > 0`.

That is genuinely falsifiable and is not circular, because the bound's direction
comes from the Lean `iff` and the data are independent of `A_ω`: if the tightest
bound **exceeded 3**, `A_ω = 3` would be refuted by the mirror series.

It cannot be computed today. It needs a **per-pair `S_A` across the series**, and
`qou-gcmn` (todo) is precisely the statement that this does not exist:

> The per-pair Coulomb unit is held at its `A=3` `H_6` value across the whole
> `A = 3..41` series, so any `A`-dependence of the underlying strong bond is
> absorbed into `kappa` and is indistinguishable from the geometric factor under
> test. … This is the single biggest blocker.

So `qou-ed61`'s surviving residue is blocked on the same input `qou-gcmn` already
identifies, and running the inversion on the `A=3`-held unit would reproduce the
circularity rather than escape it.

## 4. A correction: `A_ω = 3` is **conditional**, and the bean records it as proved

`qou-ed61`'s title asserts `A_ω = 3` is *"proved"*. The corpus says otherwise.
[`mass-theory/aomega-fourone-dt-count.md`](../../content/quantum-observable-universe/mass-theory/aomega-fourone-dt-count.md)
opens:

> **Theorem (conditional on [`conj:stokes-dt-bps-bridge`]).** Under the
> closed-sector Stokes–DT–BPS bridge, the G3 Stokes integer of the figure-eight
> `4₁` is a BPS/DT count: `A_ω(4₁) = 3`.

and the corpus's own bibliographic QA records that the licensing step is
unsourced:

> the `5 ∉ {3,4}` exclusion licensing `A_ω = 3` rests on an **unsourced step** …
> The downstream `A_ω = 3` argument should carry that conditionality explicitly.
> — `content/bib-qa-verifications.json`

This is the **"conditional-proved ≠ premise-established"** failure AGENTS.md
carries a STRICT section on, sitting in a **`completed`** bean — the status a
later agent is most likely to read as settled. The bean is corrected in this PR.

## 5. Also worth knowing: `A_ω` is an overloaded symbol

`A_ω` in `computations/deltalambda/` is **`4√2·e^{−3/8} = 3.888`**, a Bridge
Stokes datum (`deuteron_wall_alien_resummation_probe.py`,
`deuteron_coupling_s00_probe.py`), **not** the `A_ω = 3` of the `qbeta` arc. Two
different objects under one name, ~0.9 apart. Same class as the `markovZ` /
`markovZC` / `markovZc` collision. Resolve any `A_ω` to its definition before
using its value.

## Verdict

`qou-ed61` as written is not a live route: the inversion is the documented
circular-anchor pattern, two of its three checks are vacuous by sorry-free Lean,
and its one non-circular output is blocked on `qou-gcmn`. Nothing here refutes
the `S_K` **form** — the per-pair unit may well be `S_K`-shaped; what is refuted
is that *this inversion* is evidence for it.

**Recommendation (judgement, not a finding):** leave `qou-ed61` closed with the
correction, and treat `qou-gcmn` — computing `B_pp` at higher `A`, or bounding its
`A`-dependence — as the actual prerequisite. It is the blocker for both this and
`qou-o6ml`.
