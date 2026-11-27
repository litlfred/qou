# Pre-Registration: Strong-CP $\bar{\theta}_{\mathrm{QCD}} = 0$ Writhe/Determinant Cancellation & $q$-Deformed Wilson String Tension Probe (`qou-tcpx` / `Q-Gap-11`)

- **Bean:** `qou-tcpx` (`Q-Gap-11`, parent epic `qou-sm8w`; linked legacy beans `tqcp`, `qou-1jqd`, `qou-db6w`).
- **Companion Lean 4 module:** `folio/quantum-observable-universe/lean/QOU/StandardModel/StrongCPWritheCancellationAndStringTension.lean`.
- **Pre-registration rule:** Written and committed **prior to** running any `80`-dps numerical evaluation. Zero empirical parameters are tuned or fitted (`NO FITTING EXCEPT CAL-1/2/3`; `selected = "none"` under Rule 14).

---

## 1. Precision, Anchor & Isolation Discipline (`STRICT`)

1. **Working precision:** `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized decimal strings), zero `float64` imports (`math`, `numpy`, `cmath`, `scipy`, `statistics` banned), zero `float(...)` / `complex(...)` casts, zero binary64 literals (`scripts/probe-float64-guard.py --diff`, `computations/witness_raw_float64_audit.py --strict`, and `computations/mpf_context_dps_audit.py --strict` all required exit `0`).
2. **Substrate anchor:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`), with `CAL-1` electron mass $m_e$ (`codata("electron mass energy equivalent in MeV")`), proton substrate mass $m_p(q_0)$ (and CODATA validation cross-check), and `CAL-3` charged-pion mass $m_{\pi^\pm} = 139.57039\;\mathrm{MeV}$.
3. **Strict empirical comparison boundary:** Empirical bounds (`PDG-2024` $|\bar{\theta}_{\mathrm{QCD}}| < 10^{-10}$, neutron EDM $|d_n| < 1.8 \times 10^{-26}\;e\cdot\mathrm{cm}$, lattice/Regge fundamental string tension $\sqrt{\sigma} \in [420, 440]\;\mathrm{MeV}$ with Regge reference $\alpha' = 0.88\;\mathrm{GeV}^{-2} \implies \sqrt{\sigma_{\mathrm{Regge}}} = (2\pi\alpha')^{-1/2} \approx 425.3\;\mathrm{MeV}$, and PDG quark/EW masses for the Ellis–Gaillard 3-loop order-of-magnitude check) enter **solely** in comparison/diagnostic columns, never inside `.lean` proofs or QOU substrate formulas.

---

## 2. Pre-Registered Tests — Arm A: Strong-CP $\bar{\theta}_{\mathrm{QCD}} = \theta_{\mathrm{top}} + \arg\det(M_u M_d) = 0$

### A1. Topological Writhe Cancellation & $\mathrm{SU}(3)_c$ Colour-Singlet Framing (`\theta_{\mathrm{top}} = 0`)

1. **Amphicheiral Vacuum & Mirror-Paired Gluon Flux Tubes at $q_0$:**
   - Verify $w(\beta_{4_1}) = 0$ on $\beta_{4_1} = \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$, $w(\beta_{\mathrm{Bor}}) = 0$ on $\beta_{\mathrm{Bor}} = (\sigma_1 \sigma_2^{-1})^3$, chiral single-gluon writhe $w(T(2,9)) = +9 \neq 0$ (`q_0^9 - q_0^{-9} != 0`), and exact mirror-pair cancellation $w(T(2,9) \oplus \overline{T(2,9)}) = 0 \implies \Theta = q_0^0 = +1$ ($\theta_{\mathrm{top}} = 0$, strictly excluding $\Theta = -1$ / $\theta = \pi$ since $q_0 > 1$).
