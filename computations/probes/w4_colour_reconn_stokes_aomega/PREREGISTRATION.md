# Pre-Registration: Many-Body $6q\text{–}12q$ Colour-Reconnection Nuclear Carrier & $\Delta_\lambda$ Bloch–Wigner / GGM Stokes Constant $A_\omega = 3$ (2026-11-23)

Beans `qou-v2om`, `qou-0c19`, `qou-gpb5`, `qou-3q7t` (Workstream W4, session `qou-y5pi`).
Written and committed **before** running any numerical evaluation of $6q/9q/12q$ colour-reconnection overlaps, Schur-complement shifts, MeV comparisons, or 80-dps Stokes evaluations.

---

## 1. Context & Formalize-First Backing (`ColourReconnectionStokesAssembly.lean`)

Existing results on `main` narrow the light-nuclei ($A \in \{2, 3, 4\}$) binding gap to two concrete questions:

1. **Single-$\gamma\gamma$ chain & character-ratio exclusions (`LightNucleiGGChainSign.lean`, `qou-gpb5`, `qou-3q7t`):**
   - Under Reading A, the factorized single-$\gamma\gamma$ chain on production nucleon blocks unbinds at every $q > 1$ (`LightNucleiGGChainSign.chain_unbinds`, bond tails $O(h^4), O(h^5)$).
   - The multi-level character ratio (`qou-gpb5`) telescopes to an intra-ordering-dependent trace at two levels and hits the retired all-pairs ordering / non-Markov weight obstruction at the third (nuclear-jet) level.
   - Per-partition $\Delta_\lambda = (-1)^{n(\lambda)} \dim V_\lambda$ is proved unconditionally, while the $\ell^1$-ceiling (`DeltaLambdaL1Ceiling.lean`) and conditioning analysis (`qou-3q7t`, Convention-D $C_{\mathrm{knot}}(\mathrm{D}/\mathrm{T}/{}^3\mathrm{He}/{}^4\mathrm{He}) = 6.0679 / 6.7061 / 4.9054 / 290.007$ vs legacy Convention-C $5.85$) establish that closing light-nuclei binding requires a genuine **inter-nucleon hidden-colour / many-body carrier** outside factorized colour-singlet blocks (`qou-v2om`, `qou-0c19`).
2. **Algebraic origin of $A_\omega = 3$ in $\Delta_\lambda$ T5 assembly (`DeltaLambdaBindingAssembly.lean`, `StokesSymmetryConstant.lean`):**
   - `S_K(q_0) = A_\omega \cdot (\sqrt{3}/4) \cdot (\ln^2 q_0 - \vartheta_K^2)` carries $A_\omega = 3$ as an open input; `StokesSymmetryConstant` proves $(S^+_{12} + S^+_{21}) / S^+_{11} = c$ is $q$-independent *given* the linear relation $S^+_{12} + S^+_{21} = c \, S^+_{11}$, leaving open the algebraic proof of why $c = 3$ from the $4_1$ gluing / Wronskian / $A$-polynomial data.

Companion Lean 4 module:
`folio/quantum-observable-universe/lean/QOU/Nuclear/ColourReconnectionStokesAssembly.lean` (`0 sorry`, `0 axiom`, §7c generic).

---

## 2. Pre-Registered Exact Models & Observables (Zero Free Parameters)

### Part A — Figure-Eight ($4_1$) Eisenstein Cusp Lattice, Degree-3 $A$-Polynomial & GGM $A_\omega = 3$

1. **Eisenstein $\mathbb{Z}[\omega]$ & 3 Flat-Connection Saddles:**
   - Verify $\omega = e^{i\pi/3}$ satisfies $1 - \omega + \omega^2 = 0$, $\omega^3 = -1$, $\omega^6 = 1$, $(2\omega - 1)^2 = -3$, tetrahedral cross-ratio self-consistency $\omega(1 - \omega) = 1$, SnapPy's two cleared gluing equations, and pairwise distinctness of the 3 roots $\{-1, \omega, 1 - \omega\}$ of $(X + 1)(X^2 - X + 1) = X^3 + 1 = 0$ corresponding to $(\rho_{\mathrm{triv}}, \rho_{\mathrm{geom}}, \rho_{\overline{\mathrm{geom}}})$.
2. **$A$-Polynomial Degree-3 $L$-Specialization & Neumann–Zagier Cusp Jet:**
   - Verify both CCGLS (`A_CCGLS(1, L) = (L - 1)(L + 1)^2`) and Garoufalidis–Kashaev AJ (`A_AJ(1, L) = (L - 1)^3`) forms have exact $L$-degree $3$ (matching the order-3 $q$-difference state-integral recursion).
   - Verify the exact algebraic identity $\delta_Y = -3\delta_X - \delta_X^2$ ($X = M^2 + M^{-2} = 2 + \delta_X$, $Y = -(L_{\mathrm{CCGLS}} + L_{\mathrm{CCGLS}}^{-1}) = 2 + \delta_Y$) and 80-dps Cauchy contour extraction of $\tau = -i\sqrt{3}$ ($\tau^2 = -3$) and $v_3 = -i\sqrt{3}/3$ ($3 v_3 = \tau$, $\tau v_3 = -1$).
