# Observational Accuracy & Precision Scorecard

Every object in *On the Mechanics of Quantum Observable Universes* (QOU) is a mathematical construction evaluated in arbitrary-precision arithmetic (`80` decimal places, `mp.dps = 80`). Empirical physics enters strictly at the comparison boundary where a derived model quantity is set against experimental metrology (CODATA 2022, PDG 2024, NIST, and AME2020).

This scorecard is deterministically generated from the repository's machine-verified computation witnesses by [`scripts/generate-accuracy-scorecard.py`](scripts/generate-accuracy-scorecard.py) and gated in continuous quality assurance (`compute-qa`, site rendering, and post-merge publishing).

- **Anti-fit discipline:** Only **three physical calibration inputs** enter the model — the electron mass $m_e$ (fixing the overall MeV energy unit), the proton-to-electron mass ratio $m_p / m_e$ (fixing the deformation parameter $q_0 > 1$), and the charged-pion mass $m_{\pi^\pm}$ (fixing the meson-sector scale). All nuclear, electroweak, Coulomb, and molecular expressions are evaluated without free or fitted parameters, using the canonical Markov trace parameter $z = q^3/(q^2+1)$.
- **Full-spectrum reporting:** Both sub-part-per-billion successes and large multi-percent structural deficits are reported side by side so that open mathematical derivations remain visible and falsifiable.

---

## 1. Calibration Baseline & the `1 ppQ` ($10^{-15}$) Precision Floor

One **part per quadrillion** (`1 ppQ`) denotes a fractional residual of
$$1\;\mathrm{ppQ} = 10^{-15} = 10^{-6}\;\mathrm{ppb} = 10^{-9}\;\mathrm{ppm} = 10^{-13}\%.$$

Because every dimensional mass prediction $O(m_e, q_0, m_{\pi^\pm})$ scales linearly with $m_e$ or $m_{\pi^\pm}$ and depends smoothly on $q_0$, experimental input uncertainties propagate into every model prediction via the 80-dps Fréchet–Jacobian covariance law $\Sigma_O = J\,\Sigma_\theta\,J^\top$:

| Quantity | Symbol | Value (`80-dps` truncated) | Experimental $1\sigma$ | Relative Floor (`ppb`) | Relative Floor (`ppQ`) | Structural Role |
|---|---|---:|---:|---:|---:|---|
| Electron mass | $m_e$ | `0.51099895069 MeV` | `1.60e-10 MeV` | `0.3131` | `3.131e+5` | Calibration input 1 (overall MeV unit) |
| Proton/electron ratio | $m_p / m_e$ | `1836.152673426` | `3.20e-8` | `0.01743` | `1.743e+4` | Calibration input 2 (dimensionless baryon ratio) |
| Charged-pion mass | $m_{\pi^\pm}$ | `139.57039 MeV` | `0.00018 MeV` | `1289.7` | `1.290e+9` | Calibration input 3 (meson-sector scale) |
| Deformation parameter | $q_0$ | `1.109978582751380808` | `9.213e-13` | `0.000830` | `830.0` | Solved from $m_p / m_e$ (tightest framework anchor) |
| Canonical Markov weight | $z = q_0^3/(q_0^2+1)$ | `0.612688037146465252` | `9.642e-13` | `0.001574` | `1573.7` | Derived Hecke–Markov trace parameter |
| Quantum Planck & Hecke step | $\hbar_q,\; h_A$ | `0.099081716044, 0.209060298796` | `7.48e-13, 1.67e-12` | `0.0075` | `7547.0` | $\hbar_q = 1 - q_0^{-1},\; h_A = q_0 - q_0^{-1}$ |

### Implications for `1 ppQ` Comparisons

1. **Internal mathematical identities (`< 1 ppQ`):** Exact algebraic and numerical round-trip identities (such as the proton mass-identity root inversion at $q_0$, Koide resolvent polynomial identities, and Lanczos/CG eigensolver residuals in few-body $K_A$ plaquettes) hold to `< 10^{-50} ppb` (`< 10^{-44} ppQ`), well beyond `1 ppQ`.
2. **Empirical comparison floor (`830 ppQ` to `1.29e9 ppQ`):** The tightest dimensionless anchor in the framework is $q_0$ itself, whose propagated CODATA uncertainty is `830.0 ppQ` (`0.000830 ppb`). Every dimensional mass expressed in MeV inherits at minimum the CODATA electron-mass uncertainty floor of `3.131e+5 ppQ` (`0.3131 ppb`), confirmed across $A = 1\text{--}238$ (`0.313–0.316 ppb`). Even the most precisely measured non-anchor quantity in physics used here — the fine-structure constant $\alpha_{\mathrm{EM}}^{-1}$ — has a CODATA $1\sigma$ uncertainty of `1.532e+5 ppQ` (`0.1532 ppb`).
3. **Bottom-line `1 ppQ` verdict:** **Zero non-anchor observables are empirically testable at or close to `1 ppQ` today.** Current experimental metrology sits $10^5\text{--}10^9\times$ above `1 ppQ` on dimensional observables, and the closest derived QOU prediction ($\alpha_{\mathrm{EM}}^{-1}$ in the additive Schwinger Form B arm) stands at `3.65e+5 ppQ` (`-0.365 ppb`, `-2.38`$\sigma_{\mathrm{exp}}$).

---

## 2. Executive Scorecard Across All Five Categories

