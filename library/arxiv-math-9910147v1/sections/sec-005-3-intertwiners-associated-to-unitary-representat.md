---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-005-3-intertwiners-associated-to-unitary-representat
section_title: "Intertwiners associated to unitary representations of the quantum Lorentz group"
section_number: 3
pages: 13-17
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.977
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
The aim of this section is to give explicit formulae of the intertwiners between the representation ${\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}\!\!\!\otimes \!\!{\buildrel {\!\!{}_{(Y_0Y_1)}} \over {\Pi}}$ and the representation ${\buildrel {\!\!{}_{(Z_0Z_1)}} \over {\Pi}},$ in terms of complex continuations of $6j$ symbols of $\mathfrak{U}_q(su(2)).$

::: proposition
Let $\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}:V(X_0X_1)\otimes V(Y_0Y_1)\rightarrow V(Z_0Z_1)$ be a $\mathfrak{U}_q(sl(2,\CC)_{\RR})$ intertwiner. We necessarily have: $$\hskip -0.5cm\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}(\ontop{A}{e}_i(X_0X_1)\otimes  
\ontop{B}{e}_j(Y_0Y_1))=\!\sum_{C,k}\ontop{C}{e}_k(Z_0Z_1)\!\Clebpsi{A}{B}{C}{i}{j}{k}\!\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1},\label{defreducedelement}$$ where the coefficients $\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}$, called "reduced elements", are complex numbers.\
Inversely such a map defines an intertwiner if and only if the following conditions on the reduced elements are satisfied: $\forall A,B,C\in \onehalf \ZZ^+, Y^{(0)}_{(A,B,C)}=Y^{(1)}_{(A,m_X)}=Y^{(1)}_{(B,m_Y)}=1,$ $$\begin{aligned}
&&\hskip -1cm\sum_{QRSP} \ElemRed{R}{P}{T}{X_0X_1}{Y_0Y_1}{Z_0Z_1}  
\Lambda^{US}_{RA}(X_0X_1)\Lambda^{UQ}_{PB}(Y_0Y_1)  
\sixjn{U}{W}{T}{R}{P}{Q}{0}\sixjn{R}{W}{Q}{B}{U}{S}{0}\!\!\times\nonumber\\  
&&\times\sixjn{B}{W}{S}{U}{A}{C}{0}=\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}\Lambda^{UW}_{TC}(Z_0Z_1)\label{inter1}.  
\end{aligned}$$
:::

