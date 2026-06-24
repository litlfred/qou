The figure-eight braid $4_1$ lives in $H_3(R, q)$ (three strands).  Its
character in an irreducible representation $\rho_\lambda$ of $H_k(R, q)$
with $k \geq 3$ factors through the restriction $H_k(R, q) \downarrow H_3(R, q)$:

$$
  \chi(4_1, \lambda)
  = \sum_{\mu \,\vdash\, 3} f^{\lambda/\mu} \cdot \chi(4_1, \mu)
$$

where $f^{\lambda/\mu}$ is the branching multiplicity --- the number of
standard Young tableaux of skew shape $\lambda/\mu$, counting the
distinct ways to remove $k - 3$ cells from $\lambda$ along a
saturated chain in Young's lattice to arrive at $\mu$.

The three partitions of $3$ contribute:

See [Table 1](#tbl:figure-eight-branching-rule-table1-data).

Substituting:

$$
  \chi(4_1, \lambda)
  = f^{\lambda/[3]} \cdot 1
  + f^{\lambda/[2{,}1]} \cdot (-1 - h^2)
  + f^{\lambda/[1^3]} \cdot 1
$$

Collecting the constant and $h^2$ terms gives the result.

**Combinatorial structure of $b_\lambda$.**
Since $b_\lambda = -f^{\lambda/[2{,}1]}$ is always non-positive, and
$f^{\lambda/[2{,}1]} = 0$ if and only if $\lambda$ does not contain the
Young diagram of $[2{,}1]$ (i.e.\ $\lambda$ is a single row $[k]$ or
a single column $[1^k]$), the $q$-deformation correction vanishes
precisely for the trivial and sign representations.

For the dominant partitions at each level:

See [Table 2](#tbl:figure-eight-branching-rule-table2-data).

The BW scaling of each partition is determined by:

1. **Content sum** $c(\lambda) = \sum_{(i,j) \in \lambda} (j - i)$:
   positive $\to$ $A$-dominated (volume/surface), negative $\to$ $Z/N$-dominated
   (Coulomb/exchange), zero $\to$ isospin-sensitive (Wigner/hook).

2. **Self-conjugacy** ($\lambda = \lambda'$):
   self-conjugate partitions contribute isospin Casimir terms
   ($T(T+1)/A$, $T(T+1)(T+2)/A^2$, etc.).

3. **Conjugate pairing** ($\{\lambda, \lambda'\}$ with $\lambda \neq \lambda'$):
   the sum $\lambda \oplus \lambda'$ gives charge-symmetric corrections
   (form factor, pn correlation).

4. **Hook partitions** ($[k-r, 1^r]$):
   the $H_3 \hookrightarrow H_k$ branching multiplicity determines
   shell effects via the nuclear magic numbers.
$\qquad\blacksquare$
