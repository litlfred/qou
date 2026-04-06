**(0) Genus from Hecke completeness.**

The braiding on $V_1^{\otimes n}$ in $\mathrm{Rep}(\mathrm{SU}_q(2))$
gives $H_n(q)$.  For $n = 2$: $2$ irreps.  For $n = 3$: $3$ irreps.
For $n \geq 4$: the embeddability constraint $(m-1)(s-1) \leq 2g$
with $m \geq 4$, $m < s$, $\gcd(m,s) = 1$ contributes no new
torus knots at genus $g \leq 5$ beyond $T_{3,4}$ (which equals
$T_{4,3}$).  So the relevant Iwahori--Hecke algebra is
$H_2(q) \oplus H_3(q)$, with $5$ irreps total.

At genus $g$, the number of embeddable torus knots with
$r \in \{2, 3\}$ is:

| $g$ | From $r = 2$ | From $r = 3$ | Total | $\geq 5$? |
|:---:|:---:|:---:|:---:|:---:|
| $2$ | $T_{2,3}, T_{2,5}$ | --- | $2$ | No |
| $3$ | $+\, T_{2,7}$ | $T_{3,4}$ | $4$ | No |
| $4$ | $+\, T_{2,9}$ | $+\, T_{3,5}$ | $6$ | **Yes** |

At $g = 3$: $4$ evaluations cannot span a $5$-dimensional
space (rank $\leq 4$).  At $g = 4$: $6$ evaluations span
$5$ irreps (verified numerically: the $6 \times 5$ matrix
has rank $5$ for all $q > 1$, $q \neq$ root of unity).
Therefore $g_{\min} = 4$.

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

At genus $g = 4$ (from part (0)), the Seifert embedding
$\iota \colon F_p \hookrightarrow \Sigma_4$ induces
$\iota_* \colon H_1(F_p) \to H_1(\Sigma_4)$.  The
Seifert surface $F_p$ has $\mathrm{rank}\, H_1(F_p) = (p-1)/2$.
For $\iota_*$ to be injective (necessary for a Seifert embedding),
$(p-1)/2 \leq 4$.

In Hecke coordinates: each degree $u^k$ in $a_p$ corresponds
to the $k$-th Seifert cycle $\gamma_k \in H_1(F_p)$.  The
truncation $\pi_4 \colon \mathbb{Z}[u] \to \mathbb{Z}[u]/(u^5)$
projects onto the cycles that fit in $H_1(\Sigma_4)$.  The kernel
$\mathfrak{I}_4 = (u^5)$ consists of the terms with no target.

**(iii) Yekutieli = leading coefficient.**

The brane tower $A_n \hookrightarrow A_{n+1}$
([quantum characteristic classes](#def:quantum-characteristic-classes))
provides a central extension of gerbes at each level.  For a
torus knot $T_{2,p}$, the Seifert cycles index the tower levels.

The obstruction $\kappa(T_{2,p}) \in H^2(\mathcal{S}, \mathcal{B})$
at level $n = g + 1 = 5$ is nonzero if and only if the $5$th
Seifert cycle has no lift.  Via the $d_q^2$ formula:

$$
  d_q^2(\gamma_5^*\, \omega_T)
  \;=\;
  q^{-1}(1 - q^{-1}) \cdot 5 \cdot \omega_V \wedge_q \omega_T
$$

which is nonzero for $q \neq 1$.  The integer coefficient $5$
is the weight of $\gamma_5$ under the $T$-action, and the factor
$q^{-1}(1 - q^{-1})$ is the universal $d_q^2$ obstruction
coefficient ([categorical $d_q^2$](#prop:categorical-dq-squared)).

This identifies $\kappa(T_{2,p})$ with the leading Chebyshev
coefficient $c_{(p-1)/2} = 1$ (nonzero), completing the proof
that both characterisations agree.  $\square$
