---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-010-62-geometric-generators-for-q-normal-classes
section_title: "Geometric generators for Q-normal classes"
section_number: 6.2
pages: 13-16
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.928
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
The work of Kang-Rubinstein \cite[Theorem 2.1]{KR1} (also see 
Luo-Tillmann \cite[\sect2]{LT}) shows that the space 
$\tilde N(\T;\R) \subset \R^{7n}$  of all {\em closed normal classes} 
satisfying Haken's matching equations (including, for example, the 
boundary tori) has a basis given by {\em edge solutions} $\tilde E_i$ and 
{\em tetrahedron solutions} $\tilde T_j$ where $1\le i ,j \le n$. 
These project to {\em edge solutions} $E_i$ and {\em tetrahedron solutions} 
$T_j$ under the map which forgets triangular coordinates, giving the image $N(\T;\R) \subset \R^{3n}$. Define $Q_0(\T;\R)$ as the solutions of the $Q$-matching equations corresponding to closed normal surfaces. It is a result of \cite{To} that the $Q$-coordinates determine a normal surface up to multiples of the peripheral normal tori and so $Q_0(\T;\R)=N(\T;\R)$.

When considering the map from all 
closed normal classes to $Q$-normal solution space, the closed normal 
surface solutions coming from the boundary tori map to the zero vector. 
Thus, such a map introduces one linear relation for each cusp, which in fact 
gives the only relations (see for example the proof of \cite[Theorem 3.1]{KR1}), 
so $\dim Q_0(\T;\R) = 2n-r$,
Explicitly, the quad coordinates for $E_i$ are 
precisely the coefficients in the {\em edge equation} for the $i$th edge 
in $\T$, and the quad coordinates for $T_j$ are $(1,1,1)$ in the $jth$ 
tetrahedron and $(0,0,0)$ in all other tetrahedra. 

The space $Q(\T;\R)$ of all {\em Q-normal classes} is spanned by 
{\em edge solutions}, {\em tetrahedron solutions} and 
{\em peripheral curve solutions} (see \cite[Theorem 3.1]{KR1}).     
The peripheral curve solutions are linearly independent from the
edge and tetrahedron solutions, and there are two linearly independent 
peripheral curve solutions $M_k, L_k$ per cusp corresponding to a choice of 
basis (``meridian'' $\mu_k$, ``longitude'' $\lambda_k$) 
of $H_1(\bd_k M;\R)$ for each component $\bd_k M$ of $\bd M$. 
In fact, a suitable choice of $n-r$ edge solutions together with the $n$ 
tetrahedral solutions and the $2r$ peripheral solutions form a basis for 
the real solution space $Q(\T;\R)$, which therefore has dimension $2n+r$ 
(which also follows from \cite[Theorem 3.1]{KR1}). 
 
