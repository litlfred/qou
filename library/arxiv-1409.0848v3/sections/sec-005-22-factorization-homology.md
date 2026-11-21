---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-005-22-factorization-homology
section_title: "Factorization homology"
section_number: 2.2
pages: 17-20
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.972
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homology, or topological chiral homology, at the generality of stratiﬁed spaces with tangential"
---
The following is the main definition and object of interest in the present paper, that of factorization homology with coefficients in a disk algebra.

Recall Notation~\ref{slice-convention} for the $\infty$-category of $\disk_n$-algebras.  
\begin{definition}[Factorization homology]\label{def:fact-hmlgy}
Let $\cV$ be a symmetric monoidal $\infty$-category, and let $\cB$ be an $\oo$-category of basics.
The \emph{(absolute) factorization homology} functor is a left adjoint to the restriction
\\









\[
\xymatrix{
\int_-\colon \Alg_{\disk(\cB)}(\cV) \ar@(-,u)@{-->}[rr] 
&&
\Fun^\ot\bigl(\mfld(\cB), \cV\bigr)  ~. \ar[ll]
}
\]
For $X$ a $\cB$-manifold, the \emph{(relative) factorization homology} functor is a left adjoint to the restriction
\\









\[
\xymatrix{
\int_-\colon \Alg_{X}(\cV) \ar@(-,u)@{-->}[rr] 
&&
\Alg_{\mfld(\cB)_{/X}}(\cV)  ~. \ar[ll]
}
\]

\end{definition}

The left adjoint in the previous definition need not exist. The essential result provided in the following is that for a large class of targets $\cV$, factorization homology both exists and has a relatively simple expression, agreeing with the left adjoint at the level of underlying $\oo$-categories; i.e., without remembering the monoidal structures.

\begin{theorem}\label{fact-explicit}
Let $\cV$ be a symmetric monoidal $\infty$-category which is $\ot$-sifted cocomplete, and let $\cB$ be an $\oo$-category of basics.
Then each of the absolute and the relative factorization homology functors exists and each is fully faithful, and each evaluates as
\begin{equation}\label{eq.fact-explicit}
\int_X A~\simeq~ \colim\Bigl(\disk(\cB)_{/X} \to \disk(\cB) \xra{A} \cV\Bigr)~\simeq~\disk(\cB)_{/X}\underset{\disk(\cB)} \bigotimes A
\end{equation}
-- here, all terms are as the underlying $\infty$-categories of the respective $\infty$-operads.

\end{theorem}

We give a proof of this result predicated on several results to come. In Lemma~\ref{shape-existence}, we identify the general formal features for symmetric monoidal and operadic left Kan extension to exist and agree with the underlying left Kan extension. In the following sections, we show that these formal features hold in our example of interest.

\begin{proof}[Proof of Theorem \ref{fact-explicit}]
This is an application of Lemmas~\ref{shape-existence} and \ref{shape-existence-operad}.

To apply this result, we need these three facts:
\begin{itemize}
\item Let $X$ be a $\cB$-manifold.  
Then the slice $\infty$-category $\disk(\cB)_{/X}$ is sifted.
This is Corollary~\ref{quittersifted} to come.

\item 
The functor $\disk(\cB)_{/\uno_{\disk(\cB)}} \to \mfld(\cB)_{/\uno_{\mfld(\cB)}}$ is final.  
In our case, this functor is an equivalence, manifestly.  

\item 
Let $X$ and $X'$ be $\cB$-manifolds.
Then the functor $\disk(\cB)_{/X}\times \disk(\cB)_{/X'} \to \disk(\cB)_{/X\sqcup X'}$ is final.
In our case, this functor is actually an equivalence, by inspection.  

\end{itemize}

\end{proof}

