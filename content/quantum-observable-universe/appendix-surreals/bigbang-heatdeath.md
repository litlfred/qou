The QOU framework is parameter-time-symmetric. The substrate $q \in \mathbb{R}_{>0}$ controls all dimensionful constants (speed of light $c_q = 1/(q-1)$, Planck constant $\hbar_q = (q-1)/q$), but it does not evolve in any preferred direction. A cosmological reading identifies $q$-flow with cosmic time $t$. This flow possesses two natural endpoints.

- **Big Bang.** $q \to 1^+$. Here, $c_q, c_q^2 \to \infty$. The speed of light diverges, all states become causally connected, and no time separation exists.
- **Heat death.** $q \to \infty$. Here, $\hbar_q \to 1$. The quantum scale of action saturates the classical scale of action, and no further quantum dynamics remain distinguishable.

Both endpoints are singular limits in the archimedean sense. The QOU structure constants diverge or saturate. Standard physics treats these as unattainable boundary conditions.

## Conjecture

The Big Bang and heat-death endpoints are not unattainable limits. They are the standard-part of an evaluation at specific named surreals.

For each $\varepsilon \in \mathbf{No}$ with $\varepsilon > 0$, let $\mathbf{QOU}_{1 + \varepsilon}$ be the surreal QOU at $q = 1 + \varepsilon$. Let

$$
  \mathbf{BigBang}_{1 + \varepsilon}
   := \mathrm{St}_{\mathrm{QOU}}(\mathbf{QOU}_{1 + \varepsilon}).
$$

This is a functor from the infinitesimals (an ordered sub-monoid of $\mathbf{No}$) to archimedean QOUs.

1. **Big Bang as named-surreal evaluation.** We define a Big Bang functor $\mathbf{BigBang} := \mathbf{BigBang}_{1 + \varepsilon}\big|_{\varepsilon \to 0^+}$. This is not a topological limit but a named-surreal evaluation. We reach $\varepsilon \to 0^+$ in $\mathbf{No}$ by replacing $\varepsilon$ with decreasing infinitesimals $\varepsilon^2, \varepsilon^3, \ldots, \varepsilon^\omega$. The final functor evaluates at a specific transfinite surreal $\varepsilon^\omega$, composed with $\mathrm{St}$.
2. **Heat death as evaluation at $q = \omega$.** We define $\mathbf{HeatDeath} := \mathrm{St}_{\mathrm{QOU}}(\mathbf{QOU}_{q = \omega})$, which is the standard-part of QOU evaluated at the named infinite surreal $\omega$.
3. **Both functors are well-defined.** The QOU mass formula and $\mathcal{Q}$-value derivations are rational in $q$. They evaluate at any non-zero, non-pole element of $\mathbf{No}$, including the named endpoints. The functors land in well-defined archimedean QOUs. For $\mathbf{BigBang}$, we have $c \to \infty$ and $\hbar \to 0$. All particles are massless and all knots are equivalent. For $\mathbf{HeatDeath}$, we have $c \to$ finite and $\hbar \to 1$. Classical and quantum structures identify, halting further quantum evolution.
4. **Approximation by intermediate $\varepsilon$.** The standard-part of $\mathbf{QOU}_{1 + \varepsilon}$ for small archimedean $\varepsilon \in \mathbb{R}_{>0}$ approximates $\mathbf{BigBang}$ to leading order. This recovers classical early-universe perturbation theory. Each $\mathbf{BigBang}_{1 + \varepsilon}$ at finite real $\varepsilon$ quantifies deviation from the singular $\mathbf{BigBang}$ functor.

## Consequences of the conjecture

If this conjecture holds, the cosmological endpoints become objects in the category of archimedean QOUs rather than unattained limits.

1. **Singularity resolution.** The Big Bang singularity is not a place where physics breaks down. It is the standard-part of a well-defined surreal QOU.
2. **Approximation framework.** We compute physical observables near either endpoint by perturbing in $\varepsilon$ around the named-surreal evaluation. This recasts nonstandard analysis cosmologically.
3. **Functorial cosmology.** The cosmological-time evolution $t \mapsto \mathbf{QOU}_{q(t)}$ becomes a functor from surreal times to archimedean QOUs. The named endpoints are honest objects.

## Proof strategy

The mathematical kernel is well-defined. The remaining question is one of interpretation.

**Mathematical kernel** (provable now in Lean).

1. Show $\mathrm{QOU}_q$ is rational in $q$. Each structure constant lies in $\mathbb{Q}(q)$.
2. Show evaluation at any non-pole $q \in \mathbf{No}$ is well-defined. Use `QOU.AppendixSurreals.omegaSurreal` and `epsilonSurreal`.
3. Show $\mathrm{St}_{\mathrm{QOU}} \circ \mathrm{ev}_{q = \omega}$ and $\mathrm{St}_{\mathrm{QOU}} \circ \mathrm{ev}_{q = 1 + \varepsilon^\omega}$ produce well-defined archimedean QOUs (modulo [archimedean-stpart](#conj:archimedean-stpart)).

**Provable in Lean today.** We have already proved `c_q_eq_omega_at_one_plus_epsilon` in `QOU.AppendixSurreals.Conjectures`. The value $c_q = (q-1)^{-1}$ at $q = 1 + \varepsilon$ equals $\omega$.

**Required infrastructure** (interpretation).

- A definition of cosmological time as an ordering on $q \in \mathbf{No}$.
- A categorical-cosmology framework distinguishing a moment (a specific $q$) from an evolution (a path in $\mathbf{No}$).
- The main paper does not develop this framework.

**Falsification path** (mathematical). Show that the QOU structure constants have poles at $q = \omega$ or $q = 1$ in $\mathbf{No}$ that prevent evaluation. This contradicts the rational-in-$q$ formulas.

**Falsification path** (interpretive). Show that the cosmological time reading is incompatible with QOU's parameter-time symmetry (the substrate $q$ does not evolve). This is the most natural objection, and the appendix's caveat concedes it.

**Provability assessment.** The mathematical kernel is provable in Lean modulo the sub-conjectures. We deliberately bracket the cosmological interpretation as a separate matter.
