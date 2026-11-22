---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-081-153-proof-of-the-theorem
section_title: "Proof of the theorem"
section_number: 15.3
pages: 469-476
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.942
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We now conclude the proof of Theorem \ref{DF:teo}.
Through all this section, we let $M= \interior N$ be a complete orientable finite-volume cusped hyperbolic three-manifold. We have $\partial N = T_1 \cup \ldots \cup T_c$ for some $c\geqslant 1$. We also fix a positive pair $m_i, l_i$ of generators for $\pi_1(T_i)$ at each $T_i$. Recall that each $T_i$ has Euclidean structure, defined up to rescaling.


\subsection{Near the complete solution} \label{near:complete:subsection}
We now suppose that $M$ has a geometric decomposition $\calT$ into ideal hyperbolic tetrahedra, in other words the space $\Def(M,\calT)$ is non-empty and contains a complete solution $z^0$. We want to study $\Def(M,\calT)$ near $z^0$. 

We defined in Section \ref{generalized:DF:subsection} the generalised Dehn filling invariant of a solution $z\in\Def(M,\calT)$ at $T_i$ to be $\infty$ if $\mu(m_i) = \mu(l_i)=1$, or the unique point $(p,q)\in \matR^2$ such that $\tilde\mu(m_i)^p \tilde\mu(l_i)^q = e^{2\pi i}$ otherwise. We denote this invariant by $d_i(z)\in S^2 = \matR^2 \cup \{\infty\}$ and get a map 
$$d\colon \Def(M,\calT) \longrightarrow \underbrace{S^2 \times \ldots \times S^2}_c$$
such that $d(z^0) = (\infty,\ldots,\infty)$.

\begin{prop} \label{d:local:homeo:prop}
The map $d$ is a local homeomorphism at $z^0$.
\end{prop}
\begin{proof}
We set
$$u_i = \log \tilde\mu(m_i), \qquad v_i = \log \tilde \mu(l_i).$$
The sets $(u_1,\ldots,u_c)$ and $(v_1,\ldots, v_c)$ are both biholomorphic coordinates on $\Def(M,\calT)$ which vanish at $z^0$. Moreover $v_i$ vanishes precisely where $u_i$ does (on solutions that are complete at $T_i)$. 

Recall from Exercise \ref{rho:derivative:ex} that $\mu = \rho'$ is the derivative of the holonomy $\rho$ at $T_i$. When $u_i = v_i = 0$ the solution is complete at $T_i$ and up to conjugation we have
$$\rho(m_i)\colon z \mapsto z +1, \qquad \rho(l_i)\colon z \mapsto z + w_i$$
for some $w_i\in \matC$ with $\Im w_i>0$ which determines the cusp shape of $T_i$. When $u_i, v_i \neq 0$ the solution is incomplete and
$$\rho(m_i) \colon z \mapsto az, \qquad \rho(l_i) \colon z \mapsto bz$$
for some $a,b\neq 0$.
When $u_i, v_i \to 0$, a fundamental domain of $\Img\rho$ with vertices at $x,ax, bx, abx$ tends up to rescaling to one with vertices at $x, x+1, x+w_i, x+1+w_i$. Since $a,b \to 1$ we get
$$v_i = \log b \sim b-1 \sim w_i(a-1) \sim w_i \log a = w_iu_i$$
where $\sim$ means first-order equality. Therefore $\frac{v_i}{u_i} = w_i$ at the complete solution $v=u=0$. We deduce in particular that the function $\frac{v_i}{u_i}$ is analytic on $\Def(M,\calT)$.
In what follows we only use that $\Im w_i > 0$.

