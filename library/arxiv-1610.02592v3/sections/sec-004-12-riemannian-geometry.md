---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-004-12-riemannian-geometry
section_title: "Riemannian geometry"
section_number: 1.2
pages: 23-31
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.965
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We briefly introduce Riemannian manifolds and their geometric properties: distance, geodesics, volume, exponential map, injectivity radius, completeness, curvature, and isometries. These notions are carefully explained in do Carmo's \emph{Riemannian Geometry} \cite{Do}.


\subsection{Metric tensor}
A differentiable manifold lacks many natural geometric notions, such as distance between points, angle between vectors, path lengths, geodesics, volumes, etc. It is a quite remarkable fact that the introduction of a single additional mathematical entity suffices to recover all these geometric notions: this miraculous object is the metric tensor.

A \emph{metric tensor} for a differentiable manifold $M$ is the datum of a scalar product on each tangent space $T_p$ of $M$, which varies smoothly on $p$. More specifically, on a chart the scalar product may be expressed as a matrix, and we require that its coefficients vary smoothly on $p$.
\index{metric tensor}

\begin{defn}
A \emph{Riemannian manifold} is a differentiable manifold with a metric tensor that is positive definite at every point.
\end{defn}
\index{manifold!Riemannian manifold}

A Riemannian manifold is usually denoted as a pair $(M,g)$, where $M$ is the manifold and $g$ is the metric tensor. 

\begin{example}
The \emph{Euclidean space} is the manifold $\matR^n$ equipped with the Euclidean metric tensor $g(x,y) = \sum_{i=1}^n x_iy_i$ at every tangent space $T_p = \matR^n$.
\end{example}

\begin{example}
Every differential submanifold $N$ in a Riemannian manifold $M$ is also Riemannian: it suffices to restrict at every $p\in N$ the metric tensor on $T_pM$ to the linear subspace $T_pN$.

In particular, the \emph{sphere} 
$$S^n = \big\{x\in \matR^{n+1}\ \big| \ \|x\| = 1 \big\}$$
is a submanifold of $\matR^{n+1}$ and is hence Riemannian.
\end{example}
\index{sphere}

The metric tensor $g$ defines in particular a norm for every tangent vector, and an angle between tangent vectors with the same basepoint. The velocity $\gamma'(t)$ of a curve $\gamma \colon I \to M$ at time $t\in I$ now has a norm $\|\gamma'(t)\|\geqslant 0$ called \emph{speed}, and two curves that meet at a point with non-zero velocities form a well-defined angle. The \emph{length} of $\gamma$ may be defined as
$$L(\gamma) = \int_I \|\gamma'(t)\| dt$$
and can be finite or infinite. A \emph{reparametrisation} of $\gamma$ is the curve $\eta \colon J \to M$ obtained as $\eta = \gamma\circ\varphi$ where $\varphi\colon J\to I$ is a diffeomorphism of intervals. The length is invariant under reparametrisations, that is $L(\gamma) = L(\eta)$.


\subsection{Distance and geodesics}
Let $(M,g)$ be a connected Riemannian manifold. The curves in $M$ now have a length and hence may be used to define a distance on $M$. 

\begin{defn}
The \emph{distance} $d(p,q)$ between two points $p, q\in M$ is 
$$d(p,q) = \inf_\gamma L(\gamma)$$
where $\gamma$ varies among all curves $\gamma\colon [0,1] \to M$ with $\gamma(0)=p$ and $\gamma(1)=q$. 
\end{defn}
The manifold $M$ equipped with the distance $d$ is a metric space (compatible with the initial topology of $M$).

\begin{defn}
A \emph{geodesic} is a curve $\gamma\colon I \to M$ having constant speed $k$ that realises locally the distance. This means that every $t \in I$ has a closed neighbourhood $[t_0,t_1]\subset I$ such that $d(\gamma(t_0), \gamma(t_1)) = L(\gamma|_{[t_0,t_1]}) = k(t_1-t_0)$.
\end{defn}
\index{geodesic}

