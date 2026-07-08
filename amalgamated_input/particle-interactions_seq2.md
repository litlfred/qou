<!-- FILE_START: confinement-lp.md -->
We recast the confinement operator selection as a linear program over the NF basis of $H_3(q)$. This connects the categorical minimum-action principle to standard LP duality theory, providing a rigorous proof of uniqueness.

## Primal program (operator selection)

**Proposition.**
*The confinement operator $\Phi = \sum_{i=1}^{6} x_i b_i \in H_3(q)$ for quark types $(f_1, f_2, f_3)$ is the solution of:*

$$
  \min_x \quad \sum_{i=1}^{6} t_i \cdot x_i
  \qquad (\text{minimize Markov trace})
$$

*subject to:*

$$
  \sum_{i=1}^{6} x_i = n_{\mathrm{target}}
  \qquad (\text{net constraint})
$$

$$
  \sum_{j=1}^{6} G_{ij} x_j \geq 0
  \quad \forall\, i
  \qquad (\text{Frobenius positivity})
$$

$$
  x_i \geq -M \quad \forall\, i
  \qquad (\text{boundedness})
$$

*where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the basis elements, $G_{ij}$ is the Frobenius Gram matrix, $n_{\mathrm{target}}$ is the invariant net demand of the state, and $M$ is a large constant.*

The objective $\sum t_i x_i = \mathrm{tr}_M(\Phi)$ is the categorical action. The Frobenius positivity constraint $Gx \geq 0$ ensures that $\Phi$ pairs non-negatively with all basis elements.

## Dual program (demand satisfaction)

By LP duality, the dual of the primal is:

$$
  \max_y \quad n_{\mathrm{target}} \cdot y_0
$$

*subject to:*

$$
  y_0 + \sum_{i=1}^{6} G_{ij} y_i \leq t_j
  \quad \forall\, j
$$

$$
  y_i \geq 0 \quad \forall\, i \geq 1
$$

The dual variable $y_0$ is the shadow price of the net constraint. The dual variables $y_i$ are the shadow prices of the Frobenius positivity constraints.

Strong duality holds because the feasible set is non-empty and bounded.

## $\mathcal{B}_3$ as the LP solution

At specific topological evaluations, the LP has an optimal vertex at $x^* = \mathrm{NF}(\mathcal{B}_3)$.

The Frobenius positivity constraints are tight at two indices ($\sigma_0$ and $L_-$), giving the two active demand channels that correspond to the residual demand.

## Caveat: $\mathcal{B}_3$ is a local minimum

With the corrected Markov trace $\mathrm{tr}_M(e^-) = z^3$, the Gram matrix acquires a negative eigenvalue. The LP has a global minimum at $\mathrm{tr}_M = 0$. The Borromean solution $\mathcal{B}_3$ is a local minimum.

## Quadratic extension

When the interaction involves a bilinear Frobenius pairing $\langle \Phi, K \rangle_F = x^T G y$, the optimization becomes a quadratic program:

$$
  \min_{x} \quad x^T G y
  \qquad \text{s.t.} \quad
  \mathbf{1}^T x = n_1, \quad
  \mathbf{1}^T y = n_2, \quad
  Gx \geq 0
$$

When $y$ is fixed, $x^T G y$ is linear in $x$, reducing to a standard LP. When both $x$ and $y$ vary, the objective is bilinear with indefinite $G$. The nuclear assembly step fixes $y = \mathrm{NF}(\mathfrak{N}_{k+1})$ and solves the resulting LP.
<!-- FILE_END: confinement-lp.md -->

<!-- FILE_START: confinement-nucleon-unit.md -->
The confinement LP proof and the Gram indefiniteness theorem jointly justify treating nucleons as atomic units in the transfer matrix chain. The proof is purely algebraic. We use LP duality, Gram matrix eigenstructure, and braid group realizability. No physics assumptions enter.

**Statement.** The inter-nucleon transfer matrix uses nucleon strand types $p, n$ with crossing coefficients $pp: (1,0)$, $nn: (1,-\mathrm{HA})$, $pn: (1,-\mathrm{HA}/2)$, without resolving the internal quark structure. This is exact because:

