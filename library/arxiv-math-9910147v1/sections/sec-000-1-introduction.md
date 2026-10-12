---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-10
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.985
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

# Definition and properties of various continuations of 6j symbols of ${\mathfrak U}_q(su(2))$

Let us first recall some notations and results of [@BR1] which will be used throughout this work. The reader is also invited to read the first subsection of the appendix of the present article for definitions of basic hypergeometric functions.

## Intertwiners and 6j(0) of ${\mathfrak U}_q(su(2))$ 

Let $q=e^{-\hbar}$ with $\hbar\in \RR^{+*},$ ${\mathfrak U}_{q}(su(2))$ is the star Hopf algebra generated by $q^{\pm H}, J^{(\pm)}$ with the defining relations: $$\begin{aligned}
  && q^{H}J^{(\pm)}q^{-H}=q^{\pm 
1}J^{(\pm)},\;\;\;\;\;\;\;\;[J^{(+)},J^{(-)}]=\frac{q^{2H}-q^{-2H}}{q-q^{-1}},\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;(J^{(\pm)})^*=q^{\mp 1} J^{(\mp)},\nonumber\\  &&\Delta(J^{(\pm)})=q^{-H}\otimes J^{(\pm)}+J^{(\pm)}\otimes q^{H}, \;\;\;\;\;\;\;\;\Delta(q^{\pm H})=q^{\pm H} \otimes q^{\pm H},\;\;\;\;\;\;\;\;\;\;\;\;  (q^{H})^*=q^{H}.  
\end{aligned}$$ This Hopf algebra is a ribbon quasi-triangular Hopf algebra, with a universal $R-$matrix denoted $R.$ We will define as usual $R^{(+)}=R, R^{(-)}=R_{21}^{-1}$ and $\mu=q^{2H}.$

