# Pre-Registration: Purely Algebraic $O_q(SU(2))$ Woronowicz Haar Modular Entanglement First Law Across $N_\Sigma$ Braided Boundary Strands (Gap 4 Backup — Option 4B, `qou-tx4q`)

**Date:** 2026-11-23
**Branch:** `claude/gap4b-oqsu2-haar-entanglement-first-law-20261123` (branched off `origin/main` @ `e330ab6aa04`)
**Bean:** `qou-tx4q` (paired for side-by-side comparison with Option 4A `claude/gap4-a0-fefferman-lorentzian-modular-20261123` @ `dc9894be61b` and `qou-slfm` `claude/reeb-length-time-bh-lcq-20261123` / PR `#9240`)
**Discipline:** Written, committed, and pushed **before** writing or executing `gap4b_oqsu2_haar_entanglement_probe.py` or computing any numerical entanglement-to-area ratios.

---

## 1. Precision, Calibration & Anti-Fit Lock (`STRICT`)

- **Working precision:** `mpmath.workdps(80)` (`WORK_DPS = 80`, `OUT_DPS = 70` serialized into the witness JSON), `truncation_bound = 1e-70`.
- **Substrate pin:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`, CAL-1 only; zero new calibration inputs).
- **Zero `float64`:** Zero `float(...)` or `complex(...)` casts, zero binary64 floating-point literals, and zero `math` / `numpy` / `cmath` / `statistics` imports anywhere in the probe script (`scripts/probe-float64-guard.py --diff` strict gate).
- **Zero tunable parameters (`selectedCandidate = "none"`):**
  - Woronowicz's normalized Haar state $h : O_q(SU(2)) \to K$ ($h(1) = 1$) fixes the single-strand spin-$1/2$ modular eigenvalues uniquely via $(1 + q^2) h(\beta \gamma) = -q$ (`OqSU2.haar_cleared_alpha_delta` in `OqSU2ModularNakayama.lean`), giving $p_+(q) = h(\delta\alpha) = \frac{q^2}{1+q^2} = \frac{q}{[2]_q}$ and $p_-(q) = h(\alpha\delta) = \frac{1}{1+q^2} = \frac{q^{-1}}{[2]_q}$, with zero free temperature or Immirzi-like parameters.
  - All boundary ensembles (`E1`–`E4`) and all parameter-free $U_q(\mathfrak{sl}_2)$ / $O_q(SU(2))$ Casimir and algebraic puncture-area operators (`A1`–`A5`) are locked below upfront and reported side-by-side without post-hoc selection or rescaling.

---

## 2. Live-Verified Literature Citations (`doi.org/api/handles` `responseCode == 1` & Crossref)

1. **Stanisław Lech Woronowicz (1987)**, *"Twisted $SU(2)$ group. An example of a non-commutative differential calculus"*, *Publications of the Research Institute for Mathematical Sciences* **23**(1), 117–181 — DOI: `10.2977/prims/1195176848` (`responseCode == 1`, repo key `[woronowicz1987]`).
2. **David D. Blanco, Horacio Casini, Ling-Yan Hung, & Robert C. Myers (2013)**, *"Relative entropy and holography"*, *Journal of High Energy Physics* **2013**(8), 060 — DOI: `10.1007/JHEP08(2013)060` (`responseCode == 1`).
3. **Horacio Casini, Marina Huerta, & Robert C. Myers (2011)**, *"Towards a derivation of holographic entanglement entropy"*, *Journal of High Energy Physics* **2011**(5), 036 — DOI: `10.1007/JHEP05(2011)036` (`responseCode == 1`).
4. **William Donnelly (2012)**, *"Decomposition of entanglement entropy in lattice gauge theory"*, *Physical Review D* **85**(8), 085004 — DOI: `10.1103/PhysRevD.85.085004` (`responseCode == 1`).
5. **Romain Couvreur, Jesper Lykke Jacobsen, & Hubert Saleur (2017)**, *"Entanglement in Nonunitary Quantum Critical Spin Chains"*, *Physical Review Letters* **119**(4), 040601 — DOI: `10.1103/PhysRevLett.119.040601` (`responseCode == 1`).
6. **Romesh K. Kaul & Parthasarathi Majumdar (2000)**, *"Logarithmic correction to the Bekenstein–Hawking entropy"*, *Physical Review Letters* **84**(23), 5255–5257 — DOI: `10.1103/PhysRevLett.84.5255` (`responseCode == 1`).
7. **Abhay Ashtekar, John Baez, Alejandro Corichi, & Kirill Krasnov (1998)**, *"Quantum Geometry and Black Hole Entropy"*, *Physical Review Letters* **80**(5), 904–907 — DOI: `10.1103/PhysRevLett.80.904` (`responseCode == 1`).
8. **Jacob D. Bekenstein (1973)**, *"Black Holes and Entropy"*, *Physical Review D* **7**(8), 2333–2346 — DOI: `10.1103/PhysRevD.7.2333` (`responseCode == 1`, repo key `[bekenstein1973]`).
9. **Stephen W. Hawking (1975)**, *"Particle Creation by Black Holes"*, *Communications in Mathematical Physics* **43**(3), 199–220 — DOI: `10.1007/BF02345020` (`responseCode == 1`, repo key `[hawking1975]`).
10. **Ted Jacobson (1995)**, *"Thermodynamics of Spacetime: The Einstein Equation of State"*, *Physical Review Letters* **75**(7), 1260–1263 — DOI: `10.1103/PhysRevLett.75.1260` (`responseCode == 1`, repo key `[jacobson1995]`).

---

## 3. Pre-Registered Lean 4 & 80-dps Probe Batteries

### 3.1 Lean 4 Module (`folio/quantum-observable-universe/lean/QOU/GravitySpacetime/OqSU2HaarModularEntanglement.lean`)
Formalized strictly under `§7c` (`[CommRing R]`, `[Field K]`, and `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`; zero `: ℝ`, zero empirical literals, `0 sorry`, `0` custom `axiom`s, `set_option autoImplicit false`):
1. **Single-Strand Woronowicz Haar Modular State & $U_q(\mathfrak{sl}_2)$ Cup Purification:**
   - `haarProbPlus q = q^2 / (1 + q^2)` and `haarProbMinus q = 1 / (1 + q^2)`, bridged directly to `OqSU2.haar_modular_swap_alpha_delta` ($h(\delta\alpha) = p_+(q)$, $h(\alpha\delta) = p_-(q)$ when $h(1)=1$),
   - Pivotal quantum-trace equivalence $p_+(q) = q / [2]_q$ and $p_-(q) = q^{-1} / [2]_q$, unit trace $p_+(q) + p_-(q) = 1$, modular boost ratio $p_+(q)/p_-(q) = q^2$ ($= e^{\beta_{\mathrm{mod}}}$, $\beta_{\mathrm{mod}} = 2\ln q$), polarization bias $p_+(q) - p_-(q) = (q - q^{-1}) / [2]_q$, ordered-field strict hierarchy $0 < p_-(q) < 1/2 < p_+(q) < 1$ for $1 < q$, and partial-trace purification via the $U_q(\mathfrak{sl}_2)$ spin-$0$ cup state.
2. **Exact Algebraic Entanglement First Law (Blanco–Casini–Hung–Myers):**
   - Exact finite-difference identity $S(\sigma) - S(\rho) + D(\sigma \| \rho) = \mathrm{Tr}((\sigma - \rho) K_\rho)$ over any `[CommRing R]` and `[Fintype I]`,
   - Gibbs / Woronowicz Haar specialization $S(\sigma) - S(\rho) + D(\sigma \| \rho) = \beta_{\mathrm{mod}} (\langle H_{\mathrm{boost}} \rangle_\sigma - \langle H_{\mathrm{boost}} \rangle_\rho)$ with exact partition-function cancellation under $\sum_i p_i = \sum_i r_i = 1$,
   - Tangent linear variation equivalence $\delta S(\delta p) = \delta\langle K_\rho \rangle(\delta p) \iff \sum_i \delta p_i = 0$, plus ordered-field relative-entropy non-negativity and strict positivity of the quadratic Fisher–Rao / $\chi^2$ remainder.
3. **$N_\Sigma$-Strand Unprojected vs Singlet-Projected vs Bipartite Global-Singlet Spectrum & $q$-Casimir Area Lock:**
   - Exact $N_\Sigma$-strand product extensivity vs triviality of $q^{2 J_z^{\mathrm{tot}}} = 1$ on the $J = 0$ singlet sector (collapsing direct singlet projection to the $q$-independent uniform state $1/C_m$), contrasted against the explicitly $q$-dependent 2-strand ($2 N_\Sigma = 4$, $C_2 = 2$) half-system global-singlet spectrum $\{\frac{1}{2}, \frac{q^2}{2[3]_q}, \frac{1}{2[3]_q}, \frac{q^{-2}}{2[3]_q}\}$,
   - Rational $U_q(\mathfrak{sl}_2)$ spin-$1/2$ quadratic Casimir `uqCasimirSpinHalf q = (q^2 + q + 1) / (q + 1)^2` (satisfying `1/2 < uqCasimirSpinHalf q < 3/4` for $1 < q$) and exact quarter-area lock / non-coincidence theorems.

### 3.2 Pre-Registered 80-dps Numerical Batteries (`N_Sigma = 2, 4, ..., 40` and `N_Sigma -> infinity`)
1. **Battery H1 — Single-Strand Haar State & Finite / Tangent Entanglement First Law:**
   - Evaluate $p_+(q_0), p_-(q_0), \beta_{\mathrm{mod}} = 2\ln q_0, s_{\mathrm{Haar}}(q_0), \langle K_1 \rangle$ and verify `S(sigma) - S(rho) + D(sigma || rho) - Tr((sigma - rho) K_rho) = 0` to `< 1e-75` across finite states and tangent steps $\varepsilon \in \{10^{-10}, 10^{-20}, 10^{-30}\}$.
2. **Battery H2 — $N_\Sigma = 2, 4, \dots, 40$ & Asymptotic $N_\Sigma \to \infty$ Boundary Ensembles:**
   - **`E1` / `E3a` (Unprojected Haar product = Bipartite Rainbow $q$-Cup Singlet $|s_q\rangle^{\otimes N_\Sigma}$):** Compute $S/N_\Sigma$ and $\langle K_\Sigma \rangle / N_\Sigma$ via both binomial $J_z^{\mathrm{tot}}$ summation and Schur–Weyl quantum-dimension weights $w_j = M_{N_\Sigma,j} [2j+1]_{q_0} / [2]_{q_0}^{N_\Sigma}$, verifying exact agreement to `< 1e-75`.
   - **`E2` (Direct $J = 0$ Singlet Projection on $V_{1/2}^{\otimes N_\Sigma}$):** Verify $q_0^{2 J_z^{\mathrm{tot}}}|_{J=0} = 1$, singlet weight $P_{J=0} = C_{N_\Sigma/2} / [2]_{q_0}^{N_\Sigma}$, uniform projected state $\frac{1}{C_m} I_{C_m}$ with $S / N_\Sigma = (\ln C_{N_\Sigma/2}) / N_\Sigma \to \ln 2$, and Kaul–Majumdar $-\frac{3}{2}\ln(N_\Sigma/2)$ logarithmic subleading term.
   - **`E3b` (Half-System Trace of $2 N_\Sigma$-Strand Global $U_{q_0}(\mathfrak{sl}_2)$ Singlet $|\Psi_{\mathrm{Cat}}\rangle$ / $\frac{1}{C_{N_\Sigma}}\Pi_{J_{AB}=0}$):** Compute the exact $q_0$-dependent spectrum across spin sectors $j = 0, \dots, N_\Sigma/2$ with Clebsch–Gordan sublevels $q_0^{2\mu}/[2j+1]_{q_0}$, and test convergence of the spin-$j$ magnetic edge entropy to the UV-regulated asymptotic ceiling $S_\infty^{\mathrm{edge}}(q_0) = -\ln(1 - q_0^{-2}) + \frac{2\ln q_0}{q_0^2 - 1}$.
   - **`E3c` & `E4` (Pure Quantum-Dimension Squared Global Singlet $p_j \propto [2j+1]_{q_0}^2$ & Temperley–Lieb Markov Ceiling $\ln[2]_{q_0}$):** Evaluate side-by-side for completeness.
3. **Battery H3 — Side-by-Side Test Against Parameter-Free $q$-Casimir Area Operators:**
   - Compare asymptotic and finite-$N_\Sigma$ entropy rates (`E1` $s_{\mathrm{Haar}}(q_0)$, `E2`/`E3b` $\ln 2$, `E4` $\ln[2]_{q_0}$) against all five parameter-free algebraic area candidates per puncture:
     * `A1_unit_reeb_cell`: $a_1 = 1$,
     * `A2a_su2_casimir_quad`: $C_2(1/2) = 3/4$, and `A2b_su2_casimir_sqrt`: $\sqrt{3}/2$,
     * `A3a_uqsl2_casimir_quad`: $C_2^{(q_0)}(1/2) = \frac{q_0^2 + q_0 + 1}{(q_0 + 1)^2}$, and `A3b_uqsl2_casimir_sqrt`: $\frac{\sqrt{q_0^2 + q_0 + 1}}{q_0 + 1}$,
     * `A4_jones_subfactor_index`: $[2]_{q_0}^2 = (q_0 + q_0^{-1})^2$,
     * `A5_untuned_8pi_uq_casimir_sqrt`: $8\pi \sqrt{C_2^{(q_0)}(1/2)}$ (with $\gamma_{\mathrm{BI}} = 1$, testing whether even importing $8\pi$ without Bisognano–Wichmann modular cancellation hits $1/4$).
   - **Pre-Registered Decision Criterion:** Report `S / A_alg` and relative discrepancy from `1/4 = 0.25` across every `(E, A)` pair with zero post-hoc tuning (`selectedCandidate = "none"`), testing whether discrete $O_q(SU(2))$ Haar entanglement alone reproduces $1/4$ or confirms Option 4A's conclusion (`dc9894be61b`) that $1/4 = (2\pi)/(8\pi)$ strictly requires the continuum 4D Lorentzian Bisognano–Wichmann / Einstein–Raychaudhuri bridge.
