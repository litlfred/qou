---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-014-24-geometry-of-hyperbolic-space
section_title: "Geometry of hyperbolic space"
section_number: 2.4
pages: 76-81
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.804
latex_coverage_ratio: 0.971
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We study the geometry of $\matH^n$. We prove that $\matH^n$ has constant sectional curvature $-1$, that the distance function along lines is convex, we define convex combinations and barycenters, and study parallel transport along lines. Finally, we prove that $\Iso(\matH^n)$ is a unimodular Lie group.


\subsection{Area and curvature}
We can verify that $\matH^n$ has constant sectional curvature $-1$. It should be no surprise that $\matH^n$ has constant curvature, since it has many symmetries (\emph{i.e.}~isometries). To calculate its sectional curvature we compute the area of a disc. 

\begin{prop}
The disc of radius $r$ in $\matH^2$ has area 
$$A(r) = \pi \left(e^{\frac r2} -e ^{-\frac r2}\right)^2 =  4\pi \sinh^2 {\tfrac r2} = 2\pi (\cosh r -1).$$
\end{prop}
\begin{proof}
Recall that the volume form is
$$\omega = \sqrt{\det g} \cdot dx_1\cdots dx_n.$$
Let $D(r)$ be a disc in $\matH^2$ of radius $r$. If we centre it in $0$ in the disc model, its Euclidean radius is $\tanh \frac r2$ by Corollary \ref{exp:cor} and we get
\begin{align*}
A(r) & = \int_{D(r)} \sqrt{\det g} \cdot dxdy = \int_{D(r)} \left(\frac 2{1-x^2-y^2}\right)^2dxdy \\
 & = \int_0^{2\pi} \int_0^{\tanh\frac r2} \left(\frac {2}{1-\rho^2}\right)^2 \rho \cdot d\rho d\theta = 2\pi\left[ \frac 2{1-\rho^2}\right]_0^{\tanh \frac r2} \\
 & = 4\pi \left(\frac 1{1-{\tanh^2 \frac r2}} - 1 \right) = 4\pi \sinh^2 \tfrac r2.
\end{align*}
The proof is complete.
\end{proof}

\begin{cor}
The hyperbolic space $\matH^n$ has sectional curvature $-1$.
\end{cor}
\begin{proof}
Pick $p\in \matH^n$ and $W\subset T_p$ a 2-dimensional subspace. The image $\exp_p(W)$ is the hyperbolic plane tangent to $W$ in $p$. On a hyperbolic plane 
$$A(r) = 2\pi(\cosh r - 1) = 2\pi \left(\frac {r^2}{2!} + \frac {r^4}{4!} + o(r^4)\right) = \pi r^2 + \frac{\pi r^4}{12} + o(r^4)$$
and hence $K=-1$ following the area formula in Section \ref{gauss:subsection}.
\end{proof}


\subsection{Convexity of the distance function}
We recall that a function $f\colon \matR^n \to \matR$ is \emph{strictly convex} if 
$$f(tv+(1-t)w)< tf(v) + (1-t)f(w)$$
for any pair $v,w \in \matR^n$ of distinct points and any $t\in (0,1)$. 
\begin{ex} A positive strictly convex function is continuous and admits a minimum if and only if it is proper.
\end{ex}

We now prove that the distance function is strictly convex on disjoint lines of $\matH^n$. Given two lines $l, l'\subset \matH^n$, we fix an isometry of each line with $\matR$ and we get an identification of $l\times l'$ with the Euclidean plane $\matR\times\matR$.\index{convexity of the distance function}

\begin{figure}
\begin{center}
\includegraphics[width = 9cm] {\iftoggle{BW}{convex-BW}{convex}}
\nota{Distance between points in disjoint lines is a strictly convex function in hyperbolic space.}
\label{convex:fig}
\end{center}
\end{figure}

\begin{prop} \label{distanza:convessa:prop}
Let $l,l'\subset \matH^n$ be two disjoint lines. The map
\begin{align*}
l \times l' & \longrightarrow \matR_{\geqslant 0} \\
(x,y) & \longmapsto d(x, y)
\end{align*}
is strictly convex; it is proper if and only if the lines are ultraparallel. 
\end{prop}
\begin{proof}
With our identifications we have $(x,y) \in \matR \times \matR$. The function $d$ is clearly continuous, hence to prove its convexity it suffices to show that  
$$d\left(\frac{x_1+x_2}2, \frac{y_1+y_2}2\right) < \frac{d(x_1,y_1) + d(x_2,y_2)}2$$
for any pair of distinct points $(x_1,y_1), (x_2,y_2) \in l\times l'$. Suppose $x_1\neq x_2$ and denote by $m$ and $n$ the midpoints $\frac{x_1+x_2}2$ and $\frac{y_1+y_2}2$ as in Figure \ref{convex:fig}. 

Let $\sigma_p$ be the reflection at the point $p\in\matH^n$. The isometry $\tau = \sigma_n\circ \sigma_m$ translates the line $r$ containing the segment $mn$ by the quantity $2d(m,n)$: hence it is a hyperbolic transformation with axis $r$. We draw the points  $o = \tau(m)$ and $z_i = \tau(x_i)$ in the figure and note that $z_1 = \sigma_n(x_2)$, hence $d(x_2,y_2) = d(z_1,y_1)$. The triangular inequality implies that
$$d(x_1, z_1) \leqslant d(x_1,y_1) + d(y_1, z_1) = d(x_1,y_1) + d(x_2, y_2).$$
A hyperbolic transformation has minimum displacement on its axis $r$ and $x_1 \neq m$ is not in $r$, hence
$$2d(m,n) = d(m,o) = d(m,\tau(m)) < d(x_1, \tau(x_1)) = d(x_1,z_1).$$
Finally we get $2d(m,n) <  d(x_1,y_1) + d(x_2, y_2)$ and hence $d$ is convex. 

