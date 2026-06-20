**Proposition (selection-rule anchors at c=1 and c=3).**

*Let $q \in \mathbb{R}_{>0}$ and let $h := q - q^{-1}$.  The per-component
selection rule*

$$
  \mathrm{lw}(c)(q) \;:=\; \frac{1}{c+1} \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda
$$

*satisfies the two exact identities*

$$
  \mathrm{lw}(1)(q) \;=\; 1 \qquad (\text{exactly, } \forall q > 0),
$$

$$
  \mathrm{lw}(3)(q) \;=\; \frac{3q^2 + 4 + 3q^{-2}}{4} \;=\; \frac{5}{2} + \frac{3}{4} h^2.
$$

*These are the muon (c=1, knot) and the proton (c=3, Borromean 3-link)
anchors of the per-component selection rule.*

## Why this matters

The zero-parameter selection rule is
$\mathrm{lw}(L) = \frac{1}{c+1}\sum_{\lambda\vdash(c+1)} \dim_q V_\lambda$
where $c$ is the number of link components.  The c=1 case must equal 1
for all $q$ (muon, a knot, framework `linking_weight = 1`); the c=3 case
must equal the Family-A formula
$\frac{5}{2} + \frac{3}{4}h^2$ (proton).  This proposition Lean-formalises
both identities, giving the selection rule's two anchors a derivation-tight
status (not a fit — both follow from the q-deformed hook-length formula).

## Lean proof structure

Two purely algebraic identities at the symbolic level, each closed by
`field_simp; ring`:

1. **c=1 anchor** (`selection_rule_c1_eq_one`):
   $\frac{1}{2}\bigl( \dim_q V_{(2)} + \dim_q V_{(1,1)} \bigr) = 1$.
   Both q-dimensions equal $1$ (each partition of 2 has hook product equal
   to the q-factorial), so the average is exactly 1.

2. **c=3 anchor** (`selection_rule_c3_eq_family_a`):
   $\frac{1}{4} \bigl( \dim_q V_{(4)} + \dim_q V_{(3,1)} + \dim_q V_{(2,2)} +
   \dim_q V_{(2,1,1)} + \dim_q V_{(1,1,1,1)} \bigr)
   = (3q^2 + 4 + 3q^{-2})/4$.

   Using the explicit q-hook formula:
   - $\dim_q V_{(4)} = \dim_q V_{(1,1,1,1)} = 1$
   - $\dim_q V_{(3,1)} = \dim_q V_{(2,1,1)} = [3]_q = q^2 + 1 + q^{-2}$
   - $\dim_q V_{(2,2)} = [4]_q / [2]_q = q^2 + q^{-2}$

   Their sum is $1 + (q^2{+}1{+}q^{-2}) + (q^2{+}q^{-2}) + (q^2{+}1{+}q^{-2})
   + 1 = 4 + 3q^2 + 3q^{-2}$, and dividing by 4 gives the stated form.
   The $h^2$ form follows from $q^2 + q^{-2} = h^2 + 2$.

   Both steps are pure polynomial identities in $\mathbb{Z}[q, q^{-1}]$,
   closed by `ring` after `field_simp` to clear the $q^{-1}$ denominators.

## q-usage discipline

Stated over real $q > 0$ (the substrate-anchor regime).  Both
identities are q-rational, fibre-level, with the c=1 case true
for ALL $q > 0$ — an infinite set of constraints, not one point.
AGENTS.md §7c-compliant.

## Cross-references

- $\operatorname{def:coulomb-charge}$ — where the $h = q - q^{-1}$ structure
  enters at the per-crossing level.
- $\operatorname{prop:coulomb-strong-ratio-q-rational}$ — companion identity
  proving $\tanh(\ln q) = (q^2-1)/(q^2+1)$ over real $q > 0$.
- Derivation audit doc:
  [`docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md`](../../../docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md).
