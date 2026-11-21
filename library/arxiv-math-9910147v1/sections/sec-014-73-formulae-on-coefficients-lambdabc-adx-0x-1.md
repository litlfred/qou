---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-014-73-formulae-on-coefficients-lambdabc-adx-0x-1
section_title: "Formulae on coefficients $\Lambda^{BC}_{AD}(X_0X_1)$"
section_number: 7.3
pages: 29-34
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.586
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
Let us recall some properties of the coefficients $\Lambda^{BC}_{AD}(X_0X_1)$ which were proved in [@BR1]. We will say that the coefficients $\Lambda^{BC}_{AD}$ are off-diagonal if $A \not= D$ and diagonal if $A=D$ (in the latter case we will use the notation $\Lambda^{BC}_{A}=\Lambda^{BC}_{AA}$). The coefficients $\Lambda^{BC}_{A}$ are said to be on the boundary if $B\!+\!C\!=\!A,\; A\!+\!B\!=\!C, \;$ or $A\!+\!C\!=\!B.$ The coefficients $\Lambda^{BC}_{AD}(X_0X_1)$ are proportional to $Y^{(0)}_{(A,B,C)}Y^{(0)}_{(D,B,C)}Y^{(1)}_{(A,X_0-X_1)}Y^{(1)}_{(D,X_0-X_1)},$ so they vanish according to these selection rules. The following relation holds true (it is in fact equivalent to the property that ${\buildrel {\!\!{}_{(X_0X_1)}}\over {\Pi}}$ is a representation of ${\frak U}_q(an(2))$): $$\begin{aligned}
&&\hskip -1cm \coefblambda{A}{C}{F}{G}\coefblambda{B}{D}{G}{H}=\!\!\sum_{KU} \frac{e^{i \pi (G+U)}(\qn{d_U}\qn{d_G})^{\frac{1}{2}}\;\;\coefblambda{K}{U}{F}{H}}{e^{i \pi (C+D)}(\qn{d_C}\qn{d_D})^{\frac{1}{2}}}  
\sixjn{A}{D}{U}{B}{C}{G}{0}\!\!\!\sixjn{B}{U}{C}{F}{A}{K}{0}\!\!\!\sixjn{H}{U}{K}{A}{B}{D}{0}.\label{systan}  
\end{aligned}$$

As a result, by taking $F=H$ in this expression, the off-diagonal coefficients are obtained, up to a sign, from the diagonal coefficients.

These diagonal coefficients can be computed in various ways. They satisfy the following system of linear equations: $$\begin{aligned}
&&\hskip -1.2cm \forall (A,B,C)\in \halfinteger\times\halfinteger\times  {\onehalf}\mathbb{Z}^{+*}\;/\;B\!+\!A\!-\!C,\; B\!+\!C\!-\!A, \;A\!+\!C\!-\!B \in \NN^*\nonumber\\  
&&\hskip -1.3cm   
 \frac{[\mbox{\small \it A$+$B$+$C$+1$}]}{[\mbox{\small \it $2$A$+1$}]}\coefalambda{B}{\;C}{\;\;A}\!+\!    
\frac{[\mbox{\small \it A$+$C$-$B$+1$}]}{[\mbox{\small \it $2$A$+1$}]}\coefalambda{B\!-\!1}{\;C}{\;\;\;A}\!\!-\!\frac{[\mbox{\small \it C$+$B$-$A$-1$}]}{[\mbox{\small \it $2$A$+1$}]}\coefalambda{B\!-\!1}{\;C\!-\!1}{\;\;\;\;A}  
\!+\!\frac{[\mbox{\small \it B$+$A$-$C$+1$}]}{[\mbox{\small \it $2$A$+1$}]}\coefalambda{B}{\;C\!-\!1}{\;\;A}=\nonumber\\   
&&\hskip -1.4cm =  
\frac{[\mbox{\small \it A$+$B$-$C$-1$}]}{[\mbox{\small \it $2$A$-$}1]}\coefalambda{B\!-\!1}{\;\;C}{\;\;\;A\!-\!1}\!+\!\frac{[\mbox{\small \it A$+$C$-$B$-1$}]}{[\mbox{\small \it $2$A}-1]}\coefalambda{B}{\;\;C\!-\!1}{\;\;A\!-\!1}\!+\!  
\frac{[\mbox{\small \it A$+$B$+$C$-1$}]}{[\mbox{\small \it $2$A}-1]}\coefalambda{B\!-\!1}{\;C\!-\!1}{\;\;\;A\!-\!1}  
\!\!-\!\frac{[\mbox{\small \it C$+$B$-$A$+$}1]}{[\mbox{\small \it $2$A$-$}1]}\coefalambda{B}{\;C}{A\!-\!1},  
\label{linearANexpli}  
\end{aligned}$$

