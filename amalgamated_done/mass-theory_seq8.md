<!-- FILE_START: intro-hoefsmit-convergence-atomic.md -->
The Hoefsmit basis for the Hecke algebra is the categorical analogue of the Young orthogonal form for the symmetric group. It diagonalises the Jucys–Murphy operators and exposes the content-grading that controls the $q$-expansion of the binding-energy formula. This section assembles the universal braid-branching identity driving the Hoefsmit construction, proves its convergence at the substrate parameter, and exhibits the atomic-shell evidence that pins the convergence rate.

The arc proceeds in three layers. The first six blocks establish the universal braid-branching formula, prove the Hoefsmit basis exists in the categorical setting, and reduce the convergence question to a polynomial inequality in the substrate parameter. The middle blocks prove convergence at $q_0 \approx 1.1097$ and bound the rate, identifying the leading correction term. The closing blocks survey the atomic-shell evidence—the categorical predictions for the $1s, 2s, 2p, \dots$ shell sequence and their empirical agreement with the noble-gas closure pattern.

The output is the validated Hoefsmit basis with explicit content-grading. The subsequent Markov-axiom analysis exploits this to derive closed-form $\chi$-characters. The atomic-shell evidence constitutes the strongest empirical validation of the substrate-level construction.
<!-- FILE_END: intro-hoefsmit-convergence-atomic.md -->

<!-- FILE_START: operator-selection-lp.md -->
The confinement LP selects the Borromean link $\mathcal{B}_3$ as the unique optimizer over the $6$-element NF basis of $H_3(q)$. We formulate the general LP for knot operator selection in $H_n(q)$ for arbitrary strand number $n$. The confinement LP is the special case $n = 3$, $d = 6$.

## Input / Output

**Input.**
- Strand number $n \geq 2$.
- A basis $\{b_1, \ldots, b_d\}$ of $H_n(q)$ (the NF basis, with $d = n!$).
- Markov traces $t_i = \mathrm{tr}_M(b_i)$ for each basis element.
- The $d \times d$ Frobenius Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$.
- A target net value $n_{\mathrm{target}} \in \mathbb{R}_{>0}$ (the normalised categorical mass of the desired state).

**Output.**
- The optimal coefficient vector $x^* \in \mathbb{R}^d$ such that $\Phi^* = \sum_{i=1}^{d} x_i^* b_i$ is the minimum-action knot operator satisfying all Frobenius positivity and net constraints.
- The dual certificate $(y_0^*, y^*)$ proving optimality.

## Primal program (operator selection)

**Proposition (general operator selection LP).**
*The knot operator $\Phi = \sum_{i=1}^{d} x_i b_i \in H_n(q)$ for a target interaction with net value $n_{\mathrm{target}}$ is the solution of the linear program:*

$$
  \min_{x \in \mathbb{R}^d} \quad \sum_{i=1}^{d} t_i \, x_i
$$

*subject to:*

$$
  \sum_{i=1}^{d} x_i = n_{\mathrm{target}}
  \qquad (\text{net constraint})
$$

$$
  \sum_{j=1}^{d} G_{ij}\, x_j \geq 0
  \quad \forall\, i \in \{1, \ldots, d\}
  \qquad (\text{Frobenius positivity})
$$

$$
  x_i \geq -M \quad \forall\, i
  \qquad (\text{boundedness})
$$

*where $M > 0$ is a constant large enough to ensure boundedness of the feasible polyhedron.*

The objective $\sum_{i} t_i x_i = \mathrm{tr}_M(\Phi)$ is the categorical action. Minimizing it selects the operator of least action among all operators compatible with the Frobenius structure.

The Frobenius positivity constraints $Gx \geq 0$ encode the demand–supply balance: $\Phi$ must pair non-negatively with every basis element under the Frobenius inner product. No channel carries unbounded demand.

