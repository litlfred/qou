---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-038-73-fenchelnielsen-coordinates
section_title: "Fenchel–Nielsen coordinates"
section_number: 7.3
pages: 210-219
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.996
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
It is now time to fix a global set of coordinates for the Teichm\"uller space when $g\geqslant 2$. These are the \emph{Fenchel--Nielsen coordinates} and they identify $\Teich(S_g)$ with $\matR^{6g-6}$, more precisely with $\matR_{>0}^{3g-3} \times \matR^{3g-3}$. 


\subsection{The coordinates}
We want to construct a parametrisation for $\Teich(S_g)$ when $g\geqslant 2$. To identify a finite-dimensional vector space with $\matR^n$ one needs to fix a basis; likewise, here the parametrisation depends on the choice of a  frame.\index{Fenchel--Nielsen coordinates} 

Let $S_g$ be oriented. A \emph{frame} for $S_g$ consists of two essential multicurves $\mu$ and $\nu$ in minimal position, such that:

\begin{enumerate}
\item the multicurve $\mu$ is a pants decomposition,
\item the multicurve $\nu$ decomposes every pair-of-pants in two hexagons.
\end{enumerate}

\begin{figure}
\begin{center}
\includegraphics[width = 10cm] {\iftoggle{BW}{decomposizione2-BW}{decomposizione}}
\nota{A frame for the Fenchel-Nielsen coordinates consists of a (\iftoggle{BW}{light grey}{red}) pants decomposition $\mu$ and a (\iftoggle{BW}{dark grey}{blue}) transverse multicurve $\nu$ that cuts each pair of pants into two hexagons. The number of components of $\mu$ is $3g-3$, that of $\nu$ can vary.}
\label{decomposizione:fig}
\end{center}
\end{figure}

An example that generalises easily to any genus $g\geq 2$ is shown in Figure \ref{decomposizione:fig}. The pants decomposition $\mu = \gamma_1\sqcup \ldots \sqcup \gamma_{3g-3}$ consists of $3g-3$ curves, while the number of curves in $\nu$ is not fixed a priori and depends on our choice of $\nu$.
We now show that a frame induces a \emph{Fenchel--Nielsen} map
\begin{align*}
\FN\colon \Teich(S_g) & \longrightarrow \matR_{>0}^{3g-3} \times \matR^{3g-3} \\
m & \longmapsto  (l_1,\ldots, l_{3g-3}, \theta_1, \ldots, \theta_{3g-3}).
\end{align*}
The map $\FN$ is defined as follows. Let $m\in \Teich(S_g)$ be a hyperbolic metric. The $3g-3$ \emph{length parameters} $l_i = \ell^{\gamma_i}(m)$ are defined using the length functions: the multicurve $\mu$ has a unique geodesic representative 
$$\bar \mu = \bar{\gamma}_1\sqcup \ldots \sqcup \bar{\gamma}_{3g-3}$$ 
in the metric $m$ by Corollary \ref{isotopia:geodetiche:cor}, and $l_i$ is the length of $\bar{\gamma}_i$. Note that these parameters depend only on $\mu$ and not on $\nu$.

The \emph{torsion angles} $\theta_i$ are more subtle to define: the geodesic multicurve $\bar \mu$ decomposes $S_g$ into geodesic pairs-of-pants, and the angle $\theta_i$ measures somehow the way the two geodesic pairs-of-pants are glued along the closed geodesic $\bar \gamma_i$. The precise definition of $\theta_i$ needs the auxiliary multicurve $\nu$. 

\begin{figure}
\begin{center}
\includegraphics[width = 11cm] {\iftoggle{BW}{Teichmuller0-BW}{Teichmuller0}}
\nota{A closed geodesic $\bar \gamma_1$ and the two adjacent pairs-of-pants. The torsion parameter $\theta_1$ measures the distance (in the universal covering) between two orthogeodesics (\iftoggle{BW}{in light grey}{coloured in green}) via the formula $\theta_i = \frac{2\pi s_i}{l_i}$.}
\label{Teichmuller:fig}
\end{center}
\end{figure}

