# Pre-Registration: $S_3$-Equivariant / $\mathbb{Z}_3$-Circulant Mass Matrix & Algebraic Koide Trace-to-Norm Test on Bring's 3-Generation Subspace `projGen3` (Open Gap 2 Backup, Option 2B / `qou-j96h`)

- **Workstream / Gap**: Closing Open Gap 2 Backup (Option 2B, Bean `qou-j96h`)
- **Branch**: `claude/gap2b-mtau-s3-circulant-koide-test-20261123` (branched from `origin/main` @ `e330ab6aa048abefe34a93474f667f3284483d71`)
- **Date**: 2026-11-23 (authored, committed, and pushed **strictly before** computing any numerical mass-ratio or Koide-ratio evaluations)
- **Companion Lean 4 Module**: `folio/quantum-observable-universe/lean/QOU/StandardModel/S3CirculantKoideTraceIdentity.lean`
- **Companion 80-dps Probe**: `computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b_mtau_s3_circulant_koide_probe.py`
- **Companion Witness JSON**: `computations/probes/gap2b_mtau_s3_circulant_koide_test/gap2b-mtau-s3-circulant-koide-probe.witness.json`
- **Companion Results Report**: `computations/probes/gap2b_mtau_s3_circulant_koide_test/RESULTS.md`
- **Precision & Anchor**: `mpmath.workdps(80)` (`OUT_DIGITS = 50`, zero `float64`), `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`)

---

## 1. Anti-Fit, Precision, and Epistemic Guardrails (`STRICT`)

