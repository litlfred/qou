---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-004-3-polytope-decompositions
section_title: "Polytope decompositions"
section_number: 3
pages: 10-15
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.981
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
\label{s:polytope}


It will be convenient to rewrite the definition of Turaev--Viro (TV) 
invariants using not just triangulations, but more general cellular
decompositions. 
In this section we give precise definitions of these decompositions.



In what follows, the word ``manifold'' denotes a compact, oriented,
piecewise-linear (PL) manifold; unless otherwise specified, we assume that
it has no boundary. Note that in dimensions 2 and 3, the category of PL
manifolds is equivalent to the category of topological manifolds. For an 
oriented manifold $M$, we will denote by $\ov{M}$ the same manifold with
opposite orientation, and by $\del M$, the boundary of $M$ with induced
orientation. 

Instead of triangulated manifolds as in \ocite{barrett}, we prefer to
consider more general cellular decompositions, allowing individual
cells to be arbitrary polytopes (rather than just simplices); moreover,  
we will allow the attaching maps to identify some of the boundary points,
for example gluing polytopes so that some of the vertices coincide.
On the other hand, we do not want to consider arbitrary cell
decompositions (as is done, say, in \ocite{oeckl}), since it would make
describing the  elementary moves between two such decompositions more
complicated.  The following definition is the compromise; for lack of a
better word,   we will call such decompositions {\em polytope
decompositions}.

Recall that a cellular decomposition of a manifold $M$ is a collection 
of inclusion maps $B^d\to M$, where $B^d$ is the (open) $d$-dimensional
ball, satisfying certain conditions. Equivalently, we can replace
$d$-dimensional balls with $d$-dimensional cubes $I^d=(0,1)^d$. For a PL
manifold, we will call such a cellular decomposition a PL  decomposition 
if each inclusion map  $(0,1)^d\to M$ is a PL map. In particular, every
triangulation of a PL  manifold gives such a cellular decomposition (each
$d$-dimensional simplex is PL homeomorphic  to a $d$-dimensional cube).  

We will call a cell {\em regular} if the corresponding map $(0,1)^d\to M$
extends to a map of the closed cube $[0,1]^d\to M$ which is a
homeomorphism onto its image. 

\begin{definition}\label{d:polytope_d}
 A polytope decomposition of a  2- or 3-dimensional PL manifold $M$
(possibly with boundary) is a cellular   decomposition which can be
obtained from a triangulation by a sequence of moves 
 M1---M3 below (for $\dim M=2$, only moves M1, M2).
 
\begin{description}
 \item[M1: removing a vertex]
   Let $v$ be a vertex which has a neighborhood whose intersection with 
   the 2-skeleton is homeomorphic to the ``open book'' shown below with
    $k\ge 1$     leaves;    moreover, assume that all leaves in the
    figure are distinct 2-cells and the two
    1-cells  are also  distinct (i.e., not two ends of the same
    edge). Then move M1 removes vertex $v$ and replaces two 1-cells
  adjacent to it with a single 1-cell.

   \begin{figure}[ht]
   $$\figscale{0.7}{figures/M1a.eps}
     \xxto{\text{remove vertex } v}
     \figscale{0.7}{figures/M1b.eps}
   $$
  \caption{Move M1}\label{f:movef1}
  \end{figure}


 \item[M2: removing an edge]
   Let $e$ be a 1-cell which is regular and which is 
   adjacent to exactly two distinct 2-cells $c_1, c_2$ as shown in the
    figure below.  Then the move M2 removes the edge $e$ and replaces
  the cells $c_1,c_2$ with a  single cell $c$. 

   \begin{figure}[ht]
      $$\figscale{0.7}{figures/M2a.eps}
     \xxto{\text{remove edge } e}
     \figscale{0.7}{figures/M2b.eps}
   $$
  \caption{Move M2}\label{f:movef2}
  \end{figure}


 \item[M3: removing a 2-cell]
   Let $c$ be a 2-cell which is regular  and which is 
   adjacent to exactly two distinct 3-cells $F_1, F_2$ as shown in the
  figure below.  Then the move M2 removes the 2-cell $c$ and replaces the
  cells $F_1,F_2$ with a single cell $F$.

   \begin{figure}[ht]
   $$\figscale{0.7}{figures/M3a.eps}
     \xxto{\text{remove face } c}
     \figscale{0.7}{figures/M3b.eps}
   $$
  \caption{Move M3}\label{f:movef3}
  \end{figure}



\end{description}

