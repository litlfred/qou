---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-021-61-twisted-alexander-polynomials-and-fibered-man
section_title: "Twisted Alexander polynomials and fibered manifolds"
section_number: 6.1
pages: 18-21
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.982
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:fib}
Let $\phi\in H^1(N;\mathbb{Z}) = \mbox{Hom}(\pi_1(N),\mathbb{Z})$ be non--trivial. We say
\emph{$(N,\phi)$ fibers over $S^{1}$}
 if there exists
 a fibration $p:N\to S^1$ such that the induced map $p_*:\pi_1(N)\to \pi_1(S^1)=\mathbb{Z}$ coincides with $\phi$. If
$K$ is a fibered knot, then it is a classical result of Neuwirth that
$\Delta_K$ is monic and that $\deg(\Delta_K)=2 \, \mbox{genus}(K)$. Similarly, twisted Alexander polynomials provide necessary conditions to the fiberability of a pair $(N,\phi)$.


In order to state the fibering obstructions for a pair $(N,\phi)$
we need to introduce the Thurston norm. Given $(N,\phi)$ the \emph{Thurston norm} of $\phi$ is defined as
 \[
||\phi||_{T}=\min \{ \chi_-(S)\, | \, S \subset N \mbox{ properly embedded surface dual to }\phi\}.
\]
Here, given a surface $S$ with connected components $S_1\cup\dots \cup S_k$, we define
$\chi_-(S)=\sum_{i=1}^k \max\{-\chi(S_i),0\}$.
 Thurston
\cite{Th86} showed that this defines a seminorm on $H^1(N;\mathbb{Z})$ which can be extended to a seminorm
on $H^1(N;\mathbb{R} )$. As an example consider $S^3\setminus \nu K$, where $K\subset S^3$ is a non--trivial knot. Let $\phi\in H^1(S^3\setminus \nu K;\mathbb{Z})$ be a
generator, then  $||\phi||_T=2\, \mbox{genus}(K)-1$.

Let $N$ be a 3--manifold $N$ with empty or toroidal boundary and let  $\phi\in H^1(N;\mathbb{Z})$.
Recall that we identify the group ring $R[\mathbb{Z}]$ with the Laurent polynomial ring $R[t^{\pm 1}]$ and we will now identify $Q(R[\mathbb{Z}])$ with the field of rational functions $Q(t)$.
Given a  representation
${\gamma}:\pi_1(N)\to \mbox{GL}(k,R)$ we therefore view the corresponding twisted Reidemeister torsion
$\tau(N,{\gamma \otimes \phi})$ as an element in $Q(t)$ and we view the corresponding twisted
Alexander polynomials
$\Delta_{N,i}^{\gamma \otimes \phi}$ as elements in $R[t^{\pm 1}]$.

We say that the twisted Reidemeister torsion $\tau(N,\gamma\otimes \phi)$ is \emph{monic} if there exist
 polynomials
$p(t),q(t)\in R[t^{\pm 1}]$ with $\frac{p(t)}{q(t)}\doteq \tau(N,\gamma\otimes \phi)$ such that the
top coefficients of $p(t)$ and $q(t)$  lie in
\[ \{ \pm \det(\gamma(g)) \, |\, g\in \pi_1(N)\}.\]
We also say that the twisted Alexander polynomial $\Delta_{N,i}^{\gamma \otimes \phi}$ is \emph{monic}
if one (and equivalently any) representative has a top coefficient which is a unit in $R$.









We recall the following basic lemma:

\begin{lemma}
Let $N$ be a 3--manifold with empty or toroidal boundary. Let $\phi\in H^1(N;\mathbb{Z})$ be non--trivial  and let
${\gamma }:\pi_1(N)\to \mbox{GL}(k,R)$ be a  representation with $R$ a Noetherian UFD. Then the following hold:
\begin{enumerate}
\item $\Delta_{N,0}^{\gamma \otimes \phi}$ is monic,
\item If $\Delta_{N,1}^{\gamma \otimes \phi}$ is non--zero, then $\Delta_{N,2}^{\gamma \otimes \phi}$ is monic.
\end{enumerate}
\end{lemma}

\begin{proof}
As in Section \ref{section:comptau} we pick a cell decomposition of $N$ with one 0--cell $x_0$ and $n$ 1--cells $c_1,\dots,c_n$.
We denote the corresponding elements in $\pi_1(N,x_0)$ by $c_1,\dots,c_n$ as well.
Without loss of generality we can assume that $\phi(c_1)> 0$.
We then get a resolution for $H_0(N;R[t^{\pm 1}]^n)$ with presentation matrix
\[ \begin{pmatrix} \mbox{id}_n -({\gamma \otimes \phi})(c_1) &\dots & \mbox{id}_n -{(\gamma \otimes \phi)}(c_n)\end{pmatrix}. \]
We refer to \cite[Proof~of~Proposition~6.1]{FK06} for details.
We have
\[ \det(\mbox{id}_n-{(\gamma \otimes \phi)}(c_1))=\det(\mbox{id}_n-t^{\phi(c_1)}\gamma(c_1))\in R[t^{\pm 1}], \]
which is monic since the top coefficient equals $\det(\gamma(c_1))$. By definition
$\Delta_{N,0}^{\gamma \otimes \phi}$ divides $\det(\mbox{id}_n-({\gamma \otimes \phi})(c_1))$, we therefore see that $\Delta_{N,0}^{\gamma \otimes \phi}$ is monic.
The claim that $\Delta_{N,2}^{\gamma \otimes \phi}$ is monic now follows from Proposition \ref{prop:dualitydelta}.
\end{proof}