**LP over motivic shadows, not real numbers.**
*The data feeding the LP—Markov traces $t_i = \mathrm{tr}_M(b_i)$ and Frobenius Gram entries $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$—are formal elements of $\mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, hence elements of the Habiro completion $\widehat{\mathbb{Z}[q]}$. The selection of the operator $\Phi^* = \sum_i x_i^* b_i$ is a combinatorial problem over the motivic shadows of the motivic substrate (the algebraic data of the Hecke algebra independently of any place-realization). Strong duality is a purely algebraic consequence of the LP. Only after the optimizer is selected does the archimedean realization $\rho_\infty$ project the dual prices and objective value into physical binding energies in $\mathbb{R}$. The non-archimedean realizations $\rho_p$ recover the LP's cyclotomic shadows at each finite place $p$.*

## Dual program (demand pricing)

By LP duality, the dual is:

$$
  \max_{y_0, \, y \in \mathbb{R}^d} \quad n_{\mathrm{target}} \cdot y_0
  - M \sum_{i=1}^{d} s_i
$$

*subject to:*

$$
  y_0 + \sum_{i=1}^{d} G_{ji}\, y_i - s_j \leq t_j
  \quad \forall\, j \in \{1, \ldots, d\}
$$

$$
  y_i \geq 0, \quad s_i \geq 0 \quad \forall\, i
$$

For large $M$, the slack variables $s_i$ are driven to zero at optimality. The effective dual simplifies to:

$$
  \max_{y_0, \, y \geq 0} \quad n_{\mathrm{target}} \cdot y_0
$$

*subject to:*

$$
  y_0 + \sum_{i=1}^{d} G_{ji}\, y_i \leq t_j
  \quad \forall\, j \in \{1, \ldots, d\}
$$

## Strong duality

**Proposition (strong duality).**
*The primal and dual programs have equal optimal values:*

$$
  \sum_{i=1}^{d} t_i \, x_i^*
  \;=\;
  n_{\mathrm{target}} \cdot y_0^*
$$
<!-- FILE_END: operator-selection-lp.md -->

<!-- FILE_START: operator-selection-lp-interpretation.md -->
The dual variable $y_0$ is the shadow price of the net constraint: the marginal cost (in units of categorical action) of increasing the target mass $n_{\mathrm{target}}$ by one unit. The dual variables $y_i \geq 0$ are the shadow prices of the Frobenius positivity constraints (channel demand prices). A positive $y_i^*$ at optimality indicates that the $i$-th Frobenius constraint is tight, meaning the $i$-th channel is saturated.
<!-- FILE_END: operator-selection-lp-interpretation.md -->

<!-- FILE_START: sdp-degeneracy-at-metallic-coincidence.md -->
**Observation.** At the cost-coincidence loci of the operator-selection LP/SDP—points $q^* > 0$ where two cost coefficients $t_i(q)$ and $t_j(q)$ become equal—the strict-complementarity condition fails and the SDP is degenerate. These loci coincide exactly with the metallic-ratio ladder $\{\delta_n : n \in \mathbb{N}^+\}$.

**The mechanism.** For the $n=2$ LP with basis $\{\gamma, \sigma_0\}$ of $H_2(q)$, the cost coefficients are

$$
  t_1(q) \;=\; 2(q + q^{-1}),
  \qquad
  t_2(q) \;=\; q^2 - q^{-2}.
$$

A direct algebraic calculation gives

$$
  t_1(q) \;=\; t_2(q)
  \quad\Longleftrightarrow\quad
  q - q^{-1} \;=\; 2
  \quad\Longleftrightarrow\quad
  q \;=\; \delta_{\rm silver} \;=\; 1 + \sqrt{2}.
$$

At this $q$, the LP optimum is a face of the feasible polytope, not a vertex. Any feasible $x$ satisfying $x_1 + x_2 = n_{\rm target}$ achieves the same primal cost $t_1 x_1 + t_2 x_2 = t_1 \cdot n_{\rm target}$. The dual shadow prices $y_i^*$ become non-unique (multiple optimal $(y_0^*, y^*)$ values), strict complementarity fails, and the active set $\mathcal{A} = \{i : y_i^* > 0\}$ is empty. This is the SDP-degeneracy signature: rapid loss of conditioning, ambiguous identification of binding constraints, and multiple optimal solutions returned.

**Empirical verification.** The $n=2$ LP active-set sweep observed this signature. Below silver the active set was $\{0\}$ (row 1 tight), AT silver it was $\emptyset$ (degenerate), above silver it was $\{1\}$ (row 2 tight). The degeneracy at silver is the first non-null result in a series of prior canonical probes that all returned smooth observables.