Note that with this definition the constant curve $\gamma(t) = p_0$ is a geodesic with constant speed $k=0$. Such a geodesic is called \emph{trivial}. A curve that realises the distance locally may not realise it globally. 

\begin{example}
The non-trivial geodesics in Euclidean space $\matR^n$ are affine lines run at constant speed. 
The non-trivial geodesics in the sphere $S^n$ are portions of great circles, run at constant speed. 
\end{example}

A geodesic $\gamma:I \to M$ is \emph{maximal} if it cannot be extended to a geodesic on a strictly larger interval $J \supset I$. Maximal geodesics are determined by some first-order conditions: 

\begin{teo}  \label{geod:teo}
Let $p\in M$ be a point and $v\in T_pM$ a tangent vector. There exists a unique maximal geodesic $\gamma\colon I \to M$ with $\gamma(0) = p$ and $\gamma'(0) = v$. The interval $I$ is open and contains $0$.
\end{teo}


\subsection{Volume}
If the differentiable manifold $M$ is oriented, the metric tensor also induces a \emph{volume form}.
\index{volume form}

The best method to define volumes on a $n$-manifold $M$ is to construct an appropriate \emph{$n$-form}. A $n$-form $\omega$ is an alternating multilinear form
$$\omega_p: \underbrace{T_p \times \ldots \times T_p}_n \longrightarrow \matR$$
at each point $p\in M$, which varies smoothly with $p$. The alternating condition means that if we swap two vectors the result changes by a sign. 
The $n$-forms are designed to be integrated: it makes sense to write 
$$\int_D \omega$$
on any open set $D$. A \emph{volume form} on an oriented manifold $M$ is a $n$-form $\omega$ such that $\omega_p(v_1,\ldots, v_n)> 0$ for every positive basis $v_1,\ldots, v_n$ of $T_p$ and every $p\in M$. 

The metric tensor defines a volume form as follows: it suffices to set $\omega_p(e_1,\ldots, e_n)=1$ on every positive orthonormal basis $e_1,\ldots, e_n$. With this definition every open set $D$ of $M$ has a well-defined \emph{volume} 
$$\Vol(D) = \int_D \omega$$
which is a positive number or infinity. If $D$ has compact closure the volume is necessarily finite; in particular, a compact Riemannian manifold $M$ has finite volume $\Vol (M)$.
\index{volume}

On a chart, the volume form can be calculated from the metric tensor $g$ via the following formula: 
$$\omega = \sqrt{\det g} \cdot dx_1\cdots dx_n.$$


\subsection{Completeness}
A Riemannian manifold $(M,g)$ is a metric space, and as such it may be complete or not. For instance,
a compact Riemannian manifold is always complete; on the other hand, by removing a point from a Riemannian manifold we always get a non-complete space. Non-compact manifolds like $\matR^n$ typically admit both complete and non-complete Riemannian structures. 
The completeness of a Riemannian manifold may be expressed in various ways:

\index{Hopf -- Rinow theorem}
\begin{teo}[Hopf -- Rinow] \label{HR:teo}
Let $(M,g)$ be a connected Riemannian manifold. The following are equivalent: 
\begin{enumerate}
\item $M$ is complete,
\item a subset of $M$ is compact if and only if it is closed and bounded,
\item every geodesic can be extended on the whole $\matR$.
\end{enumerate}
If $M$ is complete, any two points $p,q \in M$ are joined by a \emph{minimising} geodesic $\gamma$, \emph{i.e.}~a curve such that $L(\gamma) = d(p,q)$.
\end{teo}




\subsection{Exponential map} \label{esponenziale:subsection}
Let $M$ be a complete Riemannian manifold. The fact that geodesics are determined by first-order conditions allows us to introduce the following.

\index{exponential map}
\begin{defn}
Let $p \in M$ be a point. The \emph{exponential map}
$$\exp_p\colon T_pM \longrightarrow M$$
is defined as follows.
A vector $v\in T_pM$ determines a maximal geodesic $\gamma_v\colon \matR \to M$ with $\gamma_v(0) = p$ and $\gamma_v'(0) = v$. We set $\exp_p(v) = \gamma_v(1)$.
\end{defn}

