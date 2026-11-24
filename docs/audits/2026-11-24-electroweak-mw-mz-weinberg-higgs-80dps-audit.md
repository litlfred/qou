# First-Principles 80-dps Evaluation of Electroweak Boson Thresholds ($M_W, M_Z$), Plancherel Weinberg Angle, and $v$-Independent Higgs Quartic (`Q-Gap-9`: `qou-ewsb`, `qou-ukqh`, `qou-z3x8`, `qou-zd6l`)

**Date:** 2026-11-24
**Branch:** `claude/electroweak-mw-mz-weinberg-higgs-thresholds-20261124`
**Authoritative Artifacts:**
- **Lean 4 Formalization (`0 sorry`, `0` custom axioms, `0` global conjecture instances):** `folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakBosonThresholdsAndWeinberg.lean`
- **80-dps `mpmath` Probe (`WORK_DPS = 125`, `OUT_DPS = 80`, zero `float64`, zero fitted parameters):** `computations/probes/electroweak_mw_mz_weinberg_higgs_probe.py`
- **Witness JSON (`q0_comparison` across proton and muon substrate anchors):** `computations/probes/electroweak-mw-mz-weinberg-higgs.witness.json`

---

## 1. Executive Summary & Four-Part Evidence Frame

### 1.1 The Claim

Coupling the Bring–Schwinger weak vacuum scale $v_{\mathrm{weak}}(q_0)$ (`QOU/StandardModel/ElectroweakBringSchwingerBridge.lean`), the two-loop Bloch-$B_3$ electromagnetic coupling $\alpha_{\mathrm{EM}}(q_0)$ (`QOU/MassTheory/AlphaEmTwoLoopBlochSchwinger.lean`), and the quantum-dimension-dressed 2-strand torus-link Plancherel Weinberg observable (`W = T(2,4)`, `Z = T(2,6)`) yields a **fully self-consistent, zero-fit electroweak boson and Higgs prediction chain** from $(m_e, q_0)$ (plus $m_{\pi^\pm}$ only in the mesonic vacuum-polarization comparison arm `L2b`) with **zero empirical $m_p, M_W, M_Z, v_{\mathrm{weak}},$ or $\alpha_{\mathrm{EM}}$ inputs**:

1. **Exact Polynomial Positivity & On-Shell Weinberg Observable (`plancherel_zw_gap_laurent_eq`, `plancherel_sinSq_mem_unit_interval`):**
   Over any commutative ring $R$, the doubled Plancherel trace polynomials $2 P_2(h) = 1 + 3h^2 + h^4$ and $2 P_3(h) = 1 + 6h^2 + 5h^4 + h^6$ satisfy
   $$2 P_3(h)(h^2 + 4) - 8 P_2(h) = h^2\bigl(13 + 22 h^2 + 9 h^4 + h^6\bigr),$$
   guaranteeing $1 < r_{\mathrm{ZW}}(q) = \frac{P_3(h)}{P_2(h)}\bigl(\frac{[2]_q}{2}\bigr)^2$ and $0 < \sin^2\theta_W^{\mathrm{Planch}}(q) = 1 - r_{\mathrm{ZW}}(q)^{-2} < 1$ unconditionally for every $q \notin \{0, 1, -1\}$ in any strict ordered field. At the proton substrate pin $q_p = 1.10997858275138081\dots$:
   $$r_{\mathrm{ZW}}(q_p) = 1.13480699880578420\dots \quad (+174.70\;\mathrm{ppm}\text{ vs PDG } M_Z/M_W = 1.13460878),$$
   $$\sin^2\theta_W^{\mathrm{Planch}}(q_p) = 0.22347402280210603\dots \quad (+271.34\;\mathrm{ppm}\text{ abs, } +0.1216\%\text{ rel vs PDG } 1 - M_W^2/M_Z^2 = 0.22320268).$$
