This remark applies the local substrate proposition
([local substrate $q$](#prop:local-substrate-q)) to the
electroweak boson mass measurements, deriving a
**zero-free-parameter** formula for the vertex substrate
perturbation $\delta q$ at each collider experiment.

## The vertex $\delta q$ formula

The CODATA substrate $q_0$
([local substrate $q$](#prop:local-substrate-q)) is measured in
low-field laboratories where the self-dual curvature $F_A^+$
is effectively zero.  At a collider interaction vertex --- that is,
at the exceptional divisor $\mathcal{S}_p$ where all braiding takes place
([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor))
--- the gauge-field curvature is non-negligible, and the archimedean
specialization of the substrate parameter
([Levi-curvature coupling](#rem:c-substrate-via-levi)) gives

$$
  q(p) = 1 + \bigl\lvert\langle L_\varTheta,
  F_A^+\rangle\bigr\rvert(p)
   >  q_0.
$$

The perturbation $\delta q = q(p_{\mathrm{vertex}}) - q_0$
depends on two factors:

1. **Topological charge at the vertex.**  The self-dual curvature
   carries an effective topological charge
   $\mathcal{Q}_{\mathrm{top}} = \alpha / (2\pi)$, where
   $\alpha$ is the coupling constant of the gauge field mediating
   the production process.

2. **Geometric projection onto the Bring surface.**  The Levi
   form $L_\varTheta$ and $F_A^+$ both live in the $3$-dimensional
   self-dual subspace $\Lambda^+ H^*$ of the horizontal
   distribution.  The $S_5$ automorphism group of the Bring
   surface forces the Webster curvature to be constant, and
   the Gauss--Bonnet theorem fixes the total curvature budget:

   $$
     \int_{\Sigma_4} K dA = 2\pi\chi(\Sigma_4) = -12\pi,
     \qquad |\chi(\Sigma_4)| = 6.
   $$

   A single production channel couples to one color tube out
   of $|\chi|$ total curvature units, giving a geometric
   projection factor $1/|\chi(\Sigma_4)| = 1/6$.

Combining these:

$$
  \boxed{
  \delta q(\text{vertex})
  = 
  (q_0 - 1)
   \cdot 
  \frac{\alpha}{2\pi}
   \cdot 
  \frac{1}{|\chi(\Sigma_4)|}
  }
$$

Every quantity on the right is determined:

See [Table 1](#tbl:w-boson-mass-discrepancy-table1-data).

## Predictions for each production channel

**Table 1: Forward-predicted $\delta q$ and mass shifts.**

See [Table 2](#tbl:w-boson-mass-discrepancy-table2-data).

The mass shift is computed from the sensitivity
$\partial \ln m / \partial \ln q = (q_0^2 + 1)/(q_0^2 - 1) \approx 9.62$:

$$
  \delta m = \frac{\delta q}{q_0}
  \cdot (\partial \ln m / \partial \ln q)
  \cdot m.
$$

## Why CDF differs from ATLAS and CMS

The CDF~II experiment collided **protons with antiprotons**
($pp^{\sigma}$) at $\sqrt{s} \approx 1.96$ TeV.  $W$ bosons were
produced predominantly through **valence quark--antiquark
annihilation**: a $u$ quark from the proton meets a $d^{\sigma}$
from the antiproton and annihilates directly into a $W^+$.
This is a compact two-body vertex with concentrated gauge-field
curvature $F_A^+$.

At the LHC (ATLAS, CMS, LHCb), the beams are $pp$ at
$\sqrt{s} = 7$--$13$ TeV.  Since protons lack valence
antiquarks, $W$ production requires a **sea antiquark** from
quantum fluctuations.  Sea quarks carry small momentum fractions
($x \sim 0.01$--$0.05$), and the effective topological charge is
suppressed by $x^2$:

$$
  \mathcal{Q}_{\mathrm{top}}^{\mathrm{sea}}
   \approx 
  \frac{\alpha_W}{2\pi} \cdot x^2
   \sim  10^{-5}.
$$

This drives $\delta q$ below $10^{-6}$ at the LHC — explaining
why ATLAS, CMS, and LHCb all measure
$m_W \approx m_W^{\mathrm{SM}}$ while CDF sees a $77$ MeV
excess.

CDF has the **weakest** detector magnetic field
($B \approx 1.4$ T, vs.\ $3.8$ T at CMS), ruling out the detector
$B$-field as the cause.  The signal is in the **production
vertex**, not the detection environment.

## Higgs boson: multi-experiment comparison

The Higgs ($T(2,8)$, genus $3$) is produced via **gluon--gluon
fusion** through a top-quark loop — a QCD process with
$\alpha = \alpha_s$.  The vertex $\delta q$ formula predicts

$$
  \delta q(gg \to H)
  = 
  0.10998 \times \frac{0.118}{2\pi} \times \frac{1}{6}
  =  3.4 \times 10^{-4}
$$

which is $3.5\times$ larger than the CDF $W$ shift, driven by
$\alpha_s / \alpha_W \approx 3.5$.

**Table 2: Higgs boson mass measurements.**

See [Table 3](#tbl:w-boson-mass-discrepancy-table3-data).

**Table 3: $W$ boson mass measurements.**

See [Table 4](#tbl:w-boson-mass-discrepancy-table4-data).

## Inferred $\delta q$ per experiment

The backward-inferred $\delta q$ is obtained by inverting:
$\delta q / q_0 = (\delta m / m) / (\partial \ln m / \partial \ln q)$ with sensitivity $9.62$.  These values **restate the
mass deviations** in units of the substrate parameter — they are
not independent measurements.  The hypothesis is tested by
comparing the *pattern* against the forward prediction.

**Table 4: Higgs $\delta q$ by experiment and channel**
**(ref: PDG 2024 avg $\approx 125.20$ GeV).**

See [Table 5](#tbl:w-boson-mass-discrepancy-table5-data).

**Table 5: $W$ $\delta q$ by experiment**
**(ref: SM $\approx 80357$ MeV).**

See [Table 6](#tbl:w-boson-mass-discrepancy-table6-data).

## Correlation analysis

Four patterns are tested against the forward prediction:

**1. Collision type (W boson): strongest signal.**
$\delta q(pp^{\sigma}) = +1.1 \times 10^{-4}$ vs.\
$\delta q(pp) \lesssim 5 \times 10^{-6}$.  Forward prediction:
$9.9 \times 10^{-5}$ ($pp^{\sigma}$) vs.\ $\lesssim 10^{-6}$ ($pp$).
**Match.**

**2. Decay channel (Higgs): suggestive but noisy.**
Averaging across experiments:
$\overline{\delta q}(\gamma\gamma) = +1.5 \times 10^{-4}$,
$\overline{\delta q}(4\ell) = -1.3 \times 10^{-4}$.  The
$\gamma\gamma$ channel resolves through a top-quark loop
($T(3,4)$), the $4\ell$ channel through $Z$ bosons ($T(2,6)$);
different Skein resolutions may see different effective $q$ at
the vertex.  With only $\sim 3$ measurements per channel, the
signal is not statistically significant.

**3. Detector $B$-field: no signal.**
ATLAS ($B \approx 2.0$ T) averages $\delta q = -3 \times 10^{-5}$;
CMS ($B \approx 3.8$ T) averages $+8 \times 10^{-5}$.  No
systematic trend, consistent with the prediction that static
fields at $\lesssim 4$ T produce $\delta q / q_0 \sim 10^{-8}$.

**4. Collision energy $\sqrt{s}$: no signal.**
ATLAS and CMS show opposite Run~1-to-Run~2 shifts, consistent
with Higgs threshold production ($\sqrt{\hat{s}} \approx m_H$)
being independent of beam energy.

## Summary

**Table 6: QOU predictions at the CODATA substrate $q_0$.**

See [Table 7](#tbl:w-boson-mass-discrepancy-table7-data).

## Experimental tests

1. **CDF vs.\ LHC $W$ mass.**  The $pp^{\sigma}$-vs-$pp$ split is
   the cleanest test: the formula predicts $\delta m_W(pp^{\sigma})
   = 69$ MeV and $\delta m_W(pp) < 1$ MeV.  Improved LHC
   measurements tightening the $pp$ value will sharpen the test.

2. **Higgs $\gamma\gamma$ vs.\ $4\ell$ across runs.**  If the
   channel-dependent $\delta q$ persists in Run~3 data, it
   indicates decay-vertex topology dependence at the
   $\delta q \sim 10^{-4}$ level.

3. **Half-life measurements in high fields.**  The
   $\delta q \sim 10^{-4}$ that shifts $m_W$ by $69$ MeV would
   shift beta-decay half-lives by
   $48 \times (\delta q / q_0) \approx 0.5\%$
   ([half-life as $q$-probe](#rem:half-life-as-q-probe)).
