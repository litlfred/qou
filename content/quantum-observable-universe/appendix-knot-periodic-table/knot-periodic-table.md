Every neutral atom is a composite knot configuration built from
protons, neutrons, and electrons via the three generation operations
([knot-particle generation](#def:knot-particle-generation)).
The knot formula for an atom with $Z$ protons and $N$ neutrons is

$$
  Z\mathfrak{p}  \bowtie  N\mathfrak{n}
   \bowtie  Z \cdot T_{2,3}
$$

where $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \bowtie \mathcal{L}_H$ is the
proton (color-linked quark triple), $\mathfrak{n} = [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p \bowtie \mathcal{L}_H$ is the neutron, $T_{2,3}$ is the trefoil
(electron), and $\bowtie$ denotes Hopf linking.
Here $Z$ is the atomic number (proton count) and $N$ is the
neutron count, with $A = Z + N$ the mass number.

**Mass formula.**

$$
  \mathcal{M}(Z, N) = 
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
For ${}^{56}\mathrm{Fe}$: $1540$ steps, degree $\leq 3135$; for
${}^{238}\mathrm{U}$: $28203$ steps — all evaluated in
milliseconds.

**Electron shell structure.**

The orbital shells in the table arise from the eigenvalues of the
photon-electron transfer matrix $T_{\gamma e}(q)$
([shell structure eigenvalues](#prop:shell-structure-eigenvalues)).
At the substrate parameter $q$, the dominant eigenvalue
$\lambda_+ = 1.1073$ governs shell energy scaling via the
Chebyshev recurrence
$\hat{V}(n+1, q) = (q - q^{-1}) \hat{V}(n, q) + \hat{V}(n-1, q)$,
reproducing the Rydberg formula $\mathbf{E}_{\mathrm{bind}} \propto \lambda_+^{-n} \approx 1/n^2$ for low shells.  Sub-shell
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

**Why $N > Z$ for heavy elements.**
The neutron count $N$ exceeds $Z$ for all elements beyond
calcium.  In the QOU framework, proton--proton Hopf crossings carry
a repulsive Skein phase (electromagnetic charge), while
proton--neutron and neutron--neutron crossings are purely attractive
(strong force only).  The repulsive crossing penalty grows as
$\sim Z^2$, requiring additional neutrons to stabilize the
multi-nucleon link.  Elements marked $\diamond$ have a proton
stability pair; those marked $\star$ have a neutron stability pair.
At these values the Skein polynomial has closed-shell structure
with anomalously high $B/A$.

**Stability pairs**: $2, 8, 20, 28, 50, 82$ (protons);
$2, 8, 20, 28, 50, 82, 126$ (neutrons).

**Input parameters** (one free parameter):
$q = q_0 \approx 1.1097$, $\hbar_q = 1 - q_0^{-1} \approx 0.09888$,
$\mathbf{E}_{\times} = \tfrac{1}{2}(q_0 - q_0^{-1}) \approx 0.10450$,
$m_{\mathfrak{p}} \approx 938.272$ MeV,
$m_{\mathfrak{n}} \approx 939.565$ MeV,
$m_e \approx 0.51100$ MeV.

**Fundamental constants from $q_0$ (approximate).**

| Symbol | Formula | Value |
|--------|---------|:-----:|
| $\hbar_q$ | $1 - q_0^{-1}$ | $\approx 0.09888$ |
| $\mathbf{E}_{\times}$ | $\tfrac{1}{2}(q_0 - q_0^{-1})$ | $\approx 0.10450$ |
| $s$ | $q_0^{1/2} - q_0^{-1/2}$ | $\approx 0.05049$ |
| $[2]_{q_0}$ | $q_0 + q_0^{-1}$ | $\approx 2.01099$ |

**Knot-particle identification.** Each constituent knot is
classified by the fermion--boson decomposition
([fermions are knots, bosons are links](#prop:fermion-boson-knot-link)):
proton and neutron quarks are Borromean-linked trefoils
([Borromean baryon](#def:borromean-baryon)), electrons are trefoil
fermions ($T_{2,3}$), and nuclear binding comes from Hopf link
crossings.  The full building-block catalogue with Jones polynomials
and volumes is in
([building-block knots](#rem:building-block-knots)).

| $\#$ | Element | $Z$ | $N$ | $N_{\mathrm{pred}}$ | $\Delta$ | $k_\alpha$ | $M_q$ (MeV) | $M_o$ (MeV) | $B/A$ |
|---:|------|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | Hydrogen | 1 | 0 | 1 | 1 | 0 | $938.8$ | $938.8$ | $0.0000$ |
| 2 | Helium$^{\diamond\star}$ | 2 | 2 | 2 | 0 | 1 | $3728.4$ | $3728.4$ | $7.0739$ |
| 3 | Lithium | 3 | 4 | 3 | 1 | 1 | $6535.4$ | $6535.4$ | $5.6063$ |
| 4 | Beryllium | 4 | 5 | 4 | 1 | 2 | $8394.8$ | $8394.8$ | $6.4628$ |
| 5 | Boron | 5 | 6 | 5 | 1 | 2 | $10255.1$ | $10255.1$ | $6.9277$ |
| 6 | Carbon | 6 | 6 | 6 | 0 | 3 | $11177.9$ | $11177.9$ | $7.6801$ |
| 7 | Nitrogen | 7 | 7 | 8 | 1 | 3 | $13043.8$ | $13043.8$ | $7.4756$ |
| 8 | Oxygen$^{\diamond\star}$ | 8 | 8 | 9 | 1 | 4 | $14899.1$ | $14899.2$ | $7.9762$ |
| 9 | Fluorine | 9 | 10 | 10 | 0 | 4 | $17696.9$ | $17696.9$ | $7.7790$ |
| 10 | Neon | 10 | 10 | 11 | 1 | 5 | $18622.8$ | $18622.8$ | $8.0325$ |
| 11 | Sodium | 11 | 12 | 12 | 0 | 5 | $21414.8$ | $21414.8$ | $8.1115$ |
| 12 | Magnesium | 12 | 12 | 14 | 2 | 6 | $22341.9$ | $22341.9$ | $8.2607$ |
| 13 | Aluminium | 13 | 14 | 15 | 1 | 6 | $25133.1$ | $25132.9$ | $8.3316$ |
| 14 | Silicon | 14 | 14 | 16 | 2 | 7 | $26060.3$ | $26060.3$ | $8.4477$ |
| 15 | Phosphorus | 15 | 16 | 17 | 1 | 7 | $28851.8$ | $28851.9$ | $8.4812$ |
| 16 | Sulfur | 16 | 16 | 19 | 3 | 8 | $29781.7$ | $29789.2$ | $8.4932$ |
| 17 | Chlorine | 17 | 18 | 20 | 2 | 8 | $32573.2$ | $32573.5$ | $8.5203$ |
| 18 | Argon | 18 | 22 | 21 | 1 | 9 | $37224.7$ | $37224.7$ | $8.5954$ |
| 19 | Potassium$^{\star}$ | 19 | 20 | 22 | 2 | 9 | $36294.4$ | $36294.5$ | $8.5570$ |
| 20 | Calcium$^{\diamond\star}$ | 20 | 20 | 24 | 4 | 10 | $37224.9$ | $37224.9$ | $8.5513$ |
| 21 | Scandium | 21 | 24 | 25 | 1 | 10 | $41876.1$ | $41876.2$ | $8.6190$ |
| 22 | Titanium | 22 | 26 | 26 | 0 | 11 | $44663.2$ | $44663.3$ | $8.7230$ |
| 23 | Vanadium$^{\star}$ | 23 | 28 | 28 | 0 | 11 | $47453.9$ | $47454.0$ | $8.7420$ |
| 24 | Chromium$^{\star}$ | 24 | 28 | 29 | 1 | 12 | $48382.2$ | $48382.3$ | $8.7760$ |
| 25 | Manganese | 25 | 30 | 30 | 0 | 12 | $51174.4$ | $51174.5$ | $8.7649$ |
| 26 | Iron | 26 | 30 | 32 | 2 | 13 | $52103.0$ | $52103.1$ | $8.7903$ |
| 27 | Cobalt | 27 | 32 | 33 | 1 | 13 | $54895.8$ | $54895.9$ | $8.7680$ |
| 28 | Nickel$^{\diamond}$ | 28 | 30 | 35 | 5 | 14 | $53966.3$ | $53966.4$ | $8.7322$ |
| 29 | Copper | 29 | 34 | 36 | 2 | 14 | $58618.4$ | $58618.5$ | $8.7522$ |
| 30 | Zinc | 30 | 34 | 37 | 3 | 15 | $59549.5$ | $59549.6$ | $8.7357$ |
| 31 | Gallium | 31 | 38 | 39 | 1 | 15 | $64203.7$ | $64203.8$ | $8.7246$ |
| 32 | Germanium | 32 | 42 | 40 | 2 | 16 | $68856.9$ | $68857.0$ | $8.7264$ |
| 33 | Arsenic | 33 | 42 | 42 | 0 | 16 | $69788.9$ | $69789.1$ | $8.7010$ |
| 34 | Selenium | 34 | 46 | 43 | 3 | 17 | $74441.6$ | $74441.8$ | $8.7110$ |
| 35 | Bromine | 35 | 44 | 45 | 1 | 17 | $73511.2$ | $73511.4$ | $8.6961$ |
| 36 | Krypton | 36 | 48 | 46 | 2 | 18 | $78163.0$ | $78163.2$ | $8.7172$ |
| 37 | Rubidium | 37 | 48 | 48 | 0 | 18 | $79094.7$ | $79094.9$ | $8.6974$ |
| 38 | Strontium$^{\star}$ | 38 | 50 | 49 | 1 | 19 | $81883.4$ | $81883.6$ | $8.7326$ |
| 39 | Yttrium$^{\star}$ | 39 | 50 | 51 | 1 | 19 | $82815.1$ | $82815.3$ | $8.7138$ |
| 40 | Zirconium$^{\star}$ | 40 | 50 | 52 | 2 | 20 | $83745.6$ | $83745.9$ | $8.7098$ |
| 41 | Niobium | 41 | 52 | 54 | 2 | 20 | $86541.6$ | $86541.9$ | $8.6641$ |
| 42 | Molybdenum | 42 | 56 | 55 | 1 | 21 | $91198.1$ | $91198.4$ | $8.6353$ |
| 43 | Technetium | 43 | 55 | 57 | 2 | 21 | $91201.4$ | $91201.7$ | $8.5937$ |
| 44 | Ruthenium | 44 | 58 | 58 | 0 | 22 | $94923.2$ | $94923.5$ | $8.6070$ |
| 45 | Rhodium | 45 | 58 | 60 | 2 | 22 | $95855.7$ | $95856.0$ | $8.5843$ |
| 46 | Palladium | 46 | 60 | 62 | 2 | 23 | $98649.7$ | $98650.1$ | $8.5670$ |
| 47 | Silver | 47 | 60 | 63 | 3 | 23 | $99581.3$ | $99581.6$ | $8.5536$ |
| 48 | Cadmium | 48 | 66 | 65 | 1 | 24 | $106099.2$ | $106099.6$ | $8.5398$ |
| 49 | Indium | 49 | 66 | 66 | 0 | 24 | $107032.2$ | $107032.6$ | $8.5160$ |
| 50 | Tin$^{\diamond}$ | 50 | 70 | 68 | 2 | 25 | $111688.0$ | $111688.4$ | $8.5050$ |
| 51 | Antimony | 51 | 70 | 70 | 0 | 25 | $112621.0$ | $112621.4$ | $8.4820$ |
| 52 | Tellurium | 52 | 78 | 71 | 7 | 26 | $121005.6$ | $121006.0$ | $8.4390$ |
| 53 | Iodine | 53 | 74 | 73 | 1 | 26 | $118210.6$ | $118211.0$ | $8.4455$ |
| 54 | Xenon | 54 | 78 | 75 | 3 | 27 | $122867.8$ | $122868.2$ | $8.4275$ |
| 55 | Caesium | 55 | 78 | 76 | 2 | 27 | $123800.4$ | $123800.9$ | $8.4100$ |
| 56 | Barium$^{\star}$ | 56 | 82 | 78 | 4 | 28 | $128457.7$ | $128458.1$ | $8.3937$ |
| 57 | Lanthanum$^{\star}$ | 57 | 82 | 80 | 2 | 28 | $129390.3$ | $129390.8$ | $8.3780$ |
| 58 | Cerium$^{\star}$ | 58 | 82 | 81 | 1 | 29 | $130320.9$ | $130321.4$ | $8.3765$ |
| 59 | Praseodymium$^{\star}$ | 59 | 82 | 83 | 1 | 29 | $131254.4$ | $131254.9$ | $8.3540$ |
| 60 | Neodymium$^{\star}$ | 60 | 82 | 85 | 3 | 30 | $132186.0$ | $132186.6$ | $8.3460$ |
| 61 | Promethium | 61 | 84 | 86 | 2 | 30 | $134985.0$ | $134985.6$ | $8.3040$ |
| 62 | Samarium | 62 | 90 | 88 | 2 | 31 | $141512.1$ | $141512.7$ | $8.2440$ |
| 63 | Europium | 63 | 90 | 90 | 0 | 31 | $142445.0$ | $142445.6$ | $8.2290$ |
| 64 | Gadolinium | 64 | 94 | 92 | 2 | 32 | $147103.2$ | $147103.8$ | $8.2140$ |
| 65 | Terbium | 65 | 94 | 93 | 1 | 32 | $148036.2$ | $148036.8$ | $8.1990$ |
| 66 | Dysprosium | 66 | 98 | 95 | 3 | 33 | $152694.3$ | $152695.0$ | $8.1865$ |
| 67 | Holmium | 67 | 98 | 97 | 1 | 33 | $153627.4$ | $153628.0$ | $8.1710$ |
| 68 | Erbium | 68 | 98 | 99 | 1 | 34 | $154558.4$ | $154559.1$ | $8.1690$ |
| 69 | Thulium | 69 | 100 | 101 | 1 | 34 | $157355.7$ | $157356.4$ | $8.1460$ |
| 70 | Ytterbium | 70 | 104 | 102 | 2 | 35 | $162015.1$ | $162015.8$ | $8.1280$ |
| 71 | Lutetium | 71 | 104 | 104 | 0 | 35 | $162947.8$ | $162948.5$ | $8.1165$ |
| 72 | Hafnium | 72 | 108 | 106 | 2 | 36 | $167607.5$ | $167608.2$ | $8.0985$ |
| 73 | Tantalum | 73 | 108 | 108 | 0 | 36 | $168540.2$ | $168540.9$ | $8.0870$ |
| 74 | Tungsten | 74 | 110 | 110 | 0 | 37 | $171338.1$ | $171338.8$ | $8.0639$ |
| 75 | Rhenium | 75 | 112 | 112 | 0 | 37 | $174136.5$ | $174137.2$ | $8.0390$ |
| 76 | Osmium | 76 | 116 | 114 | 2 | 38 | $178797.1$ | $178797.8$ | $8.0194$ |
| 77 | Iridium | 77 | 116 | 115 | 1 | 38 | $179730.5$ | $179731.2$ | $8.0060$ |
| 78 | Platinum | 78 | 117 | 117 | 0 | 39 | $181595.3$ | $181596.0$ | $7.9930$ |
| 79 | Gold | 79 | 118 | 119 | 1 | 39 | $183461.0$ | $183461.7$ | $7.9759$ |
| 80 | Mercury | 80 | 122 | 121 | 1 | 40 | $188122.8$ | $188123.5$ | $7.9530$ |
| 81 | Thallium | 81 | 124 | 123 | 1 | 40 | $190920.2$ | $190921.0$ | $7.9370$ |
| 82 | Lead$^{\diamond\star}$ | 82 | 126 | 125 | 1 | 41 | $193728.7$ | $193729.5$ | $7.8675$ |
| 83 | Bismuth$^{\star}$ | 83 | 126 | 127 | 1 | 41 | $194663.7$ | $194664.5$ | $7.8480$ |
| 84 | Polonium | 84 | 125 | 129 | 4 | 42 | $194665.6$ | $194666.4$ | $7.8352$ |
| 85 | Astatine | 85 | 125 | 131 | 6 | 42 | $195600.9$ | $195601.8$ | $7.8147$ |
| 86 | Radon | 86 | 136 | 133 | 3 | 43 | $206801.5$ | $206802.4$ | $7.7227$ |
| 87 | Francium | 87 | 136 | 135 | 1 | 43 | $207735.5$ | $207736.4$ | $7.7095$ |
| 88 | Radium | 88 | 138 | 137 | 1 | 44 | $210541.0$ | $210541.9$ | $7.6620$ |
| 89 | Actinium | 89 | 138 | 139 | 1 | 44 | $211474.6$ | $211475.5$ | $7.6510$ |
| 90 | Thorium | 90 | 142 | 141 | 1 | 45 | $216141.8$ | $216142.7$ | $7.6150$ |
| 91 | Protactinium | 91 | 140 | 143 | 3 | 45 | $215209.3$ | $215210.2$ | $7.6138$ |
| 92 | Uranium | 92 | 146 | 145 | 1 | 46 | $221742.6$ | $221743.5$ | $7.5701$ |

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

**Transfer matrix complexity.**
Each element's Skein polynomial requires $\binom{A}{2}$ transfer
matrix multiplications.  For the lightest elements this is trivial
(${}^{1}\mathrm{H}$: 0 steps); for the heaviest it remains
computationally cheap (${}^{238}\mathrm{U}$: 28203 steps, degree
$\leq 56643$, evaluated in milliseconds).  The factored form
$P_{\mathcal{N}}(q) = \prod_i \hat{V}_i(q)$ is never expanded —
each factor is a rational function in $q^{1/2}$ obtained from a
chain of $2 \times 2$ matrix products.

**Knot exhaustiveness.**
Detection is complete: every irreducible summand is labeled by a
knot via Alexander surjectivity and Markov non-degeneracy
([knot exhaustiveness](#rem:knot-exhaustiveness)).  Generation is
complete: every knot with genus $\leq 4$ is reachable
([generation completeness](#thm:generation-completeness)).
Faithfulness (whether distinct knots always give distinct Jones
polynomials) remains an open question, but QOU uses Jones only
for detection, not classification.