| Category | Regime / Observable Scope | $N$ | Mean $|\Delta|/O_{\mathrm{exp}}$ | Median $|\Delta|/O_{\mathrm{exp}}$ | Typical `ppQ` Error Scale | Within $\le 1\sigma_{\mathrm{exp}}$ | Within $\le 3\sigma_{\mathrm{exp}}$ | Observational Verdict | `1 ppQ` ($10^{-15}$) Verdict | Epistemic Status |
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| **1. Mass** (Elementary & Hadrons) | $m_\mu, m_\tau/m_e, m_K/m_\pi, m_K, m_n$ (+ 3 pins) | `6` (+3 pins) | `81.1 ppm` (`136 ppb` excl. $m_n, m_\tau$) | `30.9 ppm` (`211 ppb` $m_\mu$) | `5.15e+07` to `4.86e+11` | `2 / 6` ($m_K/m_\pi, m_K$) | `2 / 6` (`3/6` w/ NIST $m_\tau$) | **High** on $m_K/m_\pi$ (`+51.5 ppb`, `<0.002σ`) & $m_\mu$ (`+211 ppb`); $m_n$ (`-486 ppm`) open | **Not at `1 ppQ`** (input floor `3.13e5 ppQ`) | Derived ($m_\mu, m_K$); Conditional ($m_n$) |
| **1. Mass** (Nuclear Rest Mass $A \ge 2$) | Symbolic Q-CLT `m_symbolic_MeV` vs AME2020 | `2542` | `0.569%` | `0.578%` | `5.78e+12` | `0 / 2542` | `0 / 2542` | **`~99.4%` bulk accuracy** (constituent $Z m_p + N m_n$); `~0.57%` residual from binding | **Not at `1 ppQ`** (`~5.8e12 ppQ`) | Principled 1D Q-CLT proxy |
| **2. Binding Energy** ($A = 2\text{--}4$ & $A \ge 2$) | 3D $K_A$ plaquette ($A \le 4$) & 1D Q-CLT ($A \ge 2$) | `4` ($K_A$) / `2542` (Q-CLT) | `7.13%` ($K_A$) / `68.6%` (Q-CLT) | `4.96%` ($K_A$) / `68.9%` (Q-CLT) | `3.65e+13` ($K_4$) to `6.89e+14` | `0 / 2542` | `0 / 2542` | **Few-body $K_4$ strong** (`+1.8%` ${}^2\mathrm{H}$, `+3.65%` ${}^4\mathrm{He}$); **$A \ge 5$ underbound `~69%`** | **Not at `1 ppQ`** | Derived ($A \le 4$); Open saturation ($A \ge 5$) |
| **3. Charge, $\alpha_{\mathrm{EM}}$ & Geometry** | $Q$, $\alpha_{\mathrm{EM}}^{-1}$, mirror Coulomb (`8`), VSEPR (`7`) | `19` | `0` ($Q$), `-0.365 ppb` ($\alpha_{\mathrm{EM}}$), `0.62%` (VSEPR) | `0.23%` (across non-exact) | `0` ($Q$), `365225.8` ($\alpha_{\mathrm{EM}}$) | `3 / 19` ($Q, \mathrm{CH_4, CO_2}$) | `4 / 19` (+ $\alpha_{\mathrm{EM}}$ Form B) | **Exact** $Q$; **sub-ppb** $\alpha_{\mathrm{EM}}^{-1}$ Form B (`-2.38σ`); **`~1.3%`** mirror Coulomb mean | $Q$ exact (`0 ppQ`); $\alpha_{\mathrm{EM}}$ at `3.65e5 ppQ` | Proved ($Q$); Open arm selection ($\alpha_{\mathrm{EM}}$) |
| **4. Weak $\beta$-Decay** | Free $n$, `6` TM skein benchmarks, `1009` composite $\beta^-$ | `1010` | `-58.4%` ($n$), `60.6%` (TM), `255.5%` (table) | `71.7%` (TM), `142.4%` (table) | `1.42e+15` | `0 / 1010` | `0 / 1010` | **Order-of-magnitude keV–MeV** on TM (`-8.1%` ${}^{14}\mathrm{C}$); **unclosed** on isobaric table (`0/1009` exo.) | **Not at `1 ppQ`** | Conditional (`C1–C3` on $n$); Open ($N_v$, $A \ge 2$) |
| **5. $\alpha$-Decay & Fission** | `7` WKB emitters ($Q_{\mathrm{exp}}$), $N=126$ ${}^{210}\mathrm{Po}$, `1051` derived $Q_\alpha$ | `1051` (+7 WKB) | `0.35 dex` (WKB @ $Q_{\mathrm{exp}}$); `584.5%` ($Q_\alpha$) | `0.27 dex` (`+0.044 dex` ${}^{210}\mathrm{Po}$ MJ); `320.3%` ($Q_\alpha$) | `3.20e+15` | `0 / 1051` | `0 / 1051` | **Strong WKB + $N=126$ preformation** (`10.6%` $T_{1/2}$); **derived heavy $Q_\alpha$ open** (`3–48 dex`) | **Not at `1 ppQ`** | Derived WKB/MJ; Open heavy $Q_\alpha$ |

---

## 3. Category-by-Category Detailed Tables (Low-$A$ vs High-$A$)

### 3.1 Category 1 — Particle & Nuclear Masses

#### Table 3.1a: Elementary Leptons, Mesons, and Baryons (Proton-Anchored $q_0$)

| Observable | Predicted (`80-dps` trunc.) | Experimental Reference | $\sigma_{\mathrm{pred}}$ (from inputs) | Relative Error | $\|\Delta\|/O_{\mathrm{exp}}$ (`ppQ`) | Pull $z_{\mathrm{exp}}$ | Beats $100\times\,\sigma_{\mathrm{exp}}$? | Status |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Electron $m_e$ | `0.510998951 MeV` | `0.510998951 ± 1.6e-10 MeV` | `1.60e-10 MeV` | `0` | `0` | `0.00σ` | Anchor (input) | Calibration input 1 |
| Muon $m_\mu$ | `105.658397811 MeV` | `105.658375496 ± 2.3e-6 MeV` | `3.31e-8 MeV` | `+211.206 ppb` | `2.11e+8` | `9.70σ` | No | Derived (proton $q_0$) |
| Tau/electron $m_\tau / m_e$ | `3477.442306` | `3477.228000 ± 2.3e-2` | `—` | `+61.63 ppm` | `6.16e+10` | `+9.32σ` (`0.92σ` NIST) | No | Quadratic Koide resolvent (`gap2b`) |
| Charged pion $m_{\pi^\pm}$ | `139.570390000 MeV` | `139.570390000 ± 1.8e-4 MeV` | `1.80e-4 MeV` | `0` | `0` | `0.00σ` | Anchor (input) | Calibration input 3 |
| Meson ratio $m_{K^\pm}/m_{\pi^\pm}$ | `3.537118621` | `3.537118439 ± 9.3e-5` | `1.16e-12` | `+51.475 ppb` | `5.15e+7` | `0.00σ` | Yes (`0.20x`) | Derived (`< 0.002σ`, beats $100\times$!) |
| Charged kaon $m_{K^\pm}$ | `493.677025412 MeV` | `493.677000000 ± 0.013 MeV` | `6.37e-4 MeV` | `+51.475 ppb` | `5.15e+7` | `0.00σ` | Yes | Derived (`< 0.002σ`) |
| Proton $m_p$ | `938.272089427 MeV` | `938.272089430 ± 2.9e-7 MeV` | `2.94e-7 MeV` | `0` | `0` | `0.00σ` | Anchor (input) | Calibration input 2 ($q_0$ pin) |
| Neutron $m_n$ | `939.108522307 MeV` | `939.565421940 ± 4.8e-7 MeV` | `2.95e-7 MeV` | `-486.29 ppm` | `4.86e+11` | `-951874.24σ` | No | Conditional ($m_p + m_e + Q_{\beta^-}$) |
| Nucleon split $\Delta m_{np}$ | `0.836432879 MeV` | `1.293332510 ± 3.8e-7 MeV` | `2.62e-10 MeV` | `-35.33%` | `3.53e+14` | `-1202367.45σ` | No | Conditional (`C1–C3`) |

