---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-003-22-definitions-and-properties-of-continuation-of
section_title: "Definitions and properties of continuation of quantum $6j$ symbols"
section_number: 2.2
pages: 5-10
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 1.0
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
In order to understand the problem of continuation of quantum $6j$ symbols the reader is invited to read the appendix of [@BR1] where definitions, proofs, as well as references on $6j(1)$ are given.

Let us give a definition which is essential in order to describe the complex continuations of quantum $6j$ symbols (the notations are explained in the appendix of the present work).

::: definition
Let $\XX=\{(T,U,V,X,Y,Z)\in \CC^6, (2T, T+U-V, T+V-U, T+Y-Z, T+Z-Y)\in \NN^5\},$ we define for any $(T,U,V,X,Y,Z)\in \XX,$ $$\begin{aligned}
\hskip -0.5cm\nor6j{X}{Y}{V}{T}{U}{Z} \!\!\!\!&=&\!\!\!\!  
\;\;e^{i\pi (T+Y-Z)} \;q^{(T+Y-Z)(U-T+Y-X+1)+(V+Y-X)(T+V-U)}\nu_{1}(d_Z)\nu_{1}(d_V)  
\times\nonumber\\  
&&\times\frac{(U\!-\!T\!+\!X\!-\!Y\!+\!1)_{\infty}\;\;\omega(Y;V,X)\omega(T;Y,Z)\omega(T;V,U)}{\!\!  
(T\!-\!U\!+\!X\!+\!Y\!+\!1)_{\infty}(2T+1)_{\infty}(1)_{\infty}\;\;\omega(U;X,Z)  
}\nonumber\\  
\hskip -0.5cm\valsixj{X}{Y}{V}{T}{U}{Z}\!\!\!\!&=&\!\!\!\!\nor6j{X}{Y}{V}{T}{U}{Z}\!  
{}_4\Phi_3\!  
\left[\!\!\begin{array}{cccc} \mbox{\it \small U$-\!$V$-\!$T} &\; \mbox{\it \small U$+\!$V$-\!$T$+\!$1} & \;\;\mbox{\it \small Z$-\!$Y$-\!$T} & \;\;\;\mbox{\it \small $-\!$Z$-\!$Y$-\!$T$-\!$1}\\  
& \hskip -2cm\mbox{\it \small $-\!2$T} & \hskip -1.8cm\mbox{\it \small $\!-\!$Y$-\!$X$-\!$T$+\!$U} & \hskip -1cm \mbox{\it \small U$+\!$X$-\!$Y$-\!$T$+\!$1} \end{array} \!\!\right].  
\end{aligned}$$
:::

It is important to understand that for $(T,U,V,X,Y,Z)\in \XX,$ $\nor6j{X}{Y}{V}{T}{U}{Z}$ and $\valsixj{X}{Y}{V}{T}{U}{Z}$ are both square roots of rational functions in the variables $q^{2T}, q^{2U},q^{2V}, q^{2X},q^{2Y}, q^{2Z}.$ This is a simple consequence of the fact that the hypergeometric series is of terminating type.

We have been very cautious with the determination of the signs. This annoying problem already appeared in the case of $6j(0)$ but can be handled quite easily. This problem is strengthned in the case of $6j(1)$ and $6j(3)$ because in that case we really have to take square roots of complex numbers. This is the reason why we introduced a particular square root, denoted $\nu_{\infty}(x)$ of the Eulerian product $(x)_{\infty}$ for $x\in \CC.$

