Physical nuclei require integer proton and neutron numbers. Stable hadrons correspond to integer solutions of a quadratic energy minimisation. The continuous optimum $p^*(A)$ defines the beta-stability line.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with substrate parameter $q$. At a fixed mass number $A = Z + N$, the nuclear binding energy is a strictly convex quadratic in the proton number $p$:

$$
  E(p, A) = 
  \underbrace{\left(\frac{a_C}{A^{1/3}} + \frac{a_A}{A}\right)}_{\alpha(A)} p^2
  - \underbrace{a_A}_{\gamma} p
  + \delta(A),
$$

where $a_C = (q - q^{-1}) \lambda_C$ is the Coulomb coefficient, $a_A$ is the Pauli asymmetry coefficient, and $\delta(A)$ collects terms independent of $p$.

The continuous minimum is

$$
  p^*(A) =  \frac{\gamma}{2\alpha(A)} =  \frac{a_A A}{2(a_A + a_C A^{2/3})}.
$$

Because $E$ is strictly convex in $p$, the exact integer minimiser $p_{\mathrm{stab}}(A)$ is one of the two nearest integers to the continuous minimum:

$$
  p_{\mathrm{stab}}(A) = \mathrm{argmin}_{p \in \{0, 1, \ldots, A\}} E(p, A) \in \bigl\{\lfloor p^*(A) \rfloor, \lceil p^*(A) \rceil\bigr\}.
$$

**Archimedean specialisation.** 
The binding energy $E(p)$, its continuous optimum $p^*$, and the convex-minimisation argument are stated over $\mathbb{R}$. The integer-minimiser bound relies on the real ordering.
