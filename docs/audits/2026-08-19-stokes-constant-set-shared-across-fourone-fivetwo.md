# The Stokes constant set `{3,4}` is SHARED by `4₁` and `5₂` — what that prunes, and the discriminating `6₁` prediction

**Date:** 2026-08-19 · **Bean:** `qou-xpgq` (parent `qou-qnnq`, G3 Stokes
keystone / internal-derivation leg) · **Branch:** `claude/agent-reorientation-gap-1753rs`
**Tier:** scope-(a) measurement + candidate pruning · **Discipline:** no fit,
no `c_k` wired, nothing to production, no tier change, `qou-qnnq` stays OPEN.
**Probe:** [`qbeta_qnnq_stokes_constant_set_crossknot_probe.py`](../../computations/probes/qbeta_qnnq_stokes_constant_set_crossknot_probe.py) — 7/7, exit 0, exact integer arithmetic.

## The gap this closes

The internal derivation of `A_ω = 3` is the named open leg of `qou-qnnq`, and
the [2026-08-02 symmetry-constant-target audit](2026-08-02-aomega-internal-derivation-symmetry-constant-target.md)
§3 sets the bar precisely:

> Single-knot count-matching (`#boundary-parabolic connections = 3`, `π/3`
> dihedral, **braid index 3 / crossing number 4**) is a **coincidence trap**
> unless shown *across knots* AND *structurally forced* (`5₂`'s geometric
> block is `3×3`, different).

That paragraph pairs *braid index 3* and *crossing number 4* as a single
untested candidate. They are separable, and the corpus already holds the datum
that separates them — it had been read for its matrix **shape**, not its
**constants**.

## The observation

`5₂`'s Stokes sandwich is certified exactly against GGM's printed (96/97)
factorization, whose constants are `{3,4}`
([`qbeta-g3-5two-stokes-sandwich.witness.json`](../../computations/probes/qbeta-g3-5two-stokes-sandwich.witness.json),
check K1). `4₁`'s eq-98 off-diagonal spectrum is the pair `{3,4}`
([`aomega-qzero-dt-count.witness.json`](../../computations/aomega-qzero-dt-count.witness.json),
q→0 anchor Lean-proved in `QOU.QBeta.StokesQZeroDTCount`). So:

| driver | `4₁` | `5₂` | same? |
|---|---|---|---|
| crossing number | 4 | 5 | **NO** |
| #boundary-parabolic connections | 3 | 4 | **NO** |
| geometric block size | 2×2 | 3×3 | **NO** |
| **braid index** | **3** | **3** | **YES** |
| **Stokes constant set** | **{3,4}** | **{3,4}** | **YES** |

The `−9` in `S⁺(0)_{32}` is `3·3`, a composite entry of the product — not a
fourth elementary constant.

## What it prunes (scope-(a))

The constant set does **not** move between the two knots. Any quantity that
**does** move therefore cannot index it:

- **Crossing number is pruned.** 4 → 5 across the pair; `{3,4}` does not
  become `{3,5}`. This is the half of the flagged pair that dies.
- **#boundary-parabolic connections is pruned *as the index of the constant
  set*.** 3 → 4 (certified in `qou-btvl`: `4₁` = 2 irreducible + abelian,
  `5₂` = 3 + abelian). **This does not touch R1's `DT_max = #connections`
  handle**, which is a claim about a different quantity — do not read this row
  as refuting R1.
- **Geometric block size is pruned** on the same argument (2 → 3).

Scope note per AGENTS.md: these are **(a)** scope-limited negatives about what
can *index* the constant set. No invariant forbids these quantities from
appearing elsewhere in the physics, and none is claimed to.

## What survives — a CANDIDATE, explicitly not a derivation

A braid-index-indexed reading survives both points. The natural QOU-categorical
object at the braid index `n` is the Wedderburn decomposition of `H_n(q)`:

$$
(\#\text{blocks},\ \textstyle\sum_\lambda \dim V_\lambda) \;=\; (p(n),\ I(n)),
$$

with `p(n)` the partition count and `I(n)` the involution count of `S_n`
(Frobenius–Schur; the probe verifies the identity from hook lengths for
`n = 2…6`). At `n = 3`: partitions `(3), (2,1), (1³)` with dims `1, 2, 1`, so
the pair is exactly `(3, 4)`.

**This is not a derivation and is not asserted as one.** Two knots of equal
braid index cannot force a rule; the AGENTS.md bar is "across knots **AND**
structurally forced", and the forcing half is absent. `qou-qnnq` stays open.
What has changed is that the candidate is now *falsifiable at a specific,
already-wanted datum*.

## The discriminating test — and it is the datum the corpus is already chasing

`qou-btvl` records `6₁`'s independent resurgence DT count as **the** missing
piece of the third-knot test (its A-polynomial L-degree is certified: geometric
4, full 5). `6₁` has **braid index 4** and **#connections 5**. The two live
candidates disagree there:

| candidate | prediction for `6₁` |
|---|---|
| R1 — `DT_max = #connections` | a **5** |
| Wedderburn at the braid index | the pair **{5, 10}** |

The **10** is the discriminator: R1 does not produce it, and `p(4) = 5`,
`I(4) = 10`. Obtaining `6₁`'s Stokes constants therefore now decides between
two readings rather than merely adding a data point.

## Incidental (recorded, not fixed here)

`scripts/precision-gates.sh --changed` is green. Its no-free-parameter
certificate reports exactly **one** untraceable literal on the canonical
prediction path — `A_omega = 3` at
[`qbeta_t4_stokes3_crux_probe.py:60`](../../computations/qbeta/qbeta_t4_stokes3_crux_probe.py) —
i.e. this very open leg is the single un-derived number the certificate cannot
trace. That is an argument for the priority of `qou-qnnq`, not a defect in the
probe.

## Cross-references

- Beans: `qou-xpgq` (this), `qou-qnnq` (parent, open), `qou-btvl` (cross-knot DT data), `qou-rtec`.
- Audits: [`2026-08-02-aomega-internal-derivation-symmetry-constant-target.md`](2026-08-02-aomega-internal-derivation-symmetry-constant-target.md), [`2026-08-01-ujmw-aomega-dt-index-derivation.md`](2026-08-01-ujmw-aomega-dt-index-derivation.md), [`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`](2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md), [`2026-07-14-g3-stokes-via-3d-index.md`](2026-07-14-g3-stokes-via-3d-index.md).
- Primary source: Garoufalidis–Gu–Mariño, *Peacock patterns and resurgence in complex Chern–Simons theory*, [arXiv:2012.00062](https://arxiv.org/abs/2012.00062) (eq 59a/60/65/96/97/98) — held at [`library/arxiv-2012.00062v3`](../../library/arxiv-2012.00062v3).
- AGENTS.md §"Before declaring 'refuted'"; §"Before declaring 'open'"; §"Axiomatization is NOT a Proof".
