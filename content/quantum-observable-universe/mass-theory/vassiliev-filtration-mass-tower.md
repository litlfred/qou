The Markov trace $\operatorname{tr}_M(\beta)(q)$ of a braid word
$\beta$ is a rational function of $q$. Expanding about $q = 1$
(the classical limit) in the Hecke deformation parameter
$h = q - q^{-1}$:

$$
  \operatorname{tr}_M(\beta)(q)
  \;=\;
  \underbrace{c_0(\beta)}_{\text{type 0}}
  \;+\;
  \underbrace{c_1(\beta) \cdot h}_{\text{type 1}}
  \;+\;
  \underbrace{c_2(\beta) \cdot h^2}_{\text{type 2}}
  \;+\;
  \cdots
$$

Each coefficient $c_k(\beta)$ is a **Vassiliev invariant of type
$k$** (also called a finite-type invariant of order $k$). This is
a theorem of Birman-Lin (1993) \cite{birmanlin1993}: the coefficients of
the power series expansion of any quantum knot invariant at $q = 1$ are
finite-type invariants, with the order matching the power of the
deformation parameter.

## The Vassiliev filtration of the mass tower

### Content of the Vassiliev grading

The graded decomposition
$V_0 \subset V_1 \subset V_2 \subset \cdots$ of knot invariants
by type gives a **canonical filtration by complexity**:

| Type | Detects | Mass-formula role | Example |
|---|---|---|---|
| 0 | Number of components | Baryon vs meson | $c_0 = 1$ for all knots |
| 1 | Linking number | — (vanishes for knots) | $c_1 = 0$ for any knot |
| 2 | Framing / writhe | Leading mass correction | $c_2 \propto$ the $h^2$ term in $\lambda_{\mathrm{scale}}$ |
| 3 | Crossing-change sensitivity | Sub-leading mass | $c_3$ distinguishes trefoil from unknot |
| $k$ | $k$-fold crossing relations | Order-$k$ mass correction | $c_k$ gives the $h^k$ mass term |

**For the mass formula**, the Vassiliev filtration means:

1. **The leading term** $c_0 = \operatorname{tr}_M(\beta)(q=1)$
   is the classical Markov trace — it gives the
   "all-knots-are-equivalent" baseline (all knots have the same
   $c_0$; mass differences arise at $k \geq 2$).

2. **The $h^2$ correction** $c_2 \cdot h^2$ is the first
   mass-discriminating term. This is exactly the term that the
   CAL-4 $\lambda_{\mathrm{scale}}$ investigation (PRs #888–#969)
   was trying to derive — it is a **type-2 Vassiliev invariant**.

3. **Higher corrections** $c_k \cdot h^k$ for $k \geq 3$
   give the precision refinements. The mass tower's convergence
   rate is controlled by $|h|^k = |q - q^{-1}|^k \approx
   (0.209)^k$ at substrate $q_0 \approx 1.110$ — each order
   suppresses by a factor of $\sim 0.209$, giving roughly one
   additional decimal digit of precision per Vassiliev order.

### Connection to the Archimedean-image table

In the Archimedean-image table
([`rem:archimedean-image-table`](#rem:archimedean-image-table)),
each row's $\tau$-image can be decomposed via the Vassiliev
filtration:

- **Row 3 (Markov trace)**: $\operatorname{tr}_M = c_0 + c_2 h^2
  + c_3 h^3 + \cdots$ — the full Vassiliev expansion.
- **Row 4 (Jones polynomial)**: proportional to row 3; same
  Vassiliev coefficients up to normalisation.
- **Row 5 (HOMFLYPT)**: the two-variable expansion
  $P(K; v, z) = \sum_{i,j} a_{ij} v^i z^j$ gives a
  **two-dimensional** Vassiliev-like grading — the $z$-degree
  controls the Vassiliev type, while the $v$-degree controls
  the SU($N$) channel. This is strictly richer than the one-
  variable Jones expansion.
- **Row 7 (Wedderburn $\dim_q V_\lambda$)**: the quantum dimension
  is a type-0 invariant (it depends only on the partition, not on
  the braid). The per-partition contribution
  $y_\lambda \cdot \chi_\lambda(\beta)$ has Vassiliev type
  controlled by the partition's content statistics.

