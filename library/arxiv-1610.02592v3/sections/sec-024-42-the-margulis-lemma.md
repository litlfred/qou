---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-024-42-the-margulis-lemma
section_title: "The Margulis Lemma"
section_number: 4.2
pages: 123-131
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.995
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We state and prove the \emph{Margulis Lemma}, that concerns arbitrary discrete groups in Lie groups and more specifically in $\Iso(\matH^n)$. The lemma implies that there is a constant $\varepsilon>0$, which depends only on the dimension $n$, such that the $\varepsilon$-thin part of any complete hyperbolic $n$-manifold consists of truncated cusps and tubes only. The $\varepsilon$-thin part is by definition the set of all the points with injectivity radius smaller than $\varepsilon$.

The proof of the lemma for general Lie groups is surprisingly simple and elegant; its application to the hyperbolic case needs however a more technical argument. We start by exposing some preliminary facts on the isometries of the hyperbolic space that are of independent interest.


\subsection{Isometries that commute or generate discrete groups} \label{that:commute:subsection}
Two isometries of $\matH^n$ that commute or generate a discrete group must be of a particular kind. We let $\Fix(\varphi)$ denote the fixed points in $\overline{\matH^n}$ of an isometry $\varphi$. 

\begin{lemma} \label{commute:lemma}
Let $\varphi_1,\varphi_2\in\Iso(\matH^n)$ be two hyperbolic or parabolic isometries. If they commute then $\Fix(\varphi_1) = \Fix(\varphi_2)$.
\end{lemma}
\begin{proof}
If they commute, the map $\varphi_1$ acts on $\Fix(\varphi_2)$ and vice versa. If $\varphi_2$ is hyperbolic, then $\Fix(\varphi_2)=\{p,q\}$ and $\varphi_1$ fixes the line with endpoints $p$ and $q$, hence is again hyperbolic with $\Fix(\varphi_1)=\{p,q\}$. If $\varphi_1$ and $\varphi_2$ are parabolic then they have the same fixed point $\Fix(\varphi_1) = \Fix(\varphi_2)$.
\end{proof}

\begin{lemma} \label{fissi:lemma}
Let $\varphi_1,\varphi_2\in\Gamma$ be two non-trivial isometries in a discrete group $\Gamma < \Iso (\matH^n)$ that acts freely on $\matH^n$. Either $\Fix(\varphi_1)\cap \Fix(\varphi_2) = \emptyset$, or one of the following holds:
\begin{itemize}
\item $\varphi_1$ and $\varphi_2$ are parabolics with the same fixed point,
\item $\varphi_1$ and $\varphi_2$ are powers of the same hyperbolic $\varphi \in \Gamma$.
\end{itemize}
\end{lemma}
\begin{proof}
Suppose that $\varphi_1$ and $\varphi_2$ have some common fixed points. We first consider the case where $\varphi_1$ is hyperbolic and $\varphi_2$ is parabolic. We pick the half-space model and suppose $\Fix(\varphi_1) = \{0,\infty\}$ and $\Fix(\varphi_2) = \{\infty\}$. 

