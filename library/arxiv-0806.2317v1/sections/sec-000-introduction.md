---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.979
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
In this paper, we introduce the concept of complex Grassmannian codes and designs: codes and designs in the collection of fixed-rank subspaces of a complex vector space.

In the 1970's, Delsarte \cite{del1} developed a series of excellent bounds for certain error-correcting codes by treating codewords as points in an association scheme and then applying linear programming. Shortly thereafter, Delsarte, Goethals and Seidel \cite{dgs} showed that the same technique could also be used on systems of points on the real or complex unit sphere, which they called spherical codes and spherical designs; this resulted in important contributions to problems in sphere-packing \cite[Chapter 9]{cs1}. This linear programming technique, which is now known as ``Delsarte LP theory", has proved surprisingly portable. Recently, Bachoc, Coulangeon and Nebe \cite{bcn1} generalized the results of Delsarte, Goethals and Seidel to real Grassmannian spaces, and Bachoc \cite{bac1} pointed out that ``the same game" can be played over the complex numbers. In this paper, we investigate more closely the case of complex Grassmannian codes.

The motivation for studying complex Grassmannians comes from the theory of quantum measurements. Roughly speaking, any complex Grassmannian $1$-design defines a projective measurement in the theory of quantum mechanics. It has recently been discovered that complex projective $2$-designs correspond to quantum measurements that are optimal for the purposes of nonadaptive quantum state tomography \cite{sco}. In fact, this is also true in the more general Grassmannian setting: complex Grassmannian $2$-designs are the optimal choices of measurements for nonadaptive quantum state tomography when the observer only has access to measurements with a restricted number of outcomes. More details will appear in a paper by Godsil, R\"otteler, and the author \cite{grr}. Complex Grassmannians also play a role in certain wireless communication protocols \cite{aru1}.

Define $\gras{m}{n}$ to be the set of $m$-dimensional subspaces of an $n$-dimensional complex vector space. Without loss of generality, we will always assume $m \leq n/2$. Usually, we will represent a subspace $a$ by its $n \times n$ projection matrix $P_a$. The inner product on $\gras{m}{n}$ is the trace inner product for projection matrices:
\begin{align*}
\ip{a}{b} & := \tr(P_a^*P_b) \\
& = \tr(P_aP_b).
\end{align*}
Since $\ip{a}{b} = \ip{b}{a}$, the inner product is real. This is a measure of separation, or distance, between two subspaces---note that is not a distance metric per se: the inner product of $P_a$ with itself is maximal rather than minimal. However, the \defn{chordal distance} \cite{chs}, defined by 
\[
d_c(P_a,P_b) := \sqrt{m - \tr(P_aP_b)},
\]
is a monotonic function of the inner product. Given a finite set of inner product values $\scr{A}$, an \defn{$\scr{A}$-code} is a subset $S$ of $\gras{m}{n}$ such that 
\[
\scr{A} = \{\tr(P_aP_b): a,b \in S, \; a \neq b \}.
\]
An \defn{$s$-distance set} is an $\scr{A}$-code with $|\scr{A}| = s$. This generalizes the concept of an $s$-distance set on the complex unit sphere: if $u$ and $v$ are unit vectors, then their separation distance on the unit sphere is a function of 
\[
\abs{u^*v}^2  = \tr(uu^*vv^*).
\]
We are interested in codes of maximal size for a fixed $\scr{A}$ or $s$, and bounds on their size based on zonal polynomials. Table \ref{tab:codebounds} in Section \ref{sec:bounds} gives a summary of the bounds for small $\abs{\scr{A}}$.

The outline of this paper is as follows. In Section \ref{sec:orbitals}, we describe the orbits of pairs of subspaces in $\gras{m}{n}$ under the action of $U(n)$: these orbits play a significant role in the bounds derived later on. In Sections \ref{sec:representations}, \ref{sec:symmetric} and \ref{sec:zonal}, we develop the necessary representation theory background needed for our LP bounds. In particular, we discuss the decomposition of the square-integrable functions on $\gras{m}{n}$ into irreducible representations of $U(d)$, and the zonal polynomials for these representations. The results in this section are all known, and the development is quite similar to that of Bachoc, Coulangeon and Nebe for real Grassmannians. In fact, the complex case is actually easier than the real case, because representations of the unitary group $U(n)$ are easier to describe than representations of the orthogonal group $O(n)$. In Section \ref{sec:bounds}, we develop absolute and relative bounds for codes, and show how these bounds for $\gras{m}{n}$ reduce to known bounds for complex spherical codes when $m = 1$. These bounds are compared to some other known bounds for subspaces in Section \ref{sec:otherbounds}. In Section \ref{sec:designs}, we consider Grassmanian designs. Grassmannian codes enjoy a form of duality with complex Grassmannian designs, very similar to real Grassmannian codes or spherical codes. In Section \ref{sec:examples}, we give examples in which the bounds are tight. In many cases codes of maximal size or designs of minimal size have the structure of an association scheme, which we describe in Section \ref{sec:assoc}.
