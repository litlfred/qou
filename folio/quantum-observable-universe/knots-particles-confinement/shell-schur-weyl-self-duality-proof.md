*Proof.*

**1. $\#$ is well defined.** Put $\tau_i = h - \sigma_i$. From $\sigma_i^2 = h\sigma_i + 1$,

$$
  \tau_i^2 \;=\; h^2 - 2h\sigma_i + \sigma_i^2 \;=\; h(h - \sigma_i) + 1 \;=\; h\,\tau_i + 1,
$$

so $\tau_i$ satisfies the Hecke quadratic. For adjacent $i, j$, expanding gives

$$
  \tau_i\tau_j\tau_i - \tau_j\tau_i\tau_j
  \;=\; h^2(\sigma_j - \sigma_i) + h(\sigma_i^2 - \sigma_j^2) - (\sigma_i\sigma_j\sigma_i - \sigma_j\sigma_i\sigma_j),
$$

which vanishes by the quadratic and braid relations. Far commutativity is immediate. Since $\tau_i^2 = h\tau_i + 1$ again, $\# \circ \# = \mathrm{id}$, so $\#$ is an automorphism. The identity $h - \sigma_i = -\sigma_i^{-1}$ follows from $\sigma_i(\sigma_i - h) = 1$.

**2. $\#$ transposes the blocks.** In the split semisimple case, twisting the Specht module $S^\lambda$ by $\#$ gives the dual Specht module of $\lambda^*$, which is isomorphic to $S^{\lambda^*}$ (see Mathas, *Iwahori–Hecke algebras and Schur algebras*, Ch. 3, and \cite{dipper-james1986}). Hence $\#(e_\lambda) = e_{\lambda^*}$. At $q = 1$ this is the twist by the sign character, $V_\lambda \otimes \mathrm{sgn} \cong V_{\lambda^*}$.

**3. Fixed points.** Applying $\#$,

$$
  \#(\sigma_{\mathrm{shell}}) \;=\; \sum_\lambda x_\lambda\, e_{\lambda^*} \;=\; \sum_\lambda x_{\lambda^*}\, e_\lambda .
$$

The $e_\lambda$ are linearly independent, so $\#(\sigma_{\mathrm{shell}}) = \sigma_{\mathrm{shell}}$ if and only if $x_\lambda = x_{\lambda^*}$ for every $\lambda$. $\square$

**Relation to existing propositions.**
This result refines [Frobenius shadow-price identity](#prop:mass-coefficient-shadow-price) (which gives $y_\lambda$ per partition) by characterising when the shell operator's coefficients are symmetric under transposition. Whether $\sigma_{\mathrm{shell}}$ is in fact $\#$-invariant is not settled here. It complements [crossing asymmetry and Coulomb shift](#prop:skein-crossing-asymmetry) (which encodes the parity-violation mechanism at level 3).
