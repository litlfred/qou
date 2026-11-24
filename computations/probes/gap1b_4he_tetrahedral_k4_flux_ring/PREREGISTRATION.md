# Pre-Registration: Closing Open Gap 1 Backup (Option 1B, `qou-3kkz`) — 4-Body Tetrahedral $K_4$ Colour-Flux Ring Exchange & Nucleon-Cluster Wigner Majorana Space-Exchange across $A = 2, 3, 4$ (2026-11-23)

Bean `qou-3kkz` (Option 1B backup behind `qou-ni4i`, building on `#9212` `ConfinementLayerTower.lean` and `#9221` `ColourReconnectionStokesAssembly.lean`).
Written, committed, and pushed **before** computing any $A \in \{2, 3, 4\}$ binding energies or numerical model outputs.

---

## 1. Physical Context & Why Distinct $K_A$ Nucleon Clusters Avoid $12q$ Single-Bag Pauli Quenching

1. **Adiabatic Nucleon-Cluster Confinement (`ConfinementLayerTower.lean`, `#9212`):**
   - Each nucleon is a confined Layer-1 $\mathcal{U}_q(\mathfrak{sl}_3)$ colour singlet $|\varepsilon_{q_0}\rangle \in (K^3)^{\otimes 3}$ protected by the central ribbon full-twist Casimir gap $\Delta_8(q_0) = \frac{1 - q_0^{-6}}{q_0 - q_0^{-1}} = q_0^{-3}[3]_{q_0} > 0$ ($\to 3$ as $q_0 \to 1$).
   - Under `promoteLayer` (`ConfinementLayerTower.promoteLayer`), $s$-shell nuclei ($A \in \{2, 3, 4\}$: ${}^2\mathrm{H}, {}^3\mathrm{H}, {}^3\mathrm{He}, {}^4\mathrm{He}$) consist of $A$ **distinct colour-singlet nucleon cluster nodes** on the complete graph $K_A$ rather than collapsing all $3A$ quarks into a single zero-separation $0s$ bag (`[12]` under $S_{12}$), which suffers short-range quark-Pauli core dilution.
2. **Exact $K_A$ Simplex & Cycle Combinatorics ($A \in \{1, 2, 3, 4\}$):**
   - **2-body edges:** $e_2(A) = \binom{A}{2} \in \{0, 1, 3, 6\}$ (`1` edge in ${}^2\mathrm{H}$, `3` edges in ${}^3\mathrm{H}/{}^3\mathrm{He}$, `6` edges on the ${}^4\mathrm{He}$ tetrahedron $K_4$). Moreover, $K_4$ is $3$-regular (`deg = 3 = N_c`) and decomposes into $3$ disjoint perfect matchings (`Tait 3-edge-colouring`), pairing all $12$ valence quarks 1-to-1 with the $12$ half-edges of $K_4$ without quark reuse.
   - **3-body triangular faces:** $f_3(A) = \binom{A}{3} \in \{0, 0, 1, 4\}$ unoriented faces ($2\binom{A}{3} \in \{0, 0, 2, 8\}$ oriented cyclic faces). Crucially, $f_3(2) = 0$: **every** 3-body triangular plaquette term vanishes identically in ${}^2\mathrm{H}$, preserving `#9221`'s deuteron benchmark $B({}^2\mathrm{H}) = 2.264785\;\mathrm{MeV}$ (`+1.81%` vs `2.224566 MeV`) untouched.
   - **4-body tetrahedral Hamiltonian rings:** $c_4(A) = 3\binom{A}{4} \in \{0, 0, 0, 3\}$ unoriented Hamiltonian 4-cycles ($6\binom{A}{4} \in \{0, 0, 0, 6\}$ oriented 4-cycles: $(0\text{-}1\text{-}2\text{-}3\text{-}0)$, $(0\text{-}1\text{-}3\text{-}2\text{-}0)$, $(0\text{-}2\text{-}1\text{-}3\text{-}0)$), activating exclusively at the $A = 4$ $\alpha$-cluster closure.
