# Audit: Are Any of QOU's Algebraic Invariants Related to the Higgs Sector? (`2026-11-28`)

**Date:** 2026-11-28  
**Owner Research Question:** *"are any of the alg invariants related to higgs?"*  
**Pin & Anti-Fit Discipline:** Strictly proton-pinned $q_0^{(p)} = q_{\mathrm{at}}(105) = 1.10997858275138080759\ldots$ (`q0Anchor = "proton"`, `physical_proton` in `computations/q0_anchor_manifest.json`; muon pin on hold per owner ruling `2026-11-28`), `80`-dps `mpmath` (`WORK_DPS = 105`, `probe-float64-guard` clean), **zero fitted parameters**.

## Artefacts Delivered

1. **Lean 4 Formalization (`0 sorry`, standard axioms only, `[CommRing R]`, `0` `[Field]`/`field_simp`, `0` transcendental tokens):**  
   [`folio/quantum-observable-universe/lean/QOU/StandardModel/OqSU2HaarYukawaAndPodlesHiggs.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/OqSU2HaarYukawaAndPodlesHiggs.lean) (wired into `QOU.lean`)
2. **80-dps Proton-Pinned Verification Probe & Witness:**  
   [`computations/probes/higgs_algebraic_invariants_audit_probe.py`](../../computations/probes/higgs_algebraic_invariants_audit_probe.py) & [`computations/probes/higgs-algebraic-invariants-audit-probe.witness.json`](../../computations/probes/higgs-algebraic-invariants-audit-probe.witness.json)
3. **Primary-Verified NCG / Quantum-Group / Electroweak References Ingested (`8` CSL-JSON entries):**  
   `connes-lott1990`, `chamseddine-connes-2012-resilience`, `dubois-violette-kerner-madore1990a`, `dubois-violette-kerner-madore1990b`, `hajac-majid1999`, `dabrowski-sitarz2003`, `klimyk-schmudgen1997`, `sirlin1980` (joining existing `connes1994`, `connes1996`, `chamseddine-connes-1997`, `podles1987`, `dabrowski-landi-sitarz-vansuijlekom-varilly2005`).

---

## 1. Current Corpus Status of QOU's Higgs Sector

- **`tbl:intro-sm-26-parameters` (`intro-sm-26-parameters.md`) & `sm-params-higgs.md`:**
  - **$v_{\mathrm{weak}}$:** *Conditional* — derived via `ElectroweakBringSchwingerBridge` + `ElectroweakConditionalDischarge` (`#10005`, conditional surface reduced to 2 premises: tree crossing product $T_{\mathrm{EW}}$ + Habiro 1-loop normalization, with `BringMapChain` $g = 4 \implies c_0 = 1/\pi$ and $\mathrm{SU}(2)_L$ asymptotic-freedom sign $+1$ proved unconditionally). At $q_0^{(p)}$, $N_v = 262.418169$, $v_{\mathrm{weak}} = 246.21964356\;\mathrm{GeV}$ (`-29.37 ppb = -0.11σ` vs PDG $G_F$).
  - **$m_H$ & $\lambda_H = m_H^2 / (2 v_{\mathrm{weak}}^2)$:** *Conjectural / Open* (not yet promoted to a scored row in `ACCURACY.md`). Assigned to the 2-component torus link $T(2, 8)$ alongside $W = T(2,4), Z = T(2,6)$ (`conj:electroweak-higgs-torus-link-triplet`), with an interpretive Yukawa-coupling role for $4_1$ in `cal2-higgs-knot-coupling.md`.
  - **Self-consistent `L2a` Plancherel + Sirlin chain (`ElectroweakBosonThresholdsAndWeinberg.lean`):** Using pure $(m_e, q_0^{(p)})$ inputs, $|m_H^{(W)} - m_H^{(Z)}| = 0$ identically, $v_{\mathrm{weak}}$ and $m_e$ cancel out of $\lambda_H$, and at $q_0^{(p)}$:
    - `C0_tree_dressed` ($C_{\mathrm{loop}} = 1$): $m_H = 125.300717\;\mathrm{GeV}$ (**`+0.0804% = +0.92σ`** vs PDG 2024 $125.20 \pm 0.11\;\mathrm{GeV}$), $\lambda_H = 0.12948865$;
    - `C1_habiro_half_h2` ($1 - \frac{[2]_q}{16\pi}h^2$): $m_H = 125.081630\;\mathrm{GeV}$ (**`-0.0945% = -1.08σ`**), $\lambda_H = 0.12903623$;
    - `C2_bring_zero_hbar2` ($1 - \frac{2}{3\pi}\hbar_q^2$): $m_H = 125.039681\;\mathrm{GeV}$ (**`-0.1281% = -1.46σ`**), $\lambda_H = 0.12894970$.
  - **Why $m_H$ remains *Conjectural*:** The rational scalar-to-gauge factor $6/5 = \dim H_3 / \dim Z(H_4)$ (`HiggsCategoricalMassFormula.lean`), the categorical Goldstone/vacuum functor (`qou-ukqh`), Yukawa strand order (`qou-99qc`), and the 6-strand Hoefsmit Weinberg automorphism (`qou-zd6l`) had not been unified with QOU's $\mathcal{O}_q(\mathrm{SU}(2))$ substrate.

---

## 2. Five Exact Structural Bridges Proved in `OqSU2HaarYukawaAndPodlesHiggs.lean` (`0 sorry`)

1. **Bridge 1 — Woronowicz $\mathcal{O}_q(\mathrm{SU}(2))$ Haar Eigenvalues $\equiv$ Jimbo Singlet Yukawa VEV Weights (`haar_eq_jimbo_yukawa_weights_and_variance`, `qou-99qc`):**
   - The diagonal VEV compression weights of the Jimbo right-handed singlet projector $P_R = [2]_q^{-1}(q I_4 - \check{R})$ (`YukawaStrandOrder.lean`) are **identically Woronowicz's reduced spin-$1/2$ Haar modular eigenvalues** on $\mathcal{O}_q(\mathrm{SU}(2))$:
     $$p_+(q_0) = h(\delta\alpha) = \frac{q_0^2}{1 + q_0^2} = (P_R)_{1,1} = 0.55198185502621\ldots, \qquad p_-(q_0) = h(\alpha\delta) = \frac{1}{1 + q_0^2} = (P_R)_{2,2} = 0.44801814497379\ldots.$$
   - Flavour-blindness of the partial trace $\mathrm{ptr}_R(P_R, a, b)$ holds **if and only if $a = q^2 b$** — identically Woronowicz's KMS modular swap relation $h(\delta\alpha) = q^2 h(\alpha\delta)$.
   - For $q_0 > 1$, KMS positivity $p_-(q_0) < \tfrac{1}{2} < p_+(q_0)$ (`haar_kms_breaks_yukawa_order`) canonically breaks the `matter ⊗ Higgs` vs `Higgs ⊗ matter` tie by the Haar polarization bias $p_+(q_0) - p_-(q_0) = \frac{q_0^2 - 1}{q_0^2 + 1} = \tanh(\ln q_0) = 0.10396371005241\ldots$.
2. **Bridge 2 — Electroweak `[2]_q / 2` Dressing $\equiv$ Inverse Woronowicz Haar Variance (`haar_eq_jimbo_yukawa_weights_and_variance`):**
   - Because $[2]_q^2 \cdot h(\delta\alpha) h(\alpha\delta) = 1$ identically over `[CommRing R]`, the quantum-dimension dressing factor $([2]_{q_0}/2)^2 = 1.0109265522\ldots$ governing $r_{\mathrm{ZW}}$, $T_{\mathrm{EW}}$, and $m_H/M_W$ equals $(4\,p_+(q_0)\,p_-(q_0))^{-1}$ (`p_+ p_- = [2]_{q_0}^{-2} = 0.2472978867...`).
3. **Bridge 3 — Hajac–Majid / Podleś $q$-Monopole Projector Concrete Vacuum Realization (`podlesProj_*`, `qou-ukqh`):**
   - On $\mathcal{O}_q(\mathrm{SU}(2))$, the charge-$(+1)$ spinor column $v = (\alpha, \gamma)^T$ and charge-$(-1)$ adjoint row $v^* = (\delta, -q^{-1}\beta)$ satisfy the exact noncommutative nonlinear-$\sigma$ Higgs constraint $v^* v = \delta\alpha - q^{-1}\beta\gamma = 1$ (`hopfRow_dot_hopfCol_eq_one`).
   - Their outer product $e_{\mathrm{Podle\acute{s}}} = v v^* \in M_2(\mathcal{O}_q(\mathrm{SU}(2)))$ satisfies $e_{\mathrm{Podle\acute{s}}}^2 = e_{\mathrm{Podle\acute{s}}}$, $(e_{ij})^* = e_{ji}$, descends to $\mathcal{O}(S^2_q) = \mathcal{O}_q(\mathrm{SU}(2))^{\mathrm{U}(1)}$, and has **exact quantum pivotal trace $e_{00} + q^2 e_{11} = \alpha\delta - q\beta\gamma = 1$** (concretely realizing `HiggsVacuumResidual.VacuumPairing`), whereas its ordinary matrix trace $e_{00} + e_{11} = 1 + (q - q^{-1})\beta\gamma$ has Haar expectation $\frac{2}{1+q_0^2} = 0.8960362899\ldots$ (defect $\tanh(\ln q_0)$) and the classical determinant defect $1 - (\alpha\delta - \beta\gamma)$ has Haar expectation $\frac{q_0 - 1}{[2]_{q_0}} = 0.0546913094\ldots$.
4. **Bridge 4 — Podleś Equatorial Kurtosis $[2]_q^2 / [3]_q$ & Universal $v^2$-Cancellation (`podles_radial_kurtosis_identities`, `higgs_quartic_cleared_vev_cancellation`):**
   - Both Chamseddine–Connes spectral-action and QOU's `derivedHiggsQuartic` share the exact prefactor $\frac{g_2^2}{8} = \frac{\pi\alpha_{\mathrm{EM}}}{2\sin^2\theta_W(1-\Delta r)} = \frac{M_W^2}{2 v^2}$ with $v_{\mathrm{weak}}$ cancelling identically. On Podleś $S^2_q$, the equatorial mode $\Phi = \gamma$ has Haar kurtosis $\frac{h((\gamma^*\gamma)^2)}{h(\gamma^*\gamma)^2} = \frac{[2]_{q_0}^2}{[3]_{q_0}} = \frac{4 + h_0^2}{3 + h_0^2} = 1.3285468214\ldots < \frac{4}{3}$ (since $4[3]_q - 3[2]_q^2 = h^2 > 0$).
5. **Bridge 5 — Jucys–Murphy Content Traces & Rank-vs-$q$-Factorial Separation (`jm_h3_h4_traces_and_qfactorial_gt_six`):**
   - Multiplicative JM eigenvalues $q^{2 c(x)}$ sum to $[3]_q$ on $H_3$ `(2,1)` and $[2]_q^2$ on $H_4$ `(2,2)`, while $[2]_q [3]_q > 6$ for all $q > 1$ separates the quantum factorial from the topological Wedderburn rank ratio $\dim H_3 / \dim Z(H_4) = 6/5$.

---

## 3. Side-by-Side 80-dps Proton-Pin Comparison Against PDG Higgs Data (`STRICT NO FITTING`)

Comparison benchmarks: PDG 2024 $m_H = 125.20 \pm 0.11\;\mathrm{GeV}$, $v_{\mathrm{weak}} = 246.219651\;\mathrm{GeV}$, $\lambda_H = 0.129281 \pm 0.000227$ (and PDG 2022 $m_H = 125.25\;\mathrm{GeV} \implies \lambda_H = 0.129384$).

| Candidate Mechanism / Invariant | $\lambda_H$ at $q_0^{(p)}$ | Implied $m_H$ (GeV) | Rel. Error vs PDG-24 $\lambda_H$ | Pull vs PDG-24 $m_H$ | Epistemic Verdict |
|---|---:|---:|---:|---:|---|
| **QOU `L2a` Plancherel + `C0_tree_dressed`** | **`0.1294886547`** | **`125.300717`** | **`+0.1610%`** (`+0.081%` vs PDG-22) | **`+0.92σ`** | **Conditional Match** (`< 1σ`) |
| **QOU `L2a` Plancherel + `C1_habiro_half_h2`** | **`0.1290362314`** | **`125.081630`** | **`-0.1890%`** | **`-1.08σ`** | **Conditional Match** (`~1σ`) |
| **QOU `L2a` Plancherel + `C2_bring_zero_hbar2`** | **`0.1289496966`** | **`125.039681`** | **`-0.2559%`** | **`-1.46σ`** | **Conditional Match** (`< 1.5σ`) |
| Pre-$\sigma$ Chamseddine–Connes tree $\frac{4}{3}\frac{M_W^2}{v^2}$ | `0.1416291254` | `131.043038` | `+9.5518%` | `+53.12σ` | **Refuted** (needs NCG $\sigma$-singlet or Plancherel replacement) |
| Podleś $S^2_q$ kurtosis $\frac{[2]_{q_0}^2}{[3]_{q_0}}\frac{M_W^2}{v^2}$ | `0.1411206903` | `130.807630` | `+9.1585%` | `+50.98σ` | **Refuted** (`q_0`-shift moves right way from `4/3`, far too small) |
| Bare $\mathcal{O}_q(\mathrm{SU}(2))$ half Haar variance $\frac{1}{2[2]_{q_0}^2}$ | `0.1236489434` | `122.442670` | `-4.3561%` | `-25.07σ` | **Refuted** (`q_0 > 1` moves down from `1/8 = 0.125`) |
| Bare $\mathcal{O}_q(\mathrm{SU}(2))$ quarter Haar purity $\frac{1+q_0^4}{4(1+q_0^2)^2}$ | `0.1263510566` | `123.773413` | `-2.2660%` | `-12.97σ` | **Refuted** |
| Bare $U_q(\mathfrak{sl}_2)$ spin-$1/2$ Casimir $/ 6$: $\frac{q_0^2+q_0+1}{6(q_0+1)^2}$ | `0.1251132006` | `123.165656` | `-3.2235%` | `-18.49σ` | **Refuted** |
| Bare bipartite singlet lower triplet $\frac{q_0^{-2}}{2[3]_{q_0}}$ | `0.1333331305` | `127.147088` | `+3.1347%` | `+17.70σ` | **Refuted** |
| Replacing rank `6/5` by $q$-factorial $[2]_{q_0}[3]_{q_0}/5$ | `0.1347457600` | `127.818830` | `+4.2274%` | `+23.81σ` | **Refuted** (`6/5` must stay topological rank invariant) |

### Additional Negative Controls (`T(2,2k)` Alexander & $H_6(q_0)$ Odd/Even JM Slots)
- **Bare $T(2,2k)$ Alexander ratios:** $[3]_{q_0}/[2]_{q_0} = 1.513606$ vs $M_Z/M_W = 1.134609$ (`+33.40%`), $[4]_{q_0}/[2]_{q_0} = 2.043706$ vs $m_H/M_W = 1.557811$ (`+31.19%`), and $[4]_{q_0}/[3]_{q_0} = 1.350223$ vs $m_H/M_Z = 1.372994$ (`-1.66%`). Mass generation on $T(2,2k)$ enters via the Plancherel trace polynomials $P_m(h_0)$ (`1` at $h=0$), not the abelian Alexander quantum integers $[m]_{q_0}$ (`m` at $h=0$).
- **6-strand Hoefsmit odd/even JM slot ratios (`qou-zd6l`):** Across all irreps `(6), (5,1), (4,2), (3,3), (4,1,1), (3,2,1), (2,2,2)` of $H_6(q_0)$, $1/(1 + \langle J_1 J_3 J_5 / (J_2 J_4 J_6)\rangle^2)$ lies in `[0.3561, 0.7777]` (tending to `0.5` as $q \to 1$), confirming that physical $\sin^2\theta_W \approx 0.2232$ comes from the $O(h_0^2)$ Plancherel genus-step splitting `plancherelSinSq(q_0) = 0.223474` (`+0.122%`), not an order-zero $H_6$ JM ratio.
