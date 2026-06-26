**Proposition (Frobenius lepton–meson bridge).**
*The standard representation $V_{(2,1)}$ of $H_3(q)$ restricts to
$H_2(q)$ as the direct sum of the two lepton irreps:*

$$
  V_{(2,1)} \big\downarrow_{H_2}
  = V_{(2)} \oplus V_{(1,1)}.
$$

*The meson sector's sole mass-carrying partition is the
**entangled** lepton spectrum.*

**Proof.** The branching rule $H_3 \downarrow H_2$ follows from
the Pieri / Littlewood–Richardson rule for removing a box from the
Young diagram.  For each partition $\lambda \vdash 3$:

$$
  V_{(3)} \downarrow = V_{(2)}, \qquad
  V_{(2,1)} \downarrow = V_{(2)} \oplus V_{(1,1)}, \qquad
  V_{(1^3)} \downarrow = V_{(1,1)}.
$$

The standard representation $(2,1)$ admits removal of a box from
either the first row (giving $(2)$) or the second row (giving
$(1,1)$), hence the two-term decomposition.  $\square$

## The entanglement interpretation

At $H_2$, the lepton irreps $V_{(2)}$ and $V_{(1,1)}$ are
**separate channels**: the electron mass formula evaluates them
independently, with eigenvalues $q$ and $-q^{-1}$.  The
figure-eight knot volume $\mathrm{Vol}(4_1)$ measures the
transition **between** these channels.

At $H_3$, the same two channels are **entangled** inside the
$2 \times 2$ Hoefsmit block of $V_{(2,1)}$.  The off-diagonal
element

$$
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
  \qquad
  a_\rho = \frac{h}{1 - q^{-2\rho}},
$$

is the **binding amplitude** that prevents the lepton channels
from decoupling.  When $b = 0$ (no binding), the $(2,1)$ block
becomes diagonal and the meson reverts to two independent leptons.
When $b \ne 0$, the channels mix — this is the Hopf link binding.

## Frobenius reciprocity and the mass-ratio correspondence

By Frobenius reciprocity:

$$
  \langle \mathrm{Res}(V_{(2,1)}), V_{(2)} \rangle_{H_2}
  = \langle V_{(2,1)}, \mathrm{Ind}(V_{(2)}) \rangle_{H_3}
  = 1.
$$

Each lepton irrep appears **exactly once** in the restriction.
This means:

1. The **lepton mass ratio** $m_\mu / m_\mathfrak{e}$ measures
   the separated $V_{(2)} \leftrightarrow V_{(1,1)}$ transition
   (the figure-eight volume between the two 1-dim channels).

2. The **meson mass ratio** $m_K / m_\pi$ measures the same
   transition but **inside** the entangled $(2,1)$ block — the
   Hoefsmit $2 \times 2$ matrix encodes both channels simultaneously.

3. The **Hoefsmit off-diagonal $b$** is the bridge: it is the
   amplitude at which the lepton pair-channel becomes the meson
   binding channel.  At $b \to 0$: leptons (no binding).
   At $b \ne 0$: mesons (Hopf binding).

## Connection to $C$ versus bar

The branching also explains
[`prop:c-equals-bar-iff-all-1dim`](../../particle-interactions/c-equals-bar-iff-all-1dim.md):

- At $H_2$: $V_{(2)}$ and $V_{(1,1)}$ are separate 1-dim irreps,
  so $C = \mathrm{bar}$ (charge conjugation = bar involution).
- At $H_3$: $V_{(2,1)}$ entangles them into a 2-dim irrep, and
  the off-diagonal $b$ breaks the $C = \mathrm{bar}$ equivalence.

The standard representation is WHERE:
- the two lepton channels merge (branching),
- $C$ and bar diverge (symmetry breaking),
- the meson mass lives (SDP active set).

All three phenomena are the **same algebraic fact**: the appearance
of a multi-dimensional irrep in the Hecke tower.
