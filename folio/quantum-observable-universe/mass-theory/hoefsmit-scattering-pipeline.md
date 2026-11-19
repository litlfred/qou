**Proposition (conditional on [hyperbolic volume transcendence conjecture](#conj:hyperbolic-volume-transcendence) and baryon period ratio remark).**
*The mass of a nuclear state with braid word $\beta \in B_n$ computes via the following functorial pipeline:*

$$
  \beta
  \;\xrightarrow{\;\rho_\lambda\;}
  \prod_i \rho_\lambda(\sigma_i)
  \;\xrightarrow{\;\mathrm{tr}_M\;}
  J_K(q)
  \;\xrightarrow{\;\omega\;}
  \mathrm{Geom}(K)
  \;\xrightarrow{\;\times\, m_e\;}
  \mathfrak{m}
$$

*Stage 1 (Hoefsmit). Each crossing $\sigma_i$ acts on the Wedderburn--Artin block $\rho_\lambda$ via the Hoefsmit seminormal matrix. The scattering amplitude from tableau state $T$ to state $T'$ under crossing $\sigma_i$ is:*

$$
  W_{T \to T'} = \langle T' \mid \sigma_i \mid T \rangle
  = \begin{cases}
    a_\rho & T' = T \quad\text{(forward scattering)} \\
    b_\rho & T' = (T)_i \quad\text{(exchange scattering)} \\
    0 & \text{otherwise}
  \end{cases}
$$

*where $a_\rho = h/(1 - q^{-2\rho})$ is the $q$-deformed axial distance and $b_\rho = \sqrt{a_\rho a_{-\rho} + 1}$ is the exchange amplitude. The matrix is maximally sparse: at most $2$ nonzeros per row.*

*Stage 2 (Markov trace). The product of Hoefsmit matrices over all crossings in $\beta$ gives the braid representation matrix $\rho_\lambda(\beta)$. The Markov trace sums over all Wedderburn--Artin blocks:*

$$
  J_K(q) = \sum_{\lambda\,\vdash\,k}
  w_\lambda \cdot \frac{\chi_\lambda(\beta)}{\dim(\lambda)}
$$

*where $w_\lambda = \dim_q(\lambda)^2 / [k]_q!$ is the Wedderburn--Artin weight and $\chi_\lambda(\beta) = \mathrm{tr}(\rho_\lambda(\beta))$ is the Frobenius character.*

*By the universal branching rule, $\chi_\lambda(\beta)$ is determined by Young's lattice path counts $f^{\lambda/\mu}$ and the three base characters $\chi^{\mathrm{sym}}$, $\chi^{\mathrm{std}}$, $\chi^{\mathrm{alt}}$.*

*Stage 3 (Observation frame). The fibre functor $\tau$ evaluates the abstract Jones polynomial $J_K(q)$ on the knot complement $S^3 \setminus K$. The evaluation is geometric, determined by Thurston's geometrization:*

$$
  \tau(J_K)
  = \sum_\lambda w_\lambda \cdot
    \frac{\chi_\lambda(\beta)}{\dim(\lambda)}
    \cdot \mathrm{Geom}(K)
$$

*The factor $\mathrm{Geom}(K)$ projects the algebraic trace into a measurable observable: $\mathrm{Vol}(K)/\hbar_q^2$ for hyperbolic $K$ (mass/energy), $\mathrm{CS}(K) \cdot \hbar_q^2$ for torus $K$ (coupling phase), or $0$ for the unknot (vacuum).*

*Stage 4 (Physical mass). The mass is the norm of the evaluated trace, scaled by the electron mass $m_e$:*

$$
  \mathfrak{m}(K) = m_e \cdot \mathrm{Geom}(K)
    \cdot \sum_\lambda w_\lambda \cdot
    \frac{\chi_\lambda(\beta)}{\dim(\lambda)}
$$

*At Hecke level $k$, this sum truncates to $p(k)$ partitions. The truncation error satisfies:*

$$
  \mathrm{MAE}(k) \leq C_0 \times [2]_q^{-2(k-3)}
$$

*with convergence rate $[2]_q^2 \approx 4.04$ per level.*

*Proof.*
Each stage proves separately:

**Stage 1** uses the Hoefsmit seminormal form. The $q$-deformation of the classical axial distance $1/\rho$ to $h/(1 - q^{-2\rho})$ follows from the Hecke relation $\sigma_i^2 = h\sigma_i + 1$ and the requirement $\det = -1$ for each $2 \times 2$ block. The eigenvalues are $q$ (symmetric) and $-q^{-1}$ (antisymmetric), which are the eigenvalues of the universal $R$-matrix $\check{\mathcal{R}}$ of $U_q(\mathfrak{sl}_2)$ restricted to the isotypic component of type $\lambda$.

**Stage 2** uses the Wedderburn--Artin trace identity. The Markov trace $\mathrm{tr}_M$ factors through the Wedderburn--Artin decomposition $H_k(R, q) \cong \bigoplus_\lambda M_{d_\lambda}(\mathbb{C})$. The weight $w_\lambda$ ensures that $\mathrm{tr}_M$ is the unique trace satisfying the Markov property $\mathrm{tr}_M(x\sigma_k) = z \cdot \mathrm{tr}_M(x)$ for $x \in H_k(R, q)$.

**Stage 3** uses the $\mathrm{Geom}(K)$ alignment. The observation frame $\tau$ is the fibre functor of the Tannakian category $(\mathbf{C}, A, \tau)$. On the $\tau$-image (geometric) side, its evaluation on the knot complement is determined by $\tau$-image Thurston geometrization and the Yekutieli rigid dualizing complex: the UNIQUE non-degenerate pairing $\langle \omega_A^\bullet, S^3 \setminus K \rangle_{\mathrm{Frob}}$ yields $\mathrm{Vol}(K)/\hbar_q^2$ for hyperbolic $K$ and $\mathrm{CS}(K) \cdot \hbar_q^2$ for torus $K$. On the algebraic side this is the algebraic-quantum-volume pairing in $\mathbb{Z}[q^{\pm 1/2}]$; the geometric reading appears only after applying $\tau_{\mathrm{arch}}$. The universality follows from the rigidity of $\omega_A^\bullet$ (Yekutieli): the pairing is unique up to the scalar $\hbar_q^2$, and the scalar is fixed by requiring that $\mathrm{Geom}(\bigcirc) = 0$ (vacuum normalisation) and $\mathrm{Geom}(4_1) \cdot \hbar_q^2 = \mathrm{Vol}(4_1)$ (the figure-eight knot defines $q_0$).

**Stage 4** uses the topological mass formula. The convergence bound follows by induction on $k$ using the Pieri rule for skew tableaux counts: each level $k$ introduces $p(k) - p(k-1)$ new partitions whose total Wedderburn--Artin weight is $O([2]_q^{-2})$ of the previous level's weight, by Plancherel concentration. $\square$

*Formal asymptotic content. The truncation $\mathrm{MAE}(k) \leq C_0 \cdot [2]_q^{-2(k-3)}$ has $\mathrm{ordw}\bigl(\mathrm{MAE}(k)\bigr) = -2(k-3)\,\mathrm{ordw}([2]_q)$; see Big-O via $\mathrm{ordw}$ and the body asymptotics catalog.*