*Assessment (Elementary & Hadron Sector):* Holding $q_0$ fixed at the proton-to-electron anchor reproduces the charged-kaon to charged-pion ratio $m_{K^\pm}/m_{\pi^\pm}$ to `+51.48 ppb` (`+0.0020`$\sigma_{\mathrm{exp}}$, beating the $100\times$ experimental precision target of `263.6 ppb`) and the muon mass $m_\mu$ to `+211.21 ppb` (`+9.70`$\sigma_{\mathrm{exp}}$; equivalent to an `+11.61 ppb` shift between muon-pinned and proton-pinned $q_0$). The quadratic Koide resolvent applied to $(m_e, m_\mu^{\mathrm{QOU}})$ yields $m_\tau / m_e = 3477.4423$ (`+61.63 ppm` vs PDG 2024, $0.92\sigma$ vs NIST), while an untuned $q_0$-phase operator closure for $S_3$ generational equipartition is falsified and left open. The free neutron mass $m_n$ (`-486.3 ppm`) inherits the `-0.4569 MeV` shortfall of the conditional $Q_{\beta^-}$ weight-trace split.

#### Table 3.1b: Nuclear Rest Masses $M_{\mathrm{nuc}}(Z, N)$ Across Mass-Number Bands ($A \ge 2$)

Comparison joins `computations/mass-table-comprehensive.witness.json` (`m_symbolic_MeV`, zero-fit symbolic 1D Q-CLT proxy) against all `2,542` non-estimated $A \ge 2$ nuclides in AME2020 ($M_{\mathrm{nuc}}^{\mathrm{exp}} = Z m_p + N m_n - B_{\mathrm{AME}}$):

| Mass-Number Band | Nuclides $N$ | Mean $\|\Delta M\|/M_{\mathrm{exp}}$ | Median $\|\Delta M\|/M_{\mathrm{exp}}$ | Median Error (`ppQ`) | Min / Max $\|\Delta M\|/M_{\mathrm{exp}}$ | Within $\le 1\sigma_{\mathrm{exp}}$ / $\le 3\sigma_{\mathrm{exp}}$ | Regime Behaviour |
|---|---:|---:|---:|---:|---:|---:|---|
| Very Low-$A$ ($2\text{--}16$) | `65` | `0.332%` | `0.346%` | `3.46e+12` | `0.013% / 0.594%` | `0 / 0` | Light cluster regime; 1D chain misses 3D plaquettes |
| Low/Mid-$A$ ($17\text{--}56$) | `327` | `0.575%` | `0.603%` | `6.03e+12` | `0.106% / 0.659%` | `0 / 0` | Approach to iron peak ($B_{\mathrm{AME}}/A \to 8.79\;\mathrm{MeV}$) |
| High-$A$ Med ($57\text{--}150$) | `1083` | `0.610%` | `0.609%` | `6.09e+12` | `0.541% / 0.659%` | `0 / 0` | Shell-saturated plateau; nucleonic rest mass dominates $M$ |
| Very High-$A$ ($\ge 151$) | `1067` | `0.539%` | `0.542%` | `5.42e+12` | `0.474% / 0.584%` | `0 / 0` | Coulomb-softened heavy regime ($B_{\mathrm{AME}}/A \approx 7.6\;\mathrm{MeV}$) |
| **All Measured ($A \ge 2$)** | `2542` | `0.569%` | `0.578%` | `5.78e+12` | `0.013% / 0.659%` | `0 / 0` | Uniform `~0.57%` mass accuracy from constituent $(m_p, m_n)$ |

#### Table 3.1c: Representative Nuclide Mass & Binding Benchmarks ($A = 2 \to 238$)

| Nuclide | $(Z, N, A)$ | $M_{\mathrm{pred}}$ (MeV) | $M_{\mathrm{exp}}$ (MeV) | Mass Error (`%`) | Input Floor $\sigma_{\mathrm{pred}}$ (`ppb`) | $B_{\mathrm{pred}}^{\mathrm{Q\text{-}CLT}}$ (MeV) | $B_{\mathrm{AME}}$ (MeV) | Binding Error (`%`) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| ${}^2\mathrm{H}$ | `(1, 1, 2)` | `1875.3096` | `1875.6129` | `-0.016%` | `0.3139` | `2.071` | `2.225` | `-6.90%` |
| ${}^3\mathrm{H}$ | `(1, 2, 3)` | `2810.9747` | `2808.9211` | `+0.073%` | `0.3144` | `5.514` | `8.482` | `-34.99%` |
| ${}^4\mathrm{He}$ ($K_4$ `M3a`) | `(2, 2, 4)` | `3725.4322` | `3727.3794` | `-0.052%` | `0.3159` | `29.329` | `28.296` | `+3.65%` |
| ${}^{12}\mathrm{C}$ | `(6, 6, 12)` | `11238.3712` | `11174.8633` | `+0.568%` | `0.3161` | `25.912` | `92.162` | `-71.88%` |
| ${}^{16}\mathrm{O}$ | `(8, 8, 16)` | `14983.5958` | `14895.0808` | `+0.594%` | `0.3162` | `35.449` | `127.619` | `-72.22%` |
| ${}^{40}\mathrm{Ca}$ | `(20, 20, 40)` | `37454.9437` | `37214.6980` | `+0.646%` | `0.3164` | `92.669` | `342.052` | `-72.91%` |
| ${}^{56}\mathrm{Fe}$ | `(26, 30, 56)` | `52433.2782` | `52089.7770` | `+0.659%` | `0.3165` | `135.052` | `492.260` | `-72.56%` |
| ${}^{120}\mathrm{Sn}$ | `(50, 70, 120)` | `112346.6161` | `111662.6454` | `+0.613%` | `0.3164` | `304.585` | `1020.539` | `-70.15%` |
| ${}^{208}\mathrm{Pb}$ | `(82, 126, 208)` | `194726.1736` | `193687.1243` | `+0.536%` | `0.3162` | `539.812` | `1636.430` | `-67.01%` |
| ${}^{238}\mathrm{U}$ | `(92, 146, 238)` | `222808.9482` | `221695.8938` | `+0.502%` | `0.3160` | `621.928` | `1801.690` | `-65.48%` |

