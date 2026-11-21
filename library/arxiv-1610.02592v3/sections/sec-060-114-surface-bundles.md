---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-060-114-surface-bundles
section_title: "Surface bundles"
section_number: 11.4
pages: 367-372
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.843
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
Seifert manifolds have base orbifolds of dimension 2 and smooth fibres of dimension 1. We now introduce a complementary construction where the base orbifolds have dimension 1 and the smooth fibres have dimension 2. These are called \emph{surface bundles}.


\subsection{Surface bundles}
A \emph{surface bundle over $S^1$} is a fibre bundle $M\to S^1$ of a compact orientable 3-manifold $M$ (possibly with boundary) over the circle, whose fibre $\Sigma$ is a connected compact orientable surface. If $M$ has boundary, then $\Sigma$ also has, and $\partial M$ consists of tori fibering over $S^1$.\index{surface bundle over $S^1$}

\begin{prop}
Every surface bundle over $S^1$ is constructed by taking $\Sigma\times [0,1]$ and glueing $\Sigma\times 0$ to $\Sigma\times 1$ via an orientation-preserving diffeomorphism $\psi$.
\end{prop}
\begin{proof}
One such glueing clearly gives rise to a surface bundle over $S^1$. Conversely, by cutting a surface bundle over $S^1$ along a fibre we get a surface bundle over the interval, which is a product $\Sigma\times [0,1]$.
\end{proof}

The diffeomorphism $\psi$ is the \emph{monodromy} of the surface bundle $M_\psi$. Since isotopic glueings produce diffeomorphic manifolds, the three-manifold $M_\psi$ depends only of the class of $\psi$ in the mapping class group $\MCG(\Sigma)$ on $\Sigma$. More than that, it actually depends only on its conjugacy class:

\begin{prop}
If $\psi$ and $\phi$ are conjugate in $\MCG(\Sigma)$, then $M_\psi$ and $M_\phi$ are diffeomorphic.
\end{prop}
\begin{proof}
The diffeomorphism $g\colon \Sigma\to \Sigma$ that conjugates them extends to $\Sigma\times [0,1]$ and gives a diffeomorphism $M_\psi \to M_\phi$.
\end{proof}

The manifolds $M_\psi$ and $M_{\psi^{-1}}$ are (orientation-reversingly) diffeomorphic.


\subsection{Properties}
We now start to investigate the topological properties of surface bundles.
Let $M\to S^1$ be a surface bundle with fibre $\Sigma$.

\begin{ex}
The maps $\Sigma\to M \to S^1$ induce an exact sequence
$$0 \longrightarrow \pi_1(\Sigma) \longrightarrow \pi_1(M) \longrightarrow \pi_1(S^1) \longrightarrow 0.$$
\end{ex}

This implies in particular that $\pi_1(M)$ surjects onto $\matZ$ and therefore:

\begin{cor}
We have $b_1(M)\geqslant 1$.
\end{cor}

In other terms, the surface fibre $\Sigma$ is non-separating and hence $[\Sigma]\in H_2(M,\partial M)$ is non-trivial (and has infinite order, since there is no torsion there).

Note that there is an obvious degree-$n$ regular covering $M_{\psi^n} \to M_{\psi}$ for every $n$ and an infinite regular covering $\Sigma\times \matR \to M_{\psi}$ induced by the normal subgroup $\pi_1(\Sigma) \triangleleft \pi_1(M)$. 

\begin{prop}
The fibre $\Sigma$ is an essential surface.
If $\chi(\Sigma)>0$ then $M$ is diffeomorphic to $D\times S^1$ or $S^2\times S^1$.
If $\chi(\Sigma)\leqslant 0$ the universal cover of $\interior M$ is $\matR^3$ and $M$ is Haken.
\end{prop}
\begin{proof}
If $\chi(\Sigma)>0$ then $\MCG(\Sigma)$ is trivial and we are done, so we suppose $\chi(\Sigma)\leqslant 0$. The fibre $\Sigma$ is incompressible because $\pi_1(\Sigma)$ injects, and is also $\partial$-incompressible by a doubling argument (the double $DM$ fibres to $S^1$ with incompressible fibre $D\Sigma$, hence $\Sigma$ is $\partial$-incompressible). The fibre is clearly not $\partial$-parallel, hence it is essential.

