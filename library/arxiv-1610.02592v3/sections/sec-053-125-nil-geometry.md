---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-053-125-nil-geometry
section_title: "Nil geometry"
section_number: 12.5
pages: 394-404
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.624
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
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
