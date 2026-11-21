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

The step from this trace to the coefficient is not derived here: the
proof asserts that the coefficient is the Hecke-level scale at $k = 5$,

$$
  [5]_q! = [1]_q [2]_q [3]_q [4]_q [5]_q ,
$$

the $q$-factorial at level $5$
([Markov-trace normalization](#prop:wedderburn-trace-identity)). The
identification of the Bethe--Weizsäcker Wigner term with this coefficient is
the content of the conjecture the proposition is conditional on, and the
choice $k = 5$ is an input, not an output of the argument. What the Lean
proves is only the product expansion of $[5]_q! \cdot m_e$.

*At level $k$, the coefficient is $[k]_q! \cdot m_e$.*

The numerical comparison with the fitted liquid-drop Wigner coefficient is a
comparison against a fitted value and is not part of this proof.