The manifold $M$ is covered by $\Sigma \times \matR$, whose interior is covered by $\matR^2 \times \matR = \matR^3$: hence $M$ is irreducible. It is also $\partial$-irreducible because its double also fibres and hence is irreducible. Therefore $M$ is Haken. 
\end{proof}


\subsection{Semi-bundles}
The Seifert fibrations are circle bundles over two-dimensional orbifolds, and likewise it is natural to consider surface bundles over 1-orbifolds. The compact 1-orbifolds are $S^1$ and the closed segment with mirrored endpoints. We have already considered the $S^1$ case and we now define some surface bundles over the closed segment, called \emph{semi-bundles}.

Let $\Sigma$ be a non-orientable surface, with orientable double cover $p\colon \tilde \Sigma \to \Sigma$ and deck transformation $\tau$ that gives $\Sigma=\tilde \Sigma/_\tau$. We have 
$$\Sigma\timtil (-1,1) = \big(\tilde \Sigma \times (-1,1)\big)/_{(\tau, \iota)}$$
with $\iota(x) = -x$. A \emph{local semi-bundle} is the map $\Sigma\timtil (-1,1) \to [0,1)$ that sends $(p,x)$ to $|x|$. The fibre over $0$ is $\Sigma$, that over $x\in (0,1)$ is $\tilde \Sigma$.

A \emph{semi-bundle} $M \to [-1,1]$ is a map which is a local semi-bundle when restricted to $[-1, 1-\varepsilon)$ and $(\varepsilon, 1]$. The fibre over $\pm 1$ is $\Sigma$ and the fibre of $x\in (-1,1)$ is $\tilde \Sigma$. We should think about this object as a surface bundle over the segment orbifold $[-1,1]$ with mirror points $\pm 1$. 

\begin{ex}
Every semi-bundle is constructed by gluing two copies of $\Sigma\timtil [-1,1]$ along their boundaries via some diffeomorphism.
\end{ex}

Set $I = [-1,1]$. Let $M\to I$ be a semi-bundle with fibres $\Sigma$ and $\tilde \Sigma$.
Note that $I=\matR/_\Gamma$ where $\Gamma<\Iso(\matR)$ is generated by the reflections at the points $\pm 1$. The orbifold fundamental group of $I$ is 
$$\pi_1(I) = \Gamma = \matZ/_{2\matZ} * \matZ/_{2\matZ}.$$

\begin{ex}
The maps $\tilde\Sigma\to M \to I$ induce an exact sequence
$$0 \longrightarrow \pi_1(\tilde \Sigma) \longrightarrow \pi_1(M) \longrightarrow \pi_1(I) \longrightarrow 0.$$
\end{ex}

\begin{prop}
If $\chi(\Sigma)>0$ then $M$ is diffeomorphic to $\matRP^2 \timtil S^1$. If $\chi(\Sigma)\leqslant 0$ the orientable fibre $\tilde \Sigma$ is essential, the universal cover of $\interior M$ is $\matR^3$, and $M$ is Haken.
\end{prop}
\begin{proof}
Same proof as in the standard bundle case.
\end{proof}

\begin{ex} \label{semi:iff:ex}
An orientable 3-manifold $M$ has a (semi-)bundle structure if and only if there is an orientable $\Sigma \subset M$ that cuts $M$ into interval bundles.
\end{ex}

Let $M\to I$ be a semi-bundle. We may pull-back the semi-bundle along the orbifold double cover $S^1 \to I$ and get an ordinary surface bundle $\tilde M \to S^1$, so that the following diagram commutes:
$$
\xymatrix{ 
\tilde M\ar@{.>}[r] \ar@{.>}[d] & M \ar[d] \\
S^1\ar[r] & I
}
$$
Every semi-bundle is thus covered by an ordinary bundle.


\subsection{Seifert manifolds} \label{Seifert:fibers:subsection}
We now classify the Seifert manifolds that have a surface (semi-)bundle structure.

