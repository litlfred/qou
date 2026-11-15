---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-053-102-circle-bundles
section_title: "Circle bundles"
section_number: 10.2
pages: 318-321
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.788
latex_coverage_ratio: 0.991
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We now introduce another simple class of 3-manifolds, the orientable circle bundles over some compact surface $S$. We will discover that there is essentially only one circle bundle if $S$ has boundary, and infinitely many if $S$ is closed, distinguished by an integer called the \emph{Euler number}.


\subsection{The trivial circle bundle}
Let $S$ be a compact connected surface. As every connected manifold, the surface $S$ has a unique orientable line bundle
$$S\times I \quad {\rm or} \quad S\timtil I$$ 
depending on whether $S$ is orientable or not. We denote by 
$$M=S\times S^1 \quad {\rm or} \quad S\timtil S^1$$ 
respectively the double of $S\times I$ and $S\timtil I$ along its boundary. If we do not know whether $S$ is orientable or not, we use the symbols $S\timforsetil I$ and $S\timforsetil S^1$ to denote these objects. The manifold $S\timforsetil S^1$ is an orientable circle bundle over $S$, called the \emph{trivial} one. 


\subsection{Circle bundles with boundary}
We start by exploring the case where the base surface $S$ has non-empty boundary: in this case every bundle $M$ over $S$ is a 3-manifold with boundary; the boundary consists of tori, one fibering above each circle in $\partial S$, because the torus is the unique orientable surface that fibres over $S^1$.

It turns out that there is essentially only one bundle over $S$, the trivial one:

\begin{lemma} \label{unique:lemma}
If $\partial S \neq \emptyset$, the orientable circle bundles on $S$ are all isomorphic.
\end{lemma}
\begin{proof}
Let $N\to S$ be an orientable circle bundle. Decompose $S$ as a disc $D$ with some pairs of disjoint segments $(I_i, J_i)$ in $\partial D$ to be glued. Since $D$ is contractible the restriction of $N$ to $D$ is a product $D\times S^1$ and $N$ is obtained from it by gluing the annuli $I_i\times S^1$ and $J_i\times S^1$ via orientation-reversing fibre-preserving maps. Two such maps are always isotopic (exercise) and hence $N$ is uniquely determined.
\end{proof}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{section-BW}{section}}
\nota{A twist along a fibered annulus $A$ modifies a section $S$ as shown.}
\label{section:fig}
\end{center}
\end{figure}

We now want to study the \emph{sections} of the trivial bundle $M\to S$, because these will be useful in the study of bundles over closed surfaces. We now discover that, although the bundle is trivial, it contains many non isotopic sections, and we want to classify them.

Recall that a \emph{section} of the bundle $\pi\colon M\to S$ is a map $i\colon S\to M$ such that $\pi\circ i = \id$. Since the section $i$ is determined by its image $i(S)$, we simply consider the surface $i(S)$ as a section of $\pi$. By construction $M$ is the double of an interval bundle over $S$ and as such it contains the \emph{zero-section} $S$ there. However, this section is not unique in general, not even up to isotopy. 

To modify a section, pick a properly embedded arc in $S$. The arc determines a fibered annulus $A\subset M$ above it, which we may use to \emph{twist} the section as shown in Figure \ref{section:fig}. This operation modifies the curves $\partial S\subset \partial M$ via two Dehn twists (one positive and one negative) on the tori $\partial M$ along the two curves in $\partial A$.

By twisting along annuli we may construct all the sections of $M$:

\begin{lemma} \label{section:lemma}
Two sections of $S\timforsetil S^1$ are connected by a composition of twists along fibered annuli and fibre-preserving isotopies.
\end{lemma}
\begin{proof}
Let $i_1, i_2$ be two sections. Decompose $S$ as a 0-handle $D$ with some rectangular 1-handles attached to $\partial D$. The bundle is trivial on each handle. Since $D$ is contractible, every map $i\colon D\to S^1$ is homotopic to a constant and we may hence isotope $i_1$ and $i_2$ so that they coincide on $D$. 

