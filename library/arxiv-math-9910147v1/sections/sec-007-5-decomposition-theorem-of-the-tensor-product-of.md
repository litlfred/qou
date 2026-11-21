---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-007-5-decomposition-theorem-of-the-tensor-product-of
section_title: "Decomposition Theorem of the Tensor Product of Principal Representations and Askey-Wilson Polynomials"
section_number: 5
pages: 22-24
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.972
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
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
