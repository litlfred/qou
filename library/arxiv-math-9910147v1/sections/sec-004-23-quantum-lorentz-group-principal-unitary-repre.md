---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-004-23-quantum-lorentz-group-principal-unitary-repre
section_title: "Quantum Lorentz group, Principal Unitary Representations and Harmonic Analysis"
section_number: 2.3
pages: 10-13
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.995
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
We will recall in this section fondamental results on $\mathfrak{U}_q(sl(2,\mathbb{C})_{\RR})$ and on the harmonic analysis [@BR1] on $SL_q(2,C)_{\RR}.$

$\mathfrak{U}_q(sl(2,\mathbb{C})_{\RR})$ by definition is the quantum double of $\mathfrak{U}_q(su(2)).$ As a result we can write $\mathfrak{U}_q(sl(2,\mathbb{C})_{\RR})=  
 \mathfrak{U}_q(su(2))\otimes \mathfrak{U}_q(su(2))^{*}$ as a vector space, where $\mathfrak{U}_q(su(2))^{*}$ denotes the restricted dual of $\mathfrak{U}_q(su(2)),$ i.e the Hopf algebra spanned by the matrix elements of representations contained in $Irr(\mathfrak{U}_q(su(2))).$

A basis of $\mathfrak{U}_q(su(2))^{*}$ is the set of matrix elements of irreducible representations of $\mathfrak{U}_q(su(2))$, which we will denote by ${\buildrel {{}_{B}} \over  g}{}^i_j, B\in \halfinteger, i,j=-B,...,B.$

It can be shown that $\mathfrak{U}_q(su(2))^{*}$ is isomorphic, as a star Hopf algebra, to the quantum envelopping algebra $\mathfrak{U}_q(an(2))$ where $an(2)$ is the Lie algebra of traceless complex upper triangular 2$\times$<!-- -->2 matrices with real diagonal.

${\mathfrak U}_q(su(2))$ being a factorizable Hopf algebra, it is possible to give a nice generating family of ${\mathfrak U}_q(su(2))$. Let us introduce, for each $I\in \halfinteger$ the elements ${\buildrel I \over L}{}^{\!(\pm)}\in { End}(\CC^{d_I} )\otimes {\mathfrak U}_q(su(2))$ defined by ${\buildrel I \over L}{}^{\!(\pm)}=({\buildrel I\over \pi} \otimes id)(R^{(\pm)}).$ The matrix elements of ${\buildrel I \over L}{}^{\!(\pm)}$ when $I$ describes $\halfinteger$ span the vector space ${\mathfrak U}_q(su(2))$.

The star Hopf algebra structure on $\mathfrak{U}_q(sl(2,\mathbb{C})_{\RR})$ is described in details in [@BR1]. Let us simply recall that we have: $$\begin{aligned}
&&\hskip -1.2cm{\buildrel I \over L}{}^{(\pm)}{}^{i}_{j} {\buildrel J \over L}{}^{(\pm)}{}^{k}_{l}=  
\sum_{Kmn} \Clebphi{I}{J}{K}{i}{k}{m}\!{\buildrel K\over L}{}^{(\pm)}{}^{m}_{n}\!\Clebpsi{I}{J}{K}{j}{l}{n}\;,\;\;\;\;\;\;{\buildrel {IJ} \over {R}}_{12} \; {\buildrel I \over L}{}^{(+)}_1 {\buildrel J \over L}{}^{(-)}_2 =  
 {\buildrel J \over L}{}^{(-)}_2 {\buildrel I \over L}{}^{(+)}_1 \; {\buildrel {IJ} \over {R}}_{12},\label{Rll}\\ 
