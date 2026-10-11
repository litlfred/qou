---
doc_id: arxiv-math-9910147v1
doc_title: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗"
section_id: sec-046-52-r-matrix-in-the-tensor-product-of-inﬁnite-dim
section_title: "R-matrix in the Tensor Product of Inﬁnite dimensional Re presen-"
section_number: 5.2
pages: 24-26
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
doc_brief: "Tensor Products of Principal Unitary Representations of Quantum Lorentz Group and Askey-Wilson Polynomials E. Buffenoir ∗ — We study the tensor product of principal unitary representa tions of the"
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.987
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

## Connection with Askey-Wilson Polynomials.

In the sequel, we will show that we can reexpress $N^{{}_{(X_0X_1)\;(Y_0Y_1)}}_{\;\;\;{}_{(Z_0Z_1)}}\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}$ in terms of q-Racah polynomials and Askey-Wilson polynomials, and that the relation ([\[completeness\]](#completeness){reference-type="ref" reference="completeness"}) is an orthogonality property mixing q-Racah polynomials and Askey-Wilson polynomials in a non trivial way.

::: lemma
The following three identities are satisfied: $$\begin{aligned}
&&\hskip -1.5cm 1)\;\;\;\overline{\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}}=\psi_2\ElemRed{A}{B}{C}{\underline{X_1}\underline{X_0}}{\underline{Y_1}\underline{Y_0}}{\underline{Z_1}\underline{Z_0}}\nonumber\\  
&&\hskip -1.5cm 2)\;\;\;\ElemRed{A}{B}{C}{\underline{X_1}\underline{X_0}}{\underline{Y_1}\underline{Y_0}}{\underline{Z_1}\underline{Z_0}}=\psi_3\ElemRed{A}{B}{C}{X_1X_0}{Y_1Y_0}{Z_1Z_0}\nonumber\\ 
&&\hskip -1.5cm 3)\;\;\;\ElemRed{A}{B}{C}{X_1X_0}{Y_1Y_0}{Z_1Z_0}=e^{-i\pi B}\sqrt{[d_B]}\;  
\sum_{X_2}\sixjn{Y_0}{X_0}{Z_0}{T}{Z_1}{X_2}{3}\!\!  
\sixjn{X_1}{X_0}{A}{C}{B}{X_2}{1}\times\nonumber\\  
&&\hskip 5cm\times\sixjn{Z_1}{X_2}{Y_0}{B}{Y_1}{X_1}{3}\!\!  
\frac{v^{1/4}_{A}v^{1/2}_{X_2}}{v^{1/4}_{B}v^{1/4}_{C}v^{1/4}_{X_0}v^{1/4}_{X_1}}  
\end{aligned}$$ where $\psi_2=e^{i \pi (B+C+m_X+A)}$, and $\psi_3$ is such that $$\begin{aligned}
&&\psi_1 \psi_2 \psi_3=e^{i \pi (m_X+m_Y-m_Z)}\varphi_{(2X_1+1,-1)}\varphi_{(2Y_1+1,-1)}\varphi_{(2Z_1+1,-1)}\nonumber 
\end{aligned}$$
:::

