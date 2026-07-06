**Proposition (Frobenius lepton–meson bridge).**
*The standard representation $V_{(2,1)}$ of $H_3(q)$ restricts to $H_2(q)$ as the direct sum of the two lepton irreps:*

$$
  V_{(2,1)} \big\downarrow_{H_2}
  = V_{(2)} \oplus V_{(1,1)}.
$$

*The meson sector's sole mass-carrying partition is the **entangled** lepton spectrum.*

## The entanglement interpretation

At $H_2$, the lepton irreps $V_{(2)}$ and $V_{(1,1)}$ are separate channels. The electron mass formula evaluates them independently, with eigenvalues $q$ and $-q^{-1}$. The figure-eight knot volume $\mathrm{Vol}(4_1)$ measures the transition between these channels.

At $H_3$, the same two channels are entangled inside the $2 \times 2$ Hoefsmit block of $V_{(2,1)}$. The off-diagonal element

$$
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
  \qquad
  a_\rho = \frac{h}{1 - q^{-2\rho}},
$$

is the binding amplitude that prevents the lepton channels from decoupling. When $b = 0$ (no binding), the $(2,1)$ block becomes diagonal and the meson reverts to two independent leptons. When $b \ne 0$, the channels mix. This is the Hopf link binding.

## Frobenius reciprocity and the mass-ratio correspondence

By Frobenius reciprocity:

$$
  \langle \mathrm{Res}(V_{(2,1)}), V_{(2)} \rangle_{H_2}
  = \langle V_{(2,1)}, \mathrm{Ind}(V_{(2)}) \rangle_{H_3}
  = 1.
$$

Each lepton irrep appears exactly once in the restriction. This has the following consequences:

1. The lepton mass ratio $m_\mu / m_\mathfrak{e}$ measures the separated $V_{(2)} \leftrightarrow V_{(1,1)}$ transition (the figure-eight volume between the two 1-dim channels).
2. The meson mass ratio $m_K / m_\pi$ measures the same transition, but inside the entangled $(2,1)$ block. The Hoefsmit $2 \times 2$ matrix encodes both channels simultaneously.
3. The Hoefsmit off-diagonal $b$ is the bridge. It is the amplitude at which the lepton pair-channel becomes the meson binding channel. At $b \to 0$, we have leptons (no binding). At $b \ne 0$, we have mesons (Hopf binding).

## Connection to $C$ versus bar

The branching also explains [`prop:c-equals-bar-iff-all-1dim`](../../particle-interactions/c-equals-bar-iff-all-1dim.md):

- At $H_2$, $V_{(2)}$ and $V_{(1,1)}$ are separate 1-dim irreps. Therefore $C = \mathrm{bar}$ (charge conjugation equals bar involution).
- At $H_3$, $V_{(2,1)}$ entangles them into a 2-dim irrep. The off-diagonal $b$ breaks the $C = \mathrm{bar}$ equivalence.

The standard representation is where three things happen:
- The two lepton channels merge (branching).
- $C$ and bar diverge (symmetry breaking).
- The meson mass lives (SDP active set).

All three phenomena are the same algebraic fact: the appearance of a multi-dimensional irrep in the Hecke tower.
