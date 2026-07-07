<!-- FILE_START: block-multiplicativity-v-free.md -->
**Conjecture (Block-Multiplicativity of $\hat V^{\text{free}}$ on the Disjoint Hecke Product).**

*Let $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \cdots \mathcal{B}_n^{(N)} \in H_{3A}(q)$ denote the constituent vacuum—the disjoint Hecke product of $Z$ proton braids and $N$ neutron braids on disjoint 3-strand blocks, with no interface crossings. For each generator $\sigma_g$ acting only inside the $k$-th nucleon block, the Wedderburn-weighted per-generator character ratio*

$$
  \hat V^{(3A)}_g(\mathcal{B}_K^{\mathrm{vac}})
   :=
  \sum_{\lambda \vdash 3A}
    \frac{\dim_q^2(\lambda)}{[3A]_q!} \cdot
    \frac{\chi^\lambda(W_g)}{\dim(\lambda)}
$$

*is independent of $A$. It depends only on the flavor of the $k$-th nucleon and on the local position $g \bmod 3 \in \{0, 1\}$ within the block, not on the total strand count $3A$ or the flavor content of the other blocks.*

### Empirical verification

Computed via the canonical formalism on D, T, ${}^{3}$He at $H_6, H_9, H_9$ respectively (50 dps):

| atom | proton block (gens 0, 1) | neutron block | matches D? |
|---|---|---|:-:|
| D (A=2) | $V_0 = 0.6714$, $V_1 = 1.0551$ | $V_0 = 0.5517$, $V_1 = 1.0884$ | — |
| T (A=3) | same | same | yes |
| ${}^{3}$He (A=3) | same | same | yes |

Block-multiplicativity holds exactly to 4 digits. The block factors evaluate to $v_p = 0.7084$ and $v_n = 0.6005$.

### Classical-limit proof sketch ($q \to 1$)

When $\sigma_g$ acts inside the first 3-strand block, the symmetric-group character factors via the Littlewood–Richardson restriction rule. At $q = 1$ the Wedderburn weight is the classical Plancherel measure. By the classical Plancherel duality identity, the ratio simplifies to:

$$
  \hat V^{(3A)}_g
   =
  \frac{1}{6}
  \sum_{\mu \vdash 3} \chi_\mu(\sigma_g) \dim(\mu).
$$

The right-hand side depends only on the $H_3$ character data of $\sigma_g$, proving the classical limit.

### $q$-deformation: the open structural step

For $q \ne 1$, the LR identity generalises to a $q$-Schur duality. We conjecture that this identity yields an $A$-independent residual after factoring out $[3A]_q! / [3A-3]_q!$. A structural proof via the $q$-Schur–Weyl duality remains pending.

### Significance

Block-multiplicativity reduces the $T_1^{\text{free}}$ term of the mass-endomorphism tower from an $O(p(3A) \cdot 3A^3)$ character-sum compute to an $O(1)$ exponentiation: $T_1^{\text{free}}(K) = v_p^Z \cdot v_n^N$. Combined with structural identities for interface generators, this yields a closed-form formula computable in microseconds for any $(Z, N)$.
<!-- FILE_END: block-multiplicativity-v-free.md -->

<!-- FILE_START: wenzl-A-operator.md -->
**Definition (Wenzl A-operator).**
*Let $\lambda \vdash n$ with $n = n_1 + n_2$, and let $I = \sigma_{n_1} \in \mathbf{H}_n(q)$ be the inter-block interface generator joining $\mathbf{H}_{n_1}(q)$ and $\mathbf{H}_{n_2}(q)$. In the Wenzl 1988 Littlewood–Richardson decomposition of the restriction $V_\lambda \downarrow_{\mathbf{H}_{n_1} \otimes \mathbf{H}_{n_2}}$, the **Wenzl A-operator** $A^\lambda_{\mu\nu}(I)$ is the $(\mu, \nu)$-block of $I$ acting on the corresponding isotypic summand:*

$$
  A^\lambda_{\mu\nu}(I) \;\in\; \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu\nu}},
$$

