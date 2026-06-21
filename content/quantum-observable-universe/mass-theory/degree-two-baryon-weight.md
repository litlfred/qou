*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*The coefficient of $\Phi_2$ in the Wedderburn mass formula is*

$$
  \beta_2 = -2[3]_q
          = -2 \cdot \frac{q^3 - q^{-3}}{q - q^{-1}}
          \approx -6.087
$$

*where $[3]_q$ is the quantum 3-integer.*

*Proof sketch.*
The baryon has three color channels, corresponding to the three
roots of the color-tube cubic.  The degree-2 symmetric function
$\sigma_2 = \sum_{i<j} c_i c_j$ counts pairwise color products.
The number of pairs is $\binom{3}{2} = 3$, which $q$-deforms to
$[3]_q = (q^3 - q^{-3})/(q - q^{-1})$ at finite $q$.

The factor $-2$ arises from two sources:

1. The sign is negative because $\Phi_2 = \sum \ln|\det M_i|$
   contributes with opposite sign to the binding energy (the
   determinant of the crossing matrix is $-1$ for all crossing
   types, making $\Phi_2$ accumulate sign information).

2. The factor $2$ is the pn crossing doubling convention: each
   $\mathfrak{p}\mathfrak{n}$ crossing uses $c = 2$ (doubled to
   keep coefficients integral), and the $\beta_2$ weight
   compensates this doubling in the alternating channel.

At $q = q_0$: $[3]_q \approx 3.044$, giving
$\beta_2 \approx -6.087$.  The degree-2 binding scale is
$|\beta_2| \cdot \alpha \approx 6.09 \times 3.74 \approx 22.8$
MeV, consistent with the strong-force binding energy scale.
$\square$
