The main paper states a number of analytic error bounds in
classical Big-O / little-o / geometric-tail form. This remark
catalogs each of them and records the equivalent surreal
$\ordw$-statement under the convention of
[Big-O via $\ordw$](#rem:conway-normal-form). The body of the paper
is **not rewritten** in $\preceq$ / $\prec$ form; this catalog is
the formal anchor that body propositions point to.

## Body-paper analytic bounds

### Chapter: Braids and Knots

See [Table 1](#tbl:body-asymptotics-catalog-table1-data).

### Chapter: Fluid Dynamics

See [Table 2](#tbl:body-asymptotics-catalog-table2-data).

### Classical-limit blocks

See [Table 3](#tbl:body-asymptotics-catalog-table3-data).

### Reading conventions

For each entry above, the classical statement and the
$\ordw$-statement are **logically equivalent** under the dictionary
of [Big-O via $\ordw$](#rem:conway-normal-form):

- A classical bound $|f| \leq C \cdot g$ with $C$ a positive real
  constant is equivalent to $\ordw(f) \leq \ordw(g)$ (i.e.\
  $f \preceq g$).
- A classical $f = O(g)$ is equivalent to $\ordw(f) \leq \ordw(g)$.
- A classical $f \sim g$ is equivalent to $\ordw(f) = \ordw(g)$
  with matching leading coefficient ($f \simeq g$).
- A classical limit $\lim_{x \to x_0} f(x) = L$ in the body is
  recoverable as $\mathrm{st}\bigl(f(x_0 + \varepsilon)\bigr) = L$
  for an infinitesimal $\varepsilon$
  ([standard-part functor](#def:standard-part-functor)).

The catalog is non-load-bearing. It exists so that body
propositions can carry a single forward reference to the surreal
appendix without rewriting their statement, and so that the
appendix's notational machinery is visibly anchored in concrete
body content rather than left as an isolated convention.
