**Algorithm (Confinement primal–dual conic program and canonical $T_w$ selection).**
*Solve the primal–dual linear/semidefinite program over the Frobenius Gram cone of $H_n(q)$ to select the minimal-action confined state $x^*$ together with its dual shadow prices $(y_0^*, y^*)$ and saturated Wedderburn support.*

### Input

- *Basis Markov-trace vector $t_i = \mathrm{tr}_M(b_i) \in \mathbb{R}$ and net-crossing vector $\nu_i = \mathrm{net}(b_i) \in \mathbb{R}$ on the reduced basis $\{b_1, \dots, b_m\}$ of $H_n(q)$ (from [Step 2](#alg:gs-reduce-to-hecke-nf) and [Step 3](#alg:markov-trace)).*
- *Symmetric Frobenius Gram matrix $G_{ij} = \mathrm{tr}_M(b_i b_j)$ (or block-diagonal Wedderburn matrix cone $\bigoplus_{\lambda} \mathbb{S}_+^{d_\lambda}$) from [Step 6](#alg:frobenius-pairing).*
- *Target topological net demand $n_{\mathrm{target}} \in \mathbb{Z}_{\ge 0}$.*

### Output

- *Primal minimiser $x^* \in \mathbb{R}_{\ge 0}^m$ specifying the confined normal-form state $\sum_{i=1}^m x_i^* b_i$.*
- *Dual maximiser $(y_0^* \in \mathbb{R},\; y^* \in \mathbb{R}_{\ge 0}^m)$, primal and dual optimal values $p^* = d^*$, and active receptive channel set $\mathcal{A}(y^*) = \{i \in \{1, \dots, m\} : y_i^* > 0\}$.*

### Algorithm

1. **Formulate the primal–dual pair:** Assemble the primal minimisation over the Frobenius positivity cone and its Lagrangian dual:
   $$
     \begin{aligned}
       p^* \;=\; \min_{x \in \mathbb{R}^m}\;\; & t^\top x \\
       \text{subject to}\;\; & \nu^\top x = n_{\mathrm{target}}, \\
       & G x \ge 0, \quad x \ge 0,
     \end{aligned}
     \qquad\qquad
     \begin{aligned}
       d^* \;=\; \max_{y_0 \in \mathbb{R},\; y \in \mathbb{R}^m}\;\; & n_{\mathrm{target}}\,y_0 \\
       \text{subject to}\;\; & \nu\,y_0 + G^\top y \le t, \\
       & y \ge 0
     \end{aligned}
   $$
   (lifting $G x \ge 0$ to $\sum_i x_i \rho^\lambda(b_i) \succeq 0$ across Wedderburn blocks $\lambda \vdash n$ in the full semidefinite program).
2. **Solve by primal–dual interior-point barrier continuation:** Track the central path $(x(\mu), y_0(\mu), y(\mu))$ as the barrier parameter $\mu \downarrow 0$ until primal residual, dual residual, and duality gap $|p^* - d^*| = |t^\top x^* - n_{\mathrm{target}}\,y_0^*|$ fall below the prescribed tolerance $\varepsilon_{\mathrm{opt}}$.
3. **Extract active shadow-price channels via complementary slackness:** At optimality, enforce complementary slackness
   $$
     y_i^*\,(G x^*)_i \;=\; 0,
     \qquad
     x_j^*\,\bigl(t_j - \nu_j\,y_0^* - (G^\top y^*)_j\bigr) \;=\; 0
     \qquad (1 \le i, j \le m),
   $$
   and collect $\mathcal{A}(y^*) = \{i : y_i^* > 0\}$.

### Termination and Complexity

Self-concordant log-barrier interior-point iteration reduces the duality gap $\mu$ by a constant factor in $O(\sqrt{m})$ Newton steps per digit, yielding polynomial complexity $O\bigl(m^{3.5}\log(1/\varepsilon_{\mathrm{opt}})\bigr)$ in the basis dimension $m = \dim H_n(q)$.

### Mathematical Justification

1. **Strong duality and canonical $T_w$ optimality:** On the generic semisimple interval $q \in (1/\varphi^2, \varphi^2)$ containing $q_0$, strict interior feasibility holds (Slater's condition), so [the operator-selection LP proposition](#prop:operator-selection-lp) guarantees $p^* = d^*$ with zero duality gap and identifies the canonical confined element $T_w$ as the primal extremum.
2. **Structural meaning of the dual variables:** By [LP dual stability](#prop:lp-dual-stability), $y_0^* = \partial p^* / \partial n_{\mathrm{target}}$ measures the marginal confinement energy per unit topological net, while strictly positive shadow prices $y_i^* > 0$ isolate the Frobenius positivity faces $(G x^*)_i = 0$ saturated by the bound state, identifying its active Wedderburn blocks.
