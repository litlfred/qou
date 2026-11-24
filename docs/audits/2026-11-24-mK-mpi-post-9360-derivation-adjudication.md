# Post-`#9360` First-Principles Derivation & Epistemic Adjudication of the Meson Ratio $m_K / m_\pi$ (`qou-3l2l`, `qou-5ipv`)

**Date:** 2026-11-24  
**Beans:** `qou-3l2l`, `qou-5ipv` (Issue `#9369`)  
**Supersedes / Updates:** [`2026-08-22-mK-mpi-l2-red-team.md`](2026-08-22-mK-mpi-l2-red-team.md)  
**80-dps Probe:** [`meson_kaon_pion_derivation_probe.py`](../../computations/mesons/meson_kaon_pion_derivation_probe.py)  
**Witness:** [`meson_kaon_pion_derivation_probe.witness.json`](../../computations/mesons/meson_kaon_pion_derivation_probe.witness.json)  
**Lean 4 Formalization (`§7c` Split, `0 sorry`, `0` custom axioms):**
- Generic (`[CommRing A]` / `[Field K]`): [`MesonThreeByFourCharacterization.lean`](../../folio/quantum-observable-universe/lean/QOU/EightfoldWay/MesonThreeByFourCharacterization.lean)
- Archimedean (`ℝ` + `§3b-cond` class): [`MesonKaonPionSchwingerBridge.lean`](../../folio/quantum-observable-universe/lean/QOU/EightfoldWay/MesonKaonPionSchwingerBridge.lean)

---

## Executive Verdict

Following the retirement of the quadratic series truncation (`#5467`), the `0`-`sorry` homological Seifert pairing derivation (`#9359`), and the `0`-`sorry` four-topology `EmFermionLoop` Bring–Schwinger formalization (`#9360`), the three objections raised in [`2026-08-22-mK-mpi-l2-red-team.md`](2026-08-22-mK-mpi-l2-red-team.md) separate cleanly into **two closed items** and **two sharply localized `§3b-cond` structural hypotheses**:

1. **Quadratic truncation `(3q² - 1)/(2q²)` — CLOSED (`#5467`).** Replaced by the untruncated factor $1 + \ln(1 + \hbar_q)$ (`\hbar_q = 1 - q^{-1}`).
2. **Conditional Witten-`κ` `sorry` in $\alpha_{\mathrm{EM}}$ — DISCHARGED AS NON-LOAD-BEARING (`#9359`, `#9360`, proved Lipschitz bound).** Evaluating $\sqrt{[3]_q[4]_q + \frac{\alpha_{\mathrm{EM}}}{\pi}(1 + \ln(1 + \hbar_q))}$ at 80 decimal places across every `0`-`sorry` derived electromagnetic coupling on `main` shifts $m_K / m_\pi$ by **at most `0.048 ppb`** across loop-dressed arms (proved via `meson_ratio_alpha_lipschitz_bound`):
   - **1-loop Bring–Schwinger (`#9360`, `0 sorry`)**: **`+51.4279 ppb`** at $q_{\mathrm{proton}}$ (`+56.0167 ppb` at $q_{\mathrm{muon}}$),
   - **2-loop Bloch-$B_3(\mathbb{C})$ `EmFermionLoop` (`#9360`)**: **`+51.4279 ppb`** at $q_{\mathrm{proton}}$ (`+56.0167 ppb` at $q_{\mathrm{muon}}$),
   - **Homological Seifert pairing $\kappa_{\mathrm{Seifert}}$ (`#9359`, `0 sorry`)**: **`+51.4304 ppb`** at $q_{\mathrm{proton}}$ (`+56.0192 ppb` at $q_{\mathrm{muon}}$),
   - **Witten Chern–Simons resummation**: `+51.4754 ppb` at $q_{\mathrm{proton}}$ (`+56.0642 ppb` at $q_{\mathrm{muon}}$),
   - **Unconditional tree coupling $\alpha_{\mathrm{tree}}^{-1} = q[9]_q[10]_q = 136.8232$ (`0` loops, `0 sorry`)**: **`+209.4377 ppb`** at $q_{\mathrm{proton}}$ (`+214.0265 ppb` at $q_{\mathrm{muon}}$) — *already inside* the `263.6457 ppb` ($\sigma_{\mathrm{exp}} / 100$) threshold (`0.794×` of target; correcting an earlier rough note that mixed up the `R²` residual `+418.88 ppb` with the linear `R` residual `+209.44 ppb`).