3. **Nucleon-Level Wigner $\mathrm{SU}(4)$ Majorana Space-Exchange (`[1^A]_{\sigma\tau}`):**
   - On nucleon spin-isospin space $\mathbb{V}_{\sigma\tau} = R^2_\sigma \otimes R^2_\tau \cong R^4$, the spin-isospin swap satisfies the exact integer identity $4 P_{ab}^{\sigma\tau} = (I + \vec\sigma_a \cdot \vec\sigma_b)(I + \vec\tau_a \cdot \vec\tau_b)$.
   - Composite nucleon Fermi–Dirac antisymmetry $P_{ab}^x P_{ab}^{\sigma\tau} = -I$ yields Wigner's Majorana space-exchange operator $P_{ab}^x = -P_{ab}^{\sigma\tau} = -\frac{1}{4}(I + \vec\sigma_a \cdot \vec\sigma_b)(I + \vec\tau_a \cdot \vec\tau_b)$.
   - On the spin-isospin antisymmetric subrepresentation $\Lambda^A(R^4) = [1^A]_{\sigma\tau}$ ($\dim \binom{4}{A} = 6, 4, 1$ for $A = 2, 3, 4$, and $\dim = 0$ for $A \ge 5$, closing the $0s$ shell at ${}^4\mathrm{He}$), $P_{ab}^{\sigma\tau} = -1$ and hence **$P_{ab}^x = +1$ on every nucleon pair**, giving $\sum_{0 \le a < b < A} P_{ab}^x = \binom{A}{2} \in \{1, 3, 6\}$ space-symmetric bonds and $+1$ spatial parity on all triangular 3-cycles and tetrahedral 4-cycles.
4. **Correction of a Non-Adjacent Transport Inversion in `#9221`'s `V2_allpairs_fierz`:**
   - Inspection of `w4_colour_reconn_stokes_aomega_probe.py` lines 774–776 shows that `V2`'s non-adjacent pair word built `prefix + [(target_gen, False)] + suffix` with `prefix` descending and `suffix` ascending, which under `apply_word`'s right-to-left `reversed(word)` acted as $(R_s \cdots R_{t-2}) R_{t-1} (R_{t-2}^{-1} \cdots R_s^{-1})$ instead of $(R_s^{-1} \cdots R_{t-2}^{-1}) R_{t-1} (R_{t-2} \cdots R_s)$, fixing strand $s$ at $q \to 1$ instead of transporting $s \to t-1$. We pre-register both `#9221`'s verbatim `M0` baseline and the corrected positive-braid transport $U_{s,t}(q_0) = (\check{R}_{t-2}\cdots\check{R}_s)^{-1} \check{R}_{t-1} (\check{R}_{t-2}\cdots\check{R}_s)$ (`M1`–`M4`).

---

## 2. Formalize-First Lean 4 Deliverables (`TetrahedralFluxRingAndMajoranaCluster.lean`)

Companion Lean 4 module:
`folio/quantum-observable-universe/lean/QOU/Nuclear/TetrahedralFluxRingAndMajoranaCluster.lean` (`0 sorry`, `0 axiom`, zero empirical literals, `§7c` generic `[CommRing R]` / ordered-field + `_real` bridge):

1. **Exact $K_A$ Simplex, Hamiltonian Cycle & Tait 3-Matching Theorems:**
   - Constructive `Finset` definitions and cardinality proofs for unoriented/oriented edges, triangles, and Hamiltonian 4-cycles on `Fin A` ($A = 1, 2, 3, 4$), tetrahedral boundary Euler characteristic $V - E + F = 4 - 6 + 4 = 2$, polynomial binomial identities over `[CommRing R]`, and bijective 12-quark $\leftrightarrow$ 12-half-edge Tait 3-matching on $K_4$.
2. **Constructive Wigner $\mathrm{SU}(4)$ Majorana Space-Exchange over `[CommRing R]`:**
   - Integer Pauli tensor swap identity $4 P_{ab}^{\sigma\tau} = (2 P_{ab}^\sigma)(2 P_{ab}^\tau)$ on `(Fin 2 × Fin 2)`, explicit antisymmetric spin-isospin tensors in `[1^A]_{\sigma\tau}` for $A = 2, 3, 4$, exact eigenvalue $P_{ab}^x = +1$ on every pair $a \neq b$, pair sum $\sum_{a < b} P_{ab}^x = \binom{A}{2}$, and exact Pauli shell closure ($\Lambda^5(\mathrm{Fin}\,4 \to R) = 0$) at $A = 5$.