Proposition \ref{tre:prop} says that 
$$\varphi_1(x,t) = \lambda(Ax,t), \quad \varphi_2(x,t) = (A'x+b, t)$$ 
with $A, A' \in \On(n-1)$ and $\lambda \neq 1$. Hence
\begin{align*}
\varphi_1^n\circ \varphi_2\circ  \varphi_1^{-n}(x,t) & = \varphi_1^n\big(A'(\lambda^{-n}A^{-n}x)+b,\lambda^{-n}t) \\
& = \big(A^nA'A^{-n}x + \lambda^n A^nb , t\big).
\end{align*}
Up to interchanging $\varphi_1$ and $\varphi_1^{-1}$ we may suppose $\lambda < 1$ and get
$$\lim_{n\to \infty} \varphi_1^n \circ \varphi_2 \circ \varphi_1^{-n}(0,t) = 
\lim_{n\to \infty} \left(\lambda^nA^nb, t\right) = (0,t).$$
A contradiction since $\Gamma$ is discrete.

We now suppose that both $\varphi_1$ and $\varphi_2$ are hyperbolic, with $\Fix(\varphi_1) = \{a,\infty\}$ and $\Fix (\varphi_2) = \{b,\infty\}$. The isometries $\varphi_1$ and $\varphi_2$ permute the horospheres centred at $\infty$ and
$$[\varphi_1,\varphi_2] = \varphi_1\circ \varphi_2 \circ \varphi_1^{-1} \circ \varphi_2^{-1} \in \Gamma$$
fixes every horizontal horosphere. Hence the commutator is parabolic or trivial: the first case is excluded by the previous discussion, in the second case we have $a=b$ by Lemma \ref{commute:lemma}. 

Both $\varphi_1$ and $\varphi_2$ have the same axis $l$, and since they generate a discrete group $\Gamma_0 < \Gamma$ they are both powers of some hyperbolic $\varphi\in\Gamma_0$ with that axis. To prove this, note that $\Gamma_0$ acts effectively on $l$ as a discrete group of translations, hence $\Gamma_0 \isom \matZ$. \end{proof}

Two isometries are contained in some discrete group if and only if they generate a discrete group, so the previous lemma is actually a fact on pairs of isometries that generate discrete groups.
The two lemmas have important geometric consequences.

\begin{cor}  \label{axis:cor}
Let $\matH^n/_\Gamma$ be a complete hyperbolic manifold. The axis in $\matH^n$ of two hyperbolic isometries in $\Gamma$ are either incident or ultra-parallel (not asymptotically parallel). 
\end{cor}

\begin{cor} \label{ZxZ:cor}
Let $\matH^n/_\Gamma$ be a complete hyperbolic manifold. Every subgroup of $\Gamma$ isomorphic to $\matZ\times\matZ$ consists of parabolic elements fixing the same point at infinity.
\end{cor}

\begin{cor} \label{no:ZxZ:cor}
The fundamental group $\pi_1(M)$ of a closed hyperbolic manifold $M$ does not contain subgroups isomorphic to $\matZ\times \matZ$.
\end{cor}

\begin{cor} \label{torus:no:hyperbolic:cor}
The torus has no hyperbolic structure.
\end{cor}


\subsection{The Margulis Lemma}
We now introduce the main character of this chapter, the Margulis Lemma. We first state a general version for Lie groups and then turn more specifically to $\Iso(\matH^n)$.

\begin{lemma} \label{G:lemma}
Let $G$ be a Lie group. There is a neighbourhood $U$ of $e\in G$ such that every discrete subgroup $\Gamma < G$ generated by some elements in $U$ is nilpotent.
\end{lemma}
Note that the discreteness of $\Gamma$ is essential here, since every connected Lie group $G$ is generated by arbitrarily small elements, and $G$ needs not to be nilpotent.

\begin{proof}
Consider the commutator map 
$$[\ ,\ ]\colon G\times G \to G$$ 
that sends $(g,h)$ to the commutator $[g,h]$. The map is smooth and sends $G\times \{e\}$ and $\{e\}\times G$ to the point $e$. Therefore its differential at $(e,e)$ vanishes. We identify a neighbourhood of $e$ in $G$ with $\matR^n$, so that the commutator map near $(e,e)$ can be read as 
$$[\ ,\ ]\colon U \times U \longrightarrow \matR^n$$
for some neighbourhood $U\subset \matR^n$ of the origin.
Since its differential at $(0,0)$ vanishes, up to restricting $U$ we may suppose that the map is $\frac 12$-Lipschitz. Therefore for all $x,y \in U$ we get
$$\|[x,y]\| < \|[x,0]\| + \frac 12\|y\| = \frac 12\|y\|, \quad \|[x,y]\| < \|[0,y]\| + \frac 12\|x\| = \frac 12\|x\|$$
and hence
$$\|[x,y]\| < \frac 12 \min \big\{\|x\|, \|y\|\big\}.$$
This implies that for every smaller neighbourhood $V\subset U$ of $0$ there is a $k>0$ such that
$$\underbrace{[U, [U, \ldots [U,U]]\cdots ]}_k \subset V.$$
We now turn back to $G$. Let $\Gamma$ be discrete and generated by some elements $S\subset U$. We choose a smaller neighbourhood $V$ of $e$ such that $V \cap \Gamma = \{e\}$, hence for any $a_1,\ldots, a_k,b\in S$ we get $[a_1,[a_2, \ldots[a_k,b]]\cdots ] \in V\cap\Gamma =\{e\}$. Proposition \ref{criterion:nilpotent:prop} says that $\Gamma$ is nilpotent.
\end{proof}

We now want to refine this lemma when $G=\Iso(\matH^n)$. Let $P$ be a property of groups, like being abelian, nilpotent, etc. A group is \emph{virtually $P$} if it has a finite-index subgroup which is $P$.\index{Margulis Lemma} 

\begin{lemma}[Margulis Lemma] \label{Margulis:lemma}
In every dimension $n\geqslant 2$ there is a constant $\varepsilon_n>0$ such that for all $x\in \matH^n$, every discrete group $\Gamma<\Iso(\matH^n)$ generated by elements that move $x$ at distance smaller than $\varepsilon_n$ is virtually nilpotent.
\end{lemma}
\begin{proof}
It suffices to prove the theorem for a fixed $x\in \matH^n$ since the isometries of $\matH^n$ act transitively on points. By Lemma \ref{G:lemma} there is a neighbourhood $U$ of $e$ in $G=\Iso(\matH^n)$ such that every discrete group generated by some elements in $U$ is nilpotent. 

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{Margulis-BW}{Margulis}}
\nota{The Margulis Lemma for Lie groups furnishes a nice neighbourhood $U$ of $e\in\Iso(\matH^n)$, but here we need a nice neighbourhood $W$ of the whole compact stabiliser $\On(n)$, drawn as a \iftoggle{BW}{dark grey}{blue} line.}
\label{Margulis:fig}
\end{center}
\end{figure}

Let $V_\varepsilon\subset\Iso(\matH^n)$ be the set of all the isometries that move $x$ at distance smaller than $\varepsilon>0$. It is relatively compact. As $\varepsilon>0$ varies, the sets $V_\varepsilon$ form a neighbourhood system for the compact stabiliser $G_x <\Iso(\matH^n)$ of $x$, isomorphic to $\On(n)$. Pick a $V_\varepsilon$. Being relatively compact, it can be covered by some $m-1$ translates of $U$. See Figure \ref{Margulis:fig}.

Let now $W=W^{-1}$ be a symmetric neighbourhood of $G_x$ satisfying $W^m \subset V_\varepsilon$. Let $\Gamma$ be a discrete group generated by some elements $S\subset W$. We want to prove that the nilpotent subgroup $\Gamma_U$ generated by $\Gamma \cap U$ has index at most $m$ in $\Gamma$. This concludes the proof, for it suffices to take a $\varepsilon_n$ such that $V_{\varepsilon_n} \subset W$.

Suppose by contradiction that $\Gamma/_{\Gamma_{U}}$ contains more than $m$ cosets. Let $r(i)$ be the number of cosets represented by elements in $\Gamma$ that are products of at most $i$ generators in $S$. If $r(i)=r(i+1)$ for some $i$, then it is easy to deduce that $r(i)$ stabilises forever. This easily implies that $r(m)\geqslant m$. Therefore there are $m$ elements in $W^m$ belonging to $m$ distinct cosets. By hypothesis two of them, say $g$ and $h$, belong to the same translate of $U$. Therefore $gh^{-1} \in \Gamma\cap U$, contradicting the fact that $g$ and $h$ lie in distinct cosets.
\end{proof}

For a discrete group $\Gamma < \Iso(\matH^n)$ and a point $x\in \matH^n$, we denote by $\Gamma_\varepsilon (x)< \Gamma$ the subgroup generated by all elements $g\in \Gamma$ that move $x$ of a distance smaller than $\varepsilon$. We have proved that $\Gamma_{\varepsilon_n} (x)$ is virtually nilpotent for every $x\in\matH^n$ and every discrete $\Gamma$.

A \emph{Margulis constant} in a fixed dimension $n$ is any number $\varepsilon_n>0$ for which Lemma \ref{Margulis:lemma} holds. Every sufficiently small number is a Margulis constant.\index{Margulis constant} 


\subsection{Elementary groups}
A non-trivial discrete group $\Gamma < \Iso(\matH^n)$ is \emph{elementary} if it preserves a finite set of points in $\overline{\matH^n}$.\index{group!elementary group}

\begin{prop} \label{elementary:prop}
An elementary $\Gamma$ acting freely on $\matH^n$ is:
\begin{itemize}
\item generated by a hyperbolic isometry, or
\item generated by parabolic isometries having the same fixed point at $\infty$.
\end{itemize}
\end{prop}
\begin{proof}
Since $\Gamma$ contains no elliptics, every non-trivial element fixes one or two points at infinity in $\overline{\matH^n}$, and no other finite set of points (because of Proposition \ref{iterate:prop}). We conclude using Lemma \ref{fissi:lemma}.
\end{proof}

\begin{prop} \label{elementary:index:prop}
Let $\Gamma<\Iso(\matH^n)$ be a discrete group acting freely on $\matH^n$. If $\Gamma'<\Gamma$ has finite index and is elementary, then $\Gamma$ also is.
\end{prop}
\begin{proof}
We know that every element in $\Gamma'$ is either hyperbolic with axis $l$, or parabolic with fixed point $p\in\partial\matH^n$. If $\varphi \in \Gamma$ then $\varphi^k\in \Gamma'$ for some $k$: hence $\varphi$ is also of that type.
\end{proof}

\begin{cor}
Let $\Gamma<\Iso(\matH^n)$ be discrete and acting freely. If $\Gamma$ is virtually nilpotent, it is either trivial or elementary.
\end{cor}
\begin{proof}
We know that $\Gamma$ contains a finite-index nilpotent subgroup $H$. If $H$ is trivial then $\Gamma$ is finite and hence trivial. If $H$ is non-trivial, it has a non-trivial centre by Proposition \ref{center:prop}. Lemma \ref{commute:lemma} then implies that all the elements in $H$ have the same fixed points and so $H$ is elementary. Therefore $\Gamma$ is elementary by Proposition \ref{elementary:index:prop}
\end{proof}

Let $\varepsilon_n$ be a Margulis constant. We can strengthen the Margulis Lemma.

\begin{cor}
Let $\Gamma<\Iso(\matH^n)$ be discrete and acting freely. For every point $x\in \matH^n$ the subgroup $\Gamma_{\varepsilon_n}(x)$ is either trivial or elementary.
\end{cor}


\subsection{Thick-thin decomposition}
A notable geometric consequence of the Margulis Lemma is that every complete hyperbolic manifold decomposes into a thick and a thin part, where the thin part consists only of particularly simple star-shaped pieces. This decomposition is known as the \emph{thick-thin decomposition} of hyperbolic manifolds.\index{thick-thin decomposition}

We define a \emph{star-shaped set} centred at $p\in\partial\matH^n$ to be any subset $U\subset\matH^n$ that intersects every half-line pointing to $p$ in a half-line. For instance, a horoball is star-shaped. A \emph{star-shaped neighbourhood} of a line $l\subset\matH^n$ is any neighbourhood $V$ of $l$ that intersects every line orthogonal to $l$ into a connected set. For instance, a $R$-neighbourhood of $l$ is star-shaped.

These definitions pass to quotients. A \emph{star-shaped cusp neighbourhood} is the quotient $U/_\Gamma$ of a $\Gamma$-invariant star-shaped set $U$ centred at $p\in\partial \matH^n$ via a discrete group $\Gamma$ of parabolic transformations fixing $p$ and acting freely. Analogously, a \emph{star-shaped simple closed geodesic neighbourhood} is the quotient $V/_\Gamma$ of a $\Gamma$-invariant star-shaped neighbourhood $V$ of $l$ via a discrete group $\Gamma\isom \matZ$ of hyperbolic transformations with axis $l$.

The truncated cusps and $R$-tubes studied in Section \ref{tubes:cusps:section} are particularly nice star-shaped cusp and geodesic neighbourhoods. 

Let $\varepsilon_n>0$ be a Margulis constant. We define $M_{[\varepsilon_n,\infty)}$ and $M_{(0,\varepsilon_n]}$ respectively as the set of all points $x \in M$ having $\inj_x M \geqslant \frac{\varepsilon_n}2$, and as the closure of the complementary set $M\setminus M_{[\varepsilon_n,\infty)}$. They form respectively the \emph{thick} and \emph{thin part} of $M$. 

\begin{oss} \label{exclude:thin:oss}
We do not define the thin part simply as the set of all points $x$ having $\inj_x M \leqslant \frac{\varepsilon_n}2$ because we want to discard the degenerate and unlucky case of a closed geodesic $\gamma$ having length precisely $\varepsilon_n$. The injectivity radius would be $\frac{\varepsilon_n}2$ at the points in $\gamma$ and strictly bigger than $\frac{\varepsilon_n}2$ near $\gamma$. With our definition, the geodesic $\gamma $ is contained in $M_{[\varepsilon_n, +\infty)}$ and not in $M_{(0,\varepsilon_n]}$.
\end{oss}

The following theorem is arguably the most important structural result on complete hyperbolic manifolds of any dimension $n$.

\begin{teo}[Thick-thin decomposition] Let $M$ be a complete hyperbolic $n$-manifold. The thin part $M_{(0,\varepsilon_n]}$ consists of a disjoint union of star-shaped neighbourhoods of cusps and of simple closed geodesics of length $< \varepsilon_n$.
\end{teo}
\begin{proof}
We have $M=\matH^n/_\Gamma$. For every isometry $\varphi\in \Gamma $ we define
$$S_\varphi(\varepsilon) = \big\{ x\in\matH^n\ \big|\ d(\varphi(x),x)\leqslant \varepsilon\big\}\subset \matH^n.$$
By Proposition \ref{d:prop} the thin part $M_{(0,\varepsilon_n]}$ is the image of the set 
\begin{align*}
 S & = \big\{x\in \matH^n\ \big|\ \exists \varphi\in \Gamma, \varphi\neq \id {\rm\ such\ that\ } d(\varphi(x),x)\leqslant \varepsilon_n\big\} \\
 & = \bigcup_{\varphi\in \Gamma, \varphi \neq \id} S_\varphi(\varepsilon_n).
 \end{align*}
More precisely, we should exclude the hyperbolic $\varphi \in \Gamma$ with $d(\varphi)=\varepsilon_n$, see Remark \ref{exclude:thin:oss}, but this is not an important point and we ignore it. It is easy to check that $S_\varphi(\varepsilon)$ is star-shaped, centred at a $p\in \partial \matH^n$ or at a line $l$ according to whether $\varphi$ is parabolic fixing $p$ or hyperbolic fixing $l$.

Suppose that $x\in S_\varphi(\varepsilon_n) \cap S_\psi(\varepsilon_n)$ for some non-trivial isometries $\varphi, \psi \in \Gamma$. By the Margulis Lemma both $\varphi$ and $\psi$ belong to the elementary group $\Gamma_{\varepsilon_n}(x)$ and hence by Proposition \ref{elementary:prop} both $\varphi$ and $\psi$ are either parabolic fixing the same point $p$ at infinity or hyperbolic fixing the same line $l$.

Therefore every connected component $S_0$ of $S$ is the union of all $S_\varphi(\varepsilon_n)$ where $\varphi$ varies in some maximal elementary subgroup $\Gamma_0<\Gamma$ of parabolics fixing the same point $p$ or hyperbolics fixing the same line $l$. The set $S_0$ is a union of star-shaped sets centred at $p$ or $l$ and is hence also star-shaped. 

The group $\Gamma$ preserves $S$ and the only isometries in $\Gamma$ that preserve $S_0$ are those in $\Gamma_0$, therefore the quotient $M_{(0,\varepsilon_n]} = S/_\Gamma$ consists of star-shaped neighbourhoods of cusps and of simple closed geodesics.
\end{proof}

Star-shaped neighbourhoods are particularly nice in low dimensions.

\begin{prop}
Let $M$ be a complete orientable hyperbolic manifold of dimension $n\leqslant 3$. The thin part $M_{(0,\varepsilon_n]}$ consists of truncated cusps and $R$-tubes.
\end{prop}
\begin{proof}
Pick a non-trivial $\varphi \in \Iso^+(\matH^n)$. We check that $S_\varphi(\varepsilon)$ is either empty, or a $R$-neighbourhood of a line $l$, or a horoball, for all $\varepsilon>0$. This proves the proposition.

Suppose that $\varphi$ is hyperbolic with axis $l$. The distance $d(x,\varphi(x))$ depends only on $d(x,l)$ since all the orientation-preserving hyperbolic transformations with axis $l$ commute with $\varphi$ and act transitively on the points at fixed distance from $l$. 
It is easy to check that $d(x,\varphi(x))$ increases with $d(x,l)$ and hence $S_\varphi(\varepsilon)$ is either empty or a $R$-neighbourhood of $l$.

If $\varphi$ is parabolic, it acts on each horosphere centred at $p$ like a
Euclidean fixed-point-free orientation-preserving isometry on $\matR^{n-1}$: this must be a translation when $n\leqslant 3$. Therefore $d(x,\varphi(x))$ depends only on the horosphere $O$ containing $x$ and decreases as $O$ moves towards $p$. Therefore $S_\varphi(\varepsilon)$ is a horoball.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 11.5 cm] {\iftoggle{BW}{thick_thin-BW}{thick_thin}}
\nota{The thick-thin decomposition of a complete hyperbolic surface: the thin part (\iftoggle{BW}{light grey}{yellow}) consists of truncated cusps and neighbourhoods of short geodesics\iftoggle{BW}{}{ (blue)}.}
\label{thick_thin:fig}
\end{center}
\end{figure}

See the picture in Figure \ref{thick_thin:fig}. 

\begin{cor} \label{simple:small:geodesics:cor}
Let $M$ be a complete hyperbolic $n$-manifold. The closed geodesics in $M$ of length $< \varepsilon_n$ are simple and disjoint.
\end{cor}
\begin{proof}
These closed geodesics lie in the thin part. Star-shaped cusp neighbourhoods contain no closed geodesics, and each star-shaped geodesic neighbourhood contains only one closed geodesic, its core, which is simple.
\end{proof}


\subsection{Finite-volume hyperbolic manifolds} \label{finite-volume:subsection}
A specific feature of hyperbolic geometry is the existence of complete hyperbolic manifolds that have finite volume without being compact. The thin-thick decomposition furnishes a nice topological description of such manifolds.

\begin{prop}
A complete hyperbolic manifold $M$ has finite volume if and only if its thick part is compact.
\end{prop}
\begin{proof}
If the thick part is not compact, it contains an infinite number of points that stay pairwise at distance greater than $\varepsilon_n$. The open balls of radius $\frac{\varepsilon_n}2$ centred at these points are embedded and disjoint and all have the same volume: therefore their union has infinite volume.

If the thick part is compact, it has finite volume. Its boundary is also compact, and hence has finitely many connected components. Therefore the thin part
consists of finitely many star-shaped neighbourhoods of cusps and closed geodesics, each with compact boundary. Each such object has finite volume (because it is contained in a bigger abstract truncated cusp with compact base, or a $R$-tube, which has finite volume).
\end{proof}

\begin{cor} \label{tame:cor}
Every complete finite-volume hyperbolic manifold $M$ is diffeomorphic to the interior of a compact manifold $N$ with boundary. The boundary $\partial N$ consists of manifolds that admit some flat structure.
\end{cor}
\begin{proof}
We have seen in the previous proof that the thick part of $M$ is compact, and the thin part consists of finitely many star-shaped neighbourhoods of cusps and closed geodesics, each with compact boundary.

Every cusp neighbourhood has compact base and hence contains a smaller truncated cusp, diffeomorphic to $X\times [0,1)$ for some closed flat manifold $X$. The complement in $M$ of these truncated cusps is compact: it is obtained from the thick part by adding finitely many neighbourhoods of closed geodesics (that are compact) and compact portions of cusp neighbourhoods. Each truncated cusp is diffeomorphic to $X\times [0,1)$ and can be compactified by adding $X \times 1$. The resulting manifold $N$ is compact with boundary.
\end{proof}

Every boundary component $X$ of $N$ inherits a flat structure, uniquely determined up to rescaling (different truncations modify $X$ only by rescaling.) As already mentioned, a truncated cusp is often called simply a \emph{cusp}: for instance we say that the surface sketched in Figure \ref{thick_thin:fig} has two cusps.

We briefly discuss the effects of Corollary \ref{tame:cor} on low-dimensional manifolds. 
Let $M$ be a complete hyperbolic manifold of finite volume of dimension $n$. If $n=2$, the manifold $M$ is diffeomorphic to the interior of a compact surface $N$ with boundary. Every boundary component of $N$ is of course a circle.

If $n=3$, the manifold $M$ is diffeomorphic to the interior of a compact 3-manifold $N$ with boundary, and every boundary component $X$ of $N$ is a flat surface: if $M$ is orientable, then $\partial N$ also is, and by Proposition \ref{flat:is:torus:prop} it consists of tori.


\subsection{Geodesic boundary and cusps}
Most of the arguments of this chapter extend to hyperbolic manifolds with compact geodesic boundary.

\begin{prop} \label{geodesic:M:N:prop}
Every complete finite-volume hyperbolic manifold $M$ with compact geodesic boundary is diffeomorphic to a compact manifold $N$ with some boundary components removed. The removed components have a flat structure. The remaining components form the geodesic boundary of $M$ and hence have a hyperbolic structure.
\end{prop}
\begin{proof}
Double $M$ along the geodesic boundary to obtain a finite-volume hyperbolic manifold to which Corollary \ref{tame:cor} applies. 
\end{proof}

We briefly discuss the effects in low dimensions. In dimension $n=2$ the boundary $\partial N$ consists of circles: some are geodesic components of $\partial M$, while some others are removed and correspond to cusps. In dimension $n=3$, if $M$ is orientable the removed boundary of $\partial N$ consists of tori (the cusps), while the geodesic boundary of $M$ cannot contain any torus: a torus has no hyperbolic structure by Corollary \ref{torus:no:hyperbolic:cor}.

We add some information on fundamental groups. Let the manifolds $M$ and $N$ be as in Proposition \ref{geodesic:M:N:prop}.

\begin{prop} \label{pi1:M:prop}
For every boundary component $X$ of $N$ the homomorphism $\pi_1(X)\to\pi_1(N)$ induced by inclusion is injective. Two homotopically non-trivial closed curves in distinct boundary components of $N$ are not freely homotopic in $N$.
\end{prop}
\begin{proof}
We have $M=C/_\Gamma$ for some convex $C\subset \matH^3$ with boundary consisting of hyperplanes. If $X$ is a (cusp) flat component of $\partial N$, it is isometric to $\matR^{n-1}/_{\Gamma_X}$ and the map $\Gamma_X=\pi_1(X) \to \pi_1(N)=\Gamma$ is injective since it sends a Euclidean isometry to a corresponding parabolic isometry.
If $X$ is geodesic, it lifts to a hyperplane in $\partial C$, which is simply connected: hence $\pi_1(X) \to \pi_1(N)$ is injective.

A homotopically non-trivial closed curve $\gamma\subset X$ determines a conjugacy class of hyperbolic or parabolic transformations in $\Gamma$. Every element in this class preserves a unique boundary hyperplane or a point at infinity of $C$ that projects back to $X$, so the conjugacy class determines $X$. Therefore distinct boundary components contain different conjugacy classes. 
\end{proof}

We note that a finite-volume hyperbolic manifold $M$ may have non-compact geodesic boundary: an ideal polygon in $\matH^2$ is a simple example.
