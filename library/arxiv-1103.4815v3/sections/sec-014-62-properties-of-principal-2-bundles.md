---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-014-62-properties-of-principal-2-bundles
section_title: "Properties of Principal 2-Bundles"
section_number: 6.2
pages: 36-38
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.976
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
Principal $\Gamma$-2-bundles over $M$ form a bicategory denoted $\zwoabun\Gamma M$. There is an evident pullback 2-functor 
\begin{equation*}
f^{*}: \zwoabun\Gamma N \to \zwoabun\Gamma M
\end{equation*}
associated to smooth maps $f:M \to N$,
and these make $\zwoabun\Gamma -$ a pre-2-stack over smooth manifolds. We deduce the following important two theorems about this pre-2-stack. The first asserts that it actually is a 2-stack:

\begin{theorem}
\label{th:2stack}
Principal 
$\Gamma$-2-bundles form a  2-stack $\zwoabun\Gamma-$ over smooth manifolds. \end{theorem}

\begin{proof}
This follows from Theorem \ref{th:stack} ($\Gamma$-bundle gerbes form a 2-stack) and Theorem \ref{th:equivalence} (the equivalence $\grb\Gamma- \cong \zwoabun \Gamma-$)  we prove in Section \ref{sec:equivalences}.
\end{proof}


\begin{remark}
\label{rem:2bungrp}
Similar to Remark \ref{rem:grbgrp}, we obtain automatically bicategories $\zwoabun\Gamma{\mathcal{X}}$ of principal $\Gamma$-2-bundles over Lie groupoids $\mathcal{X}$, including bicategories of \emph{equivariant principal $\Gamma$-2-bundles}.
\end{remark}


The second concerns a homomorphism  $\Lambda: \Gamma \to \Omega$ of Lie 2-groups, which induces the extension  $\Lambda \maps \grb\Gamma- \to \grb\Omega-$ between 2-stacks of bundle gerbes (Proposition \ref{grbextension}). Combined with the equivalence $\grb\Gamma- \cong \zwoabun \Gamma-$ of Theorem \ref{th:equivalence}, it defines a 1-morphism
\begin{equation*}
\Lambda : \zwoabun\Gamma- \to \zwoabun\Omega-
\end{equation*}
between 2-stacks of principal 2-bundles. Now we get as a direct consequence of Theorem \ref{extequiv}:

\begin{theorem}
\label{extequivbun}
If $\Lambda: \Gamma \to \Omega$ is a weak equivalence between Lie 2-groups, then the 1-morphism $\Lambda \maps \zwoabun\Gamma- \to \zwoabun\Omega-$ is an equivalence of 2-stacks.
\end{theorem}


A third consequence of the equivalence of Theorem \ref{th:equivalence} in combination with Lemma \ref{lem:invertibility} is
\begin{corollary}
\label{co:bunmorphinvertible}
Every 1-morphism $F: \mathcal{P}_1 \to \mathcal{P}_2$ between principal $\Gamma$-2-bundles over $M$ is invertible. 
\end{corollary}



The following discussion centers around \emph{local trivializability} that is implicitly contained in Definition \ref{def:zwoabun}.
A principal  $\Gamma$-2-bundle that is isomorphic to the trivial $\Gamma$-2-bundle $\mathcal{I}$ introduced in Example  \ref{ex:trivzwoabun} is called \emph{trivializable}. A \emph{section} of a principal $\Gamma$-2-bundle $\mathcal{P}$ over $M$ is an anafunctor $S: \idmorph M \to \mathcal{P}$ such that $\pi \nobr\circ\nobr S \eq \id_{\idmorph M}$ (recall that an anafunctor $\pi \circ S:M \to M$ is the same as a smooth map). One can show that every point $x\in M$  has an open neighborhood $U$ together with a section $s: \idmorph U \to \mathcal{P}|_U$. Such sections  can even be chosen to be smooth functors, rather than anafunctors, namely simply as ordinary sections of the surjective submersion $\pi: (\mathcal{P}|_U)_0 \to \idmorph U$.

\begin{lemma}
\label{lem:loctriv2}
A principal $\Gamma$-2-bundle over $M$ is trivializable if and only if it has a smooth section.
\end{lemma}

\begin{proof}
The trivial $\Gamma$-2-bundle $\mathcal{I}$ has the section $S(m) := (m,1)$, where $1$ denotes the unit of $\Gamma_0$. If $\mathcal{P}$ is trivializable, and $F: \mathcal{I} \to \mathcal{P}$ is an isomorphism, then, $F \circ S$ is a section of $\mathcal{P}$. Conversely, suppose $\mathcal{P}$ has a section $S: \idmorph M \to \mathcal{P}$. Then, we get the anafunctor
\begin{equation}
\label{seccomp}
\alxydim{@C=1.5cm}{\mathcal{I}=\idmorph M \times \Gamma \ar[r]^-{S\times \id} & \mathcal{P}\times \Gamma \ar[r]^-{R} & \mathcal{P}\text{.}}
\end{equation}
It has an evident  $\Gamma$-equivariant structure and respects the projections to $M$. According to Corollary \ref{co:bunmorphinvertible}, this is sufficient to have a 1-isomorphism.
\end{proof}



\begin{corollary}
Every principal $\Gamma$-2-bundle is locally trivializable, i.e. every point $x\in M$ has an open neighborhood $U$ and a 1-morphism $T: \mathcal{I} \to \mathcal{P}|_U$.
\end{corollary}


\begin{remark}
In Wockel's version \cite{wockel1} of principal 2-bundles, local trivializations are required to be smooth functors and to be invertible as smooth functors, rather than allowing anafunctors. This version turns out to be too restrictive in the sense that the resulting bicategory receives no 2-functor from the bicategory $\grb\Gamma M$ of $\Gamma$-bundle gerbes that would establish an equivalence. 
\end{remark}



It is also possible to reformulate our definition of principal 2-bundles in terms of local trivializations. This reformulation gives us criteria which might be easier to check than the actual definition, similar to the case of ordinary principal bundles.


\begin{proposition}
Let $\mathcal{P}$ be a Lie groupoid,  $\pi: \mathcal{P} \to \idmorph M$ be a surjective submersion  functor,  and  $R$ be a smooth right action of $\Gamma$ on $\mathcal{P}$ that preserves $\pi$. Suppose every point $x\in M$ has an open neighborhood $U$ together with a $\Gamma$-equivariant anafunctor $T: \mathcal{I} \to \mathcal{P}|_U$ that respects the projections. Then, $\pi:\mathcal{P} \to \idmorph M$ is a principal $\Gamma$-2-bundle over $M$.
\end{proposition}


\begin{proof}
We only have to prove that the functor $\tau$ is a weak equivalence, and we use  Theorem \ref{weak}. Since all morphisms of $\mathcal{P}$ have source and target in the same fibre of $\pi: \mathcal{P}_0 \to \idmorph M$, we may check the two conditions of Theorem \ref{weak} locally, i.e. for $\mathcal{P}|_{U_i}$ where $U_i$ is an open cover of $M$. Using local trivializations $\mathcal{T}_i: \mathcal{I} \to \mathcal{P}|_{U_i}$, the smooth functor $\tau$ translates into the smooth functor $(\id,\mathrm{pr}_1,m) :\idmorph M \times \Gamma \times \Gamma \to (\idmorph M \times \Gamma) \times_{M} (\idmorph M \times \Gamma)$. This functor is an isomorphism of Lie groupoids, and hence essentially surjective and fully faithful.  
\end{proof}







\setsecnumdepth{1}
