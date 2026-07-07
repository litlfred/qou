<!-- FILE_START: confinement-lp.md -->
We can recast the confinement operator selection ([confinement selection](#prop:confinement-operator-selection)) as a **linear program** over the NF basis of $H_3(q)$. This connects the categorical minimum-action principle to standard LP duality theory, providing a rigorous proof of uniqueness.

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

*where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the basis elements, $G_{ij}$ is the Gram matrix ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)), $n_{\mathrm{target}}$ is the invariant net demand of the state, and $M$ is a large constant.*

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

The dual variable $y_0$ is the **shadow price of the net constraint**—the marginal cost of increasing the target mass. The dual variables $y_i$ are the **shadow prices of the Frobenius positivity constraints**—the demand prices.

**Strong duality** (the primal and dual have equal optimal values) holds because the feasible set is non-empty ($\mathcal{B}_3$ is feasible) and bounded.

## $\mathcal{B}_3$ as the LP solution

At specific topological evaluations (see [numeric probes](#audit:confinement-lp-numeric)), the LP has an optimal vertex at $x^* = \mathrm{NF}(\mathcal{B}_3)$.

The Frobenius positivity constraints are **tight** at two indices ($\sigma_0$ and $L_-$), giving the two active demand channels that correspond to the residual demand.

## Caveat: $\mathcal{B}_3$ is a local minimum

With the corrected Markov trace $\mathrm{tr}_M(e^-) = z^3$ ([corrected trace](#prop:corrected-markov-trace)), the Gram matrix acquires a negative eigenvalue. The LP has a global minimum at $\mathrm{tr}_M = 0$ (massless confined state). The Borromean solution $\mathcal{B}_3$ is a **local minimum**—the LP vertex with minimum $|\lambda|$ eigenvalue, not maximum. See [$\mathcal{B}_3$ local minimum](#rem:b3-local-minimum) for interpretation.

## Quadratic extension

When the interaction involves a bilinear Frobenius pairing $\langle \Phi, K \rangle_F = x^T G y$ (e.g., inter-nucleon binding), the optimization becomes a **quadratic program**:

$$
  \min_{x} \quad x^T G y
  \qquad \text{s.t.} \quad
  \mathbf{1}^T x = n_1, \quad
  \mathbf{1}^T y = n_2, \quad
  Gx \geq 0
$$

When $y$ is fixed (as in the nuclear assembly step), $x^T G y$ is linear in $x$, reducing to a standard LP. When both $x$ and $y$ vary, the objective is bilinear with indefinite $G$—a non-convex bilinear program. The nuclear assembly step (iv) of the derived atom ([derived atom](#def:derived-atom)) fixes $y = \mathrm{NF}(\mathfrak{N}_{k+1})$ and solves the resulting LP.
<!-- FILE_END: confinement-lp.md -->

<!-- FILE_START: confinement-nucleon-unit.md -->
The confinement LP proof ([confinement as LP](#prop:confinement-lp)) and the Gram indefiniteness theorem ([topological confinement](#prop:confinement-topological)) jointly justify treating **nucleons as atomic units** in the transfer matrix chain. The proof is purely algebraic: we use LP duality, Gram matrix eigenstructure, and braid group realizability. No physics assumptions enter; we interpret the physics (confinement, gluon, mass) strictly downstream.

**Statement.** The inter-nucleon transfer matrix ([transfer matrix](#def:transfer-matrix-operator)) uses nucleon strand types $p, n$ with crossing coefficients $pp: (1,0)$, $nn: (1,-\mathrm{HA})$, $pn: (1,-\mathrm{HA}/2)$, without resolving the internal quark structure. This is exact (not an approximation) because:

1. **LP confinement** proves that the Borromean operator $B_3 = (\sigma_0\sigma_1^{-1})^3$ traps the quark NF coefficients in the Frobenius cone $G\vec{x} \geq 0$. No quark subset can unbind: disconnected quark states are LP-infeasible.
2. **Gram indefiniteness** ($\det G < 0$, eigenvalue $\approx -0.741$) shows that energy minimization has a global minimum at $\mathrm{tr}_M = 0$ (massless). The confinement at $\mathrm{tr}_M \approx 1$ is therefore **topological**, not energetic. It requires the braid group realizability constraint, which forces $B_3$.
3. **Consequence for the transfer matrix:** Since quarks cannot unbind, the nucleon's internal braid structure (B$_3$ + quark crossings) acts as a rigid unit. The inter-nucleon crossing between nucleon $i$ and nucleon $j$ depends only on the nucleon types ($p$ or $n$), not on the quark arrangement within each nucleon. The transfer matrix Skein polynomial $P = \prod_i \hat{V}_i$ captures the full inter-nucleon physics at the nucleon level.
4. **Error bound:** The nucleon-as-unit approach introduces no error for the transfer matrix (it is exact at the inter-nucleon crossing level). Quark-level effects manifest only through the nucleon NF coefficients (proton NF, neutron NF), which we precompute once via `build_nucleon_nf`.

**Witness:** `confinement-lp.witness.json`, `confinement-operator-selection.witness.json`.
<!-- FILE_END: confinement-nucleon-unit.md -->

<!-- FILE_START: confinement-operator-selection.md -->
**Proposition.**
*Among three-strand braid closures, the Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is selected as the confinement operator by the topological principle of crossing-minimal Brunnian nontriviality. Its closure is the crossing-minimal nontrivial Brunnian three-link (every two-component sublink is the unlink). The Frobenius Gram and Markov-trace data act as a consistency check on this topologically selected operator, rather than its selector.*

We do not assert the Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ as the confinement operator out of convenience; a **topological** principle selects it. Confinement requires that no proper subset of the three quarks can be isolated. Equivalently, the braid closure must be a **Brunnian** link, and $\mathcal{B}_3$ provides the crossing-minimal such link.

This selection occurs on **braid/link space**, not on the $6\times 6$ Frobenius Gram matrix ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)). A *minimum-action* (minimum-eigenvalue) functional on that matrix does **not** select $\mathcal{B}_3$. Because $\mathrm{NF}(\mathcal{B}_3)$ is $\approx 99.8\%$ the identity $\gamma$ (the maximum-cost channel), any cost-*minimising* operator-space program instead selects the smallest-cost **mesonic** channel $L_\pm$ (a two-strand pairwise object, not a three-quark confinement). The Gram and Markov-trace data below serve strictly as a **consistency check** on the topologically selected $\mathcal{B}_3$.

## Three unconfined quarks are unstable

Consider three quarks with typed crossings but no binding operator. In $H_3(q)$, the unconfined proton quarks $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ yield the product of typed crossing elements:

$$
  \mathrm{NF}(\sigma_0 \cdot (\sigma_0 - \tfrac{1}{2}H_A) \cdot (\sigma_1 - \tfrac{1}{2}H_A))
  =
  -0.105\gamma - 0.011\sigma_0 + 1.000\sigma_1 + 0.105 L_+.
$$

The **demand profile** (channels with negative NF coefficients) is $\{\gamma = -0.105, \sigma_0 = -0.011\}$. These negative coefficients signal instability. The unconfined state requires vacuum energy ($\gamma$) and crossing content ($\sigma_0$) from its environment. Free quarks have unmet demand and are not self-consistent.

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

See [Table 1](#tbl:confinement-operator-selection-table1-data).

**Naive ranking.** Minimising demand channels and then $\mathfrak{E}_\times$ selects $L_+$. However, $L_+$ gives $\mathrm{net} \approx 1.22$, far from the physical proton mass. $L_+$ represents a pairwise (mesonic) binding; it does not confine three quarks. An operator-space cost-minimisation naturally falls into this channel, which is precisely what the **Brunnian constraint excludes**: a two-strand sublink is not Brunnian.

**Topological selection (primary).** Among three-strand braid closures, $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ is the *crossing-minimal nontrivial Brunnian* link. Its closure has three components, all three pairwise linking numbers vanish, yet every two-component sublink is the unlink (removing any one quark frees the other two). No braid of fewer than six crossings is nontrivially Brunnian. This selection relies on **no physical input**.

**Net consistency check.** We then confirm the topologically selected $\mathcal{B}_3$ against the physical data. Its $|\Delta\mathrm{net}|$ is closest (target $\approx :val[confinement_B3_net_proton]{precision=4}$) among the candidates, and it successfully confines. The identity has slightly lower trace ($0.415$ vs $0.420$), but it leaves the quark demand profile unchanged. See [Table 2](#tbl:confinement-operator-selection-table2-data). This match acts as a *consistency check* on the topological selection.

**Witness**: `confinement-operator-selection.witness.json`.

**Selection-principle support.** We derive the topological selection rigorously: the closure of $(\sigma_0\sigma_1^{-1})^3$ is a nontrivial six-crossing Brunnian three-link (pure braid, all pairwise linking numbers $0$, every two-sublink the unlink). Enumeration of all pure three-braids of word length $\le 6$ confirms no nontrivial Brunnian link exists below six crossings. At six crossings, the minimal Brunnian links all carry the Borromean signature. We refute the operator-space *minimum-action* selector analytically: the dense Wedderburn-projector SDP collapses to the minimum-eigenvector of the cost operator, which invariably yields the mesonic $L_\pm$, never $\mathcal{B}_3$.
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

- $\gamma < 0$: vacuum energy deficit—the source of the nucleon's mass (filled by the Borromean volume $\mathrm{Vol}(\mathcal{B}_3)$).
- $e^- < 0$: **trefoil demand**—the nucleon demands an electron. This is the categorical beta decay channel.

For the neutron, the demand is larger: $\gamma = -0.202$, $L_+ = -0.010$, $e^- = -0.044$. The additional $L_+$ deficit (Hopf link demand) and larger $\gamma$ deficit provide the energy that drives $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$.

## Confinement universality

The confined nucleon NF depends only on $q_0$ and the quark types $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ or $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$. It is **independent of the photon polarization** $(\varphi_0, \varphi_1, \varphi_{01})$ that created the quarks via $\gamma\gamma$ pair production. The strong interaction ($\mathcal{B}_3$ confinement) washes out the electromagnetic initial conditions.
<!-- FILE_END: confinement-operator-selection-interpretation.md -->

<!-- FILE_START: confinement-frobenius-reciprocity.md -->
**Proposition (confinement Frobenius reciprocity).**
*Let $T \in H_n(q)$ be a confined bound-state operator selected by the operator-selection LP ([operator-selection LP](#prop:operator-selection-lp)) with primal optimum $T = \sum_i x_i^* b_i$ and dual optimum $(y_0^*, y^*)$. Here, $\{b_1, \ldots, b_d\}$ is the normal form (NF) basis, $G_{ij} = \mathrm{tr}_M(b_i b_j)$ is the Frobenius Gram matrix ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)), and the LP-active set is:*

$$
  A^*(T) \;=\; \{\, i \in \{1, \ldots, d\} \;:\; y_i^* > 0 \,\}.
$$

*For every observable $O \in H_n(q)$, interpreted as a linear functional $b \mapsto \langle O, b\rangle = \mathrm{tr}_M(O \cdot b)$ on the algebra, the physical expectation value of $O$ in the bound state $T$ is the **Gram-inverse dual pairing weighted by LP-active shadow prices**:*

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

*where $u_i^* = y_i^*$ are the LP shadow prices on the active channels and $(G^{-1})_{ij}$ is the Frobenius dual-basis matrix on the $|A^*(T)|$-dimensional active subspace. Equivalently, in compact notation:*

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
The Markov trace $\mathrm{tr}_M$ is a non-degenerate Frobenius form on $H_n(q)$ ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)). The Frobenius dual $T^\vee$ of any element $T$ is defined by the equation $\langle T^\vee,\, b_j\rangle = x_j^*$ for the NF coefficients of $T$. Solving this linear system on the NF basis gives $T^\vee = \sum_{i,j} x_i^* (G^{-1})_{ij}\, b_j$. Frobenius reciprocity then asserts $\langle O, T\rangle_{\text{phys}} = \langle O, T^\vee\rangle$ for every observable $O$.

**Part 2: LP-active reduction.**
The operator-selection LP ([operator-selection LP](#prop:operator-selection-lp)) yields the primal–dual pair $(x^*, y^*)$ with strong duality $\sum_i t_i x_i^* = n_{\mathrm{target}} y_0^*$. Complementary slackness forces $y_i^* x_i^{(\text{slack})} = 0$ for every $i$. Thus, on the LP-inactive set $\{i : y_i^* = 0\}$, either the constraint is slack and $x_i^*$ is unconstrained, or $x_i^* = 0$. Substituting $x_i^* = (G^{-1} u^*)_i$ on the active set $A^*(T)$ (the precise KKT stationarity condition for the dualised LP) gives the boxed formula.

For binding energy, the observable is the Hamiltonian $O = H$ acting diagonally on the NF basis. In this case, the formula reduces to the known expression in [knot-factor-frobenius-pairing](#conj:knot-factor-frobenius-pairing). That conjecture is therefore the special case $O = H$ of this proposition. Conversely, the same reciprocity governs any other bound-state observable.
<!-- FILE_END: confinement-frobenius-reciprocity.md -->

<!-- FILE_START: confinement-frobenius-reciprocity-interpretation.md -->
## Discussion

This proposition provides the master formula for computing numerical predictions about a confined bound state of $H_n(q)$. It governs binding energies, form factors, axial couplings, magnetic moments, and any other observable linear in the algebra. It extends the binding-energy-only statement of [knot-factor-frobenius-pairing](#conj:knot-factor-frobenius-pairing) to the entire class of bound-state observables.

**Three distinct ingredients are required.**

1. **The Frobenius Gram inverse $G^{-1}$.** The naïve Markov trace $\mathrm{tr}_M(O \cdot \rho(\beta_T))$ is not the physical expectation value of $O$ in the state created by braid $\beta_T$. The Markov form is non-degenerate but non-orthonormal on the normal form (NF) basis, so dualisation requires the Gram inverse.
2. **The LP-active set $A^*(T)$.** Most of the $d = n!$ NF basis elements have zero shadow price ($y_i^* = 0$); they are LP-slack. Including them in the dual pairing pollutes the observable with off-shell contributions. Only the active channels—the "most receptive sub-braids" of the bound state ([BW shadow price](#prop:mass-coefficient-shadow-price))—carry physical weight.
3. **The shadow prices $u_i^* = y_i^*$.** By LP duality, the shadow price on channel $i$ is the marginal cost of saturating the Frobenius positivity constraint $\sum_j G_{ij} x_j \geq 0$. These prices are exactly the weights that make $\langle O\rangle_T$ coincide with the physical expectation under the categorical action functional ([Yekutieli 2D nonabelian Stokes](#rem:yekutieli-stokes)).

## Corollaries

- **Corollary (g_A as an instance).** The axial coupling $g_A = \langle \sigma_A\rangle_{\mathfrak{p}} / \langle \sigma_V\rangle_{\mathfrak{p}}$ of the proton bound state $T_{\mathfrak{p}} = \mathcal{B}_3 = (\sigma_0 \sigma_1^{-1})^3$ is the ratio of two instances of the master formula at the LP-active set $A^*(\mathcal{B}_3)$ selected by [confinement operator selection](#prop:confinement-operator-selection). See `computations/borromean-axial-coupling.py` for the numerical instantiation.
- **Corollary (raw conjugation traces are zero-information).** The pattern $\mathrm{tr}_M(\beta \cdot X \cdot \beta^{-1})$ is cyclically equal to $\mathrm{tr}_M(X)$ and therefore independent of $\beta$. Any calculation treating such a quantity as a "bound-state observable of $\beta$" is structurally flawed: the dependence on the bound-state braid disappears under cyclicity. We must replace the conjugation pattern with the master formula above—load $G^{-1}$, load $A^*$ from the operator-selection LP, and pair $O$ against $T^\vee$ on the active subspace.

## Evaluation Protocol

The rigorous evaluation of the master formula requires:

1. **$G$, $G^{-1}$**: Evaluate the Frobenius Gram matrix and its inverse on the NF basis.
2. **Active set and shadow prices**: Solve the operator-selection linear program for the target bound state to obtain the active set $A^*$ and shadow prices $u_i^* = y_i^*$.
3. **Observable coefficients $\langle O, b_j\rangle$**: Compute the Markov trace $\mathrm{tr}_M(O \cdot b_j)$ for each active $j$.
4. **Pair**: Compute $\langle O\rangle_T = \sum_{i,j \in A^*} u_i^* (G^{-1})_{ij} \langle O, b_j\rangle$.
<!-- FILE_END: confinement-frobenius-reciprocity-interpretation.md -->

<!-- FILE_START: confinement-sdp-spectral-gap.md -->
**Remark.** Feasibility of the [confinement SDP](#prop:confinement-sdp) is equivalent to a **Hecke spectral-gap condition**: the feasible cone is non-empty if and only if

$$
  \Delta_{\sigma}(q) \;:=\; \lvert q + q^{-1} \rvert \;>\; 0.
$$

The Hecke generator $\sigma$ on $V \otimes V$ has non-degenerate eigenvalues $(q, -q^{-1})$ on $S^{2} V \oplus \Lambda^{2} V$. The dual certificate at optimum is the pair of Jones--Wenzl projectors onto these two isotypic components. The SDP's complementary-slackness matrix is their orthogonal decomposition. This aligns with the categorical origin of the [crossing energy](#def:crossing-energy).

**Deconfinement.** When $q \to \pm i$ (Kauffman-bracket degeneracy), $\Delta_{\sigma}(q) \to 0$ and the feasible cone collapses. The SDP retains its role as a numerical certificate at a given $q$. However, its existence is guaranteed by the categorical volume constraint and follows from the eigenvalue structure alone, without invoking continuous optimisation.
<!-- FILE_END: confinement-sdp-spectral-gap.md -->

<!-- FILE_START: confinement-sdp-multi-operator.md -->
**Remark.** Let $P_1$ and $P_2$ be [confined particles](#def:confined-particle) whose composite satisfies the [confinement SDP](#prop:confinement-sdp). Their **binding subword** is

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

is a matrix equation, not a sum of scalar complementary-slackness relations. Its rank counts the **active dual support**—the number of Wedderburn blocks simultaneously coupled at the optimum. When the rank exceeds one, the confined state is a sum of operators from distinct blocks. The `electron-shell-ilp` witness observes this when it reports electrons alternating between $\sigma_1^{-1}$ and $\sigma_0^{-1}$: these are two tight dual blocks at the same $\Phi^*$.
<!-- FILE_END: confinement-sdp-multi-operator.md -->

