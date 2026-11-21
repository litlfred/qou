---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-018-42-intersection-homology
section_title: "Intersection homology"
section_number: 4.2
pages: 43-51
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.954
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
Recall from \cite{aft1} that the underlying space of a $n$-dimensional stratified space $X\in \snglr_n$ has a canonical filtration by the union of its strata $X_0 \subset X_1 \subset \ldots \subset X_n= X$ where each $X_i\smallsetminus X_{i-1}$ is a smooth $i$-dimensional manifold. As such, the definition of Goresky \& MacPherson's intersection homology~\cite{goreskymacpherson} applies verbatim. Namely, we restrict to stratified spaces $X$ have no codimension-1 strata, $X_{n-1}=X_{n-2}$ and for which the $n$-dimensional open stratum $X_n\smallsetminus X_{n-1}$ is nonempty.

For the definition below we use $j^{\rm th}$-stratum functor $(-)_j\colon \snglr_n \to \snglr_{\leq j}$ which assigns to stratified space $X$ the maximal substratified space $X_j$ whose strata are of dimension less than $j+1$.
\begin{definition} 
Denote the left ideal $\bsc_n^{\sf ps} \to \bsc_n$ spanned by those basics $U$ for which $U_{n-1} = U_{n-2}$.  Define the category of \emph{pseudomanifolds} as $\snglr_n^{\sf ps} = \mfld(\bsc_n^{\sf ps})$ -- its objects are those $n$-dimensional stratified spaces for which $X_{n-1} = X_{n-2}$.  
\end{definition}

Continuing, choose a perversity function $p$, i.e., a mapping $p:\{2, 3, \ldots, n\} \ra \ZZ_{\geq 0}$ such that $p(2)=0$ and for each $i>2$ either $p(i)=p(i-1)$ or $p(i) = p(i-1)+1$. Recall the following definition.

\begin{definition}[\cite{goreskymacpherson}] A $j$-simplex $g: \Delta^j \ra X$ is $p$-allowable if, for every $i$ the following bound on the dimensions of intersections holds:
\[
{\sf dim} \bigl(g(\Delta^j)\cap X_i\bigr) \leq i + j -n +p(n-i)~.
\]
A singular chain $\phi \in \sC_j(X)$ is $p$-allowable if both $|\phi|$ is $p$-allowable and $|\partial\phi|$ is $p$-allowable.
\end{definition}

This gives the following definition of Goresky--MacPherson, of intersection homology with perversity $p$.

\begin{definition}[\cite{goreskymacpherson}] The intersection homology $\sI_p\sC_\ast(X)$ of $X\in \snglr_n^{\sf ps}$ is the complex of all $p$-allowable singular chains.
\end{definition}

The condition of a simplex being $p$-allowable is clearly preserved by embeddings of stratified spaces: if $f:X \ra Y$ is a morphism in $\snglr_n^{\sf ps}$ and $g:\Delta^j \ra X$ is $p$-allowable, then $f\circ g: \Delta^j\ra Y$ is $p$-allowable. Further, being $p$-allowable varies continuously in families of embeddings. That is, there is a natural commutative diagram:
\[\xymatrix{
\snglr_n(X,Y) \ar[r]\ar[d]&\Map(X,Y)\ar[d]\\
\Map\bigl(\sI_p\sC_\ast(X), \sI_p\sC_\ast(Y)\bigr) \ar[r]&\Map\bigl(\sC_*(X), \sC_*(Y)\bigr)\\}\]
Consequently, intersection homology is defined on the $\oo$-category $\snglr_n^{\sf ps}$ of $n$-dimensional pseudomanifolds. 
Obviously $\sI_p\sC_\ast (X\sqcup Y) \cong \sI_p\sC_\ast (X) \oplus \sI_p\sC_\ast (Y)$.  
We have the following:
\begin{prop} The intersection homology functor
\[\sI_p\sC_\ast: \snglr_n^{\sf ps} \longrightarrow {\sf Ch}\] defines a homology theory in $\bcH( \snglr_n^{\sf ps} , {\sf Ch}^\oplus)$.
\end{prop}
The proof is exactly that intersection homology satisfies excision, or has a version of the Mayer-Vietoris sequence for certain gluings.
\begin{proof} Let $X\cong  X_- \cup_{\RR\times V}X_+$ be a collar-gluing. Then 
\[\xymatrix{
\sI_p\sC_\ast(\RR\times V)\ar[d]\ar[r]&\sI_p\sC_\ast(X_+)\ar[d]\\
\sI_p\sC_\ast(X_-)\ar[r]&\sI_p\sC_\ast(X)\\}\]
is a pushout diagram in the $\oo$-category of chain complexes. I.e., the natural map 
\\
$\sI_p\sC_\ast(X_-)\oplus_{\sI_p\sC_\ast(\RR\times V)}\sI_p\sC_\ast(X_+) \ra \sI_p\sC_\ast(X)$ is a quasi-isomorphism.
\end{proof}


\subsection{Link homology theories and $\disk^{\fr}_{d\subset n}$-algebras}

