The integrand $\ln_q(1+t)/t$ in the quantum dilogarithm formula above has the same formal
structure as the *information-flow density* that appears in the computation of
filled Julia sets via the Bottcher escape potential.

For the quadratic family $f_c(z)=z^2+c$, the external Green's function (escape potential)
admits the convergent series

```tex
\begin{equation}\label{eq:bottcher-series}
  G_c(z)
  \;=\;
  \sum_{k=0}^{\infty}
    \frac{1}{2^{k+1}}\,
    \ln\!\left(1+\frac{c}{f_c^k(z)^2}\right).
\end{equation}
```

Writing $t_k = c/f_c^k(z)^2$, each summand is $\frac{1}{2^{k+1}}\ln(1+t_k)$: the
function $\ln(1+t_k)/t_k$ (evaluated at $t_k$) is exactly the classical ($q=1$) limit
of the quantum dilogarithm integrand.  The sum over $k$ weighted by $2^{-(k+1)}$
accumulates the *information flow* along the orbit of $f_c$, with the weight
$2^{-k}$ reflecting the degree-$2$ expansion at each step.

In the QOU framework the role of the dynamical parameter $c$ is played by the
substrate parameter $q=q(z)$ ([substrate parameter](#def:substrate-parameter)), which varies
continuously with the spacetime coordinate $z$.  The $q$-deformed Reeb flow
([$q$-Reeb flow](#def:q-reeb-flow)) on the exceptional divisor $E_i \cong \mathbb{P}^1(\mathbb{C})$
takes the place of the orbit $\{f_c^k(z)\}_{k\geq 0}$, and the path from $0$ to $z_i$
in the quantum dilogarithm integral accumulates information along that flow exactly as
[eq:bottcher-series](#eq:bottcher-series) accumulates it along the Julia-set orbit.  The
$q$-deformation of the logarithm encodes the departure from classical ($q=1$)
dynamics: as $q\to 1$ the flow trivialises and $\Phi_q(z_i)\to\mathrm{Li}_2(z_i)$,
the classical dilogarithm; as $q\to\infty$ the quantum-number denominators $[n]_q$
suppress high-order terms, concentrating the topological charge near the blow-up centre.

In this identification the *Julia set boundary* of the classical problem---the
locus where $G_c$ transitions from zero to positive---is the analogue of the boundary
of the exceptional divisor $\partial E_i$, where the $q$-deformed torsion charge changes
regime ([Reeb exceptional divisor](#rem:reeb-exceptional-divisor)).  The substrate parameter $q(z)$
thereby acts as a *spacetime-dependent dynamical parameter*, continuously
deforming the Julia set geometry as one moves through the QOU.
