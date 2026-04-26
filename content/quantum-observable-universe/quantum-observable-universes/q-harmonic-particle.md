We now make explicit the logical chain leading from the QOU axioms to
the particle concept, before the fermion--boson decomposition that
follows.

By the self-adjointness and positive-definiteness of $\Delta_q$
([self-adjointness](#rem:hodge-laplacian-relation)), a form
$\alpha$ is $q$-harmonic ($\Delta_q \alpha = 0$) if and only if it
is simultaneously $q$-closed and $q$-coclosed:

$$
  \Delta_q\alpha = 0
  \quad\Longleftrightarrow\quad
  d_q\alpha = 0
   \text{and} 
  \delta_q\alpha = 0.
$$

This equivalence follows from $\langle \Delta_q \alpha, \alpha \rangle_\varTheta = \|d_q \alpha\|^2 + \|\delta_q \alpha\|^2$, which
vanishes only when both norms are zero.

Physically:
- $d_q \alpha = 0$ means $\alpha$ is *closed* under $q$-deformed
  differentiation — it has no "sources" in the twisted sense.
- $\delta_q \alpha = 0$ means $\alpha$ is *coclosed* under
  $q$-deformed contraction — it has no "sinks" in the twisted sense.

This is the formal definition of a *particle*: a field configuration
that is in perfect equilibrium with respect to the $q$-deformed
geometry. The [fermion--boson decomposition](#def:fermion-boson-decomposition)
then classifies particles by their vertical component under the
[weight decomposition](#def:weight-decomposition): bosons are purely
horizontal ($\alpha_V = 0$), fermions have non-trivial vertical part.

The complete logical chain is:

$$
  \text{QOU} \xrightarrow{d_q}
  \text{$q$-exterior derivative}
  \xrightarrow{\delta_q}
  \text{$q$-codifferential}
  \xrightarrow{\Delta_q}
  \text{$q$-Laplacian}
  \xrightarrow{\ker}
  \text{particle}
  \xrightarrow{\pi_H \oplus \pi_V}
  \text{boson $\oplus$ fermion.}
$$
