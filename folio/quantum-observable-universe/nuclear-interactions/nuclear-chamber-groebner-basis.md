Let $R$ be a linearly ordered additive commutative group, and consider the $1s$-shell motif conservation matrix

$$
  A_0 \;=\; \begin{pmatrix}
    1 & 0 & 1 & 1 & 2 & 2 \\
    0 & 1 & 1 & 2 & 1 & 2
  \end{pmatrix} \in \mathbb{Z}^{2 \times 6}
$$

indexing the commutative polynomial generators $(x_p, x_n, x_d, x_t, x_h, x_\alpha)$ of proton, neutron, deuteron, triton, helion, and $\alpha$-particle counts under conservation of $(Z, N)$. Let $I_{A_0} = \langle x^{g^+} - x^{g^-} : A_0 g = 0 \rangle$ denote the associated toric ideal \cite{conti-traverso1991,sturmfels-thomas1997}, and write $c = (0, 0, -B_d, -B_t, -B_h, -B_\alpha) \in R^6$ for the cluster cost vector reduced modulo the row span of $A_0$.

1. **Graver and Gröbner fan structure.** Over $\mathbb{Q}$, the integer kernel $\ker_{\mathbb{Z}}(A_0)$ admits $28$ unsigned primitive Graver binomials \cite{graver1975} ($17$ unsigned circuits), a $27$-element unsigned universal Gröbner basis (excluding only $x_\alpha - x_p x_n x_d$), and $73$ full-dimensional Gröbner fan chambers in $R^6 / \mathrm{row}(A_0) \cong R^4$.

2. **Physical chamber $\mathcal{C}_{\mathrm{phys}}$ and $11$-rule reduced Gröbner basis.** Whenever $(B_d, B_t, B_h, B_\alpha) \in R^4$ satisfies the five irredundant facet inequalities

$$
  0 < B_d, \qquad
  B_d < B_h, \qquad
  B_d < B_t, \qquad
  2 B_t < B_\alpha, \qquad
  2 B_h < B_\alpha,
$$

all eleven binomials of the minimal reduced Gröbner basis $\mathcal{G}_{\mathrm{phys}}$ are simultaneously strictly cost-decreasing ($c \cdot g > 0$):

$$
  \begin{aligned}
    x_p x_n &\to x_d, &
    x_p x_d &\to x_h, &
    x_n x_d &\to x_t, &
    x_p x_t &\to x_\alpha, \\
    x_n x_h &\to x_\alpha, &
    x_d^2 &\to x_\alpha, &
    x_d x_t &\to x_n x_\alpha, &
    x_d x_h &\to x_p x_\alpha, \\
    x_t x_h &\to x_d x_\alpha, &
    x_t^2 &\to x_n^2 x_\alpha, &
    x_h^2 &\to x_p^2 x_\alpha . &
  \end{aligned}
$$

Both the bare and tower-resummed aether binding energies at $q_0$ lie strictly inside $\mathcal{C}_{\mathrm{phys}}$.

3. **Drip-line dissociation and integer parity monomers.** Reduction modulo $\mathcal{G}_{\mathrm{phys}}$ carries ${}^5\mathrm{He}$ ($x_p^2 x_n^3$) deterministically to the irreducible degree-$2$ disconnected normal form $x_\alpha x_n$, while mapping ${}^{12}\mathrm{C}$ ($x_p^6 x_n^6 \mapsto x_\alpha^3$), ${}^{14}\mathrm{N}$ ($x_p^7 x_n^7 \mapsto x_d x_\alpha^3$), ${}^9\mathrm{Be}$ ($x_p^4 x_n^5 \mapsto x_n x_\alpha^2$), and ${}^9\mathrm{B}$ ($x_p^5 x_n^4 \mapsto x_p x_\alpha^2$) to integer cluster normal forms without fractional continuous-relaxation artifacts.

4. **Degree-$3$ Hoyle bottleneck and capacitated shell confluence.** On the $(\alpha, {}^8\mathrm{Be}, {}^{12}\mathrm{C})$ baryon-number sublattice $A_{\mathrm{Hoyle}} = (4, 8, 12)$, the inequalities $2 c_\alpha < c_{{}^8\mathrm{Be}}$ and $c_{{}^{12}\mathrm{C}} < 3 c_\alpha$ simultaneously orient the endothermic fission binomial $x_{{}^8\mathrm{Be}} \to x_\alpha^2$ and the degree-$3$ fusion binomial $x_\alpha^3 \to x_{{}^{12}\mathrm{C}}$. Adjoining the seven Mayer--Jensen shell occupation and hole variables $u_s + w_s = C_s$ for $C_s \in \{2, 6, 12, 8, 22, 32, 44\}$ recovers cumulative magic closures $(2, 8, 20, 28, 50, 82, 126)$ and guarantees $u_s > 0$ or $w_s > 0$ on every physical fiber $C_s \ge 1$, so the $S - 1$ adjacent single-shell promotions $u_{s+1} w_s \to u_s w_{s+1}$ are globally confluent.