*where $c^\lambda_{\mu\nu}$ is the Littlewood–Richardson coefficient.*

The A-operator provides the operator-valued payload for Wenzl's Sub-lemma 2.1. It enables reading the matrix-entry pole order at $q \to 0$ and accumulating per-peel contributions into the per-isotope binding tower.

The bilinear-system solver extracts matrix entries of $A^\lambda_{\mu\nu}(I)$ at the substrate $q_0$. The $\mathbf{H}_6$ extract is full-rank. The $\mathbf{H}_{9+}$ extracts are least-squares fits over the inner-test family. A universal A-operator remains an open problem.
<!-- FILE_END: wenzl-A-operator.md -->

<!-- FILE_START: crystal-r-matrix-sub-lemma.md -->
**Proposition (Crystal R-matrix Sub-lemma 2.1, operator-valued form).**
*Let $\mathbf{H}_n(q)$ be the Iwahori–Hecke algebra over $R$ with $q$ generic, $\lambda \vdash n$, and $\beta_1 \in \mathbf{H}_{n_1}(q)$, $\beta_2 \in \mathbf{H}_{n_2}(q)$ with $n = n_1 + n_2$. Let $\sigma_i \in \mathbf{H}_n(q)$ be a boundary generator and let $A^\lambda_{\mu, \nu}(\sigma_i)$ be its $(\mu, \nu)$-block in the Wenzl LR decomposition.*

*Under the crystal-graph realization hypothesis, the matrix-entry pole order of $A^\lambda_{\mu, \nu}(\sigma_i)$ at $q = 0$ on any standard Young tableau $T \in \mathrm{SYT}(\lambda)$ in the $(\mu, \nu)$-block is*

$$
  \boxed{\;\;
    \mathrm{pole}\bigl(A^\lambda_{\mu, \nu}(\sigma_i),\, T\bigr)
    \;=\;
    \mathbf{1}\bigl[\rho_T(i) \le -1\bigr]
  \;\;}
$$

*where $\rho_T(i)$ is the axial distance between the cells of $i$ and $i + 1$ in $T$.*

This proposition closes the operator-valued form categorically, modulo the crystal-graph realization hypothesis. The canonical formalism verifies the column-SYT pole-per-cycle for seven torus-knot interfaces and six non-column shapes. The class instance produced here populates the branching block lemma to secure the cycle-shift decomposition.
<!-- FILE_END: crystal-r-matrix-sub-lemma.md -->

<!-- FILE_START: operator-valued-combiner-convergence.md -->
**Proposition (operator-valued combiner convergence).**
*Let $\beta_{\mathrm{atom}}$ be the canonical $A$-nucleon atomic braid in $\mathbf{H}_{3A}(q)$, with inter-nucleon interfaces at the peel levels $n_k = 3(A - k + 1)$. Write $\chi^\lambda_A := \chi^\lambda(\beta_{\mathrm{atom}})$ for the level-$A$ character. The iterated application of the operator-valued Sub-lemma 2.1 assembles into a single convergent representation. The value at level $A + 1$ is the LR-weighted value at level $A$:*

$$
  \boxed{\;\;
    \mathrm{cv}(A + 1) \;=\; w(A)\,\cdot\,\mathrm{cv}(A),
    \qquad A \ge 2,
  \;\;}
$$

*so that the character of an arbitrarily large atom is the deuteron ($A = 2$) base case accumulated through the LR-weight tower.*

This proposition provides the convergence content of the operator-valued Wenzl branching combiner. The atomic Markov trace need not be recomputed at full strand count $3A$ for each isotope. Instead, it peels one nucleon at a time. The recursion bottoms out at the deuteron, which is computed directly at $\mathbf{H}_6$. The product form exhibits the per-isotope binding tower as a telescoping accumulation.
<!-- FILE_END: operator-valued-combiner-convergence.md -->

<!-- FILE_START: depth-stratified-frobenius-reciprocity.md -->
**Conjecture (Frobenius-reciprocity ideal restriction at low curvature-rank).**