3. **Why `(3, 4)` in `[3]_q [4]_q` — CHARACTERIZED ALGEBRAICALLY, NOT UNCONDITIONALLY DERIVED (`§3b-cond`).**
   - *Positive characterization (`MesonThreeByFourCharacterization.lean`)*: In the Eightfold Way split bundle $F = V_2 \oplus W_3^*$, the diquark square splits as $\dim_q(W_3^*)^2 = \dim_q(\Lambda_q^2 W_3^*) + \dim_q(\operatorname{Sym}_q^2 W_3^*) = [3]_q + \frac{[3]_q[4]_q}{[2]_q}$, and tensoring the symmetric diquark $\operatorname{Sym}_q^2 W_3^*$ with the weak-isospin doublet $V_2$ ($\dim_q V_2 = [2]_q$) gives **exact** quantum dimension $\dim_q(V_2 \otimes \operatorname{Sym}_q^2 W_3^*) = [3]_q [4]_q$, coinciding with the spin-$j = 3$ $U_q(\mathfrak{sl}_2)$ Casimir eigenvalue $[3]_q [4]_q = [2]_q + [4]_q + [6]_q$. Furthermore, among all classical factorizations $a \cdot b = 12$, $(3, 4)$ is proved to be the **unique minimal-$q$-curvature pair** for all $q > 0, q \neq 1$:
     $$[2]_q[6]_q - [3]_q[4]_q = (q + q^{-1} - 2)\,[2]_q\,[3]_q\,([2]_q + [3]_q) > 0, \qquad [1]_q[12]_q - [2]_q[6]_q = (q + q^{-1} - 2)\,[6]_q\,([2]_q + [3]_q)\,([3]_q + [4]_q) > 0.$$
   - *Exact obstruction (`involutive_odd_clasp_independent_of_generations`)*: In any specialization of the Hecke algebra $H_3(q)$ at $q = 1$ ($s_1^2 = s_2^2 = 1$), every odd-winding 3-strand gluon-clasp word $s_1^{2k_1+1} s_2^{2k_2+1} s_1 s_2$ ($\pi = (3,3)$, $K = (3,5)$, $\phi = (5,5)$) collapses to the **same** element $(s_1 s_2)^2$. Consequently, **every** bare $H_3(q)$ trace/Markov ratio between $(3, 5)$ and $(3, 3)$ converges to $1 \neq 12$ as $q \to 1$ (`0.8089` at $z_2$ and `0.8678` at $z_3$ at $q_{\mathrm{proton}}$; `SL₂(ℤ)` monodromy trace ratio `41/27 = 1.5185`), while the intra-octet multiplicity ratio in $\mathbf{8} \subset W_3 \otimes W_3^*$ is $[4]_q / [3]_q \approx 1.353 \neq 12.509$. Identifying $m_K^2 / m_\pi^2|_{\mathrm{strong}}$ with $[3]_q [4]_q$ (equivalently $m_s / m_d = 2[3]_q[4]_q - 1 = 24.0173$ in isospin-symmetric Gell-Mann–Oakes–Renner) therefore requires an explicit channel-selection premise and cannot be claimed as an unconditional derivation.
