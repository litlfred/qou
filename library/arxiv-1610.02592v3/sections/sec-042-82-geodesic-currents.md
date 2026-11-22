---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-042-82-geodesic-currents
section_title: "Geodesic currents"
section_number: 8.2
pages: 231-247
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.997
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We will prove Thurston's compactification Theorem \ref{compattificazione:teo} using a slightly different perspective. We are guided by the analogy with the hyperbolic space: when we embed (actually, define) the space $\matH^n$ in $\matR^{n+1}$, we make an essential use of the lorentzian form $\langle,\rangle$ in $\matR^{n+1}$, so that $\matH^n$ consists of some points $v$ with $\langle v,v \rangle = -1$, and $\partial \matH^n$ may be identified with the light cone rays, that is the rays spanned by vectors $v$ with $\langle v , v \rangle = 0$.

It would be nice to have a similar nice bilinear form $\langle,\rangle$ on $\matR^\calS$, with the property that $\Teich(S_g)$ and $\calS$ consist of points with $\langle v,v\rangle = k$ and $\langle v, v \rangle = 0$ respectively, for some fixed $k\neq 0$. Unfortunately we are not able to define such a bilinear form in $\matR^\calS$, and in order to get one we now substitute $\matR^\calS$ with a similar (but more structured) infinite-dimensional space, the space of \emph{geodesic currents}.

In geometric measure theory, a \emph{current} is a measure on some space, which generalises the notion of $m$-dimensional submanifold in a $n$-manifold. A \emph{geodesic current} is a similar tool introduced by Bonahon in 1988 specifically designed for geodesics on hyperbolic surfaces.

We will see that the geodesic currents are indeed equipped with a bilinear form, which generalises beautifully both the intersection number $i(\alpha, \beta)$ of curves and the length functions $\ell^\gamma$ on the Teichm\"uller space.


\subsection{Geodesics}
From now on, and through all the rest of this chapter, we will consider geodesics only as subsets, neglecting their parametrisation.

More precisely, let $M$ a complete hyperbolic manifold. We indicate by $\calG(M)$ the set of the supports of all the complete non-trivial geodesics $\matR \to M$. With a little language abuse, we call an element of $\calG(M)$ a \emph{geodesic}. 

A geodesic in $\calG(M)$ is \emph{closed} if it is the support of a closed geodesic $S^1 \to M$, that is if it is compact; otherwise, it is \emph{open}. We say that a geodesic is \emph{simple} if it has a simple geodesic parametrisation, either as an open geodesic $\matR \to M$ or as a closed one $S^1 \to M$. 
  
We are particularly interested in the set $\calG = \calG(\matH^2)$ of lines in $\matH^2$. A line is determined by its extremes, hence there is a natural bijection 
$$\calG \longleftrightarrow \left(\partial \matH^2 \times \partial \matH^2\setminus \Delta\right)/_\sim$$
where $\Delta = \{(a,a)\ |\ a\in\partial\matH^2\}$ is the diagonal and $(a,b) \sim (b,a)$. We assign to $\calG$ the topology of $\left(\partial \matH^2 \times \partial \matH^2\setminus \Delta\right)/_\sim$. 
\begin{ex} \label{Mobius:ex}
The space $\calG$ is homeomorphic to an open M\"obius strip. The lines intersecting a compact set $K\subset \matH^2$ form a compact subset of $\calG$.
\end{ex}
The isometries of $\matH^2$ act naturally on $\calG$ by homeomorphisms.
\begin{prop}
If $S=\matH^2/_\Gamma$ is a complete hyperbolic surface there is a natural bijection
$$\calG(S) \longleftrightarrow \calG/_\Gamma.$$
\end{prop}
\begin{proof}
Every geodesic in $S$ lifts to a $\Gamma$-orbit of lines in $\matH^2$.
\end{proof}

It is typically more comfortable to lift objects from $S$ to the universal cover $\matH^2$, and to study them there: we will often see a geodesic $\gamma\in\calG(S)$ as a $\Gamma$-orbit of lines in $\matH^2$. 

We will since now consider only closed surfaces $S_g$ of genus $g\geqslant 2$.
We now prove the crucial fact that $\calG(S_g)$ depends only mildly on the chosen hyperbolic metric for $S_g$. 
An \emph{isomorphism} between two pairs $(\calG_1, \Gamma_1)$ and $(\calG_2, \Gamma_2)$ of groups $\Gamma_i$ acting on topological spaces $\calG_i$ is an isomorphism $\psi\colon\Gamma_1\to \Gamma_2$ together with a $\psi$-equivariant homeomorphism $\calG_1\to \calG_2$.

\begin{prop}
Let $g\geqslant 2$ and $S_g = \matH^2/_\Gamma$ have a hyperbolic metric. The pair $(\calG, \Gamma)$ does not depend (up to canonical isomorphisms) on the chosen hyperbolic metric.
\end{prop}
\begin{proof}
Let $m,m'$ be two hyperbolic structures on $S_g$, inducing two different coverings $\pi, \pi' \colon \matH^2 \to S_g$. The identity map $S_g\to S_g$ lifts to a map $\matH^2 \to \matH^2$ that extends to an equivariant homeomorphism $\partial \matH^2 \to \partial \matH^2$ by Theorem \ref{estensione:teo}. This induces an equivariant homeomorphism $\calG \to \calG$.
\end{proof}

Here and in the next sections, the hyperbolic metric on $S_g$ has only an auxiliary role: we need it to identify $S_g$ with $\matH^2/_\Gamma$ and to define and study some geometric objects like $\calG(S_g) = \calG/_\Gamma$, but most of our discoveries will be independent \emph{a posteriori} of the auxiliary hyperbolic metric. 

Let $S_g=\matH^2/_\Gamma$ be a hyperbolic surface. We note that $\Gamma$ does \emph{not} act properly discontinuously on $\calG$.

\begin{prop} \label{orbit:discrete:prop}
The $\Gamma$-orbit of a line $l\in\calG$ is discrete if and only if $l$ projects to a closed geodesic in $S_g$.
\end{prop}
\begin{proof}
Let $\pi(l)\subset S_g$ be the projection of $l$ in $S_g$. Since $S_g$ is compact, the projection $\pi(l)$ is \emph{not} a closed geodesic $\Leftrightarrow$ there is a small disc $D \subset S_g$ intersecting $\pi(l)$ into infinitely many distinct segments $\Leftrightarrow$ there is a small disc $D\subset \matH^2$ intersecting infinitely many lines of the $\Gamma$-orbit of $l$ $\Leftrightarrow$ the $\Gamma$-orbit is not discrete.
\end{proof}

