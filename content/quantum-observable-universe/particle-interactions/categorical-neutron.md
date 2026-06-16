*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The **neutron** is the baryon with $1 + 2$ crossing partition:
one up quark and two down quarks in the Borromean braid
$\mathcal{B}_3$ ([Borromean quark](#conj:borromean-quark)).

$$
  \mathfrak{n} = \mathcal{B}_3(\mathfrak{u},\mathfrak{d},\mathfrak{d})
$$

**Step 1: Borromean braid NF.**
Same as [proton](#def:categorical-proton) Step 1:
$\mathrm{net}(\mathcal{B}_3) = +1.000$, with intrinsic Hopf link
content (no separate $\mathcal{L}_H$ factor).

**Step 2: typed crossings + Hopf gluon stabilisation.**
The two down quarks introduce stronger $-H_A$ shifts than
the proton's single down quark:

The crossing pairs are tabulated in
[Table: Neutron crossing pairs](#tbl:categorical-neutron-table-data).

As with the proton, the 9-crossing element
$\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{d}\mathfrak{d})$
is LP unstable — the $\sigma_0$ channel violates Frobenius
positivity after the second quark crossing.  A single Hopf
link $L_- = \sigma_1\sigma_0$ restores stability.

The **integer LP dual** selects $L_+ \to L_-$ (two Hopf
links = $4$ gluon crossings) as the minimum-action
stabiliser.  The neutron needs more gluon than the proton
($4$ vs $2$) because the $\mathfrak{d}\mathfrak{d}$ crossing
creates deeper instability ($\mathrm{tr}_M = -0.132$ vs
$-0.006$).  Total: $13$ crossings ($6$ B$_{3}$ + $3$ quarks
+ $4$ gluon).

**Step 3: neutron NF (with Hopf gluon).**
At $q_0 \approx 1.1100$:

See [Table](#tbl:categorical-neutron-table-data).

$$
  \mathrm{net}(\mathfrak{n}) = +0.7976
$$

Compared to the proton ($\mathrm{net} = +1.0065$):
the extra down quark produces a larger $L_+$ demand
($-0.2206$ vs $-0.1114$).  Both nucleons are dominated
by the trefoil channel $e^- \approx +1.0$ after Hopf
gluon stabilisation.

**Transition: proton $\to$ neutron.**
The NF difference (coefficient by coefficient) gives the
dimensionless beta decay transition
([energy scale](#rem:beta-decay-energy-scale)):

$$
  \Delta\mathrm{net}(\mathfrak{n} - \mathfrak{p})
  = 0.7976 - 1.0065 = -0.2089
$$

The energy scale $\mathfrak{E}_0 = \mathfrak{Q}_\beta / |\Delta\mathrm{net}|
\approx 4.155$ MeV converts each coefficient difference to MeV
([formation chain](#rem:meson-to-proton-via-borromean)).

**Mass.**

$$
  \mathfrak{m}_{\mathfrak{n}} =
  2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q) + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q)
$$

At the CODATA value $q_0$: $\mathfrak{m}_{\mathfrak{n}}(q_0) \approx :val[m_n_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV, derived from the substrate parameter ([local substrate](#prop:local-substrate-q)).  The
proton--neutron mass splitting is

$$
  \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} =
  \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  \approx 1.293 \text{ MeV}
$$

arising from the Skein resolution asymmetry between the
$\mathfrak{u}\text{-}\mathfrak{u}$ and $\mathfrak{d}\text{-}\mathfrak{d}$ crossing pairs within $\mathcal{B}_3$.

**Coulomb charge.**

$$
  Q(\mathfrak{n}) =
  1 \cdot (+\tfrac{2}{3}) + 2 \cdot (-\tfrac{1}{3}) = 0.
$$

The neutron is electrically neutral: its one positive-orientation
unknot ($\mathfrak{u}$) is exactly cancelled by two negative-orientation
unknots ($\mathfrak{d}$).  Inter-neutron Hopf crossings pick up the
coefficient $q^{-1}$ (negative crossings), producing an
attractive enhancement — the categorical expression of
electric neutrality.
