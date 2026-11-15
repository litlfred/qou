---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-074-133-mostow-rigidity
section_title: "Mostow rigidity"
section_number: 13.3
pages: 425-429
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.83
latex_coverage_ratio: 0.971
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\subsection{Introduction}
We want to prove the following.
\begin{teo}[Mostow rigidity] \label{Mostow:teo}
Let $M$ and $N$ be two closed connected orientable hyperbolic 3-manifolds. Every isomorphism $\pi_1(M) \stackrel \sim\to \pi_1(N)$ between fundamental groups is induced by a unique isometry $M\stackrel \sim\to N$.
\end{teo}
This very powerful theorem says that an algebraic isomorphism between fundamental groups alone is enough to produce and characterise an isometry. 

\begin{cor} Two closed orientable hyperbolic 3-manifolds with isomorphic fundamental groups are isometric.
\end{cor}

We prove Mostow's rigidity in this section. All the ingredients are already there, we only need to make a little last effort.

We note that closed hyperbolic manifolds are aspherical because their universal cover $\matH^n$ is contractible. For such manifolds every isomorphism $\pi_1(M)\to \pi_1(N)$ is induced by a homotopy equivalence $f\colon M \to N$, unique up to homotopy: see Corollary \ref{aspherical:cor}. To prove Mostow's theorem we need to promote this homotopy equivalence to an isometry in dimension $n=3$. We already know that $\Vol(M) = \Vol(N)$ by Corollary \ref{stesso:volume:cor}.


