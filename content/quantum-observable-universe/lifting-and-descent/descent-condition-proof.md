Let $\{U_i\}$ be a good cover trivialising the tower.  On
$U_i \cap U_j$ the gauge transition function $g_{ij}^{(n)}$ patches
the connection $A_n$:

$$
  A_n|_{U_j} =  g_{ij}^{(n)} \cdot A_n|_{U_i} \cdot
  (g_{ij}^{(n)})^{-1} + (g_{ij}^{(n)})^{-1} dg_{ij}^{(n)}.
$$

On a triple overlap $U_i \cap U_j \cap U_k$, the ordinary cocycle
condition $g_{ij}^{(n)} \cdot g_{jk}^{(n)} = g_{ik}^{(n)}$ holds if and
only if the connection $A_n$ is globally well-defined at level $n$ with
no twist.  The passage from level $n$ to level $n{+}1$ via the central
extension $\mathfrak{G}_{n+1} \to \mathfrak{G}_n$ introduces the
$2$-morphism twist.

By
([cocycle deviation as a twisted Cech 2-cocycle](#lem:descent-cocycle-deviation)),
the cocycle deviation at level $n+1$ satisfies the twisted Cech
$2$-cocycle equation, with cohomology class in
$H^2(M, \mathcal{O}_M^{\times})$.  This class is precisely the
obstruction class $\kappa_n$ of
[quantum characteristic classes](#def:quantum-characteristic-classes):
it vanishes if and only if the cocycle deviation at level $n$ can be
absorbed by the $2$-morphism data, i.e. the lift from $\mathfrak{G}_n$
to $\mathfrak{G}_{n+1}$ is unobstructed.

By [Theorem 1.7, yekutieli2010], this is equivalent to the
vanishing of the Yekutieli obstruction class, closing the circle with
the lifting criterion ([Yekutieli lifting](#prop:yekutieli-lifting)).
$\square$