In fact the statements above follow from the symplectic relations of 
Neumann-Zagier (see \cite{NZ}, \cite{N}, \cite{Choi}). Let $A$ be the 
$n \times 3n$ gluing equation matrix for $\tri$, with rows given by 
$E_1, \ldots, E_n$. Then the $n \times 3n$ matrix of $Q$-matching equations 
$B$ is given by $B=AC$  where $C$ is the $3n \times 3n$ block diagonal 
matrix made up of $n$ copies of
$$
\begin{bmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0\end{bmatrix}
$$
(see Tillmann \cite{Ti}). We can also regard $C$ as the linear map 
$C: \R^{3n} \to \R^{3n}$
given by
$$
C(a_1, b_1, c_1, a_2, b_2, c_2, \ldots , a_n, b_n, c_n) 
= (-b_1+c_1, -c_1+a_1,-a_1+b_1, \ldots, -b_n+c_n, -c_n+a_n,-a_n+b_n).
$$
Then the $Q$-matching equations have coefficients $C(E_i)$ for 
$i=1, \ldots , n$. (Compare Section \ref{spun_normal_construction} above.)

Now the skew-symmetric pairing of Neumann-Zagier 

is given by
$$
\omega : \R^{3n} \times \R^{3n} \to \R, \qquad 
\omega(x,x') = Cx \cdot x'
$$
where $\cdot$ denotes the dot product. Explicitly, given vectors 
$$
x=(a_1, b_1, c_1, a_2, b_2, c_2, \ldots , a_n, b_n, c_n), 
x'=(a'_1, b'_1, c'_1, a'_2, b'_2, c'_2, \ldots , a'_n, b'_n, c'_n) 
\in   (\R^3)^n
$$
we have
$$
\omega(x,x') = \sum_{j=1}^n  \left(  
\begin{vmatrix} a_j & a_j' \\ b_j & b_j' \end{vmatrix} +  
\begin{vmatrix} b_j& b_j' \\ c_j & c_j' \end{vmatrix} +   
\begin{vmatrix} c_j& c_j' \\ a_j & a_j' \end{vmatrix}\right) .
$$
(Compare \cite{N,Choi}.)

It follows that $S \in \R^{3n}$ satisfies the $Q$-matching equations if 
and only if 
\be 
\label{Qmatch}
\omega(E_i,S) = C(E_i) \cdot S = 0 \text{ for all } i = 1, \ldots ,n.
\ee

It is immediate that each tetrahedral solution $T_j$ satisfies the 
$Q$-matching equations; in fact,  $C(T_j)=0$ so 
$\omega(x,T_j)= -\omega(T_j,x) = -C(T_j) \cdot x = 0$ for all $x \in \R^{3n}$.
Further, the {\em Neumann-Zagier symplectic relations}  say that all 
symplectic products of $E_i, M_k, L_k$ for $i=1,\ldots, n$, 
$k=1,\ldots,r$ are {\em zero} except that
$$
\omega(L_k,M_k) = 2 = -\omega(M_k,L_k)  \text{ for each }k=1, \ldots , r .
$$
Hence, we can conclude that the edge solutions $E_i$ and peripheral 
solutions $M_k,L_k$ satisfy the $Q$-matching equations.  
In  fact, with some more analysis, it can been seen that the tetrahedral 
solutions together with  a suitable choice of $n-r$ edge solutions  and 
the peripheral solutions form a basis for the real solution space $Q(\T;\R)$,
which has dimension $2n+r$.

As mentioned above, there is a basis for the $Q$-coordinates of spun 
normal surfaces given by appropriately chosen edge solutions 
$\{E_i \}_{i=1}^{n-r}$, all tetrahedral solutions $\{T_j \}_{j=1}^n$, and 
peripheral solutions $\{p_k M_k + q_k L_k\}_{k=1}^r$. Hence for each choice of 
$x_i,y_j,p_k,q_k \in \R$ we obtain a spun normal class
$$
S= \sum_i x_i E_i + \sum_j y_i T_j + \sum_k (p_k M_k +q_k L_k).
$$
A normal surface has two important invariants; its Euler 
characteristic and its boundary slope. These invariants give rise to 
two linear maps on the normal surface  solution space $Q(\T;\R)$.



\begin{defn}
The {\em formal Euler characteristic} is the linear map 
$$
\chi : Q(\T;\R) \to \R, \qquad \chi(S)= \sum_i -2x_i- \sum_j y_j 
$$
giving the usual Euler characteristic for embedded closed and spun normal 
surfaces.
\end{defn}

(See \cite{LT} for a detailed discussion of the closed case, and 
Appendix \ref{gen_angle_euler} for the spun normal case using generalised 
angle structures.)

\begin{defn} 
The {\em boundary} map 
$$
\bd : Q(\T;\R) \to H_1(\bd M;\R), \qquad \bd(S)= 
2 \sum_k (p_k \mu_k +q_k \lambda_k)
$$
gives the boundary slope and the direction of spinning for embedded spun 
normal surfaces. Here $\mu_k$ and $\lambda_k$ are the meridian and longitude of cusp $k$ as defined previously. 
\end{defn}

(See Tillmann \cite{Ti} for the details.\footnote{Our sign convention is 
opposite to that in \cite{Ti} and Regina v.4.96 (\cite{regina}),
but is consistent with the boundary map defined in \cite{N} and discussed 
in \sect \ref{ZNST} below.}) Note that at each cusp, a tail of a spun 
normal surface is an infinite annulus spiralling into the cusp. There are 
two possible directions of spinning for each such a tail.

We can compute the boundary  in terms of the Neumann-Zagier symplectic 
form: since
$$
\omega(S,M_k) = \omega(p_k M_k +q_k L_k,M_k)=-2q_k
$$
and
$$
\omega(S,L_k) = \omega(p_k M_k +q_k L_k,L_k)=2p_k
$$
we have
$$
\bd(S)= \sum_k \left(  -\omega(S,L_k) \mu_k + \omega(S,M_k) \lambda_k \right).
$$
Note that 
\begin{center}
\emph{$\bd(S)=0$ if and only if $S$ defines a closed normal class.}
\end{center}

Hence $N(\T;\R)$ is the solution space of the $Q$-matching equations 
(\ref{Qmatch}) together with the
additional equations 

\be 
\label{Qmatch_closed}
\omega(M_k,S) = \omega(L_k,S)  = 0 \text{ for all } k = 1, \ldots, r.
\ee

We now define a 
quadratic function which will play an important role 
in understanding the degree of terms in the 3D-index sums.

\begin{defn}
We define a {\em double arc} function 
\be
\delta : Q(\T;\R)  \to \R, \qquad 
\delta(S) = \sum_j ( a_j b_j+b_j c_j + c_j a_j),
\ee
for 
$$
S=(a_1, b_1, c_1, a_2, b_2, c_2, \ldots , a_n, b_n, c_n). 
$$
\end{defn}

Note that for $S \in Q(\tri;\Z_+)$, $a_j b_j +b_j c_j + c_j a_j$ counts the 
number of arcs of intersection between the quads of $S$ in tetrahedron $j$.
In particular,
\begin{center}
\emph{a normal surface solution $S \in Q(\T;\Z_+)$ is embedded if and only 
if $\delta(S)=0$.}
\end{center}

There is also an associated symmetric bilinear function 
$$
\delta : Q(\T;\R) \times Q(\T;\R) \to \R
$$
such that 
\be
\delta(S+S')=\delta(S)+\delta(S') + 2 \delta(S,S') 
\text{ for all } S, S' \in Q(\T;\R) .
\label{bilinear_delta}
\ee
Explicitly
$$
\delta(S,S') = \frac{1}{2}  
\sum_j ( a_j b_j' +b_j c_j' + c_j a_j' )+( a'_j b_j +b'_j c_j + c'_j a_j )
$$
if $S$ and $S'$ have quad coordinates in  $\R^{3n}$ given by
$$
[S]=(a_1, b_1, c_1, a_2, b_2, c_2, \ldots , a_n, b_n, c_n)
$$
and
$$
[S']=(a_1', b_1', c_1', a_2', b_2', c_2', \ldots , a_n', b_n', c_n').
$$
