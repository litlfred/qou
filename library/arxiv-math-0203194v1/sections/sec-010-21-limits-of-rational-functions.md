---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-010-21-limits-of-rational-functions
section_title: "Limits of rational functions."
section_number: 2.1
pages: 25-26
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.976
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{subsec-limit-rational}

\begin{para}\label{para-complex-approx}
{\itshape Over $\C$.\ }
 Let us briefly survey the complex analytic situation.
 Let $S$ be a connected complex analytic curve, and $U$ an open set
 of $S$ (not necessarily connected) which is holomorphically convex; 
 \index{holomorphically convex@holomorphically convex}
 \ie $S\setminus U$ has no compact connected component.
 Then $\OO(S)$ is dense in $\OO(U)$ for the topology of uniform
 convergence on every compact set.
 We denote this situation by $\OO(U)=\widehat{\OO(S)^U}$
 (\cf \eg \cite[13]{qadsdr}).

 Moreover, if $S$ is the Riemann surface coming from an affine algebraic
 curve $S^{\mathrm{alg}}$, then we also have 
 $\OO(U)=\widehat{\OO(S^{\mathrm{alg}})^U}$, which generalizes the theorem
 of Runge on approximation by rational functions.
 Indeed, considering an embedding $S^{\mathrm{alg}}\hookrightarrow
 (\mathbb{A}^N)^{\mathrm{alg}}$, we may extend analytic functions on $S$ to 
 analytic functions on $(\mathbb{A}^N)^{\mathrm{alg}}$
 (due to the vanishing of the first cohomology group of the
 coherent ideal sheaf defining $S$).
 An analytic functions on $(\mathbb{A}^N)^{\mathrm{alg}}$ can be 
 approximated by polynomials, which we restrict to $S$.
\end{para}

\begin{para}\label{para-ultra-approx}
{\itshape Over the $p$-adics.\ } We have an analogous situation. Let $K$ 
be a complete subfield of $\C_p$, and let $S$ be an analytic curve 
coming from a smooth affine algebraic curve over $K$. We consider a 
closed immersion $S \hookrightarrow {\A}^N$. For any $r > 0$, $S_r := S
\cap \matheur{D}_{{\A}^N}(0,r^+)$ is an affinoid domain in $S$. 
The same argument of polynomial approximation used in 
\ref{para-complex-approx} shows that $\mathcal{O}(S_r)$ is the 
completion of $\mathcal{O}(S^{\mathrm{alg}})$. 

 For any compact $Z \subset S$ (\eg an affinoid domain), we define the
 topological ring $\mathcal{H}(Z)$\index{000H@$\mathcal{H}(\;)$}
 of \emph{analytic elements}
 \index{analytic elements@analytic elements} on $Z$ to
 be the completion of $\Gamma (Z, \mathcal{O}_S) = \liminj_{Z\subset
 U \text{: open}}\Gamma (U, \mathcal{O}_S) $ under the sup-norm.
 Whenever $Z$ is contained in a $S_r$, $\mathcal{H}(Z)$ is also the
 completion of $\mathcal{O}(S_r)_Z$, where the subscript $Z$ denotes the
 localization with respect to the set of elements which do not vanish on
 $Z$ (\cf\ \cite{staagonf} and \cite{rdldaecpecd} for a more precise
version of the Runge theorem).

 The holomorphic convexity condition on $Z$ is that for some $r$, $Z$ is
 the intersection of affinoid neighborhoods defined by inequalities of
 the form $|f_i| \leq 1$ in $S_r$. If this condition is satisfied,
 $\mathcal{H}(Z)$ is in fact the completion of $\mathcal{O}(S_r)$ itself.
\end{para}

\begin{para}
{\itshape The Krasner-Dwork viewpoint.\ }
For $S=\mathbb{A}^1$, and $K=\C_p$, we deduce
$\mathcal{H}(Z)=\widehat{\left(K[z]_Z\right)}$, which is nothing but the 
M.\ Krasner's original definition of analytic elements on $Z$.

Let $\widehat{K(z)}$ be the completion of $K(z)$ by means of Gauss
norm.
One can interpret its elements as the analytic elements on a generic
disk, and then specialize in the complement $Z\subseteq\mathbb{P}^1$ of
a finite union of disks $\matheur{D}(a_i,1^-)$, $(i=1,2,\ldots)$.
This viewpoint leads us to understand analytic continuation
as a \emph{specialization}. 
\end{para}