We now consider one of the simplest, but more interesting, classes of $n$-dimensional stratified spaces -- that of $n$-manifolds together with a distinguished properly embedded $d$-dimensional submanifold. 
While we specialize to this class of stratified spaces, the techniques for their analysis are typical of techniques that can be used for far more general classes.  

  
Recall from \cite{aft1} the $\oo$-category $\mfld_{d\subset n}^{\fr}$ whose objects are framed $n$-manifolds $M$ with a properly embedded $d$-dimensional submanifold $L\subset M$ together with a splitting of the framing along this submanifold, and the full $\infty$-subcategory $\disk^{\fr}_{d\subset n}\subset \mfld_{d\subset n}^{\fr}$ generated under disjoint union by the two objects $\RR^n := U^n_{\emptyset^{-1}}$ and $(\RR^d\subset \RR^n):= U^n_{S^{n-d-1}}$ with their standard framings.


\subsubsection{Explicating $\disk^{\fr}_{d\subset n}$-algebras}
Fix a symmetric monoidal $\oo$-category $\cV$ which is $\ot$-sifted cocomplete.  
Recall from the discussion of the push-forward and Corollary \ref{fubini} the map of $\oo$-categories $\int_Y\colon \Alg_{\disk_n^{\fr}}(\cV) \to \Alg_{\disk_{d+1}^{\fr}}(\cV)$
defined for any framed $(n-d-1)$-manifold $Y$.  

\begin{prop}\label{nk} There is a pullback diagram:

\[\xymatrix{
\Alg_{\disk^{\fr}_{d\subset n}}(\cV)\ar[d]&\ar[l]{\Alg_{\disk^{\fr}_{d+1}}}\Bigl(\displaystyle\int_{S^{n-d-1}}A~,~ \hh^\ast_{\sD^{\fr}_d}(B)\Bigr)\ar[d]\\
\Alg_{\disk^{\fr}_{n}}(\cV)\times\Alg_{\disk^{\fr}_{d}}(\cV)&\ar[l]\{(A,B)\}\\}\]
\end{prop}
That is, the space of compatible $\disk^{\fr}_{d\subset n}$-algebra structures on the pair $(A,B)$ is equivalent to the space of $\disk^{\fr}_{d+1}$-algebra maps from $\int_{S^{n-d-1}}A$ to the Hochschild cohomology $\hh^\ast_{\sD^{\fr}_d}(B)$; the datum of a $\disk^{\fr}_{d\subset n}$-algebra is equivalent to that of a triple $(A,B, \alpha)$, where $A$ is a $\disk^{\fr}_n$-algebra, $B$ is a $\disk^{\fr}_d$-algebra, and $\alpha$ is a map of $\disk^{\fr}_{d+1}$-algebras
	\[
	\alpha: \int_{S^{n-d-1}} A \longrightarrow \hh^*_{\sD^{\fr}_d} (B)
	\]
-- this is an $S^{n-d-1}$ parametrized family of central $\disk^{\fr}_d$-algebra actions of $A$ on $B$. In essence, Proposition~\ref{nk} is a parametrized version of the higher Deligne conjecture, and in the proof we will rely on the original version of the higher Deligne conjecture (proved in \S5.3 of \cite{HA}).

\begin{proof}

The $\oo$-category $\disk_{d\subset n}^{\fr}$ has a natural filtration by the number of components which are isomorphic to the stratified space $(\RR^d\subset \RR^n)$:
\[
\disk_n^{\fr}=(\disk_{d\subset n}^{\fr})_{\leq 0} \ra (\disk_{d\subset n}^{\fr})_{\leq 1} \ra \ldots \ra \colim_i ~(\disk_{d\subset n}^{\fr})_{\leq i} \simeq \disk^{\fr}_{d\subset n}
\] 
Consider the second step in this filtration, the full subcategory $(\disk_{d\subset n}^{\fr})_{\leq 1}$ of $\disk_{d\subset n}^{\fr}$ whose objects contain at most one connected component equivalent to $(\RR^d\subset \RR^n)$. 

Disjoint union endows $(\disk_{d\subset n}^{\fr})_{\leq 1}$ with a \emph{partially defined} symmetric monoidal structure. 
This partially defined symmetric monoidal structure can be articulated as follows.  Consider the pullback $(\disk^{\fr,\sqcup}_{d\subset n})_{\leq 1} := (\disk^{\fr}_{d\subset n})_{\leq 1} \times_{\disk^{\fr}_{d\subset n}} \disk^{\fr,\sqcup}_{d\subset n}$ where here we are using the map from the right factor $\sqcup\colon \disk^{\fr,\sqcup}_{d\subset n} \to \disk^{\fr}_{d\subset n}$.  
The coCartesian fibration $\disk^{\fr, \sqcup}_{d\subset n} \to \mathsf{Fin}_\ast$ restricts to a map $(\disk^{\fr,\sqcup}_{d\subset n})_{\leq 1} \to \mathsf{Fin}_\ast$ which is an inner fibration and for each edge $f$ in $\mathsf{Fin}_\ast$ with a lift $\w{J}_+$ of its source in $(\disk^{\fr,\sqcup}_{d\subset n})_{\leq 1}$ there is either a coCartesian edge over $f$ with source $\w{J}_+$ or the simplicial set of morphisms over $f$ with source $\w{J}_+$ is empty.  
In this way, by a symmetric monoidal functor from $(\disk^{\fr,\sqcup}_{d\subset n})_{\leq 1}$ over $\mathsf{Fin}_\ast$ it is meant a map over $\mathsf{Fin}_\ast$ which sends coCartesian edges to coCartesian edges.  

