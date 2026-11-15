---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-080-152-the-solution-space
section_title: "The solution space"
section_number: 15.2
pages: 458-469
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.991
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{solution:space:section}
In this section we study the combinatorial properties of ideal triangulations of three-manifolds in general. We study the space of solutions to the consistency equations, we prove that it is a complex manifold and exhibit a concrete parametrisation via the holonomy of peripheral curves.


\subsection{Edges and tetrahedra}
Throughout this section, we let $N$ be a compact oriented three-manifold $N$ with $\partial N = T_1 \sqcup \ldots \sqcup T_c$ consisting of tori, and define $M=\interior N$. Let $\calT$ be any ideal triangulation for $M$. 

\begin{prop} \label{edges:prop}
The ideal triangulation $\calT$ has the same number $n$ of tetrahedra and edges.
\end{prop}
\begin{proof}
The total space $|\calT|$ of the triangulation $\calT$ has $v$ vertices, $e$ edges, $f$ faces, and $t$ tetrahedra. Since $\chi(\partial N) = 2\chi(N)$ for every compact 3-manifold $N$ and $\partial N$ consists of tori, we get $\chi(N)=0$. Therefore
$$v = v + \chi(N) = \chi(|\calT|) = v-e+f-t = v-e+t$$
since $f = 2t$. Then $e=t$.
\end{proof}

Recall that in the consistency equations we get one complex variable $z_i$ for each tetrahedron and one equation for each edge; since we have the same number of edges and tetrahedra, one would guess that the solutions form typically a discrete set of points, but this is surprisingly not the case: we now show that some equations are redundant, leaving some space for a higher-dimensional space of solutions. The origin of this redundancy lies in the combinatorial properties of three-dimensional triangulations.


\subsection{Incidence matrices} \label{incidence:matrices:subsection}
We denote respectively by $\Delta_1, \ldots, \Delta_n$ and $e_1,\ldots, e_n$ the tetrahedra and edges of $\calT$. We fix an orientation on $M$, which induces an orientation on each tetrahedron, and we assign numbers 1, 2, and 3 to pairs of opposite edges on each $\Delta_i$ in a way that is orientation-preservingly isomorphic to Figure \ref{tetrahedron_labels:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {tetrahedron_labels.pdf} 
\nota{We label the edges of every \emph{oriented} tetrahedron as shown: the labelling is determined once we chose arbitrarily a pair of opposite edges and label them with 1 (left). The vertices of every \emph{oriented} triangle in the triangulated boundary inherit labels as in the figure (right).}
\label{tetrahedron_labels:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{ABmatrices-BW}{ABmatrices}} 
\nota{The incidence matrices $A$ and $B$ count the incidences between edge pairs, tetrahedra, edges, and ideal vertices.}
\label{ABmatrices:fig}
\end{center}
\end{figure}

We now define a $2n \times 3n$ integral matrix $A$ that encodes some combinatorial adjacencies between tetrahedra. The matrix $A$ should be seen as a $2\times 3$ rectangle of $n\times n$ sub-matrices as in Figure \ref{ABmatrices:fig}-(left), where:
\begin{itemize}
\item each column of $A$ corresponds to a pair of opposite edges of one tetrahedron, more precisely the columns $i, i+n,$ and $i+2n$ correspond the opposite edges of type 1,2,3 of $\Delta_i$;
\item the first $n$ rows of $A$ correspond to the tetrahedra $\Delta_1,\ldots, \Delta_n$;
\item the last $n$ rows of $A$ correspond to the edges $e_1,\ldots, e_n$.
\end{itemize}
When $i\leqslant n$, the entry $A_{ij}$ is 1 or 0 depending on whether $\Delta_i$ contains the $j$-th edge pair. In other words, the top three $n\times n$ sub-matrices of $A$ are three identity matrices, see Figure \ref{ABmatrices:fig}-(left).

When $i=n+i'$ with $i'>0$, the entry $A_{ij}$ counts how many edges in the $j$-th edge pair are glued to the $i'$-th edge $e_{i'}$: this number is hence 0, 1, or 2.

\begin{ex}
The entries on each column of $A$ sum to $3$.
\end{ex}