The necessary condition comes from the fact that ([\[defreducedelement\]](#defreducedelement){reference-type="ref" reference="defreducedelement"}) is equivalent to the property that $\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}$ is an intertwiner of $\mathfrak{U}_q(su(2))$ module. Such a map is an intertwiner of $\mathfrak{U}_q(an(2))$ module, if moreover, $$\begin{aligned}
\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}(\Delta({\buildrel U \over g}{}^{m}_{n})    
(\ontop{A}{e}_i(X_0X_1)\otimes \ontop{B}{e}_j(Y_0Y_1)))={\buildrel U \over g}{}^{m}_{n}    
\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}(\ontop{A}{e}_i(X_0X_1)\otimes \ontop{B}{e}_j(Y_0Y_1)).\nonumber  
\end{aligned}$$ This last condition can be rewritten as ([\[inter1\]](#inter1){reference-type="ref" reference="inter1"}) using ([\[repg\]](#repg){reference-type="ref" reference="repg"})([\[ortho1cont\]](#ortho1cont){reference-type="ref" reference="ortho1cont"})([\[vertexIRF\]](#vertexIRF){reference-type="ref" reference="vertexIRF"}). This concludes the proof.

Remark: A very important point is that $\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}$ maps the algebraic tensor product of the two domains $V(X_0X_1)\otimes V(Y_0Y_1)$ to $V(Z_0Z_1).$ As a result the sum $(\ref{defreducedelement})$ is finite. It can be seen that there are no non zero intertwiner from $V(Z_0Z_1)$ to the algebraic tensor product $V(X_0X_1)\otimes V(Y_0Y_1).$

::: lemma
The space of $\mathfrak{U}_q(sl(2,\CC)_{\RR})$ intertwiners from the module $V(X_0X_1)\otimes V(Y_0Y_1)$ to the module $V(Z_0Z_1)$ is of dimension $0$ or $1.$
:::

An elementary proof is obtained by analyzing the rank of the system of linear equations ([\[inter1\]](#inter1){reference-type="ref" reference="inter1"}). Using the isomorphism of module between $V(X_0X_1)$ and $V({\underline {X_0}},{\underline {X_1}})$, we can always assume that $m_X, m_Y, m_Z$ are non negative. It is easy to show that we can always assume that $m_Z\leq m_X+m_Y.$ If not, we use the fact that the space of intertwiners from $V(X_0X_1)\otimes V(Y_0Y_1)$ to $V(Z_0Z_1)$ is in one to one correspondence with the space of intertwiners from $V(Z_0Z_1)\otimes V({\bar X_0}{\bar X_1})$ to $V(Y_0Y_1)$ to exchange $m_Y$ and $m_Z$. This one to one correspondence easily follows from the isomorphism $V(X_0X_1)^{*}\approx{\bar  V}(X_0X_1) \approx V({\bar X_0}{\bar X_1})$ and where we denoted by $V(X_0X_1)^{*}$ the restricted dual of the Harisch-Chandra module $V(X_0X_1).$

This system of linear equations is equivalent to the subsystem where we have chosen $U=\onehalf$, because $\mathfrak{U}_q(an(2))$ is generated as an algebra by ${\buildrel U \over g}{}^{m}_{n}$ where $U=\onehalf.$ This system is therefore equivalent to the following one: $\forall \sigma,\tau \in \{\onehalf,-\onehalf  \},$

$$\begin{aligned}
&&\hskip -1cm\sum_{\epsilon,\sigma,\mu,\tau\in\{-\onehalf,\onehalf\}} \ElemRed{\!\!A+$\nu+\rho$}{B+$\epsilon+\mu$}{\!C+$\sigma+\tau$}{X_0X_1}{Y_0Y_1}{Z_0Z_1} 
\Lambda^{\onehalf \;\;A+\nu}_{A+\nu+\rho\;A}(X_0X_1) 
\Lambda^{\onehalf \;\;B+\epsilon}_{B+\epsilon+\mu\;B}(Y_0Y_1)\times\nonumber\\ 
&&\times\sixjn{A\!+\!\nu\!+\!\rho}{C\!+\!\sigma}{B\!+\!\epsilon}{\onehalf}{B\!+\!\epsilon\!+\!\mu}{C\!+\!\sigma\!+\!\tau}{0} 
\sixjn{C+\sigma}{A\!+\!\nu\!+\!\rho}{B\!+\!\epsilon}{\onehalf}{B}{A\!+\!\nu}{0}\!\!\sixjn{B}{C\!+\!\sigma}{A\!+\!\nu}{\onehalf}{A}{C}{0}= 
\nonumber\\ 
&&\hskip 1.5cm= 
\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1} 
\Lambda^{{\onehalf}{C+\sigma}}_{{C+\sigma+\tau}{C}}(Z_0Z_1) 
\label{inter1/2}.  
\end{aligned}$$ We will denote by $S(\sigma,\tau)$ this system of equations.

It is easy to show that the system $S(-\onehalf,-\onehalf)$ completely determines the reduced elements at the point $(A,B,C)$ in terms of the reduced element of the points $(A',B',C-1)$ with $A'=A+\epsilon, B'=B+\nu$ with $\epsilon,\nu \in \{\onehalf,-\onehalf  \}$. Therefore the rank of the system is less than the rank of the vectors which components are the reduced elements at the points $(A,B,m_Z).$\
Let $\Delta=\{ (A,B)\in(\onehalf\ZZ^{+})^2, Y^{(0)}_{(A,B,m_Z)}=1\}, P=\{(A,B)\in(\onehalf\ZZ^{+})^2, A-m_X\in \NN\}, 
 Q=\{(A,B)\in\onehalf(\ZZ^{+})^2, B-m_Y\in \NN\}.$ $\Delta\cap P\cap Q$ is the intersection of a lattice with a convex set which boundary consits in 3 segments and two half-lines. In the case where $m_Z\leq m_X+m_Y$ one of this segment degenerate to the point $p=(m_X,m_Y).$ It is easy to show, by a direct computation, that the system $S(\onehalf,-\onehalf)$ and $S(-\onehalf,\onehalf)$ are independent. As a result we can take linear combination of these two systems to have linear combinations of reduced elements at $(A,B,m_Z)$ involving only $8$ points and not 9. It is easy to show that the use of both of these systems determine uniquely the reduced elements at the point $(A,B,m_Z)$ in terms of the reduced elements at the point $p, p+(1,0), p+(0,1), p+(1,1).$ As a result the system is of rank less than four. But the reduced elements at the point $p, p+(1,0), p+(0,1), p+(1,1)$ are solutions of three systems of linear equations which can be shown to be independent:\
$S(\onehalf,-\onehalf)$ at $(m_X,m_Y,m_Z),$ $S(-\onehalf,\onehalf)$ at $(m_X,m_Y,m_Z),$ and $S(\onehalf,\onehalf)$ at $(m_X,m_Y,m_Z-1).$ As a result the rank of the system is of dimension less than one.

::: theorem
Assume that the numbers $\rho_X,\rho_Y,\rho_Z$ and $\epsilon_X\rho_X+\epsilon_Y\rho_Y+\epsilon_Z\rho_Z$ with $\epsilon_X,\epsilon_Y,\epsilon_Z\in \{-1,1\}$ are non zero. The space of $\mathfrak{U}_q(sl(2,\CC)_{\RR})$ intertwiners from the module $V(X_0X_1)\otimes V(Y_0Y_1)$ to the module $V(Z_0Z_1)$ is of dimension $0$ if and only if $m_X+m_Y+m_Z\notin\ZZ.$\
If $m_X+m_Y+m_Z\in\ZZ$ it is a one dimensional space which admits a non zero element, whose reduced element, given in terms of $6j(1)$ and $6j(3),$ is $$\begin{aligned}
&&\hskip -1cm\ElemRed{R}{P}{T}{\!X_0X_1}{\!Y_0Y_1}{Z_0Z_1}\!\!=\!\!\sum_{X_2}\!\sixjn{\!Y_0}{\!X_0}{\!Z_0\!}{\!T}{\!Z_1}{\!X_2\!}{3}\!\!\!  
\sixjn{\!X_1\!}{\!X_0}{\!R}{\!T\!}{\!P\!}{\!X_2}{1}\!\!\!\sixjn{\!Z_1}{\!X_2}{\!Y_0\!}{\!P}{\!Y_1}{\!X_1\!}{3}\!\!\!\!\!  
\frac{v^{1/4}_{P}v^{1/4}_{T}v^{1/4}_{X_0}v^{1/4}_{X_1}[d_P]^{1/2}}{v^{1/4}_{R}v^{1/2}_{X_2}e^{i\pi P}}. \nonumber\\ 
&& 
\label{form6jprol1}  
\end{aligned}$$ We will denote by $\GPhin{X_0X_1}{Y_0Y_1}{Z_0Z_1}$ the associated intertwining operator.

The reduced elements satisfy the condition:

$\forall C, C-\vert m_Z\vert\in \NN, \exists A,B\in \onehalf {\ZZ}^{+},  
\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}\not=0.$
:::

We have assumed that $\rho_X,\rho_Y,\rho_Z$ and $\epsilon_X\rho_X+\epsilon_Y\rho_Y+\epsilon_Z\rho_Z$ with $\epsilon_X,\epsilon_Y,\epsilon_Z\in \{-1,1\}$ are non zero in order that all the $6j(1)$ and $6j(3)$ are well defined in the expression ([\[form6jprol1\]](#form6jprol1){reference-type="ref" reference="form6jprol1"}). But this condition can nevertheless be removed by normalizing the reduced elements by a function $F(Z_0Z_1,Y_0Y_1,Z_0Z_1)$ which remove the singularities of this expression.

Using only polynomial identities on continuation of $6j$, we will show that the left handside of ([\[inter1\]](#inter1){reference-type="ref" reference="inter1"}) and the righthandside of ([\[inter1\]](#inter1){reference-type="ref" reference="inter1"}) are equal if we take the ansatz ([\[form6jprol1\]](#form6jprol1){reference-type="ref" reference="form6jprol1"}) for the reduced element.

The lefthandside of ([\[inter1\]](#inter1){reference-type="ref" reference="inter1"})= $$\begin{aligned}
&&\hskip -0.6cm=e^{-i\pi P}\sqrt{[d_P]}  
\!\!\!\!\!\sum_{QRSPX_2X_3Y_2}\!\!\!\!  
\frac{v^{1/2}_{P}v^{1/4}_{T}  
v^{1/4}_{A}v^{1/4}_{B}v^{1/4}_{X_0}v_{X_3}v_{Y_2}}  
{v_{U}v^{1/2}_{X_2}v^{1/2}_{S}v^{1/2}_{Q}v^{3/4}_{X_1}v_{Y_1}}  
\sixjn{Y_0}{X_0}{Z_0}{T}{Z_1}{X_2}{3}  
\!\!\sixjn{X_1}{X_0}{R}{T}{P}{X_2}{1}\nonumber\\  
&&\times\!\!\sixjn{Z_1}{X_2}{Y_0}{P}{Y_1}{X_1}{3}  
\!\!\sixjn{X_0}{X_1}{R}{U}{S}{X_3}{1}  
\!\!\sixjn{X_0}{X_1}{A}{U}{S}{X_3}{1}  
\!\!\sixjn{U}{W}{T}{R}{P}{Q}{0}  
\!\!\sixjn{R}{W}{Q}{B}{U}{S}{0}\nonumber\\  
&&\times\!\!\sixjn{B}{W}{S}{U}{A}{V}{0}  
\!\!\sixjn{Y_0}{Y_1}{P}{U}{Q}{Y_2}{1}  
\!\!\sixjn{Y_0}{Y_1}{B}{U}{Q}{Y_2}{1}.  
\end{aligned}$$ We apply first the pentagonal identity ([\[penta3cont\]](#penta3cont){reference-type="ref" reference="penta3cont"}) to the second and sixth $6j$, then the pentagonal identity ([\[penta3cont\]](#penta3cont){reference-type="ref" reference="penta3cont"}) to the fourth and the seventh $6j$ and finally we realize the sum on $R$ by applying the orthogonality ([\[ortho1cont\]](#ortho1cont){reference-type="ref" reference="ortho1cont"}), to obtain $$\begin{aligned}
&&\hskip -0.6cm=e^{-i\pi P}\sqrt{[d_P]}  
\!\!\!\!\!\sum_{QSPX_2X_3Y_2X_4}\!\!\!\!  
\frac{v^{1/2}_{P}v^{1/4}_{T}  
v^{1/4}_{A}v^{1/4}_{B}v^{1/4}_{X_0}v_{X_3}v_{Y_2}}  
{v_{U}v^{1/2}_{X_2}v^{1/2}_{S}v^{1/2}_{Q}v^{3/4}_{X_1}v_{Y_1}}  
\sixjn{Y_0}{X_0}{Z_0}{T}{Z_1}{X_2}{3}  
\!\!\sixjn{X_1}{X_4}{Q}{U}{P}{X_2}{0}\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\times\!\!\sixjn{Z_1}{X_2}{Y_0}{P}{Y_1}{X_1}{3}  
\!\!\sixjn{X_0}{X_2}{T}{U}{W}{X_4}{0}  
\!\!\sixjn{X_0}{X_1}{A}{U}{S}{X_3}{1}  
\!\!\sixjn{X_1}{X_4}{Q}{B}{U}{X_3}{1}  
\!\!\sixjn{X_0}{X_3}{S}{B}{W}{X_4}{1}\nonumber\\  
&&\times\!\!\sixjn{B}{W}{S}{U}{A}{V}{0}  
\!\!\sixjn{Y_0}{Y_1}{P}{U}{Q}{Y_2}{1}  
\!\!\sixjn{Y_0}{Y_1}{B}{U}{Q}{Y_2}{1}.  
\end{aligned}$$ Now we apply the symetries ([\[symcont\]](#symcont){reference-type="ref" reference="symcont"})([\[sym6j3\]](#sym6j3){reference-type="ref" reference="sym6j3"}) and transform the sum over $P$ of the second, the third, and the ninth $6j$ using the hexagonal identity ([\[hexa6j3\]](#hexa6j3){reference-type="ref" reference="hexa6j3"}), to obtain $$\begin{aligned}
&&\hskip -0.6cm=e^{-i\pi Q}\sqrt{[d_Q]}  
\!\!\!\!\!\sum_{QSZ_3X_2X_3Y_2X_4}\!\!\!\!  
\frac{v^{1/4}_{T}  
v^{1/4}_{A}v^{1/4}_{B}v^{1/4}_{X_0}v_{X_3}v^{1/2}_{Y_2}v^{1/2}_{Z_3}}  
{v_{U}v^{1/2}_{X_4}v^{1/2}_{S}v^{1/2}_{Z_1}v^{3/4}_{X_1}v^{1/2}_{Y_1}}  
\sixjn{Y_0}{X_0}{Z_0}{T}{Z_1}{X_2}{3}  
\!\!\sixjn{Y_0}{Z_1}{X_2}{U}{X_4}{Z_3}{3}  
\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\times\!\!\sixjn{X_1}{Z_1}{Y_1}{U}{Y_2}{Z_3}{3}  
\!\!\sixjn{X_0}{X_2}{T}{U}{W}{X_4}{0}  
\!\!\sixjn{X_0}{X_1}{A}{U}{S}{X_3}{1}  
\!\!\sixjn{X_1}{X_4}{Q}{B}{U}{X_3}{1}  
\!\!\sixjn{X_0}{X_3}{S}{B}{W}{X_4}{1}\nonumber\\  
&&\times\!\!\sixjn{B}{W}{S}{U}{A}{V}{0}  
\!\!\sixjn{Z_3}{Y_0}{X_4}{Q}{X_1}{Y_2}{3}  
\!\!\sixjn{Y_0}{Y_1}{B}{U}{Q}{Y_2}{1}  
(e^{i \pi}q)^{(X_4+Y_1-X_1-Y_0)}\frac{\nu_1(d_{X_1})\nu_1(d_{Y_0})}{\nu_1(d_{X_4})\nu_1(d_{Y_1})}.  
\end{aligned}$$ We realize the sum over $Q$ of the sixth, ninth and tenth $6j$ using the pentagonal identity ([\[penta1sixj3\]](#penta1sixj3){reference-type="ref" reference="penta1sixj3"}) and symetries ([\[symcont\]](#symcont){reference-type="ref" reference="symcont"}), the sum over $X_2$ of the first, second and fourth $6j$ using the pentagonal identity ([\[penta1sixj3\]](#penta1sixj3){reference-type="ref" reference="penta1sixj3"}) and transform the sum over $S$ of the fifth, seventh and eighth $6j$ according to the hexagonal identity ([\[hexacont\]](#hexacont){reference-type="ref" reference="hexacont"}) to obtain $$\begin{aligned}
&&\hskip -0.6cm=e^{-i\pi B}\sqrt{[d_B]}  
\!\!\!\!\!\sum_{Z_3X_5X_3Y_2X_4}\!\!\!\!  
\frac{v^{1/4}_{T}v^{1/2}_{V}  
v^{1/4}_{B}v^{1/4}_{X_0}v^{1/2}_{X_3}v^{1/2}_{Y_2}v^{1/2}_{Z_3}}  
{v^{1/2}_{W}v^{1/4}_{A}v_{U}v^{1/2}_{X_5}v^{1/2}_{Z_1}v^{1/4}_{X_1}v^{1/2}_{Y_1}}  
\sixjn{X_1}{Z_1}{Y_1}{U}{Y_2}{Z_3}{3}  
\!\!\sixjn{Z_3}{Y_1}{X_3}{U}{X_1}{Y_2}{3}\nonumber\\  
&&\times\!\!\sixjn{Z_3}{Y_0}{X_4}{B}{X_3}{Y_1}{3}  
\sixjn{Y_0}{Z_3}{X_4}{W}{X_0}{Z_0}{3}  
\!\!\sixjn{Z_0}{Z_1}{T}{U}{W}{Z_3}{1}  
\!\!\sixjn{B}{X_4}{X_3}{U}{X_1}{X_5}{1}  
\!\!\sixjn{X_0}{X_1}{A}{B}{V}{X_5}{1}\nonumber\\  
&&\times\!\!\sixjn{X_0}{X_5}{V}{U}{W}{X_4}{1}  
(e^{i \pi}q)^{(X_4+2Y_1-X_1-Y_0-Y_2)}  
\frac{\nu_1(d_{X_1})\nu_1(d_{Y_0})\nu_1(d_{Y_2})}{\nu_1(d_{X_4})\nu_1(d_{Y_1})^2}.  
\end{aligned}$$ Then, we realize the sum over $Y_2$ of the first and second $6j$ by using the Racah identity ([\[racah6j3\]](#racah6j3){reference-type="ref" reference="racah6j3"}) and symetries ([\[sym6j3\]](#sym6j3){reference-type="ref" reference="sym6j3"}) to find $$\begin{aligned}
&&\hskip -0.6cm=e^{-i\pi B}\sqrt{[d_B]}  
\!\!\!\!\!\sum_{Z_3X_5X_3X_4}\!\!\!\!  
\frac{v^{1/4}_{T}v^{1/2}_{V}v_{Z_3}  
v^{1/4}_{B}v^{1/4}_{X_0}v^{1/4}_{X_1}}  
{v^{1/2}_{U}v^{1/4}_{A}v_{Z_1}v^{1/2}_{W}v^{1/2}_{X_5}}  
\sixjn{Y_1}{Z_3}{X_3}{U}{X_1}{Z_1}{3}  
\!\!\sixjn{Z_3}{Y_0}{X_4}{B}{X_3}{Y_1}{3}\nonumber\\  
&&\times\!\!  
\sixjn{Y_0}{Z_3}{X_4}{W}{X_0}{Z_0}{3}  
\!\!\sixjn{Z_0}{Z_1}{T}{U}{W}{Z_3}{1}  
\!\!\sixjn{B}{X_4}{X_3}{U}{X_1}{X_5}{1}  
\!\!\sixjn{X_0}{X_1}{A}{B}{V}{X_5}{1}  
\sixjn{X_0}{X_5}{V}{U}{W}{X_4}{1}  
\nonumber\\  
&&\times\!  
(e^{i \pi}q)^{(X_4+Y_1+Z_1-X_1-Y_0-Z_3)}  
\frac{\nu_1(d_{X_1})\nu_1(d_{Y_0})\nu_1(d_{Z_3})}{\nu_1(d_{X_4})\nu_1(d_{Y_1})\nu_1(d_{Z_1})}.  
\end{aligned}$$ Now, we realize the sum over $X_3$ of the first, second and fifth $6j$ by using the pentagonal identity ([\[penta2sixj3\]](#penta2sixj3){reference-type="ref" reference="penta2sixj3"}) and symetries ([\[sym6j3\]](#sym6j3){reference-type="ref" reference="sym6j3"}) to find $$\begin{aligned}
&&\hskip -1.7cm=e^{-i\pi B}\sqrt{[d_B]}  
\!\sum_{Z_3X_5X_4}\!  
\frac{v^{1/4}_{T}v^{1/2}_{V}v_{Z_3}  
v^{1/4}_{B}v^{1/4}_{X_0}v^{1/4}_{X_1}}  
{v^{1/2}_{U}v^{1/4}_{A}v_{Z_1}v^{1/2}_{W}v^{1/2}_{X_5}}  
\sixjn{Y_0}{Z_1}{X_5}{U}{X_4}{Z_3}{3}  
\!\!\sixjn{Z_1}{Y_1}{X_1}{B}{X_5}{Y_0}{3}\nonumber\\  
&&\times  
\sixjn{Y_0}{Z_3}{X_4}{W}{X_0}{Z_0}{3}  
\!\!\sixjn{Z_0}{Z_1}{T}{U}{W}{Z_3}{1}  
\!\!\sixjn{X_0}{X_1}{A}{B}{V}{X_5}{1}  
\sixjn{X_0}{X_5}{V}{U}{W}{X_4}{1}.  
\end{aligned}$$ Finally we realize the sum over $X_4$ of the first, third and sixth $6j$ using the pentagonal equation ([\[penta36j3\]](#penta36j3){reference-type="ref" reference="penta36j3"}) to conclude $$\begin{aligned}
&&\hskip -0.9cm=e^{-i\pi B}\sqrt{[d_B]}\sum_{X_5}  
\frac{v^{1/4}_{V}  
v^{1/4}_{B}v^{1/4}_{X_0}v^{1/4}_{X_1}}  
{v^{1/4}_{A}v^{1/2}_{X_5}}  
\sixjn{Y_0}{Z_1}{X_5}{V}{X_0}{Z_0}{3}  
\!\!\sixjn{X_0}{X_1}{A}{B}{V}{X_5}{1}  
\!\!\sixjn{Z_1}{Y_1}{X_1}{B}{X_5}{Y_0}{3}\nonumber\\  
&&\times\!\!\sum_{Z_3} \frac{v^{1/4}_{T}v^{1/4}_{V}v_{Z_3}}  
{v^{1/2}_{U}v^{1/2}_{W}v_{Z_1}}  
\!\!\sixjn{Z_0}{Z_1}{T}{U}{W}{Z_3}{1}\sixjn{Z_1}{Z_0}{V}{W}{U}{Z_3}{1}\nonumber\\  
&&\hskip -0.9cm=\mbox{the righthandside of (\ref{inter1}).}\nonumber  
\end{aligned}$$ This concludes the proof that the expression of the reduced elements defines an intertwiner operator.

Let us now prove the final part of the theorem. Let us fix $C$ such that $(C-\vert m_Z\vert) \in \NN$ and assume that $\forall A, B, \;\ElemRed{A}{B}{C}{X_0X_1}{Y_0Y_1}{Z_0Z_1}\!\!=0.$ In this event, by multiplying the reduced element by $\sixjn{X_1}{X_0}{A}{C}{B}{X_3}{1}$, and summing over $A$, we would obtain, after the use of the orthogonality relation on $6j(1),$ $\forall B, \forall X_2,\;\; \sixjn{Y_0}{X_0}{Z_0}{C}{Z_1}{X_2}{3}\!\!\sixjn{Z_1}{X_2}{Y_0}{B}{Y_1}{X_1}{3}\!\!\!=0.$ But from the orthogonality relation on $6j(3),$ $\exists X_2 \; / \;\sixjn{Y_0}{X_0}{Z_0}{C}{Z_1}{X_2}{3}\!\!\!\not=0.$ As a result we obtain that $\sixjn{Z_1}{X_2}{Y_0}{B}{Y_1}{X_1}{3}\!\!=0$ for all $B$ subject to the selection rules. From the behaviour of $\sixjn{Z_1}{X_2}{Y_0}{B}{Y_1}{X_1}{3}$ when $B$ is large (see Eq. ([\[asymptotic6j3\]](#asymptotic6j3){reference-type="ref" reference="asymptotic6j3"})), we obtain a contradiction. As a result the statement of the theorem holds true and implies in particular that the intertwiner is non zero.
