The QOU framework requires exactly **two** calibration inputs
from experiment.  All other masses, binding energies, Q-values,
and coupling constants are predictions.

## The two inputs

| Input | What it fixes | Observable |
|-------|--------------|------------|
| $m_\mu / m_e \approx 206.768$ | Substrate parameter $q_0$ | Dimensionless lepton mass ratio (CODATA) |
| $m_n \approx 939.565$ MeV | Mass scale (unit conversion) | Free neutron mass (beam or bottle) |

The first input is a **dimensionless ratio** — it fixes $q_0$
via the relation $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
([Skein mass relation](#rem:skein-mass-relation)), where
$\mathrm{Vol}(4_1) \approx 2.0299$ is the topological constant
(hyperbolic volume of the figure-eight knot) and
$\hbar_q = (q-1)/q$.  No units are involved.

The second input sets the **mass scale** — the conversion
factor $E_0$ from dimensionless Hecke algebra outputs to MeV.
The free neutron is the natural choice: it is the simplest
hadron that decays freely, and its beta decay
$n \to p + e^- + \bar\nu_e$ is the most precisely measured
weak process.  Once $E_0$ is fixed from $m_n$, the proton
mass $m_p = m_n - Q_\beta$ becomes a **prediction** (where
$Q_\beta$ is computed from the Hecke engine).

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

**From $q_0$ + mass scale (in MeV):**
- Proton mass: $m_p = m_n - Q_\beta$ (first prediction)
- Deuteron binding energy: $\Delta E_D \approx 2.224$ MeV
- Beta decay Q-values: 6 benchmarks at 4.4% MAE
- Nuclear shell structure and magic numbers
- Half-life predictions

**Not yet predicted (open, requires brane tower):**
- Absolute dressed quark mass $\mu_\mathfrak{u}$ from $q_0$ alone
- Binding energy per nucleon $B/A$ from first principles
- Lepton absolute masses (requires Vol/$\hbar_q^2$ bridge)

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
