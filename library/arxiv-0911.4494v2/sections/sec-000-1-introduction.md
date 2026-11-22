---
doc_id: arxiv-0911.4494v2
doc_title: "The geometry of Markov traces"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0911.4494v2.pdf
source_sha256: 1ba1c79686b12d98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.983
doc_brief: "The geometry of Markov traces — We give a geometric interpretation of the Jones-Ocneanu trace on the Hecke algebra, using the equivariant cohomology of sheaves on SLn."
---
\label{sec:introduction}

The mid 1980's saw a remarkable burst of knot invariants appearing from surprising directions; one of the foremost was the HOMPLYPT polynomial, independently discovered by several groups of researchers (see \cite{HOMFLY,PT}). In \cite{Jon87} this invariant was then interpreted by Jones in terms of a trace, now known as the {\bf Jones-Ocneanu trace}, on the Hecke algebra $\Hec_n$. In this original paper, this trace is constructed using an inductive procedure, but Jones asks whether it has some direct interpretation in terms of the Kazhdan-Lusztig basis of \cite{KL79}.

In this paper, we describe a relationship between this trace on a Hecke
algebra and the geometry of the special linear group $G$, which passes through the ``Hecke category'' of certain equivariant sheaves on $G$. Since the Kazhdan-Lusztig basis can also be defined in terms of the Hecke category, this provides an answer to Jones' question:

\begin{theorem*}
  The Jones-Ocneanu trace applied to the Kazhdan-Lusztig basis element
  $C^{\prime}_w$ of a permutation $w$ is the mixed Poincar\'e polynomial of the $\BD$-equivariant   intersection cohomology of the Bruhat variety $\ov {BwB}$.  Equivalently, it is the
  bigraded dimension of the Hochschild homology of an indecomposible
  Soergel bimodule $S_w$.
\end{theorem*}
Here, $B$ denotes the subgroup of upper triangular matrices of $G$ and $\BD$ denotes that subgroup acting by conjugation on $G$.



This geometric construction works for reductive
algebraic groups of all types, providing a natural two-variable trace on the Hecke
algebra associated to any Dynkin diagram. Let $\Gamma$ be a Dynkin diagram, $G$ the corresponding split adjoint group over $\mathbb{F}_q$, $B$ a Borel subgroup, $W_{\Gamma}$ its Weyl group and $\Hec_{\Gamma}$ the Hecke algebra of $W$.

\begin{defi}
  For any Dynkin diagram $\Gamma$, we define the trace
  $\Tr_\Gamma:\Hec_\Gamma\to \Z(q^{\nicefrac 12})[t]$ to be the unique
  linear map sending a Kazhdan-Lusztig basis vector for $w\in
  W_\Gamma$ to the mixed Poincar\'e polynomial of the $\BD$-equivariant intersection cohomology of the Bruhat variety $\ov{BwB}$.
\end{defi}
Generalizing the
Jones-Ocneanu trace to other types has been an active avenue of
research for some years.  Traces satisfying a Markov-type condition on
Hecke algebras of classical type were classified by Geck and
Geck-Lambropoulou \cite{Geck,GL}, but such traces form an infinite
dimensional vector space.  Gomi \cite{Gomi} constructed a special
trace on the Hecke algebra of any finite type Coxeter group (even non-crystallographic). He constructs his trace by giving an explicit expression in terms of the irreducible characters of the Hecke algebra, and shows that it satisfies a strong Markov condition via case-by-case analysis.

Using the connection between the Hecke category on $G$ and the theory
of character sheaves, we prove our main result (for more precise statements
see Theorem \ref{main-theorem} and Corollary \ref{final}).  

\begin{theorem*}
  The geometrically defined trace $\Tr_\Gamma$ satisfies the following properties:
  \begin{itemize}
  \item It satisfies a Markov condition analogous to that of the Jones-Ocneanu
    trace.
  \item For Weyl groups, it coincides with the trace defined by Gomi \cite{Gomi}.
  \item Its expansion in terms of simple
    characters is given explicitly in terms of Molien series and
    Lusztig's Fourier transform.
  \end{itemize} 
\end{theorem*}


This gives a geometric interpretation of Gomi's
formula.
In fact, the decomposition of $\Tr_\Gamma$ on a Kazhdan-Lusztig basis element into ``almost characters'' of the Hecke algebra (the Fourier transform of the irreducible characters) is categorified by a decomposition of the $\BD$-equivariant intersection cohomology of $\ov{BwB}$ into summands whose mixed Poincar\'e series are given by Molien series. 
\medskip

In the course of our proof, we must show the following result, which is of some independent interest:
\begin{theorem*}
  Any simple $B\! \times \!B$-equivariant perverse sheaf on $G$ is
  $\BD$-equivariantly formal. Equivalently, the Hochschild homology of
  any Soergel bimodule is free.
\end{theorem*}
 This statement was previously proved in type $A$ by Rasmussen
\cite[Proposition 4.6]{Ras06} using an inductive calculation (similar to Jones's
construction of the trace), and conjectured for all types by the authors.
We give an independent, purely geometric proof using Lusztig's work on parabolic induction and restriction functors for character sheaves.\medskip

Just as this trace is intimately tied to the HOMFLYPT polynomial as
described in \cite{Jon87,HOMFLY}, its categorification is connected to
the triply graded link homology of Khovanov and Rozansky
\cite{Kho05,KR05,Ras06}. The main theorem of this paper in the case of
type $A$ is essentially equivalent to the fact that this knot homology
is a knot invariant categorifying the HOMFLYPT polynomial
(proven by Khovanov-Rozansky in \cite{KR05}).

However, we provide a description of
the categorified trace on the Hecke algebra from first principles,
separate from knot theory.  The authors relate this description to
knot theory in a separate paper \cite{WWcol}, which describes a
geometric construction of colored HOMFLYPT homology, a knot homology
theory whose construction had been proposed by Mackaay, \Stosic and Vaz
\cite{MSV}.
