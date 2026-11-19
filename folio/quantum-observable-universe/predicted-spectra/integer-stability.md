Physical nuclei require integer proton and neutron numbers. Stable hadrons correspond to integer solutions of a quadratic energy minimisation. The continuous optimum $p^*(A)$ defines the beta-stability line.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with aether parameter $q$. At a fixed mass number $A = Z + N$, the nuclear binding energy is a strictly convex quadratic in the proton number $p$:

$$
  E(p, A) = 
  \underbrace{\left(\frac{a_C}{A^{1/3}} + \frac{4a_A}{A}\right)}_{\alpha(A)} p^2
  - \underbrace{4a_A}_{\gamma} p
  + \delta(A),
$$

where $a_C = \lambda_C$ is the Coulomb coefficient and $a_A = a_{\mathrm{asym}}$ the Pauli asymmetry coefficient of [beta stability](#prop:beta-stability), the $p$-dependent part is that of $a_C\,p^2/A^{1/3} + a_A (A - 2p)^2/A$, and $\delta(A)$ collects terms independent of $p$.

The continuous minimum is

$$
  p^*(A) =  \frac{\gamma}{2\alpha(A)} =  \frac{A}{2 + \dfrac{a_C}{2a_A} A^{2/3}}.
$$

Because $E$ is strictly convex in $p$, the exact integer minimiser $p_{\mathrm{stab}}(A)$ is one of the two nearest integers to the continuous minimum:

$$
  p_{\mathrm{stab}}(A) = \mathrm{argmin}_{p \in \{0, 1, \ldots, A\}} E(p, A) \in \bigl\{\lfloor p^*(A) \rfloor, \lceil p^*(A) \rceil\bigr\}.
$$