\begin{remark}
Note that if $\tau(N,{\gamma \otimes \phi})$ is monic, then it follows from the previous lemma and
from Proposition \ref{prop:taudelta} that $\Delta_{N,i}^{\gamma \otimes \phi}\in R[t^{\pm 1}]$ is monic for $i=0,1,2$.
Note though that the converse does not hold in general since  twisted Alexander polynomials have in general a higher indeterminacy than twisted Reidemeister torsion.
For example, let $\mathbb{F}$ be a field and let $\gamma:\pi_1(N)\to \mbox{GL}(k,\mathbb{F})$ be a representation such that  $\Delta_{N,i}^{\gamma\otimes \phi}\ne 0$. It follows immediately from the definition
that $\Delta_{N,i}^{\gamma\otimes \phi}$ is monic. However, $\tau(N,\gamma\otimes \psi)$
is not necessarily monic (cf. e.g. \cite[Example~4.2]{GKM05}).
\end{remark}

We can now formulate the following fibering obstruction theorem
which was proved in various levels of generality by
Cha \cite{Ch03}, Kitano and Morifuji \cite{KM05}, Goda, Kitano and Morifuji \cite{GKM05}, Pajitnov \cite{Pa07}, Kitayama \cite{Kiy08a} and  \cite{FK06}.


\begin{theorem} \label{thm:fibob}
Let $N$ be a 3--manifold. Let $\phi\in H^1(N;\mathbb{Z})$ be non--trivial such that  $(N,\phi)$ fibers over
$S^1$ and such that $N\ne S^1\times D^2, N\ne S^1\times S^2$. Let
${\gamma}:\pi_1(N)\to \mbox{GL}(k,R)$ be a  representation. Then  $\tau(N,{\gamma \otimes \phi}) \in Q(t)$ is monic
and we have
\[ k ||\phi||_T =\deg(\tau(N,{\gamma \otimes \phi})).\]
\end{theorem}

\begin{remark}
\begin{enumerate}
\item If $R$ is a Noetherian UFD, then the last equality can be rewritten as
\[ k ||\phi||_T =\deg \Delta_{N,1}^{{\gamma \otimes \phi}}-\deg \Delta_{N,0}^{{\gamma \otimes \phi}}-\deg \Delta_{N,2}^{{\gamma \otimes \phi}}.\]
\item Recall that an alternating knot is fibered if and only if its ordinary Alexander polynomial is monic. In contrast to this classical result it follows from calculations by Goda and Morifuji \cite{GM03} (cf. also \cite{Mo08})
that there exists an alternating knot such that a twisted Reidemeister torsion is monic, but which is not fibered.
\item Theorem \ref{thm:fibob} has been generalized by Silver and Williams \cite{SW09d} to give an obstruction for a general group to admit an epimorphism onto $\Z$ such that the kernel is a finitely generated free group.
\end{enumerate}
\end{remark}

\begin{proof}
The condition on the degrees is proved in \cite[Theorem~1.3]{FK06} for $R$ a Noetherian UFD.
The monicness of twisted Reidemeister torsion was proved by
Goda, Kitano and Morifuji \cite{GKM05} in the case of a knot complement.
The monicness of $\Delta_{N,1}^{\gamma \otimes \phi}$ was proved in \cite[Theorem~1.3]{FK06}.
The general case of Theorem \ref{thm:fibob}  can be obtained by a direct calculation as follows.
Let $S$ be the fiber and $f:S\to S$ the monodromy. We endow $S$ with a CW--structure such that $f$ is a cellular map.
Denote by $D_i$ the set of $i$--cells of $S$ and denote by $n_i$ the number of $i$--cells.
We can then endow $N=(S\times [0,1])/(x,0)\sim (f(x),1)$ with a CW--structure where the $i$--cells are given by
$D_i$ and $E_i\mathrel{\mathop:}=\{ c\times (0,1) \, | \, c\in D_{i-1}\}$. A direct calculation using \cite[Theorem~2.2]{Tu01} now shows
that
 $\tau(N,{\gamma \otimes \phi}) \in Q(t)$ is monic
