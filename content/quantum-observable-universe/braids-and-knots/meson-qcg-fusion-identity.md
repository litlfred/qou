**Proposition (q-Clebsch–Gordan fusion identity).**
*Let $R$ be a field and $q \in R^\times$. The q-integers satisfy*

$$
  [3]_q \cdot [4]_q \;=\; [2]_q + [4]_q + [6]_q.
$$

*This is the q-deformation of the classical SU(2) Clebsch–Gordan
identity $\mathrm{spin}\text{-}1 \otimes \mathrm{spin}\text{-}\tfrac{3}{2}
= \mathrm{spin}\text{-}\tfrac{1}{2} \oplus \mathrm{spin}\text{-}\tfrac{3}{2}
\oplus \mathrm{spin}\text{-}\tfrac{5}{2}$ (dimensions $3 \cdot 4 = 2 + 4 + 6$).*

## Significance

This identity provides the categorical structure for the meson mass-squared ratio $m_K^2 / m_\pi^2$. We model a meson $M = q_1 \bar q_2$ as a 2-body state on $H_{q_1} \otimes H_{q_2}$. Its mass-squared evaluates as a bilinear (Casimir-like) quantity on the pair, forming a fusion product rather than a 1-body character. While the 1-body Hecke character ratio misses the empirical $m_K / m_\pi$ substantially, the 2-body squared ratio matches precisely via the q-fusion product $[3]_q \cdot [4]_q$.

The numerical substrate evaluation incorporates the exact sinh-channel closure form, validating this formulation with framework-derived values and no fitted integers (detailed in [`docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md`](../../../docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md)). This block isolates the categorical fusion identity.

**Mathematical Novelty:** The identity $[3]_q[4]_q=[2]_q+[4]_q+[6]_q$ follows from standard q-representation theory. The novel, framework-specific insight is its application to the 2-body meson $m_K^2/m_\pi^2$ squared-ratio rather than a 1-body character.