1. **LP confinement** proves that the Borromean operator $B_3 = (\sigma_0\sigma_1^{-1})^3$ traps the quark NF coefficients in the Frobenius cone $G\vec{x} \geq 0$. No quark subset can unbind.
2. **Gram indefiniteness** ($\det G < 0$) shows that energy minimization has a global minimum at $\mathrm{tr}_M = 0$. Confinement at $\mathrm{tr}_M \approx 1$ is topological, forced by the braid group realizability constraint $B_3$.
3. **Consequence for the transfer matrix:** Since quarks cannot unbind, the nucleon's internal braid structure acts as a rigid unit. The inter-nucleon crossing between nucleon $i$ and nucleon $j$ depends only on the nucleon types, not on the quark arrangement. The transfer matrix Skein polynomial $P = \prod_i \hat{V}_i$ captures the full inter-nucleon physics at the nucleon level.
4. **Error bound:** The nucleon-as-unit approach introduces no error for the transfer matrix. Quark-level effects manifest only through the nucleon NF coefficients, which we precompute once via `build_nucleon_nf`.
<!-- FILE_END: confinement-nucleon-unit.md -->

<!-- FILE_START: confinement-operator-selection.md -->
*Among three-strand braid closures, the Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is selected as the confinement operator by the topological principle of crossing-minimal Brunnian nontriviality. Its closure is the crossing-minimal nontrivial Brunnian three-link. The Frobenius Gram and Markov-trace data act as a consistency check on this topologically selected operator, rather than its selector.*

We do not assert the Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ as the confinement operator out of convenience; a topological principle selects it. Confinement requires that no proper subset of the three quarks can be isolated. Equivalently, the braid closure must be a Brunnian link. $\mathcal{B}_3$ provides the crossing-minimal such link.

This selection occurs on braid space, not on the Frobenius Gram matrix. A minimum-action functional on that matrix does not select $\mathcal{B}_3$. Because $\mathrm{NF}(\mathcal{B}_3)$ is $\approx 99.8\%$ the identity $\gamma$, any cost-minimising operator-space program selects the smallest-cost mesonic channel $L_\pm$. The Gram and Markov-trace data serve strictly as a consistency check.

## Three unconfined quarks are unstable

In $H_3(q)$, the unconfined proton quarks $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ yield the product of typed crossing elements:

$$
  \mathrm{NF}(\sigma_0 \cdot (\sigma_0 - \tfrac{1}{2}H_A) \cdot (\sigma_1 - \tfrac{1}{2}H_A))
  =
  -0.105\gamma - 0.011\sigma_0 + 1.000\sigma_1 + 0.105 L_+.
$$

The demand profile $\{\gamma = -0.105, \sigma_0 = -0.011\}$ signals instability. The unconfined state requires vacuum energy ($\gamma$) and crossing content ($\sigma_0$) from its environment.

For unconfined neutron quarks $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$:

$$
  \mathrm{NF}(\text{unconfined } \mathfrak{n})
  =
  -0.211\gamma + 1.011\sigma_1,
$$

with demand $\{\gamma = -0.211\}$. This larger vacuum deficit reflects the extra down quark's $-H_A$ shift.

## Candidate operator comparison

We evaluate nine candidate confinement operators by applying each to the typed crossings and measuring three quantities:

1. **Net constraint**: $|\mathrm{net}(\Phi \cdot \mathrm{crossings}) - \mathrm{net}_{\mathrm{target}}|$
2. **Markov trace**: $\mathrm{tr}_M(\Phi \cdot \mathrm{crossings})$ (categorical action)
3. **Demand channels**: number of negative NF coefficients in the confined state

**Naive ranking.** Minimising demand channels and then $\mathfrak{E}_\times$ selects $L_+$. However, $L_+$ gives $\mathrm{net} \approx 1.22$, far from the physical proton mass. $L_+$ represents a pairwise binding. An operator-space cost-minimisation falls into this channel, which the Brunnian constraint excludes.

**Topological selection.** Among three-strand braid closures, $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the crossing-minimal nontrivial Brunnian link. Its closure has three components, all three pairwise linking numbers vanish, yet every two-component sublink is the unlink. No braid of fewer than six crossings is nontrivially Brunnian. This selection relies on no physical input.

**Net consistency check.** We confirm the topologically selected $\mathcal{B}_3$ against the physical data. Its $|\Delta\mathrm{net}|$ is closest among the candidates, and it successfully confines. The identity leaves the quark demand profile unchanged. This match acts as a consistency check.
<!-- FILE_END: confinement-operator-selection.md -->

<!-- FILE_START: confinement-operator-selection-interpretation.md -->
## Beta decay emerges from the confined demand

