---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-006-23-disks-and-finite-subsets
section_title: "Disks and finite subsets"
section_number: 2.3
pages: 20-23
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.985
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
We pause our development of factorization homology to relate the $\infty$-category $\disk(\bsc)_{/X}$, which appears in the Definition~\ref{def:fact-hmlgy} of factorization homology, with the enter-path $\infty$-category of another stratified space associated to $X$: the Ran space of $X$.  







Let $i$ be a finite cardinality.  
For $X$ a topological space, the \emph{bounded Ran space} $\Ran_{\leq i}(X)$ is the topological space consisting of subsets $S\subset X$ with bounded cardinality $|S|\leq i$ for which the inclusion $S\hookrightarrow X$ is surjective on connected components;
the topology on $\Ran_{\leq i}(X)$ is the coarsest for which, for each set $I$ with cardinality $|I|=i$ equal to $i$, the map ${\sf Image}\colon X^I \to \Ran_{\leq i}(X)$ is continuous.  
For $f \colon X\hookrightarrow Y$ an open embedding that is surjective on connected components, the evident map $\Ran_{\leq i}(f) \colon \Ran_{\leq i}(X) \to \Ran_{\leq i}(Y)$ is an open embedding.  














In~\S3 of~\cite{aft1} we prove the following result, which in particular states that $\Ran_{\leq i}(X)$ inherits the structure of a stratified space from one on $X$.  
We use the notation 
\begin{equation}\label{surj-notation}
\snglr^{\sf surj}~\subset ~\snglr
\end{equation}
for the $\infty$-subcategory with the same objects and with those morphisms that induce surjections on connected components.  
\begin{prop}[Proposition 3.7.5 of \cite{aft1}]\label{ran-singular}
Let $i$ be a finite cardinality.  
There is a functor between $\infty$-categories
\begin{equation}\label{rans}
\Ran_{\leq i}\colon \snglr^{\sf surj} \longrightarrow \snglr
\end{equation}
for which the underlying topological space of each value $\Ran_{\leq i}(X)$ is the bounded Ran space of the underlying space of $X$, and whose value on a morphism $X\xra{f} Y$ is $\Ran_{\leq i}(f)$.  

\end{prop}




The next result gives a description of the topology of $\Ran_{\leq i}(X)$ in terms of that of $X$.  
\begin{lemma}\label{ran-basis}
Let $i$ be a finite cardinality.
Let $X$ be a stratified space.
Consider the collection of open embeddings 
\[
\bigl\{\Ran_{\leq i}(U) \xra{~\Ran(f)~} \Ran_{\leq i}(X)\bigr\}_{\{U\xra{f} X\}}
\]
indexed by conically smooth open embeddings from finite disjoint unions of basics which are surjective on connected components.
This collection of open embeddins forms a basis for the topology of $\Ran_{\leq i}(X)$.  

\end{lemma}
\begin{proof}
Let $S\in \Ran_{\leq i}(X)$ be an element, and let $S\in O\subset \Ran_{\leq i}(X)$ be an open neighborhood.
We must show that there is a disjoint union of basics $U\hookrightarrow X$ openly embedding into $X$ as a surjection on components so that $S$ belongs to the image of the map $\Ran_{\leq i}(U) \to \Ran_{\leq i}(X)$ and this image lies in $O$.  

