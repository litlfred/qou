# Result Summary: Strong-CP $\bar{\theta}_{\mathrm{QCD}} = 0$ Writhe/Determinant Cancellation & $q$-Deformed Wilson String Tension (`qou-tcpx` / `Q-Gap-11`)

- **Bean:** `qou-tcpx` (`Q-Gap-11`, parent epic `qou-sm8w`; linked beans `tqcp`, `qou-1jqd`, `qou-db6w`).
- **Pre-registration:** `PREREGISTRATION.md` (committed at `c16267ee045` prior to numerical evaluation).
- **Lean 4 formalization (`0 sorry`, standard axioms only):** `folio/quantum-observable-universe/lean/QOU/StandardModel/StrongCPWritheCancellationAndStringTension.lean`.
- **80-dps probe & witness:** `sm8w_strong_cp_string_tension_probe.py` $\to$ `sm8w-strong-cp-string-tension.witness.json` (`7/7` assertions passed, `q0Anchor = "proton"`, `selectedCandidate = "none"`).

---

## 1. Formalized Lean 4 Theorems (`0 sorry`, Zero Empirical Inputs)

1. **Topological Writhe Cancellation & `ColorSectorCPEven` Discharge (`§1`):**
   - `writheWord_mirror_pair_eq_zero` & `substrate_and_gluon_writhe_identities`: proves $w(\beta \oplus \overline{\beta}) = 0$ for every braid word $\beta$, $w(\beta_{4_1}) = 0$, $w(\beta_{\mathrm{Bor}}) = 0$, single-gluon chirality $w(T(2,9)) = +9 \neq 0$, and closed mirror-pair cancellation $w(T(2,9) \oplus \overline{T(2,9)}) = 0$.
   - `singletProj3_idempotent_and_trace_one`, `su3_lie_deriv_leviCivita3_eq_zero_of_trace_zero`, `sl3_action_leviCivita3_of_det_one`, & `balanced_singlet_hecke_phase_eq_one`: proves $P_{(1^3)}^2 = P_{(1^3)}$, $\mathrm{Tr}(P_{(1^3)}) = 1$, exact $\mathfrak{sl}_3(R)$ annihilation and $\mathrm{SL}_3(R)$ invariance of $|\varepsilon\rangle \in (\mathrm{Fin}\,3)^3$, and exact $[1^3]$ balanced-framing parity cancellation $(q(-q^{-1}))^{w(\beta)}\,\mathrm{sgn}(\pi(\beta)) = 1$.
   - `colorSectorCPEvenOfMirrorPair` & `cpEven_zpow_iff_zero_and_ne_neg_one`: constructively discharges `QOU.StandardModel.ThetaQCDFraming.ColorSectorCPEven` on mirror-paired vacuum loops with `framingPhase = 1`, and proves over any ordered field ($q > 0, q \neq 1$) that `IsCPEven (q^m) ↔ m = 0`, strictly selecting $\theta_{\mathrm{top}} = 0$ (`Θ = +1`) and excluding $\theta_{\mathrm{top}} = \pi$ (`Θ = -1`).

2. **Hermitian / Nelson–Barr Determinant Reality with Non-Zero Jarlskog $J_{\mathrm{CP}} \neq 0$ (`§2`):**
   - `det_hermitian3_im_eq_zero` & `det_mul_hermitian3_im_eq_zero`: characteristic-free proof over any `CommRing R` (`QuadI R = R[i]`) that $3 \times 3$ Hermitian matrices $M_u, M_d$ with real diagonals satisfy $\mathrm{Im}\det(M_u M_d) = 0$ even when $[M_u, M_d] \neq 0$ makes $M_u M_d$ non-Hermitian.
   - `det_mul_gramDiag3_real_and_pos`: proves $\mathrm{Im}\det(M_u M_d) = 0$ and $\mathrm{Re}\det(M_u M_d) > 0$ for positive-eigenvalue congruences $M_q = A_q^\dagger \mathrm{diag}(m_q) A_q$ ($\det A_q \neq 0$, $m_{q,i} > 0$), strictly excluding $\arg\det(M_u M_d) = \pi$.
   - `jarlskog_commutator_cube_trace` & `strong_cp_zero_coexists_with_jarlskog_cp`: proves $\mathrm{Im}\,\mathrm{Tr}([D, H]^3) = 6(u_0 - u_1)(u_1 - u_2)(u_2 - u_0)\,\mathrm{Im}(H_{01} H_{12} H_{20})$ and exhibits `(witnessMu, witnessMd)` over `QuadI ℤ` with $\det(M_u M_d) = 312 > 0$ (`im = 0`) and $\mathrm{Im}\,\mathrm{Tr}([M_u^2, M_d^2]^3) = -351360 \neq 0$.
   - `det_chiralDressed_im_eq_zero` & `HigherLoopStrongCPFiniteHypothesis`: proves $\mathrm{Im}\det((H_L M_u H_R)(K_L M_d K_R)) = 0$ under factorized 1-loop chiral dressings (even when $[H_L, M_u] \neq 0$ breaks Hermiticity of $H_L M_u H_R$), and isolates non-factorizable 3-loop+ UV counterterm finiteness as a zero-instance conditional class (`§3b-cond`).