It is immediate that such a symmetric monoidal functor $F$ is equivalent to the data of a $\disk^{\fr}_n$-algebra $F(\RR^n)$ and a $\disk^{\fr}_{n-d}$-$F(\RR^n)$-module given by $F(\RR^d\subset \RR^n)$. Extending such a symmetric monoidal functor $F$ to $\disk_{d\subset n}^{\fr}$ is thus equivalent to giving a $\disk^{\fr}_d$-algebra structure on $F(\RR^d\subset \RR^n)$ compatible with the $\disk^{\fr}_{n-d}$-$F(\RR^n)$-module. That is, the following is a triple of pullback squares of $\oo$-categories
\[\xymatrix{
\Alg_{\disk_{d\subset n}^{\fr}}(\cV)\ar[d]&\ar[l]\Alg_{\disk^{\fr}_{d}}\bigl(\m_A^{\disk^{\fr}_{n-d}}(\cV)\bigr)\ar[d]\\
\Fun^\ot\bigl((\disk_{d\subset n}^{\fr})_{\leq 1},\cV\bigr)\ar[d]&\ar[l]\m_A^{\disk^{\fr}_{n-d}}(\cV)\ar[d]\\
\Alg_{\disk^{\fr}_{n}}(\cV)&\ar[l]\{A\}~.
\\}\]

Using the equivalence $\m_A^{\disk^{\fr}_{n-d}}(\cV)\simeq \m_{\int_{S^{n-d-1}}A}(\cV)$ of~\cite{cotangent}, we can then apply the higher Deligne conjecture to describe an object of the $\oo$-category \[\Alg_{\disk^{\fr}_{d}}\Bigl(\m_A^{\disk^{\fr}_{n-d}}(\cV)\Bigr) \simeq \Alg_{\disk^{\fr}_{d}}\Bigl(\m_{\int_{S^{n-d-1}}A}(\cV)\Bigr)~.\] That is, to upgrade a $\disk^{\fr}_d$-algebra $B$ to the structure of a $\disk^{\fr}_d$-algebra in $\int_{S^{n-d-1}}A$-modules is equivalent to giving a $\disk^{\fr}_{d+1}$-algebra map $\alpha: \int_{S^{n-d-1}}A\ra \hh^*_{\sD^{\fr}_d}(B)$ to the $\sD^{\fr}_d$-Hochschild cohomology of $B$.
\end{proof}


\subsubsection{Hochschild cohomology in spaces}

We now specialize our discussion of $\disk^{\fr}_{d\subset n}$-algebras to the case where $\cV=\cS^\times$ is the $\oo$-category of spaces with Cartesian product, but any $\infty$-topos would do just as well. In this case, the $\sD^{\fr}_n$-Hochschild cohomology of an $n$-fold loop space has a very clear alternate description which is given below.

\begin{prop}\label{HH-Aut}
Let $Z=(Z,\ast)$ be a based space which is $n$-connective.  
In a standard way, the $n$-fold based loop space $\Omega^n Z$ is a $\disk^{\fr}_n$-algebra.  
There is a canonical equivalence of $\disk^{\fr}_{n+1}$-algebras in spaces \[\hh^*_{\sD^{\fr}_n}(\Omega^n Z) \simeq \Omega^n \Aut(Z)\] between the $\sD^{\fr}_n$-Hochschild cohomology space of $\Omega^nZ$ and the $n$-fold loops, based at the identity map, of the space of homotopy automorphisms of $Z$.
\end{prop} 

\begin{proof} 
In what follows, all mapping spaces will be regarded as based spaces, based at either the identity map or at the constant map at the base point of the target argument -- the context will make it clear which of these choices is the appropriate one.  

There are equivalences 
\[
\m_{\Omega^n Z}^{\disk^{\fr}_n}(\cS) \simeq \m_{\int_{S^{n-1}}\Omega^n Z}(\cS) \simeq \m_{\Omega Z^{S^{n-1}}}(\cS)\simeq \cS_{/Z^{S^{n-1}}}
\] 
sending the object $\Omega^n Z$ with its natural $\disk^{\fr}_n$-$\Omega^nZ$-module self-action to the space $Z$ with the natural inclusion of constant maps $Z\ra Z^{S^{n-1}}$. 
Thus, to describe the mapping space \[\hh^*_{\sD^{\fr}_n}(\Omega^nZ) \simeq {\m_{\Omega^nZ}^{\disk^{\fr}_n}}(\Omega^nZ,\Omega^nZ)\] it suffices to calculate the equivalent mapping space $\Map_{/Z^{S^{n-1}}}(Z,Z)$. By definition, there is the (homotopy) pullback square of spaces
\[\xymatrix{
\Map_{/Z^{S^{n-1}}}(Z,Z)\ar[r]\ar[d]& \ast\ar[d]\\
\Map(Z,Z)\ar[r]&\Map(Z,Z^{S^{n-1}})~.
\\}\]

