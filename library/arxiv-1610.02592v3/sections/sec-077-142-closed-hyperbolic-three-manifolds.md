---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-077-142-closed-hyperbolic-three-manifolds
section_title: "Closed hyperbolic three-manifolds"
section_number: 14.2
pages: 441-451
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.735
latex_coverage_ratio: 0.994
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We have described in Section \ref{cusped:section} a method to construct cusped finite-volume hyperbolic three-manifolds. How can we now build some \emph{closed} hyperbolic three-manifolds? 

Following the same path, we could try to parametrize \emph{compact} hyperbolic tetrahedra via some variables, and then encode the isometric gluings of their faces via some equations. However, it is really hard to parametrize compact tetrahedra and their gluings, and nobody has ever constructed any closed hyperbolic three-manifold in this way! 

The usual procedure for building closed hyperbolic three-manifolds consists of using (again) ideal tetrahedra: we start with a cusped manifold, and then we slightly modify the completeness equations to allow some appropriate Dehn-filling of some (or all) cusps. 


\subsection{Dehn filling parameters} \label{DF:parameters:subsection}
We now consider an orientable three-manifold $M = \interior N$ where $N$ is compact and $\partial N = T_1 \sqcup \ldots \sqcup T_c$ consists of tori. For simplicity we will always assume that each $T_i$ is incompressible, so that $\pi_1(T_i)=\matZ\times \matZ$ injects in $\pi_1(N) = \pi_1(M)$ for all $i$. 

We fix once for all two generators $m_i, l_i$ of $\pi_1(T_i)$ for each $i=1,\ldots,c$. A \emph{Dehn filling parameter} $s = (s_1,\ldots, s_c)$ is a sequence where each $s_i$ is either a pair $(p,q)$ of coprime integers or the symbol $\infty$. It is useful to think of $s_i$ as a point in the two-sphere $S^2 = \matR^2 \cup \{\infty \}$.

A Dehn filling parameter $s$ determines a Dehn filling of $N$ as follows: for every $i$, if $s_i=(p,q)$ we fill $T_i$ by killing the slope $pm_i + ql_i$, while if $s_i=\infty$ we do nothing. The result is a new compact manifold, whose interior we denote by $M^{\rm fill}$, that may be closed (if there are no $\infty$ in $s$) or may be bounded by some tori.

We now fix a Dehn filling parameter $s$, producing a filled manifold $M^{\rm fill}$.


\subsection{The modified equations} \label{modified:equations:subsection}
Let $\calT$ be an oriented ideal triangulation for $M$. We now describe some equations similar to that of Section \ref{cusped:section}, whose solutions now identify hyperbolic structures on $M^{\rm fill}$ instead of $M$. The equations of course will depend on the Dehn filling parameter $s$, since the manifold $M^{\rm fill}$ does.

The triangulation $\calT$ consists of some $n$ tetrahedra $\Delta_1,\ldots, \Delta_n$; we choose an edge in each $\Delta_i$ and we assign it the variable $z_i\in \matC$ with $\Im z_i >0$ as we did in Section \ref{cusped:section}.

The edges of all tetrahedra are now coloured with moduli $z_i$, $\frac 1{1-z_i}$, $\frac{z_i-1}{z_i}$ that lie in the upper half-plane and as such may be written in polar coordinates as $\rho e^{i\theta}$ with $\theta \in (0,\pi)$. It is convenient to consider these variables as elements of the multiplicative group
$$\widetilde{\matC^*} = \big\{\rho e^{i\theta}\ \big| \ \rho \in \matR_{>0},\ \theta \in \matR\big\}$$
that covers $\matC^*$ and is isomorphic to $\matC$ via the map $\exp\colon \matC \to \widetilde{\matC^*}$. 

Every edge of $\calT$ furnishes a \emph{consistency equation} in $\widetilde {\matC^*}$ as described in Section \ref{cusped:section}, of the form
$$w_1\cdots w_h = e^{2 \pi i}.$$
Note that $e^{2 \pi i} \neq 1$ in $\widetilde{\matC^*}$, so by interpreting the consistency equations in $\widetilde{\matC^*}$ we have also incorporated the request that all angles sum to $2\pi$.

Let $z=(z_1,\ldots, z_n)$ be a solution to the consistency equations.
We have defined in Proposition \ref{mu:prop} a homomorphism $\mu\colon \pi_1(T_i) \to \matC^*$ for every boundary torus $T_i$, and we now lift it to $\widetilde{\matC^*}$. 

\begin{defn} \label{tilde:mu:defn}
Represent each non-trivial $\gamma \in \pi_1(T_i)$ as a simplicial path that lifts to an embedded path in the universal cover of $T_i$. Define $\tilde\mu(\gamma)$ to be $e^{-|\gamma| \pi i }$ times the product of all the moduli that $\gamma$ encounters at its right side, considered now as elements in the group $\widetilde{\matC^*}$. If $\gamma$ is trivial, set $\tilde\mu(\gamma) = 1$.
\end{defn}

\begin{ex} The element $\tilde\mu(\gamma)\in\widetilde{\matC^*}$ is well-defined and
$$\tilde\mu\colon \pi_1(T_i) \to \widetilde{\matC^*}$$
is a homomorphism.
\end{ex}

We now define some new \emph{completeness equations} at $T_i$ for each $i=1,\ldots, c$ that depend on the Dehn filling parameter $s_i$. There are two cases to consider for each $i=1,\ldots, c$. If $s_i = \infty$, the completeness equations relative to $T_i$ are the two equations 
$$\mu(m_i) = \mu(l_i) = 1$$ 
already considered in Section \ref{complete:solutions:subsection}. (If we wish, we can substitute them with the equations $\tilde\mu(m_i) = \tilde\mu(l_i) = 1$.
Both choices will work.) 

If $s_i = (p,q)$ we define one new completeness equation
$$\tilde\mu(m_i)^p \cdot \tilde\mu(l_i)^q = e^{2\pi i}.$$
The total number of completeness equations therefore varies from $c$ to $2c$, depending on the number of cusps that are left unfilled. The main goal of this section is to prove the following.

\begin{teo} \label{modified:equations:teo}
A solution $z = (z_1,\ldots, z_n)$ to the consistency and completeness equations determines a hyperbolic structure on $M$ whose completion $\overline M$ is a complete hyperbolic manifold diffeomorphic to $M^{\rm fill}$.
\end{teo}

