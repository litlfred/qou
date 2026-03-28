**Conjecture.**
*At baryon densities exceeding the deconfinement threshold,
the Borromean linking topology of baryons
([Borromean quark](#conj:borromean-quark)) undergoes a
topological reconfiguration: the Borromean triple
$\mathcal{B}_3$ is replaced by a condensate of
Hopf-linked diquark pairs.  This is the QOU realization of
color superconductivity and color-flavor locking (CFL).*

**Background.**

In QCD at extreme baryon density (neutron star cores, $\mu_B
\gg \Lambda_{\mathrm{QCD}}$), Alford, Rajagopal, and Wilczek
\cite{alford1999} showed that quarks form **Cooper pairs** in
the color-antitriplet channel, producing a **color
superconductor**.  In the color-flavor-locked (CFL) phase, all
nine quark species (3 colors $\times$ 3 flavors) participate in
pairing, and the ground state has the symmetry
$\mathrm{SU}(3)_{\mathrm{color+flavor}}$.

**The topological transition.**

In QOU, the Borromean link $\mathcal{B}_3$ enforces confinement:
no two components are linked, so no diquark state is stable
([Borromean quark](#conj:borromean-quark)).  Color
superconductivity requires stable **diquarks** — bound states of
two quarks.  This is topologically impossible in the Borromean
phase.

At high density, adjacent Borromean triples overlap: the color
tubes of neighboring baryons interpenetrate.  When the
inter-baryon spacing falls below the color-tube diameter, the
linking topology can rearrange:

$$
  \underbrace{%
    \mathcal{B}_3(\mathfrak{u}_1, \mathfrak{d}_1, \mathfrak{s}_1)
    \;\cdot\;
    \mathcal{B}_3(\mathfrak{u}_2, \mathfrak{d}_2, \mathfrak{s}_2)
  }_{\text{two Borromean baryons}}
  \;\xrightarrow{\;\rho > \rho_c\;}
  \underbrace{%
    (\mathfrak{d}_1 \bowtie \mathfrak{s}_2)
    \;\cdot\;
    (\mathfrak{s}_1 \bowtie \mathfrak{d}_2)
    \;\cdot\;
    (\mathfrak{u}_1 \bowtie \mathfrak{u}_2)
  }_{\text{three Hopf diquark pairs}}
$$

The Borromean topology (no pairwise linking) is replaced by
**Hopf topology** (pairwise linking).  Each Hopf-linked diquark
is a Cooper pair in the color-antitriplet channel.

**Why Hopf, not Borromean.**

The Borromean link has the property that removing any one
component frees the other two — this is confinement.  The Hopf
link $\mathcal{L}_H$ has the opposite property: each pair IS
linked.  In the superconducting phase:

| Property | Borromean (confined) | Hopf (superconducting) |
|----------|---------------------|----------------------|
| Pairwise linking | None | All pairs linked |
| Stable diquarks | Forbidden | **Condensate** |
| Color neutrality | $S_5$-invariant triples | CFL pairing |
| Excitation gap | Confinement scale | Superconducting gap $\Delta_{\mathrm{CFL}}$ |

**The CFL gap as a linking energy.**

The superconducting gap $\Delta_{\mathrm{CFL}}$ — the energy
cost of breaking a Cooper pair — is the crossing energy of the
Hopf link that binds the diquark:

$$
  \Delta_{\mathrm{CFL}}
  \;\sim\;
  |\mathfrak{E}_{\mathrm{cross}}(\mathcal{L}_H)|
  \;=\;
  q + q^{-1}
  \;\approx\; 2.011 \quad\text{Skein units}
$$

at $q = 1.1097$.  This is the energy of a single Hopf-link
crossing pair: one positive ($+q$) and one negative ($-q^{-1}$)
crossing, with the strong binding dominating.

**Color-flavor locking.**

In the CFL phase, the pairing pattern locks color and flavor
indices: $\langle q^a_i q^b_j \rangle \propto
\epsilon^{abc}\epsilon_{ijk}$.  In QOU, this locking is
automatic: the three color tubes of Bring's surface
$(r, g, b)$ pair with the three quark flavors
$(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$ via the Hopf
links, and the antisymmetric tensor $\epsilon^{abc}$ arises
from the **orientation** of the Hopf linking (the linking
number $\pm 1$ determines the antisymmetry).

**Strange quark matter in neutron stars.**

The [strangelet crossing energy](#prop:strangelet-crossing-energy)
shows that equal (u,d,s) matter maximizes strong binding per
baryon.  At neutron star densities, the Witten threshold
([Witten stability](#rem:strangelet-witten-stability)) may be
crossed: the genus-cost penalty of strange quarks is offset by
the compression energy.  The phase sequence with increasing
density is:

1. **Nuclear matter** ($\rho < \rho_0$): Borromean baryons
   (protons, neutrons) in a lattice.
2. **Hyperonic matter** ($\rho_0 < \rho < 2\rho_0$):
   strange baryons ($\Lambda$, $\Sigma$, $\Xi$) appear as
   genus-$2$ cinquefoils become energetically accessible.
3. **Strange quark matter** ($2\rho_0 < \rho < \rho_c$):
   deconfined (u,d,s) quarks; Borromean structure dissolves.
4. **CFL phase** ($\rho > \rho_c$): Hopf-linked diquark
   condensate; color superconductivity.

The CFL phase is the **densest topologically ordered state**:
every quark is Hopf-linked to a partner, and the $3 \times 3$
pairing pattern fills all color-flavor channels.
