Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) equipped with
connection $\nabla$ ([categorical connection](#def:categorical-connection)),
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
and Reeb derivation $\xi$ ([categorical Reeb derivation](#def:categorical-reeb)).
The *categorical Dirac operator* is the morphism

$$
  \mathcal{D}_\nabla
  \;=\;
  q^{-1}\,\nabla \;+\; (1 - q^{-1})\,\iota_\xi\,\nabla
  \;\colon\; A \to \Omega^1(A).
$$

When $q = 1$ this reduces to $\mathcal{D}_\nabla = \nabla$, the
undeformed covariant derivative.  The $q$-deformation interpolates
between the full connection and its projection onto the Reeb direction:
as $q \to \infty$ we obtain $\mathcal{D}_\nabla \to \iota_\xi\nabla$,
the purely contact component.
