## Statement

**Proposition (knot operator selection).**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with archimedean realisation $H_r(q)$. Let $\{\tau(r_i, s_i)\}_{i=1}^{6}$ be the embeddable torus knots on $\Sigma_4$. Let $\gamma_1, \gamma_2 \in H_3(q)$ be two incoming particle states.*

**(i)** *Spectral decomposition of the mediating endomorphism. The Lagrangian endomorphism $\Phi$ decomposes via Schur orthogonality:*

$$
  \Phi
  =
  \sum_{\lambda \vdash r}
  d_\lambda(q) \cdot \Phi_\lambda,
$$

*where $d_\lambda(q)$ is the quantum dimension of irrep $\lambda$. The operator $\Phi_\lambda = e_\lambda \Phi e_\lambda$ is the projection of $\Phi$ onto the $\lambda$-isotypic component. Each irrep $\lambda$ corresponds to a torus knot $\tau(r,s)$ via the knot eigenbasis.*

**(ii)** *Multi-channel pair production. The categorical action of two photons $\gamma_1, \gamma_2$ through the mediating endomorphism is:*

$$
  \mathcal{S}(\gamma_1, \gamma_2)
  =
  \mathrm{tr}\!\left(
    \Phi \cdot (\gamma_1 \otimes \gamma_2)
  \right)
  =
  \sum_{\lambda}
  d_\lambda(q) \cdot
  \mathrm{tr}_\lambda\!\bigl(
    \gamma_1 \cdot \beta(\tau_\lambda) \cdot \gamma_2
  \bigr).
$$

*Multiple knot operators act simultaneously, each weighted by its quantum dimension; the interaction is a superposition of channels.*

**(iii)** *Frobenius demand--supply pairing. The Frobenius self-duality $A \xrightarrow{\sim} A^\vee$ via $\int_A \circ \mu$ identifies the normal form decomposition of each state with its dual. For a state $K = \sum_i c_i b_i$ in the basis $\{b_i\} = \{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$: positive coefficients $c_i > 0$ are supply (channels the state provides) and negative coefficients $c_i < 0$ are demand (channels the state requires from its partner). The Frobenius pairing $\langle K_1, K_2 \rangle_F = \mathrm{tr}_M(K_1 \cdot K_2)$ is degenerate on $H_3(q)$ under the canonical Markov convention: its radical is the one-dimensional span of the $q$-antisymmetriser $v = (-q^3, q^2, q^2, -q, -q, 1)$, and $\det G = 0$ identically in $q$. The pairing therefore descends to a non-degenerate pairing on the quotient $H_3(q)/\mathrm{rad}$, and a minimal-norm supply exists there and is unique modulo the radical — but only for demand profiles lying in the image of the pairing, equivalently those orthogonal to $v$. A demand profile with nonzero radical component admits no supply at all.*

**(iv)** *Minimum-action selection. The physical interaction selects the $\Phi \in \mathrm{End}(A)$ minimizing the categorical action $|\mathfrak{S}| = |\mathrm{tr}(\Phi)|$ among those compatible with the on-shell condition $\star_q F_\nabla = F_\nabla$. The dominant channel is the irrep $\lambda_*$ with the largest $|d_{\lambda_*}(q) \cdot \mathrm{tr}_{\lambda_*}(\gamma_1 \cdot \beta(\tau_{\lambda_*}) \cdot \gamma_2)|$.*
