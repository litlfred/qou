**Algorithm (Convention-D $\beta$-decay energy $\mathfrak{Q}_\beta$, weak axial coupling $g_A(q)$, and neutron lifetime $\tau_n$).**
*Evaluate the free-neutron (and nuclear) $\beta$-decay endpoint energy $\mathfrak{Q}_\beta$, the parameter-free $q$-Schur–Weyl axial-vector coupling $g_A(q)$, and the free-neutron lifetime $\tau_n$ under Convention D ($z_D = \frac{q^3}{q^2 + 1}$) with certified truncation order $N(\varepsilon)$.*

### Input

- *Two-term substrate parameter $q = q_{2t} > 1$, electron mass scale $m_e$, electroweak Fermi constant $G_F$ and CKM element $|V_{ud}|$, and target relative series accuracy $\varepsilon > 0$.*

### Output

- *Truncation order $N(\varepsilon) \in \mathbb{N}_{\ge 2}$, $\beta$-decay endpoint energy $\mathfrak{Q}_\beta^{(N)}(q)$ with remainder bound $< \varepsilon$, conserved vector coupling $g_V(q) = 1$, axial coupling $g_A(q)$, 3-body Fermi phase-space factor $f_0(\epsilon_0)$, and neutron lifetime $\tau_n$.*

### Algorithm

1. **Convention-D expansion coordinates and critical convergence radius:** Set $h = q - q^{-1}$, $H = h^2$, $\hbar_q = 1 - q^{-1}$, Hoefsmit factor $b(q) = \frac{\sqrt{q^4 + q^2 + 1}}{q^2 + 1} = \sqrt{\frac{H + 3}{H + 4}}$, and ladder variable $u(q) = b(q)\,\hbar_q^2$ (with bar-even coordinate $\bar{u}(H) = \frac{H}{4}\sqrt{\frac{H + 3}{H + 4}}$). From the critical branch point $H_* = \frac{-15 + \sqrt{33}}{4} \in (-3, -2)$ of $2H^2 + 15H + 24 = 0$, compute the Lagrange–Bürmann convergence radius $R_u = \sqrt{\bar{u}^2(H_*)} \approx 0.369009$ and ratio $r = u(q)/R_u < \tfrac{1}{40}$, selecting
   $$
     N(\varepsilon)
     \;=\;
     \max\!\left(2,\; \left\lceil \frac{\ln\bigl((1 - r)\,\varepsilon\bigr)}{\ln r} \right\rceil - 1\right).
   $$
2. **Convention-D generating function and cumulant product:** Evaluate the truncated Convention-D product expansion of the all-order generating function $\mathcal{G}_D(u; q) = \prod_{k=2}^{\infty}\bigl(1 + c_k^{(D)}\,u^k\bigr)$ (constructed in [the Convention-D generating-function sidecar](#alg:ck-truncation-ladder)):
   $$
     \mathfrak{Q}_\beta^{(N)}(q)
     \;=\;
     Q_{\mathrm{base}}^{(D)}(q)\,\prod_{k=2}^{N(\varepsilon)} \bigl(1 + c_k^{(D)}(q)\,u(q)^k\bigr)
     \;-\;
     \Delta m_{\mathrm{QED}}^{\mathrm{conn}}(q),
   $$
   incorporating the Kashiwara quadratic rung $c_2^{(D)} = -1$ ($1 - u^2$), the derived Convention-D rational cubic coefficient
   $$
     c_3^{(D)}(q) \;=\; -\frac{3q^2 - 1}{2q(q^2 + 1)}
   $$
   and mirror-projected eigenphase $\alpha_D^{\mathrm{proj}}(q) = \frac{(z_D - 1)h}{2} - \frac{h^2}{4}$, the quartic Wedderburn/Kashiwara cumulant $c_4^{(D)}(q)$ at $u^4 = b^4\hbar_q^8 \in \mathbb{Q}(q)$, higher distinct-partition rungs $c_k^{(D)}$ ($5 \le k \le N(\varepsilon)$), and the Two-Term Borromean QED splitting $\Delta m_{\mathrm{QED}}^{\mathrm{conn}}(q)$ from [Step 9a](#alg:mass-identity).
3. **Weak isospin coevaluation and 64D $q$-Schur–Weyl axial coupling $g_A(q)$:**
   - Apply the 3-strand $U_q(\mathfrak{sl}_2)$ raising coproduct $\Delta^{(3)}(E) = E \otimes K^{1/2} \otimes K^{1/2} + K^{-1/2} \otimes E \otimes K^{1/2} + K^{-1/2} \otimes K^{-1/2} \otimes E$ ($K = \mathrm{diag}(q, q^{-1})$), which intertwines $H_3(q)$ and satisfies $(\Delta^{(3)}(E))^2|_{V_{(2,1)}} = I_2$ ($g_V(q) = 1$), tensored with lepton-pair coevaluation $\mathrm{coev}_V \colon \mathbf{1} \to V_e \otimes V_{\bar\nu}^{\vee}$ ($3 \to 5$ strands).
   - Evaluate the bar-even 64D spin–isospin Gamow–Teller matrix element $g_A^{\mathrm{SW}}(q) = g_A^{\mathrm{diag}}(q) + g_A^{\mathrm{cross}}(q)$:
     $$
       g_A^{\mathrm{diag}}(q) \;=\; \frac{q^8 + 3q^6 + 10q^4 + 3q^2 + 1}{2(q^4 + q^2 + 1)^2},
       \qquad
       g_A^{\mathrm{cross}}(q) \;=\; \frac{(q^2 + 1)^2}{2(q^4 + q^2 + 1)} \;=\; \frac{[2]_q^2}{2[3]_q}
     $$
     ($g_A^{\mathrm{SW}}(1) = \tfrac{5}{3}$), dressed by the Bring–Schwinger / pion-pole factor to $g_A(q)$.
4. **3-body Fermi phase-space integral and neutron lifetime $\tau_n$:** Set $\epsilon_0 = (\mathfrak{Q}_\beta^{(N)} + m_e)/m_e$, evaluate the exact massless-neutrino phase-space function
   $$
     f_0(\epsilon_0)
     \;=\;
     \frac{1}{60}\bigl(2\epsilon_0^4 - 9\epsilon_0^2 - 8\bigr)\sqrt{\epsilon_0^2 - 1}
     \;+\;
     \frac{\epsilon_0}{4}\,\ln\!\bigl(\epsilon_0 + \sqrt{\epsilon_0^2 - 1}\bigr)
   $$
   (together with its Coulomb-enhanced outer radiative integral $f_R(\epsilon_0)$), and return
   $$
     \tau_n
     \;=\;
     \left[\frac{G_F^2\,|V_{ud}|^2\,m_e^5}{2\pi^3}\,\bigl(g_V(q)^2 + 3\,g_A(q)^2\bigr)\,f_R(\epsilon_0)\right]^{-1}.
   $$

### Termination and Complexity

Because $r = u(q_{2t})/R_u < \tfrac{1}{40}$, each additional rung suppresses the relative tail by more than $1.6$ orders of magnitude ($< 10^{-16}$ by $N = 9$); total work is $O(N(\varepsilon))$ arithmetic operations at $\ge 80$ decimal digits.

### Mathematical Justification

Convergence of the product expansion and the $N(\varepsilon)$ error bound follow [the categorical precision-ladder proposition](#prop:q-beta-categorical-precision-ladder), the Convention-D eigenphase transfer structure follows [Convention-D cosine resummation](#prop:q-beta-cos-resummation), and the weak-transition rate law follows [hadron half-life](#prop:hadron-half-life).
