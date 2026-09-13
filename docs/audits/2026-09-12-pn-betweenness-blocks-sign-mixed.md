# 2026-09-12 — The pn letter is an average, so the sign-mixed pattern is unreachable by construction

**Branch:** `claude/pn-betweenness-blocks-sign-mixed-2026-09-12` · **Beans:** `qou-q8vl` (narrowed), `qou-brng` (open)

## The question this answers

Bean `qou-q8vl` (PR #7226, on `main`) establishes two facts about the production
`A = 3` chain and then names one thing open.

The facts. A positive three-body Ursell coefficient needs **exactly one** bond
factor above `1` — the chain's Ursell function is the product `g_01 · g_12`, whose
sign is invariant under flipping both factors, measured byte-identical at
`-0.293278112721` for ³H. And the sign-mixed assignment that *also* gives the
correct two-nucleon spectrum — unlike pairs bind, like pairs do not — is the one
with the pn bond opposite to both like-pair bonds. Since `B = -α·log μ > 0` iff
`μ < 1`, that pattern is

$$\mu_{pn} > 1 > \mu_{pp}, \qquad \mu_{pn} > 1 > \mu_{nn},$$

i.e. `μ_pn` is the **strict maximum** of the three.

The open item, in that bean's own words: *"a THIRD bond family that supplies the
sign-mixed pattern by derivation"*. Its exclusions of the two known families are
at the **value** level — production letters by `d ≤ 0`, isospin projectors by the
identity `μ₊ + μ₋ = 1`.

## The finding

**The pn letter is not an independent third value. It is defined as a colour-weighted
average of the pp and nn letters, and an average is never an extremum.** So the
required pattern is unreachable for *every* `q` and *every* admissible colour
weight, whatever the numerical values.

Two hypotheses, both identities rather than measurements:

1. **Averaging.** `d_pn = (½ + δ/4)·d_pp + (½ − δ/4)·d_nn`, weights summing to one
   and both strictly positive for `δ ∈ (−2, 2)`. This is what "averaged interface"
   means in `atom_braid_word_3A`.
2. **Affineness.** The two-strand interface law is `μ = z + d`. An affine map carries
   a convex combination to the same convex combination.

Together: `μ_pn` is a strict convex combination of `μ_pp` and `μ_nn`, hence strictly
between them, hence never their strict maximum.

## Why this is not the same as the `d ≤ 0` exclusion

The value-level argument pins the current definitions: at today's offsets no letter
exceeds `1`, so no bond is attractive. A third family could in principle answer that
by moving letters above `1`.

The betweenness argument says moving values is not enough. **A third bond family
must break the averaging of the pn letter, or break affineness of the interface law.**
Those are the only two hypotheses used, and neither mentions `q`, `δ`, or any
numerical value. That is a narrowing of the open question, not a closing of it.

## Lean (sorry-free)

[`QOU/MassTheory/PnBetweennessBlocksSignMixed.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/PnBetweennessBlocksSignMixed.lean),
generic `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`, no `ℝ`:

| declaration | statement |
|---|---|
| `combo_not_gt_both` | a strict convex combination never strictly exceeds both endpoints |
| `combo_not_lt_both` | nor falls strictly below both |
| `affine_preserves_combo` | `z + combo w a b = combo w (z+a) (z+b)` |
| `pn_not_strict_max` | hence the pn bond factor is never the strict maximum |
| `signMixed_impossible_of_combo` | hence `signMixedPattern` is unreachable |
| `signMixed_impossible_corpus` | the instance at the corpus weight `w = ½ + δ/4`, for `δ ∈ (−2, 2)` |

`lean -DautoImplicit=false -s 65536`, exit 0, zero warnings, zero `sorry`. `#print axioms`
on all six: `propext` / `Classical.choice` / `Quot.sound` only (`affine_preserves_combo`
is `propext` / `Quot.sound`).

## Probe

[`computations/probes/pn_betweenness_blocks_sign_mixed_probe.py`](../../computations/probes/pn_betweenness_blocks_sign_mixed_probe.py)
— 8/8, exit 0, 70 dps, proton pin, convention D, mpmath end to end, no float64.

| check | result |
|---|---|
| `d_pn` is the convex combination, 8 values of `δ` | residual `0.0`, exact |
| affineness carries it to `μ` | residual `0.0`, exact |
| `μ_pn` strictly between, 9 values of `δ` | holds at every one |
| `μ_pn` never the strict maximum | holds at every one |
| betweenness off the pin, 5 values of `q` × 3 of `δ` | holds at all 15 |
| any letter above `1` at the proton pin | none — consistent with the `d ≤ 0` exclusion |
| sign-mixed pattern reachable | no |
| **control:** pattern reachable once `μ_pn` is set freely | **yes** |

The control is the load-bearing row. It shows the exclusion is carried by the
averaging hypothesis and not by the particular values: unpin `μ_pn` from the average
and the pattern becomes satisfiable immediately.

## Scope

**Scope (b), structural exclusion.** Invariant: strict convexity of the averaged pn
letter together with affineness of the two-strand trace. Both are identities.

**Not claimed:** that no third bond family exists. Only that any such family must
break one of the two named hypotheses. The binding magnitude (`qou-brng`) is
untouched; nothing here is wired to production, and no route was ranked by residual.