If $s\neq (\infty, \ldots, \infty)$ the solution $z$ determines an incomplete hyperbolic metric on $M$, and the miracle here is that the completion $\overline M$ is another hyperbolic manifold! 

We note that both the consistency and completeness equations are of type $w_1\cdots w_h = 1$ or $e^{2\pi i}$.
The rest of this section is mainly devoted to the proof of Theorem \ref{modified:equations:teo}. We start with a short discussion that introduces (truncated) solid tori with cone angles: these objects will be crucial in the proof of the theorem.


\subsection{The infinite branched covering}
Let $l\subset \matH^3$ be any line and recall the universal cover
$$\pi \colon X \longrightarrow \matH^3 \setminus l$$ 
already considered in Section \ref{singularities:subsection} when we introduced manifolds with cone singularities. The manifold $X$ is incomplete and its completion $\overline X$ is obtained by adding a copy $\tilde l$ of $l$.

We use the half-space model and represent $l$ as the vertical axis, so that $\matH^3\setminus l = \matC^* \times \matR_{>0}$ and we can write
$$X = \widetilde{\matC^*} \times \matR_{>0}.$$ 

We note that $\widetilde{\matC^*}$ acts on $X$ via isometries: the element $w\in\widetilde{\matC^*}$ acts as
$$(z,t) \longmapsto (wz, |w| t).$$
When $w = e^{\alpha i}$ this is the rotation of angle $\alpha$ that was used to define hyperbolic cone manifolds. When $|w|\neq 1$ the map projects to a hyperbolic isometry of $\matH^3$ with axis $l$ and translation distance $\log |w|$.


\subsection{Tubes with cone angles}  \label{X:quotients:subsection}
A non-trivial discrete group $\Gamma <\widetilde{\matC^*}\isom \matC$ is either isomorphic to $\matZ$ or to $\matZ\times \matZ$; it acts freely on $X$ and (not necessarily freely!) on the line $\tilde l$. Concerning $\matZ\times \matZ$, there are two cases to consider.

If $\Gamma = \matZ\times \matZ$ contains a non-trivial rotation, it is generated by some maps
$$(z,t) \mapsto (e^{\alpha i}z, t), \quad (z,t) \mapsto e^\lambda(e^{\beta i}z, t)$$
with $\lambda\neq 0$, and it acts on $\tilde l$ as translations whose step is an integer multiple of $\lambda$. The quotient $\overline X/_{\Gamma}$ is naturally a complete hyperbolic manifold with cone angles: it is an open solid torus with singular locus a closed geodesic of length $|\lambda|$ and with cone angle $\alpha$. We call it a \emph{tube with cone angle $\alpha$}. When $\alpha = 2\pi$ we get an ordinary tube as in Section \ref{tubes:subsection}, with no singular points.

If $\Gamma = \matZ \times \matZ$ does not contain a rotation, it acts on $\tilde l$ as an indiscrete group of translations and hence $\overline X/_{\Gamma}$ is not a hyperbolic manifold with cone angles (it is not even Hausdorff). We also note that $\overline X/_{\Gamma}$ is not the completion of the hyperbolic manifold $X/_{\Gamma}$ in that case, but it only maps surjectively onto it: the completion adds a single point to $X/_{\Gamma}$.

Tubes have natural truncations. For every $R>0$ the $R$-neighbourhood $N_R(\tilde l)\subset \overline X$ of the singular line $\tilde l$ projects onto the $R$-neighbourhood $N_R(l)$ of $l$, which is a Euclidean cone with axis $l$. The group $\Gamma$ preserves $N_R(\tilde l)$ and in the first case its quotient is a truncated tube with cone angles.


\subsection{Incomplete solutions}
We now go back to our triangulation $\calT$, and we let $z = (z_1, \ldots, z_n)$ be a solution to the consistency equations for $\calT$. The solution $z$ furnishes a hyperbolic metric on $M$, which might not be complete: we want to understand the metric completion $\overline M$ of $M$. Recall that $M$ is diffeomorphic to the interior of a compact $N$ whose boundary consists of $c$ tori.

We pick a boundary torus $T\subset \partial N$ and define a \emph{collar} $C(T)\subset M$ of $T$ to be the intersection of a closed collar of $T$ in $N$ with $M$. We know from Proposition \ref{mu:equivalent:prop} that when $\mu\colon \pi_1(T) \to \matC^*$ is trivial there is a collar $C(T)$ isometric to a truncated cusp, that is the truncated quotient of $\matH^3$ by a discrete $\matZ \times \matZ$ of parabolic elements.

When $\mu$ is not trivial, we now show that a similar (but different) configuration arises: there is a collar $C(T)$ isometric to a truncated quotient of the hyperbolic manifold $X$ considered above by a discrete $\matZ \times \matZ$. The crucial difference is that $C(T)$ now is incomplete, because $X$ is. To prove this fact we use developing maps and holonomies.

The hyperbolic ideal triangulation $\calT$ of $M$ determined by $z$ lifts to a hyperbolic ideal triangulation $\tilde \calT$ for the universal cover $\tilde M \to M$ with infinitely many tetrahedra. The triangulated torus $T$ is the link of a vertex $v$ of $\calT$. We fix a lift $\tilde v$ of $v$ in $\tilde \calT$, and the link of $\tilde v$ is a triangulated surface $\tilde T$ that covers $T$. Since $T$ is incompressible, $\pi_1(T)$ injects in $\pi_1(M)$ and hence $\tilde T$ is a plane.

Recall from Section \ref{non-complete:subsection} that there is a developing map $D\colon \tilde {M} \to \matH^3$ and a holonomy $\rho\colon \pi_1(M) \to \Iso^+(\matH^3)$, and both are determined once we define $D$ on an ideal tetrahedron in $\tilde\calT$. We choose for our convenience one ideal tetrahedron incident to $\tilde v$ and we map it to the half-space model $H^3$ with an isometry $D$ that sends $\tilde v$ to $\infty$. 

