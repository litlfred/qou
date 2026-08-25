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

The zero-parameter selection rule reads $\mathrm{lw}(L) = \frac{1}{c+1}\sum_{\lambda\vdash(c+1)} \dim_q V_\lambda$, where $c$ is the number of link components. The c=1 case must equal 1 for all $q$ (muon, a knot, framework `linking_weight = 1`). The c=3 case must equal the Family-A formula $\frac{5}{2} + \frac{3}{4}h^2$ (proton). This proposition Lean-formalises both identities. It grants the selection rule's two anchors derivation-tight status (they are not a fit; both follow from the q-deformed hook-length formula).

## Lean proof structure

We provide two purely algebraic identities at the symbolic level, each closed by `field_simp; ring`:

1. **c=1 anchor** (`selection_rule_c1_eq_one`):
   $\frac{1}{2}\bigl( \dim_q V_{(2)} + \dim_q V_{(1,1)} \bigr) = 1$.
   Both q-dimensions equal $1$ (each partition of 2 has a hook product equal to the q-factorial), so the average is exactly 1.
2. **c=3 anchor** (`selection_rule_c3_eq_family_a`):
   $\frac{1}{4} \bigl( \dim_q V_{(4)} + \dim_q V_{(3,1)} + \dim_q V_{(2,2)} + \dim_q V_{(2,1,1)} + \dim_q V_{(1,1,1,1)} \bigr) = (3q^2 + 4 + 3q^{-2})/4$.

   Using the explicit q-hook formula:
   - $\dim_q V_{(4)} = \dim_q V_{(1,1,1,1)} = 1$
   - $\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)} = [3]_q = q^2 + 1 + q^{-2}$
   - $\dim_q V_{(2,2)} = [4]_q / [2]_q = q^2 + q^{-2}$

   Their sum is $1 + (q^2{+}1{+}q^{-2}) + (q^2{+}q^{-2}) + (q^2{+}1{+}q^{-2}) + 1 = 4 + 3q^2 + 3q^{-2}$. Dividing by 4 yields the stated form. The $h^2$ form follows from $q^2 + q^{-2} = h^2 + 2$.

   Both steps operate as pure polynomial identities in $\mathbb{Z}[q, q^{-1}]$. They close by `ring` after `field_simp` clears the $q^{-1}$ denominators.

## q-usage discipline

This holds over real $q > 0$ (the substrate-anchor regime). Both identities are q-rational, fibre-level constructs. The c=1 case holds for ALL $q > 0$ (an infinite set of constraints, not a single point).

## Cross-references

- [`def:coulomb-charge`](#def:coulomb-charge) — introduces the $h = q - q^{-1}$ structure at the per-crossing level.
- [`prop:coulomb-strong-ratio-q-rational`](#prop:coulomb-strong-ratio-q-rational) — companion identity proving $\tanh(\ln q) = (q^2-1)/(q^2+1)$ over real $q > 0$.
