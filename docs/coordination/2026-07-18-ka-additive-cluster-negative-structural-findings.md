# k(A) additive-cluster derivation — scope-(a) negative + structural findings (bean qou-7uxa)

**Date:** 2026-07-18 · **PR:** #3875 · Different-context attack on GAP-A-3
(authorized parallel to #3808). Witness:
`computations/deltalambda/ka-additive-cluster-derivation.witness.json`
(`allPassed: false`, EXPLORATORY, no fit/BW/wiring; one a-priori anchor κ₂
fixed by the pure-2-body deuteron, consumed once).

## Verdict — scope-(a) NEGATIVE (constrains, does not close, the 3-cluster channel)

The per-knot-trace side does **not** supply k(A). Freezing the pairwise channel
to the merged Lean-grounded Mayer-b₂ bond-sum and reading off the connected-b₃
residual fails on **four independent grounds**:

1. **Magnitude / sub-extensivity.** μ_ext−1 is strongly *sub*-extensive in bond
   count (D 4.85/1 bond vs ⁴He 8.31/6 bonds), so the deuteron-anchored b₂
   bond-sum overshoots T/³He/⁴He by 4–5×; the residual is dominated by this, not
   by a clean 3-cluster.
2. **I-conn residual-mismatch.** The naive `1/(tr·tr·tr)` candidate is a product
   of 1-body traces ⇒ its connected cumulant ≡ 0 (fully disconnected, already
   inside the ceiling). The genuinely-connected joint-trace cumulant (full
   Mayer/Ursell, both 2+1 and 1+1+1 subtracted) is well-defined but the residual
   does **not** track it (C₃/b = −12.6 / −12.2 / +9.5; no single scale, sign flip).
3. **I-par bar-parity FAIL.** The connected cumulant is **not** bar-even (b₃ shifts
   −18.7%/−19.3%, b₄ −24.2% under q↦q⁻¹). Root cause: the **single-nucleon trace
   itself is bar-odd** at q₀ (+13.2%/+11.8%), so *any* cluster object built from
   raw tr_M carries bar-odd (p−n) content — the wrong channel for the bar-even
   absolute scale (cf. the `BarParityExclusion` I-2 gate on main).
4. **⁴He-max sign-flip.** No parameter-free connected-triple makes ⁴He the max:
   b₃(T), b₃(³He) > 0 but b₄(⁴He) < 0.

**Junk control (decisive):** the meaningless triple-*count* is *more*
self-consistent than the connected cumulant (spread 0.45 < 2.84) ⇒ the connected
cumulant does not beat junk. Only **A-locality** passes (C₃(D)=0 exactly).

## Structural findings to carry forward (for #3808's additive split)

- **b₃ is nearly isospin-blind and positive:** b₃(T) ≈ +0.9395 ≈ b₃(³He) ≈ +0.9515
  (the connected 3-body cumulant barely distinguishes T from ³He — the isospin
  split lives in the pairwise b₂ channel, consistent with the merged Mayer-b₂
  grounding, not in the 3-cluster).
- **b₄ is large and opposite-sign:** b₄(⁴He) = −2.2104. The b₃>0 → b₄<0 sign flip
  is a real constraint on any cluster ansatz for the channel.
- **Bar-parity obstruction:** raw per-knot tr_M(K) at q₀ is bar-odd, so the
  bar-even scale cannot be a cumulant of raw traces — a bar-even combination
  (e.g. tr_M(K)+tr_M(K̄) symmetrization) must be used first. This is the sharpest
  structural lead the negative produces.
- Joint pair traces are genuinely non-factorizing (connected 2-body cumulants all
  ≈ −0.6; diproton tr(pp)=0.5667, dineutron tr(nn)=0.2474).

## Disposition

Reported to #3808 (they own the additive-split derivation). Not fitted, not
wired. The productive next lead (if pursued): retry the cluster construction on a
**bar-even-symmetrized** trace so I-par can pass — the current negative shows the
raw-trace route is bar-parity-obstructed at the single-nucleon level.
