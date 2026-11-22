---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-012-22-compactification-and-isometries-of-hyperbolic
section_title: "Compactification and isometries of hyperbolic space"
section_number: 2.2
pages: 66-72
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.982
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
In this section we compactify the hyperbolic space $\matH^n$ by adding some ``points at infinity''. The compactification will then be used to classify the isometries of $\matH^n$ into three types. We also study the mutual position of two subspaces and define some peculiar hyperbolic objects: the horospheres. 


\subsection{Points at infinity}
Let a \emph{geodesic half-line} in $\matH^n$ be a geodesic $\gamma\colon [0,+\infty) \to \matH^n$ with constant unit speed. \index{geodesic!geodesic half-line}
\begin{defn} The set $\partial \matH^n$ of the \emph{points at infinity} in $\matH^n$ is the set of all geodesic half-lines, considered up to the following equivalence relation:
$$\gamma_1 \sim \gamma_2 \ \Longleftrightarrow \sup_{t\in [0,+\infty)}\big\{d\big(\gamma_1(t), \gamma_2(t)\big) \big\} < + \infty.$$
\end{defn}

We add its points at infinity to $\matH^n$ by defining
$$\overline {\matH^n} = \matH^n \cup \partial \matH^n.$$

\begin{prop} \label{bordo:prop}
On the disc model there is a natural 1-1 correspondence between $\partial D^n$ and $\partial \matH^n$ and hence between the closed disc $\overline{D^n}$ and $\overline{\matH^n}$.
\end{prop}
\begin{proof}
A geodesic half-line $\gamma$ in $D^n$ is a circle or line arc orthogonal to $\partial D^n$ and hence the Euclidean limit $\lim_{t\to\infty}\gamma(t)$ is a point in $\partial D^n$. We now prove that two half-lines converge to the same point if and only if they lie in the same equivalence class.

Suppose that two half-geodesics $\gamma_1$, $\gamma_2$ converge to the same point $p\in\partial D^n$. Up to isometries and inversions, we can change the conformal model to $H^n$ and take $p= \infty$. In this nicer setting $\gamma_1$ and $\gamma_2$ are vertical lines:
$$\gamma_1(t) = (x_1,\ldots,x_{n-1},x_ne^t), \quad
\gamma_2(t) = (y_1,\ldots,y_{n-1},y_ne^t). $$ 
The geodesic
$$\gamma_3(t) = (y_1,\ldots,y_{n-1},x_ne^t) $$ 
is equivalent to $\gamma_2$ since $d(\gamma_2(t),\gamma_3(t))=|\ln \frac{y_n}{x_n}|$ for all $t$ and is also equivalent to $\gamma_1$ because $d(\gamma_1(t),\gamma_3(t))\to 0$ as shown in Figure \ref{verticali:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 6 cm] {\iftoggle{BW}{verticali-BW}{verticali}}
\nota{Two vertical lines $\gamma_1$ and $\gamma_3$ in the half-space model $H^n$ at \emph{Euclidean} distance $d$. The \emph{hyperbolic} length of the horizontal segment between them at height $x_n$ is $\frac d{x_n}$ and hence tends to zero as $x_n\to\infty$ (left). 
Using as a height parameter the more intrinsic hyperbolic arc-length, we see that the two vertical geodesics $\gamma_1$ and $\gamma_3$ approach at exponential rate, since $d(\gamma_1(t), \gamma_3(t))\leqslant de^{-t}$ (right).}
\label{verticali:fig}
\end{center}
\end{figure}

Suppose that $\gamma_1$ and $\gamma_2$ converge to distinct points in $\partial D^n$. We can use the half-space model again and suppose that $\gamma_1$ is upwards vertical and $\gamma_2$ tends to some other point in $\{x_n=0\}$. In that case we easily see that $d(\gamma_1(t), \gamma_2(t))\to \infty$: for any $M>0$ there is a $t_0>0$ such that $\gamma_1(t)$ and $\gamma_2(t)$ lie respectively in $\{x_{n+1}>M\}$ and $\left\{x_n<\frac 1M\right\}$ for all $t>t_0$. Whatever curve connects these two open sets, it has length at least $\ln{M^2}$, hence $d(\gamma_1(t), \gamma_2(t)) > \ln{M^2}$ for all $t>t_0$.
\end{proof}