\begin{teo} \label{exp:teo}
The differential of the exponential map $\exp_p$ at the origin is the identity and hence $\exp_p$ is a local diffeomorphism at the origin.
\end{teo}

Via the exponential map, a small neighborhood of the origin in  $T_pM$ can be used as a chart near $p$: we recover here the intuitive idea that the tangent space approximates the manifold near $p$.

When $M$ is not complete, the exponential map is only defined in some open star-shaped neighbourhood $V_p \subset T_pM$ of the origin, and Theorem \ref{exp:teo} holds also in this case.


\subsection{Injectivity radius}
Let $M$ be a complete Riemannian manifold. We introduce the following.

\begin{defn} 
The \emph{injectivity radius} $\inj_pM>0$ of $M$ at a point $p\in M$ is the supremum of all $r>0$ such that $\exp_p|_{B_0(r)}$ is a diffeomorphism onto its image.
\end{defn}
\index{injectivity radius}

Here $B_0(r)$ is the open ball with centre $0$ and radius $r$ in the tangent space $T_pM$. The injectivity radius is always positive by Theorem \ref{exp:teo}. For every $r< \inj_pM$ the exponential map transforms the ball of radius $r$ in $T_p(M)$ into the metric ball of radius $r$ in $M$. That is, the following equality holds: 
$$\exp_p(B_0(r)) = B_p(r)$$
and the metric ball $B_p(r)$ is indeed diffeomorphic to an open ball in $\matR^n$. When $r\geq \inj_p M$ this may not be true: for instance if $M$ is compact there is a $R>0$ such that $B_p(R) = M$.

The injectivity radius $\inj_p(M)$ varies continuously with respect to $p\in M$; 
the injectivity radius $\inj (M)$ of $M$ is defined as
$$\inj (M) = \inf_{p\in M} \inj_p M.$$

\begin{prop} \label{iniettivita:prop}
A compact Riemannian manifold has positive injectivity radius.
\end{prop}
\begin{proof}
The injectivity radius $\inj_p M$ is positive and varies continuously with $p$, hence it has a positive minimum on the compact $M$.
\end{proof}

Finally we note the following. A \emph{loop} is a curve $\gamma\colon [a,b] \to M$ with $\gamma(a) = \gamma(b)$.

\begin{prop}
Let $M$ be a complete Riemannian manifold. Every loop $\gamma$ in $M$ shorter than $2\cdot \inj (M)$ is homotopically trivial.
\end{prop}
\begin{proof}
Set $p=\gamma(a) = \gamma (b)$. Since $\gamma$ is shorter than $2\cdot\inj (M)$, it cannot escape the ball $B_p(r)$ for some $r<\inj (M)\leqslant \inj_p M$. This ball is diffeomorphic to a ball in $\matR^n$, hence in particular it is contractible, so $\gamma$ is homotopically trivial.
\end{proof}

A proof of the continuity of $\inj_p(M)$ can be found in \cite{Lee}.


\subsection{Curvature} \label{curvatura:subsection}
The \emph{curvature} of a Riemannian manifold $(M,g)$ is some mathematical entity that measures how distorted $g$ is when compared to the familiar Euclidean structure on $\matR^n$. The curvature is encoded by various kinds of mathematical objects, and some of them may be frustratingly complicated when $n=\dim M \geqslant 3$. Luckily, most of the Riemannian manifolds that we will encounter in this book have ``constant curvature'' and therefore these objects will simplify dramatically. We briefly recall them here.
\index{curvature}