3. **GGM Wronskian Sandwich Proof of $A_\omega = 3$ & $\Delta_\lambda$ T5 Check:**
   - Certify over exact $\mathbb{Z}[[q]]$ through $q^{40}$ and at substrate $q_{\mathrm{sub}} = q_0^{-1}$ (`ORD_SUB = 1600`, 80 dps) that $S^+(q) = \frac{1}{2} A_{\mathrm{GGM}} W_{-1}(q) B_{\mathrm{GGM}} W_{-1}(q)^T C_{\mathrm{GGM}}$ with $A_{\mathrm{GGM}} = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$, $B_{\mathrm{GGM}} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $C_{\mathrm{GGM}} = \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix}$ satisfies $\det S^+(q) = 1$, $S^+_{12}(q) + S^+_{21}(q) = 3 S^+_{11}(q)$ identically, and $S^+(0) = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$.
   - Evaluate the T5 pure-boost cap $A_\omega (\sqrt{3}/4) (\ln q_0)^2$ at $A_\omega = 3$ against $S_\mu = +0.00968298$ and $S_p = -0.03945936$ (diagnostic comparison only; $\vartheta_K$ is not fitted to binding).

### Part B — $6q / 9q / 12q$ $\mathcal{U}_q(\mathfrak{sl}_3)$ Colour-Reconnection & Bloch–Horowitz Schur-Complement Shifts

For $A \in \{1, 2, 3, 4\}$ ($3A \in \{3, 6, 9, 12\}$ quarks in $\mathbb{C}^3_{\mathrm{col}}$), the $\mathcal{U}_q(\mathfrak{sl}_3)$-singlet space $\operatorname{Inv}_{\mathcal{U}_q(\mathfrak{sl}_3)}((\mathbb{C}^3)^{\otimes 3A})$ is isomorphic by skew-Howe / Schur–Weyl duality to the Hoefsmit Specht module $S^{[A,A,A]}_{H_{3A}(q_0)}$ of exact dimension:
$$d_{\mathrm{sing}}(A) = \frac{2\,(3A)!}{A!\,(A+1)!\,(A+2)!} \in \{1,\; 5,\; 42,\; 462\}, \qquad d_{\mathrm{hid}}(A) = d_{\mathrm{sing}}(A) - 1 \in \{0,\; 4,\; 41,\; 461\}.$$
Inside $S^{[A,A,A]}_{H_{3A}(q_0)}$, there is a **unique** column-factorized standard Young tableau $T_{\mathrm{fac}}^{(A)}$ (with $\{3k+1, 3k+2, 3k+3\}$ in column $k$ for each $k \in \{0, \dots, A-1\}$) representing the factorized $A$-nucleon singlet $|\mathbf{1}^A\rangle_{q_0}$; the remaining $d_{\mathrm{hid}}(A)$ standard Young tableaux form an orthonormal hidden-colour basis $\mathcal{H}_{\mathrm{hid}}^{(A)}$.

