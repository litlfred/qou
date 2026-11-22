---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-025-43-geodesic-spectrum-isometry-groups-and-finite
section_title: "Geodesic spectrum, isometry groups, and finite covers"
section_number: 4.3
pages: 131-136
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.956
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{geodesic:spectrum:section}
We now study the geodesic spectrum and the isometry group of hyperbolic manifolds. The geodesic spectrum of $M$ is the set of the lengths of all the closed geodesics in $M$. We prove that a finite-volume $M$ has a discrete geodesic spectrum (with finite multiplicities) and a finite isometry group.\index{geodesic spectrum}

Then we turn to finite covers and derive some geometric consequences from the residually finiteness of fundamental groups.

We are almost exclusively interested in finite-volume hyperbolic manifolds. The general strategy when proving something about finite-volume hyperbolic manifolds is the following: we first suppose that the manifold is compact for simplicity, and then we adapt the proof to the non-compact case by looking at what happens to the cusps.


\subsection{Geodesic spectrum} \label{geodesic:spectrum:subsection}
We start by proving the following.
\begin{prop} Let $M$ be a finite-volume complete hyperbolic manifold. For every $L>0$ there are finitely many closed geodesics in $M$ shorter than $L$.
\end{prop}
\begin{proof}
Suppose that there are infinitely many closed geodesics shorter than $L$. We know that $M$ decomposes into a compact part and a finite union of truncated cusps. The compact part has finite diameter $D$. 

Every closed geodesic intersects the compact part because a cusp contains no closed geodesic. Therefore we can fix a basepoint $x_0\in M$ and connect $x_0$ to these infinitely many geodesics of length $<L$ with arcs shorter than $D$. We use these arcs to freely homotope the geodesics into loops based at $x_0$ of length $<L+2D$, and lift the loops to arcs in $\matH^n$ starting from some basepoint $\tilde{x}_0\in \matH^n$.

If two such arcs end at the same point, the corresponding closed geodesics in $M$ are freely homotopic: this is excluded by Proposition \ref{unique:closed:geodesic:prop}, hence these endpoints are all distinct. The orbit of $\tilde{x}_0$ now contains infinitely many points in the ball $B(\tilde{x}_0, L+2D)$, a contradiction because the orbit is discrete.
\end{proof}

The lengths of the closed geodesics in $M$ form a discrete subset of $\matR$ called the \emph{geodesic spectrum} of $M$. Let $\ell_1(M)>0$ be the minimum of the spectrum of $M$: a \emph{shortest closed geodesic} in $M$ is a closed geodesic of shortest length $\ell_1(M)$. It is not necessarily unique (not even if considered up to orientation reversal), but there are finitely many of them.\index{shortest geodesic}

\begin{prop}
If $M$ is a closed hyperbolic manifold, then 
$$\inj M = \frac 12 \cdot \ell_1(M)$$
and every shortest closed geodesic is simple.
\end{prop}
\begin{proof}
The length of a closed geodesic is the minimum displacement of the corresponding hyperbolic transformation, so Corollary \ref{inj:cor} gives the equality.

Let now $\gamma$ be a shortest closed geodesic. Consider Proposition \ref{closed:geodesic:prop}:
if $\gamma$ wraps multiple times along a curve $\eta$, then $\eta$ is shorter than $\gamma$, a contradiction. If $\gamma$ self-intersects transversely at some point $p$, we can split $\gamma$ naturally as $\gamma_1*\gamma_2$ in $\pi_1(M,p)$, where both $\gamma_1$ and $\gamma_2$ are shorter than $\gamma$. Either $\gamma_1$ or $\gamma_2$ is non-trivial in $\pi_1(M,p)$ and is hence hyperbolic, but it has length smaller than $\ell_1(M)$: this contradicts Corollary \ref{minimum:cor}.
\end{proof}

\begin{rem}
A shortest geodesic may be non-simple when $M$ has cusps! By doubling an ideal triangle along its boundary we construct a hyperbolic surface called the \emph{thrice-punctured sphere} which has three cusps and contains various closed geodesics, none of which is simple. See Chapter \ref{surfaces:chapter}.
\end{rem}


\subsection{Isometry group}
We now study the isometry group $\Iso(M)$ of a hyperbolic manifold $M$.
Recall that the \emph{normaliser} $N(H)$ of a subgroup $H < G$ is the set of elements $g\in G$ such that $gH=Hg$. It is the biggest subgroup of $G$ containing $H$ as a normal subgroup.
The isometry group $\Iso(M)$ has an algebraic representation.\index{normaliser}

