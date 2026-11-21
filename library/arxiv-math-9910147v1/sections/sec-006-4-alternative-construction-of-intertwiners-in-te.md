---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-006-4-alternative-construction-of-intertwiners-in-te
section_title: "Alternative Construction of Intertwiners in terms of the Quantum Haar Measure"
section_number: 4
pages: 17-22
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.976
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
Let us define the linear map ${\hat \Phi}[X_0X_1,Y_0Y_1]:V(X_0X_1)\otimes V(Y_0Y_1)\rightarrow \int^{\oplus} d(Z_0Z_1)H(Z_0Z_1)$ where $\forall w\in  V(X_0X_1)\otimes V(Y_0Y_1)  
,{\hat \Phi}[X_0X_1,Y_0Y_1](w)$ is the family of functions defined by

${\hat \Phi}[X_0X_1,Y_0Y_1](w)(Z_0Z_1)=N^{{}_{(X_0X_1)\;(Y_0Y_1)}}_{\;\;\;{}_{(Z_0Z_1)}}\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}(w),$ and $N^{{}_{(X_0X_1)\;(Y_0Y_1)}}_{\;\;\;{}_{(Z_0Z_1)}}$ are complex numbers depending on $X_0, X_1, Y_0, Y_1, Z_0, Z_1.$

We want to find $N$ such that ${\hat \Phi}[X_0X_1,Y_0Y_1]$ is an isometry. As explained in the introduction, this is a delicate problem which requires another description of the space of intertwiners, where this isometry property is a direct consequence of Plancherel theorem.

::: theorem
Let $l\in V(X_0X_1), l'\in V(Y_0Y_1), v''\in V(Z_0Z_1)$, the following operator is well defined, and is an intertwiner of $\mathfrak{U}_q(sl(2,\CC)_{\RR})$ module: $$\begin{aligned}
&&\hskip -1cm \Upsilon_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']:V(X_0X_1)\otimes V(Y_0Y_1)\rightarrow V(Z_0Z_1),\nonumber\\  
&&\hskip -1cm\Upsilon_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']= \sum_{IJK} {{\buildrel {\!\!{}_{(Z_0Z_1)}} \over {\Pi}}}(u^{K})\dagger \vert v''>  <l\otimes l'\vert{\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}  (u^I) \otimes {\buildrel {\!\!{}_{(Y_0Y_1)}} \over {\Pi}}(u^J)  
 \;h(u_Iu_Ju_K).  
\end{aligned}$$

