## Definition

Let $\Lambda^2(n)$ be the [`two-row stratum`](#def:two-row-stratum) of $H_n(q)$. The :defterm[two-row projection]{#two-row-projection} is the orthogonal projection onto the two-row Wedderburn subalgebra:
$$
  \pi_{\mathrm{2-row}} \;\colon\; H_n(q) \;\to\;
    \bigoplus_{\lambda \in \Lambda^2(n)} \mathrm{End}(V_\lambda).
$$
The map is an idempotent ($\pi_{\mathrm{2-row}}^2 = \pi_{\mathrm{2-row}}$). The canonical Markov trace splits as:
$$
  \mathrm{tr}_M(\beta)
  \;=\; \underbrace{\sum_{\lambda \in \Lambda^2(n)} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M(\pi_{\mathrm{2-row}}\,\beta)}
  \;+\; \underbrace{\sum_{\ell(\lambda) > 2} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M((1-\pi_{\mathrm{2-row}})\,\beta)}
$$
where $y_\lambda$ is the Wenzl weight from [Canonical q-deformed Wedderburn-block weight $\tilde w_\lambda$ and named scalings (BW, LP for all $\lambda$)](#prop:wedderburn-weight-canonical).
