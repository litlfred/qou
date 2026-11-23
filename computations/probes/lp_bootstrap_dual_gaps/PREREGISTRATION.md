# Pre-Registration: LP/SDP Bootstrap & Extremal-Functional Dual-Gap Closure Probe

## Scope & Anti-Fit Discipline

This pre-registration fixes all algebraic spaces, symmetry projections, conic positivity conditions, discrete candidate strata, precision parameters (`mpmath` `workdps = 80`, `q0Anchor = "proton"` via `q_parameter.q_at`, zero `float64`), and pass/refutation criteria **prior to** writing or executing `lp_bootstrap_dual_gaps_probe.py`. Zero empirical fitting and zero post-hoc candidate selection against PDG/AME targets are permitted; PDG `g_A = 1.2754(13)` (`codata_constants`) enters solely at the post-derivation comparison readout.

---

## Test 1: 64D Gamow–Teller Axial Coupling $g_A(q_0)$ (`hadron-half-life-verification.md` Open Item 3)

### Background & Target Gap
In `observations/hadron-half-life-verification.md` (Open Item 3) and `QOU/Archimedean/AxialCoupling.lean`, the axial-vector coupling $g_A(q_0) \approx 1.277$ previously relied on:
1. Importing the classical $SU(6)$ quark-model prefactor $5/3$ by hand, and
2. Selecting the arithmetic mean $\frac{1}{3}(h_{01} + h_{12} + h_{02})$ from three candidate colour pairings ($-23\%, -23\%, +46\%$ vs $+0.1\%$).

### Pre-Registered Algebraic & Conic-Positivity Tests on $(\mathbb{C}^3_{\mathrm{col}} \otimes \mathbb{C}^2_{\mathrm{iso}} \otimes \mathbb{C}^2_{\mathrm{spin}})^{\otimes 3}$

We test whether combining **quantum skew-Howe colour-singlet invariance** (`QOU.Braiding.ColourFlavourMirror.singlet_exterior_iff`, PR `#9130`) with **Verstichel–van Aggelen $(D,Q)$ particle-hole positivity / NPA trace Gram positivity** uniquely selects a canonical $(g_A^{\mathrm{diag}}, g_A^{\mathrm{cross}})$ weighting without candidate-shopping:

1. **Elimination of the 3-colour-pairing freedom (`#9130` Skew-Howe Singlet Slice):**
   On the $3^3 \times 64 = 1728$-dimensional 3-quark state space, the $U_q(\mathfrak{gl}_3)$ colour singlet $\varepsilon_q \in \Lambda^3_q(\mathbb{C}^3_{\mathrm{col}})$ is 1-dimensional (`pure_eps_inj`), and total $q$-exterior fermionic antisymmetry $X_{12}|\Psi\rangle = X_{23}|\Psi\rangle = -|\Psi\rangle$ holds on $|\Psi\rangle = \varepsilon_q \otimes |f\rangle$ **if and only if** the 64D spin–isospin tensor $|f\rangle \in (\mathbb{C}^2_{\mathrm{iso}} \otimes \mathbb{C}^2_{\mathrm{spin}})^{\otimes 3}$ satisfies the $q$-symmetric Hecke eigenrelations $B_1^{\mathrm{SI}}|f\rangle = q|f\rangle$ and $B_2^{\mathrm{SI}}|f\rangle = q|f\rangle$. Because $\Lambda^3_q(\mathbb{C}^3_{\mathrm{col}})$ is 1-dimensional, any colour-singlet Gamow–Teller operator $1_{\mathrm{col}} \otimes \mathcal{O}_{\mathrm{GT}}$ factors out $\langle \varepsilon_q | \varepsilon_q \rangle$ identically, leaving **zero** free colour-pairing candidates.