Fix a set $I$ of cardinality $i$.  
Choose a map $I\xra{f_0}X$ for which the image ${\sf Image}(f_0)=S$ equals $S$.  
From the definition of the topology of $\Ran_{\leq i}(X)$, the subset $O\subset \Ran_{\leq i}(X)$ being open implies the subset
\[
\w{O}:=\bigl\{I\xra{f} X\mid {\sf Image}(f)\in O  \bigr\}~\subset~X^I
\]
is open. 
From the definition of the product topology on $X^I$, for each $s\in S$ there is an open subset $s \in V_{s}\subset X$ so that the product $\underset{i\in I} \prod V_{f_0(i)} \subset \w{O}$ lies inside $\w{O}$.  
From the definition of a stratified space in the sense of~\S3 of~\cite{aft1}, the collection of conically smooth open embeddings from basics into $X$ forms a basis for the topology of $X$.  
Therefore, we can choose each $V_s$ above to be a basic $s\in U_s\hookrightarrow X$.
Because $X$ is in particular Hausdorff, we can make these choices so that the intersection $U_s \cap U_{s'}$ is empty whenever $s\neq s'\in S$.  
We obtain an open embedding $U:=\underset{s\in S}\bigsqcup U_s \hookrightarrow X$ from a finite disjoint union of basics which is surjective on components.  
By construction, this embedding has the desired properties stated at the beginning of this proof.  


\end{proof}





















































Through Proposition~\ref{ran-singular}, and with the notation of~(\ref{surj-notation}), there is the functor between over $\infty$-categories
\begin{equation}\label{continuous-ran-slice}
\Ran_{\leq i}\colon \snglr^{\sf surj}_{/X} \to \snglr^{\sf surj}_{/\Ran_{\leq i}(X)}
\end{equation}
for each stratified space $X$.  
For the next result, we will denote the full $\infty$-subcategory 
\[
\disk(\bsc)^{{\sf surj}, \leq i}_{/X}~\subset~ \snglr^{\sf surj}_{/X}
\]
consisting of those open embeddings $U\hookrightarrow X$ that are surjective on components and for which $U$ has at most $i$ connected components, each of which is isomorphic to a basic stratified space.  

\begin{lemma}\label{EE-to-E}
Let $i$ be a finite cardinality. 
Let $X$ be a stratified space.
The functor~(\ref{continuous-ran-slice}) restricts as an equivalence of $\infty$-categories 
\[
\Ran_{\leq i}\colon \disk(\bsc)^{{\sf surj},\leq i}_{/X} \xra{~\simeq~} \bsc_{/\Ran_{\leq i}(X)}~.  
\]

\end{lemma}

\begin{proof}
The factorization happens because $\Ran_{\leq i}(U)$ is a basic whenever $U$ is an (at most) $i$-fold disjoint union of basics -- this statement is proved in~\S3 of~\cite{aft1}.  
We will argue that this functor is an equivalence by showing it is an equivalence on maximal $\infty$-subgroupoids, then that it is an equivalence on spaces of morphisms.


Keeping with the notation of~\cite{aft1}, for each stratified space $Z$ we will denote the over $\infty$-category
\[
{\sf Entr}(Z)~:=~\bsc_{/Z}
\]
of basic stratified spaces over $Z$.   
In~\S4 of~\cite{aft1} we show that, for $Z$ a stratified space, the maximal $\infty$-subgroupoid of ${\sf Entr}(Z)$ is $\underset{[B]} \coprod {\sf Entr}_{[B]}(Z)$ where the coproduct is indexed by isomorphism classes of basics, and ${\sf Entr}_{[B]}(Z) =  \sB\End(B)_{/Z}$ is the $\infty$-subcategory of those basics over $Z$ which are isomorphic to $B$.   
Also in~\S4 of~\cite{aft1} we show that ${\sf Entr}_{[B]}(Z) \simeq \Emb\bigl(B,Z\bigr)_{\Aut_0(B)}$ is the coinvariants by the origin preserving automorphisms of $B$, and thereafter that this latter space evaluates at the center of $B$ as an equivalence with the underlying space of the $[B]$-stratum $Z_{[B]}\subset Z$.  
In summary, the maximal $\infty$-subgroupoid of ${\sf Entr}(Z)$ is canonically identified as
\[
\underset{[B]}\coprod {\sf Entr}_{[B]}(Z)~{}~\simeq~{}~ \underset{[B]}\coprod Z_{[B]}~.  
\]

Similarly, the maximal $\infty$-subgroupoid of $\disk(\bsc)^{{\sf surj},\leq i}_{/Z}$ is canonically identified as
\[
\underset{[U]} \coprod \underset{\alpha \in A}\prod  \disk(\bsc_{[U_\alpha]})^{{\sf surj},= i_\alpha}_{/X}~{}~\simeq~{}~ \underset{[U]} \coprod \underset{\alpha \in A} \prod \conf_{I_\alpha}(W_{[U_\alpha]})_{\Sigma_{I_\alpha}}
\]
which we now explain.
The coproducts are indexed by isomorphism classes of finite disjoint unions of basics $U = \underset{\alpha \in A} \bigsqcup (U_\alpha)^{\sqcup I_\alpha}$, grouped here according to isomorphism type, for which $\underset{\alpha \in A} \sum |I_\alpha|\leq i$.
$\bsc_{[U_\alpha]}$ is the full $\infty$-subcategory of $\bsc$ consisting of those basics which are isomorphic to $U_\alpha$; and $i_\alpha := |I_\alpha|$ is the cardinality.  
So the left $[U]$-cofactor is the largest $\infty$-subgroupoid of $\disk(\bsc)^{\sf surj}_{/X}$ consisting of those open embeddings $V \hookrightarrow X$ for which $V$ is isomorphic to an $i_\alpha$-fold disjoint union of the basic $U_\alpha$.  
For $M$ a smooth manifold, $\conf_J(M)$ is the underlying space of the open submanifold $M^J$ consisting of the injections $J\hookrightarrow M$.
The subscript denotes the coinvariants by the evident $\Sigma_J$-action.  



Thus, the map of maximal $\infty$-subgroupoids induced by the functor $\disk(\bsc)^{{\sf surj},\leq i}_{/X} \xra{\Ran_{\leq i}} \bsc_{/\Ran_{\leq i}(X)}$ is canonically identified as the map of spaces
\[
\underset{[U]}\coprod \underset{\alpha \in A} \prod \conf_{I_\alpha}(X_{[U_\alpha]})_{\Sigma_{I_\alpha}}~{}~\simeq~{}~\underset{[U]} \coprod \underset{\alpha \in A}\prod  \disk(\bsc_{[U_\alpha]})^{{\sf surj},= i_\alpha}_{/X}
\longrightarrow
\underset{[B]}\coprod {\sf Entr}_{[B]}\bigl(\Ran_{\leq i}(X)\bigr)~{}~\simeq~{}~
\underset{[B]}\coprod \bigl(\Ran_{\leq i}(X)\bigr)_{[B]}
\]
in where the indexing set of the left coproduct consists of those such isomorphism classes $[U]$ for which $U$ has at most $i$ components.  
Lemma~\ref{ran-basis} grants that this map is a bijection on the sets indexing the coproducts.  
That this map of spaces is an equivalence then follows because, by detailed inspection, there is a canonical isomorphism of stratified spaces
\[
\underset{\alpha \in A} \prod \conf_{I_\alpha}(X_{[U_\alpha]})_{\Sigma_{I_\alpha}}~{}~\cong~{}~\bigl(\Ran_{\leq i}(X)\bigr)_{[\Ran_{\leq i}(U)]}
\]
whose map of underlying spaces is a summand of the above composite map.  


We now consider the map of spaces of morphisms induced by the functor $\disk(\bsc)^{{\sf surj},\leq i}_{/X} \xra{\Ran_{\leq i}} {\sf Entr}\bigl(\Ran_{\leq i}(X)\bigr)$.
This map fits as the top horizontal arrow in the diagram of spaces
\[
\xymatrix{




\Map\bigl([1],\disk(\bsc)^{{\sf surj},\leq i}_{/X}\bigr)  \ar[rr]  \ar[d]_{{\sf ev}_1}
&&
\Map\Bigl([1],{\sf Entr}\bigl(\Ran_{\leq i}(X)\bigr)\Bigr)  \ar[d]^{{\sf ev}_1}
\\
\bigl(\disk(\bsc)^{{\sf surj},\leq i}_{/X}\bigr)^{\sim}  \ar[rr]
&&
\Bigl({\sf Entr}\bigl(\Ran_{\leq i}(X)\bigr)\Bigr)^{\sim}~.
}
\]
We have already shown that the bottom horizontal map is an equivalence of spaces.
To show that the top horizontal map is an equivalence of spaces, it is enough to show that, for each point $(U\hookrightarrow X)$ of the bottom left space, the map of associated fibers is an equivalence.

Let $(U\hookrightarrow X)\in \disk(\bsc)^{{\sf surj},\leq i}_{/X}$.  Both $\disk(\bsc)^{{\sf surj},\leq i}_{/X}$ and ${\sf Entr}\bigl(\Ran_{\leq i}(X))$ being slice-$\infty$-categories, we canonically identify the map of fibers over $(U\hookrightarrow X)$ as the map of maximal $\infty$-subgroupoids
\[
\bigl( \disk(\bsc)^{{\sf surj},\leq i}_{/U} \bigr)^{\sim} \longrightarrow \Bigl({\sf Entr}\bigl(\Ran_{\leq i}(U)\bigr)\Bigr)^{\sim}
\]
induced by $\Ran_{\leq i}$.
We have already shown that this map is an equivalence, and so concludes this proof.


\end{proof}
