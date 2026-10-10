---
# qou-s82c
title: Unify the two YekutieliTriple modules (GroupWithZero R vs R_q = Z[q,q-1])
status: completed
type: task
priority: normal
created_at: 2026-08-15T23:26:00Z
updated_at: 2026-08-16T01:57:08Z
---

## DONE 2026-08-15 — unified, and the blocker dissolved

The two modules declared byte-identical `YekutieliTriple` structures differing only in coefficient ring (`Torsion`: `ℝ`, then `[GroupWithZero R]` after the §7c port; `LiftingDescent`: `R_q = ℤ[q,q⁻¹]`). Now there is **one definition, instantiated twice**.

### The blocker was in the wrong place

The recorded obstacle was that `R_q` is a `CommRing` whose non-monomial elements are not invertible, so it cannot satisfy `[GroupWithZero R]`. True — but **the structure never needed inverses**. Its body is data plus one non-degeneracy field (`twoMorphisms p ≠ 0`), which requires only `[Zero R]`. Only `cechDeviation` and `TwistedTwoCocycle` invert, and they ask for `[GroupWithZero R]` separately.

So the fix was to *weaken the structure*, not to restate the deviation division-free or move to `R_qˣ`. No mathematics had to change.

| | before | after |
|---|---|---|
| `QOU.Torsion.YekutieliTriple` | `[GroupWithZero R]` | **`[Zero R]`** — the minimum its body uses |
| `QOU.LiftingDescent.YekutieliTriple` | separate `structure` over `R_q` | `abbrev … := QOU.Torsion.YekutieliTriple R_q M` |

`LiftingDescent` gains `import QOU.Torsion.YekutieliTriple`. No import cycle: `Torsion` imports nothing from `LiftingDescent`, and nothing in `LiftingDescent` imported `Torsion` before.

### Compile-verified (lean-direct-cone, never `lake build`)

| module | result |
|---|---|
| `QOU.Torsion.YekutieliTriple` | `ok=1, err=0` |
| `QOU.LiftingDescent.CosimplicialCrossedGroupoid` | `ok=1, up-to-date=15` |
| `QOU.LiftingDescent` (chapter aggregator) | `ok=1, up-to-date=20` |
| `QOU.Torsion.YekutielijTriple` (compat aliases) | `ok=1, up-to-date=15` |
| `QOU.Archimedean.HyperbolicVolumeTranscendence` | `ok=4, up-to-date=31` |

The `cosimplicial_crossed_groupoid_exists` proof still goes through unchanged — it builds a triple literal `⟨n, id, fun _ => 1, fun _ => 1, fun _ => one_ne_zero⟩`, which now elaborates against the generic structure at `R_q`. Gates: orphan `exit=0`, vacuity `exit=0`.

### Still open, unchanged

`cechDeviation`'s `g_ik⁻¹` remains `GroupWithZero`-only, so the *deviation and cocycle* layer still cannot be stated over `R_q`. That is the genuine remaining question (division-free restatement, or `R_qˣ`) — but it no longer blocks sharing the triple itself, which was the actual duplication.
