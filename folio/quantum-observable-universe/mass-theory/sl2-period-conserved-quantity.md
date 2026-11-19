The one-parameter recurrence
([sl2-prolongation-recurrence proposition](#prop:sl2-prolongation-recurrence))

$$
a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)},
\qquad \tau = \mathrm{tr}\, B,\ \det B = 1,
$$

on the prolonged Seiberg--Witten periods admits a **conserved first integral** —
the discrete energy of the Lucas/Chebyshev orbit, equivalently the cup-product
symplectic form evaluated on consecutive periods:

$$
\boxed{\;
H_n := \bigl(a_D^{(n+1)}\bigr)^2 - \tau\,a_D^{(n+1)}a_D^{(n)} + \bigl(a_D^{(n)}\bigr)^2
\quad\text{satisfies}\quad H_{n+1} = H_n
\;}
$$

so $H_n = H_0$ for every $n$. The invariant exists because $\det B = 1$: it is the
quadratic form fixed by $B \in \mathrm{SL}_2$ acting on $(a_D^{(n)}, a_D^{(n+1)})$.

**Fork consequence (the depth-$2$ hypothesis is the $n\le 4$ germ).** A genuine
depth-$2$, $\det = 1$ orbit keeps $H_n$ constant; in the hyperbolic case
$\tau = 2\cosh\theta > 2$ the conic $H_n = H_0$ forces the ratio
$a_D^{(n+1)}/a_D^{(n)}$ to a **fixed** limit $\lambda_+ = e^{\theta}$ (geometric
growth). But the true prolonged period is the residue sum
([sw-period-residue-sum proposition](#prop:sw-period-residue-sum))
$a_D^{(n)} = \sum_{\lambda} \dim_q$, a per-block Wedderburn quantum-dimension sum
that grows **factorially** (super-exponentially), so its ratio
$a_D^{(n+1)}/a_D^{(n)}$ is unbounded and $H_n \to \infty$. A factorial sequence
conserves no first integral, hence satisfies **no** depth-$2$ recurrence: the
$\tau$ fitted from three residue weights
$\tau = (a_D^{(2)} + a_D^{(4)})/a_D^{(3)}$ is an effective germ matching $n\le 4$,
not the period recurrence. The exact prolongation kernel is the q-Bessel-class
$q$-difference operator of the super-exponential residue sum
([binding-genfun-qdifference proposition](#prop:binding-genfun-qdifference)), not a
$2\times 2$ Cayley--Hamilton relation.
