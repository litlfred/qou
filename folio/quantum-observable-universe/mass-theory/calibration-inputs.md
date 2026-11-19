The QOU framework requires exactly three calibration inputs from experiment: the leptonic mass scale $m_e$ (CAL-1), the neutron $\beta$-sector bar-skew channel $P_{\mathrm{skew}}^{\beta}$ (CAL-2), and the pion-sector bar-even channel $P_{\mathrm{avg}}^{\pi}$ (CAL-3). Their numerical proxies are $m_e$, the ratio $m_\mu/m_e$ (which pins $q_0$), and $m_\pi$. These inputs match the three real degrees of freedom of the first cohomology $H^1(\mathrm{Bring}) = 2W$. All other masses, binding energies, Q-values, and coupling constants are predictions. $\mathfrak{Q}_\beta = P_{\mathrm{skew}}^{\beta}$ serves as the CAL-2 proxy, validating the framework-derived hadronic energy scale $\mathfrak{E}_0$.

## The three inputs

| Input (proxy) | CAL | Canonical observable | What it fixes | Rel. precision |
|-------|:--:|-------|--------------|:-:|
| $m_e = 0.51099895000 \pm 0.00000000015$ MeV (CODATA) | CAL-1 | $m_e$ (leptonic mass scale) | the MeV unit + cohomological period | $2.9 \times 10^{-10}$ |
| $m_\mu / m_e = 206.7682830 \pm 0.0000045$ | CAL-2 | $P_{\mathrm{skew}}^{\beta}$ ($n$ $\beta$-sector bar-skew channel) | aether $q_0$ ($W$-plane modulus) | $2.2 \times 10^{-8}$ |
| $m_\pi = 139.57039 \pm 0.00018$ MeV | CAL-3 | $P_{\mathrm{avg}}^{\pi}$ (pion-sector bar-even channel) | orthogonal meson scale ($\mathrm{Vol}(\mathrm{Hopf})=0$) | $1.3 \times 10^{-6}$ |

> **CAL-2 cross-check (not a separate input).** The free-neutron
> $\beta$-decay Q-value $\mathfrak{Q}_\beta(n) = \hbar/P_{\mathrm{skew}}^{\beta}
> = 0.78233341 \pm 0.00000061$ MeV is the **proxy for CAL-2**. The
> hadronic energy scale $\mathfrak{E}_0$ is framework-derived from
> $(m_e, q_0)$; $\mathfrak{Q}_\beta$ computed from $q_0$ by the ruled
> convention-D base (the Markov trace at $z_D$) gives $0.4447$ MeV, a
> $-43.16\%$ miss, pending the convention-D $c_k$ ladder. The retired
> Form A gave $0.17\%$ (subject to the net-ansatz caveat below) and is kept
> only as a historical cross-check. Either way it serves as a cross-check rather than a
> fourth calibration.

The first input is a **dimensionless ratio** — it fixes $q_0$
via the **leading-order aether-truncation** of the canonical
operator-valued mass formula (see the note on the superseded scalar density
below):

$$
\frac{m_\mu}{m_e} \;\stackrel{\text{LO}}{=}\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
$$