&&\hskip -1.2cm{\buildrel I \over g}{}^{i}_{j} {\buildrel J \over g}{}^{k}_{l}=\sum_{Kmn}   
\Clebphi{I}{J}{K}{i}{k}{m}\!{\buildrel K \over g}{}^{m}_{n}\!\Clebpsi{I}{J}{K}{j}{l}{n}\;,\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;  
{\buildrel {IJ} \over  R}{}^{(\pm)}_{12} {\buildrel I \over L}{}^{(\pm)}_1 {\buildrel J \over g}_2=  
{\buildrel J \over g}_2 {\buildrel I \over L}{}^{(\pm)}_1 {\buildrel {IJ} \over  R}{}^{(\pm)}_{12},\label{RLg}  
\end{aligned}$$ $$\begin{aligned}
&&\hskip -1cm\Delta({\buildrel I \over L}{}^{(\pm)}{}^a_b)=\sum_{c}{\buildrel I \over L}{}^{(\pm)}{}^c_b   
\otimes {\buildrel I \over L}{}^{(\pm)}{}^a_c \;,\;\;\;\;\;\;\;\;\;\;  
\Delta({\buildrel I \over g}{}^a_b)=\sum_{c}{\buildrel I \over  
g}{}^c_b \otimes {\buildrel I \over g}{}^a_c  ,\label{coproduitD}\\  
&&\hskip -1cm({\buildrel I \over L}{}^{(\pm)}{}^a_b)^{\star}= S^{-1}({\buildrel I \over L}{}^{(\mp)}{}^b_a)\;,\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;({\buildrel I \over g}{}^a_b)^{\star}=S^{-1}({\buildrel I \over g}{}^b_a).\label{staralg}  
\end{aligned}$$ The center of $\mathfrak{U}_q(sl(2,\mathbb{C})_{\mathbb{R}})$ is a polynomial algebra in two variables $\Omega_+, \Omega_-$ and we have $\Omega_{\pm}= 
tr({\buildrel \onehalf \over \mu}{}^{-1}{\buildrel \onehalf \over L}{}^{(\mp)}{}^{-1} {\buildrel \onehalf \over g}).$

Principal Unitary Representations of $\mathfrak{U}_q(sl(2,\mathbb{C})_{\mathbb{R}})$ have been classified in [@Pu], and the following description is given in [@BR1]. They are labelled by a couple of complex numbers $(X_0, X_1) \in {\mathbb S},$ where ${\mathbb S}=\{(X_0, X_1) \in \CC^2\;\;/\;\;2X_0+1 =(m+i\rho)\;,\;2X_1+1 = (-m+i\rho),\;\;  
\;\; m \in {\frac{1}{2}}\ZZ, \rho \in ]-\frac{\pi}{\hbar}, \frac{ \pi}{\hbar}] \;\;\}.$ For $(X_0, X_1) \in {\mathbb S}$ we will often denote $m_X=X_0-X_1, i\rho_X=X_0+X_1+1.$

