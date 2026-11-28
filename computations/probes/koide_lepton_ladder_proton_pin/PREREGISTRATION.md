# Pre-Registration: Division-Free $S_3/\mathbb{Z}_3$ Singlet–Doublet Koide Equipartition & 2026-11-28 Least-Crossing Lepton Ladder Invariants at the Proton Pin (`qou-cw8i`)

- **Bean / Epics**: `qou-cw8i` (under Stability Epic `qou-s028` & Compute-Accuracy Epic `qou-myts`)
- **Date**: 2026-11-28 (authored and committed **before** executing the 80-dps proton-pin numerical probe)
- **Companion Lean 4 Modules**:
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/KoideSingletDoubletEquipartition.lean` (`0 sorry`, `0` custom `axiom`s, `100%` `[CommRing R]`, zero `[Field]`, zero `field_simp`, zero transcendental API)
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/BringThreeGenerationsAndTauSatellite.lean` (refactored bridge to `KoideSingletDoubletEquipartitionBridge`)
  - `folio/quantum-observable-universe/lean/QOU/StandardModel/S3CirculantKoideTraceIdentity.lean` (Fourier-mode moment discharge)
- **Companion 80-dps Proton-Pin Probe**:
  - `computations/probes/koide_lepton_ladder_proton_pin/koide_lepton_ladder_proton_pin_probe.py`
  - Manifest registration: `computations/q0_anchor_manifest.json` $\to$ `"physical_proton"`

---

## 1. Anti-Fit & Proton-Pin Discipline (`owner-rulings.md` rows 17–18, 228–230)

1. **Proton Pin Strictly Enforced (`q0Anchor = "proton"`)**:
   - Per the 2026-11-28 owner directive (*"make sure you are working proton pin... no longer muon (on hold, until rederivation)"*), all 80-dps substrate evaluations use **exclusively** the proton pin $q_0 = q_{\mathrm{proton}}$ (`qou_substrate.constants.q_at(80)`).
   - The `CAL-2` muon pin is explicitly **on hold** until first-principles rederivation from the 2026-11-28 lepton words (`owner-rulings.md` row 228) and is not read or mixed anywhere in this computation.
2. **Zero Fitting (`NO FITTING, EXCEPT CAL-1/2/3`)**:
   - Zero continuous or discrete parameters, angles, colours, or weights are fitted or selected against $m_\tau / m_e$, $m_\mu / m_e$, or $Q_{\mathrm{Koide}}^{\mathrm{exp}}$.
   - Per `owner-rulings.md` row 18 (*"The mass reading of the lepton closure $\cup$ axis operator is derived before anything is scored"*), all $N = 2, 3, 4$ ring-trace, closure $\cup$ axis, and $\zeta_N$ Kashaev cut-axis invariants on the 2026-11-28 least-crossing ladder (`e = \sigma_0\sigma_1\sigma_0`, `\mu = \sigma_0^4\sigma_1^{-1}`, `\tau = \sigma_0^2\sigma_1^{-1}\sigma_0\sigma_1^{-1}`) are reported strictly as **structural mathematical invariants** (unscored against CODATA lepton ratios).
   - Experimental benchmarks (`CODATA-2022` $m_\tau / m_e = 3477.23 \pm 0.23$ and `PDG-2024` $m_\tau = 1776.93 \pm 0.09\,\mathrm{MeV} \implies m_\tau / m_e = 3477.3653 \pm 0.1761$) enter **read-only** solely to cross-check the radical-free quartic Koide mass polynomial on the proton-pinned `ACCURACY.md` Table 3.1a `Conditional` row (`+0.923\sigma` CODATA / `+0.437\sigma` PDG-2024).

---

## 2. Pre-Registered Lean 4 Formalization Targets (`KoideSingletDoubletEquipartition.lean`)

Every theorem in `KoideSingletDoubletEquipartition.lean` is proved over a generic `[CommRing R]` (with `[LinearOrder R] [IsStrictOrderedRing R]` only for ordered-ring discriminant positivity):

