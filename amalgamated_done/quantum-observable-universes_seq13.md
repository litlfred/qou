<!-- FILE_START: categorical-dirac-operator-intro.md -->
We combine the substrate parameter $q$, the connection $\nabla$, and the Reeb derivation $\xi$ into a single first-order operator whose two limits recover the gauge and matter terms of the categorical action. The categorical Dirac operator interpolates between the full covariant derivative at $q = 1$ and its purely contact component $\iota_\xi \nabla$ as $q \to \infty$. This formula defines a unique morphism in $\mathbf{C}$ once $\nabla$, $q$, and $\xi$ are fixed.
<!-- FILE_END: categorical-dirac-operator-intro.md -->

<!-- FILE_START: categorical-dirac-operator.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe equipped with connection $\nabla$, substrate parameter $q$, and Reeb derivation $\xi$. The **categorical Dirac operator** is the morphism

$$
  \mathcal{D}_\nabla
  = 
  q^{-1}\nabla +  (1 - q^{-1})\iota_\xi\nabla
   \colon  A \to \Omega^1(A).
$$

When $q = 1$ this reduces to $\mathcal{D}_\nabla = \nabla$, the undeformed covariant derivative. The $q$-deformation interpolates between the full connection and its projection onto the Reeb direction. As $q \to \infty$, we obtain $\mathcal{D}_\nabla \to \iota_\xi\nabla$, the purely contact component.
<!-- FILE_END: categorical-dirac-operator.md -->

<!-- FILE_START: categorical-dirac-operator-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with connection $\nabla$, substrate parameter $q$, and Reeb derivation $\xi$. The categorical Dirac operator $\mathcal{D}_\nabla = q^{-1} \nabla + (1 - q^{-1}) \iota_\xi \nabla \colon A \to \Omega^1(A)$ exists as a morphism in $\mathbf{C}$.
<!-- FILE_END: categorical-dirac-operator-exists.md -->

<!-- FILE_START: categorical-dirac-operator-unique.md -->
Given fixed $\nabla$, $q$, and $\xi$, the categorical Dirac operator $\mathcal{D}_\nabla = q^{-1} \nabla + (1 - q^{-1}) \iota_\xi \nabla$ is uniquely determined by the formula. Any morphism $A \to \Omega^1(A)$ that decomposes as $\alpha \nabla + \beta \iota_\xi \nabla$ with $\alpha = q^{-1}$ and $\beta = 1 - q^{-1}$ equals $\mathcal{D}_\nabla$.
<!-- FILE_END: categorical-dirac-operator-unique.md -->
