The physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ of the
categorical action
([categorical action](#def\:categorical-action)) is not a single
knot operator: it is an element of a **vector space** that
decomposes over the irreducible representations of $H_n(q)$.
This decomposition, combined with the Frobenius self-duality
$A \cong A^\vee$, determines which knot operators mediate any
given interaction and with what weights.

## Statement

**Proposition (knot operator selection).**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with archimedean
realisation $H_r(q)$, and let
$\{\tau(r_i, s_i)\}_{i=1}^{6}$ be the embeddable torus knots on
$\Sigma_4$
([cohomological embedding](#prop\:cohomological-embedding)).
Let $\gamma_1, \gamma_2 \in H_3(q)$ be two incoming particle
states.*

**(i) Spectral decomposition of the mediating endomorphism.**
*The physics endomorphism $\Phi$ decomposes via Schur
orthogonality
([RJ canonical inner product](#prop\:rj-canonical-inner-product))
as:*

$$
  \Phi
  =
  \sum_{\lambda \vdash r}
  d_\lambda(q) \cdot \Phi_\lambda,
$$

*where $d_\lambda(q)$ is the quantum dimension of irrep $\lambda$
and $\Phi_\lambda = e_\lambda \Phi e_\lambda$ is the projection
of $\Phi$ onto the $\lambda$-isotypic component.  Each irrep
$\lambda$ corresponds to a torus knot $\tau(r,s)$ via the
knot eigenbasis.*

**(ii) Multi-channel pair production.**
*The categorical action of two photons $\gamma_1, \gamma_2$
through the mediating endomorphism is:*

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

*Multiple knot operators act **simultaneously**, each weighted
by its quantum dimension.  The interaction is a superposition
of channels, not a single operator selection.*

**(iii) Frobenius demand--supply pairing.**
*The Frobenius self-duality $A \xrightarrow{\sim} A^\vee$ via
$\int_A \circ \mu$ identifies the NF decomposition of each
state with its dual.  For a state $K = \sum_i c_i b_i$ in the
NF basis $\{b_i\} = \{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$:*

* *Positive coefficients $c_i > 0$ are **supply**: channels the
  state provides.*
* *Negative coefficients $c_i < 0$ are **demand**: channels the
  state requires from its interaction partner.*

*The Frobenius pairing
$\langle K_1, K_2 \rangle_F = \mathrm{tr}_M(K_1 \cdot K_2)$
is non-degenerate (QUO-1), so for every nonzero demand profile,
there exists a unique minimal-norm supply that satisfies it.*

**(iv) Minimum-action selection.**
*Among all $\Phi \in \mathrm{End}(A)$ compatible with the
on-shell condition $\star_q F_\nabla = F_\nabla$
([instanton on-shell](#rem\:instanton-on-shell)), the physical
interaction selects the $\Phi$ minimizing the categorical
action $|\mathfrak{S}| = |\mathrm{tr}(\Phi)|$.  The dominant
channel is the irrep $\lambda_*$ with largest
$|d_{\lambda_*}(q) \cdot \mathrm{tr}_{\lambda_*}(\gamma_1 \cdot \beta(\tau_{\lambda_*}) \cdot \gamma_2)|$.*

## Proof sketch

**(i)** The Hecke algebra $H_r(q)$ is semisimple for generic $q$,
so $\mathrm{End}_{H_r(q)}(V^{\otimes r})$ decomposes as
$\bigoplus_\lambda \mathrm{End}(V_\lambda)$ by the Wedderburn
theorem.  The Markov trace projects onto each component with
weight $d_\lambda(q)$ by Schur orthogonality
([RJ inner product](#prop\:rj-canonical-inner-product)).

**(ii)** The categorical action
$\mathfrak{S} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi) \circ \mathrm{coev}_A = \mathrm{tr}(\Phi)$
is linear in $\Phi$.  Substituting the spectral decomposition
(i) and using the identification
$\mathrm{tr} = \mathrm{tr}_M$ (archimedean :refterm[descent]{#descent},
[RJ interpretation](#rem\:rj-inner-product-interpretation))
gives the stated sum over channels.

**(iii)** The Frobenius pairing
$\langle a, b \rangle_F = \int_A \mu(a \otimes b) = \mathrm{tr}_M(\rho(\hat\beta_a) \cdot \rho(\hat\beta_b))$
is the categorical inner product.  Non-degeneracy (QUO-1) means
every element has a unique Frobenius dual.  In the NF basis,
this identifies positive coefficients with morphisms
$\mathbf{1} \to A$ (supply, via coevaluation) and negative
coefficients with morphisms $A \to \mathbf{1}$ (demand, via
evaluation).

**(iv)** The on-shell condition constrains $\Phi$ to lie in the
self-dual curvature subspace ($S([\sigma_i, \sigma_j])^* = [\sigma_i, \sigma_j]$).
Within this subspace, the extremum of $|\mathrm{tr}(\Phi)|$ is
attained at the irrep with largest quantum dimension times
character evaluation.  For pair production at our $q_0 = 1.109978595554181\ldots$ (50 dps),
this is $T_{2,3}$ (trefoil, $e^-$) — the lowest-crossing
operator that unconditionally opens the degree-3 channel.

## Multi-channel interpretation

For Breit--Wheeler pair production $\gamma\gamma \to e^-e^+$,
the full interaction is:

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

**All channels fire simultaneously.**  Two incoming photons
can:

* change polarisation (trivial operator, no pair created),
* exchange a gluon ($T_{2,2}$, Hopf link),
* create $e^-e^+$ ($T_{2,3}$, trefoil), and
* create $\mu^-\mu^+$ ($T_{2,5}$, cinquefoil, suppressed by
  higher crossing energy)

in a single interaction, with each channel weighted by its
quantum dimension $d_\lambda(q)$.  The branching ratios are
determined entirely by $q$ and the polarisation content
$\varphi_0, \varphi_1$ of the incoming photons.

What we detect experimentally is the **dominant channel** —
the one with the largest weight.  The subdominant channels
are real but suppressed: they contribute to radiative
corrections, vacuum polarisation, and the running of coupling
constants.  In particular, the elastic channel ($T_{1,0}$)
is always present — photon--photon scattering without pair
creation is the leading process, with pair creation as a
threshold-activated subdominant channel.

## Explicit dual construction

Given a state $K \in H_3(q)$ with NF decomposition
$K = \sum_i c_i b_i$, the **Frobenius dual** $K^\vee$ is
the unique element satisfying:

$$
  \langle K^\vee, b_i \rangle_F = c_i
  \quad \forall i.
$$

By non-degeneracy, $K^\vee$ exists and is unique.  In the
NF basis, $K^\vee = \sum_i c_i (G^{-1})_{ij} b_j$ where
$G_{ij} = \langle b_i, b_j \rangle_F = \mathrm{tr}_M(b_i \cdot b_j)$
is the $6 \times 6$ Gram matrix of $H_3(q)$.

The **demand vector** of $K$ is the negative part:

$$
  \mathrm{dem}(K) = \sum_{i : c_i < 0} |c_i| \, b_i^\vee,
$$

and the **operator that fills the demand** at minimum crossing
energy is:

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

For the positron ($e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$),
the demand profile is $\{-0.218\gamma, -0.209 L_+, -0.209 L_-\}$
— the mirror trefoil demands vacuum energy and Hopf content.
The minimum-energy supply is the coevaluation
$\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$, which
provides exactly the identity and Hopf content from the rigid
structure at cost $\mathrm{tr}(\mathrm{id}_A) = [2]_q = q + q^{-1} \approx 2.011$.
