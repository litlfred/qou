**Proposition (closed form of the counit $Q$-value).**
Let $\Delta = \mathrm{NF}(n) - \mathrm{NF}(p)$ be the single-wrap
normal-form difference of the neutron and proton typed-crossing
elements in $H_3(q)$, and write $h = q - q^{-1}$. Let
$\varepsilon$ denote the Frobenius counit (the unweighted sum of
normal-form coefficients) and $\mathfrak{E}_0 = m_e/(q(q-1))$ the
per-Hecke-step energy scale ([energy scale](#rem:energy-scale-planck)).
Then

$$
  \varepsilon(\Delta)\cdot\mathfrak{E}_0
  \;=\;
  \frac{m_e\,(q+1)(q^2 - 2q - 1)}{2q^3}.
$$

## Counit versus Markov trace

The normal-form difference is supported on the identity and the two
crossing generators,
$\Delta = \bigl[\tfrac{h^2}{2},\,-\tfrac{h}{2},\,-\tfrac{h}{2},\,0,\,0,\,0\bigr]$
in the basis $[\gamma,\sigma_0,\sigma_1,L_+,L_-,e^-]$ — the
leading $L_+$ content cancels between the two nucleons. Two
canonical functionals act on this difference:

$$
  \varepsilon(\Delta) = \frac{h^2}{2} - h,
  \qquad
  \mathrm{tr}_M(\Delta) = \frac{h^2}{2} - h\,z,
$$

where $z$ is the Markov–Jones loop parameter and the identity
$\gamma = \mathbf{1}$ carries Markov weight $\mathrm{tr}_M(\mathbf{1}) = 1$.
The counit is the Markov trace at the trivial loop value: the two
agree precisely when $z = 1$, and otherwise differ by

$$
  \varepsilon(\Delta) - \mathrm{tr}_M(\Delta) = h\,(z - 1).
$$

For $h \neq 0$, equality holds if and only if $z = 1$. Since
$z = 1/(\sqrt q + 1/\sqrt q) \le \tfrac12$ for real $q > 0$, the
trivial-loop value is never attained on the substrate; the counit
and the Markov trace are genuinely distinct functionals there.

## Factorization of the energy scale

The per-Hecke-step energy factors through the information speed
$c_q^2 = 1/(q-1)^2$ and the action-per-tick $\hbar_q^{E} = (q-1)/q$:

$$
  \mathfrak{E}_0
  =
  m_e\,c_q^2\,\hbar_q^{E}
  =
  \frac{m_e}{(q-1)^2}\cdot\frac{q-1}{q}
  =
  \frac{m_e}{q(q-1)}.
$$

(Here $\hbar_q^{E} = (q-1)/q$ is the energy-scale action quantum,
distinct from the Hecke parameter $h = q - q^{-1}$.)

## Lean formalization

The algebraic content is verified over an arbitrary field, free of
$\mathrm{sorry}$. The functional comparison
($\varepsilon = \mathrm{tr}_M$ at $z = 1$, the gap $h(z-1)$, and the
equality criterion) is `QOU.Interactions.QBetaCounitTrace`; the
energy-scale factorization `E0_eq` and the closed form
`Qbeta_closed` are `QOU.Interactions.QBetaEnergyScale`.
