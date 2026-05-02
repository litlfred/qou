**Proposition (three calibration inputs, aligned to (co)homology).**
*The QOU framework admits exactly three external calibration inputs.
Beyond these three, no further empirical, fitting, or numerological
input is permitted — every other mass, Q-value, binding energy,
coupling constant, mixing angle, and dimensionless ratio in the paper
is a prediction.*

| ID | Quantity | What it fixes | Sector |
|----|----------|--------------|--------|
| **CAL-1** | $m_e = 0.51099895\ldots\;\mathrm{MeV}$ | leptonic mass scale (MeV ↔ natural units) | leptonic size |
| **CAL-2** | $m_\mu / m_e = 206.7682830\ldots$ | substrate parameter $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ | dimensionless ratio (shape) |
| **CAL-3** | $Q_\beta(n) = 0.78233341\ldots\;\mathrm{MeV}$ | hadronic energy scale $E_0$ via $E_0 = Q_\beta(n)/|\Delta(\mathrm{net})|$ | hadronic interaction strength |

*The three inputs are independent: one dimensionless ratio plus two
dimensional scales. They align to the three (co)homological degrees
of freedom that survive on-shell quotient by
$\star_q F_\nabla = F_\nabla$ and gauge invariance
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ —
namely the three Wedderburn blocks (sym, std, alt) of
$H_3(R, q)$ ([three parameters from Wedderburn](#prop:three-parameters-wedderburn)).*

## Statement

For every numerical observable $\mathcal{O}$ in the paper —
mass $\mathfrak{m}$, Q-value $Q_\beta$, binding $B(Z, N)$,
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
  Q_\beta(n)^{\,b}
$$

with $a + b \in \{0, 1\}$ (dimensionless, mass-scale, or energy-scale
output) and $q_0$ fixed by CAL-2.

## Allowed substitutions

- $q_0$ is a numerical constant *only* via CAL-2; downstream compute
  must carry $q_0$ symbolically as long as possible and substitute
  the CAL-2 numerical value at the final reporting step
  ([symbolic-in-$q$ throughout](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-01-math-framework-workplan.md#p25)).
- $E_0$ is a numerical constant *only* via CAL-3; the symbolic
  hadronic-scale expression $E_0 = Q_\beta(n)/|\Delta(\mathrm{net})|$
  is the bridge.
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
- *A second hadronic scale*. $E_0$ is fixed by CAL-3; alternative
  hadronic scales (proton mass, pion mass, etc.) are predictions and
  must be derived from $\{m_e, q_0, Q_\beta(n)\}$, not introduced as
  inputs.

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
| $\mathrm{sym}$ ($\lambda = (3)$) | CAL-3: $Q_\beta(n)$ | Sets the hadronic energy quantum (sym is the "all crossings positive" / hadronic channel where the brane tower correction $\Delta(\mathrm{net}) = h(h-2)/2$ converts Q-value to scale). |

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

The 19 → 3 reduction is the testable framework-level claim: any
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
   pins $q_0$; two dimensional inputs ($m_e$, $Q_\beta(n)$) pin
   the leptonic mass scale and hadronic energy scale.

2. **Precision.** $m_e$ has CODATA precision $2.9 \times 10^{-10}$;
   $m_\mu/m_e$ has $2.2 \times 10^{-8}$ (limited by $m_\mu$); free
   neutron $Q_\beta$ has $7.8 \times 10^{-7}$. Each is among the
   most precisely measured quantities in its sector.

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
$\hat{\mathcal{O}}(q_0)$, with $E_0 = Q_\beta(n)/|\Delta(\mathrm{net})|$
providing the symbolic-to-numeric bridge for the hadronic energy
scale.

The forbidden-substitution clauses are not mathematically
necessary; they are *editorial* — they are the conditions under
which the paper's "three-parameter" claim is honest.

$\square$
