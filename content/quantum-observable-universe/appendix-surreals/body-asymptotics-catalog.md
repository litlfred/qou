We catalog the analytic error bounds from the main paper alongside their surreal $\ordw$-equivalents. The main paper expresses bounds in classical Big-O, little-o, and geometric-tail forms. This catalog translates them into surreal statements using [Big-O via $\ordw$](#rem:conway-normal-form). We leave the main paper in classical notation and use this catalog as a formal anchor.

## Body-paper analytic bounds

### Chapter: Braids and Knots

See [Table 1](#tbl:body-asymptotics-catalog-table1-data).

### Chapter: Fluid Dynamics

See [Table 2](#tbl:body-asymptotics-catalog-table2-data).

### Classical-limit blocks

See [Table 3](#tbl:body-asymptotics-catalog-table3-data).

## Reading conventions

The classical statement and the $\ordw$-statement are logically equivalent under the dictionary of [Big-O via $\ordw$](#rem:conway-normal-form):

- A bound $|f| \leq C \cdot g$ with $C \in \mathbb{R}_{>0}$ is equivalent to $\ordw(f) \leq \ordw(g)$ (i.e. $f \preceq g$).
- The expression $f = O(g)$ is equivalent to $\ordw(f) \leq \ordw(g)$.
- The expression $f \sim g$ is equivalent to $\ordw(f) = \ordw(g)$ with matching leading coefficients ($f \simeq g$).
- A classical limit $\lim_{x \to x_0} f(x) = L$ corresponds to $\mathrm{st}\bigl(f(x_0 + \varepsilon)\bigr) = L$ for an infinitesimal $\varepsilon$ ([standard-part functor](#def:standard-part-functor)).

This catalog anchors the surreal notation in concrete applications. It allows propositions to reference the surreal appendix without altering their classical statements.

## Engineering note

The recursive jet structures (mass endomorphism brane tower, Yekutieli jet prolongation, NS jet correction $\delta_n$) admit a common surreal interpretation. Each level adds one factor of the relevant infinitesimal ($\hbar_q$ in the brane tower, $d$ in the NS Biot--Savart structure). The $\ordw$ of the level-$n$ correction is therefore linear in $n$. This realizes the [surreal blow-up calculus](#def:surreal-blowup-calculus). It matches the geometric-series tail bounds exactly.
