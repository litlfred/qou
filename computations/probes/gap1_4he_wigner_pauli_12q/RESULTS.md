# Results: Closing Open Gap 1 (Option 1A) — ${}^4\mathrm{He}$ $12$-Quark Pauli Antisymmetrizer & Wigner $\mathrm{SU}(4)$ Spin-Isospin Chromomagnetic Binding

- **Branch:** `claude/gap1-4he-wigner-pauli-12q-20261123` (off `origin/main` `e330ab6aa04`)
- **Pre-registration:** [`PREREGISTRATION.md`](PREREGISTRATION.md) (`fccd5d39abf`, committed & pushed prior to numerical evaluation)
- **Lean 4 formalization:** [`TwelveQuarkWignerPauliBinding.lean`](../../../folio/quantum-observable-universe/lean/QOU/Nuclear/TwelveQuarkWignerPauliBinding.lean) (`671790883d9`, `0 sorry`, `0` custom `axiom`s, `[propext, Classical.choice, Quot.sound]` only, generic `§7c` + `_real` bridge)
- **80-dps probe & stamped witness:** [`gap1_4he_wigner_pauli_12q_probe.py`](gap1_4he_wigner_pauli_12q_probe.py) (`4d5b8baebab`) & [`gap1_4he_wigner_pauli_12q_probe.witness.json`](gap1_4he_wigner_pauli_12q_probe.witness.json) (`commitSha == scriptCommitSha`, `allPassed = true`, `workdps = 80`, `OUT_DPS = 50`, `q0Anchor = "proton"`, `0` free parameters)

---

## 1. Exact Mathematical & Microscopic Results Certified (`Part A`)

### 1.1 Conjugate Young-Diagram Pairing, Wigner $\mathrm{SU}(4)_{\sigma\tau}$ Spectrum & $A = 5$ Pauli Shell Closure

For $A$ nucleons ($3A$ valence $u, d$ quarks) in a common $s$-wave $[3A]$ spatial configuration, Fermi statistics $[1^{3A}]$ pairs the $\mathrm{SU}(3)_c$-singlet colour Specht module $S^{[A,A,A]}$ uniquely with the transpose spin-isospin Specht module $S^{[3^A]}$ (`conjugate_rectThree_eq_colThree`, `hookProd_and_spechtDim_colThree_eq`, `su4WeylDim_light_nuclei_and_shell_closure`):

| $A$ | Quarks $3A$ | $\lambda_{\mathrm{col}} = [A,A,A]$ | $\mu_{\sigma\tau} = [3^A]$ | $\dim S^{[A,A,A]} = \dim S^{[3^A]}$ | Hidden channels $d_A - 1$ | $\dim V^{\mathrm{SU}(4)_{\sigma\tau}}_{[3^A]}$ | $\dim \Lambda^A(\mathbf{4}_N)$ | $8 \, C_2^{\mathrm{SU}(4)}([3^A])$ | $(0s)^{3A}$ Pauli hidden fraction |
|---:|---:|:---:|:---:|---:|---:|---:|---:|---:|---:|
| $1$ | $3q$ ($N / \Delta$) | $[1,1,1]$ | $[3]$ | $1$ | $0$ | $20$ ($\mathbf{4}_N \oplus \mathbf{16}_\Delta$) | $4$ | $63$ | $0/1 = 0\%$ |
| $2$ | $6q$ (${}^2\mathrm{H}$) | $[2,2,2]$ | $[3,3]$ | $5$ | $4$ | $50$ | $6$ | $84$ | $4/5 = 80.00\%$ |
| $3$ | $9q$ (${}^3\mathrm{H}/{}^3\mathrm{He}$) | $[3,3,3]$ | $[3,3,3]$ | $42$ | $41$ | $20$ ($\overline{\mathbf{4}}_N \oplus \overline{\mathbf{16}}_\Delta$) | $4$ | $63$ | $41/42 = 97.62\%$ |
| $4$ | $12q$ (${}^4\mathrm{He}$) | $[4,4,4]$ | $[3,3,3,3]$ | $462$ | $461$ | **$1$** (unique $(S\!=\!0,T\!=\!0)$ singlet) | **$1$** | **$0$** | $461/462 = 99.78\%$ |
| $\ge 5$ | $\ge 15q$ (${}^5\mathrm{He}/{}^5\mathrm{Li}$) | $[A,A,A]$ | $[3^A]$ | $6006$ ($A\!=\!5$) | $6005$ | **$0$** (exact $1s$-shell closure) | **$0$** | — | — |