3. **$\mathfrak{su}(3)_c$ Casimir Scaling ($9/4$) & Markov-Trace / `ConfinementLayer` Area Law (`§3`):**
   - `su3_fundamental_casimir_matrix`, `su3_adjoint_casimir_matrix`, & `su3_casimir_scaling_and_baryon_half_law`: matrix-commutator proofs of $C_2(\mathbf{3}) = 4/3$, $C_2(\mathbf{8}) = 3$, ratio $C_2(\mathbf{8})/C_2(\mathbf{3}) = 9/4$, and the $\frac{1}{2}$ baryon Y-junction pairwise colour factor ($-2/3$ vs $-4/3$).
   - `markovZ3_eq_div_qIntBal_and_bar_duality`, `markovZ3_confinement_bounds`, `creutz_ratio_cancels_perimeter`, `confinementLayer_worldsheet_area_lower_bound`, & `markovAreaDecay_real`: connects $z_3(q) = q^3/[3]_q$ to `QOU.QInteger.qIntBal q 3`, proves $0 < z_3(q) < 1$ for $0 < q \le 3/2$, proves exact perimeter cancellation in the Creutz ratio, bounds `ConfinementLayerTower.configCost` below by $\Delta_q \cdot \mathrm{Area}$, and proves $z^A = \exp(-(-\ln z) A)$ with $\sigma_{\mathrm{model}} = (-\ln z)/a_{\mathrm{cal}}^2 > 0$.

---

## 2. 80-dps Numerical Evaluation & Honest Comparison Boundary (`q_0 = 1.10997858275...`)

### Arm A — Strong-CP Cancellation & Electroweak Radiative Bounds

- **Dense rotated $3 \times 3$ Hermitian Yukawa pair (`J_CP = 3.5127e-5`):**
  * $\max_{i \neq j}|\mathrm{Im}(M_u)_{ij}| = 0.1595$, $\max_{i \neq j}|\mathrm{Im}(M_d)_{ij}| = 0.0310$, $\|M_u M_d - (M_u M_d)^\dagger\|_\infty = 7.02 \times 10^{-3} \neq 0$;
  * $|\mathrm{Im}\det(M_u M_d)| = 1.96 \times 10^{-86} < 10^{-78}$, $\mathrm{Re}\det(M_u M_d) = +1.912 \times 10^{-13} > 0 \implies \bar{\theta}_{\mathrm{tree}} = 0$ (`1.03e-73 rad` numerical floor);
  * 1-loop left-handed $W^\pm$ dressing $M_u^{(1\text{-loop})} = (I_3 + \Sigma_L^{(1)}) M_u$: $\|M_u^{(1\text{-loop})} - (M_u^{(1\text{-loop})})^\dagger\|_\infty = 3.87 \times 10^{-6} \neq 0$, yet $|\mathrm{Im}\det(M_u^{(1\text{-loop})} M_d)| = 1.37 \times 10^{-86} < 10^{-78}$.
