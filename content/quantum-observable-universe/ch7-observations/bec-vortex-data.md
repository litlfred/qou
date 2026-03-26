Bose--Einstein condensates (BECs) provide the cleanest
experimental realisation of quantised vortex dynamics.  The
data summarised here tests and constrains the $q$-deformed
vortex spectrum of
[Proposition](#prop:discrete-vortex-spectrum).

**1. Quantised circulation.**
In ${}^{87}\mathrm{Rb}$ and ${}^{23}\mathrm{Na}$ BECs,
vortex circulation is measured to be $\Gamma_n = n \cdot h/m$,
with $n$ an integer \cite{madison2000}.  No intermediate values
have ever been observed.  In the QOU framework this is the
$q \to 1$ limit of the $\mathrm{SU}_q(2)$ Casimir
quantisation: the spin label $j$ reduces to the winding number
$n$, and $[j]_q[j+1]_q \to j(j+1) = n(n+1)$ gives the
discrete circulation levels.  The BEC data confirms the
**selection rule** $|\Delta n| = 1$ predicted by the
ladder-mode transition mechanism.

**2. Vortex lattice formation.**
Above a critical rotation frequency $\Omega_c$, BECs nucleate
regular lattices of singly-quantised vortices
\cite{abo-shaeer2001}.  The number of vortices follows the
Feynman rule $N_v = m \Omega A / (\pi\hbar)$, where $A$ is
the condensate area.  In the $q$-deformed brane fluid, the
Feynman rule generalises to

$$
  N_v^{(q)} \;=\;
  \frac{m_q \,\Omega \, A_q}{\pi \hbar_q}
  \;=\; \frac{\Omega \, A_q}{\pi}\,
  \frac{[1]_q}{[1]_q} \;=\; N_v \cdot
  \frac{A_q}{A}\,\frac{\hbar}{\hbar_q},
$$

so that deviations from the classical Feynman count are
controlled by the ratio $\hbar/\hbar_q$.  For laboratory BECs
($q \approx 1 + 10^{-38}$), this correction is immeasurably
small, consistent with observation.

**3. Kelvin-mode excitations.**
Bretin et al. \cite{bretin2003} observed quadrupole
oscillations of a single vortex in a ${}^{87}\mathrm{Rb}$
condensate, identified as the lowest Kelvin mode ($k = 1$).
The measured frequency $\omega_1^{\text{exp}} = 2\pi \times
(6.2 \pm 0.1)$ Hz matches the Kelvin dispersion relation.
The $q$-deformed prediction replaces $k^2$ with
$[k]_q^2 = [1]_q^2 = 1 + O((q-1)^2)$, again indistinguishable
from the classical value at laboratory $q$.

The higher Kelvin modes ($k = 2, 3, \ldots$) have been observed
in numerical simulations and are consistent with the
$q$-integer spacing.  A precision measurement of the
$k$-dependence of the Kelvin spectrum could detect
$q$-deformation through the deviation

$$
  \frac{\omega_k^{(q)}}{\omega_1^{(q)}}
  \;=\; \frac{[k]_q^2}{[1]_q^2}
  \;=\; k^2 + \frac{k^2(k^2-1)}{3}(q-1)^2 + O((q-1)^4),
$$

which grows as $k^4$ for large mode number.  Higher Kelvin
modes are exponentially more sensitive to $q$-deformation.

**4. Vortex clustering and turbulence.**
Gauthier et al. \cite{gauthier2019} observed giant vortex
clusters in 2D ${}^{87}\mathrm{Rb}$ condensates, where
same-sign vortices aggregate into macroscopic circulation
structures.  The cluster circulation is quantised in multiples
of the single-vortex quantum, directly demonstrating the
additive structure $j_{\text{cluster}} = j_1 + j_2 + \cdots$.
In the $q$-deformed framework, cluster formation corresponds to
the tensor product of $\mathrm{SU}_q(2)$ representations:
the total spin $j_{\text{total}}$ follows the
Clebsch--Gordan decomposition of $\mathrm{SU}_q(2)$, with
fusion rules that differ from $\mathrm{SU}(2)$ at
$q \neq 1$.

**5. Box-trapped condensates.**
Recent advances in uniform-potential BECs \cite{navon2021}
allow measurements in homogeneous geometry, eliminating
confining-potential artefacts.  This provides the closest
laboratory analogue to the flat brane fluid of
[§Fluid Dynamics of the Brane](#sec:brane-fluid).

**Summary of experimental constraints.**

| Observable | Measured value | $q$-deformed prediction | Sensitivity to $q-1$ |
|---|---|---|---|
| Circulation quantum | $h/m$ ($n=1$ only) | $[1]_q \cdot h_q/m_q$ | $O((q-1)^2)$ |
| Vortex lattice count | Feynman rule $N_v$ | $N_v^{(q)}$ | $O(q-1)$ via $\hbar_q$ |
| Kelvin $k=1$ frequency | $2\pi \times 6.2$ Hz | $\omega_1^{(q)}$ | $O((q-1)^2)$ |
| Kelvin ratio $\omega_k/\omega_1$ | $k^2$ (low $k$) | $[k]_q^2/[1]_q^2$ | $O(k^4(q-1)^2)$ |
| Cluster circulation | integer multiples of $h/m$ | $\mathrm{SU}_q(2)$ Clebsch--Gordan | Fusion rule deviations |

**Proposed tests and current limits.**

*Kelvin-mode ratios.*  The ratio $\omega_k/\omega_1$ is in
principle the most sensitive probe, since the $q$-correction
grows as $k^4(q-1)^2$.  In practice, only the $k = 1$ mode has
been cleanly resolved \cite{bretin2003}; higher modes are
strongly damped ($\gamma_k \propto k^2$) and have wavelengths
approaching the healing length $\xi$, where the
thin-filament approximation breaks down.  Reaching $k = 2$--$3$
with sub-percent frequency resolution would already improve
sensitivity over circulation-quantum measurements by an order
of magnitude, but this remains technically challenging.

*Vortex lattice statistics.*  A more accessible route exploits
the large number of vortices in a lattice.  The inter-vortex
spacing $b = (\hbar / m\Omega)^{1/2}$ depends on
$\hbar_q$ through the $q$-Feynman rule; statistical analysis of
lattice images \cite{abo-shaeer2001} in box-trapped condensates
\cite{navon2021} could constrain $|q - 1|$ at the level of the
imaging resolution ($\sim 1\,\mu$m), yielding bounds of order
$|q - 1| < 10^{-3}$ from $\sim 10^2$ vortices.

*Vortex cluster fusion rules.*  The $\mathrm{SU}_q(2)$
Clebsch--Gordan decomposition predicts small deviations in the
allowed angular momenta of merged vortex clusters.  Two
$j = 1$ clusters should fuse to $j = 0, 1, 2$; at
$q \neq 1$ the relative branching ratios shift.  The
2D turbulence experiments of \cite{gauthier2019} already
resolve cluster charges up to $|n| \sim 10$, and could test
fusion statistics if run with controlled pair-merging
protocols.

*Honest assessment.*  All three tests probe $q - 1$ at levels
far above the Planck-scale value expected from the
[Planck--Reynolds correspondence](#sec:planck-reynolds).
Their value is not in detecting $q$-deformation directly, but
in (a) confirming that the $q \to 1$ limit of the
$\mathrm{SU}_q(2)$ vortex spectrum correctly reproduces BEC
phenomenology, and (b) establishing upper bounds on
$|q - 1|$ in a controlled laboratory system.

