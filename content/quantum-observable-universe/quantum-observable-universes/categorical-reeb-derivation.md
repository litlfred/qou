Let $A$ be a Frobenius--Hopf substrate in a rigid :refterm[monoidal category]{#monoidal-category}
$\mathbf{C}$. The **categorical Reeb derivation** is the morphism
$\xi_q \colon A \to A$ uniquely determined by the following two
conditions.

**Normalization.** The derivation is compatible with the contact form
$\varTheta$:

$$
\xi_q \circ \varTheta =  \varTheta,
$$

so that $\xi_q$ preserves the contact structure on the state bundle
$\mathcal{S}$.

**Derivation property.** The morphism $\xi_q$ satisfies the Leibniz
rule with respect to the multiplication $\mu$ of $A$:

$$
\xi_q \circ \mu
=  \mu \circ (\xi_q \otimes \mathrm{id} + \mathrm{id} \otimes \xi_q).
$$

The *period* of the Reeb derivation is the smallest positive integer
$\Omega_q$ (when it exists) such that the iterated composition satisfies

$$
\xi_q^{\Omega_q} =  \mathrm{id}_A.
$$

The derivation $\xi_q$ encodes the *observer drift*: the intrinsic time
evolution of the substrate as seen from within. The periodicity condition
ensures that the Reeb flow closes, yielding a discrete spectrum of
frequencies on $A$. Each eigenvalue of $\xi_q$ corresponds to a
fundamental mode of the substrate, and the full Reeb spectrum is
determined by the spectral geometry of Bring's curve $\mathcal{B}$.
