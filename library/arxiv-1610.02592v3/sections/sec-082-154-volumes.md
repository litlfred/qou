---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-082-154-volumes
section_title: "Volumes"
section_number: 15.4
pages: 476-487
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We have discovered that ``most'' Dehn fillings of a cusped finite-volume hyperbolic manifold are hyperbolic, and we now discuss their volumes.

Let $M$ be a complete orientable finite-volume cusped hyperbolic three-manifold. We say that  a Dehn filling of $M$ is \emph{non-trivial} if it fills at least one boundary torus; in other words, it is determined by some Dehn filling parameter $s$ different from $(\infty, \ldots, \infty)$, after fixing some arbitrary homology bases for the boundary tori. We prove in this section the following theorem. 

\begin{teo} \label{vol:vol:teo}
If a non-trivial Dehn filling $M^{\rm fill}$ of $M$ admits a complete finite-volume hyperbolic metric, then
$$\Vol(M^{\rm fill}) < \Vol(M).$$
If $s^i$ is any sequence of non-trivial Dehn filling parameters converging to $(\infty,\ldots, \infty)$, and $M^i$ is the manifold obtained by filling $M$ along $s^i$, then $M^i$ is eventually hyperbolic and
$$\Vol (M^i) \nearrow \Vol(M).$$
The cores of the filling solid tori are eventually simple closed geodesics and their lengths tend to zero.
\end{teo}

We already know that if $s^i \to (\infty, \ldots, \infty)$ then $\Vol(M^i) \to \Vol(M)$ and the cores of the solid tori are closed geodesics whose length tend to zero: this follows from the construction of the metric on $M^i$ via geometric ideal triangulations. In some sense (that we will not make precise), the metric on $M^i$ converges to that of $M$, and the core geodesics become so short that they disappear in the limit opening the filling solid torus to a cusp.

The only new fact to prove is that the volume strictly decreases under \emph{any} Dehn filling $M^{\rm fill}$, not only those that are close to $(\infty, \ldots, \infty)$: this is rather subtle, because the hyperbolic metric on $M^{\rm fill}$ might not be obtained by completing ideal triangulations of $M$. (For instance, the core tori in $M^{\rm fill}$ may not be isotopic to closed geodesics.)

We prove the theorem as follows. We first consider the case where $M$ has an ideal geometric triangulation $\calT$: in that case $\Def(M,\calT)$ is a nice smooth complex manifold and we investigate the volume function 
$$\Vol\colon \Def(M,\calT) \longrightarrow \matR_{>0}$$
that computes the volume of each hyperbolic structure on $M$. We show that the volume function makes sense in a bigger convex set containing $\Def(M,\calT)$ and is also easier to study there. This bigger convex set is the set of \emph{angle structures} on $\calT$. We prove that the volume function is strictly concave there, and the complete solution is a global maximum.\index{angle structure} 

We conclude with a couple of finite-covering tricks to pass from local (near $(\infty, \ldots, \infty)$) to global, and to deal with more general manifolds $M$ that do not decompose into hyperbolic ideal tetrahedra.


\subsection{Angle structures}
Let $M= \interior{N}$ where $N$ is an orientable compact three-manifold bounded by $c>0$ tori, equipped with an oriented ideal triangulation $\calT$ with $n$ tetrahedra $\Delta_1,\ldots, \Delta_n$ and $n$ edges $e_1,\ldots, e_n$. We identify orientation-preservingly each $\Delta_i$ with the one shown in Figure \ref{tetrahedron_labels:fig}, and we label the edge pairs of type 1, 2, 3, with the numbers $i$, $i+n$, and $i+2n$ respectively.

