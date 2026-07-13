# The two light-nuclei binding levers are decoupled — charge symmetry ⊥ connected magnitude

**Date:** 2026-07-11
**Branch:** `claude/connected-magnitude-charge-symmetric-2026-07-11`
**Compute:** [`computations/connected_magnitude_charge_symmetric.py`](../../computations/connected_magnitude_charge_symmetric.py)
**Witness:** [`computations/connected-magnitude-charge-symmetric.witness.json`](../../computations/connected-magnitude-charge-symmetric.witness.json)
**Completes:** the open step from #3575. **Re-uses:** #3548 (merged `9c62f785`,
`su4_connected_1111_magnitude_probe`).

## The question

The charge-symmetric + Coulomb benchmark (#3575) fixed the mirror split but left the
*absolute* binding open, and named the concrete next step: re-run #3548's connected
`(2,1)`/SU(4) magnitude probe on the **charge-symmetric** kernel (since #3548 built it
on the charge-BREAKING kernel). This does exactly that, re-using #3548's machinery.

## Result — the connected magnitude is charge-symmetry-invariant

| atom | A | C(4,A) | `\|b_Ac\|` broken | `\|b_Ac\|` symm | Δ% | need broken | need symm |
|---|--:|--:|--:|--:|--:|--:|--:|
| D | 2 | 6 | 0.6051 | 0.6051 | +0.00 | 1.000 | 1.000 |
| **⁴He** | 4 | 1 | **1.9614** | **1.9719** | **+0.53** | 2.093 | 2.120 |
| ⁶Li | 6 | 0 | 22.22 | 22.52 | +1.35 | 0.944 | 0.959 |

The irreducible connected cluster `b_A^c` barely moves under charge symmetry (⁴He
+0.5%) — it is a graph sum over the K_A interface cluster and hardly sees the p/n
composition. The needed super-pairwise ratio shifts only slightly (2.093 → 2.120), and
the SU(4) A=6 vanishing is unchanged. The ~74% magnitude gap persists.

## Verdict — the two open binding levers are orthogonal

> **Charge symmetry and the connected magnitude are decoupled.** #3548's magnitude
> conclusion (PARTIAL, ⁴He ~×1.5 delivered vs ×2.09 needed) is **robust** to charge
> symmetry — re-running it charge-symmetric does not close the magnitude gap.

So the light-nuclei binding factorises into two **independent** open levers:

| lever | what it fixes | status |
|---|---|---|
| **charge structure** (mirror split) | the p↔n / isospin asymmetry | **fixed** — charge-symm + separate Coulomb (#3564/#3570/#3575) |
| **connected magnitude** (×2.09 / edge-set) | the absolute super-pairwise scale | **open** — #3548's connected `(2,1)`/SU(4), unchanged by charge symmetry |

Absolute binding needs **both**, but neither is the other. This is a clean structural
separation of the remaining binding-closure problem: the charge-symmetry work (this
session's arc) and the magnitude work (#3548) do not interfere, and can be closed
independently.

**Scope-limited (a):** reuses #3548's canonical connected-cluster machinery + proved
SU(4) gate; no new fit; no wiring. Not a binding closure — it maps the remaining open
territory.
