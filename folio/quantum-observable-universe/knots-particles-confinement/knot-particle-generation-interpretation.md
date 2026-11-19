**Operation 1: Hopf linking on the exceptional divisor.**
Let $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ be the exceptional divisor at a blow-up point $c$. The Hopf fibration $S^3 \to S^2 \cong \mathcal{S}_c$ makes the Hopf link $\mathcal{L}_{\mathrm{Hopf}}$ the canonical linking on $\mathcal{S}_c$. Given two generators $T_{m_1,n_1}$ and $T_{m_2,n_2}$, their **Hopf linking** is

$$
  \ell_H  \colon 
  T_{m_1,n_1}, T_{m_2,n_2}
   \longmapsto 
  T_{m_1,n_1} \mathbin{\cup_{\mathrm{Hopf}}} T_{m_2,n_2},
$$

producing a two-component link in $S^3$ fibered over $\mathcal{S}_c$. This is the colorless $U(1)$ binding operation:

- **Degree 0**: A single unknot $T_{1,0}$ sits on $\mathcal{S}_c$ with trivial braiding, corresponding to the neutrino at rest.
- **Degree 1**: An excited unknot $T_{1,0}$ at Reeb degree $\deg\alpha_V = 1$ acquires a unit of vertical charge.
- **Linking**: Two such unknots Hopf-link on $\mathcal{S}_c$, producing the simplest non-trivial bound state. The Hopf link contributes a binding energy $\mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})$ invisible to the $\mathbb{P}^1(\mathbb{C})$ base but detectable via the Skein polynomial.

Iterating Hopf linking builds the leptonic and mesonic sectors.

**Operation 2: Color-tube threading.**
The three color tubes $(r, g, b) = (w_2 - z, w_3 - z, w_4 - z)$ from Bring's surface provide a second linking operation. Given three generators $T_{m_1,n_1}$, $T_{m_2,n_2}$, $T_{m_3,n_3}$, their **color-tube linking** threads each knot through one of the three chiral fibers:

$$
  \ell_c  \colon 
  T_{m_1,n_1}, T_{m_2,n_2}, T_{m_3,n_3}
   \longmapsto 
  T_{m_1,n_1} \mathbin{\cup_r} T_{m_2,n_2}
  \mathbin{\cup_g} T_{m_3,n_3}.
$$

The $S_3 \subset S_5$ permutation symmetry of the color coordinates ensures this linking is invariant under color permutations. This reproduces the $\mathrm{SU}(3)$ color confinement condition. Only color-singlet combinations produce observable hadrons.

**Operation 3: Skein crossing change.**
The $q$-deformed Skein relation at a crossing

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0
$$

acts as a transmutation operation. Resolving or introducing crossings in a linked configuration converts torus topologies into hyperbolic ones. The figure-eight knot $4_1$ (muon) is not a generator. It arises from a crossing change on a linked trefoil pair:

$$
  T_{2,3} \mathbin{\cup_{\mathrm{Hopf}}} T_{2,3}
  \xrightarrow{\sigma}
  4_1 +  \text{(Skein remainder)}.
$$

The muon is a Skein excitation of the electron.

**The two operations generate the spectrum.** The particle spectrum is generated from the finite set of [torus knot generators](#def:knot-particle-generation) together with the two :refterm[linking operations]{#linking-operations}, which act on the exceptional divisor and the color-tube fibration; together with the generator family $\mathcal{G}$, they generate the full particle spectrum. We reserve $q$ for the substrate parameter and $p$ for base points; the winding indices are always $(m,n)$.