\begin{prop}
Let $M=\matH^n/_\Gamma$ be a complete hyperbolic manifold. There is a natural isomorphism 
$$\Iso(M) \Isom N(\Gamma)/_\Gamma.$$
\end{prop}
\begin{proof}
Every isometry $\varphi\colon M \to M$ lifts to an isometry $\tilde \varphi$ 
$$
\xymatrix{ 
\matH^n\ar@{.>}[r]^{\tilde \varphi} \ar[d]_\pi & \matH^n \ar[d]^\pi \\
M\ar[r]_\varphi & M
}
$$
such that $\tilde\varphi \Gamma = \Gamma \tilde\varphi$: hence $\tilde\varphi \in N(\Gamma)$. The lift is uniquely determined up to left- or right-multiplication by elements in $\Gamma$, hence we get a homomorphism
$$\Iso(M) \to N(\Gamma)/_\Gamma$$
which is clearly surjective (every element in $N(\Gamma)$ determines an isometry) and injective (if $\tilde\varphi\in\Gamma$ then $\varphi=\id$).
\end{proof}

Recall that the \emph{centraliser} of $H< G$ is the set of elements $g \in G$ such that $gh=hg$ for all $h$. It is a subgroup of $G$.\index{centraliser}

\begin{ex} \label{centralizer:ex}
Let $M=\matH^n/_\Gamma$ be a finite-volume hyperbolic manifold. The centralizer of $\Gamma$ in $\Iso(\matH^n)$ is trivial.
\end{ex}


\subsection{Outer automorphism group}
The \emph{automorphism group} of a group $G$ is the group $\Aut(G)$ of all the isomorphisms $G\to G$. The \emph{inner automorphisms} are those isomorphisms of type $g\mapsto hgh^{-1}$ for some $h\in G$, and they form a normal subgroup $\Int(G)\triangleleft \Aut(G)$. The quotient
$$\Out(G) = \Aut(G)/_{\Int(G)}$$
is called the \emph{outer automorphism group} of $G$.\index{group!automorphism group}\index{group!outer automorphism group}

If $x_0, x_1$ are two points in a path-connected topological space $X$ there is a non-canonical isomorphism
$\pi_1(X,x_0) \to \pi_1(X,x_1)$, unique only up to post-composing with an inner automorphism. Therefore there is a \emph{canonical} isomorphism $\Out(\pi_1(X,x_0))\to\Out(\pi_1(X,x_1))$. Hence $\Out(\pi_1(X))$ depends very mildly on the basepoint.

The group $\Omeo(X)$ of all homeomorphisms of $X$ does not act directly on $\pi_1(X)$ because of the inner-automorphism ambiguity, but we get a natural homomorphism 
$$\Omeo (X) \longrightarrow \Out(\pi_1(X))$$
which is neither injective nor surjective in general. We note that homotopic self-homeomorphisms give rise to the same element in $\Out(\pi_1(X))$.


\subsection{Finite isometry groups}
We turn back to hyperbolic manifolds. 

\begin{prop} \label{injective:prop}
If $M$ is a finite-volume complete hyperbolic manifold, the natural map 
$$\Iso(M) \longrightarrow \Out(\pi_1(M))$$
is injective.
\end{prop}
\begin{proof}
Set $M=\matH^n/_\Gamma$, identify $\Gamma$ with $\pi_1(M)$ and $\Iso(M)$ with $N(\Gamma)/_\Gamma$. With these identifications the map
$$N(\Gamma)/_\Gamma \longrightarrow \Out(\Gamma)$$
is just the conjugacy action that sends $h\in N(\Gamma)$ to the automorphism $g \mapsto h^{-1}gh$ of $\Gamma$. This is an inner automorphism if and only if there is a $f \in\Gamma$ such that $h^{-1}gh = f^{-1}gf$ for all $g\in\Gamma$, that is if $hf^{-1}$ commutes with $g$ for all $g\in\Gamma$. Exercise \ref{centralizer:ex} gives $h=f\in\Gamma$ and hence the map is injective.
\end{proof}

\begin{cor} \label{isometries:not:homotopic:cor}
Let $M$ be a finite-volume complete hyperbolic manifold. Distinct isometries of $M$ are not homotopic.
\end{cor}

This is a quite strong fact, from which we deduce the following.

\begin{cor} \label{finite:isometry:group:cor}
The isometry group of every finite-volume complete hyperbolic manifold $M$ is finite. 
\end{cor}
\begin{proof}
We know that $M$ is diffeomorphic to the interior of some compact $N$ having $k\geqslant 0$ boundary components. Let $C_1,\ldots, C_k \subset M$ be disjoint truncated cusps, all of the same small volume $V>0$. Every isometry of $M$ permutes these truncated cusps and fixes their complement $C = M\setminus \interior {C_1\cup \ldots \cup C_k}$.