**Structural significance.** The metallic-ratio ladder sits on the algebraic side: $q = \delta_n$ is where the Hecke scalar $q - q^{-1}$ takes the integer value $n$, making $\sigma$ satisfy the integer-coefficient quadratic $\sigma^2 = n \sigma + 1$. Smooth observables (Wenzl weights, Jones polynomial signs, $n=3$ per-block character signs) do not see this discrete arithmetic structure because they are rational functions of $q$ with no discontinuities. The LP-vertex combinatorics sees it: cost-coefficient coincidences are algebraic events that translate the arithmetic of $q - q^{-1}$ into a topological change of the optimum's face dimension.

**Physical interpretation.** Identifying the silver coincidence with the CFL phase transition of dense quark matter gives the empirical handle on this algebraic phenomenon. The CFL transition density $\rho_c$ is the physical realization of the silver-coincidence point. The SDP degeneracy there is the order-parameter discontinuity of the first-order CFL transition. Multiple metallic ratios on the ladder correspond to multiple phase transitions. The bar-mirror $\varphi^2 \approx 2.618$ of the deconfinement boundary $q_{\rm gold} = 1/\varphi^2$ forms a candidate for the CFL $\to$ gCFL boundary observed in dense-QCD phenomenology.

**Generalisation (conditional).** For the strand-$n$ LP with basis size $d_n = n!$, the cost coefficients $t_i(q)$ are rational functions of $q$. The pairwise coincidence equations $t_i(q) = t_j(q)$ have rational-function solutions. Those solutions on the metallic ladder constitute the set $S(n) \subseteq \{\delta_k : k \le n\}$ of LP-degeneracy points for $n$ strands. For $n=2$, $S(2) = \{2\}$ (silver only). For $n=3$, the categorical evaluation returns $\{\delta_{\rm silver}\}$. The higher-strand characterisation remains conditional.

**Falsifiability handle.** Running an SDP solver on the canonical operator-selection problem at $q$-values near each metallic ratio reveals measurable signs of degeneracy: rising condition-number of the KKT system, multiple optimal solutions reported by the solver, and $y_i^*$ values dropping to tolerance for all $i$ simultaneously. Each observation tests the algebraic identification.
<!-- FILE_END: sdp-degeneracy-at-metallic-coincidence.md -->

<!-- FILE_START: universal-braid-branching.md -->
**Proposition.**
*For any braid $K$ on $3$ strands and any partition $\lambda \vdash k$ with $k \geq 3$, the Frobenius character of $K$ in the irreducible representation $\rho_\lambda$ of $H_k(R, q)$ is:*

$$
  \chi(K, \lambda)
  = f^{\lambda/[3]} \cdot \chi_K^{\mathrm{sym}}
  + f^{\lambda/[2{,}1]} \cdot \chi_K^{\mathrm{std}}
  + f^{\lambda/[1^3]} \cdot \chi_K^{\mathrm{alt}}
$$

*where $f^{\lambda/\mu} = |\mathrm{SYT}(\lambda/\mu)|$ counts saturated chains from $\mu$ to $\lambda$ in Young's lattice. The three base characters compute once from the Hoefsmit seminormal form:*

| *Knot $K$* | *$\chi_K^{\mathrm{sym}}$* | *$\chi_K^{\mathrm{std}}$* | *$\chi_K^{\mathrm{alt}}$* |
|:---:|:---:|:---:|:---:|
| *$4_1$ (figure-eight)* | *$1$* | *$2 - [3]_q$* | *$1$* |
| *$B_3$ (Borromean)* | *$1$* | *$(2 - [3])([3]^2 - 4[3] + 1)$* | *$1$* |
| *unknot (identity)* | *$1$* | *$2$* | *$1$* |

**Archimedean specialisation (§7c).** The character values $\chi^{\mathrm{sym}}, \chi^{\mathrm{alt}}$ and skew-SYT counts are stated as real numbers, forming the archimedean evaluations of the generic $\mathrm{Chebyshev}/\mathfrak{sl}_2$ branching over $[\mathrm{CommRing}\ R]$.
<!-- FILE_END: universal-braid-branching.md -->

