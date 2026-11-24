# Purely Algebraic $O_q(SU(2))$ Woronowicz Haar Modular Entanglement First Law Across $N_\Sigma$ Braided Boundary Strands (Gap 4 Backup — Option 4B)

**Bean:** `qou-tx4q` (paired with Option 4A `claude/gap4-a0-fefferman-lorentzian-modular-20261123` @ `dc9894be61b` and `qou-slfm` `claude/reeb-length-time-bh-lcq-20261123` / PR `#9240`)
**Branch:** `claude/gap4b-oqsu2-haar-entanglement-first-law-20261123` (off `origin/main` @ `e330ab6aa04`)
**Pre-registration commit:** `abadf81b1da0e43b3745330c624ed1ae4c42fc62` (committed & pushed before probe authoring or numerical evaluation)
**Lean 4 module (`§7c`, zero `: ℝ`, `0` sorries, `0` custom axioms):** `folio/quantum-observable-universe/lean/QOU/GravitySpacetime/OqSU2HaarModularEntanglement.lean` (`a91c7dd28a962f7d1d57c3f8c06675ca431ee090`)
**80-dps probe & witness:** `computations/probes/gap4b_oqsu2_haar_entanglement/gap4b_oqsu2_haar_entanglement_probe.py` (`b342599c982206c2f67e9bbc1038c07199258ddc`) & `gap4b-oqsu2-haar-entanglement.witness.json` (`3644e7aa65d2544e87d7f9ce5002fcb44bafd718`, `q0Anchor = "proton"`, `workdps = 80`, `output_dps = 70`, zero `float64`, `selectedCandidate = "none"`)

---

## 1. Executive Summary & Honest Verdict

1. **Exact Single-Strand Woronowicz Haar Modular State & Entanglement First Law (`PROVED`, `0` sorries, `§7c` generic `[CommRing R]` / `[Field K]`):**
   - Directly from Woronowicz's rank-1 Haar identity $(1 + q^2) h(\beta \gamma) = -q h(1)$ (`OqSU2.haar_cleared_alpha_delta` in `OqSU2ModularNakayama`), a normalized Haar functional $h(1) = 1$ induces on a single spin-$1/2$ boundary strand the exact two-level modular state (`oqsu2_haar_reduced_eigenvalues`, `haar_single_strand_identities`)
     $$p_+(q) = h(\delta\alpha) = \frac{q^2}{1 + q^2} = \frac{q}{[2]_q}, \qquad p_-(q) = h(\alpha\delta) = \frac{1}{1 + q^2} = \frac{q^{-1}}{[2]_q}, \qquad p_+(q) + p_-(q) = 1,$$
     with modular boost step ratio $p_+(q) / p_-(q) = q^2 = e^{\beta_{\mathrm{mod}}}$ ($\beta_{\mathrm{mod}} = 2 \ln q$, matching $\nu_q(\alpha) = q^2 \alpha$) and exact purification by the $U_q(\mathfrak{sl}_2)$ spin-$0$ cup vector $|s_q\rangle = (1 + q^2)^{-1/2}(q|+,-\rangle - |-,+\rangle)$ (`uq_cup_purifies_haar_state`).
   - Over any `[CommRing R]` and `[Fintype I]`, the Blanco–Casini–Hung–Myers entanglement first law holds identically (`entanglement_first_law_exact`):
     $$S(\sigma) - S(\rho) + D(\sigma \| \rho) = \mathrm{Tr}\big((\sigma - \rho) K_\rho\big), \qquad K_\rho = -\ln\rho,$$
     with exact partition-function ($\ln Z$) cancellation for normalized Gibbs/Haar states (`gibbs_modular_first_law_normalized`, `haar_single_strand_modular_first_law`), necessary-and-sufficient linearized first law $\delta S = \delta\langle K_\rho \rangle \iff \mathrm{Tr}(\delta\rho) = 0$ (`tangent_entanglement_first_law_iff_traceless`), and strict positive-definiteness of the quadratic Fisher–Rao / $\chi^2$ remainder (`fisherChiSq_pos_def`).