The lines $l\subset \matH^2$ that project to closed geodesics in $S_g$ are precisely the axis of the hyperbolic isometries $\varphi$ in $\Gamma$, and the $\Gamma$-orbit of one such axis $l$ consists of the axis of all the isometries in $\Gamma$ conjugate to $\varphi$. Two such axis are either incident or ultraparallel by Corollary \ref{axis:cor}, and the closed geodesic in $S_g$ is simple if and only if all the distinct axis in the $\Gamma$-orbit are ultraparallel.

Proposition \ref{orbit:discrete:prop} implies in particular that the $\Gamma$-orbit of $l$ is discrete only for countably many lines $l\in\calG$. 

Recall from Corollary \ref{unique:closed:geodesic:cor} that every homotopically non-trivial closed curve in $S_g$ is homotopic to a unique closed geodesic. 


\subsection{Geodesic currents} \label{correnti:subsection}
We now introduce a measure-theoretical notion which is at first sight unrelated with everything we have seen up to now; we will later show that, on the contrary, it generalises many of the geometric objects that we have encountered in the last pages. The basic notions of measure theory that we will need are summarised in Section \ref{measure:theory:section}.

\begin{defn}
Let $S_g=\matH^2/_\Gamma$ be a hyperbolic surface. 
A \emph{geodesic current} on $S_g$ is a locally finite $\Gamma$-invariant Borel measure on $\calG = \calG(\matH^2)$.\index{geodesic current}
\end{defn}

We denote by $\calC = \calC (S_g)$ the set of all the geodesic currents in $S_g$. It is a subset of the space $\calM(\calG)$ of all the locally finite Borel measures on $\calG$, closed with respect to sums and products with non-negative scalars, and it inherits its topology, see Section \ref{topology:measure:subsection}.

The currents space $\calC$ is independent of the auxiliary hyperbolic metric on $S_g$ up to canonical isomorphisms, since the pair $(\calG, \Gamma)$ is.


\subsection{Closed geodesics}
We now introduce a fundamental example of geodesic current.

\begin{example}[Closed geodesics]
\label{scc:example}
A closed geodesic $\gamma$ on $S_g=\matH^2/_\Gamma$ lifts by Proposition \ref{orbit:discrete:prop} to a discrete $\Gamma$-orbit of lines in $\matH^2$. The Dirac measure on this discrete set is locally finite and $\Gamma$-invariant, hence it is a geodesic current.
\end{example}

We can therefore interpret every closed geodesic in $S_g$ as a particular geodesic current with discrete support. In particular we get an embedding
$$\calS \hookrightarrow \calC$$
of the set $\calS$ of all (isotopy classes of) unoriented non-trivial simple closed curves in $S_g$ into $\calC$. The embedding is defined by taking the geodesic representative of each curve. Recall that the hyperbolic metric plays only an auxiliary role.

The following proposition implies that -- conversely -- every current supported on a discrete set is a linear combination of closed geodesics. 

\begin{prop} \label{atomic:prop}
If $l\in \calG$ is an atomic point for a geodesic current $\mu$, that is if $\mu(\{l\})>0$, then $l$ projects to a closed geodesic in $S_g$.
\end{prop}
\begin{proof}
Since $l$ is atomic and $\mu$ is $\Gamma$-invariant and locally finite, the $\Gamma$-orbit of $l$ in $\calG$ is discrete. We conclude thanks to Proposition \ref{orbit:discrete:prop}.
\end{proof}

It is an important aspect of the theory that atomic points may be only of a very specific type. We remind that many closed geodesics are not simple.


\subsection{Pencils} \label{pencils:subsection}
We have determined the 0-dimensional subsets of $\calG$ that may have positive mass, and we now look at some natural 1-dimensional ones. Let a \emph{pencil} $p\subset\calG$ of lines centred at $a\in\partial \matH^2$ be some Borel set of lines all having one endpoint at $a$, as in Figure \ref{pencil-box:fig}-(left).\index{pencil}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{pencil-box-BW}{pencil-box}}
\nota{A pencil and a box (in the Klein model).}
\label{pencil-box:fig}
\end{center}
\end{figure}

We note that a pencil may contain at most one axis of some hyperbolic transformation in $\Gamma$, because two axis are never asymptotically parallel by Corollary \ref{axis:cor}.

\begin{prop} \label{pencils:prop}
Let $\mu$ be a geodesic current. The mass of a pencil $p$ is zero, unless it contains the axis of some non-trivial element in $\Gamma$.
\end{prop}
\begin{proof}
It suffices to consider the case where $p$ contains no axis, and consists of all lines with one endpoint in $a$ and another in some segment $[b,c] \subset \partial \matH^2$ not containing $a$.

As the lines in $p$ point to $a$, they project in $S_g$ to a narrow beam of lines that go on running forever and exponentially-narrowing in $S_g$ but never close up. There is a disc $D\subset S_g$ intersecting them infinitely many times, hence a lift $D\subset \matH^2$ intersects infinitely many disjoint $\Gamma$-translates of $p$. The lines intersecting $D$ form a compact subset of $\calG$, hence $\mu(p)=0$.
\end{proof}


\subsection{Boxes}
We now investigate some natural 2-dimensional subsets of $\calG$. Let $a,b,c,d \in \partial \matH^2$ be four distinct counterclockwise-ordered points as in Figure \ref{pencil-box:fig}-(right): these determine two disjoint arcs $[a,b], [c,d] \subset \partial \matH^2$ and hence a compact set $B=[a,b] \times [c,d] \subset \calG$ consisting of all lines with endpoints in $[a,b]$ and $[c,d]$, see Figure \ref{pencil-box:fig}-(right). We call this compact set $B$ a \emph{box}.\index{box}

The topological boundary $\partial B$ of a box $B$ has four sides: the four pencils of lines in $B$ with one endpoint in $a,b,c$, or $d$. We say that the box $B$ is \emph{generic} if no line $l\in\partial B$ projects to a closed geodesic, \emph{i.e.}~no $l\in\partial B$ is the axis of some hyperbolic transformation in $\Gamma$. This is indeed a generic condition: if neither of $a,b,c,d$ is the endpoint of some axis, then $B$ is certainly generic, and recall that there are only countably many axis overall.

We equip the currents space $\calC$ with the weak-* topology introduced in Section \ref{topology:measure:subsection}. We now prove that a converging sequence of currents behave well on generic boxes.

\begin{prop}
If $\mu_i \rightharpoonup \mu$ is a converging sequence of geodesic currents and $B$ is a generic box, then $\mu_i(B) \to \mu(B)$.
\end{prop}
\begin{proof}
By Proposition \ref{delta:zero:prop} it suffices to prove that $\mu(\partial B) = 0$, and this follows from Proposition \ref{pencils:prop}.
\end{proof}


\subsection{Rigidity of atoms}
We now use boxes to prove that the atomic points in $\calC$ are somehow rigid. 