The developing map $D$ sends all tetrahedra of $\tilde\calT$ incident to $\tilde v$ to vertical ideal tetrahedra in $H^3$ with one vertex at $\infty$. If $\gamma \in \pi_1(T)$, then $\rho(\gamma)$ permutes these tetrahedra and fixes $\infty$. Therefore the holonomy $\rho$ sends $\pi_1(T)=\matZ\times \matZ$ to a group of commuting elements in $\PSLC$ fixing $\infty$. Every such element may be written as $z\mapsto az+b$, and there are two possibilities:
\begin{itemize}
\item the group consists of translations $z \mapsto z+b$,
\item the group fixes a point $p\in\matC$.
\end{itemize}
In the second case we may suppose $p=0$ up to translating everything, so the maps are all of type $z\mapsto az$. Not surprisingly, the holonomy $\rho$ is tightly connected with the homomorphism $\mu\colon \pi_1(T) \to \matC^*$.
\begin{ex} \label{rho:derivative:ex}
The derivative $\rho(\gamma)'$, that is the coefficient $1$ or $a$ in the above examples, equals $\mu(\gamma)$. 
\end{ex}
We now suppose that $\mu$ is non-trivial and hence the first possibility is excluded: the group $\rho(\pi_1(T))$ consists of maps $z\mapsto az$ and we can identify $\rho$ with $\mu$. The map $D$ induces a developing map $D\colon \tilde T \to \matC$ with holonomy $\mu$.

\begin{prop}
The image $D(\tilde T)$ misses the origin.
\end{prop}
\begin{proof}
The vector field $v(z) = z$ on $\matC$ is $\mu(\pi_1(T))$-invariant and hence pulls-back via $D$ to a vector field on $T$. If $0\in D(\tilde T)$ then this vector field on $T$ has some zeroes, all with index $1$: a contradiction since $\chi(T)=0$.
\end{proof}

Let $\St_{\tilde v}\subset \tilde M$ be the open star of $\tilde v$, that is the union of all ideal tetrahedra incident to $\tilde v$, with the faces not incident to $\tilde v$ removed: it is homeomorphic to $\tilde T\times [0,+\infty)$ and hence simply connected. The proposition implies that the restriction $D|_{\St_{\tilde v}}$ of
the developing map misses the entire vertical line $l\subset \matH^3$ above the origin and hence lifts to a map 
$$\tilde {D} \colon \St_{\tilde v} \longrightarrow X.$$ 
Likewise the holonomy $\rho$ at $\pi_1(T)$ lifts to a holonomy 
$$\tilde \rho \colon \pi_1(T) \longrightarrow \widetilde{\matC^*} < \Iso^+(X)$$
which is of course related to the homomorphism $\tilde \mu\colon \pi_1(T) \to \widetilde{\matC^*}$.

\begin{ex} \label{tilde:rho:mu:ex}
We have $\tilde \rho = \tilde \mu$.
\end{ex}

After this long discussion, we can finally discover how a collar $C(T)$ of $T$ looks like.

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{Dehn_fill-BW}{Dehn_fill}} 
\nota{For sufficiently small $R>0$ the cone neighbourhood $N_R(\tilde l)$ of $\tilde l$ does not intersect the lower faces of the developed images of $\tilde\Delta_{i_1}, \ldots, \tilde\Delta_{i_h}$ (left). These tetrahedra intersect $\partial N_R(\tilde l)$ into triangles that glue up to determine a torus $T_R$ in $C(T)$ (right).}
\label{Dehn_fill:fig}
\end{center}
\end{figure}

\begin{prop} \label{DF:prop}
If $\mu$ is non-trivial then $\tilde\mu$ is injective and has discrete image. There is a collar $C(T)$ that is isometric to a truncation of $X/_{\img \tilde\mu}$.
\end{prop}
\begin{proof}
We have defined a lifted developing map $\tilde D\colon \St_{\tilde v} \to X$ with holonomy $\tilde\rho = \tilde \mu$.

Let $\Delta_{i_1}, \ldots, \Delta_{i_h}$ be the tetrahedra incident to $v$ (with multiplicities), and let $\tilde\Delta_{i_1}, \ldots, \tilde\Delta_{i_h}$ be any lifts in $\tilde\calT$ incident to $\tilde v$. We fix a sufficiently small $R_0>0$ such that the cone $N_{R_0}(\tilde l)\subset \overline X$ does not intersect the lower faces of the tetrahedra $\tilde D(\tilde\Delta_{i_1}), \ldots, \tilde D(\tilde\Delta_{i_h})$, see Figure \ref{Dehn_fill:fig}-(left). Since $N_{R_0}(\tilde l)$ is $\rho(\pi_1(T))$-invariant, it does not intersect the lower faces of any ideal tetrahedron in the image of $\tilde D$, and hence it intersects every ideal tetrahedron in a curved triangle as in Figure \ref{Dehn_fill:fig}-(right).

We define $\widetilde {C(T)}\subset \tilde M$ as the preimage of $N_{R_0}(\tilde l)$ along $\tilde D$. By construction it is a $\pi_1(T)$-invariant submanifold that projects to a submanifold $C(T) \subset M$. This submanifold intersects every tetrahedron incident to $v$ into a cone neighbourhood of $v$ and is hence a collar for $T$. We want to prove that the map
$$\tilde D\colon \widetilde {C(T)} \longrightarrow N_{R_0}(\tilde l) \setminus \tilde l$$
is an isometry. Being a local isometry, it suffices to prove that it is injective and surjective. We prove this using the natural foliation of $N_{R_0}(\tilde l)\setminus \tilde l$ into the sheets $\partial N_{R}(\tilde l)$ with $R\leqslant R_0$.

For every $R\leqslant R_0$ the map $\tilde D$ restricts to a local isometry of surfaces
$$\tilde D_R\colon \tilde {T}_R\to \partial N_R(\tilde l)$$
where $\tilde {T}_R = \tilde D^{-1}(\partial N_R(\tilde l))$ is $\pi_1(T)$-invariant and covers a torus $T_R\subset M$ parallel to $T$. Since $T_R$ is compact, the cover $\tilde T_R$ is complete. Therefore $\tilde D_R$ is a covering by Proposition \ref{local:isometry:prop} and is hence an isometry since $\partial N_R(\tilde l)$ is simply-connected. In particular it is a bijection for all $R<R_0$, and hence $\tilde D$ is a bijection.

