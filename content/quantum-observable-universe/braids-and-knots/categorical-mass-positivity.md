**Remark (no exhaustive positivity proof needed).**
*The categorical mass scalars produced by the
[mass identity](#def:mass-identity) are values of the observation
functor $\tau$ on graded projective KLR modules
\cite{khovanovlauda2009, brundankleshchev2009}.  By construction
$\tau$ takes the graded Euler characteristic, so each coefficient
of the resulting polynomial is the dimension of a $\mathrm{Hom}$-space
between graded projectives:*

$$
  [\tau(\mathfrak{M}_K)]_d \;=\;
  \dim_R \mathrm{Hom}_{\mathcal{K}_n}\bigl(P_d, \mathfrak{M}_K\bigr)
  \;\in\; \mathbb{Z}_{\geq 0}.
$$

*Consequently the categorical mass and action coefficients are
**structurally** non-negative integers; an explicit positivity
argument per coefficient is unnecessary.  Coefficients that vanish
correspond to summands that lie in the
[cemetery group](#def:cemetery-group), which the engine drops
during traversal — see
[cemetery-group emergence](#conj:cemetery-group-emergence).*

*The polynomial $\tau(\mathfrak{M}_K) = P_K(q)$ is therefore the
**mass-spectrum generating function** of $K$: each term $c_d q^d$ is
a mass component indexed by **graded Hecke energy** $d$ with
**microstate degeneracy** $c_d$. The relation to the macroscopic
scalar is a functorial composition (decategorification, then
evaluation at the substrate $q_0$, then dimensional anchor), not an
identity — see [mass-spectrum generating
function](#rem:mass-spectrum-generating-function) for the full
$\mathfrak{M}_K \to P_K(q) \to M_K \approx m_0 \cdot |P_K(q_0)|$
pipeline.*
