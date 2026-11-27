# Pre-Registration: Closing Open Gap 3 (Option 3A Primary) — Why $N_{\mathrm{gen}} = 3$ Fermion Generations via Riemann–Roch + Chevalley–Weil Zero-Mode Count on Bring's Curve Twisted by the $\mathbb{Z}_3$ Colour Kummer Line Bundle

- **Branch**: `claude/gap3-ngen3-bring-prym-riemann-roch-20261123`
- **Base commit**: `origin/main` (`e330ab6aa048abefe34a93474f667f3284483d71`)
- **Target gap**: Open Gap 3 (`sm-open-problems.md` item 18 — *"Three-generation structure (why three copies of each fermion?)"*, Option 3A Primary)
- **Companion Lean 4 module**: `folio/quantum-observable-universe/lean/QOU/StandardModel/BringPrymRiemannRochGenerations.lean`
- **Companion exact/80-dps probe**: `computations/probes/gap3_ngen3_bring_prym_riemann_roch/gap3_ngen3_bring_prym_riemann_roch_probe.py`
- **Precision & anti-fit discipline**: Exact symbolic (`sympy` / `fractions.Fraction` / $\mathbb{F}_3[S_5]$ exact linear algebra) + `mpmath` at `work_dps = 80` (`q0Anchor = "proton"`, `q_at(80)`), zero `float64`, zero adjustable parameters (`CAL-1/2/3` untouched; zero empirical literals in `.lean`).

---

## 1. Scientific Question & Mathematical Honesty Mandate

On Bring's smooth projective curve $\mathcal{B} = \{p_1 = p_2 = p_3 = 0\} \subset \mathbb{P}^4$ of genus $g(\mathcal{B}) = 4$ ($\chi_{\mathrm{eu}}(\mathcal{B}) = 2 - 2g = -6$, $\mathrm{Aut}(\mathcal{B}) \cong S_5$), canonical differentials have dimension $h^0(\mathcal{B}, K_{\mathcal{B}}) = g = 4$ (`V_{(4,1)}`), whereas observed chiral Standard Model matter has $N_{\mathrm{gen}} = 3$ families. Prior corpus filters (`BringGenerationSplitAndCKMTexture.lean`) recorded that torus-knot genus/harmonic/$S_5$-equivariance filters on $\mathcal{B}$ return disagreeing counts $\{4, 3, 2\}$.

This investigation tests—with complete mathematical honesty and zero handwaving—whether coupling internal fermions on $\mathcal{B}$ to a non-trivial $\mathbb{Z}_3$ colour Kummer line bundle $\mathcal{L}$ derives $N_{\mathrm{gen}} = 3$ via Riemann–Roch, Serre duality, and Chevalley–Weil, and compares **both** candidate geometric interpretations:

1. **Case I (Ascending Unramified Torsion / Prym–Kummer Cover $\pi : \tilde{\mathcal{B}} \to \mathcal{B}$, $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3] \setminus \{\mathcal{O}_{\mathcal{B}}\}$)**:
   - Does every non-trivial $3$-torsion line bundle $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3] \setminus \{\mathcal{O}_{\mathcal{B}}\}$ yield exact zero-mode counts $(h^0, h^1) = (3, 0)$ in both non-trivial $\mathbb{Z}_3$-triality sectors ($\mathcal{L}, \mathcal{L}^2$) and $(h^0, h^1) = (4, 1)$ in the trivial sector ($\mathcal{O}_{\mathcal{B}}$), summing to $\tilde{g} = 4 + 3 + 3 = 10$?
   - Does placing the $\mathbb{Z}_3$ Kummer holonomy in the **centre** $Z(\mathrm{SU}(3)_c) = \mu_3 \subset \mathrm{SU}(3)_c$ ($\mathcal{W}_3 = \mathbb{C}^3 \otimes \mathcal{L}$, $\det \mathcal{W}_3 \cong \mathcal{O}_{\mathcal{B}}$) preserve unbroken $\mathrm{SU}(3)_c$ gauge symmetry—unlike the non-central split bundle $\mathcal{O}_{\mathcal{B}} \oplus \mathcal{L} \oplus \mathcal{L}^2$ which breaks $\mathrm{SU}(3)_c \to \mathrm{U}(1)^2$ and assigns asymmetric $(4,3,3)$ counts across $(r,g,b)$?
   - What happens to the colour-singlet lepton sector ($t = 0$), where $h^0(\mathcal{B}, K_{\mathcal{B}}) = 4$ and $h^1(\mathcal{B}, K_{\mathcal{B}}) = 1$: what is forced by 4D gauge/gravitational anomaly cancellation on $\Lambda^1 F \oplus \Lambda^2 F^*$ ($2 y_2 + 3 y_3 = 0$), what is forced by $\mathbb{F}_3[S_5]$ symmetry breaking of $\mathrm{Stab}_{S_5}(\mathcal{L})$, and what remains a genuine dynamical/topological hypothesis?
