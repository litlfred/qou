---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-007-24-localizing-with-respect-to-isotopy-equivalenc
section_title: "Localizing with respect to isotopy equivalences"
section_number: 2.4
pages: 23-26
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.977
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
Here we explain that the $\infty$-category $\disk(\cB)_{/X}$, which appears in the Definition~\ref{def:fact-hmlgy} of factorization homology, can be witnessed as a localization of its un-topologized version $\diskd(\cB)_{/X}$ on the collection of those inclusions of finite disjoint unions of disks $U\subset V$ in $X$ for which this inclusion is isotopic to an isomorphism.  
This comparison plays a fundamental role in recognizing certain colimit expressions in this theory, for instance that support the pushforward formula of~\S\ref{sec.pushforward}.

Given a topological space $X$ and a finite set $J$, we let $\conf_J(X)$ denote the topological space of injections from $J$ to $X$.  There is an evident action of the symmetric group $\Sigma_J$ on this space, and we denote the coinvariants as $\conf_J(X)_{\Sigma_J}$. Finally, given a basic $U \cong \RR^n \times C(Z)$, we denote by $\Aut_0(U)$ the Kan complex of isomorphisms $U \to U$ that preserve the origin $(0,\ast) \in U$. (See Section~4.3 of~\cite{aft1}.) In the following lemma, $\sB$ is the classifying space functor.

\begin{lemma}\label{EE-equivs}
For $\cB$ a category of basics, the maximal $\infty$-groupoid of $\disk(\cB)$ is canonically identified as
\[
\bigl(\disk(\cB)\bigr)^\sim~{}~\simeq~{}~ \underset{[U = \underset{i\in I} \bigsqcup U_i^{\sqcup J_i}]} \coprod \prod_{i\in I} \sB\bigl(\Sigma_{J_i} \wr \End_{\cB}(U_i)\bigr)
\]
where the coproduct is indexed by isomorphism classes of finite disjoint unions of objects of $\cB$, whose connected components are grouped here according to isomorphism type.
In particular, the symmetric monoidal functor $[-]\colon \disk(\cB) \to \Fin$ is conservative.  

For $X$ a $\cB$-manifold, the underlying $\infty$-groupoid of $\disk(\cB)_{/X}$ is canonically identified as the space
\[
\bigl(\disk(\cB)_{/X}\bigr)^\sim~{}~\simeq~{}~ \underset{[U = \underset{i\in I} \bigsqcup U_i^{\sqcup J_i}]} \coprod \prod_{i\in I} \conf_{J_i}(X_{[U_i]})_{\Sigma_{J_i}}
\]
given in terms of unordered configuration spaces of various strata of $X$.  

\end{lemma}

\begin{proof}
The statement concerning $\disk(\cB)$ follows immediately from the characterization of $\bsc$ in~\cite{aft1}.  

