# All of the c₃ anchor-dependence is in the `h·D → S` bridge, and the bridge changes sign

**Date:** 2026-08-19 · **Axis:** c₃ / Q_β bar-odd · **Tier:** scope-(a)
measurement of committed numbers · **Discipline:** no value derived, no `c_k`
wired, no fit, nothing bears on q₀ (forever-gated, `qou-eic1`).

## The question

`qou-qb8e`'s surviving one-line gate is *"the map from a bar-odd, anchor-blind
fibre-level object to an anchor-DEPENDENT number."* KC21 records `S = h·D(ũ)`
and the k=31 re-pin witness calls that relation *"schematic, not a tight
identity."*

**How schematic?** Both anchor evaluations are already committed, so this is
arithmetic, not research.

## The measurement

| | proton | muon | relative variation |
|---|---|---|---|
| carrier `h·D` | $-0.003486062405593$ | $-0.0034860636358261$ | $3.53\times10^{-7}$ |
| empirical `S` | $-0.0394593643$ | $+0.009682977798$ | $1.245$ |

Define the bridge as the quotient $B := S/(h{\cdot}D)$:

$$
B(\text{proton}) = +11.319, \qquad B(\text{muon}) = -2.778 .
$$

## Two things follow

**The bridge carries essentially all of the anchor-dependence** — $3.5\times10^6$
times more variation than the carrier. The ladder is blind to the anchor at the
$10^{-7}$ level, so any route hoping to explain the swing *from the ladder* is
looking where the signal provably is not.

**And it is not a mild factor: it changes sign.** So *"$S = h{\cdot}D$ up to a
factor"* understates the gap. No positive rescaling of the carrier — no
normalisation choice, no scalar convention — reaches `S` at both anchors.

## What this does not establish

`B` is a **quotient defined here**, not a decomposition anyone derived. Per
AGENTS.md §*"Defined residual ≠ derived decomposition"*, the three checks:

1. **Is the split empirically accessible?** **No.** There are exactly **two**
   anchors. Any 2-parameter family fits two points exactly, so `B`'s *form* is
   not constrained by this data. None is proposed, and fitting one would carry
   no information.
2. **Is the factor forced, or merely in range?** Merely in range — `B` is
   defined by division and its values are whatever `S` and `h·D` happen to be.
3. **Does the corpus carry a competing split?** The `S = h·D` relation is the
   corpus's own; this adds a measurement of the residual factor, not a rival
   decomposition.

## Why a negative-shaped result is the useful one here

The contribution is about **direction**, not content. It says where the
anchor-dependence is (entirely in the bridge) and, by the sign change, rules out
the cheapest class of explanation (a positive rescaling of the carrier). It says
nothing about what `B` is, and the two-anchor obstruction means this data never
could.

That obstruction is worth carrying forward: **more anchor-fitting is not a
route.** A third independent anchor, or a structural constraint on `B` from
outside the anchor data, is what would change the situation.

## Cross-references

- Probe: [`hd_to_s_bridge_anchor_dependence_probe.py`](../../computations/qbeta/hd_to_s_bridge_anchor_dependence_probe.py) (5/5, exit 0)
- Source of both anchors: [`qbeta-c3-qstar-k31-repin.witness.json`](../../computations/qbeta/qbeta-c3-qstar-k31-repin.witness.json) `data.carrier_anchor_blindness`
- The gate: bean `qou-qb8e` (read its two front-state corrections first)
- Registry: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) KC21
- Bean: `qou-qiw9`