\begin{prop} \label{Seifert:bundle:prop}
A Seifert manifold $M$ has a (semi-)bundle structure if and only if one of the following holds: 
\begin{itemize}
\item $\partial M \neq 0$, 
\item $e(M)=0$, 
\item $M = \big(T,(1,e)\big)$ or $\big(K,(1,e)\big)$,
\item $M = \big(S^2, (2,1),\! (2,1),\! (2,1),\! (2,2q+1)\big)$ or $\big(\matRP^2, (2,1),\! (2,2q+1)\big)$.
\end{itemize}
The manifolds in the last line occur only as semi-bundles.
\end{prop}
\begin{proof}
If $\partial M \neq \emptyset$ or $e(M)=0$ then $M\to S$ has an orientable section $\Sigma$, which cuts $M$ into interval bundles: hence $\Sigma$ is a fibre of a (semi-)bundle (see Exercise \ref{semi:iff:ex}).

Let $S$ be one of the orbifolds
$$T, \quad K, \quad (S^2,2,2,2,2), \quad (\matRP^2, 2,2).$$
It contains a circle that splits $S$ into one or two annuli, M\"obius strips, or $(D,2,2)$. 
Every circle fibering over these pieces is an interval bundle by Proposition \ref{diffeo:fiberings:prop}. Therefore every fibering $M \to S$ contains a vertical torus that splits $M$ into interval bundles and is hence a (semi-)bundle.

Conversely, if $M$ has a (semi-)bundle structure the orientable fibre is essential and is hence either horizontal or vertical: we get one of the types listed.
\end{proof}


\subsection{Torus bundles}
A \emph{torus bundle} is of course a surface bundle $M\to S^1$ with fibre a torus $T$. We fix a basis for $\pi_1(T)$, so that $\MCG(T) = \SLZ$. By what said above, every matrix $A\in \SLZ$ defines a torus bundle $M_A$\index{torus bundle} with monodromy $A$. We want to understand when $M_A$ is a Seifert manifold.

\begin{ex} \label{Me:ex}
For every $e\in\matZ$ there are diffeomorphisms 
$$M_{\matr 1e01} \isom \big(T,(1,e)\big), \quad M_{\matr {-1}e0{-1}} \isom \big(K,(1,e)\big). $$
\end{ex}

The classification of torus bundles reduces to linear algebra.

\begin{prop} \label{torus:bundle:classification:prop}
Two torus bundles $M_A$ and $M_{A'}$ are diffeomorphic if and only if $A'$ is conjugate to $A^{\pm 1}$ in $\SLZ$.
\end{prop}
\begin{proof}
Let $M_A \isom M_{A'}$ be a diffeomorphism. Consider the tori $T$ and $T'$ of the two fibrations both inside $M_A$ and minimise their transverse intersection. 

If $T\cap T' = \emptyset$, by Proposition \ref{line:bundles:prop} the tori are parallel and the two fibrations are isotopic: hence $A'$ is conjugate to $A^{\pm 1}$. Otherwise by the same proposition $T'$ decomposes into fibered annuli in the product line bundle $M_A\setminus T$. One such fibered annulus identifies a circle $\gamma\subset T$ preserved by $A$. Therefore $A$ is conjugate to $\matr 1 e 0 1 $ or $\matr {-1} e 0 {-1}$, and $A'$ is conjugate to $\matr 1 {e'} 0 1 $ or $\matr {-1} {e'} 0 {-1}$ for the same reason. Exercise \ref{Me:ex} implies that $A' = A^{\pm 1}$.
\end{proof}

\begin{ex} A matrix $A\in \SLZ$ has finite order if and only if $A=\pm I$ or $|\tr A| < 2$. Every finite-order $A$ is conjugate to one of
$$ 
\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad
\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}, \quad
\begin{pmatrix} -1 & 1 \\ -1 & 0 \end{pmatrix}, \quad
 \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad
\begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}.
$$
These matrices have order 1, 2, 3, 4, 6.
\end{ex}
\begin{proof}[Hint]
Use Proposition \ref{PSLR:prop}.
\end{proof}

