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
