---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-003-22-principal-groupoid-bundles
section_title: "Principal Groupoid Bundles"
section_number: 2.2
pages: 6-9
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.975
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non-abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal 2-bundles."
---
We give the definition of a principal  bundle in exactly the same way as we are going to define principal \emph{2-}bundles in Section \ref{sec:2bundle}.

\begin{definition}
\label{def:pgb}
Let $M$ be a smooth manifold, and let $\Gamma$ be a Lie groupoid.
\begin{enumerate}
\item 
A \emph{principal $\Gamma$-bundle over $M$} is a smooth manifold $P$ with a surjective submersion $\pi: P \to M$ and a right $\Gamma$-action $(\alpha,\rho)$ that respects the projection $\pi$, such that
\begin{equation*}
\tau: P \lli{\alpha} \times_{t} \Gamma_1 \to P \times_M P : (p,g) \mapsto (p,\rho(p,g))
\end{equation*}
is a diffeomorphism.

\item
Let $P_1$ and $P_2$ be  principal $\Gamma$-bundles over $M$. A \emph{morphism} $\varphi: P_1 \to P_2$
is a $\Gamma$-equivariant smooth map that respects the projections to $M$.
\end{enumerate}
\end{definition}

Principal $\Gamma$-bundles over $M$ form a category $\bun {\Gamma} M$.
In fact, this category is a groupoid, i.e. all morphisms between principal $\Gamma$-bundles are invertible. 
There is an evident notion of a pullback $f^{*}P$ of a principal $\Gamma$-bundle $P$ over $M$ along a smooth map $f: X \to M$, and similarly, morphisms between principal $\Gamma$-bundles pull back. These define a functor
\begin{equation*}
f^{*}: \bun \Gamma M \to \bun \Gamma X\text{.}
\end{equation*} 
These functors make principal $\Gamma$-bundles a prestack over smooth manifolds. One can  easily show that this prestack is a stack (for the Grothendieck topology of surjective submersions). 


\begin{example}[Ordinary principal bundles]
\label{ex:grpdbun}
For $G$ a Lie group, we have an equality of categories
\begin{equation*}
\bun {\mathcal{B}G} M = \bun G M\text{,}
\end{equation*}
i.e. Definition \ref{def:pgb} reduces consistently to the definition of an ordinary principal $G$-bundle. 
\end{example}

\begin{example}
[Trivial principal groupoid bundles]  
\label{trivialbundle}
For $M$ a smooth manifold and $f: M \to \Gamma_0$ a smooth map, 
$P := M \lli f \times_t \Gamma_1$
and
$\pi(m,g) := m$ define a surjective submersion, and
$\alpha(m,g) := s(g)$ and $\rho((m,g),h) \df (m, g \circ h)$
define a right action of $\Gamma$ on $P$ that preserves the fibers. 
The map $\tau$
we have to look at has the inverse 
\begin{equation*}
\tau^{-1}: P \times_M P \to P \lli{\pi} \times_{t} \Gamma_1: ((m,g_1),(m,g_2)) \mapsto ((m,g_1),g_1^{-1} \circ g_2)\text{,}
\end{equation*}
which is smooth. Thus we have defined a principal $\Gamma$-bundle, which we denote by $\trivlin_f$ and which we  call the \emph{trivial bundle for the map $f$}. Any bundle that is isomorphic to a trivial bundle is called \emph{trivializable}. 
\end{example}

\begin{example}[Discrete structure groupoids]
\label{ex:idmorphbundle}
For $X$ a smooth manifold, we have an equivalence of categories
\begin{equation*}
\bun {\idmorph X}M \cong \idmorph{C^{\infty}(M,X)}\text{.}
\end{equation*}
Indeed, for a given principal $\idmorph{X}$-bundle $P$ one observes that the anchor $\alpha:P \to X$ descends along the bundle projection to a smooth map $f:M \to X$, and that isomorphic bundles determine the same map. Conversely, one associates to a smooth map $f: M \to X$ the trivial principal $\idmorph{X}$-bundle $\trivlin_f$ over $M$. 
\end{example}

