---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-010-31-classical-homology-theories
section_title: "Classical homology theories"
section_number: 3.1
pages: 35-38
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.959
---
Recall from~\S\ref{recollections} the tangent classifier functor
$
\mfld(\cB) \xra{\tau} \Psh(\cB),
$
which is symmetric monoidal with respect to coproduct of presheaves (see Construction~\ref{B-monoidals}).  

To state the next result, for $\cC$ an $\infty$-category we denote the full $\infty$-subcategory $\cC\subset\Psh^{\sf Ind\text{-}fin}(\cC)\subset \Psh(\cC)$ which is the smallest that is closed under the formation of finite colimits and filtered colimits.  
\begin{prop}[\S3.3 of~\cite{aft1}]\label{universal-excision}
The symmetric monoidal functor $\mfld(\cB) \xra{\tau} \Psh(\cB)$ is a homology theory, and it factors through $\Psh^{\sf Ind\text{-}fin}(\cB)$.  

\end{prop}


\begin{cor}
Let $\cV$ be an $\infty$-category that admits pushouts and filtered colimits, which we regard as a symmetric monoidal $\infty$-category whose symmetric monoidal structure is given by coproduct.  
Let $F\colon \Psh^{\sf Ind\text{-}fin}(\cB) \to \cV$ be a symmetric monoidal functor that preserves pushouts and filtered colimits (so $F$ is the left Kan extension of its restriction $F_{|\cB}$).
Then the composition 
\[
F\tau \colon \mfld(\cB) \xra{\tau} \Psh^{\sf Ind\text{-}fin}(\cB) \xra{F} \cV
\]
is a homology theory.  

\end{cor}

\begin{example}
\begin{itemize}
\item[~]

\item The \emph{underlying space} functor $\mfld(\cB) \to \spaces$ is a homology theory -- here, we are equipping the target with the symmetric monoidal structure given by coproduct.  
The restriction of this functor to $\mfld(\cB)^{\sf fin}$ (see \S1.1) factors through $\spaces^{\sf fin}$.  

