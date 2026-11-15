---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-012-31-classical-homology-theories
section_title: "Classical homology theories"
section_number: 3.1
pages: 35-36
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.935
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
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