1. **`NO FITTING, EXCEPT CAL-1/2/3`**:
   - Every substrate evaluation uses the proton-pinned parameter $q_0 = \mathrm{q\_at}(80)$ and $\hbar_{q_0} = 1 - q_0^{-1}$, derived solely from `CAL-1` ($m_e$), the figure-eight motivic period $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$, and CODATA-2022 $m_p / m_e$ (`qou_substrate.constants.q_at(80)`). The muon-anchored parameter `q_muon_at(80)` is recorded solely as a read-only cross-check.
   - Experimental charged-lepton mass ratios enter **strictly** as downstream comparison benchmarks (except in Benchmark R1, which explicitly tests Koide's classic `CAL-1 + CAL-2` quadratic resolvent prediction for $m_\tau / m_e$):
     - CODATA-2022 muon-to-electron mass ratio (`qou_substrate.codata.codata("muon-electron mass ratio")`): $m_\mu / m_e = 206.7682827 \pm 4.6 \times 10^{-6}$,
     - Belle-II / PDG-2024 / CODATA-2022 high-precision tau-to-electron mass ratio: $m_\tau / m_e = 3477.228 \pm 0.023$, alongside `qou_substrate.codata.codata("tau-electron mass ratio")` ($3477.23 \pm 0.23$).
   - **Zero** continuous or discrete angles, radii, or weights are tuned, swept, or post-hoc adjusted against $m_\mu / m_e$, $m_\tau / m_e$, or $Q_{\mathrm{Koide}}^{\mathrm{exp}}$.

2. **Zero `float64` in Probes**:
   - Every algebraic, trigonometric, root-finding, and uncertainty-propagation step executes inside `mpmath.workdps(80)` using `mpmath.mpf` / `mpmath.mpc` parsed from exact integer/rational expressions or NIST ASCII strings (`allascii.txt`). No `float(...)` intermediate enters any computed observable or residual.

3. **Zero Empirical Literals in Lean 4 (`AGENTS.md §7c`) & Rule 13a**:
   - `S3CirculantKoideTraceIdentity.lean` is formalized strictly over generic `[CommRing R]`, `[Field F]`, and `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` (`0 sorry`, `0` custom `axiom`s, zero `ℝ`, zero empirical literals).
   - If no un-tuned $H_3(q_0)$ or Bring `projGen3` operator simultaneously derives exact singlet-doublet equipartition ($a^2 = 2|b|^2 \iff Q_{\mathrm{Koide}} = 2/3$) **and** a substrate phase $\theta(q_0)$ matching both $m_\mu / m_e$ and $m_\tau / m_e$, any unproved Koide operator + phase closure is isolated as a zero-instance `class` under **Rule 13a**.

---

## 2. Live-Verified Literature References (Crossref / `doi.org`)

All DOIs below were live-verified against Crossref (`api.crossref.org`) and `doi.org` (HTTP 200) prior to pre-registration:

- **`[koide1983plb]`**: Y. Koide, *"A fermion-boson composite model of quarks and leptons"*, *Phys. Lett. B* **120** (1983) 161–165, DOI: [`10.1016/0370-2693(83)90644-5`](https://doi.org/10.1016/0370-2693(83)90644-5).
- **`[koide1983prd]`**: Y. Koide, *"New view of quark and lepton mass hierarchy"*, *Phys. Rev. D* **28** (1983) 252–254, DOI: [`10.1103/PhysRevD.28.252`](https://doi.org/10.1103/PhysRevD.28.252).
- **`[koide1990mpla]`**: Y. Koide, *"Charged lepton mass sum rule from $U(3)$-family Higgs potential model"*, *Mod. Phys. Lett. A* **5** (1990) 2319–2323, DOI: [`10.1142/S0217732390002663`](https://doi.org/10.1142/S0217732390002663).
- **`[foot1994]`**: R. Foot, *"A note on Koide's lepton mass relation"* (1994), `arXiv:hep-ph/9402242`, DOI: [`10.48550/arXiv.hep-ph/9402242`](https://doi.org/10.48550/arXiv.hep-ph/9402242).
- **`[harrison2002]`**: P. F. Harrison, D. H. Perkins, W. G. Scott, *"Tri-bimaximal mixing and the neutrino oscillation data"*, *Phys. Lett. B* **530** (2002) 167–173, DOI: [`10.1016/S0370-2693(02)01336-9`](https://doi.org/10.1016/S0370-2693(02)01336-9).
- **`[rodejohann2011]`**: W. Rodejohann, H. Zhang, *"Extension of an empirical charged lepton mass relation to the neutrino sector"*, *Phys. Lett. B* **698** (2011) 152–156, DOI: [`10.1016/j.physletb.2011.03.007`](https://doi.org/10.1016/j.physletb.2011.03.007).
- **`[mohr2025codata2022]`**: P. J. Mohr, D. B. Newell, B. N. Taylor, E. Tiesinga, *"CODATA recommended values of the fundamental physical constants: 2022"*, *Rev. Mod. Phys.* **97** (2025) 025002, DOI: [`10.1103/RevModPhys.97.025002`](https://doi.org/10.1103/RevModPhys.97.025002).
- **`[navas2024pdg]`**: S. Navas *et al.* (Particle Data Group), *"Review of Particle Physics"*, *Phys. Rev. D* **110** (2024) 030001, DOI: [`10.1103/PhysRevD.110.030001`](https://doi.org/10.1103/PhysRevD.110.030001).

---

## 3. Pre-Registered Lean 4 Formalization Targets (`S3CirculantKoideTraceIdentity.lean`)

1. **$3\times 3$ Circulant Square-Root Mass Algebra & Hermitian `QuadI R` Norm Identities (`[CommRing R]`)**:
   - Cyclic shift matrix $C \in \mathrm{Mat}_{3\times 3}(R)$ with $C^3 = I_3$, $C^\top = C^2$, and $\mathrm{Tr}(C) = \mathrm{Tr}(C^2) = 0$.
   - Circulant operator $S(a, b, c) = a I_3 + b C + c C^2$: closure under multiplication, commutativity $S(a_1, b_1, c_1) S(a_2, b_2, c_2) = S(a_2, b_2, c_2) S(a_1, b_1, c_1)$, exact trace $\mathrm{Tr}(S(a, b, c)) = 3a$, square trace $\mathrm{Tr}(S(a, b, c)^2) = 3(a^2 + 2bc)$, real Frobenius norm $\mathrm{Tr}(S^\top S) = 3(a^2 + b^2 + c^2)$, and Hermitian circulant over the generic Gaussian ring `QuadI R` ($a \in R$, $c = \bar{b}$, $|b|^2 = b_{\mathrm{re}}^2 + b_{\mathrm{im}}^2$): $S^\dagger = S$ and $\mathrm{Tr}(S^\dagger S) = \mathrm{Tr}(S^2) = 3(a^2 + 2|b|^2)$.

2. **Division-Free Koide Trace-to-Norm Identity & Singlet–Doublet Equipartition (`[CommRing R]` / `[Field F]`)**:
   - Exact polynomial identity over `[CommRing R]`:
     $$3\,\mathrm{Tr}(S(a, b, c)^2) - 2\,(\mathrm{Tr}\,S(a, b, c))^2 = 9(2bc - a^2).$$
   - Over `[Field F]` (`(3 : F) ≠ 0`, `a ≠ 0`), for $b c = r^2$:
     $$Q_{\mathrm{Koide}}(a, r) := \frac{3(a^2 + 2r^2)}{(3a)^2} = \frac{1 + 2 r^2 / a^2}{3}, \qquad Q_{\mathrm{Koide}}(a, r) = \frac{2}{3} \iff 2 r^2 = a^2.$$
   - Orthogonal root-mass vector decomposition on the 3D generation space $F^3 = V_{\mathrm{dem},1} \oplus V_{\mathrm{doublet},2}$ (matching Bring's $S_4 \downarrow S_3$ split `projGen3 = projDem1 + projDoublet2`): for any $\lambda = (\lambda_0, \lambda_1, \lambda_2) \in F^3$ with $a = \frac{1}{3}(\lambda_0 + \lambda_1 + \lambda_2)$, $\lambda_{\mathrm{dem}} = (a, a, a)$, and $\lambda_{\mathrm{doublet}} = (\lambda_0 - a, \lambda_1 - a, \lambda_2 - a)$,
     $$\|\lambda_{\mathrm{dem}}\|^2 = 3a^2, \quad \|\lambda_{\mathrm{doublet}}\|^2 = \sum_{k=0}^2 \lambda_k^2 - 3a^2, \quad \frac{\sum_{k=0}^2 \lambda_k^2}{\left(\sum_{k=0}^2 \lambda_k\right)^2} = \frac{2}{3} \iff \|\lambda_{\mathrm{doublet}}\|^2 = \|\lambda_{\mathrm{dem}}\|^2.$$

3. **Unbroken $S_3$-Equivariance Degeneracy Obstruction (`[CommRing R]`)**:
   - Full $S_3$ permutation equivariance on $R^3$ forces $M = a I_3 + b(C + C^2)$ ($c = b$), which satisfies $(M - (a + 2b)I_3)(M - (a - b)I_3)^2 = 0$ and leaves a 2D eigenspace at eigenvalue $a - b$ ($\lambda_1 = \lambda_2$). Thus unbroken $S_3$-equivariance cannot split all three charged-lepton masses; chiral symmetry breaking $S_3 \downarrow A_3 \cong \mathbb{Z}_3$ ($b \neq c$) is algebraically required.

4. **Exact Koide Quadratic Resolvent Identity (`[CommRing R]` / `[Field F]`)**:
   - Over every `[CommRing R]`:
     $$3(u^2 + v^2 + x^2) - 2(u + v + x)^2 = x^2 - 4(u + v)x + (u^2 + v^2 - 4uv) = \bigl(x - 2(u + v)\bigr)^2 - 3(u^2 + 4uv + v^2),$$
     with quadratic discriminant $\Delta(u, v) = (-4(u + v))^2 - 4(u^2 + v^2 - 4uv) = 12(u^2 + 4uv + v^2)$.
   - Over `[Field F]` (`(3 : F) ≠ 0`, `u + v + x ≠ 0`), $\frac{u^2 + v^2 + x^2}{(u + v + x)^2} = \frac{2}{3} \iff x^2 - 4(u + v)x + (u^2 + v^2 - 4uv) = 0$.

5. **Structural $H_3(q)$ / $TL_3(q)$ Operator Identities & Finite-$q$ Departure (`[Field K]` / Ordered `[Field K]`)**:
   - Ruled chiral photon vertex $V(q) = \rho_{M_{+1}}(\sigma_0 \sigma_1^{-1})$ (`stepPlus q (q - q⁻¹)`): reduces at $q = 1$ directly to the cyclic shift $C$, while for $q \neq 1$, $\mathrm{Tr}(V(q)) = -(q - q^{-1})^2 \neq 0$, and on $V_{(2,1)}$ its characteristic polynomial is $\mu^2 + (1 + (q - q^{-1})^2)\mu + 1$ ($\det = 1$).
   - Temperley–Lieb / Convention-D Ocneanu Wedderburn weights $w_{\mathrm{sing}}(q) = y_{(3)}(q) = 1 - 2/(q + q^{-1})^2$ and $w_{\mathrm{doub}}(q) = 2 y_{(2,1)}(q) = 2/(q + q^{-1})^2$:
     - At $q = 1$, $w_{\mathrm{sing}}(1) = 1/2 = w_{\mathrm{doub}}(1)$, yielding **exact classical singlet–doublet equipartition** $Q_{\mathrm{TL3}}(1) = 2/3$.
     - Over any ordered field, for every $q \neq 0$ with $q \neq \pm 1$, $(q - q^{-1})^2 > 0$ forces $w_{\mathrm{doub}}(q) < w_{\mathrm{sing}}(q)$ and $Q_{\mathrm{TL3}}(q) = \frac{(q + q^{-1})^2}{3(q^2 + q^{-2})} < \frac{2}{3}$ strictly.

---

## 4. Pre-Registered 80-dps Numerical Test Suite (`gap2b_mtau_s3_circulant_koide_probe.py`)

### 4.1 Part A — Quadratic Resolvent Tests for $m_\tau / m_e$ under Exact $Q_{\mathrm{Koide}} = 2/3$

Solving $x_+ = 2(1 + v) + \sqrt{3(1 + 4v + v^2)}$ with predicted tau-to-electron ratio $(m_\tau / m_e)_{\mathrm{pred}} = x_+^2$:
1. **`R1_codata_cal1_cal2`**: $v = \sqrt{(m_\mu / m_e)_{\mathrm{CODATA}}}$ (classic Koide `CAL-1 + CAL-2` benchmark; also extracts the exact empirical Brannen–Koide phase $\theta_{\mathrm{exp}} \in (0, \pi/12)$ as a read-only reference).
2. **`R2a_qou_bare_vol41`**: $v = \sqrt{\mathrm{Vol}(4_1) / \hbar_{q_0}^2}$ at $q_0 = \mathrm{q\_at}(80)$ (zero-`CAL-2` proton-anchored bare hyperbolic muon carrier + exact Koide $Q = 2/3$).
3. **`R2b_qou_inhomogeneous_9213`**: $v = \sqrt{\tau_{4_1}(q_0) / \tau_e(q_0) + \mathrm{Vol}(4_1) / \hbar_{q_0}^2}$ at $q_0 = \mathrm{q\_at}(80)$ (`#9213` electron-normalized contact + saddle muon carrier + exact Koide $Q = 2/3$).

### 4.2 Part B — Un-Tuned $H_3(q_0)$ & Bring `projGen3` Operator Equipartition Tests ($Q \stackrel{?}{=} 2/3$)

At $q_0 = \mathrm{q\_at}(80)$, evaluate the singlet-to-doublet energy ratio $\rho_{2/1} = 2 r^2 / a^2$ and resulting $Q = (1 + \rho_{2/1})/3$:
1. **`Op_B1_identity`**: $S = I_3$ ($\rho_{2/1} = 0$, $Q = 1/3$).
2. **`Op_B2_democratic_D3`**: $S = \frac{1}{3} D_3 = \frac{1}{3}(I_3 + C + C^2)$ ($\rho_{2/1} = 2$, $Q = 1$, two zero eigenvalues).
3. **`Op_B3_isotropic_Z3_plancherel` / `projGen3_trace_dof`**: equal weight per $\mathbb{Z}_3$ element ($|a|^2 = |b|^2 = |c|^2$, or $1$ singlet DOF vs $2$ doublet DOFs on `projGen3`: $\rho_{2/1} = 2$, $Q = 1$).
4. **`Op_B4_TL3_convD_wedderburn_norm`**: $3a^2 = y_{(3)}(q_0)$, $6r^2 = 2 y_{(2,1)}(q_0)$ ($\rho_{2/1}(q_0) = \frac{2}{q_0^2 + q_0^{-2}}$, $Q_{\mathrm{TL3}}(q_0) = \frac{(q_0 + q_0^{-1})^2}{3(q_0^2 + q_0^{-2})}$, equal to $2/3$ at $q = 1$ and shifted at $q_0$).
5. **`Op_B5_H3_symmetrizer_qdim`**: regular $H_3(q_0)$ Wedderburn quantum-dimension / Hook weight ratio on $V_{(3)} \oplus V_{(2,1)}$.
6. **`Op_B6_chiral_photon_vertex_Mplus1`**: exact singular values and Hermitian part $\frac{1}{2}(V(q_0) + V(q_0)^\top)$ of `stepPlus q_0 (q_0 - q_0⁻¹)` (`QOU.Photon.vertex` on $M_{+1}$), testing $I_3 + \kappa V_{\mathrm{Herm}}(q_0)$ at un-tuned $\kappa \in \{1, 1/\sqrt{2}\}$.

### 4.3 Part C — Zero-Parameter Phase Tests $\theta_j(q_0)$ under Exact $Q_{\mathrm{Koide}} = 2/3$ ($r = a / \sqrt{2}$)

In the standard positive-ordered Brannen–Koide parameterization ($0 < \theta < \pi/12$, where $\lambda_e = a(1 + \sqrt{2}\cos(\theta + 2\pi/3)) < \lambda_\mu = a(1 + \sqrt{2}\cos(\theta + 4\pi/3)) < \lambda_\tau = a(1 + \sqrt{2}\cos\theta)$):
$$\frac{m_\mu}{m_e}(\theta) = \left(\frac{1 + \sqrt{2}\cos(\theta + 4\pi/3)}{1 + \sqrt{2}\cos(\theta + 2\pi/3)}\right)^2, \qquad \frac{m_\tau}{m_e}(\theta) = \left(\frac{1 + \sqrt{2}\cos\theta}{1 + \sqrt{2}\cos(\theta + 2\pi/3)}\right)^2.$$

Evaluate at 80 dps (`q_0 = q_at(80)`, `h_{q_0} = q_0 - q_0⁻¹`, `\hbar_{q_0} = 1 - q_0⁻¹`, `[3]_{q_0} = q_0^2 + 1 + q_0^{-2}`) the **seven locked zero-parameter candidate phases**:
1. **`theta_1_two_hbar`**: $\theta_1 = 2\hbar_{q_0} = 2(1 - q_0^{-1})$.
2. **`theta_2_two_ln_q0`**: $\theta_2 = 2\ln q_0$.
3. **`theta_3_two_q0_minus_1`**: $\theta_3 = 2(q_0 - 1)$.
4. **`theta_4_hecke_h`**: $\theta_4 = h_{q_0} = q_0 - q_0^{-1}$.
5. **`theta_5_rational_two_ninths`**: $\theta_5 = \frac{2}{9} = \frac{2}{[3]_{q=1}^2}$ (Brannen rational triality / classical Casimir benchmark, independent of $q_0$).
6. **`theta_6_q_triality_casimir`**: $\theta_6 = \frac{2}{[3]_{q_0}^2} = \frac{2}{(q_0^2 + 1 + q_0^{-2})^2}$ ($q_0$-deformed triality Casimir fraction).
7. **`theta_7_chiral_vertex_eigenphase_shift`**: $\theta_7 = \arccos\!\left(-\frac{1 + (q_0 - q_0^{-1})^2}{2}\right) - \frac{2\pi}{3}$ (exact eigenphase shift of `QOU.Photon.vertex` $\sigma_0\sigma_1^{-1}$ on $V_{(2,1)}$).

---

## 5. Pre-Registered Pass / Falsification Gate (`Gate G-2B`)

- **Pass Criterion**: Option 2B closes Open Gap 2 from QOU substrate algebra **if and only if**:
  1. An un-tuned $H_3(q_0)$ or Bring `projGen3` operator in §4.2 derives $Q_{\mathrm{Koide}} = 2/3$ within experimental uncertainty, **and**
  2. One of the $q_0$-derived zero-parameter phases $\{\theta_1, \theta_2, \theta_3, \theta_4, \theta_6, \theta_7\}$ in §4.3 simultaneously reproduces **both** $m_\mu / m_e = 206.7682827(46)$ **and** $m_\tau / m_e = 3477.228(23)$ within $< 1\%$ relative error (with $< 1\sigma$ required for precision closure). Note that $\theta_5 = 2/9$ is an un-derived rational literature benchmark (`[rodejohann2011]` / Brannen) and cannot by itself close Gap 2 without a proved QOU operator derivation of both $a^2 = 2|b|^2$ and $\theta = 2/9$.
- **Falsification / Rule-13a Outcome**: If `Gate G-2B` is not satisfied, the probe records `gate_g2b_passed = false` and `selected_q0_operator = "none"`, reports all 80-dps residuals without post-hoc adjustment, and `S3CirculantKoideTraceIdentity.lean` encapsulates the unresolved finite-$q_0$ Koide operator + phase closure as a zero-instance `class` under **Rule 13a**.