\index{Levi-Civita connection}
\index{Christoffel symbol}
The metric tensor $g$ induces the \emph{Levi-Civita connection} $\nabla$, which can be used to differentiate any vector field with respect to a tangent vector at any point of $M$. We concentrate on an open chart and hence suppose that $M=U$ is an open set of $\matR^n$; let $e_1, \ldots, e_n$ be the coordinate vector fields on $U$ and $\nabla_i$ be the Levi-Civita differentiation with respect to $e_i$. We have
$$\nabla_i e_j = \Gamma^k_{ij} e_k$$
for some smooth functions $\Gamma^k_{ij} \colon U \to \matR$ called the \emph{Chistoffel symbols}. Here we use the Einstein notation: repeated indices should be added from $1$ to $n$. The Christoffel symbols are determined by $g$ via the formula:
$$\Gamma_{ij}^k = \frac{1}{2}g^{k\ell} \left(\frac{\partial g_{\ell i}}{\partial x^j} + \frac{\partial g_{\ell j}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^\ell} \right).$$
Here $g^{k\ell}$ is just the inverse matrix of $g = g_{k\ell}$.
Christoffel symbols are very useful but depend heavily on the chosen chart; a more intrinsic object is the \emph{Riemann tensor} that may be defined (quite obscurely) as
\index{Riemann tensor}
$$R^i{}_{jk\ell} = \partial_k\Gamma^i_{\ell j}
    - \partial_\ell\Gamma^i_{k j}
    + \Gamma^i_{k m}\Gamma^m_{\ell j}
    - \Gamma^i_{\ell m}\Gamma^m_{k j}.$$ 
By contracting two indices we get the \emph{Ricci tensor} \index{Ricci tensor}
$$R_{ij} = {R^k}_{ik j} =
\partial_{k}{\Gamma^k_{ji}} - \partial_{j}\Gamma^k_{k i}
+ \Gamma^k_{km} \Gamma^m_{ji}
- \Gamma^k_{jm}\Gamma^m_{k i}.
$$ 
The Ricci tensor is symmetric, and by further contracting we get the \emph{scalar curvature}
$$R = g^{ij}R_{ij}.$$
\index{scalar curvature}


\subsection{Scalar curvature} \label{gauss:subsection}
What kind of geometric information is contained in the tensors introduced above? The scalar curvature $R$ is the simplest curvature detector, and it measures the local discrepancy between volumes in $M$ and in $\matR^n$. Let $B_p(\varepsilon)\subset M$ be the $\varepsilon$-ball in $M$ centred at $p$ and $B_0(\varepsilon)\subset \matR^n$ be the $\varepsilon$-ball in the Euclidean $\matR^n$. We have
$$\Vol\big(B_p(\varepsilon)\big) = \Vol\big(B_0(\varepsilon)\big) \cdot \left( 1- \frac R{6(n+2)}\varepsilon^2 \right) + {\rm O}(\varepsilon^4).$$
We note in particular that $R$ is positive (negative) if $B_p(\varepsilon)$ has smaller (bigger) volume than the usual Euclidean volume.

If $M$ has dimension 2, that is it is a surface, the Riemann and Ricci tensors simplify dramatically and are fully determined by the scalar curvature $R$, which is in turn equal to twice the \emph{gaussian curvature} $K$: if $M$ is contained in $\matR^3$ the gaussian curvature is defined as the product of its two principal curvatures, but when $M$ is abstract principal curvatures make no sense. On surfaces, the formula above reads as
$$\Area(B_p(\varepsilon)) = \pi\varepsilon^2 - \frac{\pi \varepsilon^4}{12}K + {\rm O}(\varepsilon^4).$$
\index{gaussian curvature}

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{Gaussian_curvature-BW}{640px-Gaussian_curvature}}
\nota{Three surfaces in space (hyperboloid with one sheet, cylinder, sphere) whose gaussian curvature is respectively negative, null, and positive at each point. The curvature on the sphere is constant, while the curvature on the hyperboloid varies: a complete surface in $\matR^3$ cannot have constant negative curvature.}
\label{Gaussian:fig}
\end{center}
\end{figure}


\subsection{Sectional curvature}
If $(M,g)$ has dimension $n\geqslant 3$ the scalar curvature is a weak curvature detector when compared to the Ricci and Riemann tensors. Moreover, there is yet another curvature detector which encodes the same amount of information of the full Riemann tensor, but in a more geometric way: this is the \emph{sectional curvature} and is defined as follows. 
\index{sectional curvature}