2. **$\mathrm{SU}(3)_c$ $[1^3]$ Antisymmetrizer & $\mathrm{SL}_3$ Singlet Invariance:**
   - Verify on $(\mathbb{Q}^3)^{\otimes 3}$ (`dim = 27`) that the Levi-Civita singlet projector $P_{(1^3)} = \frac{1}{6}|\varepsilon\rangle\langle\varepsilon|$ satisfies $P_{(1^3)}^2 = P_{(1^3)}$, $\mathrm{Tr}(P_{(1^3)}) = 1$, traceless $\mathfrak{su}(3)_c$ annihilation $(T^a \otimes I \otimes I + I \otimes T^a \otimes I + I \otimes I \otimes T^a)|\varepsilon\rangle = 0$, and $(g \otimes g \otimes g)|\varepsilon\rangle = (\det g)|\varepsilon\rangle = |\varepsilon\rangle$ for $\det g = 1$, together with balanced-framing parity cancellation $\mathrm{sgn}(\pi(\beta)) \cdot (-1)^{w(\beta)} = +1$ for every 3-strand braid word $\beta \in B_3$.

### A2. $3 \times 3$ Hermitian / Bar-Symmetric Quark Mass Matrices with $J_{\mathrm{CP}} \sim 2.5 \times 10^{-5}$ (`\arg\det(M_u M_d) = 0`)

1. **Zero-Fit Substrate Braiding Benchmark `(M_u^(sub), M_d^(sub))` at `80 dps`:**
   - Define $h_0 = q_0 - q_0^{-1}$ and `[2]_{q_0} = q_0 + q_0^{-1}`, `[3]_{q_0} = q_0^2 + 1 + q_0^{-2}`.
   - Set positive Yukawa hierarchies $D_u = \mathrm{diag}(h_0^6, h_0^3, 1)$ and $D_d = \mathrm{diag}(h_0^5, h_0^3/[3]_{q_0}, h_0)$, and build $V_{\mathrm{sub}}$ in standard Chau–Keung form from the uncalibrated zero-parameter substrate test angles:
     $$s_{12} = h_0, \qquad s_{23} = h_0^2, \qquad s_{13} = \frac{h_0^3}{[2]_{q_0}}, \qquad \delta = \frac{\pi}{3}$$
     (regular ideal-simplex dihedral angle of $4_1$), rotated into a general complex basis by a non-diagonal unitary $U_0$ so that **both** $M_u^{(\mathrm{sub})} = U_0^\dagger D_u U_0$ and $M_d^{(\mathrm{sub})} = U_0^\dagger V_{\mathrm{sub}} D_d V_{\mathrm{sub}}^\dagger U_0$ carry dense non-zero imaginary off-diagonal entries.
   - **Pre-registered checks:**
     * Hermiticity residual $\|M_q - M_q^\dagger\|_\infty < 10^{-78}$ for $q \in \{u, d\}$;
     * Determinant reality $|\mathrm{Im}\det(M_u^{(\mathrm{sub})} M_d^{(\mathrm{sub})})| < 10^{-78}$ and $\mathrm{Re}\det(M_u^{(\mathrm{sub})} M_d^{(\mathrm{sub})}) > 0 \implies \bar{\theta}_{\mathrm{tree}} = \arg\det(M_u^{(\mathrm{sub})} M_d^{(\mathrm{sub})}) = 0$ to `< 10^{-78}`;
     * Non-zero CKM Jarlskog invariant $J_{\mathrm{CP}}(V_{\mathrm{sub}}) = \mathrm{Im}(V_{01} V_{12} V_{02}^* V_{11}^*) \in [2.0 \times 10^{-5}, 3.5 \times 10^{-5}]$ and exact match between $\mathrm{Im}\,\mathrm{Tr}([M_u^2, M_d^2]^3)$ and $6\,\Delta m_u^2\,\Delta m_d^2\,J_{\mathrm{CP}}$ to relative error `< 10^{-75}`.