The identity $1)$ follows from a very simple computation. The identity $2)$ follows from the use of propositions ([\[propsym6j1\]](#propsym6j1){reference-type="ref" reference="propsym6j1"}) and ([\[propsym6j3\]](#propsym6j3){reference-type="ref" reference="propsym6j3"}). Identity $3)$ is a direct consequence of a Racah and a pentagonal equation on $6j(3)$ symbols.

Using these identities theorem ([\[isometrytheorem\]](#isometrytheorem){reference-type="ref" reference="isometrytheorem"}) can be reformulated as follows

::: proposition
[]{#askeyproof label="askeyproof"} $$\begin{aligned}
&&\hskip -1cm\int \!d(Z_0Z_1)\Gamma^{\!{}_{(X_0X_1)(Y_0Y_1)}}_{\;\;\;{}_{(Z_0Z_1)}}\!\sixjn{Y_0}{X_0}{Z_0}{A}{Z_1}{X_2}{3}\!\!\sixjn{Y_0}{X_0}{Z_0}{A}{Z_1}{X_3}{3}\!\!\sixjn{Z_1}{X_2}{Y_0}{B}{Y_1}{X_1}{3}\!\!\sixjn{Z_1}{X_3}{Y_0}{C}{Y_1}{X_1}{3}\!\!=\nonumber\\   
&&=\delta_{X_2,X_3}\delta_{B,C}Y^{(1)}_{(A,X_0-X_2)}Y^{(1)}_{(B,X_1-X_3)}Y^{(1)}_{(B,Y_0-Y_1)}\label{O3}.  
\end{aligned}$$ with $$\begin{aligned}
&&\Gamma^{\!{}_{(X_0X_1)(Y_0Y_1)}}_{\;\;{}_{(Z_0Z_1)}}=  
\frac{q^{2Z_0-2 Z_1+2Y_0-2 Y_1}(1)_{\infty}^2(1-q^2)[d_B]}{(2X_1\!+\!1)_1(2Y_0\!+\!1)_1(2Z_0\!+\!1)_1}\times\nonumber\\ 
&&\times \frac{\xi(2X_1\!+\!1,2Y_1\!+\!1,2Z_1\!+\!1)} 
{\xi(Y_1\!+\!X_1\!-\!Z_1\!+\!1,X_1\!+\!Z_1\!-\!Y_1\!+\!1,Y_1\!+\!Z_1\!-\!X_1\!+\!1,X_1\!+\!Y_1\!+\!Z_1\!+\!2)} 
\end{aligned}$$
:::

Straightforward using a Racah-Wigner symmetry on $6j(3)$ and an orthogonality relation on $6j(1)$ symbols.

::: theorem
Using the notations ([\[defaskeypol\]](#defaskeypol){reference-type="ref" reference="defaskeypol"}) we have $$\begin{aligned}
&&\hskip -1cm\sqrt{{\cal P}(Z_0Z_1)}\sqrt{\Gamma^{\!{}_{(X_0X_1)(Y_0Y_1)}}_{\;\;{}_{(Z_0Z_1)}}}\sixjn{Z_1}{X_2}{Y_0}{B}{Y_1}{X_1}{3}\!\!\!= \!\sqrt{\hbar}  
\sqrt{\frac{w^{(AW)}(z;a,b,c,d)}{h^{(AW)}_n(a,b,c,d)}}p^{(AW)}_n(\tau(z);a,b,c,d) \label{expressionaskey} 
\end{aligned}$$ with $n=B+Y_0-Y_1, a=q^{2X_1+2Y_1+3}, b=q^{2Y_1-2X_1+1}, c=q^{2X_2-2Y_0+1}, d=q^{-2Y_0-2X_2-1}, 2z=2 Z_1+1.$
:::

Using two Sears transformations we can turn the parameters of the hypergeometric functions of the left handside into those of the right handside. Checking now the identity ([\[expressionaskey\]](#expressionaskey){reference-type="ref" reference="expressionaskey"}) is therefore reduced to straightforward but tedious manipulations on $\nu_{\infty}$ functions.

Note that the relation ([\[O3\]](#O3){reference-type="ref" reference="O3"}) when $A=0$ reduces to the identity: $$\int d\rho_Z \;{\cal P}(0,\rho_Z)\;\Gamma^{(X_0X_1)\;(Y_0Y_1)}_{(Z_0Z_0)} \sixjn{Z_0}{X_0}{Y_0}{B}{Y_1}{X_1}{3}\sixjn{Z_0}{X_0}{Y_0}{C}{Y_1}{X_1}{3}=\delta_{B,C}$$ which is exactly, using ([\[expressionaskey\]](#expressionaskey){reference-type="ref" reference="expressionaskey"}), the orthogonality condition on Askey-Wilson polynomials for the family of parameters $n=B+Y_0-Y_1, a=q^{2X_1+2Y_1+3}, b=q^{2Y_1-2X_1+1}, c=q^{2X_0-2Y_0+1}, d=q^{-2Y_0-2X_0-1}, 2z=2 Z_0+1.$

Although one would suspect that the relation ([\[O3\]](#O3){reference-type="ref" reference="O3"}) can be proved for any $A$ by disentangling the sum over $m_Z$ and the integration over $\rho_Z,$ we have not been able to prove it in this way.
