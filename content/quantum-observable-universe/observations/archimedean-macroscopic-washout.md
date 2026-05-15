**Why bounded observers see continuous distributions on a
deterministic substrate.** The QOU algebraic substrate is strictly
deterministic — Gröbner–Shirshov reduction on the Hecke algebra
gives unique normal forms; the Reeb flow ticks at discrete Planck
intervals; the Markov trace is a single $R$-valued functional, not
a probability distribution. Yet macroscopic experiments register
continuous distributions for nearly every observable (interference
fringes, decay-rate Gaussians, momentum spectra). The non-commutative
q-CLT
([q-CLT for Hecke transfer matrices](#conj:q-clt-non-commutative))
explains why.

**The mechanism.** A macroscopic observer is bounded by the
operational-entropy limit $\eta_q = (2q-1)/q^3$
(notation register). She cannot resolve individual Reeb ticks,
since each tick lies below the entropy resolution threshold. Her
measurement of a knot-state observable $\Phi$ is therefore not
$\mathrm{tr}_M(\Phi)$ at one instant, but a $n$-step
auto-correlated sum
$$
  \mathcal{O}_{\mathrm{macro}}(\Phi)
  \;=\;
  \frac{1}{n} \sum_{i=1}^{n}
    \mathrm{tr}_M\bigl(\sigma_{j_i}(\Phi)\bigr)
$$
where the $\sigma_{j_i}$ are the Hecke transfer matrices applied
during her observation interval and $n$ is the number of unresolved
Reeb ticks within that interval (typically $n \sim 10^{20}$ ticks
per nanosecond).

**Why the bell curve.** Under the q-CLT, the rescaled centred sum
$\sqrt{n}\bigl(\mathcal{O}_{\mathrm{macro}}(\Phi) -
\mathrm{tr}_M(\Phi)\bigr)$
converges in joint moments to a non-commutative q-Gaussian process.
The classical-limit interpretation: the observer sees not
$\mathrm{tr}_M(\Phi)$ exactly, but a measurement value drawn from
the q-Gaussian distribution
$$
  P(\mathcal{O} = x)
  \;\propto\;
  \exp_q\!\left(
    -\,\frac{\bigl(x - \mathrm{tr}_M(\Phi)\bigr)^2}
            {2\,\kappa_2^{(q)} / n}
  \right),
$$
peaked at the algebraic expectation $\mathrm{tr}_M(\Phi)$ with
width controlled by the second free q-cumulant $\kappa_2^{(q)}$
and the sample size $n$. For $n \to \infty$ the peak becomes
arbitrarily sharp; for finite $n$ the observer sees a q-Gaussian
bell curve.

**Why q-Gaussian rather than Gaussian.** The Marsh–Fuentes–Moyano–
Tsallis theorem [`marsh2006`] is the structural reason. The braid
relations
$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$
introduce *global correlations* across the entire braid — every
generator affects every other through the GS normal-form reduction.
Marsh et al. proved that for systems with such global correlations,
the central-limit attractor is the q-Gaussian, not the classical
Gaussian. The classical CLT (with Gaussian attractor) requires
asymptotic independence of summands; the QOU substrate violates this
maximally — every $\sigma_i$ talks to every $\sigma_j$ via the
non-trivial braid algebra. The q-Gaussian is the unique attractor
compatible with this global correlation structure.

**Bridge to non-extensive statistical mechanics.** Tsallis's
non-extensive entropy
$S_q = (1 - \sum p_i^q)/(q - 1)$
is the entropy functional under which the q-Gaussian is the maximum-
entropy distribution at fixed variance. The QOU substrate parameter
$q_0 \approx 1.110$ places the substrate firmly in the Tsallis
non-extensive regime; the operational entropy $\eta_q$ in QOU's
notation is precisely Tsallis's $S_q$ form. The QOU framework
therefore *predicts* that macroscopic observables follow q-Gaussian
rather than Gaussian statistics, with the q-parameter determined by
the substrate.

**Falsifiability marker.** This is testable. Any precision measurement
of a single observable's distribution should reveal a q-Gaussian
shape with $q = q_0 \approx 1.110$. Deviations from a pure Gaussian
in tails of decay-rate distributions, scattering cross-sections, or
interference-fringe widths are predicted; at current precision they
are within experimental noise, but next-generation cold-atom and
nuclear-decay experiments can distinguish $q = 1$ (Gaussian) from
$q = q_0 \approx 1.11$ (q-Gaussian) at the $10^{-3}$ level.

**Resolution of issue #649 §2.** The expository question — why does
macroscopic measurement of a deterministic substrate yield a smooth
continuous distribution — is answered by the combination of the
q-CLT
([conj:q-clt-non-commutative](#conj:q-clt-non-commutative))
and the operational-entropy bound. The macroscopic wash-out is
neither stochastic-mechanical noise nor Born-rule probability; it
is the central-limit attractor of the non-commutative probability
space, evaluated against an observer with finite operational
resolution.
