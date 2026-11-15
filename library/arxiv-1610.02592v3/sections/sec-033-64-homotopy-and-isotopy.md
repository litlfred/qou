---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-033-64-homotopy-and-isotopy
section_title: "Homotopy and isotopy"
section_number: 6.4
pages: 189-193
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.845
latex_coverage_ratio: 0.964
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We have proved that ``homotopy implies isotopy'' for non-trivial simple closed curves in $S_g$, and now we want to prove an analogous result for diffeomorphisms of $S_g$.
A crucial ingredient is the following theorem proved by Smale in the 1950s, which considers the self-diffeomorphisms of the disc $D^2$.

\begin{teo} \label{Smale:teo}
Two diffeomorphisms $\varphi, \psi\colon D^2 \to D^2$ that coincide on $\partial D^2$ are isotopic, via an isotopy that fixes $\partial D^2$ pointwise.
\end{teo}

There is a proof of Theorem \ref{Smale:teo} in the topological category that is surprisingly easy and works in any dimension. 


\subsection{The Alexander trick} \label{Alexander:subsection}
The proof of the following fact is so immediate, that it has a name: it is usually called the \emph{Alexander trick}.\index{Alexander trick}

\begin{prop}[Alexander trick] Two homeomorphisms $\varphi$, $\psi\colon D^n \to D^n$ that coincide on $\partial D^n$ are continuously isotopic, via an isotopy that fixes $\partial D^n$ pointwise.
\end{prop}
\begin{proof}
We consider $f=\varphi\circ \psi^{-1}$ and $\id_{D^n}$ and define an isotopy that transforms $f$ into $\id_{D^n}$ fixing $\partial D^n$. The following function does the job:
$$F(x,t) = \left\{ \begin{matrix} x & {\rm if \ } \|x\| \geqslant t, \\ t f\left(\frac xt \right) & {\rm if\  } \|x\| \leqslant t. \end{matrix} \right.$$
The proof is complete.
\end{proof}

Unfortunately this proof does not work in the smooth category, because the function $F$ is not smooth (and not smoothable) at $(0,0)$. Of course, as every continuous map, our $F$ may be approximated by smooth functions, but the injectivity of the slices $F(\cdot, t)$ can be lost in the approximation.  

Moreover, the statement in the smooth category is just false in dimension $n\geqslant 7$: there are self-diffeomorphisms of $D^n$ that are \emph{not} smoothly isotopic to $\id_{D^n}$ in high dimension, and this is connected to the existence of \emph{exotic spheres}, differentiable manifolds that are homeomorphic but not diffeomorphic to $S^n$.\index{exotic sphere} 


\subsection{Self-diffeomorphisms of the disc} \label{self:disc:subsection}
After this very brief excursion in the topological world, we turn back to the smooth category: every map considered so far is smooth by assumption like in the rest of the book. 

We prove here Theorem \ref{Smale:teo}. We need a fact on planar fields. 

\begin{prop} \label{PB:prop}
On a nowhere-vanishing vector field on $\matR^2$, a maximal integral curve is never trapped in a compact set.
\end{prop}
\begin{proof}
Suppose by contradiction that a maximal integral curve $\alpha\colon I \to \matR^2$ lies in a compact set $K$ for all $t>t_0$. Its \emph{$\omega$-limit} $\omega(\alpha)\subset K$ is the set of all points $x\in K$ to which $\gamma$ accumulates, that is the intersection of the closures of $\alpha(t_0,\infty)$ for all $t_0 \in I$. The $\omega$-limit is the intersection of a filtration of compact sets and is hence non-empty. Pick a point $p\in\omega(\alpha)$.

Up to a local diffeomorphism, the vector field near $p$ is constant vertical as in Figure \ref{PB:fig}-(1). The integral curves near $p$ are vertical. Since $p\in\omega(\alpha)$, the curve $\alpha$ contains infinitely many of them that tend to the one containing $p$. Two subsequent ones determine a closed curve as in Figure \ref{PB:fig}-(2), that bounds a disc by the Jordan curve theorem. 

We prove that such a disc cannot exist. If it existed, we could reverse all arrows and rotate it to obtain another disc as in Figure \ref{PB:fig}-(3), and by gluing the two discs we would construct as in Figure \ref{PB:fig}-(4) a nowhere-vanishing vector field on the sphere. Such a field of course does not exist since the sphere has non-zero Euler characteristic.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{PB-BW}{PB}}
\nota{At a point $p$, after a local diffeomorphism we may suppose that the vector field is constantly vertical (1). If $p$ is a limit point of an integral curve $\alpha$ we may find a closed curve that bounds a disc (2). If such a disc existed, we could rotate it and inverse all arrows (3) and glue the two portions to form a nowhere-vanishing vector field on the sphere (4). }
\label{PB:fig}
\end{center}
\end{figure}