The function $d$ is proper, that is it has minimum, if and only if the two lines are ultraparallel by Proposition \ref{sottospazi:prop}.
\end{proof}

\begin{ex}
The distance function on parallel lines in $\matR^n$ is not strictly convex (it is only convex).
\end{ex}


\subsection{Convex combinations} \label{convex:subsection}
Let $p_1,\ldots, p_k$ be $k$ points in $\matH^n, \matR^n$, or $S^n$ and $t_1,\ldots, t_k$ be non-negative numbers with $t_1+\ldots + t_k=1$. The \emph{convex combination}  \index{convex combination} 
$$p = t_1p_1+ \ldots + t_kp_k$$ 
is another point in the space defined as follows:
\begin{align*}
{\rm in\ } \matR^n: \quad p & =  t_1p_1+ \ldots + t_kp_k \\
{\rm in\ } I^n,S^n: \quad p & = \frac{t_1p_1+ \ldots + t_kp_k}{\| t_1p_1+ \ldots + t_kp_k\|} 
\end{align*}
where $\|v\| = \sqrt{-\langle v, v \rangle}$ on $I^n$. Using convex combination we may define the \emph{barycenter} of the points as $\frac 1k p_1 + \ldots + \frac 1k p_k$. The barycenter may in turn be used to prove the following.
\index{barycenter}

\begin{prop} \label{iterate:prop}
Let $\varphi\colon \matH^n \to \matH^n$ be a non-trivial isometry and $k\geqslant 2$:
\begin{itemize}
\item if $\varphi$ is elliptic then $\varphi^k$ is elliptic or trivial; 
\item if $\varphi$ is parabolic then $\varphi^k$ is parabolic;
\item if $\varphi$ is hyperbolic then $\varphi^k$ is hyperbolic.
\end{itemize}
\end{prop}
\begin{proof}
If $\varphi\colon \matH^n \to\matH^n$ is an isometry with no fixed points, then $\varphi^k$ also is: if $\varphi^k(x)=x$ then $\varphi$ fixes the finite set $\{x, \varphi(x), \ldots, \varphi^{k-1}(x)\}$ and hence also its barycenter.

If $\varphi$ is parabolic then it fixes the horospheres centred at some point $p\in\partial\matH^n$ and also $\varphi^k$ does, hence it is still parabolic (it cannot be hyperbolic). If $\varphi$ is hyperbolic it has two fixed points at infinity, and $\varphi^k$ too.
\end{proof}

\begin{prop} \label{finite:fixed:prop}
Every finite group $\Gamma<\Iso(\matH^n)$ fixes a point in $\matH^n$.
\end{prop}
\begin{proof}
The barycenter of any orbit is fixed by $\Gamma$.
\end{proof}


\subsection{Parallel transport} \label{parallel:subsection}
On Riemannian manifolds, the parallel transport is a way to slide frames along geodesics. On $\matH^n$ we can do this simply as follows: for every geodesic $\gamma$, we put $\gamma$ into vertical position in the half-space model $H^n$, and slide the frames vertically in the obvious way.  \index{parallel transport}

This construction furnishes in particular, for every pair $x,y \in \matH^n$ of points, a canonical isometry between $T_x\matH^n$ and $T_y\matH^n$, obtained by sliding frames along the unique geodesic $\gamma$ containing $x$ and $y$.

This canonical identification is of course not transitive on a triple of non-collinear points $x,y,z$: the curvature of $\matH^n$ is responsible for that.


\subsection{Unimodularity}
The following is a consequence of Corollary \ref{O:unimodular:cor}.

\begin{cor} \label{unimodular:cor}
The isometry group $\Isomet(\matH^n)$ is unimodular.
\end{cor}

\begin{oss} \label{Haar:oss}
A Haar measure for $\Iso(\matH^n)$ may be constructed concretely as follows: fix a point $x\in \matH^n$ and define the measure of a Borel set $S\subset \Iso(\matH^n)$ as the measure of $S(x) = \cup_{\varphi\in S} \varphi(x)\subset\matH^n$. This measure is obviously left-invariant, and is hence also right-invariant since $\Iso(\matH^n)$ is unimodular. As a consequence, it does not depend on the choice of $x$.
\end{oss}


\subsection{References}
The hyperbolic space is introduced in various books: two standard references are Benedetti -- Petronio \cite{BP} and Ratcliffe \cite{R}, and most of the arguments presented here were borrowed from these two sources. The proof of Proposition \ref{distanza:convessa:prop} was taken from Farb -- Margalit \cite{FM}.
Thurston's notes contain some useful trigonometric formulae that we have omitted, see \cite[Chapter 2]{Th}.


\chapter{Hyperbolic manifolds} \label{varieta:chapter} \label{manifold:chapter} 
 \label{orbifold:chapter} \label{orbifolds:chapter}

A hyperbolic manifold is a Riemannian manifold locally isometric to the hyperbolic space $\matH^n$. Maybe the most striking aspect of geometric topology is that, despite this quite restrictive definition, there are plenty of hyperbolic manifolds around, especially in the dimensions $n=2$ and $3$. For that reason hyperbolic manifolds (and hence hyperbolic geometry) play a central role in the topology of surfaces and three-manifolds.

The study of complete hyperbolic manifolds is tightly connected to that of discrete subgroups in the Lie group $\Iso(\matH^n)$ and of polyhedra in $\matH^n$, so it has both an algebraic and geometric flavour. We start this chapter by describing these connections; then we show some examples and discuss some important variations: non-complete hyperbolic manifolds, hyperbolic manifolds with geodesic boundary, cone manifolds, and orbifolds.