* Note on ${}^3\mathrm{He}$ and ${}^4\mathrm{He}$: `mass-table-comprehensive.witness.json` omits six light proton-rich/closed-cluster rows (`4H, 5H, 6H, 3He, 4He, 4Li`); ${}^4\mathrm{He}$ is evaluated directly in the exact $K_4$ tetrahedral plaquette model below (`Table 3.2a`), and constituent uncertainty propagation covers all $A = 1\text{--}238$ benchmarks in `master-atlas-80dps.witness.json`.

---

### 3.2 Category 2 — Nuclear Binding Energy ($B(Z, N)$)

#### Table 3.2a: Few-Body Complete-Graph $K_A$ Plaquette & Variational Models ($A = 2, 3, 4$)

| Model / Formulation | ${}^2\mathrm{H}$ $B$ (MeV) [Err] | ${}^3\mathrm{H}$ $B$ (MeV) [Err] | ${}^3\mathrm{He}$ $B$ (MeV) [Err] | ${}^4\mathrm{He}$ $B$ (MeV) [Err] | Scaling $B_3 / B_2$ | Scaling $B_4 / B_2$ |
|---|---:|---:|---:|---:|---:|---:|
| AME2020 Experimental Reference | `2.22457` | `8.48180` | `7.71804` | `28.29566` | `3.813` (`3H`) | `12.720` |
| 1D Symbolic Hecke Chain (`mass-table`) | `2.071` (`-6.90%`) | `5.514` (`-34.99%`) | `—` (omitted) | `—` (omitted) | `2.663` | `3.000` (asymptotic) |
| 3D $K_A$ Plaquette Exact (`M3a`, $E_{\mathrm{osc}}$) | `2.265` (`+1.81%`) | `9.014` (`+6.27%`) | `9.014` (`+16.79%`) | `29.329` (`+3.65%`) | `3.980` | `12.950` |
| Analytic Hoefsmit Plaquette Cumulant (`M5a`) | `2.265` (`+1.81%`) | `8.557` (`+0.89%`) | `8.557` (`+10.87%`) | `24.794` (`-12.37%`) | `3.778` | `10.948` |
| Self-Bound Jacobi Variational (Hall–Post $\eta_2$) | `2.265` (`+1.81%`) | `10.938` (`+28.96%`) | `10.938` (`+41.72%`) | `26.020` (`-8.04%`) | `4.830` | `11.489` |
| Self-Bound Jacobi Variational (Unrestricted $\eta_A^*$) | `2.265` (`+1.81%`) | `11.833` (`+39.51%`) | `11.833` (`+53.31%`) | `30.546` (`+7.95%`) | `5.225` | `13.487` |

#### Table 3.2b: Symbolic 1D Q-CLT Binding Proxy Across Mass-Number Bands ($A \ge 2$)

| Mass-Number Band | Nuclides $N$ | Bound ($B_{\mathrm{pred}} > 0$) | Mean $\|\Delta B\|/B_{\mathrm{AME}}$ | Median $\|\Delta B\|/B_{\mathrm{AME}}$ | Median Error (`ppQ`) | Mean $B_{\mathrm{pred}}/A$ (MeV) | Mean $B_{\mathrm{AME}}/A$ (MeV) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Very Low-$A$ ($2\text{--}16$) | `65` | `65/65 (100%)` | `57.16%` | `63.00%` | `6.30e+14` | `2.173` | `5.510` |
| Low/Mid-$A$ ($17\text{--}56$) | `327` | `327/327 (100%)` | `69.44%` | `71.19%` | `7.12e+14` | `2.420` | `8.026` |
| High-$A$ Med ($57\text{--}150$) | `1083` | `1083/1083 (100%)` | `70.28%` | `70.22%` | `7.02e+14` | `2.509` | `8.446` |
| Very High-$A$ ($\ge 151$) | `1067` | `1067/1067 (100%)` | `67.38%` | `67.58%` | `6.76e+14` | `2.557` | `7.844` |
| **All Measured ($A \ge 2$)** | `2542` | `2542/2542 (100%)` | `68.62%` | `68.93%` | `6.89e+14` | `2.509` | `8.064` |

*Assessment (Low-$A$ vs High-$A$ Binding):* In the few-body regime ($A \le 4$), replacing the 1D chain with the 3D complete-graph $K_A$ colour-flux plaquette (`M3a` exact Lanczos ground state in the $E_{\mathrm{osc}}$ chart) captures the tetrahedral jump from deuteron to $\alpha$-particle ($B_4/B_2 = 12.950$ vs AME2020 `12.720`, giving $B({}^4\mathrm{He}) = 29.329\;\mathrm{MeV}$, `+3.65%`). Across $A \ge 5$, the production mass table falls back to the 1D factorized symbolic Q-CLT chain, whose per-nucleon binding approaches $b_2 \approx 2.071\;\mathrm{MeV}$ asymptotically rather than the empirical $\sim 7.5\text{--}8.8\;\mathrm{MeV}$ nuclear saturation curve, producing a uniform `-67%` to `-70%` binding deficit across medium and heavy nuclei.

---

### 3.3 Category 3 — Charge, Hypercharge, $\alpha_{\mathrm{EM}}$, Coulomb Splits & Molecular Geometry

#### Table 3.3a: Electroweak / Electromagnetic Couplings & Mirror-Nuclei Coulomb Systematics

| Observable / Test | Predicted Value | Experimental Reference | Relative Error | `ppQ` Error Scale | Pull / Scatter | Status & Scope |
|---|---:|---:|---:|---:|---:|---|
| Electric charge quantization $Q(p), Q(n)$ | `+1, 0` ($c = 1/2$) | `+1, 0` ($\|Q_p + Q_e\|/e < 10^{-21}$) | `0` (exact) | `0` | Exact | Proved topological writhe $Q = \tfrac{1}{2}\operatorname{writhe}(H)$ |
| Fine-structure $\alpha_{\mathrm{EM}}^{-1}$ (Schwinger Form B) | `137.035999127` | `137.035999177 ± 2.1e-8` | `-0.365 ppb` | `365225.8` | `-2.38σ` | Derived (within $3\sigma_{\mathrm{exp}}$; canonical arm selection open) |
| Fine-structure $\alpha_{\mathrm{EM}}^{-1}$ (Chern–Simons tower) | `137.035935094` | `137.035999177 ± 2.1e-8` | `-467.64 ppb` | `4.68e+8` | `-3051.6σ` | Derived consumer arm (`-0.468 ppm` gap vs Form B) |
| Bare topological ${}^3\mathrm{H}\text{--}{}^3\mathrm{He}$ Coulomb | `0.2213 MeV` | `0.7638 MeV` | `-71.03%` (`29.0%` covered) | `7.10e+14` | `3.45x` short | Zero-fit $\tanh(\ln q_0) B_{pp}$; nuclear-geometry factor open |
| Mirror-nuclei Coulomb systematics ($N=8$, $A=3\text{--}39$) | Ratio `0.9868` | `1.0000` (AME2020 splits) | `-1.32%` mean | `1.32e+13` | `±6.94%` RMS | Canonical nuclear-radius Coulomb scaling across mirror doublets |

