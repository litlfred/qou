---
# qou-q6lw
title: 'CHARM-side hypothesis assessment (owner Q): is the additive term charm/heavy-flavor? PRELIM: it''s the COLOR sector (color-tube, gluon), NOT charm — ''gluons couple color not flavor'' (inter-nucleon-channel-color-tube.md). Color↔flavor swap (c-from-color-flavor-swap) = charge-conjugation C on u/d, not charm. Charm=\mathfrak{c} is the heavy-meson mass sector (flavor-dressing-functor). Confirm vs Agent-B sweep.'
status: in-progress
type: task
priority: normal
tags:
    - 8f-decide
    - reorg-2026-10-04
created_at: 2026-08-02T15:55:11Z
updated_at: 2026-11-16T17:50:00Z
parent: qou-8lxd
---

## Verified Resolution & Formalisation (PR `litlfred/qou#8140`, `468e210bfac6c8438bd4b6331f2fa807f91853e8`)

- **50+ dps Probe & Witness:** `computations/probes/charm_vs_color_sector_additive_term_probe.py` and `computations/probes/charm-vs-color-sector-additive-term.witness.json` (5 assertions, `allPassed: true`, proton pin).
- **Lean 4 Formalisation (`0` `sorry`, wired into `QOU.lean`):** `folio/quantum-observable-universe/lean/QOU/StandardModel/ColorVsCharmAdditiveSector.lean`.
- **Three-part structural verification:**
  1. **The inter-nucleon additive term acts on the 3-strand COLOR-SHEET sector** (`conj:inter-nucleon-channel-color-tube`, `QOU.BraidsAndKnots.InterNucleonChannelColorTube`, `QOU.BraidsAndKnots.ColorPairIsotypicDecomposition`): each nucleon carries 3 quark color sheets $(r, g, b)$ spanning the 3-dim icosahedral irrep $T_1$ of $A_5 \cong I$ ($3 \times 3 = 9$ color pairs, $T_1 \otimes T_1 = A \oplus T_1 \oplus H$). Because gluons couple color rather than flavor, the leading $gg$ interface is the flavor-blind bar-symmetric average $\sigma_{\text{avg}} = (\sigma + \sigma^{-1})/2 = \sigma - (h_q/2)\cdot 1$ (Markov factor $z - h_q/2$), with subleading light-$(u, d)$ Bring color-tube asymmetry $f_{pn}(q_0) = z(q_0) - h(q_0)(1/2 - \delta(q_0)/4)$ (`+7.19016e-5` shift at $q_0$). Under the $A_5$ isotypic + isospin selection rule ($I = 1 \to \mathrm{Alt}^2(T_1) = T_1$), $pp$ and $nn$ receive the exact same weight tensor ($W_{\text{same}} = 0, W_{\text{diff}} = 1/6$), giving 0% weight-tensor CSB.
  2. **The symbol $C$ in `conj:c-from-color-flavor-swap` is discrete CHARGE CONJUGATION, not the charm quark $\mathfrak{c}$** (`QOU.BraidsAndKnots.CFromColorFlavorSwap`): $C$ swaps $u \leftrightarrow \bar{u}$ and $d \leftrightarrow \bar{d}$ on each of the 3 color sheets ($p \leftrightarrow \bar{p}, n \leftrightarrow \bar{n}, C^2 = \mathrm{id}$), preserving the base flavor (`up` or `down`) and chirality sign $\epsilon(c_1, c_2, F_1, F_2)$ across all $16 \times 9 = 144$ nucleon/color cells.
  3. **The charm quark $\mathfrak{c}$ (`Flavor.charm`) lives in the heavy-meson mass dressing sector (`def:flavor-dressing-functor`, `QOU.FlavorDressing.Flavor`) and has ZERO projection onto the 3-strand $(u, d)$ nucleon color-sheet channel** (`charmCount_eq_zero`, `charmContactIndicator_eq_zero`, `charm_projected_color_tube_sum_eq_zero`).

## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
