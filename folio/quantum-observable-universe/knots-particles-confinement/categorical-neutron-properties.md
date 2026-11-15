The [neutron definition](#def:categorical-neutron) establishes the $\mathcal{B}_3(\mathfrak{u},\mathfrak{d},\mathfrak{d})$ baryon. We derive its normal form, mass, $\beta$-decay transition, and Coulomb charge.

**Step 1: Borromean braid NF.**
As in the [proton](#def:categorical-proton) construction, we find $\mathrm{net}(\mathcal{B}_3) = +1.000$, establishing intrinsic Hopf link content without an independent $\mathcal{L}_H$ factor.

**Step 2: Typed crossings + Hopf gluon stabilisation.**
The two down quarks induce stronger $-h_{\mathrm{A}}$ shifts than the single down quark of the proton. The crossing pairs appear in [Table: Neutron crossing pairs](#tbl:categorical-neutron-table-data).

*(Partly withdrawn — see below. Two independent corrections, four days apart.)*

~~The bare 9-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ remains LP unstable. The $\sigma_0$ channel violates Frobenius positivity following the second quark crossing.~~ A single Hopf link $L_- = \sigma_1\sigma_0$ is what the construction applies.

The integer LP dual selects $L_-$ as the minimum-action stabiliser, for a total of **11 crossings** (6 from $\mathcal{B}_3$, 3 from quarks, 2 from gluons) — [`qou-vtlj`](#rem:gluon-stabiliser-ledger), which rebuilt the block's own recipe and found the stated $\mathrm{net}(\mathfrak{n}) = +0.7976$ is the eleven-crossing value. The earlier "$L_+ \to L_-$, 4 gluon crossings, 13 total" was wrong on its own terms, independently of anything below.

~~The $\mathfrak{d}\mathfrak{d}$ crossing creates a deeper instability than the proton's ($\mathrm{tr}_M = -0.132$ versus $-0.006$), a difference in depth rather than in the number of gluon crossings required.~~

**The remaining depth claim does not survive either** (`qou-jqjx`). Those two figures come from `fsh-guts/deprecated/computations/integer-lp-gluon.py`, which computes the Markov trace on convention C with $\mathrm{tr}_M(e^-) = z^3$ — a weight retired on 2026-05-19 in favour of the Markov-recursion value $h z^2 + z$. Reproduced on the retired convention the numbers come out at $-0.132224$ and $-0.005936$, matching what was published. On the live convention the same elements are $+0.408$ and $+0.544$, and the $\sigma_0$ channel is positive at *every* step of the typed build. There is no instability, deeper or otherwise, and so no depth difference to carry a mass split.

Note the sequence, because it is the point: correcting the crossing count removed the $4$-versus-$2$ asymmetry and moved the surviving claim onto the two numbers that are themselves convention artefacts. Both corrections are needed; neither alone finishes the paragraph.

What replaces it is open. Nothing is offered here — the derivation needs re-deriving rather than patching, and the [gluon ledger](#rem:gluon-stabiliser-ledger) carries the full measurement.

What survives unchanged is the *scope* of the enumeration: every non-trivial braid word inside the crossing cap, the trefoil word $e^-$ included, admissible and simply losing the minimisation.

**Step 3: Neutron NF (with Hopf gluon).**
At $q_0 \approx 1.1100$:

See [Table](#tbl:categorical-neutron-table-data).

$$
  \mathrm{net}(\mathfrak{n}) = +0.7976
$$

Relative to the proton ($\mathrm{net} = +1.0065$), the additional down quark demands a larger $L_+$ compensation ($-0.2206$ versus $-0.1114$). After Hopf gluon stabilisation, the trefoil channel $e^- \approx +1.0$ dominates both nucleons.

**Transition: proton $\to$ neutron.**
The normal-form difference yields the dimensionless $\beta$-decay transition ([energy scale](#rem:beta-decay-energy-scale)):

$$
  \Delta\mathrm{net}(\mathfrak{n} - \mathfrak{p})
  = 0.7976 - 1.0065 = -0.2089
$$

The uniform energy scale $\mathfrak{E}_0 = \mathfrak{Q}_\beta / |\Delta\mathrm{net}| \approx 4.155$ MeV converts these coefficient differences directly to MeV ([formation chain](#rem:meson-to-proton-via-borromean)).

**Mass.**

$$
  \mathfrak{m}_{\mathfrak{n}} =
  2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q) + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q)
$$

At the CODATA value $q_0$, the base mass is $\mathfrak{m}_{\mathfrak{n}}(q_0) \approx {{ qou.computations.codata-masses.data.m_n_MeV | precision: 6 }}\;\text{MeV}$ MeV, derived strictly from the substrate parameter ([local substrate](#prop:local-substrate-q)). The resulting proton--neutron mass splitting is exactly:

$$
  \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} =
  \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  \approx 1.293 \text{ MeV}
$$

This splitting arises from the Skein resolution asymmetry between the $\mathfrak{u}\text{-}\mathfrak{u}$ and $\mathfrak{d}\text{-}\mathfrak{d}$ crossing pairs within the rigid $\mathcal{B}_3$ structure.

**Coulomb charge.**

$$
  Q(\mathfrak{n}) =
  1 \cdot (+\tfrac{2}{3}) + 2 \cdot (-\tfrac{1}{3}) = 0.
$$

The sum vanishes, and the arithmetic is the Standard Model's. What it is **not** is a consequence of the crossing-orientation mechanism. This block previously read that the single positive-orientation unknot $\mathfrak{u}$ *cancels* two negative-orientation unknots $\mathfrak{d}$; one object cannot cancel two of equal magnitude. The cancellation above works only because $|Q_{\mathfrak{u}}| = 2|Q_{\mathfrak{d}}|$, and orientation reversal is a mirror, so it forces the two magnitudes to be *equal* ([down quark](#def:down-quark)). Writing $Q(\mathfrak{u}) = a$ and hence $Q(\mathfrak{d}) = -a$, the neutron carries $a - 2a = -a$ and the proton $2a - a = +a$: the mechanism makes the neutron the proton's exact opposite, and a neutral neutron forces every quark charge to vanish (`QOU.Braiding.mirror_odd_neutral_neutron_forces_zero`, sorry-free). The quark charges are therefore an adopted input here, not a derived one. The inter-neutron Hopf crossings acquire the $q^{-1}$ coefficient associated with negative crossings.
