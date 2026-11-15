---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-008-52-r-matrix-in-the-tensor-product-of-infinite-di
section_title: "R-matrix in the Tensor Product of Infinite dimensional Representations"
section_number: 5.2
pages: 24-25
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
In this section we will compute the $R$-matrix in the tensor product of two irreducible infinite dimensional representations $({\buildrel {_{(X_0X_1)}}\over \Pi}\otimes  
 {\buildrel {_{(Y_0Y_1)}}\over \Pi})$. We will in particular show that the expression of $({\buildrel {_{(X_0X_1)}}\over \Pi}\otimes  
 {\buildrel {_{(Y_0 Y_1)}}\over \Pi})({\cal R})$ is an operator which domain contains all the vectors of the form ${\buildrel A\over e}_m(X_0X_1)\otimes {\buildrel B\over e}_n(Y_0Y_1)$, and more precisely we have the following proposition:

::: proposition
The expression of the $R$ matrix of $\mathfrak{U}_{q}(sl(2,\mathbb{C})_{\RR})$ represented on ${\buildrel {_{(X_0X_1)}}\over V}\otimes {\buildrel {_{(Y_0Y_1)}}\over V}$ is given by the following action: $$({\buildrel {_{(X_0X_1)}}\over \Pi}\otimes  {\buildrel {_{(Y_0Y_1)}}\over \Pi})({\cal R}) 
({\buildrel B\over e}_m \otimes {\buildrel C\over e}_n)= 
\sum_{DF}{\buildrel B\over e}_j\otimes {\buildrel F\over e}_p 
\Clebphi{F}{B}{D}{p}{j}{x}\Clebpsi{B}{C}{D}{m}{n}{x} \coefclambda{B}{D}{F}{C}{X_0}{X_1}.$$ In particular this expression is a finite sum although the universal formula for ${\cal R}$ is an infinite sum.
:::

The element ${\buildrel A\over L}$ are multipliers of ${\tilde \mathfrak{U}}{}_{q}(sl(2,\mathbb{C})_{\mathbb{R}})$ and we have the trivial relation ${\buildrel A\over L}{}^{(\pm)}{}^i_j= 
\sum_{B}^{\oplus}{\buildrel {AB}\over R}{}^{ik}_{jl} {\buildrel B\over X}{}^l_k.$ The $R$ matrix of ${\mathfrak U}_q(sl(2,\CC)_{\RR})$ is written as: ${\cal R}=\sum_{A}{\buildrel A\over X}{}^i_j\otimes 1\otimes 1\otimes {\buildrel A\over g}{}^j_i.$ From the expression of a representation $\tilde{\Pi}$ of ${\tilde \mathfrak{U}}{}_{q}(sl(2,\mathbb{C})_{\mathbb{R}})$, associated to $(X_0,X_1)$ a straightforward computation of the representation of the R-matrix gives the formula of the statement.

Remark. This situation is in sharp contrast with the case of $SU_{q}(1,1)$ for $q$ real. The structure of Hopf algebra on $\mathfrak{U}_{q}(su(1,1))$ is the same as $\mathfrak{U}_{q}(su(2)),$ the only difference is in the definition of the star structure: $J_z^{\star}=J_z, J_+^{\star}=-J_-,J_-^{\star}=-J_+.$ It is easy to classify the irreducible unitary representations, the principal unitary representation of $\mathfrak{U}(su(1,1))$ being now easily quantized as follows: $$\begin{aligned}
&&\hskip -1cmJ_z.e_m=m e_m\;\;\;\;\;\;J_+.e_m=[m-\tau+\epsilon]e_{m+1}\;\;\;\;\;\;J_-.e_m=-[m+\tau+\epsilon]e_{m+1}\nonumber 
\end{aligned}$$ where as usual $\epsilon\in\{0,\onehalf\}, \tau=i\nu-\onehalf, \nu\in \mathbb{R},$ and $e_m$ is an orthonormal basis of the representation. The universal $R$ matrix is still formally defined by $R=q^{2 J_z \otimes J_z}e_{q^{-1}}^{(q-q^{-1})\;(q^{J_z}J_+ \otimes J_-q^{-J_z})}.$ It is easy to see that $(\pi\otimes \pi')(R)(e_m\otimes e_n')$ has no meaning in the $l^2$ sense except in the trivial case where $q=1.$ Indeed a straightforward computation shows that a formal expansion of $(\pi\otimes \pi')(R)(e_m\otimes e_n')$ gives $(\pi\otimes \pi')(R)(e_m\otimes e_n')=\sum_{p=0}^{+\infty}a_{p}(e_{m+p}\otimes e_{n-p}')$ with $a_{p}\sim (q-q^{-1})\gamma q^{-2p^2+\alpha p+\beta}$ for $0<q<1$ with $\gamma\not=0.$
