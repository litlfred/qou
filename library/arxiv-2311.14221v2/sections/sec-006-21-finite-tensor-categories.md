---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-006-21-finite-tensor-categories
section_title: "Finite tensor categories"
section_number: 2.1
pages: 6-7
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.892
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
A  finite tensor category $\ca$ is a monoidal rigid category, with simple unit object $\uno\in \ca$. We refer to \cite{EO} for more details on finite tensor categories. Without loss of generality, we shall assume that tensor categories in this work are strict. 

\medbreak


If $\ca, \Do$ are monoidal categories, a monoidal functor is a functor $F:\ca\to \Do$ equipped with natural isomorphisms
$$\xi_{A,B}:F(A)\ot F(B)\to F(A\ot B), $$
such that
\begin{equation}\label{monoidal-functor}
\xi_{A,B\ot C} (\id_{F(A)}\ot \xi_{B,C})=\xi_{A\ot B, C} (\xi_{A,B}\ot \id_{F(C)}). 
\end{equation}
If $(F,\xi), (\widetilde{F}, \widetilde{\xi}):\ca\to \Do$ are two monoidal functors, a monoidal \textit{natural transformation} between $F$ and $\widetilde{F}$ is a natural transformation $\alpha:F\to \widetilde{F}$ such that
\begin{equation}\label{natural-monoidal}
\alpha_{A\ot B} \xi_{A,B}=\widetilde{\xi}_{A,B} (\alpha_A\ot \alpha_B),
\end{equation}
for any $A,B\in \ca$.
\medbreak

If $\ca$ is a category, for any $X\in \ca$ we shall denote by 
$$ \ev_X:X^*\ot X\to \uno, \quad \coev_X:\uno\to X\ot X^*$$
the evaluation and coevaluation. By abuse of notation, we shall also denote by
$$\ev_X:X\ot {}^*X\to \uno,  \quad \coev_X:\uno\to  {}^*X\ot X$$
the evaluation and coevaluation for the left duals. We will use the following basic result.
If $f:X\to Y$ is an isomorphism in $\ca$ then
\begin{align}\label{duality-iso} \begin{split} (\id_{ {}^*X}\ot f )\coev_X=& ({}^*f\ot \id_Y )\coev_Y,\\
\ev_Y (f\ot  \id_Y)=&\ev_X (\id_X\ot {}^*f).
\end{split}
\end{align}
 It is well known that for any pair of objects $X, Y\in \ca$ there are canonical natural isomorphisms
\begin{equation}\label{duals-product-r}
 \phi^r_{X,Y}: Y^* \ot X^* \to(X\ot Y)^*,
\end{equation} 
\begin{equation}\label{duals-product-l}
 \phi^l_{X,Y}: {}^*Y \ot {}^*X \to {}^*(X\ot Y).
\end{equation} 
These isomorphisms allow us to compute coevaluation and evaluation maps of duals; more precisely we shall need the following identity
\begin{equation}\label{coev-of-dual} \ev_{{}^*V}=  {}^*(\coev_X) \phi^l_{{}^*X,X}.
\end{equation} 

We are going to make use, very often, of the canonical natural isomorphisms
\begin{align}\label{duals1}\begin{split} \psi^Z_{X,Y}:\Hom_\Bc(X\ot {}^*Y,Z)\to \Hom_\Bc(X,Z\ot Y),\\
\psi^Z_{X,Y}(f)=(f\ot\id_Y)(\id_X\ot \coev_Y).
\end{split}
\end{align}
And its inverse
\begin{align}\label{duals2}\begin{split} \bar{\psi}^Z_{X,Y}:\Hom_\Bc(X,Z\ot Y)\to \Hom_\Bc(X\ot {}^*Y,Z)\\
\bar{\psi}^Z_{X,Y}(g)=(\id_Z\ot\ev_Y)(g\ot\id_{{}^*Y}).\end{split}
\end{align}

We shall also need the following basic fact.
\begin{lema} For any pair $V,W\in \ca$ the evaluation of $V\ot W$ is given by
\begin{equation}\label{evaluation-tensor-prod} \ev_{V\ot W} = \ev_V(\id_V\ot \ev_W\ot \id_{{}^*V})(\id_{V\ot W} \ot (\phi^l_{V,W})^{-1}).\qed
\end{equation}
\end{lema}
