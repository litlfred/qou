**Proposition (Hoefsmit binding amplitude).**
*The off-diagonal element $b$ of the Hoefsmit seminormal matrix
for the standard representation $(2,1)$ of $H_3(q)$ satisfies*

$$
  b^2 = \frac{[3]_q}{[2]_q^2},
  \qquad
  1 - b^2 = \frac{1}{[2]_q^2}.
$$

**Mathematical Novelty.** Computing the Hoefsmit seminormal matrix is standard in Hecke representation theory. The novelty lies in showing the exact rational relation $1-b^2 = 1/[2]_q^2$ governs the geometric de-entanglement fraction of the pion's mass. This reinterprets an off-diagonal matrix element as a topological binding constraint.

## Physical interpretation: pion decay

The binding amplitude $b$ dictates the entanglement of the lepton channels $V_{(2)} \oplus V_{(1,1)}$ within the meson's standard representation ([`prop:frobenius-lepton-meson-bridge`](frobenius-lepton-meson-bridge.md)):

- $b = 0$: The $(2,1)$ block diagonalises. The lepton channels decouple. No meson binds.
- $b \ne 0$: The off-diagonal element mixes $V_{(2)}$ and $V_{(1,1)}$. The meson forms as an entangled lepton pair.

The pion decay $\pi \to \mu + \nu$ releases the fraction $1 - b^2 = 1/[2]_q^2$ of the pion's rest energy as de-entanglement energy:

$$
  E_{\mathrm{bind}} = \frac{m_\pi}{[2]_q^2}.
$$

The remaining energy is $m_\pi \cdot b^2 = m_\pi \cdot [3]_q / [2]_q^2$. The Frobenius bridge directs this residual energy into the de-entangled lepton channel (the $V_{(2)}$ component of $V_{(2,1)}\!\downarrow_{H_2}$). This matches the dominant pion decay mode $\pi^+ \to \mu^+ + \nu_\mu$.

## The $q$-integer structure

The identities $b^2 = [3]_q/[2]_q^2$ and $1 - b^2 = 1/[2]_q^2$ are exact in $q$. They hold for all $q$, independent of the substrate parameter $q_0$. The pion decay fraction forms a universal algebraic identity of the Hecke algebra.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs—real-valued physical observables, analytical bounds, transcendental constants, or numerical evaluations at $q_0$. Any categorical $q$-deformation identities it draws upon remain valid over an abstract coefficient ring; we only specialise their archimedean realisations here.
