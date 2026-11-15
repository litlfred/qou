---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-014-4-distinguishing-knots-and-links
section_title: "Distinguishing knots and links"
section_number: 4
pages: 11-13
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.971
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:dist}


In this section we will restrict ourselves to twisted Alexander polynomials of knots and links.
Recall that given an oriented knot $K\subset S^3$ the \emph{reverse} $\overline{K}$ is given by reversing the orientation.
Given a knot $K\subset S^3$ we denote by $K^*$ its \emph{mirror image}, i.e. the result of reflecting $K$ in  $S^2\subset S^3$.
The mirror image is also sometimes referred to as the \emph{obverse}.

Twisted Alexander invariants have so far been surprisingly little used to distinguish a knot from its mirror image or from its reverse
(cf. \cite{KL99b} though for a deep result showing that the knot $8_{17}$ and its reverse lie in different concordance classes).
It is an interesting question whether  Kitayama's normalized Alexander polynomial \cite{Kiy08a} can be used to distinguish a knot from its mirror image and its reverse.


We  refer to \cite{Ei07} for an interesting and very successful approach to distinguishing knots using `knot colouring polynomials'.


In this section we are from now on only concerned with distinguishing knot types of prime knots.
Here we say that two knots $K_1$ and $K_2$ are of the same knot type if there exists a homeomorphism $h$ of the sphere
with $h(K_1)=K_2$. Put differently, $K_1$ and $K_2$ are of the same knot type if they are related by  an isotopy
together possibly with taking the mirror image and possibly reversing the orientation.



The most common approach for distinguishing knots using twisted Alexander polynomials is to look at the set (or product) of all twisted Alexander polynomials
corresponding to a `characteristic set' of representations.
Note that due to Lemma \ref{lem:equ:rep} we can in fact restrict ourselves to conjugacy classes of a set of characteristic representations.


The following two types of characteristic sets have been used in the literature:
\begin{enumerate}
\item Given a knot $K$ consider
all conjugacy classes  of (all upper triangular, parabolic, metabelian, orthogonal, unitary) representations of $\pi_1(S^3\setminus \nu K)$ of a fixed dimension over a finite ring.
\item Given $K$ consider all conjugacy classes of homomorphisms of $\pi_1(S^3\setminus \nu K)$ onto a finite group $G$ composed with a fixed representation of $G$.
\end{enumerate}







The first approach was used in Lin's original paper \cite{Lin01} to distinguish knots with the same Alexander module.
Wada \cite{Wa94} also used the first approach to show that twisted Alexander polynomials can distinguish the Conway knot and the Kinoshita--Terasaka knot (cf. also \cite{In00}).
This shows in particular that twisted Alexander polynomials detect mutation.
In fact in \cite{FV07a} it is shown that twisted Alexander polynomials detect all mutants with 11 crossings or less.
Furthermore, in \cite{FV07a} the authors give an example of a pair of knot types of prime knots which can be distinguished using twisted Alexander polynomials,
even though the HOMFLY polynomial, Khovanov homology and knot Floer homology agree.

\begin{remark}
\begin{enumerate}
\item
The approach of using twisted Alexander polynomials corresponding to a characteristic set of conjugacy classes can be viewed as an extension
of the approach of Riley \cite{Ri71} who studied the first homology group corresponding to such a set of representations to distinguish the Conway knot from the Kinoshita--Terasaka knot.
\item By the work of Whitten \cite{Wh87} and Gordon--Luecke \cite{GL89} the knot type of a prime knot is determined by its fundamental group.
It is therefore at least conceivable that twisted Alexander polynomials can distinguish any two pairs of knot types.
\end{enumerate}
\end{remark}

The following theorem shows that twisted Alexander polynomials detect the unknot and the Hopf link.
The statement for knots was first proved by Silver and Williams \cite{SW06}, the extension to links was later proved
 in \cite{FV07a}.

\begin{theorem}\label{thm:swfv}
Let $L\subset S^3$ be a  link which is neither the unknot nor  the Hopf link. Then there exists an epimorphism $\gamma:\pi_1(S^3\setminus \nu L)\to G$ onto a finite group
$G$ such that $\Delta^\gamma_L \not\doteq  \pm 1$.
\end{theorem}


Given a knot $K$ we denote by $t(K)$ its tunnel number.
Theorem \ref{thm:swfv} was used by Pajitnov \cite{Pa08} to show that for any knot $K$ there exists $\lambda>0$
such that $t(nK)\geq \lambda n-1$.
