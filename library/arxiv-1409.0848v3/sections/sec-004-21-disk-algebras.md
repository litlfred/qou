---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-004-21-disk-algebras
section_title: "Disk algebras"
section_number: 2.1
pages: 14-17
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.967
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
Factorization homology will have a universal property with respect to monoidal and operadic structures on $\mfld(\cB)$ and $\mfld(\cB)_{/X}$, which we present below in Constructions \ref{B-monoidals} and \ref{B-operadics}.

\begin{construction}[The symmetric monoidal structures on $\mfld(\cB)$ and $\disk(\cB)$]\label{B-monoidals}
Using disjoint union, we endow $\snglrd$, $\snglr$, $\mfldd(\cB)$, and $\mfld(\cB)$ with natural symmetric monoidal structures. The details are as follows: Disjoint union makes each of the $\Kan$-enriched categories $\snglrd$ and $\snglr$ into a symmetric monoidal $\Kan$-enriched category in the usual sense.
We then realize each as a symmetric monoidal $\infty$-category (by taking the simplicial nerve, for instance -- see Proposition 2.1.1.27 of~\cite{HA}). 

To further endow $\mfldd(\cB)$ and $\mfld(\cB)$ with symmetric monoidal structures, recall that they are defined via limit diagrams as below
\[\xymatrix{
\mfldd(\cB)\ar[r]\ar[d]&\mfld(\cB)\ar[r]\ar[d]&\psh(\bsc)_{/\cB}\ar[d]\\
\snglrd\ar[r]&\snglr\ar[r]^-\tau&\psh(\bsc)\\}\]
where the functor $\tau$ is the tangent classifier, i.e., the restriction of the Yoneda embedding to basics. 
In light of Lemma~\ref{creates-limits}, to endow $\mfld(\cB)$ with a symmetric monoidal structure it suffices to lift the diagram among $\infty$-categories $\snglr \ra \psh(\bsc)\la\psh(\bsc)_{/\cB}$ to a diagram among symmetric monoidal $\infty$-categories; this is easily accomplished. 
Both $\psh(\bsc)$ and $\psh(\bsc)_{/\cB}$ are cocomplete and hence carry a coCartesian monoidal structure (i.e., the monoidal structure given by coproducts); since the forgetful functor $\psh(\bsc)_{/\cB}\ra \psh(\bsc)$ preserves colimits, it in particular preserves coproducts, and is thus symmetric monoidal with respect to this coCartesian monoidal structure.  
Now, because each basic $U$ is connected, there is a canonical isomorphism of Kan complexes
\[
\underset{i\in I} \coprod \snglr(U,M_i) \xra{~\cong~} \snglr\bigl(U,\underset{i\in I} \bigsqcup M_i\bigr)~.  
\]
So $\snglr \xra{\tau} \psh(\bsc)$ canonically extends as a symmetric monoidal functor.

Finally, since $\snglrd\ra\snglr$ preserves disjoint union, through the same logic $\mfldd(\cB)$ obtains a symmetric monoidal structure.

\end{construction}

\begin{definition}\label{sym-mon-mflds}
The symmetric monoidal $\oo$-categories
\[
\disk(\cB)~\subset~\mfld(\cB)
\qquad\text{ and }\qquad
\diskd(\cB)~\subset~\mfldd(\cB)
\]
are smallest full symmetric monoidal subcategories containing $\cB\subset \mfld(\cB)$ and $\cB\underset{\mfld(\cB)}\times \mfldd(\cB) \subset \mfldd(\cB)$, respectively.
\end{definition}

\begin{remark}
The objects of $\disk(\cB)$ are disjoint unions of elements of $\cB$.
\end{remark}
The slice categories $\disk(\cB)_{/X}$ and $\mfld(\cB)_{/X}$ do not carry symmetric monoidal structures -- for instance, there is no natural way to take a disjoint union of two embeddings if the embeddings overlap. 
Regardless, we endow these categories with the structure of an $\infty$-operad. As usual (see Section~2.1 of~\cite{HA}), one can think of these $\infty$-operads as colored operads, one color for every embedding of a finite disjoint union of basics $U \into X$.

\begin{construction}[$\disk(\cB)_{/X}$ as an $\infty$-operad]\label{B-operadics}
The empty stratified space $\emptyset$ is a symmetric monoidal unit for $\snglrd$ and $\snglr$, and it is also initial in each of the associated underlying $\infty$-categories.
It follows that the same is true for the symmetric monoidal structures on $\mfldd(\cB)$ and $\mfld(\cB)$.
Let $X$ be a $\cB$-manifold.
Notation~\ref{slice-convention} produces the $\infty$-operads $\mfldd(\cB)_{/X}$ and $\mfld(\cB)_{/X}$ as well as $\diskd(\cB)_{/X}$ and $\disk(\cB)_{/X}$.

