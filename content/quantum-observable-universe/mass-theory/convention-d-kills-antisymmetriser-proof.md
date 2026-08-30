## Elimination

The three normalisations are linear in the weights, so the antisymmetric weight is
obtained by a single cofactor combination. Multiplying the identity normalisation by
$(q^{3} - q^{2}r + q)$, the generator normalisation by $-(2q^{2}+1)$, and the
two-crossing normalisation by $(q+r)$, and adding, eliminates $y_{(3)}$ and
$y_{(2,1)}$ simultaneously:

$$
  y_{(1^3)}\,\bigl((q^{2}+1+r^{2})(q+r)\bigr)
  \;=\;
  (z^{2}-q^{2})(q+r) \;+\; (2q^{2}+1)(q-z).
$$

No relation between $q$ and $r$ is used, so the identity holds in the polynomial ring
before any inverse structure is imposed --- which is what makes it safe to reuse over
a coefficient ring where $q$ is not invertible.

## Factorisation

Scaling by $q^{3}$ and substituting $qr = 1$ clears every inverse and exhibits the two
roots:

$$
  y_{(1^3)}\,(q^{2}+1)(q^{4}+q^{2}+1)
  \;=\;
  q^{2}\,(z-q)\,\bigl(z(q^{2}+1)-q^{3}\bigr).
$$

Both factors of the scale are sums of even powers with positive coefficients, so the
product is strictly positive for every $q$ in an ordered field and may be cancelled.
Setting $y_{(1^3)} = 0$ therefore forces $q^{2}(z-q)(z(q^{2}+1)-q^{3}) = 0$, and
$q > 0$ removes the factor $q^{2}$. The two remaining factors give the two roots.

The converse direction is the same identity read the other way: substituting either
root annihilates the right-hand side, hence $y_{(1^3)} = 0$.

## Excluding $z = q$

Only the second root survives, and the argument is that the first carries no algebra.
Substituting $z = q$ into the factorisation gives $y_{(1^3)} = 0$; feeding that back
into the generator and two-crossing normalisations leaves a two-by-two system whose
solution is $y_{(2,1)} = 0$, $y_{(3)} = 1$. The trace is then the one-dimensional
character $T_w \mapsto q^{\ell(w)}$.

Two consequences make the exclusion structural rather than aesthetic. The
mixed-symmetry block carries the entire two-dimensional irrep of $H_3(q)$, so a trace
with $y_{(2,1)} = 0$ sees none of it; and the isospin weights, being branch sums over
the Bratteli diagram, degenerate to $\mu_+ = 1$ and $\mu_- = 0$. A trace that assigns
weight zero to one of the two nucleon-pair channels cannot separate them, so the whole
selection question it was meant to answer disappears with it.

What remains is the single root $z(q^{2}+1) = q^{3}$, which is convention D.
