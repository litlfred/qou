**Proposition (Hoefsmit binding amplitude).**
*The off-diagonal element $b$ of the Hoefsmit seminormal matrix
for the standard representation $(2,1)$ of $H_3(q)$ satisfies*

$$
  b^2 = \frac{[3]_q}{[2]_q^2},
  \qquad
  1 - b^2 = \frac{1}{[2]_q^2}.
$$

**Proof.** The Hoefsmit seminormal matrix for $\sigma_2$ on
$V_{(2,1)}$ has a $2 \times 2$ block with entries

$$
  a_\rho = \frac{h}{1 - q^{-2\rho}},
  \qquad
  a_{-\rho} = \frac{h}{1 - q^{2\rho}},
  \qquad
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
$$

where $\rho = 2$ is the axial distance and $h = q - q^{-1}$.
The product of the diagonal entries is

$$
  a_\rho \cdot a_{-\rho}
  = \frac{h^2}{(1 - q^{-4})(1 - q^4)}
  = \frac{h^2}{-(h^2)(h^2 + 4)}
  = -\frac{1}{h^2 + 4}
  = -\frac{1}{[2]_q^2}.
$$

Therefore $b^2 = -1/[2]_q^2 + 1 = ([2]_q^2 - 1)/[2]_q^2$.
Since $[2]_q^2 = (q + q^{-1})^2 = h^2 + 4$ and
$[3]_q = q^2 + 1 + q^{-2} = h^2 + 3 = [2]_q^2 - 1$:

$$
  b^2 = \frac{[2]_q^2 - 1}{[2]_q^2} = \frac{[3]_q}{[2]_q^2}.
  \qquad\square
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
