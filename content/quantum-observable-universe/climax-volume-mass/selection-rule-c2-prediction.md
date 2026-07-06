**Proposition (selection-rule at c=2 — prediction).**

Let $q \in \mathbb{R}_{>0}$. The per-component selection rule ([`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3)) applied at $c=2$ gives the closed form

$$
  \mathrm{lw}(2)(q) \;:=\; \frac{1}{3} \sum_{\lambda \vdash 3} \dim_q V_\lambda
  \;=\; \frac{2 + [2]_q}{3} \;=\; \frac{(q+1)^2}{3q}.
$$

This is the prediction for a 2-component link, such as the Hopf link. The closed form is a finite Laurent rational over $\mathbb{Z}[q, q^{-1}]$. Like the $c=1$ and $c=3$ anchors, it is derivation-tight with zero free parameters.

## Significance

The per-component rule is $\mathrm{lw}(c) = (1/(c+1)) \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda$. It is anchored at $c=1$ (muon, $\mathrm{lw}=1$ exactly) and $c=3$ (proton, $\mathrm{lw} = 5/2 + (3/4)h^2$ via Family-A). The $c=2$ case provides the first testable prediction of the rule beyond the known anchors.

This proposition Lean-formalizes the closed form for $c=2$. The prediction shares the provenance of its anchors as a pure algebraic identity in the $q$-deformed hook-length formula. We can test any independent determination of a 2-component link's linking weight against this exact formula without ambiguity.

## Lean proof structure

We evaluate a single algebraic identity at the symbolic level:

$$
  \frac{1}{3} \bigl( \dim_q V_{(3)} + \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)} \bigr)
  \;=\; \frac{(q+1)^2}{3q}.
$$

We use the explicit $q$-hook values for partitions of 3:

- $\dim_q V_{(3)} = 1$ (single-row Young diagram, all hooks contribute trivially)
- $\dim_q V_{(2,1)} = [2]_q = q + q^{-1}$ (standard representation of $H_3$; $q$-hook computation)
- $\dim_q V_{(1,1,1)} = 1$ (single-column, conjugate of $V_{(3)}$)

Their sum is $2 + q + q^{-1}$. Dividing by 3 yields $(2 + q + q^{-1})/3 = (q^2 + 2q + 1)/(3q) = (q+1)^2/(3q)$.

This is a pure polynomial-ring identity once $q^{-1}$ denominators are cleared. We close it by `field_simp; ring` over $\mathbb{R}_{>0}$.

## q-usage discipline

We state the result over real $q > 0$. The closed form $(q+1)^2/(3q)$ is a Laurent rational in $\mathbb{Z}[q, q^{-1}]$, indicating a fibre-level construction. At $q = q_0$, it evaluates to $\approx 1.337$. We do not invoke $|q|=1$. Both $q$ and $q^{-1}$ remain real positive for all real $q > 0$. This complies with AGENTS.md §7c.

## Cross-references

- [`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3) — the two known anchors establishing the rule's existence.
- Derivation audit: [`docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md`](../../../docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md).