4. **Why $+\frac{\alpha_{\mathrm{EM}}}{\pi}(1 + \ln(1 + \hbar_q))$ — PROPER-TIME INTEGRAL PROVED, UV ENDPOINT & DASHEN SIGN LOCALIZED (`§3b-cond`).**
   - *Proper-time structure (`meson_em_schwinger_proper_time_decomp`, `reeb_vs_planck_schwinger_uv_gap`)*: Under the unique scale-invariant Schwinger proper-time density $\frac{ds}{s}$ (`SchwingerMeasureShape.scale_invariant_density_unique`, unit-normalized to 1 nat per proper-time e-fold $\int_{e^{-1}}^1 \frac{ds}{s} = 1$), the factor $1 + \ln(1 + \hbar_q) = 1 + \ln\!\left(\frac{2q-1}{q}\right)$ is the exact integral over $[e^{-1}, 1] \cup [1, 1 + \hbar_q]$ (1-nat infrared core plus additive Planck UV excursion). However, replacing the additive UV endpoint $1 + \hbar_q = 2 - q^{-1}$ by the multiplicative Reeb step $q = (1 - \hbar_q)^{-1}$ (`[1, q]`) yields $1 + \ln q$, separated by the exact positive gap:
     $$(1 + \ln q) - \bigl(1 + \ln(1 + \hbar_q)\bigr) = -\ln(1 - \hbar_q^2) > 0$$
     (`+967.26 ppb` vs `+51.43 ppb` on $m_K / m_\pi$). Because experimental kaon uncertainty is $\sigma_{\mathrm{exp}}(m_K / m_\pi) = 26,364.6\text{ ppb}$ ($\sigma(F_{\mathrm{EM}}) = \pm 0.2840$), **both** UV endpoints sit deep inside $0.04\,\sigma_{\mathrm{exp}}$ (`+0.0020 σ_exp` vs `+0.0367 σ_exp`), so data cannot adjudicate between them and a worldline boundary proof is required.
   - *Dashen chiral sign obstruction (`dashen_equal_em_shift_identity`, `dashen_equal_em_lowers_ratio_real`)*: Adding an equal positive pointlike electromagnetic mass-squared shift $\Delta_{\mathrm{EM}} > 0$ (Dashen's leading-order chiral limit, $\Delta_{\mathrm{EM}} \approx m_{\pi^\pm}^2 - m_{\pi^0}^2 = +1261.16\text{ MeV}^2$) to neutral strong baselines with $R_0 > 1$ **lowers** the charged ratio:
     $$\frac{R_0 m_0^2 + \Delta_{\mathrm{EM}}}{m_0^2 + \Delta_{\mathrm{EM}}} - R_0 = -\frac{(R_0 - 1)\,\Delta_{\mathrm{EM}}}{m_0^2 + \Delta_{\mathrm{EM}}} < 0 \qquad (-59,553.7\text{ ppm at } R_0 = [3]_q[4]_q).$$
     Hence $+\frac{\alpha_{\mathrm{EM}}}{\pi}(1 + \ln(1 + \hbar_q)) > 0$ (`+203.3 ppm`) cannot arise from equal additive Dashen self-energies on neutral masses; $[3]_q [4]_q$ must already be anchored at the charged-pion scale $m_{\pi^\pm}^2$ and the positive $+\frac{\alpha_{\mathrm{EM}}}{\pi}(1 + \ln(1 + \hbar_q))$ term represents a flavor-asymmetric radiative worldline correction packaged in `MesonKaonPionGMOREmBridgeClass` (`§3b-cond`, zero global instances).

---

## 80-dps Multi-Arm Matrix (`q_proton` vs `q_muon`, Zero Fitted Parameters)

Experimental validation reference (PDG 2024): $m_{K^\pm} / m_{\pi^\pm} = 493.677(13) / 139.57039(18) = 3.5371184389\dots$, $\sigma_{\mathrm{exp}} = 26,364.57\text{ ppb}$, $\sigma_{\mathrm{exp}} / 100 = 263.65\text{ ppb}$.

| Electromagnetic Coupling Arm ($\alpha_{\mathrm{EM}}^{-1}$ derived at pin) | $\alpha_{\mathrm{EM}}^{-1}(q_{\mathrm{proton}})$ | $m_K/m_\pi$ Err @ $q_{\mathrm{proton}}$ | $m_K/m_\pi$ Err @ $q_{\mathrm{muon}}$ | `sorry`-free $\alpha_{\mathrm{EM}}$ algebra? |
|---|---:|---:|---:|:---:|
| Strong core only ($\alpha_{\mathrm{EM}} \to 0$, $\sqrt{[3]_q[4]_q}$) | — | `-101,553.36 ppb` | `-101,548.76 ppb` | Yes |
| **1-Loop Bring–Schwinger (`#9360` 4-topology `EmFermionLoop`)** | `137.0359991270` | **`+51.4279 ppb`** (`+0.0020σ`) | **`+56.0167 ppb`** | **Yes** |
| **2-Loop Bloch-$B_3(\mathbb{C})$ `EmFermionLoop` (`#9360`)** | `137.0359991737` | **`+51.4279 ppb`** (`+0.0020σ`) | **`+56.0167 ppb`** | **Yes** |
| **Homological Seifert Pairing $\kappa_{\mathrm{Seifert}}$ (`#9359`)** | `137.0359958151` | **`+51.4304 ppb`** (`+0.0020σ`) | **`+56.0192 ppb`** | **Yes** |
| Witten Chern–Simons Tower (`meson_em_sinh_closed_form`) | `137.0359350940` | `+51.4754 ppb` (`+0.0020σ`) | `+56.0642 ppb` | Conditional |
| Quadratic 1-Loop Bring–Schwinger (`c_loop = 0`) | `137.0359993132` | `+51.4278 ppb` (`+0.0020σ`) | `+56.0166 ppb` | Yes |
| **Unconditional Tree $\alpha_{\mathrm{tree}}^{-1} = q[9]_q[10]_q$ (`0` loops)** | `136.8232088536` | **`+209.4377 ppb`** (`+0.0079σ`) | **`+214.0265 ppb`** | **Yes** |
| *(CODATA 2022 reference control — not a model arm)* | `137.0359991770` | `+51.4279 ppb` | `+56.0248 ppb` | — |
