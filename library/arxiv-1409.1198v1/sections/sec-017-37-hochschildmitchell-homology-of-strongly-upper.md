---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-017-37-hochschildmitchell-homology-of-strongly-upper
section_title: "Hochschild–Mitchell homology of strongly upper triangular categories"
section_number: 3.7
pages: 19-21
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.946
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
\label{sec:upper-triang-line}


Recall that the trace of a linear category is just the zeroth Hochschild--Mitchell homology.
There is a class of linear categories for which we can compute explicitly their Hochschild--Mitchell homology.  The results developed in this section will be useful in our study of the Hochschild--Mitchell homology of categorified quantum groups.

\begin{defn}
  \label{r22}
  A linear category $\modC $ is said to be {\em upper-triangular} if
there is no sequence
\begin{gather*}
  x_0\xto{f_0}x_1\xto{f_1}\dots \xto{f_{n-1}}x_n\xto{f_n}x_0 \quad (n\ge 1)
\end{gather*}
of nonzero morphisms in $\modC $ unless $x_0=x_1=\dots =x_n$.
Alternatively, a linear category $\modC $ is upper-triangular if there is
a partial order $\le$ on $\Ob(\modC )$ such that $\modC (x,y)\neq0$ implies
$x\le y$.
\end{defn}


For a linear category $\modC $, define a ring $\End(\modC )$ by
\begin{gather*}
  \End(\modC )=\bigoplus_{x\in \Ob(\modC )}\modC (x,x).
\end{gather*}
















\begin{lem}[\cite{BHLZ}]
  \label{r19}  For an upper-triangular linear category $\modC $, we have
  \begin{gather}
    \label{e5}
    \HH_*(\modC )
    \cong\bigoplus_{x\in \Ob(\modC )}\HH_*(\modC (x,x))
    \cong \HH_*(\End(\modC )).
  \end{gather}
\end{lem}

\begin{remark} Note that the ring End(C) is not unital if Ob(C) is infinite.
The definition of the Hochschild homology of a non-unital ring R is
different from the case of unital rings (see \cite{Loday}), but it is well known
that the Hochschild homology of the direct sum of unital rings is
isomorphic to the direct sum of the Hochschild homology of its direct
summands.
\end{remark}


\begin{defn}
  \label{r23}
A {\em strongly upper-triangular} linear category is an
upper-triangular linear category $\modC $ such that for all $x\in \Ob(\modC )$,
we have $\modC (x,x)\cong \modZ $.
\end{defn}

Using that $\HH_0(\Z)=\Z$ and for $n>0$, $\HH_n(\Z)=0$,
from the previous lemma we immediately get the following.

\begin{cor}[\cite{BHLZ}]
  \label{r20}
  For a strongly upper-triangular linear category $\modC $, we have
  \begin{gather*}
    \Tr\modC =\HH_0(\modC ) \cong \End(\modC )\cong\modZ \Ob(\modC ),\\
    \HH_i(\modC )=0\quad \text{for $i>0$}.
  \end{gather*}
  Here $\modZ \Ob(\modC )$ denotes the free $\modZ $-module spanned by $\Ob(\modC )$.
\end{cor}


Let $\modC $ be an additive category, and let $B\subset \Ob(\modC )$ be a subset.
Denote by $\modC |_B$ the full subcategory of $\modC $ with
$\Ob(\modC |_B)=B$.

The set $B$ is called a {\em strongly upper-triangular basis} of
$\modC $ if the following two conditions hold.
\begin{enumerate}
\item The inclusion functor $\modC |_B\rightarrow \modC $ induces equivalence of additive
  categories $(\modC |_B)^\oplus\simeq \modC $.
\item $\modC |_B$ is strongly upper-triangular.
\end{enumerate}

\begin{prop}[\cite{BHLZ}]
  \label{r24}
  Let $\modC $ be an additive category with a strongly upper-triangular
  basis $B$.  Then we have
  \begin{gather*}
    \Tr\modC =\HH_0(\modC )\cong \modZ B,\\
    \HH_i(\modC )=0\quad \text{for $i>0$}.
  \end{gather*}
