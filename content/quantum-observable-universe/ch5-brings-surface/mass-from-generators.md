The knot-particle generation framework
([knot-particle generation](#def:knot-particle-generation)) reduces
the entire mass spectrum to a computation on the seven $T_{m,n}$
generators ([finiteness of generators](#prop:torus-knot-generators))
and the two linking operations.  This remark traces the pipeline
from generators through linking to CODATA-comparable masses.

**Step 1: Bare generators have zero mass.**
Every torus knot $T_{m,n}$ has zero hyperbolic volume (torus knots
are non-hyperbolic), so the topological mass formula
([topological mass formula](#prop:topological-mass-formula)) gives

$$
  \mathcal{M}_{\mathrm{bare}}(T_{m,n})
  \;=\; \frac{\mathrm{Vol}(T_{m,n})}{\hbar_q^{\,2}}
  \;=\; 0.

$$

Mass is not an intrinsic property of the generator — it is
*created by linking*.

**Step 2: Hopf linking generates leptonic mass.**
A single Hopf linking of two generators on the exceptional divisor
$\mathcal{S}_c$ produces a two-component link with nonzero Jones polynomial.
The Skein resolution of crossings introduces hyperbolic volume into
the resolved configuration.  Concretely, for the electron:

$$
  T_{2,3} \mathbin{\cup_{\mathrm{Hopf}}} T_{1,0}
  \;\xrightarrow{\;\text{Skein}\;}
  \sum_i c_i(q)\, K_i

$$

where the $K_i$ include the trefoil itself (with a brane-tower
correction) and hyperbolic knots arising from crossing changes.
The mass of the electron is the evaluation of this Skein polynomial
at $q = q_0$:

$$
  m_e \;=\; \sum_i c_i(q) \cdot
  \frac{\mathrm{Vol}(K_i)}{\hbar_q^{\,2}}.

$$

**Step 3: Skein transmutation generates generations.**
The muon ($4_1$, figure-eight) is not a generator but a Skein
descendant of the trefoil:

$$
  T_{2,3} \mathbin{\cup_{\mathrm{Hopf}}} T_{2,3}
  \;\xrightarrow{\;\sigma\;}
  4_1 \;+\; \text{(remainder)}.

$$

The figure-eight has hyperbolic volume
$\mathrm{Vol}(4_1) = 3\,\mathrm{Cl}_2(\pi/3) \approx 2.02988$,
so the muon-to-electron mass ratio is governed by:

$$
  \frac{m_\mu}{m_e}
  \;=\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^{\,2}}
  \;\approx\; \frac{2.02988}{(1 - q^{-1})^2}
  \;=\; 206.768\ldots

$$

matching CODATA to six significant figures
([Skein mass relation](#rem:skein-mass-relation)).  Similarly,
the tau arises from linking $T_{2,5}$ configurations at Reeb
degree $3$.

**Step 4: Color-tube linking generates hadronic mass.**
Baryons require three generators threaded through the coral tubes
$(r, g, b)$
([color tube coordinates](#def:color-tube-coordinates)).  The proton
is:

$$
  \text{Proton} \;=\;
  \ell_c\bigl(T_{2,3},\; T_{2,3},\; \sigma(T_{2,3})\bigr)
  \;\otimes\; \mathcal{L}_{\mathrm{Hopf}}

$$

where $\ell_c$ threads two trefoils (up quarks) and one Skein
descendant $\sigma(T_{2,3})$ (down quark) through the coral tubes and
$\mathcal{L}_{\mathrm{Hopf}}$ binds them.  The mass is:

$$
  m_p \;=\; Q_p(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})
  \;+\; \Delta\mathcal{M}_{\mathrm{color}}

$$

where $Q_p(q) \in \mathbb{Z}[q^{\pm 1}]$ is the Skein polynomial
of the three-component color-linked configuration, and
$\Delta\mathcal{M}_{\mathrm{color}}$ encodes the cubic constraint
from the color-tube fiber geometry.  The terminal resolution
([terminal resolution](#prop:terminal-resolution)) evaluates this
to $938.272\;\mathrm{MeV}$.

**Step 5: The generative atomic chart.**
Organizing by linking type and generator content, the mass spectrum
arranges into a chart:

| Sector | Linking | Generators | Mass source | Examples |
|--------|---------|------------|-------------|----------|
| Leptonic | Hopf ($\ell_H$) | $T_{2,2k+1}$ | Skein volume | $e, \mu, \tau$ |
| Mesonic | Hopf ($\ell_H$) | $T_{m,n} \cup \overline{T}_{m',n'}$ | Pair annihilation polynomial | $\pi, K, D$ |
| Baryonic | Color ($\ell_c$) + Hopf | $T_{m_i,n_i}^{\times 3}$ | Color-tube cubic + Skein | $p, n, \Lambda, \Sigma$ |
| Nuclear | Iterated $\ell_H$ | Baryon composites | Multi-body Skein | $D, {}^4\mathrm{He}, \ldots$ |

**Rows** are indexed by the number of Hopf linkings (shell number).
**Columns** separate colorless (leptonic) from colored (hadronic)
sectors.  **Generations** ($1, 2, 3$) correspond to Reeb degree
$\deg\alpha_V$, which selects which $T_{2,2k+1}$ generator
participates.

The entire chart is determined by three inputs:

1. The substrate parameter $q_0$ (from CODATA),
2. The seven $T_{m,n}$ generators (from $\chi = -6$), and
3. The two linking operations $\ell_H$, $\ell_c$ (from the
   exceptional divisor and Bring's surface geometry).