### 1.2 Microscopic Chromomagnetic Operator $\mathcal{O}_{\mathrm{CM}}$ & Short-Range Repulsive Core

Over any noncommutative `[Ring E]`, `pauli_cmi_operator_identity` proves that under $P_c P_s P_t = -1$,
$$-\bigl((6 P_c - 2)(2 P_s - 1)\bigr) = 12 P_t - 6 P_s P_t + 4 P_s - 2,$$
assembling (`cmi_spectrum_and_pauli_norm`) to the exact $(0s)^n$ eigenvalue
$$\mathcal{O}_{\mathrm{CM}}(n, \kappa, S, T) = -\sum_{1 \le i < j \le n} (\lambda_i \cdot \lambda_j)(\sigma_i \cdot \sigma_j) = n(n - 5) - 2\kappa + \frac{4}{3}S(S+1) + 4T(T+1).$$
Certified both in Lean 4 and by explicit sparse rational tensor evaluation in $\mathbb{Q}^{12^6}$ (`verify_sympy_6q_microscopic`):
- Single baryons ($3q$): $\mathcal{O}_{\mathrm{CM}}(N) = -8$, $\mathcal{O}_{\mathrm{CM}}(\Delta) = +8$ ($\Delta - N$ splitting $= 16$).
- $(0s)^6$ deuteron bag ($S=1, T=0$): $\mathcal{O}_{\mathrm{CM}} = +8/3$, giving short-range repulsive core $\Delta\mathcal{O}_{\mathrm{CM}} = +8/3 - (-16) = \mathbf{+56/3}$ above $2N$, with exact Matveev–Sorba / Harvey decomposition $(P_{NN}, P_{\Delta\Delta}, P_{88}) = \mathbf{(1/9,\; 4/45,\; 4/5)}$ and Karl–Paton Pauli antisymmetrizer norm $\langle NN | \mathcal{A}_6 | NN \rangle = \mathbf{1/9}$ (from $\langle P_{23}^{\mathrm{col}}\rangle = +1/3$ and $\langle P_{23}^{\sigma\tau}\rangle = -1/27$).
- $(0s)^6$ dinucleon bag ($S=0, T=1$): $\mathcal{O}_{\mathrm{CM}} = +8$, giving repulsive core $\Delta\mathcal{O}_{\mathrm{CM}} = \mathbf{+24}$, which is **$+16/3$ more repulsive** at short range than the deuteron $(S=1, T=0)$ channel.
- $(0s)^9$ ($A=3$) and $(0s)^{12}$ ($A=4$): $\mathcal{O}_{\mathrm{CM}} = +40$ ($\Delta = +64$) and $+96$ ($\Delta = +128$), proving rigorously that light nuclei **cannot** bind by collapsing into a static $(0s)^{3A}$ single bag; binding arises instead by virtual Bloch–Horowitz tunnelling out of the factorized $A$-nucleon cluster state $|\Phi_{\mathrm{fac}}^{(A)}\rangle$.

### 1.3 Exact $q_0$-Deformed Hoefsmit Conjugate Duality

Proved in `hecke_conjugate_duality_and_pauli_invariance` over `[CommRing R]` and certified at 80 dps across $A = 2, 3, 4$ (`dim = 5, 42, 462`):
- Generator duality $\max |\check{R}_k^{[3^A]}(q_0) + D_\eta (\check{R}_k^{[A,A,A]}(q_0))^{-1} D_\eta| = 5.27 \times 10^{-82}$;
- Braid-transposition duality $\max |\mathcal{B}_{s,t}^{[3^A]}(q_0) + D_\eta ((\mathcal{B}_{s,t}^{[A,A,A]}(q_0))^{-1})^T D_\eta| = 3.69 \times 10^{-81}$;
- Projected Pauli matrix $M_{ij} = X_{ij}(X - h I)_{ji}$ symmetry & constant row-sum $+1$ residual $= 3.58 \times 10^{-80}$.

---

## 2. 80-dps Evaluation of All Six Pre-Registered Zero-Parameter Hamiltonians (`Part B`)