\subsection{The compactification}
We can give $\overline{\matH^n}$ the topology of $\overline{D^n}$, and in that way we have \emph{compactified} $\matH^n$ by adding its points at infinity. The interior of $\overline{\matH^n}$ is $\matH^n$, and the points at infinity form a sphere $\partial \matH^n$. \index{hyperbolic space!compactification of hyperbolic space}

The topology on $\overline {\matH^n}$ may also be defined intrinsically: for any $p\in\partial \matH^n$ we define a system of open neighbourhoods of $p$ in $\overline{\matH^n}$ as follows. Let $\gamma$ be a half-line with $[\gamma] = p$ and $V$ be an open neighbourhood of the vector $\gamma'(0)$ in the unitary sphere in $T_{\gamma(0)}\matH^n$. Pick $r>0$ and define the subset of $\overline{\matH^n}$:
\begin{align*}
U(\gamma, V, r) & = \left\{\alpha(t)\ \big|\ \alpha(0) = \gamma(0), \ \alpha'(0) \in V, \ t>r \right\} \\
& \bigcup \left\{[\alpha] \ \big|\ \alpha(0) = \gamma(0), \ \alpha'(0) \in V \right\}
\end{align*}
where $\alpha$ indicates a half-line in $\matH^n$ and $[\alpha]\in\partial\matH^n$ its class, see Figure \ref{intorno:fig}. We define an open neighbourhoods system $\{U(\gamma, V, r)\}$ for $p$ by letting $\gamma$, $V$, and $r$ vary. The resulting topology on $\overline{\matH^n}$ coincides with that induced by $\overline{D^n}$.

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{intorno-BW}{intorno}}
\nota{An open neighbourhood $U(\gamma, V, r)$ of $p\in\partial\matH^n$\iftoggle{BW}{ (in light grey)}{ (in yellow)}. We use the Klein model here.}
\label{intorno:fig}
\end{center}
\end{figure}

Note that $\matH^n$ is a complete Riemannian manifold (and hence a complete metric space), while its compactification $\overline{\matH^n}$ is only a topological space: a point in $\partial \matH^n$ has infinite distance from any other point in $\overline{\matH^n}$.


\subsection{Klein model} \label{projective:compactification:subsection}
In the Klein model $K^n\subset \matRP^n$, the compactification is obtained by adding the quadric $\partial K^n = \{x_1^2 + \ldots + x_n^2 - x_{n+1}^2=0\}$, which is the image of the light cone in $\matR^{n+1}$. Analogously, in the hyperboloid model $I^n$ we may represent $\partial I^n$ as the set of rays in the light cone.

A nice feature of the Klein model is that the points $x\in\matRP^n$ that lie ``beyond the infinity'', that is outside $\overline {K^n}$, can also be given a natural geometric interpretation. One such $x\in \matRP^n \setminus \overline{K^n}$ is a space-like ray in $\matR^{n+1}$ and as such it defines a hyperplane $x^\bot$ of signature $(n-1,1)$ in $\matR^{n+1}$, which projects to a hyperbolic hyperplane in $K^n$. The points beyond the infinity are in 1-1 correspondence with the hyperbolic hyperplanes in $K^n$.


\subsection{Incident, parallel, and ultraparallel subspaces}
A $k$-subspace $S\subset \matH^n$ has a topological closure $\overline S$ in the compactification $\overline{\matH^n}$. The boundary $\partial S = \overline S\cap \partial\matH^n$ of $S$ is a $(k-1)$-sphere.

For instance, the boundary of a line $l$ consists of two distinct points, the \emph{endpoints} of $l$. The boundary of a plane is a circle. Two distinct points in $\partial \matH^n$ are the endpoints of a unique line. A circle in the sphere $\partial D^3$ is the boundary of a unique plane in the disc model.

The usual \emph{distance} $d(A,B)$ between two subsets $A,B$ in a metric space is defined as 
$$d(A,B) = \inf_{x\in A, y\in B} \big\{d(x,y)\big\}.$$

There are three types of configurations for two subspaces in $\matH^n$, depicted in Figure \ref{lines:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{lines-BW}{lines}}
\nota{Two incident, asymptotic parallel, and ultraparallel lines.}
\label{lines:fig}
\end{center}
\end{figure}


\begin{prop} \label{sottospazi:prop}
Let $S$ and $S'$ be subspaces in $\matH^n$ of arbitrary dimension. Precisely one of the following holds: 
\begin{enumerate}
\item $S\cap S' \neq \emptyset$,
\item $S\cap S' = \emptyset$ and $\overline S \cap \overline {S'}$ is a point in $\partial \matH^n$; moreover $d(S,S')=0$ and there is no geodesic orthogonal to both $S$ and $S'$,
\item $\overline S\cap \overline{S'} = \emptyset$; moreover $d=d(S,S')>0$ and there is a unique geodesic $\gamma$ orthogonal to both $S$ and $S'$: the segment of $\gamma$ between $S$ and $S'$ is the unique arc connecting them of length $d$.
\end{enumerate}
\end{prop}
\begin{proof}
If $\overline S \cap \overline{S'}$ contains two points then it contains the line connecting them and hence $S\cap S'\neq \emptyset$.

In (2) we use the half-space model and send $\overline S\cap \overline {S'}$ at infinity. Then $S$ and $S'$ are Euclidean vertical subspaces and Figure \ref{verticali:fig} shows that $d(S,S')=0$. Geodesics are vertical or half-circles and cannot be orthogonal to both $S$ and $S'$.

In (3), let $x_i \in S$ and $x'_i \in S'$ be such that $d(x_i,x_i')\to d$. Since $\overline{\matH^n}$ is compact, on a subsequence $x_i\to x\in \overline S$ and $x_i'\to x'\in\overline {S'}$. By hypothesis $x\neq x'$ and hence $x,x' \in \matH^n$ since $d<\infty$. Therefore $d>0$.

\begin{figure}
\begin{center}
\includegraphics[width = 4 cm] {\iftoggle{BW}{unica_geodetica-BW}{unica_geodetica}}
\nota{Two ultraparallel subspaces $S, S'$ and a line $\gamma$ orthogonal to both.}
\label{unica_geodetica:fig}
\end{center}
\end{figure}

Let $\gamma$ be the line passing through $x$ and $x'$. The segment between $x$ and $x'$ has length $d(x,x') = d$. The line is orthogonal to $S$ and $S'$: if it had an angle smaller than $\frac\pi 2$ with $S'$ we could find another point $x''\in S'$ near $x'$ with $d(x,x'')<d$. We can draw $S, S', \gamma$ as in Figure \ref{unica_geodetica:fig} by placing the origin between $x$ and $x'$: no other line can be orthogonal to both $S$ and $S'$.
\end{proof}

Two subspaces of type (1), (2) or (3) are called respectively \emph{incident}, \emph{asymptotically parallel}, and \emph{ultra-parallel}.
\index{subspace!incident, asymptotically parallel, ultra-parallel subspaces}


\subsection{The conformal sphere at infinity}
The sphere at infinity $\partial \matH^n$ has no metric structure, but it has instead a \emph{conformal structure}, that is a Riemannian structure considered up to conformal transformations. Before defining it we note the following.

\begin{prop}
Every isometry $\varphi \colon \matH^n \to \matH^n$ extends to a unique homeomorphism $\varphi:\overline{\matH^n} \to \overline{\matH^n}$. An isometry $\varphi$ is determined by its trace $\varphi|_{\partial \matH^n}$ at the boundary.
\end{prop}
\begin{proof}
The extension of $\varphi$ to $\partial \matH^n$ is defined intrinsically: a boundary point is a class $[\gamma]$ of geodesic half-lines and we set $\varphi ([\gamma]) = [\varphi(\gamma)]$. 

To prove the second assertion we show that an isometry $\varphi$ that fixes the points at infinity is the identity. The isometry $\varphi$ fixes every line as a set (because it fixes its endpoints), and since every point is the intersection of two lines it fixes also every point.
\end{proof}

We give $\partial \matH^n$ the conformal structure of the sphere $\partial D^n$. The group $\Iso(\matH^n)$ is generated by sphere inversions, which act conformally: although the metric tensor of $\partial D^n$ is not preserved by this action, its conformal class is preserved and hence the conformal structure on $\partial \matH^n$ is well-defined.


\subsection{Elliptic, parabolic, and hyperbolic isometries}
It is convenient to classify the isometries of $\matH^n$ into three types.
\index{isometry!elliptic, parabolic, and hyperbolic isometry}

\begin{prop} \label{fixed:prop}
Let $\varphi$ be a non-trivial isometry of $\matH^n$. Precisely one of the following holds: 
\begin{enumerate}
\item $\varphi$ has at least one fixed point in $\matH^n$, 
\item $\varphi$ has no fixed points in $\matH^n$ and has exactly one in $\partial \matH^n$,
\item $\varphi$ has no fixed points in $\matH^n$ and has exactly two in $\partial \matH^n$.
\end{enumerate}
\end{prop}
\begin{proof}
The extension $\varphi:\overline{\matH^n} \to \overline{\matH^n}$ is continuous and has a fixed point by Brouwer's Theorem. We only need to prove that if $\varphi$ has three fixed points $P_1, P_2, P_3$ at the boundary then it has some fixed point in the interior. The isometry $\varphi$ fixes the line $r$ with endpoints $P_1$ and $P_2$.
There is only one line $s$ with endpoint $P_3$ and orthogonal to $r$ (exercise): the isometry $\varphi$ must also fix $s$ and hence fixes the point $r\cap s$.
\end{proof}
Isometries of type (1), (2), and (3) are called respectively \emph{elliptic}, \emph{parabolic}, and \emph{hyperbolic}. A hyperbolic isometry fixes two points $p,q\in \partial \matH^n$ and hence preserves the unique line $l$ with endpoints $p$ and $q$. The line $l$ is the \emph{axis} of the hyperbolic isometry, which acts on $l$ as a translation.


\subsection{Horospheres} \label{orosfere:subsection}
Parabolic transformations are related to some objects in $\matH^n$ called horospheres. \index{horosphere}

\begin{defn} Let $p$ be a point in $\partial\matH^n$. A \emph{horosphere} centred in $p$ is a connected complete hypersurface orthogonal to all the lines exiting from $p$.
\end{defn}

Horospheres may be easily visualised in the half-space model $H^n$ by sending $p$ at infinity. The lines exiting from $p$ are the Euclidean vertical lines and the horospheres centred at $p$ are precisely the horizontal hyperplanes $\{x_n = k\}$ with $k>0$. 

\begin{oss}
Since the metric tensor $g = \frac 1{x_n^2}g^E$ is constant on each hyperplane $\{x_n = k\}$, each horosphere is \emph{isometric} to the Euclidean $\matR^n$. 
\end{oss}

The horospheres centred at $p\neq \infty$ in $\partial H^n$ or at any point $p\in \partial D^n$ are precisely the Euclidean spheres tangent in $p$ to the sphere at infinity. The horospheres in $\matH^2$ are circles and are called \emph{horocycles}, see Figure \ref{Horocycle_normals:fig}. The portion of $\matH^n$ delimited by a horosphere is called a \emph{horoball}.

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{Horocycle_normals-BW}{Horocycle_normals}}
\nota{A horocycle in $\matH^2$ centred in $p\in\partial\matH^2$ is a circle tangent to $p$. It is orthogonal to all the lines exiting from $p$.}
\label{Horocycle_normals:fig}
\end{center}
\end{figure}

Let us go back to the isometries of $\matH^n$. We sometimes write a point in the half-space $H^n$ as a pair $(x,t)$ with $x\in \matR^{n-1}$ and $t>0$. Isometries with nice fixed points have nice expressions in the conformal models. 

\begin{prop} \label{tre:prop}
Let $\varphi$ be an isometry of $\matH^n$:
\begin{enumerate}
\item if $\varphi$ is elliptic with fixed point $0\in D^n$ then
$$\varphi(x) = Ax$$
for some matrix $A\in \On(n)$; 
\item if $\varphi$ is parabolic with fixed point $\infty$ in $H^n$ then
$$\varphi (x,t) = (Ax+b, t)$$ 
for some matrix $A\in \On(n-1)$ and some vector $b$;
\item if $\varphi$ is hyperbolic with fixed points $0$ and $\infty$ in $H^n$ then
$$\varphi (x,t) = \lambda(Ax,t)$$
for some matrix $A\in \On(n-1)$ and some positive scalar $\lambda\neq 1$.
\end{enumerate}
\end{prop}
\begin{proof}
Point (1) is obvious. In (2) the isometry $\varphi$ fixes $\infty$ and hence permutes the horospheres centred at $\infty$: we first prove that this permutation is trivial. The map $\varphi$ sends a horosphere $O_0$ at height $t=t_0$ to a horosphere $O_1$ at some height $t=t_1$. If  $t_1\neq t_0$, up to changing $\varphi$ with its inverse we may suppose that $t_1<t_0$. 

We know that the map $\psi\colon O_1 \to O_0$ sending $(x,t_1)$ to $(x,t_0)$ is a contraction: hence $\varphi\circ\psi \colon O_1 \to O_1$ is a contraction and thus has a fixed point $(x,t_1)$. Therefore $\varphi(x,t_0) = (x,t_1)$. Since $\varphi(\infty)=\infty$, the vertical geodesic passing through $(x,t_0)$ and $(x,t_1)$ is preserved by $\varphi$, and hence we have found another fixed point $(x,0)\in\partial \matH^n$, a contradiction.

We now know that $\varphi$ preserves the horosphere $O$ at height $t$, for all $t$.
The metric tensor on $O$ is Euclidean (rescaled by $\frac 1{t^2}$), hence $\varphi$ acts on $O$ like an isometry $x\mapsto Ax+b$.
Since $\varphi$ sends vertical geodesics to vertical geodesics, it acts with the same formula on each horosphere and we are done.

Concerning (3), the axis $l$ of $\varphi$ is the vertical line with endpoints $0=(0,0)$ and $\infty$, and $\varphi$ acts on $l$ by translations: hence it sends $(0,1)$ to some $(0,\lambda)$. The differential $d\varphi$ at $(0,1)$ is necessarily $\matr A 0 0 \lambda$ for some $A\in \On(n-1)$ and hence $\varphi$ is globally as stated. The case $\lambda = 1$ is excluded because $(0,1)$ would be a fixed point in $\matH^n$.
\end{proof}

The \emph{minimum displacement} $d=d(\varphi)$ of an isometry $\varphi$ of $\matH^n$ is \index{minimum displacement}
$$d(\varphi) = \inf_{x\in\matH^n} d\big(x,\varphi(x)\big).$$
A point $x$ realises the minimum displacement if $d(x,\varphi(x)) = d(\varphi)$.
\begin{cor} \label{spostamento:cor}
The following hold:
\begin{enumerate}
\item an elliptic transformation $\varphi$ has $d=0$ realised on its fixed points;
\item a parabolic transformation $\varphi$ with fixed point $p\in \partial\matH^n$ has $d=0$ realised nowhere and fixes every horosphere centred in $p$; 
\item a hyperbolic transformation $\varphi$ with fixed points $p,q\in\partial\matH^n$ has $d>0$ realised on its axis.
\end{enumerate}
\end{cor}
\begin{proof}
Point (1) is obvious. Point (2) was already noticed while proving Proposition \ref{tre:prop}. Concerning (3), let $l$ be the axis of the hyperbolic transformation $\varphi$. The hyperplane orthogonal to $l$ at a point $x\in l$ is sent to the hyperplane orthogonal to $l$ in $\varphi(x)$. The two hyerplanes are ultraparallel and by Proposition \ref{sottospazi:prop} their minimum distance is realised at the points $x$ and $\varphi(x)$. Hence the points on $l$ realise the minimum displacement for $\varphi$.
\end{proof}