Let us denote by ${\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}$ the principal representation associated to $(X_0, X_1)$ and $V(X_0X_1)$ the associated $\mathfrak{U}_q(sl(2,\mathbb{C})_{\mathbb{R}})$ module. $V(X_0X_1)$ is a Harisch-Chandra module and we have $V(X_0X_1)=\bigoplus_{C,C-\vert m_x\vert \in \NN} {\buildrel {C}\over V}$ as a ${\mathfrak U}_q(su(2))$ module. In term of the basis $\{{\buildrel {{}_{C}} \over e}_r(X_0X_1)={\buildrel {{}_{C}} \over e}_r, C\in \halfinteger, r=-C,\dots,C\}$ of the module $V(X_0X_1)$, the action of the generators of $\mathfrak{U}_q(sl(2,\mathbb{C})_{\mathbb{R}})$ is given by: $$\begin{aligned}
{\buildrel {{}_{B}} \over  L}{}^{(\pm)}{}^i_j \;  {\buildrel {{}_{C}} \over e}_r &=  
&\sum_{n} {\buildrel {{}_{C}} \over e}_n\;\;  
 {\buildrel {{}_{BC}}\over  R}{}^{(\pm)}{}^{in}_{jr},\label{repl}\\  
{\buildrel {{}_{B}} \over  g}{}^i_j  \;  {\buildrel {{}_{C}} \over e}_r &=&   
\sum_{DEpx} {\buildrel {{}_{E}} \over e}_p\;\;   
\Clebphi{E}{B}{D}{p}{i}{x}\Clebpsi{B}{C}{D}{j}{r}{x} \Lambda^{BD}_{EC}(X_0X_1),\label{repg}  
\end{aligned}$$ where the complex numbers $\Lambda^{BD}_{EC}(X_0X_1)$ have to verify certain constraints explained in the appendix. It is a fondamental result that these coefficients can be expressed in terms of $6j(1)$ as follows: $$\begin{aligned}
&&\hskip -1cm\Lambda^{BC}_{AD}(X_0X_1)= \sum_{X_2} \!  
\sixjn{X_0}{X_1}{A}{B}{C}{X_2}{1} \!\sixjn{X_0}{X_1}{D}{B}{C}{X_2}{1}  
\frac{v_{X_2}}{v_{X_1}}   
\frac{v^{1/4}_{A}v^{1/4}_{D}}{v^{1/2}_{B}v^{1/2}_{C}}\label{formlamb6j}\\  
&&= \sum_{X_2} \!\sixjn{X_1}{X_0}{A}{B}{C}{X_2}{1}\!  
\sixjn{X_1}{X_0}{D}{B}{C}{X_2}{1} \frac{v_{X_0}}{v_{X_2}}   
\frac{v^{1/2}_{B}v^{1/2}_{C}}{v^{1/4}_{A}v^{1/4}_{D}}.  
\end{aligned}$$ The action of the center on the module $V(X_0X_1)$ is such that ${\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}(\Omega_{\pm})=\omega_{\pm} id$ where $\omega_{+}=q^{2X_0+1}+q^{-2X_0-1}, \omega_{-}=q^{2X_1+1}+q^{-2X_1-1}.$

We can endow $V(X_0X_1)$ with a structure of pre-Hilbert space by defining the hermitian form $<.,.>$ such that the basis $\{{\buildrel {{}_{C}} \over e}_r(X_0X_1), C\in \halfinteger, r=-C,\dots,C\}$ of $V(X_0X_1)$ is orthonormal.

The representation ${\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}$ is unitary in the sense that $\forall v, w\in V(X_0X_1),\;\; \forall a\in \mathfrak{U}_q(sl(2,\mathbb{C})_{\mathbb{R}}),$ $<a^{*}v,w>=<v, aw>,$ this last property being equivalent to the relation: $\Lambda^{BC}_{AD}(X_1X_0)={\overline {\Lambda^{BC}_{AD}(X_0X_1)}}.$

We will denote by $H(X_0X_1)$ the separable Hilbert space, completion of $V(X_0X_1)$ which Hilbertian basis is $\{{\buildrel {{}_{C}} \over e}_r(X_0X_1), C\in \halfinteger, r=-C,\dots,C\}.$

The automorphism of the complex line is now playing a key role because of the following important result: the principal representations associated to $(X_0, X_1)$ and to $(\underline{X_0}, \underline{X_1})$ are unitary equivalent.

Let us now recall some basic facts about the algebra of functions on $SL_q(2,\CC)_{\RR}$ [@PW; @Wo2; @BR1]. We will use the notations of [@BR1]. The space of compact supported functions on the quantum Lorentz group, denoted $Fun_c(SL_q(2,\CC)_{\RR})$ is, by definition, $Fun(SU_q(2)') \otimes \left( \bigoplus_{ I \in \onehalf \ZZ^{+}} End(\CC^{d_I})\right).$ This is a $C^{*}$ algebra without unit. It contains the dense \*-subalgebra [@BR1] $Fun_{cc}(SL_q(2,\CC)_{\RR})=Pol(SU_q(2)')\otimes \left( \bigoplus_{ I \in \onehalf \ZZ^{+}} End(\CC^{d_I})\right)$ which is a multiplier Hopf algebra [@VD], and which can be understood as being the quantization of the algebra generated by polynomials functions on $SU(2)$ and compact supported functions on $AN(2).$

