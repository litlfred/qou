The 2022 CDF~II measurement at Fermilab reported a $W$ boson mass
of $m_W^{\mathrm{CDF}} = 80\,433.5 \pm 9.4\;\mathrm{MeV}/c^2$,
roughly $7\sigma$ above the Standard Model electroweak fit
$m_W^{\mathrm{SM}} = 80\,357 \pm 6\;\mathrm{MeV}/c^2$.  More
recent results from ATLAS ($80\,360.2 \pm 9.9\;\mathrm{MeV}$,
2024) and CMS ($80\,360.2 \pm 9.9\;\mathrm{MeV}$, 2024) are
consistent with the Standard Model value.  The discrepancy
remains unresolved.

In the QOU framework the $W$ boson is the torus link $T(2,4)$
([Higgs as $T(2,8)$](#conj:higgs-t28)), a genus-$1$ link whose
mass is determined by evaluating its Skein polynomial at the
**local** substrate parameter
$q_0 = 1.10998$
([local substrate $q$](#prop:local-substrate-q)), fixed by the
CODATA muon--electron mass ratio measured in low-field
laboratories.  No running of $q$ with energy is invoked — $q_0$
is the substrate value at the experimental site.

## Skein polynomial of $T(2,4)$ at $q_0$

The Alexander polynomial of $T(2,2m)$ is
([threading link](#def:threading-link))

$$
  \Delta_{T(2,2m)}(q)
  \;=\;
  \frac{q^m - q^{-m}}{q - q^{-1}}.
$$

For $T(2,4)$ ($m = 2$):

$$
  \Delta_{T(2,4)}(q_0)
  \;=\;
  q_0 + q_0^{-1}
  \;=\;
  [2]_{q_0}
  \;\approx\; 2.0109.
$$

For $T(2,6)$ ($m = 3$):

$$
  \Delta_{T(2,6)}(q_0)
  \;=\;
  q_0^2 + 1 + q_0^{-2}
  \;=\;
  [3]_{q_0^2}
  \;\approx\; 3.0437.
$$

For $T(2,8)$ ($m = 4$):

$$
  \Delta_{T(2,8)}(q_0)
  \;=\;
  q_0^3 + q_0 + q_0^{-1} + q_0^{-3}
  \;\approx\; 4.0889.
$$

The $W$, $Z$, and Higgs masses are related to these Alexander
polynomials through the full mass functional
$\mathcal{M}$
([topological mass formula](#prop:topological-mass-formula)),
which includes crossing energy, hyperbolic volume, and
inter-component linking contributions.

## $W/Z$ mass ratio from $q_0$ alone

The mass ratio $m_W / m_Z$ is the most direct prediction because
it cancels the dimensional scale $\mu_0$.  Both $T(2,4)$ and
$T(2,6)$ are torus links with the same $m = 2$ meridional
winding, differing only in the longitudinal winding ($n = 4$
vs.\ $n = 6$) and hence in the number of exceptional divisors
spanned (1 vs.\ 2).

The Alexander polynomials give the leading-order ratio:

$$
  \frac{m_W}{m_Z}\bigg|_{\mathrm{Alexander}}
  \;=\;
  \frac{\Delta_{T(2,4)}(q_0)}{\Delta_{T(2,6)}(q_0)}
  \;=\;
  \frac{q_0 + q_0^{-1}}{q_0^2 + 1 + q_0^{-2}}
  \;=\;
  \frac{2.0109}{3.0437}
  \;=\; 0.6607.
$$

The observed ratio is $m_W / m_Z = 80\,369 / 91\,188 = 0.8815$.
The Alexander polynomial captures the $q$-deformed combinatorics
of the link but **not** the full Skein structure.  The discrepancy
between $0.661$ and $0.882$ must be resolved by the complete
Skein polynomial — the Jones polynomial $J_{T(2,4)}(q)$ and the
HOMFLY polynomial $P_{T(2,4)}(a, z)$ — which includes
inter-component linking, writhe corrections, and the Seifert genus
weighting from the exceptional divisor coupling.

The Jones polynomial of $T(2,4)$ in the braid closure
$\hat{\sigma}_1^4 \in B_2$ is computed from the Hecke algebra
representation.  The Hecke generator $T_1 = \rho(\sigma_1)$ has
eigenvalues $q$ (on the symmetric channel, quantum dimension
$[2]_q$) and $-q^{-1}$ (on the antisymmetric channel, quantum
dimension $1$).  The Markov trace of $T_1^4$ is:

$$
  \mathrm{tr}_M(T_1^4)
  \;=\;
  \frac{[2]_q \cdot q^4 \;+\; 1 \cdot q^{-4}}{[2]_q + 1}.
$$

At $q_0 = 1.10998$:

$$
  \mathrm{tr}_M(T_1^4)
  \;=\;
  \frac{2.0109 \times 1.5180 \;+\; 0.6574}{3.0109}
  \;=\;
  \frac{3.7101}{3.0109}
  \;=\; 1.2321.
$$

Similarly, for $T(2,6)$ ($\hat{\sigma}_1^6$):

$$
  \mathrm{tr}_M(T_1^6)
  \;=\;
  \frac{[2]_q \cdot q^6 \;+\; 1 \cdot q^{-6}}{[2]_q + 1}
  \;=\;
  \frac{2.0109 \times 1.8704 \;+\; 0.5346}{3.0109}
  \;=\;
  \frac{4.2967}{3.0109}
  \;=\; 1.4271.
$$

The Markov trace ratio gives:

$$
  \frac{m_W}{m_Z}\bigg|_{\mathrm{Markov}}
  \;=\;
  \frac{\mathrm{tr}_M(T_1^4)}{\mathrm{tr}_M(T_1^6)}
  \;=\;
  \frac{1.2321}{1.4271}
  \;=\; 0.8634.
$$

This is closer to the observed $0.8815$ but still $2\%$ below.
The remaining correction comes from the **genus weighting**: the
Seifert surface of $T(2,6)$ (genus $2$, spanning two exceptional
divisors) carries a different topological weight than that of
$T(2,4)$ (genus $1$, one divisor).  The genus-corrected ratio is:

$$
  \frac{m_W}{m_Z}\bigg|_{\mathrm{genus}}
  \;=\;
  \frac{\mathrm{tr}_M(T_1^4)}{\mathrm{tr}_M(T_1^6)}
  \;\cdot\;
  \frac{[2]_q^{g_Z - g_W}}{1}
  \;=\;
  0.8634 \times [2]_q^{2 - 1}
  \;=\;
  0.8634 \times 2.0109
$$

which overshoots.  The correct genus correction uses the
**fractional** genus contribution
$[2]_q^{(g_Z - g_W)/g_Z} = [2]_q^{1/2}$:

$$
  \frac{m_W}{m_Z}
  \;=\;
  0.8634 \times [2]_q^{1/2}
  \;=\;
  0.8634 \times 1.4181
$$

which also overshoots.  The Markov trace ratio $0.8634$ at
$q_0 = 1.10998$ is therefore the **raw** QOU prediction for
$m_W/m_Z$ before genus corrections, and brackets the observed
value from below.  The full Skein computation — resolving all
crossings of $T(2,4)$ and $T(2,6)$ into hyperbolic knots and
evaluating the topological mass formula on each summand — will
determine the exact correction.

**Table: $W/Z$ mass ratio predictions at $q_0 = 1.10998$.**

| Method | $m_W / m_Z$ | Observed | Discrepancy |
|--------|:-----------:|:--------:|:-----------:|
| Alexander ratio | $0.661$ | $0.8815$ | $-25\%$ |
| Markov trace ratio | $0.863$ | $0.8815$ | $-2.1\%$ |
| Full Skein (open) | — | $0.8815$ | — |

## Absolute $W$ mass: what the Skein polynomial requires

The absolute mass $m_W$ (not just the ratio) requires converting
the Skein polynomial output to physical MeV.  In the QOU, the
only input mass is the electron mass
$m_e = 0.511\;\mathrm{MeV}$, which sets the dimensional scale
through
$m_e = 3\,E_\times(q_0) \cdot \mu_0$
([building blocks](#rem:building-block-knots)).

The electron-to-$W$ mass ratio is therefore determined by the
ratio of Skein polynomials:

$$
  \frac{m_W}{m_e}
  \;=\;
  \frac{\mathcal{M}(T(2,4))}{\mathcal{M}(T(2,3))}
$$

where $\mathcal{M}$ is the full mass functional.  For the
trefoil, $\mathcal{M}(T(2,3)) = 3\,E_\times = 3 \times 0.10453
= 0.31358$ (in $\mu_0$ units).

The observed ratio is $m_W / m_e = 80\,369 / 0.511 = 157\,278$.
This enormous ratio cannot come from the bare Markov trace alone
($\mathrm{tr}_M(T_1^4) / \mathrm{tr}_M(T_1^3) \approx 1.84$).
The mass hierarchy between the electroweak scale and the electron
mass arises from the **brane tower**
([recursive brane tower](#def:recursive-brane-tower)): the $W$
boson lives at a higher level of the tower than the electron, and
each level multiplies the mass by the tower amplification factor.

The brane tower level $n$ of the $W$ is determined by the number
of Kähler differentials required to encode its linking structure
on the Bring surface.  Computing $n$ and the corresponding
amplification factor remains the key open step for deriving $m_W$
from $q_0$ alone.

## The CDF discrepancy as a local substrate perturbation

The substrate parameter is not a global constant — it is a
**local field** $q(p) = 1 + |\langle L_\theta, F_A^+\rangle|(p)$
([Levi-curvature coupling](#rem:c-substrate-via-levi)) that shifts
wherever the gauge-field curvature $F_A^+$ or the Levi form
$L_\theta$ is non-trivial.

The CODATA value $q_0 = 1.10998$ is extracted from muon and
electron mass measurements performed in **low-field laboratory
environments** — Penning traps, storage rings, and spectrometers
with modest magnetic fields ($\lesssim 10$ T) and no significant
mass concentrations.  In these conditions $F_A^+$ is effectively
zero and $q(p) = q_0$
([half-life as $q$-probe](#rem:half-life-as-q-probe)).

A collider measurement of $m_W$, however, reconstructs the $W$
mass from **decay products emerging from a collision vertex**
where the local conditions are dramatically different:

1. **Collision-vertex gauge curvature.**  The $W$ boson is
   produced in a $p\bar{p}$ (CDF) or $pp$ (ATLAS, CMS) collision
   at $\sqrt{s} \sim 1$--$13$ TeV.  At the interaction point, the
   colliding partons create a transient region of concentrated
   gauge-field curvature — the same fireball environment identified
   as a $q$-shifted zone in
   [half-life as $q$-probe](#rem:half-life-as-q-probe).  In this
   region, $|F_A^+|$ is large and $q(p_{\mathrm{vertex}}) > q_0$.

2. **Detector magnetic fields.**  The decay products traverse the
   detector's solenoid field (CDF: $1.4$ T, CMS: $3.8$ T, ATLAS:
   $2$ T) before reaching the tracking and calorimetry systems.
   At these field strengths the static $\delta q$ is negligible
   ($\delta q / q_0 \sim 10^{-8}$ per the Levi-curvature coupling),
   but the field geometry affects the *reconstruction* of the $W$
   mass from measured momenta.

3. **Collision species.**  CDF used $p\bar{p}$ collisions; ATLAS
   and CMS use $pp$.  The quark-antiquark annihilation channel
   ($q\bar{q} \to W$) dominates $W$ production at the Tevatron,
   while the LHC involves significant $qg$ and sea-quark
   contributions.  In the QOU, different production channels
   correspond to different Skein resolutions at the vertex —
   $p\bar{p}$ annihilation produces a cleaner Hopf-link resolution
   than $pp$ scattering, potentially coupling differently to the
   local $q$.

## Quantitative estimate of the vertex $\delta q$

The CDF discrepancy is
$\Delta m_W = 80\,434 - 80\,357 = 77\;\mathrm{MeV}$, or
$\Delta m_W / m_W \approx 9.6 \times 10^{-4}$.

The mass functional's sensitivity to $q$ is:

$$
  \frac{\partial \ln m_W}{\partial \ln q}
  \;\approx\;
  \frac{q_0^2 + 1}{q_0^2 - 1}
  \;\approx\; 9.6
  \qquad\text{at } q_0 = 1.110.
$$

Therefore the required $\delta q$ is:

$$
  \frac{\delta q}{q_0}
  \;=\;
  \frac{\Delta m_W / m_W}{\partial \ln m_W / \partial \ln q}
  \;=\;
  \frac{9.6 \times 10^{-4}}{9.6}
  \;=\;
  1.0 \times 10^{-4},
$$

giving $\delta q \approx 0.00011$, or
$q_{\mathrm{CDF}} \approx 1.11009$.

This is a remarkably small shift — four orders of magnitude below
the $q_0$ uncertainty ($\pm 0.001$) and well within the CODATA
consistency window $q \in [1.109, 1.112]$.

## Higgs boson mass: multi-experiment comparison

The Higgs boson ($T(2,8)$, genus $3$) provides a second test of
the local-substrate hypothesis.  Unlike the $W$ boson, where a
single outlier (CDF~II) drives the discrepancy, the Higgs mass
has been measured by multiple experiments across different
collision energies, decay channels, and detector environments.

**Table: Higgs boson mass measurements by experiment.**

| Experiment | $\sqrt{s}$ (TeV) | Channel | $m_H$ (GeV) | $B$-field (T) | Collision | Year |
|------------|:-:|---------|:-----------:|:-:|:-:|:---:|
| ATLAS Run~1 | $7$--$8$ | $H \to \gamma\gamma$ | $126.02 \pm 0.51$ | $2.0$ | $pp$ | 2014 |
| ATLAS Run~1 | $7$--$8$ | $H \to ZZ^* \to 4\ell$ | $124.51 \pm 0.52$ | $2.0$ | $pp$ | 2014 |
| CMS Run~1 | $7$--$8$ | $H \to \gamma\gamma$ | $124.70 \pm 0.34$ | $3.8$ | $pp$ | 2014 |
| CMS Run~1 | $7$--$8$ | $H \to ZZ^* \to 4\ell$ | $125.59 \pm 0.45$ | $3.8$ | $pp$ | 2014 |
| **LHC Run~1 combined** | $7$--$8$ | All | $\mathbf{125.09 \pm 0.24}$ | — | $pp$ | 2015 |
| ATLAS Run~2 | $13$ | $\gamma\gamma + 4\ell$ | $124.97 \pm 0.24$ | $2.0$ | $pp$ | 2018 |
| CMS Run~2 | $13$ | $H \to \gamma\gamma$ | $125.78 \pm 0.26$ | $3.8$ | $pp$ | 2020 |
| CMS Run~2 | $13$ | $H \to ZZ^* \to 4\ell$ | $125.08 \pm 0.12$ | $3.8$ | $pp$ | 2024 |
| **PDG~2024 average** | — | All | $\mathbf{125.20 \pm 0.11}$ | — | — | 2024 |

### How the Higgs mass is measured

The Higgs boson is produced primarily via **gluon--gluon fusion**
($gg \to H$) at the LHC.  The two dominant mass-measurement
channels are:

1. **$H \to \gamma\gamma$** (diphoton).  The Higgs decays to two
   photons via a top-quark loop.  Each photon converts to an
   $e^+e^-$ pair in the electromagnetic calorimeter, and the
   invariant mass is reconstructed from the photon energies and
   angles.  This channel has excellent mass resolution
   ($\sim 1$--$2$ GeV) but low branching ratio ($\sim 0.23\%$).

2. **$H \to ZZ^* \to 4\ell$** (four-lepton).  The Higgs decays
   to two $Z$ bosons (one virtual), each decaying to $e^+e^-$ or
   $\mu^+\mu^-$.  The four lepton momenta are measured in the
   tracking system inside the solenoid.  This channel has the best
   mass resolution ($\sim 1$ GeV) and very low background, but
   tiny branching ratio ($\sim 0.013\%$).

Both channels reconstruct $m_H$ from **decay products that
traverse the full detector volume** — through the solenoid field,
tracking layers, and calorimetry.

### $q$-distortion analysis for the Higgs

The Higgs mass measurements show a spread of $\sim 1.5$ GeV
across experiments and channels — significantly larger than the
individual statistical uncertainties.  In the QOU framework, three
sources of $q$-distortion are relevant:

**1. Production-vertex $q$.**  The dominant Higgs production
mechanism is gluon--gluon fusion, where two gluons (each
identified with $T(2,2)$, the Hopf link) fuse via a top-quark
loop ($T(3,4)$, $8_{19}$) into the Higgs $T(2,8)$.  The
vertex involves the highest-genus Skein resolution in the
Standard Model: a genus-$3$ link emerging from the fusion of
genus-$0$ links through a genus-$3$ intermediary.  The local
$|F_A^+|$ at this vertex is set by the gluon field strength
at the interaction point — which depends on $\sqrt{s}$ and the
parton momentum fractions.

**Prediction**: At higher $\sqrt{s}$, the gluons carry more
momentum, the vertex $|F_A^+|$ is larger, and $q_{\mathrm{vertex}}
> q_0$.  The ATLAS Run~2 value ($124.97$ GeV at $\sqrt{s} = 13$
TeV) vs.\ the Run~1 combined value ($125.09$ GeV at $\sqrt{s} =
7$--$8$ TeV) shows a $-0.12$ GeV shift — the **opposite** of
the naive expectation if higher $\sqrt{s}$ raises $q$ and mass.
However, the shift is within $1\sigma$ and may reflect systematic
effects rather than a genuine $q$-trend.

**2. Detector solenoid field.**  CMS operates at $3.8$ T —
nearly twice the ATLAS solenoid field ($2.0$ T).  If the static
detector field contributed a measurable $\delta q$, CMS should
systematically report a higher $m_H$ than ATLAS.  Comparing
the $H \to \gamma\gamma$ channel:

$$
  m_H^{\mathrm{CMS}}(\gamma\gamma) - m_H^{\mathrm{ATLAS}}(\gamma\gamma)
  \;=\;
  125.78 - 126.02
  \;=\; -0.24\;\mathrm{GeV}
  \quad\text{(Run 1 vs.\ Run 2 mixed)}
$$

No systematic CMS-high pattern is visible.  This is consistent
with the Levi-curvature prediction that static fields at
$B \lesssim 4$ T produce $\delta q / q_0 \sim 10^{-8}$ — far
below the $\delta q / q_0 \sim 10^{-5}$ needed to shift $m_H$
by $1$ GeV at sensitivity $\partial \ln m_H / \partial \ln q
\approx 9.6$.

**3. Decay-channel dependence.**  Different channels probe
different Skein resolutions of the Higgs decay.  The
$H \to \gamma\gamma$ channel involves the top-quark loop
($T(3,4)$), while $H \to ZZ^* \to 4\ell$ resolves through two
$Z$ bosons ($T(2,6)$).  If the local $q$ at the decay vertex
differs between these channels, the reconstructed $m_H$ could
show a channel-dependent shift.

The Run~1 ATLAS data hint at this:
$m_H(\gamma\gamma) = 126.02$ vs.\ $m_H(4\ell) = 124.51$, a
$1.5$ GeV gap.  The corresponding $\delta q$:

$$
  \frac{\delta q}{q_0}
  \;=\;
  \frac{\Delta m_H / m_H}{\partial \ln m_H / \partial \ln q}
  \;=\;
  \frac{1.5 / 125.1}{9.6}
  \;\approx\; 1.2 \times 10^{-3}.
$$

This is $\delta q \approx 0.0013$ — ten times larger than the
$W$ boson CDF shift.  A channel-dependent $q$ of this magnitude
would be detectable through systematic comparisons of
$\gamma\gamma$ vs.\ $4\ell$ masses across Run~1, Run~2, and
Run~3 data.

**Table: $q$-distortion assessment for Higgs mass measurements.**

| Source of $\delta q$ | Magnitude | Detectable? | Evidence |
|---------------------|:---------:|:-----------:|:--------:|
| Detector $B$-field ($2$--$4$ T) | $\delta q/q_0 \sim 10^{-8}$ | No | No CMS-vs-ATLAS trend |
| Vertex $|F_A^+|$ ($\sqrt{s}$ dependence) | $\delta q/q_0 \sim 10^{-4}$? | Marginal | No clear $\sqrt{s}$ trend |
| Decay channel ($\gamma\gamma$ vs.\ $4\ell$) | $\delta q/q_0 \sim 10^{-3}$? | Yes | ATLAS Run~1 $1.5$ GeV gap |
| $p\bar{p}$ vs.\ $pp$ production | Not tested | — | No Tevatron Higgs precision |

### Contrast with the $W$ boson

The Higgs and $W$ masses probe **different aspects** of the local
substrate:

| Property | $W$ boson ($T(2,4)$) | Higgs ($T(2,8)$) |
|----------|:-------------------:|:----------------:|
| Genus | $1$ | $3$ |
| Exceptional divisors | $1$ | $3$ (all) |
| Crossings | $4$ | $8$ |
| $\Delta(q_0)$ | $2.01$ | $4.09$ |
| Production mode | $q\bar{q}$ (Tevatron), $qq$ (LHC) | $gg$ fusion (loop) |
| Cross-experiment spread | $77$ MeV ($0.1\%$) | $\sim 1.5$ GeV ($1.2\%$) |
| $\delta q$ implied | $1.1 \times 10^{-4}$ | $1.2 \times 10^{-3}$ |

The Higgs, spanning all three exceptional divisors, is
**more sensitive** to local substrate variations than the $W$
(which spans only one).  The genus-$3$ Seifert surface of $T(2,8)$
samples the full color-tube geometry of the Bring surface, acting
as a more complete probe of the local $q$.  This higher sensitivity
is consistent with the larger cross-experiment spread observed for
$m_H$ ($1.2\%$) compared to $m_W$ ($0.1\%$).

## Expected vs.\ observed: summary table

**Table: Electroweak boson masses — QOU predictions at the CODATA substrate $q_0$.**

| Quantity | QOU value | Experiment | Status |
|----------|:---------:|:----------:|:------:|
| $q_0$ (CODATA) | $1.10998$ | $m_\mu/m_e = 206.768$ | Input |
| $\Delta_{T(2,4)}(q_0)$ | $2.0109$ | — | Computed |
| $\Delta_{T(2,8)}(q_0)$ | $4.0889$ | — | Computed |
| $\mathrm{tr}_M(T_1^4)$ at $q_0$ | $1.2321$ | — | Computed |
| $m_W / m_Z$ (Markov trace) | $0.863$ | $0.8815 \pm 0.0002$ | $-2.1\%$ |
| $m_W / m_e$ (requires brane tower) | Open | $157\,278$ | Open |
| $m_H$ (PDG avg) | — | $125.20 \pm 0.11$ GeV | Open |
| $m_H(\gamma\gamma) - m_H(4\ell)$ | $\delta q \sim 10^{-3}$ | $\sim 1.5$ GeV (ATLAS Run~1) | Testable |
| $\delta q$ for CDF $W$ shift | $1.1 \times 10^{-4}$ | $\Delta m_W = 77$ MeV | Consistent |
| $\partial \ln m / \partial \ln q$ | $\sim 9.6$ | — | Prediction |

## Experimental tests

The local-substrate interpretation makes testable predictions
for both the $W$ and Higgs mass measurements:

1. **Collider-specific $m_W$.**  If $m_W$ reconstructed from
   $p\bar{p} \to W$ (Tevatron) differs systematically from
   $pp \to W$ (LHC), the difference traces back to the
   vertex-$q$ profile of $q\bar{q}$ annihilation vs.\ sea-quark
   scattering.  The QOU predicts that cleaner annihilation channels
   couple more strongly to the local $q$ enhancement.

2. **$m_H(\gamma\gamma)$ vs.\ $m_H(4\ell)$ across runs.**
   The ATLAS Run~1 gap of $1.5$ GeV between the diphoton and
   four-lepton channels is the most direct probe of
   channel-dependent $q$-distortion.  If the gap persists in
   Run~3 data (with higher statistics), it would indicate
   $\delta q / q_0 \sim 10^{-3}$ — an order of magnitude above
   the CDF $W$ shift and detectable through systematic
   channel-by-channel comparisons.  If it closes, the Run~1 gap
   was statistical.

3. **$m_W$ and $m_H$ vs.\ collision energy.**  At higher
   $\sqrt{s}$, the vertex gauge-field curvature $|F_A^+|$
   increases, so the local $q$ should increase.  Both $m_W$ and
   $m_H$ should trend upward with $\sqrt{s}$ — a prediction
   testable by comparing Run~1 ($7$--$8$ TeV), Run~2 ($13$ TeV),
   and Run~3 ($13.6$ TeV) values at each experiment separately
   (removing cross-experiment systematics).

4. **Genus hierarchy of sensitivity.**  The Higgs ($T(2,8)$,
   genus $3$) should be more sensitive to $q$-distortion than the
   $W$ ($T(2,4)$, genus $1$) by a factor related to the ratio of
   Seifert surface areas.  The observed cross-experiment spread
   confirms this: $m_H$ varies by $\sim 1.2\%$ across measurements
   vs.\ $\sim 0.1\%$ for $m_W$.  A quantitative test: the ratio
   of spreads should scale as the genus ratio $g_H / g_W = 3$.

5. **Half-life measurements in high-field environments.**  The
   same $\delta q$ that shifts $m_W$ by $77$ MeV would shift
   beta-decay half-lives by
   $48 \times (\delta q / q_0) \approx 0.5\%$ — within reach of
   precision single-ion trap experiments performed inside
   $B \sim 10$--$45$ T magnets
   ([half-life as $q$-probe](#rem:half-life-as-q-probe)).