Upon the canonical equivalence of $\infty$-categories $\disk(\cB)_{/X} \simeq \disk(\bsc)_{/X}$, we can assume $\cB = \bsc$, so that $\mfld(\cB) \simeq \snglr$ is an $\infty$-category associated to a ${\sf Kan}$-enriched category.  
In \S4.3 of~\cite{aft1} it is shown that the inclusion of $\sf Kan$-groups $\Aut_0(U) \to \End_{\bsc}(U)$ is an equivalence of underlying Kan complexes.  
Upon these considerations, to show the first statement it is sufficient to show that, for each finite set $J$, and each basic $U$, the $\Sigma_J$-equivariant map which is evaluation at each center of $U$
\[
{\sf ev}_{(0)_{j\in J}}\colon \Map_{\snglr}\bigl(U^{\sqcup J}, X\bigr)_{\Aut_0(U)^J} ~\xra{~\simeq~}~\conf_J(X_{[U]}) 
\]
is an equivalence of $\Sigma_J$-spaces.  
We do this by induction on the cardinality $|J|$, with the base case $|J|=1$ offered by results in~\cite{aft1}.  
Now suppose $|J|>1$, and choose a non-empty proper subset $J'\subset J$.
Restriction along this inclusion of subsets gives the commutative diagram
\[
\xymatrix{
\Map_{\snglr}\bigl(U^{\sqcup J}, X\bigr)_{\Aut_0(U)^J}  \ar[rr] \ar[d]^-{{\sf ev}_0}
&&
\Map_{\snglr}\bigl(U^{\sqcup J'}, X\bigr)_{\Aut_0(U)^{J'}}  \ar[d]^-{{\sf ev}_0}
\\
\conf_J(X_{[U]})  \ar[rr]
&&
\conf_{J'}(X_{[U]})
}
\]
which is evidently appropriately equivariant.
In a standard manner, the map of fibers of the horizontal maps is canonically identified as the map of $\Sigma_{J\smallsetminus J'}$-spaces
\[
\Map_{\snglr}\bigl(U^{\sqcup J\smallsetminus J'}, X\smallsetminus J'\bigr)_{\Aut_0(U)^{J\smallsetminus J'}}  \xra{~{\sf ev}_0~}  \conf_{J\smallsetminus J'}(X_{[U]}\smallsetminus J')~,
\]
which is an equivalence by induction. 
The result follows.  

\end{proof}

Let $\cB$ be a category of basics; let $X$ be a $\cB$-manifold.
Consider the $\infty$-subcategory 
\begin{equation}\label{eqn.I_X}
\cI_X\subset \diskd(\cB)_{/X}
\end{equation}
consisting of the same objects but only those morphisms $(U\hookrightarrow X) \hookrightarrow (V\hookrightarrow X)$ whose image in $\disk(\cB)_{/X}$ is an equivalence. Note that in~\ref{eqn.I_X}, we think of $X$ as an object of $\mfldd(\cB)$, while when we refer to $\disk(\cB)_{/X}$, we think of $X$ as an object of $\mfld(\cB)$.

\begin{prop}\label{EEd-vs-EE}
The standard functor
\begin{equation}\label{disc-to-cont}
\diskd(\cB)_{/X} \longrightarrow \disk(\cB)_{/X}
\end{equation}
witness an equivalence between $\infty$-operads from the localization (among $\infty$-operads):
\[
\bigl(\diskd(\cB)_{/X}\bigr)[\cI_X^{-1}]~\simeq~\disk(\cB)_{/X}~.
\]
In particular, for each symmetric monoidal $\infty$-category $\cV$, restriction defines a fully faithful functor
\[
\Alg_{\disk(\cB)_{/X}}(\cV)  ~{}~\hookrightarrow~{}~\Alg_{\diskd(\cB)_{/X}}(\cV)
\]
whose image consists of those $\diskd(\cB)_{/X}$ algebras that carry each isotopy equivalence to an equivalence in $\cV$.  
\end{prop}

\begin{proof}
First note that the $\infty$-subcategory $\cI_X\subset \diskd(\cB)_{/X}$ lies over equivalences in $\Fin_\ast$.
As so, the localization $\bigl(\diskd(\cB)_{/X}\bigr)[\cI_X^{-1}]$ (among $\infty$-categories) canonically lies over $\Fin_\ast$.  
Therefore, should the canonical functor $\bigl(\diskd(\cB)_{/X}\bigr)[\cI_X^{-1}]\xra{\simeq}\disk(\cB)_{/X}$ from the localization (among $\infty$-categories) be an equivalence between $\infty$-categories, then this localization among $\infty$-categories is in fact an $\infty$-operad itself; furthermore, this localization among $\infty$-categories also presents the $\infty$-operadic localization. 
We are thusly reduced to showing that the functor~(\ref{disc-to-cont}) is a localization between $\infty$-categories.  


Note that the functor~(\ref{disc-to-cont}) is essentially surjective, manifestly.  
We will argue that the resulting functor from the localization is an equivalence by showing it is an equivalence on underlying $\infty$-groupoids, then that it is an equivalence on spaces of morphisms.
We recall that, as in Observation \ref{B-independent}, since $\mfld(\cB) \to \snglr$ is a right fibration there are canonical equivalences of $\infty$-categories
\[
\diskd(\cB)_{/X}~ \simeq~ \diskd(\bsc)_{/X} ~=:~ \sD_X \qquad\text{ and }\qquad \disk(\cB)_{/X}~\simeq~ \disk(\bsc)_{/X} ~=:~ \cD_X
\]
and we adopt the indicated notation for this proof.
Therefore, we can assume $\cB = \bsc$.  

The underlying $\infty$-groupoid of $\sD_X$ is the classifying space $\sB \cI_X$.  
In light of the above coproduct in Lemma~\ref{EE-equivs}, fix an isomorphism type $[U=\underset{i\in I} \bigsqcup U_i^{\sqcup J_i}]$ of a finite disjoint union of a basic stratified space.
Consider the full subcategory $\cI_X^{[U]}\subset \cI_X$ consisting of those $(V\hookrightarrow X)$ for which $V\cong U$.
We thus seek to show that the resulting functor $\cI_X^{[U]} \to \underset{i\in I} \prod \conf_{J_i}(X_{[U_i]})_{\Sigma_{J_i}}$ witnesses an equivalence from the classifying space.  
We will do this by first showing that the functor $\underset{i\in I} \prod \conf_{J_i}(X_{[U_i]})\cap - \colon \cI_X^{[U]} \to \underset{i\in I} \prod \cI^{[(U_i^{\sqcup J_i})_{[U_i]}}_{X_{[U_i]}}$ induces an equivalence on classifying spaces, then observing a canonical equivalence of spaces $\sB \cI^{[(U_i^{\sqcup J_i})_{[U_i]}]}_{X_{[U_i]}} \simeq \conf_{J_i}(X_{[U_i]})_{\Sigma_{J_i}}$.  

Consider the slice category $(\cI_X^{[U]})^{(R_i\hookrightarrow X_{[U_i]})_{i\in I}/}$.
An object is an object $(U'\hookrightarrow X)$ of $\cI_X^{[U]}$ for which, for each $i\in I$, there is an inclusion $R_i\subset U'_{[U_i]}$ which is a bijection on components, and a morphism is an inclusion of such.
Because such $(U'_{[U_i]}\hookrightarrow X_{[U_i]})$ form a base for the topology about $R_i\hookrightarrow X_{[U_i]}$, then this category is filtered. 
In particular, the classifying space $\sB(\cI_X^{[U]})^{(R_i\hookrightarrow X_{[U_i]})_{i\in I}/}\simeq \ast$ is contractible.  
It follows that the functor $\underset{i\in I} \prod \conf_{J_i}(X_{[U_i]})\cap - \colon \cI_X^{[U]} \to \underset{i\in I} \prod \cI^{[(U_i^{\sqcup J_i})_{[U_i]}]}_{X_{[U_i]}}$ induces an equivalence on classifying spaces, as desired.  

Now, let $M$ be a smooth manifold, so that $I=\ast$ is a singleton. 
The category $\cI_M^{[U]}$ forms a basis for the standard Grothendieck topology on $\conf_{J_i}(M)_{\Sigma_{J_i}}$.  
It follows from Corollary 1.6 of~\cite{Dugger--Isaksen} that the canonical map of topological spaces
\[
\underset{(\underset{j\in J_i} \sqcup R_j\hookrightarrow M)\in \cI^{[U]}_M} \colim~ \underset{j\in J_i} \prod R_j~{}~\xra{~\simeq~}~{}~ \conf_{J_i}(M)_{\Sigma_{J_i}}
\]
is a homotopy equivalence.  
Because each term $R_j$ in this colimit is contractible, then this colimit is identified as the classifying space
\[
\sB \cI^{[U]}_M~\simeq~ \underset{(\underset{j\in J_i} \sqcup R_j\hookrightarrow M)\in \cI^{[U]}_M} \colim~ \underset{j\in J_i}\prod R_j~.
\]
Applying this to the case $M=X_{[U_i]}$, we conclude that $\sB \cI^{[(U_i^{\sqcup J_i})_{[U_i]}}_{X_{[U_i]}} \simeq \conf_{J_i}(M)_{\Sigma_{J_i}}$.
In summary, we have verified that the map of underlying $\infty$-groupoids
\[
\bigl(\sD_X[\cI_X^{-1}]\bigr)^{\sim} \xra{~\simeq~} \bigl(\cD_X\bigr)^{\sim}
\]
is an equivalence.  

We now show that the functor induces an equivalence on spaces of morphisms.
Consider the diagram of spaces
\[
\xymatrix{
\bigl(\sD_U[\cI_U^{-1}]\bigr)^{\sim}  \ar[r]  \ar[d]_-{(U\hookrightarrow X)}
&
\cD_U^{\sim}  \ar[d]^-{(U\hookrightarrow X)}
\\
\bigl(\sD_X[\cI_X^{-1}]\bigr)^{(1)} \ar[r]  \ar[d]_-{{\sf ev}_1}
&
\cD_X^{(1)}  \ar[d]^-{{\sf ev}_1}
\\
\bigl(\sD_X[\cI_X^{-1}]\bigr)^{\sim}  \ar[r]
&
\cD_X^{\sim}
}
\]
where a superscript ${}^{(1)}$ indicates a space of morphisms, and the upper vertical arrows are given as $(V\hookrightarrow U)\mapsto \bigl((V\hookrightarrow X)\hookrightarrow (U\hookrightarrow X)\bigr)$.
Our goal is to show that the middle horizontal arrow is an equivalence.
We will accomplish this by showing that the diagram is a map of fiber sequences, for we have already shown that the top and bottom horizontal maps are equivalences.

The right vertical sequence is a fiber sequence because such evaluation maps are coCartesian fibrations, in general.  
Then, by inspection, the fiber over $(U\hookrightarrow X)$ is the underlying $\infty$-groupoid of the slice $(\cD_X)_{/(U\hookrightarrow X)}$.
This slice is canonically identified as $\cD_U$.  

Let us show that the left vertical sequence is a fiber sequence.  
The space of morphisms of $\bigl(\sD_X[\cI_X^{-1}]\bigr)^{(1)}$ is the classifying space of the subcategory of the functor category $\Fun^{\cI_X}\bigl([1],\sD_X\bigr) \subset \Fun\bigl([1],\sD_X\bigr)$ consisting of the same objects but only those natural transformations by $\cI$.  
We claim the fiber over $(U\hookrightarrow X)$ of the evaluation map is canonically identified as in the sequence
\[
\bigl(\sD_U[\cI_U^{-1}]\bigr)^{\sim} \xra{~(U\hookrightarrow X)~}\bigl(\sD_X[\cI_X^{-1}]\bigr)^{(1)} \xra{~{\sf ev}_1~} \bigl(\sD_X[\cI_X^{-1}]\bigr)^{\sim}~.
\]
This claim is justified through Quillen's Theorem B, for the named fiber is the classifying space of the slice category $(\cI_X)_{/(U\hookrightarrow X)}$ which is canonically isomorphic to $\cI_U$.  
To apply Quillen's Theorem B, we must show that each morphism $(U\hookrightarrow X) \hookrightarrow (V\hookrightarrow X)$ in $\cI$ induces an equivalence of spaces $\sB\bigl((\cI_X)_{/(U\hookrightarrow X)}\bigr) \simeq \sB\bigl((\cI_X)_{/(V\hookrightarrow X)}\bigr)$.  
This map of spaces is canonically identified as $\sB \cI_U \to \sB \cI_V$.
Through the previous analysis of this proof, this map is further identified as the map of spaces $\underset{[B]} \coprod U_{[B]} \to \underset{[B]} \coprod V_{[B]}$ induced from the inclusion $U\hookrightarrow V$.
Because $U$ and $V$ are abstractly isomorphic, then results of~\cite{aft1} give that each such inclusion is isotopic through stratified open embeddings to an isomorphism.  
We conclude that Quillen's Theorem B applies. See also Theorem~5.3 of~\cite{barwick}.
\end{proof}

\begin{lemma}\label{refinement-localize}

Let $r\colon \w{X}\to X$ be a refinement between stratified spaces.
Then there is a functor 
\[
\disk(\bsc)_{/\w{X}} \longrightarrow \disk(\bsc)_{/X}
\]
which is a localization.

\end{lemma}

\begin{proof}

There is an obvious functor $\snglrd(\bsc)_{/\w{X}}\to \snglrd(\bsc)_{/X}$ given by assigning to $(\w{i}\colon \w{Z}\hookrightarrow\w{X})$ the object $(i\colon Z\hookrightarrow X)$ where $Z=\w{i}(\w{Z})\subset X$ is the image with the inherited stratification. 
Observe that this functor sends finite disjoint unions of basics conically smoothly openly embedding into $\w{X}$, to finite disjoint unions conically smoothly openly embedding into $X$.  
Also observe that this functor sends stratified isotopy equivalences to stratified isotopy equivalences.  
After these observations, the desired functor happens through Proposition~\ref{EEd-vs-EE}.

Notice that the map of underlying $\infty$-groupoids $\bigl(\disk(\bsc)_{/\w{X}}\bigr)^\sim \to \bigl(\disk(\bsc)_{/X}\bigr)^\sim$ respects the presentation of these spaces in Lemma~\ref{EE-equivs} as a coproduct of a product.  
Through the same logic as in the proof of Proposition~\ref{EEd-vs-EE}, it is enough to show that the functor
\[
\bsc_{/\conf_i(\w{M})} \longrightarrow \bsc_{/\conf_i(M)}
\]
is a localization for each finite cardinality $i$ and each refinement $\w{M}\xra{r} M$ of a smooth manifold.  
Because $\w{M}\to M$ is a refinement, then so is the map of stratified spaces $\conf_i(\w{M})\to \conf_i(M)$, by inspection.  
The result is an instance of Proposition~1.2.14 of~\cite{aft1}.  

\end{proof}