It will sometimes be useful to have the explicit value of the $6j$ symbols when one of the spins is equal to $0$ or $\onehalf$. From the last definition we easily get: $$\begin{aligned}
&&\forall A,B,C \in \CC, \valsixj{A}{B}{C}{0}{C}{B}=1\label{sixjzerocont}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1.5cm\valsixj{A}{B}{C}{\onehalf}{C+\onehalf}{B+\onehalf}=\frac{\nu_1(B+C-A+1)\nu_1(A+B+C+2)}{\nu_1(2C+2)\nu_1(2B+1)}\nonumber  
\end{aligned}$$ $$\begin{aligned}
&&\valsixj{A}{B}{C}{\onehalf}{C+\onehalf}{B-\onehalf}=\;-\;\frac{\nu_1(A+B-C)\nu_1(A+C-B+1)}{\nu_1(2C+2)\nu_1(2B+1)}\;q^{C+B-A+1}\nonumber  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -0.75cm\valsixj{A}{B}{C}{\onehalf}{C-\onehalf}{B+\onehalf}=\frac{\nu_1(A+C-B)\nu_1(A+B-C+1)}{\nu_1(2C)\nu_1(2B+1)}\;q^{C+B-A}\nonumber  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -2cm\valsixj{A}{B}{C}{\onehalf}{C-\onehalf}{B-\onehalf}=\frac{\nu_1(A+B+C+1)\nu_1(C+B-A)}{\nu_1(2C)\nu_1(2B+1)}.\label{sixjonehalfcont}  
\end{aligned}$$

The usual $6j(0)$ symbols which properties were described in the last section and denoted $\sixjn{D}{E}{C}{A}{B}{F}{0}$ where $A,B,C,D,E,F \in \halfinteger,$ are given by:

$$\begin{aligned}
\sixjn{D}{E}{C}{A}{B}{F}{0}=\valsixj{D}{E}{C}{A}{B}{F}  Y^{(0)}_{(A,B,C)} Y^{(0)}_{(A,E,F)}  Y^{(0)}_{(D,B,F)} Y^{(0)}_{(D,E,C).}  
\end{aligned}$$ This expression can easily be obtained from the usual expressions [@KR; @Ge] using the inversion relation and the Sears identities ([\[inversionrelation\]](#inversionrelation){reference-type="ref" reference="inversionrelation"},[\[sears\]](#sears){reference-type="ref" reference="sears"}) recalled in the appendix.

In the previous formula, and in the following ones, we will make a distinction between the first part of the right handside, which is called \"explicit value\", and the second part, products of $Y$ functions and called \"selection rules\".

In order to describe properties of continuation of 6j symbols, we will make in the sequel a convenient abuse of notation, which greatly simplifies formulae:\
if $X_1\in \CC$ is fixed, if $k$ is a positive integer and $f:\CC^{k+1}\rightarrow \CC$ is a function, a series of the type $\sum_{X_2,X_3,...,X_k}f(X_1,X_2,...,X_k)$ will always be defined as $$\sum_{X_2,X_3,...,X_k}f(X_1,X_2,...,X_k)=\sum_{n_1,n_2,...,n_k \in \onehalf\ZZ}f(X_1, X_1+n_1,...,X_k+n_k).$$

Note that we will only use the notation $X_0, X_1$ to denote a couple of complex numbers such that $X_0=-{\overline {X_1}}-1,$ and $X_0-X_1 \in\onehalf \ZZ,$ (this notation will be explained in the next part.)

Let us define the involutive endomorphism of the complex line: $\forall X\in \CC, X\mapsto \underline{X}=-X-1,$ as we will see it is important to understand the action of this symmetry on the $6j$ symbols.

In [@CGR; @BR1] two types of $6j(1)$ symbols were defined. The first type is a family of numbers denoted $\sixjn{X_1}{X_2}{C}{A}{B}{X_3}{1}$ and the second one is denoted $\sixjn{B}{X_1}{X_3}{A}{X_2}{X_4}{1},$ where both are defined for $A,B,C \in \halfinteger, \forall i,j \in \{1,\cdots,4\}, X_i \in \CC-\halfinteger, X_i\!-\!X_j \in \onehalf\ZZ.$

Their explicit expressions are given by $$\begin{aligned}
&&\hskip -1.35cm\sixjn{X_1}{X_2}{C}{A}{B}{X_3}{1}\!\!\!\!\!=\!\valsixj{X_1}{X_2}{C}{A}{B}{X_3}  Y^{(1)}_{(A,X_2-X_3)} Y^{(1)}_{(B,X_1-X_3)}  Y^{(1)}_{(C,X_1-X_2)} Y^{(0)}_{(A,B,C)},\nonumber\\ 
&&\hskip -1.35cm\sixjn{B}{X_1}{X_3}{A}{X_2}{X_4}{1}\!\!\!\!\!=\!\valsixj{B}{X_1}{X_3}{A}{X_2}{X_4}  Y^{(1)}_{(A,X_2-X_3)} Y^{(1)}_{(A,X_1-X_4)}  Y^{(1)}_{(B,X_1-X_3)} Y^{(1)}_{(B,X_2-X_4)}.  
\end{aligned}$$ These formulae deserve some remarks, concerning the very word of \"continuation\". The explicit value of the $6j(1)$ is a regular function when the $X_i$ approach half-integer values, but the selection rules appears to be different, i.e the support of the continuated 6j(1) are larger than that of the 6j(0) symbols. Nethertheless, for fixed $I,J\in \halfinteger,$ and for a sufficiently large half-integer $K$ we have $Y^{(1)}_{(I,J)}= Y^{(0)}_{(I,K,J+K)}.$ It is in this sense that the term "continuation" to complex spins has been used.

From arguments developped in [@CGR; @BR1], we can check different polynomial identities which are the continuation of the properties satisfied by the 6j(0). Rather than being exhaustive we will just mention some of them which will be important in our present work:

::: proposition
$$\begin{aligned}
&&\hskip -1cm\sixjn{X_1}{X_2}{C}{A}{B}{X_3}{1}\!\!\!\!=\!\sixjn{X_2}{X_1}{C}{B}{A}{X_3}{1}\!\!\!\!=\!(e^{i \pi}q)^{(X_1-X_3+A-C)}  
\frac{\nu_1(d_C)\nu_1(d_{X_3})}{\nu_1(d_A)\nu_1(d_{X_1})}\sixjn{X_3}{X_2}{A}{C}{B}{X_1}{1},\nonumber\\  
&&\hskip -1cm\sixjn{B}{X_1}{X_3}{A}{X_2}{X_4}{1}\!\!\!\!=\!\sixjn{B}{X_2}{X_4}{A}{X_1}{X_3}{1}=\sixjn{A}{X_2}{X_3}{B}{X_1}{X_4}{1}\!\!\!\!=\!\!\nonumber\\  
&&\hskip 3cm=\!(e^{i \pi}q)^{(X_1-X_3+X_2-X_4)}  
\frac{\nu_1(d_{X_4})\nu_1(d_{X_3})}{\nu_1(d_{X_2})\nu_1(d_{X_1})} \sixjn{B}{X_4}{X_2}{A}{X_3}{X_1}{1},\label{symcont}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -2cm\sum_{C}\sixjn{X_1}{X_2}{C}{A}{B}{X_3}{1}\!\sixjn{X_1}{X_2}{C}{A}{B}{X_4}{1}=\delta_{X_3,X_4}Y^{(1)}_{(A,X_2-X_3)}Y^{(1)}_{(B,X_1-X_3)},\label{ortho1cont}\\ 
&&\hskip -2cm\sum_{X_3}\!\sixjn{X_1}{X_2}{C}{A}{B}{X_3}{1}\!\sixjn{X_1}{X_2}{D}{A}{B}{X_3}{1}=\delta_{C,D}Y^{(0)}_{(A,B,C)}Y^{(1)}_{(C,X_1-X_2)},\label{ortho2cont}\\ 
&&\hskip -2cm\sum_{X_3}\!\sixjn{B}{X_1}{X_3}{A}{X_2}{X_4}{1}\!\sixjn{B}{X_1}{X_3}{A}{X_2}{X_5}{1}=\delta_{X_4,X_5}Y^{(1)}_{(A,X_1-X_4)}Y^{(1)}_{(B,X_2-X_4)},\label{ortho3cont} 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1.5cm\sum_{C}\!\sixjn{X_2}{X_1}{C}{A}{B}{X_3}{1}\!\!\sixjn{X_1}{X_2}{C}{A}{B}{X_4}{1}\!(\frac{v_{X_4}^{1/2}v_{X_3}^{1/2}v_{C}^{1/2}}{v_{X_1}^{1/2}v_{X_2}^{1/2}v_{A}^{1/2}v_{B}^{1/2}})^{\pm 1}\!=\!\sixjn{B}{X_2}{X_3}{A}{X_1}{X_4}{1},\label{racahcont}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1.3cm\sum_{A}\!\sixjn{X_3}{X_1}{A}{D}{F}{X_4}{1}\!\!\!\sixjn{E}{B}{A}{D}{F}{C}{0}\!\!\!\sixjn{X_1}{X_2}{B}{E}{A}{X_3}{1}\!\!\!\!\!=\!\sixjn{X_4}{X_2}{C}{E}{F}{X_3}{1}\!\!\!\sixjn{X_2}{X_1}{B}{D}{C}{X_4}{1},\label{penta1cont}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1cm \sum_{X_6}\!\sixjn{D}{X_6}{X_4}{C}{X_1}{X_2}{1}\!\!\!\sixjn{A}{X_5}{X_6}{C}{X_2}{X_3}{1}\!\!\!\sixjn{X_4}{X_5}{B}{A}{D}{X_6}{1}\!\!\!\!\!=\!\sixjn{B}{X_5}{X_4}{C}{X_1}{X_3}{1}\!\!\!\sixjn{X_1}{X_3}{B}{A}{D}{X_2}{1}\!\!,\label{penta2cont}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1.3cm\sum_{X_5}\!\sixjn{X_2}{X_1}{P}{B}{A}{X_5}{1}\!\!\!\sixjn{X_4}{X_5}{M}{A}{Q}{X_2}{1}\!\!\!\sixjn{X_4}{X_1}{N}{B}{M}{X_5}{1}\!\!\!\!\!=  
\!\sixjn{Q}{N}{P}{B}{A}{M}{0}\!\!\!\sixjn{X_4}{X_1}{N}{P}{Q}{X_2}{1},\label{penta3cont}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1.3cm\sum_{M}\!\sixjn{X_4}{X_3}{M}{A}{P}{X_2}{1}\!\sixjn{B}{N}{M}{A}{P}{C}{0}\!\sixjn{X_4}{X_1}{N}{B}{M}{X_3}{1}  
(\frac{v_P^{1/2}v_{X_3}^{1/2}}{v_M^{1/2}v_{X_2}^{1/2}})^{\pm 1}=\nonumber\\  
&&\hskip 1cm=\sum_{X_5}\!\sixjn{X_4}{X_5}{C}{B}{P}{X_2}{1}\!\sixjn{B}{X_1}{X_3}{A}{X_2}{X_5}{1}\!\sixjn{X_4}{X_1}{N}{A}{C}{X_5}{1}  
(\frac{v_C^{1/2}v_{X_1}^{1/2}}{v_N^{1/2}v_{X_5}^{1/2}})^{\pm 1}.\label{hexacont}  
\end{aligned}$$
:::

It is important to stress that every sums in the previous formulae are finite sums because of the selection rules entering into the definitions of $6j(1).$

We also have the following symmetry:

::: proposition
[]{#propsym6j1 label="propsym6j1"} $$\begin{aligned}
&&\hskip -1cm  
\sixjn{\underline{X_1}}{\underline{X_2}}{C}{A}{B}{\underline{X_3}}{1}=  
\sixjn{X_1}{X_2}{C}{A}{B}{X_3}{1}  
(-1)^{A+B-C}  
\label{symbiz6j1}  
\end{aligned}$$
:::

From the Sears identity and the inversion relation ([\[sears\]](#sears){reference-type="ref" reference="sears"}, [\[inversionrelation\]](#inversionrelation){reference-type="ref" reference="inversionrelation"}) we easily obtain the relation:

$\sixjn{\underline{X_1}}{\underline{X_2}}{C}{A}{B}{\underline{X_3}}{1}=  
\sixjn{X_1}{X_2}{C}{A}{B}{X_3}{1}  
f(A,B,C,X_1,X_1,X_3)$ where $$f(A,B,C,X_1,X_1,X_3)=(-1)^{2A}\frac{\varphi_{(A+X_2+X_3,2A+1)}  
\varphi_{(C+X_1+X_2,2C+1)}}{\varphi_{(2X_3+1,1)}\varphi_{(B+X_1+X_3,2B+1)}}.$$ Using the explicit expression of $\phi(\alpha,n)$ for $n\in \ZZ$ explained in the appendix, we conclude that $f=(-1)^{A+B-C}.$

In order to obtain neat expressions for the Clebsch-Gordan coefficients of principal representations of the quantum Lorentz group, it is necessary to introduce a new level in this hierarchy of continuations of $6j$ symbols.

::: definition
We will define $6j(3)$ symbols to be the family of numbers denoted $\sixjn{Z_1}{Y_1}{X_2}{A}{X_1}{Y_2}{3}$ where $A \in \halfinteger, X_1,X_2,Y_1,Y_2,Z_1 \in \CC-\halfinteger, X_1\!-\!X_2 \in \onehalf\ZZ,Y_1\!-\!Y_2 \in \onehalf\ZZ$ and defined by $$\begin{aligned}
\sixjn{Z_1}{Y_1}{X_2}{A}{X_1}{Y_2}{3}=\valsixj{Z_1}{Y_1}{X_2}{A}{X_1}{Y_2}\;Y^{(1)}_{(A,X_1-X_2)}Y^{(1)}_{(A,Y_1-Y_2)}.  
\end{aligned}$$
:::

These $6j(3)$ satisfy properties, which will be used in the rest of the paper and which are continuation of the identities satisfied by $6j(0)$ and $6j(1).$ We prefered to give combinatorial proofs of these properties rather than continuation arguments, in order to prepare to the $6j(6)$ case. Here again, the sums are finite which is a consequence of the selection rules in the definition of $6j(3)$. Note that these $6j(3)$ satisfy other relations, which will be explained in the section 5, as consequences of the study of the tensor product of principal representations of the quantum Lorentz group.

::: proposition
The following symmetry properties are satisfied: $$\begin{aligned}
&&\hskip -1.4cm\sixjn{Z_1}{Y_1}{X_2}{A}{X_1}{Y_2}{3}\!\!\!\!=\!  
\sixjn{Z_1}{X_1}{Y_2}{A}{Y_1}{X_2}{3}\!\!\!\!=\!(e^{i \pi}q)^{(X_1-X_2+Y_1-Y_2)}  
\frac{\nu_1(d_{X_2})\nu_1(d_{Y_2})}{\nu_1(d_{X_1})\nu_1(d_{Y_1})}  
\sixjn{Z_1}{Y_2}{X_1}{A}{X_2}{Y_1}{3}.\label{sym6j3}  
\end{aligned}$$
:::

Simple use of Sears identity ([\[sears\]](#sears){reference-type="ref" reference="sears"}).

::: proposition
We also have a discrete orthogonality property $$\begin{aligned}
\sum_{X_2}\sixjn{Z_1}{Y_1}{X_2}{A}{X_1}{Y_2}{3}\sixjn{Z_1}{Y_1}{X_2}{A}{X_1}{Y_3}{3}=\delta_{Y_2,Y_3}Y^{(1)}_{(A,Y_1-Y_2)}.\label{ortho16j3}  
\end{aligned}$$
:::

This is equivalent to the orthogonality of q-Racah polynomials (see our appendix for notations ([\[defracahpol\]](#defracahpol){reference-type="ref" reference="defracahpol"}) and [@W][@AW1] for proofs): $$\begin{aligned}
\sum_{x=0}^{N} w^{(R)}(x;a,b,c,d) p^{(R)}_n(\mu(x);a,b,c,d) p^{(R)}_m(\mu(x);a,b,c,d)=\delta_{n,m}h^{(R)}_n(a,b,c,d),  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -4cm\mbox{because }\;\;\;\;\;\nor6j{Z_1}{Y_1}{X_2}{T}{X_1}{Y_2}^2 =\frac{w^{(R)}(x;a,b,c,d)}{h^{(R)}_n(a,b,c,d)}, \mbox{and}\nonumber 
 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1.5cm{}_4\Phi_3\!\left[\!\!\begin{array}{cccc} \mbox{\it \small $X_1\!-\!X_2-\!$T} &\; \mbox{\it \small $X_1\!+\!X_2-\!$T$\;+$1} & \;\;\;\;\;\mbox{\it \small $Y_2\!-\!Y_1-\!$T} & \;\;\;\mbox{\it \small $-Y_2\!-\!Y_1\!-\!$T$-\!$1}\\ & \hskip -3.5cm\mbox{\it \small $-\!2$T} & \hskip -3.5cm\mbox{\it \small $\!-\!Y_1\!-\!Z_1-\!$T$\;+\!X_1$} & \hskip -1.8cm \mbox{\it \small $X_1+Z_1\!-\!Y_1\!-\!$T$\;+$1} \end{array} \!\!\right]\!\!=p^{(R)}_n(\mu(x);a,b,c,d),\nonumber\\  
&&\mbox{with}\;\;\;\;\;n=T\!+\!X_2\!-\!X_1, \;x=T\!+\!Y_1\!-\!Y_2,\; N=2T,\nonumber\\  
&& a=q^{-4T-2},\; b=q^{4X_1+2}, \; c=q^{2(Z_1+X_1-Y_1-T)},\; d=q^{-2(Z_1+Y_1+X_1+T+2)}.  
\end{aligned}$$

These $6j(3)$ symbols satisfy the pentagonal relations:

::: proposition
$$\begin{aligned}
&&\hskip -1.2cm\sum_C\!\sixjn{Y_3}{Y_2}{C}{A}{B}{Y_1}{1}\!\!\sixjn{X_1}{X_2}{C}{B}{A}{X_3}{1}\!\!\sixjn{Z_1}{Y_3}{X_2}{C}{X_1}{Y_2}{3}\!\!\!\!=\sixjn{Z_1}{Y_1}{X_3}{A}{X_1}{Y_2}{3}\!\!\sixjn{Z_1}{Y_3}{X_2}{B}{X_3}{Y_1}{3},\label{penta1sixj3}\\  
&&\hskip -1.2cm\sum_{X_3}\!\sixjn{Z_1}{Y_3}{X_3}{B}{X_2}{Y_1}{3}\!\!\sixjn{B}{X_3}{X_2}{A}{X_1}{X_4}{1}\!\!\sixjn{Y_3}{Z_1}{X_3}{A}{X_4}{Z_2}{3}\!\!\!\!=\sixjn{Y_1}{Z_1}{X_2}{A}{X_1}{Z_2}{3}\!\!\sixjn{Z_2}{Y_3}{X_4}{B}{X_1}{Y_1}{3}.\label{penta2sixj3}  
\end{aligned}$$
:::

These identities are simply proved by induction on $A.$ Indeed, for $A=0$ these identities are trivial and for $A=\onehalf$ they are easily checked on the exact expression of the $6j(3)$ using the finite difference equations verified by basic hypergeometric functions. The induction easily follows from the use of orthogonality and pentagonal equations on $6j(1).$\

Finally, we have a Racah relation:

::: proposition
$$\begin{aligned}
\sum_{Y_2}\sixjn{Z_2}{X_1}{Y_2}{A}{Y_1}{X_2}{3}\sixjn{X_1}{Y_1}{Z_1}{A}{Z_2}{Y_2}{3}(\frac{v^{1/2}_{Y_2}v^{1/2}_{Z_1}v^{1/2}_{X_2}}{v^{1/2}_{Z_2}v^{1/2}_{Y_1}v^{1/2}_{X_1}v^{1/2}_{A}})^{\pm 1}=\sixjn{Y_1}{Z_2}{X_2}{A}{X_1}{Z_1}{3}\label{racah6j3}  
\end{aligned}$$
:::

It can be proved by continuation arguments from the $6j(1)$ case.

We can prove other identities, which will be useful in the following chapters, and which are direct consequences of the previous ones.

::: proposition
The following pentagonal equations are satisfied: $$\begin{aligned}
\sum_{X_2}\sixjn{Y_1}{Z_3}{X_2}{C}{X_1}{Z_2}{3}\!\!\sixjn{X_1}{X_3}{B}{A}{C}{X_2}{1}\!\!\sixjn{Y_1}{Z_1}{X_3}{A}{X_2}{Z_3}{3}\!\!=\!\sixjn{Y_1}{Z_1}{X_3}{B}{X_1}{Z_2}{3}\!\!\sixjn{Z_1}{Z_2}{B}{C}{A}{Z_3}{1},\label{penta36j3}\\  
\sum_{Z_2}\sixjn{Y_1}{Z_1}{X_2}{A}{X_4}{Z_2}{3}\sixjn{Z_2}{Y_1}{X_4}{B}{X_1}{Y_2}{3}\sixjn{Y_2}{Z_1}{X_3}{A}{X_1}{Z_2}{3}=\sixjn{B}{X_2}{X_3}{A}{X_1}{X_4}{1}\sixjn{Z_1}{Y_1}{X_2}{B}{X_3}{Y_2}{3}.\label{penta46j3}  
\end{aligned}$$
:::

It is obtained from the pentagonal relations ([\[penta1sixj3\]](#penta1sixj3){reference-type="ref" reference="penta1sixj3"})([\[penta2sixj3\]](#penta2sixj3){reference-type="ref" reference="penta2sixj3"}) and the discrete orthogonality relation ([\[ortho16j3\]](#ortho16j3){reference-type="ref" reference="ortho16j3"}).

We also have the hexagonal equation:

::: proposition
$$\begin{aligned}
&&\hskip -1cm\sum_{C}\frac{v^{1/2}_{C}v^{1/2}_{Y_2}}{v^{1/2}_{B}v^{1/2}_{Y_1}}\sixjn{Z_1}{X_1}{Y_1}{C}{Y_3}{X_2}{3}\sixjn{Y_3}{Y_1}{C}{A}{B}{Y_2}{1}\sixjn{X_1}{X_2}{C}{A}{B}{X_3}{1}=\nonumber\\  
&&\hskip 1cm=\sum_{Z_2}\frac{v^{1/2}_{X_2}v^{1/2}_{Z_2}}{v^{1/2}_{X_3}v^{1/2}_{Z_1}}\sixjn{Y_3}{Z_1}{X_2}{A}{X_3}{Z_2}{3}\sixjn{X_1}{Z_1}{Y_1}{A}{Y_2}{Z_2}{3}\sixjn{Z_2}{Y_3}{X_3}{B}{X_1}{Y_2}{3}.\label{hexa6j3}  
\end{aligned}$$
:::

It is obtained by applying successively ([\[racah6j3\]](#racah6j3){reference-type="ref" reference="racah6j3"})([\[penta1sixj3\]](#penta1sixj3){reference-type="ref" reference="penta1sixj3"})([\[penta46j3\]](#penta46j3){reference-type="ref" reference="penta46j3"})([\[racah6j3\]](#racah6j3){reference-type="ref" reference="racah6j3"}).

Finally the action of the automorphism of the complex line is given as follows:

::: proposition
[]{#propsym6j3 label="propsym6j3"} $$\sixjn{\underline{Z_1}}{\underline{Y_1}}{\underline{X_2}}{A}  
{\underline{X_1}}{\underline{Y_2}}{3}=\sixjn{Z_1}{Y_1}{X_2}{A}{X_1}{Y_2}{3}  
g(A,X_1,X_2,Z_1,Y_1,Y_2)(-1)^{Y_1-Y_2+X_1-X_2}\label{symbiz6j3}$$ where $g$ is a fourth root of unit which expression is: $$g=  
\frac{\varphi_{(-Y_2+X_1+Z_1,X_1-X_2+Y_1-Y_2)}  
\varphi_{(X_1+Y_2+Z_1+1,X_1-X_2+Y_2-Y_1)}  
\varphi_{(X_1+Y_2-Z_1,X_1-X_2+Y_2-Y_1)}}  
{\varphi_{(2Y_2+1,1)}  
\varphi_{(2X_2+1,1)}  
\varphi_{(Y_2+Y_1-A,-2A-1)}\varphi_{(X_1+X_2-A,-2A-1)}  
\varphi_{(Y_2+Z_1-X_1,Y_2-Y_1+X_2-X_1)}}.$$
:::

It is proved using the inversion relation and the Sears identity. Using the explicit expression for $\varphi(\alpha, n)$ with $n$ integer, we obtain that $g$ is a fourth root of unit, but there is no simpler formula for $g.$
