**Conjecture (Confinement $\to$ NF-structure forcing).**
*Let $\beta = \beta_1 \star I \star \beta_2 \in B_n$ be a compound braid across a basis interface $I$. Assuming the confinement hypothesis $|A| < n!$, the active LP set $A$ governs the normal form behavior:*

1. *(NF-support localisation) The Wedderburn maximizer $\lambda^\star \in \arg\max_\lambda \mathrm{ord}_{q=0}^{(-)} \chi_\lambda(T_\beta)$ resides strictly inside the active set $A$.*
2. *(Shift bound) The structural shift holds to a duality-bounded deviation $\Delta$:*

$$
  \mathrm{shift}_{\mathrm{NF}}(\beta)
  \;=\; \alpha_{\mathrm{shift}}(I) + \Delta(\beta_1, \beta_2; A),
  \qquad
  |\Delta| \;\leq\; \mathrm{duality\_gap}(\beta).
$$

Empirical benchmarking on a 6-compound test set consistently returned an exact zero duality gap. The maximizer rigidly falls into the active set every time. The deviation bounded structurally to small expected length scales in all instances. The test outputs conform strictly to the continuous strong-duality theorem predictions.
