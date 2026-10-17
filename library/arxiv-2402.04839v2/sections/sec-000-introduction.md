---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.981
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
Let $M$ be a closed 3--manifold.
A topological invariant $\volt(M)$\footnote{The reader may interpret this as a quantification of how much potential the manifold has. We read this as \emph{topological volume} or \emph{volume topologique}. The name was coined with permission of Michel Boileau and Joan Porti.} is defined in~\cite{BBBMP} in an account of a complete proof of Thurston's Geometrisation Conjecture. Roughly speaking, this is the minimal volume of the complement of a (possibly empty) hyperbolic link in $M.$ Here we begin the study of this invariant in its own right by establishing some basic properties and computing it for certain families of non-hyperbolic 3--manifolds.

This introduces an interesting new organising principle for closed $3$--manifolds: Hyperbolic volume is one of the most widely used topological invariants for hyperbolic $3$--manifolds. By passing to hyperbolic links in (non-hyperbolic) manifolds we obtain a unified notion of volume for all $3$--manifolds. We show in \Cref{sec:Properties} that this volume invariant has interesting properties when studied over the whole class of closed 3--manifolds. Furthermore, we can partition the set of $3$--manifolds by asking for the number of components of the smallest volume hyperbolic link in $M$. Naturally, this number is zero if and only if $M$ is hyperbolic. It is an open question whether there exist manifolds for which this number is greater than one (cf. \Cref{que:unbounded_h(M)}).

As we demonstrate in this paper, topological volume is not just a theoretical concept. Instead, surprisingly powerful results about $\volt$ can be established by applying existing work on hyperbolic volume and exceptional surgeries. A key ingredient of our proofs is how hyperbolic volume behaves under Dehn filling according to work of J\o{}rgensen and Thurston \cite{thurston-notes,Gro81, Mai10}. This theory provides not just valuable tools, but also an insight into how hyperbolic volume is connected to the construction of general $3$--manifolds using Dehn surgery.

\paragraph{Related work}
A different but related \emph{link volume} was introduced by Rieck and Yamashita in~\cite{Rieck-link-2013}. A key difference between their invariant and $\volt$ is that there are at most finitely many 3--manifolds of the same topological volume (\Cref{pro:finiteness}) whilst there are examples of infinitely many 3--manifolds of the same link volume~\cite[Corollary 1.2]{Remigio-link-2012}. In this respect, our definition agrees with hyperbolic volume, since a given real number is realised as the volume of only finitely many hyperbolic 3--manifolds by J\o{}rgensen--Thurston theory \cite{thurston-notes,Gro81, Mai10}.

Another invariant that measures complexity of a closed orientable $3$-manifold $M$ is the Matveev complexity $c(M)$, which is defined as the
minimal number of vertices of a simple spine of $M$ \cite{Matveev}. It was shown that $c$ is additive under connected sum and agrees on irreducible manifolds that are not $S^3$, $\R P^3$, or $L(3,1)$ with the tetrahedral complexity $t(M)$. Our results show that $\volt$ behaves rather differently from $c$. For example we show in \Cref{sec:connected_sum} that $\volt$ is not additive under connected sum and in \Cref{ssec:upperlower} we observe that $\volt$ also behaves differently from the tetrahedral complexity $t$. 

On the other hand, we see a lot of overlap in our census of non-hyperbolic manifolds with topological volume at most $3.07$ with the census of non-hyperbolic manifolds of small Matveev complexity \cite{Matveev,complexity_census0,complexity_census}. For example all $19$ lens spaces with topological volume at most $3.07$ are a subset of the exactly $44$ lens spaces with Matveev complexity at most $5$, see Section 7 in \cite{complexity_census}.



\paragraph{Our contributions}

We begin, in \Cref{ssec:refinements}, by presenting some natural refinements of $\volt$. In particular, we consider $\volt_n(M)$ denoting the minimum over the volumes of all hyperbolic $n$-component links in $M$ and we define refinements of $\volt$ considering links representing a specified homology class. In the rest of \Cref{sec:Properties}, we establish some basic properties of $\volt$. In \Cref{sec:covers} we investigate how topological volume behaves under taking (branched) covers, and in \Cref{ssec:unbounded} identify sequences of closed 3--manifolds with unbounded topological volume, based on an observation on how topological volume interacts with classical topological invariants.

In \Cref{sec:bounds}, we strengthen these results by presenting upper and lower bounds for $\volt(M)$ for arbitrary closed $3$--manifolds $M$. In particular, the following two theorems can be proven as an application of results due to Adams \cite{Adams_Augmented}, Culler and Shalen \cite{Culler_Shalen2011,Culler_Shalen2012}, and Guzman and Shalen \cite{Guzman_Shalen,Guzman_Shalen2020}. 