We pre-register two zero-parameter unperturbed intra-nucleon colour-gap Hamiltonians $H_0^{(A)}(q_0)$ on $S^{[A,A,A]}_{H_{3A}(q_0)}$ (both manifestly real-symmetric in Hoefsmit's orthonormal basis, satisfying $H_0^{(A)} |T_{\mathrm{fac}}^{(A)}\rangle = 0$ and $H_0^{(A)}|_{\mathcal{H}_{\mathrm{hid}}} \succ 0$):
- **Gap G1 (`intra_generator_sum`):** Symmetric intra-nucleon adjacent-generator defect
  $$H_{\mathrm{G1}}^{(A)}(q_0) = \sum_{k=0}^{A-1} \bigl(\check{R}_{3k}(q_0) + \check{R}_{3k+1}(q_0) + 2 q_0^{-1} I\bigr),$$
  which vanishes on $[1^3]$ ($\check{R}_{3k} = \check{R}_{3k+1} = -q_0^{-1}$) and has strictly positive eigenvalues on $[2,1]$ ($\mathbf{8}_c$, classical limit $\{1, 3\}$) and on $[3]$ ($\mathbf{10}_c$, classical limit $4$).
- **Gap G2 (`intra_full_twist_casimir`, central $\mathrm{SU}(3)_c$ Casimir):** Exact central intra-nucleon ribbon full-twist gap normalized to $C_2(\mathbf{8}_c) - C_2(\mathbf{1}_c) = 3$ at $q_0 \to 1$:
  $$H_{\mathrm{G2}}^{(A)}(q_0) = \sum_{k=0}^{A-1} \frac{(\check{R}_{3k}\check{R}_{3k+1}\check{R}_{3k})^2 - q_0^{-6} I}{q_0 - q_0^{-1}}.$$
  Because $(\check{R}_{3k}\check{R}_{3k+1}\check{R}_{3k})^2$ is central in $H_3^{(k)}(q_0)$, it acts as $q_0^{-6}$ on $\mathbf{1}_c$ ($[1^3]$), $1$ on $\mathbf{8}_c$ ($[2,1]$, giving gap $\frac{1 - q_0^{-6}}{q_0 - q_0^{-1}} = q_0^{-3}[3]_{q_0} > 0$, classical limit $3$), and $q_0^6$ on $\mathbf{10}_c$ ($[3]$, giving gap $\frac{q_0^6 - q_0^{-6}}{q_0 - q_0^{-1}} = [6]_{q_0} > 0$, classical limit $6$).

And we pre-register three zero-parameter inter-nucleon colour-reconnection coupling operators $V_{\mathrm{inter}}^{(A)}(q_0)$ on $S^{[A,A,A]}_{H_{3A}(q_0)}$:
- **Coupling V1 (`chain_fierz_single_crossing`):** Adjacent-interface $q$-Fierz colour-exchange sum over the $A - 1$ chain interfaces $b_k = 3k + 2$:
  $$V_{\mathrm{V1}}^{(A)}(q_0) = \sum_{k=0}^{A-2} \frac{1}{2}\left(\check{R}_{3k+2}(q_0) - \frac{q_0^3}{[3]_{q_0}} I\right).$$
- **Coupling V2 (`allpairs_fierz_complete_graph`):** Symmetrized $\binom{A}{2}$ complete-graph ($K_A$) quark-pair exchange sum across all nucleon pairs $0 \le a < b < A$ (transporting strand $3a+2$ to $3b - 1$ via positive braid conjugation $\tau_{a,b} \check{R}_{3b-1}(q_0) \tau_{a,b}^{-1}$ and symmetrizing $\frac{1}{2}(M + M^T)$).
- **Coupling V3 (`chain_gg_bond_v3`):** Adjacent-interface $\gamma\gamma$ bond operator $V_{\mathrm{gg}, k} = \frac{1}{2}((\check{R}_{3k+2} \check{R}_{3k+3}^{-1})^3 + \text{h.c.})$ minus its $|T_{\mathrm{fac}}^{(A)}\rangle$ diagonal expectation, testing directly whether hidden-colour reconnection rescues the $\gamma\gamma$ bond from `LightNucleiGGChainSign`'s factorized unbinding!

For each pair $(H_0, V_{\mathrm{inter}})$ and $A \in \{2, 3, 4\}$, we compute **without any tunable parameter**:
1. Second-order Bloch–Horowitz / Schur-complement ground-energy lowering:
   $$\Delta \mathcal{E}_{\mathrm{BH}}^{(2)}(A; q_0) = -\langle T_{\mathrm{fac}}^{(A)} | V_{\mathrm{inter}} Q_{\mathrm{hid}} \bigl(Q_{\mathrm{hid}} H_0 Q_{\mathrm{hid}}\bigr)^{-1} Q_{\mathrm{hid}} V_{\mathrm{inter}} | T_{\mathrm{fac}}^{(A)} \rangle < 0,$$
2. Exact coupled ground eigenvalue $E_-(H_0 + V_{\mathrm{inter}})$ on $S^{[A,A,A]}_{H_{3A}(q_0)}$ ($5\times 5$, $42\times 42$, $462\times 462$), verifying the proved Lean theorem $E_- < 0$ and the $O(v^4)$ Schur-complement remainder!
3. Dimensionless scaling ratios $|\Delta \mathcal{E}(A)| / |\Delta \mathcal{E}(2)|$ for $A = (2, 3, 4)$ compared against $(A - 1) = (1, 2, 3)$, $\binom{A}{2} = (1, 3, 6)$, and empirical AME2020 ratios $B_{\mathrm{AME}}(A) / B_{\mathrm{AME}}(2) = (1.0000, 3.8128, 3.4695, 12.7196)$, plus absolute energy-scale readouts in both W6 charts ($E_0(q_0) = m_e / (q_0(q_0 - 1))$ and $E_{\mathrm{osc}}(q_0) = m_e / (q_0 - 1)^2$) and Convention-D vs Convention-C $C_{\mathrm{knot}}$ conditioning diagnostics (`qou-3q7t`).

---

## 3. Precision, Anti-Fit & Verdict Rules

- **Precision:** `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized), `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`), cross-checked against exact `sympy` rational identities over $\mathbb{Q}(q)$.
- **Zero float64:** Strict compliance with `scripts/probe-float64-guard.py --strict`.
- **Zero fitting:** Only CAL-1/2/3 (`m_e`, proton-pinned `q_0`) enter unit conversions. Every pre-registered $(H_0, V_{\mathrm{inter}})$ model is reported verbatim — whether it undershoots, overshoots, or misses the $\alpha$-cluster ratio — with no post-hoc rescaling or model selection.