The $\mathcal{B}_3$-confined proton NF has residual demand:

$$
  \mathrm{NF}(\mathfrak{p})
  =
  \underbrace{-0.100}_{\gamma < 0}\gamma
  + 0.036\sigma_0 + 0.998\sigma_1 + 0.099 L_+ + 0.009 L_-
  + \underbrace{-0.043}_{e^- < 0}e^-.
$$

- $\gamma < 0$: vacuum energy deficit—the source of the nucleon's mass.
- $e^- < 0$: **trefoil demand**—the nucleon demands an electron. This is the categorical beta decay channel.

For the neutron, the demand is larger: $\gamma = -0.202$, $L_+ = -0.010$, $e^- = -0.044$. The additional $L_+$ deficit and larger $\gamma$ deficit provide the energy that drives $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$.

## Confinement universality

The confined nucleon NF depends only on $q_0$ and the quark types. It is independent of the photon polarization $(\varphi_0, \varphi_1, \varphi_{01})$ that created the quarks. The strong interaction washes out the electromagnetic initial conditions.
<!-- FILE_END: confinement-operator-selection-interpretation.md -->

<!-- FILE_START: confinement-frobenius-reciprocity.md -->
*Let $T \in H_n(q)$ be a confined bound-state operator selected by the operator-selection LP with primal optimum $T = \sum_i x_i^* b_i$ and dual optimum $(y_0^*, y^*)$. Here, $\{b_1, \ldots, b_d\}$ is the normal form basis, $G_{ij} = \mathrm{tr}_M(b_i b_j)$ is the Frobenius Gram matrix, and the LP-active set is:*

$$
  A^*(T) \;=\; \{\, i \in \{1, \ldots, d\} \;:\; y_i^* > 0 \,\}.
$$

*For every observable $O \in H_n(q)$, the physical expectation value of $O$ in the bound state $T$ is the **Gram-inverse dual pairing weighted by LP-active shadow prices**:*

$$
  \boxed{\;
    \langle O \rangle_T
    \;\equiv\;
    O(T)
    \;=\;
    \sum_{i,\,j \,\in\, A^*(T)}
      u_i^*\,(G^{-1})_{ij}\,\langle O,\, b_j\rangle
  \;}
$$

*where $u_i^* = y_i^*$ are the LP shadow prices on the active channels and $(G^{-1})_{ij}$ is the Frobenius dual-basis matrix on the $|A^*(T)|$-dimensional active subspace. Equivalently:*

$$
  \langle O \rangle_T
  \;=\;
  \langle O,\, G^{-1}\,u^*\rangle_{A^*}
  \;=\;
  \langle O,\, T^\vee\rangle,
$$

*where $T^\vee = \sum_{i,j \in A^*} u_i^* (G^{-1})_{ij}\,b_j$ is the **Frobenius dual** of $T$ on the active subspace.*

## Sketch of Proof

The proof has two parts.

**Part 1: Frobenius reciprocity on $H_n(q)$.**
The Markov trace $\mathrm{tr}_M$ is a non-degenerate Frobenius form on $H_n(q)$. The Frobenius dual $T^\vee$ of any element $T$ is defined by $\langle T^\vee,\, b_j\rangle = x_j^*$. Solving this linear system gives $T^\vee = \sum_{i,j} x_i^* (G^{-1})_{ij}\, b_j$. Frobenius reciprocity asserts $\langle O, T\rangle_{\text{phys}} = \langle O, T^\vee\rangle$.

**Part 2: LP-active reduction.**
The operator-selection LP yields the primal–dual pair $(x^*, y^*)$ with strong duality $\sum_i t_i x_i^* = n_{\mathrm{target}} y_0^*$. Complementary slackness forces $y_i^* x_i^{(\text{slack})} = 0$ for every $i$. Substituting $x_i^* = (G^{-1} u^*)_i$ on the active set $A^*(T)$ gives the boxed formula.
<!-- FILE_END: confinement-frobenius-reciprocity.md -->

<!-- FILE_START: confinement-frobenius-reciprocity-interpretation.md -->
## Discussion

This proposition provides the master formula for computing numerical predictions about a confined bound state of $H_n(q)$. It governs binding energies, form factors, axial couplings, and magnetic moments.

**Three distinct ingredients are required.**