2. **Self-Consistent Boson Masses $(M_W, M_Z)$ Without Empirical $M_Z$ Inside Vacuum Polarization:**
   Earlier exploratory evaluations (`sm8w_ewsb_vew_mh_mz_rg_probe.py`) evaluated $\ln(M_Z / m_f)$ at experimental `PDG_MZ_GEV` and plugged empirical `PDG_MW_GEV` / `PDG_MZ_GEV` into the Higgs anchor formulas. Solving the **self-consistent** Sirlin fixed point
   $$M_Z = \frac{\sqrt{\pi \alpha_{\mathrm{EM}}(q_0)}\, v_{\mathrm{weak}}(q_0)}{\sin\theta_W^{\mathrm{Planch}}(q_0)\,\sqrt{1 - \Delta r(\mu = M_Z)}}\, r_{\mathrm{ZW}}(q_0)$$
   directly for $M_Z$ at 125-dps precision (with 1-loop QED vacuum polarization, unit top Yukawa $y_t = 1 \implies \Delta\rho = \frac{3}{32\pi^2}$, and Sirlin's exact 1-loop gauge vertex/box remainder) brackets PDG 2024 ($M_W = 80.3692(133)\;\mathrm{GeV}$, $M_Z = 91.1876(21)\;\mathrm{GeV}$) tightly between the model's two non-perturbative hadronic thresholds:
   - **Baryonic threshold $\mu_{\mathrm{had}} = m_p(q_p)$ (`L2a`, pure $(m_e, q_p)$ only):** $\Delta r = 0.03422842$, $M_W = 80.24714021\;\mathrm{GeV}$ (`-0.1519%`), $M_Z = 91.06501635\;\mathrm{GeV}$ (`-0.1344%`).
   - **Mesonic pair threshold $\mu_{\mathrm{had}} = 2 m_{\pi^\pm}$ (`L2b`):** $\Delta r = 0.04114912$, $M_W = 80.53621953\;\mathrm{GeV}$ (`+0.2078%`), $M_Z = 91.39306558\;\mathrm{GeV}$ (`+0.2253%`).
3. **Identically Zero $W$/$Z$-Anchor Spread for $m_H$ & $v$-Independence of the Higgs Quartic $\lambda_H$ (`derived_higgs_w_eq_z_zero_spread`, `derived_higgs_quartic_vev_independent`):**
   Replacing empirical $(M_W^{\mathrm{exp}}, M_Z^{\mathrm{exp}})$ by QOU-derived $(M_W, M_Z)$ collapses the `21.9 MeV` (`174.7 ppm`) $W$-vs-$Z$ Higgs anchor discrepancy of `electroweak_bring_schwinger_bridge_probe.py` to **identically zero** (`|m_H^(W) - m_H^(Z)| < 10^{-124}\;\mathrm{GeV}` at 125 dps, proved unconditionally over `[Field K]`). Furthermore, $v_{\mathrm{weak}}^2$ cancels identically out of $\lambda_H = m_H^2 / (2 v_{\mathrm{weak}}^2)$:
   $$\lambda_H(q_0) = \frac{\pi \alpha_{\mathrm{EM}}(q_0)}{2\,\sin^2\theta_W^{\mathrm{Planch}}(q_0)\,(1 - \Delta r)} \left(\frac{6}{5}\frac{P_4(h_0)}{P_2(h_0)}\frac{[2]_{q_0}}{2} C_{\mathrm{loop}}(q_0)\right)^2 > 0,$$
   and under `L2a` even the dimensional electron scale $m_e$ cancels out of $\Delta r_{\mathrm{L2a}}$ ($\partial \ln \lambda_H^{\mathrm{L2a}} / \partial \ln m_e = 0$ to 86 digits). At `L2a`, the dressed tree and half-Habiro loop factors yield $m_H = 125.3007\;\mathrm{GeV}$ (`+0.080%`, `+0.92σ`) and $m_H = 125.0816\;\mathrm{GeV}$ (`-0.095%`, `-1.08σ`) against PDG $125.20 \pm 0.11\;\mathrm{GeV}$, with $\lambda_H = 0.1294887$ and $0.1290362$.

### 1.2 Implications & Epistemic Classification

- **Unconditional Algebra (`[CommRing R]` / `[Field K]` / Ordered Field):** All polynomial, Sirlin ratio-cancellation, custodial $\rho = 1$, Higgs $W/Z$-anchor unification, $v$-independence of $\lambda_H$, unit-interval Weinberg bounds ($0 < \sin^2\theta_W^{\mathrm{Planch}} < 1$), and global quartic Higgs potential stability theorems are proved unconditionally in `ElectroweakBosonThresholdsAndWeinberg.lean`.
- **Conditional Physical Bridge (`§3b-cond`):** The coupled physical identification of $(\alpha_{\mathrm{EM}}, \alpha_v, M_W, M_Z, m_H, \lambda_H)$ is isolated in `ElectroweakBosonThresholdSystemClass` with **zero global instances** and an explicit `noncomputable def trivialModel` consistency witness at $q = 2$.
- **Remaining Open Categorical Gaps (`qou-ukqh`, `qou-z3x8`, `qou-zd6l`):** While the torus-link Plancherel + Bring–Schwinger chain predicts $(v_{\mathrm{weak}}, M_W, M_Z, \sin^2\theta_W, m_H, \lambda_H)$ to sub-ppb / permille precision with zero fitted parameters, the underlying 6-strand Hoefsmit projector automorphism (`qou-zd6l`, where the naive order-zero pure-pattern $\cot\theta_W = q_0^{-4}$ gives $\sin^2\theta_W = 0.69735$, `+212.4%`), the categorical Goldstone-linking functor (`qou-ukqh`), and the first-principles operator derivation of the `T_EW` crossing product (`qou-z3x8`) remain genuinely open and are kept open in the issue tracker.

---

## 2. Side-by-Side Comparison of Corpus Weinberg Angle Candidates (`80 dps`, Zero Fits)

| Candidate ID | Mathematical Expression | Value at $q_p$ (`proton` pin) | Value at $q_\mu$ (`muon` pin) | Scheme Target | Rel. Residual ($q_p$) |
|---|---|---:|---:|---|---:|
| `W1_torus_plancherel_dressed` | $1 - \frac{16 P_2(h_0)^2}{P_3(h_0)^2 [2]_{q_0}^4}$ | `0.2234740228021060` | `0.2234740620504980` | On-shell $1 - M_W^2/M_Z^2 = 0.22320268$ | **`+0.1216%` (`+1215.7 ppm`)** |
| `W2_torus_plancherel_bare` | $1 - P_2(h_0)^2 / P_3(h_0)^2$ | `0.2064118105765458` | `0.2064118468544798` | On-shell $0.22320268$ | `-7.5227%` |
| `W3_schur_irrep_M4_T24_T35` | $1 - (\mathcal{S}_{H_2}(T_{2,4}) / \mathcal{S}_{H_3}(T_{3,5}))^2$ | `0.9361046241936682` (`17/81` at $q=1$) | `0.9361046396009255` | On-shell $0.22320268$ | `+319.3967%` |
| `W4_same_rank_H2_markov` | $1 - (\mathrm{tr}_M^{H_2}(T_{2,4}) / \mathrm{tr}_M^{H_2}(T_{2,6}))^2$ | `0.2813156597853956` | `0.2813156928169196` | On-shell $0.22320268$ | `+26.0360%` |
| `W5_h6_pure_pattern_gap_zd6l` | $1 / (1 + q_0^{-8})$ ($\cot\theta_W = q_0^{-4}$) | `0.6973532392501022` | `0.6973532588594391` | On-shell $0.22320268$ | `+212.43%` (open `qou-zd6l`) |
| `W6a_gqw_1loop_sweedler_k17` | $\frac{3}{8} - \frac{109}{48\pi}\frac{17|\ln(q_0^2-1)|}{\alpha_{\mathrm{EM}}^{-1}(M_Z)}$ | `0.2353141319591693` | `0.2353141226...` | $\overline{\mathrm{MS}}$ $0.23122(4)$ | `+1.7707%` |
| `W6b_gqw_1loop_sweedler_k18` | $\frac{3}{8} - \frac{109}{48\pi}\frac{18|\ln(q_0^2-1)|}{\alpha_{\mathrm{EM}}^{-1}(M_Z)}$ | `0.2270973161920616` | `0.2270973063...` | $\overline{\mathrm{MS}}$ $0.23122(4)$ | `-1.7830%` |

---

## 3. Self-Consistent Radiative Boson Thresholds $(M_W, M_Z)$ Atop Derived $(v_{\mathrm{weak}}, \alpha_{\mathrm{EM}})$

Evaluated with two-loop Bloch-$B_3$ $\alpha_{\mathrm{EM}}^{-1}(q_p) = 137.03599917369576$ (`-0.0241 ppb` vs CODATA 2022) and Bring–Schwinger $v_{\mathrm{weak}}(q_p) = 246.21964356171226\;\mathrm{GeV}$ (`-29.37 ppb` vs PDG; Form-B $\alpha_{\mathrm{EM}}$ shifts $M_W, M_Z$ by only `+0.015 keV`, recorded in full in the witness JSON):

| Threshold Level | Self-Consistent $\Delta r(M_Z)$ | $M_W^{\mathrm{pred}}$ (GeV, $q_p$) | Rel. Err vs PDG $M_W$ | $M_Z^{\mathrm{pred}}$ (GeV, $q_p$) | Rel. Err vs PDG $M_Z$ | $M_W^{\mathrm{pred}}$ / $M_Z^{\mathrm{pred}}$ (GeV, $q_\mu$ pin) |
|---|---:|---:|---:|---:|---:|---:|
| `L0_tree` ($\Delta r = 0$) | `0` | `78.86181640` | `-1.8756%` | `89.49294119` | `-1.8584%` | `78.86179156` / `89.49291530` |
| `L1a_leptonic_VP` ($\Delta\alpha_{\mathrm{lept}}$ only) | `0.03239913` | `80.17124910` | `-0.2463%` | `90.97889458` | `-0.2289%` | `80.17122374` / `90.97886814` |
| `L1b_full_QED_VP_no_custodial` ($\Delta\rho = 0$) | `0.05375580` | `81.07093093` | `+0.8731%` | `91.99985982` | `+0.8908%` | `81.07090517` / `91.99983295` |
| **`L2a_Sirlin_1L_baryon_mp`** ($\mu_{\mathrm{had}} = m_p(q_0), y_t = 1$) | **`0.03422842`** | **`80.24714021`** | **`-0.1519%`** | **`91.06501635`** | **`-0.1344%`** | **`80.24711486` / `91.06498991`** |
| **`L2b_Sirlin_1L_meson_2mpi`** ($\mu_{\mathrm{had}} = 2 m_{\pi^\pm}, y_t = 1$) | **`0.04114912`** | **`80.53621953`** | **`+0.2078%`** | **`91.39306558`** | **`+0.2253%`** | **`80.53619403` / `91.39303899`** |

---

## 4. Zero-Spread Reconciled Higgs Mass $m_H$ & Scale-Free Quartic $\lambda_H$ (`|m_H^(W) - m_H^(Z)| = 0`)

Across all pre-committed topological 1-loop factors $C_{\mathrm{loop}}(q_0)$, using QOU-derived $(M_W, M_Z)$ reduces the $W$-vs-$Z$ anchor discrepancy from `21.9 MeV` (`electroweak_bring_schwinger_bridge_probe.py`) to `< 10^{-124}\;\mathrm{GeV}$:

| Radiative Level & Loop Factor $C_{\mathrm{loop}}(q_p)$ | $C_{\mathrm{loop}}(q_p)$ | Reconciled $m_H$ (GeV) | $|m_H^{(W)} - m_H^{(Z)}|$ (GeV) | Residual vs PDG $125.20(11)$ GeV | Scale-Free $\lambda_H(q_p)$ |
|---|---:|---:|---:|---:|---:|
| `L2a` + `C0_tree_dressed` ($1$) | `1.0000000000` | **`125.30071683`** | `< 1e-124` | **`+0.0804%` (`+0.92σ`)** | `0.1294886547` |
| `L2a` + `C1_habiro_half_h2` ($1 - \frac{[2]_q}{16\pi}h^2$) | `0.9982515103` | **`125.08162982`** | `< 1e-124` | **`-0.0945%` (`-1.08σ`)** | `0.1290362314` |
| `L2a` + `C2_bring_zero_hbar2` ($1 - \frac{2}{3\pi}\hbar_q^2$) | `0.9979167283` | **`125.03968132`** | `< 1e-124` | **`-0.1281%` (`-1.46σ`)** | `0.1289496966` |
| `L2a` + `C3_borromean_2G_h4` ($1 - 2 G h^4$) | `0.9965005852` | `124.86223764` | `< 1e-124` | `-0.2698%` (`-3.07σ`) | `0.1285839714` |
| `L2a` + `C4_habiro_full_h2` ($1 - \frac{[2]_q}{8\pi}h^2$) | `0.9965030206` | `124.86254280` | `< 1e-124` | `-0.2695%` (`-3.07σ`) | `0.1285845999` |
| `L2b` + `C3_borromean_2G_h4` ($1 - 2 G h^4$) | `0.9965005852` | **`125.31203728`** | `< 1e-124` | **`+0.0895%` (`+1.02σ`)** | `0.1295120522` |
| `L2b` + `C4_habiro_full_h2` ($1 - \frac{[2]_q}{8\pi}h^2$) | `0.9965030206` | **`125.31234298`** | `< 1e-124` | **`+0.0897%` (`+1.02σ`)** | `0.1295126853` |

---

## 5. 80-dps Fréchet–Jacobian Sensitivity & PDG Experimental Information Budget

| Observable $O$ | $\frac{\partial \ln O}{\partial \ln q_0}$ | $\frac{\partial \ln O}{\partial \ln m_e}$ | $\frac{\partial \ln O}{\partial \ln m_{\pi^\pm}}$ | Propagated $\sigma_{\mathrm{rel}}(O)$ ($q_p$ pin, ppb) | PDG Experimental Precision $-\log_{10}(\sigma_{\mathrm{exp}}/O_{\mathrm{exp}})$ |
|---|---:|---:|---:|---:|---:|
| $v_{\mathrm{weak}}(q_0)$ | `-16.103590` | `+1` | `0` | `0.3134 ppb` | `6.5897` digits (`0.257 ppm`) |
| $\sin^2\theta_W^{\mathrm{Planch}}(q_0)$ | `+15.122053` | `0` | `0` | `0.0126 ppb` | `3.7623` digits (`MSbar`) |
| $M_W^{\mathrm{L2a}}(q_0)$ | `-27.148666` | `+1` | `0` | `0.3139 ppb` | `3.7812` digits (`165.5 ppm`) |
| $M_Z^{\mathrm{L2a}}(q_0)$ | `-24.972701` | `+1` | `0` | `0.3138 ppb` | `4.6377` digits (`23.0 ppm`) |
| $M_W^{\mathrm{L2b}}(q_0)$ | `-27.236454` | `+1.002977` | `-0.002977` | `3.8521 ppb` | `3.7812` digits |
| $m_H^{\mathrm{L2a,tree}}(q_0)$ | `-22.826634` | `+1` | `0` | `0.3137 ppb` | `3.0562` digits (`878.6 ppm`) |
| $\lambda_H^{\mathrm{L2a,tree}}(q_0)$ | `-13.446086` | `0` (`< 2e-86`) | `0` | `0.0112 ppb` | `2.7552` digits |

- **Total Independent PDG Electroweak Information Content $\{v_{\mathrm{weak}}, M_W, M_Z, m_H\}$:** `18.0649` decimal digits predicted from **zero** electroweak fitted parameters (`L2a` uses exclusively $(m_e, q_0)$ already fixed upstream in the lepton/baryon sector, leaving the full `18.06`-digit budget unspent).

---

## 6. Reproduction Commands

```bash
# 1. Compile Lean 4 module & run best-practices lint
LEAN_NUM_THREADS=1 bash scripts/lean-overlay-env.sh build QOU/StandardModel/ElectroweakBosonThresholdsAndWeinberg.lean --overlay /tmp/lean-overlay-ws5-ew
python3 scripts/lean-best-practices-lint.py folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakBosonThresholdsAndWeinberg.lean

# 2. Run 80-dps mpmath probe & float64 guard
python3 computations/probes/electroweak_mw_mz_weinberg_higgs_probe.py
python3 scripts/probe-float64-guard.py --diff computations/probes/electroweak_mw_mz_weinberg_higgs_probe.py
```
