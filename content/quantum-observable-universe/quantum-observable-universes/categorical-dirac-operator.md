Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) equipped with
connection $\nabla$ ([categorical connection](#def:categorical-connection)),
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
and Reeb derivation $\xi$ ([categorical Reeb derivation](#def:categorical-reeb)).
The *categorical Dirac operator* is the morphism

$$
  \mathcal{D}_\nabla
  = 
  q^{-1}\nabla +  (1 - q^{-1})\iota_\xi\nabla
   \colon  A \to \Omega^1(A).
$$

When $q = 1$ this reduces to $\mathcal{D}_\nabla = \nabla$, the
undeformed covariant derivative.  The $q$-deformation interpolates
between the full connection and its projection onto the Reeb direction:
as $q \to \infty$ we obtain $\mathcal{D}_\nabla \to \iota_\xi\nabla$,
the purely contact component.

In Connes' non-commutative geometry the Dirac operator $D$ is a
self-adjoint unbounded operator on a Hilbert space, around which the
spectral action $\mathrm{Tr}\,\chi(D/\Lambda) + (\psi, D\psi)$ is built
\cite{chamseddine-connes-1997, connes1996}.  The categorical Dirac
operator $\mathcal{D}_\nabla$ above plays the same structural role inside
the monoidal setting, but its Reeb-contact decomposition
$q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$ is specific to the
substrate's contact geometry and does not appear in the
quantum-group Dirac operators of Krähmer or Neshveyev--Tuset.
