The beta-stability line
([beta-stability](#prop:beta-stability)) gives a continuous
optimum $p^*(A)$.  Physical nuclei require integer proton and
neutron numbers.  The stable hadrons are integer solutions to a
quadratic energy minimisation.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with
the substrate $q$.  At fixed mass number $A = Z + N$, the nuclear
binding energy is a **convex quadratic** in the proton number
$p$:

$$
  E(p, A)
  = 
  \underbrace{\left(\frac{a_C}{A^{1/3}} + \frac{a_A}{A}\right)}_{\alpha(A)}
  p^2
  - 
  \underbrace{a_A}_{\gamma}
  p
  +  \delta(A)
$$

where $a_C = (q - q^{-1}) \cdot \lambda_C$ is the Coulomb
coefficient, $a_A$ is the Pauli asymmetry coefficient, and
$\delta(A)$ collects terms independent of $p$.

The continuous minimum is

$$
  p^*(A) =  \frac{\gamma}{2\alpha(A)}
  =  \frac{a_A \cdot A}{2(a_A + a_C \cdot A^{2/3})}.
$$

Since $E$ is strictly convex in $p$, the integer minimiser is
**exact**:

$$
  p_{\mathrm{stab}}(A)
  = 
  \mathrm*{argmin}_{p \in \{0, 1, \ldots, A\}} E(p, A)
   \in 
  \bigl\{\lfloor p^*(A) \rfloor,
  \lceil p^*(A) \rceil\bigr\}.
$$

There is no approximation error — the integer minimiser of a
convex quadratic is always one of the two nearest integers to the
continuous minimum.

**Even-odd selection.**
The pairing energy $\pm \lambda_P / A^{1/2}$ breaks the
$p \leftrightarrow p + 1$ symmetry at the rounding boundary.
Among the two integer candidates, the pair $(p, A - p)$ with
both $p$ and $A - p$ even is preferred.  This produces the
observed even-even dominance: of the 254 stable nuclides, 166
have even $p$ and even $n$.

**Regime transitions.**
The integer minimiser $p_{\mathrm{stab}}(A)$ jumps by $+1$
when $p^*(A)$ crosses a half-integer.  The critical mass numbers
where the stable proton count increases from $k$ to $k + 1$ are

$$
  A_k
  = 
  \left(
    \frac{a_C \cdot (2k + 1)}{2a_A}
  \right)^{3/2}
  \quad\text{(to leading order).}
$$

These are the **beta-decay thresholds**: at $A = A_k$, the nuclei
$(k, A_k - k)$ and $(k + 1, A_k - k - 1)$ have equal binding
energy, and beta decay is energetically neutral.
