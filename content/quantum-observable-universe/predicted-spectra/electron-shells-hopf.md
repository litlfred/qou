The electron configuration of atoms — the shell structure
$1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} \ldots$ with shell
capacities $2, 8, 18, 32, \ldots = 2n^2$ — should arise from
the **closed sub-Hopf link structure** of the multi-electron
trefoil chain.

**The electron link.**

A neutral atom with $Z$ protons has $Z$ electrons, each a
trefoil $T_{2,3}$.  The full atom
([stable nucleus](#def:stable-nucleus)) is

$$
  \mathcal{A}(p, n)
  = 
  \underbrace{Z\mathfrak{p} \oplus N\mathfrak{n}}_{\text{nucleus}}
   \oplus 
  \underbrace{p \cdot T_{2,3}}_{\text{electron cloud}}.
$$

The electron cloud $p \cdot T_{2,3}$ is a chain of $p$
trefoils linked together by Hopf links.  An **electron shell**
is a maximal closed sub-Hopf link of this chain: a subset $S$
of trefoils such that $\bigbowtie_{i \in S} T_{2,3}$ splits
from the remaining trefoils.

**First example: helium ($p = 2$, $n = 2$).**

The electron cloud is $T_{2,3} \oplus T_{2,3}$ — a Hopf
link of two trefoils.  This pair is itself a **closed sub-link**:
it cannot accept a third trefoil without increasing the linking
number.  The two electrons fill the $1s$ shell.

This is why helium is a noble gas: its electron link is
**topologically closed**.  A third electron (lithium) must
start a new sub-link, weakly coupled to the first — the
$2s$ shell.

**Shell capacities from sub-link closure.**

The conjecture is that the shell capacities $2n^2$ are
determined by the **maximum number of trefoils that form a
closed sub-Hopf link** at linking level $n$ (the **open**
shell-capacity problem of this remark — not yet derived):

| Shell $n$ | Capacity $2n^2$ | Cumulative | Pure-$2n^2$ closure | Closed sub-link |
|----------:|----------------:|-----------:|---------------------|----------------|
| 1 | 2 | 2 | He (= noble) | $T_{2,3} \oplus T_{2,3}$ |
| 2 | 8 | 10 | Ne (= noble) | $8 \cdot T_{2,3}$ (Hopf $8$-chain) |
| 3 | 18 | 28 | Ni (**not** noble) | $18 \cdot T_{2,3}$ |
| 4 | 32 | 60 | Nd (**not** noble) | $32 \cdot T_{2,3}$ |

**Caveat — the pure-$2n^2$ closures are not the chemical noble gases.**
The cumulative pure-$2n^2$ count $[2, 10, 28, 60, \ldots]$ is the closed-shell
sequence of a *pure-Coulomb* atom; the chemical noble gases
$[2, 10, 18, 36, 54, 86]$ instead follow the **Madelung / $n+\ell$ (Aufbau)**
ordering produced by electron–electron screening.  The two agree only at He and
Ne; from $n = 3$ they diverge (Ni, Nd are not inert).  Reproducing the noble
gases therefore needs *both* the $2n^2$ derivation (open problem 1 below) *and* a
categorical screening / Madelung mechanism (absent).  The noble-gas
identifications in this remark are thus a **target, not an established
consequence**.

The noble gases (He, Ne, Ar, Kr, Xe, Rn) are the atoms
whose electron cloud is a **union of closed sub-links**:
every electron belongs to a complete shell.

**Photon absorption as a knot operation.**

When a photon is absorbed by an atom, a single electron
changes state — moving from one sub-Hopf link to another.
In the knot picture:

1. **Incoming photon**: a wavefront
   ([wavefront propagation](#rem:wavefront-propagation))
   with energy $E = h\nu$ determined by the categorical
   Lagrangian ([categorical Lagrangian](#def:categorical-lagrangian)).

2. **Absorption**: the photon's energy opens a crossing in
   the electron's sub-Hopf link, promoting the trefoil
   from the inner sub-link to the outer one.  This is a
   **single crossing change** in the Skein relation — the
   same operation that distinguishes $L_+$ from $L_-$.

3. **Emission**: the electron decays back, the crossing
   closes, and a photon is re-emitted with the same energy.

The allowed transitions (selection rules) are determined by
which crossing changes preserve the topological type of the
remaining sub-links.

**Maximal shell number from stability.**

The number of electron shells is bounded by the **stability of
the electron--hadron interaction**: the outermost trefoil must
remain Hopf-linked to the nucleus.  In the fluid-dynamic
picture, this corresponds to the **vortex capture radius** —
the distance at which the nuclear Hopf link's vortex tube can
still capture the electron's vortex tube.

The ionization energy of the outermost electron is

$$
  E_{\mathrm{ion}}  \propto 
  \frac{\mathfrak{E}_{\mathrm{cross}}(\text{electron--nucleus link})}{n^2}
$$

where $n$ is the shell number.  The atom becomes unstable
(the electron escapes) when $E_{\mathrm{ion}}$ drops below
the thermal energy $k_B T$.  This gives a maximum shell number
$n_{\max}$ that depends on the nuclear charge $p$ and the
temperature.

**Open problems.**

1. **Shell capacity derivation**: prove that the maximum
   number of trefoils in a closed sub-Hopf link at level $n$
   is $2n^2$.  This should follow from a combinatorial
   constraint on the linking matrix of the trefoil chain.

2. **Photon energy**: derive the photon energy $E = h\nu$
   from the categorical action.  The wavefront equation
   gives propagation; the frequency $\nu$ should be the
   **winding number** of the wavefront around the Reeb flow.

3. **Selection rules**: determine which crossing changes
   (Skein operations) on the electron link are allowed —
   these are the dipole selection rules $\Delta \ell = \pm 1$
   in the knot language.

4. **Orbital shapes**: the electron orbitals ($s, p, d, f$)
   should correspond to **topological types** of the
   sub-Hopf link: $s$ = unknotted Hopf pair, $p$ = trefoil
   Hopf triple, $d$ = figure-eight Hopf quintuple, etc.
   The angular momentum quantum number $\ell$ is the
   **genus of the sub-link's Seifert surface**.

5. **Noble gas stability**: prove that atoms whose electron
   cloud is a union of closed sub-links (noble gases) have
   maximal ionization energy at each period — i.e., the
   crossing energy of a complete sub-link is a local maximum.
