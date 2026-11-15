---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-008-23-the-internal-hom
section_title: "The internal Hom"
section_number: 2.3
pages: 9-10
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.894
latex_coverage_ratio: 0.865
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
\label{subsection:internal-hom} Let $\ca$ be a  tensor category and $\Mo$ be  a left $\C$-module category. For any pair of objects $M, N\in\Mo$, the \emph{internal Hom} is an object $\uhom(M,N)\in \C$ representing the left exact functor $$\Hom_{\Mo}(-\triangleright M,N):\ca^{\op}\to \vect_\ku.$$ This means that, there are natural isomorphisms
$$\Hom_{\ca}(X,\uhom_\Mo(M,N))\simeq \Hom_{\Mo}(X\triangleright M,N).$$
The internal Hom for right $\ca$-module categories is defined similarly.

\medbreak


The next technical result will be needed later. Recall natural isomorphisms $\phi^l$ defined in \eqref{duals-product-l}. 

 

\begin{lema} Let $\Mo$ be a  right $\ca$-module category with action given by $\triangleleft: \Mo\times \ca\to \Mo$. If $(F,c):\Mo\to \ca$ is a module functor, then, for any $B\in \Mo$, $X\in \ca$, the following diagrams commute. 
\begin{equation}\label{evaluation-mod}
\begin{tikzcd}[column sep=-1em]

&
(F(B)\ot X)\ot {^*}(F(B) \ot X) 
\ar{dr}{\mathrm{id}\otimes (\phi^l_{F(B),X})^{-1}}
&

\\
F(B\triangleleft X)\ot {^*}F(B \triangleleft X) 
\ar{ru}{c_{B,X}\ot {^*}c_{B,X}^{-1}}
\arrow[swap]{dr}{\mathrm{ev}_{F(B\triangleleft X )}}
&

&
(F(B)\ot X)\ot ({^*}X\ot {^*}F(B)) 
\ar{dl}{\mathrm{ev}_{F(B)}(\mathrm{id}\ot \mathrm{ev}_X\ot \mathrm{id})}
&
\\

&
\uno
&

\end{tikzcd}
\end{equation}






\begin{equation}\label{coevaluation-mod}
\begin{tikzcd}[column sep=-1em]

&
({^*}X\ot {^*}F(B)) \ot (F(B)\ot X)
\arrow[swap]{dl}{{^*}c_{B,X} \ot c^{-1}_{B,X}}
&

\\
{^*}F(B \triangleleft X)\otimes F(B\triangleleft X) 
&

&
{^*}(X\ot F(B)) \ot (F(B)\ot X)
\arrow[swap]{ul}{\phi^l_{F(B),X}\otimes \mathrm{id}}
&
\\

&
\uno
\arrow{ul}{\mathrm{coev}_{F(B\triangleleft X )}}
\arrow[swap]{ur}{(\mathrm{id}\ot \mathrm{coev}_{F(B)}\ot\mathrm{id}) \mathrm{coev}_X }
&

\end{tikzcd}
\end{equation}
\end{lema} 
\pf The proof follows, by simply checking that morphisms
$$\ev_{F(B\triangleleft X )} = \ev_{F(B)}\big(\id\ot \ev_X\ot \id \big)\big(c_{B,X}\ot ( {}^*c_{B,X}\phi^l_{F(B),X})^{-1}\big), $$
$$\coev_{F(B\triangleleft X )}= \big( {}^*c_{B,X}\phi^l_{F(B),X} \ot c^{-1}_{B,X}\big)\big(\id\ot \coev_{F(B)}\ot\id\big) \coev_X,$$
satisfy rigidity axioms.
\epf
