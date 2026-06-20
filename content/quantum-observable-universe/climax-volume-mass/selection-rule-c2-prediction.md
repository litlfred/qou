**Proposition (selection-rule at c=2 — prediction).**

*Let $q \in \mathbb{R}_{>0}$.  The per-component selection rule
([`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3))
applied at $c=2$ gives the closed form*

$$
  \mathrm{lw}(2)(q) \;:=\; \frac{1}{3} \sum_{\lambda \vdash 3} \dim_q V_\lambda
  \;=\; \frac{2 + [2]_q}{3} \;=\; \frac{(q+1)^2}{3q}.
$$

*This is the rule's prediction for a 2-component link (= 2 link components,
e.g. the Hopf link).  The closed form is a finite Laurent rational over
$\mathbb{Z}[q, q^{-1}]$ — like the c=1 and c=3 anchors, derivation-tight
(no fit, zero free parameters).*

## Why this matters

The per-component rule is
$\mathrm{lw}(c) = (1/(c+1)) \sum_{\lambda \vdash (c+1)} \dim_q V_\lambda$,
anchored at c=1 (muon, $\mathrm{lw}=1$ exactly $\forall q$) and c=3
(proton, $\mathrm{lw} = 5/2 + (3/4)h^2$ via Family-A).  The c=2 case is the
**first testable prediction** of the rule beyond the two known anchors.

This proposition Lean-formalises the closed form for c=2 so the prediction
sits alongside its anchors with the same provenance (pure algebraic identity
in the q-deformed hook-length formula).  Any independent determination of a
2-component link's linking_weight in the framework — e.g. a Hopf-link or
gluon EM-linking application — can be tested against this exact formula
without ambiguity.

## Lean proof structure

Single algebraic identity at the symbolic level:

$$
  \frac{1}{3} \bigl( \dim_q V_{(3)} + \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)} \bigr)
  \;=\; \frac{(q+1)^2}{3q}.
$$

Using the explicit q-hook values for partitions of 3:

- $\dim_q V_{(3)} = 1$ (single-row Young diagram, all hooks contribute trivially)
- $\dim_q V_{(2,1)} = [2]_q = q + q^{-1}$ (standard rep at H_3; q-hook computation)
- $\dim_q V_{(1,1,1)} = 1$ (single-column, conjugate of $V_{(3)}$)

Their sum is $2 + q + q^{-1}$, and dividing by 3 gives
$(2 + q + q^{-1})/3 = (q^2 + 2q + 1)/(3q) = (q+1)^2/(3q)$.

This is a pure polynomial-ring identity once $q^{-1}$ denominators are
cleared.  Closed by `field_simp; ring` over $\mathbb{R}_{>0}$.
## q-usage discipline

Stated over real $q > 0$ (substrate-anchor regime).  The closed form
$(q+1)^2/(3q)$ is a Laurent rational in $\mathbb{Z}[q, q^{-1}]$ — fibre-level
construction.  At $q = q_0$ it evaluates to $\approx 1.337$.  No $|q|=1$
step; both $q$ and $q^{-1}$ are real positive at any real $q > 0$.
AGENTS.md §7c-compliant.

## Cross-references

- [`prop:selection-rule-anchors-c1-c3`](#prop:selection-rule-anchors-c1-c3) — the two
  known anchors that the rule's existence is established on.
- Derivation audit:
  [`docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md`](../../../docs/audits/2026-06-03-habiro-per-knot-lambda-derivation.md).
