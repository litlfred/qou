**Proposition (Hoefsmit binding amplitude).**
*The off-diagonal element $b$ of the Hoefsmit seminormal matrix
for the standard representation $(2,1)$ of $H_3(q)$ satisfies*

$$
  b^2 = \frac{[3]_q}{[2]_q^2},
  \qquad
  1 - b^2 = \frac{1}{[2]_q^2}.
$$

**Mathematical Novelty.** While the computation of the Hoefsmit seminormal matrix is a standard algebraic procedure within Hecke representation theory, the mathematical novelty is demonstrating that this specific exact rational relation ($1-b^2 = 1/[2]_q^2$) directly governs the discrete geometric de-entanglement fraction of the pion's mass, reinterpreting an abstract representation-theoretic off-diagonal matrix element as a topological binding constraint.

$$

## Physical interpretation: pion decay

The binding amplitude $b$ governs the entanglement of the two
lepton channels $V_{(2)} \oplus V_{(1,1)}$ inside the meson's
standard representation
([`prop:frobenius-lepton-meson-bridge`](frobenius-lepton-meson-bridge.md)):

- $b = 0$: the $(2,1)$ block diagonalises $\to$ the lepton channels
  decouple $\to$ no meson binding (free leptons).
- $b \ne 0$: the off-diagonal element mixes $V_{(2)}$ and
  $V_{(1,1)}$ $\to$ meson exists as an entangled lepton pair.

The pion decay $\pi \to \mu + \nu$ releases a fraction
$1 - b^2 = 1/[2]_q^2$ of the pion's rest energy as
de-entanglement energy:

$$
  E_{\mathrm{bind}} = \frac{m_\pi}{[2]_q^2}.
$$

The remaining energy is $m_\pi \cdot b^2
= m_\pi \cdot [3]_q / [2]_q^2$.  By the Frobenius bridge,
this residual energy flows into the de-entangled lepton channel
(the $V_{(2)}$ component of $V_{(2,1)}\!\downarrow_{H_2}$),
consistent with the dominant pion decay mode
$\pi^+ \to \mu^+ + \nu_\mu$.

## The $q$-integer structure

The identities $b^2 = [3]_q/[2]_q^2$ and $1 - b^2 = 1/[2]_q^2$
are exact in $q$ — they hold for all $q$, not just $q_0$.  The
pion decay fraction is a **universal algebraic identity** of the
Hecke algebra, independent of the substrate parameter.