3. **Exact 9-Quark & 12-Quark Colour-Reconnection Traces over `[CommRing R]` and `[Field K]`:**
   - Division-free over `[CommRing R]` (for any invertible `q * qinv = 1`) and bridged to `QOU.Braiding.JimboGl3Singlet` over `[Field K]`:
     - **9-quark 2-interface & cyclic 3-quark overlap:**
       $$\langle \varepsilon_q^{\otimes 3} \mid \check{R}_{3,4}(q)\,\check{R}_{6,7}(q) \mid \varepsilon_q^{\otimes 3} \rangle = \left(\frac{q^3}{[3]_q}\right)^2 \|\varepsilon_q\|^6,$$
     - **12-quark 3-interface & cyclic 4-quark overlap:**
       $$\langle \varepsilon_q^{\otimes 4} \mid \check{R}_{3,4}(q)\,\check{R}_{6,7}(q)\,\check{R}_{9,10}(q) \mid \varepsilon_q^{\otimes 4} \rangle = \left(\frac{q^3}{[3]_q}\right)^3 \|\varepsilon_q\|^8,$$
     - **Exact $3 \times 3$ cluster ring transfer matrix $M(q)$ rank-1 decomposition:**
       $$M(q) + q^{-3} I_3 = \begin{pmatrix} q \\ q^{-1} \\ q^{-3} \end{pmatrix} \begin{pmatrix} 1 & 1 & 1 \end{pmatrix}, \qquad \mathrm{spec}(M(q)) = \{[2]_q,\; -q^{-3},\; -q^{-3}\},$$
     - **Closed 9-quark triangular plaquette $\check{R}_{3,4}\check{R}_{6,7}\check{R}_{9,1}$ & connected colour-octet cumulant:**
       $$t_3^{\triangle}(q) = \frac{q^9 [2]_q^3 - 8}{[2]_q^3 [3]_q^3}, \qquad \kappa_3(q) = t_3^{\triangle}(q) - \left(\frac{q^3}{[3]_q}\right)^3 = -\frac{8}{[2]_q^3 [3]_q^3},$$
     - **Closed 12-quark tetrahedral 4-cycle $\check{R}_{3,4}\check{R}_{6,7}\check{R}_{9,10}\check{R}_{12,1}$ & connected colour-octet cumulant:**
       $$t_4^{\square}(q) = \frac{q^{12} [2]_q^4 + 8}{[2]_q^4 [3]_q^4}, \qquad \kappa_4(q) = t_4^{\square}(q) - \left(\frac{q^3}{[3]_q}\right)^4 = +\frac{8}{[2]_q^4 [3]_q^4}.$$

---

## 3. Pre-Registered Zero-Parameter Models ($A \in \{2, 3, 4\}$)

All microscopic models act on the exact Hoefsmit Specht module $S^{[A,A,A]}_{H_{3A}(q_0)}$ ($\dim = 5, 42, 462$) with `#9221`'s unperturbed central $\mathrm{SU}(3)_c$ Casimir gap Hamiltonian
$$H_0^{(A)}(q_0) = H_{\mathrm{G2}}^{(A)}(q_0) = \sum_{a=0}^{A-1} \frac{(\check{R}_{3a}\check{R}_{3a+1}\check{R}_{3a})^2 - q_0^{-6} I}{q_0 - q_0^{-1}},$$
and are converted to MeV via `#9221`'s harmonic-oscillator Compton scale $E_{\mathrm{osc}}(q_0) = \frac{m_e}{(q_0 - 1)^2}$ (with $E_0(q_0) = \frac{m_e}{q_0(q_0 - 1)}$ also reported in parallel). For strands $0 \le s < t < 3A$, let $U_{s,t}(q_0) = (\check{R}_{t-2}\cdots\check{R}_s)^{-1} \check{R}_{t-1} (\check{R}_{t-2}\cdots\check{R}_s)$, $\overline{U}_{s,t} = \frac{1}{2}(U_{s,t} + U_{s,t}^T)$, and $\mathcal{F}_{s,t} = \frac{1}{2}(\overline{U}_{s,t} - \langle T_{\mathrm{fac}}^{(A)} | \overline{U}_{s,t} | T_{\mathrm{fac}}^{(A)}\rangle I)$.

1. **`M0_w4_v2_baseline`:** Exact reproduction of `#9221`'s `G2_intra_casimir__V2_allpairs_fierz` as regression anchor.
2. **`M1_kA_2body_boundary`:** Corrected positive-braid transport 2-body $K_A$ Majorana-Fierz sum across all $\binom{A}{2}$ edges using boundary strands $(3a+2, 3b)$:
   $$V_{\mathrm{M1}}^{(A)}(q_0) = \sum_{0 \le a < b < A} P_{ab}^x \, \mathcal{F}_{3a+2,\, 3b}(q_0).$$
3. **`M2_kA_2body_tait_matched`:** 2-body $K_A$ Majorana-Fierz sum using the canonical Tait 3-edge-colouring strand assignment $\phi(a, b)$ pairing all $12$ quarks 1-to-1 with the $12$ half-edges of $K_4$ (`(0,1)->(2,3)`, `(1,2)->(5,6)`, `(2,3)->(8,9)`, `(0,2)->(1,7)`, `(1,3)->(4,10)`, `(0,3)->(0,11)`):
   $$V_{\mathrm{M2}}^{(A)}(q_0) = \sum_{0 \le a < b < A} P_{ab}^x \, \mathcal{F}_{\phi(a,b)}(q_0).$$
