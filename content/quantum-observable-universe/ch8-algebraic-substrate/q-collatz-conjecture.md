**Conjecture ($q$-Collatz).**
Let $q$ be the substrate parameter of a QOU
$(\mathbf{C}, \theta, G, \mathcal{S})$ and let
$H_1(q)$ denote the rank-$1$ Hecke algebra with generator $T$
satisfying the Hecke relation
$(T - q)(T + q^{-1}) = 0$.

The generator $T$ has eigenvalues $q$ (symmetric channel) and
$-q^{-1}$ (antisymmetric channel).  Define the **Hecke
idempotents**:

$$
  e_+ \;=\; \frac{T + q^{-1}}{q + q^{-1}},
  \qquad
  e_- \;=\; \frac{q - T}{q + q^{-1}},
$$

so that $e_+ + e_- = 1$, $e_+^2 = e_+$, $e_-^2 = e_-$,
$e_+ e_- = 0$.  These project onto the symmetric ($e_+$) and
antisymmetric ($e_-$) eigenspaces of $T$ respectively.

**The $q$-Collatz map.**
Define $C_q \colon \mathbb{Z}[q^{\pm 1}] \to \mathbb{Z}[q^{\pm 1}]$
by replacing the discrete even/odd branching of the classical Collatz
map with a Hecke-weighted interpolation:

$$
  C_q(n)
  \;=\;
  e_+(-q^{-n})\,\cdot\,\frac{n}{[2]_q}
  \;+\;
  e_-(-q^{-n})\,\cdot\,\bigl([3]_q\, n + 1\bigr),
$$

where $[k]_q = (q^k - 1)/(q - 1)$ is the $q$-integer and the
idempotent evaluation $e_\pm(-q^{-n})$ means substituting
$T \mapsto -q^{-n}$ (the parity eigenvalue) in the Hecke
projectors:

$$
  e_+(-q^{-n})
  \;=\;
  \frac{-q^{-n} + q^{-1}}{q + q^{-1}}
  \;=\;
  \frac{q^{-1}(1 - q^{1-n})}{q + q^{-1}},
$$

$$
  e_-(-q^{-n})
  \;=\;
  \frac{q + q^{-n}}{q + q^{-1}}.
$$

**Classical limit.**
At $q = 1$:
$[2]_1 = 2$, $[3]_1 = 3$, and $(-q^{-n})\big|_{q=1} = (-1)^n$, so

$$
  e_+\bigl((-1)^n\bigr)
  = \frac{1 + (-1)^n}{2}
  = \begin{cases} 1 & n \text{ even},\\ 0 & n \text{ odd},\end{cases}
$$

$$
  e_-\bigl((-1)^n\bigr)
  = \frac{1 - (-1)^n}{2}
  = \begin{cases} 0 & n \text{ even},\\ 1 & n \text{ odd},\end{cases}
$$

and $C_1(n)$ recovers the classical Collatz map:

$$
  C_1(n)
  = \begin{cases}
      n/2 & n \text{ even},\\
      3n + 1 & n \text{ odd}.
    \end{cases}
$$

**The conjecture.**
For all $q$ in the substrate range $q > 1$ and all positive
$n \in \mathbb{Z}_{>0}$, the $q$-Collatz orbit
$\{C_q^{(k)}(n)\}_{k \geq 0}$ converges: there exists $K$
such that $|C_q^{(K)}(n) - [1]_q| < \varepsilon(q)$
for an explicit threshold $\varepsilon(q) \to 0$ as $q \to 1$.

**Hecke-theoretic interpretation.**
The key insight is that the Hecke relation
$T^2 = (q - q^{-1})T + 1$
([skein generation](#prop:skein-generation)) provides a
canonical interpolation between the two branches: the symmetric
eigenspace ($T = q$, "even" branch) corresponds to a halving
by the $q$-integer $[2]_q$, while the antisymmetric eigenspace
($T = -q^{-1}$, "odd" branch) applies the $q$-deformed $3n+1$
map.  The Skein relation
$T - T^{-1} = q - q^{-1}$ controls the defect between these
channels.

When $q \neq 1$ the map $C_q$ is no longer piecewise-integer:
the Hecke projectors produce a smooth interpolation weighted
by $q$-parity.  The conjecture asserts that the contractive
character of the even branch (division by $[2]_q > 2$ for
$q > 1$) dominates the expansive odd branch, ensuring global
convergence.

**Connection to the local $q$-zeta function.**
The density of integers requiring exactly $k$ steps to reach
the $q$-fixed point is governed by the $q$-zeta function
$\zeta_q(s)$ ([local $q$-zeta](#def:local-q-zeta-function)):
the Dirichlet series encoding the stopping-time distribution
$\sum_{n=1}^{\infty} \sigma_q(n)\, n^{-s}$ converges in the
half-plane $\mathrm{Re}(s) > 1$ and its analytic continuation
encodes the orbit statistics of $C_q$.  If the
[$q$-Riemann hypothesis](#conj:classical-riemann-hypothesis)
holds, the stopping times are equidistributed modulo
$[2]_q$-adic valuation.