$(\kE{C}{m}{n}{D}{p}{q})_{C,D,m,n,p,q}$ is a vector basis of $Fun_{cc}(SL_q(2,\CC)_{\RR})$ which is defined, for example, by duality from the generators of the envelopping algebra: $$\begin{aligned}
&&<{\buildrel {{}_{A}} \over  L}{}^{(\pm)}{}^i_j \otimes {\buildrel {{}_{B}} \over  g}{}^k_l, \;\kE{C}{m}{n}{D}{p}{q}>=  
{\buildrel {{}_{AC}}\over  R}{}^{(\pm)}{}^{im}_{jn}\delta_{B,D}\delta^{k}_{q}\delta^{p}_{l}.  
\end{aligned}$$ We can describe completely the structure of the multiplier Hopf algebra in this basis; $$\begin{aligned}
&&\hskip -1.5cm\kE{A}{i}{j}{B}{k}{l} \cdot \kE{C}{m}{n}{D}{p}{q}= \sum_{Frs} \Clebphi{A}{C}{F}{i}{m}{r}\Clebpsi{A}{C}{F}{j}{n}{s} \delta^p_l   
\delta_{B,D} \kE{F}{r}{s}{B}{k}{q}\nonumber\\  
&&\hskip -1.5cm\Delta(\kE{A}{i}{j}{B}{k}{l})={\cal F}^{-1}_{23}\;  
(\!\!\!\!\sum_{\substack{{C,D,m,}\\{p,q,r,s}}}\!\!\!\!\Clebphi{C}{D}{B}{q}{s}{l}\!\!\Clebpsi{C}{D}{B}{p}{r}{k}\!\kE{A}{i}{m}{C}{p}{q} \!\otimes \!  
 \kE{A}{m}{j}{D}{r}{s}\;)\;{\cal F}_{23}\nonumber\\  
&&\hskip -1.5cm\epsilon(\kE{A}{i}{j}{B}{k}{l})=\delta^i_j \delta_{B,0}\;\;\;\;\;\;\;(\kE{A}{i}{j}{B}{k}{l})^{\star}=S^{-1}({\buildrel A \over k}{}^j_i) \! \otimes   
\! {\buildrel B \over E}{}^l_{k}\;\;\;\;\mbox{with}\;\;  
{\cal F}^{-1}_{12}=\sum_{J,x,y}\!\!{\buildrel J \over E}{}^x_y \! \otimes \! S^{-1}\!({\buildrel J \over k}{}^y_x). 
\end{aligned}$$ The space of right and left invariant linear forms (also called Haar measures) on $Fun_c(SL_q(2,\CC)_{\RR})$ is a vector space of dimension one and we will pick one element $h$, which is defined by: $$\begin{aligned}
h(\kE{A}{i}{j}{B}{m}{l})= \delta_{A,0}({\buildrel {{}_{B}} \over \mu}{}^{-1})^m_l \qd{B}.\label{haar}  
\end{aligned}$$ Using the $L^2$ norm, $\vert \vert \; a \; \vert \vert_{L^2}=h(a^* a)^{\onehalf}$, we can complete the space $Fun_c(SL_q(2,\CC)_{\RR})$ into the Hilbert space of $L^2$ functions on the quantum Lorentz group, denoted $L^2(SL_q(2,\CC)_{\RR})$.

$Fun_{cc}(SL_q(2,\CC)_{\RR})$ is a multiplier Hopf algebra with basis $(u_\alpha)=((\kE{C}{m}{n}{D}{p}{q})_{C,D,m,n,p,q})$. The restricted dual of $Fun_{cc}(SL_q(2,\CC)_{\RR})$, denoted ${\tilde \mathfrak U}_q(sl_q(2,\CC)_{\RR}),$ is the vector space spanned by the dual basis $(u^{\alpha})= 
({\buildrel {{}_{C}}\over X }{}^{n}_m \otimes {\buildrel {{}_{D}}\over g}{}^q_p).$ It is also, by duality, a multiplier Hopf algebra and ${\mathfrak U}_q(sl(2,\CC)_{\RR} )$ is included as an algebra in the multiplier algebra of ${\tilde \mathfrak U}_q(sl(2,\CC)_{\RR} )$. If $\Pi$ is the principal representation of ${\mathfrak U}_q(sl(2,\CC)_{\RR} )$, acting on $V(Z_0Z_1),$ it is possible [@BR1] to associate to it a unique representation ${\tilde \Pi}$ of ${\tilde \mathfrak U}_q(sl(2,\CC)_{\RR} ),$ acting on $V(Z_0Z_1)$, such that ${\tilde \Pi}({\buildrel {{}_{C}}\over X }{}^{n}_m)({\buildrel {{}_{D}} \over e}_r)=\delta_{C,D}\delta^{n}_{r}{\buildrel {{}_{D}} \over e}_m.$

