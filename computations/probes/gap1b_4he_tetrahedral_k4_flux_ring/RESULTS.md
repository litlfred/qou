# Results: Closing Open Gap 1 Backup (Option 1B, `qou-3kkz`) — 4-Body Tetrahedral $K_4$ Colour-Flux Ring Exchange, Wigner Majorana Space-Exchange & 3D Jacobi Variational Compression across $A = 2, 3, 4$

- **Bean / Option:** `qou-3kkz` (Option 1B backup behind `qou-ni4i`, incorporating Cross-Worker Gap 1A `J_var` synthesis)
- **Pre-Registration:** `computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/PREREGISTRATION.md` (locked prior to numerical evaluation)
- **Lean 4 Formalization:** `folio/quantum-observable-universe/lean/QOU/Nuclear/TetrahedralFluxRingAndMajoranaCluster.lean` (`0 sorry`, `0` custom `axiom`s, `0` empirical literals, `§7c` generic `[CommRing R]` / `[LinearOrder K] [IsStrictOrderedRing K]` + `_real` specializations)
- **80-dps Probe & Witness:** `computations/probes/gap1b_4he_tetrahedral_k4_flux_ring/gap1b_4he_tetrahedral_k4_flux_ring_probe.py` $\to$ `gap1b-4he-tetrahedral-k4-flux-ring.witness.json` (`mp.dps = 80`, `OUT_DPS = 50`, `q0Anchor = "proton"`, `free_parameters = 0`, `allPassed = true`)

---

## 1. Substrate Scales & CODATA-2022 / AME2020 Benchmarks

All inputs derive exclusively from CAL-1/2/3 (`m_e`, proton-pinned `q_0`, `free_parameters = 0`):

| Quantity | Value (`80-dps` truncated) | Role |
|---|---|---|
| $q_0$ (`proton` pin) | `1.10997858275138080759166909561...` | Universal QOU substrate deformation parameter |
| $m_e$ | `0.51099895069 MeV` | CAL-1 mass scale |
| $E_0(q_0) = \frac{m_e}{q_0(q_0 - 1)}$ | `4.185981363294476 MeV` | Order-zero nuclear long-range Compton scale |
| $E_{\mathrm{osc}}(q_0) = \frac{m_e}{(q_0 - 1)^2}$ | `42.24776810914995 MeV` | Intra-nucleon harmonic-oscillator / string scale (`#9221`) |
| $\Delta_8(q_0) = q_0^{-3}[3]_{q_0}$ | `2.411912926576629...` | Single-cluster $\mathrm{SU}(3)_c$ ribbon full-twist Casimir gap (`#9212`) |
| $B_{\mathrm{exp}}({}^2\mathrm{H})$ | `2.224566370 MeV` (`1.0000x`) | CODATA-2022 deuteron binding energy |
| $B_{\mathrm{exp}}({}^3\mathrm{H})$ / $B_{\mathrm{exp}}({}^3\mathrm{He})$ | `8.481796630 MeV` (`3.8128x`) / `7.717989680 MeV` (`3.4694x`) | CODATA-2022 $A = 3$ mirror nuclei |
| $B_{\mathrm{exp}}({}^4\mathrm{He})$ | `28.29561094 MeV` (`12.7196x`) | CODATA-2022 $\alpha$-particle binding energy |

---

## 2. Lean 4 Formal Theorems (`TetrahedralFluxRingAndMajoranaCluster.lean`) & Part 1 Symbolic Checks

All Part 1 algebraic, combinatorial, and $\mathbb{Q}(q)$ identities are machine-checked in Lean 4 (`lean -j 1` exit `0`, `0` warnings) and independently cross-verified symbolically in SymPy over $\mathbb{Q}(q)$:

1. **Exact $K_A$ Simplex, Hamiltonian Cycle & Tait 12-Quark Bijection (`§1`):**
   - `kA_simplex_and_cycle_counts`: exact cardinalities across $A = 1, 2, 3, 4$:
     - 2-body edges $e_2(A) = \binom{A}{2} \in \{0, 1, 3, 6\}$,
     - 3-body unoriented triangles $f_3(A) = \binom{A}{3} \in \{0, 0, 1, 4\}$ (so $f_3(2) = 0$ identically in ${}^2\mathrm{H}$),
     - 4-body unoriented Hamiltonian rings $c_4(A) = 3\binom{A}{4} \in \{0, 0, 0, 3\}$ (`(0-1-2-3-0)`, `(0-1-3-2-0)`, `(0-2-1-3-0)` on $K_4$, activating exclusively at ${}^4\mathrm{He}$),
     - Tetrahedral Euler characteristic $V - E + F = 4 - 6 + 4 = 2$ (`k4_boundary_euler_characteristic`).
   - `k4TaitQuarkOfHalfEdge_bijective` & `k4_tait_matching_partitions_edges`: explicit 1-to-1 bijection between the $12$ valence quarks of ${}^4\mathrm{He}$ and the $12$ directed half-edges of $K_4$ via its $3$ disjoint Tait perfect matchings (`deg = 3 = N_c`).
