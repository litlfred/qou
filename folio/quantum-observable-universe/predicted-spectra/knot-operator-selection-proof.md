## Proof sketch

**(i)** The Hecke algebra $H_r(q)$ is semisimple for generic $q$,
so $\mathrm{End}_{H_r(q)}(V^{\otimes r})$ decomposes as
$\bigoplus_\lambda \mathrm{End}(V_\lambda)$ by the Wedderburn
theorem.  The Markov trace projects onto each component with
weight $d_\lambda(q)$ by Schur orthogonality
([RJ inner product](#prop:rj-canonical-inner-product)).

**(ii)** The categorical action
$\mathfrak{S} = \mathrm{ev}_A \circ (\mathrm{id}_{A^\vee} \otimes \Phi) \circ \mathrm{coev}_A = \mathrm{tr}(\Phi)$
is linear in $\Phi$.  Substituting the spectral decomposition
(i) and using the identification
$\mathrm{tr} = \mathrm{tr}_M$ (archimedean :refterm[descent]{#descent},
[RJ interpretation](#rem:rj-inner-product-interpretation))
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
character evaluation.  For pair production at our $q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps),
this is $T_{2,3}$ (trefoil, $e^-$) — the lowest-crossing
operator that unconditionally opens the degree-3 channel.

## Explicit dual construction

Consider a state $K \in H_3(q)$ with decomposition $K = \sum_i c_i b_i$. The Frobenius dual $K^\vee$ is the unique element satisfying

$$
  \langle K^\vee, b_i \rangle_F = c_i
  \quad \forall i.
$$

By non-degeneracy (**convention D**: read on the quotient $H_n/\mathrm{rad}\,\mathrm{tr}_M \cong \mathrm{TL}_n$, where the induced pairing is non-degenerate; on $H_n$ itself $\det G = 0$ exactly, the $(1^3)$ block being the radical), $K^\vee$ exists and is unique. In the basis, $K^\vee = \sum_i c_i (G^{-1})_{ij} b_j$, where $G_{ij} = \langle b_i, b_j \rangle_F = \mathrm{tr}_M(b_i \cdot b_j)$ is the $6 \times 6$ Gram matrix of $H_3(q)$.

The demand vector of $K$ is the negative part:

$$
  \mathrm{dem}(K) = \sum_{i : c_i < 0} |c_i| \, b_i^\vee.
$$

The operator that fills the demand at minimum crossing energy is

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

For the positron ($e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$), the demand profile is $\{-0.218\gamma, -0.209 L_+, -0.209 L_-\}$. The mirror trefoil demands vacuum energy and Hopf content. The minimum-energy supply is the coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$, which provides exactly the identity and Hopf content from the rigid structure. Its cost is $\mathrm{tr}(\mathrm{id}_A) = [2]_q = q + q^{-1} \approx 2.011$.