\item The \emph{underlying space of the `frame bundle'} functor $\mfld(\cB) \to \bigl(\spaces_{/|\cB|}\bigr)$ is a homology theory -- here, we are equipping the target with the symmetric monoidal product given by coproduct.  
Note that the restriction of this functor to $\mfld(\cB)^{\sf fin}$ factors through $\bigl(\spaces_{/|\cB|}\bigr)^{\sf fin}$.  

\item Let $\cV$ be a presentable $\infty$-category.
Consider a functor $E\colon \cB\to \cV$.
Use the same notation $E\colon \Psh(\cB) \to \cV$ for the left Kan extension.  
This left Kan extension preserves coproducts, and therefore defines a symmetric monoidal functor, which we again give the same notation, between their coCartesian symmetric monoidal strutures:
$
E\colon \Psh(\cB)^{\amalg} \longrightarrow \cV^{\amalg}.
$
We obtain a composite symmetric monoidal functor
\[
\mfld(\cB) \xra{\tau} \Psh(\cB)^\amalg \xra{E} \cV^{\amalg}~.
\]
In~\S3.3 of~\cite{aft1} we show that $\tau$ carries collar-gluings to pushouts and sequential open covers to sequential colimits.
Using this, and because this left Kan extension $E$ preserves sifted colimits, this symmetric monoidal functor $E\tau$ is a homology theory. 
\\
Should $\cV$ be equipped with an auxiliary symmetric monoidal structure that distributes over colimits, and should the original functor $E\colon \cB\to \cV$ factor through the full $\infty$-subcategory $\cV^{\sf dual}\subset \cV$ consisting of the dualizable objects, then the restriction of this homology theory $E\tau$ to $\mfld(\cB)^{\sf fin}$ factors through $\cV^{\sf dual}$.  
\begin{itemize}
\item Let $E$ be a spectrum.  The assignment $X\mapsto E\wedge X_+$ depicts a homology theory $\mfld(\cB) \to \spectra$, where the latter is equipped with wedge sum as its symmetric monoidal structure.
Should $E$ be dualizable with respect to smash product, then the restriction of this homology theory to $\mfld(\cB)^{\sf fin}$ factors through $\spectra^{\sf dual}$. 
In particular, the suspension spectrum $\Sigma^\infty_+ X$ of the underlying space of a finitary stratified space $X$ is dualizable.

\item Let $V$ be a chain complex over a commutative ring $\Bbbk$.  
The assignment $X\mapsto \sC_\ast(X;V)$ depicts a homology theory $\mfld(\cB) \to \Ch_\Bbbk$, where the latter is equipped with direct sum as its symmetric monoidal structure.  
Should $V$ be dualizable with respect to tensor products over $\Bbbk$, then the restriction of this homology theory to $\mfld(\cB)^{\sf fin}$ factors through $\Ch_\Bbbk^{\sf dual}$.  
\end{itemize}
\end{itemize}

\end{example}



\subsection{1-point compactifications}

We will make use of the concept of a zero-pointed embedding from \cite{ZP}. There is a $\Kan$-enriched functor 
\[
{\sf ZEmb}\colon \snglr^{\op} \times \snglr^{\op} \longrightarrow \Kan_\ast
\]
to pointed Kan complexes, given as follows.
Its value on $(X,Y)$ is the simplicial set, written as ${\sf ZEmb}(X_+,Y^+)$, for which a $p$-simplex is a diagram of conically smooth open embeddings among submersions over $\Delta^p_e$
\[
X \times \Delta^p_e\xra{~f_X~} W  \xla{~f_Y~} Y \times \Delta^p_e
\]
witnessing an open cover of $W$ -- the simplicial structure maps are evident, and the distinguished point is the case where $W$ is the disjoint union.  
That this simplicial set is a Kan complex as claimed follows from a similar argument for why the simplicial set $\snglr(X,Y)$ is a Kan complex which is explained in~\cite{aft1}; details for ${\sf ZEmb}$ can be found in~\cite{ZP}.  
The action $\snglr(X,X')\times \snglr(Y,Y') \times {\sf ZEmb}(X'_+,{Y'}^+) \to {\sf ZEmb}(X_+,Y^+)$ is given on $p$-simplices as 
\[
\bigl(g,h; (X'\times \Delta^p_e \xra{f_{X'}} W' \xla{f_{Y'}} Y'\times \Delta^p_e)\bigr) \mapsto \bigl(X\times \Delta^p_e \xra{f_{X'}g} f_{X'}(g(X)) \cup f_{Y'}(h(Y)) \xla{f_{Y'}h} Y\times \Delta^p_e\bigr)~,
\]
which is quickly noticed to be compatible with the simplicial structure maps. 
It is manifest that this action is compatible with the composition among conically smooth open embeddings.  
Equipping all stratified spaces present in the definition of the functor $\sf ZEmb$ with a $\cB$-structure, and each map as one of $\cB$-manifolds, enhances $\sf ZEmb$ to a functor
\[
\mfld(\cB)^{\op}\times \mfld(\cB)^{\op} \to \spaces_\ast
\]
to based spaces.  
The restricted adjoint to this functor is the \emph{1-point compactified} tangent classifier
\begin{equation}\label{tau-plus}
\tau^+\colon \bigl(\mfld(\cB)^{\sf fin}\bigr)^{\op} \to \Psh^{\sf fin}_\ast(\cB)~,\qquad X\mapsto \bigl({\sf Entr}(X)^+ \xra{~\tau_{X^+}~} \cB\bigr)~,
\end{equation}
where the target is endowed with the symmetric monoidal structure given by coproduct, written here as right fibrations (details and context can be found in~\cite{ZP}).  

Here is a relative version of the functor $\tau^+$.  
Let $X$ be a $\cB$-manifold.
Let us define the following functor:
\[
\tau^{X^+}\colon \mfldd(\cB)_{/X} \longrightarrow \Psh_\ast(\cB)_{/{\sf Entr}(X^+)}~, \qquad (O\subset X)\mapsto \bigl({\sf Entr}(O_{X^+}) \xra{\tau_{O}^{X^+}} \cB\bigr)~.
\]  
Let $O\subset X$ be an open subspace of the underlying stratified space.
Consider the sub-$\Kan$-enriched functor ${\sf ZEmb}(-_+,O_{X^+}) \subset {\sf ZEmb}(-_+,X^+) \colon \bsc^{\op} \to \Kan$ whose value on $U$ is the sub-simplicial set of ${\sf ZEmb}(U,X)$ consisting of those $U\times \Delta^p_e \xra{f_U}W\xla{f_X} X\times \Delta^p_e$ for which $f_{U} \amalg (f_X)_{|O} \to W$ is an open cover -- easy to check is that this simplicial set is indeed a Kan complex. 
Again, equipping each such $W$ with a $\cB$-structure and each map as one of $\cB$-manifolds, there is the presheaf $\cB^{\op} \to \spaces_\ast$.  
We will use the notation ${\sf Entr}(O_{X^+}) \to \cB$ for the associated right fibration, which is equipped with a section.
The assignment $(O\subset X)\mapsto \bigl({\sf Entr}(O_{X^+}) \xra{\tau_{O}^{X^+}} \cB\bigr)$ depicts the desired functor.
Notice that this functor $\tau^{X^+}$ canonically extends as a map of $\infty$-operads, where the target is equipped with coproduct as its symmetric monoidal structure.  


\begin{lemma}\label{pre-excision}
Let $X\cong X_- \underset{\RR\times X_0}\bigcup X_+$ be a collar-gluing among finitary $\cB$-manifolds. 
Then, in the canonical diagram of pointed presheaves on $\cB$
\[
\xymatrix{
{\sf Entr}\bigl((\RR\times X_0)_{X^+}\bigr)  \ar[r]  \ar[d]
&
{\sf Entr}\bigl((X_+)_{X^+}\bigr)  \ar[r]  \ar[d]
&
{\sf Entr}\bigl((X_+)^+\bigr)  \ar[d]^-=
\\
{\sf Entr}\bigl((X_-)_{X^+}\bigr)  \ar[r]  \ar[d]
&
{\sf Entr}(X^+)  \ar[d]  \ar[r]
&
{\sf Entr}\bigl((X_+)^+\bigr)
\\
{\sf Entr}\bigl((X_-)^+\bigr)  \ar[r]^-=
&
{\sf Entr}\bigl((X_-)^+\bigr) 
&
}
\]
the upper left square is a pushout, and the linear sequences of maps are cofibration sequences.  

\end{lemma}

\begin{proof}
The appearance of $\cB$ is superficial, and so the statement is equivalent to the one with $\cB = \bsc$.  

Because the collar-gluing, written as a constructible bundle $X\xra{f}[-1,1]$, is one among \emph{finitary} stratified spaces, it can be extended, up to non-canonical isotopy, to a collar-gluing $\ov{X} \xra{\w{f}}[-1,1]$ among stratified spaces \emph{with boundary}, with $\ov{X}$ compact.  
By composing $\w{f}$ with the constructible bundle $[-1,1]\to [-1,1]$ determined by declaring its restriction to $(-\frac{1}{2},\frac{1}{2})$ to be an orientation preserving isomorphism onto $(-1,1)$, we can assume that the closure of the image of $\RR\times \ov{X}_0 \hookrightarrow \ov{X}$ intersects $\partial \ov{X}$ as $\RR\times \partial \ov{X}_0$. 

Let $\ov{O}\subset \ov{X}$ be a sub-stratified space with boundary, and choose a collar-neighborhood $[0,1)\times\partial \ov{O}\subset \ov{O}$.
We claim that the canonical morphism of pointed presheaves on $\bsc$
\[
\ast \underset{{\sf Entr}(0,1)\times \partial \ov{O})} \coprod {\sf Entr}(O)\xra{~\simeq~}{\sf Entr}(O_{X^+})
\]
is an equivalence.
This is the case if and only if for each singularity type $[U]$, the likewise map of pointed spaces 
\[
\ast \underset{{\sf Entr}_{[U]}((0,1)\times \partial \ov{O})} \coprod {\sf Entr}_{[U]}(O)\xra{~\simeq~}{\sf Entr}_{[U]}(O_{X^+})
\]
is an equivalence.
Write $U\cong \RR^i\times \sC(Z)$, and use the notation $\ov{U} := [0,1)\times \RR^{i-1}\times \sC(Z)$ for the basic with boundary and $\partial \ov{U} := \RR^{i-1}\times \sC(Z)$ for its boundary.  
Developments of~\cite{aft1} give that the lefthand space in this last expression is canonically identified as the pushout 
\[
\ast \underset{((0,1)\times \partial\ov{O})_{[U]}} \coprod O_{[U]}
\]
in terms the underlying spaces of the $[U]$- and $[\partial \ov{U}]$-strata.
Along the same lines, the righthand pointed space in that expression is canonically identified as the pushout 
\[
\ast \underset{(\partial \ov{O})_{\partial[\ov{U}]}} \coprod \ov{O}_{[U]\leq [\ov{U}]}
\]
in terms of the underlying spaces of the $([U]\leq [\ov{U}])$- and $[\partial \ov{U}]$-strata. 
That the the map of pointed spaces in that expression is an equivalence follows by inspection: $((0,1)\times \partial \ov{O})_{[U]} = \RR\times (\partial \ov{O})_{[\partial \ov{U}]}\simeq (\partial \ov{O})_{[\partial \ov{U}]}$, and the inclusion $O_{[U]} \subset \ov{O}_{[U]\leq [\ov{U}]}$ induces a weak homotopy equivalence of underlying topological spaces.  

Developments in~\cite{aft1} give that each of the two squares of presheaves on $\bsc$
\[
\xymatrix{
{\sf Entr}\bigl(\RR\times X_0\bigr)  \ar[r]  \ar[d]
&
{\sf Entr}\bigl(X_+\bigr)   \ar[d]
\\
{\sf Entr}\bigl(X_-\bigr)  \ar[r]  
&
{\sf Entr}(X)  
}
\]
and
\[
\xymatrix{
{\sf Entr}\bigl(\RR\times (0,1)\times \partial \ov{X}_0\bigr)  \ar[r]  \ar[d]
&
{\sf Entr}\bigl((0,1)\times \partial\ov{X}_+\bigr)   \ar[d]
\\
{\sf Entr}\bigl((0,1)\times \partial \ov{X}_-\bigr)  \ar[r]  
&
{\sf Entr}((0,1)\times \partial \ov{X})  
}
\]
are pushouts. 
The latter maps to the former upon consistent choices of collars of the respective boundaries.  
By taking the levelwise mapping cones of this map of squares, the result follows then from the first paragraph, after observing a standard strata-preserving homeomorphism $(X_-)^+ \cong \bigr(\ov{X}_- \setminus \RR_{>-1}\times \ov{X}_0\bigr)/ \partial$, where $\partial =\bigl( \partial \ov{X}_- \bigcup \{-1\}\times \ov{X}_0\bigr) \setminus \RR_{>-1}\times \ov{X}_0 $, and likewise for $(X_+)^+$.  

\end{proof}
