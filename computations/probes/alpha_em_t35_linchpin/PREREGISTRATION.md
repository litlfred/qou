# Pre-Registration: $[10]_q$ $T(3,5)$ Linchpin, Weight-3 Two-Loop $\Delta_2$ Candidate Test, $2\ln t = -\alpha_{\mathrm{EM}}(q)$ Hadron-Line Coupling, and $E(Q)^{\mathrm{conn}}$ Positivity Bounds (2026-11-23)

Beans `qou-15sj`, `qou-ha6c`, `qou-itdn`, `qou-006b` (`Q-Gap-1`). Written and committed **before** evaluating any candidate two-loop $\Delta_2$ closed forms against CODATA-2022 or computing $\mathcal{W}(q_0) = t_1 + c_{\mathrm{em}} t_2$ at the substrate pin.

## 1. Calibration, Anchor & Precision Discipline (STRICT)

- **Working precision:** `mpmath.workdps(80)` throughout (`OUT_DPS = 50`), zero `float64` imports, literals, or casts (`probe-float64-guard.py --strict` / `--diff` clean).
- **Substrate pin:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`).
- **Allowed calibrations:** CAL-1 $m_e$, CAL-2 / proton-pinned $q_0$ via $\operatorname{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ (`vol_4_1_at(80)`), CAL-3 $m_\pi$ (not needed in pure dimensionless QED / knot invariants).
- **Experimental comparison isolation:** CODATA-2022 `inverse fine-structure constant` $\alpha_{\mathrm{CODATA2022}}^{-1} = 137.035999177 \pm 2.1 \times 10^{-8}$ (`qou_substrate.codata.codata("inverse fine-structure constant")`) enters **solely** in comparison/falsification columns, never inside any substrate, coupling, or two-term formula. No candidate coefficient, integer prefactor, or sign is tuned or post-hoc selected.

---

## 2. Pre-Registered Mathematical & Numerical Tests

### Part A — Exact $T(3,5)$ Knot Invariants vs $q [9]_q [10]_q$ Linchpin (`qou-15sj`, `qou-itdn`, `qou-006b`)

1. **Diophantine Genus-4 Uniqueness & Writhe/Span Coincidence:**
   - Verify that among coprime torus knots $T(p, r)$ ($2 \le p < r$, $\gcd(p, r) = 1$), $g(T_{p,r}) = (p-1)(r-1)/2 = 4 = g(\Sigma_{\mathrm{Bring}})$ holds uniquely for $\{T(2,9), T(3,5)\}$, with minimal positive-braid writhes $w(T_{2,9}) = 9$ and $w(T_{3,5}) = 10 = 2g(T_{3,5}) + 2$, whereas the 2-strand meson knots $T(2,3), T(2,5), T(2,7)$ have genera $g \in \{1, 2, 3\}$.
2. **Exact $T(3,5)$ Invariants at $q_0$ (and Exact Rational Points $q \in \{2, 3/2\}$ + Classical Limit $q \to 1$):**
   - **Symmetrized Alexander polynomial** at $t = q^2$:
     $$\Delta_{T(3,5)}(q^2) = \frac{(q - q^{-1})(q^{15} - q^{-15})}{(q^3 - q^{-3})(q^5 - q^{-5})} = q^8 - q^6 + q^2 - 1 + q^{-2} - q^{-6} + q^{-8},$$
     and at $t = q^4$ (skein variable $t^{1/2} = q^2$):
     $$\Delta_{T(3,5)}(q^4) = \frac{(q^2 - q^{-2})(q^{30} - q^{-30})}{(q^6 - q^{-6})(q^{10} - q^{-10})} = q^{16} - q^{12} + q^4 - 1 + q^{-4} - q^{-12} + q^{-16},$$
     verifying the 3-strand reduced Burau determinant $\det(I_2 - B_{q^2}(\beta_{3,5})) = 1 + q^{10} + q^{20} = (1 - q^{30})/(1 - q^{10})$ and the denominator identity $(q^{10} - q^{-10})/(q - q^{-1}) = [10]_q$, $(q^{10} - q^{-10})(q + q^{-1})/(q - q^{-1}) = [10]_q [2]_q$.
   - **Standard Jones polynomial ($N = 2$):** $V_{T(3,5)}(t) = t^4 + t^6 - t^{10}$ evaluated at $t = q_0^2$ and $t = q_0^{-2}$, cross-checked against the Convention-D Markov trace `WeakVertexT35.weakVertexTrace(q_0) = q_0^2(q_0^{12} + q_0^8 - 1)/(q_0^2 + 1)^2`.
   - **HOMFLY-PT $U_q(\mathfrak{sl}_N)$ specializations ($N = 2, 3$):**
     $$P_{T(3,5)}^{(N=3)}(q) = \frac{q^{-30}}{[3]_q}\left(\frac{[4]_q [5]_q}{[2]_q} q^{10} - [2]_q [4]_q + q^{-10}\right) = q^{-30}\left(q^{14} + q^{10} + q^8 - 2 - q^{-6} + q^{-8}\right).$$
   - **3-Irrep $H_3(q)$ Rosso–Jones vs Conjugation-Skew Top-Channel Audit (`qou-15sj`):**
     Verify that on $\beta_{3,5} = (\sigma_0 \sigma_1)^5$, $(\chi_{(3)}, \chi_{(2,1)}, \chi_{(1,1,1)}) = (q^{10}, -1, q^{-10})$, so $w_3 q^{10} - w_{21} + w_{111} q^{-10} = (q - q^{-1})[10]_q$ holds iff $(w_3, w_{21}, w_{111}) = (1, 0, -1)$ (partition-conjugation antisymmetric / bar-skew projection $\frac{1}{2}(\chi_\lambda - \chi_{\lambda'})$), whereas $N=2$ and $N=3$ quantum-dimension weights do **not** collapse to $[10]_q$. Verify $[9]_q [10]_q = \sum_{k=1}^9 [2k]_q$ (`= 90` at $q=1$) and $q = 1$ interface selectivity (`qou-itdn`: $V_L(1) = (-2)^{c-1}$ vs hadron-line $t(1)$).

---

### Part B — Pre-Registered Zero-Parameter Candidate Closed Forms for Weight-3 Two-Loop $\Delta_2$

In the Bring–Schwinger relation (`EmCouplingBringZeroMode.lean`):
$$\frac{1}{\alpha_{\mathrm{EM}}} = q_0 [9]_{q_0} [10]_{q_0} + \frac{2}{3\pi} + \alpha_{\mathrm{EM}} H(q_0)\big(1 - h_0^2 \alpha_{\mathrm{EM}}\big) + \Delta_2, \qquad H(q) = \frac{[2]_q}{8\pi},\quad h_0 = q_0 - q_0^{-1},$$
let $\alpha_B(q_0)$ denote the unique positive root at $\Delta_2 = 0$ (Form B), and $\alpha_A(q_0)$ the quadratic root without $-h_0^2 \alpha_{\mathrm{EM}}$ (Form A). Define the CODATA-2022 implied residual:
$$\Delta_2^{\mathrm{emp}} := \alpha_{\mathrm{CODATA2022}}^{-1} - \alpha_B^{-1}(q_0), \qquad c_2^{(+,\mathrm{emp})} := \frac{\Delta_2^{\mathrm{emp}}}{\alpha_B(q_0)^2}, \qquad c_2^{(-,\mathrm{emp})} := -\frac{\Delta_2^{\mathrm{emp}}}{\alpha_B(q_0)^2} = \frac{\alpha_B^{-1}(q_0) - \alpha_{\mathrm{CODATA2022}}^{-1}}{\alpha_B(q_0)^2}$$
(alongside the historical CODATA-2018 reference solely to document the `-0.313 ppb` $\to$ `-0.365 ppb` edition shift).

We pre-register the following **14 fixed zero-parameter candidate magnitudes** $|c_2|$, each tested symmetrically under both signs $\Delta_2 = \pm |c_2|\,\alpha^2$ (via exact self-consistent fixed-point root solve of $\alpha^{-1} = T_{\mathrm{tree}} + \frac{2}{3\pi} + \alpha H(1 - h_0^2 \alpha) \pm |c_2|\alpha^2$), plus Candidate `C4b` replacing Form B's $-h_0^2 H \alpha^2$ by the Penrose $\theta$-graph term $-\frac{[3]_{q_0}}{(8\pi)^2}\alpha^2$ on Form A:

| ID | Candidate family | Zero-parameter formula for $|c_2|$ (or $\Delta c_2$) | Weight / origin |
|---|---|---|---|
| `C1a` | Schwinger–Broadhurst $\zeta(3)/\pi^3$ | $\zeta(3) / \pi^3$ | Weight-3 Riemann $\zeta(3)$ over $\pi^3$ |
| `C1b` | Bring-$b_1$ Broadhurst | $\zeta(3) / (8 \pi^3)$ | $b_1(\Sigma_{\mathrm{Bring}}) = 8$ harmonic 1-cycles |
| `C1c` | Bring-Jacobian 2-loop $\zeta(3)$ | $\zeta(3) / (8 \pi)^2$ | Per-loop measure $1/(8\pi)^2 \times \zeta(3)$ |
| `C1d` | Jost–Luttinger 2-loop QED | $1 / (4 \pi^2)$ | Standard 4D QED 2-loop vacuum polarization |
| `C1e` | Petermann–Sommerfield weight-3 part | $3\,\zeta(3) / (4 \pi^2)$ | Pure $\zeta(3)$ piece of 2-loop QED $(g-2)_e$ |
| `C2a` | Hyperbolic $4_1$ volume over $\pi^2$ | $\operatorname{Vol}(4_1) / \pi^2$ | Weight-2 Bloch–Wigner $2 D(e^{i\pi/3})/\pi^2$ |
| `C2b` | Single ideal tetrahedron $D(z_{4_1})/\pi^2$ | $D(z_{4_1}) / \pi^2 = \operatorname{Vol}(4_1) / (2\pi^2)$ | Single regular ideal simplex Bloch–Wigner |
| `C2c` | Bring-Jacobian $4_1$ volume | $\operatorname{Vol}(4_1) / (8\pi)^2$ | $\operatorname{Vol}(4_1)$ with 2-loop Jacobian measure $1/(8\pi)^2$ |
| `C2d` | Bring-Area $4_1$ volume | $\operatorname{Vol}(4_1) / (12\pi)^2$ | $\operatorname{Vol}(4_1)$ with Gauss–Bonnet $\mathrm{Area}(\Sigma_4)^2$ |
| `C3a` | Bare Habiro $\times \zeta(3)$ | $h_0^2\,\zeta(3)$ | Skein square $h_0^2 = (q_0 - q_0^{-1})^2 \times \zeta(3)$ |
| `C3b` | 1-loop Bring Habiro $\times \zeta(3)$ | $h_0^2\,\zeta(3) / (8\pi)$ | $h_0^2 \zeta(3)$ over $b_1 \pi = 8\pi$ |
| `C3c` | Asymmetric $\hbar_{q_0}^2 \zeta(3)/\pi^2$ | $(1 - q_0^{-1})^2\,\zeta(3) / \pi^2$ | Asymmetric Hecke $\hbar_{q_0}^2 \times \zeta(3)/\pi^2$ |
| `C3d` | Penrose $\theta(1,1,2) \times \zeta(3)$ | $[3]_{q_0}\,\zeta(3) / (8\pi)^2$ | 2-loop $\theta$-graph $[3]_{q_0} \times \zeta(3)/(8\pi)^2$ |
| `C4a` | Penrose $\theta(1,1,2)$ on Form B | $[3]_{q_0} / (8\pi)^2$ | Additive $[3]_{q_0}/(8\pi)^2$ atop Form B |
| `C4b` | Penrose $\theta(1,1,2)$ replacing $-h_0^2 H$ | $\Delta c_2 = -[3]_{q_0}/(8\pi)^2 + h_0^2 H(q_0)$ | Exact Form-A $-\alpha^2 [3]_{q_0}/(8\pi)^2$ ladder (`2026-07-14` audit) |

**Pre-registered falsification & $q$-locality criteria:**
- **Pass ($1\sigma$):** $|\alpha_{\mathrm{cand}}^{-1}(q_0) - \alpha_{\mathrm{CODATA2022}}^{-1}| \le 1\,\sigma_{\mathrm{CODATA}} = 2.1 \times 10^{-8}$ ($0.1532\;\text{ppb}$).
- **Consistent ($2\sigma$):** $\le 2\,\sigma_{\mathrm{CODATA}} = 4.2 \times 10^{-8}$ ($0.3065\;\text{ppb}$).
- **Miss / Falsified:** $> 2\,\sigma_{\mathrm{CODATA}}$.
- **$q$-locality check:** Evaluate `d ln(1/α) / d ln q` at $q_0$ and finite-difference slope across $[q_0 - 0.05, q_0 + 0.05]$ for every candidate. Every pass and every miss is reported verbatim in the witness with zero post-hoc selection.

---

### Part C — Hadron Charge-Line $2\ln t = -\alpha_{\mathrm{EM}}(q_0)$, $c_{\mathrm{em}}$ Normalizations, $\mathcal{W}(q_0)$, & $E(Q)^{\mathrm{conn}}$ Positivity (`qou-ha6c`)

1. **Hadron Charge-Line Coupling & Exponential Jet:**
   - Set $t(q_0) = \exp(-\alpha_B(q_0)/2)$, verify $2\ln t(q_0) = -\alpha_B(q_0)$ (`HadronChargeLineCoulomb.em_coulombOnNucleons` strength $\kappa_{\mathrm{Coul}} = -\alpha_B(q_0)$), and check the alternating Taylor bounds:
     $$\alpha_B(q_0) - \frac{1}{2}\alpha_B(q_0)^2 \;\le\; 1 - t(q_0)^2 \;\le\; \alpha_B(q_0) - \frac{1}{2}\alpha_B(q_0)^2 + \frac{1}{6}\alpha_B(q_0)^3.$$
2. **Two-Term Weak-Vertex Form Factor $\mathcal{W}(q_0) = t_1(q_0) + c_{\mathrm{em}} t_2(q_0)$:**
   - Evaluate $t_1(q_0) = \mathcal{W}_{\mathrm{conv\text{-}D}}(q_0)$ and $t_2(q_0)$ for uniform quark charges ($t_2 = 0$ identically) and mixed C-lep strand-0 charges (`QpLeptonFirst`, `QmLeptonFirst`), across the three zero-parameter $c_{\mathrm{em}}$ normalizations:
     * **N1 (Monodromy log-coupling):** $c_{\mathrm{em}}^{(\mathrm{mon})} = -2\ln t(q_0) = \alpha_B(q_0)$;
     * **N2 (Chordal holonomy jet):** $c_{\mathrm{em}}^{(\mathrm{jet})} = 1 - t(q_0)^2 = 1 - \exp(-\alpha_B(q_0))$;
     * **N3 (Categorical Lagrangian Reeb-scale ratio):** $c_{\mathrm{em}}^{(\mathrm{Lag})} = \alpha_B(q_0) / (1 - q_0^{-1})$.
3. **Gatermann–Parrilo / Verstichel–van Aggelen Semidefinite Positivity Bounds on $E(Q)^{\mathrm{conn}}$:**
   - Verify the Wedderburn isotypic eigendecomposition $E(Q)^{\mathrm{conn}} = \kappa(Q) P_3 + (-\frac{1}{2}\kappa(Q))(I_3 - P_3)$, the Cartan inner-derivation Hilbert–Schmidt identity $-\frac{1}{2}\operatorname{Tr}([Q, P_3]^2) = \operatorname{Var}_{P_3}(Q) \ge 0$, the Cauchy–Schwarz bound $\kappa(Q)^2 \le (\sum_b (d_b - 1/3)^2)(\sum_b (Q_b - \bar{Q})^2)$, and the dressed density-kernel semidefinite cone $I_3 + c_{\mathrm{em}} E(Q)^{\mathrm{conn}} \succeq 0 \iff c_{\mathrm{em}}\,\kappa(Q) \in [-1, 2]$ across both $W_{+1}$ and $W_{-1}$ and all three $c_{\mathrm{em}}$ normalizations.
