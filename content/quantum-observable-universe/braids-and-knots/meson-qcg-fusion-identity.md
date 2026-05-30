**Proposition (q-Clebsch–Gordan fusion identity).**
*Let $R$ be a field and $q \in R^\times$. The q-integers satisfy*

$$
  [3]_q \cdot [4]_q \;=\; [2]_q + [4]_q + [6]_q.
$$

*This is the q-deformation of the classical SU(2) Clebsch–Gordan
identity $\mathrm{spin}\text{-}1 \otimes \mathrm{spin}\text{-}\tfrac{3}{2}
= \mathrm{spin}\text{-}\tfrac{1}{2} \oplus \mathrm{spin}\text{-}\tfrac{3}{2}
\oplus \mathrm{spin}\text{-}\tfrac{5}{2}$ (dimensions $3 \cdot 4 = 2 + 4 + 6$).*

## Proof

Using $[n]_q = (q^n - q^{-n})/(q - q^{-1})$, multiply both sides by
$(q - q^{-1})^2$ to clear denominators. The identity becomes the
ring identity

$$
  (q^3 - q^{-3})(q^4 - q^{-4})
  \;=\;
  (q - q^{-1}) \cdot
  \bigl((q^2 - q^{-2}) + (q^4 - q^{-4}) + (q^6 - q^{-6})\bigr),
$$

which holds in any field with $q \ne 0$ by direct expansion (`ring`
in the Lean formalisation). $\square$

## Significance

This identity is the *categorical* content behind the meson mass-squared
ratio $m_K^2 / m_\pi^2$. A meson $M = q_1 \bar q_2$ is a **2-body** state
on $H_{q_1} \otimes H_{q_2}$, so its mass-squared is a bilinear (Casimir-
like) quantity on the *pair* — a fusion product, not a 1-body character.
The 1-body Hecke character ratio for the kaon vs pion misses
$m_K / m_\pi$ by 71%; the 2-body **squared** ratio
$m_K^2/m_\pi^2$ is the genuinely-derived target, and the right q-fusion
is precisely $[3]_q \cdot [4]_q$ — verified at $q_0$ to 203 ppm with
**zero fitted integers** (see audit
[2026-05-28-meson-mass-ratio-derived-vs-fitted.md](../../../docs/audits/2026-05-28-meson-mass-ratio-derived-vs-fitted.md)).

The remaining 203 ppm residual is the EM/Coulomb (sinh-channel)
correction, closed to **0.056 ppm on the full ratio** by
$(\alpha_{\mathrm{em}}/\pi) \cdot (1 + \hbar_q - \hbar_q^2/2)$ — the
first three terms of $1 + \log(1 + \hbar_q)$, where $\hbar_q$ is the
universal substrate Planck quantum (also ubiquitous in the Habiro
bridge, deuteron binding, and flavor split). Both ingredients are
framework-derived; the derived-candidate exact closure form is the
sinh-channel categorical action open piece.