\begin{lemma}\label{shape-existence}
Let $\cV$ be a symmetric monoidal $\infty$-category; let $\iota \colon \cB \to \cM$ be a symmetric monoidal functor with small domain and locally small codomain.
Consider the commutative diagram of solid arrows
\[
\xymatrix{
\Fun^\ot(\cB, \cV)  \ar@{-->}@(-,u)[rr]^-{\iota_\natural^\ot}  \ar[dd]
&&
\Fun^\ot(\cM,\cV)  \ar[ll]^-{\iota^\ast}  \ar[dd]
\\
&&
\\
\Fun(\cB, \cV)  \ar@{-->}@(-,u)[rr]^-{\iota_\natural}  
&&
\Fun(\cM,\cV)  \ar[ll]_-{\iota^\ast} 
}
\]
where $\iota^\ast$ is restriction along $\iota$, and the vertical arrows forget that a given functor was symmetric monoidal. Suppose both:
\begin{itemize}
\item[(1)] the underlying $\infty$-category of $\cV$ admits sifted colimits;
\item[(2)] for each $M\in \cM$, the slice $\infty$-category $\cB_{/M}$ is sifted.
\end{itemize}
Then $\iota^\ast$ has a left adjoint $\iota_\natural$ as indicated, which can be calculated as
\begin{equation}\label{lke-expression-1}
\iota_\natural F \colon M\mapsto \colim\bigl(\cB_{/M} \to \cB \xra{F} \cV\bigr)~\simeq~ \iota^\ast M \underset{\cB} \ot F~.
\end{equation}
The last expression is a coend, and we have identified $M\in \cM$ with its image under the Yoneda functor.
In addition, suppose
\begin{itemize}
\item[(3)] the symmetric monoidal structure for $\cV$ distributes over sifted colimits; 

\item[(4)] the functor between slice $\infty$-categories over units 
\[
\cB_{/\uno_\cB} \to \cB_{/\uno_\cM}
\]
is final; and 

\item[(5)] for each pair of objects $M, M'\in \cM$, the tensor product functor 
\[
\bigotimes \colon \cB_{/M} \times \cB_{/M'}  \longrightarrow \cB_{/M\ot M'}
\]
is final.
\end{itemize}
Then there is a left adjoint $\iota_\natural^\ot$ as indicated, and the downward right square commutes.  
If $\iota$ is fully faithful then so are each of $\iota_\natural$ and $\iota_\natural^\ot$.  

\end{lemma}

\begin{proof}
Conditions (1) and (2) grant that each value of the expression~(\ref{lke-expression-1}) exists.  
Lemma 4.3.2.13 of~\cite{HTT} states that these expressions depict a functor as indicated.
Proposition 4.3.3.7 of~\cite{HTT} states that this functor satisfies the universal property of being a left adjoint to $\iota^\ast$.

We now argue that conditions (3) and (4) grant that, for each symmetric monoidal functor $\cB\xra{F} \cV$, and for each based map among finite sets $I_+ \xra{f} J_+$, the diagram of $\infty$-categories 
\[
\xymatrix{
\cM^I  \ar[d]_-{f_\ast}  \ar[rr]^-{(\iota_\natural F)^I}
&&
\cV^I  \ar[d]^-{f_\ast}
\\
\cM^J  \ar[rr]^-{(\iota_\natural F)^J}
&&
\cV^J
}
\]
commutes.
Each based map $f \colon I_+ \to J_+$ is canonically a composition of a surjective active map $f^{\sf surj}$ followed by an injective active map $f^{\sf inj}$ followed by an \emph{inert} map $f^{\sf inrt}$, and so it is enough to verify commutativity for each such class of maps.
The case of inert maps is obvious, because then $f_\ast$ is projection and $(\iota_\natural F)^I$ is defined as the $I$-fold product of functors.   
The case of injective active maps amounts to verifying that $\iota_\natural F$ sends a symmetric monoidal unit to a symmetric monoidal unit.  This follows from Condition~(4) because $F$ does so.  

The case of surjective active maps follows from the case that $f\colon I_+ \to \ast_+$ is given by $i\mapsto \ast$, so that $f_\ast = \bigotimes^I$ is the $I$-fold tensor product.
Well, because $F$ is symmetric monoidal, there is a canonical arrow
$
\iota_\natural F \circ \bigotimes^I 
\longrightarrow 
\bigotimes^I\circ (\iota_\natural F)^I
$
between functors $\cM^I \to \cV$ that we will argue is an equivalence.
This arrow evaluates on $(M_i)_{i\in I}$ as the horizontal one in the following natural diagram inside $\cV$:
\[
\Small
\xymatrix{
\colim\bigl(\cB_{/\underset{i\in I}\bigotimes M_i} \to \cB\xra{F} \cV \bigr)  \ar[rr]
&&
\underset{i\in I}\bigotimes \colim\bigl(\cB_{/M_i} \to \cB \xra{F} \cV\bigr) 
\\
&
\colim\bigl( \underset{i\in I}\prod \cB_{/M_i} \to \cB^I \xra{F^I} \cV^I\xra{\bigotimes^I} \cV \bigr) \ar[ul]^-{(5)}  \ar[ur]_-{(3)}
&
.
}
\]
The arrow labeled by~(3) is an equivalence precisely because of condition~(3). 
Condition~(5) implies that the functor $\prod_{i\in I} \cB_{/M_i} \to \cB_{/\underset{i\in I}\bigotimes M_i}$ is final, for it is a composition of final functors.
It follows that the arrow labeled by~(5) is an equivalence, after observing the following diagram among $\infty$-categories:
\[
\xymatrix{
\underset{i\in I} \prod \cB_{/M_i}  \ar[rr]^-{\bigotimes^I}  \ar[d]
&&
\cB_{/\underset{i\in I} \bigotimes M_i}  \ar[d]
\\
\cB^I  \ar[rr]^-{\bigotimes^I}  \ar[d]_-{F^I}
&&
\cB  \ar[d]^-F
\\
\cV^I \ar[rr]^-{\bigotimes^I} 
&&
\cV~.
}
\]

