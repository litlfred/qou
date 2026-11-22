---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-019-82-invariants-of-3-manifolds
section_title: "Invariants of 3-manifolds"
section_number: 8.2
pages: 50-52
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.99
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\label{TQFT}
There are two classes of invariants of 3-manifolds associated with a modular tensor
category $\2C$, cf.\ \cite{t}. On the one hand we have the surgery invariants $RT(M,\2C)$
of Reshetikhin and Turaev \cite{rt2} which are based on the fact that every connected
oriented closed 3-manifold can be obtained from $S^3$ by surgery along a framed link. It
turned out \cite{brug1} that modularity of the category $\2C$ is not really necessary,
since it suffices that $\2C$ be `modularizable'. Yet, the invariant of the manifold being
defined in terms of a link invariant, the existence of a (non-symmetric) braiding is
essential. On the other hand there are the state sum invariants based on a triangulation
of the manifold. Generalizing on \cite{tv}, an invariant $TV(M,\2C)$ associated with any
modular category $\2C$ was defined in \cite{t}. Later it was understood that in fact no
braiding is necessary for the construction of a triangulation invariant, cf.\ \cite{bw1,
gk}, provided $\2C$ has two-sided duals. (This had been anticipated in \cite{ocn4}, which
was never published.) We denote the corresponding invariant by $Tr(M,\2C)$. Gelfand and
Kazhdan formulated a conjecture \cite[Conjecture 1]{gk} pointing towards a link between
the two invariants being provided by the quantum double. Our results on the quantum double
of semisimple tensor categories allow us to prove this conjecture.

\bprop 
Let $\2C$ satisfy the assumptions of Theorem \ref{main1} and consider the state-sum TQFT
associated with $\2C$, as defined in \cite{gk}. Then the dimension of the vector space
$\2H_{S^1\times S^1}$ associated to the two dimensional torus equals the number
$\#\2Z_1(\2C)$ of isomorphism classes of simple objects of $\2Z_1(\2C)$. 
\eprop 
{\it Sketch of Proof.} By the considerations of Subsection \ref{ss-tube}, $\#\2Z_1(\2C)$
coincides with the dimension of the center of the tube algebra $\Xi_L$. But this center is 
isomorphic to $\2H_{S^1\times S^1}$, as discovered by Ocneanu \cite{ocn3} and explained in
more detail in \cite[Theorem 3.1]{ek1}. \qed 

\brem The above argument is only a sketch because the triangulation TQFT in 2+1 dimensions
considered in \cite{ocn3, ek1} is derived from a subfactor, see \cite{kosu} for a detailed
exposition. Here as in \cite[Section 7]{mue09} we use the fact that the latter is
equivalent to the invariant defined in \cite{bw1, gk}. This is more or less clear, but
certainly deserves being made precise, as we plan to do in \cite{mue15}. Note also that in
order for a spherical category to give rise to a triangulation TQFT -- as opposed to just
the invariant -- one must assume that it does not contain symplectic self-dual simple
objects. This is done in \cite{t} and \cite[p.\ 4018]{bw2}, but unfortunately ignored in
the bulk of the literature on the subject.
\erem

By Theorem \ref{main1}, $\2Z_1(\2C)$ is modular, thus gives rise to a surgery TQFT in 2+1
dimensions, cf.\ \cite{t}. For these TQFTs it is known (by construction) that the
dimension of the vector space $\2H_{S^1\times S^1}$ associated with the torus equals the 
number of isomorphism classes of simple objects in the category. Thus the above result
provides support for the conjecture that the triangulation and surgery TQFTs associated with
$\2C$ and $\2Z_1(\2C)$, respectively, are isomorphic. (This conjecture, while very natural,
seems to have appeared in print only in \cite[Question 5]{ke}.) In particular, the
corresponding invariants of closed oriented 3-manifolds should coincide:
\begin{equation} \label{conject}
  RT(M,\2Z_1(\2C))=Tr(M,\2C)\quad\forall M. 
\end{equation}
Presently, we have no proof for this, but we note that Sato and Wakui recently announced a
proof in the setting of unitary categories arising from a subfactor. If $\2C$ is modular,
the braided equivalence $\2Z_1(\2C)\stackrel{\otimes}{\simeq}_{br}\2C\boxtimes\tilde{\2C}$
proven in Section \ref{moddoub} implies
\[ RT(M,\2Z_1(\2C))=RT(M,\2C\boxtimes\tilde{\2C})=RT(M,\2C)\cdot RT(M,\tilde{\2C})
  =RT(M,\2C)\cdot RT(-M,\2C), \]
and (\ref{conject}) follows from \cite[Theorem VII.4.1.1]{t}, according to which
$TV(M,\2C)=RT(M,\2C)\cdot RT(-M,\2C)$. For non-modular $\2C$ we only have the following
weaker result:

\bprop 
Let $\2C$ be as in Theorem \ref{main1} and $M$ an oriented closed 3-manifold. Then
\[ RT(M,D(\2C))\cdot RT(-M,\2Z_1(\2C))=Tr(M,\2C)\cdot Tr(-M,\2C). \]
If $\2C$ is unitary then $|RT(M,\2Z_1(\2C))|=|Tr(M,\2C)|$.
\eprop
\prf We compute
\bean RT(M,\2Z_1(\2C))\cdot RT(-M,\2Z_1(\2C)) &=& TV(M,\2Z_1(\2C)) \\
  &=& Tr(M,\2Z_1(\2C)) \\
  &=& Tr(M,\2C\boxtimes\2C^\op) \\
  &=& Tr(M,\2C)\cdot Tr(M,\2C^\op) \\
  &=& Tr(M,\2C)\cdot Tr(-M,\2C). \eean
Here the first equality is due to Turaev's theorem, which applies since $\2Z_1(\2C)$ is
modular. The second is the equality \cite{bw2} of $TV$ and $Tr$ for spherical $\2C$. The
third equality follows from the weak monoidal Morita equivalence
$\2Z_1(\2C)\approx\2C\boxtimes\2C^\op$ together with the Morita invariance of the invariant
$Tr$, cf.\ \cite[Theorem 7.1]{mue09}. The last two equalities follow from general
properties of the invariant $Tr$ \cite{bw2}. 

If $\2C$ is unitary we have $RT(-M,\2Z_1(\2C))=\ol{RT(M,\2Z_1(\2C))}$ and
$Tr(-M,\2C)=\ol{Tr(M,\2C)}$, and we are done.
\qed