#### Table 3.3b: $q$-Weighted VSEPR Molecular Geometry & Condensed-Matter Benchmarks

| Molecule / Observable | Symmetry / Weighting | Predicted | Experimental | Residual | Relative Error | `ppQ` Error Scale | Pull $z_{\mathrm{exp}}$ |
|---|---|---:|---:|---:|---:|---:|---:|
| $\theta(\mathrm{CH_4})$ | Exact $T_d$ tetrahedral ($4$ single bonds) | `109.4712°` | `109.4712°` | `0.0000°` | `+5.796 ppb` | `5.80e+6` | `0.00σ` |
| $\theta(\mathrm{CO_2})$ | Exact $D_{\infty h}$ linear ($2$ double bonds) | `180.0000°` | `180.0000°` | `0.0000°` | `0` | `0` | `0.00σ` |
| $\theta(\mathrm{NH_3})$ | $C_{3v}$ $AX_3E_1$ ($q$ bond vs $q^3$ lone pair) | `106.8802°` | `106.6700°` | `+0.2102°` | `+0.20%` | `1.97e+12` | `+4.20σ` |
| $\theta(\mathrm{H_2O})$ | $C_{2v}$ $AX_2E_2$ ($2\times q$ vs $2\times q^3$) | `104.7195°` | `104.4776°` | `+0.2419°` | `+0.23%` | `2.31e+12` | `+24.19σ` |
| $\theta(\mathrm{C_2H_4})$ | $C_{2v}$ planar $AX_3$ ($q^2$ double vs $q$ single) | `117.2322°` | `116.6000°` | `+0.6322°` | `+0.54%` | `5.42e+12` | `+6.32σ` |
| $\theta(\mathrm{H_2S})$ | Orthogonal $p$-orbital baseline | `90.0000°` | `92.1100°` | `-2.1100°` | `-2.29%` | `2.29e+13` | `-42.20σ` |
| $L_{\mathrm{vap}}(\mathrm{H_2O})$ | Hydrogen-bond $q$-plaquette enthalpy | `40.1136 kJ/mol` | `40.6570 kJ/mol` | `-0.5434 kJ/mol` | `-1.34%` | `1.34e+13` | `-27.17σ` |

*Assessment (Charge & EM Sector):* Electric charge quantization is exact ($0\;\mathrm{ppQ}$) from topological writhe $Q(H) = \tfrac{1}{2}\operatorname{writhe}(H)$. The additive Schwinger Form B series reproduces $\alpha_{\mathrm{EM}}^{-1}$ to `-0.365 ppb` (`-2.38`$\sigma_{\mathrm{exp}}$, within $3\sigma_{\mathrm{exp}}$), whereas the Chern–Simons tower arm stands at `-467.64 ppb`; deriving a unique canonical selection between the two arms remains open. In nuclear isospin doublets, the bare topological ratio $\tanh(\ln q_0) = 0.103964$ accounts for `29.0%` of the ${}^3\mathrm{H}\text{–}{}^3\mathrm{He}$ split without nuclear-radius input, while canonical nuclear-radius Coulomb across $8$ mirror pairs ($A = 3\text{--}39$) matches AME2020 splits with mean ratio `0.9868` ($\pm 6.94\%$ RMS). Molecular bond angles are exact (`0–5.8 ppb`) where tetrahedral/linear symmetry dominates ($\mathrm{CH_4}, \mathrm{CO_2}$) and accurate to `0.20%–2.29%` under $q$-weighted lone-pair and double-bond repulsion ($\mathrm{NH_3}, \mathrm{H_2O}, \mathrm{C_2H_4}, \mathrm{H_2S}$).

---

### 3.4 Category 4 — Weak $\beta$-Decay ($Q_{\beta^-}$ & Weak Scale)

#### Table 3.4a: Free-Neutron Conditional Split, Bare Monotone Transfer-Matrix Benchmarks, & Weak Scale

| Transition / Observable | Formulation | Predicted | Experimental | Relative Error | `ppQ` Error Scale | Pull $z_{\mathrm{exp}}$ | Status |
|---|---|---:|---:|---:|---:|---:|---|
| Free neutron $n \to p e^- \bar\nu_e$ | Conditional $T^3$ weight-trace split (`V^3`) | `0.32543 MeV` | `0.78233 MeV` | `-58.40%` | `5.84e+14` | `-1202367.3σ` | Conditional (`C1–C3`) |
| ${}^3\mathrm{H} \to {}^3\mathrm{He}$ | Bare monotone transfer-matrix skein shift | `0.03675 MeV` | `0.01861 MeV` | `+97.50%` | `9.75e+14` | `+1814.4σ` | Zero-fit TM proxy |
| ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$ | Bare monotone transfer-matrix skein shift | `0.14379 MeV` | `0.15648 MeV` | `-8.11%` | `8.11e+13` | `-317.3σ` | Zero-fit TM proxy (`-8.11%`) |
| ${}^{60}\mathrm{Co} \to {}^{60}\mathrm{Ni}$ | Bare monotone transfer-matrix skein shift | `0.08553 MeV` | `0.31817 MeV` | `-73.12%` | `7.31e+14` | `-1789.5σ` | Zero-fit TM proxy |
| ${}^{90}\mathrm{Sr} \to {}^{90}\mathrm{Y}$ | Bare monotone transfer-matrix skein shift | `0.05482 MeV` | `0.54590 MeV` | `-89.96%` | `9.00e+14` | `-7015.4σ` | Zero-fit TM proxy |
| ${}^{137}\mathrm{Cs} \to {}^{137}\mathrm{Ba}$ | Bare monotone transfer-matrix skein shift | `0.15314 MeV` | `0.51400 MeV` | `-70.21%` | `7.02e+14` | `-1718.4σ` | Zero-fit TM proxy |
| ${}^{210}\mathrm{Bi} \to {}^{210}\mathrm{Po}$ | Bare monotone transfer-matrix skein shift | `0.52314 MeV` | `1.16270 MeV` | `-55.01%` | `5.50e+14` | `-10659.3σ` | Zero-fit TM proxy |
| Electroweak crossing invariant $N_v$ | $v_{\mathrm{weak}} = N_v E_\times \mu_0$ ($G_F$ scale) | Open | `1445519.45` | Open | Open | — | Required for absolute $\Gamma_\beta$ rates |