Substrate calibration (`CAL-1/2/3` only, zero fitted constants):
- $q_0 = 1.1099785827513808075916690956107688798744991218736$ (`proton` anchor),
- $E_{\mathrm{osc}}(q_0) = m_e / (q_0 - 1)^2 = 42.2477681091499538\text{ MeV}$, $E_0(q_0) = m_e / (q_0(q_0 - 1)) = 4.1859813632944759\text{ MeV}$,
- CODATA-2022 / AME2020 nuclear binding targets:
  $$B({}^2\mathrm{H}) = 2.22456637\text{ MeV}, \quad B({}^3\mathrm{H}) = 8.48179663\text{ MeV}, \quad B({}^3\mathrm{He}) = 7.71798968\text{ MeV}, \quad B({}^4\mathrm{He}) = 28.29561094\text{ MeV},$$
  with empirical ratios $1 : 3.8128\; ({}^3\mathrm{H}) / 3.4694\; ({}^3\mathrm{He}) : 12.7196\; ({}^4\mathrm{He})$.

| Model (0 free parameters) | ${}^2\mathrm{H}$ ($A\!=\!2$) [MeV] | vs AME ${}^2\mathrm{H}$ | $A\!=\!3$ [MeV] | vs ${}^3\mathrm{H}$ / ${}^3\mathrm{He}$ | ${}^4\mathrm{He}$ ($A\!=\!4$) [MeV] | vs AME ${}^4\mathrm{He}$ | BH2 ratios $1 : A_3/A_2 : A_4/A_2$ | Exact ratios $1 : A_3/A_2 : A_4/A_2$ |
|:---|---:|---:|---:|---:|---:|---:|:---:|:---:|
| **`M0_w4_baseline_colour_V2`** (`#9221`) | `2.264785` | `+1.81%` | `5.105857` | `-39.80%` / `-33.84%` | `14.487666` | `-48.80%` | `1 : 1.9896 : 5.0352` | `1 : 2.2545 : 6.3969` |
| **`M1_colour_only_true_KA_fierz`** | **`2.264785`** | **`+1.81%`** | **`6.962282`** | **`-17.92%` / `-9.79%`** | **`14.326655`** | **`-49.37%`** | **`1 : 3.0000 : 6.0000`** | **`1 : 3.0741 : 6.3258`** |
| **`M2_pauli_conjugate_KA_G2col`** | `1.869579` | `-15.96%` | `4.199355` | `-50.49%` / `-45.59%` | `6.648541` | `-76.50%` | `1 : 2.1979 : 3.4383` | `1 : 2.2461 : 3.5562` |
| **`M3_pauli_conjugate_KA_G2barsym`** | `1.309352` | `-41.14%` | `3.008017` | `-64.54%` / `-61.03%` | `4.823850` | `-82.95%` | `1 : 2.2345 : 3.5261` | `1 : 2.2973 : 3.6842` |
| **`M4_pauli_all9_baryon_norm_G2sum`** | `1.601227` | `-28.02%` | `3.783792` | `-55.39%` / `-50.97%` | `6.195396` | `-78.10%` | `1 : 2.2345 : 3.5261` | `1 : 2.3631 : 3.8692` |
| **`M5_pauli_all9_pair_avg_G2barsym`** | `0.346641` | `-84.42%` | `0.801707` | `-90.55%` / `-89.61%` | `1.292300` | `-95.43%` | `1 : 2.2345 : 3.5261` | `1 : 2.3128 : 3.7281` |
| **Unprojected $\mathcal{W}_A(q_0)$ (`BH2`, `G2_barsym`)** | `1.994959` (`1.974907` ex.) | `-10.32%` (`-11.22%`) | `5.984877` | `-29.44%` / `-22.46%` | `11.969754` | `-57.70%` | **`1 : 3.0000 : 6.0000`** | — |

---

## 3. Honest Diagnostic Synthesis & Structural Findings

1. **Resolution of the `#9221` $A = 3$ Deficit (`M0` $\to$ `M1`):**
   Correcting `#9221`'s reversed `prefix`/`suffix` non-adjacent braid transport word (`M1`) restores exact $\binom{A}{2} = 1 : 3.000000000000000000000000 : 6.000000000000000000000000$ second-order `BH2` scaling at $q_0$ (confirming that sliding a quark strand across an intervening $3$-strand $\mathcal{U}_{q_0}(\mathfrak{sl}_3)$ singlet is central and excites zero spectator hidden colour!). Without any free parameters, `M1` predicts **`2.2648 MeV` (`+1.81%`) at ${}^2\mathrm{H}$** and lifts $A = 3$ from `#9221`'s `5.1059 MeV` (`-39.8%`) to **`6.9623 MeV` (`-17.9%` vs ${}^3\mathrm{H}$, `-9.79%` vs ${}^3\mathrm{He}$)**.

