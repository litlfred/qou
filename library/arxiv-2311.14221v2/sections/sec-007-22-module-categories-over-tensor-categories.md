---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-007-22-module-categories-over-tensor-categories
section_title: "Module categories over tensor categories"
section_number: 2.2
pages: 7-9
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.904
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
A  left \emph{module} category over  
$\ca$ is a  category $\Mo$ together with a $\ku$-bilinear 
bifunctor $\rhd: \ca \times \Mo \to \Mo$, exact in each variable,  endowed with 
 natural associativity
and unit isomorphisms 
$$m_{X,Y,M}: (X\otimes Y)\triangleright   M \to X\triangleright  
(Y\triangleright M), \ \ \ell_M: \uno \triangleright  M\to M.$$ 
These isomorphisms are subject to the following conditions: 


\begin{equation}\label{left-modulecat1}
\pentagon
{(X \otimes (Y\otimes Z))\triangleright M }
{\rotatebox{60}{$\sim$}}

{((X \otimes Y)\otimes Z)\triangleright M}
{m_{X\otimes Y, Z, M}}
{(X \otimes Y)\triangleright (Z\triangleright M)}
{m_{X, Y, Z\triangleright M}}
{X \triangleright (Y\triangleright (Z\triangleright M))}

{m_{X, Y\otimes Z, M}}
{X \triangleright ((Y\otimes Z)\triangleright M) }
{\mathrm{id}_{X}\triangleright m_{Y,Z, M}}
\end{equation}





















for any $X, Y, Z\in\C, M\in\Mo$, as well as 
\begin{equation}\label{left-modulecat2} (\id_{X}\triangleright \ell_M)m_{X,{\bf 1} ,M}=\id.
\end{equation} 
Sometimes we shall also say  that $\Mo$ is a $\ca$-\emph{module category} or a representation of $\ca$.

\medbreak


Let $\Mo$ and $\Mo'$ be a pair of $\C$-module categories. A \emph{ module functor} is a pair $(F,c)$, where  $F:\Mo\to\Mo'$  is a functor equipped with natural isomorphisms
$$c_{X,M}: F(X\triangleright M)\to
X\triangleright F(M),$$ 
for $X\in  \ca$, $M\in \Mo$, such that



\begin{equation}\label{modfunctor1}
\pentagon
{F((X\otimes Y)\triangleright M)}
{F(m_{X,Y,M})}
{F(X\triangleright (Y\triangleright M))}
{c_{X,Y\triangleright M}}
{X\triangleright F(Y\triangleright M)}
{\mathrm{id}_X \triangleright  c_{Y,M}}
{X\triangleright (Y\triangleright F(M))}

{c_{X\otimes Y,M}}
{(X\otimes Y)\triangleright F(M)}
{m_{X,Y,F(M)}}
\end{equation}
for any $X, Y\in\ca$, $M\in \Mo$, as well as
\begin{align}\label{modfunctor2}
\ell_{F(M)} \,c_{\uno ,M} &=F(\ell_{M}).
\end{align}

 
Module functors are composable, if $\Mo''$ is a $\ca$-module category and
$(G,d): \Mo' \to \Mo''$ is another module functor then the
composition
\begin{equation}\label{modfunctor-comp}
(G\circ F, e): \Mo \to \Mo'', \qquad  e_{X,M} = d_{X,F(M)}\circ
G(c_{X,M}),
\end{equation} is
also a module functor.

\smallbreak  

A \textit{natural module transformation}, between  module functors $(F,c)$ and $(G,d)$, is a 
 natural transformation $\theta: F \to G$ such
that
\begin{gather}
\label{modf-nat} d_{X,M}\theta_{X\triangleright M} =
(\id_{X}\triangleright \theta_{M})c_{X,M},
\end{gather}
 for any $X\in \ca$, $M\in \Mo$. The vector space of natural module transformations will be denoted by $\Nat_{\!m}(F,G)$. Two module functors $F, G$ are \emph{equivalent} if there exists a natural module isomorphism
$\theta:F \to G$. We denote by $\Fun_{\ca}(\Mo, \Mo')$ the category whose
objects are module functors $(F, c)$ from $\Mo$ to $\Mo'$ and arrows module natural transformations. 

\medbreak
Two $\C$-modules $\Mo$ and $\Mo'$ are {\em equivalent} if there exist module functors $F:\Mo\to
\Mo'$, $G:\Mo'\to \Mo$, and natural module isomorphisms
$\Id_{\Mo'} \to F\circ G$, $\Id_{\Mo} \to G\circ F$.

\medbreak

A module category will be called \textit{strict} if isomorphisms $m$ and $l$ are identities. Any module category is equivalent to a strict one. We will often  assume that the module category is strict without further mention.

\medbreak
 A \emph{right module category} over $\ca$
 is a   category $\Mo$ equipped with an exact
bifunctor $\triangleleft:  \Mo\times  \ca\to \Mo$ and natural   isomorphisms 
$$\widetilde{m}_{M, X,Y}: M\triangleleft (X\ot Y)\to (M\triangleleft X) \triangleleft Y, \quad r_M:M\triangleleft \uno\to M$$ such that



\begin{equation}\label{right-modulecat1} 
\pentagon
{M\triangleleft((X\otimes Y)\otimes Z)}
{\rotatebox{60}{$\sim$}}

{M\triangleleft(X\otimes (Y\otimes Z))}
{\widetilde{m}_{M,X ,Y\ot Z }}
{(M\triangleleft X)\triangleleft (Y\otimes Z)}
{\widetilde{m}_{M\triangleleft X, Y ,Z }}
{((M\triangleleft X)\triangleleft Y)\triangleleft Z)}

{\widetilde{m}_{M,X\ot Y ,Z}}
{(M\triangleleft(X\otimes Y))\triangleleft Z}
{\widetilde{m}_{M,X,Y}\triangleleft \mathrm{id}_Z}
\end{equation}
as well as 
\begin{equation}\label{right-modulecat2} (r_M\triangleleft \id_X)  \widetilde{m}_{M,\uno, X}= \id.
\end{equation}

 

If $\Mo,  \Mo'$ are right $\ca$-modules, a module functor from $\Mo$ to $  \Mo'$ is a pair $(T, d)$ where
$T:\Mo \to \Mo'$ is a  functor and $d_{M,X}:T(M\triangleleft X)\to T(M)\triangleleft X$ are natural  isomorphisms
such that for any $X, Y\in
\ca$, $M\in \Mo$:




\begin{equation}\label{modfunctor11}
\pentagon
{T(M\triangleleft(X\otimes Y))}
{T(\tilde{m}_{M, X, Y})}
{T((M\triangleleft X)\triangleleft Y)}
{d_{M\triangleleft X, Y}}
{T(M\triangleleft X)\triangleleft Y}
{d_{M,X}\triangleleft \id_Y}
{(T(M)\triangleleft X)\triangleleft Y}

{d_{M, X\ot Y}}
{T(M)\triangleleft(X\otimes Y))}
{\tilde{m}_{T(M), X,Y}}
\end{equation}
as well as
\begin{align}\label{modfunctor21}
r_{T(M)} \,d_{ M,\uno} &=T(r_{M}).
\end{align}