2. **Constructive Wigner $\mathrm{SU}(4)$ Majorana Space-Exchange & Pauli Closure (`§2`):**
   - `four_spinIsospinSwap_eq_pauli_product`: exact integer identity $4 P_{ab}^{\sigma\tau} = (2 P_{ab}^\sigma)(2 P_{ab}^\tau)$ over any `[CommRing R]`.
   - `wignerMajorana_eigenvalue_and_pair_sum`: on every antisymmetric spin-isospin state in $\Lambda^A(\mathrm{Fin}\,4 \to R) = [1^A]_{\sigma\tau}$ for $A \in \{2, 3, 4\}$, Wigner's space-exchange operator $P_{ab}^x = -P_{ab}^{\sigma\tau}$ has exact eigenvalue $+1$ on every nucleon pair $a \neq b$, yielding pair sum $\sum_{0 \le a < b < A} P_{ab}^x = \binom{A}{2} \in \{1, 3, 6\}$.
   - `IsSpinIsospinAntisym5_eq_zero`: exact Pauli $0s$-shell closure $\Lambda^5(\mathrm{Fin}\,4 \to R) = 0$ at $A = 5$.
3. **Exact 9-Quark & 12-Quark Colour-Reconnection Traces, Rank-1 Transfer Matrix $M(q)$ & Closed Plaquette Cumulants (`§3`):**
   - Open-chain factorization (`reconnNineOpen_eq_q9_normSq_cubed`, `reconnTwelveOpen_eq_q12_normSq_pow4`): $t_3^{\mathrm{open}}(q) = (q^3/[3]_q)^2$ and $t_4^{\mathrm{open}}(q) = (q^3/[3]_q)^3$.
   - Exact rank-1 cluster ring transfer matrix (`ringPairTransfer_rank_one_shift`, `trace_ringPairTransfer_cubed`, `trace_ringPairTransfer_pow4`):
     $$M(q) + q^{-3} I_3 = \begin{pmatrix} q \\ q^{-1} \\ q^{-3} \end{pmatrix}\begin{pmatrix} 1 & 1 & 1 \end{pmatrix}, \qquad \mathrm{spec}(M(q)) = \{[2]_q,\; -q^{-3},\; -q^{-3}\}.$$
   - Closed 9-quark triangular face & 12-quark tetrahedral 4-cycle overlaps and connected colour-octet cumulants (`closed_plaquette_expectations_and_cumulants_field`):
     $$t_3^{\triangle}(q) = \frac{q^9 [2]_q^3 - 8}{[2]_q^3 [3]_q^3}, \quad \kappa_3(q) = -\frac{8}{[2]_q^3 [3]_q^3} \;\;(-0.02581808\text{ at }q_0),$$
     $$t_4^{\square}(q) = \frac{q^{12} [2]_q^4 + 8}{[2]_q^4 [3]_q^4}, \quad \kappa_4(q) = +\frac{8}{[2]_q^4 [3]_q^4} \;\;(+0.00405749\text{ at }q_0).$$
4. **Deuteron Invariance, Bloch–Horowitz Plaquette Enhancement & 3D Jacobi Hall–Post Bounds (`§4`–`§5`):**
   - `kASimplexBinding_deuteron_invariance_and_light_nuclei`, `kABlochHorowitz_super_pairwise_enhancement`, `jacobi_mode_factorization_and_hall_post_ring`, and `hall_post_variational_exceeds_six_deuterons` (+ `_real` bridges).

---

## 3. Part 2A: Fixed-Radius Hoefsmit $S^{[A,A,A]}_{H_{3A}(q_0)}$ (`5D / 42D / 462D`) & Analytic Plaquette Models

All Part 2A models have `free_parameters = 0` and are read out in `#9221`'s harmonic-oscillator Compton scale $E_{\mathrm{osc}}(q_0) = 42.247768\;\mathrm{MeV}$. Every Hecke relation, Clebsch–Gordan projector, and Lanczos ground-state residual is certified in pure 80-dps arithmetic to $\le 2.017 \times 10^{-80}$:

