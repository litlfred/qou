---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-002-2-sextic-integrals-and-dilogarithm-identities
section_title: "Sextic integrals and dilogarithm identities"
section_number: 2
pages: 4-7
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.994
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
[]{#sectionsextic label="sectionsextic"} One of the main tools to be applied in this paper is given by the functional equations involved in Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"} below. For our derivation of this Theorem, we require the integral identities such that $$\label{integrandforsum1}
 \int_{0}^{h} \frac{(1 - y)^c y^d}{1 + g^2 (1 - y)^a y^b} \, dg = (1 - y)^{c - \frac{a}{2}} y^{d - \frac{b}{2}} 
 \operatorname{arctan}\left( h (1 - y)^{\frac{a}{2}} y^{\frac{b}{2}} \right)$$ for $\Re\left( \frac{ \left( 1 - y \right)^{-a/2} y^{-b/2} }{h} \right) \neq 0$ and such that $$\label{integrandforsum2}
 \int_0^h \frac{(1 - y)^c y^d}{\sqrt{1 - g^2 (1 - y)^a y^b}} \, dg = (1 - y)^{c - \frac{a}{2}} y^{d - 
 \frac{b}{2}} \text{arcsin}\left( h (1 - y)^{\frac{a}{2}} y^{\frac{b}{2}} \right)$$ for $\Re\left( \frac{ \left( 1 - y \right)^{-a/2} y^{-b/2} }{h} \right) > 1$ and for $\Re\left( \frac{1}{h \sqrt{ -(1-y)^{a} y^{b} }} \right) \neq 0$. We refer to such integrals as *sextic integrals*, in reference ot the sixfold combinations of parameters involved in each of [\[integrandforsum1\]](#integrandforsum1){reference-type="eqref" reference="integrandforsum1"} and [\[integrandforsum2\]](#integrandforsum2){reference-type="eqref" reference="integrandforsum2"}. In view of the integrands among [\[integrandforsum1\]](#integrandforsum1){reference-type="eqref" reference="integrandforsum1"} and [\[integrandforsum2\]](#integrandforsum2){reference-type="eqref" reference="integrandforsum2"}, we are to also make use of the power series identities such that $$\label{powersum1}
 \sum_{n=0}^{\infty} (-1)^n g^{2n} y^{bn} (1 - y)^{an} = \frac{1}{1 + g^2 (1 - y)^a y^b}$$ and such that $$\label{powersum2}
 \sum_{n=0}^{\infty} g^{2n} y^{bn} (1 - y)^{an} \frac{ \left( \frac{1}{2}
 \right)_n}{(1)_n} = \frac{1}{\sqrt{1 - g^2 (1 - y)^a y^b}}$$ for a suitable radius of convergence. Informally, by multiplying both sides of [\[powersum1\]](#powersum1){reference-type="eqref" reference="powersum1"} by the integrand factors indicated in [\[displayw1\]](#displayw1){reference-type="eqref" reference="displayw1"} and [\[displayw2\]](#displayw2){reference-type="eqref" reference="displayw2"} below, and by then using the dominated convergence theorem to apply term-by-term integration to the infinite sums that we obtain from [\[powersum1\]](#powersum1){reference-type="eqref" reference="powersum1"} and [\[powersum2\]](#powersum2){reference-type="eqref" reference="powersum2"}, we would then use the beta integral identity in [\[betaevaluate\]](#betaevaluate){reference-type="eqref" reference="betaevaluate"}, following a similar approach as in our past work [@Hakimoglupreprint], with the equality of the values $w_{1}$ and $w_{2}$ shown in [\[displayw1\]](#displayw1){reference-type="eqref" reference="displayw1"} and [\[displayw2\]](#displayw2){reference-type="eqref" reference="displayw2"} providing a key tool in our work.

We make use of the notational shorthand such that $$\left[ \begin{matrix} \alpha, \beta, \ldots, \gamma \vspace{1mm} \\ 
 A, B, \ldots, C \end{matrix} \right]_{n} = \frac{ (\alpha)_{n} (\beta)_{n} 
 \cdots (\gamma)_{n} }{ (A)_{n} (B)_{n} \cdots (C)_{n}}.$$ From the sextic integral relation in [\[integrandforsum1\]](#integrandforsum1){reference-type="eqref" reference="integrandforsum1"}, we obtain that $$\label{addedexplanation1}
 \frac{ \operatorname{arctan}\left( h (1 - y) \sqrt{y} \right) }{2 h y} = \int_{0}^{h} 
 \frac{1-y}{2 h \sqrt{y} \left(1 + g^2 (1-y)^2 y \right)} \, dg,$$ and, from the power series expansion in [\[powersum1\]](#powersum1){reference-type="eqref" reference="powersum1"}, we obtain that $$\label{addedexplanation2}
 \frac{1-y}{2 h \sqrt{y} \left(1 + g^2 (1-y)^2 y \right)} 
 = \frac{1}{2h } \sum_{n=0}^{\infty} (-1)^{n} g^{2n} y^{n - \frac{1}{2}} (1-y)^{2n+1},$$ and from [\[addedexplanation1\]](#addedexplanation1){reference-type="eqref" reference="addedexplanation1"} and [\[addedexplanation2\]](#addedexplanation2){reference-type="eqref" reference="addedexplanation2"} together, we obtain that $$\label{displayw1}
 w_1 = \int_0^1 \frac{\arctan\left(h (1 - y) \sqrt{y}\right)}{ 2 h y} \, dy = 
 \int_{0}^{1} \frac{ (3x^2 - 1) \ln x }{1 + h^2 x^2 (1-x^2)^2} \, dx
 = \frac{ 2 s_1}{3},$$ where $s_1$ is such that $$\label{displays1}
 s_1 = \sum_{n=0}^{\infty} 
 h^{2n} \left( -\frac{4}{27} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, \frac{1}{2}, 1 
 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n}.$$ A symmetric approach gives us the companion to [\[displayw1\]](#displayw1){reference-type="eqref" reference="displayw1"} such that $$\label{displayw2}
 w_2 = \int_0^1 \frac{\arctan\left(h (1 - y) \sqrt{y}\right)}{h(1 - y)} \, dy 
 = \int_{0}^{1} \frac{ (1-3x^2) \ln(1-x^2) }{1 + h^2 x^2 (1-x^2)^2} \, dx = \frac{ 2 s_1}{3},$$ and the key insight associated with one of the main techniques in this paper is given by how $\frac{w_1}{w_2}$ is a constant, as this can be used, as we demonstrate, to produce dilogarithm identities via a "shifting" applied related ${}_{4}F_{3}$-series.

Our method may be thought of as having the advantage of avoiding the double integrals required in the related work of Batir [@Batir2005]. By iterating substitutions and taking multiple integrals that may be expressed as [\[displays1\]](#displays1){reference-type="eqref" reference="displays1"} in terms of $g$, it is typically feasible to compute order-$n$ polylogarithms without having to compute a multivariable integral of [\[powersum1\]](#powersum1){reference-type="eqref" reference="powersum1"}. For example, applying our iterative approach in a twofold manner using [\[integrandforsum2\]](#integrandforsum2){reference-type="eqref" reference="integrandforsum2"} and [\[powersum2\]](#powersum2){reference-type="eqref" reference="powersum2"}, we obtain $$\begin{gathered}
 s_2 = \int_0^1 \frac{x(1 - 3x^2) \arcsin \left( g x (x^2 - 1) \right)}{x^2 - 1} \, dx = \\ 
 g\int_0^1 \frac{\left( \frac{3}{2}(x^2 - 1) + \ln(x^2 - 1) \right) (3x^2 - 1)}{\sqrt{1 - g^2 x^2 (x^2 - 1)^2}} \, dx, 
\end{gathered}$$ writing $$s_2 = -\frac{4g}{15} \sum_{n=0}^{\infty} g^{2n} \left( \frac{4}{27} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, \frac{1}{2}, \frac{1}{2} 
 \vspace{1mm} \\ 
 \frac{7}{6}, \frac{11}{6}, \frac{3}{2} \end{matrix} \right]_{n}.$$ By setting $g = ig_0$, and by then enforcing the substitution $g_0 = \frac{1}{u(1-u^2)}$, the denominator of the latter integrals among [\[displayw1\]](#displayw1){reference-type="eqref" reference="displayw1"} and [\[displayw2\]](#displayw2){reference-type="eqref" reference="displayw2"} factors into three quadratics, yielding the product $$\label{productforpartial}
 (u^2+ux+x^2-1)(u^2-ux+x^2-1)(u^2-x^2)$$ This leads us to our first main result below.

::: theorem
[]{#maintheorem label="maintheorem"} Let $$\begin{aligned}
 A & := \operatorname{Li}_2\left(\frac{\sqrt{4 - 3u^2} + u^2 - 2}{u (u + 1)}\right) 
 - \operatorname{Li}_2\left(\frac{\sqrt{4 - 3u^2} + u^2 - 2}{(u - 1) u}\right), \\ 
 B & := 
 \frac{1}{2} \ln^2\left(\frac{-i \sqrt{3 u^2-4}+u+2}{4} \right) - 
 \frac{1}{2} \ln ^2\left(\frac{- i \sqrt{3 u^2 - 4} - u^2 +2}{u 
 (u+1)}\right) + \\ 
 & \quad \frac{1}{2} \ln ^2\left(\frac{i \sqrt{3 u^2 - 4} + u + 2}{4} \right)-\frac{\pi ^2}{6}, \\ 
 J & := \frac{1}{4} \ln^2 \left( \frac{-4}{-i \sqrt{3 u^2 - 4} + u + 2} \right) + 
 \frac{1}{4} \ln^2 \left( \frac{-4}{i \sqrt{3 u^2 - 4} + u + 2} \right) - \\ 
 &\quad \frac{1}{4} \ln^2 \left( \frac{-4}{-i \sqrt{3 u^2 - 4} - u + 2} \right) - \frac{1}{4} 
 \ln^2 \left( \frac{-4}{i \sqrt{3 u^2 - 4} - u + 2} \right), \\ 
 C & := - \frac{1}{2} \ln \left( \frac{ - i \sqrt{3 u^2 - 4} + u + 
 2}{4} \right) \ln \left( \frac{ i \sqrt{3 u^2 - 4} - u + 2}{4} \right) - \\ 
 & \quad \frac{1}{2} \ln \left( \frac{i \sqrt{3 u^2 - 4} + u + 2}{4} \right) 
 \ln \left( \frac{- i \sqrt{3 u^2 - 4} - u + 2}{4} \right) + \frac{\pi^2}{6}, \\ 
 H & := 
 \frac{1}{4} \ln^2\left(\frac{2}{u-1}\right)-\frac{1}{4} \ln ^2\left(-\frac{2}{u+1}\right)+\frac{1}{2} \ln \left(\frac{-u + 1}{2} \right) 
 \ln \left(\frac{u+1}{2}\right) - \\ 
 & \quad \frac{\pi i}{2} \ln \left(\frac{u + 
 1}{u-1}\right)-\ln (2) \ln \left(\frac{u+1}{u-1}\right)-\frac{\pi^2}{12}, \\ 
 D & := \operatorname{Li}_2 \left( \frac{1 - u}{2} \right) 
 + \ln(2) \ln \left( \frac{u - 1}{u + 1} \right) + \left( 2 \ln(2) + \frac{\pi i}{2} \right) \ln \left( \frac{u + 
 1}{u - 1} \right), \\ 
 K & := \frac{1}{2} \operatorname{Li}_2 \left( \frac{2}{- \sqrt{4 - 3 u^2} + u} \right) - 
 \frac{1}{2} \operatorname{Li}_2 \left( \frac{2}{\sqrt{4 - 3 u^2} - u} \right) \\ 
 &\quad - \frac{1}{2} \operatorname{Li}_2 \left( \frac{-2}{\sqrt{4 - 3 u^2} + u} \right) + 
 \frac{1}{2} \operatorname{Li}_2 \left( \frac{2}{\sqrt{4 - 3 u^2} + u} \right) + 
 \frac{1}{2} \operatorname{Li}_2 \left( \frac{-1}{u} \right) - 
 \frac{1}{2} \operatorname{Li}_2 \left( \frac{1}{u} \right). 
\end{aligned}$$ Then, for all $u \in \mathbb{C} \setminus \mathbb{R}$ such that $\Re u \geq 0$ and such that the power series in [\[displays3\]](#displays3){reference-type="eqref" reference="displays3"} converges, we have that $$\label{mainABCD}
 A + B + J + C + H + D = s_3 = K,$$ and that $$\label{MequalsAB}
 M = A + B = 
 - \operatorname{Li}_{2}\left( \frac{\sqrt{4 - 3 u^2} - u + 2}{4} \right) 
 - \operatorname{Li}_{2}\left( \frac{-\sqrt{4 - 3 u^2} - u + 2}{4} \right),$$ writing $$\label{displays3}
 s_3 = \frac{2}{3u(u^2-1)} \sum_{n=0}^{\infty} \left( \frac{1}{u(u^2-1)} \right)^{2n} \left( \frac{4}{27} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, \frac{1}{2}, 1 
 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n}.$$ Moreover, for $u \in \mathbb{R}_{\geq 0}$ such that [\[displays3\]](#displays3){reference-type="eqref" reference="displays3"} converges, by letting $v \in \mathbb{C} \setminus \mathbb{R}$ approach $u$ and taking the corresponding limits on all sides of the equalities among [\[mainABCD\]](#mainABCD){reference-type="eqref" reference="mainABCD"}, these limits are equal, and similarly for [\[MequalsAB\]](#MequalsAB){reference-type="eqref" reference="MequalsAB"}.
:::

::: proof
*Proof.* This follows from our sextic integral identities, by applying partial fraction decomposition to the reciprocal of the product in [\[productforpartial\]](#productforpartial){reference-type="eqref" reference="productforpartial"}, and by then applying this partial fraction decomposition within the appropriate integrands in [\[displayw1\]](#displayw1){reference-type="eqref" reference="displayw1"} and [\[displayw2\]](#displayw2){reference-type="eqref" reference="displayw2"}, and by then evaluating the indefinite integrals corresponding to the definite integrals we obtain by expanding the aforementioned integrands. More explicitly, in the latter equality in [\[displayw1\]](#displayw1){reference-type="eqref" reference="displayw1"}, we set $-\frac{i}{u \left(u^2-1\right)}$, yielding $$\begin{gathered}
 \int_{0}^{1} \frac{\left(3 x^2 - 
 1\right) \ln (x)}{\left(u^2+u x+x^2-1\right) \left(u^2-u x+x^2-1\right) \left(u^2-x^2\right)} \, dx = \\ 
 \frac{2}{3 (u-1)^2 u^2 (u+1)^2} \sum_{n=0}^{\infty} 
 \left( \frac{1}{u(u^2-1)} \right)^{2n} \left( \frac{4}{27} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, \frac{1}{2}, 1 
 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n}, 
\end{gathered}$$ and, by applying partial fraction decomposition to the above integrand, an indefinite integral corresponding to the resultant integrand is equivalent to $$\begin{gathered}
 \frac{1}{2 u-2 u^3} \Bigg( \operatorname{Li}_2\left(-\frac{2 x}{u-\sqrt{4-3 u^2}}\right) - 
 \operatorname{Li}_2\left(\frac{2 x}{u-\sqrt{4-3 u^2}}\right)+\operatorname{Li}_2\left(-\frac{2
 x}{u+\sqrt{4-3 u^2}}\right) - \\ 
 \operatorname{Li}_2\left(\frac{2 x}{u+\sqrt{4-3
 u^2}}\right)-\operatorname{Li}_2\left(-\frac{x}{u}\right)+\operatorname{Li}_2\left(\frac{x}{u}\right) + \ln (x) \ln \left(\frac{\sqrt{4-3 u^2}-u-2
 x}{\sqrt{4-3 u^2}-u}\right) - \\ 
 \ln (x) \ln \left(\frac{\sqrt{4-3 u^2}+u-2 x}{\sqrt{4-3 u^2}+u}\right)-\ln (x) \ln \left(\frac{\sqrt{4-3
 u^2}-u+2 x}{\sqrt{4-3 u^2}-u}\right) + \\ 
 \ln (x) \ln \left(\frac{\sqrt{4-3 u^2}+u+2 x}{\sqrt{4-3 u^2}+u}\right)+\ln (x) \ln
 \left(\frac{u-x}{u}\right)-\ln (x) \ln \left(\frac{u+x}{u}\right) \Bigg). 
\end{gathered}$$ By then setting $x \to 1$ and $x \to 0$, we obtain an equivalent version of the desired equality $s_3 = K$, and similarly for $A + B + J + C + H + D = s_3$ and for $M = A + B$, for the case whereby $u \in \mathbb{C} \setminus \mathbb{R}$ satisfies the specified convergence condition, and an analytic continuation then gives us the desired result for real arguments. ◻
:::
