This remark catalogs the analytic error bounds from the main paper alongside their surreal $\ordw$-equivalents. The main paper expresses bounds in classical Big-O, little-o, and geometric-tail forms; each translates via [Big-O via $\ordw$](#rem:conway-normal-form). The main paper retains classical notation while this catalog serves as a formal anchor.

### Chapter: Braids and Knots
See [Table 1](#tbl:body-asymptotics-catalog-table1-data).

### Chapter: Fluid Dynamics
See [Table 2](#tbl:body-asymptotics-catalog-table2-data).

### Classical-limit blocks
See [Table 3](#tbl:body-asymptotics-catalog-table3-data).

The classical statement and the $\ordw$-statement are logically equivalent:
- $|f| \leq C \cdot g$ ($C \in \mathbb{R}_{>0}$) or $f = O(g)$ translates to $\ordw(f) \leq \ordw(g)$ ($f \preceq g$).
- $f \sim g$ translates to $\ordw(f) = \ordw(g)$ with matching leading coefficients ($f \simeq g$).
- $\lim_{x \to x_0} f(x) = L$ translates to $\mathrm{st}\bigl(f(x_0 + \varepsilon)\bigr) = L$ for an infinitesimal $\varepsilon$.

The recursive jet structures (mass endomorphism brane tower, jet prolongation, NS jet correction $\delta_n$) admit a common surreal interpretation. Each level adds one factor of the relevant infinitesimal ($\hbar_q$ or $d$). The $\ordw$ of the level-$n$ correction is linear in $n$. This realizes the [surreal blow-up calculus](#def:surreal-blowup-calculus) and matches the geometric-series tail bounds exactly.