as well as $\forall A,B,C \in \halfinteger / Y^{(0)}_{(A,B,C)}=1,$ $$\begin{aligned}
&&\hskip -0.5cm [B\!\!+\!\!C\!\!-\!\!A\!\!+\!\!1][A\!\!+\!\!B\!\!+\!\!C\!\!+\!\!2]q^{\pm(C-B)}\Lambda^{B+\onehalf\;C+\onehalf}_{\;\;A}  
-[A\!\!+\!\!C\!\!-\!\!B][A\!\!+\!\!B\!\!-\!\!C\!\!+\!\!1]q^{\mp(C+B+1)}\Lambda^{B+\onehalf\;C-\onehalf}_{\;\;A}+\nonumber\\  
&&\hskip -0.4cm+[A\!\!+\!\!C\!\!+\!\!B\!\!+\!\!1][B\!\!+\!\!C\!\!-\!\!A]q^{\mp(C-B)}\Lambda^{B-\onehalf\;C-\onehalf}_{\;\;A}  
-[A\!\!+\!\!B\!\!-\!\!C][A\!\!+\!\!C\!\!-\!\!B\!\!+\!\!1]q^{\pm(C+B+1)}\Lambda^{B-\onehalf\;C+\onehalf}_{\;\;A}\nonumber\\  
&&\hskip -0.5cm=\omega_{\pm}[2C\!\!+\!\!1][2B\!\!+\!\!1]\Lambda^{B\;C}_{\;\;A},\!\!\!\!\label{lambdacasimir}  
\end{aligned}$$ where we have denoted $\omega_+=q^{2X_0+1}\!+\!q^{-2X_0-1},\;\omega_-=q^{2X_1+1}\!+\!q^{-2X_1-1}.$

These two linear systems have a unique normalized solution. The value of the diagonal coefficients on the boundary have the following simple expression:

$$\begin{aligned}
&&\hskip -1cm\Lambda^{B\;\;\;C}_{B+C}(X_0X_1)= \sum_{k=-B}^{B}\frac{q^{-2k(X_0+X_1+1)}\binom{B+C+X_0-X_1}{B+k}_q\binom{B+C-X_0+X_1}{B-k}_q}{(-1)^{2B}\binom{2B+2C}{2B}_q},\label{lambdaboundary}\\  
&&\hskip -1cm\Lambda^{B\;A+B}_{\;\;\;A}(X_0X_1)=\!\!\!\sum_{k=-B}^{B}\frac{q^{-2k(X_0+X_1+1)}\binom{A+X_0-X_1+B-k}{B-k}_q\binom{A-X_0+X_1+B+k}{B+k}_q}{\binom{2A+2B+1}{2B}_q}\nonumber\\ 
&&= \frac{v_{X_0}}{v_{X_1}}\Lambda^{A+B\;B}_{\;\;\;A}(X_1X_0)\label{symetryLambda}. 
\end{aligned}$$