2. **Resolution of the $N_\Sigma$-Strand Singlet Projection vs Half-System Global Singlet Dichotomy (`PROVED` + Verified to 80 dps):**
   - **Ensemble `E1` / `E3a` (Unprojected Haar Product = Pairwise $U_q(\mathfrak{sl}_2)$ Rainbow-Cup Global Singlet $|s_q\rangle^{\otimes N_\Sigma}$ Traced Over $B$):** Strictly extensive at **every** $N_\Sigma$ (`n_strand_haar_extensivity`), giving $S / N_\Sigma = \langle K_\Sigma \rangle / N_\Sigma = s_{\mathrm{Haar}}(q_0) = 0.68773317650021572977...$ and quantum Schur–Weyl sector weights $w_j = M_{N_\Sigma, j}[2j+1]_{q_0} / [2]_{q_0}^{N_\Sigma}$.
   - **Ensemble `E2` (Direct $J = 0$ Singlet Projection $\Pi_{J=0} \rho_\Sigma^{\mathrm{unproj}} \Pi_{J=0} / Z$ on $V_{1/2}^{\otimes N_\Sigma}$):** Because $J_z^{\mathrm{tot}}|_{J=0} = 0$, the Haar modular operator $q^{2 J_z^{\mathrm{tot}}}$ collapses identically to $1$ on $J = 0$, forcing $\rho_\Sigma|_{\mathrm{sing}} = \frac{1}{C_m} I_{C_m}$ (`singlet_projected_haar_uniform_q_independent`) — **strictly $q$-independent**, with $\langle K_{\mathrm{boost}} \rangle = 0$ and $S / N_\Sigma = (\ln C_{N_\Sigma/2}) / N_\Sigma \to \ln 2 = 0.69314718055994530942...$ (with the Kaul–Majumdar $-\frac{3}{2}\ln(N_\Sigma/2)$ subleading term).
   - **Ensemble `E3b` (Half-System Trace of $2 N_\Sigma$-Strand Global Singlet $|\Psi_{\mathrm{Cat}}\rangle$ / $\frac{1}{C_{N_\Sigma}}\Pi_{J_{AB}=0}$):** Tracing out half ($B$) of a global $U_{q_0}(\mathfrak{sl}_2)$ singlet produces a **genuinely $q_0$-dependent** reduced state on $\mathcal{H}_A = V_{1/2}^{\otimes N_\Sigma}$ at every finite $N_\Sigma \ge 2$ (`bipartite_two_strand_singlet_spectrum_properties`), weighted within each spin-$j$ block by Clebsch–Gordan sublevels $q_0^{2\mu} / [2j+1]_{q_0}$. For real $q_0 > 1$, the spin-$j$ magnetic edge entropy **saturates at the finite UV-regulated ceiling**
     $$S_\infty^{\mathrm{edge}}(q_0) = -\ln(1 - q_0^{-2}) + \frac{2\ln q_0}{q_0^2 - 1} = 2.56875892175693627183...$$
     (verified to `4.22e-81` at $j = 500$, vs unbounded $\ln(2j+1)$ at $q = 1$), so $S(\rho_A^{\mathrm{Cat\text{-}sing}}) / N_\Sigma$ also converges asymptotically to $\ln 2$ while retaining exact finite-$N_\Sigma$ $q_0$-splitting. (By contrast, pure $[2j+1]_{q_0}^2$ weighting without multiplicity `E3c` concentrates near $j = N_\Sigma/2$ where $M_{2m,m} = 1$, giving $O(1/N_\Sigma) \to 0$ per strand.)

