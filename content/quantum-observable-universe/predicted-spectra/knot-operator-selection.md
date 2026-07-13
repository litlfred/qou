The Lagrangian endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ of the categorical action decomposes over the irreducible representations of $H_n(q)$. This decomposition and the Frobenius self-duality $A \cong A^\vee$ determine the specific knot operators that mediate any interaction. They also determine their corresponding weights.

## Statement

**Proposition (knot operator selection).**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with archimedean realisation $H_r(q)$. Let $\{\tau(r_i, s_i)\}_{i=1}^{6}$ be the embeddable torus knots on $\Sigma_4$. Let $\gamma_1, \gamma_2 \in H_3(q)$ be two incoming particle states.*

**(i) Spectral decomposition of the mediating endomorphism.**
*The Lagrangian endomorphism $\Phi$ decomposes via Schur orthogonality:*

$$
  \Phi
  =
  \sum_{\lambda \vdash r}
  d_\lambda(q) \cdot \Phi_\lambda,
$$

*where $d_\lambda(q)$ is the quantum dimension of irrep $\lambda$. The operator $\Phi_\lambda = e_\lambda \Phi e_\lambda$ is the projection of $\Phi$ onto the $\lambda$-isotypic component. Each irrep $\lambda$ corresponds to a torus knot $\tau(r,s)$ via the knot eigenbasis.*

**(ii) Multi-channel pair production.**
*The categorical action of two photons $\gamma_1, \gamma_2$ through the mediating endomorphism is:*

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

*Multiple knot operators act simultaneously. The quantum dimension weights each operator. The interaction is a superposition of channels.*

**(iii) Frobenius demand--supply pairing.**
*The Frobenius self-duality $A \xrightarrow{\sim} A^\vee$ via $\int_A \circ \mu$ identifies the normal form decomposition of each state with its dual. For a state $K = \sum_i c_i b_i$ in the basis $\{b_i\} = \{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$:*

* *Positive coefficients $c_i > 0$ are supply. These are channels the state provides.*
* *Negative coefficients $c_i < 0$ are demand. These are channels the state requires from its interaction partner.*

*The Frobenius pairing $\langle K_1, K_2 \rangle_F = \mathrm{tr}_M(K_1 \cdot K_2)$ is non-degenerate (QUO-1). For every nonzero demand profile, a unique minimal-norm supply satisfies it.*

**(iv) Minimum-action selection.**
*The physical interaction selects the $\Phi \in \mathrm{End}(A)$ minimizing the categorical action $|\mathfrak{S}| = |\mathrm{tr}(\Phi)|$ among those compatible with the on-shell condition $\star_q F_\nabla = F_\nabla$. The dominant channel is the irrep $\lambda_*$ with the largest $|d_{\lambda_*}(q) \cdot \mathrm{tr}_{\lambda_*}(\gamma_1 \cdot \beta(\tau_{\lambda_*}) \cdot \gamma_2)|$.*

## Multi-channel interpretation

For Breit--Wheeler pair production $\gamma\gamma \to e^-e^+$, the full interaction is:

$$
  \mathcal{S}(\gamma_1, \gamma_2)
  =
  \underbrace{d_{\mathrm{triv}}(q) \cdot P_{T_{1,0}}}_{\text{elastic: polarisation change}}
  +
  \underbrace{d_{\Box}(q) \cdot P_{T_{2,1}}}_{\text{single crossing}}
  +
  \underbrace{d_{\Box\Box}(q) \cdot P_{T_{2,2}}}_{\text{Hopf link (gluon)}}
  +
  \underbrace{d_{\yng(2,1)}(q) \cdot P_{T_{2,3}}}_{\text{trefoil (electron)}}
  +  \cdots
$$

All channels fire simultaneously. Two incoming photons can:

* change polarisation (trivial operator, no pair created),
* exchange a gluon ($T_{2,2}$, Hopf link),
* create $e^-e^+$ ($T_{2,3}$, trefoil),
* create $\mu^-\mu^+$ ($T_{2,5}$, cinquefoil, suppressed by higher crossing energy).

These events occur in a single interaction. The quantum dimension $d_\lambda(q)$ weights each channel. The branching ratios depend entirely on $q$ and the incoming photon polarisation content $\varphi_0, \varphi_1$.

Experiments detect the dominant channel. This channel carries the largest weight. The subdominant channels contribute to radiative corrections, vacuum polarisation, and the running of coupling constants. The elastic channel ($T_{1,0}$) is always present. Photon--photon scattering without pair creation is the leading process. Pair creation is a threshold-activated subdominant channel.

## Explicit dual construction

We consider a state $K \in H_3(q)$ with decomposition $K = \sum_i c_i b_i$. The Frobenius dual $K^\vee$ is the unique element satisfying:

$$
  \langle K^\vee, b_i \rangle_F = c_i
  \quad \forall i.
$$

By non-degeneracy, $K^\vee$ exists and is unique. In the basis, $K^\vee = \sum_i c_i (G^{-1})_{ij} b_j$. The term $G_{ij} = \langle b_i, b_j \rangle_F = \mathrm{tr}_M(b_i \cdot b_j)$ is the $6 \times 6$ Gram matrix of $H_3(q)$.

The demand vector of $K$ is the negative part:

$$
  \mathrm{dem}(K) = \sum_{i : c_i < 0} |c_i| \, b_i^\vee.
$$

The operator that fills the demand at minimum crossing energy is:

$$
  \Phi_{\mathrm{min}}
  =
  \arg\min_{\Phi \in \mathrm{End}(A)_{\mathrm{on-shell}}}
  \left\{
    \mathfrak{E}_{\mathrm{cross}}(\Phi)
    \ \Big|\ 
    \langle \Phi, \mathrm{dem}(K) \rangle_F \geq
    \|\mathrm{dem}(K)\|_F
  \right\}.
$$

For the positron ($e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$), the demand profile is $\{-0.218\gamma, -0.209 L_+, -0.209 L_-\}$. The mirror trefoil demands vacuum energy and Hopf content. The minimum-energy supply is the coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$. This morphism provides exactly the identity and Hopf content from the rigid structure. Its cost is $\mathrm{tr}(\mathrm{id}_A) = [2]_q = q + q^{-1} \approx 2.011$.
