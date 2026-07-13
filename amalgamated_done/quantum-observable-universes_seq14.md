<!-- FILE_START: categorical-lagrangian-intro.md -->
The categorical Dirac operator $\mathcal{D}_\nabla$ combines with a state $\psi \colon \mathbf{1} \to A$ to form the endomorphism of $A$ that will be traced to yield the action. The categorical Lagrangian $\mathcal{L}_q(\nabla, \psi) = \mathcal{D}_\nabla^2 + \psi^* \otimes \mathcal{D}_\nabla\psi \in \mathrm{End}_{\mathbf{C}}(A)$ packages the bosonic and fermionic sectors before trace-integration. This endomorphism exists uniquely once $\nabla$, $\psi$, $q$, and $\xi$ are chosen.
<!-- FILE_END: categorical-lagrangian-intro.md -->

<!-- FILE_START: categorical-lagrangian.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with categorical Dirac operator $\mathcal{D}_\nabla$ and a state $\psi \colon \mathbf{1} \to A$. The **categorical Lagrangian** is the endomorphism

$$
  \mathcal{L}_q(\nabla, \psi)
  = 
  \mathcal{D}_\nabla^{2}
  + 
  \psi^* \otimes \mathcal{D}_\nabla\psi
   \in  \mathrm{End}_{\mathbf{C}}(A),
$$

where $\psi^* = \int_A \!\circ S(\psi) \colon A \to \mathbf{1}$ is the adjoint section. The Lagrangian acts as the categorical analog of a Lagrangian density before integration over spacetime. Its first summand $\mathcal{D}_\nabla^2$ encodes the bosonic sector; the second summand encodes the fermionic coupling of the state to the connection.
<!-- FILE_END: categorical-lagrangian.md -->

<!-- FILE_START: categorical-lagrangian-exists.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with categorical Dirac operator $\mathcal{D}_\nabla$ and state $\psi \colon \mathbf{1} \to A$. The categorical Lagrangian $\mathcal{L}_q(\nabla, \psi) = \mathcal{D}_\nabla^2 + \psi^* \otimes \mathcal{D}_\nabla \psi \in \mathrm{End}_{\mathbf{C}}(A)$ exists as an endomorphism of $A$.
<!-- FILE_END: categorical-lagrangian-exists.md -->

<!-- FILE_START: categorical-lagrangian-unique.md -->
For fixed $(\nabla, \psi)$, the categorical Lagrangian $\mathcal{L}_q(\nabla, \psi)$ is uniquely determined by its defining formula. Any endomorphism of $A$ equal to $\mathcal{D}_\nabla^2 + \psi^* \otimes \mathcal{D}_\nabla \psi$ coincides with $\mathcal{L}_q$.
<!-- FILE_END: categorical-lagrangian-unique.md -->