We will denote in the rest of this article $Irr({\mathfrak U}_{q}(su(2)))$ the set of all equivalence classes of finite dimensional irreducible unitary representations with $Sp(q^{H}) \in \RR^+.$ They are completely classified by a half-integer $K$ and we will denote by ${\buildrel K \over\pi}$ the representation of spin $K.$ The tensor product of elements of $Irr({\mathfrak U}_{q}(su(2)))$ is completely reducible in elements of $Irr({\mathfrak U}_{q}(su(2))).$ Let us define ${\buildrel K \over V}$ as being the vector space, of dimension $d_K=2K+1,$ associated to the representation of spin $K.$ Let $({\buildrel {{}_{K}} \over e}_m)_{m=-K \cdots K},$ be an orthonormal basis of ${\buildrel K \over V}$ such that ${\buildrel {{}_{K}} \over e}_m$ is of weight $q^m$ for the action of $q^H$. The central ribbon element that we choose is such that ${\buildrel K \over\pi}(v)=v_{K}id,$ where $v_K=e^{2i \pi K}q^{-2K(K+1)}.$ Note that we have included a sign in order to satisfy relation ([\[twistclebsch\]](#twistclebsch){reference-type="ref" reference="twistclebsch"}).

Let us introduce the following notation: $\forall I,J,K \in \halfinteger, \forall m \in \onehalf\ZZ$ we define $$\begin{aligned}
Y^{(0)}_{(I,J,K)}&=&  
\left\{\begin{array}{ll} 1\;\;\;\;\;\;  
\mbox{if\;\;\; $I\!+\!J\!-\!K, \;J\!+\!K\!-\!I,\; K\!+\!I\!-\!J \in \ZZ^+$} \\0 \;\;\;\;\;\;\mbox{otherwise}   
\end{array}\right.\\  
Y^{(1)}_{(I,m)}&=&  
\left\{\begin{array}{ll} 1\;\;\;\;\;\;  
\mbox{if\;\;\; $I+m,\; I-m \in \ZZ^+$} \\0 \;\;\;\;\;\; 
\mbox{otherwise.}\end{array}\right.  
\end{aligned}$$ Let us now recall some properties about braiding matrices, $3j$ and $6j$ symbols of the finite dimensional representations of ${\mathfrak U}_q(su(2)).$ We will always refer to conventions as well as explicit expressions given in [@BR1], see also [@KR; @Ge; @KV]. The group-like element ${\buildrel { {}_{K}} \over \mu},$ the square root of the ribbon element $v^{1/2}_{ {}_{K}}$, the quantum Weyl element ${\buildrel  { {}_{K}}\over w},$ the braiding matrices ${\buildrel { {}_{I}{}_{J}} \over R}{}^{(\pm)}$, and the Clebsch-Gordan coefficients satisfy the following relations: $$\begin{aligned}
&&\hskip -0.4cm\sum_{m,n}\!\Clebpsi{I}{\!J}{L}{m}{n}{r}\!\!\Clebphi{I}{\!\!J}{K}{m}{\!n}{p}\!=\!Y^{(0)}_{(I,J,K)}\delta_{K,L}\delta_{p}^{r}Y^{(1)}_{(K,p)},\nonumber\\  
&&\hskip -0.4cm \sum_{K,p}\!\Clebphi{I}{\!\!J}{K}{m}{\!\!n}{p}\!\!\Clebpsi{I}{J}{K}{i}{j}{p}\!\!=\delta_{i}^{m}\delta_{j}^{n}Y^{(1)}_{(I,m)}Y^{(1)}_{(J,n)},\label{ortho1clebsch}
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1cm\sum_{k,l}\Clebpsi{I}{J}{K}{k}{l}{p} {\buildrel { {}_{J}{}_{I}} \over R}{}^{(\pm)}{}_{ji}^{lk}=(\frac{v^{1/2}_{I}v^{1/2}_{J}}{v^{1/2}_{K}})^{\pm 1} \Clebpsi{J}{I}{K}{j}{i}{p},\label{twistclebsch}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -2cm\sum_{i'j'm}\Clebpsi{A}{B}{C}{i'}{j'}{k} {\buildrel { {}_{A}{}_{D}} \over R}{}^{(\pm)}{}_{im}^{i'l}   
{\buildrel { {}_{B}{}_{D}} \over R}{}^{(\pm)}{}_{jn}^{j'm}= \sum_p{\buildrel { {}_{C}{}_{D}} \over R}{}^{(\pm)}{}_{pn}^{kl}  \Clebpsi{A}{B}{C}{i}{j}{p},\label{quasitriang}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1cm \sum_{a'}v^{1/2}_{I} \; {\buildrel { {}_{I}} \over w}{}_{aa'} \Clebphi{I}{J}{K}{a'}{b}{k}=e^{i \pi (J-K)} (\frac{\qd{K}}{\qd{J}})^{1/2}\Clebpsi{I}{K}{J}{a}{k}{b}= \sum_{k'}v^{1/2}_{I} \;{\buildrel { {}_{K}} \over w}{}_{k'k} \Clebphi{J}{K}{I}{b}{k'}{a},\nonumber\\  
&&\hskip -1cm\sum_{i',k'} \ontop{J}{w}_{ii'} {\buildrel { {}_{J}{}_{I}} \over R}{}^{(\pm)}{}_{ji'}^{lk'} \ontop{J}{w}{}^{k'k}={\buildrel { {}_{I}{}_{J}} \over R}{}^{(\mp)}{}_{kj}^{il} \;,\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;{v_{J}}\sum_k \ontop{J}{w}{}^{ik} \ontop{J}{w}_{kj}=\delta^i_j Y^{(1)}_{(J,j)}, \label{contra} 
\end{aligned}$$ $$\begin{aligned}
&&\hskip -2cm \Clebpsi{I}{J}{0}{a}{b}{0}\!\!=\!\frac{\delta_{I,J} \ontop{J}{w}_{ab} e^{i \pi J} }{\sqrt{\qd{I}}},  
\;\;\;\;\;\;\;\;\;\;\;\;{v_{J}}\sum_b \ontop{J}{w}^{ab} \ontop{J}{w}_{kb}=e^{2i \pi J}\ontop{J}{\mu}{}^a_k, \;\;\;\;\;\;\;\;\;\;\qd{K}\!=\!\sum_a \ontop{K}{\mu}{}^a_a, \label{normaclebsch}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -2cm \Clebpsi{A}{B}{C}{i}{j}{k}=\Clebphi{A}{B}{C}{i}{j}{k}\in {\mathbb R}  
.
\end{aligned}$$

The Clebsch-Gordan coefficients also satisfy the relations [@KV]: $$\begin{aligned}
 \Clebpsi{A}{B}{C}{i}{j}{k}(q)=\Clebpsi{B}{A}{C}{-j}{-i}{-k}(q)=(-1)^{A+B-C} \Clebpsi{A}{B}{C}{-i}{-j}{-k}(q^{-1})\label{symmetry3j}. 
\end{aligned}$$

Let us now recall basic facts about $6j(0)$ that we will use extensively in our work.

6j(0) of ${\mathfrak U}_q(su(2))$ are defined as follows: $$\begin{aligned}
&&\hskip -1cm\sixjn{C}{F}{E}{A}{B}{D}{0}\delta_{F,H}\delta^{p}_{n}Y^{(1)}_{(H,p)}=\sum_{i,j,k,l,m}\Clebpsi{A}{B}{E}{i}{j}{m}\Clebpsi{E}{C}{H}{m}{k}{p}\Clebphi{B}{C}{D}{j}{k}{l}\Clebphi{A}{D}{F}{i}{l}{n}.\label{vertexIRF}  
\end{aligned}$$

The properties of the Clebsch-Gordan coefficients, recalled above, imply the following relations on 6j(0): $$\begin{aligned}
&&\sixjn{C}{D}{E}{A}{B}{F}{0}=\sixjn{D}{C}{E}{B}{A}{F}{0}=\sixjn{A}{B}{E}{C}{D}{F}{0}=\sixjn{C}{B}{F}{A}{D}{E}{0}\mbox{(Symmetries)},\label{trivsymm6j0}  
\end{aligned}$$ $$\begin{aligned}
&&\sixjn{B}{E}{F}{A}{C}{D}{0}=e^{i \pi(C-F+E-D)}(\frac{[d_F][d_D]}{[d_C][d_E]})^{1/2}\sixjn{B}{D}{C}{A}{F}{E}{0}\mbox{(Racah-Wigner)},\label{racahwigner6j0}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip 0.7cm\sum_{C}\sixjn{G}{H}{C}{A}{B}{I}{0}\sixjn{G}{H}{C}{A}{B}{J}{0}=\delta_{I,J}Y^{(0)}_{(A,H,I)}Y^{(0)}_{(B,G,I)}\mbox{(Orthogonality)},\label{ortho6j0}\\  
&&\hskip 0.4cm\sum_{C}\sixjn{H}{G}{C}{A}{B}{I}{0}\sixjn{G}{H}{C}{A}{B}{J}{0}(\frac{v_{J}^{1/2}v_{I}^{1/2}v_{C}^{1/2}}{v_{G}^{1/2}v_{H}^{1/2}v_{A}^{1/2}v_{B}^{1/2}})^{\pm 1}=\sixjn{B}{H}{I}{A}{G}{J}{0},\label{racah6j0}\\  
&&\sum_{A}\sixjn{I}{G}{A}{D}{F}{J}{0}\!\!\sixjn{E}{B}{A}{D}{F}{C}{0}\!\!\sixjn{G}{H}{B}{E}{A}{I}{0}\!\!=\sixjn{J}{H}{C}{E}{F}{I}{0}\!\!\sixjn{H}{G}{B}{D}{C}{J}{0}\label{penta6j0}.  
\end{aligned}$$ The relation ([\[racah6j0\]](#racah6j0){reference-type="ref" reference="racah6j0"}) is called the "Racah-relation", whereas the relation ([\[penta6j0\]](#penta6j0){reference-type="ref" reference="penta6j0"}) is usually referred to as the "Pentagonal equation" or the "Biedenharn-Elliot"equation. The relations ([\[racah6j0\]](#racah6j0){reference-type="ref" reference="racah6j0"})([\[penta6j0\]](#penta6j0){reference-type="ref" reference="penta6j0"}) imply the Yang-Baxter equation on $6j(0),$ also called "Hexagonal relation".

Explicit expressions, as well as special values for low spins, of $6j(0)$ symbols are given in [@BR1], but we want to add here the following asymptotic formulae which will be of importance in the rest of this paper (for details see [@KV]): $$\begin{aligned}
&&\hskip -1.2cm \lim_{K \rightarrow +\infty}\sixjn{K}{K\!+\!m\!+\!n}{C}{A}{B}{K\!+\!n}{0}=e^{i \pi (A+B-C)}\Clebpsi{A}{B}{C}{m}{n}{m\!+\!n},\label{asymptot1}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1.2cm \lim_{K \rightarrow +\infty}\sixjn{D}{K}{K\!+\!n_2}{A}{K\!+\!n_1\!+\!n_2}{K\!+\!n'_1}{0}\!  
(\frac{v^{1/2}_{K+n_2}v^{1/2}_{K+n'_1}}{v^{1/2}_{K}v^{1/2}_{K+n_1+n_2}})^{\pm 1} \delta_{n_1+n_2,n'_1+n'_2}=\!  
{\buildrel {{}_A {}_D} \over R}{}^{(\pm)}{}^{n'_1 n'_2}_{n_1 n_2}.\label{asymptot2}  
\end{aligned}$$

## Definitions and properties of continuation of quantum $6j$ symbols

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