An \emph{angle structure} $\theta$ on $M$ is the assignment of an \emph{angle} $0< \theta_j < \pi$ to the $j$-th edge pair in $\calT$, with the following requirements:
\begin{enumerate}
\item at each tetrahedron $\Delta_i$ we have $\theta_i + \theta_{i+n} + \theta_{i+2n} = \pi$,
\item at each edge $e_i$, the sum of the incident angles is $2\pi$.
\end{enumerate}
The set of angle structures is thus a subset $\calA \subset \matR_{>0}^{3n}$. It is the intersection of the affine subspace in $\matR^{3n}$ determined by the conditions (1) and (2) with the cone $\matR_{>0}^{3n}$, so in particular it is convex. By definition this affine subspace is the solution space of the linear system
$$A\theta = \begin{pmatrix} \pi \\ 2\pi \end{pmatrix}$$
where $A$ is the incidence $2n \times 3n$ defined in Section \ref{incidence:matrices:subsection} and depicted in Figure \ref{ABmatrices:fig}-(left), and $\theta = (\theta_1, \ldots, \theta_{3n})\in \matR^{3n}$.

What is the geometric meaning of an angle structure $\theta$ on $\calT$? Thanks to condition (1), every $\Delta_i$ is realised by a unique ideal hyperbolic tetrahedron with dihedral angles $\theta_i, \theta_{i+n}$, and $\theta_{i+2n}$ whose complex modulus is
\begin{equation} \label{theta:z:eqn}
z_i = \frac{\sin \theta_{i+n}}{\sin \theta_{i+2n}}e^{i\theta_i}.
\end{equation}
Angle structures are then in natural 1-1 correspondence with the realisations of the tetrahedra $\Delta_1,\dots, \Delta_n$ as ideal hyperbolic tetrahedra, with the mild condition (2) that their dihedral angles around each edge $e_i$ must sum to $2\pi$. 

Condition (2) is only ``half'' of the consistency equation at each $e_i$, which requires the product of the complex moduli to be 1: condition (2) alone does \emph{not} guarantee that by gluing these tetrahedra we get a hyperbolic structure on $M$: some ``shearing'' may arise when you turn around an edge $e_i$.

With this geometric description, the deformation space $\Def(M,\calT)$ is naturally a smooth submanifold of $\calA$. 


\subsection{Dimensions}
We will henceforth suppose that $\Def(M,\calT)$ is non-empty and contains a complete solution $z^0$, that is $\calT$ can be realised as a geometric ideal triangulation. This implies in particular that $\calA$ is also non-empty and has dimension $\dim\ker A = 3n - (2n-c) =n+c$ by Corollary \ref{rk:A:cor}. The space $\Def(M,\calT)$ is a real smooth submanifold of dimension $2c$. 

The tangent space $T_\theta\calA$ at any point $\theta\in\calA$ is of course $\ker A$. We now construct an explicit set of generators for $\ker A$. Recall from Section \ref{boundary:curves:subsection} that every simplicial closed oriented curve $\gamma$ in a triangulated boundary torus $T_i$ defines an integer vector $v_\gamma \in \matR^{3n}$. 

Recall the alternating form $\omega$ on $\matR^{3n}$ from Section \ref{symplectic:form:subsection}: we consider it as a matrix and write $v^* = \omega v$ for all $v\in \matR^{3n}$, so that $\omega(v,w) = \langle v, w^* \rangle$ where $\langle, \rangle$ is the Euclidean scalar product. We denote by $A_i$ the $i$-th row of $A$, considered as a vector in $\matR^{3n}$.

We fix two arbitrary generators $m_i, l_i$ of $\pi_1(T_i)$ for all $i=1,\ldots, c$.