\end{proof}

Recall Notation~\ref{slice-convention}.  
We now state a likewise result as Lemma~\ref{shape-existence} for the case of the $\infty$-operads of Notation~\ref{slice-convention}.
The proof of this lemma is the same as that for Lemma~\ref{shape-existence}.  

\begin{lemma}\label{shape-existence-operad}
Let $\cV$ be a symmetric monoidal $\infty$-category.
Let $\iota \colon \cD \to \cM$ be a symmetric monoidal functor between symmetric monoidal $\infty$-categories with $\cD$ small and $\cM$ locally small. 
Suppose both the symmetric monoidal unit for each of $\cD$ and $\cM$ is initial.
Let $X\in \cM$ be an object of the underlying $\infty$-category, and consider the $\infty$-operads $\cD_{/X}$ and $\cM_{/X}$ over $\cD$ and $\cM$, respectively.  
Consider the solid commutative sub-diagram of restriction and forgetful functors
\[
\xymatrix{
\Alg_{\cD_{/X}}(\cV)  \ar@{-->}@(-,u)[rr]^-{\iota_\natural^\ot}  \ar[dd]
&&
\Alg_{\cM_{/X}}(\cV)  \ar[ll]^-{\iota^\ast}  \ar[dd]
\\
&&
\\
\Fun(\cD_{/X}, \cV) \ar@{-->}@(-,u)[rr]^-{\iota_\natural}  
&&
\Fun(\cM_{/X},\cV)  \ar[ll]_-{\iota^\ast} 
}
\]
where the superscript ${}^\ast$ denotes the evident restriction and the vertical arrows restrict to active $\infty$-subcategories.
Suppose both:
\begin{itemize}
\item[(1)] the underlying $\infty$-category of $\cV$ admits sifted colimits;
\item[(2)] for each $Z=(Z\to X)\in \cM_{/X}$, the slice $\infty$-category $(\cD_{/X})_{/Z} \simeq \cD_{/Z}$ is sifted.
\end{itemize}
Then $\iota^\ast$ has a left adjoint $\iota_\natural$ as indicated, which can be calculated as
\begin{equation}\label{lke-expression}
\iota_\natural A \colon (Z\to X) \mapsto \colim\bigl(\cD_{/Z} \to \cD_{/X} \xra{A} \cV\bigr)~\simeq~ \iota^\ast (Z\to X)\underset{\cD_{/X}} \ot A
\end{equation}
-- here in the expression of the coend we identify $(Z\to X)\in \cM$ with its image under the Yoneda functor.
In addition, suppose
\begin{itemize}
\item[(3)] the symmetric monoidal structure for $\cV$ distributes over sifted colimits; 

\item[(4)] the functor between slice $\infty$-categories over units 
\[
\cD_{/\uno_\cD} \to \cM_{/\uno_\cM}
\]
is final; 

\item[(5)] for each pair of objects $(Z\to X), (Z'\to X) \in \cM_{/X}$, the tensor product functor 
\[
\bigotimes \colon \cD_{/Z} \times \cD_{/Z'}  \longrightarrow \cD_{/Z\ot Z'}
\]
is final.
\end{itemize}
Then there is a left adjoint $\iota_\natural^\ot$ as indicated, and the downward right square commutes.  
If $\iota$ is fully faithful then so are each of $\iota_\natural$ and $\iota_\natural^\ot$.  
\end{lemma}
