---
# qou-1dnr
title: Derive c_3 EXACTLY (as q-lift recursion output / Berezinian even-odd cross-term B·D⁻¹·C) -> Q_beta 100x target (c_4·u^4 already < 7.8ppb); the single concrete 1ppq gap-closer
status: in-progress
type: task
priority: normal
created_at: 2026-07-20T16:02:13Z
updated_at: 2026-07-20T16:35:36Z
---


## 2026-07-20 — DM-cubic/Berezinian route: scope-(a) NEGATIVE (commit e52279df)
Both CODATA-independent 3-jet realizations (categorical phase ∂³F; Berezinian cross-term B·D⁻¹·C from H_3 super-period matrix, even={3,111} bar-even / odd={21} bar-odd) are anchor-invariant to ~1e-5%; empirical c_3 swings 2.43% (dc_3/dq≈3.8e6 — the 1/u³ ladder inversion of a smooth zero, KC21). A smooth real-q construction (dc_3/dq=O(1)) structurally cannot track it → matches at most one anchor, here NEITHER (phase 3-jet +0.027 vs empirical −2.07). Re-confirms Lean-proved KC20 (real-q/quadratic excluded), KC21, KC22 (odd channel resurgent/non-holonomic — task approach #1 'read c_3 off the q-lift recurrence' refuted a priori). Q_β does NOT meet 100× via this route; nothing wired; c_3 stays EMPIRICAL/REFUTED-as-real-q. Lean QOU.Mass.QbetaC3DMCubic (sorry-free falsification thms + open ResurgentBarOddC3 class). Bean STAYS OPEN: genuine target is the resurgent bar-odd S=h·D(ũ), not a real-q c_3.



---
**Habiro-element / fibre-level route (parallel to q-lift/DM-cubic) — NEGATIVE** (2026-07-20, branch `claude/argument-principle-residue-sum-2026-07-20`, commit 8cd22c81; owner 2026-07-17 parallel-attack directive).

The **formal**-Habiro-element route to c_3 is **refuted as a class** (scope-b, Lean sorry-free). The Q_β ladder g(u)=Σc_k u^k is **GEOMETRIC** (simple pole at u_substrate, finite radius, c_{k+1}/c_k→1/u≈117.409; KC8/PR#1713/#1727), whereas any formal Habiro element's q=1/Ohtsuki expansion is **GEVREY-1** (radius 0 — the KC22 class the *binding* D(ũ) lives in). Disjoint growth classes ⇒ the c_k are **not** formal-Habiro/Ohtsuki coefficients. Surviving object = the **analytic simple-pole residue** (argument-principle); its c_3 near-match **swings ~2.9% cross-anchor** (proton −2.0693 / muon −2.0097) ⇒ FAILS anchor-invariance ⇒ **fit, not derivation**. No new c_3 derived; Q_β residual unchanged.

**Converges with the q-lift route:** c_3 closure, if any, is an **analytic** statement at real q₀ (Φ_b axis, qou-9lot / PR #3540), NOT a formal Habiro element — this result explains WHY every formal-Habiro attack (C14/C15/C16/C17) failed.

Lean: `QOU/Mass/QbetaC3Habiro.lean` (`geometric_not_superGeometric`, `qbeta_ck_not_formal_habiro`, `simplePole_coeff_geometric`). Probe: `computations/probes/qbeta_c3_habiro_growth_dichotomy.py`. Audit: `docs/audits/2026-07-20-c3-habiro-route.md`. **Bean kept in-progress** (route negative, not the whole c_3 goal).



## 2026-07-20 — GGM colored-Jones / resurgence (Stokes) route: scope-(a) NEGATIVE (commit 6f3ab3f2)

Parallel-independent attack (distinct from DM-cubic + Habiro siblings), on the
RESURGENT bar-odd target the DM sibling pointed to. Falsifiable two-anchor test
of "c_3 = order-3 Stokes coefficient": the GGM order-3 Stokes datum for 4_1
(integer constant -3 on the Vol(4_1)/pi singularity; S+_11 tower eq 61, certified
in qbeta-g3-ggm-stokes-41) IS the right TYPE (anchor-invariant: tower swings
6e-6% across the 11.5-ppb proton/muon pins) but its VALUE is not c_3. As c_3,
-3 -> 576 ppb Q_beta residual (74x the 7.8 ppb 100x target), WORSE than the -2
near-match (43 ppb); off ~45% from cal c_3 ~ -2.069. Substrate-meridian Stokes
jump 10^-27 suppressed (dladder-fibre-branch). The extracted-c_3 swing is 1/u^3
ladder hyper-sensitivity, NOT the obstruction (smooth Habiro form swings 6.2 ppb).

VERDICT: c_3 is NOT a bare GGM Stokes constant. scope-(a) NEGATIVE, narrows the
route to the OPEN normalized §4e quantum-modularity / 3d-index bridge (NOT a
scope-(b) exclusion of the Stokes route). No fit; nothing inverted from Q_beta;
no c_k wired; no tier change. Lean QOU.Mass.QbetaC3Stokes sorry-free
(stokesInt_strictly_worse_c3_than_nearMatch + constantStokesDatum_* + open
NormalizedStokesC3Bridge class, no instance). audit 2026-07-20-c3-stokes-route.md.
Bean STAYS OPEN: genuine target is the normalized/resurgent bar-odd datum, not a
bare integer.