4. **`M3a_kA_plaquette_holonomy`:** $V_{\mathrm{M2}}^{(A)}(q_0)$ (and in parallel $V_{\mathrm{M1}}^{(A)}(q_0)$ as `M3a_bnd`) plus closed 3-interface triangular plaquette holonomies across all $\binom{A}{3}$ faces $\triangle = (a < b < c)$,
   $$W_{\triangle}(q_0) = U_{3a+2,3b}(q_0)\, U_{3b+2,3c}(q_0)\, U_{3c+2,3a}(q_0), \qquad \mathcal{P}_{\triangle} = \frac{1}{2}\bigl(\overline{W}_{\triangle} - \langle T_{\mathrm{fac}} | \overline{W}_{\triangle} | T_{\mathrm{fac}}\rangle I\bigr),$$
   with attractive colour-reconnection sign $-\mathcal{P}_{\triangle}$ vs $+\mathcal{P}_{\triangle}$ FIXED BEFOREHAND by the fundamental colour-Fierz convention: for 2-body, $+\mathcal{F}_{ab} = +\frac{1}{2}(\overline{U}_{ab} - t_2 I)$ has negative attractive eigenvalue $-\frac{[4]_{q_0}}{2[3]_{q_0}} < 0$; for 3-body and 4-body Wilson plaquettes, the Kogut–Susskind magnetic plaquette term is $-\frac{1}{2}(W_P + W_P^\dagger - 2\langle W_P\rangle I)$ (`-P_\triangle` and `-P_\square`), while the direct permutation-sum sign is `+P_\triangle` and `+P_\square` — we pre-register BOTH `+` (`M3a_pos`, direct braid holonomy addition) and `-` (`M3a_neg`, Kogut–Susskind Wilson plaquette sign) across the $\binom{A}{3} \in \{0, 1, 4\}$ triangles and $c_4(A) \in \{0, 0, 3\}$ unoriented Hamiltonian 4-cycles $W_{\square}(a,b,c,d) = U_{3a+2,3b} U_{3b+2,3c} U_{3c+2,3d} U_{3d+2,3a}$ without post-hoc selection!
5. **`M3b_kA_connected_fierz_ring`:** $V_{\mathrm{M2}}^{(A)}(q_0)$ plus the connected $q$-Fierz ring products $\sum_{\triangle} \mathrm{sym}(\mathcal{F}_{ab}\mathcal{F}_{bc}\mathcal{F}_{ca})_{\mathrm{cen}} + \sum_{\square} \mathrm{sym}(\mathcal{F}_{ab}\mathcal{F}_{bc}\mathcal{F}_{cd}\mathcal{F}_{da})_{\mathrm{cen}}$.
6. **`M4_kA_cyclic_quark_ring`:** $V_{\mathrm{M2}}^{(A)}(q_0)$ plus single-quark-per-cluster cyclic $3$-cycle braids $C_{\triangle} = U_{3a+2, 3b+2} U_{3b+2, 3c+2}$ ($\binom{A}{3}$ faces) and $4$-cycle braids $C_{\square} = U_{3a+2, 3b+2} U_{3b+2, 3c+2} U_{3c+2, 3d+2}$ ($c_4(A)$ 4-cycles), centered by $\frac{1}{2}(\overline{C} - \langle\overline{C}\rangle I)$ (both raw `+` and orthogonal-cumulant projected onto $k$-cluster hidden channels so 2-body edges are not double-counted).
7. **`M5_analytic_simplex_cumulant`:** Closed-form analytic cluster-simplex sum using exact `#9221` deuteron pair energy $b_2(q_0) = |E_-(A=2)| E_{\mathrm{osc}}(q_0)$ across $\binom{A}{2}$ Majorana bonds plus 2nd-order Bloch–Horowitz cyclic $3$- and $4$-cluster shifts $\binom{A}{3} \frac{v_3(q_0)^2}{3\Delta_8(q_0)} E_{\mathrm{osc}}(q_0) + c_4(A) \frac{v_4(q_0)^2}{4\Delta_8(q_0)} E_{\mathrm{osc}}(q_0)$.

---

## 4. Precision, Anti-Fit & Verdict Rules

- **Precision:** `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized), `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`), cross-checked symbolically in `sympy` over $\mathbb{Q}(q)$ for $6q$, $9q$, and $12q$ overlaps and transfer-matrix eigenvalues.
- **Zero float64:** `scripts/probe-float64-guard.py --strict` must pass with 0 violations.
- **Zero fitting:** Only CAL-1/2/3 (`m_e`, proton-pinned `q_0`) enter MeV unit readouts (`free_parameters = 0`). All pre-registered models (`M0`–`M5`) are reported verbatim against AME2020 / CODATA-2022 (`2.224566`, `8.481797` / `7.717990`, `28.295611 MeV`) in `RESULTS.md` with honest residuals and no post-hoc parameter tuning.
