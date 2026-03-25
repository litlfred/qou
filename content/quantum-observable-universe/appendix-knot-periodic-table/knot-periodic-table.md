Every neutral atom is a composite knot configuration built from
protons, neutrons, and electrons via the three generation operations
([knot-particle generation](#def:knot-particle-generation)).
The knot formula for an atom with $p$ protons and $n$ neutrons is

$$
  p\,\mathfrak{p} \;\bowtie\; n\,\mathfrak{n}
  \;\bowtie\; p \cdot T_{2,3}
$$

where $\mathfrak{p} = [u, u, d]_c \bowtie \mathcal{L}_H$ is the
proton (color-linked quark triple), $\mathfrak{n} = [u, d, d]_c
\bowtie \mathcal{L}_H$ is the neutron, $T_{2,3}$ is the trefoil
(electron), and $\bowtie$ denotes Hopf linking.
Here $p$ is the number of protons (atomic number) and $n$ is the
number of neutrons, with $p + n$ the mass number.

**Mass formula.**

$$
  \mathcal{M}(p, n) \;=\;
  p \cdot m_{\mathfrak{p}}
  \;+\; n \cdot m_{\mathfrak{n}}
  \;-\; (p + n) \cdot (B/A)
  \;+\; p \cdot m_e
$$

where $m_{\mathfrak{p}} = \mathcal{S}_{uu} + 2\mathcal{S}_{ud}$
and $m_{\mathfrak{n}} = 2\mathcal{S}_{ud} + \mathcal{S}_{dd}$ are
the nucleon masses from the pair Skein formula
([terminal resolution](#prop:terminal-resolution)), $B/A$ is the
binding energy per nucleon from the Skein polynomial of the
multi-nucleon Hopf link (AME2020 values used here), and
$m_e = 0.511$ MeV is the electron mass.

All individual knot types satisfy the embeddability closure
([embeddability closure](#thm:embeddability-closure)): every
constituent has Seifert genus $\leq 4$ and descends to the
base manifold.

**Why $n > p$ for heavy elements.**
The neutron count $n$ exceeds $p$ for all elements beyond
calcium.  In the QOU framework, proton--proton Hopf crossings carry
a repulsive Skein phase (electromagnetic charge), while
proton--neutron and neutron--neutron crossings are purely attractive
(strong force only).  The repulsive crossing penalty grows as
$\sim p^2$, requiring additional neutrons to stabilize the
multi-nucleon link.  Elements marked $\diamond$ have a magic proton
number; those marked $\star$ have a magic neutron number.  At these
values the Skein polynomial has closed-shell structure with
anomalously high $B/A$.

**Magic numbers**: $2, 8, 20, 28, 50, 82$ (protons);
$2, 8, 20, 28, 50, 82, 126$ (neutrons).

**Input parameters** (one free parameter):
$q = 1.10997$, $\hbar_q = 0.09907$,
$m_{\mathfrak{p}} = 938.269$ MeV,
$m_{\mathfrak{n}} = 939.565$ MeV,
$m_e = 0.511$ MeV.

| $\#$ | Element | $p$ | $n$ | Knot formula | $\mathcal{M}_{\mathrm{QOU}}$ (MeV) | $B/A$ (MeV) |
|---:|---------|---:|---:|-------------|---:|---:|
| 1 | Hydrogen | 1 | 0 | $1\mathfrak{p} \bowtie 0\mathfrak{n} \bowtie 1T_{2,3}$ | $938.8$ | $0.0000$ |
| 2 | Helium$^{\diamond\star}$ | 2 | 2 | $2\mathfrak{p} \bowtie 2\mathfrak{n} \bowtie 2T_{2,3}$ | $3728.4$ | $7.0739$ |
| 3 | Lithium | 3 | 4 | $3\mathfrak{p} \bowtie 4\mathfrak{n} \bowtie 3T_{2,3}$ | $6535.4$ | $5.6063$ |
| 4 | Beryllium | 4 | 5 | $4\mathfrak{p} \bowtie 5\mathfrak{n} \bowtie 4T_{2,3}$ | $8394.8$ | $6.4628$ |
| 5 | Boron | 5 | 6 | $5\mathfrak{p} \bowtie 6\mathfrak{n} \bowtie 5T_{2,3}$ | $10255.1$ | $6.9277$ |
| 6 | Carbon | 6 | 6 | $6\mathfrak{p} \bowtie 6\mathfrak{n} \bowtie 6T_{2,3}$ | $11177.9$ | $7.6801$ |
| 7 | Nitrogen | 7 | 7 | $7\mathfrak{p} \bowtie 7\mathfrak{n} \bowtie 7T_{2,3}$ | $13043.8$ | $7.4756$ |
| 8 | Oxygen$^{\diamond\star}$ | 8 | 8 | $8\mathfrak{p} \bowtie 8\mathfrak{n} \bowtie 8T_{2,3}$ | $14899.1$ | $7.9762$ |
| 9 | Fluorine | 9 | 10 | $9\mathfrak{p} \bowtie 10\mathfrak{n} \bowtie 9T_{2,3}$ | $17696.9$ | $7.7790$ |
| 10 | Neon | 10 | 10 | $10\mathfrak{p} \bowtie 10\mathfrak{n} \bowtie 10T_{2,3}$ | $18622.8$ | $8.0325$ |
| 11 | Sodium | 11 | 12 | $11\mathfrak{p} \bowtie 12\mathfrak{n} \bowtie 11T_{2,3}$ | $21414.8$ | $8.1115$ |
| 12 | Magnesium | 12 | 12 | $12\mathfrak{p} \bowtie 12\mathfrak{n} \bowtie 12T_{2,3}$ | $22341.9$ | $8.2607$ |
| 13 | Aluminium | 13 | 14 | $13\mathfrak{p} \bowtie 14\mathfrak{n} \bowtie 13T_{2,3}$ | $25133.1$ | $8.3316$ |
| 14 | Silicon | 14 | 14 | $14\mathfrak{p} \bowtie 14\mathfrak{n} \bowtie 14T_{2,3}$ | $26060.3$ | $8.4477$ |
| 15 | Phosphorus | 15 | 16 | $15\mathfrak{p} \bowtie 16\mathfrak{n} \bowtie 15T_{2,3}$ | $28851.8$ | $8.4812$ |
| 16 | Sulfur | 16 | 16 | $16\mathfrak{p} \bowtie 16\mathfrak{n} \bowtie 16T_{2,3}$ | $29781.7$ | $8.4932$ |
| 17 | Chlorine | 17 | 18 | $17\mathfrak{p} \bowtie 18\mathfrak{n} \bowtie 17T_{2,3}$ | $32573.2$ | $8.5203$ |
| 18 | Argon | 18 | 22 | $18\mathfrak{p} \bowtie 22\mathfrak{n} \bowtie 18T_{2,3}$ | $37224.7$ | $8.5954$ |
| 19 | Potassium$^{\star}$ | 19 | 20 | $19\mathfrak{p} \bowtie 20\mathfrak{n} \bowtie 19T_{2,3}$ | $36294.4$ | $8.5570$ |
| 20 | Calcium$^{\diamond\star}$ | 20 | 20 | $20\mathfrak{p} \bowtie 20\mathfrak{n} \bowtie 20T_{2,3}$ | $37224.9$ | $8.5513$ |
| 21 | Scandium | 21 | 24 | $21\mathfrak{p} \bowtie 24\mathfrak{n} \bowtie 21T_{2,3}$ | $41876.1$ | $8.6190$ |
| 22 | Titanium | 22 | 26 | $22\mathfrak{p} \bowtie 26\mathfrak{n} \bowtie 22T_{2,3}$ | $44663.2$ | $8.7230$ |
| 23 | Vanadium$^{\star}$ | 23 | 28 | $23\mathfrak{p} \bowtie 28\mathfrak{n} \bowtie 23T_{2,3}$ | $47453.9$ | $8.7420$ |
| 24 | Chromium$^{\star}$ | 24 | 28 | $24\mathfrak{p} \bowtie 28\mathfrak{n} \bowtie 24T_{2,3}$ | $48382.2$ | $8.7760$ |
| 25 | Manganese | 25 | 30 | $25\mathfrak{p} \bowtie 30\mathfrak{n} \bowtie 25T_{2,3}$ | $51174.4$ | $8.7649$ |
| 26 | Iron | 26 | 30 | $26\mathfrak{p} \bowtie 30\mathfrak{n} \bowtie 26T_{2,3}$ | $52103.0$ | $8.7903$ |
| 27 | Cobalt | 27 | 32 | $27\mathfrak{p} \bowtie 32\mathfrak{n} \bowtie 27T_{2,3}$ | $54895.8$ | $8.7680$ |
| 28 | Nickel$^{\diamond}$ | 28 | 30 | $28\mathfrak{p} \bowtie 30\mathfrak{n} \bowtie 28T_{2,3}$ | $53966.3$ | $8.7322$ |
| 29 | Copper | 29 | 34 | $29\mathfrak{p} \bowtie 34\mathfrak{n} \bowtie 29T_{2,3}$ | $58618.4$ | $8.7522$ |
| 30 | Zinc | 30 | 34 | $30\mathfrak{p} \bowtie 34\mathfrak{n} \bowtie 30T_{2,3}$ | $59549.5$ | $8.7357$ |
| 31 | Gallium | 31 | 38 | $31\mathfrak{p} \bowtie 38\mathfrak{n} \bowtie 31T_{2,3}$ | $64203.7$ | $8.7246$ |
| 32 | Germanium | 32 | 42 | $32\mathfrak{p} \bowtie 42\mathfrak{n} \bowtie 32T_{2,3}$ | $68856.9$ | $8.7264$ |
| 33 | Arsenic | 33 | 42 | $33\mathfrak{p} \bowtie 42\mathfrak{n} \bowtie 33T_{2,3}$ | $69788.9$ | $8.7010$ |
| 34 | Selenium | 34 | 46 | $34\mathfrak{p} \bowtie 46\mathfrak{n} \bowtie 34T_{2,3}$ | $74441.6$ | $8.7110$ |
| 35 | Bromine | 35 | 44 | $35\mathfrak{p} \bowtie 44\mathfrak{n} \bowtie 35T_{2,3}$ | $73511.2$ | $8.6961$ |
| 36 | Krypton | 36 | 48 | $36\mathfrak{p} \bowtie 48\mathfrak{n} \bowtie 36T_{2,3}$ | $78163.0$ | $8.7172$ |
| 37 | Rubidium | 37 | 48 | $37\mathfrak{p} \bowtie 48\mathfrak{n} \bowtie 37T_{2,3}$ | $79094.7$ | $8.6974$ |
| 38 | Strontium$^{\star}$ | 38 | 50 | $38\mathfrak{p} \bowtie 50\mathfrak{n} \bowtie 38T_{2,3}$ | $81883.4$ | $8.7326$ |
| 39 | Yttrium$^{\star}$ | 39 | 50 | $39\mathfrak{p} \bowtie 50\mathfrak{n} \bowtie 39T_{2,3}$ | $82815.1$ | $8.7138$ |
| 40 | Zirconium$^{\star}$ | 40 | 50 | $40\mathfrak{p} \bowtie 50\mathfrak{n} \bowtie 40T_{2,3}$ | $83745.6$ | $8.7098$ |
| 41 | Niobium | 41 | 52 | $41\mathfrak{p} \bowtie 52\mathfrak{n} \bowtie 41T_{2,3}$ | $86541.6$ | $8.6641$ |
| 42 | Molybdenum | 42 | 56 | $42\mathfrak{p} \bowtie 56\mathfrak{n} \bowtie 42T_{2,3}$ | $91198.1$ | $8.6353$ |
| 43 | Technetium | 43 | 55 | $43\mathfrak{p} \bowtie 55\mathfrak{n} \bowtie 43T_{2,3}$ | $91201.4$ | $8.5937$ |
| 44 | Ruthenium | 44 | 58 | $44\mathfrak{p} \bowtie 58\mathfrak{n} \bowtie 44T_{2,3}$ | $94923.2$ | $8.6070$ |
| 45 | Rhodium | 45 | 58 | $45\mathfrak{p} \bowtie 58\mathfrak{n} \bowtie 45T_{2,3}$ | $95855.7$ | $8.5843$ |
| 46 | Palladium | 46 | 60 | $46\mathfrak{p} \bowtie 60\mathfrak{n} \bowtie 46T_{2,3}$ | $98649.7$ | $8.5670$ |
| 47 | Silver | 47 | 60 | $47\mathfrak{p} \bowtie 60\mathfrak{n} \bowtie 47T_{2,3}$ | $99581.3$ | $8.5536$ |
| 48 | Cadmium | 48 | 66 | $48\mathfrak{p} \bowtie 66\mathfrak{n} \bowtie 48T_{2,3}$ | $106099.2$ | $8.5398$ |
| 49 | Indium | 49 | 66 | $49\mathfrak{p} \bowtie 66\mathfrak{n} \bowtie 49T_{2,3}$ | $107032.2$ | $8.5160$ |
| 50 | Tin$^{\diamond}$ | 50 | 70 | $50\mathfrak{p} \bowtie 70\mathfrak{n} \bowtie 50T_{2,3}$ | $111688.0$ | $8.5050$ |
| 51 | Antimony | 51 | 70 | $51\mathfrak{p} \bowtie 70\mathfrak{n} \bowtie 51T_{2,3}$ | $112621.0$ | $8.4820$ |
| 52 | Tellurium | 52 | 78 | $52\mathfrak{p} \bowtie 78\mathfrak{n} \bowtie 52T_{2,3}$ | $121005.6$ | $8.4390$ |
| 53 | Iodine | 53 | 74 | $53\mathfrak{p} \bowtie 74\mathfrak{n} \bowtie 53T_{2,3}$ | $118210.6$ | $8.4455$ |
| 54 | Xenon | 54 | 78 | $54\mathfrak{p} \bowtie 78\mathfrak{n} \bowtie 54T_{2,3}$ | $122867.8$ | $8.4275$ |
| 55 | Caesium | 55 | 78 | $55\mathfrak{p} \bowtie 78\mathfrak{n} \bowtie 55T_{2,3}$ | $123800.4$ | $8.4100$ |
| 56 | Barium$^{\star}$ | 56 | 82 | $56\mathfrak{p} \bowtie 82\mathfrak{n} \bowtie 56T_{2,3}$ | $128457.7$ | $8.3937$ |
| 57 | Lanthanum$^{\star}$ | 57 | 82 | $57\mathfrak{p} \bowtie 82\mathfrak{n} \bowtie 57T_{2,3}$ | $129390.3$ | $8.3780$ |
| 58 | Cerium$^{\star}$ | 58 | 82 | $58\mathfrak{p} \bowtie 82\mathfrak{n} \bowtie 58T_{2,3}$ | $130320.9$ | $8.3765$ |
| 59 | Praseodymium$^{\star}$ | 59 | 82 | $59\mathfrak{p} \bowtie 82\mathfrak{n} \bowtie 59T_{2,3}$ | $131254.4$ | $8.3540$ |
| 60 | Neodymium$^{\star}$ | 60 | 82 | $60\mathfrak{p} \bowtie 82\mathfrak{n} \bowtie 60T_{2,3}$ | $132186.0$ | $8.3460$ |
| 61 | Promethium | 61 | 84 | $61\mathfrak{p} \bowtie 84\mathfrak{n} \bowtie 61T_{2,3}$ | $134985.0$ | $8.3040$ |
| 62 | Samarium | 62 | 90 | $62\mathfrak{p} \bowtie 90\mathfrak{n} \bowtie 62T_{2,3}$ | $141512.1$ | $8.2440$ |
| 63 | Europium | 63 | 90 | $63\mathfrak{p} \bowtie 90\mathfrak{n} \bowtie 63T_{2,3}$ | $142445.0$ | $8.2290$ |
| 64 | Gadolinium | 64 | 94 | $64\mathfrak{p} \bowtie 94\mathfrak{n} \bowtie 64T_{2,3}$ | $147103.2$ | $8.2140$ |
| 65 | Terbium | 65 | 94 | $65\mathfrak{p} \bowtie 94\mathfrak{n} \bowtie 65T_{2,3}$ | $148036.2$ | $8.1990$ |
| 66 | Dysprosium | 66 | 98 | $66\mathfrak{p} \bowtie 98\mathfrak{n} \bowtie 66T_{2,3}$ | $152694.3$ | $8.1865$ |
| 67 | Holmium | 67 | 98 | $67\mathfrak{p} \bowtie 98\mathfrak{n} \bowtie 67T_{2,3}$ | $153627.4$ | $8.1710$ |
| 68 | Erbium | 68 | 98 | $68\mathfrak{p} \bowtie 98\mathfrak{n} \bowtie 68T_{2,3}$ | $154558.4$ | $8.1690$ |
| 69 | Thulium | 69 | 100 | $69\mathfrak{p} \bowtie 100\mathfrak{n} \bowtie 69T_{2,3}$ | $157355.7$ | $8.1460$ |
| 70 | Ytterbium | 70 | 104 | $70\mathfrak{p} \bowtie 104\mathfrak{n} \bowtie 70T_{2,3}$ | $162015.1$ | $8.1280$ |
| 71 | Lutetium | 71 | 104 | $71\mathfrak{p} \bowtie 104\mathfrak{n} \bowtie 71T_{2,3}$ | $162947.8$ | $8.1165$ |
| 72 | Hafnium | 72 | 108 | $72\mathfrak{p} \bowtie 108\mathfrak{n} \bowtie 72T_{2,3}$ | $167607.5$ | $8.0985$ |
| 73 | Tantalum | 73 | 108 | $73\mathfrak{p} \bowtie 108\mathfrak{n} \bowtie 73T_{2,3}$ | $168540.2$ | $8.0870$ |
| 74 | Tungsten | 74 | 110 | $74\mathfrak{p} \bowtie 110\mathfrak{n} \bowtie 74T_{2,3}$ | $171338.1$ | $8.0639$ |
| 75 | Rhenium | 75 | 112 | $75\mathfrak{p} \bowtie 112\mathfrak{n} \bowtie 75T_{2,3}$ | $174136.5$ | $8.0390$ |
| 76 | Osmium | 76 | 116 | $76\mathfrak{p} \bowtie 116\mathfrak{n} \bowtie 76T_{2,3}$ | $178797.1$ | $8.0194$ |
| 77 | Iridium | 77 | 116 | $77\mathfrak{p} \bowtie 116\mathfrak{n} \bowtie 77T_{2,3}$ | $179730.5$ | $8.0060$ |
| 78 | Platinum | 78 | 117 | $78\mathfrak{p} \bowtie 117\mathfrak{n} \bowtie 78T_{2,3}$ | $181595.3$ | $7.9930$ |
| 79 | Gold | 79 | 118 | $79\mathfrak{p} \bowtie 118\mathfrak{n} \bowtie 79T_{2,3}$ | $183461.0$ | $7.9759$ |
| 80 | Mercury | 80 | 122 | $80\mathfrak{p} \bowtie 122\mathfrak{n} \bowtie 80T_{2,3}$ | $188122.8$ | $7.9530$ |
| 81 | Thallium | 81 | 124 | $81\mathfrak{p} \bowtie 124\mathfrak{n} \bowtie 81T_{2,3}$ | $190920.2$ | $7.9370$ |
| 82 | Lead$^{\diamond\star}$ | 82 | 126 | $82\mathfrak{p} \bowtie 126\mathfrak{n} \bowtie 82T_{2,3}$ | $193728.7$ | $7.8675$ |
| 83 | Bismuth$^{\star}$ | 83 | 126 | $83\mathfrak{p} \bowtie 126\mathfrak{n} \bowtie 83T_{2,3}$ | $194663.7$ | $7.8480$ |
| 84 | Polonium | 84 | 125 | $84\mathfrak{p} \bowtie 125\mathfrak{n} \bowtie 84T_{2,3}$ | $194665.6$ | $7.8352$ |
| 85 | Astatine | 85 | 125 | $85\mathfrak{p} \bowtie 125\mathfrak{n} \bowtie 85T_{2,3}$ | $195600.9$ | $7.8147$ |
| 86 | Radon | 86 | 136 | $86\mathfrak{p} \bowtie 136\mathfrak{n} \bowtie 86T_{2,3}$ | $206801.5$ | $7.7227$ |
| 87 | Francium | 87 | 136 | $87\mathfrak{p} \bowtie 136\mathfrak{n} \bowtie 87T_{2,3}$ | $207735.5$ | $7.7095$ |
| 88 | Radium | 88 | 138 | $88\mathfrak{p} \bowtie 138\mathfrak{n} \bowtie 88T_{2,3}$ | $210541.0$ | $7.6620$ |
| 89 | Actinium | 89 | 138 | $89\mathfrak{p} \bowtie 138\mathfrak{n} \bowtie 89T_{2,3}$ | $211474.6$ | $7.6510$ |
| 90 | Thorium | 90 | 142 | $90\mathfrak{p} \bowtie 142\mathfrak{n} \bowtie 90T_{2,3}$ | $216141.8$ | $7.6150$ |
| 91 | Protactinium | 91 | 140 | $91\mathfrak{p} \bowtie 140\mathfrak{n} \bowtie 91T_{2,3}$ | $215209.3$ | $7.6138$ |
| 92 | Uranium | 92 | 146 | $92\mathfrak{p} \bowtie 146\mathfrak{n} \bowtie 92T_{2,3}$ | $221742.6$ | $7.5701$ |

$\diamond$ = magic proton number, $\star$ = magic neutron number.

$B/A$ values from AME2020; QOU masses computed at $q = 1.10997$.
The most stable (longest-lived) isotope is listed for each element.