\begin{example}[Exact sequences]
Let
\begin{equation}
\label{exact1}
\alxydim{}{1 \ar[r] & H \ar[r]^{t} & G \ar[r]^{p} & K \ar[r] & 1}
\end{equation} 
be an exact sequence of Lie groups, and let  $\Gamma := \act GH$ be the action groupoid associated to the Lie group homomorphism $t:H \to G$ as explained in Example \ref{exliecat} \erf{extHG}. In this situation, $p:G \to K$ is a surjective submersion, and
\begin{equation*}
\alpha:G \to \Gamma_0:g \mapsto g
\quand
\rho: G \lli{\alpha}\times_{t}\Gamma_1 \to G: (g,(h,g')) \mapsto g'
\end{equation*}
define a smooth right action of $\Gamma$ on $G$ that preserves $p$. The inverse of the  map $\tau$ is
\begin{equation*}
\tau^{-1}: G \times_K G \to G \lli{\alpha}\times_{t}\Gamma_1: (g_1,g_2) \mapsto (g_1, (t^{-1}(g_1g_2^{-1}),g_2))\text{,}
\end{equation*}
which is smooth because $t$ is an embedding. Thus, $G$ is a principal $\Gamma$-bundle over $K$. 
\end{example}



Next we  provide some elementary statements about trivial principal $\Gamma$-bundles.

\begin{lemma}
\label{lem:loctriv}
A principal $\Gamma$-bundle over $M$ is trivializable if and only if it has a smooth section.
\end{lemma}

\begin{proof}
A trivial bundle $\trivlin_f$ has the section
\begin{equation*}
s_f: M \to \trivlin_{f}: x \mapsto (x,\id_{f(x)})\text{;}
\end{equation*}
and so any trivializable bundle has a section. Conversely, suppose a principal $\Gamma$-bundle $P$ has a smooth section $s: M \to P$. Then, with $f := \alpha \circ s$,
\begin{equation*}
\varphi: \trivlin_f \to P: (m,g) \mapsto \rho(s(m),g)
\end{equation*}
is an isomorphism.
\end{proof}

The following consequence shows that principal $\Gamma$-bundles of Definition \ref{def:pgb}  are locally trivializable in the usual sense.

\begin{corollary}
Let $P$ be a principal $\Gamma$-bundle over $M$. Then, every point $x\in M$ has an open neighborhood $U$ over which $P$ has a  trivialization: a smooth map $f: U \to \Gamma_0$ and a morphism
$\varphi: \trivlin_f \to P|_U$.
\end{corollary}

\begin{proof}
One can choose $U$ such that the surjective submersion $\pi:U \to P$ has a smooth section. Then, Lemma \ref{lem:loctriv} applies to the restriction $P|_U$.
\end{proof}

We  determine the Hom-set $\hom {\trivlin_{f_1}} {\trivlin_{f_2}}$ between trivial principal $\Gamma$-bundles defined by smooth maps $f_1,f_2\maps M \to \Gamma_0$. To a bundle morphism $\varphi: \trivlin_{f_1} \to \trivlin_{f_2}$ one associates the smooth function $g: M \to \Gamma_1$ which is uniquely defined by the condition
\begin{equation*}
(\varphi \circ s_{f_1})(x) = s_{f_2}(x) \circ g(x)\text{.}
\end{equation*}
for all $x\in M$. It is straightforward to see that

\begin{lemma}
\label{homsets}
The above construction defines a bijection
\begin{equation*}
\hom {\trivlin_{f_1}} {\trivlin_{f_2}} \to \left \lbrace g \in C^{\infty}(M,\Gamma_1) \;|\; s \circ  g=f_1\;\text{ and }\;t \circ g=f_2 \right \rbrace\text{,}
\end{equation*}
under which identity morphisms correspond to constant maps and the composition of  bundle morphisms corresponds to the point-wise composition of functions. \end{lemma}



Finally, we consider the case of principal bundles for action groupoids. 

\begin{lemma}
\label{actionbundles}
Suppose $\act X H$ is a smooth action groupoid. The category $\bun {\act XH}M$ is equivalent to a category with 
\begin{itemize}
\item
Objects: principal $H$-bundles $P_H$ over $M$ together with a smooth, $H$-anti-equivariant map $f\colon P_H \to X$, i.e. $f(p\cdot h) = h^{-1}f(p)$. 

\item
Morphisms: bundle morphisms $\varphi_H:P_H \to P'_H$ that respect the maps $f$ and $f'$.
\end{itemize}
\end{lemma}
\begin{proof}
For a principal $\act XH$-bundle $(P, \alpha, \rho)$ we set $P_H := P$ with the given projection to $M$. The action of $H$ on $P_H$ is defined by
\begin{equation*}
p\star h := \rho(p,(h,h^{-1}\cdot\alpha(p)))\text{.}
\end{equation*}
This action is smooth, and it follows from the axioms of the principal bundle $P$ that it is principal.
\begin{comment}
Freeness is clear. It is transitive: for $p_1,p_2 \in P$ there exists a morphism $(h,x)$ with $p_2 = \rho(p_1,(h,x))$, where $\alpha(p_1) = hx$ and $\alpha(p_2) = x$. Then,
\begin{equation*}
p_1 \cdot h = \rho(p_1,(h,h^{-1}\cdot \alpha(p_1)))= \rho(p_1,(h,x)) = p_2\text{.}
\end{equation*}
\end{comment}
The map $f: P_H \to X$ is  the anchor $\alpha$. 
\begin{comment}
The anti-equivariance is easy to see:
\begin{equation*}
\alpha(p \star h) = \alpha(\rho(p,(h,h^{-1}\alpha(p)))) = s((h,h^{-1}\alpha(p)))=h^{-1}\alpha(p)\text{.}
\end{equation*}
\end{comment}
The remaining steps are straightforward and  left as an exercise.
\end{proof}
