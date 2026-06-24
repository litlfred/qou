*Since $K$ is unstable, the ILP
$\{x \in \mathbb{Z}_{\geq 0}^N : \mathrm{G}(q) x \geq 0\}$ has no
solution within the confinement filtration $J^{\ell(K, q)}(q)$.*

*Run the LP relaxation
$\{x \in \mathbb{R}_{\geq 0}^N : \mathrm{G}(q) x \geq 0\}$.  This is
always feasible (the trivial $x = 0$ vector satisfies $G \cdot 0
= 0 \geq 0$, and the relaxation is the convex hull of integer
solutions).  Pick the unique optimal vertex $x^*_{LP} \in
\mathbb{R}_{\geq 0}^N$ closest to an integer point.*

*The **violated constraint** is*

$$
  \gamma^*(K, q)
  \;:=\;
  \arg\min_\gamma\;
    (\mathrm{G}(q)\, \lceil x^*_{LP} \rceil)_\gamma,
$$

*the constraint with the smallest (most negative) Frobenius
positivity value at the rounded integer point.  By LP duality
([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)),
this corresponds to a unique partition $\lambda^*(K, q)$ — the
operator $e_{\lambda^*}$ that fails to satisfy positivity.*

*Uniqueness: if two distinct partitions $\lambda_1, \lambda_2$
both achieve the minimum at the same integer point, they have
identical shadow prices at $q$, i.e., $|y_{\lambda_1}(q)| =
|y_{\lambda_2}(q)|$ — these lie on the **boundary variety**
([local shadow ordering](#def:local-shadow-ordering)) of measure
zero.  Generically (off the boundary variety), $\lambda^*$ is
unique.
$\qquad\blacksquare$