\end{construction}

\begin{example}
The fiber of the $\infty$-operad $\snglr_{/X}$ over the finite set $\ast_+$ is an $\infty$-category whose objects are conically smooth open embeddings $(Y \into X)$, where $Y$ is a connected stratified space. A morphism $(Y \into X) \to (Y' \into X)$ is specified by a conically smooth open embedding $Y \into Y'$ and an isotopy from $Y \into X$ to the composite $Y \into Y' \into X$. A multi-morphism from $\bigl((Y_1 \into X), (Y_2 \into X)\bigr)$ to $(Y \into X)$ is a conically smooth open embedding $Y_1\sqcup Y_2\hookrightarrow Y$ from the disjoint union, together with a pair of isotopies $\gamma_\nu \colon Y_\nu \times [0,1]\to X$ from the given $Y_\nu \into X$ to the composition $Y_\nu \into Y_1\sqcup Y_2\into X$.  
Notice that this last composition makes use of $\emptyset$ being both initial and the symmetric monoidal unit.  
\end{example}


\begin{remark}
We caution the reader about a notational conflict: There are equivalences
\[
\bigl(\disk(\cB)_{/X}\bigr)_{|\ast_+}~\simeq ~ \disk(\cB)_{/X}\qquad \text{ and }\qquad \bigl(\mfld(\cB)_{/X}\bigr)_{|\ast_+}~\simeq ~ \mfld(\cB)_{/X}~.
\]   
Here, the lefthand side of each equivalence is the underlying $\infty$-category of the $\infty$-operad defined in Construction~\ref{B-operadics}, while the righthand side is the $\infty$-category of disks/$\cB$-manifolds equipped with a map to $X$.
Furthermore, the maps of $\oo$-operads
\[
\disk(\cB)_{/X} \to \disk(\cB)\qquad\text{ and }\qquad \mfld(\cB)_{/X} \to \mfld(\cB)
\]
restrict to the standard functors on underlying $\infty$-categories.  

\end{remark}

\begin{observation}\label{B-independent}
Let $X= (X,g)$ be a $\cB$-manifold.
Then the $\infty$-operad $\disk(\cB)_{/X}$ is independent of the $\cB$-structure on the underlying stratified space of $X$.  
More precisely, because $\cB \to \bsc$ is a right fibration, then the map
\[
\disk(\cB)_{/X} \xra{~\simeq~} \disk(\bsc)_{/X}
\]
is an equivalence of $\infty$-operads.  
For the same reason, for $(U\hookrightarrow X)$ a point of $\disk(\cB)_{/X}$, there is a canonical identification of $\infty$-categories
\[
\disk(\cB)_{/U}~{}~\simeq~{}~\bigl(\disk(\cB)_{/X}\bigr)_{/(U\hookrightarrow X)}~.
\] The analogous assertions hold if replacing $\disk(\cB)$ by $\mfld(\cB)$.

\end{observation}

\begin{notation}
Defined in~\cite{aft1} is the category of basics $\sD_n$, governing smooth $n$-manifolds, and the various elaborations governing smooth $n$-manifolds with boundary, possibly equipped with a framing.  
We use the shorthand notation
	\[
	\disk_n = \disk(\sD_n)~,
	\qquad
	\disk_n^{\fr} = \disk(\sD_n^{\fr})~,
	\qquad
	\disk_n^{\partial} = \disk(\sD_n^{\partial})~,
	\qquad
	\disk_{d\subset n}^{\fr} = \disk(\sD_{d\subset n}^{\fr})~,
	\]
and likewise for other elaborations on $\sD$. For example, the underlying $\infty$-category of $\disk(\sD_n)$ is the $\infty$-category whose objects are diffeomorphic to a finite disjoint union of standard $\RR^n$, and whose morphisms are given by smooth open embeddings between them. The underlying $\infty$-category of $\disk_n^{\fr}$ has objects finite, disjoint unions of $\RR^n$ together with a framing. The space of morphisms between two framed manifolds has the homotopy type of the space of smooth embeddings together with a choice of homotopy between framings. In all these cases, the symmetric monoidal structure is disjoint union.
\end{notation}

\begin{notation}\label{notation.disks}

Prompted by the upcoming Proposition~\ref{smoothing}, and by Notation~\ref{slice-convention}, we will make the following notational conventions
\[
\Alg_{\diskd(\cB)}(\cV)~:=~\Fun^\ot\bigl(\diskd(\cB),\cV\bigr)\qquad\text{ and }\qquad\Alg_{\disk(\cB)}(\cV)~:=~\Fun^\ot\bigl(\disk(\cB),\cV\bigr)
\]
and refer to their objects as $\diskd(\cB)$-algebras and $\disk(\cB)$-algebras, respectively. 

\end{notation}

\begin{remark}
We caution the reader concerning our non-standard notation, which is summarized as follows.
\begin{itemize}
\item As Notation~\ref{sym-cat-same}, we do not distinguish between the notation for a symmetric monoidal $\infty$-category and its underlying $\infty$-category.
\item As Notation~\ref{slice-convention}, we do not distinguish between the notation for certain slice $\infty$-categories and their corresponding $\infty$-operads.  
\item As Notation~\ref{notation.disks}, we use $\Alg_{\disk(\cB)}(\cV)$ for \emph{symmetric monoidal} functors, not just maps of operads.  
Likewise for the other variants such as that concerning $\mfld(\cB)$.
\item As Notation~\ref{slice-convention} we use $\Alg_{X}(\cV)$ for those maps of $\infty$-operads $\disk(\cB)_{/X} \to \cV$  that send \emph{pre-coCartesian} edges to coCartesian edges.  
Likewise for the other variants such as that concerning $\mfld(\cB)$.

\end{itemize}
\end{remark}

\begin{example}\label{n-disk-algebras}
A $\disk^{\fr}_1$-algebra in $\cV$ is canonically identified as an $A_\infty$-algebra in $\cV$.  

\end{example}

In what follows, we let $\cE_n$ denote the $\infty$-operad of little $n$-disks.

\begin{prop}\label{smoothing}
Let $\cV$ be a symmetric monoidal $\infty$-category.
Let $n$ be a finite cardinality.  
There is a canonical equivalence of $\infty$-categories
\[
\Alg_{\disk_n^{\sf fr}}(\cV)\xra{\simeq}\Alg_{\cE_n}(\cV)~.
\]
With respect to the given $\sO(n)$-action on the righthand side of the above equivalence, there is an equivalence of $\infty$-categories
\[
\Alg_{\disk_n}(\cV) \xra{\simeq} \Alg_{\cE_n}(\cV)^{\sf \sO(n)}
\]
to the $\sO(n)$-invariants.  

\end{prop}
\begin{proof}
The evident $\cE_n$-algebra in $\disk_n^{\sf fr}$ induces a symmetric monoidal functor ${\sf Env}(\cE_n)\to \disk_n^{\sf fr}$ from the symmetric monoidal envelope.  
The mapping homotopy types of both sides of this functor are in terms of the spaces $\conf_I(\RR^n):= \{I\hookrightarrow \RR^n\}$, spaces of injective maps into $\RR^n$ from finite sets.  
Inspecting this symmetric monoidal functor reveals that it is an equivalence.  
This gives the first equivalence.

There is the symmetric monoidal right fibration $\disk_n^{\sf fr} \to \disk_n$, which manifestly factors through the $\sO(n)$-invariants.
The fiber over $\RR^n$ is canonically identified as $\Emb(\RR^n,\RR^n) \simeq \sO(n)$, with the translation action of $\sO(n)$.  
The second equivalence follows.  

\end{proof}

\begin{example}\label{deligne-boundary}
Consider the category of basics $\sD^{\partial,\fr}_n$. Then a $\sD^{\partial,\fr}_n$ manifold is an $n$-manifold possibly with boundary, equipped with a framing of the $n$-manifold and a splitting of the framing on the boundary as a product framing. $\disk_n^{\partial,\fr}$-algebras are equivalent to algebras over the Swiss-cheese operad of \cite{voronov}; an object can be regarded as a triple $(A,B,\alpha)$ of a $\disk^{\fr}_n$-algebra $A$, a $\disk^{\fr}_{n-1}$-algebra $B$, and a map
	\[
	\alpha\colon A\longrightarrow {\sf HC}^\ast_{\sD^{\fr}_{n-1}}(B) := {\m_B^{\disk^{\fr}_{n-1}}}(B,B)
	\] 
which is a map of $\disk^{\fr}_n$-algebras; this reformulation is the higher Deligne conjecture, proved in this generality in~\cite{HA} and~\cite{thomas}.
\end{example}
