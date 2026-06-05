**Proposition (jet decomposition of the Archimedean functor).**

Let $\tau$ be the Archimedean realisation functor (step 9 of the canonical
chain). Applied to the surface-ordered multiplicative integral of the
mass-identity connection--curvature pair over the exceptional divisor
$\mathcal{S}_c$, it decomposes as the sum over vertical (jet) degrees of the
prolonged Seiberg--Witten periods:

$$
\tau\!\left(\mathrm{MI}\!\!\int_{\mathcal{S}_c}\bigl(\nabla_A q,\,L\wedge F^+\bigr)\right)
\;=\;
\sum_{n\geq 0} a_D^{(n)}
\;=\;
\sum_{n\geq 0}\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)} .
$$

The $n=0$ term is the electron period $a_D^{(e)}$; each higher term is the
$n$-th prolonged period of [`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation),
which by [`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum) is an
algebraic residue sum. Hence the Seiberg--Witten differential **is the
jet-graded decomposition of the Archimedean functor**: $\tau$ observes the whole
prolongation tower at once, and the vertical (jet/body) order $n$ indexes its
graded pieces. This is the structural counterpart, on the realisation side, of
the "observe last" principle — the jet tower is carried intact through the
filtration and $\tau$ collapses it to the graded sum only at observation.
