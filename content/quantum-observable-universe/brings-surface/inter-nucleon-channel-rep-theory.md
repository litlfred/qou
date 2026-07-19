The chirality sign $\epsilon(c_1, c_2, F_1, F_2) \in \{+1, -1, 0\}$ is constrained by the $\mathrm{SO}(3) = \mathrm{SU}(2)/\mathbb{Z}_2$ level structure. The $\mathbb{Z}_2$ kernel of the covering map $\mathrm{SU}(2) \to \mathrm{SO}(3)$ acts as $-1$ on half-integer-spin (spinorial) irreps and $+1$ on integer-spin (tensor) irreps. The chirality dichotomy \{+1, -1\} from the $S_5/\mathrm{SO}(3)$ fiber action supplies this **grading by this $\mathbb{Z}_2$**. The neutral value $0$ (the bar-symmetric $\mathrm{pn}$ average) identifies the $\mathbb{Z}_2$-fixed locus.

With $q = e^{\eta}$, the $\mathrm{SU}(2)_q$ doublet character is $[2]_q = 2\cosh\eta$ and the lowest $\mathrm{SO}(3)_q$ (integer-spin) character is the adjoint $[3]_q$. They satisfy the Chebyshev/Clebsch–Gordan square identity

$$
  [3]_q \;=\; [2]_q^{\,2} - 1,
$$

formalised as `so3_adjoint_eq_chebyshev` in [`MassVolDensity.lean`](../lean/QOU/Mass/MassVolDensity.lean) §6. The $\mathrm{SO}(3)$ characters are exactly the polynomials in $[2]_q$ invariant under the $\mathbb{Z}_2$ quotient. Any admissible $\epsilon$ rule must be a section of this same $\mathbb{Z}_2$-grading. A valid $\epsilon$ cannot assign $-1$ to a color-sheet pair whose combined flavor content sits in the integer-spin (tensor) sector. The explicit map from color-sheet pairs $(c_1, c_2)$ to the $\mathbb{Z}_2$-grade still requires the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action of `conj:s5-so3-fiber-action`.

## Cross-references

- $\mathrm{SO}(3)_q = \mathrm{SU}(2)_q/\mathbb{Z}_2$ level structure: [`MassVolDensity.lean`](../lean/QOU/Mass/MassVolDensity.lean) §6 (`so3_adjoint_eq_chebyshev`)