([Skein mass relation](#rem:skein-mass-relation)), where
$\mathrm{Vol}(4_1) \approx 2.0299$ is the topological constant
(hyperbolic volume of the figure-eight knot) and
$\hbar_q = (q-1)/q$.  No units are involved.  The precision
is limited by the muon mass ($2.2 \times 10^{-8}$) rather than
the electron ($2.9 \times 10^{-10}$).

> **Aether density refinement.**
> The dimensional factor $1/\hbar_q^2$ forms the leading-order scalar aether density.
> The canonical operator-valued form replaces it with the
> Wedderburn-graded expansion. The Skein form closes $m_\mu/m_e = 206.77$ because it evaluates the Kashaev $q \to 1$ limit (the hyperbolic volume $\mathrm{Vol}(4_1)$), dressed by the scalar $1/\hbar_q^2$. The operator-level lepton factor $\xi_\ell(q)$ replacing $1/\hbar_q^2$ is formulated in the [operator-level lepton mass-tower conjecture](lepton-mass-tower-canonical.md).

The second input sets the **leptonic mass scale** — the
conversion from dimensionless natural units to MeV.  The
electron is the natural choice: it is the simplest charged
lepton, its mass is the most precisely measured particle mass
in the Standard Model, and its brane tower is fully computable
from $q_0$ alone:

$$
  m_e(\text{natural})
  =
  \frac{\mathrm{Li}_2(q^{-2})}{\hbar_q^2}
  \approx  112
$$

where $\mathrm{Li}_2(q^{-2}) = \sum_{n=1}^{\infty} q^{-2n}/n^2$
converges in $\sim 20$ terms.  The conversion factor is then
$m_e(\text{MeV}) / m_e(\text{natural}) \approx 4.57 \times 10^{-3}$ MeV.

**CAL-2 realization — the hadronic energy scale $\mathfrak{E}_0$ and
the $\mathfrak{Q}_\beta$ cross-check.** (CAL-3 proper is the meson scale
$m_\pi$; see below.) The leptonic inputs ($m_e$, $q_0$) give a
framework-derived hadronic scale in two forms — the single-Planck-tick value
$\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV
([energy scale](#rem:energy-scale-planck)) and the tower-summed
$\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2)
\approx 4.228$ MeV ([beta-decay energy scale](../nuclear-interactions/beta-decay-energy-scale.md)
§"tower-summed form"). The free neutron $\beta$-decay Q-value
calibrates $\mathfrak{E}_0$:

$$
  \mathfrak{E}_0^{(\text{cal})}
  =
  \frac{\mathfrak{Q}_\beta(n)}{|\Delta(\mathrm{net})|}
  =
  \frac{0.78233}{|h(h-2)/2|}
  \approx  4.179 \text{ MeV}
$$

(The typed-crossings 6-term decomposition yields $\lvert\Delta(\text{net,typed})\rvert \approx 0.18829$ and a slightly smaller $\mathfrak{E}_0 \approx 4.155$ MeV; the 0.6% gap is finite-size noise in the typed decomposition — see
[Hecke normal-form energy scale](../nuclear-interactions/beta-decay-energy-scale.md) §"three values".)

where $\Delta(\mathrm{net}) = h(h-2)/2$ is the symbolic NF
difference between neutron and proton
([symbolic Q-value](#prop:neutron-qvalue-symbolic)).
The free neutron is the simplest hadronic decay — one
crossing change ($\mathfrak{d} \to \mathfrak{u}$) inside
one nucleon, no nuclear environment. Once $\mathfrak{E}_0$ is fixed,
**$\mathfrak{Q}_\beta$ cross-check gap.**
With the tower form $\mathfrak{E}_0^{\text{full}}$ active, the framework-derived value overshoots the calibrated value by $+1.75\%$. The geometric series direction does not close the $\mathfrak{Q}_\beta$ residual; it widens it. This leaves an explicit residual requiring categorical-derivation review.

**Fitting constraint.**
The relation $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$ constitutes an ansatz. The unweighted $\mathrm{net}$ sum differs structurally from the Markov-trace weighted sums of the mass tower. Until resolved by direct per-braid computation, the $\mathfrak{Q}_\beta$-from-$q_0$ reproduction remains an unclosed cross-check.

## Necessity of exactly three inputs

The Lagrangian endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$
([categorical action](#def:categorical-action)) lives in a
vector space of dimension $\dim \mathrm{End}(A) = (\dim A)^2$.
For $H_3(R, q)$ this is $6^2 = 36$ in principle.  The on-shell
constraint $\star_q F_\nabla = F_\nabla$
([instanton on-shell](#rem:instanton-on-shell)) and gauge
invariance $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([observability](#def:quantum-observable-universe)) eliminate
all but three real parameters:

1. **The deformation parameter $q$.**  This is the single
   continuous parameter of the Iwahori--Hecke algebra $H_n(R, q)$.
   It controls all dimensionless ratios: mass ratios, coupling
   constants, crossing asymmetries.  The observability condition
   forces $q \neq 1$ (otherwise $\mathrm{Ad}(A)$ has invariants),
   and the Descartes condition $\chi(A) = -6$ constrains $q$ to
   a one-parameter family, but does not fix a specific value.
   The value $q_0 \approx 1.110$ is fixed by one dimensionless
   measurement.

2. **The leptonic mass scale.**  The categorical mass
   $\mathfrak{m}(\varrho) = \mathrm{tr}_M(\rho(\beta))$
   ([categorical mass as Markov trace](#prop:categorical-mass-markov))
   is dimensionless and signed at the categorical level.
   Trace positivity gives $\mathrm{tr}_M(x^* x) \geq 0$ rather than
   $\mathrm{tr}_M(x) \geq 0$ for a braid element $x$, so the sign of
   $\mathfrak{m}(\varrho)$ at $q_0$ is a property of the particular
   $T_w$ rather than a consequence of positivity.  Converting to physical units (MeV)
   requires one mass measurement.  The electron mass sets this
   scale, analogous to the speed of light $c$ and Planck's
   constant $\hbar$ in the Standard Model.

3. **The orthogonal meson scale (CAL-3 = $P_{\mathrm{avg}}^{\pi}$, proxy
   $m_\pi$).**  The brane tower converts the single-level Hecke
   algebra to full particle masses, but the meson sector carries an
   orthogonal class ($\mathrm{Vol}(\mathrm{Hopf})=0$) genuinely
   independent of $(m_e, q_0)$ — the charged-pion mass $m_\pi$ fixes
   it (SDP-validated). The hadronic $\beta$-decay scale $\mathfrak{E}_0$
   is *derived* from $(m_e, q_0)$ and cross-checked by
   $\mathfrak{Q}_\beta$ (the CAL-2 proxy), so it is not the third
   independent input. The three inputs correspond to the three
   physical sectors: shape ($q$, via $P_{\mathrm{skew}}^{\beta}$/CAL-2),
   leptonic size ($m_e$/CAL-1), meson scale ($m_\pi$/CAL-3).

Four structural constraints exclude any further free parameters.
* The knot-particle dictionary is **determined by $\chi = -6$**:
  6 embeddable torus knots arise with no choice
  ([cohomological embedding](#prop:cohomological-embedding)).
* The crossing weights $q$ and $-q^{-1}$ are **eigenvalues of
  the $R$-matrix**, determined by $q$ alone.
* The typed crossing operators $C(f_i, f_j; \sigma_k)$ are
  **determined by the Hecke relation and quark flavors**, with no
  free parameters
  ([typed crossing operator](#def:typed-crossing-operator)).
* The Markov trace $\mathrm{tr}_M$ is **unique** (up to the
  Markov parameter $z$, which is determined by $q$) by Schur
  orthogonality
  ([RJ canonical inner product](#prop:rj-canonical-inner-product)).

## Predictions from the three inputs

The three calibration inputs organize the derived observables into four scope classes.

**Dimensionless predictions from $q_0$ alone.**
* Lepton mass ratios: $m_\tau/m_e$, $m_\tau/m_\mu$.
* Hecke amplitude: $h = q - q^{-1} \approx 0.209$.
* Crossing asymmetry: $q/q^{-1} \approx 1.231$ (matter/antimatter).
* Neutron-proton splitting structure: $m_n - m_p \propto \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}$.
* Pair production polarisation selection rule (a model statement; tree-level QED gives nonzero pair production for parallel linear polarisations, so this is not a successful prediction; see [Breit–Wheeler polarisation vertex](#rem:breit-wheeler-vertex)).
* All NF decompositions and operator selection weights.

**Mass-scale predictions from $q_0$ and $m_e$ (in MeV).**
* Muon mass: $m_\mu = m_e \times \mathrm{Vol}(4_1)/\hbar_q^2$
  (first prediction, matching the calibration input by construction).
* Proton mass: via Skein pair formula and dressed quark masses
  from the Skein resolution tree (tractable computation).
* Neutron mass: $m_n = m_p + \mathfrak{Q}_\beta$ (Hecke engine).
* Deuteron binding energy: $\Delta E_D \approx 2.224$ MeV.
* Beta decay Q-values: 6 benchmarks at 4.4% MAE.
* Nuclear shell structure and magic numbers.
* Half-life predictions.

**Structurally predicted quantities (verified against CODATA).**
* Neutron-proton splitting: $m_n - m_p$ from crossing pair
  isolation (categorical, no calibration beyond $q_0$).
* Q-value ratios: dimensionless, from $q_0$ alone.
* Shell structure and magic numbers: from transfer matrix
  eigenvalues at $q_0$.

**Open quantities (concrete computation, not conceptual gap).**
* Dressed quark mass $\mu_\mathfrak{u}$ from $q_0$ alone:
  requires Skein resolution of Borromean braid ($\leq 729$ terms,
  each requiring a hyperbolic volume computation).
* Binding energy per nucleon $B/A$: same Skein resolution approach.

## Comparison with the Standard Model

The Standard Model has **19 free parameters** (6 quark masses,
3 lepton masses, 3 CKM angles + 1 phase, 3 gauge couplings,
Higgs mass, Higgs VEV, QCD theta angle).  The QOU framework
replaces all 19 with **3** (one dimensionless ratio + two
mass/energy scales), deriving the rest from the topology of
the Bring surface $\Sigma_4$ and the Iwahori--Hecke algebra
$H_n(R, q)$.

Four identifications underlie the reduction from 19 to 3.
- **Particle content** is topological (from $\chi = -6$) rather than a
  free choice.
- **Mass ratios** are knot invariants (from Vol and $\mathrm{tr}_M$)
  rather than free parameters.
- **Coupling constants** are $R$-matrix eigenvalues (from $q$)
  rather than independent inputs.
- **Mixing angles** are Clebsch--Gordan coefficients of the knot
  eigenbasis decomposition.
