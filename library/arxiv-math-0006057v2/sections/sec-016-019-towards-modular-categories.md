---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-016-019-towards-modular-categories
section_title: "Towards modular categories"
section_number: 0.19
pages: 21-23
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.953
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
In \cite{RT} a general method of constructing invariants of
$3$-manifolds from modular Hopf algebras was introduced. 
Later it became clear that the technique of Hopf algebras can
be replaced by a more general technique of
modular categories (see \cite{T}). In addition to quantum groups,
such categories also arise from skein categories of tangles
and, as it was observed by A.~Ocneanu, from certain bimodule
categories of type II${}_1$
subfactors.

The representation categories of {\em quantum groupoids} give
quite general construction of modular categories.
Recall some definitions needed here. 
Let ${\mathcal V}$ be a ribbon $Ab$-category over $k$, i.e.,
such that all $\Hom(V,W)$ are $k$-vector spaces (for all objects
$V,W\in {\mathcal V}$) and both operations $\circ$ and $\otimes$ are
$k$-bilinear.

An object $V\in {\mathcal V}$ is said to be {\it simple} if any 
endomorphism of $V$ is multiplication by an element of $k$.
We say that a family $\{V_i\}_{i\in I}$ of objects of ${\mathcal V}$ 
dominates  an object $V$ of ${\mathcal V}$ if there exists a finite set
$\{V_{i(r)}\}_r$ of objects of this family (possibly, with repetitions)
and a family of morphisms  $f_r:V_{i(r)} \to V,g_r:V\to V_{i(r)}$ such that 
$\id_V = \sum_r f_r g_r$.

A modular category (\cite{T}, II.1.4) is a pair consisting of
a ribbon $Ab$-category ${\mathcal V}$ and a finite family $\{V_i\}_{i\in I}$
of simple objects of ${\mathcal V}$ satisfying four axioms:
\begin{enumerate}
\item[(i)] There exists $0\in I$ such that $V_0$
is the unit object.
\item[(ii)] For any $i\in I$, there exists $i^*\in I$ such that $V_{i^*}$ is 
isomorphic to $V^*_i$.
\item[(iii)] All objects of ${\mathcal V}$ are dominated by the
family $\{V\}_{i\in I}$.
\item[(iv)] The square matrix $S=\{S_{ij}\}_{i,j\in I} =
\{ \tr_q(c_{V_i,V_j}\circ c_{V_j,V_i}) \}_{i,j\in I}$ is invertible over $k$
(here $\tr_q$ is the quantum trace in a ribbon category defined by 
(\ref{q1-trace})).
\end{enumerate}

If a quantum groupoid $H$ is connected and semisimple over an 
algebraically closed field, modularity of $\Rep(H)$ is equivalent to 
$\Rep(H)$ being ribbon and such that the matrix $S=\{S_{ij}\}_{i,j\in I} =
\{ \tr_q(c_{V_i,V_j}\circ c_{V_j,V_i}) \}_{i,j\in I}$, where $I$ is the set of 
all (equivalent classes of) irreducible representations, is invertible.
The following proposition extends a result known for Hopf algebras 
(\cite{EG}, 1.1).
\begin{proposition}
\label{factorizable implies modular}
If $H$ is a connected, ribbon, factorizable quantum groupoid 
over an algebraically closed field $k$,
possessing a normalized two-sided integral, then $\Rep(H)$ is a modular category.
\end{proposition}

\begin{proof}
Here we only need to prove the invertibility of the matrix formed by
\begin{eqnarray*}
S_{ij} 
&=& \tr_q(c_{V_i,V_j}\circ c_{V_j,V_i}) \\
&=& (\dim H_t)^{-1} \Tr( (u\nu)\circ c_{V_i,V_j}\circ c_{V_j,V_i}) \\
&=& (\dim H_t)^{-1}  (\chi_j \otimes \chi_i)( (u\nu\otimes u\nu)\R_{21}\R),
\end{eqnarray*}
where $V_i$ are as above, $I = \{1,\dots n\},\ \{ \chi_j\}$ is a basis 
in the space $C(H)$ of characters 
of $H$ (we used above the  formula (\ref{q-trace}) for the quantum trace).

It was shown in (\cite{NTV}, 5.12, 8.1) that the map $F : 
\phi\mapsto (\phi\otimes \id)(R_{21}R)$ is a linear isomorphism between
$C(H)\actl u\nu$ 
and the center $Z(H)$ (here $(\chi\actl u\nu)(a) =
\chi(u\nu a)~\forall a\in H,\ \chi\in C(H)$).
So, there exists an invertible matrix $T=(T_{ij})$ representing 
the map $F$ in the bases $\{ \chi_j\}$ of $C(H)$ and $\{e_i\}$ of $Z(H)$, 
i.e., such that
$F(\chi_j\actl u\nu) = \sum_i\, T_{ij}e_i$. Then
\begin{eqnarray*}
S_{ij} 
&=& (\dim H_t)^{-1} \chi_i(u\nu F(\chi_j\actl u\nu)) 
    = (\dim H_t)^{-1} \sum_k\, T_{kj} \chi_i(u\nu e_k) \\
&=& (\dim H_t)^{-1} (\dim V_i) \chi_i(u\nu) T_{ij}. 
\end{eqnarray*}
Therefore, $S = DT$, where $D = \mbox{diag}\{ (\dim H_t)^{-1} (\dim V_i) 
\chi_i(u\nu) \}$.
Theorem\ref{Haar theorem} below, shows that the existence of
a normalized two-sided integral in $H$ is equivalent to $H$
being semisimple and possessing an invertible element $g$ such
that $S^2(x)=gxg^{-1}$ for all $x\in H$ and $\chi(g^{-1})\neq O$
for all irreducible character $\chi$ of $H$. 
Then
$u^{-1}g$ is an invertible central element of $H$ and
$\chi_i(u^{-1})\neq 0$ for all $\chi_i$. By Corollary~\ref{uv is central} $uS(u)=c$
is invertible central, therefore 
$\chi_i(u)= \chi_i(c)\chi_i(S(u^{-1})))\neq 0$. 
Hence, $\chi_i(u\nu)\neq 0$ for all $i$ and $D$ is invertible.
\end{proof}
\end{section}





\begin{section}
{Twisting and dynamical quantum groups}

In this section we present a generalization of the Drinfeld 
twisting construction to quantum groupoids
developed in \cite{NV1}, \cite{Xu}, and \cite{EN}. We show that
{\em dynamical} twists of Hopf algebras give rise to quantum groupoids.
An important concrete example is given by dynamical quantum groups
at roots of $1$ \cite{EN}, which are dynamical deformations of the 
Drinfeld-Jimbo-Lusztig quantum groups $U_q(\g)$. 
The resulting quantum groupoids turn out to be selfdual, which is
a fundamentally new property, not satisfied by $U_q(\g)$. 

Most of the material of this section is taken from \cite{EN}.
