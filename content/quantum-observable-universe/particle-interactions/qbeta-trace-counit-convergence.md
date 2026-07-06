**Conjecture (trace–counit convergence).**
*The per-braid Markov-trace nucleon mass difference $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$, summed over the brane tower, equals the Frobenius-counit $Q$-value $\varepsilon(\Delta)\cdot\mathfrak{E}_0$ of [`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form):*
$$
  \mathfrak{m}(n) - \mathfrak{m}(p) - m_e
  \;=\;
  \varepsilon(\Delta)\cdot\mathfrak{E}_0
  \;=\;
  \frac{m_e\,(q+1)(q^2 - 2q - 1)}{2q^3}.
$$
*The two sides represent evaluations through two canonical functionals on $H_3(q)$: the static-mass Markov trace $\mathrm{tr}_M$ (pairing with the unit) and the transition counit $\varepsilon$ (pairing with the integral $\omega = G^{-1}\mathbf{1}$). The conjecture posits their equality.*

## Formalization

We axiomatize this conjecture as the Lean class `QOU.Interactions.QBetaConvergence.QBetaTraceCounitConvergence`. The `counitForm_eq` field records the proven closed form ([`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form), `Qbeta_closed`), and the `converges` field carries the conjectural identity. Given this class, the conditional corollary `qbeta_is_trace_mass_difference` proves that the physical trace mass difference equals the counit closed form. The class instance is the only unproved input.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-valued physical observables, real-analytic bounds, transcendental constants, and numerical evaluation at the substrate parameter $q_0$. Any generic categorical identities remain valid over an abstract coefficient ring; we specialise only their archimedean realisation here.
