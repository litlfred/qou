The closed form
[`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form)
clarifies the standing of the free-neutron relation
$Q_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$
([`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic)).
The relation uses the Frobenius counit $\varepsilon$, whereas the
per-braid mass is built on the Markov trace $\mathrm{tr}_M$. These
are not interchangeable: they are distinct canonical functionals on
$H_3(q)$, agreeing on the nucleon difference only at the trivial loop
$z = 1$, which the substrate never attains.

## Two functionals, two observables

Both functionals are the Frobenius pairing
$\langle x, y\rangle_G = \mathrm{tr}_M(xy)$ against different
distinguished elements. The Markov trace pairs against the unit,
$\mathrm{tr}_M(\beta) = \langle\beta, \mathbf{1}\rangle_G$ — the
closed-loop reading, which is the static mass of a particle. The
counit pairs against the canonical integral $\omega = G^{-1}\mathbf{1}$,
$\varepsilon(\beta) = \langle\beta, \omega\rangle_G$ — the
crossing-stripped reading, which counts net reduction content.

A static mass is a closed loop, so it is read by $\mathrm{tr}_M$. A
$\beta$-decay is a transition: the nucleon braid is reduced, with one
crossing re-typed under $d \to u$. The energy of a reduction is the
number of reduction steps times the energy per step, and the
per-Hecke-step energy is exactly $\mathfrak{E}_0$
([energy scale](#rem:energy-scale-planck)). The counit form

$$
  Q_\beta = \varepsilon(\Delta)\cdot\mathfrak{E}_0
$$

is therefore the natural transition observable, while the Markov
trace — the loop observable — is the wrong functional for a
transition. Evaluated with $\mathrm{tr}_M$ in place of $\varepsilon$,
the predicted $Q$-value falls short of the measured value by roughly a
factor of two; evaluated with the counit, it matches to $+0.17\%$.

## Status of the agreement

The $+0.17\%$ residual is the $N=0$ brane-tower truncation, the same
residual that separates the derived energy scale
$\mathfrak{E}_0 \approx 4.186$ MeV from its calibration cross-check
$\approx 4.155$ MeV ([energy scale](#rem:energy-scale-planck)). The
counit form and the Markov-trace mass difference
$\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$ are the same physical
observable computed two ways; their coincidence to $N=0$ order is a
consistency between two named functionals rather than a fit. A fully
tower-summed derivation — establishing that the trace mass difference
converges to $\varepsilon(\Delta)\cdot\mathfrak{E}_0$ with the
$+0.17\%$ as its remainder — remains open.
