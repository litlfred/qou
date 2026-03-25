The $R$-matrix braiding
([Definition](#def:r-matrix-braiding)) introduces a fundamental
asymmetry between positive and negative crossings: the Skein
relation

$$
  q \, L_+ \;-\; q^{-1} L_-
  \;=\; (q^{1/2} - q^{-1/2})\, L_0
$$

weights positive crossings by $q$ and negative crossings by
$q^{-1}$.  Since $q > 1$ (specifically $q \approx 1.11$), positive
crossings contribute *more* to the Skein polynomial than negative
ones.  This asymmetry is the topological origin of electromagnetic
repulsion.

**Crossing chirality from nucleon braids.**
When two nucleons are Hopf-linked within a nucleus, the sign of
the crossing at the Hopf junction depends on the *relative
meridional winding* of their constituent quark braids.

The proton $\mathfrak{p} = [u, u, d]_c \bowtie \mathcal{L}_H$ is
dominated by trefoil ($T_{2,3}$) content: two up quarks are
trefoils with meridional winding $m = 2$.  The neutron
$\mathfrak{n} = [u, d, d]_c \bowtie \mathcal{L}_H$ is dominated
by the Skein descendant $\sigma(T_{2,3})$ (down quarks), whose
crossing change has reversed the winding orientation at the
transmuted site.  This gives three distinct inter-nucleon crossing
types:

**$\mathfrak{p}$--$\mathfrak{p}$ crossings** (proton--proton).
Both nucleons have the same dominant meridional winding ($m = 2$
from trefoil content).  Same-winding crossings are *positive*
($L_+$), so the Skein resolution picks up the larger coefficient
$q$:

$$
  \text{Skein weight}(\mathfrak{p}\text{--}\mathfrak{p})
  \;\propto\; q.
$$

This gives *less binding* per crossing pair compared to the
baseline — a **repulsive correction**.

**$\mathfrak{p}$--$\mathfrak{n}$ crossings** (proton--neutron).
The neutron's reversed winding from $\sigma(T_{2,3})$ makes
the crossing *mixed*: the resolution averages over $L_+$ and
$L_-$:

$$
  \text{Skein weight}(\mathfrak{p}\text{--}\mathfrak{n})
  \;\propto\; \tfrac{1}{2}(q + q^{-1}).
$$

This is the neutral **baseline binding** — neither repulsive
nor enhanced.

**$\mathfrak{n}$--$\mathfrak{n}$ crossings** (neutron--neutron).
Both neutrons have reversed winding, producing predominantly
*negative* crossings ($L_-$) with the smaller coefficient
$q^{-1}$:

$$
  \text{Skein weight}(\mathfrak{n}\text{--}\mathfrak{n})
  \;\propto\; q^{-1}.
$$

This gives *more binding* per crossing pair — an **attractive
enhancement**.

**Emergent Coulomb repulsion.**
The per-crossing repulsive correction between protons relative
to the proton--neutron baseline is

$$
  \delta_{\mathrm{Coulomb}}
  \;=\; q \;-\; \tfrac{1}{2}(q + q^{-1})
  \;=\; \tfrac{1}{2}(q - q^{-1})
  \;> 0.
$$

In a nucleus with $p$ protons and $n$ neutrons, the number of
proton--proton pairs is $\binom{p}{2} = p(p-1)/2$.  The total
repulsive correction to the nuclear binding energy is

$$
  \Delta E_{\mathrm{Coulomb}}
  \;\propto\;
  \binom{p}{2} \cdot (q - q^{-1}) \cdot \varepsilon
  \;\sim\; \frac{p^2}{2} \cdot (q - q^{-1}) \cdot \varepsilon
$$

where $\varepsilon$ is the per-crossing Skein mass scale.  This
reproduces the $p^2$ scaling of the Coulomb term in the
Bethe--Weizsäcker liquid-drop model.

**Unification of strong and electromagnetic interactions.**
Electromagnetic repulsion is *not* a separate force in the QOU
framework.  It is a **phase asymmetry** in the same Skein
polynomial that encodes the strong binding.  Both interactions
arise from the $R$-matrix braiding of
$\mathcal{U}_q(\mathfrak{su}(2))$, with $q$ controlling the
relative strength:

- The strong binding is proportional to
  $\tfrac{1}{2}(q + q^{-1})$ (the baseline Skein weight).
- The electromagnetic repulsion is proportional to
  $\tfrac{1}{2}(q - q^{-1})$ (the crossing asymmetry).

Their ratio is

$$
  \frac{\text{Coulomb}}{\text{Strong}}
  \;=\; \frac{q - q^{-1}}{q + q^{-1}}
  \;=\; \tanh\!\left(\ln q\right)
  \;\approx\; 0.104
  \qquad (q = 1.10997).
$$

At $q = 1$ (classical limit), the asymmetry vanishes:
$q - q^{-1} = 0$, and the electromagnetic interaction disappears
along with all quantum effects.  At $q \to \infty$
(deep-quantum regime), the ratio approaches $1$ and the two
interactions become comparable — this is the regime near the
Big Bang where the fundamental forces unify.

**Consequences for nuclear stability.**
The $p^2$ growth of the Coulomb correction explains why heavy
nuclei require $n > p$: the extra neutrons provide
$\mathfrak{p}$--$\mathfrak{n}$ and
$\mathfrak{n}$--$\mathfrak{n}$ crossings (both non-repulsive)
to compensate the growing $\binom{p}{2}$ penalty.  The stable
neutron-to-proton ratio $n/p$ increases from $\sim 1$ at small
$p$ (where the Coulomb term is negligible) to $\sim 1.5$ at
$p = 92$ (uranium), exactly as observed experimentally.
