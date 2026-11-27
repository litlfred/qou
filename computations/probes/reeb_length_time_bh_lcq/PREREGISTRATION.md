# Pre-Registration: Reeb Length/Time Reconciliation ($d_{\mathrm{Reeb}}$, KMS Time, $c_q$, $\mathfrak{E} = \mathfrak{m} c_q^2$, $L_{\mathrm{cal}}$) & Light-Cone (`LCQ`) Bekenstein–Hawking Channel Counting (2026-11-23)

Bean `qou-slfm` (with upstream threads `qou-mumr`, `qou-5uj7`, `qou-jfx8`, `qou-apma`, and `#9207` `UnifiedClockScaleLayers` / `FiniteRieffelQuantumMetric`). Written and committed **before** running the 80-dps numerical evaluation of candidate horizon entropy rates and elementary area quanta.

## 1. Calibration, Precision & Anti-Fit Discipline (STRICT)

- **Working precision:** `mpmath.workdps(80)` throughout (`OUT_DPS = 70` serialized into the witness), zero `float64` imports, literals, or casts (`parse_float=str` on any JSON reads).
- **Substrate pin:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`).
- **Zero empirical inputs in `.lean` proofs (`§7c`):** `QOU/GravitySpacetime/ReebLengthTimeAndLightConeEntropy.lean` is authored strictly over generic `[CommRing R]` / `[Field K]` / `[LinearOrder K] [IsStrictOrderedRing K]` with **zero** `ℝ` and **zero** empirical constants.
- **Boundary unit conversions (`Layer III`):** Laboratory calibration scales $L_{\mathrm{cal}}$ (CAL-1 electron Compton scale $\lambda_{C,e} = \hbar_{\mathrm{SI}} / (m_e c_{\mathrm{SI}})$ vs SI gravitational Planck chart $\ell_{\mathrm{Planck}}^{\mathrm{SI}} = \sqrt{\hbar_{\mathrm{SI}} G_{\mathrm{Newton}} / c_{\mathrm{SI}}^3}$) enter **only** as boundary conversion functors in Battery A4; **zero** parameters are tuned or fitted to force $S_{\mathrm{BH}} = A / (4 \ell_P^2)$.

## 2. Pre-Registered Batteries & Falsifiable Hypotheses

### Battery A — Reeb Length, Computation Time, Causal Cone $c_q(q_0)$, $\mathfrak{E} = \mathfrak{m} c_q^2$, and $L_{\mathrm{cal}}$
1. **A1 (Share vs Total & Step-to-Time Dictionary):** Verify at 80 dps at $q_0$:
   - Per-step Reeb share $\hbar_{q_0} = 1 - q_0^{-1} = (q_0 - 1)/q_0$,
   - Full-circuit Reeb/Planck tick $t_P(q_0) = \hbar_{q_0}^{-1} = q_0 / (q_0 - 1)$,
   - Unit-normalised circuit length $\ell_P(q_0) = \hbar_{q_0} t_P(q_0) = 1$,
   - Horizontal $D_\nabla$ transport weight $q_0^{-1}$ with convex split $q_0^{-1} + \hbar_{q_0} = 1$,
   - Causal Lieb–Robinson cone slope $c_q(q_0) = q_0^{-1} / \hbar_{q_0} = 1 / (q_0 - 1) = t_P(q_0) - 1$,
   - $N$-step causal cone identity $\Delta x_{\mathrm{cone}}(N, q_0) = N q_0^{-1} = c_q(q_0) \cdot \Delta t_{\mathrm{comp}}(N, q_0)$ where $\Delta t_{\mathrm{comp}}(N, q_0) = N \hbar_{q_0}$.
2. **A2 (KMS Traciality Obstruction vs Woronowicz–Nakayama Modular Clock):**
   - Confirm that tracial Markov states ($\mathrm{tr}_M(xy) = \mathrm{tr}_M(yx)$) force $\beta = 0$ on any grading character, whereas Woronowicz's Haar/Nakayama modular operator $\nu_{q_0}(\alpha) = q_0^2 \alpha$ on $O_{q_0}(SU(2))$ generates a genuine non-tracial discrete KMS clock with modular step ratio $q_0^2$ and effective modular inverse temperature $\beta_{\mathrm{mod}}(q_0) = 2 \ln q_0$.
3. **A3 (Categorical Energy $\mathfrak{E} = \mathfrak{m} c_q^2$ & Internal Gravitational Identities):**
   - Evaluate $c_q(q_0)^2 = 1 / (q_0 - 1)^2$, operational entropy $\eta_q(q_0) = (2 q_0 - 1)/q_0^3$, jet-cell entropy $S_{\mathrm{cell}}(q_0) = (q_0 - 1)^2 / q_0^3$, and gravitational constant $G_q(q_0) = c_q(q_0)^3 \hbar_{q_0} / S_{\mathrm{cell}}(q_0) = q_0^2 / (q_0 - 1)^4$.
   - Contrast the two substrate Planck-area normalisations:
     $$G_q(q_0)\left(\frac{\hbar_{q_0}}{c_q(q_0)}\right)^2 = 1 \quad\text{vs}\quad \frac{\hbar_{q_0} G_q(q_0)}{c_q(q_0)^3} = \frac{\hbar_{q_0}^2}{S_{\mathrm{cell}}(q_0)} = q_0,$$
     originating from $\hbar_{q_0} c_q(q_0) = q_0^{-1} \neq 1$ in native $q$-connection units.
4. **A4 (Layer-III Boundary Scale Invariance under $L_{\mathrm{cal}}$):**
   - Verify to 80 dps that rescaling substrate lengths by any laboratory unit conversion factor $L_{\mathrm{cal}} > 0$ (tested on $\lambda_{C,e}$ and $\ell_{\mathrm{Planck}}^{\mathrm{SI}}$) leaves every dimensionless ratio, $c_q(q_0)$, relative Rieffel–Kantorovich distance, and $A_{\mathrm{lab}} / (4 \ell_{P,\mathrm{lab}}^2)$ invariant to $< 10^{-76}$.

### Battery B — Exact Horizon Crossing Channel Entropy Rates at $q_0$
On a discrete causal horizon surface $\Sigma$ pierced by $N_\Sigma$ minimal punctures:
1. **B1 (Catalan / $TL_{N_\Sigma}(q_0)$ Singlet Vector-Space Count):**
   - Odd $N_\Sigma = 2m + 1$: $\dim \mathcal{H}_{\mathrm{singlet}}(2m+1) = 0$.
   - Even $N_\Sigma = 2m$: $\dim \mathcal{H}_{\mathrm{singlet}}(2m) = C_m = \frac{1}{m+1}\binom{2m}{m}$, with asymptotic entropy per puncture $s_{\mathrm{Cat}} = \ln 2$ and Kaul–Majumdar logarithmic subleading expansion:
     $$\ln C_{N_\Sigma/2} = N_\Sigma \ln 2 - \frac{3}{2}\ln N_\Sigma + \frac{1}{2}\ln\!\left(\frac{8}{\pi}\right) - \frac{9}{4 N_\Sigma} + O(N_\Sigma^{-2}),$$
     evaluated and checked across $N_\Sigma \in \{20, 100, 500, 2000, 10000\}$ alongside Meissner's $U(1)$-only $\ln \binom{2m}{m} = N_\Sigma \ln 2 - \frac{1}{2}\ln N_\Sigma + \frac{1}{2}\ln(2/\pi) + O(N_\Sigma^{-1})$.
2. **B2 (Jones–Wenzl / Temperley–Lieb Quantum Dimension & Woronowicz Haar Qubit Entropy):**
   - Spin-$1/2$ quantum-dimension / half-log Jones index rate: $s_{\mathrm{TL}}(q_0) = \ln [2]_{q_0} = \ln(q_0 + q_0^{-1})$.
   - Woronowicz Haar single-puncture modular state $\rho_1 = \mathrm{diag}(q_0^2/(1+q_0^2),\, 1/(1+q_0^2))$ von Neumann entropy:
     $$s_{\mathrm{Haar}}(q_0) = \ln [2]_{q_0} - \frac{q_0 - q_0^{-1}}{q_0 + q_0^{-1}}\ln q_0.$$
   - Spin-$1$ / 3-strand rates: $\ln [3]_{q_0} = \ln(q_0^2 + 1 + q_0^{-2})$, per-strand $\frac{1}{3}\ln [3]_{q_0}$, and $\frac{1}{3}\ln(\dim TL_3) = \frac{1}{3}\ln 5$.
3. **B3 (Full $SU_{q_0}(2)$ Spin-Tower Partition-Function Pole $Z_1(s_\star) = 1$):**
   - Solve $\sum_{j \in \frac{1}{2}\mathbb{Z}_{>0}} [2j+1]_{q_0} \exp(-s_\star [j]_{q_0}[j+1]_{q_0}) = 1$ at 80 dps by Newton/bisection to obtain $s_\star(q_0)$ and $\gamma_\star(q_0) = s_\star(q_0)/(2\pi)$, compared against classical $q = 1$ Domagala–Lewandowski $\gamma_{\mathrm{DL}}(1)$.

### Battery C — Zero-Parameter Candidate Puncture Area Quanta $a_0$ vs Required Lock $a_0^\star = 4 s_{\mathrm{punct}}$
For $S = (s_{\mathrm{punct}} / a_0) (A / \ell_P^2)$, exact Bekenstein–Hawking coefficient $1/4$ holds **iff** $a_0 = 4 s_{\mathrm{punct}}$. We pre-register and evaluate side-by-side (with **no** post-hoc selection) six zero-parameter candidate area ratios $a_0$:
- **Q1 (Unit Reeb-circuit cell):** $a_0 = 1$.
- **Q2a / Q2b (Elementary spatial step & jet-cell ratios):** $a_0 = q_0^{-2}$ and $a_0 = \hbar_{q_0}^2 / S_{\mathrm{cell}}(q_0) = q_0$ (plus jet-cell entropy density $S_{\mathrm{cell}}(q_0) / \hbar_{q_0}^2 = q_0^{-1}$).
- **Q3 ($D_\nabla$ Reeb-share Ashtekar candidate $\gamma = \hbar_{q_0}$):** $a_0 = 8\pi \hbar_{q_0} \sqrt{[1/2]_{q_0}[3/2]_{q_0}}$ (and direct comparison $\hbar_{q_0}$ vs $\gamma_\star(q_0)$).
- **Q4 ($D_\nabla$ contact anisotropy candidate $\gamma = q_0 - 1 = c_{q_0}^{-1}$):** $a_0 = 8\pi (q_0 - 1) \sqrt{[1/2]_{q_0}[3/2]_{q_0}}$.
- **Q5 (Sasakian / CR geometric solid-angle quanta):** $a_0 \in \{\pi, 2\pi, 4\pi\}$.
- **Q6 (LCQ Null-Sheet Clausius–Raychaudhuri Focusing Lock):** Test the exact cancellation $\frac{\delta S}{\delta A} = \frac{2\pi / \hbar}{8\pi G / c^3} = \frac{1}{4 \ell_{P,\mathrm{grav}}^2}$ and record honestly whether QOU's CR structure currently derives the two required Lorentzian null-focusing premises or leaves $a_0 = 4 s_{\mathrm{punct}}$ as a Rule-13a open geometric conjecture (`LCQHorizonPunctureAreaConjecture`).
