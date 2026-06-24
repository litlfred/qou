Fix a Descartes universe $(\mathbf{C}, A, \tau)$ with $\chi(A) = -6$. By the
Euler-characteristic relation $\chi = 2 - 2g$ this fixes the genus of Bring's
surface at $g(A) = 4$.

A torus knot $T_{m,n}$ with $\gcd(m,n) = 1$ localized in the fibre
$\mathcal{S}_c$ ([`def:localized-knot`](#def:localized-knot)) inherits a
Seifert surface of genus $g(T_{m,n}) = (m-1)(n-1)/2$. Embeddability into the
genus-$4$ ambient surface forces

$$
  g(T_{m,n}) = \frac{(m-1)(n-1)}{2} \leq g(A) = 4,
  \qquad\text{i.e.}\qquad (m-1)(n-1) \leq 8.
$$

This bounds a product of two non-negative integers, so it cuts out a finite
region: with $m \geq 2$ and $n > m$ the inequality forces $m, n \leq 9$, a
finite range. Discharging the coprimality and ordering constraints across it
leaves exactly the six pairs

$$
  (2,3),\ (2,5),\ (2,7),\ (2,9),\ (3,4),\ (3,5).
$$

The formalisation `QOU.Torsion.torus_knot_generators_finite` carries out
precisely this argument: it exhibits the finite witness set $S$ of these six
pairs and verifies, by reducing to the genus bound and an exhaustive case
split over the forced range $m, n \leq 9$, that every admissible $(m,n)$ lies
in $S$.

Adjoining the unknot $T_{1,0} = 0_1$ of genus $0$ yields the generator set
$\mathcal{G}$ ([`def:knot-particle-generation`](#def:knot-particle-generation))
with $|\mathcal{G}| = 7$, a cardinality fixed by $\chi(A)$. The recursive brane
tower refines the blow-up structure within existing handles without raising the
genus, so this count is stable across all brane levels. $\qquad\blacksquare$