We can now prove Theorem \ref{Smale:teo}.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{trajectories-BW}{trajectories}}
\nota{A self-diffeomorphism $\varphi$ of $D^2$ fixing $\partial D^2$ pointwise (left). To get an isotopy fixing $\partial D^2$ pointwise we need to rescale via a diffeomorphism that maps each arc as in the right figure to itself, and varies smoothly from $\id$ to $f_t^{-1}$ from bottom to top (right).}
\label{trajectories:fig}
\end{center}
\end{figure}

\begin{proof}[Proof of Theorem \ref{Smale:teo}]
After composing with $\psi^{-1}$ we can suppose that $\psi=\id$. Now $\varphi|_{S^1}$ is the identity. Every self-diffeomorphism of any compact manifold that fixes the boundary is isotopic to one which is the identity on a collar of the boundary: hence we can suppose that $\varphi=\id$ on a collar of $S^1$.

We sketch $\varphi$ in Figure \ref{trajectories:fig}-(left): vertical lines are transformed into paths with the same endpoints. We want to construct an isotopy between $\varphi$ and $\id_{D^2}$ that ``straightens'' smoothly these lines, and we start by straightening their tangent vector fields.

Consider the constant unitary vertical vector field $X_0=(0,1)$ on $D^2$ and let $X_1$ be its image along the diffeomorphism $\varphi$. It is easy to construct a  homotopy $X_t$ between $X_0$ and $X_1$ through non-vanishing vector fields: we see both $X_0$ and $X_1$ as maps $D^2 \to \matC^*$, we lift them to maps $D^2\to \matC$ via the universal cover $\exp\colon \matC \to \matC^*$, we make a convex combination and we project it back to $\matC^*$.
By construction the vectors $X_t$ are constantly $(0,1)$ on a collar of $S^1$.

We now carefully integrate the homotopy $X_t$ of vector fields to an isotopy of diffeomorphisms. Let $S^1_+$ and $S^1_-$ be the upper and lower hemisphere of $S^1$. The vectors $X_t$ at $S^1_-$ point inside and those at $S^1_+$ point outside $D^2$. By Proposition \ref{PB:prop} the integral curve $\gamma_x^t$ of $X_t$ starting from a point $(x,-\sqrt{1-x^2}) \in S^1_-$ exits at some point in $S^1_+$ after some time $T_x^t$ that varies smoothly in $x$ and $t$.

The point $\gamma_x^t(u)$ is defined for $u\in [0, T_x^t]$ and varies smoothly on $x,t,u$. We obviously have $T_x^0= 2\sqrt{1-x^2}$ and also $T_x^1 = T_x^0$ since $\gamma_x^1 = \varphi\circ\gamma_x^0$. However $T_x^t$ may not be constant in $t$, so we rescale the integral curves as
$$\tilde\gamma_x^t(u) = \gamma_x^t\left( u \cdot \frac{T_x^t}{2\sqrt{1-x^2}}\right).$$
The new curve $\tilde\gamma_x^t$ is defined in the interval $\big[0, 2\sqrt{1-x^2}\big]$ not depending on $t$. We can now define
$$ \varphi_t \big(x, -\sqrt{1-x^2} + u \big) = \tilde\gamma_x^t\left(u\right).
$$
The diffeomorphism $\varphi_t\colon D^2 \to D^2$ furnishes an isotopy between $\id = \varphi_0$ and $\varphi=\varphi_1$. However, the diffeomorphism $\varphi_t$ does not fix the points in $S^1_+$ since the endpoint of $\tilde\gamma_x^t$ has a first coordinate $f_t(x)$ which might be distinct from $x$ when $0<t<1$ (but varies smoothly on $t$ and $x$). 

To fix that it suffices to compose each $\varphi_t$ with a diffeomorphism of $D^2$ that maps each arc as in Figure \ref{trajectories:fig}-(right) to itself and varies smoothly from $\id$ to $f_t^{-1}$ from bottom to top.
\end{proof}

\begin{oss} \label{Smale:collar:rem}
If $\varphi\colon D^2 \to D^2$ is the identity on a collar of $S^1$, we can easily transform the isotopy $\varphi_t$ so that it is the identity on this collar for all $t$. This will be useful to glue isotopies.
\end{oss}


\subsection{Homotopy and isotopy of diffeomorphisms}
We are now ready to promote homotopies to isotopies of diffeomorphisms. We start with the easier sphere case, which is a simple consequence of Theorem \ref{Smale:teo}.

\begin{teo} \label{S2:omotopi:teo}
Two diffeomorphisms $\varphi, \psi\colon S^2 \to S^2$ are isotopic $\Longleftrightarrow$ they are homotopic $\Longleftrightarrow$ they are co-oriented.
\end{teo}
\begin{proof}
We suppose that $\varphi$ and $\psi$ are co-oriented and we must prove that they are isotopic. Pick any disc $D\subset S^2$. Both $\varphi$ and $\psi$ send $D$ to some disc in $S^2$. Theorem \ref{dischi:teo} furnishes an ambient isotopy relating these maps, so we may suppose that $\varphi$ and $\psi$ coincide on $D$. The closed complement is another disc and we conclude by Theorem \ref{Smale:teo}.