We consider the following map, defined whenever $(p_i,q_i) \neq (0,0)$ for all $i$:
$$\varphi\big((p_1,q_1), \ldots, (p_c, q_c)\big) = 2\pi i \left( \frac 1 {p_1+q_1w_1}, \ldots, \frac 1{p_c + q_cw_c}\right).$$
We extend it continuously to the case $(p_i, q_i) = \infty$ by setting the $i$-th component of the image to be zero.
By composing $\Phi = \varphi \circ d$ we get a map $\Phi\colon \Def(M,\calT) \to \matC^c$ that sends the complete solution $u=0$ to $(0,\ldots,0)$. We prove that $\Phi$ is differentiable and $d\Phi_0$ is invertible: this will conclude the proof. When $u_j, v_j \neq 0$ we have
$$p_ju_j + q_jv_j = 2\pi i$$
and Proposition \ref{pq:explicit:prop} gives
$$p_j = - 2 \pi \frac{\Re v_j}{\Im (\bar u_j v_j)}, \qquad q_j = 2 \pi \frac{\Re u_j}{\Im (\bar u_jv_j)}.$$
Near $u=v=0$ we have $v_j \sim w_ju_j$ and hence
$$p_j \sim - 2 \pi \frac{\Re w_j \Re u_j - \Im w_j \Im u_j}{|u_j|^2\Im w_j}, \qquad
q_j \sim 2 \pi \frac{\Re u_j}{|u_j|^2\Im w_j}
$$
and therefore
\begin{align*}
\varphi_j & = 2\pi i \frac 1{p_j + q_jw_j} \sim i\frac{|u_j|^2 \Im w_j}{-\Re w_j \Re u_j + \Im w_j \Im u_j + w_j \Re u_j} \\
& =
i\frac{|u_j|^2 \Im w_j}{\Im w_j \Im u_j + i\Im w_j \Re u_j} 
=
i\frac{|u_j|^2 \Im w_j}{i \bar u_j \Im w_j} = u_j
\end{align*}
giving $d\Phi_0 = \id$. 
\end{proof}

If $M$ has a geometric decomposition $\calT$ into ideal tetrahedra, we can easily conclude the proof of Theorem \ref{DF:teo} as follows: the geometric ideal triangulation $\calT$ determines a complete solution $z^0 \in \Def(M,\calT)$, and by Proposition \ref{d:local:homeo:prop} the image of the generalised Dehn filling map $d\colon \Def(M,\calT) \to S^2\times \ldots \times S^2$ is an open set $U$ containing $(\infty, \ldots, \infty)$. The discussion in Section \ref{generalized:DF:subsection} finishes the proof.

However, we still do not know if every complete cusped finite-volume $M$ decomposes into ideal tetrahedra! If that were the case, we would be done. Unfortunately we are not able to prove this, so more effort is needed to complete the proof.


\subsection{Triangulations with flat tetrahedra}
As we said, we are not able to prove that every cusped finite-volume $M$ decomposes into ideal tetrahedra. The best that we can do is to show that $M$ decomposes into ideal tetrahedra that are either ordinary or ``flat'', that is degenerated to an ideal quadrilateral. We show this using the Epstein--Penner canonical decomposition.

The Epstein-Penner canonical decomposition (see Theorem \ref{EP:teo}) partitions $M$ into some ideal polyhedra $P_1,\ldots, P_k$, glued isometrically along their faces. Can we further subdivide this partition to get a geometric triangulation of $M$? We start by triangulating each $P_i$ individually.

