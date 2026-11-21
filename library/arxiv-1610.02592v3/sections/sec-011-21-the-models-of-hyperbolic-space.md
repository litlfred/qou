---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-011-21-the-models-of-hyperbolic-space
section_title: "The models of hyperbolic space"
section_number: 2.1
pages: 53-66
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.989
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
In contrast with $S^n$ and $\matR^n$, the hyperbolic space $\matH^n$ may be described in various different ways, no-one of which is prevalent in the literature. Each description is a \emph{model} for $\matH^n$. We first introduce the hyperboloid model, which has a more algebraic flavour, and then we turn to the disc and half-space models that are somehow more geometric (and easier to visualise in dimensions $n=2$ and $3$).


\subsection{Hyperboloid}
The sphere $S^n$ is the set of all points with norm 1 in $\matR^{n+1}$, equipped with the Euclidean scalar product. Analogously, we may define $\matH^n$ as the set of all points of norm $-1$ in $\matR^{n+1}$, equipped with the usual \emph{Lorentzian} scalar product. This set forms a hyperboloid with two sheets, and we choose one. 
\index{Lorentzian scalar product}

\begin{defn} The \emph{Lorentzian scalar product} on $\matR^{n+1}$ is:
$$\langle x, y \rangle = \sum_{i=1}^n x_iy_i - x_{n+1}y_{n+1}.$$
It has signature $(n,1)$. A vector $x \in \matR^{n+1}$ is \emph{time-like}, \emph{light-like}, or \emph{space-like} if $\langle x, x \rangle$ is negative, null, or positive respectively.
The \emph{hyperboloid model} $I^n$ is defined as follows:
\index{vector!time-like, light-like, and space-like vector} \index{hyperbolic space} \index{hyperbolic space!hyperboloid model}
$$I^n = \big\{x \in \matR^{n+1}\ \big| \ \langle x, x \rangle = -1, \ x_{n+1} > 0 \big\}.$$
\end{defn}

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{Hyperboloid2-BW}{640px-Hyperboloid2}}
\nota{The hyperboloid with two sheets defined by the equation $\langle x, x \rangle = -1$. The model $I^n$ for $\matH^n$ is the upper sheet.}
\label{Hyperboloid2:fig}
\end{center}
\end{figure}

The set of points $x$ with $\langle x,x \rangle = -1$ is a \emph{hyperboloid with two sheets}, and $I^n$ is the connected component (sheet) with $x_{n+1}>0$. Let us prove a general fact. For us, a scalar product is a real non-degenerate symmetric bilinear form.\index{$I^n$}

\begin{prop}
Let $\langle, \rangle$ be a scalar product on $\matR^{n+1}$. The function $f\colon \matR^n \to \matR$ given by
$$f(x) = \langle x,x\rangle$$
is everywhere smooth and has differential  
$$df_x(y) = 2\langle x,y\rangle.$$
\end{prop}
\begin{proof}
The following equality holds:
$$\langle x+y, x+y\rangle = \langle x,x\rangle + 2 \langle x,y \rangle + \langle y, y \rangle.$$
The component $\langle x,y\rangle $ is linear in $y$ while $\langle y,y \rangle$ is quadratic. 
\end{proof}
\begin{cor}
The hyperboloid $I^n$ is a Riemannian manifold.
\end{cor}
\begin{proof}
The hyperboloid is the set of points with $f(x)=\langle x,x\rangle = -1$. For all $x\in I^n$ the differential $y\mapsto 2\langle x,y\rangle $ is surjective and hence the hyperboloid is a differentiable submanifold of codimension 1. 

The tangent space $T_xI^n$ at $x\in I^n$ is the hyperplane
$$T_x = \ker df_x = \big\{ y \ \big| \ \langle x, y \rangle = 0 \big\} = x^\bot$$
orthogonal to $x$ in the Lorentzian scalar product. Since $x$ is time-like, the restriction of the Lorentzian scalar product to $x^\bot$ is positive definite and hence defines a metric tensor on $I^n$. \end{proof}

The hyperboloid $I^n$ is a model for hyperbolic space $\matH^n$. We will soon prove that it is simply connected, complete, and has constant curvature $-1$. 


\subsection{Isometries of the hyperboloid}
The isometries of $I^n$ are easily classified using linear algebra. 

Let $O(n,1)$ be the group of linear isomorphisms $f$ of $\matR^{n+1}$ that preserve the Lorentzian scalar product, \emph{i.e.}~such that $\langle v,w\rangle = \langle f(v),  f(w) \rangle$ for any $v,w \in \matR^n$. An element in $O(n,1)$ preserves the hyperboloid with two sheets, and the elements preserving the upper sheet $I^n$ form a subgroup of index two in $O(n,1)$ that we indicate with $O^+(n,1)$.\index{$O(n,1)$}\index{$O^+(n,1)$}

