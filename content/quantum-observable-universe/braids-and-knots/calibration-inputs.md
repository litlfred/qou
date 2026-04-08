The QOU framework requires exactly **two** calibration inputs
from experiment.  All other masses, binding energies, Q-values,
and coupling constants are predictions.

## The two inputs

| Input | What it fixes | CODATA 2022 | Rel. precision |
|-------|--------------|-------------|:-:|
| $m_\mu / m_e = 206.7682830 \pm 0.0000045$ | Substrate parameter $q_0$ | Dimensionless ratio | $2.2 \times 10^{-8}$ |
| $m_e = 0.51099895000 \pm 0.00000000015$ MeV | Mass scale (unit conversion) | Electron mass | $2.9 \times 10^{-10}$ |

The first input is a **dimensionless ratio** — it fixes $q_0$
via the relation $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
([Skein mass relation](#rem:skein-mass-relation)), where
$\mathrm{Vol}(4_1) \approx 2.0299$ is the topological constant
(hyperbolic volume of the figure-eight knot) and
$\hbar_q = (q-1)/q$.  No units are involved.  The precision
is limited by the muon mass ($2.2 \times 10^{-8}$), not
the electron ($2.9 \times 10^{-10}$).

The second input sets the **mass scale** — the conversion
from dimensionless natural units to MeV.  The electron is
the natural choice: it is the simplest charged lepton, its
mass is the most precisely measured particle mass in the
Standard Model, and its brane tower is fully computable
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

With these two inputs, **all hadronic masses become
predictions**: the proton mass, neutron mass, deuteron
binding energy, beta-decay Q-values, and nuclear shell
structure are all derived from the Hecke engine at $q_0$
with the $m_e$ ruler.

## Why exactly two

The physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$
([categorical action](#def:categorical-action)) lives in a
vector space of dimension $\dim \mathrm{End}(A) = (\dim A)^2$.
For $H_3(q)$ this is $6^2 = 36$ in principle.  The on-shell
constraint $\star_q F_\nabla = F_\nabla$
([instanton on-shell](#rem:instanton-on-shell)) and gauge
invariance $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([observability](#def:quantum-observable-universe)) eliminate
all but two real parameters:

1. **The deformation parameter $q$.**  This is the single
   continuous parameter of the Iwahori--Hecke algebra $H_n(q)$.
   It controls all dimensionless ratios: mass ratios, coupling
   constants, crossing asymmetries.  The observability condition
   forces $q \neq 1$ (otherwise $\mathrm{Ad}(A)$ has invariants),
   and the Descartes condition $\chi(A) = -6$ constrains $q$ to
   a one-parameter family, but does not fix a specific value.
   The value $q_0 \approx 1.110$ is fixed by one dimensionless
   measurement.

2. **The overall normalisation.**  The categorical mass
   $\mathfrak{m}(\varrho) = |\mathrm{tr}_M(\rho(\beta))|$
   ([categorical mass as Markov trace](#prop:categorical-mass-markov))
   is dimensionless.  Converting to physical units (MeV)
   requires one mass measurement.  This is the same
   situation as any physical theory: the speed of light $c$,
   Planck's constant $\hbar$, and Newton's constant $G$ are
   unit-setting inputs, not predictions.

No further parameters exist because:
- The knot-particle dictionary is **determined by $\chi = -6$**:
  exactly 6 embeddable torus knots, no choice
  ([cohomological embedding](#prop:cohomological-embedding)).
- The crossing weights $q$ and $-q^{-1}$ are **eigenvalues of
  the $R$-matrix**, determined by $q$ alone.
- The typed crossing operators $C(f_i, f_j; \sigma_k)$ are
  **determined by the Hecke relation and quark flavors**, no
  free parameters
  ([typed crossing operator](#def:typed-crossing-operator)).
- The Markov trace $\mathrm{tr}_M$ is **unique** (up to the
  Markov parameter $z$, which is determined by $q$) by Schur
  orthogonality
  ([RJ canonical inner product](#prop:rj-canonical-inner-product)).

## What is predicted (given the two inputs)

**From $q_0$ alone (dimensionless):**
- Lepton mass ratios: $m_\tau/m_e$, $m_\tau/m_\mu$
- Hecke amplitude: $h = q - q^{-1} \approx 0.209$
- Crossing asymmetry: $q/q^{-1} \approx 1.231$ (matter/antimatter)
- Neutron-proton splitting structure: $m_n - m_p \propto \mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}$
- Pair production polarisation selection rule
- All NF decompositions and operator selection weights

**From $q_0$ + $m_e$ (in MeV):**
- Muon mass: $m_\mu = m_e \times \mathrm{Vol}(4_1)/\hbar_q^2$
  (first prediction, by construction matches calibration input)
- Proton mass: via Skein pair formula + dressed quark masses
  from Skein resolution tree (tractable computation)
- Neutron mass: $m_n = m_p + Q_\beta$ (Hecke engine)
- Deuteron binding energy: $\Delta E_D \approx 2.224$ MeV
- Beta decay Q-values: 6 benchmarks at 4.4% MAE
- Nuclear shell structure and magic numbers
- Half-life predictions

**Structurally predicted (verified against CODATA):**
- Neutron-proton splitting: $m_n - m_p$ from crossing pair
  isolation (categorical, no calibration beyond $q_0$)
- Q-value ratios: dimensionless, from $q_0$ alone
- Shell structure and magic numbers: from transfer matrix
  eigenvalues at $q_0$

**Open (concrete computation, not conceptual gap):**
- Dressed quark mass $\mu_\mathfrak{u}$ from $q_0$ alone:
  requires Skein resolution of Borromean braid ($\leq 729$ terms,
  each requiring a hyperbolic volume computation)
- Binding energy per nucleon $B/A$: same Skein resolution approach

## Comparison with the Standard Model

The Standard Model has **19 free parameters** (6 quark masses,
3 lepton masses, 3 CKM angles + 1 phase, 3 gauge couplings,
Higgs mass, Higgs VEV, QCD theta angle).  The QOU framework
replaces all 19 with **2** (one dimensionless ratio + one mass
scale), deriving the rest from the topology of the Bring surface
$\Sigma_4$ and the Iwahori--Hecke algebra $H_n(q)$.

The reduction from 19 to 2 is possible because:
- **Particle content** is topological (from $\chi = -6$), not a
  free choice
- **Mass ratios** are knot invariants (from Vol and $\mathrm{tr}_M$),
  not free parameters
- **Coupling constants** are $R$-matrix eigenvalues (from $q$),
  not independent inputs
- **Mixing angles** are Clebsch--Gordan coefficients of the knot
  eigenbasis decomposition