<!-- FILE_START: hoefsmit-scattering-pipeline.md -->
**Proposition (conditional on [`conj:hyperbolic-volume-transcendence`](#conj:hyperbolic-volume-transcendence) and `rem:baryon-period-ratio`).**
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

*Formal asymptotic content. The truncation $\mathrm{MAE}(k) \leq C_0 \cdot [2]_q^{-2(k-3)}$ has $\operatorname{ordw}\bigl(\mathrm{MAE}(k)\bigr) = -2(k-3)\,\operatorname{ordw}([2]_q)$; see Big-O via $\operatorname{ordw}$ and the body asymptotics catalog.*

**Archimedean specialisation (§7c).** The scattering-amplitude vanishing test is stated over real inputs $v_1,v_2,v_3 : \mathbb{R}$ with real coefficients. These form the archimedean evaluations of the generic Hoefsmit pipeline over $[\mathrm{Field}\ R]$.
<!-- FILE_END: hoefsmit-scattering-pipeline.md -->

<!-- FILE_START: hecke-convergence-bound.md -->
**Proposition (convergence bound).**
*Let $\mathcal{A}$ be the active set of partitions that dominate the Hoefsmit trace. The difference between the full trace $\mathrm{tr}_M(W)$ and the restricted trace over $\mathcal{A}$ is bounded by:*

$$
  \left| \mathrm{tr}_M(W) - \sum_{\lambda \in \mathcal{A}} W_\lambda \, \mathrm{tr}_{\rho_\lambda}(W) \right|
  \;\leq\;
  C \cdot q^{- \Delta}
$$

*where $\Delta$ is the gap in content norm between the active set and the next-leading partition, and $C$ depends only on the Coxeter length of $W$.*

This bounds the error introduced by truncating the trace to the dominant channels. The algebraic convergence relies on the rapid decay of the quantum dimensions $W_\lambda$ outside the active set. The gap $\Delta$ grows linearly with the strand count $n$, driving the asymptotic suppression of off-shell configurations.
<!-- FILE_END: hecke-convergence-bound.md -->

<!-- FILE_START: algebraic-quantum-volume.md -->
**Definition (Algebraic Quantum Volume).**
*Let $W \in H_n(q)$ be a knot operator representing a confined state. The **algebraic quantum volume** of $W$ is its full canonical Markov trace over $\mathbb{Z}[q^{\pm 1/2}]$:*

$$
  \mathrm{Vol}_{\mathrm{alg}}(W)
  \;:=\; \mathrm{tr}_M(W)
  \;=\; \sum_{\lambda \vdash n} W_\lambda \, t_\lambda(W)
$$

*where $W_\lambda$ are the quantum dimensions and $t_\lambda(W)$ are the irreducible character traces.*

This defines the exact algebraic quantity that governs the mass expansion. The algebraic volume encodes both the knot topology (via $t_\lambda$) and the algebraic space structure (via $W_\lambda$). The archimedean realisation $\rho_\infty$ projects this polynomial into the physical binding energy.

**Structure of the sum.** The volume decomposes into independent channel contributions. Each channel $\lambda$ corresponds to a distinct phase of the $n$-nucleon cluster. The standard partition $(n-1, 1)$ carries the primary interaction strength, while the trivial partition $(n)$ acts as a scalar background field.

**Substrate isolation.** The algebraic volume computes entirely within the categorical substrate, before any numerical evaluation at $q_0$. It represents the pure combinatorial content of the mass formula. The convergence of the $z$-Habiro expansion depends crucially on the algebraic properties of this un-evaluated polynomial.
<!-- FILE_END: algebraic-quantum-volume.md -->

<!-- FILE_START: habiro-ring.md -->
**Definition (Habiro ring).**
*Let $R = \mathbb{Z}[q]$. The **$q$-Habiro ring** $\widehat{\mathbb{Z}[q]}_q$ is the inverse limit of the polynomial rings $R / ( (q; q)_n )$ as $n \to \infty$, where $(q; q)_n = \prod_{k=1}^n (1 - q^k)$ is the $q$-Pochhammer symbol:*

$$
  \widehat{\mathbb{Z}[q]}_q
  \;:=\;
  \varprojlim_n \frac{\mathbb{Z}[q]}{((q; q)_n)}.
$$

*Elements of the $q$-Habiro ring are formal power series of the form $\sum_{n=0}^\infty c_n(q) \, (q; q)_n$ with $c_n \in \mathbb{Z}[q]$.*

The Habiro ring completes the polynomial ring $\mathbb{Z}[q]$ at the cyclotomic ideals. It forms the natural home for quantum topological invariants evaluated at roots of unity, where the terms $(q; q)_n$ vanish for $n$ large enough, truncating the infinite series to a finite sum.

**Application to QOU.** The algebraic quantum volume evaluates as a finite sum precisely because its components belong to a generalized Habiro ring where the truncation depth connects to the physical shell structure.
<!-- FILE_END: habiro-ring.md -->

<!-- FILE_START: habiro-expansion-atomic.md -->
**Proposition (atomic Habiro expansion).**
*The algebraic quantum volume of a confined atom $\mathfrak{H}$ admits a $q$-Habiro expansion:*

$$
  \mathrm{Vol}_{\mathrm{alg}}(\mathfrak{H})
  \;=\;
  \sum_{n=0}^N c_n(q) \, (q; q)_n
$$

*where the truncation depth $N$ correlates with the number of valence nucleons.*

This proposition guarantees that the binding energy formula terminates algebraically when evaluated at a root of unity. The coefficients $c_n(q)$ determine the specific shell contributions. This structure bridges the categorical operator traces to the empirical magic-shell mass phenomenology.
<!-- FILE_END: habiro-expansion-atomic.md -->

<!-- FILE_START: z-habiro-ring.md -->
**Definition (z-Habiro ring).**
*Let $R = \mathbb{Z}[q^{\pm 1}][z]$. The **$z$-Habiro ring** $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$ is the inverse limit of the quotient rings $R / (P_n(q, z))$ as $n \to \infty$, where $P_n(q, z) = \prod_{k=1}^n (1 - q^{-k}z)$ is the $z$-Pochhammer analog:*

$$
  \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z
  \;:=\;
  \varprojlim_n \frac{\mathbb{Z}[q^{\pm 1}][z]}{(P_n(q, z))}.
$$

*Elements are formal series $\sum_{n=0}^\infty c_n(q, z) \, P_n(q, z)$ with $c_n \in \mathbb{Z}[q^{\pm 1}][z]$.*

The $z$-Habiro ring provides the algebraic completion needed to formalize the brane-tower contributions. The infinite product $\Phi_q(z) = \prod_{k\geq 1} (1 - q^{-k}z)^{-1}$ is ill-defined as a polynomial but exists as a formal limit within this completion.

**Role in the mass formula.** The transient (brane-tower) component of the Hecke mass element lives naturally in the $z$-Habiro ring. Its evaluation at physical $(q, z)$ values relies on the algebraic truncation properties of this ring.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$). Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: z-habiro-ring.md -->

<!-- FILE_START: quantum-dilog-convergence.md -->
**Proposition (convergence of the quantum dilogarithm).**
*Let $q \in \mathbb{R}$ with $1 < q$, and let $z \in \mathbb{R}$ with $|z| < q$. Then the quantum dilogarithm*

$$
  \Phi_q(z) \;=\; \prod_{k \geq 1} \bigl(1 - q^{-k} z\bigr)^{-1}
$$

*is multipliable: the infinite product converges to a well-defined, non-zero real number.*
<!-- FILE_END: quantum-dilog-convergence.md -->

<!-- FILE_START: brane-tower-z-habiro.md -->
The mass-endomorphism conjecture states that the Hecke mass element $\Phi_{\mathrm{mass}}$ admits a closed-form NF decomposition. Its **transient (brane-tower) component** is the sum

$$
  \Phi_{\mathrm{mass}}^{\mathrm{trans}}(\beta)
  \;=\;
  \sum_{i=1}^{N} \Phi_q(z_i),
$$

where $z_i = |\hat{V}_i^{\mathrm{full}}|$ are the per-generator additive Wedderburn traced-volume magnitudes, and $\Phi_q$ is the quantum dilogarithm.

For low isotopes $\{D, T, {}^3\mathrm{He}\}$, the per-generator volumes satisfy $z_i \in [0.85, 1.0]$—just below the first pole of $\Phi_q$ at $z = q_0 \approx 1.11$. Canonical evaluations $\Phi_q(0.989) \approx 6.7 \times 10^5$ and $\Phi_q(1) \approx 9 \times 10^5$ show each summand is enormous; the analytic brane tower dominates the mass formula by orders of magnitude beyond the empirical binding.

Two regularizations exist but neither uniformly closes the gap:
1. **Yekutieli truncation** at GB filtration depth $k_{\max}$ (empirical, not structural).
2. **$q$-Habiro completion**, regularizing in $q$, not $z$.

## Statement

**Conjecture (brane tower in $z$-Habiro).**
*Let $\mathfrak{H}$ be a confined particle/atom with per-generator volumes $\{\hat{V}_i(q)\}_{i=1}^{N}$ in $\mathbb{Z}[q^{\pm 1/2}]$. The brane-tower partial sums form a Cauchy sequence in the $z$-Habiro topology as $N$ varies. Their limit exists as an algebraic element $\widetilde{\Phi}_q^{\mathrm{tower}}(\beta) \in \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$, well-defined purely algebraically.*

*Furthermore, there exists a **canonical level-selection rule***

$$
  n_\star \;:\; \{\text{confined particles}\} \;\longrightarrow\; \mathbb{N}_{\geq 1},
  \qquad
  \mathfrak{H} \;\longmapsto\; n_\star(\mathfrak{H}),
$$

*derivable from QOU substrate data alone, such that the cyclotomic projection evaluated at $q = q_0$ and $z = z_i$ recovers the empirical brane-tower contribution to the binding $B(\mathfrak{H})$ uniformly across atoms.*

## Consequences of the conjecture

If true, the conjecture:
1. **Replaces the analytic infinite product** $\Phi_q(z)$ with an algebraic element.
2. **Promotes Yekutieli truncation** to a **structural cyclotomic projection** at a canonical level.
3. **Predicts the level-selection rule** $n_\star$ structurally.

## The open component: $n_\star$

The level-selection rule $n_\star$ forms the open part. A correct $n_\star$ must be a structural invariant of $\mathfrak{H}$, reproduce the empirical $B(\mathfrak{H})$ across atoms, and be derivable without external calibration.

**Empirical observation.** A uniform-depth canonical evaluation sweeping $k \in \{1, 2, 3, 4, 5, 6, 8, 10\}$ across $\{D, T, {}^3\mathrm{He}\}$ shows:
1. The absolute formula overshoots at every uniform $k$.
2. The subtractive form has a sign-flip at $k = 2$.
3. ${}^3\mathrm{He}$ overshoots at every $k \geq 2$ in subtractive form.

## Relation to the $q$-Habiro picture

The two completions remain independent. The full picture forms a bicompletion at the bigraded ideal generated by both $(q;q)_n$ and $P_n(q,z)$, where colored Jones data and brane-tower data coexist. Construction of the bicompletion is open.

## Falsifiability

The conjecture is falsifiable by computation:
1. Pick a candidate $n_\star$ rule.
2. Compute the projection at $q_0$ for each isotope.
3. Form the binding $B(\mathfrak{H})$.
4. Compare with the AME values $\{2.224566, 8.481798, 7.71806\}$ MeV.

A candidate rule closing all three to within $\sim 5\%$ without per-atom retuning constitutes the empirical signature.

## Surviving claims after closure attempts

Six candidate families have been probed and refuted. The remaining claims are:
1. **Algebraic Cauchy-limit claim**: Remains untouched and open. The analytic prerequisite is proved. The sole algebraic gap is identifying which coefficient family reproduces $\Phi_q$.
2. **$n_\star$ existence claim**: Refuted across probed forms; remains open.

## Structural finding: pair-knot operators are selected at closed shells

Independent of the refuted forms, the LP dual active set distinguishes the pair-knot composites $\sigma_{pp}, \sigma_{nn}$ from per-generator operators exactly at magic configurations, exposing the operator-level signature of shell closure.

## Structural finding: $Z \leftrightarrow N$ isospin symmetry

At the canonical Markov-trace operator-volume level, the two magic-shell sub-braids are isomorphic Hecke elements: $\mathrm{tr}_M(\sigma_{pp}) = \mathrm{tr}_M(\sigma_{nn}) = 0.0622$, rendering $Z \leftrightarrow N$ isospin symmetry exact.

## Structural conclusion

No probed choice recovers the light-isotope binding uniformly; the ${}^3\mathrm{He}$ gap represents a structural deficit at $A=3$, not an operator-volume choice.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$). Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: brane-tower-z-habiro.md -->

