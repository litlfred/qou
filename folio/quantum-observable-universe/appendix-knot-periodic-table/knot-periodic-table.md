Every neutral atom is a composite knot configuration built from
protons, neutrons, and electrons via the three generation operations
([knot-particle generation](#def:knot-particle-generation)).
The knot formula for an atom with $Z$ protons and $N$ neutrons is

$$
  Z\mathfrak{p}  \oplus  N\mathfrak{n}
   \oplus  Z \cdot T_{2,3}
$$

where $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_H$ is the
proton (color-linked quark triple), $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p \oplus \mathcal{L}_H$ is the neutron, $T_{2,3}$ is the trefoil
(electron), and $\oplus$ denotes Hopf linking.
Here $Z$ is the atomic number (proton count) and $N$ is the
neutron count, with $A = Z + N$ the mass number.
Throughout, fraktur letters name particles ($\mathfrak{p}$ the
proton, $\mathfrak{n}$ the neutron, with $\mathfrak{u}, \mathfrak{d}$
their quark constituents).

**Mass formula.**

$$
  \mathfrak{m}(Z, N) = 
  Z \cdot m_{\mathfrak{p}}
  +  N \cdot m_{\mathfrak{n}}
  -  (Z + N) \cdot (B/A)
  +  Z \cdot m_e
$$

where $m_{\mathfrak{p}} = \mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$
and $m_{\mathfrak{n}} = 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}} + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}$ are
the nucleon masses from the pair Skein formula
([terminal resolution](#prop:terminal-resolution)), $B/A$ is the
binding energy per nucleon from the Skein polynomial of the
multi-nucleon Hopf link (AME2020 values used here), and
$m_e \approx 0.511$ MeV is the electron mass.

All individual knot types satisfy the embeddability closure
([embeddability closure](#thm:embeddability-closure)): every
constituent has Seifert genus $\leq 4$ and descends to the
base manifold.  The generation completeness theorem
([generation completeness](#thm:generation-completeness)) guarantees
that every knot with genus $\leq 4$ is reachable from the seven
torus generators via Skein crossing changes, so the particle
spectrum tabulated below is complete over embeddable knots.

**Transfer matrix computation.**

The binding energy $B/A$ and the nuclear Skein polynomial
$P_{\mathcal{N}}(q)$ are computed via transfer matrices
([transfer matrix operator](#def:transfer-matrix-operator)).
Each nucleon pair $(i, j)$ contributes a $2 \times 2$ transfer
matrix $T_{ij}(q)$ with crossing coefficients determined by the
pair type ($\mathfrak{p}$-$\mathfrak{p}$,
$\mathfrak{n}$-$\mathfrak{n}$, or mixed).  The nuclear Skein
polynomial in factored form
([Skein polynomial](#prop:skein-polynomial-transfer-matrix)) is:

$$
  P_{\mathcal{N}}(q)
  = 
  \prod_{i=0}^{A-2} \hat{V}_i(q)
$$

computed by exactly $\binom{A}{2}$ transfer matrix multiplications
(one per nucleon pair), with polynomial degree $\leq A^2 - 1$.
The factored form is never expanded — each factor $\hat{V}_i(q)$ is
a rational function in $q^{1/2}$ obtained from a chain of
$2 \times 2$ matrix products.  The step count ranges from trivial
(${}^{1}\mathrm{H}$: $0$ steps) to cheap at the heavy end:
${}^{56}\mathrm{Fe}$ takes $1540$ steps (degree $\leq 3135$) and
${}^{238}\mathrm{U}$ takes $28203$ steps (degree $\leq 56643$) —
all evaluated in milliseconds.

**Electron shell structure.**

The orbital shells in the table arise from the eigenvalues of the
photon-electron transfer matrix $T_{\gamma e}(q)$
([shell structure eigenvalues](#prop:shell-structure-eigenvalues)).
At the substrate parameter $q$, the dominant eigenvalue
$\lambda_+ = 1.1073$ governs shell energy scaling via the
Chebyshev recurrence
$\hat{V}(n+1, q) = (q - q^{-1}) \hat{V}(n, q) + \hat{V}(n-1, q)$,
reproducing the Rydberg formula $\mathfrak{E}_{\mathrm{bind}} \propto \lambda_+^{-n} \approx 1/n^2$ for low shells.  Sub-shell
structure ($s, p, d, f$ with capacities $2, 6, 10, 14$) emerges
from tensor product eigenvalue degeneracies of multi-electron
atoms.

**Beta decay universality.**

Beta transitions between table entries are governed by a single
universal matrix $\Delta_\beta(q)$
([beta decay matrix](#prop:beta-decay-transfer-matrix)):
the same $2 \times 2$ perturbation for every nucleus, regardless
of partner nucleon type.  The $Q$-value of any decay
is the difference of parent and daughter Skein polynomials,
concentrated at the converting nucleon's generators.

**Neutron excess $N > Z$ for heavy elements.**
In the QOU framework, proton--proton Hopf crossings carry a
repulsive Skein phase (electromagnetic charge), while
proton--neutron and neutron--neutron crossings are purely attractive
(strong force only), so heavy nuclei must acquire extra neutrons to
stay bound.  The neutron count $N$ therefore exceeds $Z$ for all
elements beyond calcium: the repulsive crossing penalty grows as
$\sim Z^2$, requiring additional neutrons to stabilize the
multi-nucleon link.  Elements marked $\diamond$ have a proton
stability pair; those marked $\star$ have a neutron stability pair.
At these values the Skein polynomial has closed-shell structure
with anomalously high $B/A$.

**Stability pairs**: $2, 8, 20, 28, 50, 82$ (protons);
$2, 8, 20, 28, 50, 82, 126$ (neutrons).

**Input parameters** (one free parameter):
$q = q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps), $\hbar_q = 1 - q_0^{-1} \approx 0.09908$,
$\mathfrak{E}_{\times} = \tfrac{1}{2}(q_0 - q_0^{-1}) \approx 0.10453$,
$m_{\mathfrak{p}} \approx {{ qou.library.codata-2022.proton-mass-energy-equivalent-in-mev | precision: 6 }}\;\text{MeV}$ MeV,
$m_{\mathfrak{n}} \approx {{ qou.computations.codata-masses.data.m_n_MeV | precision: 6 }}\;\text{MeV}$ MeV,
$m_e \approx 0.51100$ MeV.

**Fundamental constants from $q_0$ (approximate).**

| Symbol | Formula | Value |
|--------|---------|:-----:|
| $\hbar_q$ | $1 - q_0^{-1}$ | $\approx 0.09908$ |
| $\mathfrak{E}_{\times}$ | $\tfrac{1}{2}(q_0 - q_0^{-1})$ | $\approx 0.10453$ |
| $s$ | $q_0^{1/2} - q_0^{-1/2}$ | $\approx 0.10439$ |
| $[2]_{q_0}$ | $q_0 + q_0^{-1}$ | $\approx 2.01090$ |

**Knot-particle identification.** Each constituent knot is
classified by the fermion--boson decomposition
([fermions are knots, bosons are links](#prop:fermion-boson-knot-link)):
proton and neutron quarks are Borromean-linked trefoils
([Borromean baryon](#def:borromean-baryon)), electrons are trefoil
fermions ($T_{2,3}$), and nuclear binding comes from Hopf link
crossings.  The full building-block catalogue with Jones polynomials
and volumes is in
([building-block knots](#rem:building-block-knots)).

**Column key.** $N_{\mathrm{pred}}$ = predicted $N$ from beta-stability formula
([beta-stability](#prop:beta-stability)),
$\Delta$ = $|N - N_{\mathrm{pred}}|$,
$k_\alpha$ = closed $\alpha$ sub-links ($= \min(\lfloor Z/2 \rfloor, \lfloor N/2 \rfloor)$),
$M_q$ = QOU predicted mass, $M_o$ = observed mass.
$\diamond$ = proton stability pair, $\star$ = neutron stability pair.
All masses in MeV/$c^2$.  $M_q$ computed at
$q = q_0$; $M_o$ from AME2020 nuclear
masses plus $Z \cdot m_e$.  $B/A$ (MeV) from AME2020.
The most stable (longest-lived) isotope is listed for each element.

**Knot exhaustiveness.**
Detection is complete: every irreducible summand is labeled by a
knot via Alexander surjectivity and Markov non-degeneracy
([knot exhaustiveness](#rem:knot-exhaustiveness)).  Generation is
complete: every knot with genus $\leq 4$ is reachable
([generation completeness](#thm:generation-completeness)).
Faithfulness (whether distinct knots always give distinct Jones
polynomials) remains an open question, but QOU uses Jones only
for detection, not classification.
