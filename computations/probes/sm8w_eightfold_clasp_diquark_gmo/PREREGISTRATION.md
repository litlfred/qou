# Pre-Registration: Eightfold Way `(V_2, W_3^*)` Framed 3-Strand Hyperbolic Meson Clasp, `H_3(q_0)` `S^{(2,1)}` Diquark Projector Split, and 2nd-Order Quantum Casimir Gell-Mann–Okubo Probe (`qou-8fw2`)

- **Beans:** `qou-8fw2` (parent), `qou-8fl1`, `qou-3ttt`, `qou-qpj9`, `qou-pwz4`, `qou-c9uj`, `qou-3oi0`
- **Branch:** `claude/sm8w-eightfold-wire-clasp-lambda-sigma-20261123`
- **Lean 4 Companions:**
  - `folio/quantum-observable-universe/lean/QOU/Eightfold/HyperbolicMesonClaspAndDiquarkSplit.lean`
  - `folio/quantum-observable-universe/lean/QOU/Eightfold/USpinColemanGlashowLambdaSigma.lean`
  - `folio/quantum-observable-universe/lean/QOU/Eightfold/GellMannOkuboSecondOrder.lean`
- **Probe Script:** `computations/probes/sm8w_eightfold_clasp_diquark_gmo/sm8w_eightfold_clasp_diquark_gmo_probe.py`
- **Witness Output:** `computations/probes/sm8w_eightfold_clasp_diquark_gmo/sm8w-eightfold-clasp-diquark-gmo.witness.json`
- **Precision & Calibration Discipline (`STRICT`):**
  - `workdps = 80` (`mpmath.mp.workdps(80)`), zero `float64` (`probe-float64-guard.py --diff`, `witness_raw_float64_audit.py --strict`, `mpf_context_dps_audit.py --strict`).
  - `q0Anchor = "proton"`: canonical 1-term proton substrate pin `q_0 = q_at(80)` (`qou_substrate.constants`).
  - **ZERO FITTING (`CAL-1/2/3` ONLY):** No parameter is tuned to PDG hadron masses (`Lambda`, `Sigma^0`, `K`, `eta`, `Xi`, `D^0`). PDG-2024 hadron masses enter strictly as downstream validation comparators; any quantitative under- or over-prediction by a zero-parameter mechanism is reported honestly as an empirical miss / scope boundary.

---

## 1. Fixed Inputs & Zero-Parameter Operators

1. **Substrate parameters at `80 dps`:**
   - `q_0 = q_at(80)`, `h_0 = q_0 - q_0^{-1}`, `[n]_{q_0} = (q_0^n - q_0^{-n}) / (q_0 - q_0^{-1})`.
   - Rank-2 (Convention-D / `V_2`) Markov parameter: `z_2 = q_0^2 / [2]_{q_0} = q_0^3 / (q_0^2 + 1)`.
   - Rank-3 (`W_3^*` flavour/colour split-bundle) Markov parameter: `z_3 = q_0^3 / [3]_{q_0} = q_0^5 / (q_0^4 + q_0^2 + 1)`.
2. **PDG-2024 / CODATA-2022 downstream validation comparators (never used as upstream inputs):**
   - Registry imports (`codata_constants`): `M_E_MEV`, `M_P_MEV_VALIDATION`, `M_N_MEV_VALIDATION`, `M_PI_PM_MEV_VALIDATION`, `M_PI_0_MEV_VALIDATION`, `M_K_PM_MEV_VALIDATION`, `M_K_0_MEV_VALIDATION`.
   - PDG-2024 octet hadron validation comparators:
     - `m_Lambda = 1115.683 MeV`, `m_Sigma0 = 1192.642 MeV` (`m_Sigma0 - m_Lambda = 76.959 MeV`),
     - `m_Sigma_plus = 1189.37 MeV`, `m_Sigma_minus = 1197.449 MeV`,
     - `m_Xi0 = 1314.86 MeV`, `m_Xi_minus = 1321.71 MeV`,
     - `m_eta = 547.862 MeV`.

---

## 2. Pre-Registered Analytical Predictions & Falsification Criteria (`tol = 1e-75 .. 1e-78` at `80 dps`)

### P1 — `(V_2, W_3^*)` Split-Bundle Framing, `W_3^{\otimes 3} = 10 \oplus 8 \oplus 8 \oplus 1`, and 3-Strand Hyperbolic Meson Clasp (`qou-3ttt`, `qou-qpj9`, `qou-3oi0`)