<!-- FILE_START: hoefsmit-ew-cell-content.md -->
**Theorem (Hoefsmit cell-content identification of EW triplet).**
*Let $R$ be the categorical coefficient ring with $q \in R$ generic. The electroweak force-carriers $W^\pm, Z, H$—identified topologically as the 2-component torus links $T(2,4), T(2,6), T(2,8)$ on Bring's surface—are realised inside $\mathrm{End}_R(V^{\otimes 6})$ as the **disjoint-strand-pair** Hoefsmit projectors:*

$$
  W \;\longleftrightarrow\; \sigma_1^{\,4} \;\;(\text{strands 1--2}),
  \quad
  Z \;\longleftrightarrow\; \sigma_3^{\,6} \;\;(\text{strands 3--4}),
  \quad
  H \;\longleftrightarrow\; \sigma_5^{\,8} \;\;(\text{strands 5--6}).
$$

*Strand count $n = 6$ is the **minimum** at which all three carriers admit simultaneous non-trivial action with pairwise-commuting generators. The pure-eigenspace tableaux multiplicities identify eight pairwise-orthogonal projectors.*

### Statement (formal)

For $n = 6$, the standard Young tableaux supply the Hoefsmit seminormal basis. A tableau is **pure for $(\sigma_1, \sigma_3, \sigma_5)$** if all three generators act diagonally. The enumeration shows exactly **20 such pure tableaux**, distributed across eight sym/alt eigenvalue patterns.