\begin{prop} \label{isom:prop}
The following equality holds:
$$\Iso (I^n) = O^+(n,1).$$
\end{prop}
\begin{proof}
Pick $f\in O^+(n,1)$. If $x\in I^n$ then $f(x) \in I^n$ and $f$ sends $x^\bot$ to $f(x)^\bot$ isometrically, hence $f \in\Iso (I^n)$. Therefore $O^+(n,1) \subseteq \Iso (I^n)$.

To prove the converse inclusion we show that for every pair $x,y \in I^n$ and every
linear isometry $g\colon x^\bot \to y^\bot$ there is an element $f\in O^+(n,1)$ such that $f(x)=y$ and $f|_{x^\bot} = g$. Since isometries are determined by their first-order behaviour at a point $x$, this implies $\Iso(I^n) \subseteq O^+(n,1)$.

Via elementary linear algebra we prove that $O^+(n,1)$ acts transitively on $I^n$ and hence we may suppose that $x=y=(0,\ldots,0,1)$. Now $x^\bot = y^\bot$ is the horizontal hyperplane and $g\in O(n)$.  To define $f$ simply take
$$f = \begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix}.$$
The proof is complete.
\end{proof}

The isometry groups of $S^n$ and $\matR^n$ are described analogously:
\begin{prop} \label{isom2:prop}
The following equalities hold:
\begin{align*}
\Iso(S^n) & = O(n+1), \\
\Iso(\matR^n) & = \big\{x \mapsto Ax+b\ \big| \ A\in O(n), b \in \matR^n\big\}.
\end{align*}
\end{prop}
\begin{proof}
The proof is analogous to the one above.
\end{proof}

We have also proved the following fact. A \emph{frame} at a point $p$ in a Riemannian manifold $M$ is an orthonormal basis for $T_pM$.

\begin{cor} \label{riferimento:cor}
Let $M= S^n$, $\matR^n$, or $\matH^n$. Given two points $p,q \in M$ and two frames at $p$ and $q$, there is a unique isometry that carries the first frame to the second.
\end{cor}


\subsection{Subspaces}
We introduce the following natural objects. \index{hyperbolic space!subspace of hyperbolic space}

\begin{defn}
A $k$-dimensional \emph{subspace} of $\matR^n$, $S^n$, $I^n$ is respectively:
\begin{itemize}
\item an affine $k$-dimensional space in $\matR^n$,
\item the intersection of a $(k+1)$-dimensional vector subspace of $\matR^{n+1}$ with $S^n$,
\item the intersection of a $(k+1)$-dimensional vector subspace of $\matR^{n+1}$ with $I^n$, when it is non-empty.
\end{itemize}
\end{defn}
\begin{oss}
Elementary linear algebra shows that the following conditions are equivalent for any $(k+1)$-dimensional vector subspace $W\subset\matR^{n+1}$:
\begin{enumerate}
\item $W\cap I^n \neq \emptyset$,
\item $W$ contains at least a time-like vector,
\item the signature of $\langle,\rangle|_W$ is $(k,1)$.
\end{enumerate}
\end{oss}

A $k$-subspace in $\matR^n, S^n, \matH^n$ is itself isometric to $\matR^k, S^k, \matH^k$. 
The non-empty intersection of two subspaces is always a subspace. An isometry of $\matR^n, S^n, \matH^n$ sends $k$-subspaces to $k$-subspaces. 

\begin{ex}
Let $S$ be a $k$-subspace in $\matR^n, S^n$, or $\matH^n$ and $p\in S$ a point. There is a unique $(n-k)$-subspace $S'$ intersecting $S$ orthogonally in $p$.
\end{ex}


\subsection{Reflections} \label{reflections:subsection}
We now introduce a basic kind of isometry.
The \emph{reflection} $r_S$ along a subspace $S$ in $I^n$ is an isometry of $I^n$ defined as follows. By definition $S=I^n \cap W$ with $\langle,\rangle|_W$ non-degenerate, hence $\matR^{n+1} = W \oplus W^\bot$ and we set $r_S|_W = \id$ and $r_S|_{W^\bot} = -\id$.
Analogous definitions work for subspaces of $S^n$ and $\matR^n$. 
\index{reflection}

\begin{ex}
The reflection $r_S$ has fixed set $S$ and preserves all the subspaces orthogonal to $S$. It is orientation-preserving if and only if $S$ has even codimension.
\end{ex}

