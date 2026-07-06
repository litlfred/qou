**Conjecture (spectral form of $\delta_{\mathrm{CP}}$).**
*Let $A = H_n(R_\mathbb{C}, q)$ with $R_\mathbb{C} = R \otimes
\mathbb{Z}[i]$ the complexified ground ring, allowing
$q = |q| \exp(i\theta)$ as in
([complex chirality rotation](#conj:complex-chirality-rotation)).
For a hadronic braid $\beta_\mathcal{K} \in B_n$ the CP-violating
discriminant is the imaginary part of the alternating/symmetric
Wedderburn-block trace ratio*

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

*The real part recovers the Pauli statistical weight
([Pauli factor](#prop:pauli-factor-wedderburn)); the imaginary part
captures CP violation.  CP-symmetric configurations
(amphicheiral or real-$q$) have $\mathrm{Im}(\chi_\lambda) = 0$ and
$\delta_{\mathrm{CP}} = 0$.*

**Phase accumulation.**
*For multi-crossing composites the residual phase $\theta_{\mathrm{res}}$
of $q$ accumulates linearly in the crossing count.  Writing
$\chi_\lambda(q) = \chi_\lambda(|q|) \exp(i\, n_\lambda \theta)$ for
the leading character behaviour,*

$$
  \mathrm{Im}\!\left(
    \frac{\chi_{(1^n)}(\beta_\mathcal{K})}
         {\chi_{(n)}(\beta_\mathcal{K})}
  \right)
  \;\sim\; \bigl(n_{(1^n)} - n_{(n)}\bigr) \cdot \theta_{\mathrm{res}}
$$

*to leading order in $\theta_{\mathrm{res}}$.  The factor
$n_{(1^n)} - n_{(n)}$ is the difference of phase exponents on the
two extremal blocks; for kaons (multi-crossing $\mathcal{K}$) it
scales with the total crossing number, recovering the empirical
$\delta_{\mathrm{CP}} \sim n_c \theta_{\mathrm{res}}$ ansatz of
([CP violation](#sec:cp-violation-evidence)).*

**Sketch.**
Spectral completeness over $R_\mathbb{C}$ (the complexified analogue
of the real spectral completeness for $\alpha_{\mathrm{EM}}$) decomposes
$F_{\mathrm{Pauli}}$ into central-idempotent characters.  The
alternating block $V_{(1^n)}$ is the unique source of phase
asymmetry: its character carries $(-q)^{-w}$ on a writhe-$w$
crossing
([antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)),
while the symmetric block carries $q^w$.  The ratio's imaginary part
is therefore the CP-violating amplitude.

**Falsifiability.**
A direct prediction: amphicheiral knots have
$\delta_{\mathrm{CP}} = 0$ exactly.  Any observed CP violation in a
single amphicheiral hadron would falsify the spectral characterisation.
The kaon system ($K_L \to \pi\pi$ at $\sim 2 \times 10^{-3}$,
non-amphicheiral $\bar{u}s$ configuration) is the empirical test
case.

*Remark.* This conjecture is downstream of
([complex chirality rotation](#conj:complex-chirality-rotation)),
which is itself conjectural.  Promotion to a proposition requires:
(a) a categorical proof that $R_\mathbb{C}$-enrichment is the
unique CP-violating extension, (b) a quantitative match between
$\theta_{\mathrm{res}}$ and the Wolfenstein parametrisation of the
CKM matrix.

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