2. **Closed 2-Branch Test of $B_i^{\mathrm{SI}}$ on the 9D $(uud, \uparrow\uparrow\downarrow)$ Sector of the 64D Space:**
   Within the 9-dimensional $(I_3 = \pm 1/2, S_z = +1/2)$ weight sector of $(\mathbb{C}^2_{\mathrm{iso}} \otimes \mathbb{C}^2_{\mathrm{spin}})^{\otimes 3}$, where $\mathcal{O}_{\mathrm{GT}} = \sum_{a=1}^3 \Delta^{(3)}_a(E_{\mathrm{iso}}) \otimes \sigma_z^{(a)}$, we test both canonical parameter-free realisations of the spin–isospin braiding + positivity cone:
   - **Arm 1A (Full $U_q(\mathfrak{gl}_4)$ Skew-Howe Symmetric Cube $\mathrm{Sym}^3_q(\mathbb{C}^4)$):**
     Construct the exact $16 \times 16$ Jimbo $\check{R}^{(4)}(q)$ matrix on $\mathbb{C}^4 \otimes \mathbb{C}^4$ ordered lexicographically on $\{(u\uparrow), (u\downarrow), (d\uparrow), (d\downarrow)\}$, restrict $\check{R}^{(4)}_{12}(q) - q I_{64}$ and $\check{R}^{(4)}_{23}(q) - q I_{64}$ to the 9D $(uud, \uparrow\uparrow\downarrow)$ weight space, intersect with the highest-weight kernels $\ker \Delta^{(3)}(E_{\mathrm{iso}}) \cap \ker \Delta^{(3)}(E_{\mathrm{spin}})$, and measure:
     (i) whether the intersection has exact dimension $1$ over $\mathbb{Q}(q)$, and
     (ii) the exact symbolic rational function $g_A^{\mathrm{gl4}}(q) = \langle p_\uparrow^{\mathrm{gl4}}(q) | \mathcal{O}_{\mathrm{GT}}(q) | n_\uparrow^{\mathrm{gl4}}(q) \rangle / (\|p_\uparrow^{\mathrm{gl4}}\| \|n_\uparrow^{\mathrm{gl4}}\|)$ and its 80-dps value at $q_0$.
   - **Arm 1B (Factorised $U_q(\mathfrak{sl}_2)_{\mathrm{iso}} \times U_q(\mathfrak{sl}_2)_{\mathrm{spin}}$ Doublet + $(D,Q)$ Gram Positivity SDP):**
     On the 2D $(I = 1/2, S = 1/2)$ doublet $\mathrm{span}\{|\Phi_+(q)\rangle, |\Phi_-(q)\rangle\}$ (`WeakCoevaluationAndNeutronLifetimeBridge`), any Hermitian reduced 1-state Gram matrix $\Gamma = \begin{pmatrix} p_+ & c/2 \\ c/2 & p_- \end{pmatrix}$ satisfying Verstichel–van Aggelen $(D,Q)$ positivity ($0 \preceq \Gamma \preceq I_2$, $\mathrm{tr}\,\Gamma = 1$) and $S_3$-exchange symmetry ($p_+ = p_- = 1/2$) is parameterised by a single cross-coherence $c \in [-1, 1]$, yielding
     $$g_A(\Gamma; q) = g_A^{\mathrm{diag}}(q) + c \cdot g_A^{\mathrm{cross}}(q),$$
     with $g_A^{\mathrm{diag}}(q) = \frac{q^8 + 3q^6 + 10q^4 + 3q^2 + 1}{2(q^4+q^2+1)^2}$ and $g_A^{\mathrm{cross}}(q) = \frac{(q^2+1)^2}{2(q^4+q^2+1)}$.
     We test:
     - **Pure-state rank-1 $(D,Q)$ extreme point + $q \to 1$ symmetric continuity ($c = +1$):** uniquely selects $(w_{\mathrm{diag}}, w_{\mathrm{cross}}) = (1, 1)$, giving $g_A^{\mathrm{SW}}(q_0)$ with classical limit $5/3$ derived (not imported).
     - **Centralizer-decohered $(D,Q)$ midpoint ($c = 0$, projection onto $Z(H_3)$ block diagonal):** uniquely selects $(w_{\mathrm{diag}}, w_{\mathrm{cross}}) = (1, 0)$, giving $g_A^{\mathrm{diag}}(q_0)$.
     - **Feasible $(D,Q)$ SDP interval $[g_A^{\mathrm{diag}}(q_0) - g_A^{\mathrm{cross}}(q_0),\; g_A^{\mathrm{diag}}(q_0) + g_A^{\mathrm{cross}}(q_0)]$:** test whether PDG $g_A = 1.2754(13)$ lies strictly inside the $(D,Q)$-positive interval ($c_{\mathrm{req}} \in (0, 1)$), and test whether any parameter-free Convention-D centralizer trace weight ($w_{(3)}(z_D) = \frac{q^4+1}{(q^2+1)^2}$ or $2 w_{(2,1)}(z_D) = \frac{2q^2}{(q^2+1)^2}$) reproduces $c_{\mathrm{req}}$ or leaves a quantified QCD/axial-current renormalisation residual.