| Model (`free_parameters = 0`) | ${}^2\mathrm{H}$ [MeV] (`err`) | $A = 3$ [MeV] (`vs 3H` / `vs 3He`) | ${}^4\mathrm{He}$ [MeV] (`err vs 28.296`) | Ratio `1 : A3/A2 : A4/A2` | Physical Structure |
|---|---:|---:|---:|---|---|
| `M0_w4_v2_baseline` | `2.264785` (`+1.81%`) | `5.105857` (`-39.80%` / `-33.84%`) | `14.487665` (`-48.80%`) | `1 : 2.2544 : 6.3969` | `#9221` baseline (reversed non-adjacent braid transport) |
| `M1_kA_2body_boundary` | `2.264785` (`+1.81%`) | `6.962281` (`-17.92%` / `-9.79%`) | `14.326655` (`-49.37%`) | `1 : 3.0741 : 6.3258` | Corrected positive-braid transport (`BH2` exact `1:3:6`, err `0.0`) |
| `M2_kA_2body_tait_matched` | `2.264785` (`+1.81%`) | `6.934883` (`-18.24%` / `-10.15%`) | `14.049724` (`-50.35%`) | `1 : 3.0620 : 6.2036` | 12-quark Tait 3-matching bijection (pure 2-body) |
| **`M3a_kA_plaquette_pos`** | **`2.264785` (`+1.81%`)** | **`9.014017` (`+6.27%` / `+16.79%`)** | **`29.329056` (`+3.65%`)** | **`1 : 3.9800 : 12.9500`** | **Tait 2-body + $\binom{A}{3}\mathcal{P}_\triangle + c_4(A)\mathcal{P}_\square$ (direct `+` sign)** |
| `M3a_kA_plaquette_neg` | `2.264785` (`+1.81%`) | `7.565454` (`-10.80%` / `-1.98%`) | `17.536005` (`-38.03%`) | `1 : 3.3404 : 7.7429` | Tait 2-body $-\binom{A}{3}\mathcal{P}_\triangle - c_4(A)\mathcal{P}_\square$ (Kogut–Susskind `-` sign) |
| `M3a_bnd_plaquette_pos` | `2.264785` (`+1.81%`) | `9.971601` (`+17.56%` / `+29.20%`) | `31.054346` (`+9.75%`) | `1 : 4.4028 : 13.7118` | Boundary 2-body $+\binom{A}{3}\mathcal{P}_\triangle + c_4(A)\mathcal{P}_\square$ |
| `M3a_bnd_plaquette_neg` | `2.264785` (`+1.81%`) | `6.983918` (`-17.66%` / `-9.51%`) | `16.596806` (`-41.34%`) | `1 : 3.0837 : 7.3282` | Boundary 2-body $-\binom{A}{3}\mathcal{P}_\triangle - c_4(A)\mathcal{P}_\square$ |
| `M3b_kA_connected_fierz_pos` | `2.264785` (`+1.81%`) | `7.279888` (`-14.17%` / `-5.68%`) | `15.239104` (`-46.14%`) | `1 : 3.2143 : 6.7287` | Connected $q$-Fierz products $+\mathcal{F}_{ab}\mathcal{F}_{bc}\mathcal{F}_{ca} + \mathcal{F}^4_\square$ |
| `M3b_kA_connected_fierz_neg` | `2.264785` (`+1.81%`) | `6.812600` (`-19.68%` / `-11.73%`) | `13.718549` (`-51.52%`) | `1 : 3.0080 : 6.0573` | Connected $q$-Fierz products $-\mathcal{F}_{ab}\mathcal{F}_{bc}\mathcal{F}_{ca} - \mathcal{F}^4_\square$ |
| `M4a_kA_cyclic_quark_raw_pos` | `2.264785` (`+1.81%`) | `7.140304` (`-15.82%` / `-7.48%`) | `33.171417` (`+17.23%`) | `1 : 3.1527 : 14.6466` | Unprojected single-quark cyclic 3-/4-braids (`+`) |
| `M4a_kA_cyclic_quark_raw_neg` | `2.264785` (`+1.81%`) | `10.09273` (`+18.99%` / `+30.77%`) | `83.833193` (`+196.28%`) | `1 : 4.4563 : 37.0159` | Unprojected single-quark cyclic 3-/4-braids (`-`, edge double-counting) |
| `M4b_kA_cyclic_quark_cumulant_pos` | `2.264785` (`+1.81%`) | `7.478827` (`-11.83%` / `-3.10%`) | `17.839574` (`-36.95%`) | `1 : 3.3022 : 7.8769` | Orthogonal $k$-cluster cumulant projected cyclic braids (`+`) |
| `M4b_kA_cyclic_quark_cumulant_neg` | `2.264785` (`+1.81%`) | `7.296917` (`-13.97%` / `-5.46%`) | `17.540891` (`-38.01%`) | `1 : 3.2219 : 7.7451` | Orthogonal $k$-cluster cumulant projected cyclic braids (`-`) |
| **`M5a_analytic_hoefsmit_plaq_cumulant`** | **`2.264785` (`+1.81%`)** | **`8.557353` (`+0.89%` / `+10.88%`)** | **`24.794274` (`-12.37%`)** | **`1 : 3.7784 : 10.9477`** | **2nd-order non-double-counted Hoefsmit 3-/4-cluster cumulants** |
| `M5b_analytic_closed_octet_cumulant` | `2.264785` (`+1.81%`) | `6.796281` (`-19.87%` / `-11.94%`) | `13.596529` (`-51.95%`) | `1 : 3.0008 : 6.0035` | Planar $S^1$ closed-ring cumulant (no interior braid over-crossings) |
| **CODATA-2022 Empirical** | **`2.224566`** | **`8.481797` / `7.717990`** | **`28.295611`** | **`1 : 3.8128 : 12.7196`** | Experimental reference (`3H` / `3He` at $A=3$) |