Since $\tilde D$ is an isometry, its holonomy $\tilde\rho$ is discrete and injective and 
$$C(T) \isom \big(N_{R_0}(\tilde l) \setminus \tilde l \big)/_{\tilde\rho(\pi_1(T))}.$$
The proof is complete.
\end{proof}


\subsection{The completion}
We now have an isometric model for the collar $C(T)$ of $T$ and we study its completion. This analysis will lead to a proof of Theorem \ref{modified:equations:teo}.

We suppose that $\mu$ is non-trivial and hence $C(T)$ is not complete. By Proposition \ref{DF:prop}, the completion $\overline{C(T)}$ of $C(T)$ depends on the $\matZ\times \matZ$ group $\Img \tilde \mu< \widetilde{\matC^*}$ acting on $X$: see Section \ref{X:quotients:subsection} where we defined in particular the (truncated) tubes with cone angles. 

\begin{prop} \label{DF1:prop}
If $\Img \tilde \mu$ contains a non-trivial rotation then $\overline{C(T)}$ is a truncated tube with some cone angle; otherwise it is a one-point compactification of $C(T)$. 

In the first case, there are generators $\gamma, \eta$ for $\pi_1(T)$ such that 
$$\tilde \mu(\gamma) = e^{\alpha i}, \qquad \tilde \mu(\eta) = e^{\lambda + \beta i}$$
and the core geodesic of $\overline {C(T)}$ has cone angle $\alpha$ and length $|\lambda|$. The curve $\gamma$ is a meridian of the truncated tube.
\end{prop}
\begin{proof}
We know that $C(T)$ is isometric to a truncation of $X/_{\Img \tilde \mu}$ and we apply the discussion of Section \ref{X:quotients:subsection}.
\end{proof}

We now look at $M$ globally: every boundary torus $T_i\subset \partial N$ has its own homomorphisms $\mu$ and $\tilde \mu$.

\begin{cor} \label{DF2:cor}
Suppose that at every boundary torus $T_i\subset \partial N$ one of the following holds:
\begin{enumerate}
\item $\mu$ is trivial, or
\item there is a primitive $\gamma_i\in \pi_1(T_i)$ such that $\tilde\mu(\gamma_i) = e^{\alpha_i i}$.
\end{enumerate}
The completion $\overline M$ is a complete hyperbolic cone manifold obtained by Dehn filling the slopes $\gamma_i$. The core of the $i$-th Dehn filling is a closed geodesic with cone angle $\alpha_i$.
\end{cor}

Theorem \ref{modified:equations:teo} now follows immediately.

\dimo{modified:equations:teo}
The equation $\tilde\mu(m_i)^p\tilde\mu(l_i)^q = e^{2\pi i}$ implies that $\tilde\mu(pm_i + ql_i) = e^{2\pi i}$ and therefore the completion is a hyperbolic manifold (with no cone angles since $\alpha = 2\pi$) diffeomorphic to $M^{\rm fill}$.
\finedimo


\subsection{Generalised Dehn filling invariants} \label{generalized:DF:subsection}
We have proved Theorem \ref{modified:equations:teo} and we now make some comments that will be useful in the next chapter. Let $z$ be a solution of the consistency equations and consider a boundary torus $T_i\subset \partial N$ with fixed generators $m_i,l_i$ for $\pi_1(T)$.

\begin{prop} \label{pq:prop}
If $\mu$ is non-trivial, there is a unique $(p,q)\in\matR^2$ such that $\tilde\mu(m_i)^p \tilde\mu(l_i)^q = e^{2\pi i}$.
\end{prop}
\begin{proof}
We know from Proposition \ref{DF:prop} that $\tilde\mu$ is injective and has discrete image. Therefore $\tilde\mu(m_i)$ and $\tilde\mu(l_i)$ form a basis of $\widetilde{\matC^*}$ considered as a $\matR$-vector space.
\end{proof}

We now define the \emph{generalised Dehn filling invariant} $(p,q)\in S^2 = \matR^2 \cup \{\infty\}$ of the solution $z$ at the torus $T_i$ to be:
\begin{itemize}
\item $(p,q) = \infty$ if $\mu$ is trivial,
\item the $(p,q)\in\matR^2$ from Proposition \ref{pq:prop} if $\mu$ is non-trivial.
\end{itemize}

If $(p,q)=\infty$ there is a complete collar $C(T_i)$ of $T_i$ that is a truncated cusp; if $(p,q) \in \matR^2$ then Proposition \ref{DF:prop} provides a nice incomplete collar $C(T_i)$ and Proposition \ref{DF1:prop} tells us everything about its completion $\overline{C(T_i)}$. Namely, the following holds:

\begin{itemize}
\item if $\frac pq\in\matQ\cup \{\infty\}$ then $(p,q) = k(r,s)$ for a unique real number $k>0$ and coprime integers $(r,s)$, and $\overline{C(T_i)}$ is a solid torus with meridian $rm+sl$, isometric to a truncated tube with cone angle $\frac{2\pi}k$;
\item if $\frac pq \not\in \matQ \cup \{\infty\}$ then $\overline{C(T_i)}$ is the much less interesting one-point compactification.
\end{itemize}
We deduce the following:
\begin{itemize}
\item if $(p,q)$ are coprime integers then $\overline{C(T_i)}$ is a standard truncated tube; if this holds at all boundary tori $T_i$ then $\overline M$ is a hyperbolic manifold; 
\item if $(p,q)$ are integers then $k$ is a natural number and the cone angle divides $2\pi$; if this holds at all boundary tori $T_i$ then $\overline M$ may be interpreted as an orbifold thanks to Proposition \ref{from:cone:to:orbifold:prop};
\item if $\frac pq \in \matQ\cup \{\infty\}$ at all boundary tori $T_i$ then $\overline M$ is a hyperbolic cone manifold.
\end{itemize}

\begin{cor}
If the generalised Dehn filling invariants $(p,q)$ at each $T_i$ are either $\infty$ or coprime integers, the completion $\overline M$ is a complete hyperbolic manifold obtained by $(p,q)$-Dehn filling the cusps of the second type.
\end{cor}

