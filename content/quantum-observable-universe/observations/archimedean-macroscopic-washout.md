**Why bounded observers see continuous q-Gaussian distributions on
a deterministic substrate.** A macroscopic observer is bounded by the
operational-entropy limit $\eta_q = (2q-1)/q^3$ and cannot resolve
individual Reeb ticks; her measurement of an observable $\Phi$ is an
$n$-step auto-correlated sum
$\mathcal{O}_{\mathrm{macro}}(\Phi) = n^{-1} \sum_{i=1}^n
\mathrm{tr}_M(\sigma_{j_i}(\Phi))$ over the unresolved ticks within
her observation window (typically $n \sim 10^{20}$ per nanosecond).
By the q-CLT
([conj:q-clt-non-commutative](#conj:q-clt-non-commutative)),
the rescaled centred sum converges in joint moments to the q-Gaussian
$G_{q_0}(t, x)$ peaked at $\mathrm{tr}_M(\Phi)$ with width
$\sqrt{\kappa_2^{(q)}/n}$. The observer therefore registers a
q-Gaussian bell curve, not the underlying delta-function expectation.

**Why q-Gaussian rather than Gaussian.** The braid relations
$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$
are global correlations across the entire braid: every generator
talks to every other through the Hecke algebra structure. The
classical CLT (Gaussian attractor) requires asymptotic independence;
the QOU substrate violates this maximally. By Marsh–Fuentes–Moyano–
Tsallis [`marsh2006`], systems with such global correlations have
q-Gaussian attractors, not Gaussian — with the deformation parameter
of the limit equal to the substrate's $q$. At $q_0 \approx 1.110$,
the substrate's q-Gaussian width differs from a classical Gaussian
of the same variance at $O(10^{-3})$ in the tails — falsifiable in
next-generation precision experiments.

This resolves the apparent paradox between deterministic algebraic
dynamics and probabilistic-looking macroscopic data: the
probabilistic appearance is the CLT attractor of the substrate, not
a stochastic-mechanical postulate.
