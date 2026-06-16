**Definition (Wenzl A-operator).**
*Let $\lambda \vdash n$ with $n = n_1 + n_2$, and let
$I = \sigma_{n_1} \in \mathbf{H}_n(q)$ be the inter-block interface
generator joining $\mathbf{H}_{n_1}(q)$ and $\mathbf{H}_{n_2}(q)$. In the
Wenzl 1988 Littlewood–Richardson decomposition of the restriction*

$$
  V_\lambda \;\downarrow_{\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q)}
  \;=\; \bigoplus_{\mu \vdash n_1,\; \nu \vdash n_2}
        c^\lambda_{\mu\nu}\,(V_\mu \boxtimes V_\nu),
$$

*the **Wenzl A-operator** $A^\lambda_{\mu\nu}(I)$ is the $(\mu, \nu)$-block
of $I$ acting on the corresponding isotypic summand:*

$$
  A^\lambda_{\mu\nu}(I) \;\in\; \mathrm{End}(V_\mu \otimes V_\nu)^{\oplus c^\lambda_{\mu\nu}},
$$

*where $c^\lambda_{\mu\nu}$ is the
[Littlewood–Richardson coefficient](lr-coefficient-hecke.md).*

## Role

The A-operator is the operator-valued payload of Wenzl 1988 Sub-lemma 2.1:
for $\beta_1 \in \mathbf{H}_{n_1}(q)$, $\beta_2 \in \mathbf{H}_{n_2}(q)$,

$$
  \chi^\lambda(\beta_1 \cdot I \cdot \beta_2)
    = \sum_{\mu \vdash n_1,\; \nu \vdash n_2}
      c^\lambda_{\mu\nu}\,
      \mathrm{Tr}\!\bigl(A^\lambda_{\mu\nu}(I)\,
                         (\rho_\mu(\beta_1) \otimes \rho_\nu(\beta_2))\bigr).
$$

Two downstream blocks consume it:

- [`prop:crystal-r-matrix-sub-lemma`](crystal-r-matrix-sub-lemma.md)
  reads its matrix-entry **pole order** at $q \to 0$
  ($\mathbf{1}[\rho_T(i) \le -1]$, conditional on
  [`conj:crystal-graph-realization`](crystal-graph-realization.md)).
- [`prop:operator-valued-combiner-convergence`](operator-valued-combiner-convergence.md)
  accumulates its **per-peel contributions** into the per-isotope binding
  tower.

## Computational realisation

The matrix entries of $A^\lambda_{\mu\nu}(I)$ at the substrate $q_0$ are
extracted by the bilinear-system solver
[`a_operator/A_operator_extract_at_level.py`](../../../computations/a_operator/A_operator_extract_at_level.py),
with per-level witnesses
`A-operator-extract-h{n}-{iface}.witness.json`. The $\mathbf{H}_6$
(deuteron) extract is full-rank; the $\mathbf{H}_{9+}$ extracts are
least-squares fits over the inner-test family, so a *universal*
A-operator — the input required for a concrete
[`prop:operator-valued-combiner-convergence`](operator-valued-combiner-convergence.md)
instance — remains the research-grade open item.

## Lean

[`wenzl-A-operator.lean`](wenzl-A-operator.lean) names the operator data as a
class `WenzlAOperator` carrying the per-`(λ, μ, ν, I)` block slot and its LR
multiplicity. This is a naming/structure block (no semantic claim beyond the
existence of the operator data), so it carries no `sorry`.