Let now $v_1,\ldots, v_c$ be the ideal vertices of $\calT$. We define another $c \times 2n$ integral matrix $B$, which consists of two $c\times n$ sub-matrices as in Figure \ref{ABmatrices:fig}-(right), where:
\begin{itemize}
\item the rows of $B$ correspond to the ideal vertices $v_1,\ldots, v_c$;
\item the first $n$ columns of $B$ correspond to the $n$ tetrahedra $\Delta_1,\ldots, \Delta_n$;
\item the last $n$ columns correspond to the edges $e_1,\ldots, e_n$.
\end{itemize}

When $j \leqslant n$, the entry $B_{ij}$ is \emph{minus} the number of times $\Delta_j$ is incident to $v_i$, and when $j = n+j'$ with $j'>0$ the entry $B_{ij}$ is \emph{plus} the number of times $e_{j'}$ is incident to $v_i$. The possible entries are $0,-1,-2,-3,-4$ and $0,1,2$ respectively.

\begin{ex}
The entries on each column of $B$ sum to $-4$ or $2$.
\end{ex}

The matrices $A$ and $B$ are designed to be interpreted as linear maps, and to be composed.

\begin{prop} \label{AB:exact:prop}
The following sequence is exact:
$$ \matR^{3n} \stackrel{A}{\longrightarrow} \matR^{2n} \stackrel{B}{\longrightarrow} \matR^c \longrightarrow 0.$$
\end{prop}
The proof of this proposition splits into three lemmas. 

\begin{lemma} We have $BA = 0$.
\end{lemma}
\begin{proof}
The $i$-th row of $B$ corresponds to the ideal vertex $v_i$ and the $k$-th column of $A$ corresponds to the $k$-th pair of opposite edges. The sum $\sum_{j=1}^{2n} B_{ij} A_{jk}$ counts \emph{minus} the number of times $v_i$ is incident to the tetrahedron containing the edge pair, \emph{plus} the number of times it is incident to the two edges of the pair. These numbers are equal and hence we get 0.
\end{proof}

\begin{lemma} The $c$ rows in $B$ are independent vectors.
\end{lemma}
\begin{proof}
Suppose there is a vanishing linear combination $\sum_{i=1}^c \lambda_i B_i = 0$ of the rows $B_i$ of $B$. If the edge $e_j$ has endpoints at $v_a$ and $v_b$, the entries in the $(n+j)$-th column $B^{n+j}$ are 1 at the rows $a$ and $b$ and zero everywhere else: therefore we get $\lambda_a+\lambda_b=0$. If we apply this argument to the three edges of a triangle we get
$$\lambda_a+\lambda_b=0, \quad \lambda_b+\lambda_c=0, \quad \lambda_c+\lambda_a = 0$$
which implies $\lambda_a=\lambda_b=\lambda_c=0$. Then all coefficients $\lambda_a$ vanish.
\end{proof}

\begin{lemma} \label{B:surj:lemma}
The $c$ rows in $B$ generate $\ker(A^\intercal)$. 
\end{lemma}
\begin{proof}
Since $BA=0$ implies $A^\intercal B^\intercal=0$, we already know that the rows in $B$ are contained in $\ker(A^\intercal)$, and we must prove that they generate it. We pick a generic horizontal vector $q=(q_1, \ldots, q_{2n})\in \matR^{2n}$ with $qA=0$ and we need to prove that $q$ is generated by the rows $B_i$ of $B$. 

Recall that the columns $A^j, A^{j+n}, A^{j+2n}$ of $A$ correspond to the edge pairs of type 1, 2, and 3 of the tetrahedron $\Delta_j$. We label the vertices of $\Delta_j$ as $a,b,c,d$, the edges of $\Delta_j$ as pairs like $ab$, and the corresponding vertices and edges in $\calT$ as $j(a)$ and $j'(ab)$, interpreted as numbers in $\{1,\ldots,c\}$ and $\{1,\ldots, n\}$ respectively. Moreover we set $j(ab) = j'(ab)+n$. We suppose that $ab, ac, ad$ are of type 1, 2, 3.

The conditions $qA^j = qA^{j+n} = qA^{j+2n}=0$ say that
$$
\begin{aligned}
qA^j & = q_j + q_{j(ab)} + q_{j(cd)} = 0, \\
qA^{j+n} & = q_j + q_{j(ac)} + q_{j(bd)} = 0, \\
qA^{j+2n} & = q_j + q_{j(ad)} + q_{j(bc)} = 0. 
\end{aligned}
$$
This implies that
\begin{equation} \label{qq:eqn}
q_{j(ab)} + q_{j(cd)} = q_{j(ac)} + q_{j(bd)} = q_{j(ad)} + q_{j(bc)} = - q_j.
\end{equation}
We now prove that $q= \sum \lambda_i B_i$ where the coefficients $\lambda_i$ are defined as follows. Consider an ideal triangle in $\Delta_j$ with vertices $a,b,c$ and define
$$\lambda_{j(a)} = \frac{q_{j(ab)} + q_{j(ca)} - q_{j(bc)}}2.$$
We check that $\lambda_{j(a)}$ does not depend on the ideal triangle: the triangle in $\Delta_j$ with vertices $a,b,d$ gives 
$$\lambda_{j(a)} = \frac{q_{j(ab)} + q_{j(da)} - q_{j(bd)}}2 = \frac{q_{j(ab)} + q_{j(ca)} - q_{j(bc)}}2$$
using (\ref{qq:eqn}). Two triangles incident to the ideal vertex $v_{j(a)}$ are connected by a path of adjacent tetrahedra and hence $\lambda_{j(a)}$ is well-defined.

Finally, we need to check that indeed $q = \sum \lambda_iB_i$. We consider the edge $j(ab)$ and recall that the $(n+j(ab))$-th column of $B$ is everywhere zero except at rows $j(a)$ and $j(b)$; hence the $(n+j(ab))$-th entry of $\sum \lambda_iB_i$ is $\lambda_{j(a)} + \lambda_{j(b)}$, which by definition equals $q_{j(ab)}$, so we are done.

Analogously, the $j$-th column of $B$ is everywhere zero except at the rows $j(a),j(b),j(c),j(d)$ and hence the $j$-th entry of $\sum \lambda_iB_i$ is $-(\lambda_{j(a)} + \lambda_{j(b)} + \lambda_{j(c)} + \lambda_{j(d)})$ which equals $-q_{j(ab)} - q_{j(cd)} = q_j$. The proof is complete.
\end{proof}

These three lemmas imply Proposition \ref{AB:exact:prop}. In particular we get the following:

\begin{cor} \label{rk:A:cor}
We have $\rk A = 2n-c$.
\end{cor}


\subsection{A symplectic form} \label{symplectic:form:subsection}
We define an alternating bilinear form $\omega$ on $\matR^{3n}$ as follows: for every $i=1,\ldots, n$ consider the form
$$\omega_i = \begin{pmatrix}
0 & 1 & -1 \\
-1 & 0 & 1 \\
1 & -1 & 0
\end{pmatrix}
$$
on the subspace $V_i$ generated by $e_i, e_{i+n}$, and $e_{i+2n}$, and define $\omega = \oplus_i \omega_i$. Strictly speaking, the form $\omega$ is not symplectic because it is degenerate: its radical is generated by all vectors of type $e_i+e_{i+n} + e_{i+2n}$, that is by the first $n$ rows of the matrix $A$. The form $\omega$ becomes symplectic after quotienting $\matR^3$ by the radical.

\begin{prop} \label{rows:lagrangian:prop}
The rows of $A$ generate a lagrangian subspace.
\end{prop}
\begin{proof}
In other words, we need to prove that $\omega(A_j, A_k)=0$ for any rows $A_j, A_k$ of $A$. The first $n$ rows lie in the radical, hence we are left to check that $\omega(A_{n+j}, A_{n+k})=0$ for all $0 < j < k \leqslant n$ corresponding to the $j$-th and $k$-th edge of the triangulation. 

Each tetrahedron $\Delta_i$ contributes to the number $\omega(A_{n+j}, A_{n+k})$ as follows: if two edges contained in some face $f$ of $\Delta_i$ correspond to the edges $j$ and $k$ of the triangulation, they contribute with a $\pm 1$; the face $f$ is also contained in an adjacent tetrahedron where they contribute with opposite sign, and hence everything sums to zero.
\end{proof}


\subsection{The solution space} \label{solution:space:subsection}
We now employ the combinatorial results of the previous sections to study the consistency equations for $\calT$. 
We assign the variables $z_j$, $\frac 1{1-z_j}$, and $\frac{z_j-1}{z_j}$ to the edges of type 1, 2, and 3 in each tetrahedron $\Delta_j$. These three variables lie in the upper half-plane 
$$\matC_+ = \big\{\Im z > 0\big\}$$
which we see as the subset $\matC_+ \subset \widetilde{\matC^*}$ consisting of all $\rho e^{i\theta}$ with $0<\theta < \pi$.
The consistency equation at the edge $e_i$ is the following equation in $\widetilde{\matC^*}$:
\begin{equation} \label{gi:eqn}
g_i(z) = \prod_{j=1}^n z_j^{A_{n+i,j}} \left(\frac 1{1-z_j}\right)^{A_{n+i,n+j}} 
\left(\frac{z_j-1}{z_j}\right)^{A_{n+i,2n+j}} = e^{2\pi i}.
\end{equation}
The elements $\frac{1}{1-z_j}, \frac{z_j-1}{z_j}\in\matC_{+}\subset \widetilde \matC^*$ depend holomorphically on $z_j\in\matC_{+}$.
We have defined a complex function
$$g \colon \matC_{+}^n \longrightarrow \big(\widetilde{\matC^*}\big)^n$$
by setting $g=(g_1,\ldots, g_n)$. The \emph{solution space} is the set
$$\Def(M,\calT) = g^{-1}(e^{2\pi i},\ldots, e^{2\pi i}).$$
This space consists precisely of the solutions to the consistency equations of $\calT$. 
Each solution $z\in \Def(M,\calT)$ gives a hyperbolic metric on $M$, which ``deforms'' as $z$ varies: this justifies the use of the symbol ``$\Def$''. We want to prove that $\Def(M,\calT)$ is a complex manifold of dimension $c$. 


\subsection{Complex differentials} \label{complex:diff:subsection}
We use the biholomorphism $\log\colon \widetilde{\matC^*} \to \matC$ and define the function $G(z) = \log g(z)$ for all $z\in \matC_+^n$. Now 
$$\Def(M,\calT) = G^{-1}(2\pi i, \ldots, 2\pi i).$$ 
We may write
$$G_i(z) = \sum_{j=1}^n A_{i,j}' \log z_j + A'_{i,n+j}\log(1-z_j) + N_i\pi i$$
where $A'$ is the $n \times 2n$ integral matrix defined by
$$A'_{i,j} = A_{n+i,j} - A_{n+i,2n+j}, \quad A'_{i,n+j} = -A_{n+i,n+j} + A_{n+i,2n+j}$$ 
and $N_i$ is some fixed integer that depends on the way we interpret $\log(1-z_j)$. 
The complex differential of $G$ at $z$ splits as a composition of two linear maps
$$ dG_{ z}\colon \matC^{n} \stackrel{Z}{\longrightarrow} \matC^{2n} \stackrel{A'}{\longrightarrow} \matC^n$$
where
$$Z = \begin{pmatrix}
\frac 1{z_1} & 0 & \ldots & 0 \\
0 & \frac 1{z_2} & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \ldots & \frac 1{z_n} \\
\frac {1}{z_1-1} & 0 & \ldots & 0 \\
0 & \frac {1}{z_2-1} & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \ldots & \frac {1}{z_n-1} 
\end{pmatrix}
$$
is obtained by differentiating $\log z_j$ and $\log (1-z_j)$.
Let now
$$B'\colon \matC^n \longrightarrow \matC^c$$
be the linear map defined by the right $(c\times n)$-sub-matrix $B'$ of $B$, that is $$B'_{i,j} = B_{i.n+j}.$$

\begin{prop} \label{AB2:exact:prop}
The following sequence is exact:
$$ \matC^{2n} \stackrel{A'}{\longrightarrow} \matC^{n} \stackrel{B'}{\longrightarrow} \matC^c \longrightarrow 0.$$
\end{prop}
\begin{proof}
Lemma \ref{B:surj:lemma} shows that $B$ is surjective, and its proof actually shows that $B'$ is surjective. Recall that $A$ decomposes into six square matrices, and via Gauss moves on columns we get 
\begin{equation} \label{GaussA:eqn}
A=\begin{pmatrix}
I & I & I \\
A^1 & A^2 & A^3 
\end{pmatrix}
\longrightarrow
\begin{pmatrix}
0 & 0 & I \\
A^1-A^3 & -A^2 + A^3 & A^3
\end{pmatrix}
=
\begin{pmatrix}
0 & I \\
A' & A^3
\end{pmatrix}.
\end{equation}
Now $BA=0 \Rightarrow B'A'=0$, and $\rk A = 2n-c \Rightarrow \rk A' = n-c$.
\end{proof}

This shows in particular that the image of $G$ lies in a fixed affine subspace parallel to $\ker B'$ of complex codimension $c$. We now consider the standard symplectic form $\omega = \matr 0{I}{-I}0$ on $\matR^{2n}$. 
\begin{prop} \label{rows:lagrangian2:prop}
The rows of $A'$ generate a lagrangian subspace.
\end{prop}
\begin{proof}
We know that the rows of $A$ generate a lagrangian subspace with respect to the degenerate form on $\matR^{3n}$ by Proposition \ref{rows:lagrangian:prop}. The Gauss moves (\ref{GaussA:eqn}) imply the assertion.
\end{proof}

\begin{prop} \label{Choi:prop}
For every $z\in \matC_+^n$ the following sequence is exact:
$$ \matC^n \stackrel{dG_{z}} \longrightarrow \matC^n \stackrel {B'} \longrightarrow \matC^c \longrightarrow 0.$$
\end{prop}
\begin{proof}
We have $dG_{z} = A'Z$. Proposition \ref{AB2:exact:prop} gives an exact sequence
$$ \matC^{2n} \stackrel{A'}{\longrightarrow} \matC^{n} \stackrel{B'}{\longrightarrow} \matC^c \longrightarrow 0.$$
We only need to prove that $\Img (A'Z) = \Img A'$, that is $\rk (A'Z) = n-c$. We prefer to consider the transpose matrix $M= (A'Z)^\intercal =  Z^\intercal (A')^\intercal$. We have
$$ Z^\intercal = \begin{pmatrix}
\frac 1{z_1} & 0 & \ldots & 0 & \frac {1}{z_1-1} & 0 & \ldots & 0 \\
0 & \frac 1{z_2} & \ldots & 0 & 0 & \frac {1}{z_2-1} & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \ldots & \frac 1{z_n} & 0 & 0 & \ldots & \frac {1}{z_n-1} 
\end{pmatrix}.
$$
The map $Z^\intercal\colon \matC^{2n} \to \matC^n$ is obviously not injective, but its restriction 
$$Z^\intercal |_{\matR^{2n}}\colon \matR^{2n} \longrightarrow \matC^n$$ 
is an isomorphism of real spaces because $\frac 1{z_i}$ and $\frac {1}{z_i-1}$ are independent over $\matR$ (we use here that $z_i\not\in \matR$).  

We define a symplectic form $\Omega$ on the real vector space $\matC^n$ by pushing-forward $\omega$ along $Z^\intercal |_{\matR^{2n}}$, that is we set $\Omega(Z^\intercal v,\, Z^\intercal w) = \omega(v,w)$. By construction $\Omega$ is a sum of symplectic forms on the coordinate complex lines of $\matC^n$. Note that a symplectic form on $\matC$ is unique up to rescaling.

Since $\Img z_i >0$, the complex numbers $\frac{1}{z_i}$ and $\frac{1}{z_i-1}$ form a negatively-oriented $\matR$-basis of $\matC$, and this implies that $\Omega (v,iv) < 0$ for every non-zero vector $v\in \matC^n$. In particular $\langle \cdot, \cdot \rangle = -\Omega(\cdot, i \cdot)$ is a positive-definite scalar product that induces a norm $\| \cdot \|$ on $\matC^n$. 

On each coordinate complex line of $\matC^n$, the form $\Omega$ is just a rescaling of the standard symplectic form and hence $\langle,\rangle$ is a rescaling of the standard scalar product. In particular we get $\Omega(iv,iw) = \Omega(v,w)$ and $\langle iv, iw \rangle  = \langle v,w \rangle$.

Finally, we suppose by contradiction that $\rk M < n-c$. Since $Z^\intercal |_{\matR^{2n}}$ is injective, the real subspace $M(\matR^{n})$ has real dimension $n-c$.
Since $\rk M < n-c$, there are vectors $v_1,v_2\in \matR^{n}$ such that $M(v_1+iv_2) = 0$ while $Mv_1 \neq 0$ and $Mv_2 \neq 0$. Proposition \ref{rows:lagrangian2:prop} gives  
$$\Omega(Mv_1, Mv_2)= \omega ((A')^\intercal v_1,(A')^\intercal v_2) = 0$$
and therefore
\begin{align*}
0 = \|M(v_1 + iv_2)\|^2 & = \|Mv_1\|^2 + \|iM v_2\|^2 + 2\langle M v_1, iM v_2 \rangle \\
& = \|Mv_1\|^2 + \|Mv_2\|^2 -2\Omega(M v_1, -Mv_2) \\
& = \|Mv_1\|^2 + \|Mv_2\|^2
\end{align*}
implies $Mv_1 = Mv_2=0$, a contradiction.
\end{proof}

\begin{cor} \label{smooth:cor}
The solution space $\Def(M,\calT) \subset \matC_+^n$ is either empty or a complex submanifold of dimension $c$.
\end{cor}
\begin{proof}
The image of $G\colon \matC_+^n \to \matC^n$ lies entirely in a $(n-c)$-dimensional complex affine space $S$ parallel to $\ker B' \subset \matC^n$ and by the previous proposition the holomorphic map $G\colon \matC_+^n \to S$ is a submersion onto its image. Therefore the counterimage of any point is a either empty or is a complex submanifold of dimension $n-(n-c)=c$.
\end{proof}

We now want to define a nice holomorphic parametrisation for the manifold $\Def(M,\calT)$, and to this purpose we need to investigate further the combinatorial properties of $\calT$ by looking more closely at its ideal vertices.


\subsection{Boundary curves} \label{boundary:curves:subsection}
Recall that $M=\interior N$ and the ideal vertices $v_1,\ldots, v_c$ of $\calT$ correspond to the boundary tori $T_1,\ldots, T_c$ of $N$, which are triangulated by $\calT$. Recall also that there are $n$ tetrahedra $\Delta_1,\ldots, \Delta_n$ in $\calT$ and each $\Delta_i$ has three edge pairs labeled with $i, n+i,$ and $2n+i$.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{path_holonomy-BW}{path_holonomy}} 
\nota{We mark with a dot all the interior angles that $\gamma$ encounters on its right as in the picture: each dot determines an edge in some tetrahedron $\Delta_j$ and hence an edge pair (left). We also consider the ``degenerate path'' consisting of a single point ``run counterclockwise'', and recover the last $n$ rows of $A$ in this way (right).}
\label{path_holonomy:fig}
\end{center}
\end{figure}

Every simplicial closed oriented curve $\gamma$ in a triangulated torus $T_i$ determines an integer vector $v_\gamma \in \matR^{3n}$ that counts the (right-)incidences between $\gamma$ and the $3n$ edge pairs of $\calT$. More precisely, each interior angle of a triangle in $T_i$ determines an edge in some tetrahedron $\Delta_j$ and hence an edge pair: we define $(v_\gamma)_j$ to be the number of times $\gamma$ encounters the $j$-th edge pair on its right, as in Figure \ref{path_holonomy:fig}-(left).

We defined an alternating degenerate form $\omega$ on $\matR^{3n}$ and we now want to extend Proposition \ref{rows:lagrangian:prop}. We denote by $\gamma \cdot \gamma'$ the algebraic intersection of $\gamma$ and $\gamma'$ in $H_1(\partial M, \matZ)$.

\begin{prop} \label{A:gamma:gamma':prop}
Let $\gamma, \gamma'$ be simplicial closed curves in $\partial N$. We have:
\begin{itemize}
\item $\omega(v_\gamma, v_{\gamma'}) = 2 \gamma \cdot \gamma'$,
\item $\omega(v_\gamma, A_i) = 0 $ for every row $A_i$ of $A$.
\end{itemize}
\end{prop}
\begin{proof}
The row $A_i$ with $i\leqslant n$ lies in the radical of $\omega$, and $A_{n+i}$ records the incidences of the $i$-th edge $e_i$ of $\calT$ with the $3n$ edge pairs. We may write $A_{n+i} = v_{\gamma'}$ where $\gamma'$ is a ``degenerate'' closed path consisting of a single point (one of the endpoints of $e_i$), see Fig~\ref{path_holonomy:fig}-(right). Now the second assertion is just a special case of the first.

\begin{figure}
\begin{center}
\includegraphics[width = 7 cm] {\iftoggle{BW}{two_paths_holonomy-BW}{two_paths_holonomy}} 
\nota{We draw the paths $\gamma$, $\gamma'$ and their dots in \iftoggle{BW}{dark grey}{blue} and \iftoggle{BW}{grey}{red}.}
\label{two_paths_holonomy:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{curves_dots_contribution-BW}{curves_dots_contribution}} 
\nota{Two dots in a triangle contribute to $\omega(\gamma, \gamma')$ with $+1$, $0$, or $-1$ according to their mutual position.}
\label{curves_dots_contribution:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{curves_near_contribution-BW}{curves_near_contribution}} 
\nota{Two portions of \iftoggle{BW}{dark grey}{blue} and \iftoggle{BW}{grey}{red} paths that intersect the same triangle contribute to $\omega(\gamma, \gamma')$ as shown here. The contribution depends on their mutual configuration, and changes by a sign if we interchange the \iftoggle{BW}{dark grey}{blue}/\iftoggle{BW}{grey}{red} colours. If one of the two portions contains at least two edges (as in bottom-right) it determines a vector in the radical, and the contribution is always zero.}
\label{curves_near_contribution:fig}
\end{center}
\end{figure}

We draw the two paths $\gamma$ and $\gamma'$ in \iftoggle{BW}{dark grey}{blue} and \iftoggle{BW}{grey}{red} as in Figure \ref{two_paths_holonomy:fig}, marking with dots the angles they encounter on their right. A couple of \iftoggle{BW}{dark grey}{blue} and \iftoggle{BW}{grey}{red} dots in the same triangle contribute to $\omega(\gamma, \gamma')$ according to their mutual position as shown in Figure \ref{curves_dots_contribution:fig}. Therefore portions of \iftoggle{BW}{dark grey}{blue} and \iftoggle{BW}{grey}{red} paths intersecting the same triangle contribute to $\omega(\gamma, \gamma')$ as shown in Figure \ref{curves_near_contribution:fig}.

For every contribution $+1$ as in Figure \ref{curves_near_contribution:fig}-(top-left), there is an analogous but opposite contribution $-1$ provided by the other triangle adjacent to the edge joining the coloured endpoints: these all cancel. We are left with a $+1$ every time the \iftoggle{BW}{grey}{red} path exits leftward from an intersection with the \iftoggle{BW}{dark grey}{blue} path, a $-1$ every time it enters from the left, and the opposite contributions with the \iftoggle{BW}{dark grey}{blue}/\iftoggle{BW}{grey}{red} colours interchanged. We easily get a total of $2\gamma \cdot \gamma'$.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{curves_far_contribution-BW}{curves_far_contribution}} 
\nota{When $\gamma$ and $\gamma'$ encounter in different truncated triangles of the same tetrahedron $\Delta_i$, they also contribute to $\omega(\gamma,\gamma')$.}
\label{curves_far_contribution:fig}
\end{center}
\end{figure}

The proof is not yet complete, because every tetrahedron $\Delta_i$ determines four triangles in $\partial N$ and some contributions to $\omega(\gamma, \gamma')$ arise also from paths intersecting distinct triangles of the same $\Delta_i$: we need to prove that these contributions all cancel.

Up to symmetries of the tetrahedron and up to interchanging the colours, the possible non-zero contributions are all shown in Figure \ref{curves_far_contribution:fig}. Each configuration as in the first row cancels with an opposite one produced by the tetrahedron adjacent to the grey face. The contributions in the second row arise when $\gamma$ and $\gamma'$ cross the endpoints of an edge $e$ on opposite sides, and one checks that the contributions of all the cycle of tetrahedra incident to $e$ sum to zero (exercise).
\end{proof}


\subsection{Holonomy parameters} \label{holonomy:subsection}
We now fix a non-trivial oriented simple closed curve $\gamma_i$ on each $T_i$ and a representation of $\gamma_i$ as a simplicial (possibly non-injective) path in the triangulated $T_i$.

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{ABmatrices_extended-BW}{ABmatrices_extended}} 
\nota{The enlarged matrix $\bar A$.}
\label{ABmatrices_extended:fig}
\end{center}
\end{figure}

We enlarge the incident $2n \times 3n$ matrix $A$ to a $(2n+c)\times 3n$ matrix $\bar A$ by adding the vectors $v_{\gamma_1}, \ldots, v_{\gamma_c}$ at its bottom, see Figure \ref{ABmatrices_extended:fig}.

\begin{prop} \label{A:bar:lagrangian:prop}
We have $\rk \bar A = 2n$. The rows of $\bar A$ generate a maximal lagrangian subspace in $\matR^{3n}$.
\end{prop}
\begin{proof}
Let $\mu_i \subset T_i$ be a simplicial closed curve with $\gamma_i\cdot \mu_i = 1$. We already know that the first $2n$ rows of $\bar A$ generate a lagrangian subspace of dimension $2n-c$, and to conclude it suffices to use Proposition \ref{A:gamma:gamma':prop} and deduce that $v_{\mu_i}$ is $\omega$-orthogonal to all the rows of $\bar A$ except $\bar A_{2n+i}=v_{\gamma_i}$. Therefore $\rk \bar A = \rk A +c = 2n$.
\end{proof}

Every point $z\in \Def(M,\calT)$ determines a hyperbolic structure on $M$ and a homomorphism
$$\tilde\mu_z \colon \pi_1(T_i) \to \widetilde{\matC^*}$$
for each $i=1,\ldots, c$, see Definition \ref{tilde:mu:defn}. We define
$$h_i(z) = \tilde\mu_z(\gamma_i) = e^{-|\gamma_i| \pi i } \prod_{j=1}^n z_j^{\bar A_{2n+i,j}} \left(\frac 1{1-z_j}\right)^{\bar A_{2n+i,n+j}} 
\left(\frac{z_j-1}{z_j}\right)^{\bar A_{2n+i,2n+j}} $$
and get a holomorphic function
$$h\colon \matC_+^n \longrightarrow \big(\widetilde{\matC^*}\big)^c.$$
We want to prove that $h$ furnishes a nice parametrisation for the $c$-dimensional space $\Def(M,\calT)$. The letter $h$ stands for ``holonomy'': recall that $h_i$ is the holonomy of $\gamma_i$, see Exercise \ref{tilde:rho:mu:ex}.

As in Section \ref{complex:diff:subsection}, we define $H(z) = \log h(z)$. 
We get a map
$$G \times H \colon \matC_+^n \longrightarrow \matC^n \times \matC^c.$$
As above, the differential splits as a composition of linear maps
$$ d(G\times H)_{z}\colon \matC^{n} \stackrel{Z}{\longrightarrow} \matC^{2n} \stackrel{\bar A'}{\longrightarrow} \matC^n \times \matC^c$$
where $\bar A'$ is constructed from $\bar A$ exactly as $A'$ from $A$.

\begin{prop} \label{Choi2:prop}
The differential $d(G\times H)_{z}$ is injective $\forall z \in \matC_+^n$.
\end{prop}
\begin{proof}
As above, Proposition \ref{A:bar:lagrangian:prop} implies that the rows of $\bar A'$ form a lagrangian subspace of dimension $n$ and we conclude with the same proof as Proposition \ref{Choi:prop}.
\end{proof}

\begin{cor}
The restriction
$$h|_{\Def(M,\calT)}\colon \Def(M,\calT) \longrightarrow \big(\widetilde{\matC^*}\big)^c$$ is a local biholomorphism.
\end{cor}

A \emph{complete solution} $z\in\Def(M,\calT)$ is one that determines a complete metric on $M$, that is such that $h(z)=(1,\ldots,1)$.

\begin{cor} \label{complete:isolated:cor}
Every complete solution in $\Def(M,\calT)$ is isolated.
\end{cor}

The local biholomorphism $h$ depends on the isotopy class of the curves $\gamma_i$ chosen: different choices give different parametrisations. Note however that the condition that $h_i(z)=1$ corresponds geometrically to the completeness of $T_i$ and hence does not depend on $\gamma_i$.
