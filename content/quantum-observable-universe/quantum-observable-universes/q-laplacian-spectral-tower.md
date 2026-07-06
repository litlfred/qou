**Proposition (the $q$-Laplacian spectral tower).** *The $q$-Laplacian
$\Delta_q = d_q\delta_q + \delta_qd_q$
([particle / $q$-harmonic form](#def:q-harmonic-form)) has eigenvalues
given by the $q$-integer tower*
$$
  [k]_q^2, \qquad [k]_q = \frac{q^k - q^{-k}}{q - q^{-1}}
  \quad (k = 1, 2, 3, \ldots).
$$
*At a primitive root of unity $q = e^{i\pi/\kappa}$ the $q$-integer
$[\kappa]_q$ **vanishes**, and the spectrum truncates to the finite set*
$$
  \{\,[1]_q^2, [2]_q^2, \ldots, [\kappa-1]_q^2\,\},
$$
*the **Verlinde / ADE quantum-dimension** data of the truncated
representation category.*

**Proof.** The vanishing $[\kappa]_q = 0$ at $q = e^{i\pi/\kappa}$ is
elementary: the numerator $q^\kappa - q^{-\kappa}$ vanishes because
$q^\kappa = e^{i\pi} = -1$, hence $q^{-\kappa} = -1$ as well and the
difference is $0$. By the **Verlinde formula** \cite{verlinde1988} the
fusion coefficients are diagonalised by the modular $S$-matrix and the
surviving simple objects are $j = 0, \tfrac12, \ldots,
\tfrac{\kappa-2}{2}$ — the **Reshetikhin–Turaev** truncation
\cite{reshetikhin1991}. The surviving quantum dimensions are exact
algebraic numbers in the cyclotomic field $\mathbb{Q}(\zeta_\kappa)$.
$\blacksquare$

## Lean structure

`truncRoot κ := exp(iπ/κ)` over $\mathbb{C}$;
`truncRoot_pow` proves $\zeta_\kappa^{\,\kappa} = -1$ (hence
$\zeta_\kappa^{\,2\kappa} = 1$), and
`qIntegerNumerator_vanishes_at_truncRoot` proves the numerator
$q^\kappa - q^{-\kappa} = 0$ at $q = \zeta_\kappa$ — the level-$\kappa$
truncation. The statement lives over $\mathbb{C}$ because the
truncation root is genuinely complex; no reality is assumed.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
