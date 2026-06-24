The braid $K$ lives in $H_3(R, q)$ (generators $T_1, T_2$).  The
representation $\rho_\lambda$ of $H_k(R, q)$ restricts to $H_3(R, q)$
via the standard inclusion $H_3(R, q) \hookrightarrow H_k(R, q)$
(using the first two generators).  The branching rule gives:

$$
  \rho_\lambda \!\downarrow_{H_3}
  = \bigoplus_{\mu\,\vdash\,3} f^{\lambda/\mu} \cdot \rho_\mu
$$

Taking characters and using additivity yields the formula.

**Base characters (symbolic proofs).**

*Figure-eight.*
$4_1 = T_1 T_2^{-1} T_1^{-1} T_2$ is the commutator $[T_1, T_2^{-1}]$.
In the symmetric and alternating channels ($\dim = 1$), the eigenvalue
products are $q \cdot q^{-1} \cdot q^{-1} \cdot q = 1$ and
$(-q^{-1})(-q)(-q)(-q^{-1}) = 1$ respectively.

In the standard channel $[2{,}1]$ ($\dim = 2$), the Hoefsmit matrices
give $T_1 = \mathrm{diag}(q, -q^{-1})$ and $T_2$ with entries
$\alpha = -1/(q^3{+}q)$, $\gamma = q^3/(q^2{+}1)$.  Direct computation:

$$
  \mathrm{tr}(T_1 T_2^{-1} T_1^{-1} T_2)
  = \alpha^2 - h\alpha + \gamma^2 - h\gamma
    - (q^2 + q^{-2})(\alpha\gamma + 1)
$$

Using $\alpha + \gamma = h$ and $\alpha\gamma = -1/([3]+1)$ (both
verified symbolically), this simplifies to:

$$
  = -\alpha\gamma(1 + [3]) - ([3] - 1)
  = \frac{1+[3]}{[3]+1} - [3] + 1
  = 2 - [3]_q
  \qquad
$\qquad\blacksquare$
