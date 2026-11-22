---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-002-our-approach
section_title: "Our approach"
section_number: null
pages: 3-5
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.977
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
The point of view of this paper owes a lot to \cite{PS}. However, we shall work only with finite categories. Let $\ku$ be an arbitrary field, and let $\Bc, \vc$ be finite $\ku$-linear abelian categories. Assume both $\ca, \Bc$ are  rigid monoidal categories, and $F:\Bc\to \vc$ is a monoidal functor. If $F$ has a {\it section} $G:\vc\to \Bc$, that is $F\circ G\simeq \Id_\vc$ as monoidal functors, then it is possible to endow $\Bc$ with an action of $\vc$, such that $F$ is a monoidal $\vc$-module functor. This action behaves well together with the monoidal product of $\Bc$, in a sense that we call \textit{monoidal module category}.
 
 
 
  Under these conditions, we aim at constructing a Hopf algebra $H\in \vc$ and obtaining a kind of Radford projection Theorem in this categorical setting.
 
 
 \medbreak
 
The reconstruction of such Hopf algebra is given in some steps, that we describe as follows. If $\Bc$ is a right $\vc$-module category, $F:\Bc\to \vc$ is an exact faithful  module functor, we construct a coalgebra $C(F)\in \vc$ as
 $$ C(F)=\oint^{B\in \Bc} F(B)\ot {}^*F(B).$$
 Here $\oint$ stands for the \emph{relative coend}, a new tool, developed in \cite{BM}, in the context of module categories. This tool is one of the new features that we incorporate in these reconstruction theorems. The coproduct and counit of  $C(F)$ are defined using universal properties of the dinatural transformations associated with the relative coend. See Proposition \ref{coalg-coend}. Moreover, we show that the functor $F$ factorizes as 
\begin{equation*}
\vspace{.1cm}
\xymatrix{
\Bc\;\;
\ar[rr]^-{\widehat{F}}
\ar[dr]_-{F}
&&
{}^C\vc
\ar[dl]^-{\uc}\ar@{}[d]|{}&\\
&\vc.&
}
\end{equation*} 
Here $f:{}^C\vc\to \vc $ is the forgetful functor, and $\widehat{F}: \Bc\to {}^C\vc$ is an equivalence of $\vc$-module categories. The existence of $\widehat{F}$ is stated in Proposition \ref{factorization-F}, and the proof that it is an equivalence of categories is given in Theorem \ref{recons-th}. 


If in addition $\vc$ is a braided rigid monoidal  $\vc$-module category,  $\Bc$ is a rigid monoidal category, and $F$ is a monoidal functor, then we endow the coalgebra $C(F)$ with a product, turning it into a bialgebra in $\vc$. Rigidity of $\Bc$ allows to define an antipode on $C(F)$, making it into a braided Hopf algebra. These results are stated in Theorem \ref{hopf-rec} and Corrollary \ref{antipode-reconstruct}.

\medbreak 

The contents of the paper are the following. In Section \ref{Section:tensor-categories} we give a brief account of some basic facts about tensor categories and module categories that will be used throughout the paper. In Section \ref{Section:mcoends} we review the notion of  \emph{relative (co)end} of a functor  in the setting of module categories over a tensor category $\ca$. This tool was developed by the second author in \cite{BM} as generalization of the usual (co)end. 
Let $\ca$ be a tensor category, $\Mo$ be a left $\vc$-module category and $\Ac$ is some target category. If a functor 
$S:\Mo^{\op}\times \Mo\to \Ac$ has a \textit{prebalancing}, that is natural isomorphisms
$$\beta^X_{M,N}: S(M,X\triangleright N)\to S(X^*\triangleright M,N),$$
then the relative coend 
$$\oint^{M\in \Mo} (S,\beta)$$
is an object in $ \Ac$ equipped with dinatural transformations $\pi_M:S(M,M)\xrightarrow{ . .} \oint^{M\in \Mo} (S,\beta)$, such that it satisfies some extra condition, see for example \eqref{dinat:coen:module:left}, and it is universal with this property. When $\ca=\vect_\ku$, the relative (co)end coincides with the usual (co)end. 

\medbreak

Since relative (co)ends are objects defined by a universal property, they may not exist in general. Section \ref{Section_coendExists} is devoted to prove that all relative coends, used in this work, actually exist. In this Section, it is crucial that all categories, the tensor category $\vc$ and the module category $\Mo$ are finite. We also require that the action $ \vc\times \Mo\to \Mo$ is exact in each variable, allowing us to use \cite[Thm 2.24]{DSS}, that says that there is an equivalence of module categories $\Mo\simeq \vc_A$, for some algebra $A\in \vc.$

\medbreak

In Section \ref{Section_Hopf} we review the definition of a Hopf algebra $H$ in a braided tensor category $\vc$ and its tensor category of comodules ${^H}\vc$. We also review the definition of $H$-$H$-Yetter Drinfeld modules in this setting, which produces a braided tensor category ${^H_H}\YD(\vc)$. Then we introduce a notion of a $\vc$-module category $\Bc$ with a compatible tensor structure in the sense that there is a natural isomorphism 
$$l_{X,B}: X \triangleright B\xrightarrow{\;\simeq\; } (X\triangleright \uno_\Bc)\ot B,$$
for all $X\in\vc,\,B\in\Bc$, satisfying certain axioms. Note that there is a second reasonable notion of a monoidal module category, where the action $X\triangleright-$ is a monoidal functor, and this definition is not equivalent. Under the presence of a monoidal  functor $F:\Bc\to \ca$, compatibility of the monoidal product in $\Bc$ and the action of $\vc$ on $\Bc$, is equivalent to the existence of a section to $F$, that is a monoidal functor $G:\vc\to \Bc$ such that there is a monoidal natural isomorphism $F\circ G\simeq \Id.$