1. **Division-Free $S_3$ Singlet–Doublet Projectors on $V_{\mathrm{gen}} = R^3$ & Bring's $V_{\mathrm{std}} \subset R^5$**:
   - Scaled projectors $3 P_{\mathbf{1}} = J_3$ and $3 P_{\mathrm{std}} = 3 I_3 - J_3$: scaled idempotency, orthogonality, completeness $3 P_{\mathbf{1}} + 3 P_{\mathrm{std}} = 3 I_3$, traces $(3, 6)$, Pythagorean vector split $9\|v\|_3^2 = \|3 P_{\mathbf{1}} v\|_3^2 + \|3 P_{\mathrm{std}} v\|_3^2$, and exact division-free Koide equivalence:
     $$\|3 P_{\mathrm{std}} v\|_3^2 = \|3 P_{\mathbf{1}} v\|_3^2 + 3\bigl(3\|v\|_3^2 - 2(v_0 + v_1 + v_2)^2\bigr).$$
   - Ambient $R^5$ metric stretch on Bring's 3-generation subspace (`4 * normSq3` on singlet vs `1 * normSq3` on doublet) without division.
2. **Operator Trace Equipartition, $S_3/\mathbb{Z}_3$ Circulant Fourier Moments & Classical $V^{\otimes 3}$ Schur–Weyl $4 = 4$ Equipartition**:
   - General $3\times 3$ matrix identity $\mathrm{tr}((3 A - (\mathrm{tr}\,A)I_3)^2) = \mathrm{tr}(((\mathrm{tr}\,A)I_3)^2) + 3(3\,\mathrm{tr}(A^2) - 2(\mathrm{tr}\,A)^2)$.
   - Symmetric $S_3$-circulant $M^{1/2} = a_0 I_3 + a_1(C + C^2)$: $3\,\mathrm{tr}((M^{1/2})^2) = 2(\mathrm{tr}\,M^{1/2})^2 \iff 2 a_1^2 = a_0^2$.
   - Unconditional discharge of the first and second spectral moments ($\sum \lambda_k = 3 a_0$, $\sum \lambda_k^2 = 3(a_0^2 + 2bc)$) for any circulant $S(a_0, b, c)$ over `[CommRing R]` ($1 + \omega + \omega^2 = 0$), plus exact algebraic Chebyshev / Brannen–Koide parameterization ($c^2 + s^2 = 1, r_2^2 = 2, r_3^2 = 3$).
   - Exact 3-strand Schur–Weyl quantum-dimension decomposition $q^3 [4]_q + 2 q^3 [2]_q = (q^2 + 1)^3$, proving **unconditional $4 = 4$ singlet–doublet dimension equipartition** on $(\mathbb{C}^2)^{\otimes 3} = (\mathbf{4}\otimes\mathbf{1}) \oplus (\mathbf{2}\otimes\mathbf{2})$ at $q^2 = 1$ and exact $(q^2 + 1)(q^2 - 1)^2$ quantum-dimension drift for $q^2 \neq 1$.
3. **Homogeneous Quadratic Resolvent, Ordered-Ring Discriminant Positivity & Radical-Free Quartic Koide Mass Polynomial**:
   - Sum-of-squares positivity $\Delta(u, v) = 12((u + v)^2 + 2uv) > 0$ over any strict ordered commutative ring, hierarchy root dominance $x_+ > 2(u + v) > \max(u, v)$, $v$-eliminated quartic saddle equation, and the radical-free degree-4 symmetric mass polynomial:
     $$K_4(m_1, m_2, m_3) := \bigl((m_1 + m_2 + m_3)^2 - 16(m_1 m_2 + m_2 m_3 + m_3 m_1)\bigr)^2 - 1536 (m_1 + m_2 + m_3) m_1 m_2 m_3 = 0.$$
4. **Irreducible Physical Bridge (`KoideSingletDoubletEquipartitionBridge`)**:
   - Narrows `KoideTopologicalProtectionHypothesis` so 100% of the circulant, projector, Schur–Weyl, and resolvent algebra is unconditionally proved, leaving **only** the single 1-equation physical bridge $\|3 P_{\mathbf{1}} \lambda\|_3^2 = \|3 P_{\mathrm{std}} \lambda\|_3^2$ (with Pattern-3.3 `def trivialModel` and `def brannenAlgebraicModel` consistency witnesses).
