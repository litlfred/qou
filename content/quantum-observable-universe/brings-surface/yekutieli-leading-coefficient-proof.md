**Proof.**
The brane tower $A_n \hookrightarrow A_{n+1}$
([quantum characteristic classes](#def:quantum-characteristic-classes))
provides a central extension of gerbes at each level.  For a
torus knot $T_{2,p}$, the Seifert cycles index the tower levels.

The obstruction $\kappa(T_{2,p}) \in H^2(\mathcal{S}, \mathcal{B})$
at level $n = g + 1 = 5$ is nonzero if and only if the $5$th
Seifert cycle has no lift.  Via the $d_q^2$ formula:

$$
  d_q^2(\gamma_5^* \omega_T)
  = 
  q^{-1}(1 - q^{-1}) \cdot 5 \cdot \omega_V \wedge_q \omega_T
$$

which is nonzero for $q \neq 1$.  The integer coefficient $5$
is the weight of $\gamma_5$ under the $T$-action, and the factor
$q^{-1}(1 - q^{-1})$ is the universal $d_q^2$ obstruction
coefficient ([categorical $d_q^2$](#prop:categorical-dq-squared)).

This identifies $\kappa(T_{2,p})$ with the leading Chebyshev
coefficient $c_{(p-1)/2} = 1$ (nonzero), completing the proof
that both characterisations agree.  $\square$
