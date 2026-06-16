**Proposition (three calibration inputs, aligned to (co)homology).**
*The QOU framework admits exactly three external calibration inputs.
Beyond these three, no further empirical, fitting, or numerological
input is permitted — every other mass, Q-value, binding energy,
coupling constant, mixing angle, and dimensionless ratio in the paper
is a prediction.*

| ID | Observable | Measurement | What it fixes | DOF of $H^1 = 2W$ |
|----|-----------|-------------|--------------|-------------------|
| **CAL-1** | $m_\mathfrak{e}$ | electron mass (Penning trap) | the dimensional unit (leptonic mass scale) | $W$-plane scale |
| **CAL-2** | $m_\mu$ | muon mass (CODATA) | substrate $q_0$ via $m_\mu/m_\mathfrak{e} = \mathrm{Vol}(4_1)/\hbar_q^2$, $\hbar_q = 1-q_0^{-1}$ | $W$-plane modulus |
| **CAL-3** | $m_\pi$ | charged-pion mass (PDG) | meson scale; independent of $(m_\mathfrak{e}, q_0)$ via $\mathrm{Vol}(\mathrm{Hopf})=0$ | orthogonal class |

All three are the three real degrees of freedom of the single $H^1 = 2W$
(rank-2 $W$-plane scale + modulus, plus one orthogonal class: $2+1=3$),
**not** three distinct degrees $H^0/H^1/H^2$.

The three measured inputs are **three masses** $(m_\mathfrak{e}, m_\mu, m_\pi)$;
$m_\mathfrak{e}$ sets the unit, so $q_0$ (dimensionless) is fixed by $m_\mu$
*in that unit* — the ratio $m_\mu/m_\mathfrak{e}$.

$\mathfrak{Q}_\beta$ (neutron $\beta$-decay, $\mathfrak{D}_\beta$) is **derived**
from CAL-1 + CAL-2, **not** a calibration — the bar-odd $\sinh$ partner
of the bar-even $\cosh$ meson scale $m_\pi$. In the
**Physical-Observations** layer $q_0$ may be numerically anchored on the
more-precise proton ratio $m_p/m_\mathfrak{e}$ (re-pin 2026-05-28; the
muon ratio is then a $9.5\sigma$ cross-check), a precision substitution
within the same $H^1$ datum — not a fourth calibration.

