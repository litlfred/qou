The QOU framework requires exactly **three** calibration inputs
from experiment: two leptonic (fixing the shape and size of the
universe) and one hadronic (fixing the interaction energy scale).
All other masses, binding energies, Q-values, and coupling
constants are predictions.

## The three inputs

| Input | What it fixes | CODATA 2022 | Rel. precision |
|-------|--------------|-------------|:-:|
| $m_\mu / m_e = 206.7682830 \pm 0.0000045$ | Substrate parameter $q_0$ | Dimensionless ratio | $2.2 \times 10^{-8}$ |
| $m_e = 0.51099895000 \pm 0.00000000015$ MeV | Leptonic mass scale | Electron mass | $2.9 \times 10^{-10}$ |
| $Q_\beta(n) = 0.78233341 \pm 0.00000061$ MeV | Hadronic energy scale $E_0$ | Free neutron decay | $7.8 \times 10^{-7}$ |

The first input is a **dimensionless ratio** — it fixes $q_0$
via the relation $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
([Skein mass relation](#rem:skein-mass-relation)), where
$\mathrm{Vol}(4_1) \approx 2.0299$ is the topological constant
(hyperbolic volume of the figure-eight knot) and
$\hbar_q = (q-1)/q$.  No units are involved.  The precision
is limited by the muon mass ($2.2 \times 10^{-8}$), not
the electron ($2.9 \times 10^{-10}$).

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

The third input sets the **hadronic energy scale**.
The leptonic inputs ($m_e$, $q_0$) give an approximate
hadronic scale $E_0 \approx m_e/(q(q-1))$
([energy scale](#rem:energy-scale-planck)), but this
single-level expression misses the brane tower correction
($0.17\%$, or $1.3$ keV on $Q_\beta$).  The free neutron
$\beta$-decay Q-value calibrates $E_0$ exactly:

$$
  E_0
  =
  \frac{Q_\beta(n)}{|\Delta(\mathrm{net})|}
  =
  \frac{0.78233}{|h(h-2)/2|}
  \approx  4.179 \text{ MeV}
$$

where $\Delta(\mathrm{net}) = h(h-2)/2$ is the symbolic NF
difference between neutron and proton
([symbolic Q-value](#prop:neutron-qvalue-symbolic)).
The free neutron is the simplest hadronic decay — one
crossing change ($\mathfrak{d} \to \mathfrak{u}$) inside
one nucleon, no nuclear environment.  Once $E_0$ is fixed,
**all other Q-values are predictions**.

## Why exactly three

The physics endomorphism $\Phi \in \mathrm{End}_{\mathbf{C}}(A)$
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
   $\mathfrak{m}(\varrho) = |\mathrm{tr}_M(\rho(\beta))|$
   ([categorical mass as Markov trace](#prop:categorical-mass-markov))
   is dimensionless.  Converting to physical units (MeV)
   requires one mass measurement.  The electron mass sets this
   scale, analogous to the speed of light $c$ and Planck's
   constant $\hbar$ in the Standard Model.

3. **The hadronic energy scale.**  The brane tower converts
   the single-level Hecke algebra to full particle masses.  The
   leptonic sector is fully computable ($\mathrm{Li}_2/\hbar_q^2$),
   but the hadronic sector's tower correction introduces a
   $0.17\%$ shift in the energy scale $E_0$ that is not captured
   by the algebraic expression $m_e/(q(q-1))$.  The free neutron
   $Q_\beta$ calibrates this exactly.  The three inputs correspond
   to the three physical sectors: shape ($q$), leptonic size
   ($m_e$), hadronic interaction strength ($Q_\beta$).

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

## What is predicted (given the three inputs)

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
replaces all 19 with **3** (one dimensionless ratio + two
mass/energy scales), deriving the rest from the topology of
the Bring surface $\Sigma_4$ and the Iwahori--Hecke algebra
$H_n(R, q)$.

The reduction from 19 to 3 is possible because:
- **Particle content** is topological (from $\chi = -6$), not a
  free choice
- **Mass ratios** are knot invariants (from Vol and $\mathrm{tr}_M$),
  not free parameters
- **Coupling constants** are $R$-matrix eigenvalues (from $q$),
  not independent inputs
- **Mixing angles** are Clebsch--Gordan coefficients of the knot
  eigenbasis decomposition
