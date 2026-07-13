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
  p_{\mathrm{stab}}(A) = \mathrm*{argmin}_{p \in \{0, 1, \ldots, A\}} E(p, A) \in \bigl\{\lfloor p^*(A) \rfloor, \lceil p^*(A) \rceil\bigr\}.
$$

**Even-odd selection.**
The pairing energy $± \lambda_P / A^{1/2}$ breaks the $p \leftrightarrow p + 1$ symmetry at the rounding boundary. The system selects the pair $(p, A - p)$ where both are even. This yields the observed even-even dominance: of the 254 stable nuclides, 166 have even $p$ and even $n$.

**Regime transitions.**
The minimiser $p_{\mathrm{stab}}(A)$ increases by $1$ when $p^*(A)$ crosses a half-integer. To leading order, the critical mass numbers for this transition are

$$
  A_k = \left( \frac{a_C (2k + 1)}{2a_A} \right)^{3/2}.
$$

These are the **beta-decay thresholds**. At $A = A_k$, the nuclei $(k, A_k - k)$ and $(k + 1, A_k - k - 1)$ have equal binding energy. Beta decay is energetically neutral.

**Archimedean specialisation.** 
The binding energy $E(p)$, its continuous optimum $p^*$, and the convex-minimisation argument are stated over $\mathbb{R}$. The integer-minimiser bound relies on the real ordering.
