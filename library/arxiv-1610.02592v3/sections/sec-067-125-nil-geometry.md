---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-067-125-nil-geometry
section_title: "Nil geometry"
section_number: 12.5
pages: 394-404
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.979
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
There are still three non-isotropic geometries to analyse. These geometries are not products, but they have a reasonable bundle structure, so that many of the arguments of the previous section can be extended with not much effort.

We start with the geometry $\Nil$, which is a $\matR$-bundle over $\matR^2$. This geometry is fully carried by a Lie group called the \emph{Heisenberg group}.\index{group!Heisenberg group}\index{$\Nil$\ geometry}


\subsection{The Heisenberg group} 
The \emph{Heisenberg group} consists of all matrices
$$\begin{pmatrix} 1 & x & z \\ 0 & 1 & y \\ 0 & 0 & 1 \end{pmatrix}$$
with $x, y, z \in \matR$, with the multiplication operation. This is a nilpotent (but non-abelian) Lie group (see Exercise \ref{Heisenberg:ex}) and is hence also called Nil. It is clearly diffeomorphic to $\matR^3$.
There is a Lie groups exact sequence
$$ 0 \longrightarrow \matR \longrightarrow \Nil \longrightarrow \matR^2 \longrightarrow 0$$
where $\matR = [\Nil, \Nil] $ is the centre of $\Nil$ and consists of all matrices with $x=y=0$. Therefore Nil is naturally a line bundle over $\matR^2$.
We identify Nil with $\matR^3$ using the coordinates $(x,y,z)$. The product operation becomes
$$(x,y,z) \cdot (x',y',z') = (x+x', y+y', z+z'+xy').$$
\begin{ex} \label{Nil:commutator:ex}
The commutator of two elements is
$$\big[(x,y,z), (x',y',z')\big] = (0,0,xy'-x'y).$$
\end{ex}


\subsection{The geometry of Nil}
Every left-invariant Riemannian structure on a Lie group $G$ is constructed by fixing a scalar product at the tangent space $T_e G$ of $e\in G$ and then extending it by left-multiplication. Here $e=(0,0,0)$ and we give $T_e\Nil = \matR^3$ the Euclidean scalar product. This defines a left-invariant Riemannian structure on $\Nil$.

\begin{ex} \label{metric:tensor:Nil:ex}
The metric tensor at $(x,y,z)$ is
$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & x^2 + 1 & -x \\
0 & -x & 1
\end{pmatrix}.
$$
\end{ex}
The following triple is an orthonormal basis at $(x,y,z)$:
\begin{equation} \label{orthonormal:eqn}
(1,0,0), \quad (0,1,x), \quad (0,0,1).
\end{equation}

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {Standard_contact_structure.pdf}
\nota{The planes orthogonal to the $z$ axis in $\Nil$ form the standard contact structure on $\matR^3$.}
\label{contact:fig}
\end{center}
\end{figure}

The planes spanned by the first two vectors form the standard \emph{contact structure} in $\matR^3$ shown in Figure \ref{contact:fig}. It is a non-integrable distribution of planes: no surface is tangent to it at every point.\index{contact structure}

We remark that the metric tensor has unit determinant at every point: therefore the volume form on $\Nil$ is the standard one on $\matR^3$.

We can calculate the Christoffel symbols $\Gamma_{ij}^k$ by hand or using a computer code; these are all zero except the following:
$$\Gamma^1_{22} = -x, \quad \Gamma^1_{23} = \Gamma^1_{32} = \frac 12,$$  
$$\Gamma^2_{12} = \Gamma^2_{21} = \frac x 2, \quad \Gamma^2_{13} = \Gamma^2_{31} = -\frac 12, $$
$$\Gamma^3_{12} = \Gamma^3_{21} = \frac{x^2-1}2, \quad \Gamma^3_{13} = \Gamma^3_{31} = -\frac x2.$$
The Ricci tensor at $(x,y,z)$ is 
$$R_{ij} = \frac 12 \cdot \begin{pmatrix}
-1 & 0 & 0 \\
0 & {x^2-1} & -x \\
0 & -x & 1
\end{pmatrix}.
$$
When $x=0$ the Ricci tensor is a diagonal matrix with entries $-\frac 12, -\frac 12, \frac 12$. For a unit vector $v\in T_p\Nil$, recall that $R_{ij}v^iv^j$ equals twice the average value of the sectional curvatures of the planes containing $v$: this average value ranges here from $-\frac 14$ to $\frac 14$ and is maximal when $v=(0,0,\pm 1)$. This holds when $x=0$ and hence at all points $p\in \Nil$ by left-multiplication.


\subsection{The isometry group of Nil}
The group Nil acts on itself isometrically by left-multiplication. Left-multiplication by $(a,b,c)$ preserves the bundle $\Nil \to \matR^2$ and induces on $\matR^2$ a translation by the vector $(a,b)$. 

There are also more complicate isometries of $\Nil$ that preserve the bundle structure but induce rotations on $\matR^2$: one such isometry $\varphi$ sends $(x,y,z)$ to 
$$\Big(x\cos\theta -y\sin \theta, \  x\sin \theta + y \cos \theta,\ z+ \frac 12 (x^2-y^2)\sin \theta \cos \theta - xy\sin^2 \theta \Big).$$
This map preserves the bundle and induces a rotation on $\matR^2$.
\begin{prop} \label{varphi:isometry:prop}
The map $\varphi$ is an isometry of $\Nil$.
\end{prop}
\begin{proof}
Set $(x',y',z') = \varphi (x,y,z)$. The differential $d\varphi$ at $(x,y,z)$ is
$$
\begin{pmatrix} 
\cos \theta & -\sin \theta & 0 \\
\sin \theta & \cos \theta & 0 \\
x\sin\theta \cos\theta - y\sin^2 \theta & - y\sin\theta\cos \theta  - x\sin^2\theta & 1 
\end{pmatrix} 
$$
and may be rewritten as
$$
\begin{pmatrix} 
\cos \theta & -\sin \theta & 0 \\
\sin \theta & \cos \theta & 0 \\
x'\sin \theta & x'\cos \theta - x & 1.
\end{pmatrix} 
$$
The differential $d\varphi$ sends the orthonormal basis (\ref{orthonormal:eqn}) to
$$(\cos\theta, \sin \theta, x'\sin\theta), \quad (-\sin\theta, \cos\theta, x'\cos\theta), \quad (0,0,1).$$
These vectors at $(x',y',z')$ are also orthonormal.
\end{proof}

We deduce the following.

\begin{prop} \label{Nil:isometries:prop}
Every isometry of $\Nil$ preserves the line bundle and induces an isometry of $\matR^2$. We have
$$0 \longrightarrow \matR \longrightarrow \Iso^+(\Nil) \stackrel p \longrightarrow \Iso(\matR^2) \longrightarrow 0$$
where $\matR$ is the centre of $\Nil$.
The group $\Iso^+(\Nil)$ has two components.
\end{prop}
\begin{proof}
The rotational isometries $\varphi$ with angle $\theta$ introduced above form a $S^1$-subgroup of $\Iso^+(\Nil)$. The subgroups $S^1$ and $\Nil$ belong to the component $\Iso^+_\circ(\Nil) < \Iso^+(\Nil)$ containing the identity, which hence has dimension at least $1+3=4$ and acts transitively on $\Nil$. Stabilisers have dimension at least $4-3=1$ and cannot have bigger dimension by Proposition \ref{subgroups:SO3:prop}, otherwise $\Nil$ would have constant sectional curvature: therefore $\dim(\Iso^+_\circ(\Nil))=4$ and $\Iso^+_\circ(\Nil)$ is generated by $S^1$ and $\Nil$, and it preserves the line bundle since $S^1$ and $\Nil$ do.

The subgroup $\Iso^+_\circ(\Nil)$ preserves the orientation of the fibres and of $\matR^2$.
We leave as an exercise the existence of another component of $\Iso^+(\Nil)$ which inverts the orientation of the fibres and of $\matR^2$.
\end{proof}

\begin{example}  \label{Nil:example}
A manifold $M = \Nil/_\Gamma$ modelled on Nil is described in Figure \ref{Nil_example:fig}. The figure shows a fundamental domain for the group $\Gamma<\Iso^+(\Nil)$ generated by the isometries
$$(x,y,z) \longmapsto (x+1,y,z+y),$$
$$(x,y,z) \longmapsto (x, y+1, z), \quad (x,y,z) \longmapsto (x,y,z+1).$$
obtained by left-multiplication with the canonical basis of $\matR^3$.
Both the unit cube and $M$ have volume one. The manifold $M$ is clearly a torus bundle with monodromy $\matr 1101$ and is hence diffeomorphic to the Seifert manifold $\big(T,(1,1)\big)$ by Exercise \ref{Me:ex}.
\end{example}

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {Nil_example.pdf}
\nota{The $\Nil$\ manifold $M=\Nil/_\Gamma$ is obtained by identifying the faces of this unit cube as follows: the triangular faces are glued via the affine maps as shown by the labels, and the pairs of unlabelled opposite square faces are identified by translations. The cube is a fundamental domain for $\Gamma$.}
\label{Nil_example:fig}
\end{center}
\end{figure}

A group $\Gamma< \Iso(X)$ is \emph{cocompact} if $X/_\Gamma$ is compact.
We prove that cocompact groups in $\Iso(\matR^2)$ do not lift.

\begin{prop} \label{Nil:no:lift:prop}
Let $\Gamma < \Iso(\matR^2)$ be discrete and cocompact. There is no homomorphism $f\colon \Gamma \to \Iso^+(\Nil)$ such that $p\circ f = \id$.
\end{prop}
\begin{proof}
Up to taking a finite-index subgroup we may suppose that $\Gamma$ is generated by two translations along independent vectors $(x,y)$ and $(x',y')$. We prove that two lifts $\varphi, \varphi' \in \Iso^+(\Nil)$ of these translations never commute, thus forbidding the existence of a homomorphism $f$.

If $\varphi$, $\varphi' \in \Nil$, Exercise \ref{Nil:commutator:ex} gives $[\varphi, \varphi'] = xy'-x'y \neq 0$. All the other lifts are of type $g\varphi, g'\varphi'$ for some $g,g'\in \matR$, hence we get the same commutator. 
\end{proof}

Let $\Iso_0^+(\Nil)$ be the connected component of $\Iso^+(\Nil)$ containing $e$.

\begin{ex} \label{isonil:nilpotente:ex}
We have 
$$\big[\Iso_0^+(\Nil), \Iso_0^+(\Nil)\big] = \matR.$$ 
Therefore $\Iso_0^+(\Nil)$ is nilpotent.
\end{ex}

\begin{cor} \label{Nil:is:Nil:cor}
If a three-manifold $M$ has a $\Nil$ geometry, then $\pi_1(M)$ is virtually nilpotent.
\end{cor}
\begin{proof}
It has a nilpotent subgroup of index at most two, because
the subgroup $\Iso_0^+(\Nil)< \Iso^+(\Nil)$ is nilpotent and has index two.
\end{proof}


\subsection{Nil geometry}
We now classify the manifolds modelled on $\Nil$. 

\begin{prop} \label{Nil:cofinite:prop}
A discrete group $\Gamma < \Iso^+ (\Nil)$ is cofinite if and only if both $p(\Gamma)$ and $\Gamma \cap \ker p$ are discrete and cofinite.
\end{prop}
\begin{proof}
We follow the proof of Proposition \ref{H2R:prop}. Up to taking finite-index subgroups we may suppose that $\Gamma<\Iso^+_0(\Nil)$.
If $p(\Gamma)$ is discrete the proof of Proposition \ref{H2R:prop} applies also here; note that the formula (\ref{volume:product:eqn}) holds because the volume form in $\Nil$ is the standard one on $\matR^3$.

If $p(\Gamma)$ is not discrete then that proof shows that there is a neighbourhood $U\subset \Iso^+(\Nil)$ of $e$ such that every two elements $f,g\in\Gamma$ projecting in $p(U)$ commute. (It is still true that $[f,g]$ depends only on $p(f)$ and $p(g)$ since $\ker p = \matR$ is central.) We deduce again that the isometries in $p(\Gamma)$ commute: hence they are either rotations fixing the same point or translations. 

In the former case $\Gamma$ is not cofinite. In the latter, we get $\Gamma < \Nil$ acting as left-multiplication. Every two $f,g \in \Gamma$ projecting to $p(U)$ commute and hence project to parallel translations by Exercise \ref{Nil:commutator:ex}. As in the proof of Proposition \ref{H2R:prop} we deduce that $p(\Gamma)$ preserves a line, and hence it is not cofinite.
\end{proof}


\begin{cor} If the interior of a compact orientable manifold $M$ admits a finite-volume complete $\Nil$ geometry then $M$ is a closed Seifert manifold with $\chi=0$ and $e \neq 0$.
\end{cor}
\begin{proof}
We have $\interior M = \Nil/_\Gamma$ with $\Gamma$ cofinite and Proposition \ref{Nil:cofinite:prop} provides a Seifert fibration $M\to S$ over a finite-area orbifold $S=\matR^2/_{p(\Gamma)}$. Finite-area flat orbifolds have $\chi(S)=0$ and are closed (there are no cusps in flat geometry), hence $M$ is closed. 

We have $e\neq 0$, otherwise up to finite-index we would get $M = T\times S^1$ contradicting Proposition \ref{Nil:no:lift:prop}.
\end{proof}

We prove the converse.

\begin{prop} \label{Nil:construct:prop}
If $M$ is a closed Seifert manifold with $\chi=0$ and $e\neq 0$, then $M$ admits a $\Nil$ geometry.
\end{prop}
\begin{proof}
We have
$$ M = \big(S, (p_1,q_1), \ldots, (p_k, q_k) \big).$$
Suppose $S$ is a closed orientable surface of genus $g\geqslant 0$. In the following $\pi_1(S)$ is the orbifold fundamental group. We have:
\begin{align*}
\pi_1(S) & = \langle a_1, b_1, \ldots, a_g, b_g, c_1, \ldots, c_k \ |\ [a_1,b_1]\cdots [a_g,b_g] c_1 \cdots c_k, c_i^{p_i} \rangle, \\
\pi_1(M) & = \langle a_1, b_1, \ldots, a_g, b_g, c_1, \ldots, c_k, l \ |\ [a_1,b_1]\cdots [a_g,b_g] c_1 \cdots c_k, c_i^{p_i}l^{q_i}, \\ 
& \qquad [a_i,l], [b_i,l] \rangle. 
\end{align*}
We fix any flat structure on the orbifold $S$ and get an injection $\pi_1(S) \to\Iso^+(\matR^2)$. We now want to lift this map to an injection $\pi_1(M) \to \Iso^+(\Nil)$, so that the resulting diagram commutes:
$$
\xymatrix{ 
\pi_1(M) \ar@{.>}[r] \ar[d] & \Iso^+(\Nil) \ar[d] \\
\pi_1(S)\ar[r] & \Iso^+(\matR^2)
}
$$
Recall that $\Iso_0^+(\Nil)$ contains the group $\matR$ of vertical translations: we use the multiplicative notation and indicate it as $\matR_{>0}$. We note that $\matR_{>0}$ is central in $\Iso_0^+(\Nil)$ because it commutes with $\Nil$ and the isometries $\varphi$ from Proposition \ref{varphi:isometry:prop}, which altogether generate $\Iso_0^+(\Nil)$.

We identify $\pi_1(S)$ with its image in $\Iso^+(\matR^2)$.
We lift arbitrarily $a_i,b_i,c_i$ inside $\Iso^+(\Nil)$ and pick $l\in \matR_{>0}$. We get
\begin{align*}
[a_1,b_1]\cdots [a_g,b_g] c_1 \cdots c_k & = e^\mu, \\
c_i^{p_i}l^{q_i} & = e^{\lambda_i}
\end{align*}
for some $\mu, \lambda_i \in \matR$. To get a homomorphism $\pi_1(M) \to \Iso^+(\Nil)$ we need $\mu = \lambda_i = 0$. To obtain that we change the lifts as $c_i' = e^{t_i} c_i$, $l' = e^u l$ to get
\begin{align*}
[a_1,b_1]\cdots [a_g,b_g] c'_1 \cdots c'_k & = e^{t_1 + \ldots + t_k + \mu}, \\
(c'_i)^{p_i}(l')^{q_i} & = e^{t_ip_i+ uq_i + \lambda_i}.
\end{align*}
We want
\begin{align*}
t_1+\ldots + t_k &= - \mu, \\
t_ip_i + uq_i &= - \lambda_i.
\end{align*}
The determinant of the $k\times k$ coefficient matrix was already calculated in the proof of Proposition \ref{Seifert:homology:prop}, and is
$$\pm\sum \frac{q_i}{p_i} (p_1\cdots p_k)= \pm e \cdot p_1\cdots p_k \neq 0.$$
Therefore the linear system has a unique solution $(t_1,\ldots, t_k, u)$. The lift $l'$ is necessarily non-trivial, otherwise we would get a lift $\pi_1(S) \to \Iso^+(\Nil)$ that is excluded by Proposition \ref{Nil:no:lift:prop}. Therefore the lift is injective.

If $S$ is non-orientable the proof is similar and left as an exercise.
\end{proof}


\section{$\widetilde{\SL_2}$ geometry}
The $\widetilde{\SL_2}$ geometry is similar to $\Nil$, but it is now a $\matR$-bundle over $\matH^2$. The geometry is again fully carried by the Lie group $\widetilde{\SL_2}$, which is the universal cover of both $\SL_2(\matR)$ and $\PSLR$. It is convenient to identify $\PSLR$ with the unit tangent bundle of $\matH^2$.\index{$\widetilde{\SL_2}$ geometry}


\subsection{The unit tangent bundle}
The tangent bundle $TM$ of a Riemannian $n$-manifold $M$ has a natural Riemannian structure, which we briefly introduce.

The tangent space at any point $x\in TM$ splits into a \emph{vertical} subspace $V_x  = \ker dp_x$ where $p\colon TM \to M$ is the projection, and a \emph{horizontal} subspace $H_x $ determined by the metric tensor on $M$ as follows: use the parallel transport to move the tangent vector $x$ along all geodesics exiting from $p(x)$; the result is a small $n$-surface in $TM$ containing $x$ and we set $H_x$ to be its tangent space at $x$. 

To define a metric on $TM$ we impose that $V_x$ and $H_x$ be orthogonal and we give to each space the metric of $T_xM$, via the natural identification $V_x = T_xM$ and via the isomorphism $dp_x\colon H_x \to T_xM$. 

The \emph{unit tangent bundle} $UM\subset TM$ consists of all unitary tangent vectors and inherits a Riemannian structure. Every isometry $f\colon M \to M$ induces an isometry $df\colon UM \to UM$.



\subsection{The space $U\matH^2$}
We now focus on the case $M=\matH^2$ we are interested in. Parallel transport was defined explicitly in Section \ref{parallel:subsection}. 
We represent $\matH^2$ using the upper half-plane model $H^2 = \{\Im z > 0\}$, so that $TH^2 = H^2 \times \matC$ and $UH^2 = H^2 \times S^1$ has coordinates $(z,\theta)$. The tangent space $T_{(z,\theta)}UH^2$ is naturally identified with $\matC\times \matR = \matR^3$.

\begin{lemma} \label{UH2:tensor:lemma}
The metric tensor of $UH^2$ at $(z,\theta)$ is
$$
\begin{pmatrix}
2y^{-2} & 0 & y^{-1} \\
0 & y^{-2} & 0 \\
y^{-1} & 0 & 1 
\end{pmatrix}
$$
where $z=x+iy$.
\end{lemma}
\begin{proof}
We first consider the disc model $D^2$ of $\matH^2$ with $TD^2 = D^2 \times \matC$ and $T_{(z,v)} TD^2 = \matC \times \matC$.  
We focus at a point $(0,v)$ and determine the decomposition 
$$T_{(0,v)} = H_{(0,v)} \oplus V_{(0,v)}.$$ 
We have $V_{(0,v)} = 0 \times \matC$ and we now determine $H_{(0,v)}$. Every geodesic through $0$ is a Euclidean line $l$ and the parallel transport of $v\in T_0D^2$ along $l$ forms a constant angle with $l$: the parallel transport of $v$ at $z\in l$ is just the rescaled vector $(1-|z|^2)v$. Parallel transports of $v$ along lines passing through $0$ form a surface, which is the graph of the function $f(z) = (1-|z|^2)v$, whose tangent plane at $0$ is $H_{(0,v)} = \matC \times 0$ since $\frac{\partial f}{\partial x} = \frac{\partial f}{\partial y} = 0$ at $0$.

We have discovered that the horizontal and vertical planes at $(0,v)$ are just the coordinate ones of $T_{(0,v)} = \matC \times \matC$. By definition these are orthogonal and inherit a metric tensor from that of $T_0D^2$, which is $4$ times the Euclidean one. Therefore the metric tensor at $T_{(0,v)} = \matC^2$ is $4$ times the Euclidean one. 

We now turn to the unitary sub-bundle $UD^2 = D^2 \times S^1$. We use the natural identifications $T_{(0,\theta)} UD^2 = \matC \times \matR = \matR^3$ and we deduce that the vectors $(1,0,0)$, $(0,1,0)$, $(0,0,1) \in T_{(0,\theta)}$ are orthogonal and have norm $2,2,1$ respectively. 

The M\"obius transformation
$$f(z) = \frac{z - i}{i z - 1}$$
is an isometry between the two models $D^2$ and $H^2$ that sends $0$ to $i$. 
It is holomorphic and its complex derivative is
$$f'(z) = \frac{-2}{(iz-1)^2}.$$
The isometry $f\colon D^2\to H^2$ induces an isometry $f_*\colon UD^2 \to UH^2$, that is $f_*\colon D^2\times S^1 \to H^2 \times S^1$, which is as follows:
\begin{align*}
f_*(z,\theta) & = \left(\frac{z-i}{iz-1}, \theta + {\rm arg} (f'(z))\right) \\
& = \left(\frac{z-i}{iz-1}, \theta +\pi - 2 {\rm arg} (iz-1)\right)  \\
& = \left(\frac{z-i}{iz-1}, \theta +\pi - 2 \Im \log (iz-1)\right).  
\end{align*}
In particular $f_*(0,\theta) = (i, \theta + \pi)$.
Recall that the Jacobians of a holomorphic $g$ and of $\log g$ are
$$
Jg = \begin{pmatrix} \Re g' & -\Im g' \\ \Im g' & \Re g' \end{pmatrix},
\quad
J(\log g) = \begin{pmatrix} \Re \frac{g'}g & -\Im \frac{g'}g \\ \Im \frac{g'}g & \Re \frac{g'}g \end{pmatrix}.
$$
The differential of $f_*$ at the point $(z,\theta)$ is hence
$$
(df_*)_{(z,\theta)} =
\begin{pmatrix}
\Re \frac{-2}{(iz-1)^2} & - \Im \frac{-2}{(iz-1)^2} & 0 \\
\Im \frac{-2}{(iz-1)^2} & \Re \frac{-2}{(iz-1)^2} & 0 \\
-2 \Im \frac{1}{z+i} & - 2 \Re \frac{1}{z+i} & 1 
\end{pmatrix}.
$$
In particular at $z=0$ we get
$$
(df_*)_{(0,\theta)} =
\begin{pmatrix}
-2 & 0 & 0 \\ 
0 & -2 & 0 \\
2 & 0 & 1 
\end{pmatrix}.
$$
Since this is an isometry, the three image vectors $(-2,0,2)$, $(0,-2,0)$, and $(0,0,1)$ are orthogonal with norm $2,2,1$, hence $(1,0,-1)$, $(0,1,0)$, and $(0,0,1)$ form an orthonormal basis at $T_{(i,\theta+\pi)}UH^2$ and the metric tensor there is
$$\begin{pmatrix}
2 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 1
\end{pmatrix}.
$$
The tensor is independent of $\theta$. To find its value at $(z,\theta)$ for a generic $z\in H^2$ it suffices to transport it via an isometry that sends $i$ to $z$. Every such isometry is a composition of a horizontal translation (which does not change the tensor) and a dilation $g(z) = \lambda z$ with $\lambda >0$. We have $g'(z) = \lambda$ and $g_*(z,\theta) = (\lambda z, \theta)$, therefore $dg_*$ sends the above orthonormal basis at $T_{(i,\theta)}$ to the basis $(\lambda, 0, -1)$, $(0,\lambda,0)$, $(0,0,1)$. The metric tensor at $(\lambda i, \theta)$ is hence
$$\begin{pmatrix}
2\lambda^{-2} & 0 & \lambda^{-1} \\
0 & \lambda^{-2} & 0 \\
\lambda^{-1} & 0 & 1
\end{pmatrix}.
$$
The proof is complete.
\end{proof}
At a point $(x,y,\theta) \in UH^2$, an orthonormal basis is
\begin{equation} \label{UH2:orthonormal:eqn}
(y,0,-1), \quad (0,y,0), \quad (0,0,1).
\end{equation}
The planes orthogonal to $(0,0,1)$ form a contact structure similar to the one drawn in Figure \ref{contact:fig}. 

We remark that the metric tensor at $(x,y,\theta)$ has determinant $y^{-4}$, like in the product metric $H^2 \times S^1$: therefore the volume form in $UH^2$ is the same as in the product metric (although the metric tensor is not).

The non-zero Christoffel symbols at $(x,y,\theta)$ are:
$$\Gamma^1_{12} = \Gamma^1_{21} = -\frac 3{2y}, \quad 
\Gamma^1_{23} = \Gamma^1_{32} = -\frac 12,$$
$$\Gamma^2_{11} = \frac 2y, \quad
\Gamma^2_{13} = \Gamma^2_{31} = \frac 12, \quad \Gamma^2_{22} = -\frac 1y,$$
$$\Gamma^3_{12} = \Gamma^3_{21} = \frac 1{y^2}, \quad
\Gamma^3_{23} = \Gamma^3_{32} = \frac 1{2y}.$$
The Ricci tensor is
$$
R_{ij} = \frac 12 \cdot
\begin{pmatrix}
-2 y^{-2} & 0 & y^{-1} \\
0 & - 3y^{-2} & 0 \\
y^{-1} & 0 & 1
\end{pmatrix}.
$$
When $y=1$ we can represent the Ricci tensor in the orthonormal basis (\ref{UH2:orthonormal:eqn}) and get a diagonal matrix with values $-\frac 32$, $-\frac 32$, $\frac 12$. For a vector $v\in T_{(z,\theta)} U\matH^2$, recall that $R_{ij}v_iv_j$ is twice the average value of the sectional curvatures of the planes containing $v$: this average value ranges from $-\frac 34$ to $\frac 14$ and is maximal when $v=(0,0,\pm 1)$. This holds when $y=1$ and hence for any $z\in U\matH^2$ by acting via isometries of $\matH^2$. 


\subsection{$\widetilde{\SL_2}$ geometry}
Let $\widetilde {\SL_2}$ be the universal cover of $\SL_2 = \SL_2(\matR)$. 
As a universal cover of a Lie group, it is also a Lie group.
We have coverings
$$\widetilde{\SL_2} \longrightarrow \SL_2 \longrightarrow \PSLR = \Iso^+(\matH^2).$$
The group $\PSLR$ acts freely and transitively on $U\matH^2$ and hence we can identify $\PSLR$ with $U\matH^2$. With this identification $\PSLR$ inherits a left-invariant Riemannian metric that lifts to a left-invariant Riemannian metric on the Lie group $\widetilde{\SL_2}$. 

In the previous section we have identified $U\matH^2$ with $H^2 \times S^1$ and we can likewise identify $\widetilde{\SL_2}$ with $H^2 \times \matR$, and get an explicit metric tensor from Lemma \ref{UH2:tensor:lemma}.

Since $U\matH^2$ is a circle bundle over $\matH^2$, likewise $\widetilde{\SL_2}$ is a line bundle over $\matH^2$. The group $\matR$ acts isometrically on $\widetilde \SL_2$ by translating every fibre.

\begin{prop}
Every isometry of $\widetilde{\SL_2}$ preserves the line bundle and induces an isometry of $\matH^2$. We have
$$0 \longrightarrow \matR \longrightarrow \Iso^+(\widetilde{\SL_2}) \stackrel p\longrightarrow \Iso(\matH^2) \longrightarrow 0.$$
The group $\Iso^+(\widetilde{\SL_2})$ has two components. 
\end{prop}
\begin{proof}
The groups $\matR$ and $\widetilde{\SL_2}$ belong to the component $\Iso^+_\circ (\widetilde{\SL_2})$ containing $e$ which has dimension at least $1+3=4$. We conclude as in the proof of Proposition \ref{Nil:isometries:prop}.
\end{proof}

\begin{ex}
The unit tangent bundle of a finite-area complete hyperbolic surface is naturally a manifold modelled on $\widetilde{\SL_2}$.
\end{ex}

As for $\Nil$, cocompact groups do no lift.

\begin{prop} \label{SL2:no:lift:prop}
Let $\Gamma < \Iso(\matH^2)$ be discrete and cocompact. There is no homomorphism $f\colon \Gamma \to \Iso^+(\widetilde{\SL_2})$ such that $p\circ f = \id$.
\end{prop}
\begin{proof}
Up to taking a finite index subgroup we may suppose that $\Gamma$ acts freely and hence $S=\matH^2/_\Gamma$ is a closed hyperbolic surface. If $\Gamma$ lifts, consider the group $G< \Iso^+(\widetilde{\SL_2})$ generated by $f(\Gamma)$ and $2 \pi\in \matR$, isomorphic to $\Gamma \times \matZ$. The quotient $\widetilde{\SL_2}/_G$ is naturally the unit tangent bundle of $S$ and is hence the Seifert manifold $\big(S, (1, \chi(S))\big)$ by Remark \ref{bundle:oss}. Its fundamental group is however not a product $\Gamma \times \matZ$ by Exercise \ref{bundle:ex}.
\end{proof}

\begin{prop} \label{SL2:cofinite:prop}
A discrete group $\Gamma < \Iso^+(\widetilde{\SL_2})$ is cofinite if and only if both $p(\Gamma)$ and $\Gamma \cap \ker p$ are discrete and cofinite.
\end{prop}
\begin{proof}
Same proof as Proposition \ref{H2R:prop}, with a minor variation: if $p(\Gamma)$ is not discrete, up to taking an index-two subgroup we suppose that $p(\Gamma) <  \Iso^+(\matH^2)$; the $\matR$-action commutes with $\Gamma$ and $[f,g]$ depends only on $p(f)$ and $p(g)$, so that proof applies.
\end{proof}

We now classify the manifolds having a $\widetilde{\SL_2}$ geometry.

\begin{cor}
If the interior of a compact orientable manifold $M$ admits a finite-volume complete $\widetilde{\SL_2}$ geometry then $M$ is a Seifert manifold with $\chi<0$. If $M$ is closed then $e\neq 0$.
\end{cor}
\begin{proof}
We have $\interior M= \widetilde{\SL_2}/_\Gamma$ with $\Gamma$ cofinite. Proposition \ref{SL2:cofinite:prop} furnishes a Seifert fibration $M\to S$ over the finite-area orbifold $S=\matH^2/_{p(\Gamma)}$. If $M$ is closed we get $e\neq 0$: if not, up to taking a finite index subgroup we would get $M=S\times S^1$ contradicting Proposition \ref{SL2:no:lift:prop}.
\end{proof}

We now prove the converse.

\begin{prop}
If $M$ is a Seifert manifold with $\chi<0$ and either $\partial M\neq \emptyset$ or $e\neq 0$, the interior of $M$ admits a finite-volume $\widetilde{\SL_2}$ geometry.
\end{prop}
\begin{proof}
If $M$ is closed we apply the proof of Proposition \ref{Nil:construct:prop}. If $\partial M \neq \emptyset$ the presentations of $\pi_1(S)$ and $\pi_1(M)$ are as described there, except that they do not contain the relator $c_i^{p_i}$ whenever $c_i$ represents a boundary component of $M$. So we have less constraints and we easily see that a solution to the final linear problem exists also in this case. 
\end{proof}