Choose a base point $p\in S^{n-1}$.  The restriction of the evaluation map $ev_p^\ast\colon\Map(Z,Z) \ra \Map(Z,Z^{S^{n-1}})$ is a map of based spaces.   
Thus, the pullback diagram above factorizes as the (homotopy) pullback diagrams
\[\xymatrix{
\Map_{/Z^{S^{n-1}}}(Z,Z)\ar[r]\ar[d]& \ast\ar[d]\\
\Map(Z,Z)^{S^n}\ar[r]\ar[d]&\Map(Z,Z)\ar[d]\\
\Map(Z,Z)\ar[r]&\Map(Z,Z^{S^{n-1})}\\
}\]
where the space of maps from the suspension $S^n= \Sigma S^{n-1}$ to $\Map(Z,Z)$ is realized as the homotopy pullback of the two diagonal maps $\Map(Z,Z) \ra \Map(Z,Z)^{S^{n-1}}$; this is a consequence of the fact that the functor $\Map(-,Z)$ sends homotopy colimits to homotopy limits, applied to the homotopy colimit $\colim(\ast \la S^{n-1}\ra \ast)\simeq S^n$.

Applying the adjunction between products and mapping spaces, we obtain that the Hochschild cohomology space $\Map_{/Z^{S^{n-1}}}(Z,Z)$ is the homotopy fiber of the map $\Map\bigl(S^n, \Map(Z, Z)\bigr) \ra \Map(Z,Z)$ over the identity map of $Z$, which recovers exactly the definition of the based mapping space $\Map_*\bigl(S^n,\Map(Z,Z)\bigr) \simeq \Map_*\bigl(S^n,\Aut(Z)\bigr)$, where the last equivalence follows by virtue of $S^n$ being connected.

\end{proof}

\begin{cor}
Let $Z$ and $W$ be pointed spaces.  Suppose $Z$ is $n$-connective and $W$ is $d$-connective. A $\disk^{\fr}_{d\subset n}$-algebra structure on the pair $(\Omega^n Z,\Omega^d W)$ is equivalent to the data of a pointed map of spaces
	\[
	Z^{S^{n-d-1}} \longrightarrow {\sf BAut}(W)~.
	\]

\end{cor}

\begin{proof} 
Proposition~\ref{nk} informs us that giving the structure of a $\disk^{\fr}_{d\subset n}$-algebra on $(\Omega^nZ,\Omega^dW)$ is equivalent to defining a $\disk^{\fr}_{d+1}$-algebra map \[\int_{S^{n-d-1}}\Omega^nZ \longrightarrow \hh^*_{\sD^{\fr}_d}(\Omega^dW)~.\] 
By way of nonabelian Poincar\'e duality (Theorem~\ref{non-abel}), the factorization homology $\int_{S^{n-d-1}}\Omega^nZ$ is equivalent as $\disk^{\fr}_{d+1}$-algebras to the mapping space $\Omega^{d+1}Z^{S^{n-d-1}}$.  Proposition~\ref{HH-Aut} gives that the Hochschild cohomology $\hh^*_{\sD^{\fr}_d}(\Omega^dW)$ is equivalent to the space of maps to $\Omega^d \Aut(W)$.

Finally, a $(d+1)$-fold loop map $\Omega^{d+1}Z^{S^{n-d-1}} \ra \Omega^d \Aut(W)$ is equivalent to a pointed map between their $(d+1)$-fold deloopings. The $(d+1)$-fold delooping of $\Omega^{d+1}Z^{S^{n-d-1}}$ is $Z^{S^{n-d-1}}$, since $Z$ is $n$-connective; the $(d+1)$-fold delooping of $\Omega^d \Aut(W)$ is $\tau_{\geq d+1}{\sf BAut}(W)$, the $d$-connective cover of ${\sf BAut}(W)$. However, since $Z^{S^{n-d-1}}$ is already $(d+1)$-connective, the space of maps from it into $\tau_{\geq d+1}{\sf BAut}(W)$ is homotopy equivalent to the space of maps into ${\sf BAut}(W)$.
\end{proof}


\subsubsection{Free $\disk^{\fr}_{d\subset n}$-algebras}\label{free-examples}

Fix a symmetric monoidal $\oo$-category $\cV$ whose underlying $\oo$-category is presentable and whose monoidal structure distributes over colimits in each variable.  
We analyze the factorization homology theory resulting from one of the simplest classes of $\disk^{\fr}_{d\subset n}$-algebras, that of freely generated $\disk^{\fr}_{d\subset n}$-algebras. 
That is, there is a forgetful functor
	\begin{equation}\label{forget-two}
	\Alg_{\disk^{\fr}_{d\subset n}}(\cV) \to \cV \times \cV~,
	\end{equation}
given by evaluating on the objects $\RR^n$ and $(\RR^d\subset \RR^n)$, and this functor admits a left adjoint $\free_{d\subset n}$. 
To accommodate more examples, we modify~(\ref{forget-two}).  
Consider the maximal sub-Kan complex $\cE\subset \sD_{d\subset n}$.  
 $\cE$ is a coproduct $\End_{\sD_{d\subset n}}(\RR^n)\coprod \End_{\sD_{d\subset n}}(\RR^d\subset \RR^n) \simeq \sO(n) \coprod \sO(d\subset n)$, here $\sO(d\subset n):= \sO(n-d)\times \sO(d)$.  
