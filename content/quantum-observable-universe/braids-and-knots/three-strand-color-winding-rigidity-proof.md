*Proof.* Write $M = \rho_{(2,1)}(\sigma_1)\,\rho_{(2,1)}(\sigma_2)$ with
$\rho_{(2,1)}(\sigma_1) = \mathrm{diag}(q, -q^{-1})$ and the axial-distance-$2$
Hoefsmit block for $\sigma_2$, so that

$$
M = \begin{pmatrix} q\,a_{-2} & q\,\beta \\ -q^{-1}\beta & -q^{-1} a_{2} \end{pmatrix},
\qquad
a_{\pm 2} = \frac{q - q^{-1}}{1 - q^{\mp 4}},
\qquad
\beta^2 = a_2 a_{-2} + 1 .
$$

Two scalar computations. **Trace:** using $q\,a_{-2} = (q^2-1)/(1-q^4)$ and
$q^{-1} a_2 = q^2(q^2-1)/(q^4-1)$,

$$
\mathrm{tr}\, M
= \frac{(q^2-1)(1+q^2)}{1-q^4}
= \frac{q^4-1}{1-q^4} = -1,
$$

a rational identity in $q$ alone (denominators nonzero since $q^4 \neq 1$).
**Determinant:** $\det M = (q\,a_{-2})(-q^{-1}a_2) - (q\beta)(-q^{-1}\beta)
= \beta^2 - a_2 a_{-2} = 1$, which is exactly the Hoefsmit constraint on
$\beta$.

By Cayley–Hamilton for a $2\times 2$ matrix,
$M^2 - (\mathrm{tr}\,M)\,M + (\det M)\,\mathrm{Id} = 0$, so
$M^2 = -M - \mathrm{Id}$ (the $\zeta_3$ quadratic), and multiplying by $M$:

$$
M^3 = -M^2 - M = (M + \mathrm{Id}) - M = \mathrm{Id}. \qquad \blacksquare
$$

Neither the trace nor the determinant identity involves $q$ beyond the
nonvanishing conditions, so the conclusion holds for every $q$ with
$q^4 \neq 1$: the eigenvalues of $M$ are the primitive cube roots of unity
at every $q$ — the color winding is rigid.
