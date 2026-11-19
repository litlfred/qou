*Let $q \in \mathbb{R}_{>0}$ and let $h := q - q^{-1}$. The per-component selection rule*

$$
  \mathrm{lw}(c)(q) \;:=\; \frac{1}{c+1} \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda
$$

*satisfies the two exact identities:*

$$
  \mathrm{lw}(1)(q) \;=\; 1 \qquad (\text{exactly, } \forall q > 0),
$$

$$
  \mathrm{lw}(3)(q) \;=\; \frac{3q^2 + 4 + 3q^{-2}}{4} \;=\; \frac{5}{2} + \frac{3}{4} h^2.
$$

*These form the muon (c=1, knot) and the proton (c=3, Borromean 3-link) anchors of the per-component selection rule.*

## Significance

The zero-parameter selection rule reads $\mathrm{lw}(L) = \frac{1}{c+1}\sum_{\lambda\vdash(c+1)} \dim_q V_\lambda$, where $c$ is the number of link components. The $c=1$ case equals $1$ for all $q$ (muon, a single-component knot with linking weight $1$), and the $c=3$ case equals the Family-A formula $\frac{5}{2} + \frac{3}{4}h^2$ (proton, a three-component Borromean link). Both identities follow directly from the $q$-hook-length formula by evaluating the quantum dimensions $\dim_q V_\lambda$ over the partitions of $2$ and $4$, where each partition shape maps through its conjugate and hook lengths to $[n]_q!$ divided by the hook $q$-integer product.

## Proof structure

Two purely algebraic identities hold at the symbolic level:

1. **$c=1$ anchor**:
   $\frac{1}{2}\bigl( \dim_q V_{(2)} + \dim_q V_{(1,1)} \bigr) = 1$.
   Both $q$-dimensions equal $1$ (each partition of $2$ has a hook product equal to the $q$-factorial), so the average is $1$.
2. **$c=3$ anchor**:
   $\frac{1}{4} \bigl( \dim_q V_{(4)} + \dim_q V_{(3,1)} + \dim_q V_{(2,2)} + \dim_q V_{(2,1,1)} + \dim_q V_{(1,1,1,1)} \bigr) = (3q^2 + 4 + 3q^{-2})/4$.

   Using the explicit $q$-hook formula:
   - $\dim_q V_{(4)} = \dim_q V_{(1,1,1,1)} = 1$
   - $\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)} = [3]_q = q^2 + 1 + q^{-2}$
   - $\dim_q V_{(2,2)} = [4]_q / [2]_q = q^2 + q^{-2}$

   Their sum is $1 + (q^2{+}1{+}q^{-2}) + (q^2{+}q^{-2}) + (q^2{+}1{+}q^{-2}) + 1 = 4 + 3q^2 + 3q^{-2}$. Dividing by $4$ yields the stated form. The $h^2$ form follows from $q^2 + q^{-2} = h^2 + 2$.

   Both steps hold as polynomial identities in $\mathbb{Z}[q, q^{-1}]$ after clearing $q^{-1}$ denominators.

## $q$-usage discipline

This holds over real $q > 0$ (the aether-anchor regime). Both identities are $q$-rational, fibre-level constructs. The $c=1$ case holds for all $q > 0$ (an infinite set of constraints, not a single point).

## Cross-references

- [Coulomb charge](#def:coulomb-charge) — introduces the $h = q - q^{-1}$ structure at the per-crossing level.
- [Coulomb-strong ratio identity](#prop:coulomb-strong-ratio-q-rational) — companion identity proving $\tanh(\ln q) = (q^2-1)/(q^2+1)$ over real $q > 0$.