There results a map of $\oo$-categories $\cE \to \sD_{d\subset n} \to \disk_{d\subset n} \to \disk_{d\subset n}^\sqcup$, restriction along which gives the map of $\oo$-categories
\[
\Alg_{\disk_{d\subset n}}(\cV) \to \Map(\cE,\cV) \simeq \cV^{\sO(n)}\times \cV^{\sO(d\subset n)}
\]
to the $\oo$-category of pairs $(P,Q)$ consisting of an $\sO(n)$-object in $\cV$ and an $\sO(d\subset n)$-object in $\cV$.  
We will denote the left adjoint to this map as $\free_\cE$.  
Denote the inclusion as $\delta \colon \cV\times \cV \to \Map(\cE,\cV)$ as the pairs $(P,Q)$ whose respective actions are trivial.  

For $X$ a $\sD_{d\subset n}$-manifold (not necessarily framed) define $\int_X \free^{(P,Q)}_{d\subset n}:= \int_X \free^{\delta(P,Q)}_\cE$.  
When $X$ is framed (i.e., is a $\sD^{\fr}_{d\subset n}$-manifold) the lefthand side of this expression has already been furnished with meaning as the factorization homology of $X$ with coefficients in the free $\disk^{\fr}_{d\subset n}$-algebra generated by $(P,Q)$.  
The following lemma ensures that the two meanings agree.
Recall the forgetful map $\disk^{\fr, \sqcup}_{d\subset n} \to \disk_{d\subset n}^\sqcup$.  

\begin{lemma}\label{frame-or-not}
Let $(P,Q)$ be a pair of objects of $\cV$.  
Then the universal arrow
\[
\free_{d\subset n}^{(P,Q)} \xra{\simeq} \bigl(\free_\cE^{\delta(P,Q)}\bigr)_{|\disk^{\fr, \sqcup}_{d\subset n}}
\]
is an equivalence.  

\end{lemma}

\begin{proof}

Denote the pullback $\oo$-category $\cE^{\fr} = \cE\times_{\sD_{d\subset n}} \sD^{\fr}_{d\subset n}$.  
Like $\cE$, $\cE^{\fr}\subset \sD^{\fr}_{d\subset n}$ is the maximal sub-Kan complex (=$\infty$-groupoid).  
The projection $\cE^{\fr} \to \cE$ is a Kan fibration with fibers $\sO(n)$ or $\sO(d\subset n)$, depending on the component of the base.  
As so, the inclusion of the two objects with their standard framings $\{\RR^n\}\coprod \{\RR^d\subset \RR^n\} \xra{\simeq} \cE^{\fr}$ is an equivalence of Kan complexes.  
Therefore $\Map(\cE^{\fr},\cV) \xra{\simeq} \cV\times \cV$.  

Let us explain the following diagram of $\oo$-categories
\[
\xymatrix{
\Alg_{\disk_{d\subset n}}(\cV)   \ar[rr]^-{\rho}  \ar@(l,l)[dd]_-{\rho}
&&
\Map(\cE,\cV)   \ar@(r,r)[dd]^-{\rho}    \ar@(u,u)[ll]^-{\free_\cE} 
\\
&&
\\
\Alg_{\disk^{\fr}_{d\subset n}}(\cV)  \ar[rr]_-{\rho}  \ar[uu]_-{\mathsf{RKan}}  
&&
\Map(\cE^{\fr},\cV)~.   \ar[uu]^-{\mathsf{RKan}}  \ar@(d,d)[ll]^-{\free_{d\subset n}}
}
\]
Each leg of the square is an adjunction.
All maps labeled by $\rho$ are the evident restrictions.  
The maps denoted as $\mathsf{RKan}$ are computed as point-wise right Kan extension.  
(That is, $\mathsf{RKan}(A)\colon U\mapsto \lim_{U\to U'} A(U')$ where this limit is taking place in $\cV$ and is indexed by the appropriate over category.  
We emphasize that, unlike the case for left extensions, this point-wise right Kan extension agrees with operadic right Kan extension.)
As so, the straight square of right adjoints commutes.
It follows that the outer square of left adjoints also commutes.  

The right downward map is equivalent to that which assigns to a pair of objects $(P,Q)$ with respective actions of $\sO(n)$ and $\sO(d\subset n)$, the pair $(P,Q)$.  
The map $\delta\colon \cV\times \cV \to \cV^{\sO(n)}\times \cV^{\sO(d\subset n)}$ is a section to this right downward map $\rho$.    
We have established the string of canonical equivalences
\[
\free_{d\subset n} \simeq \free_{d\subset n}\circ\bigl(\rho \circ \delta\bigr) = \bigl(\free_{d\subset n}\circ \rho\bigr)\circ \delta \simeq \bigl(\rho\circ \free_\cE\bigr)\circ \delta~.
\]
This completes the proof.  

\end{proof}

In order to formulate our main result, we first give the following definition.

\begin{definition} For $M$ a topological space and $P$ an object of $\cV$, the \emph{configuration object of points in $M$ labeled by $P$} is 
\[
\conf^P(M) = \coprod_{j\geq 0} \conf_j(M)\underset{\Sigma_j}\ot P^{\ot j} \in \cV
\] 
where $\conf_j (M)\subset M^{\times j}$ is the configuration space of $j$ ordered and distinct points in $M$.
\end{definition}

For the remainder of the section, assume that the monoidal structure of $\cV$ distributes over small colimits.