---

## 4. Part 2B: Zero-Parameter 3D Jacobi Variational Compression Battery (`J_var`)

All Part 2B models have `free_parameters = 0` (`r_c / b_0 = 1` intrinsic bag-to-oscillator range ratio; theoretical $q_0$ deuteron saddle lock $b_2^{\mathrm{th}}(q_0) = 2.264785\;\mathrm{MeV}$ with zero empirical nuclear input). Stationarity gradients are certified to $\le 8.959 \times 10^{-61}$:

| Variational Model (`free_parameters = 0`) | ${}^2\mathrm{H}$ [MeV] | $A = 3$ [MeV] | ${}^4\mathrm{He}$ [MeV] (`err vs 28.296`) | Ratio `1 : A3/A2 : A4/A2` | Equilibrium Scale $\eta_A^*$ (`A=2, 3, 4`) |
|---|---:|---:|---:|---|---|
| `J_var_breath__M1_boundary` | `2.366959` | `7.464216` | `15.812774` (`-44.12%`) | `1 : 3.1535 : 6.6806` | Monopole breathing around $\eta=1$ (pure 2-body `M1`) |
| `J_var_breath__M2_tait` | `2.366959` | `7.443136` | `15.511929` (`-45.18%`) | `1 : 3.1445 : 6.5535` | Monopole breathing around $\eta=1$ (pure 2-body `M2`) |
| `J_var_breath__M3a_plaq_pos` | `2.366959` | `9.781387` | `35.270023` (`+24.65%`) | `1 : 4.1324 : 14.9009` | Monopole breathing + `M3a_pos` plaquettes |
| `J_var_breath__M3a_plaq_neg` | `2.366959` | `8.231144` | `19.927571` (`-29.57%`) | `1 : 3.4775 : 8.4191` | Monopole breathing + `M3a_neg` plaquettes |
| `J_var_selfbound_Eosc__hall_post_fixed_eta2` | `2.264785` | `27.76923` | `76.513349` (`+170.41%`) | `1 : 12.261 : 33.7839` | Kinetic in intra-bag $E_{\mathrm{osc}}(q_0)$ (fixed $\eta_2^*$) |
| `J_var_selfbound_Eosc__unrestricted_etaA` | `2.264785` | `35.68414` | `115.70838` (`+308.93%`) | `1 : 15.756 : 51.0902` | Kinetic in intra-bag $E_{\mathrm{osc}}(q_0)$ (short-range Thomas collapse) |
| **`J_var_selfbound_E0__hall_post_fixed_eta2`** | **`2.264785`** | **`10.93800`** | **`26.019670` (`-8.04%`)** | **`1 : 4.8296 : 11.4888`** | **Order-zero nuclear kinetic $E_0(q_0)$, fixed-$\eta_2^*$ Hall–Post bound** |
| **`J_var_selfbound_E0__unrestricted_etaA`** | **`2.264785`** | **`11.83260`** | **`30.545727` (`+7.95%`)** | **`1 : 5.2246 : 13.4872`** | **Order-zero nuclear kinetic $E_0(q_0)$, unrestricted $\eta_A^*$ minimum** |
| `J_var_micro_E0__fixed_eta2` | `2.264785` | `15.94431` | `42.029338` (`+48.54%`) | `1 : 7.0401 : 18.5577` | Coupled Hoefsmit `M1` saturation in $E_0(q_0)$ (fixed $\eta_2^*$) |
| `J_var_micro_E0__unrestricted_etaA` | `2.264785` | `17.36903` | `49.114646` (`+73.58%`) | `1 : 7.6691 : 21.6862` | Coupled Hoefsmit `M1` saturation in $E_0(q_0)$ (unrestricted $\eta_A^*$) |