1. **Split-bundle `F = V_2 \oplus W_3^*` & Quantum `W_3^{\otimes 3}` Decomposition:**
   - `z_2(q_0) - z_3(q_0) = q_0^3 / ((q_0^2 + 1)(q_0^4 + q_0^2 + 1)) > 0` holds to `< 10^{-78}`.
   - Quantum Schur–Weyl dimension sum `dim_{q_0}(10) + 2 dim_{q_0}(8) + dim_{q_0}(1) = [3]_{q_0}^3` (with `dim_q(10) = (q^2 + q^{-2})[5]_q`, `dim_q(8) = [2]_q [4]_q`, `dim_q(1) = 1`, classical limit `10 + 2*8 + 1 = 27`) and rank-3 Ocneanu trace normalization `w_{(3)}(q_0, z_3) + 2 w_{(2,1)}(q_0, z_3) + w_{(1^3)}(q_0, z_3) = 1` (`w_{(1^3)}(q_0, z_3) = [3]_{q_0}^{-3} > 0` vs `w_{(1^3)}(q_0, z_2) = 0`) hold to `< 10^{-78}`.
   - `(V_2, W_3^*)`-framed quark/antiquark charge `Q(s_2, tau_3) = s_2 / 2 + tau_3 / 6` produces `(+2/3, -1/3, +1/3, -2/3)` on `(u, d, d_bar, u_bar)`, separating `u_bar` (`-2/3`) from `d` (`-1/3`) by `+1/3 != 0` despite equal crossing sign `s_2 = -1`.
2. **3-Strand Gluon-Clasp Map `(n_1, n_2) in {3, 5, 7}^2 |-> beta_clasp(n_1, n_2) = sigma_1^{n_1} sigma_2^{-n_2} sigma_1 sigma_2^{-1} in B_3`:**
   - Across all `9` pairs `(n_1, n_2) in {3, 5, 7}^2`, `det rho_{(2,1)}(beta_clasp(n_1, n_2)) = 1` to `< 10^{-76}`.
   - Classical Thurston `SL_2(Z)` monodromy trace satisfies `tr_{SL_2(Z)}(beta_clasp(n_1, n_2)) = 2 n_1 n_2 + n_1 + n_2 + 3 >= 27 > 2` (hyperbolic / pseudo-Anosov on all `9` pairs, spectral radius `lambda_pA > 26.96`, bypassing `Vol = 0` 2-strand torus closures), and `|tr rho_{(2,1)}(beta_clasp(n_1, n_2))|_{q_0} > 27 > 2` across all `9` pairs.
   - **Ordered-pair `D_bar^0 = (-5, +3)` vs `K^0 = (+3, -5)` separation:** While the `2 x 2` `SL_2` trace `tr rho_{(2,1)}(beta_clasp(n_1, n_2))` is symmetric under `n_1 <-> n_2` (`|tr_{(2,1)}(5,3) - tr_{(2,1)}(3,5)| < 10^{-75}`), both the rank-2 (`z_2`) and rank-3 (`z_3`) full `H_3(q_0)` Markov traces strictly separate `(n_1, n_2)` from `(n_2, n_1)` for every `n_1 != n_2` via the exact closed identities:
     - `tr_{M,2}(beta_clasp(n_1, n_2)) - tr_{M,2}(beta_clasp(n_2, n_1)) = w_{(3)}(q_0, z_2) (q_0^{n_1 - n_2} - q_0^{-(n_1 - n_2)}) != 0`,
     - `tr_{M,3}(beta_clasp(n_1, n_2)) - tr_{M,3}(beta_clasp(n_2, n_1)) = (w_{(3)}(q_0, z_3) - w_{(1^3)}(q_0, z_3)) (q_0^{n_1 - n_2} - q_0^{-(n_1 - n_2)}) != 0`,
     verified to `< 10^{-75}` on `(5,3)` vs `(3,5)` (`D_bar^0` vs `K^0`), `(7,3)` vs `(3,7)`, and `(7,5)` vs `(5,7)`. Together with `(V_2, W_3^*)` framed constituent charges `(Q_1, Q_2)`, all `5` dictionary mesons (`pion`, `kaon`, `etaPhi`, `Dmeson`, `K0`) carry pairwise distinct invariants.

### P2 — Zero-Parameter `H_3(q_0)` `S^{(2,1)}` Diquark Spin-Isospin Projector Split vs `m_{Sigma^0} - m_Lambda = 76.959 MeV` (`qou-pwz4`)

1. **Exact Idempotent Split in Both 2D `S^{(2,1)}` and 3D Baryon Weight Space `W`:**
   - `P_Lambda(q_0) + P_{Sigma^0}(q_0) = I_2` on `S^{(2,1)}` and `eLambda(q_0) + eSigma0(q_0) = e21p(q_0)` on `W` satisfy idempotency, mutual orthogonality, unit trace, and cross-representation trace equality on `sigma_1`, `sigma_2`, `V = sigma_1 sigma_2^{-1}`, and `V^3 = (sigma_1 sigma_2^{-1})^3` to `< 10^{-76}`.