#### Table 3.4b: Isobaric Mass-Difference $Q_{\beta^-} = M(Z, N) - M(Z+1, N-1) - m_e$ Across Measured $\beta^-$ Emitters

Evaluated across all `1,010` non-estimated exothermic $\beta^-$ transitions ($Q_{\beta^-}^{\mathrm{AME}} > 10\;\mathrm{keV}$) present in `mass-table-comprehensive.witness.json`:

| Mass-Number Band | Transitions $N$ | Predicted Exothermic ($Q_{\mathrm{pred}} > 0$) | Mean $\|\Delta Q\|/Q_{\mathrm{AME}}$ | Median $\|\Delta Q\|/Q_{\mathrm{AME}}$ | Median Error (`ppQ`) | Physical Diagnosis |
|---|---:|---:|---:|---:|---:|---|
| Free Neutron ($A = 1$) | `1` | `1/1` | `58.4%` | `58.4%` | `5.84e+14` | Exothermic (`0.325` vs `0.782 MeV`, `-58.4%`) |
| Very Low-$A$ ($2\text{--}16$) | `27` | `0/27` | `167.1%` | `111.2%` | `1.11e+15` | Missing 3D cluster + symmetry energy |
| Low/Mid-$A$ ($17\text{--}56$) | `175` | `0/175` | `157.6%` | `120.7%` | `1.21e+15` | Missing Pauli asymmetry + Coulomb shift |
| High-$A$ Med ($57\text{--}150$) | `514` | `0/514` | `210.2%` | `134.5%` | `1.34e+15` | Isobaric parabola absent in 1D Q-CLT chain |
| Very High-$A$ ($\ge 151$) | `293` | `0/293` | `402.3%` | `191.7%` | `1.92e+15` | Large $Z$ Coulomb gradient omitted |
| **All Measured ($A \ge 1$)** | `1010` | `1/1010` | `255.5%` | `142.4%` | `1.42e+15` | Only $A=1$ exothermic without 3D/Coulomb closure |

*Assessment ($\beta$-Decay):* On the single-nucleon baseline, the $T^3$ weight-trace split on the cost-minimal $\gamma\gamma$-reachable Borromean braid $V^3 = (\sigma_1 \sigma_2^{-1})^3$ (conditional on conjectures `C1–C3`) gives $Q_{\beta^-}(n) = 0.325434\;\mathrm{MeV}$ (`-58.40%` vs `0.782334 MeV`). For composite nuclei ($A \ge 2$), bare monotone transfer-matrix skein shifts (`Table 3.4a`) land in the physical keV–MeV window (best at ${}^{14}\mathrm{C}$, `-8.11%`), whereas direct mass-table subtraction $M(Z,N) - M(Z+1,N-1) - m_e$ (`Table 3.4b`) predicts `0 / 1,009` exothermic composite transitions because the 1D chain omits Coulomb repulsion $\propto Z(Z-1)/A^{1/3}$ and Pauli neutron-excess pressure $\propto (N-Z)^2/A$. Absolute $\beta$ half-lives additionally require deriving the electroweak topological crossing count $N_v \approx 1,445,519$ fixing $v_{\mathrm{weak}}$ ($G_F$).

---

### 3.5 Category 5 — $\alpha$-Decay & Heavy / Composite Fission

#### Table 3.5a: Gamow WKB $\alpha$-Tunneling at Experimental $Q_\alpha$ & $N = 126$ Shell Preformation

| Emitter / Mechanism | $(Z, N, A)$ | $Q_\alpha^{\mathrm{AME}}$ (MeV) | $T_{1/2}^{\mathrm{exp}}$ (s) | $T_{1/2}^{\mathrm{model}}$ (s) | $\log_{10}(T_{\mathrm{model}}/T_{\mathrm{exp}})$ (dex) | Factor Error | Notes |
|---|---|---:|---:|---:|---:|---:|---|
| `8Be` (bare WKB, $S_\alpha=1$) | `(4, 4, 8)` | `0.0918` | `8.19e-17` | `6.29e-16` | `+0.885` | `7.68x` | 81.9 as (resonance) |
| `212Po` (bare WKB, $S_\alpha=1$) | `(84, 128, 212)` | `8.9542` | `2.94e-7` | `1.32e-7` | `-0.350` | `2.24x` | 294.4 ns (open shell, N=128) |
| `214Po` (bare WKB, $S_\alpha=1$) | `(84, 130, 214)` | `7.8335` | `1.64e-4` | `1.19e-4` | `-0.139` | `1.38x` | 163.6 us (open shell, N=130) |
| `222Rn` (bare WKB, $S_\alpha=1$) | `(86, 136, 222)` | `5.5904` | `3.30e+5` | `4.60e+5` | `+0.144` | `1.39x` | 3.8215 d (open shell, N=136) |
| `210Po` (bare WKB, $S_\alpha=1$) | `(84, 126, 210)` | `5.4075` | `1.20e+7` | `6.61e+5` | `-1.257` | `18.08x` | Closed $N=126$ shell ($S_\alpha^{\mathrm{emp}} = 0.0553$) |
| `226Ra` (bare WKB, $S_\alpha=1$) | `(88, 138, 226)` | `4.8707` | `5.05e+10` | `7.81e+10` | `+0.189` | `1.55x` | 1600 y (open shell, N=138) |
| `238U` (bare WKB, $S_\alpha=1$) | `(92, 146, 238)` | `4.2699` | `1.41e+17` | `3.58e+17` | `+0.405` | `2.54x` | 4.468 Gy (open shell, N=146) |
| **`210Po` + Mayer–Jensen $S_\alpha^{\mathrm{MJ}}=1/20$** | `(84, 126, 210)` | `5.4075` | `1.20e+7` | `1.32e+7` | **`+0.044`** | **`1.11x`** | Parameter-free $(1h_{9/2}, 3p_{1/2}/2g_{9/2})$ shell preformation |

