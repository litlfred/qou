---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-034-825-regularizing-the-action
section_title: "Regularizing the action"
section_number: 8.2.5
pages: 51-52
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.92
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:corner}

In this paper we have calculated the rate of growth of action of the WDW patch at late times. If we wish to calculate the rate of growth at finite times we must introduce a method of regularizing divergences, for example those that occur at the boundary of AdS. A divergence of this type shows up in the part of the WDW patch that lies behind the past horizon. The corner term at the bottom, which consists of the intersection of two lights heets, is divergent.\footnote{We thank Henry Maxfield for helpful discussions that prompted us to revisit this issue.}



Let us take for example the BTZ black hole. One way of regulating the action using timelike radial geodesics leads to the formula
\begin{equation}
\begin{aligned}
\frac{d\CA}{dt}=\frac{r_h^2}{4G\lads^2}\left(\tanh^2(\pi t/\beta)+\frac{\log\left(\cosh(\pi t/\beta)\right)}{\cosh^2(\pi t/\beta)} - \frac{\log\epsilon}{\cosh^2(\pi t/\beta)}\right)+\mathcal{O}(\epsilon),
\end{aligned}
\end{equation}
where $t \equiv t_L + t_R$ and $\epsilon$ is an ultraviolet regulator. There are three terms in parentheses.
The first term  tends to the constant late-time growth rate from Sec.~\ref{sec:actionuncharged}. This correctly gives the linear growth that has been the subject of this paper and is robust against changes in the cutoff prescription. The second term is a UV-finite transient, which dies away exponentially fast. The third term is more problematic. While it exponentially decreases with time, it is logarithmically UV divergent.




A UV-divergent complexification rate violates the bound of Eq.~\ref{C-bound}, and mixes IR and UV dependence in an anomalous way. We do not understand the physics of this term. It seems likely there is an improved regulator that removes the divergence. This UV divergence is  tied up with the issue of the complexity of formation (the complexity already present at $t_L=t_R=0$) and we intend to address  this question in \cite{ToAppear}.

Because there is no corner, this issue does not arise for either one-sided black holes or geometries with a wide Penrose diagram, e.g. wormholes lengthened by multiple shock waves. So while a subtlety with the regulator does occur for the action growth of unperturbed eternal black holes, these black holes are dual to rather special states of the conformal field theory. For many other states, such as those dual to black holes formed by collapse or wormholes perturbed by multiple strong shock waves, CA-duality gives a robust regulator-independent characterization of the growth of complexity.
