# Charge-symmetric strong + separate Coulomb — the light-nuclei binding benchmark

**Date:** 2026-07-11
**Branch:** `claude/charge-symmetric-coulomb-binding-2026-07-11`
**Compute:** [`computations/charge_symmetric_coulomb_binding.py`](../../computations/charge_symmetric_coulomb_binding.py)
**Witness:** [`computations/charge-symmetric-coulomb-binding.witness.json`](../../computations/charge-symmetric-coulomb-binding.witness.json)
**Payoff of:** #3564 + #3570 (mirror split is Coulomb). **Cross-refs:** #2089 (log-trace
kernel), #3548 (connected `(2,1)`/SU(4) mechanism, merged `9c62f785`).

## What was built

The #3564/#3570 diagnosis said: the mirror binding split is Coulomb, so the #2089
strong kernel (`f_pp=z`, `f_nn=z−h`) over-breaks charge symmetry ~3×; the fix is a
charge-symmetric strong bond + separate Coulomb. This benchmarks that fix on
D/T/³He/⁴He (`B = E₀·Σ_bonds log(1/f_bond)`, complete-graph bonds, `E₀=4.186 MeV`):

1. **broken** — #2089 kernel, no Coulomb;
2. **broken + Coulomb** — double-counts (the kernel already carries a spurious EM split);
3. **charge-symm + Coulomb** — all bonds = the isoscalar `f_pn`, minus canonical Coulomb.

## Result — the split is fixed (verified accuracy win)

| model | B(³H)−B(³He) | vs AME 0.764 |
|---|--:|--:|
| broken, no Coulomb | +2.271 | 3.0× |
| broken + Coulomb | +3.269 | double-counts |
| **charge-symm + Coulomb** | **+0.998** | **1.3×** |

Model (3) collapses the split to the Coulomb value — a ~3× accuracy gain and it removes
the EM double-count, exactly as the diagnosis predicted. The residual ~30% is the
uniform-sphere Coulomb over-estimate (see #3570), not charge symmetry.

## Honest boundary — the absolute magnitude stays open

| nuc | AME | charge-symm + Coulomb | err |
|---|--:|--:|--:|
| D | 2.225 | 3.890 | +75% |
| T | 8.482 | 11.671 | +38% |
| ³He | 7.718 | 10.673 | +38% |
| ⁴He | 28.296 | 22.436 | −21% |

The absolute binding is **not** closed — the fix corrects the *charge* structure (the
split), not the *magnitude*. D is over-bound, ⁴He under-bound; this is the edge-set /
`E₀` scale / connected-magnitude problem (#2089's "form bug"), unchanged by charge
symmetry.

## The remaining step — re-run #3548 on the charge-symmetric kernel

#3548 (merged) pinned the magnitude *mechanism* — the connected (Ursell/Mayer) part is
extensive, localized to the non-abelian `(2,1)` rep, gated by SU(4) `dim = C(4,A)`
(vanishes at ⁶Li, "right order of magnitude" at ⁴He). But it is **explicitly
no-fit/no-closure and still built on the charge-BREAKING kernel** (`g_ij = 1−f_ij` with
`f_pp=z`, `f_nn=z−h`). So its connected magnitudes carry the same spurious 3× CSB this
diagnosis flagged.

> **Actionable open step:** re-run #3548's connected-`(2,1)`/SU(4) magnitude probe on
> the **charge-symmetric** kernel (`f_pp=f_nn=f_pn` isoscalar) with Coulomb separated.
> That is the concrete path to the *absolute* binding — the charge structure (this PR)
> and the connected magnitude (#3548, re-run charge-symmetric) together.

## Verdict (scope-limited (a))

> Charge-symmetric strong + separate Coulomb is a **verified accuracy win on the mirror
> split** (0.998 vs AME 0.764, from the broken kernel's 2.27–3.27) — the diagnosis's
> prediction, realized. It is **not** a binding closure: the absolute magnitude (edge-set
> / connected `(2,1)`/SU(4)) is unchanged and still needs #3548's mechanism re-run
> charge-symmetric. No fit, no wiring.