More precisely, we pick a smaller closed disc $D' \subset \interior D$ and consider the closed complement $D'' = S^2\setminus \interior {D'}$. The diffeomorphisms $\varphi$ and $\psi$ of $D''$ coincide on a collar of $\partial D''$ and Theorem \ref{Smale:teo} together with Remark \ref{Smale:collar:rem} furnishes an isotopy that is the identity on that collar. We extend this isotopy as the identity on $D\setminus D''$ and we are done.
\end{proof}

The theorem has a very important three-dimensional application.\index{Smale theorem}

\begin{cor} [Smale's Theorem]
Every self-diffeomorphism of $S^2$ extends to a self-diffeomorphism of $D^3$.
\end{cor}
\begin{proof}
Every self-diffeomorphism of $S^2$ is isotopic either to the identity or to a reflection by Theorem \ref{S2:omotopi:teo}. We map a collar of $S^2$ to itself using this isotopy, then extend to the rest of $D^3$ using the identity or the reflection.
\end{proof}

We can finally promote homotopies to isotopies on a general genus-$g$ surface $S_g$. The proof uses many of the techniques introduced in the last sections: we employ multicurves to cut the surface into discs, and then use Theorem \ref{Smale:teo} individually on each disc.

\begin{figure}
\begin{center}
\includegraphics[width = 10cm] {\iftoggle{BW}{decomposizione2-BW}{decomposizione}}
\nota{Two essential multicurves (\iftoggle{BW}{dark and light grey}{blue and red}) in minimal position, which subdivide the surface into hexagons.}
\label{multicurva_decomposizione:fig}
\end{center}
\end{figure}

\begin{teo} \label{omotopi:isotopi:teo}
Two diffeomorphisms $\varphi$, $\psi\colon S_g \to S_g$ are isotopic if and only if they are homotopic.
\end{teo}
\begin{proof}
We have seen the case $g=0$, so we suppose $g\geqslant 1$. By composing with $\psi^{-1}$ we can suppose that $\psi = \id$.

Fix two essential multicurves $\mu$ and $\eta$ as in Figure \ref{multicurva_decomposizione:fig}. The figure easily generalises to any genus $g$, and the reader may check that $\mu$ and $\eta$ subdivide the surface into hexagons (or a single square when $g=1$). The important point is that $S_g \setminus (\mu \cup \eta)$ consists of polygons, none of which is a bigon.

By hypothesis $\varphi$ is homotopic to the identity, so the image multicurves $\varphi(\mu)$ and $\varphi(\eta)$ are curve by curve homotopic to $\mu$ and $\eta$. By Proposition \ref{ambiente:multicurve:prop} the multicurve $\varphi(\mu)$ is isotopic to $\mu$, and $\varphi(\eta)$ is isotopic to $\eta$.

The curves $\mu$ and $\eta$ are in minimal position because there are no bigons. The images $\varphi(\mu)$ and $\varphi(\eta)$ are also in minimal position because $\varphi$ is a diffeomorphism. 
By Proposition \ref{minimale:unica:prop} the supports $\mu \cup \eta$ and $\varphi(\mu\cup \eta)$ are ambiently isotopic, so we may suppose that they coincide.

The graph $\mu\cup \eta$ is made of vertices (the intersections $\mu\cap \eta$) and edges. The components of $\mu$ and $\eta$ are pairwise non-homotopic simple closed curves, hence $\varphi$ sends necessarily every component to itself, and it does so orientation-preservingly by Proposition \ref{no:inverso:prop}. This implies easily that vertices and edges are sent to themselves by $\varphi$. Hence $\varphi=\id$ on vertices and after an isotopy we may suppose that $\varphi=\id$ on edges too. 

After an isotopy we may also suppose that $\varphi = \id$ on a regular neighbourhood $U$ of $\mu\cup\eta$, obtained by thickening the cellularisation of $\mu\cup\eta$ to a handle decomposition with 0- and 1-handles. The complement of $U$ consists of discs (the hexagons). Consider one such disc $D$, enlarged a bit so that $\partial D \subset \interior U$. The map $\varphi$ sends $D$ to itself and is the identity on a collar of $\partial D$. By Theorem \ref{Smale:teo} and Remark \ref{Smale:collar:rem} there is an isotopy connecting $\varphi$ to $\id$ on every such disc $D$ that fixes pointwise this collar, so we can extend it constantly on the rest of $U$ and get a global isotopy on $S_g$ connecting $\varphi$ and $\id$.
\end{proof}

This theorem has important consequences in dimensions two and three.