---

## 5. Honest Physical Synthesis & Conclusions

1. **Cluster Separation Resolves Single-Bag $12q$ Pauli Quenching & Fixes `#9221` Transport Inversion:**
   - Modeling $s$-shell nuclei as $A$ colour-singlet cluster nodes on $K_A$ (`S^{[A,A,A]}`) avoids the `6.65 MeV` quark-Pauli core quenching of collapsing 12 quarks into a single `[12]_{S_{12}}` $0s$ bag (`Option 1A`).
   - Fixing `#9221`'s reversed non-adjacent braid transport (`M1_kA_2body_boundary`) restores exact `1 : 3 : 6` `BH2` scaling (`err = 0.0`) and lifts fixed-radius $A = 3$ from `5.1059 MeV` to **`6.9623 MeV` (`-9.79%` vs ${}^3\mathrm{He}$)** while keeping ${}^2\mathrm{H} = 2.2648\;\mathrm{MeV}$ (`+1.81%`) untouched (`0.0` deviation across all 15 static models).
2. **Tetrahedral $K_4$ 3-Face & 4-Cycle Colour-Flux Plaquettes (`Part 2A`):**
   - With direct positive-braid holonomy addition (`M3a_kA_plaquette_pos`, `0` free parameters), adding $\binom{A}{3}$ 3-interface triangular plaquettes and $c_4(A)$ 4-interface Hamiltonian tetrahedral rings yields **${}^2\mathrm{H} = 2.2648\;\mathrm{MeV}$ (`+1.81%`), $A = 3 = 9.0140\;\mathrm{MeV}$ (`+6.27%` vs ${}^3\mathrm{H}$), and ${}^4\mathrm{He} = 29.3291\;\mathrm{MeV}$ (`+3.65%` vs `28.2956 MeV`; scaling `1 : 3.980 : 12.950` vs empirical `1 : 3.813 : 12.720`)**.
   - Orthogonal projection onto pure $3$- and $4$-cluster $8_c^{\otimes k}$ cumulants (`M5a`) removes any 2-body edge overlap from interior braid over-crossings and gives **$A = 3 = 8.5574\;\mathrm{MeV}$ (`+0.89%` vs ${}^3\mathrm{H}$) and ${}^4\mathrm{He} = 24.7943\;\mathrm{MeV}$ (`-12.37%`)**.
   - **Caveat (Sign & Strand-Ordering Sensitivity):** Reversing to the Kogut–Susskind `-` sign (`M3a_neg = 17.5360 MeV`) or dropping interior linear strand over-crossings (`M5b = 13.5965 MeV`) substantially reduces the 3-/4-body enhancement, showing that a first-principles derivation of the 3D spatial-braid sign/embedding on $K_4$ is essential.
3. **3D Relative Jacobi Variational Compression (`Part 2B`):**
   - Pure 2-body Wigner pairing with $(A - 1)$ relative kinetic modes in the **order-zero long-range nuclear Compton chart** $E_0(q_0) = \frac{m_e}{q_0(q_0 - 1)} = 4.1860\;\mathrm{MeV}$ (`J_var_selfbound_E0`, `0` free parameters) symmetrically brackets empirical ${}^4\mathrm{He}$ between **`26.0197 MeV` (`-8.04%`, fixed-$\eta_2^*$ Hall–Post lower bound)** and **`30.5457 MeV` (`+7.95%`, unrestricted $\eta_4^*$ minimum)**, whereas setting the inter-cluster kinetic scale to the intra-bag string scale $E_{\mathrm{osc}}(q_0) = 42.2478\;\mathrm{MeV}$ produces short-range Thomas over-compression (`76.51`–`115.71 MeV`).
   - Combining monopole compression naively with full `M3a_pos` plaquettes (`35.2700 MeV`, `+24.65%`) overbinds by ~`25%`, demonstrating that 3D Jacobi wave-function compression and multi-cluster colour-flux reconnection must be derived from a **single unified 3D spatial-braid functional** rather than summed independently.