3. **Honest Verdict on $1/4 = 0.25$ — Confirms Option 4A (`dc9894be61b`):**
   - Note on `PREREGISTRATION.md` §3.1: algebraic proof of `uqCasimirSpinHalf_algebraic_identities` established the exact positive excess $C_2^{(q)}(1/2) - \frac{3}{4} = \frac{(q - 1)^2}{4(q + 1)^2} > 0$, so $\frac{3}{4} < C_2^{(q_0)}(1/2) = 0.7506792038... < 1$ (`uqCasimirSpinHalf_strict_bounds`, correcting the pre-registered sign guess $< 3/4$).
   - Across all **21** combinations of the 3 extensive entropy rates (`E1` $s_{\mathrm{Haar}}(q_0)$, `E2`/`E3b` $\ln 2$, `E4` $\ln[2]_{q_0}$) and 7 parameter-free algebraic area operators (`1`, $3/4$, $\sqrt{3}/2$, $C_2^{(q_0)}(1/2)$, $\sqrt{C_2^{(q_0)}(1/2)}$, $[2]_{q_0}^2$, and $\gamma_{\mathrm{BI}}=1$ $8\pi\sqrt{C_2^{(q_0)}(1/2)}$), **zero** purely algebraic discrete candidates hit $1/4 = 0.25$ — the closest (`ln[2]_{q_0} / [2]_{q_0}^2 = 0.17275755...`) still misses $1/4$ by **$-30.90\%$**.
   - **Conclusion:** Pure discrete $O_q(SU(2))$ Haar modular theory furnishes the exact non-tracial modular state and entanglement first law $\delta S = \delta\langle K_\Sigma \rangle$, but **confirming Option 4A (`FeffermanLorentzianHorizonEntropy` @ `dc9894be61b`)**, converting $\delta\langle K_\Sigma \rangle$ into $\delta A / (4\ell_{\mathrm{grav}}^2)$ strictly requires the continuum 4D Lorentzian $(2\pi)/(8\pi) = 1/4$ Bisognano–Wichmann + Einstein–Raychaudhuri geometric bridge (`HaarLorentzianModularBridgeConjecture`).

---

## 2. Live-Verified Bibliographic Ledger (`doi.org/api/handles` `responseCode == 1`)

| Reference | Citation | Verified DOI (`responseCode == 1`) |
|---|---|---|
| Woronowicz (1987) | *Publ. RIMS* **23**(1), 117–181 | `10.2977/prims/1195176848` |
| Blanco, Casini, Hung & Myers (2013) | *JHEP* **2013**(8), 060 | `10.1007/JHEP08(2013)060` |
| Casini, Huerta & Myers (2011) | *JHEP* **2011**(5), 036 | `10.1007/JHEP05(2011)036` |
| Donnelly (2012) | *Phys. Rev. D* **85**(8), 085004 | `10.1103/PhysRevD.85.085004` |
| Couvreur, Jacobsen & Saleur (2017) | *Phys. Rev. Lett.* **119**(4), 040601 | `10.1103/PhysRevLett.119.040601` |
| Kaul & Majumdar (2000) | *Phys. Rev. Lett.* **84**(23), 5255–5257 | `10.1103/PhysRevLett.84.5255` |
| Ashtekar, Baez, Corichi & Krasnov (1998) | *Phys. Rev. Lett.* **80**(5), 904–907 | `10.1103/PhysRevLett.80.904` |
| Bekenstein (1973) | *Phys. Rev. D* **7**(8), 2333–2346 | `10.1103/PhysRevD.7.2333` |
| Hawking (1975) | *Commun. Math. Phys.* **43**(3), 199–220 | `10.1007/BF02345020` |
| Jacobson (1995) | *Phys. Rev. Lett.* **75**(7), 1260–1263 | `10.1103/PhysRevLett.75.1260` |

---

## 3. 80-dps Numerical Results (`q0Anchor = "proton"`)

### 3.1 Battery H1 — Single-Strand Haar State & Finite / Tangent Entanglement First Law