We can easily determine whether a torus bundle is Seifert by looking at its monodromy $A$.

\begin{prop} \label{torus:bundle:prop}
Let $M = M_A$ be a torus bundle with monodromy $A\neq \pm I$. The following holds:
\begin{itemize}
\item if $|\tr A| < 2$ then $M$ is a Seifert manifold with $e=0$ and $\chi = 0$,
\item if $|\tr A|=2$ then $M$ is a Seifert manifold with $e\neq 0$ and $\chi = 0$,
\item if $|\tr A|>2$ then $M$ is not a Seifert manifold.
\end{itemize}
\end{prop}
\begin{proof}
Consider $T \times [-1,1]$ foliated by lines $\{x\}\times [-1,1]$. The foliation extends to $M_A$. If $A$ has finite order, then $M_A$ is finitely covered by $M_I = T\times S^1$ and hence all fibers are compact. Therefore $M_A$ is Seifert fibered and covered by $T\times S^1$, and we get $e=\chi=0$. 

If $|\tr A|=2$ then $A$ is conjugate to $\matr {\pm 1}e0{\pm 1}$ and we use Exercise \ref{Me:ex}. Proposition \ref{Seifert:bundle:prop} easily shows that all the Seifert manifolds that are torus bundles are realised with $|\tr A| \leqslant 2$, hence if $|\tr A|>2$ the manifold $M$ is not Seifert by Proposition \ref{torus:bundle:classification:prop}.
\end{proof}

When $|\tr A| > 2$ we say that the monodromy $A$ is \emph{Anosov}.


\subsection{Bundles with $\chi(\Sigma) <0$}
Proposition \ref{torus:bundle:classification:prop} does not extend to surface bundles with $\chi(\Sigma)<0$; indeed it may happen that non-conjugate monodromies in $\MCG(\Sigma)$ give rise to diffeomorphic manifolds and understanding when this happens is a hard problem.

Proposition \ref{torus:bundle:prop} extends nevertheless and reflects the trichotomy of mapping classes. Let $\Sigma$ be a closed orientable surface with $\chi(\Sigma)<0$.
Recall from Section \ref{surface:diffeomorphisms:section} that every element $\psi\in\MCG(\Sigma)$ is either finite order, reducible, or pseudo-Anosov.

\begin{prop} \label{trichotomy:prop}
Let $M_\psi$ be a surface bundle with fibre $\Sigma$ and monodromy $\psi\in\MCG(\Sigma)$. The following holds:
\begin{itemize}
\item if $\psi$ has finite order, then $M_\psi$ is Seifert with $\chi <0$ and $e=0$,
\item if $\psi$ is reducible, then $M_\psi$ contains an essential torus,
\item if $\psi$ is pseudo-Anosov, then $M_\psi$ is simple and not Seifert.
\end{itemize}
\end{prop}
\begin{proof}
Same proof as Proposition \ref{torus:bundle:prop}. If $\psi$ has finite order, it is an isometry for some hyperbolic metric on $\Sigma$, and the line fibration of $\Sigma \times [-1,1]$ glues to a Seifert fibration for $M_\psi$. 

If $\psi$ is reducible there are disjoint essential simple closed curves $\gamma_1,\ldots, \gamma_k$ with $\psi(\gamma_i) = \gamma_{i+1}$ cyclically; by gluing the annuli $\gamma_i \times [-1,1]$ we get a torus $T\subset M_\psi$. It is essential because by cutting along it we still get a fibration over $S^1$ with fibers having $\chi \leqslant 0$.

If $\psi$ is pseudo-Anosov there are no essential tori $T\subset M_\psi$, for by minimising $T\cap \Sigma$ then $M_\psi \setminus T$ would consist of essential annuli of type $\gamma \times [-1,1]$ and hence $\psi$ would be reducible.
The manifold $M_\psi$ is not Seifert because the fibre $\Sigma$ would become a horizontal surface: then $M$ would be covered by $\Sigma \times S^1$ and hence $\psi$ would be of finite order.
\end{proof}