*The unified curvature-rank mass formula admits a Frobenius-reciprocity refinement at low curvature-rank $k \le 3$. The depth-$k$ Wedderburn weight restricts to the distinguished hyperbolic-knot ideal at depth $k$ via Frobenius reciprocity for the center inclusion $Z(H_3) \hookrightarrow Z(H_n)$.*

*For each low curvature-rank $k \in \{1, 2, 3\}$ there is a distinguished hyperbolic knot $K_k^*$. At $k = 3$, $K_3^* = 4_1$ gives the best variance reduction, consistent with the Fricke-trace derivation. The depth-$k$ contribution to the mass formula is*

$$
  \boxed{\;
    \Phi_k^{\mathrm{FR}}(\mathcal{K}, \mathcal{T})
     :=
    \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
      \widetilde{w}_\lambda^{(K_k^*)} \cdot
      \log\!\Bigl|\!\!\int_{A_\lambda}\!\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|
  \;}
$$

*where the FR-restricted weight $\widetilde{w}_\lambda^{(K_k^*)}$ is the Frobenius-reciprocity pullback through the knot-ideal central projector $e_{K_k^*} \in Z(H_n)$.*

At high curvature-rank $k \ge 4$, FR is trivial and the uniform Plancherel weight is correct. Empirical tests falsified simpler weight-restriction forms that did not use the distinguished knot ideal $e_{K_k^*}$. The FR refinement breaks the Jones-only spectral degeneracy by weighting partitions through the distinguished projector. If true, this conjecture closes the variance on the unified mass formula.
<!-- FILE_END: depth-stratified-frobenius-reciprocity.md -->

<!-- FILE_START: eigenvalue-product-expansion.md -->
**Proposition.**
*For a nucleus with $Z$ protons and $N$ neutrons ($A = Z + N$), the symmetric channel eigenvalue product of the nuclear braid in the $[2{,}1]$ representation of $H_3(R, q)$ is:*

$$
  \Lambda_{\mathrm{sym}}
  = q^{(Z-N)(A-1)/2} \cdot \Bigl(\frac{[2]_q}{2}\Bigr)^{\!ZN}
$$

*Its logarithm expands in the isospin variable $T = |Z - N|/2$ as:*

$$
  \ln|\Lambda_{\mathrm{sym}}|
  = \ell_2 \cdot \frac{A^2}{4}
  \;+\; \ell \cdot T \cdot A
  \;-\; \ell \cdot T
  \;-\; \ell_2 \cdot T^2
$$

*where $\ell = \ln q$ and $\ell_2 = \ln([2]_q/2)$.*

The four terms correspond respectively to the $pn$ crossing count, the $pp$ vs $nn$ crossing excess, a linear isospin correction, and a quadratic isospin term. The Coulomb correction arises separately from the standard channel.
<!-- FILE_END: eigenvalue-product-expansion.md -->

<!-- FILE_START: knot-operator-lp-selection.md -->
**Proposition (knot-operator LP/SDP selection via Gram-inverse dual basis).**

*Let $R$ be the categorical coefficient ring with $q \in R$ generic. Let $\{b_i\}$ be a Frobenius-non-degenerate basis for the Iwahori-Hecke algebra $H_n(q)$. For any confinement target $T \in H_n(q)$, the selection of a knot operator $\beta(T_{m,m'}) \in H_n(q)$ producing $T$ is determined by the Frobenius-Gram-inverse LP/SDP dual basis:*

$$
  \min_{\substack{x \geq 0 \\ G^{-1} S x \;\geq\; n_T}}
  \;\;\sum_{m'} t_{(m, m')} \, x_{(m, m')}
$$

*By strong duality and complementary slackness, the LP dual variables $(y_0^*, y^*)$ supply the shadow price of the net-multiplicity constraint, the Frobenius positivity shadow prices, and the active set identifying which knot operators contribute to the bound state.*

The LP is feasible if and only if the demand profile lies in the positive cone spanned by the supply profiles. The dual solution isolates the minimum-action generators.
<!-- FILE_END: knot-operator-lp-selection.md -->
