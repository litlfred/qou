Let $q \in \mathbb{C}^{\times}$ not be a root of unity. The Iwahori--Hecke algebra $H_n(\mathbb{C}, q)$ admits a unique $\mathbb{C}$-linear functional $\mathrm{tr}_M$ satisfying:
1. Normalisation: $\mathrm{tr}_M(1) = 1$.
2. Trace property: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$.
3. Markov property, for $x \in H_n(\mathbb{C}, q)$:
$$
  \mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x), \qquad
  z = \frac{q^3}{q^2 + 1} = \frac{q^2}{[2]_q} = \mathrm{tr}_M(\sigma_i)
$$
the Markov-trace loop value, with $z(q_0) \approx 0.61268803714646525160$.
Under the quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$,
the Temperley–Lieb generator is $e_i := q - \sigma_i$, satisfying
$e_i^2 = [2]_q e_i$ with loop parameter $\delta = [2]_q = q + q^{-1}$.
The value $z = q^3/(q^2+1)$ reproduces the Jones–Temperley–Lieb normalisation
$\mathrm{tr}_M(e_i) = q - z = q/(q^2+1) = 1/[2]_q = 1/\delta$;
this parameter is forced rather than stipulated: see
[Primitive Markov-trace axioms](#rem:markov-axioms-primitive).

For each partition $\lambda \vdash n$, the restriction of $\mathrm{tr}_M$ to the irreducible $H_n(\mathbb{C}, q)$-module $S_\lambda$ is the scalar multiple $y_\lambda \chi_\lambda$, with explicit Young-diagram weights given by Vaughan F. R. Jones \cite{jones1987}, Hans Wenzl \cite{wenzl1988}, Rosa C. Orellana \cite{orellana1998}, and Meinolf Geck and Sofia Lambropoulou \cite{geck-lambropoulou-2004}. At $z = q^3/(q^2+1)$ that scalar **vanishes** precisely when $\ell(\lambda) \geq 3$: the fibre $V$ is the two-dimensional fundamental of $\mathrm{SU}_q(2)$ \cite{jimbo1986}, so no partition with three or more rows survives Schur–Weyl, and $\mathrm{tr}_M$ is faithful on the two-row partitions and on nothing else. The vanishing blocks span the radical of the trace form; the quotient is the algebra of Harold Neville Vazeille Temperley and Elliott H. Lieb \cite{temperley-lieb1971}, $H_n(q)/\mathrm{rad} \cong \mathrm{TL}_n(q)$, and the surviving $\sum \dim^2$ is the Catalan number $C_n$ — $2, 5, 14, 42, 132, 429$ for $n = 2, \ldots, 7$. For any braid $\beta$, $\mathrm{tr}_M(\rho_n(\beta))$ computes the Jones polynomial of the closure $\hat{\beta}$ up to framing.