See a 1-handle as $[-1,1]^2$ with $\{\pm 1\}\times [-1,1]$ glued to $D$. The sections $i_1, i_2\colon [-1,1]^2 \to S^1$ coincide on $\{\pm 1\}\times [-1,1]$, and up to reparametrising we may suppose that they are constantly $1$ there. The section $i_1 \colon [-1,1]^2 \to S^1$ defines an element $d\in \pi_1(S^1,1) = \matZ$, determined by the loop $t\mapsto i_1(t,u)$, whose homotopy class does not depend on the fixed $u\in [-1,1]$. The section is in fact determined up to isotopy by $d$, and by twisting along the annulus $0 \times [-1,1]$ we can vary this integer arbitrarily. Therefore after some twists and isotopies the sections $i_0$ and $i_1$ are both constantly 1 on 1-handles, and thus coincide everywhere.
\end{proof}

\begin{cor} \label{unique:cor}
If $S$ has only one boundary component, the boundary of a section of $M=S\timforsetil S^1$ is a slope in $\partial M$ that does not depend on the section.
\end{cor}
\begin{proof}
Distinct sections are connected by finitely many Dehn twists along annuli. One such twist acts on the torus $\partial M$ as a composition of two opposite Dehn twists, which cancel each other. Hence it does not affect the boundary slope of a section.
\end{proof}

\begin{ex} Prove this corollary using Proposition \ref{lagrangian:prop}.
\end{ex}


\subsection{Closed circle bundles} \label{closed:circle:subsection}
We now turn to closed circle bundles. In this section we prove that 
the oriented circle bundles over a closed surface are parameterised by an integer called the \emph{Euler number} of the fibering.\index{Euler number}

We prefer to see the bundles over closed surfaces as Dehn fillings of bundles over surfaces with boundary. Here are the details.

Let $S$ be a compact surface with non-empty boundary. Pick $M=S\timforsetil S^1$ and fix an orientation for $M$. Recall that we denote by $S$ the zero-section of $M$. Every boundary component $T$ of $M$ is an oriented torus, which contains two natural unoriented simple closed curves: the boundary $m=T\cap \partial S$ of the section $S$ and the fibre $l$ of the bundle. If oriented, the curves $m$ and $l$ form a basis $(m,l)$ for $H_1(T,\matZ)$. We choose orientations for $m$ and $l$ such that $(m,l)$ form a positively oriented basis: there is a unique choice up to reversing both $m$ and $l$.

A Dehn filling on $T$ is determined as usual by a pair $(p,q)$ of coprime integers that indicate the slope $\pm (pm+ql)$ to be killed. 

Suppose now that $S$ has only one boundary component and let $M^{\rm fill}$ be obtained by Dehn filling $M$ along the slope $(1,q)$. Let $\hat S$ be the closed surface obtained by capping $S$ with a disc.

\begin{prop} \label{classify:bundles:prop}
The circle bundle $M\to S$ extends to a circle bundle $M^{\rm fill}\to \hat S$. Every oriented circle bundle on $\hat S$ is obtained in this way, and distinct values of $q$ yield vector bundles that are not orientation-preservingly isomorphic.
\end{prop}
\begin{proof}
The meridian of the filling solid torus is $m'=m + ql$. The fibre $l$ has geometric intersection 1 with $m'$ and is hence a longitude for the filling solid torus. We may represent the filling solid torus as $D \times S^1$ with $m' = S^1 \times \{y\}$ and $l=\{x\}\times S^1$. The circle bundle $M\to S$ extends naturally to a circle bundle $M^{\rm fill} \to \hat S$ with $\hat S = S\cup D$.

Every closed circle bundle $N\to \hat S$ arises in this way: the bundle above a disc $D\subset \hat S$ is the trivial $D\times S^1$, and if we remove it we get $M \to S$ back. 
The number $q$ is intrinsically determined: the meridian $m$ does not depend on the section of $M\to S$ by Corollary \ref{unique:cor}, and the equality $m' = m+ql$ determines $q$. Therefore distinct values of $q$ yield non-isomorphic bundles.
\end{proof}