Its matrix elements satisfy the relation: $$\begin{aligned}
&&\hskip -4.5cm \sum_{IJK}{\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}\!{}^{A',i'}_{A,i}\!(u^I){\buildrel {\!\!{}_{(Y_0Y_1)}} \over {\Pi}}\!{}^{B',j'}_{B,j}\!(u^J){\buildrel {\!\!{}_{(Z_0Z_1)}} \over {\Pi}}\!{}^{\dagger}{}^{C,k}_{C',k'}(u^K)\;\;h(u_Iu_Ju_K)=\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\hskip 3.5cm =\sum_{v}\Clebpsi{A}{B}{C}{i}{j}{k}{\buildrel C \over \mu}  
{}_{k'}^{v}\!\Clebphi{A'}{B'}{C'}{i'}{j'}{v}\!\!\Entrela{A'}{B'}{C'}{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}  
\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1.5cm\mbox{with}\Entrela{A'}{B'}{C'}{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}\!\!=\!\!\!\sum_{KLMN}\frac{\qd{N}\qd{K}}{\qd{C}\qd{C'}}\Lambda^{KL}_{A'A}(X_0X_1)\Lambda^{KM}_{B'B}(Y_0Y_1)\Lambda^{KN}_{C'C}(Z_1Z_0)\times  
\nonumber\\  
&&\hskip 5cm\times\sixjn{B}{N}{L}{K}{A}{C}{0}\!\!\sixjn{K}{N}{C'}{A'}{B'}{M}{0}\!\!\sixjn{A'}{N}{M}{B}{K}{L}{0}\label{form3lambda}.  
\end{aligned}$$ This infinite series converges absolutely and uniformly in $\rho_X,\rho_Y,\rho_Z.$ Its square is a continuous function of $\rho_X,\rho_Y,\rho_Z.$
:::

We will use the convention of summation of repeated up and low small indices. $$\begin{aligned}
&&\hskip -3.5cm \sum_{IJK}{\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}\!{}^{A',i'}_{A,i}\!(u^I){\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}\!{}^{B',j'}_{B,j}\!(u^J){\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}\!{}^{\dagger}{}^{C,k}_{C',k'}(u^K)\;h(u_Iu_Ju_K)\;=\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -0.5cm=\!\!\!\!\!\!\!\!\sum_{KLK'MK''N}\!\!\!\!\!\!\!\! \Lambda^{KL}_{A'A}(X_0X_1)  
\Clebphi{A'}{K}{L}{r}{s}{t}\!\Clebpsi{K}{A}{L}{u}{i}{t}  
\Lambda^{K'M}_{B'B}(Y_0Y_1)  
\Clebphi{B'}{K'}{M}{a}{b}{c}\!\Clebpsi{K'}{B}{M}{d}{j}{c}\!\!  
\times \nonumber\\  
&&\hskip -0.5cm\times   
\Lambda^{K''N}_{C'C}(Z_1Z_0) \Clebpsi{C'}{K''}{N}{m}{p}{n}\!\Clebphi{K''}{C}{N}{l}{k}{n}  
{\buildrel {C'} \over w}{}_{qk'}({\buildrel {C'} \over w}{}^{-1})^{mo}  
h(\kE{A'}{i'}{r}{K}{u}{s}\;  
 \kE{B'}{j'}{a}{K'}{d}{b} \;\kE{C'}{q}{o}{K''}{p}{l})\nonumber  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -0.5cm=\!\!\!\sum_{KLMN} \!\!\!\frac{e^{2i \pi K}\qd{K}}{\qd{C'}}  
\Lambda^{KL}_{A'A}(X_0X_1)\Lambda^{KM}_{B'B}(Y_0Y_1)\Lambda^{KN}_{C'C}(Z_1Z_0)  
\Clebphi{A'}{K}{L}{r}{s}{t}\!\Clebpsi{K}{A}{L}{u}{i}{t}\!\!  
\Clebphi{B'}{K}{M}{a}{p}{c}\nonumber\\  
&&\hskip -0.5cm\times  
\Clebpsi{K}{B}{M}{s}{j}{c}\!\!  
 \Clebpsi{C'}{K}{N}{m}{p}{n}\!\Clebphi{K}{C}{N}{l}{k}{n}  
\Clebpsi{A'}{B'}{C'}{r}{a}{m} ({\buildrel {K} \over \mu}{}^{-1})^{u}_{l}  
\Clebphi{A'}{B'}{C'}{i'}{j'}{v}{\buildrel {C'} \over \mu}{}_{k'}^{v}\nonumber  
\end{aligned}$$ after the use of formulae ([\[haar\]](#haar){reference-type="ref" reference="haar"}) and ([\[normaclebsch\]](#normaclebsch){reference-type="ref" reference="normaclebsch"}) $$\begin{aligned}
&&\hskip -0.5cm=\!\!\!\sum_{KLMN} \!\!\!\frac{e^{2i \pi K}\qd{K}}{\qd{C'}}  
\Lambda^{KL}_{A'A}(X_0X_1)\Lambda^{KM}_{B'B}(Y_0Y_1)\Lambda^{KN}_{C'C}(Z_1Z_0)  
\sixjn{K}{N}{C'}{A'}{B'}{M}{0}  
\Clebphi{A'}{K}{L}{r}{s}{t}\!  
\nonumber\\  
&&\hskip -0.5cm\times \Clebpsi{K}{A}{L}{u}{i}{t}\!\! \Clebpsi{A'}{M}{N}{r}{c}{n}  
\!\!\Clebpsi{K}{B}{M}{s}{j}{c}\!\!  
 \!\Clebphi{K}{C}{N}{l}{k}{n}  
 ({\buildrel {K} \over \mu}{}^{-1})^{u}_{l}  
\Clebphi{A'}{B'}{C'}{i'}{j'}{v}{\buildrel {C'} \over \mu}{}_{k'}^{v}\nonumber  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -0.5cm=\!\!\!\sum_{KLMN} \!\!\!\frac{e^{2i \pi K}\qd{K}}{\qd{C'}}  
\Lambda^{KL}_{A'A}(X_0X_1)\Lambda^{KM}_{B'B}(Y_0Y_1)\Lambda^{KN}_{C'C}(Z_1Z_0)  
\sixjn{K}{N}{C'}{A'}{B'}{M}{0}  
\sixjn{A'}{N}{M}{B}{K}{L}{0}  
\nonumber\\  
&&\hskip -0.5cm\times \Clebpsi{K}{A}{L}{u}{i}{t}\!\!   
\Clebpsi{L}{B}{N}{t}{j}{n}  
 \!\Clebphi{K}{C}{N}{l}{k}{n}  
 ({\buildrel {K} \over \mu}{}^{-1})^{u}_{l}  
\Clebphi{A'}{B'}{C'}{i'}{j'}{v}{\buildrel {C'} \over \mu}{}_{k'}^{v}\nonumber  
\end{aligned}$$ after having used twice the formula ([\[vertexIRF\]](#vertexIRF){reference-type="ref" reference="vertexIRF"}) $$\begin{aligned}
&&\hskip -0.5cm=\!\!\!\sum_{KLMN} \!\!\!\frac{e^{2i \pi K}\qd{K}}{\qd{C'}}  
\Lambda^{KL}_{A'A}(X_0X_1)\Lambda^{KM}_{B'B}(Y_0Y_1)\Lambda^{KN}_{C'C}(Z_1Z_0)  
\sixjn{K}{N}{C'}{A'}{B'}{M}{0}  
\sixjn{A'}{N}{M}{B}{K}{L}{0}  
\nonumber\\  
&&\hskip -0.5cm\times \frac{e^{2i \pi (N-C)}\qd{N}}{\qd{C}}  
\Clebphi{K}{L}{A}{l}{t}{i}\Clebpsi{L}{B}{N}{t}{j}{n}\!\Clebpsi{K}{N}{C}{l}{n}{k}  
 ({\buildrel {K} \over \mu}{}^{-1})^{u}_{l}  
\Clebphi{A'}{B'}{C'}{i'}{j'}{v}{\buildrel {C'} \over \mu}{}_{k'}^{v}\nonumber\\  
&&\hskip -0.5cm= \mbox{righthandside of (\ref{form3lambda})},\nonumber  
\end{aligned}$$ where we have used formulae ([\[contra\]](#contra){reference-type="ref" reference="contra"}) and ([\[vertexIRF\]](#vertexIRF){reference-type="ref" reference="vertexIRF"}) to conclude.

This proof holds true as soon as we have shown that these series are absolutely convergent. Proof of the convergence of the last series can be obtained using asymptotic properties of coefficients $\Lambda^{BC}_{AD},$ as well as asymptotic properties of $6j(0)$. Indeed, using the selection rules of $6j(0),$ we know that in the four sums $$\begin{aligned}
&&\sum_{Klmn}\frac{\qd{K+n}\qd{K}}{\qd{C}\qd{C'}}\Lambda^{K\;K+l}_{A'A}(X_0X_1)\Lambda^{K\;K+m}_{B'B}(Y_0Y_1)\Lambda^{K\;K+n}_{C'C}(Z_1Z_0)\times  
\nonumber\\  
&&\hskip 1cm\times\sixjn{B}{K+n}{K+l}{K}{A}{C}{0}\!\!\sixjn{K}{K+n}{C'}{A'}{B'}{K+m}{0}\!\!\sixjn{A'}{K+n}{K+m}{B}{K}{K+l}{0},  
\end{aligned}$$ for a fixed $K,$ the range of the sum over $l,m,n$ is finite and fixed by $\vert l \vert \leq {\rm min}(A,A'),\vert m \vert \leq {\rm min}(B,B'), \vert n \vert \leq {\rm min}(C,C'),\vert l-n \vert \leq B, \vert n-m \vert \leq A'.$ Thus, in order to show the absolute convergence of this series, it is sufficient to bound the general term in $K$ by a geometric series. This can be proved using the behaviour of the coefficients $\Lambda^{KK+l}_{AD}$ when $K$ is large, derived in the appendix. Precisely, using ([\[asymptlambda1\]](#asymptlambda1){reference-type="ref" reference="asymptlambda1"}) and ([\[asymptot1\]](#asymptot1){reference-type="ref" reference="asymptot1"})([\[asymptot2\]](#asymptot2){reference-type="ref" reference="asymptot2"}), we have the following property: $\forall l,m,n,A,B,C,A',B',C' \in \onehalf \ZZ,$ there exist $Q,Q' \in \RR,$ such that $\forall \rho_X, \rho_Y, \rho_Z \in ]-\frac{\pi}{\hbar},\frac{\pi}{\hbar}]$ : $$\begin{aligned}
&&\hskip -1cm\forall K,\left\vert  \frac{\qd{K+n}\qd{K}}{\qd{C}\qd{C'}}\Lambda^{K\;K+l}_{A'A}(X_0X_1)\Lambda^{K\;K+m}_{B'B}(Y_0Y_1)\Lambda^{K\;K+n}_{C'C}(Z_1Z_0) \right\vert \; \leq \; Q K^3 q^{2K}  
\nonumber\\  
&&\hskip -1cm\forall K,\left\vert  \sixjn{B}{K+n}{K+l}{K}{A}{C}{0}\!\!\sixjn{K}{K+n}{C'}{A'}{B'}{K+m}{0}\!\!\sixjn{A'}{K+n}{K+m}{B}{K}{K+l}{0} \right\vert \; \leq \; Q'.  
\end{aligned}$$ The series is therefore absolutely convergent and uniformly convergent in $\rho_X ,\rho_Y,\rho_Z.$ From this last result and using the property that ${\cal N}^{(A)}(q^{2X_1+1},m_X){\cal N}^{(D)}(q^{2X_1+1},m_X)^{-1}\Lambda^{BC}_{AD}(X_0X_1)$ is a continuous functions of $\rho_X,$ the square of the matrix coefficients of the operator $\Upsilon_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}$ are continuous functions of the three variables $\rho_X, \rho_Y, \rho_Z.$ Note that in the case where $A=A', B=B', C=C'$ the expression ([\[form3lambda\]](#form3lambda){reference-type="ref" reference="form3lambda"}) is itself a continuous function of $\rho_X, \rho_Y, \rho_Z.$

We still have to show that the linear map $\Upsilon_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']$ is an intertwiner. We have $$\begin{aligned}
&&\Upsilon_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']=\nonumber\\  
&& =\sum_{IJK} {{\buildrel {\!\!{}_{(Z_0Z_1)}} \over {\Pi}}}(u^{K})\dagger \vert v''>  <l\otimes l'\vert{\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}  (u^I) \otimes {\buildrel {\!\!{}_{(Y_0Y_1)}} \over {\Pi}}(u^J)  
 \;h(u_Iu_Ju_K)\nonumber\\  
&&= \sum_{IJK} {{\buildrel {\!\!{}_{(Z_0Z_1)}} \over {\Pi}}}(S^{-1}(u^{K})) \vert v''> <l\otimes l'\vert{\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}  (u^I) \otimes {\buildrel {\!\!{}_{(Y_0Y_1)}} \over {\Pi}}(u^J)\;h(u_Iu_Ju_K)\nonumber  
\end{aligned}$$ Using the identity verified by any Haar measure on a co-quasitriangular Hopf algebra $A$ [@Wo1; @C] $$\begin{aligned}
h(ab)=\sum_{(a)}h(ba_{(2)})<\mu,a_{(1)}><\mu,a_{(3)}>, \;\;\;\forall a,b \in A,   
\end{aligned}$$ and simple transformations using properties of the antipode and of the group-like element $\mu$, we obtain that $\Upsilon_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']$ is related to the operator: $$\begin{aligned}
&& \Xi_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']:V(X_0X_1)\otimes V(Y_0Y_1)\rightarrow V(Z_0Z_1),\\  
&&\Xi_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']= \sum_{IJK} {{\buildrel {\!\!{}_{(Z_0Z_1)}} \over {\Pi}}}(S(u^{K})\mu) \vert v''>  <l\otimes l'\vert{\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}  (u^I) \otimes {\buildrel {\!\!{}_{(Y_0Y_1)}} \over {\Pi}}(u^J)  
 \;h(u_Ku_Iu_J),\nonumber  
\end{aligned}$$ as follows:

$\Upsilon_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']=  
\sum_{C,r}\Xi_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';{\buildrel {C} \over e}_r]  
<{\buildrel {C} \over \mu}{\buildrel {C} \over e}_r, v''>.$

As a result it is equivalent to show that $\Xi_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']$ is an intertwiner operator. This is a simple consequence of the absolute convergence of the series and of the right invariance of the Haar measure.

The following proposition gives the link between intertwiners constructed using the Haar measure and the reduced elements.

::: proposition
There exists a real number ${\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}$ such that $$\begin{aligned}
&&\hskip -0.6cm\Entrela{A'}{B'}{C'}{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}=   
{\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}  
\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1} \; \overline{\ElemRed{A'}{B'}{C'}{X_0X_1}{Y_0Y_1}{Z_0Z_1}}.  
\label{mainformula}  
\end{aligned}$$
:::

The operator $\Xi_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']$ being an intertwiner,the theorem 1 ensures the existence of a complex number $\lambda (l,l';v'')$ such that: $\Xi_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']=\lambda (l,l';v'')  
\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}.$ We will denote $\Pi={\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}, \Pi'={\buildrel {\!\!{}_{(Y_0Y_1)}} \over {\Pi}},\Pi''={\buildrel {\!\!{}_{(Z_0Z_1)}} \over {\Pi}}$ and we have the following sequence of equalities: $$\begin{aligned}
&&\hskip -0.6cm \overline{\lambda(l, l';v'')}\;\;\overline{<l''\vert \Phi^{\Pi \;\Pi'}_{\;\;\Pi''} \vert v \otimes v'>}=\nonumber\\  
&&\hskip -0.6cm=\sum_{IJK}<v''\vert\Pi''((S(e^I)\mu)^*)\vert l''><v\otimes v' \vert \Pi(e^J{}^*) \otimes \Pi'(e^K{}^*)\vert l\otimes l'> \overline{h(e_Ie_Je_K)}=\nonumber\\  
&&\hskip -0.6cm=\sum_{IJK}<v''\vert\Pi''(\mu S^{-1}(e^I{}^*))\vert l''><v\otimes v' \vert \Pi(e^J{}^*) \otimes \Pi'(e^K{}^*)\vert l\otimes l'> h(e^*_Ke^*_Je^*_I)=\nonumber\\  
&&\hskip -0.6cm=\sum_{IJK}<v''\vert\Pi''(\mu S^{-1}(e^I))\vert l''><v\otimes v' \vert \Pi(e^J) \otimes \Pi'(e^K)\vert l\otimes l'> h(S^{-1}(e_K)S^{-1}(e_J)S^{-1}(e_I))=\nonumber\\  
&&\hskip -0.6cm=\sum_{IJK}<v''\vert\Pi''(S(e^I)\mu)\vert l''><v\otimes v' \vert \Pi(e^J) \otimes \Pi'(e^K)\vert l\otimes l'> h(e_Ie_Je_K)=\nonumber\\  
&&\hskip -0.6cm= \lambda(v, v';l'')\;<v'' \vert \Phi^{\Pi \;\Pi'}_{\;\;\Pi''} \vert l \otimes l'>.\nonumber  
\end{aligned}$$ As a result $$\begin{aligned}
\lambda(v, v';l'')= {\cal M}_{\;\;\Pi''}^{\Pi \;\Pi'} \; {\overline { <l''\vert \Phi^{\Pi \;\Pi'}_{\;\;\Pi''} \vert v \otimes v'>}},\nonumber  
\end{aligned}$$ from which we get $$\begin{aligned}
&&\hskip -1cm\sum_{IJK} <l''\vert  {\Pi''}(S(e^{I})\mu) \vert v''> <l\vert \Pi(e^J)\vert v>  
 <l'\vert \Pi'(e^K)\vert v'> \;h(e_Ie_Je_K)=\nonumber\\  
&&\hskip 1cm= {\cal M}_{\;\;\Pi''}^{\Pi \;\Pi'}  
 <l''\vert \Phi^{\Pi \;\Pi'}_{\;\;\Pi''} \vert v \otimes v'> \overline{<v'' \vert \Phi^{\Pi \;\Pi'}_{\;\;\Pi''} \vert l \otimes l'>}.  
\end{aligned}$$ Using the relation between the operator $\Xi_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']$ and $\Upsilon_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}[l,l';v'']$ we obtain the announced result.

In order to make a precise connection, later on, between matrix elements of ${\hat \Phi}[X_0X_1,Y_0Y_1]$ and Askey-Wilson polynomials we need an explicit formula for ${\cal M}.$

::: proposition
The normalization factor ${\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}$ is a positive number and is given by the following expression: $$\begin{aligned}
&&\hskip -1cm{\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}=  
\vert\frac{ q^{2(X_0-X_1+Y_0-Y_1+Z_0-Z_1)}(1-q^2)(1)^2_{\infty}  
}{\nu_1(2X_0\!+\!1)^2\nu_1(2Y_0\!+\!1)^2\nu_1(2Z_0\!+\!1)^2}\vert \times\nonumber\\  
&&\hskip 0.8cm\times\frac{\vert \xi(2X_1\!+\!1)\xi(2Y_1\!+\!1)\xi(2Z_1\!+\!1)\vert   
}{\vert \xi(X_1\!+\!Y_1\!-\!Z_1\!+\!1)\xi(X_1\!-\!Y_1\!+\!Z_1\!+\!1)\xi(Y_1\!+\!Z_1\!-\!X_1+\!1)\xi(X_1\!+\!Y_1\!+\!Z_1+\!2)\vert }  \label{Mformula} 
\end{aligned}$$ where we have defined the function $\xi$, by $\xi(z)=(z)_{\infty}(1-z)_{\infty}.$
:::

We will identify certain asymptotics of the lefthandside and the righthandside of ([\[mainformula\]](#mainformula){reference-type="ref" reference="mainformula"}) in order to compute the normalization ${\cal M}_{\;\;\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}.$ Let us first find the behaviour of $$\begin{aligned}
&&\hskip -1cm f(T)=\Entrela{P+T}{P}{T}{P+T}{P}{T}{X_0X_1}{Y_0Y_1}{Z_0Z_1}\;\;\;\; \mbox{when}\;\;T \rightarrow +\infty, \;\;P=Y_0-Y_1 >0.  
\end{aligned}$$

It can be seen from the properties ([\[asymptot1\]](#asymptot1){reference-type="ref" reference="asymptot1"})([\[asymptot2\]](#asymptot2){reference-type="ref" reference="asymptot2"})([\[asymptlambda2\]](#asymptlambda2){reference-type="ref" reference="asymptlambda2"}), that the unique leading term in the explicit expression : $$\begin{aligned}
&&\hskip -1cm f(T)=  
\sum_{KlMn}\frac{\qd{T+n}\qd{K}}{\qd{T}^2}\Lambda^{K\;P+T+l}_{P+T}(X_0X_1)  
\Lambda^{K\;M}_{\;\;P}(Y_0Y_1)\Lambda^{K\;T+n}_{\;\;T}(Z_1Z_0)\!\times  
\nonumber\\  
&&\times\sixjn{P}{T\!+\!n}{P\!+\!T\!+\!l}{K}{P\!+\!T}{T}{0}\!\!\sixjn{P\!+\!T}{T\!+\!n}{M}{K}{P}{T}{0}  
\!\!\sixjn{P\!+\!T}{T\!+\!n}{M}{P}{K}{P\!+\!T\!+\!l}{0},\nonumber  
\end{aligned}$$ is the term corresponding to $l=n=0.$ The behaviour when $T \rightarrow +\infty$ of $f(T)$ is therefore given by $$\begin{aligned}
f(T) \sim q^{2T} (1-q^2)\sum_{KM} \qd{K}\Clebpsi{K}{\;P}{\;M}{0}{-P}{-P}\Clebphi{\;P}{K}{\;M}{-P}{0}{-P} \Lambda^{K\;M}_{\;\;P}(Y_0Y_1).\nonumber  
\end{aligned}$$ The series in the right handside can be exactly computed using the formula ([\[formsumlambda\]](#formsumlambda){reference-type="ref" reference="formsumlambda"}) proved in the appendix. We finally obtain, for $P=Y_0-Y_1 >0:$ $$\begin{aligned}
\Entrela{P+T}{P}{T}{P+T}{P}{T}{X_0X_1}{Y_0Y_1}{Z_0Z_1} \sim_{{}_{T \rightarrow +\infty}} q^{2T} (1-q^2) \frac{\hbar \qd{\vert Y_0-Y_1\vert }}{2\pi {\cal P}(Y_0Y_1)}.  
\end{aligned}$$ From the fact that the righthandside of the last expression is positive, and that the right handside of ([\[mainformula\]](#mainformula){reference-type="ref" reference="mainformula"}) is in this situation a modulus square we obtain that ${\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}$ is a positive number. Let us now compute the behaviour of the righthandside of ([\[mainformula\]](#mainformula){reference-type="ref" reference="mainformula"}) for $T \rightarrow +\infty, P=m_Y$ (this computation has been done for $0 \leq m_Y,$ but for $m_Y < 0$ a similar proof can be done). In the appendix, we have proved the following result: $$\begin{aligned}
&&\hskip -0.8cm\ElemRed{$\!\!\!T\!+\!Y_0\!\!-\!\!Y_1$}{$\!\!Y_0\!\!-\!\!Y_1$}{T}{X_0X_1}{Y_0Y_1}{Z_0Z_1}  
 {\sim}\;  
e^{-i \pi 2T}q^{-T(Y_0+Y_1)}\;e^{i \pi (\frac{X_0-X_1}{2})}   
q^{-Z_0Z_1}\sqrt{\qd{Y_0-Y_1}}\!\!\times\nonumber\\ 
&&\hskip -0.5cm\times \nu_1(2X_1\!+\!1)\nu_1(2Z_0\!+\!1)   
\frac{\varphi_{(2X_0,P\!+\!T\!+\!X_0\!-\!X_1)}\varphi_{(Z_1\!+\!X_1\!-\!Y_1,Z_1\!-\!Z_0\!+\!X_1\!-\!X_0\!+\!Y_0\!-\!Y_1)}}{\varphi_{(Z_0\!+\!Z_1,T)}}  
\times\nonumber\\  
&&\hskip -0.5cm\times \;  
\frac{\nu_{\infty}(Y_0\!+\!X_0\!-\!Z_0\!+\!1)  
\nu_{\infty}(Y_0\!+\!X_0\!+\!Z_0\!+\!2)\nu_{\infty}(Y_0\!-\!X_0\!-\!Z_0)  
\nu_{\infty}(Y_0\!+\!Z_0\!-\!X_0\!+\!1)}{  
q^{\frac{3}{2}X_0^2+\onehalf X_0-\onehalf Z_0^2+\onehalf Z_0}  
(1)_{\infty}  
\nu_{\infty}(2Y_1\!+\!1)\nu_{\infty}(2Y_0\!+\!1)}\times\nonumber\\  
&&\hskip -0.5cm\times \;  
\frac{\nu_{\infty}(Y_1\!+\!X_1\!-\!Z_1\!+\!1)\nu_{\infty}(Y_1\!+\!X_1\!+\!Z_1\!+\!2)  
\nu_{\infty}(Y_1\!-\!X_1\!-\!Z_1)\nu_{\infty}(Y_1\!+\!Z_1\!-\!X_1\!+\!1)}{  
q^{-\frac{3}{2}X_1^2-\onehalf X_1-\onehalf Z_1^2 -\onehalf Z_1}  
\nu_{\infty}(2X_0\!+\!1)  
\nu_{\infty}(-\!2X_0)\nu_{\infty}(Z_0\!+\!Z_1+1)\nu_{\infty}(-\!Z_0\!-\!Z_1)}.  
\end{aligned}$$ From ([\[mainformula\]](#mainformula){reference-type="ref" reference="mainformula"}), and after elementary algebraic relations on q-factorials, we finally get the announced expression for ${\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}$.

The formula $(\ref{mainformula})$ is an identity where the left hansdside is a complicated series, and the right handside is the infinite product (${\cal M}$), multiplied by square roots of rational fractions. Let us give an example of this formula in its simplest case, which is achieved when $A=A'=B=B'=C=C'=0.$ We necessarily have $m_X=m_Y=m_Z=0,$ i.e $X_0=X_1, Y_0=Y_1, Z_0=Z_1.$ In this case we can compute ${\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}$ directly. Indeed: $$\Entrela{0}{0}{0}{0}{0}{0}{X_0X_1}{Y_0Y_1}{Z_0Z_1}=  
\sum_{B}[d_B]^2 \Lambda^{BB}_{0}(X_0X_1) \Lambda^{BB}_{0}(Y_0Y_1)\Lambda^{BB}_{0}(Z_0Z_1)\label{Sommem0}.$$ Using the identity $\Lambda^{BB}_{0}(X_0X_0)=\frac{[(2X_0+1)(2B+1)]}{[2X_0+1][2B+1]},$ the formula (Exercice 12 of [@WW]) $$4\sum_{n=1}^{+\infty}q^{n}\frac{sin(2nz)}{1-q^{2n}}=  
\frac{\theta'_{4}(z,\tau)}{\theta_4(z,\tau)}$$ where $q=e^{-\hbar}=e^{i\pi\tau}$, and the Jacobi's fundamental formulae ([@WW] 21.22): $$2\theta_4(x')\theta_4(y')\theta_4(z')\theta_4(w')= 
\sum_{j=1}^4(-1)^{\delta_{j,2}}\theta_j(x)\theta_j(y)\theta_j(z)\theta_j(w)$$ where $2w'=-w+x+y+z$ (and circular permutation to define x',y',z'), we obtain that the series ([\[Sommem0\]](#Sommem0){reference-type="ref" reference="Sommem0"}) is equal to:

$$\frac{(1-q^2)q^{-3/4}(1)_{\infty}^3\theta_1(2\lambda_x)\theta_1(2\lambda_y)\theta_1(2\lambda_z)(sin(2\lambda_x)sin(2\lambda_y)sin(2\lambda_z))^{-1}}  
{8\theta_4(\lambda_x+\lambda_y+\lambda_z)\theta_4(-\lambda_x+\lambda_y+\lambda_z)\theta_4(\lambda_x-\lambda_y+\lambda_z)  
\theta_4(\lambda_x+\lambda_y-\lambda_z)}\label{Mtheta}$$ where we have chosen $2X_0+1=i\frac{4\lambda_x}{\hbar}, 2Y_0+1=i\frac{4\lambda_y}{\hbar},   
2Z_0+1=i\frac{4\lambda_z}{\hbar},$ and $\theta_j, (j=1,..4)$ are the usual Theta functions, as defined in [@WW]. Note that this expression is exactly the coefficient ${\cal M}_{\;\;{}_{(Z_0Z_0)}}^{{}_{(X_0X_0)}{}_{(Y_0Y_0)}},$ once we have expressed the Theta functions in term of infinite products. However such a simple derivation of ${\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}},$ does not generalize so easily to the case where $m_X, m_Y, m_Z$ are non zero.\
Formula ([\[Mtheta\]](#Mtheta){reference-type="ref" reference="Mtheta"}) is the quantum deformation of a formula first found in [@ARRW].

Remark: We will need in the next section the following identity, which can be easily proved using $(\ref{Mformula})$. ${\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}},$ can also be written as: $$\begin{aligned}
&&\hskip -0.6cm {\cal M}_{\;\;{}_{(Z_0Z_1)}}^{{}_{(X_0X_1)}{}_{(Y_0Y_1)}}= 
\psi_1\times 
 \frac{q^{Z_0-3 Z_1+Y_0-3 Y_1+X_0-3 X_1-3}(1)_{\infty}^2(1-q^2)}{\nu_1(2X_0\!+\!1)\nu_1(-2X_1\!-\!1)\nu_1(2Y_0\!+\!1) 
\nu_1(-2Y_1\!-\!1)\nu_1(2Z_0\!+\!1)\nu_1(-2Z_1\!-\!1)}\times\nonumber\\ 
&&\times \frac{\xi(2X_1\!+\!1,2Y_1\!+\!1,2Z_1\!+\!1)}{\xi(Y_1\!+\!X_1\!-\!Z_1\!+\!1,X_1\!+\!Z_1\!-\!Y_1\!+\!1,Y_1\!+\!Z_1\!-\!X_1\!+\!1,X_1\!+\!Y_1\!+\!Z_1\!+\!2)}\label{Mformula2} 
\end{aligned}$$ where we have denoted $\xi(a_1,\cdots, a_n)=\prod_{k=1}^{n}\xi(a_k)$ and where $\psi_1$ is the fourth root of unit given by: $$\begin{aligned}
&&\hskip -0.6cm \psi_1=\frac{\varphi_{(2Y_1,2Y_1-2Y_0-1)}\times (\mbox {\small cycl. perm. on}\;\; X,Y,Z))}{\varphi_{(Y_1\!+\!X_1\!-\!Z_1\!+\!1, Y_1\!-\!Y_0\!+\!X_1\!-\!X_0\!-\!Z_0\!+\!Z_1)}\times (\mbox{\small cycl. perm. on}\;\; X,Y,Z)\times \varphi_{(Y_1\!+\!X_1\!+\!Z_1\!+\!2,Y_1\!-\!Y_0\!+\!X_1\!-\!X_0\!+\!Z_1\!-\!Z_0)}}\nonumber 
\end{aligned}$$