\begin{defn}
Let $(M,g)$ be a Riemannian manifold. Let $p \in M$ be a point and $W \subset T_pM$ be a 2-dimensional vector subspace. By Theorem \ref{exp:teo} there exists an open set $U_p \subset T_pM$ containing the origin where $\exp_p$ is a diffeomorphism onto its image. In particular $S = \exp_p(U_p \cap W)$ is a small smooth surface in $M$ passing through $p$, with tangent plane $W$. As a submanifold of $M$, the surface $S$ has a Riemannian structure induced by $g$.

The \emph{sectional curvature} of $(M,g)$ along $W$ is defined as the gaussian curvature of $S$ in $p$.
\end{defn}

We can use the sectional curvature to unveil the geometric nature of the Ricci tensor:
the Ricci tensor $R_{ij}$ in $p$ measures the average sectional curvature along axes, that is for every unit vector $v\in T_p(M)$ the number $R_{ij} v^iv^j$ is $(n-1)$ times the average sectional curvature of the planes $W\subset T_p(M)$ containing $v$.

The Riemann tensor is determined by the sectional curvatures and vice-versa. In dimension $n=3$ the Ricci tensor fully determines the sectional curvatures and hence also the Riemann tensor. This is not true in dimension $n\geqslant 4$.


\subsection{Constant sectional curvature}
A Riemannian manifold $(M,g)$ has \emph{constant sectional curvature} $K$ if the sectional curvature of every 2-dimensional vector space $W\subset T_pM$ at every point $p\in M$ is always $K$.

\begin{oss}
On a Riemannian manifold $(M,g)$ one may \emph{rescale} the metric by some factor $\lambda >0$ substituting $g$ with the tensor $\lambda g$. At every point the scalar product is rescaled by $\lambda$. Consequently, lengths of curves are rescaled by $\sqrt \lambda$ and volumes are rescaled by $\lambda^{\frac n2}$. The sectional curvature is rescaled by $1/\lambda$. 
\end{oss}

By rescaling the metric we may transform every Riemannian manifold with constant sectional curvature $K$ into one with constant sectional curvature $-1$, $0$, or $1$.

\begin{example}
Euclidean space $\matR^n$ has constant curvature zero. A sphere of radius $R$ has constant curvature $1/R^2$.
\end{example}


\subsection{Isometries}
Every honest category has its morphisms. Riemannian manifolds are so rigid, that in fact one typically introduces only isomorphisms: these are called \emph{isometries}.
\index{isometry}

\begin{defn}
A diffeomorphism $f\colon M\to N$ between two Riemannian manifolds $(M,g)$ and $(N,h)$ is an \emph{isometry} if it preserves the scalar product. That is, the equality
$$\langle v,w \rangle = \langle df_p(v), df_p(w) \rangle$$
holds for all $p\in M$ and every pair of vectors $v,w \in T_pM$. The symbols $\langle,\rangle$ indicate the scalar products in $T_pM$ and $T_{f(p)}N$.
\end{defn}

As we said, isometries are extremely rigid. These are determined by their first-order behaviour at any single point.

\begin{teo} \label{isom:teo}
Let $f,g\colon M \to N$ be two isometries between two connected Riemannian manifolds. If there is a point $p\in M$ such that $f(p) = g(p)$ and $df_p = dg_p$, then $f  =g$ everywhere.
\end{teo}
\begin{proof}
Let us show that the subset $S\subset M$ of the points $p$ such that $f(p) = g(p)$ and $df_p = dg_p$ is open and closed.

The locus where two functions coincide is typically closed, and this holds also here (to prove it, take a chart). We prove that it is open: pick $p\in S$. 
By Theorem \ref{exp:teo} there is an open neighbourhood $U_p \subset T_pM$ of the origin where the exponential map is a diffeomorphism onto its image. We show that the open set $\exp_p(U_p)$ is entirely contained in $S$.

A point $q\in\exp_p(U_p)$ is the image $q=\exp(v)$ of a vector $v\in U_p$ and hence $q=\gamma(1)$ for the geodesic $\gamma$ determined by the data $\gamma(0)=p, \gamma'(0)=v$. The maps $f$ and $g$ are isometries and hence send geodesics to geodesics: here $f\circ \gamma$ and $g\circ\gamma$ are geodesics starting from $f(p)=g(p)$ with the same initial velocities and thus they coincide. This implies that $f(q)=g(q)$. Since $f$ and $g$ coincide on the open set $\exp_p(U_p)$, also their differentials do.
\end{proof}