- **Finite 3-loop Ellis–Gaillard electroweak + QCD shift vs PDG-2024:**
  * $|\delta\bar{\theta}_{\mathrm{EW}}^{(3\text{-loop})}| = 2.52 \times 10^{-20}$ (conservative envelope $3.20 \times 10^{-22}$) $\ll 10^{-10}$ (`PDG-2024`);
  * Induced neutron EDM $|d_n|_{\mathrm{EW}} = 6.04 \times 10^{-36}\;e\cdot\mathrm{cm}$ (envelope $7.69 \times 10^{-38}\;e\cdot\mathrm{cm}$) $\ll 1.8 \times 10^{-26}\;e\cdot\mathrm{cm}$ (`PDG-2024`).
  * **Open boundary:** UV counterterm finiteness beyond factorized 1-loop order remains conditional on `HigherLoopStrongCPFiniteHypothesis`.

### Arm B — Zero-Parameter Wilson String Tension Candidates vs Lattice/Regge $[420, 440]\;\mathrm{MeV}$

At $q_0 = 1.10997858275\dots$: $z_3(q_0) = q_0^3/[3]_{q_0} = 0.4493048091$, $-\ln z_3(q_0) = 0.8000537594$, and $\ln [3]_{q_0} = 1.1130759204$.

| Candidate | $a_{\mathrm{cal}}\;[\mathrm{fm}]$ | $\sqrt{\sigma_{\mathbf{3}}}\;[\mathrm{MeV}]$ | $\sqrt{\sigma_{\mathbf{8}}} = \frac{3}{2}\sqrt{\sigma_{\mathbf{3}}}\;[\mathrm{MeV}]$ | $\alpha'\;[\mathrm{GeV}^{-2}]$ | Diff vs $430\;\mathrm{MeV}$ | Verdict |
|---|---:|---:|---:|---:|---:|---|
| `S1_pi_bare` ($a = \lambda_{\pi^\pm}$) | $1.4138$ | $124.84$ | $187.26$ | $10.212$ | $-70.97\%$ | `MISS` |
| `S2_pi_nc3` ($a = \lambda_{\pi^\pm}/3$, $z_3$) | $0.4713$ | $374.52$ | $561.78$ | $1.135$ | $-12.90\%$ | `NEAR_15PCT` |
| `S3_pi_nc3_sym` ($a = \lambda_{\pi^\pm}/3$, $[3]_{q_0}^{-1}$) | $0.4713$ | $441.75$ | $662.63$ | $0.816$ | $+2.73\%$ | `NEAR_15PCT` |
| `S4_mp_compton` ($a = \lambda_p$) | $0.2103$ | $839.24$ | $1258.87$ | $0.226$ | $+95.17\%$ | `MISS` |
| `S5a_rp_full` ($a = 4\lambda_p$) | $0.8412$ | $209.81$ | $314.72$ | $3.615$ | $-51.21\%$ | `MISS` |
| `S5b_rp_half` ($a = 2\lambda_p$, $z_3$) | $0.4206$ | $419.62$ | $629.43$ | $0.904$ | $-2.41\%$ | `NEAR_15PCT` |
| `S6_rp_half_sym` ($a = 2\lambda_p$, $[3]_{q_0}^{-1}$) | $0.4206$ | $494.95$ | $742.42$ | $0.650$ | $+15.10\%$ | `MISS` |
| `S7_diag_codata_rp_half` (diag $r_{p,\mathrm{CODATA}}/2$) | $0.4204$ | $419.86$ | $629.80$ | $0.903$ | $-2.36\%$ | `NEAR_15PCT` |

- **Honest outcome (`selectedCandidate = "none"`, Rule 14):** `0/7` zero-parameter candidates fall strictly inside $[420, 440]\;\mathrm{MeV}$; the two sub-hadronic flux-arm spacings — half QOU proton radius `S5b_rp_half` ($419.62\;\mathrm{MeV}$, $-0.38\;\mathrm{MeV}$ below $420\;\mathrm{MeV}$, $\alpha' = 0.904\;\mathrm{GeV}^{-2}$ vs Regge $0.88\;\mathrm{GeV}^{-2}$) and $N_c=3$ bar-symmetric pion subcell `S3_pi_nc3_sym` ($441.75\;\mathrm{MeV}$, $+1.75\;\mathrm{MeV}$ above $440\;\mathrm{MeV}$, $\alpha' = 0.816\;\mathrm{GeV}^{-2}$) — bracket $[420, 440]\;\mathrm{MeV}$ to $\sim 2.5\%$, whereas un-subdivided pion Compton `S1` and bare proton Compton `S4` miss by factors of $3.4\times$ and $2.0\times$.