A 2 or 3-dimensional PL manifold $M$ with boundary together with a choice
of polytope decomposition will be called a {\em combinatorial manifold};
for $\dim M=2$, we will also use the term ``combinatorial surface''. We
will use  script letters to denote combinatorial manifolds and Roman
letters for underlying PL manifolds.  
\end{definition}


Note that the extension of the  inclusion maps $(0,1)^d\to M$ to the 
boundary does not have to be injective. 

If $F$ is an oriented $d$-dimensional cell of a combinatorial manifold $\M$
(i.e., a pair consisting of a cell and its orientation), we can define
its boundary $\del F$ in the obvious way, as a formal union of oriented
$(d-1)$-dimensional cells. Note that $\del F$ can contain the same 
(unoriented) cell $C$ more than once: for example, one could have 
$\del F=\dots \cup C\cup \ov{C}\dots$. 
\begin{lemma}\label{l:delF}
If $\M$ is a combinatorial manifold  of dimension $d$ with boundary, then 
$$
\bigcup_{F}\del F=\Bigl(\bigcup_{C\in \del M} C\Bigr)
   \cup
     \Bigl(\bigcup_{c_{in}} c'_{in}\cup c''_{in}     \Bigr)
$$
where $F$ runs over the set of $d$-cells of $M$ \textup{(}each taken with
induced orientation\textup{)}, $C$ runs over the set of $(d-1)$-cells of
$\del M$ \textup{(}each taken with induced orientation\textup{)}, and
$c_{in}$ runs over the set of \textup{(}unoriented\textup{)} $(d-1)$-cells
in the interior of $M$, with $c', c''$ denoting two possible orientations
of $c$ \textup{(}so that $\ov{c'}=c''$\textup{)}. 
\end{lemma}


The main result of this section is the following theorem.

\begin{theorem}\label{t:moves}
  Let $M$ be a PL 2- or 3-manifold without boundary. Then any two
  polytope decompositions of $M$ can be obtained from each other by a
  finite sequence of moves M1--M3 and their inverses \textup{(}if $\dim
  M=2$, only     moves M1, M2 and their inverses\textup{)}.
\end{theorem}
\begin{proof}
 It is immediate from the definition that it suffices to prove that any
  two triangulations can be obtained one from another by a sequence of
  moves M1--M3 and their inverses. On the other hand, since it is 
  known that any two triangulations  are related by a sequence of Pachner
  bistellar moves \ocite{pachner}, it suffices to show that each Pachner
  bistellar move can be  presented as a  sequence of moves M1--M3 and
  their inverses. For
  $\dim M=2$,   this is left as an easy exercise to the reader; for $\dim
  M=3$, this is   shown in \firef{f:pachner1}, \firef{f:pachner2}.

   \begin{figure}[ht]
   \begin{align*}&\figscale{0.7}{figures/pachner1a.eps}
     \xxto{\text{remove face } ADE}
    \figscale{0.7}{figures/pachner1b.eps}
     \xxto{\text{remove edge } DE}
     \figscale{0.7}{figures/pachner1c.eps}
     \\ 
   &  \xxto{\text{remove face } CDBE}  
   \figscale{0.7}{figures/pachner1d.eps} 
    \xxto{\text{add face }ABC}
      \figscale{0.7}{figures/pachner1e.eps}
    \end{align*}
  \caption{Pachner 3-2 move as composition of elementary
            moves}\label{f:pachner1}
  \end{figure}



   \begin{figure}[ht]
    \begin{align*}&\figscale{0.7}{figures/pachner2a.eps}
       \xxto{\text{remove faces } AOB, DOC}
       \figscale{0.7}{figures/pachner2b.eps}
    \\ 
   & \qquad \xxto{\text{remove edges } AO, OB}
     \figscale{0.7}{figures/pachner2c.eps}
      \xxto{\text{remove vertex } O}  
   \figscale{0.7}{figures/pachner2d.eps} 
   \\
    & \qquad \xxto{\text{remove edge } DC}
      \figscale{0.7}{figures/pachner2e.eps}
      \xxto{\text{remove face } ADBC}
     \figscale{0.7}{figures/pachner2f.eps}
    \end{align*}
      
\caption{Pachner 4-1 move as composition of elementary
            moves}\label{f:pachner2}
  \end{figure}


\end{proof}

This can be generalized to manifolds with boundary.


\begin{theorem}\label{t:moves_rel}
  Let $M$ be a PL 2- or 3-manifold with boundary and let $\N$ be a
  polytope decomposition of $\del M$. Then
  \begin{enumerate}
  \item $\N$ can be extended to a polytope decomposition $\M$ of $M$.
  \item Any two polytope decompositions $\M_1, \M_2$ of $M$ which coincide
  with $\N$ on  $\del M$ can be obtained from each other by  a finite
  sequence of moves M1--M3 and their  inverses which do not change the
  polytope decomposition of $\del M$.
  \end{enumerate}
\end{theorem}
\begin{proof}
 The theorem immediately follows from the following two lemmas. 
 \begin{lemma}\label{l:moves_rel1}
  If $\N$ is a triangulation, then the statement of the theorem holds. 
 \end{lemma}
 \begin{lemma}\label{l:moves_rel2}
  If $\N$ is obtained from another polytope decomposition $\N'$ of $\del 
  M$ by a move M1, M2 \textup{(}only M1 if $\dim M=2$\textup{)}, and the
  statement of the theorem holds for $\N'$, then the statement of the
  theorem holds for $\N$.
 \end{lemma}
\begin{proof}[Proof of \leref{l:moves_rel1}]
  Follows from the relative version of Pachner moves \ocite{casali}.
\end{proof}
 \begin{proof}[Proof of \leref{l:moves_rel2}]


  We will do the proof in the case when $\dim M=3$ and $\N$ is obtained
  from $\N'$ by erasing an edge $e$ separating two cells $c_1, c_2$.  The
  proof in other cases is   similar and left to the reader. 

  Let $\M'$ be a polytope decomposition of the $M$ which agrees with
  $\N'$ on $\del M$; by assumption such a decomposition exists. Denote
  $c=c_1\cup e\cup c_2$. Let us glue to $\M'$ another copy of 2-cell $c$
  along the boundary of $c_1\cup e\cup c_2$ and a 3-cell $F$ filling the
  space between $c_1\cup e\cup c_2$ and $c$ as   shown in
  \firef{f:rel_moves2} 


   \begin{figure}[ht]
  $$
  \fig{figures/rel_moves2a.eps}\xxto{}\fig{figures/rel_moves2b.eps}
  $$
\caption{Proof of \leref{l:moves_rel2}}\label{f:rel_moves2}
  \end{figure}

  This gives a new
  manifold $\tilde M$ which is obviously homeomorphic to $M$, together
  with a polytope decomposition $\tilde M$ such that its restriction to the
  boundary is $\N$. This proves existence of extension. Moreover, it is
  immediate from the assumption on $\N'$ that any two polytope
  decompositions $\tilde M_1$, $\tilde M_2$ obtained in this way from
  polytope decomposition $\M'_1, \M'_2$  extending $\N'$  can be
  obtained from each other by a sequence of moves  M1,  M2 and their
  inverses which do not  change decomposition of $\del  M$.
  
  To prove the second part, let $\M_1$, $\M_2$ be two polytope
  decompositions which coincide  with $\N$ on $\del M$. Let us add 2-cells
  $c_1,c_2$ and an edge $e$ to to each of these
    decomposition as shown in \firef{f:rel_moves2b}; this  gives  new
  decompositions
  $\tilde \M_1,\tilde \M_2$ which are of  of the form discussed  above and
    thus can be obtained from each   other by  a sequence of moves
  M1,  M2 and their inverses which do not  change decomposition of $\del
  M$. 
  
   \begin{figure}[ht]
$$   \fig{figures/rel_moves3a.eps}\xxto{}\fig{figures/rel_moves3b.eps}$$
  \caption{Proof of \leref{l:moves_rel2}}\label{f:rel_moves2b}
  \end{figure}

  
 \end{proof}
\end{proof}

Finally, we will need a slight generalization of this result.

\begin{theorem}\label{t:moves_rel2}
  Let $M$ be a  3-manifold with boundary and let $X\subset \del M$ be a
  subset homeomorphic to a 2-manifold with boundary. Let $\N$ be a
  polytope decomposition of a $X$. Then
  \begin{enumerate}
  \item $\N$ can be extended to a polytope decomposition $\M$ of $M$
  \item Any two polytope decompositions $\M_1, \M_2$ of $M$ which coincide
  with $\N$ on  $X$ can be obtained from each other by  a finite
  sequence of moves M1--M3 and their  inverses which do not change the
  polytope decomposition of $X$.
  \end{enumerate}
\end{theorem}
A proof is similar to the proof of the previous theorem; details are left
to the reader.