\begin{theorem}\label{thm:surgery_bound}
  Let $M$ be a closed, orientable 3--manifold given by surgery along a nontrivial $n$-component link $L\subset S^3$ with crossing number $c=c(L)$. Then 
  \begin{equation*}
  	\volt(M)\leq \big(9c+15n-20\big)v_{oct}+4v_{tet}
  \end{equation*}
  where $v_{oct}\approx3.6638$ and $v_{tet}\approx1.01494$ are the volumes of a regular hyperbolic ideal octahedron and a regular hyperbolic ideal tetrahedron respectively.
\end{theorem}

\begin{theorem}\label{thm:lower_bounds}
    Let $M$ be a closed, orientable 3--manifold and $p$ be a prime. Then
    \begin{equation*}
        \frac{\operatorname{rk}(H_1(M;\Z_p))}{168.602}< \volt(M).
    \end{equation*}
    Moreover, we have $\volt(M)>3.08,$ $3.69$, $3.77$ for $\operatorname{rk}(H_1(M;\Z_2))>5$, $7$, $10$, respectively.
\end{theorem}

These bounds are asymptotically tight in the sense that there exist infinite families of $3$-manifolds, for which lower and upper bounds grow at the same rate up to a multiplicative constant: For instance, in \Cref{ex:SFS} we follow from \Cref{thm:surgery_bound,thm:lower_bounds} that for $M$ a Seifert fibered space over a genus $g$ orbifold with $n$ exceptional fibres of index $p$ a prime we have
\[ \frac{2g + n}{168.602} < \volt(M ) < 37g + 22n - 28.\] 

Dunfield's classification of exceptional Dehn fillings of cusped $3$--manifolds \cite{Du20} allows us to determine the exact topological volume of all non-hyperbolic closed $3$--manifolds of topological volume at most $3.07$. See \Cref{tab:complete} and \Cref{sec:computations} for summaries and discussion of observations arising from this computation.

The last result of this paper observes that for all but finitely many lens spaces, their volume minimiser arises as a Dehn filling of either the complement of the Whitehead link $W$ or its sister manifold $P$. Its proof exhibits the interesting interplay between the computation of topological volume of non-hyperbolic 3--manifolds and properties of the volume spectrum of cusped hyperbolic 3--manifolds.

\begin{theorem}\label{prop:lens-space-limit}
For all but finitely many homeomorphism types of lens spaces $L(p,q)$ ($p>q\geq 1$ coprime), the volume minimising link in $L(p,q)$ has complement one of $W(\frac{p'}{q'}, \infty)$ or $P(\frac{p''}{q''}, \infty)$, where the filling slopes $\frac{p'}{q'}$ and $\frac{p''}{q''}$ can be determined from an efficiently computable finite set. For $P$ this means that we fill along the unknotted component.
\end{theorem}

We hope that this survey over the properties of $\volt$, its refinements, and first results will convince the reader of the usefulness of this topological invariant as both an organising principle as well as a meaningful topological property. And in fact, our article has already inspired further work. In~\cite{schmalian} Schmalian proves that $\volt$ is algorithmically computable. More precisely he describes an algorithm that takes as input a triangulation of a $3$-manifold $M$ and a real number $\varepsilon>0$ and returns in finite time $\volt(M)$ up to an error of at most $\varepsilon$. Similar, results hold true for the refinements of $\volt$ that we discuss below. Moreover, in~\cite{volt2} $\volt$ is studied on product manifolds and computed for some manifolds with boundary. 

\textbf{Acknowledgements.} 
The authors thank the MATRIX Institute in Creswick and the Ma\-the\-ma\-tisches Forschungsinstitut Oberwolfach for a collaborative environment between different continents and time-zones during a tandem workshop in 2021. This is where this work was begun. They thank the organisers and participants of the workshop for stimulating conversations. Special mention goes to Jonathan Bowden, Jessica Purcell and Saul Schleimer for comments and contributions during the initial phase of this project. We also thank the anonymous referee for useful feedback. In particular, for providing the argument for the first statement of \Cref{cor:p-1}.

Figures~\ref{fig:m003}--\ref{fig:m034} were created using KLO~\cite{KLO}.

MK, AR, and ST thank the Max-Planck-Institut f\"ur Mathematik in Bonn, where parts of this work were carried out, for its hospitality. MK was supported by the SFB/TRR 191 \textit{Symplectic Structures in Geometry, Algebra and Dynamics}, funded by the DFG (Projektnummer 281071066 - TRR 191) and is now supported by a Ram\'on y Cajal grant (RYC2023-043251-I) and by project PID2024-157173NB-I00 funded by MCIN/AEI/10.13039/501100011033, ESF+ and FEDER, EU; and by a VII Plan Propio de Investigaci\'on y Transferencia (SOL2025-36103) of the University of Sevilla.
Research of JS and ST is supported in part under the Australian Research Council's Discovery funding scheme (project number DP190102259). JS thanks Michael Joswig and Technische Universit\"at Berlin, where parts of this work were carried out, for their hospitality. ET is supported by an Australian Government Research Training Program (RTP) Scholarship.