- **Composite Generation Fission Threshold (`gap3b`):** Machine-checked Hecke algebra identities prove $\sigma_1^9 = P_6(h_0)\sigma_1^3 + h_3 \cdot 1$ and strict super-additivity $Q_3 = E(9) - 3E(3) > 0$ for all $q > 1$ across all four subtracted torus functionals, opening the 3-body decay cut $T(2,9) \to 3\,T(2,3)$ on the second Riemann sheet ($\operatorname{Im} z_{\mathrm{pole}} = -\Gamma_9/2 < 0$) and algebraically excluding a stable fourth odd-torus generation at winding $n = 9$ (Fock-space continuum embedding carried as explicit hypothesis `CompositeT29DecayExclusionHypothesis`).

#### Table 3.5b: Fully Derived $Q_\alpha$ Across Measured Exothermic $\alpha$-Emitters ($N = 1,051$) & Heavy-Emitter Sensitivity

| Regime / Model | Sample / Nuclide | Exothermic ($Q_\alpha^{\mathrm{pred}} > 0$) | $Q_\alpha^{\mathrm{pred}}$ vs $Q_\alpha^{\mathrm{AME}}$ | Relative / `dex` Error | Median Error (`ppQ`) | Tunneling Assessment |
|---|---|---:|---:|---:|---:|---|
| High-$A$ Med ($57\text{--}150$, Q-CLT + $K_4$ $\alpha$) | `N = 178` | `178/178 (100%)` | Med `19.79` vs `1.73 MeV` | Med `1043.2%` (Mean `1265.2%`) | `1.04e+16` | 1D chain underbinds parent/daughter slope $\Delta B/\Delta A$ |
| Very High-$A$ ($\ge 151$, Q-CLT + $K_4$ $\alpha$) | `N = 873` | `873/873 (100%)` | Med `19.79` vs `5.41 MeV` | Med `265.7%` (Mean `445.7%`) | `2.66e+15` | Over-exothermic ($Q_\alpha^{\mathrm{pred}} \approx 21\;\mathrm{MeV}$) without shell/Coulomb |
| **All Measured Exothermic ($A \ge 6$)** | `N = 1051` | `1051/1051 (100%)` | Med `19.79` vs `4.71 MeV` | Med `320.3%` (Mean `584.5%`) | `3.20e+15` | All `1,051` exothermic, but multi-MeV $Q_\alpha$ offset dominates |
| FCC $k=12$ cluster model (`H2_FCC_k12_std`) | `210Po` | `Yes` | `2.18` vs `5.41 MeV` | `-59.7%` (`+32.80 dex` in $T_{1/2}$) | `5.97e+14` | Gamow sensitivity `-5.37 dex/MeV` |
| FCC $k=12$ cluster model (`H2_FCC_k12_std`) | `212Po` | `Yes` | `2.09` vs `8.95 MeV` | `-76.6%` (`+48.24 dex` in $T_{1/2}$) | `7.66e+14` | Gamow sensitivity `-2.39 dex/MeV` |
| FCC $k=12$ cluster model (`H2_FCC_k12_std`) | `238U` | `Yes` | `3.97` vs `4.27 MeV` | `-7.1%` (`+3.15 dex` in $T_{1/2}$) | `7.13e+13` | Gamow sensitivity `-8.52 dex/MeV` |

*Assessment ($\alpha$-Decay):* The barrier-penetration kinematics are quantitatively sound: parameter-free Gamow WKB tunneling with FCC touching radii reproduces half-lives across **24 orders of magnitude** ($10^{-17}\;\mathrm{s}$ to $10^{17}\;\mathrm{s}$) within `0.14–0.89 dex` on open-shell emitters, and the $N=126$ magic-shell suppression in ${}^{210}\mathrm{Po}$ (`-1.26 dex` bare) is closed to **`+0.044 dex` (`10.6%` in $T_{1/2}$)** by the parameter-free Mayer–Jensen combinatorial preformation factor $S_\alpha^{\mathrm{MJ}} = \tfrac{1}{10}\times\tfrac{2}{10} = \tfrac{1}{20}$. Conversely, when $Q_\alpha$ is computed purely from unclosed heavy-nuclide Q-CLT masses (`Table 3.5b`), multi-MeV parent/daughter binding errors are exponentially amplified by the Gamow sensitivity $|\partial \log_{10} T_{1/2}/\partial Q_\alpha| \approx 2.4\text{--}10\;\mathrm{dex/MeV}$, yielding `3.15–48.2 dex` half-life offsets until $A \ge 5$ binding saturation is derived.

---

## 4. Symbolic Q-CLT Proxy Justification & Formal Scope Boundary

Why does the comprehensive nuclear table achieve `~0.57%` rest-mass accuracy across `2,542` measured nuclides while missing `~68.6%` of total nuclear binding energy and failing isobaric $Q_\beta$ / $Q_\alpha$ differences? Both the justification of the symbolic proxy and the exact mathematical reason for its $A \ge 5$ saturation deficit are **machine-checked theorems in Lean 4**:

| Lean 4 Module | Key Machine-Checked Declarations | Mathematical Statement & Physical Consequence |
|---|---|---|
| `QOU.CategoricalMassMarkov` | `CategoricalMassMarkov.ofHecke`, `ofHecke_Φ_apply`, `ofHecke_φ_zero`, `ofHecke_φ_succ` | Constructs the exact categorical mass endomorphism and proves compatibility of the canonical Markov trace $z = q^3/(q^2+1)$ across inductive Hecke tower inclusions $H_n(q) \hookrightarrow H_{n+1}(q)$. Justifies evaluating composite braid traces algebraically without free parameters. |
| `QOU.Observations.QCltNonCommutative` | `class QCltNonCommutative` | Formalizes the non-commutative $q$-Central Limit Theorem interface governing factorized symbolic trace asymptotics (`Exact symbolic (-alpha * ln|tau_M|)`), enabling exact $O(A)$ evaluation across all `14,972` chart-of-nuclides entries with zero fitting. |
| `QOU.MassTheory.AmeBindingNotPairwise` | `ame_b3_ne_zero`, `ame_not_isPairwise` | Proves from $B({}^2\mathrm{H}), B({}^3\mathrm{H}), B({}^4\mathrm{He})$ that the irreducible 3-body cumulant is strictly nonzero ($b_3 \neq 0$): **no pairwise two-body graph Hamiltonian can reproduce light-nuclear binding.** Explains why higher-order $K_A$ plaquette cumulants (`Table 3.2a`) are mathematically mandatory. |
| `QOU.MassTheory.ChainBindingNoSaturationPeak` | `chainPerNucleon_eq_hyperbola`, `chain_no_saturation_peak` | Proves that any 1D nearest-neighbor chain satisfies $B_{\mathrm{chain}}(A)/A = b_2(1 - 1/A)$, which is strictly increasing and bounded above by $b_2 \approx 2.071\;\mathrm{MeV}$ with **no local maximum at $A \approx 56$**. Certifies that `mass-table-comprehensive` (`principled-derivation (Q-CLT proxy)`) is a rigorous 1D baseline, not a complete 3D nuclear shell/cluster theory. |

