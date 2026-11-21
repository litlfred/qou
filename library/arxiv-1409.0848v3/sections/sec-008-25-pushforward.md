---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-008-25-pushforward
section_title: "Pushforward"
section_number: 2.5
pages: 26-30
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.977
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
\label{sec.pushforward}
For this subsection, we fix a symmetric monoidal $\infty$-category $\cV$ that is $\ot$-sifted cocomplete.  

\begin{lemma}\label{f-inv-factr}
Let $X$ be a $\cB$-manifold and $Y$ a $\cB'$-manifold, and let $f\colon X\to Y$ be a constructible bundle of the underlying stratified spaces. Taking inverse images defines a functor of $\oo$-operads
\[f^{-1}: \disk(\cB')_{/Y}\longrightarrow \mfld(\cB)_{/X}\]
which on objects sends $U\hookrightarrow Y$ to $f^{-1}U\hookrightarrow X$. As a consequence, there is a natural pushforward functor \[f_\ast: \Alg_{X}(\cV)\longrightarrow \Alg_{Y}(\cV)\] that sends an algebra $A$ on $X$ to the algebra on $Y$ taking values 
\[
f_\ast A(U\hookrightarrow Y) ~{}~\simeq~{}~ \int_{f^{-1}U}A ~.
\] 

\end{lemma}

\begin{proof}

Note that taking point-wise inverse images defines a functor of discrete categories $\diskd(\bsc)_{/Y} \ra \snglrd_{/X}$ which, additionally, preserves the multi-category structure of Construction \ref{B-operadics}. We first show that this functor can be naturally extended to the topological case, i.e., that there is a preferred filler in the diagram of $\infty$-operads
\[
\xymatrix{
\diskd(\bsc)_{/Y}  \ar[rr]^-{f^{-1}}  \ar[d]
&&
\snglrd_{/X}  \ar[d]
\\
\disk(\bsc)_{/Y}  \ar@{-->}[rr]^-{f^{-1}}
&&
\snglr_{/X}~.
}
\]
Because $f$ is a constructible bundle, the collections $\cI$ and $\cJ$ of isotopy equivalences in $\diskd(\bsc)_{/Y}$ and $\snglrd_{/X}$, respectively, are mapped to one another by $f^{-1}$. Further, they map to equivalences in $\disk(\bsc)_{/Y}$ and $\snglr_{/X}$, respectively. By the universal property of localization, we can thus factor the previous diagram as
\[
\xymatrix{
\diskd(\bsc)_{/Y}  \ar[rr]^-{f^{-1}}  \ar[d]
&&
\snglrd_{/X}  \ar[d]
\\
\diskd(\bsc)_{/Y}[\cI^{-1}]  \ar[rr]^-{f^{-1}}  \ar[d]^{\sim}
&&
\snglrd_{/X}[\cJ^{-1}]  \ar[d]
\\
\disk(\bsc)_{/Y}  \ar@{-->}[rr]^-{f^{-1}}
&&
\snglr_{/X}~.
}
\]
Proposition~\ref{EEd-vs-EE} states that the bottom left downward arrow is an equivalence, as indicated, thereby determining the filler.  

Recall from Observation \ref{B-independent} that $\cB$-manifold structure on $X$ defines an equivalence $\snglr_{/X} \simeq \mfld(\cB)_{/X}$, directly from the definition of structures by right fibrations; the same is true for the $\cB'$-manifold structures on basics in $Y$. Under the hypotheses of the Lemma, we consequently have a map of $\oo$-operads $\disk(\cB')_{/Y}\ra \mfld(\cB)_{/X}$ defined by $f^{-1}$. The desired functor is the composition
\[\xymatrix{
f_\ast \colon \Alg_{X}(\cV) \ar[rr]^-{\int_-}&&\Alg_{\mfld(\cB)_{/X}}(\cV)\ar[rr]^-{(f^{-1})^\ast}&&\Alg_{Y}(\cV)~.\\
}\]

\end{proof}

We have the following result about this pushed-forward algebra $f_\ast A$.

\begin{theorem}[Pushforward]\label{:(}
Let $\cV$ be a symmetric monoidal $\oo$-category which is $\ot$-sifted cocomplete; let $X$ be a $\cB$-manifold with $f:X\ra Y$ a weakly constructible bundle over a stratified space $Y$. 
There is a commutative diagram:
\[\xymatrix{
\Alg_{X}(\cV)\ar[rr]^{\int_X}\ar[dr]_{f_\ast }&&\cV\\
&\Alg_{Y}\ar[ur]_{\int_Y}(\cV)\\}
\] In particular, for any $\disk(\cB)$-algebra $A$, there is a canonical equivalence in $\cV$:
\[ 
\int_Y f_\ast A~{}~ \simeq~{}~ \int_XA~.
\]
\end{theorem}

The proof of this theorem will involve an auxiliary $\oo$-category $\cX_f$ built from the constructible bundle $f$.

\begin{definition}\label{def.disk-f}
Let $X$ be a $\cB$-manifold, and let $Y$ be a $\cB'$-manifold. For $f:X\ra Y$ a constructible bundle, the $\oo$-category $\cX_f$ is the limit of the following diagram
\[
\xymatrix{
\disk(\cB)_{/X}\ar@{_{(}->}[dr]
&
&
\Fun\bigl([1],\mfld(\cB)_{/X}\bigr)\ar[rd]_{{\sf ev}_1}   \ar[ld]^{{\sf ev}_0}    
&
&
\disk(\cB')_{/Y}   \ar[dl]^{f^{-1}}
\\
&
\mfld(\cB)_{/X}
&
&
\mfld(\cB)_{/X}
}
\] 
where $\Fun\bigl([1],\mfld(\cB)_{/X}\bigr)$ is the $\oo$-category of 1-morphisms in $\mfld(\cB)_{/X}$. 
\end{definition}

Informally, $\cX_f$ consists of compatible triples $(U, V, U\hookrightarrow f^{-1}V)$, where $V$ is a finite disjoint union of basics in $Y$; $U$ is a finite disjoint union of basics in $X$; the embedding $U\hookrightarrow f^{-1}V$ is compatible with the embeddings $f^{-1}V\hookrightarrow X$ and $U\hookrightarrow X$. 
We are able to utilize this $\oo$-category $\cX_f$ because of the following key finality property.

\begin{lemma}\label{final} For any constructible bundle $X\xra{f} Y$ between stratified spaces, the functor ${\sf ev}_0:\cX_f \ra \disk(\cB)_{/X}$ is final.
\end{lemma}
\begin{proof} 
The functor ${\sf ev}_0$ is a Cartesian fibration of $\oo$-categories. Thus, to check finality, by Lemma 4.1.3.2 of \cite{HTT}, it suffices to show that, for each $U\in \disk(\cB)_{/X}$, the fiber ${\sf ev}_0^{-1}V$ has contractible classifying space.
So let $V\in \disk(\cB)_{X}$.
Unwinding the definition of $\cX_f$, we must show contractibility of the classifying space of the iterated slice $\infty$-category $\bigl(\disk(\cB)_{/Y}\bigr)^{U/}$. 

The projection from this slice $\bigl(\disk(\cB)_{/Y}\bigr)^{U/} \to \disk(\cB)_{/Y}$ is a left fibration, and so it is classified by a functor, justifiably written as 
\[
\Map_{\mfld(\cB)_{/X}}(U,f^{-1}-)\colon \disk(\cB)_{/Y} \to \spaces~,
\]
whose colimit is identified as the relevant classifying space 
\[
\sB\bigl(\disk(\cB)_{/Y}\bigr)^{U/}~{}~\simeq~{}~\underset{(V\hookrightarrow Y)\in \disk(\cB)_{/Y}}\colim ~\Map_{\mfld(\cB)_{/X}}(U,f^{-1}V)~.  
\]
So we seek to show the righthand colimit is contractible.

Formal is that the sequence of maps
\[
\Map_{\mfld(\cB)_{/X}}(U,f^{-1}V)~\longrightarrow~\Map_{\mfld(\cB)}(U,f^{-1}V)~\longrightarrow~\Map_{\mfld(\cB)}(U,X)
\]
is a fiber sequence (here the fiber is taken over any implicit morphism $U\hookrightarrow X$, thereby giving meaning to the lefthand space).  
So we seek to show the map from the colimit
\[
\underset{(V\hookrightarrow Y)\in \disk(\cB)_{/Y}}\colim \Map_{\mfld(\cB)}(U,f^{-1}V)~{}~\longrightarrow~{}~ \Map_{\mfld(\cB)}(U,X)
\]
is an equivalence of spaces. 
We recognize this map of spaces as the map of fibers over $U\in \disk(\cB)$ of the map of right fibrations over $\disk(\cB)$:
\[
\underset{(V\hookrightarrow Y)\in \disk(\cB)_{/Y}}\colim \disk(\cB)_{/f^{-1}V} \longrightarrow \disk(\cB)_{/X}~.
\]
Being right fibrations, it is enough to show that this functor is an equivalence on underlying $\infty$-groupoids.

Through Lemma~\ref{EE-equivs} this is the problem of showing, for each finite set $J$ and each basic $U$, that the map of spaces
\[
\underset{(V\hookrightarrow Y)\in \disk(\cB)_{/Y}}\colim \conf_J\bigl((f^{-1}V)_{[U]}\bigr)_{\Sigma_J} ~\longrightarrow~ \conf_J(X_{[U]})_{\Sigma_J}
\]
is an equivalence. 
So we can assume that the underlying stratified space of $X=M$ is an ordinary smooth manifold.  

Lemma~\ref{EEd-vs-EE} grants that the forgetful map
\[
\underset{(V\hookrightarrow Y)\in \diskd(\bsc)_{/Y}}\colim \conf_J\bigl(f^{-1}V\bigr)_{\Sigma_J} 
~\xra{~\simeq~}~
\underset{(V\hookrightarrow Y)\in \disk(\cB)_{/Y}}\colim \conf_J\bigl(f^{-1}V\bigr)_{\Sigma_J} 
\]
is an equivalence of spaces.  
Now notice that, for each $(V\hookrightarrow Y)\in \diskd(\bsc)_{/Y}$, the map $\conf_J(f^{-1}V) \to \conf_J(M)$ an open embedding.  Also, for each point $c\colon J\hookrightarrow M$ the image $f\bigl(c(J)\bigr)\subset Y$ has cardinality at most $J$.  So there is an object $(V\hookrightarrow Y)$ of $\diskd(\bsc)_{/Y}$ whose image contains the subset $f\bigl(c(J)\bigr)$.  We see then that the collection of open embeddings
\[
\Bigl\{ \conf_J(f^{-1}V)_{\Sigma_J} \hookrightarrow \conf_J(M)_{\Sigma_I}\mid (V\hookrightarrow Y)\in \diskd(\bsc)_{/Y} \Bigr\}
\]
form an open cover.

Proved in~\cite{aft1} is that open embeddings of basics into $Y$ form a basis for the topology of $Y$.
It follows that the collection of (at most) $|J|$-tuples of disjoint basics in $Y$ form an open cover of $Y$ in such a way that any finite intersection of such is again covered by such.  
It follows that the collection of open embeddings above is an open cover for which any finite intersection of its terms is again covered by terms of the collection.  
In particular, this collection of open embeddings forms a hypercover of $\conf_J(M)_{\Sigma_J}$.
Corollary 1.6 of \cite{Dugger--Isaksen} gives that the map
\[
\underset{(V\hookrightarrow Y)\in \diskd(\bsc)_{/Y}}\colim \conf_J\bigl(f^{-1}V\bigr)_{\Sigma_J} 
~\xra{~\simeq~}~
\conf_J(M)_{\Sigma_J}
\]
is an equivalence of spaces.
This completes the proof. 

\end{proof}

This has the following important corollary, which completes the proof of Theorem \ref{fact-explicit}.

\begin{cor}\label{quittersifted}
For $X$ a $\cB$-manifold, the $\oo$-category $\disk(\cB)_{/X}$ is sifted.
\end{cor}
\begin{proof}

The $\oo$-category $\disk(\cB)_{/X}$ is evidently nonempty, as it contains the object $(\emptyset \hookrightarrow X)$. 
We must then prove that the diagonal functor $\disk(\cB)_{/X} \to \disk(\cB)_{/X}\times \disk(\cB)_{/X}$ is final.
This diagonal functor fits into a diagram among $\infty$-categories
\[
\xymatrix{
\disk_{\nabla} \ar[rr]^-{{\sf ev}_0}  \ar[d]_-{{\sf ev}_1}
&&
\disk(\cB)_{/X\sqcup X}  
\\
\disk(\cB)_{/X}  \ar[rr]^-{\sf diag}
&&
\disk(\cB)_{/X}\times \disk(\cB)_{/X}    \ar[u]^-{\simeq}_{\sqcup}
}
\]
that we now explain.
The upper left $\infty$-category is that of Definition~\ref{def.disk-f} applied to the fold map $\nabla \colon M \sqcup M \to M$; as so, it is equipped with the indicated projection functors.
The right vertical arrow is induced by the symmetric monoidal structure on $\mfld(\cB)$, which is disjoint union.  
This right vertical arrow is an equivalence; an inverse is given by declaring its projection to each factor to be given by intersecting with the corresponding cofactor of the disjoint union.
Therefore, to prove that the diagonal functor is final it is sufficient to prove that both of the projection functors ${\sf ev}_1$ and ${\sf ev}_0$ are final.  
The finality of ${\sf ev}_0$ is Lemma~\ref{final}.

We explain that ${\sf ev}_1$ is final.
Note that the functor $\nabla^{-1} \colon \disk(\cB)_{/X} \to \mfld(\cB)_{/X\sqcup X}$ factors through the full $\infty$-subcategory $\disk(\cB)_{/X\sqcup X}$.  
As so, there is a canonical identification between $\infty$-categories
\[
\disk_\nabla~\simeq~ \disk(\cB)_{/X}\underset{\disk(\cB)_{/X\sqcup X}}\times  {\sf Ar}(\disk(\cB)_{/X\sqcup X})
\]
over $\disk(\cB)_{/X}$.
Through this identification, the composite functor 
\[
\disk(\cB)_{/X} \xra{~\nabla~} \disk(\cB)_{/X\sqcup X} \xra{~\sf const~} {\sf Ar}(\disk(\cB)_{/X\sqcup X})
\]
determines a right adjoint to the functor ${\sf ev}_1$.  
Finality of ${\sf ev}_1$ follows.



\end{proof}

Using Lemma \ref{final}, we can now prove our push-forward formula for factorization homology.

\begin{proof}[Proof of Theorem \ref{:(}] 
After Lemma~\ref{refinement-localize}, we can assume that the \emph{weakly} constructible bundle $f$ is actually constructible.  

The functor \[f_\ast A:\xymatrix{\disk(\bsc)_{/Y}\ar[r]^{f^{-1}}& \disk(\cB)_{/X}\ar[r]^{\int A}& \cV}\] is the left Kan extension of $A:\cX_f\ra \cV$ along the functor ${\sf ev}_1:\cX_f\ra \disk(\bsc)_{/Y}$.
 Therefore there is a natural equivalence \[\colim_{\cX_f} A \simeq \colim_{U\in\disk(\bsc)_{/Y}}\int_{f^{-1}U}A \simeq \int_N f_\ast A~.\] By Lemma \ref{final}, the functor ${\sf ev}_0:\cX_f \ra \disk(\cB)_{/X}$ is final, which implies the equivalence $\colim_{\cX_f} A \simeq \int_MA$, and the result follows.
\end{proof}

In the case of the projection map $X\times Y\ra Y$ off of a product, this result has the following consequence.

\begin{cor}[Fubini]\label{fubini}
Let $\cB_-$ and $\cB_+$ and $\cB$ be $\oo$-categories of basics with a functor $\cB_-\times \cB_+ \to \cB$ over the product functor $\bsc\times\bsc\xra{\times} \bsc$.  
Let $A$ be a $\disk(\cB)$-algebra in $\cV$.  
Let $X$ be a $\cB_-$-manifold, and $Y$ be a $\cB_+$-manifold; so $X\times Y$ is canonically equipped as a $\cB$-manifold.
There is a canonical equivalence in $\cV$:
\[
\int_{X\times Y} A~{}~\simeq~{}~\int_Y \int_X A~.
\]


\end{cor}
