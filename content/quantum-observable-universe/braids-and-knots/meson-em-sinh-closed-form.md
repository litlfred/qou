**Proposition (meson EM sinh-channel closed-form).**
*Let $R$ be a field and $q \in R^\times$. Writing the substrate Planck
quantum $\hbar_q = (q - 1)/q$, the following are equal:*

$$
  1 + \hbar_q - \hbar_q^2/2
  \;=\;
  1 + \frac{1 - q^{-2}}{2}
  \;=\;
  \frac{3 - q^{-2}}{2}
  \;=\;
  \frac{3 q^2 - 1}{2 q^2}.
$$

## Proof

The four expressions are equal as rational functions of $q$ over any
field with $q \ne 0$. Starting from the leftmost, expand
$\hbar_q^2 = (1 - q^{-1})^2 = 1 - 2 q^{-1} + q^{-2}$, so

$$
  1 + \hbar_q - \tfrac{1}{2}\hbar_q^2
  = 1 + (1 - q^{-1}) - \tfrac{1}{2}(1 - 2 q^{-1} + q^{-2})
  = \tfrac{3}{2} - \tfrac{1}{2} q^{-2}
  = \frac{3 - q^{-2}}{2}.
$$

Multiplying numerator and denominator by $q^2$ gives
$(3 q^2 - 1)/(2 q^2)$. The Lean formalisation closes each step with
`field_simp; ring`. $\square$

## Significance: the meson $m_K^2/m_\pi^2$ closure form

Substituting the closed form into the meson mass-squared ratio gives
a **single closed-form derived expression** for the full
$m_K^2 / m_\pi^2$ ratio:

$$
  \frac{m_K^2}{m_\pi^2}
  \;=\;
  [3]_q \cdot [4]_q
  \;+\;
  \frac{\alpha_{\mathrm{em}}}{\pi}
  \cdot
  \frac{3 q^2 - 1}{2 q^2}.
$$

Both pieces are framework-derived (no fitted integers): the strong
fusion $[3]_q \cdot [4]_q$ from the qq̄ 2-body decomposition
([`prop:meson-qcg-fusion-identity`](#prop:meson-qcg-fusion-identity)),
and the sinh-channel EM correction from the CS-corrected
$\alpha_{\mathrm{em}} = q \cdot [9]_q \cdot [10]_q$ ([force-carrier
Diophantine uniqueness](#prop:force-carrier-bring-uniqueness))
multiplied by $(3 q^2 - 1)/(2 q^2)$.

(See [`docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md`](../../../docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md)
for the archimedean substrate evaluation.)

## Structural reading

The numerator $3 q^2 - 1$ has a Bring-surface generation structure:
**3** is the number of saturating-genus generation torus knots
$T_{2,3}, T_{2,5}, T_{2,7}$ on Bring's surface (per the same
Diophantine uniqueness that fixes the force-carrier set), and $q^2$
is the substrate's squared coupling. The denominator $2 q^2$
contributes the standard EM-self-energy halving (Casimir) and puts
the correction on the substrate-natural scale. Per
[`prop:cosh-sinh-q-bridge`](#prop:cosh-sinh-q-bridge) (#1417, $[n]_q
= \sinh(n\lambda)/\sinh(\lambda)$ with $\sinh$ = Coulomb channel),
this is the sinh-side categorical-action correction on the qq̄ pair,
modulo a rigorous first-principles derivation of the
$\hbar_q - \hbar_q^2/2$ truncation order.