\begin{prop} \label{poly:tetra:prop}
Every ideal polyhedron $P\subset \matH^3$ subdivides into ideal tetrahedra.
\end{prop}
\begin{proof}
We can use the Klein model, so that ideal polyhedra in $\matH^3$ correspond to Euclidean polyhedra with vertices in $S^2$. We fix a vertex $v\in P$, and a vertex $v_i$ in every face $f_i$ of $P$ not incident to $P$. We triangulate each $f_i$ by coning along $v_i$, and then we triangulate $P$ by coning all the triangulated faces $f_i$ along $v$.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{layered-BW}{layered}} 
\nota{The triangulations of two isometric faces that do not match (left) because they are obtained by coning along distinct vertices $v\neq v'$ (centre). We can add some additional ``flat'' tetrahedra to correct this (right).}
\label{layered:fig}
\end{center}
\end{figure}

The problem is, that we are not able to guarantee that the triangulations of the polyhedra $P_1,\ldots, P_k$ match at each pair of glued faces. The typical situation is shown in Figure \ref{layered:fig}-(left): two isometric $n$-gons (with $n\geqslant 4$) are triangulated by coning on distinct vertices $v\neq v'$.

There is one thing that we can do, however: we can insert some \emph{flat} tetrahedra between the two $n$-gons that connect the two mismatching triangulations as in Figure \ref{layered:fig}-(right), and obtain a partially-flat ideal triangulation of $M$. The flat tetrahedra can be inserted as follows: if $v$ and $v'$ share an edge we insert $n-3$ flat tetrahedra as suggested by Figure \ref{layered:fig}-(right); otherwise, the diagonal joining $v$ and $v'$ is common to both triangulations and we proceed inductively on each of the two sub-polygons cut by this diagonal. 

The resulting ideal triangulation $\calT$ contains $n$ tetrahedra $\Delta_1,\ldots, \Delta_n$; each $\Delta_i$ is either \emph{fat} (it lies inside some polyhedron $P_j$) or \emph{flat} (it connects two faces of the $P_j$). We now fix arbitrarily a pair of opposite edges in each $\Delta_i$ and denote by $z_i\in \matC$ the modulus of $\Delta_i$ at these edges. If $\Delta_i$ is fat, then $\Im z_i>0$ as usual; if $\Delta_i$ is flat, the modulus $z_i$ still makes sense as a number in $\matR\setminus\{0,1\}$:
the vertex triangle of Figure \ref{tetraedro2:fig}-(left) is a degenerated flat triangle with three vertices $0,1,z_i$. The flat tetrahedron has three real moduli $z_i, \frac{z_i-1}{z_i}, \frac 1{1-z_i}$; two arguments are $0$ and one is $\pi$.

We set $z^0 = (z_1,\ldots, z_n)$. By construction, the point $z^0$ satisfies the consistency equations (\ref{gi:eqn}). 


\subsection{Perturbations}
We now let $U$ be a small contractible neighbourhood of $z^0$ in $(\matC \setminus \{0,1\})^n$. Note that $U$ necessarily contains some points $z$ with $\Im z_i <0$ for some $i$. The consistency equations (\ref{gi:eqn}) make sense in $U$, and we define $\Def_U \subset U$ to be the set of solutions. We still have $\Def_U = G^{-1}(2\pi i, \ldots, 2\pi i)$.

Does a solution $z\in \Def_U$ determine a hyperbolic structure on $M$? Intuitively, each modulus $z_j$ with $\Im z_j=0$ should represent a flat tetrahedron, each $z_j$ with $\Im z_j <0$ a negatively oriented fat tetrahedron, and positively and negatively oriented tetrahedra should overlap; although appealing, it is however hard (and sometimes impossible) to translate this idea into a concrete definition in general.

Our aim is to prove Theorem \ref{DF:teo} by perturbing $z^0$, so we only need here to furnish a geometric interpretation for the solutions $z$ that lie in a sufficiently small neighbourhood $U$. We do this as follows. 

If $z$ is sufficiently close to $z^0$, all the fat tetrahedra that triangulate a single polyhedron $P_i$ stay positively fat, and since they satisfy the consistency equations along the internal edges of $P_i$ they glue to form a possibly non-convex polyhedron $P_i(z)\subset \matH^3$. The original faces of $P_i$ are now bent in $P_i(z)$ along their diagonals.

We now consider the originally flat tetrahedra joining two faces of two polyhedra $P_i(z)$ and $P_j(z)$. We assign all of them to one of the two polyhedra, say $P_i(z)$, and forget about $P_j(z)$. These tetrahedra are attached to some $n$-gonal face $f$ of $P_i(z)$, bent along its diagonals. The effect of each attached tetrahedron $\Delta_j$ is to flip a diagonal, and we modify $P_i(z)$ accordingly by replacing the two ideal triangles in $f$ incident to the old diagonal with the two triangles sharing the new one. Geometrically, this corresponds to adding $\Delta_j$ if $\Im z_i >0$, or to cut $\Delta_j$ away from $P_j(z)$ is $\Im z_j <0$. At the end of the process, we get a new polyhedron $P_j'(z)$ with the same vertices as $P_j(z)$, whose faces are bent along different diagonals.

The new possibly non-convex polyhedra $P_j'(z)$ glue isometrically along their paired faces, that are now bent along the same diagonals. The consistency equations are satisfied along these diagonals, hence we get a hyperbolic structure for $M$. We summarise our discoveries:

\begin{prop}
If $U$ is sufficiently small, every solution $z \in \Def_U$ represents naturally a hyperbolic structure on $M$.
\end{prop}


\subsection{Local smoothness}
We have seen that every solution $z$ that is sufficiently close to $z^0$ determines a hyperbolic metric on $M$. We now need to extend Corollary \ref{smooth:cor}. 

\begin{prop} \label{smooth:flat:prop}
If $U$ is sufficiently small then $\Def_U$ is a complex manifold of dimension $c$.
\end{prop}
\begin{proof}
As in Corollary \ref{smooth:cor}, it suffices to prove that $dG_{z^0}\colon V^n \to \ker B'$ has maximum rank and is hence invertible.

The only place where we used $\Im z_j >0$ is the proof of Proposition \ref{Choi:prop}, and we now modify it so that it applies also to our partially flat solution $z^0$. We have $M = Z^\intercal (A')^\intercal$ and we need to prove that $\rk M = \rk A' = n-c$.

We needed $z_i \not \in \matR$ to prove that $Z^\intercal|_{\matR^{2n}}$ is injective: this is not the case here, since $\frac 1{z_i}$ and $\frac 1{z_i-1}$ are not $\matR$-independent when $\Delta_i$ is flat. Now we have
$$\ker Z^\intercal |_{\matR^{2n}} = \Span \{ z_ie_i +(1-z_i)e_{i+n}\ | \ \Delta_i\ {\rm is\ flat} \}.$$
For $\matK=\matR, \matC$ we write 
$$\matK^{2n} = \matK^{2n}_{\rm fat} \oplus \matK^{2n}_{\rm flat}, \qquad \matK^n = \matK^n_{\rm fat} \oplus \matK^n_{\rm flat}$$
where $\matK^{2n}_{\rm fat}$ ($\matK^{2n}_{\rm flat}$) is generated by the $e_i, e_{i+n}$ such that $\Delta_i$ is fat (flat), and similarly $\matK^{n}_{\rm fat}$ ($\matK^{n}_{\rm flat}$) is generated by the $e_i$ such that $\Delta_i$ is fat (flat).

The following restriction of $Z^\intercal$ is still an isomorphism:
$$Z^\intercal|_{\matR^{2n}_{\rm fat}}\colon \matR^{2n}_{\rm fat}
\longrightarrow \matC^n_{\rm fat}.$$
We use it to push-forward $\omega$ to a symplectic form $\Omega$ on $\matC^n_{\rm fat}$, and we extend it trivially to an alternating bilinear form $\Omega$ on $\matC^n$ with radical $\matC^n_{\rm flat}$.

It is still true that $M(\matR^{2n})$ has real dimension $n-c$, because $(A')^\intercal(\matR^{2n})$ intersects $\ker Z^\intercal$ trivially. To prove this, suppose that a vector $v'\in\matR^{2n}$ that is $\matR$-generated by the rows of $A'$ lies in the kernel of $Z^\intercal$, that is:
\begin{itemize}
\item $(v_i', v_{i+n}')=(0,0)$ for every fat $\Delta_i$,
\item $(v_i',v_{i+n}') = k_i(z_i, 1-z_i)$ for some $k_i \in \matR$, for every flat $\Delta_i$. 
\end{itemize}
We define $v \in \matR^{3n}$ by setting
$$v_i = v'_i, \quad v_{n+i} = - v'_{n+i}, \quad, v_{2n+i} = 0$$
for all $i=0,\ldots, n-1$. We note that each triple $(v_i, v_{n+i}, v_{2n+i})$ is either $(0,0,0)$, or it contains three pairwise distinct real numbers. The vector $v' \in\matR^{2n}$ is generated by the $n$ rows of $A'$ $\Longleftrightarrow$ the vector $v\in\matR^{3n}$ is generated by the $n$ rows of $A$ (exercise). 

We interpret $v$ as a colouring of the $3n$ edge pairs in $\calT$. The colouring $v$ is everywhere zero on all fat tetrahedra, and on each flat tetrahedron it is either $(0,0,0)$ or consists of three pairwise distinct numbers. We must prove that it is zero everywhere.

The vector $v$ is contained in the lagrangian subspace generated by the rows $A_1,\ldots, A_{2n}$ of $A$. In particular we have $\omega(v,A_{n+i})=0$ for all $i$. Every row $A_{n+i}$ corresponds to an edge $e$ of $\calT$, and this equality says that the colours on all tetrahedra incident to $e$ of the edge pairs not containing $e$ sum to zero, provided that they are counted with signs in each tetrahedron. This implies the following: if all such tetrahedra except one $\Delta_j$ have colour zero on all their edge pairs, then two edge pairs on $\Delta_j$ have the same colours, and by what just said on $v$ this implies that all colours are zero also on $\Delta_j$. 

Consider a sequence $\Delta_1, \ldots, \Delta_k$ of flat tetrahedra that connects two faces of two polyhedra $P_i$ and $P_j$ of the Epstein-Penner decomposition. There is one edge of $\Delta_1$ that is incident only to fat tetrahedra except $\Delta_1$, and the above discussion implies that all the colours on $\Delta_1$ are zero; by induction we deduce that all the flat $\Delta_i$ have zero colours. Therefore $v=0$, as required.

We have proved that $\dim M(\matR^{2n}) = n-c$, and we conclude as in the proof of Proposition \ref{Choi:prop}. The form $\Omega$ defines a positive semidefinite scalar product $\langle, \rangle$ on $\matC^n$ with radical $\matC^n_{\rm flat}$. If $\rk M < n-c$, there are two vectors $v_1,v_2\in \matR^n$ such that $M(v_1+iv_2) = 0$ while $Mv_1 \neq 0$ and $Mv_2 \neq 0$. We get $\|Mv_1\| = \|Mv_2\| = 0$ as in the proof of Proposition \ref{Choi:prop}, and this implies that $Mv_1, Mv_2$ both lie in the radical $\matC^n_{\rm flat}$.

If $Mv_1, Mv_2 \in \matC^n_{\rm flat}$ then both $Mv_1$ and $Mv_2$ are real since $\frac 1{z_i}, \frac{1}{z_i-1} \in \matR$ for every flat $\Delta_i$. Now $0 = M(v_1+iv_2) = Mv_1 + iMv_2$ implies that $Mv_1 = Mv_2 = 0$, a contradiction.
\end{proof}


\subsection{Conclusion of the proof}
The proof of Theorem \ref{DF:teo} finishes like in the geometric triangulation case.
All the discussion of Section \ref{holonomy:subsection} applies here: the holonomies are defined also in this context and may be used to parametrize the complex manifold $U(z^0)$. The strategy of Section \ref{near:complete:subsection} is still valid: the generalised Dehn filling invariant map $d$ sends $U(z^0)$ to an open neighbourhood of $(\infty,\ldots, \infty)$ in $S^2\times \ldots \times S^2$ and the discussion in Section \ref{generalized:DF:subsection} finishes the proof.
We have completed the proof of Theorem \ref{DF:teo}.


\subsection{Mostow--Prasad rigidity}
We can use the Dehn filling Theorem \ref{DF:teo} to extend Mostow Rigidity Theorem \ref{Mostow:teo} from the closed to the cusped case. The cusped case was proved by Prasad in 1973, hence the theorem is known as \emph{Mostow--Prasad Rigidity Theorem}.\index{Mostow--Prasad rigidity theorem}

Let $N$ a be compact orientable three-manifold bounded by some $c\geqslant 0$ tori, and let $M=\interior N$.

\begin{teo}[Mostow--Prasad rigidity]
The manifold $M$ admits at most one finite-volume complete hyperbolic metric up to isometries homotopic to the identity.
\end{teo}
\begin{proof}
The $c=0$ case is Theorem \ref{Mostow:teo}, so we suppose $c>1$. Roughly, the metric on $M$ is unique because it is the limit of hyperbolic metrics on its closed Dehn fillings, that are unique by Theorem \ref{Mostow:teo}. (We are using the hyperbolic Dehn filling theorem as a trick to extend Mostow's rigidity from the closed to the cusped case: this is certainly not Prasad's original proof, that was published before any hyperbolic Dehn filling was studied, and more importantly it applies to all dimensions $n\geqslant 3$.)

More precisely, let $M$ have two finite-volume hyperbolic metrics $m_1$ and $m_2$. The Dehn filling Theorem holds for both, and yields sequences $M_i^j$ of closed hyperbolic three-manifolds obtained from $M$ by Dehn filling with parameter $s^j$ such that  $s^j \to (\infty, \ldots, \infty)$, for $i=1,2$.

Mostow theorem furnishes an isometry $M_1^j \to M_2^j$ homotopic to the identity. The core closed geodesics of the filling solid tori are unique in their homotopy classes, hence by removing them we get isometric incomplete metrics. Since $m_1$ and $m_2$ are limits of these, they are also isometric.

This latter sentence can be made rigorous as follows: let $\calT$ be a partially flat ideal triangulation for $M$ in the metric $m_1$. Pick an ideal tetrahedron $\Delta$ in $\calT$ and note that it can be straightened uniquely also in the incomplete metrics for $M$ close to the complete ones, just by extending the construction in the proof of Proposition \ref{straighten:incomplete:prop} from dimension two to three (an orientation of the core geodesics is needed to define the straightening unambiguously). The modulus $z\in \matC_{>0} \cup (\matR \setminus \{0,1\})$ of the straightened $\Delta$ in $M$ is intrinsically determined as the limit of the moduli of the straightenings of $\Delta$ in the $M_i^j$, hence it is the same for both metrics $m_1$ and $m_2$. It follows that $m_2$ has the same geometric ideal decomposition of $m_1$, and hence $m_1=m_2$ after a homotopy. 
\end{proof}