\subsection{Proof of Mostow's theorem}
Let $f\colon M \to N$ be a smooth homotopy equivalence. Recall from Theorem \ref{estensione:teo} that $f$lifts to a map $\tilde f\colon \matH^3 \to \matH^3$ which extends continuously to a homeomorphism $\tilde f\colon\partial \matH^3 \to \partial\matH^3$ of the boundary spheres.
We start with a lemma.

\begin{lemma} \label{regolare:lemma}
The extension $\tilde f\colon \partial\matH^3 \to \partial \matH^3$ sends the vertices of every regular ideal simplex to the vertices of some regular ideal simplex. 
\end{lemma}
\begin{proof}
Let $w_0,\ldots, w_3$ be vertices of a regular ideal simplex and suppose by contradiction that their images $\tilde f(w_0),\ldots ,\tilde f(w_3)$ span a non-regular ideal simplex, which has volume smaller than $v_3-2\delta$ for some $\delta >0$. 
By Exercise \ref{volume:continuo:ex} there are neighbourhoods $U_i$ of $w_i$ in $\overline{\matH^3}$ for $i=0,\ldots, 3$ such that the volume of the simplex with vertices $\tilde f(u_0), \ldots, \tilde f(u_3)$ is smaller than $v_3-\delta$ for any choice of $u_i\in U_i$. 

In Section \ref{efficienti:subsection} we have defined a cycle
$$\alpha(t) = \sum_{\sigma \in \Sigma} \lambda_\sigma(t) \cdot \sigma$$
where $t$ depends on $\varepsilon$. We say that a singular simplex $\sigma\in \Sigma$ is \emph{bad} if its $i$-th vertex is contained in $U_i$ for all $i$. 
Let $\Sigma^{\rm bad}\subset\Sigma$ be the subset of all bad singular simplices and define
$$\alpha(t)^{\rm bad} = \sum_{\sigma \in \Sigma^{\rm bad}} \lambda_\sigma(t) \cdot \sigma.$$
We want to estimate $|\alpha(t)|$ and $|\alpha(t)^{\rm bad}|$. We prove that  
$$|\alpha(t)| = \sum_{\sigma\in \Sigma} |\lambda_\sigma(t)|$$
is a real number independent of $t$: let $S_0\subset S(t)$ be the set of all $t$-simplices having the first vertex in the Dirichlet domain $D(x_0)$ of the fixed base point $x_0\in\matH^3$. It follows from the definitions that $|\alpha(t)|$ equals the measure of $S_0$ for sufficiently big $t$. Moreover the set $S_0$ is in natural correspondence with the set of all isometries that send $x_0$ to some point in $D(x_0)$: its volume does not depend on $t$. 

To estimate $|\alpha(t)^{\rm bad}|$ we fix $g_0\in \Gamma$ so that $D(g_0x_0)\subset U_0$. Let $S^{\rm bad}\subset S(t)$ be the set of all bad $t$-simplices with first vertex in $D(g_0x_0)$. If $t$ is sufficiently big, the volume of $S^{\rm bad}$ is bigger than a constant independent of $t$ (exercise). 

We have proved that $|\alpha(t)^{\rm bad}| / |\alpha(t)|>C>0$ independently of $t$. We may suppose that $\alpha(t)$ represents $[M]$ up to renormalising. The map $f\colon M \to N$ has degree $\pm 1$ and it sends $\alpha(t)$ to a class 
$$f_*(\alpha(t)) = \sum_{\sigma\in \Sigma} \lambda_\sigma(t) \cdot (f\circ\sigma)^{\rm st} $$
representing $\pm [N]$. Since a $C$-portion of $\alpha(t)$ is bad, a $C$-portion of simplices in $f_*(\alpha(t))$ has volume smaller than $v_3-\delta$ and hence
$$\Vol(N) = \left|\int_{f_*(\alpha(t))} \omega\right| < |\alpha(t)| ( (1-C)v_3 + C(v_3 - \delta)) = |\alpha(t)| (v_3 -\delta C).$$
Since this holds for all $t$ and $|\alpha(t)| \to \|M\|$ we get
$$\Vol(N) < \|M\| (v_3 - \delta C) = \Vol (M) - \delta C \cdot \|M\|.$$
Corollary \ref{stesso:volume:cor} gives $\Vol(M) = \Vol(N)$, a contradiction.
\end{proof}

\begin{prop} \label{riflessione:prop}
Every ideal triangle in $\matH^3$ is the face of precisely two regular ideal tetrahedra.
\end{prop}
\begin{proof}
Pick the line $l$ orthogonal to the barycenter of the triangle: the vertex of a regular ideal tetrahedron must be an endpoint of $l$. To prove that these vertices give regular ideal tetrahedra, note that all ideal triangles in $\matH^3$ are isometric, so one concrete example suffices. 
\end{proof}

We turn back to Mostow rigidity.

\begin{prop}
Let $f\colon M \to N$ be a smooth homotopic equivalence between closed hyperbolic orientable 3-manifolds.  
The restriction $\tilde f|_{\partial \matH^3}\colon \partial \matH^3 \to \partial \matH^3$ is the trace of an isometry $\psi\colon \matH^3 \to \matH^3$.
\end{prop}
\begin{proof}
Let $v_0,\ldots, v_3\in\partial \matH^n$ be vertices of a regular ideal tetrahedron $\Delta$. By Lemma \ref{regolare:lemma} the lift $\tilde f$ sends them to the vertices of some regular ideal tetrahedron, and let $\psi$ be the unique isometry of $\matH^3$ such that $\psi (v_i) = \tilde f(v_i)$ for all $i$. 

By Proposition \ref{riflessione:prop} there is a unique point $v_4\neq v_3$ such that $v_0, v_1, v_2, v_4$ are the vertices of an ideal regular tetrahedron, and $\psi (v_4)$ is the unique point other than $\psi(v_3)$ such that $v_0,v_1,v_2, \psi(v_4)$ are the vertices of an ideal regular tetrahedron. By Lemma \ref{regolare:lemma} we also have $\tilde f(v_4) = \psi(v_4)$.

If we mirror $\Delta$ along its faces iteratively we get a tessellation of $\matH^3$ via regular ideal tetrahedra, whose ideal vertices form a dense subset of $\partial \matH^3$. By iterating this argument in all directions the functions $\psi$ and $\tilde f$ coincide on this dense subset and hence on the whole of $\partial \matH^3$.
\end{proof}

We can finally prove Mostow's rigidity theorem.
\begin{teo}[Mostow Rigidity] Let $f\colon M \to N$ be a homotopic equivalence between closed orientable hyperbolic 3-manifolds. The map $f$ is homotopically equivalent to an isometry.
\end{teo}
\begin{proof}
Set $M = \matH^3/_\Gamma$ and $N = \matH^3/_{\Gamma'}$, and pick a lift $\tilde f$. We have
\begin{equation} \label{equivariance:eqn}
\tilde f\circ g = f_*(g)\circ \tilde f \quad \forall g \in \Gamma
\end{equation}
for an isomorphism $f_*\colon \Gamma \to \Gamma'$. We may suppose $f$ smooth. The boundary extension of $\tilde f$ is the trace of an isometry $\psi\colon \matH^3 \to \matH^3$ and hence
\begin{equation} \label{equivariance2:eqn}
\psi\circ g = f_*(g)\circ \psi \quad \forall g \in \Gamma
\end{equation}
holds at $\partial \matH^3$. Both terms in (\ref{equivariance2:eqn}) are isometries, and isometries are determined by their boundary traces: hence (\ref{equivariance2:eqn}) holds for all points in $\matH^3$. Therefore $\psi$ descends to an isometry 
$$\psi\colon M \to N.$$
A homotopy between $f$ and $\psi$ may be constructed from a convex combination of $\tilde f$ and $\psi$ in $\matH^n$, which is also $\Gamma$-equivariant and hence descends.
\end{proof}


\subsection{Consequences of Mostow rigidity}
The most important consequence is that the entire geometry of a closed hyperbolic $3$-manifold is a topological invariant:  numerical quantities like the volume of the manifold, its geodesic spectrum, etc.~depend only on the topology of the manifold.
We single out another application. 

\begin{cor} Let $M$ be a closed orientable hyperbolic 3-manifold. The natural map
$$\Iso (M) \to \Out(\pi_1(M))$$
is an isomorphism.
\end{cor}
\begin{proof}
We already know that it is injective by Proposition \ref{injective:prop}. We prove that it is surjective:
every automorphism of $\pi_1(M)$ is represented by a homotopy equivalence since $M$ is aspherical (see Corollary \ref{aspherical:cor}), which is in turn homotopic to an isometry by Mostow's rigidity.
\end{proof}
We note that this is false in dimension $n=2$, where $\Iso(S)$ is finite and $\Out(\pi_1(S))$ is infinite. 


\subsection{Orbifolds and cone manifolds}
While by Mostow's theorem an orientable closed 3-manifold $M$ can have at most one hyperbolic structure, it may have plenty of hyperbolic cone manifold or orbifold structures, typically distinguished by their singular sets and their cone angles. For instance $M=S^3$ has plenty of such structures, as we will see.

For the moment we note that the volumes of these hyperbolic orbifold structures may be arbitrarily big, but not arbitrarily small:

\begin{prop} \label{Vol:M:O:prop}
Let a closed orientable 3-manifold $M$ be the underlying space of a hyperbolic orbifold $O$. We have
$$\Vol(O) \geqslant v_3\|M\|.$$
\end{prop}
\begin{proof}
By Selberg's Lemma there is a degree-$d$ orbifold covering $N \to O$ which is a closed hyperbolic manifold. We have $\Vol(N) = d\Vol(O)$, and since the covering is a degree-$d$ map $N \to M$ we can apply Corollary \ref{degree:d:cor} and get $\|M\| \leqslant \frac{\|N\|}d = \frac{\Vol(N)}{dv_3} = \frac{\Vol(O)}{v_3}.$
\end{proof}


\subsection{References}
Most of the proofs presented in this chapter were taken from Benedetti -- Petronio \cite{BP}, and are also contained in Thurson's notes \cite{Th}. The proof of Mostow's rigidity presented here was proposed by Gromov and applies to every dimension $n\geqslant 3$, because ideal regular simplexes have indeed the maximum volume by Haagerup and Munkholm \cite{HM}. 

\chapter{Hyperbolic three-manifolds} \label{three:chapter}

We have studied and classified the three-manifolds having seven of the eight geometries, and we are now left with the most interesting ones: hyperbolic three-manifolds.

In dimension two every closed hyperbolic surface is constructed by gluing some geodesic pair-of-pants. In dimension three, although closed hyperbolic three-manifolds are everywhere, it is somehow harder to construct them explicitly: the most general procedure to determine a hyperbolic metric (if any) on a given closed 3-manifold consists of solving \emph{Thurston's equations}.

Thurston's equations arise naturally in the attempt of constructing a hyperbolic three-manifold by triangulating it into hyperbolic tetrahedra. 
The most relevant and unexpected aspect of the theory is that it is much easier to employ hyperbolic \emph{ideal} tetrahedra than compact ones. The combinatorial framework in the ideal case is so convenient, that we use it also for closed three-manifolds.

In this chapter we describe these equations and use them to determine various finite-volume hyperbolic 3-manifolds. We start with the cusped case and then turn to the slightly more complicate closed one.
