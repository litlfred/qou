The baryon has three color channels, the three roots of the color-tube
cubic. The degree-2 symmetric function $\sigma_2 = \sum_{i<j} c_i c_j$
counts pairwise color products; there are $\binom{3}{2} = 3$ pairs, which
$q$-deforms at finite $q$ to the quantum 3-integer
$[3]_q = (q^3 - q^{-3})/(q - q^{-1})$.

The prefactor $-2$ has two sources:

1. **Sign.** $\Phi_2 = \sum \ln|\det M_i|$ contributes to the binding
   energy with the opposite sign; the crossing matrix has $\det M_i = -1$
   for every crossing type, so $\Phi_2$ accumulates the sign information,
   making the weight negative.
2. **Magnitude $2$.** This is the p–n crossing doubling convention: each
   $\mathfrak{p}\mathfrak{n}$ crossing carries $c = 2$ (doubled to keep
   coefficients integral), and the $\beta_2$ weight compensates the
   doubling in the alternating channel.

Hence $\beta_2 = -2[3]_q$. Evaluating at the substrate $q_0 \approx 1.110$
gives $[3]_q \approx 3.044$ and $\beta_2 \approx -6.087$; both numerical
evaluations are the Lean witnesses `QOU.BaryonWeight.qInt3_approx` and
`QOU.BaryonWeight.beta2_approx` (`norm_num`). The degree-2 binding scale
$|\beta_2|\cdot\alpha \approx 6.09 \times 3.74 \approx 22.8$ MeV is
consistent with the strong-force binding scale. $\qquad\blacksquare$
