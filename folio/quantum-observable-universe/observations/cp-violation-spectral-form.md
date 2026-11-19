**Conjecture (spectral form of $\delta_{\mathrm{CP}}$).**
*Let $A = H_n(R_\mathbb{C}, q)$ with complexified ground ring $R_\mathbb{C} = R \otimes \mathbb{Z}[i]$, accommodating $q = |q| \exp(i\theta)$ ([complex chirality rotation](#conj:complex-chirality-rotation)). For a hadronic braid $\beta_\mathcal{K} \in B_n$, the CP-violating discriminant equals the imaginary part of the alternating/symmetric Wedderburn-block trace ratio:*

$$
  \delta_{\mathrm{CP}}(\beta_\mathcal{K})
  \;=\;
  \mathrm{Im}\bigl(F_{\mathrm{Pauli}}(\beta_\mathcal{K})\bigr)
  \;=\;
  \mathrm{Im}\!\left(
    \frac{\chi_{(1^n)}(\beta_\mathcal{K})}
         {\chi_{(n)}(\beta_\mathcal{K})}
  \right) \,\in\, R_\mathbb{C}.
$$

*The real part supplies the Pauli statistical weight ([Pauli factor](#prop:pauli-factor-wedderburn)). The imaginary part isolates CP violation. Amphicheiral or real-$q$ configurations have $\mathrm{Im}(\chi_\lambda) = 0$ and $\delta_{\mathrm{CP}} = 0$.*

**Phase accumulation.**
*For multi-crossing composites, $\theta_{\mathrm{res}}$ accumulates linearly. With $\chi_\lambda(q) = \chi_\lambda(|q|) \exp(i\, n_\lambda \theta)$:*

$$
  \mathrm{Im}\!\left(
    \frac{\chi_{(1^n)}(\beta_\mathcal{K})}
         {\chi_{(n)}(\beta_\mathcal{K})}
  \right)
  \;\sim\; \bigl(n_{(1^n)} - n_{(n)}\bigr) \cdot \theta_{\mathrm{res}}
$$

*to leading order. The difference $n_{(1^n)} - n_{(n)}$ scales with total crossing number, recovering $\delta_{\mathrm{CP}} \sim n_c \theta_{\mathrm{res}}$.*

**Sketch.**
Spectral completeness over $R_\mathbb{C}$ decomposes $F_{\mathrm{Pauli}}$. The alternating block $V_{(1^n)}$ provides phase asymmetry, carrying $(-q)^{-w}$ on a writhe-$w$ crossing ([antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)). The symmetric block carries $q^w$. Their ratio's imaginary part isolates the CP-violating amplitude.

**Falsifiability.**
Amphicheiral knots must yield exactly $\delta_{\mathrm{CP}} = 0$. Any amphicheiral hadron exhibiting CP violation falsifies this characterization.

*Remark.* This relies on ([complex chirality rotation](#conj:complex-chirality-rotation)). Proof requires demonstrating $R_\mathbb{C}$-enrichment uniqueness and matching $\theta_{\mathrm{res}}$ to the Wolfenstein parameterization.