The integer $q$ is the \emph{Euler number} of the circle bundle and is usually denoted with the letter $e$. We summarise our discovery:
\begin{cor} \label{unique:e:cor}
For every $e\in \matZ$ and every closed surface $S$ there is a unique oriented circle bundle over $S$ with Euler number $e$.
\end{cor}

A change of orientation for $M$ transforms $e$ into $-e$.
Recall that every closed surface $S$ has a trivial circle bundle $S\timforsetil S^1$ constructed by doubling the unique oriented line bundle on $S$.

\begin{ex} \label{circle:bundle:ex}
An oriented circle bundle over a closed surface is trivial $\Longleftrightarrow$ $e=0$ $\Longleftrightarrow$ the bundle has a section. 
\end{ex}

We may see the Euler number of a bundle $M\to S$ over a closed $S$ as an obstruction for the existence of a section.

\begin{oss} \label{bundle:oss}
Every oriented $n$-dimensional vector bundle $E \to S$ over a closed oriented $n$-manifold $S$ has a \emph{Euler number} defined by taking two generic sections and counting their signed intersections. We briefly explain how this number is closely related to the one we defined here.\index{Euler number}

Each vector bundle $E \to S$ induces a sphere bundle $M\to S$: it suffices to fix a Riemannian metric on $E$ and take the sub-bundle consisting of unit tangent vectors. When $n=2$ we get a circle bundle $M\to S$ and the Euler number of $E\to S$ coincides with that of $M\to S$ that we defined above.

When $E$ is the tangent bundle of $S$, the Euler number is the Euler characteristic $\chi(S)$. For instance, the unit tangent bundle of $S^2$ has Euler number $e=\chi(S^2)=2$ and hence it is diffeomorphic to $L(2,1) = \matRP^3$. 
\end{oss}

\begin{ex} \label{bundle:ex}
Let $M$ be a circle bundle over the genus-$g$ surface $S_g$ with Euler number $e$. We have 
$H_1(M,\matZ) = \matZ^{2g} \times \matZ/_{e\matZ}$.
\end{ex}

\begin{cor} \label{distinct:bundle:cor}
Let $M \to S_g$ and $M' \to S_{g'}$ be circle bundles with Euler numbers $e$ and $e'$. The manifolds $M$ and $M'$ are diffeomorphic $\Longleftrightarrow$ $g=g'$ and $|e|=|e'|$.
\end{cor}

\begin{ex} \label{e:ex}
The circle bundle $M$ over $S^2$ with Euler number $e$ is diffeomorphic to the lens space $L(|e|,1)$.
\end{ex}
\begin{proof}[Hint] The base sphere $S^2$ decomposes into two discs, and the fibration over each disc is a solid torus. Therefore $M$ is the union of two solid tori.
\end{proof}

We end the discussion by defining explicitly a famous non-trivial circle bundle over $S^2$.


\subsection{The Hopf fibration} \label{Hopf:lens:subsection}
The quotient map 
\begin{align*}
(\matC^2)^* & \longrightarrow \matCP^1 \\
(z,w) & \longmapsto [z,w]
\end{align*}
restricts to a circle bundle $S^3 \to \matCP^1 = S^2$ called the \emph{Hopf fibration}.
The fibre over $[z,w]$ is the circle $(\omega z, \omega w)$ as $\omega \in S^1$ varies. See Figure \ref{Hopf:fig}.\index{Hopf fibration}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{Hopf_Fibration-BW}{Hopf_Fibration}}
\nota{The fibre of every point in the Hopf fibration $S^3\to S^2$ is a circle, and the counterimage of a circle in $S^2$ is a torus in $S^3$. The picture shows the counterimage of three circle arcs: each is a portion of standard torus in $S^3 = \matR^3\cup \infty$, foliated by circles of type $(1,1)$.}
\label{Hopf:fig}
\end{center}
\end{figure}

Exercise \ref{e:ex} implies that the Euler number of the Hopf fibration $S^3 \to S^2$ is $\pm 1$, and hence it has no section by Exercise \ref{circle:bundle:ex}.
