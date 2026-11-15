---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-029-52-extensions-of-homotopies
section_title: "Extensions of homotopies"
section_number: 5.2
pages: 151-161
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.952
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
This section is entirely devoted to the proof of the following theorem. Recall that every map $f\colon M\to N$ between connected manifolds lifts to a (non-unique) map $\tilde f\colon \tilde M \to \tilde N$ between their universal covers.
\begin{teo} \label{estensione:teo}
Let $f\colon M \to N$ be a smooth homotopy equivalence between closed hyperbolic $n$-manifolds. Every lift $\tilde f\colon \matH^n \to \matH^n$ extends to a continuous map $\tilde f\colon \overline{\matH^n} \to \overline{\matH^n}$ whose restriction $\tilde f|_{\partial \matH^n}\colon \partial \matH^n \to \partial \matH^n$ is a homeomorphism.
\end{teo}

Every smooth homotopy equivalence extends to a homeomorphism of the boundaries of the universal coverings. This theorem will have important consequences in the Chapters \ref{automorphisms:chapter} and \ref{Mostow:chapter}.
To prove it, we need to define a weaker notion of isometry.


\subsection{Quasi-isometries}

We introduce the following.\index{quasi-isometry}

\begin{defn} A map $F\colon X \to Y$ between metric spaces is a \emph{quasi-isometry} if there are two constants $C_1>0$, $C_2\geqslant 0$ such that
$$\frac 1 {C_1} d(x_1,x_2) - C_2 \leqslant d(F(x_1), F(x_2)) \leqslant C_1d(x_1,x_2) + C_2$$
for all $x_1,x_2 \in X$ and $d(F(X),y)\leqslant C_2$ for all $y\in Y$.
\end{defn}
A quasi-isometry is an isometry up to some error: note that $F$ might neither be continuous nor injective. Two metric spaces are \emph{quasi-isometric} if there is a quasi-isometry $F\colon X \to Y$ (which implies the existence of a quasi-isometry $G\colon Y\to X$, exercise) and quasi-isometry is an equivalence relation between metric spaces. Intuitively, looking at a space up to quasi-isometries is like watching it from some distance. Compact metric spaces are obviously quasi-isometric to a point. 

This notion is an important ingredient in \emph{geometric group theory}: one may for instance give every finitely-presented group $G$ a canonical metric (through its \emph{Cayley graph}), uniquely determined up to quasi-isometries.\index{geometric group theory}\index{Cayley graph} 


\subsection{Pseudo-isometries}
Let $f\colon M \to N$ be a homotopic equivalence between closed hyperbolic $n$-manifolds. Every continuous function is homotopic to a smooth one, hence we suppose that $f$ is smooth. The map lifts to a map $\tilde f\colon \matH^n \to \matH^n$. We will prove that $\tilde f$ is a quasi-isometry. Actually, the map $\tilde f$ is also continuous and (as we soon see) Lipschitz: it will be useful for us to retain this information on $\tilde f$ to simplify some arguments, so we introduce a different (more restrictive but less natural) version of a quasi-isometry.\index{pseudo-isometry}

\begin{defn} A map $F\colon X \to Y$ between metric spaces is a \emph{pseudo-isometry} if there are two positive constants $C_1, C_2>0$ such that
$$\frac 1 {C_1} d(x_1,x_2) - C_2 \leqslant d(F(x_1), F(x_2)) \leqslant C_1d(x_1,x_2)$$
for all $x_1,x_2 \in X$.
\end{defn}
In particular a pseudo-isometry is $C_1$-Lipschitz and hence continuous. Let $f\colon M \to N$ be a smooth map between Riemannian $n$-manifolds; the \emph{maximum dilatation} of $f$ at a point $x\in M$ is the maximum ratio $\frac{\|df_x(v)\|}{\|v\|}$ where $v$ varies among all the unitary vectors in $T_x$. The maximum dilatation of $f$ is the supremum of all maximum dilatations as $x \in M$ varies.\index{maximum dilatation} 

\begin{ex}
If $f\colon M\to N$ has maximum dilatation $C$ the map $f$ is $C$-Lipschitz.
\end{ex}

