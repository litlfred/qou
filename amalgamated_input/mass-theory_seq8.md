<!-- FILE_START: intro-hoefsmit-convergence-atomic.md -->
The Hoefsmit basis for the Hecke algebra is the categorical
analogue of the Young orthogonal form for the symmetric group:
it diagonalises the Jucys–Murphy operators and exposes the
content-grading that controls the binding-energy formula's
$q$-expansion.  This section assembles the universal
braid-branching identity that drives the Hoefsmit construction,
proves its convergence at the substrate parameter, and exhibits
the atomic-shell evidence that pins the convergence rate
empirically.

The arc proceeds in three layers.  The first six blocks
establish the universal braid-branching formula, prove the
Hoefsmit basis exists in the categorical setting, and reduce
the convergence question to a polynomial inequality in the
substrate parameter.  The middle blocks prove convergence at
$q_0 \approx 1.1097$ and bound the rate, identifying the
leading correction term.  The closing blocks survey the
atomic-shell evidence — the categorical predictions for the
$1s$, $2s$, $2p$, ..., shell sequence and the empirical
agreement with the noble-gas closure pattern.

The output is the validated Hoefsmit basis with explicit
content-grading, which the next section's Markov-axiom analysis
exploits to derive the closed-form $\chi$-characters.  The
atomic-shell evidence is the chapter's strongest empirical
validation of the substrate-level construction; readers can
take it as the chapter's primary cross-check.
<!-- FILE_END: intro-hoefsmit-convergence-atomic.md -->

<!-- FILE_START: operator-selection-lp.md -->
The confinement LP ([confinement LP](#prop:confinement-lp)) selects the
Borromean link $\mathcal{B}_3$ as the unique optimizer over the $6$-element
NF basis of $H_3(q)$.  We now formulate the **general LP** for knot operator
selection in $H_n(q)$ for arbitrary strand number $n$, with the confinement
LP recovered as the special case $n = 3$, $d = 6$.

## Input / Output

**Input.**

- Strand number $n \geq 2$.
- A basis $\{b_1, \ldots, b_d\}$ of $H_n(q)$ (the NF basis, with
  $d = \dim H_n(q) = n!$).
- Markov traces $t_i = \mathrm{tr}_M(b_i)$ for each basis element.
- The $d \times d$ Frobenius Gram matrix
  $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$
  ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)).
- A target net value $n_{\mathrm{target}} \in \mathbb{R}_{>0}$
  (the normalised categorical mass of the desired state).

**Output.**

- The optimal coefficient vector $x^* \in \mathbb{R}^d$ such that
  $\Phi^* = \sum_{i=1}^{d} x_i^* b_i$ is the minimum-action knot
  operator satisfying all Frobenius positivity and net constraints.
- The dual certificate $(y_0^*, y^*)$ proving optimality.

## Primal program (operator selection)

**Proposition (general operator selection LP).**
*The knot operator $\Phi = \sum_{i=1}^{d} x_i b_i \in H_n(q)$ for a
target interaction with net value $n_{\mathrm{target}}$ is the solution
of the linear program:*

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

*where $M > 0$ is a sufficiently large constant ensuring boundedness of
the feasible polyhedron.*

