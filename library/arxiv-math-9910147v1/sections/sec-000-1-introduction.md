---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.994
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
In [@BR1] we have pursued the work of Podles-Woronowicz [@PW] and Pusz [@Pu]: we have shown that the unitary representations of ${\mathfrak U}_q(sl(2,\mathbb{C})_{\RR})$ can be nicely expressed in terms of one variable complex continuation of $6j$ symbols of ${\mathfrak U}_q(su(2))$. Using this result we were able to construct the characters of these unitary representations and prove a Plancherel theorem for $L^2$ functions. One has to work in the category of $C^{*}$ multiplier Hopf algebras [@PW; @Wo2] in order to handle functional analysis problems.\
Let $G$ be the complex Lie group $SL(2,\mathbb{C})$ and denote by $\{{\buildrel {\lambda} \over {\Pi}}, \lambda\in  {\frac{1}{2}}\mathbb{Z}\times \RR\}$ the set of principal unitary representations of $G$. The Plancherel measure is given by $P(\lambda)d\lambda = {\frac{1}{2}}(m^2+\rho^2)d\rho$ where $\lambda=(m, \rho)$ and ${\buildrel {\lambda} \over {\Pi}}$ is equivalent to ${\buildrel {-\lambda} \over {\Pi}}$. Naimark [@N] has shown the following decomposition theorem:

$${\buildrel {\!{}_{(m,\rho)}} \over {\Pi}}\otimes {\buildrel 
{\!{}_{(m',\rho')}} \over {\Pi}}=  \bigoplus_{m''\in J_{m,m'} }  \int^{\oplus} 
\!\!\!d\rho'' \;\; {\buildrel {{}_{(m'',\rho'')}} \over {\Pi}}$$

where $J_{m,m'}=\{m\in \onehalf\ZZ, m+m'+m''\in \ZZ\}.$ The aim of the present article is to prove the quantum analog of this theorem and to give explicit formulae for the Clebsch-Gordan coefficients associated to this decomposition.

Let us also denote by $\{ {\buildrel {\lambda} \over {\Pi}},   \lambda\in 
\frac{1}{2}\mathbb{Z}\times ]-\frac{\pi}{\hbar},\frac{\pi}{\hbar}] \}$, where $q=e^{-\hbar},$ the set of principal representations of ${\mathfrak 
U}_q(sl(2,\mathbb{C})_{\RR}).$ The representation ${\buildrel {\lambda} \over 
{\Pi}}$ is a unitary representation of ${\mathfrak 
U}_q(sl(2,\mathbb{C})_{\RR})$ with domain $V_{\lambda}.$ We have shown in [@BR1], that these representations can be constructed using complex continuation in one variable (namely $\rho$) of $6j$ of ${\mathfrak 
U}_q(su(2)).$ Let us denote by $6j(1)$ the complex continuation of these coefficients to distinguish them from the $6j$ of finite dimensional representations of ${\mathfrak U}_q(su(2)),$ which will be denoted by $6j(0).$ We have shown that the Plancherel measure is $P(\lambda)d\lambda 
= (q-q^{-1})^2\frac{\hbar}{4 \pi}[m+i\rho][m-i\rho]d\rho$ where $\lambda=(m, 
\rho).$

In section 2 we recall definitions and properties of $6j(0)$ and $6j(1).$ We then introduce and study the basic properties of complex continuations, in three independent continuous spins, of $6j$ symbols that we call $6j(3).$ We review the main theorems of harmonic analysis on $SL_q(2,\CC)_{\RR}$ which are needed in the sequel.

In section 3 we study the space of intertwiners $\Phi^{\lambda\lambda'}_{\lambda''} :  
V_{\lambda}\otimes V_{\lambda'}\rightarrow  V_{\lambda''},$ and give an expression for them in terms of $6j(1)$ and $6j(3).$ Even in the classical case, such a simple expression of $\Phi^{\lambda\lambda'}_{\lambda''}$ was not known. We can define a linear map, denoted ${\hat \Phi},$ from $V_{\lambda}\otimes V_{\lambda'}$ to $\int^{\oplus} \!d\lambda''{\buildrel 
{\;\lambda''} \over {\Pi}},$ by associating to each $u\in  
V_{\lambda}\otimes V_{\lambda'}$ the map $\lambda''\mapsto\Phi^{\lambda 
\lambda'}_{\lambda''}(u).$ It remains to show that we can find a normalization $N(\lambda,\lambda',\lambda'')$ of $\Phi^{\lambda 
\lambda'}_{\lambda''}$ in such a way that ${\hat \Phi}$ is an isometry. This cannot easily be obtained from the definition of the $\Phi^{\lambda\lambda'}_{\lambda''}$ in terms of $6j(3).$

We therefore use another construction of the intertwiners using the quantum analogue of the operator $\int dh(g) \; {\buildrel {\lambda} \over {\Pi}}(g)\otimes 
{\buildrel {\lambda'} \over {\Pi}}(g)  \otimes {\buildrel {\;\lambda''} \over 
{\Pi}}(g^{-1})$ where $dh$ is the Haar measure. By using the relations between these operators and the $\Phi^{\lambda \lambda'}_{\lambda''}$ we are able to compute the normalization factor. This is the content of section 4.

In section 5 we show that with this choice of normalization ${\hat 
\Phi}$ is an isometry. We then show that $\Phi^{\lambda 
\lambda'}_{\lambda''}$ is expressed in terms of $q-$ Racah polynomials and Askey-Wilson polynomials. As a result this last property implies non trivial identities which mix q-Racah polynomials and Askey-Wilson polynomials.

It is important to keep in mind the following hierarchy of complex continuations of $6j$ symbols of ${\mathfrak U}_q(su(2))$:

-   $6j(0)$ are defined as being Racah coefficients (i.e recoupling coefficients) of finite dimensional representations of ${\mathfrak 
    U}_q(su(2)).$

<!-- -->

-   $6j(1)$ are building blocks of matrix elements of unitary representations of ${\mathfrak 
    U}_q(sl(2,\mathbb{C})_{\RR}).$ They are matrix elements of the universal shifted cocycle [@BBB] and are equivalent to the Fusion Matrix of [@EV].

-   $6j(3),$ as we will show, are building blocks of the Clebsch-Gordan coefficients associated to the tensor product of principal representations of ${\mathfrak U}_q(sl(2,\mathbb{C})_{\RR}).$ For the moment there is no real understanding of these $6j(3)$ in terms of Fusion matrix or as matrix elements of some universal element.

There also exists a final level of this hierarchy, called $6j(6)$, where the 6 spins are arbitrary complex numbers. They are the building blocks of the Racah coefficients of principal representations of ${\mathfrak 
U}_q(sl(2,\mathbb{C})_{\RR}).$ Their expressions in terms of basic hypergeometric functions, as well as their properties will be given in [@BR2].