\begin{prop} \label{closed:discrete:currents:prop}
The closed geodesics form a discrete subset in $\calC$.
\end{prop}
\begin{proof}
Let $\mu \in \calC$ be a closed geodesic, \emph{i.e}~it is the Dirac measure on the $\Gamma$-orbit of an axis $l\subset \matH^2$ of some hyperbolic transformation $\varphi\in\Gamma$. 

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{boxes-BW}{boxes}}
\nota{The box $B$ containing $l$ and the sub-boxes $B'$ and $B''$ (left). A line $l\in U_\gamma$ parametrised by the pair $(t,\theta)$ (right).}
\label{boxes:fig}
\end{center}
\end{figure}

Let $B=[a,b]\times [c,d]$ be a small generic box containing $l$ and no other $\Gamma$-translate of $l$, so that $\mu(B) = 1$. Up to substituting $\varphi$ with $\varphi^{-1}$ we may suppose that $\varphi([a,b]) = [a',b'] \subset [a,b]$. Consider the sub-boxes $B' = [a,a']\times [c,d]$ and $B'' = [b',b]\times [c,d]$ shown in Figure \ref{boxes:fig}-(left). Since $\varphi$ contracts $[a,b]$ and expands $[c,d]$, we have 
\begin{equation} \label{Bl:eqn}
B\setminus p \subset \bigcup_{i=1}^\infty \varphi^i(B' \sqcup B'').
\end{equation}
where $p$ is the pencil containing $l$ and other lines with one endpoint varying in $[b,c]$. Note that $p$ contains no axis of $\Gamma$ other than $l$.
If necessary, we move $a'$ and $b'$ slightly farther from $a$ and $b$ to ensure that $B'$ and $B''$ (and hence all their $\varphi$-translates) are generic while (\ref{Bl:eqn}) still holds.

We have $\mu(B' \sqcup B'')=0$ and we define an open neighbourhood $U$ of $\mu$ in the current space $\calC$ as follows: 
$$U = \big\{ \eta\in \calC\ |\ \eta(B' \sqcup B'') < \varepsilon,\ \eta(B)>1-\varepsilon\big\}$$ 
for some fixed $0<\varepsilon < 1$. This is indeed an open set because $B, B',$ and $B''$ are generic. We now prove that $U$ contains no closed geodesic except $\mu$.

By contradiction, suppose $U$ contains a closed geodesic $\eta$. Since $\eta(B)>1-\varepsilon>0$, at least one atom $l'$ of $\eta$ is contained in $B$. If $l'=l$ then $\eta=\mu$ and we are done. Otherwise, the line $l'$ is contained in $B\setminus p$ and hence in $\varphi^i(B' \sqcup B'')$ for some $i$. This is impossible since this set has measure $\varepsilon < 1$.
\end{proof}

We have classified the elements in $\calC$ supported on discrete sets, and it is now time to  introduce some geodesic currents supported on the whole of $\calG$.


\subsection{The Liouville measure}
There is a continuous measure on $\calG = \calG(\matH^2)$ that is invariant under the action of the whole isometry group $\Iso(\matH^2)$. This measure is called the \emph{Liouville measure}, and is defined as follows.\index{Liouville measure}

Let $\gamma\colon \matR \to \matH^2$ be a geodesic parametrised by arc length, and $U_\gamma\subset \calG$ be the open set consisting of all the lines intersecting $\gamma$, except $\gamma$ itself. We can parametrise $U_\gamma$ via the homeomorphism 
$$\matR \times (0,\pi) \to U_\gamma$$ 
that sends $(t, \theta)$ to the line $l$ that intersects $\gamma$ at the point $\gamma(t)$ with angle $\theta$, see Figure \ref{boxes:fig}-(right). We define a volume 2-form on $U_\gamma$ by setting: 
$$L_\gamma = \frac 12 \sin\theta\, dt\wedge d\theta.$$
Since $\calG$ is non-orientable, we cannot hope to define a global area form on $\calG$. However all these local forms match up to sign and hence give rise to a measure.
\begin{prop}
The charts $U_\gamma$ form a differentiable atlas for $\calG$. The 2-forms $L_\gamma$ match up to sign and hence define a measure  $L$ on $\calG$.
\end{prop}
\begin{proof}
Every line in $\matH^2$ intersects some other line, hence the charts cover $\calG$. 
We consider a line $r\in U_\gamma\cap U_{\gamma'}$. The charts $U_\gamma$ and $U_{\gamma'}$ have parametrisations $(t,\theta)$ and $(t', \theta')$ and 2-forms 
$$L_\gamma = \frac 12 \sin\theta dt \wedge d\theta, \quad 
L_{\gamma'} = \frac 12 \sin\theta' dt' \wedge d\theta'.$$ 
We consider the jacobian $J = \frac{\partial (t', \theta')}{\partial (t,\theta)}$ 
and recall that 
$$dt' \wedge d\theta' = \det J \cdot dt \wedge d\theta$$
so we need to show that
\begin{equation} \label{J:eqn}
\det J = \pm\frac {\sin \theta}{\sin \theta'}.
\end{equation}
We can reparametrise $\gamma$ at our please, since this may change $L_\gamma$ only by a sign. We may suppose that $\gamma$ and $\gamma'$ are asymptotically parallel, because any two lines $\gamma, \gamma'$ intersecting $r$ are connected by a path $\gamma = \gamma_1, \ldots, \gamma_k = \gamma'$ of lines intersecting $r$, such that any two subsequent lines $\gamma_i$, $\gamma_{i+1}$ are asymptotically parallel (actually $k= 3$ suffices). 

\begin{figure}
\begin{center}
\includegraphics[width = 5 cm] {\iftoggle{BW}{Liouville-BW}{Liouville}}
\nota{The two asymptotic lines $\gamma, \gamma'$ in the half-space model $H^2$ and the line $r$ intersecting both.}
\label{Liouville:fig}
\end{center}
\end{figure}

We represent the lines $\gamma, \gamma',$ and $r$ in the half-plane model $H^2\subset \matR^2$ as in Figure \ref{Liouville:fig}. Up to isometries and reparametrisations we have 
$$\gamma(t) = (0, e^t), \qquad \gamma'(t') = (1,e^{t'}).$$
The line $r$ is a Euclidean half-circle with center at some point $C\in \matR$ and with some radius $R>0$. It intersects $\gamma$ and $\gamma'$ at some heights $e^t$ and $e^{t'}$, with some angles $\theta$ and $\theta'$. We now calculate the determinant of $J = \frac{\partial (t', \theta')}{\partial (t,\theta)}$. Figure \ref{Liouville:fig} shows that


$$ R = \frac{e^t}{\sin \theta} = \frac{e^{t'}}{\sin \theta'}$$


$$ C = -e^t \cot \theta, \qquad 1 - C = e^{t'} \cot \theta'.$$

Now
$$\frac{\partial (C,R)}{\partial(t,\theta)} = 
\begin{pmatrix} 
-e^t\cos\theta\sin^{-1}\theta & e^t\sin^{-2}\theta \\
e^t\sin^{-1}\theta & -e^t \cos\theta\sin^{-2} \theta
\end{pmatrix}
$$
whose determinant is $-e^{2t} \sin^{-1}\theta = -R\sin\theta$, and we get the same formula for $\frac{\partial (C,R)}{\partial(t',\theta')}$. Therefore
$$\det \frac{\partial (t', \theta')}{\partial (t,\theta)} =
\det \frac{\partial (t', \theta')}{\partial (C, R)}
\cdot 
\det \frac{\partial (C,R)}{\partial(t,\theta)} 
=
(-R\sin\theta')^{-1} \cdot (R \sin\theta) = \frac{\sin\theta}{\sin\theta'}$$
and we finally obtain (\ref{J:eqn}), as required.
\end{proof}
The measure $L$ on $\calG$ is called the \emph{Liouville measure} and is clearly invariant by the action of $\Iso(\matH^2)$. The renormalising factor $\frac 12$ in the definition was chosen to get the following property, which nicely characterises $L$.

\begin{prop} \label{l:prop}
Let $s\subset \matH^2$ be a geodesic segment of length $l$. The lines in $\matH^2$ intersecting $s$ form a set of measure $l$.
\end{prop}
\begin{proof}
The set has measure
$$\int_0^\pi\int_0^l \frac 12 \sin\theta \, dt\, d\theta = l \int_0^\pi \frac 12 \sin \theta \, d\theta = l.$$
The proof is complete.
\end{proof}

The Liouville measure $L$ is supported on the whole of $\calG$.

\begin{ex}
The Liouville measure of a box $B=[a,b]\times [c,d]$ is 
$$L(B) = \big| \log \beta(a,b,c,d) \big|$$
where $\beta$ is the cross-ratio of the four points.
\end{ex}


\subsection{The Liouville current}
Let now $S_g=\matH^2/_\Gamma$ be equipped with a hyperbolic metric. The Liouville measure on $\calG$ is $\Iso(\matH^2)$-invariant: in particular it is $\Gamma$-invariant and hence defines a current $L \in \calC(S_g)$, called the \emph{Liouville current}.\index{Liouville current} 

It is important to note that the space of currents $\calC = \calC(S_g)$ does not depend on the given hyperbolic metric for $S_g$, but the Liouville current does! Every metric $m\in \Teich(S_g)$ induces a Liouville current $L_m\in \calC$, and in this way we get a \emph{Liouville map}\index{Liouville map}
$$\Teich(S_g) \longrightarrow \calC$$
that sends $m$ to $L_m$.
We will soon see that this map is injective: as promised, we have mapped both $\calS$ and $\Teich(S_g)$ inside the currents space $\calC$. 

\begin{rem}
We constructed the Liouville current $L_m$ by assigning to $\calG$ a differentiable atlas -- hence a smooth structure -- and a 2-form defined up to sign. We note that the smooth structure on $\calG$ also depends crucially on $m$, because the boundary extension of Theorem \ref{estensione:teo} is not guaranteed to be a diffeomorphism.
\end{rem}

The crucial feature that makes $\calC$ preferable to $\matP(\matR^\calS)$ as a comfortable ambient space for both $\calS$ and $\Teich(S_g)$ is the existence of a nice bilinear form in $\calC$ that extends both the length and the geometric intersection of closed geodesics. We now introduce this bilinear form.


\subsection{The projective frame bundle}
We denote by $\calI \subset \calG \times \calG$ the open subset consisting of all the pairs of \emph{incident} distinct lines in $\matH^2$. We give $\calI$ the topology induced by $\calG \times \calG$, hence $\calI$ is an open topological 4-manifold. Since two distinct incident lines intersect in a single point $p\in\matH^2$, the set $\calI$ can be interpreted as the set of triples $(p,l_1,l_2)$ with $p\in \matH^2$ and $l_1,l_2$ two distinct vector lines in the tangent plane $T_p\matH^2$.

Let now $S_g=\matH^2/_\Gamma$ be equipped with a hyperbolic metric. The action of $\Gamma$ on $\calG$ is not properly discontinuous, but the diagonal action of $\Gamma$ on $\calI$ is, as the following shows.
\begin{prop}
The map $\calI \to \calI/_\Gamma$ is a topological covering.
\end{prop}
\begin{proof}
The group $\Gamma$ acts freely and properly discontinuously on $\matH^2$, and hence it does so \emph{a fortiori} on the triples $(p,l_1,l_2)$.
\end{proof}

In particular $\calI/_\Gamma$ is a four-manifold, and it is naturally a bundle over $S_g$, whose fibre above $p\in S_g$ consists of the ordered pairs of distinct vector lines $l_1,l_2$ in $T_pS_g$. Recall that the \emph{frame bundle} on a manifold $M$ is a bundle whose fibre above $p\in M$ is the set of all \emph{frames} (i.e.~basis) in $T_pM$. The space $\calI/_\Gamma$ can be seen as some projective quotient of the frame bundle on $S_g$.


\subsection{Intersection form}
Two geodesic currents $\alpha, \beta \in \calC = \calC(S_g)$ induce a $\Gamma$-invariant product measure $\alpha\times \beta$ on $\calG\times \calG$ and hence on $\calI$. This measure descends via the covering $\calI \to \calI/_\Gamma$ to a measure on $\calI/_\Gamma$ which we still indicate by $\alpha\times \beta$, see Section \ref{measure:descends:subsection}.\index{intersection form on currents}

\begin{defn}
The \emph{intersection} $i(\alpha,\beta)$ of two geodesic currents is the total volume of $\calI/_\Gamma$ in the measure $\alpha\times\beta$. 
\end{defn}

The intersection $i(\alpha, \beta)$ does not depend on the auxiliary hyperbolic metric for $S_g$. The finiteness of $i(\alpha,\beta)$ is not immediate since $\calI/_\Gamma$ is not compact, and it deserves a proof.

\begin{prop}
The intersection $i(\alpha,\beta)$ is finite.
\end{prop}
\begin{proof}
Let $D$ be a compact fundamental domain for $S_g = \matH^2/_\Gamma$. Since $D$ is compact, the lines intersecting $D$ form a compact subset $X\subset \calG$ which has finite measures $\alpha(X)$ and $\beta(X)$. The projection sends $(X \times X) \cap \calI$ surjectively onto $\calI/_\Gamma$. 
Therefore $i(\alpha,\beta) = (\alpha\times \beta) (\calI/_\Gamma) < \alpha(X) \cdot \beta(X)$.
\end{proof}

The form $i$ is clearly bilinear and symmetric. 


\subsection{Geometric intersection and length of closed geodesics}
We now show that this abstract-looking intersection form generalises both the geometric intersection and the length of simple closed geodesics.
We consider as usual the set $\calS$ of simple closed curves as a subset of $\calC$. The following proposition explains why we employed the notation $i$ for the intersection form of two geodesic currents.

\begin{prop}
If $\alpha, \beta \in \calS$, the number $i(\alpha,\beta)$ is the geometric intersection of the simple closed curves $\alpha$ and $\beta$.
\end{prop}
\begin{proof}
Represent $\alpha$ and $\beta$ as simple closed geodesics. The measure $\alpha\times \beta$ is the Dirac measure with support the pairs of incident lines in $\matH^2$ that cover respectively $\alpha$ and $\beta$. The $\Gamma$-orbits of these pairs are in natural bijection with the transverse intersection points in $\alpha\cap \beta$. Hence the volume of $\calI/_\Gamma$ is the cardinality of $\alpha\cap\beta$, except when $\alpha = \beta$ and in this case we get zero.
\end{proof}

We note in particular that $i(\alpha,\alpha)=0$ for every $\alpha\in\calS$, hence the set $\calS$ is contained in the ``light cone'' consisting of all the currents $\alpha$ with $i(\alpha,\alpha)=0$. (Of course $i(\alpha, \alpha)\geqslant 0$ for every geodesic current $\alpha$.) We now consider the Liouville current $L_m\in\calC$ determined by some hyperbolic metric $m$ on $S_g$.

\begin{prop} \label{i:metric:curve:prop}
If $\alpha\in \calS$ then $i(L_m, \alpha) = \ell^\alpha(m)$ is the length of the geodesic representative of $\alpha$ in the metric $m$.
\end{prop}
\begin{proof}
Represent $\alpha$ as a simple closed geodesic in the metric $m$, of length $\ell^\alpha(m)$. The measure $L_m \times \alpha$ has its support on the pairs $(l,l')$ of incident lines where $l$ is arbitrary and $l'$ is a lift of $\alpha$. 

Any segment $s'\subset l'$ of length $\ell^\alpha(m)$ in a fixed lift $l'$ of $\alpha$ is a fundamental domain for the action of $\Gamma$ on the lifts of $\alpha$. Therefore $i(L_m, \alpha)$ is the volume of the pairs $(l,l')$ where $l'$ is fixed, and $l$ is arbitrary and intersects $s'$. By Proposition \ref{l:prop} these pairs have volume $\ell^\alpha(m)$.
\end{proof}

The intersection form $i$ on $\calC$ generalises both the geometric intersection of curves and the length functions on Teichm\"uller space, two apparently unrelated objects! As promised, we can easily deduce that $\Teich(S_g)$ embeds in $\calC$.

\begin{cor}
The Liouville map $\Teich(S_g) \to \calC$ is injective.
\end{cor}
\begin{proof}
If $m\neq m'$ there is a curve $\gamma\in\calS$ with $\ell^\gamma(m) \neq \ell^\gamma(m')$ by Proposition \ref{9g-9:prop} and hence $i(L_m,\gamma) \neq i(L_{m'},\gamma)$. Therefore $L_m \neq L_{m'}$.
\end{proof}

We will since now consider both $\Teich(S_g)$ and $\calS$ as subsets of $\calC$.
We know the geometric meaning of the intersection of two curves, and of a curve and a hyperbolic metric. What is the intersection of two hyperbolic metrics? When they coincide, we get a positive constant.

\begin{prop}
If $m \in \Teich(S_g)$ we have $i(L_m, L_m) = -\pi^2 \chi(S_g)$.
\end{prop}
\begin{proof}
The metric $m$ produces a smooth structure on $\calG$ and hence on $\calI$, and $L_m$ is induced by a $\Gamma$-invariant 2-form on $\calG$ defined up to sign, that we also denote as $L_m$. We need to integrate the 4-form $L_m \times L_m$ on $\calI/_\Gamma$.

Recall that $\calI/_\Gamma$ may be interpreted as a bundle over $S_g$.
We make a first-order computation on a very small region of $S_g$, which we may suppose to be Euclidean: a very thin rectangle $R$ in $S_g$ of sides $l$ and $a$ with $a \ll l$. We compute the volume of the portion of bundle lying above $R$.

We integrate $L_m \times L_m$ on all the pairs of segments intersecting in some point in $R$, and we consider only segments with both endpoints on the big $l$ sides, neglecting the small $a$ sides. A segment meeting the $l$ sides at angle $\theta$ has length $L(\theta) = a/\sin \theta$. By Proposition \ref{l:prop} the $L_m \times L_m$ volume of the portion of $\calI$ above $R$ is (at a first order) equal to
$$\int_0^\pi \int_0^l \frac 12 \sin \theta \cdot L(\theta) \, dt\, d\theta \sim
\frac 12 l \int_0^\pi \sin \theta \cdot \frac a{\sin \theta} = \frac{\pi}2 la.$$

The first-order contribution of a small region is hence $\frac{\pi}2$ times its area. Since the volume is induced by a differentiable form, by taking the limit we find that the contribution of any region is precisely $\frac{\pi}2$ its area and we conclude by the Gauss-Bonnet theorem.
\end{proof}

We have already noted that $i$ is symmetric and bilinear. 
As we mentioned, there is an evident analogy between the embeddings $\Teich(S_g)\hookrightarrow \calC$ and $\matH^n\hookrightarrow \matR^{n+1}$, since there is a bilinear form on both spaces $\calC$ and $\matR^{n+1}$, and $\Teich(S_g)$ is also contained in a ``hyperboloid'' consisting of vectors $v$ with $i(v,v) = k$ for some fixed $k \neq 0$. On the other hand $\calS$ is contained in the ``light cone'' formed by all vectors $v$ with $i(v,v)=0$. 

We may compactify $\matH^n$ by projecting the hyperboloid to the Klein model $K^n\subset \matRP^{n}$. Now $K^n$ is an open disc, whose boundary is the image of the light cone. We would like to apply the same compactification strategy to $\Teich(S_g)$. Before doing that, we need to prove a slightly technical fact: that the bilinear form $i$ is continuous. 


\subsection{Continuity of the intersection form}
Let $S_g=\matH^2/_\Gamma$ be a closed hyperbolic surface.
The following theorem is not obvious because $\calI$ is not compact: the proof relies on the fact that closed geodesics form a discrete rigid set in $\calC$ and therefore atomic points cannot ``escape to infinity'' on a converging sequence of currents.

\begin{teo}
The form $i\colon \calC \times \calC \to \matR$ is continuous.
\end{teo}
\begin{proof}
Let $\beta_1, \beta_2$ be two currents converging to $\alpha_1, \alpha_2$. We need to prove that $i(\beta_1,\beta_2)$ converges to $i(\alpha_1, \alpha_2)$. The bundle $\calI/_\Gamma$ is not compact and we need to control that no mass escapes to infinity: the infinity here is the diagonal $\Delta \subset \calG \times \calG$, so our aim is to cover $\Delta$ with small boxes and prove that they contribute very little to $i(\beta_1,\beta_2)$. For any box $B$, we define
$$\Psi(B) = \big((B\times B)\cap \calI \big)/_\Gamma.$$
We show that for every $\varepsilon >0$ there are finitely many small generic boxes $B_i$ whose $\Gamma$-translates cover $\calG$, such that 
$$(\beta_1 \times \beta_2) (\cup_i\Psi(B_i)) < \varepsilon$$
as soon as $\beta_1,\beta_2$ are sufficiently close to $\alpha_1,\alpha_2$. Since the $\Gamma$-translates of $\cup_i (B_i\times B_i)$ form an open neighbourhood of $\Delta$, the set $(\calI/_\Gamma )\setminus (\cup_i \Psi(B_i))$ is compact with zero-measure boundary (because the boxes $B_i$ are generic) so its contribution to $i(\beta_1, \beta_2)$ tends to that to $i(\alpha_1,\alpha_2)$ if $\beta_1,\beta_2$ are sufficiently close, and the theorem is proved.

It remains to construct the boxes $B_i$. We first fix finitely many generic boxes $B_i$ whose $\Gamma$-translates cover $\calG$. Let $K>0$ be bigger than the total $\alpha_1$ and $\alpha_2$-mass of the boxes. 

We now pick a small number $0<\varepsilon' < \varepsilon / 2K$ and subdivide each box $B_i$ into finitely many generic sub-boxes (which we still call $B_i$) such that the following holds for each $i$ and each $j=1,2$:
\begin{enumerate}
\item either $\alpha_j(B_i) < \varepsilon'$, or
\item there is an atomic point $l \in B_i$ with $\alpha_j(l) > \varepsilon'$ and $\alpha_j(B_i \setminus l) < \varepsilon'$.
\end{enumerate}
If the second case holds for both $j=1,2$, we also require $l\in B_i$ to be the same line for $j=1,2$.
We note that the total $\alpha_1$ and $\alpha_2$-mass of the boxes is still smaller than $K$ after the subdivision.
We have
$$(\beta_1 \times \beta_2)(\Psi(B)) \leqslant \beta_1(B) \cdot \beta_2(B)$$
so if $\beta_1,\beta_2$ are sufficiently close to $\alpha_1, \alpha_2$ the boxes $B_i$ that are of the first kind for at least one value of $j=1,2$ contribute to $i(\beta_1, \beta_2)$ less than $2\varepsilon' K<\varepsilon$.

We are left to consider the boxes $B_i$ containing a line $l$ whose $\alpha_1$ and $\alpha_2$-mass are both bigger than $\varepsilon'$. This is a potentially bad situation since the point $(l,l) \in \calG\times \calG$ is atomic and contained in the frontier of $\calI$, and could enter inside $\calI$ abruptly for some arbitrarily small perturbations of $\alpha_1$ and $\alpha_2$. We show that this cannot happen because atomic points are rigid, as noted in Proposition \ref{closed:discrete:currents:prop}.

As in the proof of Proposition \ref{closed:discrete:currents:prop}, we set $B_i = B = [a,b] \times [c,d]$ and construct $B' = [a,a'] \times [c,d], B'' = [b',b] \times [c,d]$ whose $\varphi$-translates cover $B\setminus p$ where $p$ is a pencil containing $l$. We note that
$$(\beta_1 \times \beta_2) (\Psi(B)) \leqslant \beta_1(B' \sqcup B'') \cdot \beta_2(B) + \beta_2(B'\sqcup B'') \cdot \beta_1(B)$$
is smaller than $\varepsilon' (\beta_1(B) + \beta_2(B))$ and hence by summing on the $B_i$ we get again a contribution smaller than $2\varepsilon' K < \varepsilon$.
\end{proof}


\subsection{Filling geodesic currents}
We now define an interesting class of currents, whose importance will be evident in the next section.

We say that a geodesic current $\alpha\in\calC(S_g)$ \emph{fills} the surface $S_g=\matH^2/_\Gamma$ if every line in $\matH^2$ intersects transversely at least one line in the support of $\alpha$. For instance, a Liouville measure fills $S_g$ since its support is the whole of $\calG$. We say that $k$ closed geodesics $\gamma_1,\ldots, \gamma_k$ \emph{fill $S_g$} if the geodesic current $\gamma_1+\ldots + \gamma_k$ does.

\begin{prop}
Let $\gamma_1,\ldots, \gamma_k$ be closed geodesics. If $S_g \setminus (\gamma_1\cup \cdots\cup \gamma_k)$ consists of polygons, the curves fill $S_g$.
\end{prop}
\begin{proof}
Every geodesic in $S_g$ intersects these curves.
\end{proof}

As an example, we can pick two multicurves $\eta$ and $\mu$ in $S_g$ that intersect transversely forming only polygons but no bigons. By the bigon criterion $\eta$ and $\mu$ are in minimal position and by Proposition \ref{minimale:unica:prop} their geodesic representatives have the same configuration as $\eta\cup\mu$, so they fill $S_g$.

It is a bit more difficult to construct a single (non-simple) closed geodesic that fills $S_g$. The following remark is straightforward.

\begin{oss} \label{correnti:oss}
Let $\alpha$ and $\beta$ be currents. We have $i(\alpha,\beta)>0$ if and only if there are two lines in the supports of $\alpha$ and $\beta$ that intersect in a point.
\end{oss}

\begin{cor} \label{riempie:cor}
If $\alpha$ fills $S_g$ then $i(\alpha,\beta)>0$ for every non-trivial $\beta\in\calC$.
\end{cor}


\subsection{A compactness criterion}
We now state a simple and general compactness criterion for subsets of $\calC$ that has various nice (and apparently unrelated) geometric consequences.

\begin{prop}[Compactness criterion] \label{compattezza:C:prop}
If $\alpha\in\calC$ fills $S_g$, the set of all $\beta\in\calC$ with $i(\alpha,\beta)\leqslant M$ is compact, for all $M>0$.
\end{prop}
\begin{proof}
Let $C\subset\calC$ be the set of all $\beta$ with $i(\alpha,\beta)\leqslant M$. It is closed because $i$ is continuous.

Let $l$ be a line in $\matH^2$. By hypothesis there is another line $l'$ in the support of $\alpha$ which intersects $l$ in a point. Let $B'$, $B$ be two sufficiently small boxes neighbourhoods of $l',l$ in $\calG$, so that $B' \times B \subset \calI$ and
$B' \times B$ is mapped injectively into $\calI/_\Gamma$.
If $\beta\in C$ we have
$$\alpha(B')\beta(B) = (\alpha\times\beta)(B' \times B) \leqslant (\alpha\times\beta)\left(\calI/_\Gamma\right) = i(\alpha,\beta) \leqslant M.$$
Therefore every line $l$ in $\matH^2$ has a box neighbourhood $B$ such that
$$\beta(B) \leqslant K_l \quad \forall \beta \in C$$
for some constant $K_l = M/\alpha(B')$ that depends only on $l$. The set $C$ is relatively compact by Theorem \ref{compact:measure:teo}, and hence compact since it is closed. The proof is complete.
\end{proof}

We now state some corollaries. The first concerns the immersion of $\Teich(S_g)$ in $\calC$. 

\begin{cor}
The Liouville map $\Teich(S_g)\hookrightarrow\calC$ is proper and a homeomorphism onto its image.
\end{cor}
\begin{proof}
We prove that the map is proper: if $m_j\in \Teich(S_g)$ is a diverging sequence of metrics, we know from Proposition \ref{diverges:infinity:prop} that there is a closed curve $\gamma\in\calS$ such that $\ell^\gamma(m_j) = i(m_j, \gamma) \to \infty$ on a subsequence. Since $i$ is continuous, the sequence $m_j$ diverges also in $\calC$. 

We denote the Liouville map by $L$. We should now prove that $L$ is continuous, but we prefer to consider the inverse map $L^{-1}\colon L(\Teich(S_g)) \to \Teich(S_g)$. The map $L^{-1}$ is continuous because $i$ is and $\Teich(S_g)$ has the weakest topology where the length functions are continuous. We show that $L^{-1}$ is proper. Let $\gamma_1, \ldots, \gamma_k$ be simple closed curves that fill $S_g$. If $L(m_i)$ is a diverging sequence, by Proposition \ref{compattezza:C:prop} we have $i(L(m_i),\sum_t \gamma_t)\to \infty$ and hence $i(L(m_i),\gamma_t)\to \infty$ for some $t$. Therefore $m_i$ is divergent also in $\Teich(S_g)$.

Now $L^{-1}$ is continuous and proper and hence a homeomorphism by
Corollary \ref{propria:chiusa:cor}.
\end{proof}

A second immediate corollary is a general compactness criterion for the Teichm\"uller space.

\begin{cor} \label{bounded:metrics:compact:cor}
Let $\gamma_1,\ldots, \gamma_k$ be some closed geodesics that fill $S_g$. The metrics $m\in\Teich(S_g)$ with $\ell^{\gamma_i}(m) \leqslant M$ form a compact subset of $\Teich(S_g)$, for all $M>0$.
\end{cor}

We can similarly deduce the following.
\begin{cor}
Let $\gamma_1,\ldots, \gamma_k$ be some simple closed curves that fill $S_g$. For every $M$ there are only finitely many $\alpha \in \calS$ with $i(\gamma_i, \alpha) < M$ for all $i$.
\end{cor}


\begin{ex} Use the compactness criterion to re-prove that on a hyperbolic closed surface there are only finitely many closed geodesics of bounded length.
\end{ex}

We are finally ready to construct Thurston's compactification of the Teichm\"uller space, using Bonahon's geodesic currents. 


\subsection{Projective currents}
As usual, we pick a hyperbolic closed surface $S_g=\matH^2/_\Gamma$.
The currents space $\calC$ is equipped with a multiplication by positive scalars, hence we can define its projectivisation
$$\pi\colon \calC\setminus 0 \longrightarrow \matP\calC$$
where $\matP \calC = (\calC \setminus 0)/_\sim$ with $\alpha \sim \lambda \alpha$ for all $\lambda>0$. We give $\matP\calC$ the quotient topology.

\begin{prop} The space $\matP\calC$ is compact.
\end{prop}
\begin{proof}
Pick an $\alpha\in\calC$ that fills $S_g$. By the compactness criterion the set $C = \{\beta\in\calC\ |\ i(\alpha,\beta)=1\}$ is compact. By Corollary \ref{riempie:cor} we have $i(\alpha,\beta)>0$ for all $\beta$, hence $\lambda\beta \in C$ for some $\lambda>0$. Therefore $\pi(C) = \matP\calC$ and $\matP\calC$ is compact.
\end{proof}

We now want to embed both $\Teich(S_g)$ and $\calS$ in $\matP\calC$.

\begin{prop}
The composition $\calS \to \calC\setminus 0 \to \matP\calC$ is injective.
\end{prop}
\begin{proof}
Let $\gamma_1,\gamma_2 \in\calS$ be distinct. There is always a closed curve $\eta\in\calS$ with $i(\gamma_1,\eta)\neq 0$ and $i(\gamma_2,\eta)=0$.
\end{proof}

\begin{prop} \label{embed:Teich:prop}
The composition $\Teich(S_g) \to \calC \setminus 0\to \matP\calC$ is injective and a homeomorphism onto its image.
\end{prop}
\begin{proof}
We see $\Teich(S_g)$ already properly embedded in $\calC$.
Since $i(m,m) = -\pi^2\chi(S_g)$ is constant on $\Teich(S_g)$, the composition is injective. The restriction $\pi\colon \Teich(S_g) \to \pi(\Teich(S_g))$ is also continuous, and we now prove that it is proper (note that we need to restrict the codomain to get this).

Consider a diverging sequence $m_j\in \Teich(S_g)$. By compactness of $\matP\calC$ the sequence $[m_j]\in\matP\calC$ converges on a subsequence to some $[\alpha]\in\matP\calC$. For each $j$ there is a $\lambda_j>0$ such that $\lambda_jm_j \to \alpha$ in $\calC$. Since $m_j$ diverges in $\Teich(S_g)$ and hence in $\calC$ we get $\lambda_j\to 0$. We get
$$i(\alpha,\alpha) = \lim_{j\to \infty} i(\lambda_jm_j, \lambda_jm_j) =  -\pi^2\chi(S_g) \lim_{j\to \infty} \lambda_j^2 = 0.$$
In particular $[\alpha]\not\in \pi(\Teich(S_g))$. Therefore the restriction $\pi\colon \Teich(S_g) \to \pi(\Teich(S_g))$ is proper and hence a homeomorphism. 
\end{proof}

We will since now consider both $\calS$ and $\Teich(S_g)$ embedded in $\matP\calC$. 


\subsection{Thurston's compactification}
We consider the closure $\overline{\Teich(S_g)}$ of $\Teich(S_g)$ inside $\matP\calC$. This closure is compact since $\matP\calC$ is, and it is called the \emph{Thurston compactification} of Teichm\"uller space. We define its \emph{boundary} simply as
$$\partial\Teich(S_g) = \overline{\Teich(S_g)} \setminus \Teich(S_g).$$ 
Our aim is now to identify the topology of the Thurston boundary.
The proof of Proposition \ref{embed:Teich:prop} already shows the following.

\begin{prop} \label{alpha:zero:prop}
The Thurston boundary consists of projective currents $[\alpha]$ with $i(\alpha,\alpha)=0$.
\end{prop}

We will later prove that the Thurston boundary actually consists of \emph{all} the projective currents $[\alpha]$ with $i(\alpha,\alpha)=0$. For the moment we content ourselves with some examples. 


\subsection{Weighted pants decompositions}
We construct some geodesic currents based on geodesic pants decompositions. We will need the following.

\begin{ex} \label{pants:simple:line:ex}
Let $P$ be a hyperbolic geodesic pair-of-pants. Every simple geodesic $\gamma$ in the interior of $P$ is open and has both ends that converge to $\partial P$, winding around it.
\end{ex}
\begin{proof}[Hint]
Decompose $P$ into two right-angled hexagons.
\end{proof}

Let a \emph{weighted pants decomposition} for $S_g$ be a pants decomposition $\mu = \gamma_1 \sqcup \ldots \sqcup \gamma_{3g-3}$ equipped with some real numbers $\lambda_1,\ldots,\lambda_{3g-3}\geqslant 0$. A weighted pants decomposition defines a geodesic current $\mu = \lambda_1\gamma_1+\ldots + \lambda_{3g-3}\gamma_{3g-3}$ such that $i(\mu,\mu)=0$.\index{pants decomposition!weighted pants decomposition} 

We will soon prove that $[\mu]$ lies in the Thurston boundary if $\mu\neq 0$. We will need the following lemma that characterises the positively weighted pants decompositions among all currents.

\begin{lemma}
Let $\mu = \sum \lambda_i\gamma_i$ be a weighted pants decomposition with all positive weights $\lambda_i>0$. A current $\alpha \in \calC$ has $i(\alpha,\alpha) = i(\alpha,\mu)=0$ if and only if $\alpha = \sum \lambda_i'\gamma_i$ for some weights $\lambda_i'\geqslant 0$.
\end{lemma}
\begin{proof}
If $\alpha = \sum \lambda_i'\gamma_i$, then clearly $i(\alpha,\alpha) = i(\alpha,\mu)=0$. Conversely, let $\alpha$ be a current with $i(\alpha,\alpha) = i(\alpha, \mu)=0$. Since $\lambda_i>0$, the support of $\mu$ is the preimage in $\matH^2$ of the geodesic pants decomposition. Since $i(\alpha, \mu)=0$, the support of $\alpha$ consists of lines that are either contained or disjoint from that of $\mu$. 

By Exercise \ref{pants:simple:line:ex} a line $l$ of the latter type has both its endpoints at the endpoints of some line of $\mu$, so there are only countably many of them overall; they are not atomic since their projection in $S_g$ is not closed and hence have zero mass. So such lines $l$ do not occur. The support of $\alpha$ is hence contained in that of $\mu$ and the proof is complete.
\end{proof}

We now characterise simple closed curves.

\begin{lemma} \label{characterize:S:lemma}
Let $\gamma\in\calS$ be a simple closed curve and $\mu\in\calC$ be a non-trivial current. If $i(\gamma,\alpha)=0$ implies $i(\mu,\alpha)=0$ for all $\alpha\in\calS$, then $[\mu] = [\gamma]$.
\end{lemma}
\begin{proof}
Extend $\gamma=\gamma_1$ to a geodesic pants decomposition $\beta = \sum_i\gamma_i$. The previous lemma implies that $\mu = \sum_i\lambda_i\gamma_i$ and by letting the pants decomposition vary we get $\mu = \lambda_1\gamma_1$.
\end{proof}


\subsection{Pinching and twisting} \label{pinching:twisting:subsection}
How can we construct sequences of hyperbolic metrics on $S_g$ that converge to some point at infinity? We can do this quite easily by \emph{pinching} a simple geodesic, or by \emph{twisting} along it. 

To define the former, we need to fix some Fenchel--Nielsen coordinates $(l_i, \theta_i)$ for $\Teich(S_g)$ based on a pants decomposition $\mu = \gamma_1\sqcup \ldots \sqcup \gamma_{3g-3}$.
Fix a metric $(l_i,\theta_i) \in \Teich(S_g)$. A \emph{pinching} along $\gamma=\gamma_1$ is any sequence of metrics where the first length coordinate $l_1$ tends to zero and all the other coordinates are kept bounded (from above and below).

\begin{prop}
The limit of a pinching is $[\gamma]$.
\end{prop}
\begin{proof}
By the Collar Lemma \ref{collar:lemma}, the length of a closed geodesic $\alpha$ in the pinched metrics tends to infinity if $i(\gamma,\alpha)>0$ and stays bounded if $i(\gamma,\alpha)=0$. Therefore the pinched metrics tend in $\matP\calC$ to a class $[\mu]$ such that $i(\gamma,\alpha) = 0 \Rightarrow i(\mu,\alpha)=0$ for all $\alpha \in \calS$. Lemma 
\ref{characterize:S:lemma} gives $[\mu] = [\gamma]$.
\end{proof}

Let $m\in \Teich(S_g)$ be any metric and $\gamma$ be a closed geodesic.  We denoted by $m_\theta^\gamma$ the metric obtained from $m$ via an earthquake of angle $\theta$ along $\gamma$, see Section \ref{earthquakes:subsection}.

\begin{prop}
The limit of $m_\theta^\gamma$ as $\theta \to \pm \infty$ is $[\gamma]$.
\end{prop}
\begin{proof}
By Proposition \ref{strettamente:convessa:prop} the length of a closed geodesic $\alpha$ tends to infinity if $i(\gamma,\alpha)>0$ and is constant if $i(\gamma,\alpha)=0$. We conclude as above that the metrics tend to $[\gamma]$.
\end{proof}



To appreciate the qualitative difference between pinching and twisting along $\gamma$, recall the explicit torus case from Section \ref{length:torus:subsection}: if we pinch along $\gamma$, the sequence of metrics converge to $[\gamma]\in \partial \matH^2$ roughly like a geodesic pointing to $[\gamma]$, while if we twist along $\gamma$ it does so along a horosphere centred at $[\gamma]$.

We have discovered in particular that the set $\calS$ is entirely contained in Thurston's boundary. To fully identify the Thurston boundary, we now analyse the geodesic currents $\alpha$ lying in the ``light cone'', that is those with $i(\alpha,\alpha)=0$. We already know that the weighted pants decompositions are there, but there is more: we will soon see that the light cone contains many new fascinating objects called \emph{laminations}.
