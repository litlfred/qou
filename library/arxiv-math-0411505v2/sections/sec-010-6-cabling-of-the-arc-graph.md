---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-010-6-cabling-of-the-arc-graph
section_title: "Cabling of the arc graph"
section_number: 6
pages: 9-11
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
\lbl{sec.stateCJ}

Recall the operation of {\em cabling} $\K^{(n)}$ the knot projection $\K$ $n$ 
times.
 Recall that $a_1,\dots, a_{r+1}$ are the arcs of $\K$.
Each $a_l$ is in the cabling replaced by $n^2$ arcs $a^l_{i,j}$, 
$i,j=1,\dots, n$,
with the agreement that the 'long arcs' obtained by cabling arc $a_k$ will be
$a^k_{1j}$, $j=1,\dots, n$ and the 'small arcs' obtained by cabling of crossing
$k$ will be denoted by $a^k_{ij}$ for $i=2,\dots, n$ and $j=1,\dots, n$.
Note that all crossings which replace the original crossing $k$ have the
same sign, equal to the sign of the crossing $k$.
We make the following agreement: assume the parallel arcs 
$a^l_{i,1},\dots, a^l_{i,n}$
go horizontally from left to right. Then $a^l_{i,1}$ is the upmost one.
See figure below for part of Example \ref{ex.1} and of its
3-cabled version $\K^{(3)}$:
$$
\psdraw{cab41}{4in}
$$

We further let $K^{(n)}$ denote the link obtained from $\K^{(n)}$ by deletion
of the $n$ special long arcs $a^{r+1}_{1j}$, $j=1,\dots, n$.

Next we consider the arc-graph of the cabling of $\K$.
For example, part of the red-blue digraph $G_{\K}$ of Example \ref{ex.1} and 
of its 3-cabled version is depicted as follows:
$$
\psdraw{cab42}{3.5in}
$$
where vertical edges are blue and horizontal edges are red.

We now define an n-cabling $G_K^{(n)}$ of the arc-graph $G_K$. 
Cabling of a planar projection is a local operation, and
so is cabling of a digraph. In the language of combinatorics, we blow up
the vertices of $G$ using a suitable {\em gadget}. For a similar discussion,
see also \cite[Section 4]{GL}.



\begin{definition}
\lbl{def.cabled2}
Fix a red-blue arc-graph $G_K$. Let $G_K^{(n)}$
denote the digraph with vertices $a^v_j$ for $v$ a vertex of $G_K$ 
and $j=1,\dots,n$.
$G_K^{(n)}$ contains blue directed edges $(a^l_j,a^{l+1}_j)$ with weight
$t^{-\e n}$ (where $\e \in \{-1,+1\}$ is the sign of the crossing $l$)
for each $l=1,\dots,r-1$ and $j=1,\dots,n$. Moreover,
if $(a_k,a_l)$ is a red directed edge of $G_K$, then $G_K^{(n)}$ contains
red edges $(a^k_i,a^l_j)$ for all $i,j=1,\dots n$ with weight
$t^{(j-1)}(1-t)$ resp. $t^{-(n-j)}(1-t^{-1})$, if the sign of the $i$ 
crossing is $-1$ resp. $+1$. Notice that the weights of the red edges are 
independent of the index $i$. 
\end{definition}



\begin{lemma}
\lbl{lem.evenn}
There is a 1-1 correspondence
$$
\{\text{\rm{admissible subgraphs of}} \,\,
G_{K^{(n)}}\} \longleftrightarrow 
\{\text{\rm{admissible subgraphs of}} \,\, G_K^{(n)} \}.
$$
\end{lemma}

We will denote the set of admissible even subgraphs of $G_K^{(n)}$ by 
$\Sev_n(G_K)$.


\begin{proof}
Denote by $p^k_j$ path $(a^k_{1j},a^k_{2j}, \dots, a^k_{nj})$ of $n-1$
blue edges in $G_{K^{(n)}}$, $k=1,\dots, r$ and $j=1,\dots,n$. 
There is a natural map $G_{K^{(n)}}\longto G_K^{(n)}$ which contracts each 
directed path $p^k_j$ into its initial vertex, and deletes all vertices 
$a^{r+1}_{ij}$.
Forgetting the weights, it is clear that the result of the contraction
coincides with $G_K^{(n)}$.

$G_{K^{(n)}}$ has two types of vertices: $a^k_{ij}$ for
$k=1,\dots, r+1$ and $i,j=1,\dots,n$ and $i \neq 1$ (call these white)
and $a^k_{1j}$, $k< r+1$ (call these black). The indegree of a white vertex 
is $1$, but the indegree of a black vertex may be higher. The black vertices
are the initial vertices of the paths $p^k_j$, hence the vertices
of $G_K^{(n)}$. Let $E^{\{n\}}$ and $E^{(n)}$ denote the set of edges of 
$G_{K^{(n)}}$ 
and $G_K^{(n)}$ respectively. Then each edge $e$ of $E^{(n)}$ replaces the 
unique 
directed path $P_e$ of $G_{K^{(n)}}$ between the corresponding black 
end-vertices of $e$, 
which contains no other black vertices.
If $E \subset E^{\{n\}}$ is an admissible even subgraph of $G_{K^{(n)}}$ 
then $E$ is a vertex-disjoint union of directed cycles of  $G_{K^{(n)}}$
and each directed cycle may be decomposed into directed paths between the 
black vertices.
If each such directed path is replaced by a directed edge, we get an admissible
even subgraph $E'$ of $G_K^{(n)}$. This gives the 1-1 correspondence between 
the admissible even subgraphs without the weights. To realize that the 
weights are correct as well, we only need to compare the product of the 
weights in $G_{K^{(n)}}$ along $P_e$ with the weights of $e$ in $G_K^{(n)}$.
\end{proof}

Theorem \ref{thm.arcjonesn} and Lemmas \ref{lem.arc}, \ref{lem.evenn} 
imply that:

\begin{lemma}
\lbl{lem.arcjonesnn}
For every knot $\K$ and every $n \in \BN$, we have
$$
J_n(\K, t)=
t^{n \d(K)} \sum_{c \in \Sev_n(G_K)} t^{\d(c)} \b(c). 
$$
\end{lemma}

Our next task is to figure out $\d(c)=\exc(c)-\rot(c)$ for $c\in \Sev_n(G_K)$. 

The following lemma is clear from the Definition \ref{def.rotten}: 

\begin{lemma}
\lbl{lem.rot}
If $f$ is a flow on $G_K$ and $\ti f$ is a lift
of $f$ to flow on $G_K^{(n)}$,
for some $n$, then $\rot(f)=\rot(\ti f)$.
\end{lemma}
