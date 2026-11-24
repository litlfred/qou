# Q-Gap-10 (`qou-nu01`): First-Principles Adjudication of Non-Zero Neutrino Mass Lifts Above $\operatorname{Vol}(0_1) = 0$, Bring–Schwinger $\alpha_v^3$ Bridge, & Stabilization Framing Parity

**Date:** 2026-11-24
**Mission / Bean:** `Q-Gap-10` (`qou-nu01`)
**Lean 4 Module:** `folio/quantum-observable-universe/lean/QOU/StandardModel/NeutrinoUnknotSweedlerLift.lean` (`0 sorry`, `0` custom axioms, `BP001..BP009` `0/0/0`, extending `NeutrinoUnknotSweedlerMassLift` and `ElectroweakBringSchwingerBridge`)
**80-dps Cross-Anchor Probe & Witness:** `computations/probes/neutrino_unknot_sweedler_lift_probe.py` / `computations/probes/neutrino-unknot-sweedler-lift-probe.witness.json` (`mpmath` 80 dps + `sympy` over $\mathbb{Q}(q)$, `q0Anchor: "comparison"`, zero `float64`, zero fitting)

---

## 1. Pre-Committed Zero-Parameter Candidate Menu & Observational Window

At tree level in the volume–density channel, the neutrino ($0_1$) and antineutrino ($0_1^\sigma$) carry $\operatorname{Vol}(0_1) = 0$ and therefore $m_{\nu}^{(0)} = 0$ (`unknot_vol_zero_implies_tree_mass_zero`). Using **only** CAL-1 ($m_e = 0.51099895069 \pm 0.00000000016\;\mathrm{MeV}$, CODATA-2022) and the registered substrate pins $q_p = q_{\mathrm{at}}(80)$ and $q_\mu = q_{\mu\mathrm{on,at}}(80)$ (with zero free parameters), we pre-commit and test the complete hierarchy of Sweedler weak-jet, Habiro loop-rung, electron quadratic, Bring–Schwinger electroweak crossing ($\alpha_v = 1/N_v = m_p / v_{\mathrm{weak}}$ from `ElectroweakBringSchwingerBridge`), and Weinberg dimension-5 see-saw scales against:

- **Solar splitting scale (PDG 2024):** $\sqrt{\Delta m_{21}^2} = 8.6776 \pm 0.1037\;\mathrm{meV}$ ($\Delta m_{21}^2 = (7.53 \pm 0.18)\times 10^{-5}\;\mathrm{eV}^2$),
- **Atmospheric splitting scale (PDG 2024, NH):** $\sqrt{\Delta m_{31}^2} = 50.3021 \pm 0.2798\;\mathrm{meV}$ ($\Delta m_{31}^2 = (2.5303 \pm 0.0281)\times 10^{-3}\;\mathrm{eV}^2$),
- **Cosmological & direct kinematic bounds:** $\sum m_\nu < 120\;\mathrm{meV}$ ($95\%\;\mathrm{CL}$, Planck 2018 + BAO) and $m_{\nu_e}^{\mathrm{eff}} < 450\;\mathrm{meV}$ ($90\%\;\mathrm{CL}$, KATRIN 2024).

---

## 2. 80-dps Cross-Anchor Adjudication Table