\begin{prop}\label{prop:conf} Let $(P,Q)$ be a pair of objects of $\cV$.  
Let $(L\subset M)$ be a $\sD_{d\subset n}$-manifold, i.e., a smooth $n$-manifold and a properly embedded $d$-submanifold.  
There is a natural equivalence
	\[
	\int_{(L\subset M)} \free_{d\subset n}^{(P,Q)}
	\simeq
	\conf^{P}(M\smallsetminus L) \ot \conf^{Q}(L)\]
between the factorization homology of $(L\subset M)$ with coefficients in the $\disk_{d\subset n}$-algebra freely generated by $(P,Q)$ and the tensor product of the configurations objects of the link complement $M\smallsetminus L$ and the link $L$ labeled by $P$ and $Q$, respectively.
\end{prop}

We make some remarks before proceeding with the proof of this result.

\begin{remark} We see from this result with $(d\subset n)=(3,1)$ that factorization homology in particular distinguish knots whose knot complements have distinct homotopy types. For instance, the unknot, whose knot group is $\ZZ$, and the trefoil knot, whose knot group is presented by $\langle x,y | x^2 = y^3 \rangle$, give rise to different factorization homologies.
\end{remark}

\begin{remark} Specializing to the case where the link $L$ is empty, we obtain the equivalence $\int_M \free_n^P \simeq \conf^P(M)$. Consequently, factorization homology is not a homotopy invariant of $M$, in as much as the homotopy types of the configuration spaces $\conf_j(M)$ are sensitive to the homeomorphism (or, at least, the simple homotopy) type of $M$, see~\cite{simple}. This is in contrast to the case in which the $\disk^{\fr}_n$-algebra $A$ comes from an $n$-fold loop space on an $n$-connective space, in which case nonabelian Poincar\'e duality~(Theorem~\ref{non-abel}) implies that factorization homology with such coefficients is a proper homotopy invariant. However, note that the factorization homology $\int_M \free_n^P$ is independent of the framing on $M$; this is a consequence of the fact that the $\disk_n^{\fr}$-algebra structure on $\free_n^P$ can be enhanced to a $\disk_n$-algebra.
\end{remark}

Recall the maps of symmetric monoidal $\oo$-categories $\disk^{\fr, \sqcup}_n \to \disk^{\fr,\sqcup}_{d\subset n}$ and $\disk^{\fr,\sqcup}_d \to \disk^{\fr,\sqcup}_{d\subset n}$ indicated by the assignments $\RR^n\mapsto \RR^n$ and $\RR^d \mapsto (\RR^d\subset \RR^n)$, respectively.
The following lemma describes the free $\disk_{d\subset n}^{\fr}$-algebras in terms of free $\disk^{\fr}_n$-algebras and free $\disk^{\fr}_d$-algebras. 

\begin{lemma}\label{free-free}
Let $(P,Q)$ be a pair of objects of $\cV$. Then the universal arrows to the restrictions
	\[
	 \free_n^P\xra{\simeq} \bigl(\free_{d\subset n}^{(P,Q)}\bigr)_{|\disk^{\fr,\sqcup}_n} 
	\qquad \&
	\qquad
	 \free_d^Q \ot\int_{S^{n-d-1}\times \RR^{d+1}}\free_n^P~{}~\xra{\simeq} ~{}~\bigl(\free_{d\subset n}^{(P,Q)}\bigr)_{|\disk^{\fr,\sqcup}_d}
	\]
are equivalences.  
\end{lemma}

\begin{proof} 
Recall from the proof of Proposition~\ref{nk} that a $\disk^{\fr}_{d\subset n}$-algebra structure $A$ on $(A_n, A_d)$, where $A_n$ is a $\disk^{\fr}_n$-algebra and $A_d$ is a $\disk^{\fr}_d$-algebra, is equivalent to the structure of a $\disk_{n-d}^{\fr}$-$A_n$-module structure on $A_d$ in the $\oo$-category $\Alg_{\disk^{\fr}_d}(\cV)$. 
The forgetful functor factors as the forgetful functors
\[
\Alg_{\disk^{\fr}_{d\subset n}}(\cV)\longrightarrow\Alg_{\disk^{\fr}_n}(\cV)\times\Alg_{\disk^{\fr}_d}(\cV)\longrightarrow\cV\times\cV
\] 
and thus, passing to the left adjoints, we can write the free algebra $A$ on a pair $(P,Q)$ as the composite of the two left adjoints, which gives the free $\disk^{\fr}_n$-algebra on $P$ and the free $\disk^{\fr}_{n-d}$-module on the free $\disk^{\fr}_d$-algebra on $Q$; the latter is calculated by tensoring with the factorization homology $\int_{S^{n-d-1} \times \RR^{d+1}}\free_n^P$, which is a special case of the equivalence between ${\disk^{\fr}_j}$-$R$-modules and left modules for $\int_{S^{j-1}}R$, see Proposition 3.16 of~\cite{cotangent}, applied to $R =\free_n^P$ and $j=n-d$.

\end{proof}

\begin{proof}[Proof of Proposition ~\ref{prop:conf}]

