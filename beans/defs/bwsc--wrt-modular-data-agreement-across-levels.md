---
# bwsc
title: 'bwS0-closure: WRT=modular-data agreement across enough roots (OPEN)'
status: in-progress
pr: 8298
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T00:30:00Z
updated_at: 2026-11-17T10:22:30Z
parent: qou-o9ge
---

Parent: bws0. OPEN. Need bwS0(zeta_N) = d_{zeta_N}(lambda)/D for enough levels N to exceed the
value-map polynomial degree (n=5 blocks: max mark-6 => degree 5 in t, so need >= 6 distinct fibre
points, N >= 7). #4365 supplies only the Sigma(2,3,5) slice (2 flat connections). The full antecedent
is the Habiro root-family agreement — the WRT invariant equals the modular datum at each fibre root
across levels. Route: extend the LR/WRT amplitude identity to Sigma(2,3,q) / colored levels, OR use
Habiro's unified-WRT root-family evaluation (habiro2008: bwS0 evaluated at each root = level-N WRT).
This is the Habiro-injectivity content (#3681). Feeds `KeystoneHabiroRootFamily.eq_of_root_family_agreement`.


---

## Corrected 2026-09-03 — the degree premise is false, and level 6 suffices (PR #6459)

This bean sets the obligation at `N >= 7` by the reasoning *"max mark-6 => degree 5 in t, so need >= 6 distinct fibre points"*. **The premise is wrong**, and the corpus already held the counter-value in `KeystoneWLambdaContinuation.block_dims_explicit`.

The mark-6 block is `d((3,1,1)) = [5] + 1 = t^4 - 3t^2 + 2` — the A5-split `3 + 3'` signature — **not** `[6] = t^5 - 4t^3 + 3t`.

| | value at `t = 2` | degree |
|---|---|---|
| `d((3,1,1)) = [5]+1` | 6 | **4** |
| `[6]` | 6 | **5** |

They agree at `t = 2`, which is what the mark *names*, and are different polynomials. Reading the mark as an index into the quantum integers is what put a degree-5 block into the `n = 5` list; there is none. `KeystoneN5ValueMapRigidity` had already *computed* the four degrees as `0, 3, 4, 4` — this bean's `n5_degrees_lt_six` bound was chosen to match the six level-7 fold points rather than the polynomials, so the discrepancy sat in plain sight.

**Max degree 4 => five points suffice => level `N = 6` closes the `n = 5` case.** Five fold points `2cos(k*pi/6)`, `k = 1..5`. That is one root fewer and one level lower than the standing obligation — a strictly smaller demand on the open WRT = modular-data agreement, which is what this bean is actually about and which is **unchanged and still open**.

### The lower bracket was not about the number two

`KeystoneHabiroInfiniteRigidity.two_roots_insufficient` brackets from below at 2. The sharp form is `no_finite_root_set_suffices`: **without a degree bound no finite set of roots suffices at all** — the same one-line witness `V + prod_{s in S}(X - s)` works for any finite `S`. That is precisely why `bwsd`'s dissolution had to go through the *infinite* family rather than a larger finite one.

With the measured degree bound the bracket then closes exactly: four roots fail, five succeed. Five is the threshold, not a sufficient-but-unsharp count.

### What is NOT changed

The residual content of this bean — that the gauge row `bwS0` actually agrees with the value map at those roots (WRT = modular-data), of which `KeystoneLRAmplitudeReal` (#4365) supplies the `Sigma(2,3,5)` slice — is untouched and still open. Only the price moved.

Landed in `QOU/BraidKnot/KeystoneN5LevelSixSuffices.lean`: `lean`-direct exit 0 (5/5, no warnings), `#print axioms` clean on all eight declarations.


## Round 58 Update (PR #8298)
- **Status:** `in-progress` (PR `litlfred/qou#8298`, head `92f8a80b907a40e6db76eb1a8a85f081c5960913`, Commit 1 `df446885b17718b4f18e584a2765ba2e802adb68`).
- **Lean 4.24.0 Modules:** `folio/quantum-observable-universe/lean/QOU/BraidKnot/N5LevelSixRootThresholdAndThreeLinkTriad.lean` and `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoSaddleHessianAndFourOneStokesCrossCheck.lean` (`0` `sorry`, `0` `axiom`, `0` warnings, `0` advisories across all 5 static audits).
- **80-dps Probe & Witness:** `computations/probes/round58_n5_level_six_ohtsuki_thimble_fourone_stokes_dilog_probe.py` and `computations/probes/round58-n5-level-six-ohtsuki-thimble-fourone-stokes-dilog.witness.json` (`allPassed: true`, `0` raw `float64`).