- $q_0 = 1.10997858275138080759166909561076887987449912187358...$ (`[2]_{q_0} = 2.0108968667...`, `[3]_{q_0} = 3.0437062085...$)
- $p_+(q_0) = 0.5519818550262050728383264...$, $p_-(q_0) = 0.4480181449737949271616736...$, $p_+/p_- = q_0^2 = 1.23205245416676393127...$, $\beta_{\mathrm{mod}} = 2\ln q_0 = 0.20868144063903902463...$
- $s_{\mathrm{Haar}}(q_0) = 0.6877331765002157297686575...$, $\ln 2 = 0.6931471805599453094172321...$, $\ln[2]_{q_0} = 0.6985808248941738760383627...$
- Max single-strand cup-purification & finite-difference first-law residual: **`1.38e-81`**.
- Tangent variation check ($\delta p = (+1, -1)$, exact $\frac{1}{2}\sum \delta p_i^2 / p_i = 2.02185310426626099470...$):
  - $\varepsilon = 10^{-10}$: $\delta\langle K_\rho \rangle - \Delta S / \varepsilon = 2.0218531043 \times 10^{-10}$, quadratic Fisher error `2.83e-11`;
  - $\varepsilon = 10^{-20}$: $\delta\langle K_\rho \rangle - \Delta S / \varepsilon = 2.0218531043 \times 10^{-20}$, quadratic Fisher error `2.83e-21`;
  - $\varepsilon = 10^{-30}$: $\delta\langle K_\rho \rangle - \Delta S / \varepsilon = 2.0218531043 \times 10^{-30}$, quadratic Fisher error `2.83e-31`.

### 3.2 Battery H2 — Multi-Strand Entanglement Spectra ($N_\Sigma = 2, 4, \dots, 40$ & $N_\Sigma \to \infty$)

| $N_\Sigma$ | `E1`/`E3a` $S/N_\Sigma$ (Haar / Cup) | `E2` $S/N_\Sigma$ ($\Pi_{J=0}$ Direct) | `E3b` $S/N_\Sigma$ ($q_0$ Global Singlet) | `E3b` $S/N_\Sigma$ ($q=1$ Global Singlet) | `E3c` $S/N_\Sigma$ ($[2j+1]_{q_0}^2$) | $\langle K_{\mathrm{boost}}\rangle / N_\Sigma$ (`E1` / `E3b`) |
|---:|---:|---:|---:|---:|---:|---|
| `2` | `0.687733176500` | `0.000000000000` | `0.617636765984` | `0.621226662447` | `0.649004549270` | `-0.0108476484` / `-0.0072058044` |
| `4` | `0.687733176500` | `0.173286795140` | `0.635929744543` | `0.638993782228` | `0.592505335515` | `-0.0108476484` / `-0.0061589789` |
| `8` | `0.687733176500` | `0.329882166201` | `0.658782646675` | `0.661612976059` | `0.517590767992` | `-0.0108476484` / `-0.0057089087` |
| `16` | `0.687733176500` | `0.454089357703` | `0.673548643051` | `0.676232491561` | `0.418462265917` | `-0.0108476484` / `-0.0054504306` |
| `24` | `0.687733176500` | `0.510222960388` | `0.679005840518` | `0.681609506300` | `0.344658670530` | `-0.0108476484` / `-0.0053224996` |
| `32` | `0.687733176500` | `0.543157059371` | `0.681853675346` | `0.684394936589` | `0.287790959038` | `-0.0108476484` / `-0.0052280879` |
| `40` | `0.687733176500` | `0.565122108888` | `0.683610368279` | `0.686097590078` | `0.244984558686` | `-0.0108476484` / `-0.0051485388` |
| `200` | `0.687733176500` | `0.655690577822` | `0.689847892909` | — | — | — |
| $\infty$ | `0.687733176500` | `0.693147180560` | `0.693147180560` | `0.693147180560` | `0` | `-0.0108476484` / `0` |

- At $N_\Sigma = 2$, `E3b` matches the Lean §3 spectrum `(0.50000000000000, 0.20239345878930, 0.16427341068541, 0.13333313052528)` to **`2.11e-80`**, and binomial vs quantum Schur–Weyl summation agrees across all $N_\Sigma = 2 \dots 40$ to **`2.11e-80`**.

### 3.3 Battery H3 — Side-by-Side Comparison Against Parameter-Free $q$-Casimir Area Operators (`selectedCandidate = "none"`)

| Area Operator Candidate | $a_{\mathrm{alg}}(q_0)$ per Strand | $s_{\mathrm{Haar}}(q_0) / a_{\mathrm{alg}}$ | Rel. Diff vs $1/4$ (`Haar`) | $\ln 2 / a_{\mathrm{alg}}$ (`E2`/`E3b`) | $\ln[2]_{q_0} / a_{\mathrm{alg}}$ (`E4`) |
|---|---:|---:|---:|---:|---:|
| `A1_unit_reeb_cell` ($1$) | `1.000000000000` | `0.687733176500` | `+175.09%` | `0.693147180560` | `0.698580824894` |
| `A2a_su2_casimir_quad` ($3/4$) | `0.750000000000` | `0.916977568667` | `+266.79%` | `0.924196240747` | `0.931441099859` |
| `A2b_su2_casimir_sqrt` ($\sqrt{3}/2$) | `0.866025403784` | `0.794125869135` | `+217.65%` | `0.800377422546` | `0.806651654705` |
| `A3a_uqsl2_casimir_quad` ($C_2^{(q_0)}(1/2)$) | `0.750679203871` | `0.916147900422` | `+266.46%` | `0.923360041135` | `0.930598317972` |
| `A3b_uqsl2_casimir_sqrt` ($\sqrt{C_2^{(q_0)}(1/2)}$) | `0.866417453580` | `0.793766530927` | `+217.51%` | `0.800015255517` | `0.806286636827` |
| `A4_jones_subfactor_index` ($[2]_{q_0}^2$) | `4.043706208533` | `0.170074961144` | `-31.97%` | `0.171413832934` | `0.172757562624` (`-30.90%`) |
| `A5_untuned_8pi_uq_casimir_sqrt` ($8\pi\sqrt{C_2^{(q_0)}}$) | `21.77544565653` | `0.031582966729` | `-87.37%` | `0.031831595605` | `0.032081125812` |
| **Option 4A Arm N1 Lock** ($G_q(\hbar_q/c_q)^2 = 1$) | $4 s_{\mathrm{strand}}$ (`2.7509` / `2.7726` / `2.7943`) | **`0.250000000000`** | **`0.00%`** | **`0.250000000000`** | **`0.250000000000`** |
| **Option 4A Arm N2 Lock** ($\hbar_q G_q / c_q^3 = q_0$, in Reeb cells) | $4 q_0 s_{\mathrm{strand}}$ (`3.0535` / `3.0775` / `3.1016`) | `0.225229570989` | `-9.91%` ($-\hbar_{q_0}$) | `0.225229570989` | `0.225229570989` |

---

## 4. Remaining Open Boundary (`Rule 13a` — `HaarLorentzianModularBridgeConjecture`)

- **Closed in Option 4B:** Exact generic-field Woronowicz Haar spin-$1/2$ modular spectrum (`oqsu2_haar_reduced_eigenvalues`), exact Blanco–Casini–Hung–Myers finite & tangent entanglement first law (`entanglement_first_law_exact`, `tangent_entanglement_first_law_iff_traceless`), exact contrast between $q$-independent direct singlet projection (`E2`) and $q_0$-split half-system global-singlet entanglement (`E3b`), and exact $U_q(\mathfrak{sl}_2)$ Casimir bounds (`uqCasimirSpinHalf_strict_bounds`).
- **Isolated as open (`0` instances):** Coupling Woronowicz's discrete modular boost $\beta_{\mathrm{mod}} = 2\ln q$ to the 4D Lorentzian Fefferman–Rindler boost period $2\pi$ and Einstein–Raychaudhuri null-sheet focusing $8\pi G / c^3$ (`HaarLorentzianModularBridgeConjecture` / Option 4A `FeffermanDynamicalEinsteinHorizonConjecture`).
