---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-016-31-discrete-groups-of-isometries
section_title: "Discrete groups of isometries"
section_number: 3.1
pages: 81-86
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.993
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We define hyperbolic manifolds and prove a crucial theorem, that says that every complete hyperbolic manifold is isometric to a quotient $\matH^n/_\Gamma$ for some discrete group $\Gamma <\Iso(\matH^n)$ acting freely on $\matH^n$.


\subsection{Hyperbolic, flat, and elliptic manifolds}
We introduce three important classes of Riemannian manifolds.
\index{hyperbolic manifold} \index{flat manifold} \index{elliptic manifold}

\begin{defn} A \emph{hyperbolic} (resp.~\emph{flat} or \emph{elliptic}) \emph{manifold} is a connected Riemannian $n$-manifold that may be covered by open sets isometric to open sets of $\matH^n$ (resp.~$\matR^n$ o $S^n$). 
\end{defn}

A hyperbolic (resp.~flat or elliptic) manifold has constant sectional curvature $-1$ (resp.~$0$ or $+1$). We show that the model $\matH^n$ is indeed unique.


\begin{teo} \label{simply:teo}
Every complete simply connected hyperbolic $n$-manifold $M$ is isometric to $\matH^n$.
\end{teo}
\begin{proof}
Pick a point $x\in M$ and choose an isometry $D\colon U \to V$ between an open ball $U$ containing $x$ and an open ball $V\subset \matH^n$. 
We show that $D$ extends (uniquely) to an isometry $D\colon M\to\matH^n$. 

For every $y \in M$, choose an arc $\alpha\colon [0,1]\to M$ from $x$ to $y$. By compactness there is a partition $0=t_0 < t_1 < \ldots < t_k =1$ and for each $i=0,\ldots, k-1$ an isometry $D_i\colon U_i \to V_i$ from an open ball $U_i$ in $M$ containing $\alpha([t_i,t_{i+1}])$ to an open ball $V_i\subset \matH^n$. 

We may suppose that $U_0 \subset U$ and $D_0 = D|_{U_0}$. Inductively on $i$, we now modify $D_i$ so that $D_{i-1}$ and $D_i$ coincide on the component $C$ of $U_{i-1}\cap U_i$ containing $\alpha(t_i)$. To do so, note that
$$D_{i-1}\circ D_i^{-1}\colon D_i(C) \longrightarrow D_{i-1}(C)$$
is an isometry of open connected sets in $\matH^n$ and hence extends to an isometry of $\matH^n$. Then it makes sense to compose $D_i$ with $D_{i-1}\circ D_i^{-1}$, so that the new maps $D_{i-1}$ and $D_i$ coincide on $C$. Finally, we define $D(y) = D_{k-1}(y)$.

The proof that $D(y)$ is well-defined is a standard argument. First, it is easy to check that different partitions $0=t_0 <\ldots <t_k=1$ do not vary $D(y)$, just by considering a common refinement. Then we consider another path $\beta$ connecting $x$ to $y$. Since $M$ is simply-connected, there is a homotopy connecting $\alpha$ and $\beta$. The image of the homotopy is compact and is hence covered by finitely many open balls $U_i$ isometric to open balls $V_i\subset \matH^n$ via some maps $D_i$. By the Lebesgue number theorem, there is a $N>0$ such that in the grid in $[0,1]\times [0,1]$ of $\frac 1N \times \frac 1N$ squares, the image of every square is entirely contained in at least one $U_i$. We can now modify as above the isometries $D_i$ inductively on the grid, starting from the bottom-left square, so that they all glue up and show that $D(y)$ does not depend on $\alpha$ or $\beta$.

The resulting map $D\colon M \to \matH^n$ is a local isometry by construction. Since $M$ is complete, the map $D$ is a covering by Proposition \ref{local:isometry:prop}. Since $\matH^n$ is simply connected, the covering $D$ is a homeomorphism and $D$ is actually an isometry.
\end{proof}

The isometry $D\colon M \to \matH^n$ constructed in the proof is called a \emph{developing map}.
The same proof shows that every complete simply connected flat (or elliptic) $n$-manifold is isometric to $\matR^n$ (or $S^n$). \index{developing map}


\subsection{Complete hyperbolic manifolds}
We have determined the unique complete simply connected hyperbolic $n$-manifold, and we now look at complete hyperbolic manifolds with arbitrary fundamental group. We first note that if $\Gamma < \Iso(\matH^n)$ is a group of isometries that acts freely and properly discontinuously on $\matH^n$, the quotient manifold $\matH^n/_\Gamma$ has a natural Riemannian structure that promotes the covering
$$\pi\colon\matH^n \longrightarrow \matH^n/_\Gamma$$
to a local isometry, see Proposition \ref{quotient:prop}. The quotient $\matH^n/_\Gamma$ is a complete hyperbolic manifold. 
We now show that every complete hyperbolic manifold is realised in this way:

\begin{prop} \label{corto:prop}
Every complete hyperbolic $n$-manifold $M$ is isometric to $\matH^n/_\Gamma$ for some subgroup $\Gamma<\Iso(\matH^n)$ acting freely and properly discontinuously.
\end{prop}
\begin{proof}
The universal cover of $M$ inherits a Riemannian structure that is complete (by Proposition \ref{local:isometry:prop}), hyperbolic, and simply connected: hence it is isometric to $\matH^n$ by Theorem \ref{simply:teo}. The deck transformations $\Gamma$ of the covering $\matH^n\to M$ are necessarily locally isometries, hence isometries. We conclude that $M=\matH^n/_\Gamma$ and $\Gamma$ acts freely and properly discontinuously using Proposition \ref{equivalent:prop}.
\end{proof}

Note that $\Gamma$ is isomorphic to the fundamental group $\pi_1(M)$.

\begin{oss}
A group $\Gamma<\Iso(\matH^n)$ acts freely if and only if it does not contain elliptic isometries: that is, every non-trivial isometry in $\Gamma$ is either hyperbolic or parabolic.
\end{oss}
Note also that $\Gamma$ acts properly discontinuously if and only if it is discrete, see Proposition \ref{iff:discrete:prop}. 

\begin{oss}
The same proofs show that every complete flat or spherical $n$-manifold is isometric to $\matR^n/_\Gamma$ or $S^n/_\Gamma$ for some discrete group $\Gamma$ of isometries acting freely on $\matR^n$ or $S^n$. 
\end{oss}

\begin{cor} There is a natural 1-1 correspondence
$$\left\{\!
\begin{array}{c}{\rm complete\ hyperbolic} \\ {\rm manifolds\ } M {\rm\ up\ to\ isometry}\end{array}\!\right\} \longleftrightarrow
\left\{\!
\begin{array}{c}{\rm discrete\ subgroups\ } \Gamma < \Iso(\matH^n) \\ {\rm without\ elliptics} \\ {\rm up\ to\ conjugation}\end{array}\!\right\}$$
\end{cor}
\begin{proof}
When passing from the complete hyperbolic manifold $M$ to the group $\Gamma$, the only choice we made is an isometry between the universal cover of $M$ and $\matH^n$. Different choices produce conjugate groups $\Gamma$.
\end{proof}


\subsection{Discrete groups}
We investigate some basic properties of discrete groups $\Gamma$ of isometries of $\matH^n$.

\begin{ex} If $\Gamma<\Iso(\matH^n)$ is discrete then it is countable.
\end{ex}

Note that $\Gamma$ is not necessarily finitely generated. We denote by $\Gamma_p < \Gamma$ the stabiliser of a point $p\in \matH^n$.

\begin{prop} \label{discrete:prop}
Let $\Gamma <\Iso(\matH^n)$ be discrete and $p\in\matH^n$ be a point. The stabiliser $\Gamma_p$ is finite and the orbit $\Gamma(p) = \{g(p)\ |\ g\in \Gamma\}$ is discrete.
\end{prop}
\begin{proof}
Both are obvious consequence of the fact that $\Gamma$
acts properly discontinuously.
\end{proof}

Of course $\Gamma$ acts freely on $\matH^n$ if and only if $\Gamma_p$ is trivial for all $p\in\matH^n$. A set of subspaces in $\matH^n$ is \emph{locally finite} if every compact subset in $\matH^n$ intersects only finitely many of them.

\begin{prop} \label{dense:prop}
Let $\Gamma<\Iso(\matH^n)$ be discrete. The points $p\in\matH^n$ with trivial stabiliser $\Gamma_p$ form an open dense set in $\matH^n$.
\end{prop}
\begin{proof}
The fixed-points set $\Fix(g)$ of a non-trivial isometry $g$ is a proper subspace of $\matH^n$. The subspaces $\Fix(g)$ with $g\in\Gamma$ are locally finite: if infinitely many of them intersect a compact set they accumulate and $\Gamma$ does not act properly discontinuously. The complement of a locally finite set of proper subspaces is open and dense.
\end{proof}

Recall that a group \emph{has no torsion} if every non-trivial element has infinite order.

\begin{prop} \label{no:torsion:prop}
A discrete group $\Gamma < \Iso(\matH^n)$ acts freely on $\matH^n$ if and only if it has no torsion.
\end{prop}
\begin{proof}
By Proposition \ref{iterate:prop} parabolic and hyperbolic elements have infinite order. On the other hand, an elliptic element $g\in\Gamma$ has finite order since $\Gamma_p$ is finite for $p\in\Fix(g)$.
\end{proof}

\begin{cor}
The fundamental group of a complete hyperbolic manifold has no torsion.
\end{cor}

It is now time to exhibit some examples. Recall that $H^2$ is the half-plane model, see Section \ref{isometry:2:3:section}.