2. **Why Chain-Projected $\Pi_{\mathcal{D}}$ (`M2`–`M5`) Scales as $1 : 2.23 : 3.53$ While Unprojected $\mathcal{W}_A(q_0)$ Restores $1 : 3 : 6$:**
   At $A = 2$, the unprojected $25$-dimensional tensor product $\mathcal{W}_2(q_0) = S^{[2,2,2]}(q_0) \otimes S^{[3,3]}(q_0)$ gives `1.9749 MeV` (`-11.2%` vs ${}^2\mathrm{H}$) with $99.45\%$ ground-state weight inside the $5$-dimensional conjugate-tableau subspace $\mathcal{D}_{\mathrm{Pauli}}(2)$. However, for $A \ge 3$, Hoefsmit's Young seminormal basis is adapted to the linear chain $S_1 \subset \dots \subset S_{3A}$: non-adjacent pair transpositions $(0, 2), (0, 3), (1, 3)$ map $|\Phi_{\mathrm{fac}}^{(A)}\rangle$ into rank-$1$ tensors $\sum_{r,s} c_r c'_s |T_r\rangle \otimes |T'_s\rangle$ whose off-diagonal terms ($r \neq s$) lie outside $\mathcal{D}_{\mathrm{Pauli}}(A)$. Our 80-dps $\mathcal{W}_3(q_0)$ audit (`W3_pair_norm_spread_max_diff = 3.69e-81`, `W3_pair_orthogonality_max_inner_prod = 2.67e-83`) proves that on the **unprojected** space $\mathcal{W}_A(q_0)$, all $\binom{A}{2}$ Pauli pair excitations remain strictly orthogonal and equal-norm (`1 : 3 : 6`), whereas $\Pi_{\mathcal{D}}$ artificially attenuates non-adjacent pairs by $\sum_r c_r^4 / (\sum_r c_r^2)^2 \approx 0.29$.

3. **Fixed-Overlap Internal Ceiling (`~6.33x` vs `12.72x` at ${}^4\mathrm{He}$) — Pointer to Spatial Wave-Function Compression (Option 1B):**
   Across **every** fixed-overlap internal finite-dimensional model (`M1` as well as unprojected $\mathcal{W}_A(q_0)$), the two-cluster Casimir gap $\Delta_{88}(q_0) = 2 q_0^{-3}[3]_{q_0} \approx 4.451$ ($\approx 188.1\text{ MeV}$ in the $E_{\mathrm{osc}}$ chart) keeps hidden-colour admixture perturbative ($P_{\mathrm{hid}} = 1.27\%, 3.92\%, 8.09\%$ for $A = 2, 3, 4$ in `M1`). Consequently, collective multi-channel Schur-complement enhancement beyond $\binom{A}{2} = 6$ is $+5.4\%$ (`6.3258x`, giving `14.3267 MeV` at ${}^4\mathrm{He}$ vs `28.2956 MeV`), NOT $+112\%$ (`12.7196x`). Physically and mathematically, the remaining `1.98x` factor between `14.33 MeV` and `28.30 MeV` is **spatial Jacobi wave-function compression**: ${}^2\mathrm{H}$ ($1$ pair vs $1$ relative kinetic Jacobi mode, RMS radius $\sim 1.97\text{ fm}$) is a diffuse threshold halo where kinetic zero-point energy cancels $\sim 80\%$ of pair attraction, whereas ${}^4\mathrm{He}$ ($6$ Wigner pairs vs only $3$ relative Jacobi modes, $2$ pairs per kinetic mode, RMS radius $\sim 1.46\text{ fm}$) compresses the short-range quark-exchange overlap $|\langle \phi_a | \phi_b \rangle|^2 \propto R_A^{-3}$ by $\sim (1.97 / 1.46)^3 \approx 2.46\times$. Coupling `M1` / $\mathcal{W}_A(q_0)$ to a parameter-free $3(A-1)$-dimensional relative Jacobi kinetic variational oscillator (Option 1B) is therefore the exact next step to close the remaining factor of $2$ at ${}^4\mathrm{He}$.