\begin{prop} \label{pseudo-isometria:prop}
Let $f\colon M\to N$ be a smooth homotopy equivalence of closed hyperbolic $n$-manifolds. The lift $\tilde f\colon \matH^n \to \matH^n$ is a pseudo-isometry.
\end{prop}
\begin{proof}
Since $M$ is compact, the map $f$ has some finite maximum dilatation $C$. Since $\tilde f$ is locally like $f$, it also has maximum dilatation $C$ and is hence $C$-Lipschitz. The same holds for the homotopic inverse $g\colon N\to M$. Therefore there is a $C_1>0$ such that
\begin{align*}
d\big(\tilde f(x_1), \tilde f(x_2)\big) & \leqslant C_1 \cdot d(x_1,x_2) \quad \forall x_1,x_2 \in \matH^n, \\
d\big(\tilde g(y_1), \tilde g(y_2)\big) & \leqslant C_1 \cdot d(y_1,y_2) \quad \forall y_1,y_2 \in \matH^n.
\end{align*}
We have $M = \matH^n/_\Gamma$.
Being a composition of lifts, the map $\tilde g \circ \tilde f$ commutes with $\Gamma$ and has maximum displacement bounded by some $K>0$ equal to the maximum displacement of the points in a (compact) Dirichlet domain. Hence
$$d(x_1,x_2) - 2K \leqslant d\big( \tilde g (\tilde f(x_1)), \tilde g (\tilde f(x_2)) \big) \leqslant C_1 \cdot d\big(\tilde f(x_1), \tilde f(x_2)\big) $$
for all $x_1,x_2 \in \matH^n$. Therefore $\tilde f$ is a pseudo-isometry with $C_2 = 2K/C_1$.
\end{proof}


\subsection{Boundary extension of a pseudo-isometry}
We now prove that not only pseudo-isometries $\matH^n \to \matH^n$ extend at infinity, but their extensions at $\partial \matH^n$ eliminate the ``errors'' and behave nicely.
\begin{teo} Every pseudo-isometry $F\colon \matH^n \to \matH^n$ extends to a continuous map $F\colon \overline{\matH^n} \to \overline{\matH^n}$ that injects $\partial\matH^n$ into itself.
\end{teo}
We separate the proof in some lemmas.

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{cosh-BW}{cosh}} 
\nota{We use the half-space model. The hyperbolic cosine of the distance between $x$ and $\pi(x)$ is the inverse of the cosine of $\theta$ (left). To determine the maximum dilatation we decompose the tangent space $T_x$ orthogonally as $U\oplus V$ (right).}
\label{cosh:fig}
\end{center}
\end{figure}

\begin{lemma} \label{cosh:cos:lemma}
Consider the picture in Figure \ref{cosh:fig}. We have
$$\cosh d(x,\pi(x)) = \frac 1{\cos \theta}.$$
\end{lemma}
\begin{proof} We can work with the half-plane model $H^2\subset \matC$ and up to translations and dilations suppose that $\pi(x)=i$. The geodesic $r$ is parametrized as $ie^t$. The M\"obius transformation $z \mapsto \frac{z+1}{-z+1}$ sends $r$ to $\gamma$ and fixes $i$, hence $\gamma(t) = \frac{ie^{t}+1}{-ie^{t}+1}.$
Set $s=d(x, \pi(x))$. We get $ x = \frac{ie^{s}+1}{-ie^{s}+1}$ and
$$\cos\theta = \Im x = \Im \frac{(ie^s+1)^2}{e^{2s}+1} = \frac{2e^s}{e^{2s}+1} = \frac 2{e^s+e^{-s}} = \frac 1 {\cosh s}.$$
The proof is complete.
\end{proof}

\begin{lemma} \label{dilatation:lemma}
Let $r\subset \matH^n$ be a line and $\pi\colon \matH^n \to r$ be the orthogonal projection to $r$. The maximum dilatation of $\pi$ at $x\in\matH^n$ is
$$d =\frac 1 {\cosh s}$$
where $s=d(x,r)$.
\end{lemma}
\begin{proof}
We use the half-space model with $r$ and $x$ as in Figure \ref{cosh:fig}-(left): we know that $\cosh s = \frac 1 {\cos \theta}$. We have $T_x=U\oplus V$ as in Figure \ref{cosh:fig}-(right) with $V= \ker d\pi_x$. A generator $u$ of $U$ is just rotated by $d\pi_x$ with respect to the Euclidean metric; with respect to the hyperbolic metric  we have
$$\frac{\|d\pi_x(u)\|}{\|u\|} = \frac {x_n}{\pi(x)_n} = \cos\theta = \frac 1{\cosh s}.$$
The proof is complete.
\end{proof}

