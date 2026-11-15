---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-023-45-two-categorifications-of-lusztigs-integral-fo
section_title: "Two categorifications of Lusztig's integral form A(sl2)"
section_number: 4.5
pages: 30-32
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.967
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a higher categorical level."
---
Here we present the results of \cite{Lau1,KLMS} computing $K_0$ and
of \cite{BHLZ} computing $\Tr$ of $\Ucat(\mf{sl}_2)$.

The algebra $\UA(\mf{sl}_2)$ has a well-known basis, called
Lusztig's canonical basis $\Bbb B$ consisting of
\begin{enumerate}[(i)]
     \item $E^{(a)}F^{(b)}1_{n} \quad $ for $a,b\geq 0$,
     $n\in\Z$, $n\leq b-a$,
     \item $F^{(b)}E^{(a)}1_{n} \quad$ for $a$,$b\geq 0$, $n\in\Z$,
     $n\geq
     b-a$,
\end{enumerate}
where $E^{(a)}F^{(b)}1_{b-a}=F^{(b)}E^{(a)}1_{b-a}$.
Let $_m\Bbb B_n$ be set of elements in $\Bbb B$ belonging to $1_m(\UA)1_n$.

















We associate to
 each $x \in \Bbb B$  a $1$-morphism in $\UcatD$ as follows:
