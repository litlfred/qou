Let $q \in \mathbb{C}^{\times}$ not be a root of unity. The Iwahori--Hecke algebra $H_n(\mathbb{C}, q)$ admits a unique $\mathbb{C}$-linear functional $\mathrm{tr}_M$ satisfying:
1. Normalisation: $\mathrm{tr}_M(1) = 1$.
2. Trace property: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$.
3. Markov property, for $x \in H_n(\mathbb{C}, q)$:
$$
  \mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x), \qquad
  z = \frac{q^3}{q^2 + 1} = \frac{q^2}{[2]_q} = \mathrm{tr}_M(\sigma_i)
$$
the Markov-trace loop value (**convention D**), with $z(q_0) \approx 0.61268803714646525160$.
The alternative normalisation $z = 1/(q^{1/2}+q^{-1/2})$ (**convention C**) is
**not** interchangeable with it: the two traces differ by $195.8$ ppm on
$\beta_{\mathrm{Bor}}$. Convention C is a Temperley–Lieb quantity attached to
the wrong element and at the wrong argument: under the quadratic relation used here,
$\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$, the Temperley–Lieb
generator is $e_i := q - \sigma_i$, with $e_i^2 = [2]_q e_i$, so the loop
parameter is $\delta = [2]_q = q + q^{-1}$ and not $q^{1/2}+q^{-1/2}$.
Convention D lands on the Jones–Temperley–Lieb normalisation exactly,
$\mathrm{tr}_M(e_i) = q - z = q/(q^2+1) = 1/[2]_q = 1/\delta$,
while C assigns a loop reciprocal to the Hecke generator
$\sigma_i$ itself, and at $x = q^{1/2}$ rather than $x = q$ in $1/(x+x^{-1})$;
the two differ by $0.408\,\%$. The
selection is forced rather than stipulated: see
[Primitive Markov-trace axioms (M1–M4 from Jones 1985 / Wenzl 1988)](#rem:markov-axioms-primitive).

For each partition $\lambda \vdash n$, the restriction of $\mathrm{tr}_M$ to the irreducible $H_n(\mathbb{C}, q)$-module $S_\lambda$ is the scalar multiple $y_\lambda \chi_\lambda$. Under convention D that scalar **vanishes** precisely when $\ell(\lambda) \geq 3$: the fibre $V$ is the two-dimensional fundamental of $\mathrm{SU}_q(2)$, so no partition with three or more rows survives Schur–Weyl, and $\mathrm{tr}_M$ is faithful on the two-row stratum and on nothing else. The vanishing blocks span the radical of the trace form; the quotient is the Temperley–Lieb algebra, $H_n(q)/\mathrm{rad} \cong \mathrm{TL}_n(q)$, and the surviving $\sum \dim^2$ is the Catalan number $C_n$ — $2, 5, 14, 42, 132, 429$ for $n = 2, \ldots, 7$. The degeneracy is not a defect convention D introduced; it is what convention D means. For any braid $\beta$, $\mathrm{tr}_M(\rho_n(\beta))$ computes the Jones polynomial of the closure $\hat{\beta}$ up to framing.