We define for all $\psi$ element of $Fun_{cc}(SL_q(2,\CC)_{\RR})$, the operator $\Pi(\psi)=\sum_I {\tilde\Pi}(u^I)\; h(u_I \; \psi).$ It is easy to show that $\Pi(\psi)$ is of finite rank.

If $f$ is a function on ${\mathbb S}$, we will sometimes write $f(m_X,\rho_X)$ instead of $f(X_0X_1).$ The Plancherel formula can be written as: $$\begin{aligned}
&&\hskip -0.6cm \forall \psi\in Fun_{cc}(SL_q(2,\CC)_{\RR}),\;\; \vert \vert \; \psi \;  
 \vert \vert_{L^2}^2  = \; \int d{\cal P}(X_0X_1) \;\;  
{\rm tr} \left( \; {\buildrel {\!\!{}_{(X_0X_1)}}  
 \over {\Pi}}\!\!(\mu^{-1}){\buildrel {\!\!{}_{(X_0X_1)}}   
\over {\Pi}}\!\!\!\!(\psi){\buildrel {\!\!{}_{(X_0X_1)}} \over {\Pi}}\!\!\!\!(\psi)^{\dagger} \; \right),  
\end{aligned}$$ where we have denoted $$\begin{aligned}
&&\hskip -0.5cm\int d{\cal P}(X_0X_1) \; f(X_0X_1)=  
\!\!\!\sum_{m \in \onehalf \ZZ} \; \int_{-\frac{\pi}{\hbar}}^{\frac{\pi}{\hbar}} \!\!\!d\rho\;\;  
{\cal P}(m,\rho)\; f(m,\rho)\nonumber\\  
&&\mbox{with}\;\;\;\;\;{\cal P}(m,\rho)=  
\frac{\hbar}{2\pi}(q-q^{-1})^2\;[m+i\rho][m-i\rho].\nonumber  
\end{aligned}$$

The proof of this theorem is purely combinatorial and uses as a central tool the following identity on Fourier coefficients of the Laurent polynomials $\Lambda^{BC}_{AA}$: $$\int d{\cal P}(X_0X_1) \; \Lambda^{BC}_{AA}(X_0X_1)\; = \;\delta_{B,0}\delta_{A,C}\qd{A}\label{intlambda}.$$

A Plancherel Theorem for $L^2$ functions has been proved [@BR1], it follows easily from the previous result and from the following lemma, which will be useful later on

::: lemma
The only function $f:{\mathbb S}\rightarrow \CC$ satisfying the following conditions:

1)$\forall m\in \onehalf \ZZ, \forall \rho\in ]-\frac{\pi}{\hbar},\frac{\pi}{\hbar}] , f(m,\rho)=f(-m,-\rho),$

2)$\forall m\in  \onehalf \ZZ, f(m,.)$ is a $L^2$ function on $]-\frac{\pi}{\hbar},\frac{\pi}{\hbar}],$

3)$\exists m_0\in  \onehalf \NN, \forall m, \vert m \vert > m_0, f(m,.)=0,$

4\) $\exists  A,D \in \halfinteger \cap [\vert m_0 \vert, +\infty[,  
 \forall B,C \in \halfinteger,\;\;\int d{\cal P}(X_0X_1)\; f(X_0X_1) \; \Lambda^{BC}_{AD}(X_0X_1)\; = \;0,$

is the nul function.
:::