Recall the construction of the $\infty$-operad $\cE^{\amalg}_{\sf inert}$ -- it is the free $\infty$-operad on $\cE$.  That is, the map 
\[
\mathsf{Fun}^\ot(\cE^{\amalg}_{\sf inert},\cV) \xra{\simeq} \mathsf{Fun}(\cE,\cV)\simeq \cV^{\sO(n)}\times \cV^{\sO(d\subset n)}~, 
\]
induced by restriction along the inclusion of the underlying $\oo$-category $\cE \to \cE^\amalg_{\sf inert}$, is an equivalence of Kan complexes -- here we are using exponential notation for simplicial sets of maps.
Explicitly, a vertex of $\cE^\amalg_{\sf inert}$ is a pair of finite sets $(J_n,J_d)$ while an edge is the data of a pair of based maps $(J_n)_+ \xra{a} (J_n')_+$ and $(J_d)_+ \xra{b} (J_d')_+$ which are \emph{inert}, which is to say, the fibers over non-base points $a^{-1}(j')$ and $b^{-1}(j'')$ are each singletons, together with a pair of elements $\alpha\in \sO(n)^{J_n'}$ and $\beta\in \sO(d\subset n)^{J_d'}$.  
We will denote a typical object of $\cE^\amalg_{\sf inert}$ as $E=(J_n,J_d)$.  

The the standard inclusion $\cE \to \mfld_{d\subset n}$ then induces the map of $\infty$-operads $\cE^\amalg_{\sf inert} \xra{i} \mfld^{\sqcup}_{d\subset n}$ whose value on vertices is
\[
i\colon (J_n,J_d)\mapsto \bigl(\bigsqcup_{J_n} \RR^n\bigr)\sqcup \bigl(\bigsqcup_{J_d} (\RR^d\subset \RR^d)\bigr)~.
\] 
Likewise, let $(\sO(n)\xra{\w{P}}\cV~,~\sO(d\subset n)\xra{\w{Q}} \cV)$ be a pair $(P,Q)$ of objects in $\cV$ each equipped with actions of $\sO(n)$ and $\sO(d\subset n)$, respectively.  
These data then determine the solid diagram of $\infty$-operads
\[
\xymatrix{
\cE^{\amalg}_{\sf inert}  \ar[rrrrrd]^-{(P^\bullet,Q^\bullet)}   \ar[d]^i
&&&&&
\\
\mfld^{\sqcup}_{d\subset n}  \ar@{.>}[rrrrr]^-{\mathsf{Free}_\cE^{(\w{P},\w{Q})}}
&&&&&
\cV
}
\]
in where the value of $(P^\bullet,Q^\bullet)$ on $(J_n,J_d)$ is canonically equivalent to $ P^{\ot J_n} \ot Q^{\ot J_d}$ as a $\bigl(\sO(n)^{J_n} \times \sO(d\subset n)^{J_d}\bigr)$-objects.  
The filler $\mathsf{Free}_\epsilon^{(\w{P},\w{Q})}$ is the desired free construction, and is computed as operadic left Kan extension.  Explicitly, for $X\in \mfld_{d\subset n}$, the value
\begin{equation}\label{free-colimit}
\mathsf{Free}_\cE^{(\w{P},\w{Q})}(X) = \colim_{E\xra{\mathsf{act}} X}  (P^\bullet,Q^\bullet)(E) = \colim_{(J_n,J_d)\xra{\sf act} X} P^{\ot J_n} \ot Q^{\ot J_d}
\end{equation}
where the colimit is over the $\oo$-category $\cE^\amalg_X  := \cE^\amalg_{\sf inert} \times_{\mfld^{\sqcup}_{d\subset n}} \bigl((\mfld^{\sqcup}_{d\subset n})_{\sf act}\bigr)_{/X}$ of active morphisms in $\mfld^{\sqcup}_{d\subset n}$ from the image under $i$ of $\cE^\amalg_{\sf inert}$ to the object $X$.  

We will now compute the colimit in~(\ref{free-colimit}).  
By construction, the projection $\cE^\amalg_X \to \cE^\amalg_{\sf inert}$ is a right fibration whose fiber over $E$ is the Kan complex $\mfld_{d\subset n}(i(E),X)$. 
Consider the subcategory of isomorphisms $\cE^\amalg_{\sf iso}\subset \cE^\amalg_{\sf inert}$ -- it is isomorphic to the category of pairs of finite sets and pairs of bijections among them. 
Denote $\cG = \cE^\amalg_{\sf iso}\times_{\cE^\amalg_{\sf inert}} \cE^\amalg_X$.  
Because the inclusion $\cE^\amalg_{\sf iso}\subset \cE^\amalg_{\sf inert}$ is final, so is the inclusion $\cG \subset \cE^\amalg_X$.  So the colimit~(\ref{free-colimit}) is canonically equivalent to the colimit of the composite $\cG \subset \cE^\amalg_X \xra{(P^\bullet,Q^\bullet)} \cV$.  
Because $\cE^\amalg_{\sf iso}$ is a coproduct of $\infty$-groupoids (Kan complexes) indexed by isomorphism classes of its objects, then $\cG$ is a coproduct of $\infty$-groupoids indexed by isomorphism classes of objects of $\cE^\amalg_{\sf iso}$.  As so, the colimit~(\ref{free-colimit}) breaks up as a coproduct over isomorphism classes of objects of $\cE^\amalg_{\sf iso}$.  

We will now understand the $[E]^{\rm th}$ summand of this colimit.  
Choose a representative $E=(J_n,J_d)\in \cE^\amalg_{\sf iso}$ of this isomorphism class. 
We point out that the Kan complex of $\Aut(E)$ fits into a Kan fibration sequence $\sO(n)^{ J_n}\times \cO(d\subset n)^{ J_d} \to \Aut(E) \to \Sigma_{J_n}\times \Sigma_{J_d}$.  
Consider the right fibration $(\cE^\amalg_{\sf iso})_{/E} \to \cE^\amalg_{\sf iso}$ whose fiber over $E'$ is the Kan complex $\Iso(E',E)$ which is a torsor for the Kan complex $\Aut(E)$ is $E'$ if isomorphic to $E$ and is empty otherwise.  
Denote the resulting right fibration $\cG_E = (\cE^\amalg_{\sf iso})_{/E} \times_{\cE^\amalg_{\sf iso}} \cG~\longrightarrow~ \cG$ whose fibers are either a torsor for $\Aut(E)$ or empty.  
The composite $\cG_E \to \cG \subset \cE^\amalg_X \xra{(P^\bullet,Q^\bullet)} \cV$ is canonically equivalent to the constant map at $P^{\ot J_n}\ot Q^{\ot J_d}$.  
It follows from the definition of the tensor over spaces structure, that the colimit of this composite  is 
\[
\Bigl(\mfld_{d\subset n}\bigl(i(J_n, J_d),X \bigr)\Bigr) \ot \bigl(P^{\ot J_n} \ot Q^{\ot J_d}\bigr)~.
\]  
We conclude from this discussion that the colimit of the composite $\cG \subset \cE^\amalg_X \xra{(P^\bullet,Q^\bullet)} \cV$ is 
\begin{equation}\label{tensor-time}
\coprod_{[(J_n,J_d)]} \Bigl(\mfld_{d\subset n}\bigl(i(J_n,J_d),X \bigr)\Bigr) \ot_{\Aut(J_n,J_d)} \bigl(P^{\ot J_n} \ot Q^{\ot J_d}\bigr)~.
\end{equation}