and that
\[ \deg(\tau(N,{\gamma \otimes \phi}))=-k\chi(S)=k ||\phi||_T.\]
\end{proof}



The calculations in \cite{Ch03}, \cite{GKM05} and \cite{FK06} gave evidence that
twisted Alexander polynomials are very successful at detecting non--fibered manifolds.
The results of Morifuji \cite[p.~452]{Mo08} also give evidence to the conjecture that the twisted Alexander polynomial corresponding to a `generic' representation
detect fiberedness.


Using a deep result of Agol \cite{Ag08} the authors proved in \cite{FV08c} (see also \cite{FV10} for an outline of the proof)
the following converse to Theorem \ref{thm:fibob}.

\begin{theorem} \label{thm:fv08} Let $N$ be a $3$--manifold with empty or toroidal boundary.
 Let $\phi \in H^{1}(N;\mathbb{Z})$ a nontrivial class. If for
any epimorphism $\gamma:\pi_1(N)\to G$ onto a finite group
the twisted Alexander polynomial $\Delta_{N}^{\gamma\otimes \phi}\in \mathbb{Z}[t^{\pm 1}]$ is monic
and  \[ k||\phi||_T=\deg(\tau(N,\gamma\otimes \phi))\] holds,
then $(N,\phi)$ fibers over $S^1$.
 \end{theorem}

\begin{remark}
Building on work of Taubes \cite{Ta94,Ta95}, Donaldson \cite{Do96} and Kronheimer \cite{Kr99} the authors
also show that Theorem \ref{thm:fv08} implies the following: If $N$ is a closed 3--manifold
and if $S^1\times N$ is symplectic, then $N$ fibers over $S^1$. This provides a converse to a theorem
of Thurston \cite{Th76}. We refer to \cite{FV06,FV08a,FV08b,FV08c} for details, and we refer to
Kutluhan--Taubes \cite{KT09}, Kronheimer--Mrowka \cite{KM08} and  Ni \cite{Ni08} for an alternative proof in the case that $b_1(N)=1$.
\end{remark}

It is natural to ask whether $(N,\phi)$ fibers if all twisted Alexander polynomials are monic.
An affirmative answer  would be of great interest in the study of symplectic structures of 4--manifolds with a free circle action (cf. \cite{FV07b}).
An equivalent question has also been raised as a conjecture by Goda and Pajitnov \cite[Conjecture~13.2]{GP05} in the study of Morse--Novikov numbers. We refer to
 \cite{GP05} and \cite{Pa07} for more information on the relationship between twisted Alexander polynomials, twisted Novikov homology and Morse--Novikov numbers.


Somewhat surprisingly, there is strong evidence to the following much weaker conjecture:
A pair $(N,\phi)$ fibers if all twisted Alexander polynomials are non--zero.
In fact the authors showed the following theorem
(cf. \cite[Theorem~1.3]{FV07a} and \cite[Theorem~1,~Proposition~4.6,~Corollary~5.6]{FV08b}).

\begin{theorem}\label{thm:zerodelta}
Let $N$ be a 3--manifold with empty or toroidal boundary and $\phi \in H^1(N;\mathbb{Z})$ non--trivial.
Suppose that $\Delta_{N}^{\gamma\otimes\phi}$ is non--zero for any epimorphism $\gamma:\pi_1(N)\to G$ onto a finite group.
Furthermore suppose that one of the following holds:
\begin{enumerate}
\item $N=S^3\setminus \nu K$ and $K$ is a genus one knot,
\item $||\phi||_T=0$,
\item $N$ is a graph manifold,
\item $\phi$ is dual to a  connected incompressible
surface $S$ such that $\pi_1(S)\subset \pi_1(N)$ is separable,
\end{enumerate}
then $(N,\phi)$ fibers over $S^1$.
\end{theorem}

Here we say that a subgroup $A$ of a group $\pi$ is \emph{separable} if for any $g\in \pi\setminus A$ there exists an epimorphism ${\gamma}:\pi\to G$ onto a finite group $G$ such that ${\gamma }(g)\not\in {\gamma }(A)$.
It is conjectured (cf. \cite{Th82}) that given a hyperbolic 3--manifold $N$ any finitely generated subgroup
$A\subset \pi_1(N)$ is separable. In particular, if Thurston's conjecture is true, then Condition (4) of Theorem
\ref{thm:zerodelta} is satisfied for any hyperbolic $N$.

The following theorem of Silver--Williams \cite{SW09b} (cf. also \cite{SW09a}) gives an interesting criterion for a knot to have vanishing twisted Alexander polynomial.

\begin{theorem}\label{thm:sw}
Let $K\subset S^3$ a knot.
Then there exists an epimorphism ${\gamma }:\pi_1(S^3\setminus \nu K)\to G$ to a finite group such that $\Delta_{K}^{\gamma} =0$
if and only if the universal abelian cover of $S^3\setminus \nu K$ has uncountably many finite covers.
\end{theorem}