The set $C$ is compact and preserved by the Lie group $\Iso(M)$, which is hence compact. To show that it is finite it suffices to prove that it is discrete. Suppose that a sequence of isometries $\varphi_i$ converges to the identity: we will deduce that $\varphi_i$ is homotopic to $\id$ for sufficiently large values of $i$, a contradiction.

For any $\varepsilon>0$ there is a $\varphi_i$ that moves all points of $C$ at distance $<\varepsilon$. 
If $\varepsilon>0$ is sufficiently small, the isometry $\varphi_i$ preserves each $C_i$, 
it restricts to an isometry of the flat torus $X_i = \partial C_i$ and its extension to $C_i$ is just a smaller rescaling of $\varphi_i|_{X_i}$ at every flat torus leaf in the cusp. 

Let also $\varepsilon>0$ be sufficiently small, so that $\varepsilon <\inj_x M$ for every $x\in C$. We get $d(x,\varphi_i(x))<\inj_xM$ for all $x\in C$, and since $\varphi_i$ acts on each $C_i$ just by rescaling its action on $X_i$, we get the same inequality for every $x\in M$.

For every $x\in M$ there is a unique geodesic $\gamma_x$ of length $d(x,\varphi_i(x))$ connecting $x$ and $\varphi_i(x)$. The geodesics $\gamma_x$ vary continuously with $x$ and we can use them to define a homotopy between $\varphi_i$ and $\id$: a contradiction.
\end{proof}

The finiteness of the isometry groups is peculiar to the hyperbolic world: we will see in Remark \ref{torus:isometries:oss} that the isometry group of a flat torus is infinite.


\subsection{Finite covers} \label{finite:covers:subsection}
Let $M=\matH^n/_\Gamma$ be a complete finite-volume hyperbolic manifold. How many finite covers $\tilde M \to M$ are there above $M$? Quite a lot, thanks to the following.

\begin{prop} \label{RF:hyperbolic:prop}
The fundamental group $\pi_1(M)$ of a complete finite-volume hyperbolic manifold $M$ is residually finite.
\end{prop}
\begin{proof}
The group $\pi_1(M)$ is finitely generated (actually, finitely presented) because $M$ is homeomorphic to the interior of a compact manifold with boundary, so Proposition \ref{FG:RF:prop} applies.
\end{proof}

This algebraic fact has some nice geometric consequences. Recall that $\ell_1(M)$ is the length of the shortest closed geodesic in $M$.

\begin{cor}
For every $L>0$ there is a finite cover $\tilde M \to M$ with $\ell_1(\tilde M)>L$.
\end{cor}
\begin{proof}
There are finitely many hyperbolic elements $a_1,\ldots, a_k \in \pi_1(M)$ such that every closed geodesic in $M$ of length $<L$ is freely homotopic to some of these.
By residually finiteness there is a finite-index normal $H \triangleleft \pi_1(M)$ that does not contain any of the elements $a_1,\ldots, a_k$, and hence none of their conjugates. 

The finite-index $H$ determines a finite cover $\pi\colon \tilde M \to M$ with $\pi_*(\pi_1(\tilde M)) = H$. A closed geodesic in $\tilde M$ cannot be shorter than $L$ because its image in $M$ would be freely homotopic to one of $a_1,\ldots, a_k$.
\end{proof}

\begin{cor}
If $M$ is a closed hyperbolic manifold, for every $R>0$ there is a finite cover $\tilde M \to M$ with $\inj\tilde M > R$.
\end{cor}

We can summarise this by saying that every closed hyperbolic manifold has arbitrarily fat finite covers.


\subsection{Subgroup separability}
The geometric consequences of residually finiteness are quite remarkable: we now introduce a stronger algebraic notion that will lead to more geometric applications.

Let $G$ be a group. A subgroup $H<G$ is \emph{separable} if the intersection of all the finite-index subgroups of $G$ containing $H$ is $H$ itself. In other words, for every non-trivial element $a\in G\setminus H$, there is a finite-index subgroup $G'< G$ that contains $H$ but not $a$ and hence ``separates'' $H$ from $a$.\index{separable subgroup} 

By definition, the trivial subgroup $\{e\}$ in $G$ is separable if and only if $G$ is residually finite. Note that, for general $H<G$, we cannot require the subgroup $G'$ to be normal in $G$, because $H$ itself may not be normal in $G$, as opposite to $\{e\}$.
The following proposition furnishes some interesting examples.

