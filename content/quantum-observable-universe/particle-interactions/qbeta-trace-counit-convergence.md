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

The two sides are the same physical observable evaluated through two
canonical functionals on $H_3(q)$ — the static-mass Markov trace
$\mathrm{tr}_M$ (pairing with the unit) and the transition counit
$\varepsilon$ (pairing with the integral $\omega = G^{-1}\mathbf{1}$) —
so their equality is required for consistency.

## Why the convergence is non-perturbative

The equality is not a small-correction limit. At the substrate the
single Markov-trace term already misses the target by a wide margin:
the $N=0$ contribution $\lvert\mathrm{tr}_M(\Delta)\rvert\cdot\mathfrak{E}_0
\approx 0.49$ MeV falls short of $\mathfrak{Q}_\beta \approx 0.78$ MeV, a deficit of
roughly $259\%$ of the leading term. The Markov trace and the counit
differ at leading order by $\varepsilon(\Delta) - \mathrm{tr}_M(\Delta)
= h\,(z-1)$, which the substrate loop $z = 1/(\sqrt q + 1/\sqrt q)$ does
not render small. The counit form, by contrast, matches to $+0.17\%$ at
$N=0$ — the same residual that separates the derived energy scale
$\mathfrak{E}_0 \approx 4.186$ MeV from its calibration cross-check
$\approx 4.155$ MeV ([energy scale](#rem:energy-scale-planck)).

The conjecture therefore asserts a **functional-consistency identity**:
the tower-summed Markov-trace difference reorganizes onto the counit
form, with the $+0.17\%$ as the brane-tower remainder. A perturbative
expansion of the trace tower about its $N=0$ term does not establish it,
because the corrections exceed the leading term; what is required is a
closed evaluation of the tower-summed difference.

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
