**Proposition.**
*Let $\mathfrak{O}\in \Gamma(U, \mathrm{Ad}(J^1 \mathcal{S}))$
be an observation ([observation](#def:observation)) with
substrate perturbation $\delta q$.  Then:*

1. **(Quantum energy increases.)** *The quantum Planck constant
   $\hbar_q = 1 - q^{-1}$
   ([quantum Planck constant](#def:quantum-planck-constant))
   satisfies*

   $$
     \hbar_{q + \delta q} - \hbar_q
     =  \frac{\delta q}{q(q + \delta q)}
      >  0
   $$

   *for $\delta q > 0$.  Every observation with positive
   substrate perturbation strictly increases the quantum
   energy of the system.*

2. **(Action deformation.)** *The categorical action
   $S_q[\nabla, \lambda, \psi]$
   ([categorical action](#def:categorical-action)) evaluated
   at the perturbed parameter $q' = q + \delta q$ satisfies*

   $$
     S_{q'}
     = 
     S_q +  \delta q \cdot \frac{\partial S_q}{\partial q}
     +  O((\delta q)^2)
   $$

   *The first-order shift $\partial S_q / \partial q$ is the
   **observation cost**: the rate at which the action changes
   per unit of substrate perturbation.*

3. **(Classical energy is unconstrained in sign.)** *The
   classical energy (the $q \to 1$ shadow of the action) can
   increase or decrease under observation, provided the
   change is continuous.  Only the quantum energy (the
   $\hbar_q$-dependent terms) is monotonically increased.*
