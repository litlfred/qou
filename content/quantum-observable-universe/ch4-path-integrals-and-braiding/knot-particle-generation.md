The particle spectrum is generated from a finite set of torus knot
*generators* $T_{m,n}$ (with $\gcd(m,n) = 1$) embedded in the
standard torus $\mathbb{T}^2 \subset S^3$, together with two
*linking operations* that act on the exceptional divisor and the
color-tube fibration.

**Notation.** A torus knot $T_{m,n}$ winds $m$ times around the
meridian and $n$ times around the longitude of $\mathbb{T}^2$.
We reserve $q$ for the substrate parameter
([substrate parameter](#def:substrate-parameter)) and $p$ for base
points, so the winding indices are always $(m,n)$.

**Generator set.** The *torus knot generators* are the family

$$
  \mathcal{G} \;=\; \bigl\{\, T_{m,n} \;\big|\;
  \gcd(m,n) = 1,\; m < n,\;
  m + n \leq N(\chi) \,\bigr\}
$$

where $N(\chi)$ is a cutoff determined by the Euler characteristic
of the Frobenius--Hopf object.  For the Descartes universe with
$\chi(A) = -6$, the bound is $N(-6) = 9$, admitting:

| Generator | Knot | Crossing number | Particle sector |
|-----------|------|-----------------|-----------------|
| $T_{1,0}$ | Unknot $0_1$ | $0$ | Neutrino (trivial braiding) |
| $T_{2,3}$ | Trefoil $3_1$ | $3$ | Electron / Up quark (gen.\ 1) |
| $T_{2,5}$ | Cinquefoil $5_1$ | $5$ | Tau / Bottom quark (gen.\ 3) |
| $T_{2,7}$ | $7_1$ | $7$ | Charm quark (heavy sector) |
| $T_{3,4}$ | $8_{19}$ | $8$ | Top-quark candidate |
| $T_{3,5}$ | $10_{124}$ | $10$ | Beyond-Standard-Model sector |

All torus knots have *zero hyperbolic volume*: they are not
hyperbolic but satellite/torus type.  Consequently their bare mass
under the topological mass formula
([topological mass formula](#prop:topological-mass-formula)) vanishes:

$$
  \mathcal{M}_{\mathrm{bare}}(T_{m,n}) \;=\;
  \frac{\operatorname{Vol}(T_{m,n})}{\hbar_q^{\,2}} \;=\; 0.
$$

Mass arises *entirely* through the linking operations below.

**Operation 1: Hopf linking on the exceptional divisor.**
Let $E_c \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ be the
exceptional divisor at a blow-up point $c$.  The Hopf fibration
$S^3 \to S^2 \cong E_c$ makes the Hopf link
$\mathcal{L}_{\mathrm{Hopf}}$ the *canonical linking* on $E_c$.
Given two generators $T_{m_1,n_1}$ and $T_{m_2,n_2}$, their
**Hopf linking** is

$$
  \ell_H \;\colon\;
  T_{m_1,n_1},\; T_{m_2,n_2}
  \;\longmapsto\;
  T_{m_1,n_1} \mathbin{\cup_{\mathrm{Hopf}}} T_{m_2,n_2}
$$

producing a two-component link in $S^3$ fibered over $E_c$.
This is the colorless ($U(1)$) binding operation:

- **Degree 0**: A single unknot $T_{1,0}$ sits on $E_c$ with
  trivial braiding — the neutrino at rest.
- **Degree 1**: An excited unknot $T_{1,0}$ at Reeb degree
  $\deg\alpha_V = 1$ acquires a unit of vertical charge.
- **Linking**: Two such unknots Hopf-link on $E_c$, producing the
  simplest non-trivial bound state.  The Hopf link contributes a
  binding energy $\mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})$ that
  is invisible to the $\mathbb{P}^1(\mathbb{C})$ base but
  detectable via the Skein polynomial.

Iterating Hopf linking builds the leptonic and mesonic sectors.

**Operation 2: Color-tube threading.**
The three color tubes $(r, g, b) = (w_2 - z,\, w_3 - z,\, w_4 - z)$
from Bring's surface
([color tube coordinates](#def:color-tube-coordinates)) provide a
second linking operation.  Given three generators
$T_{m_1,n_1}$, $T_{m_2,n_2}$, $T_{m_3,n_3}$, their **color-tube
linking** threads each knot through one of the three chiral fibers:

$$
  \ell_c \;\colon\;
  T_{m_1,n_1},\; T_{m_2,n_2},\; T_{m_3,n_3}
  \;\longmapsto\;
  T_{m_1,n_1} \mathbin{\cup_r} T_{m_2,n_2}
  \mathbin{\cup_g} T_{m_3,n_3}
$$

The $S_3 \subset S_5$ permutation symmetry of the color coordinates
([color tube interpretation](#rem:color-tube-interpretation)) ensures
this linking is invariant under color permutations, reproducing the
$\mathrm{SU}(3)$ color confinement condition: only color-singlet
combinations produce observable hadrons.

**Operation 3: Skein crossing change.**
The $q$-deformed Skein relation at a crossing

$$
  q \, L_+ \;-\; q^{-1} L_-
  \;=\; (q^{1/2} - q^{-1/2})\, L_0
$$

acts as a *transmutation* operation: resolving or introducing
crossings in a linked configuration converts torus-type topologies
into hyperbolic ones.  In particular, the figure-eight knot $4_1$
(muon) is *not* a generator but arises from a crossing change on a
linked trefoil pair:

$$
  T_{2,3} \mathbin{\cup_{\mathrm{Hopf}}} T_{2,3}
  \;\xrightarrow{\;\sigma\;}
  4_1 \;+\; \text{(Skein remainder)}.
$$

The muon is literally a Skein excitation of the electron.

**Presentation of the particle Skein module.** Combining these
three operations, the Skein module
([Skein generation](#prop:skein-generation)) admits a presentation

$$
  \mathcal{S}_q(\mathbf{C}) \;=\;
  \mathbb{Z}[q^{\pm 1}]\bigl\langle\,
    \mathcal{G},\;
    \mathcal{L}_{\mathrm{Hopf}},\;
    \ell_c
  \,\bigr\rangle
  \Big/
  \bigl(\,
    q\,L_+ - q^{-1}L_- - (q^{1/2} - q^{-1/2})\,L_0
  \,\bigr)
$$

where $\mathcal{G}$ is the torus knot generator set and the
relation is the HOMFLY-PT Skein relation applied at every crossing.
Every particle in the knot--particle dictionary
([knot--particle dictionary](#rem:knot-particle-dictionary)) is
a word in this presentation.