We end this discussion by calculating $(p,q)$ explicitly. We define
$$u_i = \log \tilde \mu(m_i), \quad v_i = \log \tilde \mu(l_i)$$
and find the following.
\begin{prop} \label{pq:explicit:prop}
If $\mu$ is non trivial we have
$$p = - 2\pi\frac{\Re v_i}{\Im(\bar u_iv_i)}, \qquad 
q = 2\pi\frac{\Re u_i}{\Im(\bar u_iv_i)}.$$
\end{prop}
\begin{proof}
The pair $(p,q)$ is the unique solution of  
\begin{equation} \label{pquv:eqn}
pu_i + qv_i = 2\pi i
\end{equation}
when $u_i,v_i \neq 0$, or is $\infty$ otherwise. Note that $u_i=0 \Leftrightarrow v_i=0$.
The relation
$$i\Im (\bar u_iv) = -(\Re v_i)u_i + (\Re u_i)v_i$$
implies easily that the pair $(p,q)$ stated above is a solution to (\ref{pquv:eqn}).
\end{proof}



\subsection{Closed census}
The Lickorish-Wallace Theorem \ref{LW:teo} states that
every closed orientable three-manifold $M$ is the result of a Dehn surgery along some link $L\subset S^3$, and as such it can be easily presented to SnapPea. The program tries to solve numerically the consistency and completeness equations for $M$, based on some ideal triangulation for the complement of $L$.

If it succeeds to find a solution $z$, the closed manifold $M$ is hyperbolic and SnapPea calculates numerically various geometric invariants of $M$: the volume (which is just the sum of the volumes of the ideal tetrahedra), the length of the core geodesics of the filling solid tori (using Proposition \ref{DF1:prop}), a segment of the geodesic spectrum, a Dirichlet domain, etc.

Various closed manifolds $M$ have been tested and listed, and the ten closed hyperbolic three-manifolds of smallest volume known today are in Table \ref{closed:census:table}, taken from Hodgson -- Weeks \cite{Ho-We}.

\begin{table}
\begin{center}
\begin{tabular}{c||ccccccc}
Name & Volume & Homology & Symmetry & SG & C \\
 \hline \hline
Vol1 & $0.94270736$ & $\matZ_5+\matZ_5$ & $D_{12}$ & $0.5846$ & c \\
Vol2 & $0.98136883$ & $\matZ_5$ & $D_{4}$ & $0.5780$ & c \\
Vol3 & $1.01494161$ & $\matZ_3 + \matZ_6$ & $S_{16}$ & $0.8314$ & a \\
Vol4 & $1.26370924$ & $\matZ_5 + \matZ_5$ & $D_8$ & $0.5750$ & c \\
Vol5 & $1.28448530$ & $\matZ_6$ & $D_4$ & $0.4803$ & c \\
Vol6 & $1.39850888$ & $\{e\}$ & $D_4$ & $0.3661$ & c \\
Vol7 & $1.41406104$ & $\matZ_6$ & $D_4$ & $0.7941$ & c \\ 
Vol8 & $1.41406104$ & $\matZ_{10}$ & $D_4$ & $0.3648$ & c \\
Vol9 & $1.42361190$ & $\matZ_{35}$ & $D_4$ & $0.3523$ & c \\
Vol10 & $1.44069901$ & $\matZ_3$ & $D_4$ & $0.3615$ & c
\end{tabular}
\vspace{.2 cm}
\nota{The ten closed hyperbolic three-manifolds with smallest volume known. Here $S_{16}$ is the semidihedral group of order 16 with presentation $\langle x,y\ |\ x^8 = y^2 = 1, y^{-1}xy = x^3\rangle$, SG indicates the length of the shortest geodesics (volume and SG values are truncated after few digits), and C indicates whether the manifold is achiral (a) or chiral (c), that is whether it admits an orientation-reversing isometry or not.}
\label{closed:census:table}
\end{center}
\end{table}


\subsection{References}
The material contained in this chapter originated from Thurston's notes \cite{Th} and Neumann -- Zagier \cite{NZ}, see also Benedetti -- Petronio \cite{BP}. The program SnapPea is freely available and can now be used via a Python interface \cite{Sna}. We have used the computer censuses of Callahan -- Hildebrand -- Weeks \cite{CaHiWe}, Hoste -- Thistlethwaite -- Weeks \cite{HTW}, and Hodgson -- Weeks \cite{Ho-We}.

It is conjectured in \cite{A} that each link in Figure \ref{sequence:fig} with $c=1,\ldots, 5$ cusps has minimum volume among orientable hyperbolic manifolds with $c$ cusps. This has been proved for $c=1$ by Cao and Meyerhoff \cite{CM}, for $c=2$ by Agol \cite{A}, and for $c=4$ by Yoshida \cite{Yo}. The manifold Vol1 from Table \ref{closed:census:table} is called the \emph{Fomenko -- Matveev -- Weeks manifold} and has indeed smallest volume among all complete hyperbolic three-manifolds by Gabai -- R.~Meyerhoff -- P.~Milley \cite{GMM}.


\chapter{Hyperbolic Dehn filling} \label{Hyperbolic:Dehn:chapter}
We have completely classified in Chapter \ref{Seifert:chapter} the closed three-manifolds that belong to the six Seifert geometries, and now we long for a similar catalogue that displays all the closed hyperbolic three-manifolds that exist in nature. Is there something like a ``name'' to assign to each closed hyperbolic three-manifold, together with some reasonable tables that list all possible names?

There is not yet one such thing, and we do not know if there will ever be one: we still do not understand hyperbolic three-manifolds globally. The main difficulty is that there are really many hyperbolic three-manifolds around, so many that topologists often say informally that ``most three-manifolds are hyperbolic.''

This folk sentence is supported by a fundamental theorem that we prove in this chapter, the \emph{Hyperbolic Dehn filling Theorem}, which says roughly that by Dehn-filling generically a cusped hyperbolic three-manifold we still get a hyperbolic manifold.\index{hyperbolic Dehn filling theorem}


\section{Introduction}
It sometimes happens in three-dimensional topology, that a topological or geometric property of a manifold is preserved under Dehn fillings, with only few exceptions.
For instance, the Dehn filling of a Seifert manifold is again a Seifert manifold, with only one exception (a fibre-parallel Dehn filling gives a connected sum of Seifert manifolds, see Corollary~\ref{DF:Seifert:cor}).

The most striking appearance of this phenomenon is the Hyperbolic Dehn filling Theorem, proved by Thurston at the end of the 1970s. This theorem says roughly that ``most'' Dehn fillings of a cusped hyperbolic manifold are still hyperbolic.


