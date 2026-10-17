---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-003-22-neumannzagier-data
section_title: "Neumann–Zagier data"
section_number: 2.2
pages: 6-8
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.96
---
\label{sub.NZ}

In this section, we discuss in detail Neumann--Zagier data following~\cite{DG}.
We start with a 3-manifold $M$ with torus boundary component (all manifolds and their
triangulations will be oriented throughout the paper) equipped with
a concrete oriented ideal triangulation, that is with a triangulation such that
each tetrahedron $\Delta$ of $\calT$ comes with a bijection of its vertices with
those of the standard 3-simplex. (All triangulations that are used in the computer
programs \texttt{SnapPy}~\cite{snappy} and \texttt{Regina}~\cite{regina} are concrete).

Every concrete tetrahedron $\Delta$ has shape parameters $(z,z',z'')$ assigned to
pairs of opposite edges as in Figure~\ref{fig.tetshapes}, where the complex numbers
$z'=1/(1-z)$ and $z''=1-1/z$ satisfy the equations
\be
\label{3z}
z''+z^{-1}=1, \qquad z z' z'' =-1 \,.
\ee

\begin{figure}[htpb!]
\begin{center}  
\begin{tikzpicture}[baseline=-3] 
    
\filldraw (2,3.5) circle (2pt) node[above] {$0$};
\filldraw (0,0) circle (2pt) node[below] {$1$};
\filldraw (4,1) circle (2pt) node[right] {$2$};
\filldraw (0.5,2) circle (2pt) node[left] {$3$};;
\draw (0,0) -- (2,3.5);
\draw (0,0) -- (4,1);
\draw (0,0) -- (0.5,2);
\draw (4,1) -- (2,3.5);
\draw (0.5,2) -- (2,3.5);
\draw[dashed] (0.5,2) -- (4,1);

\filldraw[white] (1.3,2.2) circle (6pt);
\filldraw[white] (2.2,1.5) circle (5pt);
\filldraw[white] (3,2.3) circle (6pt);
\filldraw[white] (0.25,1) circle (7pt);
\filldraw[white] (2.6,0.75) circle (8pt);
\filldraw[white] (1,2.5) circle (8pt);

\node at (1.3,2.2) {$z$};
\node at (2.2,1.5) {$z$};
\node at (3,2.3) {$z'$};
\node at (0.25,1) {$z'$};
\node at (2.6,0.75) {$z''$};
\node at (1,2.5) {$z''$};

\end{tikzpicture}
  \caption{The shapes of an ideal tetrahedron.}
\label{fig.tetshapes}
\end{center}
\end{figure}

If $\calT$ is a triangulation as above, an Euler characteristic argument shows
that the number of tetrahedra equals to the number of edges. Fix an ordering
of the tetrahedra $\Delta_j$ for $j=1,\dots,N$ and of the edges $e_1,\dots,e_N$
of $\calT$, and assign a shape $z_j$ to the tetrahedron $\Delta_j$ for $j=1,\dots,N$.
To describe the complete hyperbolic structure of $M$ (when it exists) and its
deformations, Thurston~\cite{Th} introduced the gluing equations
for the variables $z=(z_1,\dots,z_N)$ 
around each edge $e_i$, for $i=1,\dots, N$. In logarithmic form, these equations
have the form
\be
\label{3G}
\sum_{j=1}^N G_{i,j} \log z_j + G'_{i,j} \log z'_j + G''_{i,j} \log z''_j \= 2 \pi i,
\qquad (i=1, \dots, N)
\ee
where $G_{i,j}$ (and likewise for $G'_{i,j}$ and $G''_{i,j}$) denote the number
of times that an edge of $\Delta_j$ labelled $z_j$ winds around the edge $e_i$.
Every peripheral curve $\gamma$ in the boundary also gives rise to a gluing
equation of the same form as~\eqref{3G}, except the right hand side is $0$
instead of $2 \pi i$. Choosing a symplectic basis for $H_1(\partial M,\BZ)$, we
can enhance the equations~\eqref{3G} by adding the peripheral equations
\be
\label{3Gb}
\sum_{j=1}^N G_{N+c,j} \log z_j + G'_{N+c,j} \log z'_j + G''_{N+c,j} \log z''_j
\= 0, \qquad (c=1,2) \,.
\ee
It turns out that the $(N+2) \times N$ matrices $G$, $G'$ and $G''$ have both
symmetry and redundancy. Any one of the edge equations is implies by the others,
and we make a choice to remove one of them, and replace it by one peripheral
equation for a fixed peripheral curve, resulting into $N \times N$ matrices
$\mathbf G$, $\mathbf G'$ and $\mathbf G''$. Using the second
Equation~\eqref{3z} in logarithmic form $\log z_j + \log z'_j + \log z''_j = \pi i$,
we can eliminate one of the three shapes of each tetrahedron (this is a choice of
quad). For example, eliminating the shape $z'_j$ for $j=1,\dots,N$ then results
into a system of equations
\be
\label{3Gc}
\sum_{j=1}^N A_{i,j} \log z_j + B_{i,j} \log z''_j \= \pi i \nu
\qquad (i=1, \dots, N)
\ee
where
\be
\label{AB}
A \= \mathbf G - \mathbf G', \qquad B \= \mathbf G'' - \mathbf G'
\ee
are the Neumann--Zagier matrices~\cite{NZ} and
$\nu = (2,\dots,2,0)^t -\mathbf G' (1,\dots,1,1)^t \in \BZ^N$.
The Neumann--Zagier matrices $(A\,| \,B)$ have an important symplectic property,
they are the upper part of a symplectic matrix over $\BZ[1/2]$ (and even a symplectic
matrix over $\BZ$ if one divides the peripheral gluing equation by 2 while keeping
the integrality of its coefficients)~\cite{NZ}. It follows that $A B^t$ is
symmetric, that $(A \,|\, B)$ has full rank, and that one can always choose a
quad such that $B$ is invertible--for this see~\cite[Lem.A.3]{DG}.

A further ingredient of a Neumann--Zagier datum is a flattening, that is a triple
$(f,f',f'')$ of vectors in $\BZ^N$ that satisfy the conditions
\be
\label{3f}
f + f' + f''=(1,\dots,1)^t, \qquad 
\mathbf G f + \mathbf G' f' + \mathbf G'' f'' = (2,\dots,2,0)^t \,.
\ee
Using our choice of quad, we can eliminate $f'$ and thus obtain a pair
$(f,f'')$ of vectors in $\BZ^N$ that satisfy the condition
\be
\label{2f}
A f + B f'' = \nu \,.
\ee
This defines all the terms that appear in a NZ-datum $\Xi=(A,B,\nu,z,f,f'')$. 
The definition of the series $\Phi^\Xi(\hbar)$ requires a nondegenerate NZ datum
$\Xi$, that is one that satisfies the condition $\det(B) \neq 0$, which as
we discussed above, can always be achieved, as well as the condition
$\det(\Lambda) \neq 0$. We discuss this choice next, and connect it to
the geometric representation of a hyperbolic 3-manifold $M$. 

We end this section with a comment regarding Neumann--Zagier data of 3-manifolds
with several (as opposed to one) torus boundary components. Their ideal
triangulations with equal number $N$ of tetrahedra as edges and the edge gluing
equations have the same shape~\eqref{3G} as above. If $r$ denotes the number of
boundary components, then there are $2r$ peripheral equations~\eqref{3Gb} and after
a choice of one peripheral curve per boundary component, this leads to $(N+r)\times N$
matrices $G$, $G'$ and $G''$. The edge gluing equations have redundancy, and although
it is not true that we can remove any $r$ of them, it is shown
in~\cite[Sec.4.6]{GHRS} that one can remove $r$ of them and and replace them by
$r$ peripheral equations so as to obtain $N \times N$ matrices 
$\mathbf G$, $\mathbf G'$ and $\mathbf G''$ such that the corresponding matrices
$(A \,|\,B)$ defined in~\eqref{AB} have the same symplectic properties as in the
case of $r=1$. Moreover, any two choices of removal of the $r$ edge equations are
related to each other by an invertible matrix in $\GL_r(\BZ)$. Finally, flattenings
satisfy Equations~\eqref{3f} where the right hand side of the second equation
is the vector $(2,\dots,2,0,\dots,0)^t \in \BZ^{N+r}$ with the first $N$ coordinates
equal to $2$ and the remaining $r$ coordinates equal to zero.

For simplicity in the presentation (related to the choice of peripheral curves and
the flattenings), we will give the proof of Theorem~\ref{thm.1} assuming that the
3-manifold $M$ has one cusp. The proof applies verbatim to the general case of
arbitrary number of cusps.
