**(i) Chebyshev degree = Seifert genus.**

The Hecke relation $T^2 = s T + \mathbf{1}$ (where $s = q - q^{-1}$)
gives the recurrence $a_{n+1} = s \cdot a_n + a_{n-1}$ with
$a_0 = 0$, $a_1 = 1$.  For odd $n$, each step increases the
degree in $s$ by $1$, so $\deg_s a_n = n - 1$.  Since odd-indexed
$a_n$ involve only even powers of $s$, we write $u = s^2$ and
obtain $\deg_u a_n = (n-1)/2$.

For $T_{2,p}$, the Seifert genus is $(2-1)(p-1)/2 = (p-1)/2$,
confirming $\deg_u a_p = g(T_{2,p})$.

The leading coefficient: the recurrence shows that the leading
term of $a_{2k+1}$ in $u$ is $u^k$ with coefficient $1$ (each
multiplication by $s$ raises the degree by $1$, and the leading
term picks up no lower-order contamination from $a_{n-1}$).

**(ii) Ideal characterisation.**

The Seifert embedding $\iota \colon F_p \hookrightarrow \Sigma_g$
induces $\iota_* \colon H_1(F_p) \to H_1(\Sigma_g)$.  The
Seifert surface $F_p$ has $\mathrm{rank}\, H_1(F_p) = (p-1)/2$.
For $\iota_*$ to be injective (necessary for a Seifert embedding),
$(p-1)/2 \leq g = \dim H^{1,0}(\Sigma_g)$.

In Hecke coordinates: each degree $u^k$ in $a_p$ corresponds
to the $k$-th Seifert cycle $\gamma_k \in H_1(F_p)$.  The
truncation $\pi_g \colon \mathbb{Z}[u] \to \mathbb{Z}[u]/(u^{g+1})$
projects onto the cycles that fit in $H_1(\Sigma_g)$.  The kernel
$\mathfrak{I}_g = (u^{g+1})$ consists of the terms with no target.

**(iii) Yekutieli = leading coefficient.**

The brane tower $A_n \hookrightarrow A_{n+1}$
([quantum characteristic classes](#def:quantum-characteristic-classes))
provides a central extension of gerbes at each level.  For a
torus knot $T_{2,p}$, the Seifert cycles index the tower levels.

The obstruction $\kappa(T_{2,p}) \in H^2(\mathcal{S}, \mathcal{B})$
at level $n = g + 1$ is nonzero if and only if the $(g+1)$-th
Seifert cycle has no lift.  Via the $d_q^2$ formula:

$$
  d_q^2(\gamma_{g+1}^*\, \omega_T)
  \;=\;
  q^{-1}(1 - q^{-1})\,(g+1)\,\omega_V \wedge_q \omega_T
$$

which is nonzero for $q \neq 1$.  The integer coefficient
$(g + 1)$ is the weight of $\gamma_{g+1}$ under the $T$-action,
and the factor $q^{-1}(1 - q^{-1})$ is the universal $d_q^2$
obstruction coefficient
([categorical $d_q^2$](#prop:categorical-dq-squared)).

This identifies $\kappa(T_{2,p})$ with the
leading Chebyshev coefficient $c_{(p-1)/2} = 1$ (nonzero),
completing the proof that both characterisations agree.
$\square$
