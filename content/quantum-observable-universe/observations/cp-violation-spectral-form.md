**Conjecture (spectral form of $\delta_{\mathrm{CP}}$).**
*Let $A = H_n(R_\mathbb{C}, q)$ with complexified ground ring $R_\mathbb{C} = R \otimes \mathbb{Z}[i]$, permitting $q = |q| \exp(i\theta)$ as detailed in ([complex chirality rotation](#conj:complex-chirality-rotation)). For a hadronic braid $\beta_\mathcal{K} \in B_n$, the CP-violating discriminant is the imaginary part of the alternating/symmetric Wedderburn-block trace ratio:*

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

*The real part recovers the Pauli statistical weight ([Pauli factor](#prop:pauli-factor-wedderburn)). The imaginary part isolates CP violation. CP-symmetric configurations (amphicheiral or real-$q$) have $\mathrm{Im}(\chi_\lambda) = 0$ and $\delta_{\mathrm{CP}} = 0$.*

**Phase accumulation.**
*For multi-crossing composites, the residual phase $\theta_{\mathrm{res}}$ of $q$ accumulates linearly in the crossing count. Writing the leading character behavior as $\chi_\lambda(q) = \chi_\lambda(|q|) \exp(i\, n_\lambda \theta)$:*

$$
  \mathrm{Im}\!\left(
    \frac{\chi_{(1^n)}(\beta_\mathcal{K})}
         {\chi_{(n)}(\beta_\mathcal{K})}
  \right)
  \;\sim\; \bigl(n_{(1^n)} - n_{(n)}\bigr) \cdot \theta_{\mathrm{res}}
$$

*to leading order in $\theta_{\mathrm{res}}$. The term $n_{(1^n)} - n_{(n)}$ is the difference of phase exponents on the two extremal blocks. For multi-crossing structures like kaons, this difference scales with the total crossing number. This recovers the empirical $\delta_{\mathrm{CP}} \sim n_c \theta_{\mathrm{res}}$ relation from ([CP violation](#sec:cp-violation-evidence)).*

**Sketch.**
Spectral completeness over $R_\mathbb{C}$ (the complexified analogue of the real spectral completeness for $\alpha_{\mathrm{EM}}$) decomposes $F_{\mathrm{Pauli}}$ into central-idempotent characters. The alternating block $V_{(1^n)}$ provides the sole source of phase asymmetry. Its character carries $(-q)^{-w}$ on a writhe-$w$ crossing ([antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)), while the symmetric block carries $q^w$. The imaginary part of their ratio isolates the CP-violating amplitude.

**Falsifiability.**
This framework mandates that amphicheiral knots yield exactly $\delta_{\mathrm{CP}} = 0$. Any observed CP violation in a single amphicheiral hadron strictly falsifies this spectral characterization. The non-amphicheiral $\bar{u}s$ configuration of the kaon system ($K_L \to \pi\pi$ at $\sim 2 \times 10^{-3}$) serves as the primary empirical test.

*Remark.* This conjecture depends on ([complex chirality rotation](#conj:complex-chirality-rotation)). Promoting it to a formal proposition requires:
(a) A categorical proof that $R_\mathbb{C}$-enrichment is the unique CP-violating extension.
(b) A quantitative match between $\theta_{\mathrm{res}}$ and the Wolfenstein parameterization of the CKM matrix.

**Archimedean specialisation (§7c).** This block relies on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical or $q$-deformation identities it draws on remain valid over an abstract coefficient ring. Only their archimedean realization is specialized here.
