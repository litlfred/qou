# M4 mass table — magic-shell correction reveals Coulomb bottleneck

**Date:** 2026-05-16
**Branch:** `claude/post-662-c3-chain-anti-staleness`
**Builds on:** [M2](2026-05-16-m2-mass-table-cos-q-beta.md) (cos Q_β), M3 (full N=4 chain)

After wiring the full N=4 categorical Q_β chain (which closes the
Q_β residual to **+17.7 ppb** — Story B confirmed) we found the
mass-table per-atom residuals were unchanged at ~0.19 % MAE.
This is because Q_β enters mass only through `binding_T1` and
`binding_T5` — small contributions. The dominant residuals are
**structural in T1–T4**, not Q_β precision.

M4 tests adding the interface-type-resolved magic-shell coupling
correction (from PR #656's v6 probe) to the binding energy.

## Result

```
 iso   M_codata    M_pred (n4)   err_n4 ppm   Δ_coup MeV   M_pred (M4)   err_m4 ppm
   p    938.272      937.597      −720           0.000      937.597        −720      (unchanged)
   n    939.565      938.747      −872           0.000      938.747        −872      (unchanged)
   D   1875.613     1875.582      − 16           0.000     1875.582        − 16      (unchanged)
   T   2808.921     2814.157     +1864          +7.622     2806.534        −850      ↘ 2.2× better
 ³He   2808.392     2801.527     −2444          +5.481     2796.047       −4396      ↗ 1.8× WORSE
 ⁴He   3727.379     3747.302     +5345         +13.175     3734.128       +1811      ↘ 3.0× better

MAE:                              1877 ppm                                  1444 ppm   (1.30× improvement)
```

## Headline finding — Coulomb bottleneck

**³He gets worse** under the magic-shell correction. The
interpretation:

- ³He has $M_{\mathrm{pred}}$ **lower** than CODATA (over-bound),
  but Δ_coup adds **more** binding — wrong sign.
- T (mirror partner: 1p + 2n) has $M_{\mathrm{pred}}$ **higher** —
  needs *more* binding; magic-shell correction works correctly.
- ⁴He (Z=N=2): the interface-asymmetry term vanishes
  (n_pp − n_nn = 0); only the H7a piece [A−2]_q·E_0·log(1/h)
  contributes; closes to ~1800 ppm (3× better).

**Diagnosis**: ³He = 2p + 1n has **proton–proton Coulomb
repulsion** absent from the categorical 6-term formula. The
Markov-trace algebra (Wedderburn / Hoefsmit / Frobenius
selection) is per-irrep, with no continuum Coulomb. T has no
protons to repel → the categorical 6-term + magic-shell closes
its residual. ³He's residual is **dominated by Coulomb**, not by
the substrate magic-shell coupling.

## Why ³He's pattern wasn't predicted by the categorical model

The interface-type-resolved formula was derived from the F2 / #656
anchors *which are categorical Δ_cat differences*, not CODATA
masses. The κ slope fit on categorical anchors absorbs the
Z↔N asymmetry of the magic-shell coupling. But for
CATEGORICAL-vs-CODATA closure, additional **Archimedean** physics
is needed:

1. **Coulomb repulsion** ∝ Z(Z−1)/A^(1/3) — classical continuum effect
2. **Symmetry energy** ∝ (N−Z)²/A — captured partially by the
   categorical magic-shell? not fully
3. **Pairing correction** — for ⁴He, the doubly-magic structure
   is captured; for odd-A nuclei T, ³He extra structure

## Path to closing the mass-table residual

The 1 ppb mass-table closure now decomposes:

| component | category | status | candidate fix |
|---|---|---|---|
| Q_β | categorical | ✅ +17.7 ppb (full_chain_n4) | done (Story B) |
| T binding | categorical | ⚠ +1864 → −850 ppm (M4) | magic-shell + sign tuning |
| ³He binding | **continuum** | ❌ +2444 → −4396 ppm (M4 made worse) | **Coulomb term needed** |
| ⁴He binding | mixed | ⚠ +5345 → +1811 ppm (M4) | magic-shell + Coulomb + pairing |
| p, n binding | substrate | −720 / −872 ppm | m_p chain closure (#663) |

Recommended next:

1. **Add Coulomb correction** $E_C \approx -3 e^2 Z(Z-1) / (5 R_0 A^{1/3})$
   to the per-atom binding. Tune $R_0$ empirically (1 parameter)
   to close ³He without breaking ⁴He.
2. **m_p chain closure** per #663's audit — drops the −720/−872
   ppm baseline.
3. **Magic-shell sign convention review** — ³He's wrong-sign
   suggests the categorical formula's sign was tuned to the
   *categorical* anchor differences, which absorb Coulomb already.
4. After 1–3, expect MAE in the ppm range; the remaining gap to
   1 ppb is then Q_β-style categorical refinement of the structural
   terms.

## Caveat

The κ = −1.07 MeV/excess in this probe is **empirical** (from
PR #656's v6 fit), not categorically derived. Once the
substrate-derivation for the asymmetry slope is wired (open work),
this becomes a categorical correction.

## Witness

`computations/m4-magic-shell-correction-mass-table.witness.json`
**(deleted as orphan in PR #1077 — producer script
`probe_m4_magic_shell_correction.py` was removed in `aac4f0050`
"cleanup(batch2): move 148 probes + 2 deprecated to `_deprecated/`").**
At its 2026-05-16 commit, the witness recorded all 6 atoms × both
Q_β modes × magic-shell correction with full per-term breakdown.
The data was a snapshot of the categorical-Coulomb bottleneck
diagnosis at the time of this audit; the analysis above stands
on its own without the JSON.