2. **Closed-Form Zero-Parameter Diquark Splittings & Honest PDG Comparison:**
   - Adjacent `ud` crossing `sigma_1`: `tr(P_{Sigma^0} sigma_1) - tr(P_Lambda sigma_1) = q_0 + q_0^{-1} = [2]_{q_0} > 0`.
   - Commuting Jucys–Murphy twists `J_2 = sigma_1^2`, `J_3 = sigma_2 sigma_1^2 sigma_2` (`[J_2, J_3] = 0`): `tr(P_{Sigma^0} J_2) = q_0^2`, `tr(P_Lambda J_2) = q_0^{-2}`, ratio `q_0^4`, difference `q_0^2 - q_0^{-2} = h_0 [2]_{q_0} > 0`.
   - Single Borromean period `V = sigma_1 sigma_2^{-1}`: `|tr(P_{Sigma^0} V)| / |tr(P_Lambda V)| = q_0^6`, `|tr(P_{Sigma^0} V)| - |tr(P_Lambda V)| = h_0 [3]_{q_0} / [2]_{q_0} > 0`.
   - Full Borromean braid `V^3 = (sigma_1 sigma_2^{-1})^3`:
     `tr(P_Lambda V^3) - tr(P_{Sigma^0} V^3) = h_0^3 [3]_{q_0} [4]_{q_0} / [2]_{q_0}^2 > 0`
     holds to `< 10^{-76}`.
   - **Honest empirical comparison (no fitting):** Compare the zero-parameter scale-free ratios `q_0`, `q_0^2`, `q_0^4`, `1 + h_0 [2]_{q_0} / 2`, and `1 + h_0^3 [3]_{q_0} [4]_{q_0} / [2]_{q_0}^2` against `m_{Sigma^0} / m_Lambda = 1192.642 / 1115.683 = 1.06897927...` (`Delta m = 76.959 MeV`, relative split `6.898%` over `m_Lambda`), recording exact relative residuals without introducing any fitted constant, and verify exact microscopic Borromean `V^3` Coleman–Glashow QED cancellation to `< 10^{-78}`.

### P3 — `O((q_0 - q_0^{-1})^2)` 2nd-Order Quantum Casimir Correction to Gell-Mann–Okubo vs PDG-2024 (`qou-c9uj`)

1. **Exact Parameter-Free Quantum Casimir GMO Ratio Identity:**
   - For the rational quantum Casimir `d_q(I, Y) = [I]_q [I+1]_q - [Y/2]_q^2` (`d_q(1,0) = [2]_q`, `d_q(0,0) = 0`, `d_q(1/2, +-1) = [2]_q / ([2]_q + 2)`), any octet mass/mass-squared law `M(I, Y) = a + b Y + c d_q(I, Y)` (`c != 0`) satisfies the `(a, b, c)`-independent identity:
     $$\frac{4 M_{\mathrm{avg}}(1/2, \pm 1) - 3 M(0, 0) - M(1, 0)}{M(1, 0) - M(0, 0)} = -\left(\frac{q - 1}{q + 1}\right)^2 = -\frac{(q - q^{-1})^2}{([2]_q + 2)^2}$$
     verified at `q = q_0` to `< 10^{-78}` across distinct arbitrary test triples `(a, b, c)`.
2. **Sign Agreement & Honest Magnitude Deficit vs PDG-2024:**
   - **Sign prediction (both octets simultaneously):** Because `m_pi^2 - m_eta^2 < 0` on the pseudoscalar meson octet while `m_Sigma - m_Lambda > 0` on the baryon octet, multiplying by `-((q_0 - 1)/(q_0 + 1))^2 < 0` predicts `4 m_K^2 - 3 m_eta^2 - m_pi^2 > 0` for mesons AND `2(m_N + m_Xi) - 3 m_Lambda - m_Sigma < 0` for baryons — matching BOTH observed PDG-2024 signs without free parameters.
   - **Honest magnitude comparison:** Evaluate `((q_0 - 1)/(q_0 + 1))^2` (`approx 2.716 x 10^{-3}`) against the observed PDG-2024 normalized ratios `(4 m_K^2 - 3 m_eta^2 - m_pi^2) / (m_eta^2 - m_pi^2)` (`approx 0.220`, corresponding to the `approx 6.1%–6.5%` meson GMO deviation over `4 m_K^2`) and `(3 m_Lambda + m_Sigma - 2(m_N + m_Xi)) / (m_Sigma - m_Lambda)` (`approx 0.333`, corresponding to the `approx 0.57%` baryon GMO deviation over `2(m_N + m_Xi)`), demonstrating that single-`q_0` `U_{q_0}(su_2)_I` Casimir curvature accounts for only `~1.2%` of the meson GMO deviation and `~0.8%` of the baryon GMO deviation, leaving the bulk of the `~6%` meson deviation to `eta`–`eta'` singlet mixing (`NonetMixingUnconstrained.lean`) and higher-order `SU(3)_f` breaking (`[kleinkreisler1996]`).