\end{prop}


\begin{remark} \label{rem-overk}
For $\k$-linear categories it is natural to modify the Definition~\ref{r23} to define a strongly upper-triangular $\k$-linear category by requiring that for all $x\in \Ob(\modC )$,
we have $\modC (x,x)\cong \k$.  In that case, Corollary~\ref{r20} and Proposition ~\ref{r24} remain valid with $\Z$ replaced by the field $\k$.
\end{remark}


An additive category is said to be {\em Krull-Schmidt} if any object has a unique decomposition into a finite direct sum of objects having local endomorphism rings.  That is to say, given an isomorphism $x_1 \oplus x_2 \oplus \dots \oplus x_r \cong y_1 \oplus y_2 \oplus \dots \oplus y_s$ where $x_i$ and $y_j$ are indecomposable, then $r=s$, and there exists some permutation $\sigma \in S_r$ such that $x_{\sigma(i)} \simeq y_i$.

\begin{exercise}
Show that any category $\C$ enriched in $\cat{Vect}_{\k}$, i.e. the hom spaces form vector spaces and composition is a bilinear map, is Krull-Schmidt if and only if all idempotents split.
\end{exercise}

In a Krull-Schmidt category  $\C$ the classes of indecomposables in the split Grothendieck group $K_0(\C)$ give rise to a distinguished basis.
When $\C$ is a graded linear category, then the graded hom between a pair of objects $x$, $y \in \Ob(\C)$ is defined as
\[
 \HOM_{\C}(x,y) := \bigoplus_{k \in \Z} \Hom_{\C}(x, y \la k \ra).
\]
When $\C$ is a graded $\k$-linear category, this graded hom gives rise to a sesquilinear inner product $\la - , - \ra \maps K_0(\C) \times K_0(\C) \to \Z((q))$ defined by
\[
 \la [x]_{\cong}, [y]_{\cong} \ra := \dim_q \HOM_{\C}(x,y) = \sum_{k \in \Z} q^k \dim \Hom_{\C}(x, y \la k\ra).
\]

One consequence of a graded linear category possessing a
strongly upper triangular basis $B$ is that the classes of $B$ in the Grothendieck group satisfy the property that for any pair $x, y \in B$, we have
\[
 \la x, y \ra \in \delta_{x,y} + q\N[q],
\]
in which case the basis resulting from $B$ is said to be {\em almost orthogonal}.

\vspace*{3mm}
\noindent
{\bf Remarks for experts}.
Strongly upper triangular bases often arise in geometric constructions where the categories of interest are categories of sheaves on certain varieties.
Usually one starts with a triangulated category $\C$ and produces an abelian category $\cal{A}$ as the heart of a $t$-structure for $\C$. Distinguished basis  $B$ arise as the simple objects in the heart of the corresponding $t$-structure.
 If $\cal{A}$ is endowed with a grading given by the cohomological ${\rm Ext}$-grading from $\C$, then the resulting basis of simple objects
 is strongly upper triangular and their classes in the Grothendieck group are almost orthogonal.

For example, categories of perverse sheaves are the heart of a certain $t$-structure on the derived category of sheaves~\cite{BBD}.
 In this way, simple perverse sheaves naturally give rise to distinguished bases in geometric representation theory.  The Kazhdan-Lusztig
 basis of a Hecke algebra associated to a Weyl group $W$ arise in this way~\cite{KazLus}.  Likewise, simple integrable representations and
 their tensor products of quantum Kac-Moody algebra  possess canonical bases~\cite{Lus1,Lus2,Lus3,Lus4,Kash1,Kash2}. Outside of geometry,
there is a $t$-structure on the bounded derived category $D^b(\Lambda{\rm -mod})$ of a finite-dimensional $\k$-algebra $\Lambda$ in which
the simple $\Lambda$-modules form a strongly upper triangular basis in the heart of the $t$-structure~\cite{AN}.