5. **2026-11-28 Ruled Least-Crossing 2-Component Link Ladder (`e = \sigma_0\sigma_1\sigma_0`, `\mu = \sigma_0^4\sigma_1^{-1}`, `\tau = \sigma_0^2\sigma_1^{-1}\sigma_0\sigma_1^{-1}`) over `[CommRing R]`**:
   - Constructive 2-component strand-tracking decomposition `writhe = interComponentWrithe + selfComponentWrithe`, proving `2 * lk = (2, 4, 0)` ($\mathrm{lk} = (1, 2, 0)$, $U(1) = (3, 6, 0)$) and writhes `(3, 3, 1)`.
   - Reduced $2\times 2$ Burau representation over `[CommRing R]` (`t : Rˣ`), proving `burauWord (-1) w = imgZ w` and the **universal 3-braid identity** $\det(I_2 - B_w(-1)) = 2 - \mathrm{tr}(\mathrm{imgZ}\,w)$ for **every** $w \in B_3$, plus Morton–Birman $(1 - t^3)\Delta_L(t)$ factorizations on 2-component $(e, \mu, \tau)$ and $-(1 + t + t^2)\Delta_{4_1}(t)$ on 1-component $4_1$.
   - Cleared-denominator $N = 2$ ring-mass skein differences $q^{12}(m_e - m_\mu) = q^{12} - 1$ and $q^{12}(m_\tau - m_e) = q^4(q^{12} - 1)$, proving $m_e(1) = m_\mu(1) = m_\tau(1) = 4$ has **zero** $S_3$-doublet component (`threeDoubletVec ![4, 4, 4] = 0`).

---

## 3. Pre-Registered 80-dps Proton-Pin Numerical Measurements

1. Exact `sympy` verification of all Lean `[CommRing R]` identities (`K_4(m_1, m_2, m_3)` 4-sign factorization, Morton–Birman Burau determinants, $q^{12}$ skein differences, Schur–Weyl $4 = 4$ split).
2. 80-dps proton-pin evaluation (`q0 = q_at(80)`) on `e = \sigma_0\sigma_1\sigma_0`, `\mu = \sigma_0^4\sigma_1^{-1}`, `\tau = \sigma_0^2\sigma_1^{-1}\sigma_0\sigma_1^{-1}`:
   - Bare 3-strand $U_q(\mathfrak{sl}_2)$ ring traces $m_N(\beta)$ and $U_N(q_0) = -q_0 \partial_q \ln m_N$ for colours $N = 2, 3, 4$, plus singlet–doublet Koide ratios $Q(\sqrt{m_N(e)}, \sqrt{m_N(\mu)}, \sqrt{m_N(\tau)})$.
   - 4-strand `closure(\beta) \cup axis` convolution traces $m_N(\beta \cup A)$ for colours $N = 2, 3, 4$ via exact isotypic decomposition, cross-checked against brute-force $N^4 \times N^4$ R-matrix trace to `< 10^{-65}` relative residual.
   - Root-of-unity $\zeta_N$ Kashaev cut-axis invariants $|c_N(\beta)|$ (`q = e^{i\pi/N}`, `N = 2..16`) at 80-dps `mpmath` complex precision, cross-checked against 4-strand partial trace for $N = 2, 3, 4$ to `< 10^{-65}`, measuring $(2\pi / N)\ln|c_N(\beta)|$ vs mapping-torus volumes (`0`, `6.35458656...`, `9.50340398...`).
   - 80-dps proton-pin evaluation of the radical-free quartic Koide polynomial $K_4(1, m_\mu/m_e, m_\tau/m_e) = 0$ on $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_{q_0}^2$, verifying `< 10^{-70}` residual and recording the `ACCURACY.md` Table 3.1a `Conditional` benchmark pulls.
