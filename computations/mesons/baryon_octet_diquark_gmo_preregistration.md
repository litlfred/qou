# Pre-Registration: Zero-Parameter Baryon Octet `Λ⁰–Σ⁰` Diquark Splitting, 2nd-Order Gell-Mann–Okubo, and Decuplet Curvature Catalog (`qou-8fw2`, `qou-d7h1`, `qou-wyy9`, `#9375`)

**Date:** 2026-11-24  
**Branch:** `claude/eightfold-baryon-diquark-lambda-sigma-gmo-20261124`  
**Epistemic Discipline:** Strictly zero fitted parameters, zero production wiring, multi-arm reporting at both `q_proton` and `q_muon` (`mp.mp.dps = 80`). Committed strictly prior to authoring and running `computations/mesons/baryon_octet_diquark_gmo_probe.py`.

---

## 1. Pre-Committed Zero-Parameter Scale Candidates for $\Delta m_{\Sigma^0 - \Lambda^0}$

Given the Temperley–Lieb $(u, d)$ diquark exchange operator $e_{12} = q I - \sigma_1$ on $S^{(2,1)}$ with exact eigenvalue split $\operatorname{tr}(P_{\Lambda} e_{12}) - \operatorname{tr}(P_{\Sigma^0} e_{12}) = [2]_q = q + q^{-1}$, the six canonical zero-parameter QOU energy combinations tested against $\Delta m_{\Sigma^0 - \Lambda^0}^{\mathrm{PDG}} = 1192.642(24) - 1115.683(6) = 76.959(25)\text{ MeV}$ are fixed *a priori* as:

1. **`S1_E0_b3sq_b2`**: $E_0(q) \cdot [3]_q^2 \cdot [2]_q$, where $E_0(q) = \frac{m_e}{q(q-1)}$ is the fundamental nucleon/beta energy quantum, $[3]_q^2 = \dim_q(W_3^* \otimes W_3)$, and $[2]_q$ is the $e_{12}$ diquark eigenvalue split.
2. **`S2_E0_dimq8_b2`**: $E_0(q) \cdot \dim_q(\mathbf{8}_q) \cdot [2]_q = E_0(q) \cdot [2]_q^2 [4]_q$ (traceless octet dimension $\dim_q(\mathbf{8}_q) = [3]_q^2 - 1 = [2]_q[4]_q$ times the $[2]_q$ diquark split).
3. **`S3_mpi_over_b2`**: $\frac{m_{\pi^\pm}}{[2]_q}$ (chiral pion scale divided by the $[2]_q$ diquark exchange factor).
4. **`S4_mp_h_over_b3`**: $m_p \cdot \frac{q - q^{-1}}{[3]_q}$ (nucleon scale times the balanced skein parameter per $W_3^*$ flavor dimension).
5. **`S5_mp_hbar_b2_over_b3`**: $m_p \cdot \frac{(1 - q^{-1})[2]_q}{[3]_q}$ (nucleon scale times the asymmetric Planck step and $[2]_q / [3]_q$).
6. **`S6_mp_V3_diquark_split`**: $m_p \cdot \frac{(q - q^{-1})^3 (q^2 + q^{-2}) [3]_q}{[2]_q}$ (nucleon scale times the 4th-order Borromean $V^3$ diquark projector trace difference).

---

## 2. Pre-Committed 2nd-Order Octet GMO & Decuplet Curvature Tests

1. **Rational Quantum Casimir $d_q(I, Y) = [I]_q[I+1]_q - [Y/2]_q^2$ on the Baryon Octet:**
   - Normalized $(M_0, a, c)$-free GMO ratio:
     $$\frac{2(M_N + M_\Xi) - 3 M_\Lambda - M_\Sigma}{M_\Sigma - M_\Lambda} = -\left(\frac{q - 1}{q + 1}\right)^2$$
     evaluated against PDG 2024 isospin-averaged octet masses ($M_N = \frac{m_p + m_n}{2}$, $M_\Xi = \frac{m_{\Xi^0} + m_{\Xi^-}}{2}$, $M_\Sigma = \frac{m_{\Sigma^+} + m_{\Sigma^0} + m_{\Sigma^-}}{3}$, $M_\Lambda = m_{\Lambda^0}$; note $2(M_N + M_\Xi) - 3 M_\Lambda - M_\Sigma \approx -25.68\text{ MeV}$, or half-combination $(M_N + M_\Xi) - \frac{3 M_\Lambda + M_\Sigma}{2} \approx -12.84\text{ MeV}$, and neutral-only $2(m_n + m_{\Xi^0}) - 3 m_{\Lambda^0} - m_{\Sigma^0} \approx -20.83\text{ MeV}$ — both normalization conventions reported transparently!).
2. **Weighted Jucys–Murphy $27 \times 27$ Operator (`u < d < s` vs `s < u < d`):**
   - Exact closed-form rational verification of $M_{\Sigma^0} - M_\Lambda$ and $\mathrm{GMO} / (M_\Xi - M_N)$ in both adjacent-(u,d) flavor orders, testing both sign and magnitude against PDG.
3. **Rational Quantum Casimir $d_q(I, Y)$ on the Baryon Decuplet ($\Delta, \Sigma^*, \Xi^*, \Omega^-$):**
   - Exact $(M_0, a, c)$-free ratio of upper to lower second differences:
     $$\frac{M_{\Omega^-} - 2 M_{\Xi^*} + M_{\Sigma^*}}{M_{\Xi^*} - 2 M_{\Sigma^*} + M_\Delta} = \frac{1}{q + 1 + q^{-1}}$$
     plus predicted MeV second differences using $c_{\mathrm{baryon}} = (M_\Sigma - M_\Lambda) / [2]_q$ (zero new parameters), tested directly against PDG 2024 decuplet spacings ($\Delta(1232), \Sigma^*(1385), \Xi^*(1530), \Omega^-(1672.45)$) as a strict sign-and-ratio falsification test.