\subsection{Local isometries}
A \emph{local isometry} $f\colon M \to N$ between Riemannian manifolds is a map where every $p\in M$ has an open neighbourhood $U$ such that $f|_U$ is an isometry onto its image. Theorem \ref{isom:teo} applies with the same proof to local isometries.
\index{isometry!local isometry}

The following proposition relates nicely the notions of local isometry, topological covering, and completeness.

\begin{prop} \label{local:isometry:prop}
Let $f\colon M \to N$ be a local isometry.
\begin{enumerate}
\item If $M$ is complete, the map $f$ is a covering.
\item If $f$ is a covering, then $M$ is complete $\Longleftrightarrow$ $N$ is complete.
\end{enumerate}
\end{prop}
\begin{proof}
Since $f$ is a local isometry, every geodesic in $M$ projects to a geodesic in $N$. If $f$ is also a covering, the converse holds: every geodesic in $N$ lifts to a geodesic in $M$ (at any starting point). 

If $f$ is a covering we can thus project and lift geodesics via $f$: therefore every geodesic in $M$ can be extended to $\matR$ if and only if every geodesic in $N$ can; this proves (2) using the Hopf -- Rinow Theorem \ref{HR:teo}.

We prove (1) by showing that the ball $B=B(p,\inj_pN)$ is well-covered for all $p\in N$. Since $M$ is complete, every geodesic in $N$ can be lifted to a geodesic in $M$ (at any starting point).  For every $\tilde p \in f^{-1}(p)$ the map $f$ sends the geodesics exiting from $\tilde p$ to geodesics exiting from $p$ and hence sends isometrically $B(\tilde p, \inj_p N)$ onto $B$. On the other hand, given a point $q\in f^{-1}(B)$, the geodesic in $B$ connecting $f(q)$ to $p$ lifts to a geodesic connecting $q$ to some point $\tilde p \in f^{-1}(p)$. Therefore 
$$f^{-1}\big(B(p,\inj_p N)\big) = \bigsqcup_{\tilde p \in f^{-1}(p)} B(\tilde p, \inj_p N)$$
and $f$ is a covering.
\end{proof}

\begin{prop} \label{volume:covering:prop}
Let $f\colon M \to N$ be a local isometry and a degree-$d$ covering. We have
$$\Vol(M) = d \cdot \Vol (N).$$
\end{prop}
\begin{proof}[Sketch of the proof]
We may find a disjoint union of well-covered open sets in $N$ whose complement has zero measure. Every such open set lifts to $d$ copies of it in $M$, and the zero-measure set lifts to a zero-measure set.
\end{proof}

The formula makes sense also when some of the quantities $\Vol(M)$, $\Vol(N)$, and $d$ are infinite.


\subsection{Totally geodesic submanifolds}
A differentiable submanifold $M$ in a Riemannian manifold $N$ is \emph{totally geodesic} if 
every geodesic in $M$ with the induced metric is also a geodesic in $N$. 
\index{submanifold!totally geodesic submanifold}

When $\dim M=1$ this notion is equivalent to that of an unparametrized embedded geodesic; if $\dim M\geqslant 2$ then $M$ is a quite peculiar object: generic Riemannian manifolds do not contain totally geodesic surfaces at all. An equivalent condition is that, for every $p\in M$ and every $v \in T_p(M)$, the unique geodesic in $N$ passing through $p$ with velocity $v$ stays in $M$ for some interval $(-\varepsilon, \varepsilon)$.


\subsection{Riemannian manifolds with boundary}
Many geometric notions in Riemannian geometry extend easily to manifolds $M$ with boundary. The boundary $\partial M$ of a Riemannian manifold $M$ is naturally a Riemannian manifold without boundary. 
\index{submanifold!Riemannian submanifold}
A particularly nice (and exceptional) case is when $\partial M$ is totally geodesic.