\begin{prop} \label{reflections:generate:prop}
Reflections along hyperplanes generate the isometry groups of $S^n$, $\matR^n$, and $\matH^n$.
\end{prop}
\begin{proof}
It is a standard linear algebra fact that orthogonal reflections along vector hyperspaces
generate $O(n)$. This proves the case $S^n$ and shows that reflections generate the stabiliser of any point in $\matR^n$ and $\matH^n$. To conclude it suffices to check that reflections act transitively on points: to send $x$ to $y$, reflect along the hyperplane orthogonal to the segment connecting $x$ to $y$ in its midpoint.
\end{proof}


\subsection{Lines}
A $1$-subspace is a \emph{line}. We now show that lines and geodesics are the same thing. We recall the hyperbolic trigonometric functions: \index{line}
$$\sinh (t) = \frac{e^t-e^{-t}}2, \quad \cosh (t) = \frac{e^t+e^{-t}}2.$$

\begin{prop} \label{lines:prop}
A non-trivial complete geodesic in $S^n$, $\matR^n$, or $\matH^n$ is a line run at constant speed. Concretely, let $p\in M$ be a point and $v\in T_pM$ a unit vector. The geodesic $\gamma$ exiting from $p$ with velocity $v$ is:
\begin{itemize}
\item $\gamma(t) = \cos (t) \cdot p + \sin (t) \cdot v$ if $M=S^n$,
\item $\gamma(t) = p + tv$ if $M=\matR^n$,
\item $\gamma(t) = \cosh (t) \cdot p + \sinh (t) \cdot v$ if $M=I^n$.
\end{itemize}
\end{prop}
\begin{proof}
Let $p\in I^n$ be a point, $v\in T_pM$ a unit vector, and $\gamma$ the geodesic exiting from $p$ with velocity $v$.
The plane $W\subset \matR^{n+1}$ generated by $p$ and $v$ intersects $I^n$ into a line $l$ containing $p$ and tangent to $v$. To prove that $l$ is the support of $\gamma$ we use a symmetry argument: the reflection $r_l$ fixes $p$ and $v$ and hence $\gamma$, therefore $\gamma$ is forced to be contained in its fixed locus, which is $l$. This shows that non-trivial geodesics are lines run at constant speed.

We now consider the curve $\alpha(t) = \cosh (t) \cdot p + \sinh(t) \cdot v$. We have $\alpha(0) = p$ and $\alpha'(0) = v$. It remains to prove that $\alpha$ parametrizes $l$ with unit speed, and from this we deduce that $\gamma = \alpha$. We note that 
\begin{align*}
\langle \alpha (t), \alpha(t) \rangle & = \cosh^2(t) \langle p,p \rangle + 2\cosh(t)\sinh(t) \langle p,v \rangle + \sinh^2(t) \langle v,v\rangle \\
 & = -\cosh^2(t) + \sinh^2(t) = -1.
 \end{align*}
Therefore $\alpha$ parametrizes $l$. Its velocity is 
$$\alpha'(t) = \cosh'(t)\cdot p + \sinh'(t)\cdot v = \sinh(t)\cdot p + \cosh(t) \cdot v$$
whose squared norm is $-\sinh^2(t) + \cosh^2(t) = 1$. Therefore $\gamma=\alpha$. The proofs for $S^n$ and $\matR^n$ are analogous.
\end{proof}

\begin{cor}
The spaces $S^n$, $\matR^n$, and $\matH^n$ are complete.
\end{cor}
\begin{proof}
The previous proposition shows that geodesics are defined on $\matR$, hence the space is complete by the Hopf -- Rinow Theorem \ref{HR:teo}.
\end{proof}

