Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. A :defterm[categorical action]{#categorical-action} on $(\mathbf{C}, A, \tau)$ is a morphism $\mathfrak{S} \colon \mathbf{1} \to \mathbf{1}$ of the form

$$
  \mathfrak{S}
  = 
  \mathrm{ev}_A
    \circ
    \bigl(\mathrm{id}_{A^\vee} \otimes \Phi\bigr)
    \circ
    \mathrm{coev}_A,
$$

where $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$ is the Lagrangian endomorphism. The evaluation $\mathrm{ev}_A \colon A^\vee \otimes A \to \mathbf{1}$ and coevaluation $\mathrm{coev}_A \colon \mathbf{1} \to A \otimes A^\vee$ are the structure maps of the rigid duality on $A$. Composing them with an inserted endomorphism produces the categorical trace $\mathfrak{S} = \mathrm{tr}(\Phi)$.