\subsection{Generalised Dehn filling parameters} \label{generalised:subsection}
In all this chapter, we consider a compact oriented three-manifold $N$ with $\partial N = T_1 \sqcup \ldots \sqcup T_c$ consisting of tori, and we fix generators $m_i,l_i$ for every $\pi_1(T_i)$. 

Let a \emph{generalised Dehn filling parameter} $s=(s_1,\ldots, s_c)$ be a sequence where each $s_i$ is either the symbol $\infty$ or a rationally related pair of real numbers $(p,q) = (kp',kq') = k(p',q')$ where $k>0$ is real and $(p',q')$ are coprime integers. We think at $s_i$ as lying in the two-sphere $S^2 = \matR^2 \cup \{\infty\}$.

A generalised Dehn filling parameter $s$ determines a Dehn filling $N^{\rm fill}$ of $N$ as follows:
for every $i$, if $s_i=k(p',q')$ we fill $T_i$ by killing the slope $p'm_i + q'l_i$, while if $s_i=\infty$ we do nothing. The result is a new compact manifold, that may be closed (if there are no $\infty$ in $s$) or be bounded by some tori. We also mark the cores of the filled solid tori with the label $\alpha_i = \frac{2\pi} k>0$. 


\subsection{The Hyperbolic Dehn filling Theorem}
This chapter is mainly devoted to the proof of the following theorem. 

\begin{teo} \label{DF:teo} \label{hyperbolic:Dehn:filling:teo}
Let $M = \interior N$ be a complete orientable finite-volume cusped hyperbolic three-manifold. There is a neighbourhood $U$ of $(\infty,\ldots,\infty)$ in $S^2\times \ldots \times S^2$ such that for every generalised Dehn filling parameter $s \in U$ the interior $M^{\rm fill}$ of the manifold $N^{\rm fill}$ obtained by Dehn filling $N$ along $s$ admits a finite-volume complete hyperbolic structure with cone angles. 

The cores of the filling solid tori are closed geodesics with cone angles $\alpha_i$. The singular locus of $M^{\rm fill}$ consists of the core geodesics with $\alpha_i \neq 2\pi$.
\end{teo}

If $s\in U$ is an ordinary (not extended) Dehn filling parameter (see Section \ref{DF:parameters:subsection}), that is if $s_i$ is either $\infty$ or a coprime pair $(p,q)$ for all $i$, then $\alpha_i = 2\pi$ and $N^{\rm fill}$ is a hyperbolic manifold without cone angles: this is of course the case of most interest. 

\begin{cor}
Let $M = \interior N$ be a complete orientable finite-volume hyperbolic three-manifold. For every $i=1,\ldots, c$ there is a finite set $S_i$ of slopes in $T_i$ such that for every Dehn filling parameter $s$ with $s_i \not \in S_i$ for all $i$, the filled manifold $M^{\rm fill} = \interior{N^{\rm fill}}$ is hyperbolic.
\end{cor}

When $M$ has one cusp, the corollary may be stated simply as follows.

\begin{cor}
If $M$ is a complete orientable finite-volume hyperbolic three-manifold with one cusp, all but finitely many Dehn fillings $M^{\rm fill}$ are hyperbolic.
\end{cor}

To appreciate the power of these theorems, consider for instance a hyperbolic link $L\subset S^3$ (recall that $L\subset S^3$ is hyperbolic if $S^3\setminus L$ admits a finite-volume complete hyperbolic metric). By the hyperbolic Dehn filling theorem, there is a finite subset $S\subset \matQ$ such that every surgery on $L$ with coefficients in $\matQ\setminus S$ produces a closed hyperbolic manifold.


\subsection{Examples} We describe a couple of clarifying examples. We know that the figure eight knot $K\subset S^3$ is hyperbolic: by the Dehn filling Theorem, there is an open neighbourhood $U \subset S^2$ of $\infty$ such that every Dehn surgery on $K$ with parameter $s\in U$ produces a hyperbolic cone manifold. 

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{figure8_U-BW}{figure8_U}} 
\nota{Hyperbolic Dehn fillings on the figure-eight knot complement.}
\label{figure8_U:fig}
\end{center}
\end{figure}

We will prove in the next section that the subset $U$ shown in Figure \ref{figure8_U:fig} fulfils this requirement. The only coprime pairs $(p,q)$ that are not contained in $U$ are those with $\frac pq$ equal to one of the following
\begin{equation} \label{K:list:eqn}
-4,-3,-2,-1,0,1,2,3,4,\infty.
\end{equation}
Every other surgery on $K$ yields a closed hyperbolic three-manifold. For instance, the manifold Vol2 from Table \ref{closed:census:table} can be obtained with $\frac pq = \pm 5$ (there is a symmetry of $K$ sending $\frac pq$ to $-\frac pq$).

On the other hand, a $\frac pq$ surgery from the list (\ref{K:list:eqn}) does not produce a hyperbolic manifold: see Table \ref{non:hyp:table}, taken from Martelli -- Petronio \cite{MP}.

\begin{table}
\begin{center}
\begin{tabular}{c||c}
$\frac pq$ & manifold \phantom{\Big|}\!\! \\
\hline
\hline
$0$ & $T_{\matr 31{-1}0}$ \phantom{\Big|}\!\!  \\
$\pm 1$ & $\big(S^2, (2,1), (3,1), (7,-6)\big)$  \phantom{\Big|}\!\! \\
$\pm 2$ & $\big(S^2, (2,1), (4,1), (5,-4)\big)$  \phantom{\Big|}\!\! \\
$\pm 3$ & $\big(S^2, (3,1), (3,1), (4,-3)\big)$  \phantom{\Big|}\!\! \\
$\pm 4$ & $\big(D,(2,1), (2,1)\big) \bigcup_{\matr 0110} \big(D, (2,1), (3,1)\big) $\phantom{\Big|}\!\!
\end{tabular}
\vspace{.2 cm}
\nota{The non-hyperbolic Dehn surgeries of the figure-eight knot. We get a torus bundle with Anosov monodromy and hence of $\Sol$ geometry, three Seifert manifolds of $\widetilde {\SL_2}$ geometry, and a graph manifold that splits into two Seifert manifolds via a map that interchanges the fibres and the boundary sections of the two portions (the map is here denoted by a matrix in the section-fibre basis).}
\label{non:hyp:table}
\end{center}
\end{table}