3. **Honest Outcome Classification:**
   - Record exact 80-dps values and relative residuals `(computed - PDG) / PDG` for Arm 1A (`g_A^{gl4}(q_0)`), Arm 1B pure (`g_A^{SW}(q_0)`), Arm 1B decohered (`g_A^{diag}(q_0)`), and the Convention-D centralizer trace-weighted state (`c = 2 w_{(2,1)}(z_D)` and `c = w_{(3)}(z_D)`), with **zero promotion to production** unless uniquely forced by proved symmetry + positivity axioms alone.

---

## Test 2: Extremal-Functional Strict Dual-Slack Uniqueness on Discrete Strata (`SymmetryReducedDualCertificate`)

### Mathematical Criterion (`unique_support_of_strict_dual_slack`)
For a standard-form LP $\min \{ \langle c, x \rangle : A x = b,\; x \ge 0 \}$ and dual feasible multiplier $u^*$ with $A^T u^* \le c$ and zero duality gap $\langle b, u^* \rangle = \langle c, x^* \rangle$:
- Every index $i$ with strictly positive dual slack $s_i = c_i - (A^T u^*)_i > 0$ is certified to satisfy $x_i = 0$ in **every** optimal primal solution (`unique_support_of_strict_dual_slack`).
- On a simplex normalization $\sum_{i=1}^n x_i = 1$, $u_0^* = \min_i c_i$; the optimal primal solution is **algebraically unique** ($|S| = 1$) if and only if $s_i = c_i - u_0^* > 0$ for all $i \neq i^*$. When $|S| > 1$, strict dual slacks isolate the exact symmetry-degenerate optimal face $S = \{i : s_i = 0\}$.

### Pre-Registered Strata (80-dps `mpmath`, `q0Anchor = "proton"`, Convention D $z_D = q_0^3/(q_0^2+1)$)

1. **Stratum 2A (${}^4\mathrm{He}$ $A=4, Z=2, N=2$ Nucleon-Arrangement LP across all $\binom{4}{2} = 6$ Permutations):**
   Evaluate the exact Convention-D transfer-action objective (`ground_state_ordering_argmin_sweep.py` closed form at 80 dps) on all $6$ arrangements $\{ppnn, pnnp, pnpn, npnp, nppn, nnpp\}$ for:
   - **2A-i (Bare nuclear $\Phi_{\mathrm{nuc}}$):** measure $u_0^* = \min_i \Phi_{\mathrm{nuc}}(w_i)$, the active zero-slack face $S_{\mathrm{nuc}} = \{i : s_i = 0\}$, and the minimum nonzero dual slack $\min_{i \notin S_{\mathrm{nuc}}} s_i$. Test whether reversal symmetry produces a 2-element zero-slack face ($|S_{\mathrm{nuc}}| > 1$) or a singleton ($|S_{\mathrm{nuc}}| = 1$).
   - **2A-ii (Full atomic $\Phi_1$ with $1s^2$ electron tail `ee` appended):** measure $u_0^* = \min_i \Phi_1(w_i + ee)$, the active face $S_{\mathrm{atom}}$, and $\min_{i \notin S_{\mathrm{atom}}} s_i$. Test whether appending the chiral $ee$ tail breaks any nuclear mirror tie down to a **singleton** optimal vertex ($|S_{\mathrm{atom}}| = 1$) with strictly positive dual slacks $s_i > 0$ on all $5$ suboptimal arrangements!

2. **Stratum 2B (Meson $q$-Integer Fusion Stratum $a + b = 7$, $1 \le a \le b$ for $m_K^2/m_\pi^2$):**
   Under topological crossing-sum conservation $a + b = 7$ (`T(2,3)` + `T(2,5)` $\to 3 + 4 = 7$, integer partitions $(a,b) \in \{(1,6), (2,5), (3,4)\}$), test the internal parameter-free quadratic Casimir-imbalance LP
   $$\min_{x \ge 0,\; \sum x_i = 1} \sum_{i \in \{(1,6),(2,5),(3,4)\}} \bigl([b_i]_{q_0} - [a_i]_{q_0}\bigr)^2 x_i$$
   (and dually $\max \sum [a_i]_{q_0}[b_i]_{q_0} x_i$, since $[a]_q [b]_q = \frac{q^{a+b} + q^{-(a+b)} - (q^{b-a} + q^{-(b-a)})}{(q - q^{-1})^2}$ strictly increases as $|b - a|$ decreases!). Verify algebraically and at 80 dps that $(3,4)$ (`[3]_q [4]_q`) is the **unique** primal optimizer ($|S| = 1$) of both minimum Casimir imbalance and maximum product $[a]_q [7-a]_q$ over $a + b = 7$, with strictly positive dual slacks $s_{(2,5)} > 0$ and $s_{(1,6)} > 0$.
