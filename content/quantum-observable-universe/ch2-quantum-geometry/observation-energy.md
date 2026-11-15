**Proposition.**
*Let $O \colon A \to A$ be an observation
([observation](#def:observation)) with
substrate perturbation $\delta q$.  Then:*

1. **(Quantum energy increases.)** *The quantum Planck constant
   $\hbar_q = 1 - q^{-1}$
   ([quantum Planck constant](#def:quantum-planck-constant))
   satisfies*

   $$
     \hbar_{q + \delta q} - \hbar_q
     \;=\; \frac{\delta q}{q(q + \delta q)}
     \;>\; 0
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
     \;=\;
     S_q \;+\; \delta q \cdot \frac{\partial S_q}{\partial q}
     \;+\; \mathcal{O}((\delta q)^2)
   $$

   *The first-order shift $\partial S_q / \partial q$ is the
   **observation cost**: the rate at which the action changes
   per unit of substrate perturbation.*

3. **(Classical energy is unconstrained in sign.)** *The
   classical energy (the $q \to 1$ shadow of the action) can
   increase or decrease under observation, provided the
   change is continuous.  Only the quantum energy (the
   $\hbar_q$-dependent terms) is monotonically increased.*

*Proof.*
(1) $\hbar_q = 1 - q^{-1}$ is strictly increasing in $q$
for $q > 0$.  Its derivative $d\hbar_q/dq = q^{-2} > 0$.
Hence $\delta q > 0$ implies $\delta\hbar_q > 0$.

(2) Direct Taylor expansion of $S_{q'}$ about $q$.

(3) The classical action $S_1 = \lim_{q \to 1} S_q$ depends
on $\nabla, \lambda, \psi$ but not on $q$.  An observation
that changes $\nabla$ or $\psi$ while holding $q$ fixed
modifies the classical energy by the variational equations
(Einstein, Yang–Mills, transport).  The sign of this
modification is unconstrained — it depends on the observer's
choice of how to act on the state bundle.  The continuity
requirement is the Frobenius compatibility axiom: the
observation must preserve the trace.  $\square$
