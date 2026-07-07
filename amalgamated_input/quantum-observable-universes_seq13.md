<!-- FILE_START: categorical-dirac-operator-intro.md -->
The examples of the previous section showed how the
abstract QOU triple realises over different base rings; the
substrate parameter $q$, the connection $\nabla$, and the Reeb
derivation $\xi$ are now in hand as universal data. We combine
them into a single first-order operator whose two limits will
recover the gauge and matter terms of the categorical action.

Definition: Categorical Dirac operator introduces
$\mathcal{D}_\nabla = q^{-1}\nabla + (1 - q^{-1})\,\iota_\xi
\nabla \colon A \to \Omega^1(A)$, interpolating between the
full covariant derivative at $q = 1$ and its purely contact
component $\iota_\xi \nabla$ as $q \to \infty$. Proposition: Existence of the categorical Dirac operator — with its proof —
verifies that the formula defines a morphism in $\mathbf{C}$,
and Proposition: uniqueness of the categorical Dirac operator —
with its proof — pins it down once $\nabla$, $q$, and $\xi$ are
fixed. The next section, **Categorical Lagrangian**, takes
$\mathcal{D}_\nabla$ as input and combines it with a state to
form the Lagrangian density.

_(draft.)_
<!-- FILE_END: categorical-dirac-operator-intro.md -->

<!-- FILE_START: categorical-dirac-operator.md -->
Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) equipped with
connection $\nabla$ ([categorical connection](#def:categorical-connection)),
substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)),
and Reeb derivation $\xi$ ([categorical Reeb derivation](#def:categorical-reeb)).
The :defterm[categorical Dirac operator]{#categorical-dirac-operator} is the morphism

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

Cf.\ the spectral-action Dirac operator $D$ on the Hilbert space of a
spectral triple \cite{chamseddine-connes-1997, connes1996}; the
geometric Dirac operators on contact manifolds carrying an analogous
horizontal / Reeb-direction decomposition
\cite{nicolaescu2005, petit-2005}; the one-parameter family
of Dirac operators on contact 3-manifolds
\cite{tsai-2015-i, tsai-2015-ii}; and the Kohn--Dirac operator
built from the Tanaka--Webster connection on CR manifolds
\cite{leitner-2018}.
<!-- FILE_END: categorical-dirac-operator.md -->

<!-- FILE_START: categorical-dirac-operator-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a
[quantum observable universe](#def:quantum-observable-universe) with
connection $\nabla$, substrate parameter $q$, and Reeb derivation
$\xi$.  Then the
[categorical Dirac operator](#def:categorical-dirac-operator)

$$
  \mathcal{D}_\nabla \;=\; q^{-1} \nabla + (1 - q^{-1})  \iota_\xi \nabla
  \;\colon\; A \to \Omega^1(A)
$$

exists as a morphism in $\mathbf{C}$.

Uniqueness is
([uniqueness of categorical Dirac operator](#prop:categorical-dirac-operator-unique)).
<!-- FILE_END: categorical-dirac-operator-exists.md -->

<!-- FILE_START: categorical-dirac-operator-unique.md -->
Given fixed $\nabla$, $q$, and $\xi$, the
[categorical Dirac operator](#def:categorical-dirac-operator)
$\mathcal{D}_\nabla = q^{-1} \nabla + (1 - q^{-1}) \iota_\xi \nabla$
is uniquely determined by the formula.  Any morphism $A \to \Omega^1(A)$
that decomposes as $\alpha \nabla + \beta \iota_\xi \nabla$ with
$\alpha = q^{-1}$ and $\beta = 1 - q^{-1}$ equals $\mathcal{D}_\nabla$.
<!-- FILE_END: categorical-dirac-operator-unique.md -->

