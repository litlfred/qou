Let $\mathfrak{S}_q$ be the categorical action. The three variational equations are:

1. **Gravity (vary $\int_A$)**: $\delta\mathfrak{S}_q / \delta\!\int_A = 0$ is postulated to yield the *categorical Einstein equation* (in the Lean formalisation the equation is a field of the class `HasCategoricalEOM`, taken as a hypothesis, not derived by a variation):
   $$
     R_{\int} - \tfrac{1}{2}\mathrm{tr}(R_{\int})\mathrm{id}_A =  T_q[\nabla, \psi],
   $$
   where $T_q$ is the stress-energy endomorphism constructed from the gauge and matter terms.

2. **Gauge (vary $\nabla$)**: $\delta\mathfrak{S}_q / \delta\nabla = 0$ yields the *categorical Yang--Mills equation*:
   $$
     \nabla \star_q F_\nabla + q \cdot [F_\nabla, \star_q F_\nabla] =  J_\psi,
   $$
   where $J_\psi = \psi^* \otimes D_\nabla\psi - D_\nabla\psi^* \otimes \psi$ is the matter current.

3. **Matter (vary $\psi$)**: $\delta\mathfrak{S}_q / \delta\psi = 0$ yields the *categorical transport equation*:
   $$
     D_\nabla\psi =  0.
   $$