\begin{example}
The \emph{modular group} 
$$\Gamma = \PSLZ < \PSLR = \Iso^+(H^2)$$ 
consists of all matrices in $\PSLR$ having integer entries and is clearly a discrete subgroup. It does not act freely on $H^2$, however: the matrix $\matr 01{-1}0$ represents the elliptic transformation $z\mapsto -\frac 1z$ with fixed point $i$. \index{modular group}
\end{example} 


\subsection{Coverings}
We now make a simple but crucial observation: if $\Gamma < \Iso(\matH^n)$ acts freely and properly discontinuously, then also every subgroup $\Gamma' < \Gamma$ does; we get a manifolds covering
$$\matH^n/_{\Gamma'} \longrightarrow \matH^n/_\Gamma$$
whose degree $d$ is precisely the index of $\Gamma'$ in $\Gamma$.  Recall from Proposition \ref{volume:covering:prop} that we get
$$\Vol\big(\matH^n/_{\Gamma'}\big) = d \cdot \Vol\big(\matH^n/_{\Gamma}\big)$$
where some of the terms in the formula may be infinite. Moreover, every covering of a hyperbolic complete $M= \matH^n/_\Gamma$ is constructed in this way: there is a nice bijective correspondence
$$\big\{{\rm coverings\ of\ }M \big\} \longleftrightarrow
\big\{{\rm subgroups\ of\ }\Gamma \big\} .$$
This holds of course also for flat and spherical manifolds.


\subsection{Congruence subgroups}
We can now exhibit a family of two-dimensional hyperbolic manifolds. 

Pick an integer $m\geqslant 2$. Let $\SL_2(\matZ/_{m\matZ})$ be the group of $2\times 2$ matrices with coefficients in $\matZ/_{m\matZ}$ and determinant 1. We define the quotient 
$$\matP\SL_2(\matZ/_{m\matZ}) = \SL_2(\matZ/_{m\matZ})/_{\{ \pm I\}}.$$
The reduction modulo $m$ homomorphism $\matZ \to \matZ/_{m\matZ}$ induces the group homomorphisms $\SL_2(\matZ) \to \SL_2(\matZ/_{m\matZ})$ and 
$$\PSLZ \longrightarrow \matP\SL_2(\matZ/_{m\matZ}).$$
The kernel of this homomorphism is the \emph{principal congruence subgroup} $\Gamma(m)$ of $\PSLZ$. It is clearly discrete, since $\PSLZ$ is. It has finite index in $\PSLZ$ because $\matP\SL_2(\matZ/_{m\matZ})$ is finite. 
\index{principal congruence subgroup}
\begin{prop}
If $m\geqslant 4$ the group $\Gamma(m)$ acts freely on $H^2$.
\end{prop}
\begin{proof}
An element $A\in\Gamma(m)$ is a matrix $\matr abcd$ congruent to $\matr 1001$ modulo $m$. In particular $a+d$ is congruent to 2 modulo $m$, and hence is not $-1, 0, 1$. Therefore $A$ is never elliptic. 
\end{proof}

The quotient $\matH^2/_{\Gamma(m)}$ is a hyperbolic surface. We will construct many hyperbolic surfaces in Section \ref{surface:geometrisation:section} via some more geometric methods.


\subsection{Selberg's lemma}
The discrete group $\Gamma = \PSLZ$ does not act freely on $H^2$, but its finite-index normal subgroup $\Gamma(m)$ does as soon as $m\geqslant 4$. Is this the instance of a more general principle? Yes, it is. \index{Selberg lemma}

\begin{prop} \label{Selberg:prop}
Every finitely generated discrete group $\Gamma < \Iso(\matH^n)$ contains a finite-index normal subgroup $\Gamma'\triangleleft \Gamma$ that acts freely on $\matH^n$.
\end{prop}
\begin{proof}
The group $\Iso(\matH^n)$ is isomorphic to $O^+(n,1) < \GL(n+1,\matC)$, so Selberg's Lemma \ref{Selberg:lemma} applies to $\Gamma$, and it furnishes a finite-index torsion-free normal subgroup $\Gamma'\triangleleft \Gamma$. This subgroup acts freely by Proposition \ref{no:torsion:prop}.
\end{proof}

Every finitely generated discrete group $\Gamma < \Iso(\matH^n)$ contains at least one finite-index subgroup that acts freely. But how many such subgroups does it contain? Quite a lot, in fact.

\begin{prop} \label{FG:RF:prop}
Every finitely generated discrete group $\Gamma<\Iso(\matH^n)$ is residually finite.
\end{prop}
\begin{proof}
See Lemma \ref{RF:lemma}.
\end{proof}

The following corollary shows that there is an abundance of torsion-free subgroups. Although algebraic in nature, it has some remarkable geometric consequences, that will be revealed soon in Section \ref{finite:covers:subsection}.

\begin{cor}
Let $\Gamma < \Iso(\matH^n)$ be discrete and finitely generated. For every non-trivial $g \in \Gamma$ there is a finite-index normal subgroup $\Gamma'\triangleleft \Gamma$ that acts freely on $\matH^n$ and does not contain $g$.
\end{cor}
