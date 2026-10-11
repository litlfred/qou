---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-004-5-decomposition-theorem-of-the-tensor-product-of
section_title: "Decomposition Theorem of the Tensor Product of Principal Representations and Askey-Wilson Polynomials"
section_number: 5
pages: 22-25
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.982
---
## Decomposition Theorem of the Tensor Product of Principal Representations

Let us now prove that, chosing $N^{{}_{(X_0X_1)\;(Y_0Y_1)}}_{\;\;\;{}_{(Z_0Z_1)}}\!\!=({\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}})^{1/2}\!>0$, ${\hat \Phi}[X_0X_1,Y_0Y_1]$ is an isometry.

::: theorem
[]{#isometrytheorem label="isometrytheorem"} ${\hat \Phi}[X_0X_1,Y_0Y_1]: V(X_0X_1)\otimes V(Y_0Y_1) \rightarrow   
\int^{\oplus}d(Z_0Z_1)H(Z_0Z_1)$ is an isometry. This is a direct consequence of the following identity: $$\forall C\in \onehalf \ZZ^{+},   
\int d{\cal P}(Z_0Z_1)\Entrela{A'}{B'}{C}{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}=\delta_{A,A'}\delta_{B,B'}Y^{(1)}_{(A,X_0-X_1)}Y^{(1)}_{(B,Y_0-Y_1)}.  
\label{completeness}$$
:::

$V(X_0X_1)\otimes V(Y_0Y_1)$ is a ${\mathfrak U}_q(su(2))$ module, let us denote by $( V(X_0X_1)\otimes V(Y_0Y_1))^{[C]}$ its isotypic component of spin $C$. From the definition of ${\hat \Phi}[X_0X_1,Y_0Y_1]$ and the choice $N=({\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}})^{1/2},$ it is simple to show that the restriction of ${\hat \Phi}[X_0X_1,Y_0Y_1]$ to $( V(X_0X_1)\otimes V(Y_0Y_1))^{[C]}$ is an isometry if and only if $(\ref{completeness})$ is satisfied for this $C.$ We already proved that $\Entrela{A'}{B'}{C}{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}$ is a piecewise continuous function of $\rho_Z$, as a result it is integrable, and using formula ([\[form3lambda\]](#form3lambda){reference-type="ref" reference="form3lambda"}) and the uniform convergence properties of this series, we can invert the integral and the sum: $$\begin{aligned}
&&\hskip -2cm\mbox{lefthandside of} \;\;(\ref{completeness})=\nonumber\\ 
&&\hskip -2cm=\!\!\!\sum_{KLMN}\!\!\frac{\qd{N}\qd{K}}{\qd{C}^2}\Lambda^{KL}_{A'A}(X_0X_1)\Lambda^{KM}_{B'B}(Y_0Y_1)\int d{\cal P}(Z_0Z_1)\Lambda^{KN}_{A'A}(Z_1Z_0)\times\nonumber\\  
&&\hskip 2cm\times\sixjn{B}{N}{L}{K}{A}{C}{0}\!\!\sixjn{K}{N}{C}{A'}{B'}{M}{0}\!\!\sixjn{A'}{N}{M}{B}{K}{L}{0} \nonumber 
\end{aligned}$$ Using the Plancherel formula ([\[intlambda\]](#intlambda){reference-type="ref" reference="intlambda"}), we obtain that this series is equal to: $$\begin{aligned}
&&\hskip -1cm=\delta_{A,A'}\delta_{B,B'}\Lambda^{0A}_{AA}(X_0X_1)\Lambda^{0B}_{BB}(Y_0Y_1)\sixjn{B}{C}{A}{0}{A}{C}{0}\!\!\sixjn{0}{C}{C}{A}{B}{B}{0}\!\!\sixjn{A}{C}{B}{B}{0}{A}{0}=\nonumber\\  
&&\hskip -1cm=\mbox{righthandside of} \;\;(\ref{completeness})\nonumber.  
\end{aligned}$$

${\hat \Phi}[X_0X_1,Y_0Y_1]$ being an isometry from $V(X_0X_1)\otimes V(Y_0Y_1)$ to the Hilbert space $\int^{\oplus}d(Z_0Z_1)H(Z_0Z_1)$, there exists a unique isometry $\Phi^{\#}[X_0X_1,Y_0Y_1]$ from the tensor product of Hilbert space $H(X_0X_1)\otimes H(Y_0Y_1)$ to $\int^{\oplus}d(Z_0Z_1)H(Z_0Z_1)$ which restriction to $V(X_0X_1)\otimes V(Y_0Y_1)$ gives back ${\hat \Phi}[X_0X_1,Y_0Y_1].$

::: theorem
$\Phi^{\#}[X_0X_1,Y_0Y_1]:  H(X_0X_1)\otimes H(Y_0Y_1) \rightarrow   
\int^{\oplus}d(Z_0Z_1)H(Z_0Z_1)$ is an invertible isometry of Hilbert space.
:::

It is trivial that $\Phi^{\#}[X_0X_1,Y_0Y_1]$ is an isometry, as a result it is injective. We therefore have only to show that $\Phi^{\#}[X_0X_1,Y_0Y_1]$ is surjective. The proof goes along the same lines as the proof of the surjectivity of the Fourier transform in [@BR1]. It is sufficient to show that $E=\Phi^{\#}[X_0X_1,Y_0Y_1](V(X_0X_1)\otimes V(Y_0Y_1))$ is dense in $\int^{\oplus}d(Z_0Z_1)H(Z_0Z_1),$ which is equivalent to show that $E^{\perp}=\{0\}.$ Let $f\in \int^{\oplus}d(Z_0Z_1)H(Z_0Z_1),$ and assume that $<f, \Phi[X_0X_1,Y_0Y_1](\ontop{A}{e}_i(X_0X_1)\otimes  
\ontop{B}{e}_j(Y_0Y_1))>=0, \forall A,B,i,j.$ This in particular implies that $$<f, \Phi[X_0X_1,Y_0Y_1](\Delta(a)(\ontop{A}{e}_i(X_0X_1)\otimes 
\ontop{B}{e}_j(Y_0Y_1)))>=0$$ for any element $a$ in the center of ${\mathfrak U}_q(sl(2,\CC))_{\RR}.$ As a result, by taking $a=\Omega_+^{p}\Omega_-^{r}$ and using the property that $\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}$ is an intertwiner, we get the identity: $\forall p,r\in \NN, \forall A,B,C\in \onehalf \ZZ^{+}, \forall k=-C,..,C$ $$\int d(Z_0Z_1) <f\vert \ontop{C}{e}_k(Z_0Z_1)> 
\omega_+(Z_0Z_1)^p\omega_-(Z_0Z_1)^r 
 g(X_0X_1,Y_0,Y_1,Z_0,Z_1)=0,\label{centerorthogonality}$$ where $g(X_0X_1,Y_0,Y_1,Z_0,Z_1)= 
\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1} N^{{}_{(X_0X_1)\;(Y_0Y_1)}}_{\;\;\;{}_{(Z_0Z_1)}}.$ $\vert g\vert^2$ being a continuous function in $\rho_Z,$ $<f\vert \ontop{C}{e}_k> g$ is an $L^2$ function in the variable $\rho_Z.$ We can now apply the argument of the proof of Plancherel Formula in [@BR1]and conclude that the set of equations ([\[centerorthogonality\]](#centerorthogonality){reference-type="ref" reference="centerorthogonality"}) for all $p,r$ implies that $<f\vert \ontop{C}{e}_k> g=0$ as a $L^2$ function. From theorem 1, we can always find for every $C$, a couple $A,B$ such that $g\not=0$. From the explicit form of $g$ we know that the zeroes of $g$ considered as a $\rho_Z$ function are finite, we obtain that $<f\vert \ontop{C}{e}_k>=0,$ which implies $f=0.$

## R-matrix in the Tensor Product of Infinite dimensional Representations

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