\begin{equation} \label{eq_basis}
  x \mapsto \cal{E}(x) := \left\{
\begin{array}{cl}
  \cal{E}^{(a)}\cal{F}^{(b)}\onen & \text{if $x=E^{(a)}F^{(b)}1_n$,} \nn \\
  \cal{F}^{(b)}\cal{E}^{(a)}\onen & \text{if $x=F^{(b)}E^{(a)}1_n$.} \nn
\end{array}
  \right.
\end{equation}
Let $\B=\{\E(x)\mid x\in\Bbb B\}$
and $_m\B_n =\{\E(x)\mid x\in\, _m{\Bbb B_n}\}$.


The first categorification of $\UA$ was given in \cite{Lau1} where the decategorification functor is given by $K_0$.  The original proof worked with the 2-category $\UcatD(\mf{sl}_2)$ defined over a field $\k$, so that spaces of 2-morphisms formed vector spaces and the Krull-Schmidt property could be utilized.  In rank one the choice of scalars $Q$ does not enter the definition.  Later this result was enhanced in \cite{KLMS} to prove the result when working over the integers.   Unique decomposition for spaces of 2-morphisms follows as a corollary of these results, implying that the category $\U_{\Z}(\mf{sl}_2)$ is Krull-Schmidt. Very recently, it was shown in \cite{BHLZ} that $\Udot_\Z$ also categorifies $\UA$ via the alternative trace decategorification functor $\Tr$.

\begin{thm}\label{K0}
(\cite{KLMS}, \cite{BHLZ}) For ${\fsl}_2$,
$\B$ is the strongly upper triangular basis of $\Udot_\Z$.
The maps
\[ \begin{array}{rrr}
\gamma\maps  \UA & \longrightarrow& K_0(\UcatD_\Z)
\\
   x & \mapsto & [\cal{E}(x)]_{\cong} \end{array}\quad{\text{and}}\quad
\begin{array}{rrr}
  h_{\Udot_\Z}\maps K_0(\Udot_\Z)&\longrightarrow& \Tr(\U_\Z)\\
 x &\mapsto & [1_x] \\
\end{array}\]
are isomorphisms of graded linear categories, providing two categorifications of $\UA$.
\end{thm}






\subsubsection{Strategy of the Proof}



In section 6 of \cite{BHLZ}, based on the results of  \cite{KLMS} we give an
explicit presentation of the subcategory $\Udot(n,m)_\Z|_{_m\B_n}$
by generators and relations, which shows that this category is strongly upper triangular.
Hence, the indecomposable 1-morphisms from $\B$ generates $K_0$ and, by Proposition \ref{r24}, also $\Tr$ as $\Z[q,q^{-1}]$-modules. In \cite{KLMS} explicit isomorphisms in $\Udot_\Z$ are given lifting the
the defining relations of $\UA$, showing that $\gamma$ is an isomorphism of graded categories. Since the functor $h_{\Udot}: K_0(\Udot_\Z) \to \Tr(\Udot_\Z)$ preserves composition.
Finally, we use that $\Tr(\Udot)=\Tr(\U)$, the result follows.







\subsection{Two categorifications of $\UA ({\mathfrak sl}_n)$}


Here we present the results of  \cite{KL3} computing $K_0$ and
of \cite{BGHL} computing $\Tr$ for general $n$.

There is a special choice of scalars, where all $t_{i\, j}=1$  for $1\leq i< n-1$.  In this case, the graphical calculus is cyclic with respect to the biadjoint structure, so that isotopic diagrams represent the same 2-morphism.   This will be our default choice of $Q$ in sections unless explicitly stated otherwise. We will omit explicitly mentioning $Q$ in the notation when no confusion is likely to arise.




Theorem \ref{K0} was possible because the explicit isomorphisms constructed in \cite{KLMS} provide decompositions of arbitrary 1-morphisms into indecomposables.   However, the lack of an explicit description of the canonical basis for $\UA$ beyond $\mf{sl}_2$ presents an obstacle to generalizing this result beyond $\mf{sl}_2$.   However, if one works with the 2-category $\Ucat(\mf{sl}_n)$ defined over a field $\k$ of characteristic 0, then one can utilize various connections between this category and known geometric constructions to prove the following result.


\begin{thm}\label{K0n}
(\cite{KL3}, \cite{BGHL}) Let $\k$ be a field of characteristic $0$.
For ${\mathfrak {sl}}_n$,
the 2-category $\Udot$
is strongly upper triangular (see Remark~\ref{rem-overk}).
Moreover,
$$K_0(\Udot)=\UA$$
as graded linear categories and
$$\Tr(\U)=K_0(\Udot)\otimes_\Z \k, \quad
\HH_i(\U)=0 \quad{\text {for}}\quad i>0.$$
\end{thm}



Following a recommendation
of the first author, the $\fsl_3$ case of this theorem was studied in
\cite{Marko}.





\subsubsection{Strategy of the Proof}


Let us make few remarks about the proof.
The result about $K_0$ was proved in \cite{KL3}. It relies on the fact that
$\Udot$ is Krull-Schmidt.  To control the size of $K_0$ an action of $\Udot$ was defined on the cohomology rings of partial flag varieties.
Even when for $n>2$, the explicit form of the Lusztig canonical basis is not known,
but the results of \cite{VV} and \cite{Web4} allows us to deduce that
$\Udot$ is strongly upper triangular.
The full argumentation will be given in \cite{BGHL}.





\subsubsection{Applications}




In \cite{LQR,QR} it was shown that $\mf{sl}_n$ link homology theories can be obtained
from $\Udot(\fsl_m)$ by means of the so-called foamation functors $F$, first studied in \cite{MackFoam}.
More precisely, there is an extended version $2{\rm BFoam}$ of the Bar-Natan foam category introduced by Blanchet~\cite{Blan}.   (The advantage of Blanchet's version is that it
is functorial with respect to link cobordisms, when Bar-Natan version is functorial up to sign.)
In \cite{LQR,QR} an analog $n{\rm BFoam}$ of the Blanchet foam category for $\mf{sl}_2$ is defined for $\mf{sl}_n$ and families of 2-representations $F$ for were defined from $\Udot(\fsl_m)$ into the foam categories $n{\rm BFoam}$.


A general procedure was laid out by Cautis ~\cite{Cautis-clasp} using categorical skew Howe duality to pull back complexes associated to a tangle to a complex in $\Kom(\Udot)$.  Combining this with the foamation functors allows one to pull back the complexes of foams associated to a tangle to a complex in $\Kom(\Udot)$.   It was shown that all of the foam relations used for $\mf{sl}_n$-link homology arise from relations in $\Udot(\fsl_m)$ via foamation functors.  These foamation functors categorify a skew Howe functor defined at the decategorified level by Cautis, Kamnitzer, and Morrison that realize web relations from relations in the quantum group $\dot{\mathbf{U}}_q(\mf{sl}_m)$~\cite{CKM}.



Recall that we have two flavors of Euler characteristic associated with $K_0$ and $\Tr$,
\begin{eqnarray*}
\chi_{\tr}: &\Kom(F(\U)) \to \Tr(F(\U))\\
\chi: &\Kom(F(\Udot)) \to K_0(F(\Udot))  .
\end{eqnarray*}
Below is one of the applications of Theorem \ref{K0n}.

\begin{cor}\label{chi}
In $\mf{sl}_n$ link homologies theories, we have
$$\chi_{tr}=\chi\, .$$
\end{cor}


\begin{remark}
The $\mf{sl}_2$ case of  Corollary \ref{chi} was first proven  by Cooper-Krushkal~\cite[Section 3]{CK2}.
\end{remark}


\begin{proof}

Let $\C:=F(\Udot(\fsl_m))$. We have the Chern character map
$h_\C: K_0(\C) \to \Tr(\C)$ sending $[x]_{\cong} \to [1_x]$. The induced  map $\chi \to \chi_{\tr}$ is surjective,
since $\chi_{\tr}$ uses trace classes of the identity maps only.
It remains to show that this map is injective.
Note that $K_0(\Udot)$ is freely generated by indecomposables and $h_{\Udot}$ is an isomorphism after tensoring with any field of zero characteristic by Theorem \ref{K0n}, so
 $h_{\Udot}$ is injective. Hence, $F(K_0(\Udot))=F(h_{\Udot}(K_0(\Udot)))$. The fact that any linear functor commutes with $K_0$ implies the result.
\end{proof}