It is easy to show that two points in $\matH^n$ are contained in a unique line.
\index{Euclid's V postulate}
\begin{oss}
Euclid's fifth postulate holds only in $\matR^2$. Given a line $r$ and a point $P\not\in r$, there is exactly one line passing through $P$ and disjoint from $r$ in $\matR^2$, there is no-one in $S^2$, and there are infinitely many in $\matH^2$.
\end{oss}

We can easily calculate the distance between two points.

\begin{prop}
Let $p, q\in M$ be two points. We have
\begin{itemize}
\item $\cos (d(p,q)) = \langle p,q \rangle $ if $M=S^n$,
\item $\cosh (d(p,q)) = -\langle p,q \rangle $ if $M=I^n$.
\end{itemize}
\end{prop}
\begin{proof}
Let $\gamma$ be a geodesic that goes from $p$ to $q$ at unit speed. We have $\gamma(0)=p$ and $\gamma(t)=q$ with $t=d(p,q)$. Set $v=\gamma'(0)$ and use Proposition \ref{lines:prop} to conclude.
\end{proof}


\subsection{The Poincar\'e disc} \label{Poincare:subsection}
We introduce two models of $\matH^n$, the \emph{disc} and the \emph{half-space}, that are easier to visualise especially in the dimensions $n=2,3$ we are interested in. The first model is the \emph{Poincar\'e disc}\index{$D^n$}
$$D^n = \big\{x\in \matR^n\ \big| \ \|x\|<1 \big\}.$$

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{bigezione-BW}{bigezione}}
\nota{The projection towards $P=(0,\ldots,0,-1)$ induces a bijection between the hyperboloid model $I^n$ and the disc model $D^n$.}
\label{bigezione:fig}
\end{center}
\end{figure}

The metric tensor on $D^n$ is obviously not the Euclidean one of $\matR^n$, but instead is induced by a particular diffeomorphism between $I^n$ and $D^n$ that we construct now. We identify $\matR^n$ with the horizontal hyperplane $x_{n+1}=0$ in $\matR^{n+1}$ and note that the projection towards $P=(0,\ldots,0,-1)$ depicted in Figure \ref{bigezione:fig} induces a bijection between $I^n$ and the horizontal disc $D^n\subset \matR^n$. 
The projection $p$ may be written as:
$$p(x_1,\ldots,x_{n+1}) = \frac {(x_1,\ldots, x_n)}{x_{n+1} +1}$$
and is indeed a diffeomorphism $p\colon I^n \to D^n$ that transports the metric tensor on $I^n$ to some metric tensor $g$ on $D^n$. \index{hyperbolic space!disc model}

\begin{prop}
The metric tensor $g$ at $x\in D^n$ is:
$$g_x = \left( \frac 2 {1-\|x\|^2}\right)^2 \cdot g^E_x$$
where $g^E$ is the Euclidean metric tensor on $D^n \subset \matR^n$.
\end{prop}
\begin{proof}
The inverse $q\colon D^n \to I^n$ of $p$ is:
$$q(x) = \left( \frac{2x_1}{1-\|x\|^2}, \ldots, \frac{2x_n}{1-\|x\|^2}, \frac{1+\|x\|^2}{1-\|x\|^2}\right).$$
Pick $x\in D^n$. Rotations around the $x_{n+1}$ axis are isometries of $I^n$ and commute with $p$, therefore they are isometries of $(D^n, g)$ too. Up to rotating we may take
$x = (x_1,0,\ldots, 0)$ and
find
$$dq_x = 
\frac {2}{1-x_1^2} \cdot
\begin{pmatrix}
\frac{1+x_1^2}{1-x_1^2} & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1 \\
2\frac{x_1}{1-x_1^2} & 0 & \cdots & 0
\end{pmatrix}.
$$
The column vectors form an orthonormal basis of $T_{q(x)}I^n$. Hence $dq_x$  stretches all vectors of a constant $\frac 2{1-x_1^2}$. Therefore $g_x =\frac 4{(1-x_1^2)^2} g^E_x$. 
\end{proof}

The Poincar\'e disc is a \emph{conformal} model of $\matH^n$: it is a model where the metric differs from the Euclidean metric only by multiplication by a positive scalar $\big(\frac 2{1-\|x\|^2}\big)^2$ that depends smoothly on $x$. We note that the scalar tends to infinity when $x$ tends to $\partial D^n$. On a conformal model the lengths of vectors are different from the Euclidean lengths, but the angles formed by two adjacent vectors coincide with the Euclidean ones. Shortly: lengths are distorted but angles are preserved. \index{hyperbolic space!conformal model}

Let us see how we can easily visualise $k$-subspaces in the disc model.

\begin{prop}
The $k$-subspaces in $D^n$ are the intersections of $D^n$ with $k$-spheres and $k$-planes of $\matR^n$ orthogonal to $\partial D^n$.
\end{prop}
\begin{proof}
Since every $k$-subspace is an intersection of hyperplanes, we easily restrict to the case $k=n-1$. A hyperplane in $I^n$ is $I^n\cap v^\bot$ for some space-like vector $v$. If $v$ is horizontal (\emph{i.e.}~its last coordinate is zero) then $v^\bot$ is vertical and $p(I^n\cap v^\bot) = D^n \cap v^\bot$, a hyperplane orthogonal to $\partial D^n$.

If $v$ is not horizontal, up to rescaling and rotating around $x_{n+1}$ we may suppose $v=(\alpha,0,\ldots, 0, 1)$ with $\alpha>1$. The hyperplane is
$$\big\{x_1^2 +\ldots + x_n^2 - x_{n+1}^2 = -1 \big\} \cap \big\{x_{n+1} = \alpha x_1 \big\}.$$
On the other hand the sphere in $\matR^n$ of centre $(\alpha,0,\ldots,0)$ and radius $\sqrt{\alpha^2 -1}$ is orthogonal to $\partial D^n$ and is described by the equation
$$\left\{(y_1-\alpha)^2 +y_2^2 + \ldots + y_n^2 = \alpha^2 - 1\right\} =
\left\{y_1^2 + \ldots + y_n^2 - 2\alpha y_1 = -1 \right\}$$
which is equivalent to $||y||^2 = -1 + 2\alpha y_1$. If $y = p(x)$ the relations
$$y_1 = \frac {x_1}{x_{n+1}+1}, \quad \|y\|^2 = \frac{x_{n+1}-1}{x_{n+1}+1}$$
transform the latter equation in $x_{n+1}=\alpha x_1$.
\end{proof}

Three lines in $D^2$ delimiting a hyperbolic triangle are drawn in Figure \ref{Triangolo_iperbolico:fig}. Since the disc is a conformal model, the inner angles $\alpha, \beta, \gamma$ are the ones we see on the picture. In particular we verify easily that $\alpha+\beta+\gamma<\pi$. 

\begin{figure}
\begin{center}
\includegraphics[width = 4 cm] {\iftoggle{BW}{Triangolo_iperbolico-BW}{Triangolo_iperbolico}}
\nota{Three lines that determine a hyperbolic triangle in the Poincar\'e disc. The inner angles $\alpha, \beta,$ and $\gamma$ coincide with the Euclidean ones, and we have $\alpha + \beta + \gamma < \pi$.}
\label{Triangolo_iperbolico:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{Order-5_tetrakis_square_tiling-BW}{Order-5_tetrakis_square_tiling}}
\nota{A \emph{tessellation} of $S^2$, $\matR^2$ o $\matH^2$ is a subdivision of the plane into polygons. The tessellation of $\matH^2$ shown here is obtained by drawing infinitely many lines in the plane. The triangles have inner angles $\frac \pi 2, \frac \pi {5}, \frac \pi {5}$ and are all isometric.}
\label{square_tiling:fig}
\end{center}
\end{figure}

\begin{ex} For any triple of positive angles $\alpha,\beta,\gamma$ with $\alpha+\beta+\gamma < \pi$ there is a triangle with inner angles $\alpha,\beta,\gamma$. This triangle is unique up to isometry.
\end{ex}


\subsection{Inversions} \label{inversions:subsection}
To construct our second conformal model we need to introduce a geometric transformation called inversion. \index{sphere inversion}

\begin{defn}
Let $S=S(x_0,r)$ be the sphere in $\matR^n$ centred in $x_0$ and with radius $r$. The \emph{inversion} along $S$ is the map $\varphi\colon \matR^n\setminus\{x_0\} \to \matR^n\setminus \{x_0\}$ defined as follows:
$$\varphi(x) = x_0 + r^2 \frac {x-x_0}{\|x-x_0\|^2}.$$
\end{defn}
The map may be extended continuously on the whole sphere $S^n$, identified with $\matR^n \cup \{\infty\}$ through the stereographic projection, by setting $\varphi(x_0) = \infty$ and $\varphi(\infty) = x_0$. A geometric description is shown in Figure \ref{Inversion_illustration1:fig}. 

We have already talked about conformal models. More generally, a diffeomorphism $f\colon M\to N$ between two oriented Riemannian manifolds is \emph{conformal} (respectively, \emph{anticonformal}) if for any $p\in M$ the differential $df_p$  
is the product of a scalar dilation $\lambda_p >0$ and an isometry that preserves (respectively, inverts) the orientation. 
The scalar $\lambda_p$ depends smoothly on $p$. A conformal map preserves the angle between two tangent vectors but multiplies their lengths by $\sqrt{\lambda_p}$.

\begin{ex} The stereographic projection is conformal.
\end{ex}

\begin{figure}
\begin{center}
\includegraphics[width = 4 cm] {\iftoggle{BW}{Inversion_illustration1-BW}{Inversion_illustration1}}
\includegraphics[width = 4 cm] {\iftoggle{BW}{Inversion_illustration2-BW}{Inversion_illustration2}}
\includegraphics[width = 4 cm] {\iftoggle{BW}{Inversion_illustration3-BW}{Inversion_illustration3}}
\nota{The inversion trough a sphere of centre $O$ and radius $r$ moves $P$ to $P'$ so that $OP \times OP' = r^2$ (left). It transforms a $k$-sphere $S$\iftoggle{BW}{}{ (blue)} into a $k$-plane\iftoggle{BW}{}{ (green)} if $O\in S$ (centre) or into a $k$-sphere\iftoggle{BW}{}{ (green)} if $O\not\in S$ (right).}
\label{Inversion_illustration1:fig}
\end{center}
\end{figure}

\begin{prop} \label{inversione:prop}
The following hold:
\begin{enumerate}
\item every inversion is a smooth and anticonformal map;
\item inversions send $k$-spheres and $k$-planes to $k$-spheres and $k$-planes.
\end{enumerate}
\end{prop}
\begin{proof}
Up to conjugating with translations and dilations we may suppose $x_0=0$ and $r=1$. The inversion is $\varphi(x) = \frac{x}{\|x\|^2}$ and we show that $d\varphi_x$ is $\frac 1{\|x\|^2}$ times a reflection with respect to the hyperplane orthogonal to $x$. We may suppose $x=(x_1,0,\ldots,0)$ and calculate the partial derivatives:
$$ 
\varphi(x_1,\ldots,x_n) = \frac{(x_1,\ldots, x_n)}{\|x\|^2}, \qquad
\frac{\partial \varphi_i}{\partial x_j} = \frac{\delta_{ij} \|x\|^2 - 2x_ix_j}{\|x\|^4}.
$$
The partial derivatives at $x=(x_1,0,\ldots, 0)$ are
$$\frac{\partial \varphi_1}{\partial x_1} = -\frac {1}{x_1^2}, \quad  \frac{\partial \varphi_i}{\partial x_i} = \frac {1}{x_1^2}, \quad \frac{\partial \varphi_j}{\partial x_k} = 0$$
for all $i>1$ and $j\neq k$. This proves our assertion.

The fact that an inversion preserves sphere and planes may be easily reduced to the two-dimensional case (with circles and lines), a classical fact of Euclidean geometry.
\end{proof}


\subsection{The half-space model}
We introduce another conformal model. The \emph{half-space model} is the space
\index{hyperbolic space!half-space model}\index{$H^n$}
$$H^n = \big\{(x_1,\ldots,x_n)\in \matR^n \ \big|\ x_n>0\big\}.$$
It is obtained from the disc model $D^n$ by an inversion in $\matR^n$ with centre $C=(0,\ldots,0,-1)$ and radius $\sqrt 2$ as shown in Figure \ref{inversion:fig}. The boundary $\partial H^n$ is the horizontal hyperplane $\{x_n=0\}$, to which we add the point $\infty$ at infinity to get a bijective correspondence between $\partial H^n$ and $\partial D^n$ through the inversion.

\begin{prop} The half-space $H^n$ is a conformal model for $\matH^n$. Its $k$-subspaces are the $k$-planes and $k$-spheres in $\matR^n$ orthogonal to $\partial H^n$. 
\end{prop}
\begin{proof}
The inversion is anticonformal and hence preserve angles, moreover it transforms $k$-spheres and $k$-planes in $D^n$ orthogonal to $\partial D^n$ into $k$-spheres and $k$-planes in $H^n$ orthogonal to $\partial H^n$.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{inversion-BW}{inversion}}
\nota{The inversion along the sphere with centre $C=(0,\ldots,0,-1)$ and radius $\sqrt 2$ transforms the Poincar\'e disc $D^n$ into the half-space model $H^n$. Here $n=2$.}
\label{inversion:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{semispazio-BW}{semispazio}}
\nota{Lines and planes in the half-space model for $\matH^3$.}
\label{semispazio:fig}
\end{center}
\end{figure}

Some lines and planes in $H^3$ are drawn in Figure \ref{semispazio:fig}. The metric tensor $g$ on $H^n$ has a particularly nice form. 

\begin{prop}
The metric tensor on $H^n$ is:
$$g_x = \frac 1 {x_n^2} \cdot g^E$$
where $g^E$ is the Euclidean metric tensor on $H^n \subset \matR^n$.
\end{prop}
\begin{proof}
The inversion $\varphi\colon D^n \to H^n$ is the function
\begin{align*}
\varphi(x_1,\ldots, x_n) & = (0,\ldots,0,-1) + 2\frac{(x_1,\ldots,x_{n-1},x_n+1)}{\|(x_1,\ldots,x_{n-1},x_n+1)\|^2} \\
& = \frac{(2x_1,\ldots,2x_{n-1},1-\|x\|^2)}{\|x\|^2 +2x_n+1}.
\end{align*}
As seen in the proof of Proposition \ref{inversione:prop}, the inversion $\varphi$ is anticonformal with scalar dilation
$$\frac{2}{\|(x_1,\ldots,x_{n-1},x_n+1)\|^2} = \frac{2}{\|x\|^2+2x_n+1}.$$
The map $\varphi$ hence transforms the metric tensor $\left(\frac 2 {1-\|x\|^2}\right)^2\cdot g^E$ in $x\in D^n$ into the following metric tensor in $\varphi(x) \in H^n$:
$$\left( \frac 2 {1-\|x\|^2}\right)^2 \cdot \left(\frac{\|x\|^2+2x_n+1}2\right)^2
\cdot g^E = 
\frac 1 {\varphi_n(x)^2}\cdot g^E.$$
The proof is complete.
\end{proof}


\subsection{Geodesics in the conformal models}
The disc $D^n$ and the half-space $H^n$ are conformal models for $\matH^n$. In both models the hyperbolic metric differs from the Euclidean one only by a multiplication with some function.

In the half-space $H^n$ the lines are Euclidean vertical half-lines or half-circles orthogonal to $\partial H^n$ as in Figure \ref{semispazio:fig}. Vertical geodesics have a particularly simple form.
\begin{prop} \label{verticale:prop}
The vertical geodesic in $H^n$ passing through the point $(x_1,\ldots,x_{n-1},1)$ at time $t=0$ and pointing upward with unit speed is:
$$\gamma(t) = (x_1,\ldots,x_{n-1},e^t).$$
\end{prop}
\begin{proof}
A tangent vector $v$ at $(x_1,\ldots,x_n) \in H^n$ has norm $\frac{\|v\|^E}{x_n}$ where $\|v\|^E$ indicates the Euclidean norm. We get 
$$\|\gamma'(t)\| = \|(0,\ldots,0,e^t)\| = \frac {e^t}{e^t} = 1.$$
Therefore $\gamma(t)$ runs on a line at unit speed.
\end{proof}
We can easily deduce a parametrisation for the geodesics in $D^n$ passing through the origin. Recall the hyperbolic tangent:
$$\tanh (t) = \frac {\sinh (t)}{\cosh (t)} = \frac{e^t-e^{-t}}{e^t+e^{-t}} = \frac{e^{2t} -1}{e^{2t}+1}.$$
\begin{prop}
The geodesic in $D^n$ passing through the origin at time $t=0$ and pointing towards $x \in S^{n-1}$ at unit speed is:
$$\gamma(t) = \frac{e^{t}-1}{e^{t}+1}\cdot x = \left(\tanh \tfrac {t}2\right)\cdot x.$$
\end{prop}
\begin{proof}
We can suppose $x=(0,\ldots,0,1)$ and obtain this parametrisation from that of the vertical line in $H^n$ through inversion.
\end{proof}

We obtain in particular:
\begin{cor} \label{exp:cor}
The exponential map $\exp_0\colon T_0D^n \to D^n$ at the origin $0 \in D^n$ is the diffeomorphism:
$$\exp_0(x) = \frac{e^{\|x\|}-1}{e^{\|x\|}+1}\cdot \frac{x}{\|x\|} = \left(\tanh\tfrac{\|x\|}2 \right)\cdot \frac x{\|x\|}.$$
\end{cor}

Since the isometries of $\matH^n$ act transitively on points, we deduce that the exponential map at any $p\in \matH^n$ is a diffeomorphism. As a consequence, the injectivity radius of $\matH^n$ is $\infty$, as in the Euclidean $\matR^n$.


\subsection{Isometries of the conformal models}
In the half-space model it is easy to identify some isometries:

\begin{prop} \label{traslazioni:prop}
The following are isometries of $H^n$:
\begin{itemize}
\item horizontal translations $x \mapsto x+b$ with $b=(b_1,\ldots, b_{n-1}, 0)$,
\item dilations $x \mapsto \lambda x$ with $\lambda>0$,
\item inversions with respect to spheres orthogonal to $\partial H^n$.
\end{itemize}
\end{prop}
\begin{proof}
Horizontal translations obviously preserve the metric tensor $g= \frac 1{x_n^2}\cdot g^E$. 
We indicate by $\|\cdot \|$ and $\|\cdot\|^E$ the hyperbolic and Euclidean norm of tangent vectors. On a dilation $\varphi( x)= \lambda x$ we get 
$$\|d\varphi_x(v)\| = \frac{\|d\varphi_x(v)\|^E}{\varphi(x)_n} =
\frac{\lambda \|v\|^E}{\lambda x_n} = 
\frac{\|v\|^E}{x_n} = \|v\|.
$$

Concerning inversions, up to conjugating by translations and dilations it suffices to consider the map $\varphi(x) = \frac{x}{\|x\|^2}$. We have already seen that $d\varphi_x$ is $\frac {1}{\|x\|^2}$ times a linear reflection. Therefore
$$\|d\varphi_x(v)\| = \frac{\|d\varphi_x(v)\|^E}{\varphi(x)_n} =
\frac{\|v\|^E/\|x\|^2 }{x_n/\|x\|^2} = 
\frac{\|v\|^E}{x_n} = \|v\|.
$$
This completes the proof.
\end{proof}

In the disc model we can easily write the isometries that fix the origin:

\begin{prop}
The group $O(n)$ acts isometrically on $D^n$.
\end{prop}
\begin{proof}
The metric tensor on $D^n$ has a spherical symmetry.
\end{proof}

It is harder to write the isometries that fix another point of $D^n$ or $H^n$. 

\begin{prop} \label{generate:Hn:prop}
On the conformal models $D^n$ and $H^n$, the isometry group is generated by inversions along spheres and reflections along Euclidean planes orthogonal to the boundary.
\end{prop}
\begin{proof}
We know from Proposition \ref{traslazioni:prop} that these maps are isometries of $H^n$. One such isometry fixes a hyperplane $S$, hence it is the hyperbolic reflection $r_S$ (which is the unique non-trivial isometry fixing $S$). Hyperbolic reflections generate the isometry group by Proposition \ref{reflections:generate:prop}. 

In $D^n$ the proof is the same, we leave as an exercise to prove that a sphere inversion preserves the metric tensor and is hence an isometry.
\end{proof}


\subsection{Balls in the conformal models}
How does a metric ball $B(x_0,r)$ in the hyperbolic space look like? The answer in the conformal models is surprisingly  simple. 

\begin{prop} \label{sfere:prop}
In the conformal models balls are Euclidean balls.
\end{prop}
\begin{proof}
In the disc model $B(0,r)$ is a ball centred at $0$ by symmetry. The ball $B(x_0,r)$ at another point $x_0$ is obtained from $B(0,r)$ by composing inversions, which send spheres to spheres and hence balls to balls. The inversion $D^n \to H^n$ also sends balls to balls. 
\end{proof}

The centre of the ball is not its Euclidean centre in general!


\subsection{The Klein model} \label{Klein;subsection}
There is a fourth model for the hyperbolic space that is some kind of intermediate version between the hyperboloid and the Poincar\'e disc model.\index{hyperbolic space!Klein model}\index{hyperbolic space!projective model}

The \emph{Klein} or \emph{projective model} for $\matH^n$ is obtained by embedding the hyperboloid $I^n$ inside $\matRP^n$ via the projection $\matR^{n+1}\setminus \{0\} \to \matRP^n$. The image of this embedding is an open disc $K^n\subset \matRP^n$ bounded by the quadric $x_1^2+\ldots +x_n^2-x_{n+1}^2 = 0$. We equip $K^n$ with the metric tensor transported from $I^n$ , so that $K^n$ is indeed a model for $\matH^n$. 

When read in the chart $x_{n+1} = 1$, the Klein model $K^n$ becomes the open disc $x_1^2 + \ldots + x_n^2 < 1$. It is like the Poincar\'e disc $D^n$, but with a different metric tensor! 

The Klein model $K^n$ is not conformal and its metric tensor is a bit more complicated than that of $D^n$ or $H^n$. On the other hand, the subspaces in $K^n$ are easier to identify: by definition, these are just the projective subspaces of $\matRP^n$ intersected with the open disc $K^n$. Therefore lines are straight lines, but the angles and distances are distorted. Note also that the isometries of $K^n$ are projective transformations. The distance function is particularly nice:

\begin{ex}
The distance of two distinct points $p, q$ in $K^n$ is 
$$d(p,q) = \frac 12 | \log \beta (p,q,r,s) |$$
where $r,s$ are the intersections of the projective line $l$ containing $p$ and $q$ with $\partial K^n$, and $\beta(p,q,r,s)$ is the cross-ratio of the four points.\index{cross-ratio}
\end{ex}

\begin{figure}
\begin{center}
\includegraphics[width = 4.5 cm] {\iftoggle{BW}{Klein-BW}{Klein}}
\nota{A tessellation of $\matH^2$ into regular triangles and heptagons in the Klein model.}
\label{uniform_tiling:fig}
\end{center}
\end{figure}