We write $\overline{pq}$ for the segment with endpoints $p$ and $q$ and we denote by $N_r(A)$ the $r$-neighbourhood of $A$. 

\begin{lemma}
Let $F\colon\matH^n\to\matH^n$ be a pseudo-isometry. There is a $R>0$ such that
$$F(\overline{pq}) \subset N_R\big(\overline{F(p)F(q)}\big)$$ 
for all distinct points $p,q\in\matH^n$. 
\end{lemma}
\begin{proof}
Let $C_1, C_2$ be the pseudo-isometry constants of $F$. Fix a sufficiently big $R$ so that $\cosh R > 2C_1^2$. Let $l$ be the line containing $F(p)$ and $F(q)$.  We show that $F(\overline{pq})$ can exit from $N_R(l)$ only for a limited amount of time. Let $\overline {rs} \subset \overline {pq}$ be a maximal segment where $F(\overline{rs})$ is disjoint from the interior of $N_R(l)$, as the \iftoggle{BW}{dark grey}{blue} arc in Figure \ref{Mostow:fig}-(left). We have

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{Mostow0-BW}{Mostow0}} 
\nota{We use the \iftoggle{BW}{grey}{red} paths to estimate the distance between $F(r)$ and $F(s)$. On the left: since $F$ is $C_1$-Lipschitz, the \iftoggle{BW}{dark grey}{blue} path has length at most $C_1 d(r,s)$. Its projection onto $l$ has dilatation at most $1/{\cosh R}$ by Lemma \ref{dilatation:lemma}, hence the \iftoggle{BW}{grey}{red} path in $l$ has length at most $C_1d(r,s)/\cosh R$. Therefore $d(F(r), F(s)) \leqslant C_1 \frac {d(r,s)}{\cosh R} + 2R$. On the right we get $d(F(r), F(s)) \leqslant 2R$.}
\label{Mostow:fig}
\end{center}
\end{figure}

\begin{equation*}
\frac 1{C_1} d(r,s) - C_2 \leqslant d(F(r), F(s)) \leqslant C_1d(r,s). 
\end{equation*}
We can improve the right inequality as shown in Figure \ref{Mostow:fig}-(left) and write
$$\frac{1}{C_1}d(r,s) - C_2 \leqslant d(F(r), F(s)) \leqslant C_1\frac{d(r,s)}{\cosh R} + 2R.$$
Therefore
$$\left( \frac 1{C_1} - \frac{C_1}{\cosh R}\right)d(r,s) \leqslant 2R + C_2.$$
Since $\cosh R > 2C_1^2$ we deduce that $d(r,s) < M$ for some constant $M$ that depends only on $C_1$ and $C_2$. 

We have proved that $F(\overline {pq})$ may exit from $N_R(l)$ only on subsegments of $\overline{pq}$ with length $<M$. Since $F$ is $C_1$-Lipchitz the curve $F(\overline{pq})$ lies entirely in $N_{R+C_1M}(l)$, and we replace $R$ with $R+C_1M$.

It remains to prove that $F(\overline{pq})$ lies entirely (up to taking a bigger $R$) in the bounded set $N_R(\overline{F(p)F(q)})$: the proof is analogous and easier, since Figure \ref{Mostow:fig}-(right) shows that $d(F(r), F(s))\leqslant 2R$. 
\end{proof}

In the previous and following lemmas, the constant $R$ depends only on the pseudo-isometry constants $C_1$ and $C_2$.

\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{Mostow2-BW}{Mostow2}} 
\nota{For every $0<u<t$, the point $F(l(u))$ is contained in the (\iftoggle{BW}{light grey}{yellow}) $R$-neighbourhood of $\overline{F(p) F(l(t))}$. If $u$ is big, the \iftoggle{BW}{}{blue }segment $\overline{F(p)F(l(u))}$ is long, while the \iftoggle{BW}{grey}{red} one is bounded by $R$: hence the angle $\alpha_{tu}$ between $v_t$ and $v_u$ is small. Therefore $v_t$ is a Cauchy sequence.}
\label{Mostow2:fig}
\end{center}
\end{figure}