2. **1-Loop Chiral Dressing Exact Determinant Reality & 3-Loop Ellis–Gaillard Radiative Bound:**
   - Verify that for left-handed 1-loop $W^\pm$ dressing $M_u^{(1\text{-loop})} = (I_3 + \Sigma_L^{(1)}) M_u$ with Hermitian $\Sigma_L^{(1)} = \epsilon_W V M_d^2 V^\dagger$, even though $[ \Sigma_L^{(1)}, M_u ] \neq 0$ makes $M_u^{(1\text{-loop})}$ **non-Hermitian**, $|\mathrm{Im}\det(M_u^{(1\text{-loop})} M_d)| < 10^{-78}$ holds identically.
   - Evaluate the finite 3-loop Ellis–Gaillard electroweak + QCD estimate:
     $$\delta\bar{\theta}_{\mathrm{EW}}^{(3\text{-loop})} = \frac{\alpha_s(M_Z)}{\pi}\left(\frac{\alpha_{\mathrm{EM}}}{4\pi\sin^2\theta_W}\right)^2 \frac{m_c^2 m_s^2}{M_W^4}\,J_{\mathrm{CP}}\,\ln\!\left(\frac{M_W^2}{m_c^2}\right)$$
     and the conservative dimensional upper envelope $(\alpha_{\mathrm{EM}}/\pi)^2 G_F^2 m_c^2 m_s^2 J_{\mathrm{CP}}$, comparing both against $|\bar{\theta}_{\mathrm{QCD}}|_{\mathrm{PDG}} < 10^{-10}$ and $|d_n|_{\mathrm{PDG}} < 1.8 \times 10^{-26}\;e\cdot\mathrm{cm}$ (via $|d_n| \approx 2.4 \times 10^{-16}|\bar{\theta}|\;e\cdot\mathrm{cm}$), while explicitly recording UV counterterm finiteness (`HigherLoopStrongCPFiniteHypothesis`) as open.

---

## 3. Pre-Registered Tests — Arm B: Zero-Parameter Wilson String Tension Candidates $\sqrt{\sigma}$

From the rank-3 colour Markov trace step at $q_0 = q_{\mathrm{at}}(80)$:
$$z_3(q_0) := \frac{q_0^3}{[3]_{q_0}} = \frac{q_0^3}{q_0^2 + 1 + q_0^{-2}}, \qquad z_3^{\mathrm{sym}}(q_0) := \frac{1}{[3]_{q_0}} = \sqrt{z_3(q_0) z_3(q_0^{-1})}, \qquad z_3^{(-)}(q_0) := \frac{q_0^{-3}}{[3]_{q_0}},$$
with dimensionless area-law tensions $\hat{\sigma}_+ = -\ln z_3(q_0)$, $\hat{\sigma}_{\mathrm{sym}} = \ln [3]_{q_0}$, and $\hat{\sigma}_- = -\ln z_3^{(-)}(q_0)$, we pre-register **7 zero-parameter fundamental string-tension candidates** $\sqrt{\sigma} = a_{\mathrm{cal}}^{-1}\sqrt{\hat{\sigma}}$ across pion-Compton (`CAL-3`) and self-consistent proton-size (`CAL-1` + proton $q_0$) lattice spacings $a_{\mathrm{cal}}$, plus an isolated CODATA $r_p$ comparison diagnostic `S7_diag`:

