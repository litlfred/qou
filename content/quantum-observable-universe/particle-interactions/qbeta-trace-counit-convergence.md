**Conjecture (trace–counit convergence).**
The per-braid Markov-trace nucleon mass difference
$\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$, summed over the brane tower,
equals the Frobenius-counit $Q$-value
$\varepsilon(\Delta)\cdot\mathfrak{E}_0$ of
[`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form):

$$
  \mathfrak{m}(n) - \mathfrak{m}(p) - m_e
  \;=\;
  \varepsilon(\Delta)\cdot\mathfrak{E}_0
  \;=\;
  \frac{m_e\,(q+1)(q^2 - 2q - 1)}{2q^3}.
$$

The two sides represent evaluations through two
canonical functionals on $H_3(q)$ — the static-mass Markov trace
$\mathrm{tr}_M$ (pairing with the unit) and the transition counit
$\varepsilon$ (pairing with the integral $\omega = G^{-1}\mathbf{1}$).
The conjecture posits their equality.

## Formalization

The conjecture is axiomatized as the Lean class
`QOU.Interactions.QBetaConvergence.QBetaTraceCounitConvergence`: the
`counitForm_eq` field records the proved closed form
([`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form),
`Qbeta_closed`), and the `converges` field carries the conjectural
identity. Granting the class, the conditional corollary
`qbeta_is_trace_mass_difference` derives that the physical trace mass
difference equals the counit closed form; the lone unproved input is the
class instance.