### Minimality of $n = 6$

Each EW carrier acts on a single strand-pair. Three carriers need three disjoint strand-pairs. For $n < 6$, carriers share strand-pairs, their generators no longer commute, and the simultaneous-eigenspace decomposition degenerates.

### Refinement: coupling via interface knot

The disjoint-product framing treats $W, Z, H$ as independent. The corrected EW braid uses an **interface knot** $\bowtie_K \in H_6(q)$ to mediate the coupling, analogous to the inter-nucleon interface in the deuteron derivation. The corrected braid is:

$$
  \beta_{\rm EW}(\bowtie_K)
  \;:=\;
  \sigma_1^{\,4} \cdot \bowtie_K^{(W \to Z)} \cdot \sigma_3^{\,6}
  \cdot \bowtie_K^{(Z \to H)} \cdot \sigma_5^{\,8} \cdot \bowtie_K^{(H \to W)}.
$$

This modifies pattern multiplicities, impacts bar-self-duality, gives the Higgs-vev automorphism a concrete form, and twists the 8 pure patterns.

### Resolution of the dimension-collapse issue

The six EW projectors live as rank-1 to rank-3 projectors in $\mathrm{End}_R(V^{\otimes 6})$. They sit alongside two non-EW projectors (vacuum and fully-broken), resolving the dimension-collapse issue of the $H_2(q)$-only completeness sum.

### The Plancherel weight is a degenerate special case

The earlier Plancherel-weighted multiplier framing is incorrect. The structural multiplier is the direct unweighted trace $\mathrm{tr}_{\rm pure}$, which preserves bar-self-duality automatically from the disjoint-strand-pair construction.

### Implication for $N_v$ derivation

The constrained-PSLQ basis for $N_v$ must use the direct cell-content trace $\mathrm{tr}_{\rm pure}$ as the structural input, demoting the Plancherel framing to a degenerate special case.

### Historical alignment: quaternionic electroweak theory

The disjoint-strand-pair identification parallels Morita's quaternionic formulation of the electroweak sector. The QOU tetraplectic boundary supplies a geometric home for the $\mathrm{SU}(2)$ structures. The unit-quaternion actions are norm-preserving and commute; identifying these algebraic actions with physical carriers is an interpretive alignment, not a derivation.
<!-- FILE_END: hoefsmit-ew-cell-content.md -->