We fix $i=1$ for simplicity and define $\theta_1$.
Figure \ref{Teichmuller:fig}-(left) shows the two geodesic pants adjacent to $\bar{\gamma}_1$ (they might coincide). The second multicurve $\nu$ intersects these pants in four \iftoggle{BW}{dark grey}{blue} arcs, two of which $\lambda$, $\lambda'$ intersect $\bar{\gamma}_1$: we pick one, say $\lambda$. We fix a lift $\tilde P\in\matH^2$ of $P=\bar{\gamma}_1\cap\lambda$ and we lift all the curves incident to $P$: the geodesic $\bar{\gamma}_1$ lifts to a line $\tilde{\gamma}_1$ and $\lambda$ lifts to a (non-geodesic) curve $\tilde\lambda$ that connects two lifts $\tilde{\gamma}_2$ and $\tilde{\gamma}_3$ of the closed geodesics $\bar{\gamma}_2$ and $\bar{\gamma}_3$. See Figure \ref{Teichmuller:fig}-(right).

We draw as in the figure the unique orthogeodesics connecting $\tilde{\gamma}_1$ to $\tilde{\gamma}_2$ and $\tilde{\gamma}_3$ and we denote by $s_1$ the signed length of the segment in $\tilde{\gamma}_1$ comprised between these two orthogeodesics, with positive sign if (as in the figure) an observer walking on a orthogeodesic towards $\tilde{\gamma}_1$ sees the other orthogeodesic on its left (here we use the orientation of $S_g$). 

By repeating this construction for each $\bar{\gamma}_i$ we find some real numbers $s_i$. Finally, the torsion parameter $\theta_i$ is 
$$\theta_i = \frac {2\pi s_i}{l_i}.$$

\begin{figure}
\begin{center}
\includegraphics[width = 5cm] {\iftoggle{BW}{Teichmuller2-BW}{Teichmuller2}}
\nota{If we pick $\lambda'$ instead of $\lambda$ we find a segment of the same length $s_1$. This holds because the two geodesic pairs-of-pants incident to $\gamma_1$ decompose into two hexagons isometric to $A$ and $B$ as shown, and the sides of $A$ and $B$ contained in $\tilde{\gamma}_1$ have the same length $\frac{l(\gamma_1)}2$, that is half the length of $\gamma_1$.}
\label{Teichmuller2:fig}
\end{center}
\end{figure}

\begin{teo}[Fenchel-Nielsen coordinates]
The map $\FN$ is well-defined and is a bijection.
\end{teo}
\begin{proof}
We first note that in the definition of the torsion parameters we could have chosen $\lambda'$ instead of $\lambda$. We would have obtained the same length $s_i$ as shown in Figure \ref{Teichmuller2:fig}. Moreover a hyperbolic metric $m'$ isometric to $m$ through a diffeomorphism $\varphi$ isotopic to the identity has the same parameters $l_i$ and $\theta_j$ since they depend only on the isotopy classes of $\mu$ and $\nu$. Therefore $\FN$ is well-defined.

We prove that $\FN$ is surjective. For every vector $(l_1,\ldots,l_{3g-3})\in\matR_{>0}^{3g-3}$ we may use Proposition \ref{pantaloni:prop} and construct a metric on $S_g$ by assigning to each pair-of-pants of the pants decomposition $\mu$ the (unique) hyperbolic metric with boundary lengths $l_i$. We get a metric with some arbitrary torsion angles $\theta$, which can be changed arbitrarily by an earthquake along $\mu$: it is easy to check that an earthquake with angles $\theta'$ changes the torsion angles from $\theta$ to $\theta+\theta'$, hence any torsion parameter can be realised and $\FN$ is surjective.

We prove that $\FN$ is injective. If $\FN(m) = \FN(m')$, up to acting via earthquakes we may suppose that $\FN(m)=\FN(m') = (l_1,\ldots,l_{3g-3},0,\ldots,0)$. Since the torsion parameter is zero, the orthogeodesics in Figure \ref{Teichmuller:fig}-(right) match and project in $S_g$ to a geodesic multicurve $\bar \nu$ isotopic to $\nu$ and orthogonal to $\bar\mu$. Therefore $S_g\setminus (\bar\mu \cup \bar\nu)$ is a tessellation of $S_g$ into right-angled hexagons, determined by the lengths $l_i$. Both metrics $m$ and $m'$ have the same tessellation and are hence isometric, via an isometry which is isotopic to the identity.
\end{proof}

\begin{oss}
As shown in the proof, the torsion parameters for $m$ are zero if and only if the geodesic representatives $\bar \nu$ and $\bar \mu$ of $\nu$ and $\mu$ are everywhere orthogonal. 
\end{oss}



\subsection{Length functions of $9g-9$ curves}
It is now natural to ask whether the length functions determine every point in $\Teich(S_g)$. The answer is positive; as usual, to warm up we start by examining the torus.

\begin{figure}
\begin{center}
\includegraphics[width = 7cm] {\iftoggle{BW}{torus_3_curves-BW}{torus_3_curves}}
\nota{The curves $\gamma$\iftoggle{BW}{}{ (red)}, $\gamma'$\iftoggle{BW}{}{ (blue)}, and $\gamma'' = T_{\gamma}(\gamma')$\iftoggle{BW}{}{ (green)} on the torus.}
\label{torus_3_curves:fig}
\end{center}
\end{figure}

