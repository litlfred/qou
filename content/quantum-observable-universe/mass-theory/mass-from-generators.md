*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

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
  =  \frac{\mathrm{Vol}(T_{m,n})}{\hbar_q^{2}}
  =  0.
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
  \xrightarrow{ \text{Skein}}
  \sum_i c_i(q) K_i
$$

where the $K_i$ include the trefoil itself (with a brane-tower
correction) and hyperbolic knots arising from crossing changes.
The mass of the electron is the evaluation of this Skein polynomial
at $q = q_0$:

$$
  m_e =  \sum_i c_i(q) \cdot
  \frac{\mathrm{Vol}(K_i)}{\hbar_q^{2}}.
$$

**Step 3: Skein transmutation generates generations.**
The Higgs field ($4_1$, figure-eight) is not a generator but a Skein
descendant of the trefoil:

$$
  T_{2,3} \mathbin{\cup_{\mathrm{Hopf}}} T_{2,3}
  \xrightarrow{\sigma}
  4_1 +  \text{(remainder)}.
$$

The figure-eight has hyperbolic volume
$\mathrm{Vol}(4_1) = 3\mathrm{Cl}_2(\pi/3) \approx :val[Vol_4_1]{precision=6}$,
The muon-to-electron mass ratio is governed by the Higgs
mechanism:

$$
  \frac{m_\mu}{m_e}
  =  \frac{\mathrm{Vol}(4_1)}{\hbar_q^{2}}
   \approx  \frac{:val[Vol_4_1]{precision=6}}{(1 - q^{-1})^2}
  =  :val[m_mu_over_e]{precision=6}\ldots
$$

matching CODATA to six significant figures
([Skein mass relation](#rem:skein-mass-relation)).

The muon ($T_{2,5}$, cinquefoil) lives **on the exceptional
divisor** — its braid word carries a Hecke dressing
$\sigma_i \cdot T_{2,5}$ that embeds it in the Reeb bundle
(color tube).  The bare torus knot $T_{2,5}$ has zero
hyperbolic volume; the muon's mass arises from the Higgs
mass mechanism ($4_1$), which universally couples to every
knot-particle with crossings $> 0$.  The ratio
$m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$ is the Higgs
coupling constant for the muon--electron channel.  Similarly,
the tau ($T_{2,7}$) acquires mass through the same Higgs
mechanism at Reeb degree $3$.

**Step 4: Color-tube linking generates hadronic mass.**
Baryons require three generators threaded through the coral tubes
$(r, g, b)$
([color tube coordinates](#def:color-tube-coordinates)).  The proton
is:

$$
  \text{Proton} = 
  \ell_c\bigl(T_{2,3}, T_{2,3}, T_{2,3}^{\sigma}\bigr)
  \otimes \mathcal{L}_{\mathrm{Hopf}}
$$

where $\ell_c$ threads two trefoils (up quarks) and one Skein
descendant $T_{2,3}^{\sigma}$ (down quark) through the coral tubes and
$\mathcal{L}_{\mathrm{Hopf}}$ binds them.  The mass is:

$$
  m_p =  Q_p(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})
  +  \Delta\mathcal{M}_{\mathrm{color}}
$$

where $Q_p(q) \in \mathbb{Z}[q^{\pm 1}]$ is the Skein polynomial
of the three-component color-linked configuration, and
$\Delta\mathcal{M}_{\mathrm{color}}$ encodes the cubic constraint
from the color-tube fiber geometry.  The terminal resolution
([terminal resolution](#prop:terminal-resolution)) evaluates this
to $:val[m_p_MeV]{precision=6, witness=computations/codata-masses.witness.json} \mathrm{MeV}$.

**Step 5: The generative atomic chart.**
Organizing by linking type and generator content, the mass spectrum
arranges into a chart:

| Sector | Linking | Generators | Mass source | Examples |
|--------|---------|------------|-------------|----------|
| Leptonic | Hopf ($\ell_H$) | $T_{2,2k+1}$ | Skein volume | $e, \mu, \tau$ |
| Mesonic | Hopf ($\ell_H$) | $T_{m,n} \cup T_{m',n'}^{\sigma}$ | Pair annihilation polynomial | $\pi, K, D$ |
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
