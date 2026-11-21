---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-007-26-parametrisation
section_title: "Parametrisation"
section_number: 2.6
pages: 9-9
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.984
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a single real"
---
For later purposes, we now give a parametrisation of an octonion by its $(1,0)$ and $(0,1)$ coordinates. The $(1,0)$ coordinates of eigenvalue of $E^4$ of $-{\rm i\,}$ are given by $$\begin{aligned}
L:= x_0-{\rm i\,}x_4, \quad Q_i = x_i -{\rm i\,}x_{i+4},
\end{aligned}$$ where we introduced suggestive names. An octonion $x$ with coordinates $x_0,x_1,\ldots, x_7$ is then parametrised as $$\begin{aligned}
x_0 = \frac{1}{2}( L+ \bar{L}), \quad x_4= \frac{{\rm i\,}}{2}(L-\bar{L}), \quad x_i = \frac{1}{2}( Q_i +\bar{Q}_i), \quad x_{i+4} = \frac{{\rm i\,}}{2} ( Q_i - \bar{Q}_i).
\end{aligned}$$ Here the bar is both part of the name, as well as the complex conjugation that maps between the eigenspaces $(1,0), (0,1)$ of the complex structure $J$. Another complex structure and its related complex conjugation will appear later when we consider ${\rm Spin}(4,3)$. It will be important to distinguish them.

For later purposes, we give formulas for various useful pairings in this parametrisation $$\begin{aligned}
\label{O-formulas-1}
\langle x, x \rangle = \bar{L}L + \bar{Q}^i Q^i, \\ \nonumber
\langle x, (E^1-{\rm i\,}E^5)(E^2-{\rm i\,}E^6)(E^3-{\rm i\,}E^7) x \rangle= -4{\rm i\,}L^2, \\ \nonumber
\langle x, (E^1 E^5 + E^2 E^6+E^3 E^7)E^4 x \rangle = -3 \bar{L}L + \bar{Q}^i Q^i,
\end{aligned}$$ where the summation convention is implied. We will also need versions of these formulas with two different octonions paired. We have $$\begin{aligned}
\label{O-formulas-2}
\langle x_1, x_2 \rangle = \frac{1}{2}\left( \bar{L}_1 L_2 + \bar{L}_2 L_1  + \bar{Q}^i_1 Q^i_2 + \bar{Q}^i_2 Q^i_1\right), \\ \nonumber
\langle x_1, E^4 x_2 \rangle = \frac{{\rm i\,}}{2} \left( -\bar{L}_1 L_2 + \bar{L}_2 L_1  - \bar{Q}^i_1 Q^i_2 + \bar{Q}^i_2 Q^i_1\right), \\ \nonumber
\langle x_1, (E^1 E^5+E^2 E^6 +E^3 E^7) x_2 \rangle = \frac{{\rm i\,}}{2}\left( -3\bar{L}_1 L_2 + 3\bar{L}_2 L_1  - \bar{Q}^i_1 Q^i_2 + \bar{Q}^i_2 Q^i_1\right).
\end{aligned}$$ We will need these results when we compute the Yukawa mass terms.