Let $\gamma,\gamma'$ be two simple closed curves in the torus $T$ with $i(\gamma, \gamma')=1$ and let $\gamma'' = T_{\gamma}(\gamma')$ be obtained by Dehn twisting $\gamma'$ along $\gamma$, see Figure \ref{torus_3_curves:fig}.

\begin{prop} \label{3:prop}
The map
\begin{align*}
L\colon \Teich(T) & \longrightarrow \matR_{>0}^{3} \\
m & \longmapsto \big(\ell^{\gamma}(m), \ell^{\gamma'}(m), \ell^{\gamma''}(m)\big)
\end{align*}
is injective.
\end{prop}
\begin{proof}
After fixing $\gamma$ and $\gamma'$ as a homology basis, we have $\gamma = (1,0)$, $\gamma' = (0,1)$, and $\gamma'' = (1,-1)$. Proposition \ref{lunghezza:toro:prop} gives
$$L(z) = \left(\frac{1}{\sqrt{\Im z}}, \frac{|z|}{\sqrt{\Im z}}, \frac{|z-1|}{\sqrt{\Im z}} \right)$$
which is easily seen to be injective on $\Teich(T) = H^2$.
\end{proof}

A similar set of $9g-9$ curves does the job on $S_g$ when $g\geqslant 2$.
Let $\mu = \gamma_1\sqcup \ldots \sqcup \gamma_{3g-3}$ be a pants decomposition for $S_g$. For each $\gamma_i$ we choose a curve $\gamma_i'$ as in Figure \ref{dual_curves:fig}, and we indicate by $\gamma_i'' = T_{\gamma_i}(\gamma_i')$ the curve obtained by Dehn-twisting $\gamma_i'$ along $\gamma_i$, see an example in Figure \ref{dual_curves2:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 4cm] {\iftoggle{BW}{dual_curves2-BW}{dual_curves2}}
\nota{The curves $\gamma_i$\iftoggle{BW}{}{ (red)}, $\gamma_i'$\iftoggle{BW}{}{ (blue)}, and $\gamma_i'' = T_{\gamma_i}(\gamma_i')$\iftoggle{BW}{}{ (green)} when $\gamma_i$ is adjacent twice to the same pair of pants. It is an instructive exercise to draw $\gamma_i'$ and $\gamma_i''$ when $\gamma_i$ is incident to distinct pair of pants.}
\label{dual_curves2:fig}
\end{center}
\end{figure}

\begin{prop} \label{9g-9:prop}
The map
\begin{align*}
L\colon \Teich(S_g) & \longrightarrow \matR_{>0}^{9g-9} \\
m & \longmapsto \big(\ell^{\gamma_i}(m), \ell^{\gamma_i'}(m), \ell^{\gamma_i''}(m)\big)
\end{align*}
is injective.
\end{prop}
\begin{proof}
We compose $L$ with $\FN^{-1}$ and obtain a map
\begin{align*}
L\circ \FN^{-1}\colon \matR^{3g-3}_{>0} \times \matR^{3g-3} & \longrightarrow \matR_{>0}^{9g-9} \\
(l_i, \theta_i) \quad \ \ & \longmapsto (l_i, l_i', l_i'') 
\end{align*}
We prove that it is injective: it suffices to consider the case where the values $l_i$ are fixed and $\theta_i$ vary. Note that $\gamma_i'$ and $\gamma_i''$ intersect $\gamma_j$ if and only if $i=j$: hence $l_i'$ and $l_i''$ depend only on $\theta_i$ and not on the other torsion parameters $\theta_j$. Proposition \ref{strettamente:convessa:prop} says that $l_i' = f(\theta_i)$ is strictly convex and Proposition \ref{root:prop} gives $l_i'' = f(\theta_i+2\pi)$. 
A strictly convex proper function $f\colon\matR \to \matR$ is at most 2 to 1, hence the function 
\begin{align*}
\matR & \longrightarrow \matR \times \matR \\
\theta_i & \longmapsto \big(f(\theta_i), f(\theta_i + 2 \pi)\big)
\end{align*}
is injective. Therefore $L$ is injective. 
\end{proof}


\subsection{Collar lemma}
The thick-thin decomposition theorem implies that the closed geodesics of length smaller than a Margulis constant $\varepsilon_2$ on a complete hyperbolic surface are simple and have disjoint $R$-neighbourhoods (see Corollary \ref{simple:small:geodesics:cor}). When the curves are very short, one may choose $R$ to be very large: this fact is called the \emph{collar lemma} and we prove it directly using elementary tools.\index{collar lemma}

\begin{figure}
\begin{center}
\includegraphics[width = 11cm] {\iftoggle{BW}{collar-BW}{collar}}
\nota{Pick a segment of length $l$ and draw two perpendiculars at the endpoints: this determines a quadrilateral with two ideal vertices; let $f(l)$ be the distance between the opposite sides $l$ and $r$ (left). A geodesic pair-of-pants is the union of two isometric hexagons, which form in $\matH^2$ a right-angled octagon as drawn. The picture shows that the closed boundary geodesics $a$ and $b$ have disjoint $f(a)$ and $f(b)$-neighbourhoods, coloured here in \iftoggle{BW}{light grey}{yellow} (right).} 
\label{collar:fig}
\end{center}
\end{figure}

For any number $l>0$, draw the quadrilateral as in Figure \ref{collar:fig}-(left) and define $f(l)$ to be the distance between its opposite sides $l$ and $r$.

\begin{ex} The function $f\colon \matR_{>0}\to \matR_{>0}$ is strictly decreasing and a homeomorphism. In particular we get
$\lim_{l \to 0} f(l) = \infty$. 
Explicitly, we have 
$$\sinh f(l) = \frac{1}{\sinh \frac l2}.$$ 
\end{ex}
\begin{proof}[Hint]
Put $l$ in vertical position in $H^2$ and use Lemma \ref{cosh:cos:lemma}.
\end{proof}

The function $f$ is simple to define, and is particularly useful.

\begin{prop} \label{collar:pants:prop}
Let $P$ be a geodesic pair-of-pants with boundary lengths $a,b$, and $c$. The $f(a)$, $f(b)$, and $f(c)$-neighbourhoods of the boundary components form three disjoint collars.
\end{prop}
\begin{proof}
Consider two boundary components $a$ and $b$. 
The geodesic pair-of-pants $P$ is divided into two isometric hexagons, and we lift them to $\matH^2$ where they form a right-angled octagon as in Figure \ref{collar:fig}-(right). The picture shows that the $f(a)$ and $f(b)$-neighbourhoods of $a$ and $b$ are disjoint.
\end{proof}

Here is the collar lemma.

\begin{lemma}[Collar lemma] \label{collar:lemma}
Let $g\geqslant 2$ and $S_g$ have a hyperbolic metric. Disjoint simple closed geodesics $\gamma_1, \ldots, \gamma_k$ of length $l_1,\ldots, l_k$ have disjoint tubular $f(l_i)$-neighbourhoods. 
\end{lemma}
\begin{proof}
We may suppose (by adding more simple closed geodesics if necessary) that the closed geodesics form a pants decomposition, and it suffices to consider two curves that cobound the same pair-of-pants. Proposition \ref{collar:pants:prop} applies.
\end{proof}

We recall from Corollary \ref{simple:small:geodesics:cor} that every closed geodesic shorter than $\varepsilon_2$ is simple. Therefore very short closed geodesics are simple and have large disjoint tubular neighbourhoods: the more we shrink the curves, the larger are their neighbourhoods, and hence the larger is the diameter of the surface (the diameter of a metric space is the supremum of the distance of its points). In particular, if on a sequence of closed hyperbolic surfaces the injectivity radius tends to zero, their diameters must tend to infinity.

Among the many consequences of the collar lemma, we focus on a simple inequality which relates the geometric intersection of simple closed geodesics to their lengths. We denote by $L(\gamma)$ the length of $\gamma$.

\begin{cor}  \label{strizza:cor}
Let $g\geqslant 2$ and $S_g$ have a hyperbolic metric. Let $\gamma$ and $\eta$ be two simple closed geodesics in $S_g$. The following inequality holds:
$$L(\eta)\geqslant 2i(\eta, \gamma) \cdot f(L(\gamma)).$$
\end{cor}
\begin{proof}
The geodesic $\gamma$ has a tubular $f(L(\gamma))$-neighbourhood. The geodesic $\eta$ intersects $\gamma$ in $i(\eta,\gamma)$ points and hence crosses the tubular neighbourhood at least $i(\eta,\gamma)$ times, each with a segment of length $\geqslant 2f(L(\gamma))$.
\end{proof}


\subsection{A topology for the Teichm\"uller space} \label{Topology:Teich:subsection}
There are various equivalent ways to assign a topology to the Teichm\"uller space. 
On the torus $T$, we have seen that $\Teich(T)$ can be identified with the hyperbolic plane $\matH^2$, and the mapping class group acts as isometries on it: we could not hope for a better picture of $\Teich(T)$ and we are fully satisfied.

When $g\geqslant 2$ we could similarly use the Fenchel-Nielsen coordinates and give $\Teich(S_g)$ the topology of $\matR^{6g-6}$, but then to be honest we should also check that the topology does not depend on the frame... we prefer to equip the Teichm\"uller space with an intrinsic topology and then prove that the Fenchel-Nielsen coordinates are homeomorphisms.\index{$\calS$} 

We indicate by $\calS= \calS(S_g)$ the set of all the non-trivial simple closed curves in $S_g$, considered up to isotopy and orientation reversal (we say that the curves are \emph{unoriented}). Each element $\gamma\in\calS$ induces a length function
$$\ell^\gamma\colon \Teich(S_g) \longrightarrow \matR_{>0}.$$
We indicate as usual with $\matR^\calS$ the set of all functions $\calS \to \matR$ and give it the usual product topology (the weakest one such that all the projections are continuous). The natural map
\begin{align*}
\Teich(S_g) & \longrightarrow \matR^\calS \\
m & \longmapsto \big( \gamma \longmapsto \ell^\gamma(m) \big)
\end{align*}
is injective by Propositions \ref{3:prop} and \ref{9g-9:prop}. We may hence consider $\Teich(S_g)$ as a subspace of $\matR^\calS$ and assign it the subspace topology. This topology on $\Teich(S_g)$ is the weakest one where the length functions $\ell^\gamma$ are continuous.
Recall that a topological space is \emph{second-countable} if it has a countable base.

\begin{prop}
The space $\matR^\calS$ is Hausdorff and second-countable.
\end{prop}
\begin{proof}
Every product of Hausdorff spaces is Hausdorff, and every countable product of second-countable spaces is second-countable.
\end{proof}

We recall the following topological fact.

\begin{prop} \label{propria:chiusa:prop}
Let $f\colon X \to Y$ be a continuous and proper map between topological spaces. If $Y$ is Hausdorff and second-countable then $f$ is closed.
\end{prop}

Proper maps onto reasonable spaces are closed. If they are also injective, we can obtain more.

\begin{cor} \label{propria:chiusa:cor}
Let $f\colon X \to Y$ be a continuous, proper, and injective map between topological spaces. If $Y$ is Hausdorff and second-countable then $f$ is a homeomorphism onto its image. 
\end{cor}

We will use this corollary in a moment.
Recall that every isometry $\varphi\in \Iso^+(H^2) = \PSLR$ has a trace $\tr \varphi$ defined only up to sign, whose modulus is $>2$ precisely when $\varphi$ is hyperbolic, see Proposition \ref{PSLR:prop}.

\begin{prop} \label{trace:prop}
Let $S = \matH^2/_\Gamma$ be an orientable hyperbolic surface. Every hyperbolic transformation $\varphi\in\Gamma$ produces a closed geodesic $\gamma$ in $S$
with
$$|\tr\varphi| = 2\cosh \frac {L(\gamma)} 2.$$
\end{prop}
\begin{proof}
Up to conjugacy we have $\varphi(z) = e^{L(\gamma)} z$. The matrix is 
$$\varphi = \left(\begin{matrix} e^{\frac{L(\gamma)}2} & 0 \\ 0 & e^{-\frac{L(\gamma)}2} \end{matrix}\right)$$
hence $|\tr\varphi| = 2\cosh \frac{L(\gamma)}2$.
\end{proof}

In particular, the length of $\gamma$ depends continuously on the transformation $\varphi$. We will use this fact to prove the following. We suppose $g\geqslant 2$.

\begin{prop} \label{FN:omeom:prop}
The Fenchel-Nielsen map 
$$\FN\colon \Teich(S_g) \longrightarrow \matR_{>0}^{3g-3}\times\matR^{3g-3}$$
is a homeomorphism.
\end{prop}
\begin{proof}
We consider $\Teich(S_g)$ inside $\matR^\calS$ and examine the inverse map
$$\FN^{-1}\colon\matR_{>0}^{3g-3}\times\matR^{3g-3} \longrightarrow \matR^\calS.$$

We prove that $\FN^{-1}$ is continuous. The map $\FN^{-1}$ assigns to the parameters $(l_i, \theta_i)$ a metric on $S_g$ constructed by attaching right-angled hexagons. Both the hexagons and the attaching maps depend continuously on the parameters $(l_i, \theta_i)$ and lift to a tessellation of $\matH^2$ into hexagons. Since the decomposition into hexagons varies continuously, its deck transformations vary continuously in $\PSLR$ and hence the length functions too by Proposition \ref{trace:prop}. Therefore $\FN^{-1}$ is continuous.

We prove that $\FN^{-1}$ is proper. Take a diverging sequence of parameters $(l_i,\theta_i)$ (that is, without converging subsequences) in $\matR_{>0}^{3g-3}\times \matR^{3g-3}$: we need to show that its image is also a diverging subsequence. The thesis is equivalent to show that the length function of some curve goes to infinity. If $l_i\to +\infty$ for some $i$ we are done. If $l_i\to 0$, the length of any curve intersecting essentially the shrinking curve $\gamma_i$ goes to infinity by Corollary \ref{strizza:cor}. It remains to consider the case where the length parameters $l_i$ converge to some non-zero value, but some twist parameter $\theta_j$ goes to infinity: in that case the length of any curve intersecting the twisted curve $\gamma_j$ goes to infinity by Proposition \ref{strettamente:convessa:prop}.

Finally, the map $\FN^{-1}$ is a homeomorphism onto its image by Corollary \ref{propria:chiusa:cor}. The proof is complete.
\end{proof}

During the proof we have also discovered the following.

\begin{prop} \label{diverges:infinity:prop}
If a sequence $m_i\in\Teich(S_g)$ diverges, there is a $\gamma \in \calS$ such that $\ell^\gamma(m_i) \to \infty$ on a subsequence.
\end{prop}

Recall that the action of a topological group $G$ on a topological space $X$ is \emph{continuous} if the action map $G\times X \to X$ is continuous. This implies that $G$ acts on $X$ by homeomorphisms. We give the mapping class group $\MCG(S_g)$ the discrete topology.

\begin{prop}
The earthquakes and mapping class group actions on the Teichm\"uller space are continuous.
\end{prop}
\begin{proof}
The mapping class group acts on $\calS$ by permutations, hence its action on $\matR^\calS$ is continuous. On Fenchel-Nielsen coordinates the earthquake action sends $\theta$ to $\theta+\theta'$ and is hence continuous.
\end{proof}

The immersion in $\matR^{9g-9}$ is also a topological embedding.

\begin{prop}
The injective representation $\Teich(S_g) \hookrightarrow \matR^{9g-9}$
furnished by Proposition \ref{9g-9:prop} is a homeomorphism onto its image.
\end{prop}
\begin{proof}
Using Fenchel-Nielsen coordinates the map is clearly continuous. The proof that it is proper is as in Proposition \ref{FN:omeom:prop}.
\end{proof}


\subsection{Surfaces of finite type} \label{Teich:finite:type:subsection}
We have considered only closed surfaces $S_g$ for simplicity, but most of the arguments exposed in this chapter extend easily to all surfaces $S_{g,b,p}$ of finite type with negative Euler characteristic. 

The Teichm\"uller space $\Teich(S_{g,b,p})$ is the set of all the complete hyperbolic metrics with geodesic boundary, considered up to isometries that are isotopic to the identity. Fenchel-Nielsen coordinates are defined analogously: the surface decomposes into $-\chi(S_{g,b,p}) = 2g+b+p-2$ pairs-of-pants, and the interior curves of the decomposition are 
$$\frac 12 \big(3(2g+b+p-2) - b - p \big) = 3g+b+p-3.$$
The Fenchel-Nielsen coordinates are
$$\big(l_1, \ldots, l_{3g+b+p-3}, l_1^\partial, \ldots, l_b^\partial, \theta_1,\ldots, \theta_{3g+b+p-3}\big)$$
where the $l_i$ and $l_j^\partial$ are the length parameters of the $3g+b+p-3$ interior and $b$ boundary curves, and the $\theta_i$ are the torsion angles of the interior curves. We get a bijection
$$\FN\colon \Teich (S_{g,b,p}) \longrightarrow \matR_{>0}^{3g+2b+p-3} \times \matR^{3g+b+p-3}$$
which is a homeomorphism with respect to the natural topology on Teichm\"uller space as a subset of $\matR^\calS$. Therefore the Teichm\"uller space is homeomorphic to a ball of dimension $-3\chi(S_{g,b,p})-p$.

For instance, the Teichm\"uller space of a pair-of-pants is $\matR_{>0}^3$ parametrized by the lengths of the boundary geodesics, while that of a thrice-punctured sphere is a point (there is a unique metric).

An alternative description of the Teichm\"uller space for punctured surfaces, with ideal triangles playing the role of pairs-of-pants, is described in the next section.
