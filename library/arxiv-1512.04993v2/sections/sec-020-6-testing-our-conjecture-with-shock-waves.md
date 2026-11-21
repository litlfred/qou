---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-020-6-testing-our-conjecture-with-shock-waves
section_title: "Testing our conjecture with shock waves"
section_number: 6
pages: 31-32
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.966
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:shockwaves}

The original complexity/geometry duality passed a number of nontrivial tests involving the effects of shock waves on the growth of complexity and volume. It is important that the new CA-proposal passes the same tests.
In this section we consider the growth of complexity in eternal black hole geometries perturbed by shock waves and verify this.

Shock waves are constructed by perturbing the thermofield double state with thermal scale operators
\be
e^{-i H_L t_L}\, e^{-i H_R t_R}\, W(t_{n}) \dots W(t_1) \TFD, \label{eq:multiple-precursors}
\ee
where $W(t) = e^{i H_L t}\, W\, e^{-i H_L t}$, $W$ is a simple operator smeared over a thermal scale acting on the left boundary.\footnote{Here our conventions for precursors $W(t)$ are that Hamiltonian evolution $t_L$ increases to the future, but Killing time evolution in the left side of the bulk eternal black hole geometry increases to the past.} The state \eqref{eq:multiple-precursors} is dual to eternal black hole geometries perturbed by $n$ shock waves. Sometimes we will take $W$ to be smeared over the entire spatial boundary sphere. In these cases, we imagine that the field theory is sitting right above its Hawking-Page point so that smearing the operator over a thermal scale corresponds to smearing it over the sphere. At other times we will consider a high temperature limit with $W$ a spatially local operator smeared over the thermal scale. Similar states have been considered in the context of holography in \cite{shock,Shenker:2013yza,Leichenauer:2014nxa,localshocks,Shenker:2014cwa}, though they had previously been studied in other contexts \cite{Dray:1984ha,Dray:1985yt,Sfetsos:1994xa}.

These states provide a nontrivial check of the CA-duality. Because of boost invariance, in \S\ref{sec:bh} we only considered a one parameter family of states given by the overall time evolution $t_L + t_R$ of the thermofield double state. Shock wave states of the form \eqref{eq:multiple-precursors} let us dial the times $t_1 \cdots t_n$ and in some cases the spatial positions $x_1 \cdots x_n$ of an essentially arbitrary number of perturbations. Additionally, the tensor network construction of states \eqref{eq:multiple-precursors} gives specific predictions for the complexity growth \cite{localshocks} which is very naturally matched by the action prescription for complexity. These include matching growth rates that are different from linear in boundary time evolution $t_L$ \cite{localshocks} and matching cancellation effects between $e^{i H_L t}$ and $e^{-i H_L t}$ to the left and right of the $W$ operator \cite{complexityshocks}. While these tensor network predictions were all previously matched by the CV notion of complexity \cite{localshocks,complexityshocks,Susskind:2014jwa}, we will show they are just as naturally matched by the complexity equals action conjecture.