2. **Case II (Descending Degree-3 Covers $\pi : \Sigma_4 \to \mathcal{B}_0$ from Genus $4$, $\chi_{\mathrm{eu}}(\Sigma_4) = -6$)**:
   - Can *any* descending cyclic $\mathbb{Z}_3$ Galois quotient of a genus-$4$ curve ($\mathcal{B} \to \mathcal{C}_2$ unramified over $g_0 = 2$, $\Sigma_4 \to E$ branched at $3$ points over $g_0 = 1$, or $\Sigma_4 \to \mathbb{P}^1$ branched at $6$ points over $g_0 = 0$) yield $3$ zero modes in both conjugate $\mathbb{Z}_3$-sectors?

---

## 2. Pre-Registered Exact Claims to Test & Formalize

### A. §1 — Divisor Positivity, Twisted Canonical Riemann–Roch, Spinor Contrast, & Prym $10 = 4 + 3 + 3$ Split
1. **Effective Degree-$0$ Divisor Vanishing**: Over any finite support, an effective divisor ($D(P) \ge 0$) of degree $\sum_P D(P) = 0$ vanishes identically ($D = 0$), forcing $h^0(\mathcal{B}, \mathcal{M}) = 0$ for every non-trivial degree-$0$ line bundle $\mathcal{M} \not\cong \mathcal{O}_{\mathcal{B}}$.
2. **Serre Duality + Riemann–Roch on Genus $g = 4$**:
   - For any $3$-torsion class $L \in \mathrm{Pic}(\mathcal{B})$ with $3 L = 0$ and $L \ne 0$: $\deg L = 0$, $\deg(2L) = 0$, and $2L \ne 0$ follow algebraically without extra hypotheses.
   - Untwisted sector ($t = 0$): $h^0(K_{\mathcal{B}}) = 4$, $h^1(K_{\mathcal{B}}) = 1$, net Dolbeault index $h^0 - h^1 = 3$.
   - Twisted triality-$1$ and triality-$2$ sectors ($t = 1, 2$): $h^0(K_{\mathcal{B}} + L) = 3$, $h^1(K_{\mathcal{B}} + L) = 0$, and $h^0(K_{\mathcal{B}} + 2L) = 3$, $h^1(K_{\mathcal{B}} + 2L) = 0$, net index $3 - 0 = 3$.
   - Étale Kummer cover $\tilde{\mathcal{B}} \to \mathcal{B}$: Riemann–Hurwitz gives $\tilde{g} = 10$ ($\chi_{\mathrm{eu}}(\tilde{\mathcal{B}}) = -18$), matching $h^0(\tilde{\mathcal{B}}, K_{\tilde{\mathcal{B}}}) = 4 + 3 + 3 = 10$ and $\dim \mathrm{Prym}(\tilde{\mathcal{B}}/\mathcal{B}) = 3 + 3 = 6$.
3. **Honest Spin-Bundle Contrast**: For an untwisted theta characteristic / spinor bundle $S$ with $2 S = K_{\mathcal{B}}$ ($\deg S = g - 1 = 3$), Riemann–Roch gives $h^0(S + L) - h^1(S + L) = 0$ for every degree-$0$ $L$. Thus nonzero chiral generation index on $\mathcal{B}$ specifically requires the canonical / Spin$^c$ Euler-flux twist $K_{\mathcal{B}} = S \otimes K_{\mathcal{B}}^{1/2}$ ($\deg K_{\mathcal{B}} = 6$).