\begin{prop} \label{Long:prop}
Every maximal abelian subgroup $H$ in a residually finite group $G$ is separable.
\end{prop}
\begin{proof}
More generally, we suppose that $H$ is maximal with respect to some word relation $f(h_1,\ldots, h_n)=e$. (In our case, $f(h_1, h_2) = [h_1, h_2]$.) Since $G$ is residually finite, there is a sequence $N_i \triangleleft G $ of finite-index normal subgroups with $\cap N_i = \{e\}$. 

We show that $H = \cap_i HN_i$, and we conclude since $HN_i > N_i$ has finite index in $G$. We have $H \subset \cap_i HN_i$. We now show that the elements of $\cap_i HN_i$ satisfy $f=e$, and by maximality of $H$ we get $H=\cap_i HN_i$.

For every $N_i$ and $h_1,\ldots, h_n \in H$, we have $f(h_1N_i, \ldots, h_nN_i) \subset  N_i$ since its projection in $G/_{N_i}$ is trivial. Therefore $\cap_i f(HN_i, \ldots, HN_i) = \{e\}$ and the elements of $\cap_i HN_i$ satisfy $f=e$.
\end{proof}

\begin{cor} \label{separable:cor}
Let $M$ be a complete finite-volume hyperbolic $n$-manifold. The following subgroups are separable:
\begin{itemize}
\item the subgroup $\langle \varphi \rangle = \matZ$ generated by a primitive hyperbolic transformation $\varphi$;
\item the subgroup $\pi_1(T)$ generated by a $(n-1)$-torus cusp section $T$.
\end{itemize}
\end{cor}
\begin{proof}
Both subgroups are maximal abelian, see Section \ref{that:commute:subsection}.
\end{proof}

We deduce a couple of geometric consequences from this algebraic fact.

\begin{cor}
Let $M$ be a complete finite-volume hyperbolic $n$-manifold. Every closed geodesic $\gamma$ in $M$ lifts to a closed geodesic in some finite covers of $M$ of arbitrarily large degree.
\end{cor}
\begin{proof}
We have $M= \matH^n/_\Gamma$. The closed geodesic $\gamma$ is obtained by projecting the axis $l$ of a primitive hyperbolic element $\varphi \in \Gamma$.
Since $\langle \varphi \rangle$ is separable, there are subgroups $H<\pi_1(M)$ of arbitrarily large index that contain $\langle \varphi \rangle$.
\end{proof}

We have discovered in particular that there are many closed hyperbolic manifolds of bounded injectivity radius with arbitrarily large volume.
We can also use separability to promote some primitive closed geodesics to simple ones on some finite coverings.

\begin{cor}
Let $M$ be a complete finite-volume hyperbolic $n$-manifold. Every primitive closed geodesic $\gamma$ in $M$ lifts to a simple closed geodesic in some finite cover of $M$.
\end{cor}
\begin{proof}
We have $M= \matH^n/_\Gamma$. The closed geodesic $\gamma$ is obtained by projecting the axis $l$ of a primitive hyperbolic element $\varphi \in \Gamma$. If $\gamma$ is not simple, it self-intersects in $k>0$ points, which lift to $k$ transverse intersections between $l$ and some translates $\varphi_1(l), \ldots, \varphi_k(l)$, for some $\varphi_i \in \Gamma$. Therefore the elements $\psi \in \Gamma$ such that $\psi(l)$ intersects $l$ transversely are those of the form $\psi = \varphi^h\varphi_i\varphi^l$ for some $i=1,\ldots, k$ and $h,l \in \matZ$.

Since $\langle \varphi \rangle$ is separable, there is a finite-index $H<\Gamma$ with $\varphi_1, \ldots, \varphi_k \not\in H$ and $\langle \varphi \rangle \subset H$. No $\varphi^h\varphi_i\varphi^l$ lies in $H$, hence for every $\psi\in H$ the lines $l$ and $\psi(l)$ coincide or are disjoint. The line $l$ projects to a simple geodesic in $\matH^n/_H$.
\end{proof}

Concerning cusps, we deduce analogously the following.

\begin{cor}
Let $M$ be a complete finite-volume hyperbolic $n$-manifold and $T\subset M$ be a $(n-1)$-torus cusp section. The cusp section $T$ lifts to a cusp section in some finite covers of $M$ with arbitrarily large degree.
\end{cor}
\begin{proof}
The subgroup $\pi_1(T)$ is separable, so there are subgroups $H<\pi_1(M)$ of arbitrarily large finite degree containing it.
\end{proof}