| Candidate Key | Zero-Parameter Closed Form | Proton Pin $q_p$ (`meV`) | Muon Pin $q_\mu$ (`meV`) | Ratio to $\sqrt{\Delta m_{21}^2}$ | Ratio to $\sqrt{\Delta m_{31}^2}$ | Verdict |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| `M0_tree_unknot` | $\operatorname{volumeMass}(m_e, \operatorname{Vol}(0_1)=0)$ | `0` | `0` | `0` | `0` | Tree-level massless baseline |
| `S_k8_sweedler_4hop` | $(q_0^2 - 1)^8 m_e$ | `4296.4458` | `4296.4500` | `495.12` | `85.413` | **Excluded** ($> 120\;\mathrm{meV}$ Planck & $450\;\mathrm{meV}$ KATRIN) |
| `S_k10_sweedler_5hop` | $(q_0^2 - 1)^{10} m_e$ | `231.3565` | `231.3568` | `26.661` | `4.5993` | **Excluded** ($> 120\;\mathrm{meV}$ Planck) |
| **`S_k12_sweedler_6hop`** | **$(q_0^2 - 1)^{12} m_e$** | **`12.458163`** | **`12.458181`** | **`1.4357`** | **`0.2477`** | **In strict $[8.68, 50.30]\;\mathrm{meV}$ band** |
| **`S_k12_t35_2loop`** | **$W_{T(3,5)}(q_0)^2 (q_0^2 - 1)^{12} m_e$** | **`17.567382`** | **`17.567413`** | **`2.0245`** | **`0.3492`** | **In strict $[8.68, 50.30]\;\mathrm{meV}$ band** |
| `S_k14_sweedler_7hop` | $(q_0^2 - 1)^{14} m_e$ | `0.670851` | `0.670853` | `0.0773` | `0.0133` | Over-suppressed ($12.9\times$ below solar) |
| **`H_k7_habiro`** | **$\hbar_{q_0}^7 m_e$** | **`47.904316`** | **`47.904352`** | **`5.5205`** | **`0.9523`** | **In strict $[8.68, 50.30]\;\mathrm{meV}$ band ($-4.77\%$ vs $\sqrt{\Delta m_{31}^2}$)** |
| `H_k8_habiro` | $\hbar_{q_0}^8 m_e$ | `4.746442` | `4.746446` | `0.5470` | `0.0944` | Sub-solar ($0.55\times \sqrt{\Delta m_{21}^2}$) |
| `H_k12_habiro` | $\hbar_{q_0}^{12} m_e$ | `0.00045745` | `0.00045745` | `5.27e-5` | `9.09e-6` | **Excluded** ($1.90\times 10^4\times$ below solar) |
| `E_me3_over_v2` | $m_e^3 / v_{\mathrm{weak}}(q_0)^2$ | `0.00220097` | `0.00220097` | `2.54e-4` | `4.38e-5` | **Excluded** ($3,943\times$ below solar) |
| `EW_k2_alpha_v2_me` | $\alpha_v(q_0)^2 m_e = m_e / N_v^2$ | `7420.4836` | `7420.4827` | `855.13` | `147.52` | **Excluded** ($61.8\times$ above Planck) |
| **`EW_k3_alpha_v3_me`** | **$\alpha_v(q_0)^3 m_e = m_e / N_v^3$** | **`28.277324`** | **`28.277319`** | **`3.2587`** | **`0.5621`** | **In strict $[8.68, 50.30]\;\mathrm{meV}$ band** |
| **`EW_k3_t35_alpha_v3_me`** | **$W_{T(3,5)}(q_0)^2 \alpha_v(q_0)^3 m_e$** | **`39.874143`** | **`39.874143`** | **`4.5951`** | **`0.7927`** | **In strict $[8.68, 50.30]\;\mathrm{meV}$ band** |
| `EW_k4_alpha_v4_me` | $\alpha_v(q_0)^4 m_e = m_e / N_v^4$ | `0.107757` | `0.107757` | `0.0124` | `0.0021` | **Excluded** ($80.5\times$ below solar) |
| `W_seesaw_Nv6` | $v_{\mathrm{weak}}^2 / (m_p N_v^6) = \alpha_v^4 m_p$ | `197.8578` | `197.8577` | `22.801` | `3.9334` | Excluded ($1.65\times$ above Planck sum bound) |
| `W_seesaw_Nv7` | $v_{\mathrm{weak}}^2 / (m_p N_v^7) = \alpha_v^5 m_p$ | `0.753979` | `0.753979` | `0.0869` | `0.0150` | Over-suppressed ($11.5\times$ below solar) |

---

## 3. Proved Algebraic Explanations & Dirac vs Majorana Framing Parity (`NeutrinoUnknotSweedlerLift.lean`)

1. **Why $(q_0^2 - 1)^{12} m_e = 12.46\;\mathrm{meV}$ succeeds while $\hbar_{q_0}^{12} m_e = 0.000457\;\mathrm{meV}$ fails (`sweedlerMassLift_eq_habiro_mul_factor` & `habiroMassLift_lt_sweedlerMassLift`):**
   Over any field $K$ ($q \neq 0$), $(q^2 - 1)^k = \hbar_q^k \cdot [q(q + 1)]^k$. At $q_0 = 1.10997858$, $q_0(q_0 + 1) = 2.342031$, so the 12-passage Sweedler weak-radical norm exceeds the 12th Habiro power by $[q_0(q_0 + 1)]^{12} = \mathbf{27,234.12\times}$. Its exact logarithmic $q$-sensitivity is $\frac{\partial \ln m_\nu}{\partial \ln q} = \frac{24 q^2}{q^2 - 1} = 127.445$, producing a $1.480\;\mathrm{ppm}$ shift between $q_p$ and $q_\mu$.