The objective $\sum_{i} t_i x_i = \mathrm{tr}_M(\Phi)$ is the categorical
action ([knot operator selection](#prop:knot-operator-selection), part iv).
Minimizing it selects the operator of least action among all operators
compatible with the Frobenius structure.

The Frobenius positivity constraints $Gx \geq 0$ encode the
demand--supply balance: $\Phi$ must pair non-negatively with every
basis element under the Frobenius inner product, so no channel
carries unbounded demand.

**LP over motivic shadows, not real numbers.**
*The data feeding the LP — Markov traces $t_i = \mathrm{tr}_M(b_i)$
and Frobenius Gram entries $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ —
are formal elements of $\mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$,
hence elements of the Habiro completion $\widehat{\mathbb{Z}[q]}$
([Habiro ring](#def:habiro-ring)). The selection of the operator
$\Phi^* = \sum_i x_i^* b_i$ is therefore a combinatorial problem
over the **motivic shadows** of the
[motivic substrate](#def:motivic-substrate) — the algebraic data
of the Hecke algebra independently of any place-realization.
Strong duality (which produces the Borromean $\mathcal{B}_3$ as the
unique optimizer at $n=3$) is a purely algebraic consequence of the
LP; only **after** the optimizer is selected does the archimedean
realization $\rho_\infty$
([archimedean realization](#def:archimedean-realization-functor))
project the dual prices and objective value into physical binding
energies in $\mathbb{R}$. The non-archimedean realizations
$\rho_p$ recover the LP's cyclotomic shadows at each finite place
$p$ — useful for verifying optimality at roots of unity without
$\mathbb{C}$-evaluation.*

## Dual program (demand pricing)

By LP duality, the dual of the primal is:

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

For large $M$ the slack variables $s_i$ are driven to zero at optimality,
and the effective dual simplifies to:

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
**Remark.**
The dual variable $y_0$ is the **shadow price of the net constraint** --
the marginal cost (in units of categorical action) of increasing the
target mass $n_{\mathrm{target}}$ by one unit.  The dual variables
$y_i \geq 0$ are the **shadow prices of the Frobenius positivity
constraints** — channel demand prices.  A positive $y_i^*$ at optimality
indicates that the $i$-th Frobenius constraint is active (tight), meaning
the $i$-th channel is saturated.
<!-- FILE_END: operator-selection-lp-interpretation.md -->

<!-- FILE_START: sdp-degeneracy-at-metallic-coincidence.md -->
**Observation.**  At the cost-coincidence loci of the operator-selection
LP/SDP ([operator selection LP](#prop:operator-selection-lp)) — points
$q^* > 0$ where two cost coefficients $t_i(q)$ and $t_j(q)$ become equal
— the strict-complementarity condition fails and the SDP is
**degenerate**.  These loci coincide exactly with the metallic-ratio
ladder $\{\delta_n : n \in \mathbb{N}^+\}$.

**The mechanism.**  For the n=2 LP with basis $\{\gamma, \sigma_0\}$ of
$H_2(q)$ the cost coefficients are

$$
  t_1(q) \;=\; 2(q + q^{-1}),
  \qquad
  t_2(q) \;=\; q^2 - q^{-2}.
$$

A direct algebraic calculation (Lean-proved sorry-free in
`QOU.AlgebraicSubstrate.MetallicLPIdentities.silver_lp_coincidence`) gives

$$
  t_1(q) \;=\; t_2(q)
  \quad\Longleftrightarrow\quad
  q - q^{-1} \;=\; 2
  \quad\Longleftrightarrow\quad
  q \;=\; \delta_{\rm silver} \;=\; 1 + \sqrt{2}.
$$

At this q, the LP optimum is not a vertex but a **face** of the
feasible polytope: any feasible $x$ satisfying $x_1 + x_2 = n_{\rm target}$
achieves the same primal cost $t_1 x_1 + t_2 x_2 = t_1 \cdot n_{\rm target}$.
The dual shadow prices $y_i^*$ become non-unique (multiple optimal
$(y_0^*, y^*)$ values), strict complementarity fails, and the active set
$\mathcal{A} = \{i : y_i^* > 0\}$ is empty.  This is exactly the
**SDP-degeneracy** signature one would observe by running an
interior-point solver: rapid loss of conditioning, ambiguous
identification of binding constraints, multiple optimal solutions
returned.

**Empirical verification.**  The n=2 LP active-set sweep
(the formal derivation)
observed exactly this signature: below silver the active set was
$\{0\}$ (row 1 tight), AT silver it was $\emptyset$ (degenerate),
above silver it was $\{1\}$ (row 2 tight).  The degeneracy at silver
is the **first non-null result** in a series of five prior canonical
probes that all returned smooth observables.

**Structural significance.**  The metallic-ratio ladder
(see [`docs/audits/2026-06-08-metallic-q-hierarchy-proof.md`](../../../docs/audits/2026-06-08-metallic-q-hierarchy-proof.md)
and Lean module `QOU.AlgebraicSubstrate.MetallicHierarchy`)
sits on the algebraic side: $q = \delta_n$ is exactly where the Hecke scalar
$q - q^{-1}$ takes the integer value $n$, making $\sigma$ satisfy the
integer-coefficient quadratic $\sigma^2 = n \sigma + 1$.  Smooth
observables (Wenzl weights, Jones polynomial signs, n=3 per-block
character signs) do not see this discrete arithmetic structure because
they are rational functions of $q$ with no discontinuities.  The
**LP-vertex combinatorics** does see it: cost-coefficient coincidences
are algebraic events that translate the arithmetic of $q - q^{-1}$ into
a topological change of the optimum's face dimension.

**Physical interpretation.**  Identifying the silver coincidence with
the CFL phase transition of dense quark matter
([color superconductivity Borromean](#conj:color-superconductivity-borromean))
gives the empirical handle on this otherwise abstract algebraic
phenomenon: the CFL transition density $\rho_c$ is the physical
realization of the silver-coincidence point, and the SDP degeneracy
there IS the order-parameter discontinuity of the first-order CFL
transition.  Multiple metallic ratios on the ladder should correspond
to multiple phase transitions; the bar-mirror $\varphi^2 \approx 2.618$
of the deconfinement boundary $q_{\rm gold} = 1/\varphi^2$ is a
candidate for the CFL $\to$ gCFL (gapless / crystalline color
superconductor) boundary observed in dense-QCD phenomenology.

**Generalisation (conditional).**  For the strand-$n$ LP with basis
size $d_n = n!$, the cost coefficients $t_i(q)$ are rational functions
of $q$.  The pairwise coincidence equations $t_i(q) = t_j(q)$ have
rational-function solutions; those solutions that lie on the metallic
ladder constitute the set $S(n) \subseteq \{\delta_k : k \le n\}$ of
LP-degeneracy points for n strands.  For n=2 we have proven $S(2) = \{2\}$
(silver only).  For n=3 the categorical canonical evaluation (with Gram approximation)
also returned $\{\delta_{\rm silver}\}$; the full higher-strand
characterisation is the content of the conditional class
`SDPDegeneracyDetectsMetallic` in `MetallicLPIdentities.lean`.

**Falsifiability handle.**  This remark predicts that running an
SDP solver on the canonical operator-selection problem at q-values
near each metallic ratio should reveal **measurable** signs of
degeneracy: rising condition-number of the KKT system, multiple
optimal solutions reported by the solver, $y_i^*$ values dropping to
tolerance for all $i$ simultaneously.  Each such observation is a
direct test of the algebraic identification.
<!-- FILE_END: sdp-degeneracy-at-metallic-coincidence.md -->

<!-- FILE_START: universal-braid-branching.md -->
**Proposition.**
*For any braid $K$ on $3$ strands and any partition $\lambda \vdash k$
with $k \geq 3$, the Frobenius character of $K$ in the irreducible
representation $\rho_\lambda$ of $H_k(R, q)$ is:*

$$
  \chi(K, \lambda)
  = f^{\lambda/[3]} \cdot \chi_K^{\mathrm{sym}}
  + f^{\lambda/[2{,}1]} \cdot \chi_K^{\mathrm{std}}
  + f^{\lambda/[1^3]} \cdot \chi_K^{\mathrm{alt}}
$$

*where $f^{\lambda/\mu} = |\mathrm{SYT}(\lambda/\mu)|$ counts
saturated chains from $\mu$ to $\lambda$ in Young's lattice, and
the three base characters are computed once from the Hoefsmit
seminormal form
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)):*

| *Knot $K$* | *$\chi_K^{\mathrm{sym}}$* | *$\chi_K^{\mathrm{std}}$* | *$\chi_K^{\mathrm{alt}}$* |
|:---:|:---:|:---:|:---:|
| *$4_1$ (figure-eight)* | *$1$* | *$2 - [3]_q$* | *$1$* |
| *$B_3$ (Borromean)* | *$1$* | *$(2 - [3])([3]^2 - 4[3] + 1)$* | *$1$* |
| *unknot (identity)* | *$1$* | *$2$* | *$1$* |

**Archimedean specialisation (§7c).** The character values $\chi^{\mathrm{sym}}, \chi^{\mathrm{alt}}$ and skew-SYT counts are stated as real numbers, the archimedean evaluations of the generic $\mathrm{Chebyshev}/\mathfrak{sl}_2$ branching over $[\mathrm{CommRing}\ R]$; acknowledged here.
<!-- FILE_END: universal-braid-branching.md -->

<!-- FILE_START: hoefsmit-scattering-pipeline.md -->
**Proposition (conditional on
[`conj:hyperbolic-volume-transcendence`](#conj:hyperbolic-volume-transcendence)
and
`rem:baryon-period-ratio`).**
*The mass of a nuclear state with braid word $\beta \in B_n$ is
computed by the following pipeline, each stage of which is
functorial:*

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

*Stage 1 (Hoefsmit). Each crossing $\sigma_i$ in the braid word acts
on the Wedderburn--Artin block $\rho_\lambda$ via the Hoefsmit
seminormal matrix
([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)).
The scattering amplitude from tableau state $T$ to state $T'$
under crossing $\sigma_i$ is:*

$$
  W_{T \to T'} = \langle T' \mid \sigma_i \mid T \rangle
  = \begin{cases}
    a_\rho & T' = T \quad\text{(forward scattering)} \\
    b_\rho & T' = (T)_i \quad\text{(exchange scattering)} \\
    0 & \text{otherwise}
  \end{cases}
$$

*where $a_\rho = h/(1 - q^{-2\rho})$ is the $q$-deformed axial
distance and $b_\rho = \sqrt{a_\rho a_{-\rho} + 1}$ is the exchange
amplitude. The matrix is maximally sparse: at most $2$ nonzeros per
row.*

*Stage 2 (Markov trace). The product of Hoefsmit matrices over all
crossings in $\beta$ gives the braid representation matrix
$\rho_\lambda(\beta)$. The Markov trace sums over all
Wedderburn--Artin blocks:*

$$
  J_K(q) = \sum_{\lambda\,\vdash\,k}
  w_\lambda \cdot \frac{\chi_\lambda(\beta)}{\dim(\lambda)}
$$

*where $w_\lambda = \dim_q(\lambda)^2 / [k]_q!$ is the
Wedderburn--Artin weight and $\chi_\lambda(\beta) =
\mathrm{tr}(\rho_\lambda(\beta))$ is the Frobenius character
([Wedderburn--Artin trace identity](#prop:wedderburn-trace-identity)).*

*By the universal branching rule
([universal braid branching](#prop:universal-braid-branching)),
$\chi_\lambda(\beta)$ is determined by Young's lattice path counts
$f^{\lambda/\mu}$ and the three base characters
$\chi^{\mathrm{sym}}$, $\chi^{\mathrm{std}}$,
$\chi^{\mathrm{alt}}$.*

*Stage 3 (Observation frame). The fibre functor $\tau$ evaluates the
abstract Jones polynomial $J_K(q)$ on the knot complement
$S^3 \setminus K$. The evaluation is geometric, determined by
Thurston's geometrization
([Geom(K) alignment](#conj:geom-yekutieli-alignment)):*

$$
  \tau(J_K)
  = \sum_\lambda w_\lambda \cdot
    \frac{\chi_\lambda(\beta)}{\dim(\lambda)}
    \cdot \mathrm{Geom}(K)
$$

*The factor $\mathrm{Geom}(K)$ projects the algebraic trace into a
measurable observable: $\mathrm{Vol}(K)/\hbar_q^2$ for hyperbolic $K$
(mass/energy), $\mathrm{CS}(K) \cdot \hbar_q^2$ for torus $K$
(coupling phase), or $0$ for the unknot (vacuum).*

*Stage 4 (Physical mass). The mass is the norm of the evaluated
trace, scaled by the electron mass $m_e$
([topological mass formula](#prop:topological-mass-formula)):*

$$
  \mathfrak{m}(K) = m_e \cdot \mathrm{Geom}(K)
    \cdot \sum_\lambda w_\lambda \cdot
    \frac{\chi_\lambda(\beta)}{\dim(\lambda)}
$$

*At Hecke level $k$, this sum truncates to $p(k)$ partitions. The
truncation error satisfies:*

$$
  \mathrm{MAE}(k) \leq C_0 \times [2]_q^{-2(k-3)}
$$

*with convergence rate $[2]_q^2 \approx 4.04$ per level
([universal braid branching](#prop:universal-braid-branching)).*

*Proof.*
Each stage is proved separately:

**Stage 1** is [Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form).
The $q$-deformation of the classical axial distance $1/\rho$ to
$h/(1 - q^{-2\rho})$ follows from the Hecke relation
$\sigma_i^2 = h\sigma_i + 1$ and the requirement $\det = -1$ for each $2 \times 2$
block. The eigenvalues are $q$ (symmetric) and $-q^{-1}$
(antisymmetric), which are the eigenvalues of the universal
$R$-matrix $\check{\mathcal{R}}$ of $U_q(\mathfrak{sl}_2)$ restricted
to the isotypic component of type $\lambda$.

**Stage 2** is [Wedderburn--Artin trace identity](#prop:wedderburn-trace-identity).
The Markov trace $\mathrm{tr}_M$ factors through the
Wedderburn--Artin decomposition $H_k(R, q) \cong \bigoplus_\lambda
M_{d_\lambda}(\mathbb{C})$. The weight $w_\lambda$ ensures that
$\mathrm{tr}_M$ is the unique trace satisfying the Markov property
$\mathrm{tr}_M(x\sigma_k) = z \cdot \mathrm{tr}_M(x)$ for
$x \in H_k(R, q)$.

**Stage 3** is [Geom(K) alignment](#conj:geom-yekutieli-alignment).
The observation frame $\tau$ is the fibre functor of the
Tannakian category $(\mathbf{C}, A, \tau)$. On the τ-image
(geometric) side, its evaluation on the knot complement is determined
by τ-image Thurston geometrization and the Yekutieli rigid
dualizing complex: the UNIQUE non-degenerate pairing
$\langle \omega_A^\bullet, S^3 \setminus K \rangle_{\mathrm{Frob}}$
yields $\mathrm{Vol}(K)/\hbar_q^2$ for hyperbolic $K$ and
$\mathrm{CS}(K) \cdot \hbar_q^2$ for torus $K$. On the algebraic
side this is the [algebraic-quantum-volume](#def:algebraic-quantum-volume)
pairing in $\mathbb{Z}[q^{\pm 1/2}]$; the geometric reading
appears only after applying $\tau_{\mathrm{arch}}$. The universality
follows from the rigidity of $\omega_A^\bullet$ (Yekutieli): the
pairing is unique up to the scalar $\hbar_q^2$, and the scalar is
fixed by requiring that $\mathrm{Geom}(\bigcirc) = 0$ (vacuum
normalisation) and $\mathrm{Geom}(4_1) \cdot \hbar_q^2 =
\mathrm{Vol}(4_1)$ (the figure-eight knot defines $q_0$).

**Stage 4** is [topological mass formula](#prop:topological-mass-formula).
The convergence bound follows by induction on $k$ using the Pieri
rule for skew tableaux counts
([universal braid branching](#prop:universal-braid-branching)):
each level $k$ introduces $p(k) - p(k-1)$ new partitions whose
total Wedderburn--Artin weight is $O([2]_q^{-2})$ of the previous
level's weight, by Plancherel concentration.
$\square$

*Formal asymptotic content. The truncation
$\mathrm{MAE}(k) \leq C_0 \cdot [2]_q^{-2(k-3)}$ has
$\ordw\bigl(\mathrm{MAE}(k)\bigr) = -2(k-3)\,\ordw([2]_q)$;
see [Big-O via $\ordw$](#rem:conway-normal-form) and the
[body asymptotics catalog](#rem:body-asymptotics-catalog).*

**Archimedean specialisation (§7c).** The scattering-amplitude vanishing test is stated over real inputs $v_1,v_2,v_3 : \mathbb{R}$ with real coefficients; these are the archimedean evaluations of the generic Hoefsmit pipeline over $[\mathrm{Field}\ R]$, acknowledged here.
<!-- FILE_END: hoefsmit-scattering-pipeline.md -->

<!-- FILE_START: hecke-convergence-bound.md -->
**Proposition (conjectural).**
*Let $M_k(Z,N)$ denote the atomic mass predicted by the BW formula
with coefficients derived from $H_3(R, q)$ through $H_k(R, q)$ Wedderburn
decomposition.  Then for stable nuclei:*

$$
  \frac{|M_k(Z,N) - M_{\mathrm{obs}}(Z,N)|}{M_{\mathrm{obs}}(Z,N)}
  \leq C \cdot r^{-(k-3)}
$$

*with $C \approx 0.001$ and $r \approx 4$ (geometric convergence).*

*Evidence: $H_3$ (0.10%), $H_4$ (0.020%), $H_5$ (0.006%).
Geometric mean ratio $r \approx 4.1$.*

*Equivalently: each Hecke level halves the error twice.
For precision $10^{-j}$, need $k \geq \lceil 3 + 1.66\,j \rceil$.*

*The convergence rate $1/r \approx 0.25$ matches the QCD coupling
$\alpha_s \approx 0.3$ at nuclear scales to within 20%.  Each Hecke
level corresponds to one QCD loop order.*

*At $k = 11$: the model error drops below the $q_0$ measurement
uncertainty $\delta q/q = 1.22 \times 10^{-9}$.  Beyond $H_{11}$,
improving the model requires better measurement of $m_\mu/m_e$.*

*Formal asymptotic content. The geometric bound has
$\ordw\bigl(\mathrm{MAE}(k)\bigr) = -(k-3)\,\ordw(r)$ in the
surreal valuation; see [Big-O via $\ordw$](#rem:conway-normal-form)
and the [body asymptotics catalog](#rem:body-asymptotics-catalog).*
<!-- FILE_END: hecke-convergence-bound.md -->

<!-- FILE_START: algebraic-quantum-volume.md -->
**Definition.**
*The **algebraic quantum volume** of a braid element
$\beta \in H_n(R, q)$ is the product of traced volumes:*

$$
  \mathrm{Vol}_q(\beta)
  \;=\;
  \prod_{i=0}^{n-2} \hat{V}_i(q)
  \;\in\;
  \mathbb{Z}[q^{1/2}, q^{-1/2}]
$$

*where $\hat{V}_i(q) = z(q) \cdot a_i(q) + b_i(q)$ is the
traced volume of generator $i$, with $a_i(q)$ and $b_i(q)$
the Laurent polynomial entries of the transfer matrix chain
([Markov trace product](#thm:markov-trace-product)).*

*The algebraic quantum volume lives in
$\mathbb{Z}[q^{1/2}, q^{-1/2}]$ — the ring of Laurent
polynomials in $q^{1/2}$. It is an algebraic object.
Its real-valued archimedean shadow is obtained by
applying the QOU fibre functor*

$$
  \tau \;:\;\mathbf{C}\;\longrightarrow\;\mathbf{Arch},
$$

*restricted to its archimedean component
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
(see [archimedean realization functor](#def:archimedean-realization-functor)
and [Vol(K) factors through $\tau$](#prop:vol-through-tau)). Concretely,*

$$
  \Phi_1(\beta)
  \;:=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\;
  \ln\lvert\mathrm{Vol}_{q_0}(\beta)\rvert
  \;=\;
  \sum_{i=0}^{n-2} \ln\lvert\hat{V}_i(q_0)\rvert,
$$

*where $\tau_{\mathrm{arch}}$ acts on a generator $\hat{V}_i$ by
specializing $q \mapsto q_0$ at the archimedean place and taking
the absolute logarithm. The logarithm is not an extraneous
transcendental operation: it is the canonical map
$|\cdot|_\infty \to \log|\cdot|_\infty$ on the archimedean place
of the [adelic substrate](#def:adelic-substrate), packaged as the
$\tau_{\mathrm{arch}}$-image of the multiplicative quantum-volume
generator. Every archimedean physical observable derived from
$\mathrm{Vol}_q$ is the image of a categorical morphism under
$\tau_{\mathrm{arch}}$ — there is no other archimedean route.*

*The three Wedderburn invariants of the mass formula
([three-invariant mass formula](#thm:wedderburn-mass-formula))
correspond to three algebraic volumes:*

| Invariant | Algebraic volume | Ring |
|:----------|:-----------------|:-----|
| $\Phi_1$ | $\prod \hat{V}_i$ | trace of std rep |
| $\Phi_2$ | $\prod \det(M_i)$ | sym $\times$ alt product |
| $\Phi_3$ | $\prod (\lambda_i^{\mathrm{sym}}/\lambda_i^{\mathrm{alt}})$ | sym/alt ratio |

*Each factor is algebraic in $q$. The mass formula is the
$\tau_{\mathrm{arch}}$-image of the categorical product, evaluated
on the three Wedderburn channels:*

$$
  \mathcal{M}
  = M_{\mathrm{free}}
  + \alpha \cdot \ln\left\lvert
    \mathrm{Vol}_q^{(1)} \cdot
    \bigl(\mathrm{Vol}_q^{(2)}\bigr)^{-2[3]_q} \cdot
    \bigl(\mathrm{Vol}_q^{(3)}\bigr)^{H_A^2}
  \right\rvert_{q=q_0}
$$

*Every intermediate computation — ground-state ordering, electron
insertion, transfer matrix chain, partition traces — is algebraic
in $q$ and internal to $\mathbf{C}$; the only step that exits is
the final $\tau_{\mathrm{arch}}$, which is the unique boundary at
which categorical data crosses into archimedean geometry.*

*For the Habiro ring: the algebraic volume embeds into
$\widehat{\mathbb{Z}[q]}$ (the cyclotomic completion),
where it coexists with the colored Jones polynomials at all
roots of unity. The mass at $q_0$ is the evaluation at a
non-root-of-unity point.*

## Partial-product (q-Pochhammer) expansion

*Each generator volume $\hat{V}_i(q) = z(q)\, a_i(q) + b_i(q)$ admits
a $q$-Pochhammer partial-product expansion
([q-Pochhammer partial product](#def:q-pochhammer-partial-product))
of the form*

$$
  \hat{V}_i(q)
  \;=\;
  C_i(q) \cdot \Phi_{n_i}(x_i; q),
  \qquad
  \Phi_{n_i}(x_i; q)
  \;=\;
  \prod_{k=0}^{n_i - 1}\frac{1}{1 - x_i\, q^k},
$$

*with $C_i(q) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$ a Laurent prefactor
and $x_i$ the state variable at the $i$-th crossing. The full
algebraic volume*

$$
  \mathrm{Vol}_q(\beta)
  \;=\;
  \prod_{i=0}^{n-2} \hat{V}_i(q)
  \;=\;
  \Bigl(\prod_i C_i(q)\Bigr)
  \cdot
  \Bigl(\prod_i \Phi_{n_i}(x_i; q)\Bigr)
$$

*therefore exposes its **shared denominator** explicitly: the product
$\prod_i (x_i; q)_{n_i} \in \mathbb{Z}[q, x_1, \dots, x_{n-2}]$ is a
polynomial whose zero locus is the algebraic address of the JSJ-piece
cusps under the Archimedean realization
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
This factorisation does not change $\mathrm{Vol}_q(\beta)$ as a
Laurent polynomial; it only names the denominator structure that
the subsequent thimble / volume-tower derivations rely on.*
<!-- FILE_END: algebraic-quantum-volume.md -->

<!-- FILE_START: habiro-ring.md -->
**Definition.**
*The **Habiro ring** is the inverse limit*

$$
  \widehat{\mathbb{Z}[q]}
  \;=\;
  \varprojlim_n \;
  \mathbb{Z}[q] \big/ \bigl((q;q)_n\bigr)
$$

*where $(q;q)_n = (1-q)(1-q^2)\cdots(1-q^n)$ is the
$q$-Pochhammer symbol. It is the cyclotomic completion
of $\mathbb{Z}[q]$: every element specialises to
$\mathbb{Z}[\zeta]$ at every root of unity $\zeta$.*

The Habiro ring is the natural home for quantum invariants
because:

1. **Universality.** The colored Jones polynomials
 $J_N(K; q)$ for all $N$ coexist as a single element of
 $\widehat{\mathbb{Z}[q]}$ (Habiro, 2002). In
 $\mathbb{Z}[q, q^{-1}]$ alone, the $J_N$ are separate
 objects; in $\widehat{\mathbb{Z}[q]}$ they unify.

2. **Embedding.** The Laurent polynomial ring
 $\mathbb{Z}[q, q^{-1}]$ embeds into
 $\widehat{\mathbb{Z}[q]}$. The Hecke algebra
 $H_n(R, q) = \mathbb{Z}[q, q^{-1}][B_n] / (\sigma_i^2 -
   H_A\sigma_i - 1)$ and its normal form coefficients
 $c_w \in \mathbb{Z}[q, q^{-1}]$ embed accordingly.

3. **The algebraic quantum volume**
 ([algebraic quantum volume](#def:algebraic-quantum-volume))
 $\mathrm{Vol}_q(\beta) = \prod \hat{V}_i(q)$ is a
 finite product of Laurent polynomials, hence already in
 $\mathbb{Z}[q^{1/2}, q^{-1/2}]
   \subset \widehat{\mathbb{Z}[q^{1/2}]}$.

4. **Specialisation to volume.** At roots of unity
 $q = e^{2\pi i/N}$, the Kashaev invariant recovers the
 hyperbolic volume via:

 $$
     \lvert J_N(K; e^{2\pi i/N}) \rvert
     \;\sim\;
     \exp\!\Bigl(\frac{N}{2\pi}\,
       \mathrm{Vol}(S^3 \setminus K)\Bigr)
   $$

 At $q = q_0$ (our substrate parameter, not a root of
 unity), the evaluation gives the mass via the algebraic
 quantum volume.

The distinction between **nuclear volume** and **particle
volume** is:

- **Nuclear volume**
 $\mathrm{Vol}_q(\mathcal{N}(Z,N)) = \prod_{i=0}^{A-2}
  \hat{V}_i(q)$: a finite product in
 $\mathbb{Z}[q^{1/2}, q^{-1/2}]$. Already computed
 exactly by the transfer matrix.

- **Particle volume**
 $\mathrm{Vol}_q(K) = \prod_{n=1}^{\infty}
  (\text{tower contribution at level } n)$: an infinite
 product requiring the Habiro completion. This is the
 categorical version of the Volume Conjecture.
<!-- FILE_END: habiro-ring.md -->

<!-- FILE_START: habiro-expansion-atomic.md -->
For an atomic closed braid the Habiro expansion of the Markov trace
([Habiro completion](#prop:full-pole-structure-mass-trace))
**terminates**: only finitely many cyclotomic coefficients $a_m$
are nonzero. This corollary records the explicit termination bound
and integrality, with a constructive proof by sequential cyclotomic
division.

**Corollary.**
*Let $T_w(Z, N) \in H_{3A}(q)$ be the atomic-braid image for
$A = Z + N$ nucleons
([categorical mass, Markov](#prop:categorical-mass-markov)), and
let $u = q^{1/2}$. Then there exists a denominator $D(u)$ — a
finite product of cyclotomic polynomials — and a Laurent
polynomial $p(u) := D(u) \cdot \mathrm{tr}_M(T_w(Z, N), u^2) \in \mathbb{Z}[u, u^{-1}]$
admitting the finite Habiro expansion*

$$
  p(u) \;=\; \sum_{m=0}^{m_{\max}} a_m(u)\,(u; u)_m,
  \qquad (u; u)_m = \prod_{k=1}^{m}(1 - u^k),
$$

*with*

1. **Integrality.** *$a_m(u) \in \mathbb{Z}[u]$ for every $m$.*
2. **Degree bound.** *$\deg_u a_m(u) \leq m$.*
3. **Termination.** *$a_m = 0$ for $m > m_{\max}$, and
   $m_{\max} \leq \lceil \sqrt{2 \deg_u p(u)} \rceil$.*
4. **Uniqueness.** *Given $\deg a_m \leq m$, the sequence
   $\{a_m\}$ is uniquely determined by $p$.*
<!-- FILE_END: habiro-expansion-atomic.md -->

<!-- FILE_START: z-habiro-ring.md -->
**Definition (proposed; conjectural backing).**
*The **$z$-Habiro ring** is the inverse limit*

$$
  \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z
  \;:=\;
  \varprojlim_n \;
  \mathbb{Z}[q^{\pm 1}][z] \big/ \bigl(P_n(q, z)\bigr),
$$

*where*

$$
  P_n(q, z)
  \;:=\;
  \prod_{k=1}^{n} \bigl(1 - q^{-k} z\bigr)
  \;=\;
  (z q^{-1};\, q^{-1})_n
$$

*is the $q$-Pochhammer symbol in the variable $z$ at base $q^{-1}$.
The completion is taken with respect to the descending chain of
ideals $I_n = (P_n(q, z))$.*

The construction is parallel to the [Habiro ring](#def:habiro-ring)
$\widehat{\mathbb{Z}[q]}$ — the latter is the cyclotomic completion of
$\mathbb{Z}[q]$ at $((q;q)_n)$, the former is the cyclotomic completion of
$\mathbb{Z}[q^{\pm 1}][z]$ at $((zq^{-1};q^{-1})_n)$. The q-side
construction is now established for the Markov trace
([Habiro completion of mass trace](#prop:full-pole-structure-mass-trace),
[atomic Habiro expansion](#cor:habiro-expansion-atomic) — termination
at $m_{\max} \leq \lceil\sqrt{2 \deg p}\rceil$), so the z-side
parallel below is the natural extension to the brane-tower /
exceptional-divisor variable.

| Variable | Cyclotomic ideal generator | Completion | Universal element |
|:---|:---|:---|:---|
| $q$ | $(q;q)_n = \prod_{k=1}^{n}(1-q^k)$ | $\widehat{\mathbb{Z}[q]}$ | colored Jones $J_K$ |
| $z$ (this block) | $P_n(q,z) = \prod_{k=1}^{n}(1-q^{-k}z)$ | $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$ | brane-tower element $\widetilde{\Phi}_q^{\mathrm{tower}}$ (conjectural) |

## Choice of ideal

The poles of the analytic quantum dilogarithm
([quantum dilogarithm](#cor:quantum-dilogarithm))
$\Phi_q(z) = \prod_{k=1}^{\infty}(1 - q^{-k}z)^{-1}$ are exactly at
$z = q^k$ for $k \geq 1$. The cyclotomic-in-$z$ ideal $I_n = (P_n(q,z))$
is generated by the polynomial whose zero locus is the first $n$ poles
of $\Phi_q$. Successive partial products $P_n$ form a descending chain
$I_1 \supset I_2 \supset \cdots$ (each $P_{n+1}$ contains $P_n$ as a
factor), so the inverse limit is well-defined.

## Cyclotomic projections

For each $n \geq 1$ there is a **level-$n$ cyclotomic projection**

$$
  \pi_n^{(z)} \;:\; \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z
  \;\longrightarrow\; \mathbb{Z}[q^{\pm 1}][z] / (P_n(q, z)).
$$

Evaluation in the quotient is finite — every class has a unique
representative of degree $< n$ in $z$ — so $\pi_n^{(z)}$ acts as a
**structural truncation** at depth $n$. This generalizes the
[Yekutieli finite-slice truncation](#prop:atom-knot-mass-derivation)
from an ad-hoc cutoff to a structural quotient: the truncation depth
$n$ becomes a parameter labelling cyclotomic quotients, parallel to
how $N$ labels the $N$-th colored Jones in the $q$-Habiro picture.
## Relation to existing blocks

- The [algebraic quantum volume](#def:algebraic-quantum-volume)
  $\mathrm{Vol}_q(\beta) = \prod_{i} \hat{V}_i(q)$ embeds as a constant
  in $z$ into $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$ via the inclusion
  $\mathbb{Z}[q^{\pm 1}] \hookrightarrow \mathbb{Z}[q^{\pm 1}][z]$.
- The [Habiro ring](#def:habiro-ring) $\widehat{\mathbb{Z}[q]}$ embeds
  as the $z$-constant subring fixed by the projection $z \mapsto 0$.
- The combined object — a bicompletion in both $q$ and $z$ — would
  carry both the colored-Jones-coexistence (in $q$) and the
  brane-tower-coexistence (in $z$) data simultaneously. Construction
  of the bicompletion is open.

## Discussion

This definition is **proposed structure**, not established. The
parallel with the $q$-Habiro ring is formal and the construction of
$\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$ as an inverse limit is
straightforward, but its **utility** depends on the conjecture that
the brane-tower partial sums are Cauchy in this topology and that
their limit recovers the empirical mass under cyclotomic projection
at a canonically determined depth. See
[brane tower in $z$-Habiro](#conj:brane-tower-z-habiro).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: z-habiro-ring.md -->

<!-- FILE_START: quantum-dilog-convergence.md -->
**Proposition (convergence of the quantum dilogarithm).**

*Let $q \in \mathbb{R}$ with $1 < q$, and let $z \in \mathbb{R}$ with
$\lvert z \rvert < q$. Then the quantum dilogarithm*

$$
  \Phi_q(z) \;=\; \prod_{k \geq 1} \bigl(1 - q^{-k} z\bigr)^{-1}
$$

*is multipliable: the infinite product converges to a well-defined,
non-zero real number.*
<!-- FILE_END: quantum-dilog-convergence.md -->

<!-- FILE_START: brane-tower-z-habiro.md -->
The [mass-endomorphism conjecture](#conj:mass-endomorphism) states that
the Hecke mass element $\Phi_{\mathrm{mass}}$ admits a closed-form NF
decomposition. Its **transient (brane-tower) component** is the sum

$$
  \Phi_{\mathrm{mass}}^{\mathrm{trans}}(\beta)
  \;=\;
  \sum_{i=1}^{N} \Phi_q(z_i),
$$

where $z_i = |\hat{V}_i^{\mathrm{full}}|$ are the per-generator *additive
Wedderburn* (regular-representation) traced-volume magnitudes
([mass-endomorphism tower](#prop:mass-endomorphism-tower)) and
$\Phi_q$ is the [quantum dilogarithm](#cor:quantum-dilogarithm). The
single-channel $\hat{V}_i = z\,a_i + b_i$ of
[algebraic quantum volume](#def:algebraic-quantum-volume) is the standard-rep
projection alone — for the proton $\sigma_0$ it is $\approx 1.146 > q_0$, past
the $\Phi_q$ radius — so the bounded brane-tower argument is the full
regular-representation trace, not this single channel.

For low isotopes $\{D, T, {}^3\mathrm{He}\}$, the per-generator
volumes satisfy $z_i \in [0.85, 1.0]$ — just below the first pole of
$\Phi_q$ at $z = q_0 \approx 1.11$. canonical
$\Phi_q(0.989) \approx 6.7 \times 10^5$ and $\Phi_q(1) \approx 9 \times 10^5$,
so each summand is enormous and the analytic brane tower dominates the
mass formula by orders of magnitude beyond the empirical AME binding.

Two regularizations have been documented but neither uniformly closes
the gap (see [mass-endomorphism conjecture §"Two distinct convergence problems"](#conj:mass-endomorphism)):

1. **Yekutieli truncation** at GB filtration depth $k_{\max}$ — works
   for $D$ ($k_{\max}=2$, error $\sim 22\%$), grossly fails for $T$
   ($k_{\max}=9$, error $\sim 17000\%$). Empirical, not structural.
2. **$q$-Habiro completion** (the
   [Habiro ring](#def:habiro-ring) at $((q;q)_n)$) — regularizes in
   the variable $q$, not $z$. Does not change the analytic value of
   $\Phi_q$ at fixed $z$. The $q$-side termination
   ([atomic Habiro expansion](#cor:habiro-expansion-atomic), proved:
   $m_{\max} \leq \lceil\sqrt{2 \deg p}\rceil$) is the q-analog of
   the parallel claim conjectured for $z$ below.

## Statement

**Conjecture (brane tower in $z$-Habiro).**

*Let $\mathfrak{H}$ be a confined particle/atom with per-generator
volumes $\{\hat{V}_i(q)\}_{i=1}^{N}$ in
$\mathbb{Z}[q^{\pm 1/2}]$. The brane-tower partial sums*

$$
  \widetilde{\Phi}^{(N)}(\beta)
  \;:=\;
  \sum_{i=1}^{N}
    \mathrm{Trunc}_{<n}\!\bigl[\Phi_q(\hat{V}_i)\bigr]
  \;\in\;
  \mathbb{Z}[q^{\pm 1}][z] / (P_n(q, z))
$$

*(where $\mathrm{Trunc}_{<n}$ takes the unique representative of
degree $< n$ in $z$ in the cyclotomic-in-$z$ quotient)
form a Cauchy sequence in the* $z$*-Habiro topology
([$z$-Habiro ring](#def:z-habiro-ring)) **as $N$ varies**. Their limit*

$$
  \widetilde{\Phi}_q^{\mathrm{tower}}(\beta)
  \;\in\;
  \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z
$$

*exists as an algebraic element — well-defined purely algebraically,
with no analytic regularization required.*

*Furthermore, there exists a **canonical level-selection rule***

$$
  n_\star \;:\; \{\text{confined particles}\} \;\longrightarrow\;
  \mathbb{N}_{\geq 1},
  \qquad
  \mathfrak{H} \;\longmapsto\; n_\star(\mathfrak{H}),
$$

*derivable from QOU substrate data alone (e.g. confinement level
$\ell$, strand count $n_0$, GB filtration on $H_{n_0}(q)$,
or analogous structural invariants), such that the cyclotomic
projection*

$$
  \pi_{n_\star(\mathfrak{H})}^{(z)}\!\bigl(\widetilde{\Phi}_q^{\mathrm{tower}}(\beta_\mathfrak{H})\bigr)
$$

*evaluated at $q = q_0$ and $z = z_i$ recovers the empirical brane-tower
contribution to the binding $B(\mathfrak{H})$ uniformly across atoms,
not just for the single atom whose GB filtration depth happens to
match.*

## Consequences of the conjecture

If true, the conjecture:

1. **Replaces the analytic infinite product** $\Phi_q(z)$ — which has
   no algebraic home and blows up at $|z| \to q$ — with an algebraic
   element of $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$.
2. **Promotes Yekutieli truncation** from an ad-hoc cutoff at GB depth
   to a **structural cyclotomic projection** at a canonical level.
3. **Predicts the level-selection rule** $n_\star$ structurally — the
   single open computation reduces from "find the right Φ_q
   regularization" to "identify $n_\star$ from substrate data".

## The open component: $n_\star$

The level-selection rule $n_\star$ is **the open part**. Candidate
structural inputs:

See [Table 1](#tbl:brane-tower-z-habiro-table1-data).

A correct $n_\star$ must (i) be a structural invariant of
$\mathfrak{H}$, (ii) reproduce the empirical $B(\mathfrak{H})$ across
atoms when fed into $\pi_{n_\star}^{(z)}$, and (iii) be derivable from
the QOU substrate without external calibration.

**Empirical observation (uniform-$k$ sweep).** A
uniform-depth canonical evaluation
(the canonical formalism)
sweeping $k \in \{1, 2, 3, 4, 5, 6, 8, 10\}$ uniformly across
$\{D, T, {}^3\mathrm{He}\}$ shows:

1. **The absolute formula** $B = m_e \cdot \rho \cdot (\mathrm{tr}_M(T_w) + \mathrm{tower}^{(k)} + \sigma_{3A})$
   overshoots at every uniform $k$ — errors grow monotonically with
   $k$ ($+775\%$ at $k=1$, $+1.27 \times 10^6\,\%$ at $k=10$). No
   uniform absolute-form $k$ closes the gap.

2. **The subtractive form** $B = E_0 \cdot (\mathrm{tower}_{\mathrm{free}}^{(k)} - \mathrm{tower}_{\mathrm{atom}}^{(k)})$
   has a **sign-flip at $k = 2$**: for all three atoms,
   $\Delta\mathrm{tower}^{(k=1)} < 0$ but $\Delta\mathrm{tower}^{(k \geq 2)} > 0$.
   At $k = 2$:
   $B(D) \approx +1.74\,\mathrm{MeV}$ (err $-22\%$),
   $B(T) \approx +5.18\,\mathrm{MeV}$ (err $-39\%$),
   $B({}^3\mathrm{He}) \approx +18.05\,\mathrm{MeV}$ (err $+134\%$).

3. **${}^3\mathrm{He}$ overshoots at every $k \geq 2$ in subtractive
   form**, suggesting the per-generator volume list for ${}^3\mathrm{He}$
   carries a doubled $|\hat{V}| \approx 0.989$ contribution that the
   subtractive cancellation does not absorb. This is consistent with
   ${}^3\mathrm{He}$'s 8-generator list having two near-pole entries
   (positions 0 and 3), versus $D$'s single near-pole entry.

The sign-flip at $k = 2$ is structurally interesting: it is the
smallest depth that includes the **Hecke quadratic relation slice**
($\sigma_i^2 = (q - q^{-1})\sigma_i + 1$, two factors of $\Phi_q$).
This may indicate that the correct $n_\star$ rule depends not only on
filtration depth but also on how the per-generator volume list
**multiplicities** interact with the cyclotomic projection — a refined
form of the conjecture would need to fold per-generator-volume
multiplicity into $n_\star$.

## Relation to the $q$-Habiro picture

The two completions are **independent**:

See [Table 2](#tbl:brane-tower-z-habiro-table2-data).

The full picture would be a **bicompletion**
$\widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}$ at the bigraded ideal
generated by both $(q;q)_n$ and $P_n(q,z)$, in which the colored Jones
data and the brane-tower data coexist as a single algebraic object.
Construction of the bicompletion is open.

## Falsifiability

The conjecture is **falsifiable** by computation:

1. Pick a candidate $n_\star$ rule (one of the rows above, or a
   combination).
2. Compute $\pi_{n_\star(\mathfrak{H})}^{(z)}(\widetilde{\Phi}^{(N)})$
   at $q_0$ for each isotope in the AME light-isotope sample
   $\{D, T, {}^3\mathrm{He}\}$.
3. Form $B(\mathfrak{H}) = m_e \cdot \rho \cdot (\mathrm{tr}_M(T_w) + \mathrm{tower}(\mathfrak{H}) + \sigma_{3A})|_{q_0}$.
4. Compare with the AME values $\{2.224566, 8.481798, 7.71806\}$ MeV.

A candidate $n_\star$ rule that closes all three to within $\sim 5\%$
**without per-atom retuning** is the empirical signature that
$n_\star$ has been correctly identified. A rule that requires
per-atom retuning is structurally equivalent to Yekutieli's $k_{\max}$
and does not constitute progress.


## Closure attempts: probed $n_\star$ forms

The conjecture's $n_\star$ existence claim asserts a canonical
level-selection rule derivable from substrate data without per-atom
retuning. Six candidate families have been probed against the AME
light-isotope sample $\{D, T, {}^3\mathrm{He}\}$ and **all are
refuted** by the conjecture's own falsifiability criterion (each
exceeds the $\sim 5\%$ confirmation threshold on at least one isotope
without per-atom retuning):

1. scalar uniform-$k$,
2. scalar $\ell\cdot n_0 + k$,
3. per-eigenvalue operator-valued,
4. multiplicity / Type-B-folded-crystal,
5. pair-knot product-volume,
6. pair-knot Markov-trace (full Frobenius Gram + SDP).

The full canonical evaluation record — sweep tables, error magnitudes, and the
per-form falsification theorems — is consolidated in the
refuted-ansatz audit
([`docs/audits/2026-06-17-refuted-ansatz-lemmas.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-17-refuted-ansatz-lemmas.md)).
The sibling [`brane-tower-z-habiro.lean`](brane-tower-z-habiro.lean)
records the six refutations as witness-driven theorems combined in
`nStar_all_probed_forms_refuted`.

## Surviving claims after the closure attempts

The conjecture has two independent claims:

1. **Algebraic Cauchy-limit claim** —
   $\widetilde{\Phi}_q^{\mathrm{tower}}(\beta)$ exists as a Cauchy
   limit in the $z$-Habiro topology
   ([$z$-Habiro ring](#def:z-habiro-ring)). **Untouched by any of the
   $n_\star$ probes and remains open**; a direct algebraic proof
   proceeds via the cyclotomic projections $\pi_n^{(z)}$ and does not
   depend on $n_\star$. The analytic prerequisite — that the infinite
   product $\Phi_q(z) = \prod_{k\geq 1}(1-q^{-k}z)^{-1}$ is a
   well-defined positive real on $|z| < q$ — is now **proved** as
   [convergence of the quantum dilogarithm](#prop:quantum-dilog-convergence)
   (Lean `QOU.MassEndomorphism.PhiQConvergence.quantumDilog_multipliable`,
   sorry-free): the convergence half of the conjecture is a theorem, so the
   $z$-Habiro Cauchy limit has a well-defined analytic target.

   The algebraic Cauchy/limit infrastructure is formalized sorry-free in
   `QOU.MassEndomorphism.ZHabiroCauchy` (filtration, increment-coherence
   core, the cyclotomic completion ring `ZHabiroCompletion` as a
   `CommRing`, and the limit element `zHabiroLimit`). The **sole remaining
   algebraic gap** is *which* coefficient family $c_n$ reproduces the
   actual $\Phi_q$ and *over which ring*. This is now characterized: the
   power-series coefficients are the closed Euler form
   $b_n = [z^n]\Phi_q = q^{-n}/\prod_{j=1}^n(1-q^{-j})$, and the cyclotomic
   coordinates $c_n$ (the triangular change of basis into the $P_m$) are
   **not** integral over $\mathbb{Z}[q^{\pm1}]$ — their denominators are
   products of the cyclotomic factors $(1-q^{-j})$, so they live in the
   **localisation** $S^{-1}\mathbb{Z}[q^{\pm1}]$ at
   $S = \langle 1-q^{-j} : j\geq 1\rangle$ (the compute witness
   `z-habiro-increment-canonical evaluation`, verdict `cauchy-limit-exists-localised`:
   $\Phi_q$'s poles at $z=q^k$ are the integrality obstruction). The Lean
   `eulerCoeff` realises the $b_n$ in that localised ring, and
   `braneMonic_coords_unique` proves the cyclotomic coordinates are
   **unique** (the monic $g_m$ are linearly independent). What is **not**
   yet closed — and is not faked — is the analytic$\leftrightarrow$algebraic
   identification that this localised Euler family is the $c$ whose
   `zHabiroLimit` equals the analytic $\Phi_q$.

2. **$n_\star$ existence claim** — refuted across every probed form
   (above). The block kind remains `conjecture` because the algebraic
   Cauchy-limit half is still open.

## Structural finding: pair-knot operators are selected at closed shells

Independent of the refuted $n_\star$ forms, the operator-selection LP
dual yields a positive structural result. For magic-shell nuclei the
closed shell contributes as a single composite knot operator (the
Hopf-linked sub-knot of the magic nucleon pair) rather than a sum of
separate per-generator $\Phi_q(|\hat V_i|)$ terms. The per-generator
magnitudes make the duplicated intra-block structure visible:

See [Table 7](#tbl:brane-tower-z-habiro-table7-data).

Solving the operator-selection LP over the basis
$\{\sigma_i,\ \sigma_{pp},\ \sigma_{nn}\}$ with cost $t_i = |\hat V_i|$
and the Frobenius Gram (per
[`prop:operator-selection-lp`](#prop:operator-selection-lp)), with
strong duality verified (gap $= 0$), the dual active set distinguishes
the pair-knot composites $\sigma_{pp}, \sigma_{nn}$ from per-generator
operators **at exactly the magic configurations** — and they are
absent from $D$'s active set, which has no magic shell:

See [Table 8](#tbl:brane-tower-z-habiro-table8-data).

This is the operator-level signature of $Z=2$ / $N=2$ shell closure in
the substrate algebra, recorded in the sibling `.lean` as
`lpDualActiveSetIncludesPairKnotAtMagicShells` for downstream use.

## Structural finding: $Z \leftrightarrow N$ isospin symmetry

At the canonical Markov-trace operator-volume level the two
magic-shell sub-braids are isomorphic Hecke elements:

$$
  \mathrm{tr}_M(\sigma_{pp}) \;=\; \mathrm{tr}_M(\sigma_{nn})
  \;=\; 0.0622 \quad(\text{exactly}),
$$

so $Z \leftrightarrow N$ isospin symmetry holds exactly. (An apparent
$1.326\times$ asymmetry under the cruder product-volume convention was
a product-volume artifact, not a real symmetry breaking.)

## Structural conclusion

No probed $n_\star$ choice and no operator-volume convention (product,
geometric-mean, or canonical Markov trace) recovers the AME
light-isotope binding uniformly; the ${}^3\mathrm{He}$ gap is a
structural deficit of the brane-tower formula at the $A=3$ / $n_0=9$
regime, not an operator-volume choice. The surviving open paths are
the algebraic Cauchy-limit half (above) and the ${}^3\mathrm{He}$
structural-gap branch.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: brane-tower-z-habiro.md -->

<!-- FILE_START: hoefsmit-ew-cell-content.md -->
**Theorem (Hoefsmit cell-content identification of EW triplet —
categorical existence, Sprint 5 discharge; concrete EW-projector
identifications deferred to per-partition follow-up).**
*Let $R$ be the categorical coefficient ring with $q \in R$ generic
(not a root of unity in $R$, $q \neq 1$). The electroweak
force-carriers $W^\pm, Z, H$ — identified topologically as the
2-component torus links $T(2,4), T(2,6), T(2,8)$ on Bring's
surface (per
`conj:electroweak-higgs-torus-link-triplet`)
— are realised inside $\mathrm{End}_R(V^{\otimes 6})$ as the
**disjoint-strand-pair** Hoefsmit projectors of*

$$
  W \;\longleftrightarrow\; \sigma_1^{\,4} \;\;(\text{strands 1\text{--}2}),
  \quad
  Z \;\longleftrightarrow\; \sigma_3^{\,6} \;\;(\text{strands 3\text{--}4}),
  \quad
  H \;\longleftrightarrow\; \sigma_5^{\,8} \;\;(\text{strands 5\text{--}6}).
$$

*Strand count $n = 6$ is the **minimum** at which all three
carriers admit simultaneous non-trivial action with pairwise-
commuting generators (via far-commutativity $\sigma_i \sigma_j =
\sigma_j \sigma_i$ for $|i - j| \geq 2$). The eight
$(\sigma_1, \sigma_3, \sigma_5)$ sym/alt eigenvalue patterns
identify eight pairwise-orthogonal projectors in
$\mathrm{End}_R(V^{\otimes 6})$ with pure-eigenspace tableaux
multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ (for the eight pure
patterns enumerated in lexicographic order, total dim $= 20$).*

### Statement (formal)

For $n = 6$, the standard Young tableaux for partitions $\lambda
\vdash 6$ supply the Hoefsmit seminormal basis of $\bigoplus_{\lambda
\vdash 6} V_\lambda$, with $\sum_\lambda f_\lambda = 76$
seminormal-basis vectors and $\dim_R \mathrm{End}_R(V^{\otimes 6}) =
\sum_\lambda f_\lambda^2 = 720$. On each tableau $b$, the generator
$\sigma_i$ acts via the standard Hoefsmit formula

$$
  \sigma_i \cdot b
  \;=\; \begin{cases}
    +q \cdot b, & \text{if } i, i+1 \text{ same row of } b, \\
    -q^{-1} \cdot b, & \text{if } i, i+1 \text{ same column of } b, \\
    \text{off-diagonal mixing}, & \text{otherwise}.
  \end{cases}
$$

A tableau is **pure for $(\sigma_1, \sigma_3, \sigma_5)$** if all
three of these generators act diagonally (no mixing). The
[`hoefsmit-ew-cell-content.witness.json`](../../computations/hoefsmit-ew-cell-content.witness.json)
enumeration shows there are exactly **20 such pure tableaux**,
distributed across the **eight** sym/alt eigenvalue patterns:

See [Table 1](#tbl:hoefsmit-ew-cell-content-table1-data).

(The "$+$"/"$-$" labels mark the sym/alt eigenchannel of each
$\sigma_i^{2k_i}$. The multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$
reflect non-trivial cell-content combinatorics — they are **not**
uniform.)

### Minimality of $n = 6$

Each EW carrier $T(2, 2k)$ acts non-by definition on a **single
strand-pair** (the two endpoints of its 2-component link
projection). Three carriers therefore need three disjoint
strand-pairs:
- $W$: strands 1, 2 (acting via $\sigma_1$)
- $Z$: strands 3, 4 (acting via $\sigma_3$)
- $H$: strands 5, 6 (acting via $\sigma_5$)

For $n < 6$, two of the three carriers must share strand-pairs;
their generators no longer commute (they share a generator
between consecutive strands), and the simultaneous-eigenspace
decomposition degenerates. So $n = 6$ is the structural minimum
for the simultaneous Hoefsmit identification.

### Refinement: coupling via interface knot $\bowtie_K$, not disjoint product

The disjoint-product framing $\sigma_1^4 \cdot \sigma_3^6 \cdot
\sigma_5^8$ — equivalent to a tensor product via far-commutativity
$\sigma_i \sigma_j = \sigma_j \sigma_i$ for $|i - j| \geq 2$ —
treats $W, Z, H$ as **independent** carriers. This is
mathematically clean but does not match the physics: the electroweak
symmetry breaking $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y \to
\mathrm{U}(1)_{\rm em}$ is a *coupling* mediated by the Higgs
vacuum-expectation value, not a disjoint sum.

The categorical analog of the Higgs-vev coupling is an **interface
knot** $\bowtie_K \in H_6(q)$ — directly parallel to the
inter-nucleon interface $I$ in the W-3 deuteron derivation
([`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf), where the
deuteron braid $\beta_D = (\mathcal{B}_p \otimes \mathcal{B}_n) \cdot I$
contributes the $+1$ in $u_{\rm shift} = 18Z + 21N + 1$).

The corrected EW braid is

$$
  \beta_{\rm EW}(\bowtie_K)
  \;:=\;
  \sigma_1^{\,4} \cdot \bowtie_K^{(W \to Z)} \cdot \sigma_3^{\,6}
  \cdot \bowtie_K^{(Z \to H)} \cdot \sigma_5^{\,8} \cdot \bowtie_K^{(H \to W)}
  \;\in\; H_6(q),
$$

where $\bowtie_K^{(X \to Y)}$ is the interface knot connecting the
strand-pair of $X$ to the strand-pair of $Y$. These interfaces use
the **non-far-commutative** generators $\sigma_2, \sigma_4$ (which
sit between adjacent strand-pairs) — analogues of the inter-nucleon
interface generator $\sigma_3$ in $H_6(q)$ for the deuteron.

**Implications:**

1. **Pattern multiplicities change.** The disjoint-product
 $(4, 2, 1, 3, 3, 1, 2, 4)$ multiplicities are computed
 ignoring $\bowtie_K$. With $\bowtie_K$ inserted, $\beta_{\rm
   EW}$ acts non-by definition across strand-pairs; pure-pattern
 counting needs recomputation.

2. **Bar-self-duality may break or be modified.** The
 $\sigma_i^{2k}$ trace was bar-self-dual term-by-term; the
 $\bowtie_K$-coupled trace may have a $\bowtie_K$-orientation-
 dependent phase, or the duality may be restored only modulo
 the orientation of the interface knots.

3. **Higgs-vev automorphism gets concrete form.** The Weinberg
 automorphism $(W^3, B) \to (Z, \gamma)$ pre-EWSB is plausibly
 the change-of-basis induced by inserting a specific $\bowtie_K$;
 $\theta_W$ then reads off the eigendirections of the
 interface coupling.

4. **The 8 pure patterns become 8 $\bowtie_K$-twisted patterns.**
 Mixing depends on $\bowtie_K$'s structural data, suggesting
 $\theta_W$ — and possibly the entire EW Wedderburn block
 structure — is *parametrised* by the interface knot's choice.

**Action items prompted by the $\bowtie_K$ refinement:**

- Author $\bowtie_K$ as a categorical content block (candidate
 `def:ew-interface-knot`), defining the analog of the
 inter-nucleon interface generalised to gauge-boson couplings.
- Recompute the Hoefsmit pure-pattern enumeration under
 $\beta_{\rm EW}(\bowtie_K)$; extend
 [`hoefsmit-ew-cell-content.witness.json`](https://github.com/litlfred/qou/blob/main/computations/hoefsmit-ew-cell-content.witness.json)
 to include $\sigma_2, \sigma_4$ in the eigenvalue analysis.
- Re-derive $\mathrm{tr}_{\rm pure}(\beta_{\rm EW}(\bowtie_K))$
 symbolically.
- Connect the Weinberg-angle automorphism to $\bowtie_K$
 eigendirections — both the simple-uniform reading at 64% and
 the corrected best at 8.4% are $\bowtie_K$-free; the structural
 closure likely lives in $\bowtie_K$.

### Resolution of the dimension-collapse issue

The audit
[`docs/audits/-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-path-alpha-bring-refinement.md)
flagged that $H_2(q)$-only completeness sums six rank-1 projectors
in a 2-dimensional algebra — dimensionally inconsistent. The Hoefsmit
identification at $n = 6$ resolves this:

- The six EW projectors live as **rank-1 to rank-3** projectors in
 $\mathrm{End}_R(V^{\otimes 6})$ (multiplicities depending on
 pattern).
- They are pairwise orthogonal (as eigenspace projectors of
 pairwise-commuting generators with distinct eigenvalues at
 generic $q$).
- They sit alongside two **non-EW** projectors (vacuum and
 fully-broken) in the 8-pattern decomposition of the
 pure-eigenspace.
- Total: 8 pairwise-orthogonal projectors of multiplicities $(4,
  2, 1, 3, 3, 1, 2, 4)$, summing to a rank-20 projector on the
 pure-eigenspace; the complementary rank-56 mixed-eigenspace
 carries off-diagonal generator mixing.

### The Plancherel weight is a degenerate special case

Earlier drafts of this audit posited a **Plancherel weight**
$w_X = (\dim_q \mathrm{im}\,e_X)^2 / [n]_q!$ as the structural
multiplier for each EW projector. **This framing is wrong.** The
Hoefsmit cell-content data give a more direct quantity: the
**unweighted trace** of the operator product
$\sigma_1^4 \sigma_3^6 \sigma_5^8$ on each pure pattern is
just (cell-content multiplicity) $\times$ (eigenvalue of pattern).
No external Plancherel prefactor is required.

Concretely, $\sigma_i^{2k}$ has eigenvalue $q^{2k}$ on a sym
tableau and $q^{-2k}$ on an alt tableau, so on the pure pattern
$(X_W, X_Z, X_H) \in \{\mathrm{sym}, \mathrm{alt}\}^3$ the operator
$\sigma_1^4 \sigma_3^6 \sigma_5^8$ has eigenvalue

$$
  \varepsilon(X_W, X_Z, X_H) \;=\; q^{\,\pm 4} \cdot q^{\,\pm 6} \cdot q^{\,\pm 8}
$$

with sign $+1$ for sym and $-1$ for alt in each factor. The trace
on the pure-eigenspace is:

$$
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  \sum_{(X_W, X_Z, X_H)} m(X_W, X_Z, X_H) \cdot \varepsilon(X_W, X_Z, X_H).
$$

Substituting the multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ and
collecting powers:

$$
\boxed{\;
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  4\bigl(q^{18} + q^{-18}\bigr)
  + 2\bigl(q^{10} + q^{-10}\bigr)
  + 1\bigl(q^{6} + q^{-6}\bigr)
  + 3\bigl(q^{2} + q^{-2}\bigr)
\;}
$$

This is **bar-self-dual** under $\iota \colon q \mapsto q^{-1}$ —
exactly the substrate-level
[bar self-duality](#prop:bar-t-duality-substrate) at the level of
the trace. The bar-self-duality is **automatic** from the
disjoint-strand-pair construction (each $\sigma_i^{2k}$ is
bar-self-dual on its own per
`prop:even-twist-torus-link-psd-feasibility`,
and the disjoint product preserves the duality).

By contrast, the Plancherel-weighted "uniform-1/[2]_q" form
$q^6 (1 + q^2 + q^4) / 3$ from the prior draft is **not**
bar-self-dual: under $\iota$ it becomes $q^{-6}(1 + q^{-2} +
q^{-4})/3 \neq q^6 (1 + q^2 + q^4) / 3$. So the Plancherel
expression cannot be the substrate-level trace; it was a
**degenerate artifact** of the dimensionally-collapsed
$H_2(q)$-only computation, which lost the cell-content structure
that enforces bar-self-duality.

canonical comparison at $q_0 = 1.109978595554181\ldots$ (50 dps):

See [Table 2](#tbl:hoefsmit-ew-cell-content-table2-data).

The two differ by a factor of $\sim 22$ at $q_0$ and are
**inequivalent** as $R$-elements.

### Implication for $N_v$ derivation

The constrained-PSLQ basis for $N_v$ should therefore use the
**direct cell-content trace** $\mathrm{tr}_{\rm pure}$ as the
structural input — not the Plancherel-weighted form. The
[`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization)
block needs corresponding refinement: the Plancherel framing is
demoted to "degenerate special case" status; the bar-self-dual
$\mathrm{tr}_{\rm pure}$ is the operative quantity going forward.
### Audit-flag impact

If this conjecture is discharged, it **fixes** the
$\mathrm{End}_R(A)$-decomposition issue noted in
[`docs/audits/-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-path-alpha-bring-refinement.md)
(Fix A reading), and supplies a corrected closed form for
$\mathcal{N}_{\rm sym}(q)$ derived from the actual Hoefsmit cell-
content arithmetic — not the dimensionally-inconsistent uniform-
weight expression.

**Witness.**
[`computations/hoefsmit-ew-cell-content.witness.json`](../../computations/hoefsmit-ew-cell-content.witness.json)
— enumerates standard Young tableaux of partitions of 6 with
their $(\sigma_1, \sigma_3, \sigma_5)$ eigenvalue classes; reports
pure-eigenspace counts and 8-pattern multiplicities.

### Historical alignment: quaternionic electroweak theory

The disjoint-strand-pair identification of $W^\pm, Z, H$ above sits
alongside a much older algebraic observation: Morita's quaternionic
formulation of the electroweak sector \cite{morita1981, morita1982}, in which writing
fermion and Higgs multiplets over the quaternion field $\mathbb{H}$
rather than $\mathbb{C}$ makes the left–right symmetric gauge structure
$\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R \times \mathrm{U}(1)$ appear
algebraically, with quarks and leptons organised into flavor doublets
(compare also the quaternionic/superconformal constructions of
Cederwall and Preitschopf \cite{cederwallpreitschopf1995}).

The QOU tetraplectic boundary supplies a geometric home for the same
$\mathrm{SU}(2)$: the Reeb triad on the Bring-cone link (the quaternionic
twist $[M_i, M_j] = 2 M_k$, formalised in
[`BringCone.lean`](../lean/QOU/BringCone.lean)). The unit-quaternion
$\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ actions on the flavor doublet
are formalised in
[`QuaternionicElectroweak.lean`](../lean/QOU/QuaternionicElectroweak.lean),
where they are proved to be **norm-preserving** (a genuine unitary gauge
action) and to **commute** as two factors. What is established is exactly
this group-action content; the identification of these algebraic actions
with the physical $W^\pm, Z, H$ carriers is an interpretive alignment
\cite{morita1981, cederwallpreitschopf1995}, **not** a derivation.
<!-- FILE_END: hoefsmit-ew-cell-content.md -->

