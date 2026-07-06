**Proposition (selection-rule anchors at c=1 and c=3).**

Let $q \in \mathbb{R}_{>0}$ and let $h := q - q^{-1}$. The per-component selection rule

$$
  \mathrm{lw}(c)(q) \;:=\; \frac{1}{c+1} \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda
$$

satisfies the two exact identities

$$
  \mathrm{lw}(1)(q) \;=\; 1 \qquad (\text{exactly, } \forall q > 0),
$$

$$
  \mathrm{lw}(3)(q) \;=\; \frac{3q^2 + 4 + 3q^{-2}}{4} \;=\; \frac{5}{2} + \frac{3}{4} h^2.
$$

These are the muon (c=1, knot) and the proton (c=3, Borromean 3-link) anchors of the per-component selection rule.

## Significance

The zero-parameter selection rule is $\mathrm{lw}(L) = \frac{1}{c+1}\sum_{\lambda\vdash(c+1)} \dim_q V_\lambda$ where $c$ is the number of link components. The $c=1$ case evaluates to $1$ for all $q$. This matches the muon framework expectation of `linking_weight = 1`. The $c=3$ case evaluates to the Family-A formula $\frac{5}{2} + \frac{3}{4}h^2$, matching the proton. This proposition Lean-formalizes both identities. The two anchors of the selection rule follow strictly from the $q$-deformed hook-length formula, elevating their status from fits to derivations.

## Lean proof structure

We prove two purely algebraic identities at the symbolic level. Both close by `field_simp; ring`:

1. **c=1 anchor** (`selection_rule_c1_eq_one`):
   $\frac{1}{2}\bigl( \dim_q V_{(2)} + \dim_q V_{(1,1)} \bigr) = 1$.
   Both $q$-dimensions equal $1$. Each partition of 2 has a hook product equal to the $q$-factorial, so the average is exactly 1.

2. **c=3 anchor** (`selection_rule_c3_eq_family_a`):
   $\frac{1}{4} \bigl( \dim_q V_{(4)} + \dim_q V_{(3,1)} + \dim_q V_{(2,2)} + \dim_q V_{(2,1,1)} + \dim_q V_{(1,1,1,1)} \bigr) = (3q^2 + 4 + 3q^{-2})/4$.

   We use the explicit $q$-hook formula:
   - $\dim_q V_{(4)} = \dim_q V_{(1,1,1,1)} = 1$
   - $\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)} = [3]_q = q^2 + 1 + q^{-2}$
   - $\dim_q V_{(2,2)} = [4]_q / [2]_q = q^2 + q^{-2}$

   Their sum is $1 + (q^2+1+q^{-2}) + (q^2+q^{-2}) + (q^2+1+q^{-2}) + 1 = 4 + 3q^2 + 3q^{-2}$. Dividing by 4 gives the stated form. The $h^2$ form follows from $q^2 + q^{-2} = h^2 + 2$.

   Both steps are pure polynomial identities in $\mathbb{Z}[q, q^{-1}]$. They are closed by `ring` after using `field_simp` to clear the $q^{-1}$ denominators.

## q-usage discipline

We state these identities over real $q > 0$, aligning with the substrate-anchor regime. Both identities are $q$-rational at the fibre-level. The $c=1$ case holds for all $q > 0$. We thus constrain an infinite set, not a single point. This complies with AGENTS.md §7c.

## Cross-references

- $\operatorname{def:coulomb-charge}$ — introduces the $h = q - q^{-1}$ structure at the per-crossing level.
- $\operatorname{prop:coulomb-strong-ratio-q-rational}$ — companion identity proving $\tanh(\ln q) = (q^2-1)/(q^2+1)$ over real $q > 0$.
- Derivation audit document: [`docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md`](../../../docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md).
