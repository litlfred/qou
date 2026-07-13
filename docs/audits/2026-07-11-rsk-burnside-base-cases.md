# `#SYT(⊥) = 1` — salvaged base lemma (RSK first-swing, mostly subsumed)

**Date:** 2026-07-11 · **Axis:** s5-so3-keystone / Identity-I axiom (i) ·
**Trigger:** owner "genuine first swing at RSK" · **Not a closure. No fit.**

## What happened (corpus-grep discipline in action)

The first swing at the open RSK / Burnside identity `RSKBurnsideHolds n :
∑_{p⊢n} #SYT(p)² = n!` produced three sorry-free `n=0` base-case lemmas
(`numStandardYoungTableaux_bot`, `partitionShape_zero`, `rskBurnside_zero`). Before
merging, a corpus-grep found a **sibling had landed the far-stronger result on
main during the same session**:

- `PartitionsOfBridge.rskBurnsideHolds_le12 : ∀ n ≤ 12, RSKBurnsideHolds n` —
  proved via the sorry-free hook-length bridge `IdentityIHLFBridge.dimSYT_eq_dimHLF`
  + the `decide` certificate `dim_validated_le12`;
- plus an active RSK build (`SchenstedInsertion`, `SYTHookFormula`, `RSKBridge`,
  `SYTEnumerationBridge`, `YoungDiagramCorner`, …).

So `rskBurnside_zero` (just the `n=0` case) and `partitionShape_zero` are
**subsumed** — dropped rather than merged as redundant duplicates.

## What was salvaged

[`QOU/Mathlib/StandardYoungTableauBot.lean`](../../content/quantum-observable-universe/lean/QOU/Mathlib/StandardYoungTableauBot.lean)
— the one genuinely-distinct lemma:

- `numStandardYoungTableaux_bot : #SYT(⊥) = 1` — proved **directly** by
  `Subsingleton` + `Nonempty` on `StandardYoungTableau ⊥`, **without** routing
  through the FRT hook-length bridge the sibling `le12` proof uses. It is an
  independent, elementary computation of a `numStandardYoungTableaux` (a
  noncomputable `Nat.card`) of a concrete shape; `lean`-direct `EXIT=0`, axioms
  `[propext, Classical.choice, Quot.sound]`.

## Honest assessment

This tranche was largely **overtaken** by concurrent sibling work on the RSK
frontier (`n ≤ 12` done sorry-free). The single salvaged lemma is a small,
independent brick. The forward-looking action is to **coordinate with the RSK
build** rather than add parallel base cases; the general RSK correspondence remains
the open multi-session P1–P5 program. No fit, no scale, no physics.
