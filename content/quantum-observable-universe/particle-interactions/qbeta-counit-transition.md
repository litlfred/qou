The closed form ([`prop:qbeta-counit-closed-form`](#prop:qbeta-counit-closed-form)) clarifies the standing of the free-neutron relation $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})|\cdot\mathfrak{E}_0$ ([`prop:neutron-qvalue-symbolic`](#prop:neutron-qvalue-symbolic)). The relation uses the Frobenius counit $\varepsilon$, whereas the per-braid mass uses the Markov trace $\mathrm{tr}_M$. These are distinct canonical functionals on $H_3(q)$. They agree on the nucleon difference only at the trivial loop $z = 1$. The substrate never attains this value.

## Two functionals, two observables

Both functionals are the Frobenius pairing $\langle x, y\rangle_G = \mathrm{tr}_M(xy)$ evaluated against different distinguished elements. The Markov trace pairs against the unit, $\mathrm{tr}_M(\beta) = \langle\beta, \mathbf{1}\rangle_G$. This closed-loop reading computes the static mass of a particle. The counit pairs against the canonical integral $\omega = G^{-1}\mathbf{1}$, $\varepsilon(\beta) = \langle\beta, \omega\rangle_G$. This crossing-stripped reading counts the net reduction content.

A static mass is a closed loop, read by $\mathrm{tr}_M$. A $\beta$-decay is a transition: the nucleon braid reduces, with one crossing re-typed under $d \to u$. The energy of a reduction is the number of reduction steps multiplied by the energy per step. The per-Hecke-step energy is exactly $\mathfrak{E}_0$ ([energy scale](#rem:energy-scale-planck)). The counit form:
$$
  \mathfrak{Q}_\beta = \varepsilon(\Delta)\cdot\mathfrak{E}_0
$$
is therefore the natural transition observable. The Markov trace (the loop observable) is the incorrect functional for a transition. When evaluated with $\mathrm{tr}_M$ instead of $\varepsilon$, the predicted $Q$-value falls short of the measured value by roughly a factor of two. When evaluated with the counit, it matches to $+0.17\%$.

## Agreement with the measured value

The $+0.17\%$ residual corresponds to the $N=0$ brane-tower truncation. This is the same residual that separates the derived energy scale $\mathfrak{E}_0 \approx 4.186$ MeV from its calibration cross-check $\approx 4.155$ MeV ([energy scale](#rem:energy-scale-planck)). The counit form and the Markov-trace mass difference $\mathfrak{m}(n) - \mathfrak{m}(p) - m_e$ compute the same physical observable in two ways. Their coincidence at the $N=0$ order demonstrates consistency between two canonical functionals, rather than a curve fit. A fully tower-summed derivation, which establishes that the trace mass difference converges to $\varepsilon(\Delta)\cdot\mathfrak{E}_0$ with the $+0.17\%$ serving as its remainder, remains open.