\begin{lemma} \label{half:lemma}
Let $F\colon \matH^n \to \matH^n$ be a pseudo-isometry. There is a $R>0$ such that for all $p\in\matH^n$ and every half-line $l$ starting from $p$ there is a unique half-line $l'$ starting from $F(p)$ such that
$$F(l) \subset N_R(l').$$
\end{lemma}
\begin{proof}
We parametrize $l$ as a geodesic $l\colon [0,+\infty) \to \matH^n$ with unit speed. We have $l(0)=p$. Since $F$ is a pseudo-isometry we get 
$$\lim_{t\to\infty} d\big(F(p), F(l(t))\big) = \infty.$$
Let $v_t\in T_{F(p)}$ be the unitary tangent vector pointing towards $F(l(t))$:
Figure \ref{Mostow2:fig} shows that $\{v_t\}_{t\in\matN}$ is a Cauchy sequence, hence it converges to a unitary vector $v\in T_{F(p)}$. Let $l'$ be the half-line starting from $F(p)$ with direction $v$. It is easy to check that $F(l)\subset N_R(l')$ and $l'$ is the unique half-line from $p$ with this property. 
\end{proof}
The previous lemma gives a recipe to transform every half-line $l$ into a half-line $l'$ that approximates $F(l)$. Since $\partial \matH^n$ is an equivalence relation of half-lines, we define the extension $F\colon\partial\matH^n \to \partial \matH^n$ by sending $l$ to $l'$.

\begin{lemma}
The boundary extension $F\colon \partial \matH^n \to \partial\matH^n$ is well-defined and injective.
\end{lemma}
\begin{proof}
Let $l_1, l_2$ be two half-lines at bounded distance $d(l_1(t), l_2(t))<M$ for all $t$. If $d(l_1'(t), l_2'(t)) \to \infty$ we get $d\big(F(l_1(t)), F(l_2(t))\big) \to +\infty$, a contradiction since $F$ is Lipschitz. Therefore $l_1',l_2'$ are at bounded distance and $F$ is well-defined.

Injectivity is proved analogously: if $l_1$ and $l_2$ are divergent then $l_1'$ and $l_2'$ also are because $F$ is a pseudo-isometry.
\end{proof}

It remains to prove that the extension $F\colon \overline{\matH^n} \to \overline{\matH^n}$ is continuous. We start by extending Lemma \ref{half:lemma} from half-lines to lines.

