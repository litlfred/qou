**Remark.**
*[Prop:confinement-phase-stratification](#prop:confinement-phase-stratification) is the scope caveat attached to every statement in the confinement framework. Any formal statement about a [confined particle](#def:confined-particle) $P$, its electron shell, a [dressing morphism](#def:dressed-particle) $\mathrm{dress}_S$, or a trace-class invariant $\mathcal{F}(P)$ includes the implicit quantifier:*

$$
  \forall\, q \in \Omega_\alpha(P),
$$

*where $\Omega_\alpha(P)$ is a fixed connected component of the confinement locus $\Omega(P)$ — a single confinement phase.*

**Phase-scoped theorems (these hold only within a single $\Omega_\alpha$):**

- *[prop:level-sufficiency](#prop:level-sufficiency) — preservation of Markov trace under unfolding.*
- *[prop:shell-closure-stability](#prop:shell-closure-stability) — monotonicity of $\sigma_F$ along the dressing chain and local maxima at noble-gas $Z$.*
- *Functoriality of $\mathrm{tr}_M: \mathbf{Conf} \to \mathbb{C}(q)$ ([confinement category](#def:confinement-category)).*
- *Multi-operator binding structure (electron shell) — constancy of the active support $\mathcal{S}^*(S, q)$.*

**Boundary phenomena — not covered by within-phase theorems:**

- ***Deconfinement events.*** *At $q \in \partial\Omega(P)$ with Slater-strict feasibility lost, $P$ ceases to be realisable as a closed-braid bound state; the archetype is the [deconfinement threshold](#rem:deconfinement-golden-threshold).*
- ***Regime switches.*** *At $q \in \partial\Omega(P)$ with a $\mu$-jump but preserved feasibility, the active support gains or loses a Wedderburn block; witnessed by [prop:parity-regime-selection](#thm:parity-regime-selection).*
- ***Critical scaling.*** *Near a phase boundary, $\sigma_F$ typically has a non-analytic limit. Scaling exponents and critical phenomena require separate analysis (see [phase-transition interpretation](#rem:phase-transition-interpretation)).*
- ***Chemical and nuclear rearrangements.*** *Transitions between disconnected components of $\Omega(P)$ for a composite $P$ are realised physically as structural rearrangements — $\mathrm{sp}^3 \leftrightarrow \mathrm{sp}^2$ hybridisations, isomerisations, $\alpha$-decay channel openings. These transitions require an explicit cross-component analysis using the stratification of $\Omega(P)$.*

**Practical reading.**
*When encountering a confinement-framework statement, treat $q$ as ranging over a fixed open phase unless the text addresses boundary behaviour. Numerical witnesses evaluate at a single $q = q_0 \approx 1.110$. As long as that point lies in $\Omega_\alpha(P)$, all within-phase theorems apply. Auditing behaviour across $q$ ranges requires explicit stratification analysis.*