We make expression~(\ref{tensor-time}) more explicit for the case that $(\w{P},\w{Q}) = \delta(P,Q)$ is a pair of objects with trivial group actions.  
As so, the map $\cG \subset \cE^\amalg_X \xra{(P^\bullet,Q^\bullet)} \cV$ factors through the projection $\cG \to \cE^\amalg_{\sf iso} \to (\mathsf{Fin}_\ast)_{iso}$ the groupoid of finite sets and bijections -- we denote this groupoid as $\Sigma$.   

Recall that the $\sD_{d\subset n}$-manifold $X=(L\subset M)$ is the data of a framed $n$-manifold $M$, a properly embedded smooth submanifold $L$, and a splitting of the framing along $L$.  Evaluation at the origins of $i(J_n,J_d) = \bigl(\bigsqcup_{J_n} \RR^n\bigr)\sqcup \bigl(\bigsqcup_{J_d} (\RR^d\subset \RR^n)\bigr)$ gives a map
\[
\mfld_{d\subset n}\bigl((\bigsqcup_{J_n} \RR^n)\sqcup (\bigsqcup_{J_d} \bigl(\RR^d\subset \RR^n)\bigr)~,~(L\subset M)\bigr) ~\longrightarrow~ \mathsf{Conf}_{J_n}(M\smallsetminus L)\times \mathsf{Conf}_{J_d}(L)~.  
\]
This map is evidently natural among morphisms among the variable $(J_n,J_d)\in \cG$ where the action of $\cG$ on the righthand side factors through the projection $\cG \to \Sigma$.   
There results a $\Sigma$-equivariant map
\[
\Bigl(\mfld_{d\subset n}\bigl(i(J_n,J_d),(L\subset M)\bigr)\Bigr)_{/\sO(n)^{ J_n}\times \sO(d\subset n)^{ J_d}} ~\overset{\sim}\longrightarrow~ \mathsf{Conf}_{J_n}(M\smallsetminus L)\times \mathsf{Conf}_{J_d}(L)~;
\]
and for standard reasons it is an equivalence of Kan complexes.  
We conclude that
\[
\free_\cE^{\delta(P,Q)}(L\subset M) \xra{\simeq} \conf^P(M\smallsetminus L)\ot \conf^Q(L)~.
\]
Finally, the formula 
\[
\free_\cE^{\delta(P,Q)}(L\subset M) = \int_{(L\subset M)} \free_\cE^{\delta(P,Q)}
\]
is a formal consequence of commuting left Kan extensions (here we are using the same notation for $\free_\cE^{\delta(P,Q)}$ and its restriction to $\disk^{\sqcup}_{d\subset n}$).  With Lemma~\ref{frame-or-not}, this completes the proof of the proposition.  

\end{proof}

\begin{remark}
The methods employed here in~\S\ref{free-examples} have been intentionally presented to accommodate much greater generality.  
For instance, with appropriate modifications of the statements, the role of $\sD_{d\subset n}$ (or its framed version) could be replaced by any category of basics $\cB$.  Likewise, the maximal sub-Kan complex $\cE\subset \sD_{d\subset n}$ could be replaced by any map $\cE\to \cB$ of $\oo$-categories.  

\end{remark}
