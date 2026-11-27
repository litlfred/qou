Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe, with $\mathbf{C}$ linear over the Laurent ring $R_q$, and let $q \in R_q$ have inverse $q^{-1}$. Given morphisms

$$
  \nabla \colon A \to A \otimes \Omega^1, \qquad
  \iota_\xi \nabla \colon A \to A, \qquad
  \theta_\nabla \colon A \to A \otimes \Omega^1,
$$

define

$$
  \nabla_q \;:=\; q^{-1}\,\nabla \;+\; (1 - q^{-1})\,(\iota_\xi \nabla \mathbin{;} \theta_\nabla) \colon A \to A \otimes \Omega^1 .
$$

Then these data assemble into a [categorical $q$-connection](#def:categorical-q-connection) whose $q$-connection morphism is $\nabla_q$.

The existence is by construction: $\nabla_q$ is defined by the formula above. That $\nabla$ is a categorical connection in the sense of [prop:categorical-connection-exists](#prop:categorical-connection-exists), and any property of $\nabla_q$ beyond its formula, are not part of this statement.
