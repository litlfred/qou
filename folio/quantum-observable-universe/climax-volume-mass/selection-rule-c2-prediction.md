*Let $q \in \mathbb{R}_{>0}$. The per-component selection rule ([the $c=1,3$ anchor proposition](#prop:selection-rule-anchors-c1-c3)) applied at $c=2$ yields the closed form:*

$$
  \mathrm{lw}(2)(q) \;:=\; \frac{1}{3} \sum_{\lambda \vdash 3} \dim_q V_\lambda
  \;=\; \frac{2 + [2]_q}{3} \;=\; \frac{(q+1)^2}{3q}.
$$

*This supplies the rule's prediction for a 2-component link (e.g. the Hopf link). The closed form is a finite Laurent rational over $\mathbb{Z}[q, q^{-1}]$. Like the c=1 and c=3 anchors, it is derivation-tight (no fit, zero free parameters).*

## Significance

The per-component rule states $\mathrm{lw}(c) = (1/(c+1)) \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda$. It is anchored at $c=1$ (muon, $\mathrm{lw}=1$ for all $q$) and $c=3$ (proton, $\mathrm{lw} = 5/2 + (3/4)h^2$ via Family-A). The $c=2$ case provides the **first testable prediction** of the rule beyond the two anchors.

The closed form for $c=2$ follows directly from the hook-length formula: the sum ranges over the quantum dimensions $\dim_q V_\lambda$ of the three partitions of $3$, with $\dim_q V_{(2,1)} = [2]_q$ derived from the hook multiset $\{3,1,1\}$. Any independent determination of a $2$-component link's linking weight—such as a Hopf-link or gluon electromagnetic-linking application—can be tested against this exact formula.

## Proof structure

The result rests on a single algebraic identity at the symbolic level:

$$
  \frac{1}{3} \bigl( \dim_q V_{(3)} + \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)} \bigr)
  \;=\; \frac{(q+1)^2}{3q}.
$$

Using the explicit $q$-hook values for partitions of $3$:

- $\dim_q V_{(3)} = 1$ (single-row Young diagram, all hooks contribute trivially)
- $\dim_q V_{(2,1)} = [2]_q = q + q^{-1}$ (standard representation of $H_3(q)$)
- $\dim_q V_{(1,1,1)} = 1$ (single-column, conjugate of $V_{(3)}$)

Their sum is $2 + q + q^{-1}$. Dividing by $3$ yields $(2 + q + q^{-1})/3 = (q^2 + 2q + 1)/(3q) = (q+1)^2/(3q)$, a polynomial-ring identity over $\mathbb{R}_{>0}$ once $q^{-1}$ denominators are cleared.

## $q$-usage discipline

This holds over real $q > 0$ (aether-anchor regime). The closed form $(q+1)^2/(3q)$ is a Laurent rational in $\mathbb{Z}[q, q^{-1}]$ — a fibre-level construction. At $q = q_0$, it evaluates to $\approx 1.337$. There is no $|q|=1$ step; both $q$ and $q^{-1}$ are real positive at any real $q > 0$.

## Cross-references

- [The $c=1,3$ selection-rule anchors](#prop:selection-rule-anchors-c1-c3) — the two anchors that establish the rule's existence.