*The three inputs are independent: one dimensionless ratio plus two
dimensional scales. They align to the three (co)homological degrees
of freedom that survive on-shell quotient by
$\star_q F_\nabla = F_\nabla$ and gauge invariance
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ —
namely the three Wedderburn blocks (sym, std, alt) of
$H_3(R, q)$ ([three parameters from Wedderburn](#prop:three-parameters-wedderburn)).*

## Statement

For every numerical observable $\mathcal{O}$ in the paper —
mass $\mathfrak{m}$, Q-value $\mathfrak{Q}_\beta$, binding $B(Z, N)$,
crossing energy $E_{\mathfrak{H}}$, coupling $\alpha$, mixing angle,
shell parameter — there exists a $\mathbb{Q}(q_0)$-element
$\hat{\mathcal{O}}(q_0) \in \mathbb{Z}[q_0^{\pm 1/2}]$ and integers
$a, b \in \mathbb{Z}$ with

$$
  \mathcal{O}
  \;=\;
  \hat{\mathcal{O}}(q_0)
  \cdot
  m_e^{\,a}
  \cdot
  m_\pi^{\,b}
$$

with $a + b \in \{0, 1\}$ (dimensionless, mass-scale, or energy-scale
output) and $q_0$ fixed by CAL-2 ($m_\mu/m_e$). The two dimensional
bridges are the calibration scales $m_e$ and $m_\pi$; the derived
hadronic energy scale $\mathfrak{E}_0 = m_e/(q_0(q_0-1))$ and the
derived $\mathfrak{Q}_\beta$ are $m_e^{1}\cdot\mathbb{Q}(q_0)$ expressions, not
independent factors.

## Allowed substitutions

- $q_0$ is a numerical constant *only* via CAL-2; downstream compute
  must carry $q_0$ symbolically as long as possible and substitute
  the CAL-2 numerical value at the final reporting step
  ([symbolic-in-$q$ throughout](https://github.com/litlfred/qou/blob/main/docs/audits/-math-framework-workplan.md#p25)).
- $\mathfrak{E}_0$ has two framework-derived forms and one CODATA
  cross-check, all related by the brane-tower correction $1/(1-\hbar_q^2)$:
    - $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1)) \approx 4.186$ MeV
      (single Planck-tick, CAL-1 + CAL-2 only),
    - $\mathfrak{E}_0^{\text{full}} = \mathfrak{E}_0^{(N=0)}/(1-\hbar_q^2) \approx 4.228$ MeV
      (tower-summed, CAL-1 + CAL-2 only),
    - $\mathfrak{E}_0^{(\text{cal})} = \mathfrak{Q}_\beta(n)/|\Delta(\mathrm{net})| \approx 4.155$ MeV
      (CAL-3 cross-check via CODATA).
  See the [notation register](../notation/notation-register.md) energy
  row and the [collisions note](../notation/notation-collisions.md)
  for the convention $\mathfrak{E}_0 \neq \mathfrak{Q}_\beta(n)$ (they differ by
  the dimensionless factor $1/|\Delta(\mathrm{net})| \approx 5.31$).
- $m_e$ enters as the unique dimensional bridge from $\mathbb{Q}(q_0)$
  to MeV.

## What is forbidden

The framework forbids:

- *Free parameters* beyond CAL-1, CAL-2, CAL-3.
- *Coefficient fits* to AME, CODATA, PDG, or any external dataset
  (e.g. "ad hoc" or "approx" tags on Bethe-Weizsäcker coefficients
  must be derived to symbolic $\mathbb{Q}(q_0)$ form, not retained
  as fits).
- *Numerological substitutions* (e.g. magic numbers
  $\{2, 8, 20, 28, 50, 82, 126\}$ asserted as data; they must be
  derived from Bring's surface period structure or the BB / LR
  homological framework).
- *A second pinning of $q_0$*. The substrate uncertainty floor
  $\delta q_0$ propagated from CODATA $m_\mu/m_e$ is a CAL-2 cross-check;
  it may not be supplemented by independent fits to $m_e$, $m_\mu$,
  $m_\tau$, or any other mass.
- *A second hadronic scale*. $m_{\pi^{\pm}}$ is CAL-3; the hadronic
  energy scale $\mathfrak{E}_0$ and $\mathfrak{Q}_\beta(n)$ are both derived from
  CAL-1 + CAL-2 and serve as cross-checks. Proton mass, neutron mass,
  and all nuclear binding energies must be derived from
  $\{m_e, q_0, m_{\pi^{\pm}}\}$, not introduced as inputs.

## (Co)homological alignment

The Wedderburn-Artin decomposition
$H_3(R, q) \cong M_1^{\mathrm{sym}} \oplus M_2^{\mathrm{std}} \oplus M_1^{\mathrm{alt}}$
gives three independent block characters $\chi_\lambda$ for
$\lambda \in \{(3), (2,1), (1^3)\}$, with degrees $1, 2, 1$. The
three on-shell parameters of the categorical action survive as the
three independent traces $\mathrm{tr}_\lambda$, one per block.

The calibration map is:

| Wedderburn block | Calibration | Role |
|------------------|-------------|------|
| $\mathrm{alt}$ ($\lambda = (1^3)$) | CAL-2: $m_\mu/m_e \mapsto q_0$ | Sets the deformation scale (alt is the "antisymmetric" / antimatter channel; $q_0 = 1$ collapses it). |
| $\mathrm{std}$ ($\lambda = (2,1)$) | CAL-1: $m_e$ | Sets the leptonic mass quantum (std is the 2-dimensional "matter" channel where $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$). |
| $\mathrm{sym}$ ($\lambda = (3)$) | CAL-3: $m_{\pi^{\pm}}$ | Sets the chiral / Goldstone scale (sym is the "all crossings positive" / hadronic channel). The pion mass is the pseudo-Goldstone boson of broken chiral $\mathrm{SU}(2)_A$; its mass encodes the chiral condensate $\langle\bar{q}q\rangle^{1/3} \approx 240\;\mathrm{MeV}$ which is absent from $(m_e, q_0)$. $\mathfrak{Q}_\beta(n)$ is **derived** from CAL-1 + CAL-2 via $\mathfrak{Q}_\beta = m_e \lvert q_0^2 - 2q_0 - 1\rvert(q_0+1)/(2q_0^3) \approx 0.784\;\mathrm{MeV}$ (0.17% miss) and serves as a cross-check, not an independent input. |

This is the meaning of "aligned to (co)homology": the three
calibrations correspond bijectively to the three irreducible
characters of $H_3(R, q)$, which are the three cohomology classes
that survive the on-shell / gauge-invariance quotient. The
framework is rigid in this sense: increasing or decreasing the
number of calibrations would require deforming the categorical
substrate to a different on-shell quotient, which would no longer
satisfy the QOU axioms.

## Comparison with the Standard Model

The Standard Model has 19 free parameters (6 quark masses, 3 lepton
masses, 3 CKM angles + 1 phase, 3 gauge couplings, Higgs mass, Higgs
VEV, QCD theta angle). The QOU framework replaces all 19 with these
**3** ([calibration inputs context](#rem:calibration-inputs)):

- particle content is topological (from $\chi(A) = -6$), not chosen;
- mass ratios are knot invariants (from algebraic quantum volume and
  $\mathrm{tr}_M$), not free;
- coupling constants are $R$-matrix eigenvalues (from $q_0$);
- mixing angles are Clebsch-Gordan coefficients of the knot eigenbasis
  decomposition.

The 19 $\to$ 3 reduction is the testable framework-level claim: any
prediction of the paper that *would* require a 4th calibration to
match data is a falsification of the framework, not a free-parameter
adjustment.

## Proof

The three-parameter count follows directly from
[`prop:three-parameters-wedderburn`](#prop:three-parameters-wedderburn):
on-shell + gauge-invariance restricts the categorical action to a
3-dimensional real parameter family. The choice of which three
external measurements pin the three parameters is conventional but
constrained by:

1. **Dimensional analysis.** One dimensionless input ($m_\mu/m_e$)
   pins $q_0$; two dimensional inputs ($m_e$, $m_\pi$) pin the
   leptonic mass scale and the meson scale. The hadronic energy scale
   $\mathfrak{E}_0$ (and hence $\mathfrak{Q}_\beta$) is **derived** from $m_e$
   and $q_0$, not an independent input.

2. **Precision.** $m_e$ has CODATA precision $2.9 \times 10^{-10}$;
   $m_\mu/m_e$ has $2.2 \times 10^{-8}$ (limited by $m_\mu$); $m_\pi$
   has PDG precision $\sim 2 \times 10^{-6}$. Each is among the
   most precisely measured quantities in its sector. In the
   Physical-Observations layer $q_0$ may instead be anchored on the
   proton ratio $m_p/m_e$ ($6 \times 10^{-11}$), the most precise
   anchor available.

3. **Naturality.** The electron is the simplest charged lepton; the
   $m_\mu/m_e$ ratio dimensionalises to $\mathrm{Vol}(4_1)$, the
   simplest hyperbolic knot invariant; the free-neutron decay is the
   simplest hadronic decay (one crossing change, no nuclear
   environment).

The categorical mass identity
[`prop:categorical-mass-markov`](#prop:categorical-mass-markov)
gives every mass as $\mathfrak{m}(\varrho) = |\mathrm{tr}_M(\rho(\beta))|$
with $\rho(\beta) \in H_n(R, q_0)$; multiplication by $m_e$ converts
to MeV. For Q-values, the brane-tower correction in the hadronic
sector is captured by the dimensionless factor
$\hat{\mathcal{O}}(q_0)$, with $E_0 = \mathfrak{Q}_\beta(n)/|\Delta(\mathrm{net})|$
providing the symbolic-to-numeric bridge for the hadronic energy
scale.

The forbidden-substitution clauses are not mathematically
necessary; they are *editorial* — they are the conditions under
which the paper's "three-parameter" claim is honest.

$\square$