---

## 5. Open Mathematical Derivations & Deterministic Witness Provenance

### 5.1 Ranked Frontier of Open Derivations

| Priority | Open Problem | Current Quantitative Gap | Downstream Impact When Closed |
|---:|---|---|---|
| **1** | **Muon–Proton $q_0$ Residual ($\Delta_{\mu p}$)** | $m_\mu$ residual `+211.21 ppb` ($9.70\sigma_{\mathrm{exp}}$), equivalent to $\Delta q_0 / q_0 = +11.61\;\mathrm{ppb}$ between muon and proton pins | Unifies lepton and baryon $q_0$ anchors below CODATA $1\sigma$ (`21.8 ppb`) and sharpens $m_\tau/m_e$ resolvent inputs. |
| **2** | **Canonical $\alpha_{\mathrm{EM}}^{-1}$ Arm Selection** | Schwinger Form B is at `-0.365 ppb` ($-2.38\sigma_{\mathrm{exp}}$) vs Chern–Simons tower at `-467.64 ppb` | Establishes a single parameter-free electromagnetic coupling across QED radiative corrections and meson/Coulomb sectors. |
| **3** | **Unconditional Free-Neutron $Q_{\beta^-}$ & $\Delta m_{np}$ Sign** | Conditional $T^3$ weight-trace split gives `0.3254 MeV` vs `0.7823 MeV` (`-58.40%`); $m_n - m_p$ underpredicts by `-0.4569 MeV` | Discharges conjectures `C1–C3`, fixes $m_n$ to sub-ppm accuracy, and anchors the $A=1$ weak-decay threshold. |
| **4** | **$A \ge 5$ 3D Cluster, Pauli & Coulomb Saturation** | 1D Q-CLT proxy underbinds $A \ge 5$ by `~68.6%` (`2.07` vs `~8.5 MeV/A`), inverting composite $Q_{\beta^-}$ and shifting $Q_\alpha$ by `3–45 MeV` | Simultaneously closes medium/heavy nuclear binding $B(Z,N)$, composite $\beta$-stability valleys, and derived heavy-emitter $\alpha$ half-lives. |
| **5** | **Electroweak Brane-Tower Crossing Count $N_v$** | Empirical $G_F$ requires $N_v = v_{\mathrm{weak}}/(E_\times \mu_0) \approx 1,445,519$ (currently uncomputed from tower topology) | Enables first-principles prediction of absolute weak decay rates ($\Gamma_\beta, \tau_n, \tau_\mu$) from $(m_e, q_0)$ alone. |

### 5.2 Redisplay, Regeneration & QA Gate Commands

```bash
# Redisplay the rendered scorecard to stdout (no file writes):
python3 scripts/generate-accuracy-scorecard.py --print

# Regenerate ACCURACY.md after upstream witness updates:
python3 scripts/generate-accuracy-scorecard.py --write

# Run the strict QA gate (witness health + drift check + hygiene + README link):
python3 scripts/generate-accuracy-scorecard.py --check --qa-report

# Run via the unified compute-QA harness:
python3 scripts/compute-qa.py --gate accuracy-scorecard
```

### 5.3 Deterministic Upstream Witness Provenance

`ACCURACY.md` intentionally omits transient git `HEAD` commit hashes and wall-clock timestamps so that the document changes **if and only if** an upstream witness or reference dataset moves:

| Upstream Witness / Dataset | SHA-256 (`[:12]`) | Gate Status | Scorecard Sections Fed |
|---|---:|---|---|
| [`computations/master-atlas-80dps.witness.json`](computations/master-atlas-80dps.witness.json) | `d7c3a972c41a` | `allPassed: true` | §1, §2, §3.1, §3.3, §3.4 |
| [`computations/per-observable-100x-status.witness.json`](computations/per-observable-100x-status.witness.json) | `61658878af7e` | `allPassed: true` | §2, §3.1a, §3.4a |
| [`computations/mass-table-comprehensive.witness.json`](computations/mass-table-comprehensive.witness.json) | `28a5344181a1` | `allPassed: true` | §2, §3.1b–c, §3.2b, §3.4b, §3.5b, §4 |
| [`computations/data/ame2020.json`](computations/data/ame2020.json) | `a74f4204c189` | Reference dataset (`3558` entries) | §2, §3.1b–c, §3.2a–b, §3.4b, §3.5b |
| [`computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/gap1b-4he-tetrahedral-k4-flux-ring.witness.json`](computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/gap1b-4he-tetrahedral-k4-flux-ring.witness.json) | `63f0971cb24d` | `allPassed: true` | §2, §3.2a, §3.5b |
| [`computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b-mtau-s3-circulant-koide-probe.witness.json`](computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b-mtau-s3-circulant-koide-probe.witness.json) | `c0d6c0a4784e` | `allPassed: true` | §2, §3.1a |
| [`computations/probes/gap3b_t29_composite_decay_threshold/gap3b-t29-composite-decay-threshold.witness.json`](computations/probes/gap3b_t29_composite_decay_threshold/gap3b-t29-composite-decay-threshold.witness.json) | `61d781bdf3d8` | `allPassed: true` | §2, §3.5a |
| [`computations/u1-hypercharge-assignment.witness.json`](computations/u1-hypercharge-assignment.witness.json) | `f00e0c3d4ed5` | `allPassed: true` | §2, §3.3a |
| [`computations/charge-coulomb-tn3he-derived.witness.json`](computations/charge-coulomb-tn3he-derived.witness.json) | `0b254a046dd6` | `allPassed: true` | §2, §3.3a |
| [`computations/mirror-nuclei-coulomb-systematics.witness.json`](computations/mirror-nuclei-coulomb-systematics.witness.json) | `1b11035996c1` | `allPassed: true` | §2, §3.3a |
| [`computations/beta-decay-from-q.witness.json`](computations/beta-decay-from-q.witness.json) | `6845cc311b6b` | Audit witness (`verified`) | §2, §3.4a, §5.1 |
| [`computations/probes/alpha_decay_n126_and_derived_qalpha/alpha_decay_n126_qalpha_probe.witness.json`](computations/probes/alpha_decay_n126_and_derived_qalpha/alpha_decay_n126_qalpha_probe.witness.json) | `7b152b846217` | `allPassed: true` | §2, §3.5a–b |