\begin{lemma}
Let $F\colon \matH^n \to \matH^n$ be a pseudo-isometry. There is a $R>0$ such that for every line $l$ there is a unique line $l'$ with $F(l) \subset N_R(l')$.
\end{lemma}
\begin{proof}
Parametrize $l$ as $l\colon (-\infty,+\infty) \to \matH^n$ with unit speed. By cutting $l$ into two half-lines we know that $F(l(t))$ is a curve that tends to two distinct points $x_\pm\in\partial\matH^n$ as $t\to\pm\infty$. Let $l'$ be the line with endpoints $x_\pm$. For any $t>0$ we have
$$F\big(l([-t,t])\big) \subset N_R\left(\overline{F(l(-t))F(l(t))}\right)$$
and by sending $t\to +\infty$ we deduce that $F(l)\subset N_R(l')$.
\end{proof}

The next lemma says that a pseudo-isometry does not distort much lines and orthogonal hyperplanes. We will need it to prove continuity.

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{Mostow3-BW}{Mostow3}} 
\nota{Let $l$ and $H$ be a line and an orthogonal hyperplane. The orthogonal projection of $H$ onto $l$ is obviously a point $l\cap H$; the pseudo-isometry $F$ mildly distorts this picture: the image $F(H)$ projects to a bounded segment in $l'$.}
\label{Mostow3:fig}
\end{center}
\end{figure}

\begin{lemma}
Let $F\colon\matH^n \to \matH^n$ be a pseudo-isometry. There is a $R>0$ such that for any line $l$ and hyperplane $H$ orthogonal to $l$, the image $F(H)$ projects orthogonally to $l'$ onto a bounded segment length smaller than $R$.
\end{lemma}
\begin{proof}
See Figure \ref{Mostow3:fig}. Consider a generic line $s\subset H$ passing through $p=l\cap H$. By the previous lemmas $F(s)\subset N_R(s')$ with $s'\neq l'$, and the orthogonal projection on $l'$ sends any other line $s'$ onto a segment, bounded by the images of the endpoints of $s'$. 

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{Mostow4-BW}{Mostow4}} 
\nota{The lines $s_1$ and $s_2$ have a distance $d$ from $p$ which depends on nothing (in fact, $\cosh d = \sqrt 2$). The lines $l'$, $s_1'$, and $s_2'$ approximate up to an error $R$ the images of $l$, $s_1$, and $s_2$ along $F$. The projection $q$ of $F(p)$ on $l'$ is hence $R$-close to $F(p)$, which is in turn $(C_1d)$-close to the lines $s_i'$. Therefore $q$ is $(C_1d+2R)$-close to both $s_1'$ and $s_2'$. This easily implies that $f$ is $(C_1d+2R)$-close to $q$.
}
\label{Mostow4:fig}
\end{center}
\end{figure}

Consider as in Figure \ref{Mostow4:fig} the line $s$, with one endpoint $s^\infty$ and the corresponding endpoint $F(s^\infty)$ of $s'$. The figure shows that the projection $f$ of $F(s^\infty)$ to $l'$ is at bounded distance from a point $q$ which does not depend on $s$.
\end{proof}

Finally, we prove that the extended $F$ is continuous.

\begin{lemma}
The extension $F\colon \overline{\matH^n} \to \overline{\matH^n}$ is continuous.
\end{lemma}
\begin{proof}
Consider $x\in \partial \matH^n$ and its image $F(x) \in \partial \matH^n$. Let $l$ be a half-line pointing to $x$: hence $l'$ points to $F(x)$. The half-spaces orthogonal to $l'$ determine a neighbourhood system for $F(x)$: consider one such half-space $S$.

Let $R>0$ be as in the previous lemmas. The image $F(l)$ is $R$-close to $l'$, hence for sufficiently big $t$ the point $F(l(t))$ and its projection into $l'$ lie in $S$ at distance $>R$ from $\partial S$. By the previous lemma the image $F(H(t))$ of the  hyperplane $H(t)$ orthogonal to $l$ in $l(t)$ is also contained in $S$. Hence the entire half-space bounded by one such $H(t)$ goes inside $S$ through $F$.
This shows that $F$ is continuous at every point $x\in\partial \matH^n$.
\end{proof}

With some effort, we have proved that every pseudo-isometry of $\matH^n$ extends continuously to the boundary. Theorem \ref{estensione:teo} now follows easily.

\begin{proof}[Proof of Theorem \ref{estensione:teo}]
We know that $\tilde f$ is a pseudo-isometry and hence extends to a map $\tilde f \colon \overline {\matH^n} \to \overline{\matH^n}$ that sends injectively $\partial \matH^n$ to itself. It remains to prove that $\tilde f|_{\partial \matH^n}$ is a homeomorphism.

Pick a smooth homotopic inverse $g$ for $f$. The homotopy $\id_M \sim g \circ f$ lifts to a homotopy $\id_{\matH^n}\sim\tilde g\circ \tilde f$ for some lift $\tilde g$. Since $M$ is compact, the latter homotopy moves every point at uniformly bounded distance and hence $\tilde g\circ \tilde f$ extends continuously to the identity on $\partial \matH^n$, and the same holds for $\tilde f\circ \tilde g$. Therefore $\tilde g|_{\partial \matH^n}$ is the inverse of $\tilde f|_{\partial \matH^n}$ and they are both homeomorphisms.
\end{proof}


\subsection{References}
As in the previous chapters, we have mostly consulted Benedetti -- Petronio \cite{BP}, Ratcliffe \cite{R}, and Thurston's notes \cite{Th}. The Epstein -- Penner decomposition is taken from their 1988 paper \cite{EP}. 



\part{Surfaces}
\chapter{Surfaces} \label{superfici:chapter} \label{surfaces:chapter}

A surface is a differentiable manifold of dimension $n=2$, possibly with boundary. The closed orientable surfaces are classified topologically by their Euler characteristic, a complete invariant that also determines their possible geometries: a closed surface has a hyperbolic, flat, or spherical structure if and only if its Euler characteristic is negative, null, or positive.

We devote some time here to expose the topological classification and the geometrisation of closed surfaces. Then we describe some of the beautiful features of geometrisation: the geometry of a surface (typically, hyperbolic geometry) can be used to prove in an elegant way various non-trivial topological facts. 

We end this chapter by defining and studying the \emph{mapping class group}, a group that encodes the topological symmetries of a surface.