| Candidate ID | Dimensionless step $\hat{\sigma}$ | Lattice spacing $a_{\mathrm{cal}}$ ($\hbar = c = 1$) | Formula for $\sqrt{\sigma_{\mathbf{3}}}$ | Physical spacing reading |
|---|---|---|---|---|
| `S1_pi_bare` | $-\ln z_3(q_0)$ | $\lambda_{\pi^\pm} = 1 / m_{\pi^\pm}$ | $m_{\pi^\pm}\sqrt{-\ln z_3(q_0)}$ | Full charged-pion Compton step (`CAL-3`) |
| `S2_pi_nc3` | $-\ln z_3(q_0)$ | $\lambda_{\pi^\pm} / 3 = 1 / (3 m_{\pi^\pm})$ | $3 m_{\pi^\pm}\sqrt{-\ln z_3(q_0)}$ | $N_c = 3$ colour-subcell of $\lambda_{\pi^\pm}$ |
| `S3_pi_nc3_sym` | $\ln [3]_{q_0}$ | $\lambda_{\pi^\pm} / 3 = 1 / (3 m_{\pi^\pm})$ | $3 m_{\pi^\pm}\sqrt{\ln [3]_{q_0}}$ | Bar-symmetric $[3]_{q_0}^{-1}$ step on $\lambda_{\pi^\pm}/3$ |
| `S4_mp_compton` | $-\ln z_3(q_0)$ | $\lambda_p = 1 / m_p(q_0)$ | $m_p(q_0)\sqrt{-\ln z_3(q_0)}$ | Bare proton Compton step |
| `S5a_rp_full` | $-\ln z_3(q_0)$ | $r_{p,\mathrm{QOU}} = 4 / m_p(q_0)$ | $\frac{1}{4} m_p(q_0)\sqrt{-\ln z_3(q_0)}$ | Full QOU proton charge-radius step ($4\lambda_p$) |
| `S5b_rp_half` | $-\ln z_3(q_0)$ | $r_{p,\mathrm{QOU}} / 2 = 2 / m_p(q_0)$ | $\frac{1}{2} m_p(q_0)\sqrt{-\ln z_3(q_0)}$ | Half proton radius / Y-junction arm ($2\lambda_p$) |
| `S6_rp_half_sym` | $\ln [3]_{q_0}$ | $r_{p,\mathrm{QOU}} / 2 = 2 / m_p(q_0)$ | $\frac{1}{2} m_p(q_0)\sqrt{\ln [3]_{q_0}}$ | Bar-symmetric $[3]_{q_0}^{-1}$ step on $r_{p,\mathrm{QOU}}/2$ |
| `S7_diag_codata_rp_half` | $-\ln z_3(q_0)$ | $r_{p,\mathrm{CODATA}} / 2$ | $\frac{2\hbar c}{r_{p,\mathrm{CODATA}}}\sqrt{-\ln z_3(q_0)}$ | Diagnostic only (measured CODATA-2022 $r_p$) |

**Pre-registered evaluation & classification criteria (no post-hoc selection):**
- Compare every candidate against the lattice/Regge fundamental string-tension band $\sqrt{\sigma_{\mathrm{lat}}} \in [420, 440]\;\mathrm{MeV}$ (midpoint $430\;\mathrm{MeV}$):
  * `IN_BAND`: $420\;\mathrm{MeV} \le \sqrt{\sigma} \le 440\;\mathrm{MeV}$;
  * `NEAR_15PCT`: outside $[420, 440]\;\mathrm{MeV}$ with $|\sqrt{\sigma} - 430| / 430 \le 0.15$;
  * `MISS`: $|\sqrt{\sigma} - 430| / 430 > 0.15$.
- Also compute for each candidate: the Casimir-scaled adjoint string tension $\sqrt{\sigma_{\mathbf{8}}} = \frac{3}{2}\sqrt{\sigma_{\mathbf{3}}}$ ($C_2(\mathbf{8})/C_2(\mathbf{3}) = 9/4$), the implied Regge slope $\alpha'_{\mathrm{cand}} = 1 / (2\pi\sigma_{\mathbf{3}})$ in $\mathrm{GeV}^{-2}$ vs $\alpha'_{\mathrm{Regge}} \approx 0.88\;\mathrm{GeV}^{-2}$, the multiplicative Creutz-ratio identity residual (`< 10^{-78}`), and the logarithmic $q$-slope $d\ln\sqrt{\sigma}/d\ln q$ at $q_0$.
- Every candidate (`IN_BAND`, `NEAR_15PCT`, and `MISS`) is reported verbatim in the witness with `selected = "none"` until a first-principles categorical derivation fixes $a_{\mathrm{cal}}$ uniquely.
