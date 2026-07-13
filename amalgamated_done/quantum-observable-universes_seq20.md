<!-- FILE_START: dq-squared-intro.md -->
We assess the behavior of the deformed differential $d_q$ under iteration. The composition $d_q^2$ does not vanish in general; the obstruction is concentrated on non-Reeb-invariant forms. The $q$-connection forms the structural object whose curvature absorbs this obstruction.
<!-- FILE_END: dq-squared-intro.md -->

<!-- FILE_START: categorical-dq-squared.md -->
The composition $d_q^2 = d_q \circ d_q \colon \Omega^k(A) \to \Omega^{k+2}(A)$ is given by

$$
  d_q^2\alpha =  q^{-1}(1 - q^{-1})\omega_V \wedge_q [\xi, \alpha],
$$

where $\omega_V \in \Omega^2(A)$ is the curvature of the weight decomposition and $[\xi, \alpha]$ is the Lie derivative along the generator $\xi$. 

The composition vanishes if and only if $q = 1$ or $[\xi, \alpha] = 0$. For generic $\alpha$ with $q \neq 1$, $d_q^2 \neq 0$, so the $q$-deformed de Rham complex fails to be a cochain complex. On $\xi$-invariant horizontal forms, $d_q$ reduces to $q^{-1} d$ and $d_q^2 = 0$.
<!-- FILE_END: categorical-dq-squared.md -->

<!-- FILE_START: categorical-q-lie-bracket.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. The **$q$-deformed Lie bracket** on derivations of $A$ is

$$
  [X, Y]_q =  q^{-1}[X, Y] + (1 - q^{-1})\bigl(\varTheta_A(X)[\xi, Y] - \varTheta_A(Y)[\xi, X]\bigr),
$$

where $\varTheta_A$ is the canonical $1$-form dual to the Reeb derivation $\xi$.
<!-- FILE_END: categorical-q-lie-bracket.md -->

<!-- FILE_START: categorical-q-connection.md -->
Let $\nabla$ be a categorical connection on $A$ and $\xi$ the Reeb derivation. The **$q$-deformed connection** is

$$
  \nabla_q =  q^{-1}\nabla + (1 - q^{-1})(\iota_\xi \nabla)\varTheta_A.
$$

At $q = 1$, $\nabla_q = \nabla$.
<!-- FILE_END: categorical-q-connection.md -->

<!-- FILE_START: categorical-q-connection-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with categorical connection $\nabla$. The categorical $q$-connection $\nabla_q$ exists as a morphism $A \to \Omega^1(A)$.
<!-- FILE_END: categorical-q-connection-exists.md -->

<!-- FILE_START: categorical-q-connection-unique.md -->
For fixed $\nabla$, $\xi$, $\varTheta$, and $q$, the categorical $q$-connection is uniquely determined. Up to gauge transformations, $\nabla_q$ inherits the gauge freedom of its base connection $\nabla$.
<!-- FILE_END: categorical-q-connection-unique.md -->