2. **Why $\alpha_v^3 m_e = m_e / N_v^3 = 28.28\;\mathrm{meV}$ lands in the oscillation band while $m_e^3 / v_{\mathrm{weak}}^2 = 0.00220\;\mathrm{meV}$ fails (`ewCrossingMassLift_three_eq_weinbergSeesaw` & `meCubedDivVewSq_eq_ewCrossing_three_mul`):**
   In `ElectroweakBringSchwingerBridge`, $\alpha_v = 1/N_v = m_p / v_{\mathrm{weak}} = 0.00381071$ ($N_v = 262.418$, $v_{\mathrm{weak}} = 246.220\;\mathrm{GeV}$), whose highest-order monomial in the Bring–Schwinger self-consistency cubic `ewFixedPointCubic` is $\alpha_v^3$. Algebraically:
   $$\alpha_v^3 m_e = \frac{v_{\mathrm{weak}}^2}{\Lambda_{\mathrm{EWB}}}, \qquad \Lambda_{\mathrm{EWB}} = \frac{v_{\mathrm{weak}}^5}{m_e m_p^3} = 2.138 \times 10^{15}\;\mathrm{GeV},$$
   whereas $\frac{m_e^3}{v_{\mathrm{weak}}^2} = (\alpha_v^3 m_e) \cdot \frac{v_{\mathrm{weak}} m_e^2}{m_p^3} = (\alpha_v^3 m_e) \times 7.7835 \times 10^{-5}$ (`meCubedDivVewSq_lt_ewCrossing_three`), suppressing $m_e^3 / v_{\mathrm{weak}}^2$ by $12,848\times$. Moreover, $\alpha_v^2 m_e = 7.420\;\mathrm{eV}$ and $\alpha_v^4 m_e = 0.1078\;\mathrm{meV}$ bracket $[8.68, 50.30]\;\mathrm{meV}$ from outside, uniquely isolating $k = 3$ (`28.28 meV`, $q_p$ vs $q_\mu$ swing $= 170.50\;\mathrm{ppb}$).

3. **Dirac vs Majorana Framing Parity on $0_1$ Stabilizations (`stab_markov_diff_and_ratio`, `jones_writhe_normalised_eq`, `stabilized_unknot_dirac_vs_majorana`):**
   On 2-strand Reidemeister-I stabilizations $\sigma_1^{+1}$ (`writhe = +1`) vs $\sigma_1^{-1} = \sigma_1 - h \cdot 1$ (`writhe = -1`) of the unknot $0_1$, the unnormalised Markov traces at $z_D = q^3/(q^2 + 1)$ satisfy $\tau_M(\sigma_1) - \tau_M(\sigma_1^{-1}) = q - q^{-1} \neq 0$ and $\tau_M(\sigma_1)/\tau_M(\sigma_1^{-1}) = q^4 \neq 1$, whereas Jones writhe normalisation $q^{-2w} \tau_M(\sigma_1^w)$ collapses both to $\frac{q}{q^2 + 1} = \frac{1}{[2]_q}$. Consequently:
   - **Framed reading (`Dirac`):** Spatial mirror conjugation exchanges $\sigma_1 \leftrightarrow \sigma_1^{-1}$, supporting conserved lepton number $L = \pm 1$ and predicting $m_{\beta\beta} = 0$ (no $0\nu\beta\beta$).
   - **Writhe-normalised / symmetric reading (`Majorana`):** The `writhe = 0` symmetric stabilization $\sigma_1 + \sigma_1^{-1}$ is mirror-invariant, forbidding any conserved $\pm 1$ lepton charge and permitting Weinberg $(LH)^2$ Majorana mass with $|m_{\beta\beta}| \in [1.45, 3.77]\;\mathrm{meV}$ at $m_1 = 0$ (NH, below KamLAND-Zen-800's $28\text{--}122\;\mathrm{meV}$ upper limit).
   - Which reading QOU's physical electroweak completion selects remains an open structural derivation, packaged without global instances in `NeutrinoRadiativeLiftClass` (`§3b-cond`).
