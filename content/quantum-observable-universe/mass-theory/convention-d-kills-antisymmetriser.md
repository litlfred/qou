*Let*

$$
  \mathrm{tr}_M \;=\; y_{(3)}\,\chi^{(3)} \;+\; y_{(2,1)}\,\chi^{(2,1)} \;+\; y_{(1^3)}\,\chi^{(1^3)}
$$

*be the Wedderburn expansion of a Markov trace on $H_3(q)$, normalised by
$\mathrm{tr}_M(1) = 1$, $\mathrm{tr}_M(\sigma) = z$ and
$\mathrm{tr}_M(\sigma_0\sigma_1) = z^2$. Then for every $q > 0$*

$$
  \boxed{\;\;
  y_{(1^3)} \;=\; 0
  \quad\Longleftrightarrow\quad
  z \;=\; q
  \;\;\text{ or }\;\;
  z \;=\; \frac{q^{3}}{q^{2}+1},
  \;\;}
$$

*and the first root forces $y_{(3)} = 1$, $y_{(2,1)} = y_{(1^3)} = 0$. Convention D is
therefore the unique non-trivial Markov trace on $H_3(q)$ whose radical contains the
three-strand antisymmetriser.*

## Three normalisations, three unknowns

A Markov trace on $H_3(q)$ is determined by its values on three conjugacy classes, and
the Wedderburn expansion turns those values into a linear system in the weights. With
$r$ a formal inverse for $q$ and the Hoefsmit character values
$\chi(1) = (1,2,1)$, $\chi(\sigma) = (q,\; q-r,\; -r)$,
$\chi(\sigma_0\sigma_1) = (q^{2},\, -1,\, r^{2})$, the three normalisations read

```tex
\[
\begin{aligned}
  y_{(3)} + 2y_{(2,1)} + y_{(1^3)} &= 1, \\
  q\,y_{(3)} + (q-r)\,y_{(2,1)} - r\,y_{(1^3)} &= z, \\
  q^{2}y_{(3)} - y_{(2,1)} + r^{2}y_{(1^3)} &= z^{2}.
\end{aligned}
\]
```

Eliminating $y_{(3)}$ and $y_{(2,1)}$ and clearing inverses with $qr = 1$ leaves the
antisymmetric weight in factored form,

$$
  y_{(1^3)}\,(q^{2}+1)(q^{4}+q^{2}+1)
  \;=\;
  q^{2}\,(z - q)\,\bigl(z(q^{2}+1) - q^{3}\bigr).
$$

The scale factor on the left is a sum of even powers and is strictly positive, so it
cancels: the antisymmetriser dies at exactly the two roots of the right-hand side, and
nowhere else.

## The trivial branch is not a competitor

At $z = q$ the whole trace collapses. Substituting the root back into the linear system
gives $y_{(2,1)} = 0$ alongside $y_{(1^3)} = 0$, hence $y_{(3)} = 1$: the trace is the
one-dimensional character. Such a trace carries no mixed-symmetry block, so the two
isospin weights degenerate to $1$ and $0$ and no nucleon-pair structure survives. It is
a Markov trace only in the empty sense, which is what "non-trivial" excludes in the
statement above.

The second root is convention D, $z\,(q^{2}+1) = q^{3}$. Reading the closed forms off
the same system recovers, now derived rather than tabulated,

$$
  y_{(2,1)} \;=\; \frac{q^{2}}{(q^{2}+1)^{2}} \;=\; \frac{1}{[2]_q^{2}},
  \qquad
  y_{(3)} \;=\; \frac{q^{4}+1}{(q^{2}+1)^{2}} \;=\; \frac{[4]_q}{[2]_q^{3}},
$$

the $n = 3$ instance of the two-row closed form
$y_{(n-k,k)} = [n-2k+1]_q/[2]_q^{\,n}$.

## What the characterisation replaces

The selection criterion for the Markov trace is not non-degeneracy. Convention D
violates non-degeneracy by construction --- the pairing has a radical, and the radical
is exactly the block killed above --- so a non-degeneracy criterion could never have
selected it. What this proposition supplies in its place is a *derivation*: impose the
row cap $y_\lambda = 0$ for $\ell(\lambda) \ge 3$, and $z$ is forced. Convention C is
then excluded by the same computation rather than by fiat, since
$z = 1/(q^{1/2}+q^{-1/2})$ is neither root; that is precisely why the antisymmetric
weight is nonzero there.

The pinning first becomes available at three strands. On $H_2(q)$ there is no
three-row partition whose weight can be asked to vanish, the algebra is commutative
with a single generator, and every $z$ is admissible. The row cap is vacuous at
$n \le 2$ and bites at $n = 3$.

**Archimedean specialisation.** What follows sits on the archimedean side of the
substrate wall: it invokes real- or complex-analytic constructs --- real-valued
physical observables, real-analytic bounds, transcendental constants, or numerical
evaluation at the substrate parameter $q_0$. Any generic categorical or
$q$-deformation identities it draws on remain valid over an abstract coefficient ring;
only their archimedean realisation is specialised here. At
$q_0 = 1.10997858275138080759$ the two conventions give
$z_{\mathrm{D}} = 0.61268803714646525160$ with weights
$(0.5054042,\, 0.2472979,\, 0)$, against
$z_{\mathrm{C}} = 0.49932033418369445241$ with
$(0.4153958,\, 0.2809296,\, 0.0227449)$.
