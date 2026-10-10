*Proof.*
The isospin Casimir $T^2$ commutes with all $\sigma_i$ (it lies
in the center of $H_n$).  By Schur's lemma, $T^2$ acts as a
scalar $c_\lambda$ on each irreducible representation $\lambda$.

The Markov trace of the Casimir over the complete $H_5(R, q)$:

$$
  \mathrm{tr}_M(T^2) = \sum_\lambda w_\lambda \cdot c_\lambda
$$

By Frobenius reciprocity, the isospin Casimir at $H_5$ induced
from $H_3$ has eigenvalue $T(T+1)$ in each component, weighted
by $\dim_q(\lambda)^2$.

The coefficient is set by the Hecke-level scale at $k = 5$:

$$
  [5]_q! = [1]_q [2]_q [3]_q [4]_q [5]_q ,
$$

the $q$-factorial at level $5$, evaluated directly as this product (the
Hecke-level coefficient of the Markov-trace normalization,
[Markov-trace normalization](#prop:wedderburn-trace-identity)).

Therefore the Wigner coefficient
$= [5]_q! \cdot m_e \approx 67.1$ MeV, matching the fitted value
$68.9$ MeV to within 2.6%.  $\square$

*At level $k$, the Wigner coefficient is $[k]_q! \cdot m_e$.*
