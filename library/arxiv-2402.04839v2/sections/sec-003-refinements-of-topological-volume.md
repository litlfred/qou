---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-003-refinements-of-topological-volume
section_title: "Refinements of topological volume"
section_number: null
pages: 5-5
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.912
latex_coverage_ratio: 0.933
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{ssec:refinements}

Let $M$ be a closed, orientable $3$--manifold. For each integer $n\ge 0,$ we define the invariant
\begin{equation}
\volt_n(M) = \inf \big\{ \; \volh(M\setminus K) \;\mid \; K \subset M \text{ is a hyperbolic $n$--component link } \; \big\}.
\end{equation}
For all $n\ge 1$ and all closed, orientable 3--manifolds $M$,
we have $\volt(M)\le \volt_n(M)$. 
In particular, $\volt(M)=\volt_0(M)< \volt_n(M)$ if and only if $M$ is hyperbolic. This also allows us to define an integer valued invariant
\[
h(M) = \min \{ \; n \; \mid \volt(M)= \volt_n(M)\;\}.
\]
Hence $M$ is hyperbolic if and only if $h(M)=0.$ The examples presented in \Cref{sec:computations} and based on the census in~\cite{GHMTY21} satisfy $h(M)=1.$

\begin{question}\label{que:unbounded_h(M)}
Is there an explicit family of examples $(M_n)$ with $h(M_n)=n$?
\end{question}

Myers~\cite{My93} showed that every homology class (indeed every free homotopy class) in a closed $3$--manifold is represented by some hyperbolic knot. More generally, he showed that every given finite set of free homotopy classes can be represented by a hyperbolic link. Hence for each class $c \in H_1(M),$ there is an invariant
\begin{equation}
\volt(M, c) = \inf \big\{ \; \volh(M\setminus L) \;\mid \; L \subset M \text{ is an oriented hyperbolic link with } [L]=c\; \big\}.
\end{equation}
A natural question is to ask which homology classes satisfy $\volt(M, c)= \volt(M).$
Some examples and a further discussion of this refinement can be found in \Cref{sec:Homology classes of minimisers}.