### B. §2 — Complete Classification & No-Go for Descending Degree-3 Covers from Genus $4$
1. **Diophantine Hurwitz Classification**: $2(4) - 2 = 3(2g_0 - 2) + 2r \iff 3g_0 + r = 6$ in $\mathbb{N}^2$ has **exactly three** solutions: $(g_0, r) \in \{(2, 0), (1, 3), (0, 6)\}$.
2. **Chevalley–Weil Eigenspace Census**:
   - $(g_0, r) = (2, 0)$ (Bring's unique free $C_3 \subset S_5$ quotient $\mathcal{B} \to \mathcal{C}_2$): $(d_0, d_1, d_2) = (2, 1, 1)$.
   - $(g_0, r) = (1, 3)$ with $a_1 + a_2 + a_3 \equiv 0 \pmod 3$, $a_j \in \{1, 2\}$: $(d_0, d_1, d_2) \in \{(1, 2, 1), (1, 1, 2)\}$ (and obstructed on $\mathcal{B}$ since all $20$ order-$3$ elements of $S_5$ act freely).
   - $(g_0, r) = (0, 6)$ with $\sum_{j=1}^6 a_j \equiv 0 \pmod 3$, $a_j \in \{1, 2\}$: $(d_0, d_1, d_2) \in \{(0, 1, 3), (0, 2, 2), (0, 3, 1)\}$ (also obstructed as a Galois $\mathbb{Z}_3$-quotient of $\mathcal{B}$).
   - **Theorem**: No descending cyclic $\mathbb{Z}_3$-cover of a genus-$4$ curve can ever achieve $(d_1, d_2) = (3, 3)$ (since $d_0 + d_1 + d_2 = 4 < 6$).

### C. §3 — Exact $S_5$ Normalizer of $C_3$ & $\mathbb{F}_3[S_5]$ Torsion Action on $\mathrm{Pic}^0(\mathcal{B})[3]$
1. **Subgroup Structure in $S_5 = \mathrm{Perm}(\mathrm{Fin}\ 5)$**: For $C_3 = \langle(0\,1\,2)\rangle$, $|C_{S_5}(C_3)| = 6$ ($C_3 \times S_2$) and $|N_{S_5}(C_3)| = 12$ ($S_3 \times S_2$).
2. **Simplicity & Universal Fixed-Point Vanishing over $\mathbb{F}_3$**:
   - $V_{\mathrm{std}}(\mathbb{F}_3) = \{v \in \mathbb{F}_3^5 \mid \sum_{i=0}^4 v_i = 0\}$ (`card = 81`) is a **simple** $\mathbb{F}_3[S_5]$-module (since $5 \equiv 2 \not\equiv 0 \pmod 3$).
   - $(V_{\mathrm{std}}(\mathbb{F}_3))^{C_5} = \{0\}$, hence for **every** $\mathbb{F}_3[S_5]$-extension $0 \to V_{\mathrm{std}}(\mathbb{F}_3) \to M \to V_{\mathrm{std}}(\mathbb{F}_3) \to 0$ (`|M| = 3^8 = 6561`), $M^{C_5} = M^{F_{20}} = M^{A_5} = M^{S_5} = \{0\}$. Thus **every** non-trivial $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3] \setminus \{\mathcal{O}_{\mathcal{B}}\}$ spontaneously/geometrically breaks $S_5$ (and $A_5$).
   - Conversely, $\dim_{\mathbb{F}_3} V_{\mathrm{std}}(\mathbb{F}_3)^{S_4} = 1$ (spanned by `(1,1,1,1,2)`) and $\dim_{\mathbb{F}_3} V_{\mathrm{std}}(\mathbb{F}_3)^{S_3 \times S_2} = 1$ (spanned by `(1,1,1,0,0)`), yielding $3^2 - 1 = 8$ non-trivial $S_4$-invariant $3$-torsion classes and $8$ non-trivial $(S_3 \times S_2)$-invariant $3$-torsion classes in $V_{\mathrm{std}}(\mathbb{F}_3)^{\oplus 2}$, while $\dim_{\mathbb{F}_3} V_{\mathrm{std}}(\mathbb{F}_3)^{C_3} = 2$.

