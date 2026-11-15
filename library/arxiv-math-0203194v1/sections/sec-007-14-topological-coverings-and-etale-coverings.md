---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-007-14-topological-coverings-and-etale-coverings
section_title: "Topological coverings and 'etale coverings."
section_number: 1.4
pages: 20-21
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.76
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub-top-cov-et-cov}
\begin{para}\label{para-complex-vs-padic}
 Complex manifolds are locally contractible,
 and have universal coverings.  There is no need to distinguish between
 topological
 coverings and \'etale coverings (finite or infinite).

 In $p$-adic rigid geometry, the situation is more complicated. It is
 natural to call
 topological covering any morphism $f: Y \rightarrow X$ such that there is
 an admissible
 cover $(X_i)$ of $X$ and an admissible cover $(Y_{ij})$ of $f^{-1}(X_i)$
 with disjoint $Y_{ij}$
 isomorphic to $(X_i)$ via  $f$. Indeed, such topological coverings
 correspond to locally constant
 sheaves of sets on $X$. It is still true that \emph{topological coverings
 are \'etale, but the converse is wrong}, even if one restricts to
 finite surjective morphisms. Indeed, the Kummer covering
 $z \mapsto z^n$ of the punctured unit disk is an \'etale 
 covering, but not a topological covering, if $n>1$.
\end{para}

\begin{para}
 It is again more convenient to tackle these questions in the framework
 of Berkovich's geometry.  For instance, one sees immediately that a
 Kummer covering $z\mapsto z^n$ as above is not a topological covering
 because a classical point has $n$ preimages, while the ``generic
 point'' $\eta_{0,1}$ (corresponding to the sup-norm on the disk) is its
 own single preimage. 
 Topological coverings of a $p$-adic manifold $X$ are defined in the
 usual way; they correspond to locally constant sheaves of sets on $X$.
 They coincide \cite[3.3.4]{staagonf} with topological coverings of the
 rigid analytic variety associated to $X$.
\end{para}

\begin{para}
 There are only three one-dimensional simply connected complex manifolds up to
 isomorphism: the projective line ${\P}^1(\C)$, the affine line $\C$, and
 the disk $\matheur{D}$ ($\simeq \mathfrak{h}$, the complex upper half
 plane). In contrast, there are plenty of \emph{simply-connected}
 one-dimensional 
 $p$-adic manifolds, for instance: any annulus, the line deprived from a
 finite number of points, more generally any connected $p$-adic manifold
 homeomorphic to a \emph{subset of} $\;{\P}^1(\C_p)$, any smooth
 projective curve with ``good reduction''... (all these Berkovich spaces
 look like ``bushy trees'').
\end{para}

\begin{para}
 One defines the (discrete) topological fundamental group
 $\pi_1^{\mathrm{top}}(S,s)$ of
 a pointed $p$-adic manifold $(S,s)$ in the usual way. The general
 topological theory of
 coverings applies: $(S,s)$ is naturally isomorphic to the quotient of the
 pointed universal
 covering $({\til{S}},{\tilde{s}})$ by $\pi_1^{\mathrm{top}}(S,s)$, and
 $\pi_1^{\mathrm{top}}(S,s)$ classify the
 topological coverings of $(S,s)$.   In the one-dimensional case, the
 topological fundamental
 group is a discrete \emph{free} group (more precisely, it is isomorphic to
 the fundamental
 group of the dual graph of the so-called semistable reduction of $S$
 (\cite[5.3]{efgonas})). 

 For instance, if $S=\Omega/\Gamma$ is the
 uniformization of a Mumford curve
 (\cf~\ref{subsection-rigid-and-unique-cont}), $\Omega$ is the universal
 covering of $S$ and the Schottky group $\Gamma$ is isomorphic to the 
 topological fundamental group.


 On the other hand, one can define the (profinite) algebraic fundamental
 group $\pi_1^{\mathrm{alg}}(S,s)$ \`a la Grothendieck, classifying the finite
 \'etale coverings of $(S,s)$. In contrast to the complex situation, the
 natural map $\pi_1^{\mathrm{alg}}(S,s) \rightarrow
 \pi_1^{\mathrm{top}}(S,s)^{\wedge}$
 to the profinite completion of $\pi_1^{\mathrm{top}}(S,s)$ is
 \emph{generally not injective} (\eg for annuli).
\end{para}
