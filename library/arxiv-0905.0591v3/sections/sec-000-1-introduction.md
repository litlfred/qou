---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.956
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
In 1928 Alexander introduced a polynomial invariant for knots and links which quickly got referred  to as the Alexander polynomial.
His definition was later recast in terms of Reidemeister torsion by Milnor \cite{Mi62}
and it was extended by Turaev \cite{Tu75,Tu86} to an invariant of 3-manifolds.
More precisely, to a 3-manifold with empty or toroidal boundary $N$ we can associate its Alexander polynomial $\Delta_N$
which lies in the group ring $\Z[H]$, where $H$ is the maximal abelian quotient of $H_1(N;\Z)$.
The Alexander polynomial of knots, links and 3-manifolds in general is closely related to the topology properties of the underlying space.
For example it is known to contain information on the knot genus \cite{Se35}, knot concordance (\cite{FM66}), fiberedness and symmetries.

The Alexander polynomial carries only metabelian information on the fundamental group.
This limitation explain why in all the above  cases the Alexander polynomial carries partial, but not complete information.
The idea behind twisted invariants is to associate a polynomial invariant to a 3-manifold \emph{together}
with a choice of a representation of its fundamental group.

This approach makes it possible to
extract more powerful topological information.


The twisted Alexander polynomial for a knot $K \subset S^3$
was first  introduced by Xiao--Song Lin in 1990 (cf. \cite{Lin01}).
Whereas Lin's original definition used `regular Seifert surfaces' of knots,
later extensions to links and 3--manifolds either
generalized the Reidemeister--Milnor--Turaev torsion (cf. \cite{Wa94,Ki96,KL99a,FK06}) or
generalized the homological definition of the Alexander polynomial (cf. \cite{JW93,KL99a,Ch03,FK06,HKL08}).

In most cases the setup for twisted invariants is as follows:
Let $N$ be a 3--manifold with empty or toroidal boundary,  $\psi:\pi_1(N)\to F$ an epimorphism onto a free abelian group $F$
and $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$  a representation with $R$ a domain.
In that case one can define the  twisted Reidemeister torsion $\tau(N,\gamma\otimes \psi)$, an invariant which in general lives in the quotient field of
the group ring $R[F]$.
If $R$ is furthermore a Noetherian unique factorization domain (e.g. $R=\mathbb{Z}$ or $R$ a field),
then  the twisted Alexander polynomials $\Delta_{N,i}^{\gamma\otimes \psi}\in R[F]$ is defined to be
the order of the twisted Alexander module $H_i(N;R[F]^k)$.

These two invariants are closely related, for example in the case that $\mbox{rank}(F)\geq 2$ we will see  that
\[ \tau(N,\gamma\otimes \psi)=\Delta_{N,1}^{\gamma\otimes \psi}\in R[F]. \]
 In fact in many papers the twisted Reidemeister torsion $\tau(N,\gamma\otimes \psi)$
is referred to as the twisted Alexander polynomial (cf. e.g. \cite{Wa94}).

The most important raison d'\^etre of these invariants lies in the fact that they contain deep information on the underlying topology
while at the same time being, as we will see, very computable invariants.

We now give a short outline of the paper.
In Section \ref{section:definition} we define twisted Reidemeister torsion and twisted Alexander polynomials of 3-manifolds,
and we show how to calculate these invariants.
In Section \ref{section:basics} we discuss basic properties of twisted invariants,
in particular we discuss the  relationship between twisted Reidemeister torsion and twisted Alexander polynomials
and we discuss the effect of Poincar\'e duality on twisted invariants.
Section \ref{section:dist} contains applications to distinguishing knots and links using twisted invariants.
In Section \ref{section:conc} we outline the results of Kirk and Livingston
regarding the behavior of twisted invariants under knot concordance and we extend the results
to the study of doubly slice knots and ribbon knots.
In Section \ref{section:fibgenus} we show that twisted invariants
give lower bounds on the knot genus and the Thurston norm, and we show that they give obstructions to
the fiberedness of 3-manifolds.
Sections \ref{section:twodim}, \ref{section:misc} and \ref{section:general}
contains a discussion of the many generalizations and further applications of twisted invariants.
In Section \ref{section:ho} we give an overview of the closely related theory of higher-order Alexander polynomials,
this theory was initiated by Cochran and Harvey.
Finally in Section \ref{section:question} we provide a list of open questions and problems.









































































\noindent \textbf{Conventions and Notation.}
Unless we say otherwise we adopt the following conventions:\\
(1) rings are commutative domains with unit element,\\
(2) 3--manifolds are  compact, connected and orientable,\\
(3) homology is taken with integral coefficients,\\
(4) groups are finitely generated.\\
We also use the following notation:
Given a ring $R$ we denote by $Q(R)$ its quotient field
and given a link $L\subset S^3$ we denote by $\nu L$ a (open) tubular neighborhood of $L$ in $S^3$.




\noindent \textbf{Remark.} For space reasons we unfortunately have to exclude from our exposition several important aspects of the subject. Among the most relevant omissions, we mention Turaev's torsion function, and the relation between torsion invariants on the one hand and Seiberg--Witten theory and Heegaard--Floer homology on the other.
Turaev's torsion function is defined using Reidemeister torsion corresponding to one--dimensional abelian representations.
This theory and its connection to Seiberg--Witten invariants, first unveiled by Meng and Taubes in \cite{MT96} (cf. also \cite{Do99}), is treated beautifully in Turaev's original papers
\cite{Tu97,Tu98} and in Turaev's books \cite{Tu01,Tu02a}. We also refer to \cite{OS04} for the relation of Turaev's torsion function to Heegaard--Floer homology.


\noindent \textbf{Remark.}
Almost all the results of this survey paper appeared already in previous paper.
We hope that we correctly  stated  the results of the many authors who worked on twisted Alexander polynomials. For the definite statements we nonetheless refer to the original papers.
The only new results are some theorems in Section \ref{section:slice} on knot and link concordance and
Theorem \ref{thm:fibob} on Reidemeister torsion of fibered manifolds.



















\noindent \textbf{Acknowledgments.}
The first author would like to thank Markus Banagl and Denis Vogel for organizing the workshop
`The Mathematics of Knots: Theory and Application' in Heidelberg in December 2008.
The authors also would like to thank Takahiro Kitayama, Taehee Kim, Chuck Livingston, Takayuki Morifuji, Andrew Ranicki and
Dan Silver for many helpful comments and remarks. Finally we wish to thank the referee for many helpful comments and remarks.