\begin{prop} \label{redundant:generators:prop}
The tangent space $T_\theta \calA = \ker A$ is generated by the (not independent) $n+2c$ vectors
$A_{n+1}^*,\ldots, A_{2n}^*, v_{m_1}^*, v_{l_1}^*, \ldots, v_{m_c}^*, v_{l_c}^*$.
\end{prop}
\begin{proof}
Propositions \ref{rows:lagrangian:prop} and \ref{A:gamma:gamma':prop} say that the rows of $A$ are $\omega$-orthogonal to themselves and to $v_\gamma$ for any $\gamma$, hence they are $\langle, \rangle$-orthogonal to all vectors $A_i^*$ and $v_\gamma^*$, in other words $A_i^*, v_\gamma^* \in \ker A$.

To prove that the $n+2c$ listed vectors generate $\ker A$ it suffices to show that they span a subspace of dimension $n+c$. Proposition \ref{A:bar:lagrangian:prop} says that if we add the rows $v_{m_1}, \ldots, v_{m_c}$ to $A$ we get a rank-$2n$ matrix. The same proof shows that by further adding the rows $v_{l_1},\ldots, v_{l_c}$ we get a rank-$(2n+c)$ matrix. 

The vectors $A_1,\ldots, A_{2n},v_{m_1}, v_{l_1}, \ldots, v_{m_c}, v_{l_c}$  span a dimension-$(2n+c)$ space. Since $\dim \ker \omega = n$, the vectors $A_1^*,\ldots, A_{2n}^*,v_{m_1}^*, v_{l_1}^*, \ldots, v_{m_c}^*, v_{l_c}^*$ span a space of dimension at least $2n+c-n = n+c$. Since $A_1^* = \ldots = A_n^* = 0$, we are done.
\end{proof}


\subsection{The volume function}
The volume function on $\Def(M,\calT)$ extends naturally to a function
$$\Vol\colon \calA \longrightarrow \matR_{>0}$$
which assigns to each angle structure $\theta$ the sum of the volumes of the ideal hyperbolic realisations of $\Delta_1,\ldots, \Delta_n$ determined by $\theta$. 
Recall from Section \ref{volume:tetrahedra:section} that the volume of $\Delta_i$ is
$$\Vol(\Delta_i) = \Lambda(\theta_i) + \Lambda(\theta_{i+n}) + \Lambda(\theta_{i+2n})$$
where $\Lambda$ is the Lobachevsky function
$$\Lambda(\alpha) = -\int_0^\alpha \log |2\sin t| dt.$$
We therefore get a simple-looking formula
$$\Vol(\theta) = \sum_{j=1}^{3n} \Lambda(\theta_j)$$
which implies immediately the following important fact.

\begin{prop} \label{derivative:Vol:prop}
For every $\theta \in \calA$ and $v\in T_\theta  \calA$ we have 
$$\frac{\partial \Vol}{\partial v} = \sum_{j=1}^{3n} -v_j \log \sin \theta_j, \qquad 
\frac{\partial^2 \Vol}{\partial v^2} < 0.$$
\end{prop}
\begin{proof}
We consider a single addendum $\Lambda(\theta_j)$ of $\Vol(\theta)$. We have
$$\frac{\partial \Lambda(\theta_j)}{\partial v} = 
\Lambda'(\theta_j) \frac{\partial \theta_j}{\partial v}
= - \log |2\sin \theta_j| v_j = -v_j\log 2 - v_j\log\sin \theta_j. $$
Since $v\in T_\theta \calA$ we have $v_i+v_{i+n}+v_{i+2n}=0$ for all $i$ and hence $\sum_j v_j\sin 2=0$. This proves the first equality. To estimate the second derivative, we may suppose up to symmetries that $\theta_i, \theta_{i+n} < \frac \pi 2$ and we get
\begin{align*}
-\frac {\partial^2 \Vol(\Delta_i)}{\partial v^2} 
& = v_i^2 \cot \theta_i + v_{i+n}^2 \cot \theta_{i+n} + v_{i+2n}^2 \cot \theta_{i+2n} \\
& = v_i^2 \cot \theta_i + v_{i+n}^2 \cot \theta_{i+n} + 
(v_i+v_{i+n})^2 \frac{1-\cot \theta_i\cot\theta_{i+n}}{\cot \theta_i + \cot \theta_{i+n}} \\
& = \frac{(v_i+v_{i+n})^2 + (v_i\cot\theta_i - v_{i+n}\cot\theta_{i+n})^2}
{\cot \theta_i + \cot \theta_{i+n}} > 0.
\end{align*}
Indeed the denominator is positive since $\theta_i, \theta_{i+n} < \frac \pi 2$, and if the numerator is zero we get $v_i=-v_{i+n}$ and hence $\cot \theta_i = -\cot \theta_{i+n}$, a contradiction.
\end{proof}

We have discovered that $\Vol$ is a smooth strictly concave function on $\calA$. 


\subsection{The complete solution}
We now remember that $\Def(M,\calT)$ contains a complete solution $z^0$ by assumption.

\begin{prop} \label{Vol:maximum:prop}
The function $\Vol\colon \calA \to \matR_{>0}$ has a unique global maximum at the complete solution $z^0$.
\end{prop}
\begin{proof}
The complete solution $z^0$ has an angle structure $\theta$. Proposition \ref{derivative:Vol:prop} says that
$$\frac{\partial \Vol}{\partial v} = \sum_{j=1}^{3n} -v_j \log \sin \theta_j$$
for all $v\in T_{\theta}\calA$. At every edge $e_i$, the consistency equation is of type $\sum_j \log w_j = 2\pi i$ where $w_1,\ldots, w_k$ are the moduli of the incident tetrahedra. The imaginary part of this equation is satisfied at every point of $\calA$, so we look at the real part and using (\ref{theta:z:eqn}) we discover that 
$$0 = \Re \sum_j \log w_j = \sum_j \log |w_j| = \sum_j \big(\log \sin \alpha_{j}^1 - \log \sin \alpha_j^2\big) $$
where $\alpha_j^1$ and $\alpha_j^2$ are the other two angles in the tetrahedron with modulus $w_j$, in counterclockwise order. The latter expression is in fact equivalent to 
$$-\sum_{j=1}^{3n} (A_{n+i}^*)_j\log\sin \theta_j = \frac{\partial \Vol}{\partial A_{n+i}^*}$$
which is hence zero for all $i=1,\ldots, n$.

We make some analogous considerations for the completeness equations. Since $z^0$ is complete, for every simplicial boundary curve $\gamma$ we have $\sum_j \log w_j = |\gamma|\pi i$ where $w_1,\ldots, w_k$ are the moduli encountered by $\gamma$ at its right, and the real part of this equation implies that $\frac{\partial \Vol}{\partial v_\gamma^*} = 0$.

Proposition \ref{redundant:generators:prop} shows that vectors of type $A_{n+i}^*$ and $v_\gamma^*$ generate $T_{\theta}\calA$, hence the gradient of $\Vol$ vanishes at $\theta$. Since $\Vol$ is strictly concave, this critical point is the unique global maximum.
\end{proof}

\begin{cor}
The space $\Def(M,\calT)$ contains at most one complete solution.
\end{cor}


\subsection{Volumes and Dehn filling}
We can now prove Theorem \ref{vol:vol:teo} on manifolds having a geometric ideal triangulation. We start with a ``local'' version which also considers generalised Dehn fillings, see Section \ref{generalised:subsection}.

\begin{lemma} \label{U:lemma}
If $M$ has a geometric ideal triangulation, there is a neighbourhood $U$ of $(\infty,\ldots, \infty)$ such that $\Vol(M^{\rm fill})< \Vol(M)$ for every non-trivial generalised Dehn filling parameter $s\in U$. Moreover $\Vol(M^{\rm fill}) \nearrow \Vol(M)$ as $s$ tends to $(\infty, \ldots, \infty)$.
\end{lemma}
\begin{proof}
The Dehn Filling Theorem \ref{DF:teo} says that all Dehn fillings in an open neighbourhood $U$ of $(\infty,\ldots,\infty)$ are hyperbolic and constructed by completing solutions in $\Def(M,\calT)$, and they have smaller volume than $M$ in virtue of Proposition \ref{Vol:maximum:prop}. (The completion adds a circle to $M$ which does not contribute to the volume.)

The volume of $M^{\rm fill}$ depends smoothly on $s\in U$ and has a global maximum at $(\infty,\ldots,\infty)$. In particular, when $s\to (\infty, \ldots, \infty)$ we get $\Vol(M^{\rm fill}) \to \Vol(M)$ from below.
\end{proof}

We now need to drop the open set $U$ and prove that volume decreases under \emph{any} Dehn filling of $M$. 

\begin{lemma} \label{strict:everywhere:lemma}
Let $M$ have a geometric ideal triangulation. If a non-trivial Dehn filling $M^{\rm fill}$ admits a complete finite-volume hyperbolic metric, then $\Vol(M^{\rm fill}) < \Vol(M)$.
\end{lemma}
\begin{proof}
Let $s=(s_1,\ldots, s_c)$ be the Dehn filling parameter giving $M^{\rm fill}$ and let
$U$ be the open neighbourhood of $(\infty,\ldots, \infty)$ furnished by Lemma \ref{U:lemma}. For sufficiently big integer $k>0$ we have $ks \in U$ and hence $M^{\rm fill}$ also admits a hyperbolic metric with cone angles $\frac{2\pi}k$ on the core geodesics of the filling solid tori, with volume strictly smaller than $\Vol(M)$. We may interpret this metric as a hyperbolic orbifold $O$, and we have $\Vol(O)<\Vol(M)$.

If $M^{\rm fill}$ is closed Proposition \ref{Vol:M:O:prop} gives $\Vol(M) > \Vol(O) \geqslant v_3\|M^{\rm fill}\| = \Vol(M^{\rm fill})$ and we are done.

If $M^{\rm fill}$ is not closed, we can find some closed fillings of $M^{\rm fill}$ with volume arbitrarily close to $\Vol(O)$ that can be interpreted as orbifolds, and get $\Vol(O)\geqslant \Vol(M^{\rm fill})$ as a limit.
\end{proof}

The proof of Lemma \ref{strict:everywhere:lemma} shows also the following.
\begin{lemma} \label{closed:decreases:lemma}
Let $M$ have a geometric ideal triangulation. We have $v_3\|M^{\rm fill}\| < \Vol(M)$ for every closed Dehn filling $M^{\rm fill}$ of $M$.
\end{lemma}

We prove a lemma that will be useful below.
\begin{lemma} 
Let $M$ have a geometric ideal triangulation. If $M_i$ is a hyperbolic Dehn filling of $M$ with parameter $s^i$ and $\Vol(M_i) \to \Vol(M)$, then $s^i \to (\infty,\ldots, \infty)$.
\end{lemma}
\begin{proof}
We may suppose that the $M_i$ are closed, since every sequence of Dehn fillings can be approximated by a sequence of closed ones. If $s^i$ lies definitely in the open set $U$ furnished by Theorem \ref{DF:teo}, the assertion follows because the volume function there has $\Vol(M)$ as a unique maximum (thanks to Proposition \ref{Vol:maximum:prop}). 

Otherwise, there is a fixed big $k\in\matN$ such that $ks^i\in U$ for all $i$, but $ks^i$ does not converge to $(\infty,\ldots, \infty)$. Therefore $M_i$ admits a hyperbolic orbifold structure $O_i$ with $\Vol(M) - \varepsilon > \Vol(O_i) $ and Proposition \ref{Vol:M:O:prop} gives $\Vol(M) -\varepsilon > \Vol(O) \geqslant v_3\|M_i\| = \Vol(M_i)$ for all $i$. 
\end{proof}

Again, the proof shows also the following.
\begin{lemma} \label{sse:converge:lemma}
Let $M$ have a geometric ideal triangulation. If $M_i$ is a closed Dehn filling of $M$ with parameter $s^i$ and $v_3\|M_i\| \to \Vol(M)$, then $s^i \to (\infty, \ldots, \infty)$.
\end{lemma}

To conclude the proof of Theorem \ref{vol:vol:teo} we only need to consider the unlucky case where $M$ has no geodesic ideal triangulations. We prove that geometric triangulations exist on some finite cover of $M$, and this will suffice.


\subsection{Geometric triangulations exist virtually}
We prove here the following.

\begin{teo}
Every cusped complete finite-volume three-manifold $M$ has a finite-sheeted cover $\tilde M$ that has a geometric ideal triangulation $\calT$.
\end{teo}
\begin{proof}
The Epstein-Penner decomposition subdivides $M$ into ideal polyhedra $P_1,\ldots, P_k$. If distinct vertices of $P_i$ lie in distinct cusps of $M$ for all $i$, then the decomposition can be easily subdivided into an ideal triangulation: we order the cusps, so the vertices of each $P_i$ inherit an ordering which is preserved along the matching faces; we subdivide each $P_i$ as in the proof of Proposition \ref{poly:tetra:prop} by coning on the smallest vertex at each step: the triangulations on the paired faces match and we get a geometric ideal triangulation for $M$ itself.

We now show that some cover $\tilde M$ has a decomposition of this type. The decomposition of $M$ into $P_1,\ldots, P_k$ lifts in any degree-$d$ cover $\tilde M$ to a decomposition of $\tilde M$ into $P_1^i, \ldots, P_k^i$ with $i=1,\ldots, d$. We now prove that there is a $\tilde M$ such that distinct vertices of $P_j^i$ lie in distinct cusps, for all $i,j$.

To do so, we prove that for every pair of vertices $v \neq v'$ of some $P_i$ there is a covering where the lifts $\tilde v, \tilde v'$ in $P_i^j$ for some $j$ lie in distinct cusps. This is enough to conclude: pick a \emph{regular} covering $\tilde M$ that covers all these finitely many coverings; since its desk transformation group acts transitively on lifts, all distinct vertices on every $P_i^j$ lie in distinct cusps.

We have $M=\matH^3/_\Gamma$. We fix an arbitrary lift $\tilde P_i \subset \matH^3$ of $P_i$. Two vertices $v \neq v'$ of $P_i$ lie in the same cusp $T$ $\Leftrightarrow$ there is a $\gamma \in \Gamma$ such that $\gamma(\tilde v) = \tilde v'$, where $\tilde v, \tilde v' \in \tilde P_i$ are the lifts of $v,v'$.
The subgroup $\Stab_\Gamma(\tilde v) = \pi_1(T)$ is separable by Corollary \ref{separable:cor} and hence there is a finite-index $H< \Gamma$ that contains $\Stab_\Gamma(\tilde v)$ but avoids $\gamma$. 

No element $\varphi\in H$ is such that $\varphi(\tilde v) = \tilde v'$, otherwise we would have $\gamma^{-1}\varphi \in \Stab_\Gamma(v) < H$ and hence $\gamma \in H$, a contradiction. We have constructed a finite-cover $\matH^3/_H$ where in some lift $P_i^j$ of $P_i$ the two lifted vertices $\tilde v,\tilde v'$ lie in distinct cusps.
\end{proof}


\subsection{Conclusion of the proof}
We can finally prove Theorem \ref{vol:vol:teo}.

\dimo{vol:vol:teo}
Some degree-$d$ cover $\tilde M$ of $M$ has an ideal geometric triangulation, hence the theorem holds for $\tilde M$. 

For every Dehn filling $M^{\rm fill}$ of $M$, there is a Dehn filling $\tilde M^{\rm fill}$ of $\tilde M$ such that the cover $\tilde M \to M$ extends to a degree-$d$ map $\tilde M^{\rm fill} \to M^{\rm fill}$. 

If $M^{\rm fill}$ is closed hyperbolic, we have 
$$d\Vol(M) =\Vol(\tilde M) > v_3\| (\tilde M^{\rm fill})\|  \geqslant dv_3\|M^{\rm fill}\| =d\Vol(M^{\rm fill}) $$
using Lemma \ref{closed:decreases:lemma}, hence $\Vol(M) > \Vol(M^{\rm fill})$. 

If $M^{\rm fill}$ is cusped hyperbolic, it can be approximated by closed hyperbolic fillings $M^{\rm fill}_i$, and there are closed fillings $\tilde M^{\rm fill}_i$ of $\tilde M^{\rm fill}$ with degree-$d$ maps $\tilde M^{\rm fill}_i \to M^{\rm fill}_i$.
By Lemma \ref{sse:converge:lemma} there is an $\varepsilon > 0$ such that 
$$\Vol(\tilde M) - \varepsilon > v_3\|\tilde M^{\rm fill}_i\| \geqslant d v_3\|M^{\rm fill}_i\| = d\Vol(M^{\rm fill}_i)$$
for all $i$, hence $d\Vol(M) - \varepsilon = \Vol(\tilde M) - \varepsilon \geqslant d\Vol(M^{\rm fill})$. 
\finedimo


\subsection{Bounded volume}
How many hyperbolic manifolds are there with bounded volume? In general, infinitely many. 

We have just discovered that there are infinitely many hyperbolic manifolds with volume smaller than $2v_3 = 2.0298832128 \ldots$ because the figure-eight knot complement $M$ has $\Vol(M) = 2v_3$ and every hyperbolic Dehn filling of $M$ has volume smaller than $\Vol(M)$. Moreover, the volumes of the Dehn fillings of $M$ form an indiscrete set that tends to $2v_3$ from below.

Theorem \ref{vol:vol:teo} shows that this is the typical situation: the hyperbolic Dehn filling produces infinite sequences of manifolds with bounded volume. Despite this variety of manifolds, we can still control topologically the hyperbolic manifolds having bounded volume, at least in principle.

\begin{teo} \label{V:teo}
For every $V>0$ there is a compact 3-manifold $N$ bounded by tori, such that every complete finite-volume orientable hyperbolic 3-manifold $M$ with $\Vol(M)<V$ is diffeomorphic to the interior of some Dehn filling of $N$.
\end{teo}
\begin{proof}
This is a consequence of the thick-thin decomposition. Let $\varepsilon>0$ be a fixed Margulis constant: every complete finite-volume $M$ decomposes along disjoint embedded tori as $M=M^{\rm thick} \cup M^{\rm thin}$ where $M^{\rm thick}$ is compact and has injectivity radius $>\varepsilon$, and $M^{\rm thin}$ consists of truncated cusps and tube neighbourhoods of short geodesics. In particular $M$ is a Dehn filling of $M^{\rm thick}$.

We now show that there are only finitely many possible diffeomorphism types for $M^{\rm thick}$ with volume $<V$. This concludes the proof: by Proposition \ref{LW:bordo:prop}
every such diffeomorphism type is realised from a link $L\cup C\subset S^3$ by surgerying along $L$ and drilling along $C$; we take a disjoint union of all these links in $S^3$, and the complement of the resulting link in $S^3$ is our $N$.

Let $X\subset M^{\rm thick}$ be a \emph{maximal $\frac{\varepsilon}2$-net}, that is a finite set of points that stay at pairwise distance $\geqslant \frac{\varepsilon}2$, such that every other point in $M^{\rm thick}$ stays at distance $< \frac {\varepsilon}2$ from $X$ ($X$ exists because $M^{\rm thick}$ is compact). The $\frac{\varepsilon}4$-balls centred at the points in $X$ are embedded and disjoint: hence $X$ has cardinality at most $C(V) = V/\Vol\big(B(x, \frac{\varepsilon}4)\big)$.

The set $X$ determines a cellularisation of $M^{\rm thick}$ as follows. Lift $X$ to $\tilde X\subset \matH^3$, take the Voronoi tessellation (see Section \ref{Voronoi:subsection}) determined by $\tilde X$ and project it back to $M$: this furnishes a subdivision of $M^{\rm thick}$ into polyhedra. Since $X$ is maximal, every polyhedron has at most $C'(\varepsilon)$ faces with $C'$ depending only on $\varepsilon$. Hence there are finitely many combinatorial types of polyhedra, depending only on $\varepsilon$. With at most $C(V)$ of them we obtain only finitely many manifolds. (The proof of Proposition \ref{X:triangulation:prop} applies to polyhedra and shows that the combinatorial subdivision determines the smooth manifold.)
\end{proof}


\subsection{Volumes of hyperbolic three-manifolds}
We finish this chapter by furnishing some qualitative information on the set of volumes of hyperbolic three-manifolds. We start with the following.

\begin{prop}
Let $M_i$ be a sequence of pairwise non-diffeomorphic complete orientable hyperbolic three-manifolds of uniformly bounded volume. After passing to a subsequence, we may suppose that there is a hyperbolic manifold $M$ such that each $M_i$ is a Dehn filling of $M$ with parameter $s^i\to (\infty, \ldots, \infty)$ . 
\end{prop}
\begin{proof}[Proof using geometrisation]
We know from Theorem \ref{V:teo} that there is a manifold $N$ such that each $M_i$ is a Dehn filling of $N$ with parameter $s^i$. After passing to a subsequence, we may suppose that at each boundary torus $T_j$ of $N$ the slope $s^i_j$ is either constant or goes to infinity. Let $M$ be obtained from $N$ by Dehn filling the slopes that stay constant.

If $M$ is hyperbolic, we are done. Unfortunately, this may not be the case, and we use geometrisation to solve this annoying possibility (the original proof of J\o rgensen and Thurston \cite{Th} does not need geometrisation and follows from a discussion on the geometric convergence of hyperbolic manifolds: we employ geometrisation only for simplicity). If $M$ is not prime, it contains some essential spheres that always bound balls in the filled $M_i$ and hence we may cut $M$ along them and cup off with balls (reducing the components of $\partial M$). Now $M$ is prime and its geometric decomposition must contain some hyperbolic block, otherwise $M$ would be a graph manifold and no Dehn filling of $M$ would be hyperbolic (it would be a graph manifold again). The tori of the decomposition of $M$ become compressible in $M_i$, so up to passing to a subsequence we may suppose that each $M_i$ is a Dehn filling of one fixed hyperbolic block of $M$. If $s_i$ does not tend to $(\infty, \ldots, \infty)$ in this new setting, we restart from the beginning and proceed by induction on the number of boundary components of $M$.
\end{proof}

\begin{cor}
The set of volumes of all complete orientable hyperbolic three-manifolds is well-ordered. For every value $V$ there are only finitely many such manifolds with volume $V$.
\end{cor}
\begin{proof}
Suppose that there is a sequence of manifolds $M_i$ with $\Vol(M_1) > \Vol (M_2) > \ldots $ By the previous proposition these are all obtained by Dehn filling the same hyperbolic $M$ with $s^i \to (\infty,\ldots,\infty)$, and Theorem \ref{vol:vol:teo} says they should converge to $\Vol(M)$ from below, a contradiction. The same argument show that there are finitely many manifolds of any fixed volume.
\end{proof}

We deduce that the volumes of all the complete orientable hyperbolic three-manifolds are indexed by countable ordinals. The volumes $v_1< v_2< \ldots, $ of the smallest closed manifolds converge to the volume $v_\omega$ of the smallest 1-cusped manifold; the volumes $v_\omega < v_{2\omega} < \ldots$ of the smallest 1-cusped manifolds converge to the volume $v_{\omega^2}$ of the smallest 2-cusped manifold, and so on. The set of all volumes has order type $\omega^\omega$, see Figure \ref{ordinal:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {Omega-exp-omega-labeled} 
\nota{The volumes of all the complete orientable hyperbolic three-manifolds form a well-ordered subset of $\matR$ of type $\omega^\omega$.}
\label{ordinal:fig}
\end{center}
\end{figure}

We can also deduce the following.

\begin{cor}
For every $V>0$ and $R>0$ there are only finite many closed hyperbolic three-manifolds $M$ with $\Vol(M)<V$ and $\inj(M)>R$.
\end{cor}
\begin{proof}
On a sequence of closed hyperbolic three-manifolds with bounded volume, the length of some core geodesic tends to zero.
\end{proof}



\subsection{References}
To furnish a complete proof of Thurston's Dehn filling Theorem we have patched together a number of different sources. The most relevant ones are as usual Thurston's notes \cite{Th}, Benedetti -- Petronio \cite{BP}, and Ratcliffe \cite{R}, together with Neumann -- Zagier \cite{NZ}. 

Some arguments have been updated here in light of some new results that were discovered more recently by some authors. The list of non-exceptional slopes for the figure-eight knot and the Whitehead link can be found in Martelli -- Petronio \cite{MP}. The smoothness of the deformation space stated in Corollary \ref{smooth:cor} has been proved by Choi \cite{Ch} in 2004. Many of the arguments of this chapter, including all the discussion on angle structures, have been taken from a nice paper of Futer -- Gu\'eritaud \cite{FG}. The first complete proof of Thurson's Dehn filling Theorem, that takes care of the annoying case of triangulations with flat tetrahedra, is due to Petronio -- Porti \cite{PP}. We diverge from that proof in the last arguments, where we extend Choi's smoothness theorem to this partially flat context in Proposition \ref{smooth:flat:prop} (this proposition is probably the only original result of this book). The virtual existence of geometric triangulations was proved by Luo -- Schleimer -- Tillmann \cite{LST} in 2008.