1. **The Frobenius Gram inverse $G^{-1}$.** The naïve Markov trace $\mathrm{tr}_M(O \cdot \rho(\beta_T))$ is not the physical expectation value of $O$. The Markov form is non-orthonormal on the NF basis, so dualisation requires the Gram inverse.
2. **The LP-active set $A^*(T)$.** Most of the $d = n!$ NF basis elements have zero shadow price ($y_i^* = 0$). Including them in the dual pairing pollutes the observable with off-shell contributions. Only the active channels carry physical weight.
3. **The shadow prices $u_i^* = y_i^*$.** By LP duality, the shadow price on channel $i$ is the marginal cost of saturating the Frobenius positivity constraint. These prices are exactly the weights that make $\langle O\rangle_T$ coincide with the physical expectation.

## Corollaries

- **Corollary (g_A as an instance).** The axial coupling $g_A = \langle \sigma_A\rangle_{\mathfrak{p}} / \langle \sigma_V\rangle_{\mathfrak{p}}$ of the proton bound state is the ratio of two instances of the master formula at the LP-active set $A^*(\mathcal{B}_3)$.
- **Corollary (raw conjugation traces are zero-information).** The pattern $\mathrm{tr}_M(\beta \cdot X \cdot \beta^{-1})$ is cyclically equal to $\mathrm{tr}_M(X)$ and independent of $\beta$. We must replace the conjugation pattern with the master formula.

## Evaluation Protocol

The rigorous evaluation of the master formula requires:

1. **$G$, $G^{-1}$**: Evaluate the Frobenius Gram matrix and its inverse on the NF basis.
2. **Active set and shadow prices**: Solve the operator-selection linear program to obtain $A^*$ and $u_i^* = y_i^*$.
3. **Observable coefficients $\langle O, b_j\rangle$**: Compute $\mathrm{tr}_M(O \cdot b_j)$ for each active $j$.
4. **Pair**: Compute $\langle O\rangle_T = \sum_{i,j \in A^*} u_i^* (G^{-1})_{ij} \langle O, b_j\rangle$.
<!-- FILE_END: confinement-frobenius-reciprocity-interpretation.md -->

<!-- FILE_START: confinement-sdp-spectral-gap.md -->
**Remark.** Feasibility of the confinement SDP is equivalent to a **Hecke spectral-gap condition**: the feasible cone is non-empty if and only if

$$
  \Delta_{\sigma}(q) \;:=\; \lvert q + q^{-1} \rvert \;>\; 0.
$$

The Hecke generator $\sigma$ on $V \otimes V$ has non-degenerate eigenvalues $(q, -q^{-1})$ on $S^{2} V \oplus \Lambda^{2} V$. The dual certificate at optimum is the pair of Jones--Wenzl projectors onto these two isotypic components. The SDP's complementary-slackness matrix is their orthogonal decomposition.

**Deconfinement.** When $q \to \pm i$, $\Delta_{\sigma}(q) \to 0$ and the feasible cone collapses. The SDP retains its role as a numerical certificate at a given $q$. However, its existence is guaranteed by the categorical volume constraint and follows from the eigenvalue structure alone.
<!-- FILE_END: confinement-sdp-spectral-gap.md -->

<!-- FILE_START: confinement-sdp-multi-operator.md -->
**Remark.** Let $P_1$ and $P_2$ be confined particles whose composite satisfies the confinement SDP. Their **binding subword** is

$$
  W_{\mathrm{bind}}
  \;=\;
  \sum_{\lambda \in \mathcal{S}^*} y_\lambda^* \cdot \pi_\lambda \cdot \Phi^*
$$

where $\mathcal{S}^* = \{\lambda : y_\lambda^* > 0\}$ is the **active support** at optimum. The cardinality $|\mathcal{S}^*| \ge 1$ is the **binding multiplicity**:

* $|\mathcal{S}^*| = 1$ is the scalar LP regime (single-channel binding).
* $|\mathcal{S}^*| \ge 2$ is the generic multi-operator regime. It includes all shell-closure and magic-number configurations.

The optimality identity

$$
  \Phi^* \cdot \bigl(y_0^* I + \textstyle\sum_\lambda y_\lambda^* \pi_\lambda - T\bigr) \;=\; 0
$$

is a matrix equation. Its rank counts the **active dual support**—the number of Wedderburn blocks simultaneously coupled at the optimum. When the rank exceeds one, the confined state is a sum of operators from distinct blocks.
<!-- FILE_END: confinement-sdp-multi-operator.md -->

