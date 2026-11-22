---
doc_id: arxiv-0901.1612v1
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-001-2-background-and-motivation
section_title: "Background and motivation"
section_number: 2
pages: 4-5
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.984
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
[]{#sec:background label="sec:background"}

Let $L$ be an ordered oriented link in $\mathbb R^3$ with two parametrized components $$X = \{x(s) \ | \ s \in S^1\} \ \  \text{and} \ \ Y = \{y(t) \ | \ t \in S^1 \}.$$ The classical linking number $\text{Lk}(X, Y)$ is the degree of the Gauss map $S^1\times S^1\to S^2$ sending $(s,t)$ to $(y(t)-x(s))/\|y(t)-x(s)\|$, and can be expressed by the famous integral formula of Gauss [@Gauss], $$\begin{aligned}
    \text{Lk}(X, & Y) = 
    \frac{1}{4\pi} \int_{S^1 \times S^1} x'(s)  \times  y'(t)  \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,\frac{x(s)-y(t)}{\|x(s)-y(t)\|^3} \ ds \, dt \\
    & = \int_{S^1 \times S^1} x'(s)  \times  y'(t)  \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,\nabla_x \, \varphi\left(\|x(s)-y(t)\|\right) \ ds \, dt,
\end{aligned}$$ where $\varphi(r) = -1/(4\pi r)$ is the fundamental solution of the scalar Laplacian in $\mathbb R^3$. The integrand is invariant under the group of orientation-preserving rigid motions of $\mathbb R^3$, acting on the link $L$. Corresponding formulas in $S^3$ appear in DeTurck and Gluck [@DeTurckGluck] and in Kuperberg [@Kuperberg].

Theorems [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} and [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} above give a similar formulation of Milnor's triple linking number in $S^3$. We emphasize that these two theorems are set specifically in $S^3$, and that so far we have been unable to find corresponding formulas in Euclidean space $\mathbb R^3$ which are equivariant (for Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}) and invariant (for Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}) under the *noncompact* group of orientation-preserving rigid motions of $\mathbb R^3$.

For some background on higher order linking invariants, see Milnor [@Milnor57] and, for example, Massey [@Massey68], Casson [@Casson75], Turaev [@Turaev76], Porter [@Porter], Fenn [@Fenn83], Orr [@Orr], and Cochran [@Cochran].

The ***helicity*** of a vector field $V$ defined on a bounded domain $\Omega$ in $\mathbb R^3$ is given by the formula $$\begin{aligned}
    \text{Hel}&(V) = \int_{\Omega \times \Omega} V(x) \times V(y) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,\frac{x-y}{\|x-y\|^3} \  dx \, dy \\
    &= \int_{\Omega \times \Omega} V(x) \times V(y) \,\,\raisebox{.2ex}{\text{\tiny\textbullet}}\,\,\nabla_x \varphi\left(\|x-y\|\right) \ dx \, dy
    \end{aligned}$$

where, as above, $\varphi$ is the fundamental solution of the scalar Laplacian on $\mathbb R^3$.

Woltjer [@Woltjer] introduced this notion during his study of the magnetic field in the Crab Nebula, and showed that the helicity of a magnetic field remains constant as the field evolves according to the equations of ideal magnetohydrodynamics, and that it provides a lower bound for the field energy during such evolution. The term "helicity" was coined by Moffatt [@Moffatt], who also derived the above formula.

There is no mistaking the analogy with Gauss's linking integral, and no surprise that helicity is a measure of the extent to which the orbits of $V$ wrap and coil around one another. Since its introduction, helicity has played an important role in astrophysics and solar physics, and in plasma physics here on earth.

Looking back at Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}, we see that the integral in our formula for Milnor's $\mu$-invariant of a three-component link $L$ in the 3-sphere expresses the helicity of the associated vector field $V_L$ on the 3-torus.

Our study was motivated by a problem proposed by Arnol$'$d and Khesin [@ArnoldKhesin98] regarding the search for "higher helicities" for divergence-free vector fields. In their own words:

::: indentation
2.6em2.6em ***The dream is to define such a hierarchy of invariants for generic vector fields such that, whereas all the invariants of order $\leq k$ have zero value for a given field and there exists a nonzero invariant of order $k+1$, this nonzero invariant provides a lower bound for the field energy.***
:::

Many others have been motivated by this problem, and have contributed to its understanding; see, for example, Berger and Field [@Berger84], Berger [@Berger90; @Berger91], Evans and Berger [@EvansBerger92], Akhmetiev and Ruzmaiken [@Akhmetiev94; @Akhmetiev95], Akhmetiev [@Akhmetiev98], Laurence and Stredulinsky [@Laurence], Hornig and Mayer [@Hornig], Rivière [@Riviere], Khesin [@Khesin], and Bodecker and Hornig [@Bodecker04].

The formulation in Theorems [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} and [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} has led to partial results that address the case of vector fields on invariant domains such as flux tubes modeled on the Borromean rings; see Komendarczyk [@Komendarczyk].
