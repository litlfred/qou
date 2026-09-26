---
# sp10
title: 'D [independent]: burnside Sum(f^lam)^2=n! (DeltaLambdaSignRule.lean:292)'
status: completed
type: task
priority: low
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-09-26T11:03:23Z
parent: sp00
---

RSK bijection S_n ~ Sum_lam SYT(lam)^2, or {Wedderburn split sp07 + HLF sp09}. Mathlib has no RSK. Famous.

Parent: sp00.

## MEASURED COMPLETE 2026-09-06 (audit under `qou-1knw` follow-up)

Re-measured with `#print axioms` against freshly-rebuilt oleans. This bean was
`todo`; the declaration it tracks is proved.

`BurnsideDischarge.burnside_proved` —
`[propext, Classical.choice, Quot.sound]`, and `BurnsideDischarge.lean:110`
supplies the `BurnsideContext` instance from it, so
`DeltaLambdaSignRule`'s `ctx.burnside_claim` is discharged rather than assumed.

The bean said "Mathlib has no RSK. Famous." Both true and beside the point: the
corpus built RSK \*\*in-repo\*\*, ~48 `QOU/Mathlib/Schensted*` modules, and
`QOU.Mathlib.rskBurnsideHolds` proves `∑(f^λ)² = n!` unconditionally.
`burnside_proved` carries `[SnIsotypicSpechtSplit ℚ]`, which is inhabited — see sp07.