Different explicit formulae for the coefficients $\Lambda^{BC}_{AD}$ can be obtained, the fundamental one is expressed in terms of 6j(1) ([\[formlamb6j\]](#formlamb6j){reference-type="ref" reference="formlamb6j"}). This last expression can be simplified, using the universal shifted cocycle associated to $6j(1),$ and we get: $$\begin{aligned}
&&\hskip -1.8cm\Lambda^{BC}_{AD}(X_0,X_1)  
= \sum_{\sigma_1 \sigma_2}\frac{v_A^{1/4}}{v_D^{1/4}}  
\frac{{\cal N}^{(D)}(q^{2X_1+1},m_X)}{{\cal N}^{(A)}(q^{2X_1+1},m_X)}\Clebpsi{C}{B}{A}{\sigma_2}{\sigma_1}{m_X}\;  
q^{- 2i\sigma_1 \rho_X}  
\Clebphi{B}{C}{D}{\sigma_1}{\sigma_2}{m_X}\label{lambda3j}  
\end{aligned}$$ where ${\cal N}^{(A)}(q^{2X+1},\sigma)$ are normalization factors, given in [@BR1], which values will not be useful in our paper. This last expression is simpler than ([\[formlamb6j\]](#formlamb6j){reference-type="ref" reference="formlamb6j"}) in many aspects: it is a sum of a product of basic hypergeometric of 3-2 type rather than 4-3 type, and moreover it explicitely shows that $\Lambda^{BC}_{A}$ are Laurent polynomials in $q^{i\rho_X}.$

Remark: From the system of constraints satisfied by the coefficients $\Lambda^{BC}_{AD}$, it is easy to show that $(\Lambda^{BC}_{AD})^2$ is a Laurent polynomials in both variables $q^{2X_0+1}, q^{2X_1+1}.$

The constraint systems described before, as well as explicit expressions, allow us to derive most of the asymptotic properties of these coefficients when some of the variables are large.

::: proposition
The coefficients $\Lambda^{BC}_{AD}$ satisfy the following inequality: $$\forall A,D \in \halfinteger, \forall R \in {\onehalf}\ZZ, \forall m  \in {\onehalf}\ZZ, \exists \;{\cal C}, {\cal B}\;>0,  
\forall\rho\in \RR, \forall B > {\cal B}, \vert \Lambda^{B \;B+R}_{A\;\;D}(m,\rho) \vert \leq  
{\cal C} Bq^{2B}\label{asymptlambda1}.$$
:::

The proof is divided in two steps. We first show this inequality when $A=D$, by a direct computation. Then we use the system ([\[systan\]](#systan){reference-type="ref" reference="systan"}) and an induction argument to show this inequality when $A\not=D.$ We can always assume that $R\geq 0$, because the other case is deduced from this one and the identity ([\[symetryLambda\]](#symetryLambda){reference-type="ref" reference="symetryLambda"}). Using the relation ([\[lambda3j\]](#lambda3j){reference-type="ref" reference="lambda3j"}), we have $\vert \Lambda^{BB+R}_{A}(m,\rho)\vert \leq \sum_{j}u(j,m-j;B),$ where $u(j,k;B)=\vert \Clebpsi{B+R}{B}{A}{\;\;\;j}{k}{m}\;  
\Clebpsi{B+R}{B}{A}{\;\;-j}{\!-k}{-m}\vert.$

Using the formula (4) of ([@KV], section 14.3.5), we easily obtain that: $$\hskip -0.3cm\frac{\vert u(j,m\!-\!j;B)\vert }{q^{(A-R)(2B+R+A+1)}}=  
\frac{[2A]![2A+1]![A\!+\!B\!-\!j]![B\!+\!A\!+\!j]![2B\!+\!R\!-\!A]!F(j,m\!-\!j;B)F(-j,j\!-\!m;B)}{[A\!+\!R]! [A\!-\!R]![A\!+\!m]! [A\!-\!m]! [B\!+\!m\!-\!j]![B\!-\!m\!+\!j]![2B\!\!+\!\!R\!\!+\!\!A\!\!+\!\!1]!} \nonumber$$ where $F(j,m\!-\!j;B)={}_{3}\!\Phi_2\left[\!\!\begin{array}{ccc} m\!-\!A &-2B\!-\!R\!-\!A\!-\!1 &\!\! R\!-\!A\\&\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!-B\!-\!A\!+\!j &\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!-2A  \end{array} \!\!\right]\!.$ Using the fact that $-2B\!-\!A\!-\!R\leq -B\!-\!A\!+\!j  
\leq R\!-\!A,$ we can choose $C_1$ such that $\forall j, \forall B, \vert F(j,m-j;B)\vert \leq C_1 q^{-2Bn(m)}$ where $n(m)=inf(A-m,A-R)$. As a result, there exists a constant $C_1$ such that $$\begin{aligned}
\forall j,B,&& u(j,m-j;B)\leq C_1 q^{2B(A-R-n(m)-n(-m))-\vert B+j\vert (A+m)-\vert B-j\vert (A-m)-2B(2A+1)}.\nonumber 
\end{aligned}$$ From this, and the various inequalities between $B, j, m, R$, it is easy to show that we can find $C_2$ such that $$\vert \Lambda^{BB+R}_{A}(m,\rho)\vert \leq C_2(2B+2R+1)q^{2B}.\label{bounddiagonalLambda}$$ We can now prove this bound for the non diagonal case using an induction argument on $\vert A-D\vert.$ Indeed from ([\[systan\]](#systan){reference-type="ref" reference="systan"}), $$\hskip -0.2cm\vert  \coefblambda{B}{B\!+\!R}{A}{D\!+\!1} 
\coefblambda{\onehalf}{D\!+\!\onehalf}{D\!+\!1}{D}\vert \! \leq \! 
\sum_{KU}\!\frac{(\qn{d_{U}}\qn{d_{D+1}})^{\frac{1}{2}}\vert\coefblambda{K}{U}{A}{D}\vert} 
 {(\qn{d_{B+R}}\qn{d_{D+\onehalf}})^{\frac{1}{2}}}\vert 
\sixjn{A}{D\!+\!\onehalf}{U}{\onehalf}{\!B\!+\!R}{D\!+\!1\!}{0}\!\!\!\!\sixjn{\onehalf}{U}{\!B\!+\!R}{A}{B}{K}{0}\!\!\!\!\sixjn{D}{U}{K}{B}{\onehalf}{D\!+\!\onehalf}{0}\!\!\!\vert \nonumber.$$ Note that, due to the $Y$ functions, the previous sums contain at most four terms: $U=B+R\pm\onehalf, K=B\pm \onehalf.$ From the asymptotics property ([\[bounddiagonalLambda\]](#bounddiagonalLambda){reference-type="ref" reference="bounddiagonalLambda"}) when $B$ goes to $+\infty,$ and the induction hypothesis, we obtain that there exists a constant $C_3,$ with $\forall B, \forall \rho,\vert  \coefblambda{B}{B+R}{A}{D+1}(m,\rho) 
\coefblambda{\onehalf}{D+\onehalf}{D+1}{D}(m,\rho)\vert \leq  
C_3 B q^{2B}.$ From the explicit formulae of the coefficients $\coefblambda{\onehalf}{D+\onehalf}{D+1}{D}(m,\rho),$ in [@BR1], there exists $C_4>0$ such that $\forall\rho\in \RR , \forall B,\vert \coefblambda{\onehalf}{D+\onehalf}{D+1}{D}(m,\rho),\vert >C_4,$ as a result we get that the induction hypothesis is also true for $A, D+1.$

We will also need the following asymptotics:

::: proposition
The coefficients $\Lambda^{BC}_{A}$ own the following asymptotic behaviour: $$\begin{aligned}
&&\hskip -2cm\forall B \in \halfinteger,\forall R \in {\onehalf}\ZZ, B \pm R \in \NN, \forall (X_0X_1) \in {\mathbb S}, \exists {\cal C} \in \RR \nonumber\\  
&&\hskip -2cm\Lambda^{B \;\;K+R}_{\;\;K} \sim_{K\rightarrow +\infty} q^{2K \vert R \vert} \; {\cal C} \; Y^{(1)}_{(B,R)} \;\;\mbox{with}\;\;(\; {\cal C}=1\;\;\mbox{when}\;\; R=0).\label{asymptlambda2}  
\end{aligned}$$
:::

We use the formula ([\[lambda3j\]](#lambda3j){reference-type="ref" reference="lambda3j"}) to express $\Lambda^{B K+R}_{K}$. The asymptotic when $K$ is large is easily obtained using the formula (1) of ([@KV] section 14.3.5). The details are left to the reader and we easily obtain the statement of the proposition.

In the section $5$ we will need the following identity on the following series of weighted diagonal coefficients:

::: proposition
If $P>0$ the following series is absolutely and uniformly convergent in $\rho_X$ and we have: $$\begin{aligned}
&&\hskip -1.3cm\sum_{KM}\qd{K} \Clebpsi{K}{P}{M}{\sigma}{-P}{\sigma-P}\Clebphi{P}{K}{M}{-P}{\sigma}{\sigma-P}\Lambda^{KM}_{P}(X_0X_1) = \frac{\hbar\qd{P}q^{-2i \sigma \rho_X}e^{i\pi \sigma}\delta_{m_X,P}}{2\pi{\cal P}{(X_0X_1)}} .\label{formsumlambda}  
\end{aligned}$$ When $P=0$ we still have : $$\sum_{K}[d_K]\Lambda^{KK}_0(X_0X_1)= \frac{\hbar\qd{P}\delta_{m_X,P}}{2\pi{\cal P}{(X_0X_1)}}.$$
:::

\
When $P=0$, we see from ([\[lambda3j\]](#lambda3j){reference-type="ref" reference="lambda3j"}) that $\Lambda^{KK}_0(X_0X_1)$ is non zero only when $m_X=0.$ The series $\sum_{K}[d_K]\Lambda^{KK}_0(X_0X_1)$ is in this case very simple to compute because $\Lambda^{KK}_0(X_0X_1)=\frac{[(2X_0+1)(2K+1)]}{[2X_0+1][2K+1]},$ and we obtain the announced statement. Note that in this case the series is not uniformly convergent and is even divergent at $\rho_Z=0.$ When $P>0$ we will first show that the series is absolutely and uniformly convergent. Using the analogue of the Van-Der-Waerden formula for $3j$ [@KV], as well as relation ([\[symmetry3j\]](#symmetry3j){reference-type="ref" reference="symmetry3j"}) we can choose $C_1$ such that: $$\begin{aligned}
\vert \Clebpsi{K}{P}{K\!+\!R}{\sigma}{\!-P}{\sigma\!-\!P}\Clebphi{P}{K}{K\!+\!R}{\!\!-P}{\sigma}{\sigma\!-\!P} \vert \!\!\!\! &=&\!\!\!\! \vert \frac{[d_{K+R}][2P]![2K\!\!+\!\!R\!\!-\!\!P]![K\!\!+\!\!R\!\!+\!\!P\!\!-\!\!\sigma]![K\!\!+\!\!\sigma]!  
}{[P\!\!-\!\!R]![R\!\!+\!\!P]![2K\!\!+\!\!R\!\!+\!\!P\!+\!\!1]![K\!\!+\!\!R\!\!-\!\!P\!\!+\!\!\sigma]![K\!\!-\!\!\sigma]!}\vert\nonumber\\  
&\leq& C_1 \; q^{2KP}\nonumber 
\end{aligned}$$ Using $\Lambda^{K K+R}_{P}(X_0X_1) \leq C_2 \;K q^{2K}$, we obtain that the series is absolutely and uniformly convergent. Using ([\[systan\]](#systan){reference-type="ref" reference="systan"})([\[intlambda\]](#intlambda){reference-type="ref" reference="intlambda"})([\[contra\]](#contra){reference-type="ref" reference="contra"})([\[lambda3j\]](#lambda3j){reference-type="ref" reference="lambda3j"}) we have $$\begin{aligned}
&&\hskip -1cm\int d{\cal P}(X_0X_1)\;\left(\sum_{KM}\qd{K} \Clebpsi{K}{\;P}{\;\;M}{\sigma}{-P}{\sigma-P}\Clebphi{\;P}{K}{\;\;M}{-P}{\sigma}{\sigma-P}\Lambda^{KM}_{P}(X_0X_1)\right) \Lambda^{AC}_{P}(X_0X_1)=\nonumber\\  
&&\hskip -1cm=\sum_{KM}\qd{K} \Clebpsi{K}{\;P}{\;\;M}{\sigma}{-P}{\sigma-P}\Clebphi{\;P}{K}{\;\;M}{-P}{\sigma}{\sigma-P} \int d{\cal P}(X_0X_1) \Lambda^{KM}_{P}(X_0X_1) \Lambda^{AC}_{P}(X_0X_1)=\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1cm=\sum_{KM}\qd{K} \Clebpsi{K}{\;P}{\;\;M}{\sigma}{-P}{\sigma-P}\Clebphi{\;P}{K}{\;\;M}{-P}{\sigma}{\sigma-P}   
\sum_{JU} \frac{(\qn{2U\!+\!1}\qn{2P\!+\!1})^{\frac{1}{2}}}{(\qn{2C\!+\!1}\qn{2M\!+\!1})^{\frac{1}{2}}e^{i \pi (C+M-P-U)}}\times\nonumber\\  
&&\times\sixjn{A}{M}{U}{K}{C}{P}{0}\!\!\!\sixjn{K}{U}{C}{P}{A}{J}{0}\!\!\!\sixjn{P}{U}{J}{A}{K}{M}{0}.  
\int d{\cal P}(X_0X_1) \Lambda^{JU}_{P}(X_0X_1) =\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1cm=\sum_{KM}\qd{K} \Clebpsi{K}{\;P}{\;\;M}{\sigma}{-P}{\sigma-P}\Clebphi{\;P}{K}{\;\;M}{-P}{\sigma}{\sigma-P}  
e^{2i\pi A} \delta_{A,K}\frac{\qd{P}}{\qd{A}} \sixjn{A}{M}{P}{A}{C}{P}{0}=\nonumber\\  
&&\hskip -1cm=\sum_{M} \qd{M} \Clebphi{\;\;M}{A}{\;P}{P-\sigma}{\sigma}{P}\Clebpsi{A}{\;\;M}{\;P}{\sigma}{P-\sigma}{P}  
 \sixjn{A}{M}{P}{A}{C}{P}{0}=\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1cm=\sum_{M}\qd{M} \sixjn{A}{M}{P}{A}{C}{P}{0} \frac{\hbar}{2\pi}\int^{\frac{\pi}{\hbar}}_{-\frac{\pi}{\hbar}} d\rho \; q^{2i \sigma \rho} \Lambda^{AM}_{P}(P,\rho).\nonumber  
\end{aligned}$$ Then we use the relation $$\begin{aligned}
&&\hskip -1cm \sum_{M}\qd{M}\sixjn{A}{M}{P}{A}{C}{P}{0}\!\!\!\!\Lambda^{AM}_{P}(X_0X_1)=e^{-2i\pi A}\qd{P}\;\Lambda^{AC}_{P}(X_1X_0).\nonumber  
\end{aligned}$$ which has been proved in [@BR1] and which is the key point to prove unitarity of the representation and the relation $$\begin{aligned}
\hskip -1cm\int^{\frac{\pi}{\hbar}}_{-\frac{\pi}{\hbar}}  d\rho \; q^{2i \sigma \rho} \Lambda^{AC}_{P}(-P,\rho)=  
\int^{\frac{\pi}{\hbar}}_{-\frac{\pi}{\hbar}}  d\rho \; q^{-2i \sigma \rho} \Lambda^{AC}_{P}(P,\rho)  
\end{aligned}$$ which is proved using twice ([\[lambda3j\]](#lambda3j){reference-type="ref" reference="lambda3j"}),([\[contra\]](#contra){reference-type="ref" reference="contra"}) and ([\[intlambda\]](#intlambda){reference-type="ref" reference="intlambda"}). Combining these two steps, we obtain $$\begin{aligned}
&&\hskip -1cm\int d{\cal P}(X_0X_1)\;\left(\sum_{KM}\qd{K} \Clebpsi{K}{\;P}{\;\;M}{\sigma}{-P}{\sigma-P}\Clebphi{\;P}{K}{\;\;M}{-P}{\sigma}{\sigma-P}\Lambda^{KM}_{P}(X_0X_1)\right) \Lambda^{AC}_{P}(X_0X_1)=\nonumber\\  
&&=\int d{\cal P}{(X_0X_1)} \;\frac{\hbar\;e^{2i \pi \sigma} \qd{P}q^{-2 \sigma (X_0+X_1+1)}\delta_{X_0-X_1,P}}{2\pi\; {\cal P}{(X_0X_1)}} \Lambda^{AC}_{P}(X_0X_1).\nonumber  
\end{aligned}$$ Finally using Lemma 1 we conclude this proof.
