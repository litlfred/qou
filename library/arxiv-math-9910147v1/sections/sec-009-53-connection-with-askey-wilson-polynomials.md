---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-009-53-connection-with-askey-wilson-polynomials
section_title: "Connection with Askey-Wilson Polynomials."
section_number: 5.3
pages: 25-26
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.988
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
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