### D. §4 — $\Lambda^1 F \oplus \Lambda^2 F^*$ Anomaly Cancellation & $S_5 \to S_4$ Vector-Like Lepton Decoupling
1. **Symbolic Anomaly Polynomials over `[CommRing R]`** ($2 y_2 + 3 y_3 = 0$, $N_q$ chiral quark families, $N_\ell$ chiral lepton families):
   - $2\mathcal{A}_{[\mathrm{SU}(3)_c]^2 \mathrm{U}(1)_Y} = -N_q(2y_2 + 3y_3) = 0$ and $\mathrm{Tr}(Y) = -3 N_q(2y_2 + 3y_3) = 0$ identically.
   - $2\mathcal{A}_{[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y} = (N_\ell - N_q) y_2$ and $9\mathcal{A}_{[\mathrm{U}(1)_Y]^3} = 54(N_q - N_\ell) y_2^3$, vanishing (for $y_2 \ne 0$ over a domain of char $\nmid 6$) **iff** $N_\ell = N_q$.
   - Witten global $\mathrm{SU}(2)_L$ doublet count $N_\ell + 3 N_q$ is odd ($= 13$) at $(N_q, N_\ell) = (3, 4)$ and even ($= 12$) at $(N_q, N_\ell) = (3, 3)$.
2. **Consequence for the $t = 0$ Lepton Sector**:
   - Truncating to $H^0$ alone (`(N_q, N_\ell) = (3, 4)`) is **forbidden** by $[\mathrm{SU}(2)_L]^2 \mathrm{U}(1)_Y$, $[\mathrm{U}(1)_Y]^3$, and Witten's $\mathbb{Z}_2$ anomaly.
   - Retaining the full Dolbeault complex (`(3,0)` quarks + `(4,1)` leptons) is **anomaly-free** (`N_\ell^{\mathrm{net}} = 4 - 1 = 3 = N_q`), consisting of $3$ chiral lepton families plus $1$ vector-like pair $(1_L, 1_R)$.
   - Under unbroken $S_5$, $\mathrm{Hom}_{S_5}(V_{\mathrm{std}}(F), F_{\mathrm{triv}}) = 0$ (protecting the 4th mode); once $\mathcal{L} \ne \mathcal{O}_{\mathcal{B}}$ breaks $S_5 \to S_4$, $\dim_F \mathrm{Hom}_{S_4}(V_{\mathrm{std}}(F), F_{\mathrm{triv}}) = 1$, unlocking a unique $G_{\mathrm{SM}} \times S_4$-invariant Dirac mass pairing whose kernel (when $M_{\mathrm{vec}} \ne 0$) has exact dimension $3$ (`V_{(3,1)}`).
   - A Rule-13a zero-instance `class BringKummerGenerationClosureHypothesis` records the three physical inputs not derived by kinematics alone: (i) canonical/Spin$^c$ twist $K_{\mathcal{B}}$, (ii) non-trivial central $\mu_3$ Kummer bundle $\mathcal{L} \in \mathrm{Pic}^0(\mathcal{B})[3]^{S_4} \setminus \{0\}$, and (iii) nonzero vector-like singlet coupling $M_{\mathrm{vec}} \ne 0$.

---

## 3. Pre-Registered 80-dps Numerical & Exact Verification Plan

1. **Exact Hurwitz & Chevalley–Weil Verification**: Exhaustive check of all $\mathbb{Z}_3$-covers of/from genus $4$, verifying $(4, 3, 3)$ on $\tilde{\mathcal{B}} \to \mathcal{B}$ vs $(2, 1, 1), (1, 2, 1), (0, 2, 2), (0, 3, 1)$ on $\Sigma_4 \to \mathcal{B}_0$.
2. **Exact 120-Element $S_5$ & $6561$-Element $\mathbb{F}_3^8$ Orbit Census**: Complete stabilizer, normalizer, and $S_5$-orbit size decomposition on $V_{\mathrm{std}}(\mathbb{F}_3)$ (`81` elements) and $V_{\mathrm{std}}(\mathbb{F}_3)^{\oplus 2}$ (`6561` elements, `3280` cyclic $\mathbb{Z}_3$-subgroups), including explicit verification on non-split $\mathbb{F}_3[S_5]$-extensions (`H^1(S_5, \mathrm{End}(D^{(4,1)}))` check) that $M^{C_5} = M^{A_5} = M^{S_5} = \{0\}$.
3. **80-dps Bring Period Matrix & Kummer 3-Torsion Theta/Projector Witness**:
   - Evaluate Riera–Rodríguez / Braden–Northover period matrix $\Omega_{\mathcal{B}}$ of Bring's curve ($\mathrm{Jac}(\mathcal{B}) \sim E_{5\tau_0}^3 \times E_{\tau_0}$, $j(\tau_0) = -29^3 \cdot 5 / 2^5 = -121945/32$, $j(5\tau_0) = -25/2$) at `work_dps = 80` via inverse modular $j$-inversion, verify $\det \mathrm{Im}\,\Omega_{\mathcal{B}} > 0$ and $S_4$-invariant vs $V_{(3,1)}$ period-block projectors to $< 10^{-75}$, and evaluate $3$-torsion characteristics $\frac{1}{3}(p\Omega_{\mathcal{B}} + q) \in \mathrm{Jac}(\mathcal{B})[3]$ confirming exact $S_4$-invariance on the elliptic factor $E$.
   - Evaluate $q_0 = \mathrm{q\_at}(80)$ substrate invariants (`[2]_{q_0}, [3]_{q_0}, z_2, z_3, z_5`) and verify exact 80-dps vanishing of all anomaly residuals at $(N_q, N_\ell) = (3, 3)$ vs non-vanishing at $(3, 4)$.