More generally, a parameter $k(p,q) \in U$ produces a hyperbolic closed manifold with a core geodesic of cone angle $\frac{2\pi}k$, which may be interpreted as an orbifold when $k\in \matN$. In particular, if $(p,q) = (1,0)$ the closed manifold is just $S^3$, because an $\infty$-surgery on a knot in $S^3$ gives $S^3$ back. Therefore by looking at Figure \ref{figure8_U:fig} we discover that for every $k\geqslant 5$ there is a hyperbolic structure on $S^3$ with cone angle $\frac{2\pi}k$ on the figure-eight knot $K$. 

We now consider a link with two components.
The \emph{Whitehead link} $L$ shown in Figure \ref{sequence:fig} is hyperbolic: it is hard to determine an explicit open set $U\subset S^2\times S^2$ in this case, but a careful computer-aided analysis carried with SnapPy \cite{Sna} shows the following, see \cite{MP}.

\begin{teo}
A surgery on the Whitehead link with coefficients $(\frac pq, \frac rs)$ produces a closed hyperbolic manifold, unless one of the following holds:
\begin{itemize}
\item $\frac pq$ or $\frac rs$ belongs to the set $\{0, 1, 2, 3, 4, \infty\}$,
\item up to permutation the pair $\big( \frac pq, \frac rs \big)$ belongs to the set
$$\left\{ (-4,-1), (-3,-1), (-2,-2), (-2,-1), \left(\tfrac 32, 5\right), \left(\tfrac 43, 5\right) \left(\tfrac 52, \tfrac 72\right) \right\}.$$
\end{itemize}
\end{teo}
The proposition is symmetric in the two coefficients because the link itself has a symmetry that interchanges the two components. All the Dehn filling parameters listed in the theorem indeed produce non-hyperbolic manifolds. For instance, if $\frac pq\in \{1,2,3\}$ we get a Seifert manifold fibering over the disc with two singular fibres, see \cite{MP}.

We first prove Theorem \ref{hyperbolic:Dehn:filling:teo} for the figure-eight knot, where the combinatorics is so simple that everything can be verified by hand.
We will then prove the theorem in general in Section \ref{solution:space:section} using more sophisticated tools.


\subsection{The figure-eight knot example} \label{figure:8:example:subsection}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{triangulation_figure8_2-BW}{triangulation_figure8_2}} 
\nota{We truncate the tetrahedra and flatten their boundary. We assign a modulus $z$ and $w$ to them. The edge numbered $i=1,2,3$ has modulus $z_i$ (on the left tetrahedron) or $w_i$ (on the right tetrahedron).}
\label{triangulation_figure8_2:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{triangulation_figure8_3-BW}{triangulation_figure8_3}} 
\nota{The triangulated boundary is a torus obtained by identifying the opposite edges of this parallelogram. The triangulation $\calT$ has two edges, that we colour in \iftoggle{BW}{grey}{red} and white. Their endpoints are shown here.}
\label{triangulation_figure8_3:fig}
\end{center}
\end{figure}

We now discuss in detail the standard example: the figure-eight knot complement, one of the very few cases where the consistency and completeness equations can be solved by hand. This part will not be needed in the proof of Theorem \ref{hyperbolic:Dehn:filling:teo}, so the reader may wish to skip it and go directly to Section \ref{sketch:filling:subsection}.

Let $\calT$ be the triangulation with two tetrahedra shown in Figure \ref{triangulation_figure8:fig}. The truncated version is in Figure \ref{triangulation_figure8_2:fig}. We assign the complex variable $z$ and $w$ to the left and right tetrahedron, respectively. We set
$$z_1 = z, \quad z_2 = \frac{1}{1-z}, \quad z_3 = \frac {z-1}{z}$$
and define $w_1,w_2,w_3$ similarly. Recall that
\begin{equation} \label{m1:eq}
z_1z_2z_3 = w_1w_2w_3 = -1.
\end{equation}
The modulus of an edge in Figure \ref{triangulation_figure8_2:fig} labeled with $i\in \{1,2,3\}$ is $z_i$ or $w_i$ depending on the tetrahedron. With some patience one sees that the boundary triangulated surface is a torus $T$ as in Figure \ref{triangulation_figure8_3:fig}. The triangulation $\calT$ has two edges shown in Figure \ref{triangulation_figure8:fig}, each yielding a consistency equation. Figure \ref{triangulation_figure8_3:fig} shows that the consistency equations are
$$z_2^2z_3w_2^2w_3 = 1, \quad z_1^2z_3w_1^2w_3=1.$$
Using (\ref{m1:eq}) we see that the equations are both equivalent to 
$$z_2w_2 = z_1w_1,$$ 
that is
\begin{equation} \label{c:eqn}
z(1-z)w(1-w) = 1.
\end{equation}
We now look at the boundary torus $T$. Let $m$ and $l$ be the generators of $\pi_1(T)$ shown in Figure \ref{triangulation_figure8_3:fig}. We have
\begin{equation} \label{ml:eqn}
\mu(m) = - z_1z_3w_1 = w(1-z), \quad \mu(l) = z_2^2z_3^2w_1^4w_2^2w_3^2 = \frac{z^2}{w^2}.
\end{equation}
The completeness equations are
\begin{equation} \label{c2:eqn}
w(1-z) = 1,\quad z^2 = w^2.
\end{equation}

\begin{ex}
The only solution to (\ref{c:eqn}) and (\ref{c2:eqn}) is $z=w= e^{\frac{\pi i}3}$.
\end{ex}

We have confirmed that the figure-eight complement $M$ has a complete hyperbolic structure obtained by representing both tetrahedra with ideal regular hyperbolic tetrahedra. We now investigate the non-complete solutions of the consistency equations.

The two ideal tetrahedra have moduli $w$ and $z$ and the consistency equations reduce to one equation (\ref{c:eqn}) which we rewrite as
$$z^2 - z +\frac{1}{w(1-w)} = 0.$$
The solutions are
$$ z = \frac{1 \pm \sqrt{1-\frac 4{w(1-w)}}}{2}.$$
We are only interested in solutions with $\Im z, \Im w>0$. For every $w$ with $\Im w>0$ there is a unique solution $z$ with $\Im z >0$, except when $\Delta \in \matR_{\geqslant 0}$.

