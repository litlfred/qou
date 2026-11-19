**Algorithm (Two-Term Categorical Lagrangian Trace and nucleon mass anchor).**
*Evaluate the dimensionless lepton-to-nucleon mass ratios $m_\mu / m_e$, $m_p / m_e$, and $m_n / m_e$ together with the corrected electromagnetic coupling $\alpha_{\mathrm{EM}}^{\mathrm{corr}}(q)$ via the Two-Term Categorical Lagrangian Trace $M = M_{\mathrm{QCD}} + M_{\mathrm{QED}}$ in arbitrary-precision real ball arithmetic ($\ge 80$ decimal digits).*

*(Terminological note: the phrase "mass identity" in [the vortex-filament mass-identity definition](#def:mass-identity) denotes the nonabelian multiplicative integral around a single vortex filament; the algorithm below evaluates the composite archimedean mass ratios determined by that trace functional.)*

### Input

- *Balancing substrate twist root $q_0 > 1$ (or its Chern–Simons-shifted two-term counterpart $q_{2t} = q_0 - \delta q_{\mathrm{CS}}$ determined by anchoring $m_p / m_e$) and unit scale $m_e > 0$ (rendering dimensionless ratios $M / m_e$ into energy units).*
- *Hyperbolic volume of the figure-eight knot complement $S^3 \setminus 4_1$:*
  $$
    \mathrm{Vol}(4_1)
    \;=\;
    6\,\Lambda(\pi / 3)
    \;=\;
    2\,\mathrm{Cl}_2(\pi / 3)
    \;=\;
    2 \sum_{k=1}^{\infty} \frac{\sin(k\pi / 3)}{k^2},
  $$
  *realised by two regular ideal hyperbolic tetrahedra of dihedral angle $\pi/3$ \cite{martelli2016}.*

### Output

- *Corrected electromagnetic fine-structure coupling $\alpha_{\mathrm{EM}}^{\mathrm{corr}}(q_{2t}) \in \mathbb{R}_{> 0}$.*
- *Two-term mass ratios $m_\mu / m_e$, $m_p / m_e$, and $m_n / m_e$ (and energy renderings $m_\mu, m_p, m_n$ against $m_e$) enclosed to $\ge 80$ decimal digits.*

### Algorithm

1. **Transcendental hyperbolic volume enclosure:** Evaluate $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ to $\ge 80$ decimal digits by accelerated Euler–Maclaurin / Borwein–Bradley series summation with rigorous tail enclosure.
2. **Strong topological channel ($M_{\mathrm{QCD}}$) and tower resummation:** Set $\hbar_q = 1 - q^{-1}$ and $h = q - q^{-1}$ (with geometric Kaluza–Klein/Reeb tower resummation $\sum_{k=0}^\infty \hbar_q^{2k} = (1 - \hbar_q^2)^{-1}$). Evaluate:
   - *Muon hyperbolic anchor:*
     $$
       \frac{m_\mu(q)}{m_e} \;=\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2};
     $$
   - *Exact rational Convention-D Borromean trace and $q$-factorial dressing:*
     $$
       \bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr|
       \;=\;
       \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4},
       \qquad
       F_{\mathrm{Bor}}(q)
       \;=\;
       \bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr| \cdot \frac{[3]_q!}{q^3},
     $$
     where $[3]_q! = (1 + q)(1 + q + q^2)$;
   - *Strong proton trace:*
     $$
       M_{\mathrm{QCD}}^{(p)}(q)
       \;=\;
       \dim V_{(2,1)}\,\bigl(m_\mu(q)\,F_{\mathrm{Bor}}(q) - |S_3|\,m_e\bigr)
       \;=\;
       2\,\bigl(m_\mu(q)\,F_{\mathrm{Bor}}(q) - 6\,m_e\bigr).
     $$
3. **Form-B Bring–Schwinger cubic electromagnetic coupling ($\alpha_{\mathrm{EM}}^{\mathrm{corr}}$):** Using the genus-$4$ Bring invariants $g = 4$ and $\frac{2g}{4\pi(g-1)} = \frac{2}{3\pi}$ from [Step 4](#alg:bring-brane) and the one-loop Hecke factor $H_{\mathrm{loop}}(q) = \frac{[2]_q}{8\pi}$, solve the depressed cubic fixed-point equation
   $$
     \frac{1}{\alpha}
     \;=\;
     q\,[9]_q\,[10]_q \;+\; \frac{2}{3\pi} \;+\; \alpha\,\frac{[2]_q}{8\pi}\bigl(1 - h^2\,\alpha\bigr)
   $$
   by Newton–Raphson iteration in real ball arithmetic to isolate the unique physical root $\alpha_{\mathrm{EM}}^{\mathrm{corr}}(q) \in (0, 10^{-2})$.
4. **Electromagnetic Borromean self-energy ($M_{\mathrm{QED}}$) and Chern–Simons shift:** Evaluate the connected fourth-order Borromean $V^3 = (\sigma_1\sigma_2^{-1})^3$ charge-weighted traces on the proton and neutron three-strand weight spaces,
   $$
     \mathrm{tr}_{\mathrm{conn}}(p, V^3) \;=\; -\frac{2}{27}\,h^4(h^2 + 3),
     \qquad
     \mathrm{tr}_{\mathrm{conn}}(n, V^3) \;=\; +\frac{1}{27}\,h^4(2h^2 + 3),
   $$
   with isovector difference $\Delta\mathrm{tr}_{\mathrm{QED,conn}}(V^3) = \frac{1}{27}\,h^4(4h^2 + 9)$. Combine $M = M_{\mathrm{QCD}} + M_{\mathrm{QED}}$ at the two-term root $q_{2t} = q_0 - \delta q_{\mathrm{CS}}$ (incorporating the $S^3$ framing shift $\delta q_{\mathrm{CS}}$ proportional to $\frac{1}{2\pi^2} = (\mathrm{Vol}(S^3))^{-1}$), reconciling the proton and muon anchors simultaneously.
5. **Neutron mass closure:** Combine $m_p(q_{2t})$, the Convention-D $\beta$-decay energy $\mathfrak{Q}_\beta(q_{2t})$ from [Step 11](#alg:q-beta-truncation), and the two-term electromagnetic isospin splitting $\Delta m_{\mathrm{QED}}^{\mathrm{conn}}(q_{2t})$ to return $m_n = m_p + \mathfrak{Q}_\beta + m_e$.

### Termination and Complexity

All rational trace factors have bounded degree $\le 8$ in $q^{\pm 1}$, and Newton–Raphson root isolation for $q_{2t}$ and $\alpha_{\mathrm{EM}}^{\mathrm{corr}}$ converges quadratically in $\le 8$ iterations at $80$-digit precision, giving $O(D \log D)$ bit complexity in the working digit count $D$.

### Mathematical Justification

1. **Mass-ratio existence, uniqueness, and Borromean trace:** Existence and uniqueness of the categorical mass functional follow from [mass-identity existence](#prop:mass-identity-exists), [mass-identity uniqueness](#prop:mass-identity-unique), and [the unified knot-mass theorem](#thm:knot-mass-formula-unified); the exact rational formula for $|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)|$ is proved in [the Borromean Markov-trace closed form](#prop:borromean-markov-trace-closed-form).
2. **Electromagnetic fixed point and isospin splitting:** The tree-plus-Bring-zero-mode decomposition and Form-B cubic Schwinger closure are established in [the additive Bring zero-mode coupling proposition](#prop:em-coupling-bring-zero-mode), while the two-term neutron–proton splitting structure follows [neutron–proton mass splitting](#prop:neutron-proton-splitting).