\begin{ex} 
We have $\Delta = 1-\frac 4{w(1-w)}\in\matR_{\geqslant 0}$ if and only if $w$ belongs to the half-line $s = \big\{\frac 12 + yi {\rm\ with\  } y\geqslant \frac{\sqrt{15}}2\big\}$, see Figure \ref{figure8_R:fig}-(left).
\end{ex}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{figure8_R-BW}{figure8_R}} 
\nota{Every $w\in R$ determines a hyperbolic structure for $M$ (left). The Dehn filling generalised invariants $d$ map $R$ onto a neighbourhood of $\infty$ (right).}
\label{figure8_R:fig}
\end{center}
\end{figure}

We define the open region 
$$R =  \{w\in \matC\ |\ \Im w >0 \} \setminus s.$$
Every $w\in R$ determines a hyperbolic structure for $M$. The complete structure is obtained at $w_0=\frac 12 + \frac {\sqrt 3}2$, see Figure \ref{figure8_R:fig}-(left). 

The manifold $M$ is a knot complement and hence the boundary torus $T$ is equipped with its natural meridian/longitude basis $m',l'$, see Section \ref{canonical:longitudes:subsection}. Using SnapPea we find out that
$$m'=m, \qquad l'=l+2m.$$
From (\ref{ml:eqn}) we get
\begin{equation} \label{mlp:eqn}
 \tilde\mu(m') = w(1-z), \quad \tilde\mu(l') = \frac{z^2}{w^2} w^2(1-z)^2 = z^2(1-z)^2. 
\end{equation}
We fix $m',l'$ as generators for $\pi_1(T)$. We defined in Section \ref{generalized:DF:subsection} the generalised Dehn surgery invariant $(p,q) = d(w)$ for every non-complete solution $w\in R \setminus \{w_0\}$. This gives a continuous map
$$d \colon R \longrightarrow S^2$$
that sends $w_0$ to $\infty$.
\begin{prop}
The image $d(R)$ contains the coloured region shown in Figure \ref{figure8_R:fig}-(right).
\end{prop}
\begin{proof}
The domain $R$ is an open disc and its abstract closure $\bar R$ is homeomorphic to the closed disc. We show that $d$ extends to a continuous map $\bar R \to S^2$ which sends $\partial R$ to the almost-rectangle shown in Figure \ref{figure8_R:fig}. 

The invariants $d(w) = (p,q)$ are such that
\begin{equation} \label{pq:eqn}
w^p(1-z)^{p+2q}z^{2q} = e^{2\pi i}.
\end{equation}

The region $R$ has two involutions (determined in fact by isometries of $M$):
\begin{itemize}
\item the involution $\tau(w) = z = \frac{1 \pm \sqrt{1-\frac 4{w(1-w)}}}{2}$. This involution sends $\mu(m)$ to $\mu(m)^{-1} = \mu(m^{-1})$, hence $d(\tau(w)) = -d(w)$;
\item the involution $\sigma(w) = \overline{1-w}$: using (\ref{mlp:eqn}) we get $d(\sigma(w)) = \overline{d(w)}$.
\end{itemize}
Now we note that when $w$ tends to a point in the line $l_+ = [1, +\infty]$ then $z$ tends to a point in $l_- = [-\infty,0]$. Therefore the argument of $w,z,1-z$
tends respectively to $0, \pi, 0$. Equation (\ref{pq:eqn}) implies that $q \to 1$.

If $w\to 1$ then $z \to -\infty$ and (\ref{pq:eqn}) implies that $p+2q+2q=p+4q\to 0$, so $(p,q)\to (-4,1)$. If $w\to +\infty$ then $z \to 0$ and equation $z(1-z)w(1-w)=1$ implies that $|z||w|^2\to 1$; here (\ref{pq:eqn}) gives $|w|^{p-4q}\to 1$, hence $p-4q\to 0$, so $(p,q)\to (4,1)$. We have proved that $d$ maps $[1,+\infty]$ onto the segment 
$$\overline{(-4,+1), (+4,+1)}.$$
Using the involution $\tau$ we deduce that $d$ maps $[-\infty, 0]$ onto the segment
$$\overline{(+4,-1),(-4,-1)}.$$
When $w$ is near the right side of the half-line $s$, the number $z$ tends to the segment $(0,\frac 12]$. Therefore the arguments of $z$ and $1-z$ tend to $0$ and (\ref{pq:eqn}) implies that the argument of $w^p$ tends to $2\pi$. When $w\in s$ the argument of $w$ is at least $\arctan \sqrt{15} = 1.31811607\ldots $ and hence $p$ is at most $\frac{2\pi}{\arctan \sqrt{15}} = 4.374\ldots < 5$. This implies that we can connect $(4,1)$ and $(4,-1)$ while staying inside the image of $d$ with a curve as in Figure \ref{figure8_R:fig}.
\end{proof}


\subsection{A road map} \label{sketch:filling:subsection}
The rest of this chapter is mostly devoted to the proof of Theorem \ref{hyperbolic:Dehn:filling:teo}. Here is our plan: we first study the combinatorial properties of an arbitrary ideal triangulation $\calT$ for $M$, and we prove that the solutions to the consistency equations form a complex manifold $\Def(M,\calT)$ of (complex) dimension $c$ equal to the number of cusps of $M$. The manifold $\Def(M,\calT)$ is nicely parametrized by the holonomies on any $c$ fixed curves at different cusps. 

The manifold $\Def(M,\calT)$ is often empty, but since $M$ is hyperbolic we expect that there should be some ideal triangulation $\calT$ for which $\Def(M,\calT)$ is not empty and contains a solution $z$ that also satisfies the completeness equations (we are unfortunately not able to prove this in general, and this will be a technical issue). The generalised Dehn filling invariants defined in Section \ref{generalized:DF:subsection} furnish a local diffeomorphism $d\colon \Def(M,\calT) \to S^2 \times \ldots \times S^2$ that sends $z$ to $(\infty,\ldots,\infty)$. In particular this map is open and its image covers a neighbourhood $U$ of $(\infty,\ldots, \infty)$. We conclude thanks to the discussion of Section \ref{generalized:DF:subsection}. 

We start by defining and exploring the solution space $\Def(M,\calT)$.
