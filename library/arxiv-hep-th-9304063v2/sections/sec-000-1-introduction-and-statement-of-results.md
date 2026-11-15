---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: sec-000-1-introduction-and-statement-of-results
section_title: "Introduction and Statement of Results"
section_number: 1
pages: 1-5
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.968
---
## Introduction

Scaling models of random $N\times N$ hermitian matrices and passing to the limit $N\ra\iy$ leads to integral operators whose Fredholm determinants describe the statistics of the spacing of the eigenvalues of hermitian matrices of large order [@mehta_book; @porter]. Which integral operators (or, more precisely, which kernels of integral operators) result depends on the matrix model one starts with and at which location in the spectrum the scaling takes place.

For the simplest model, the Gaussian Unitary Ensemble (GUE), and for many others as well (see, e.g., [@kpw; @mahoux_mehta91; @nagao_wadati; @pastur]), the kernel one obtains by scaling in the "bulk" of the spectrum is the "sine kernel" $$\frac{\sin\pi(x-y)}{\pi(x-y)}.$$ Precisely, this comes about as follows. If $\{\phi_{k}(x)\}_{k=0}^{\iy}$ is the sequence obtained by orthonormalizing the sequence $\{x^{k}\,e^{-x^{2}/2}\}$ over $(-\iy,\iy)$ and if K\_N(x,y) = \_k=0\^N-1 \_k(x) \_k(y)  , []{#KN label="KN"} then in the GUE the probability density that $n$ of the eigenvalues (irrespective of order) lie in infinitesimal intervals about $x_{1},\ldots,x_{n}$ is equal to $$R_{n}(x_{1},\ldots,x_{n})\,=\,\mbox{det}\ (K_{N}(x_{i},x_{j}))\,_{i,j=1,\ldots,n}.$$ The density of eigenvalues at a fixed point $z$ is $R_{1}(z)$, and this is $\sim\sqrt{2N}/\pi$ as $N\ra\iy$. Rescaling at $z$ leads to the sine kernel because of the relation $$\lim_{N\ra\iy}\frac{\pi}{\sqrt{2N}}K_{N}(z+\frac{\pi x}{\sqrt{2N}},z+\frac{\pi y}
{\sqrt{2N}})\,=\,\frac{\sin\pi(x-y)}{\pi(x-y)}.$$

Rescaling the GUE at the "edge" of the spectrum, however, leads to a different kernel. The edge corresponds to $z\sim\sqrt{2N}$, at which point the density is $\sim2^{\hf}N^{\frac{1}{6}}$, and we have there the scaling limit [@bowick_brezin; @forrester; @moore] $$\lim_{N\ra\iy}\frac{1}{2^{\hf}N^{\frac{1}{6}}} K_{N}(\sqrt{2N}+
\frac{x}{2^{\hf}N^{\frac{1}{6}}},\sqrt{2N}+\frac{y}{2^{\hf}N^{\frac{1}{6}}})\,
=\,\frac{{\rm Ai}(x)\,{\rm Ai}'(y)\,-{\rm Ai}'(x)\,{\rm Ai}(y)}{x-y}$$ where ${\rm Ai}$ is the Airy function. In previous work [@tw2] we found several analogies between properties of this "Airy kernel" and known properties of the sine kernel: a system of partial differential equations associated with the logarithmic differential of the Fredholm determinant when the underlying domain is a union of intervals [@jmms]; a representation of the Fredholm determinant in terms of a Painlevé transcendent in the case of a single interval [@jmms]; and, also in this case, asymptotic expansions for these determinants and related quantities [@dyson76; @btw; @widom92; @dyson92; @mehta_mahoux92b], achieved with the help of a differential operator which commutes with the integral operator. (See [@tw1] for further discussion of these properties of the sine kernel.)  

In this paper we show that there are completely analogous properties for a class of kernels which arise when one rescales the Laguerre or Jacobi ensembles at the edge of the spectrum. For the Laguerre ensemble the analogue of the sequence of functions $\{\phi_{k}(x)\}$ in ([\[KN\]](#KN){reference-type="ref" reference="KN"}) is obtained by orthonormalizing the sequence$$\{x^{k}\,x^{\al/2}\,e^{-x/2}\}$$over $(0,\iy)$ (here $\al>-1$), whereas for Jacobi one orthonormalizes $$\{x^{k}(1-x)^{\al/2}(1+x)^{\beta/2}\}$$ over $(-1,1)$. (Here $\al,\beta\,>\,-1$.) In the Laguerre ensemble of (positive) hermitian $N\times N$ matrices the eigenvalue density satisfies [@bronk; @nagao_wadati], for a fixed $x<1$, $$R_{1}(4Nx)\sim\frac{1}{2\pi}\sqrt{\frac{1-x}{x}}.$$ This limiting law is to be contrasted with the well-known Wigner semi-circle law in the GUE. The new feature here is the "hard edge" for $x\sim 0$. At this edge we have the scaling limit [@forrester]: $$\lim_{N\ra\iy}\frac{1}{4N}K_{N}(\frac{x}{4N},\frac{y}{4N}) 
=\,\frac{ J_{\al}(\sqrt{x})\,\sqrt{y} J_{\al}'(\sqrt{y})\,-
\sqrt{x} J_{\al}'(\sqrt{x})\, J_{\al}(\sqrt{y})}{2(x-y)}$$ where $J_\al(z)$ is the Bessel function of order $\al$. Both limits follow from the asymptotic formulas for the generalized Laguerre polynomials. (Scaling in the bulk will just lead to the sine kernel and scaling at the "soft edge," $x\sim 1$, will lead to the Airy kernel.) The same kernel arises when scaling the Jacobi ensemble at $-1$ or $1$. (Recall that in the Jacobi ensemble both $\pm 1$ are hard edges; see e.g. [@nagao_wadati].) 

For later convenience we introduce now a parameter $\la$ and define our "Bessel kernel" by

::: mathletters
$$\begin{aligned}
K(x,y):&=&\,\la\,\frac{J_{\al}(\sqrt{x})\,\sqrt{y}J_{\al}'(\sqrt{y})\,-
\sqrt{x}J_{\al}'(\sqrt{x})\,J_{\al}(\sqrt{y})}{2(x-y)}
\, ,\ \ \ (x\neq y)\label{Kdef}\\
&=&\, {\la\over 4}\left( J_{\al}(\sqrt{x})^2-J_{\al+1}(\sqrt{x})
 J_{\al-1}(\sqrt{x})
\right)\ \ \ (x=y).
\label{Kdiagdef}
\end{aligned}$$
:::

Before stating our results, we mention that in the cases $\al=\mp\hf$ we have, when $\la=1$,  K(x\^2,y\^2) =    , []{#dyson_kernels label="dyson_kernels"} which are kernels which arise when taking scaling limits in the bulk of the spectrum for the Gaussian orthogonal and symplectic ensembles [@mehta_book]. In particular, an asymptotic expansion we derive will generalize ones found by Dyson [@dyson76] for the Fredholm determinants of these kernels.

We now state the results we have obtained.

## The System of Partial Differential Equations

We set J:= \_j=1\^m(a\_2j-1,a\_2j) (a\_j) []{#Jform label="Jform"} and write $D(J;\la)$ for the Fredholm determinant of $K$ (the operator with kernel $K(x,y)$) acting on $J$. If we think of this as a function of $a=(a_{1},\ldots,a_{2m})$ then d D(J;) = -\_j=1\^2m(-1)\^j R(a\_j,a\_j) da\_j[]{#diff label="diff"} where $R(x,y)$ is the kernel of $K(I-K)^{-1}$. We introduce the notations (x):=  J\_(~~x~~), (x):= x '(x)[]{#phidef label="phidef"} and the quantities $$\begin{aligned}
q_{j}:&=&\,(I-K)^{-1}\phi\,(a_{j}),~~p_{j}:=\,(I-K)^{-1}\psi\,(a_{j}),
\;\;\;\;(j=1,\ldots ,2m)\label{pqdef} \\
u:&=&\,(\phi,(I-K)^{-1}\phi),~~v:=\,(\phi,(I-K)^{-1}\psi),\label{uvdef} 
\end{aligned}$$ where the inner products refer to the domain $J$. The differential equations are $$\begin{aligned}
\frac{\partial q_{j}}{\partial a_{k}}&=&(-1)^{k}\,
\frac{q_{j}p_{k}-p_{j}q_{k}}{a_{j}-a_{k}}  \,q_{k} \hspace{2em} (j\neq k)\label{qjk}\\
\noalign{\vskip3pt}
\frac{\partial p_{j}}{\partial a_{k}}&=&(-1)^{k}\,
\frac{q_{j}p_{k}-p_{j}q_{k}}{a_{j}-a_{k}}  \,p_{k} \hspace{2em} (j\neq k)\label{pjk}\\
\noalign{\vskip3pt}
a_{j}\frac{\pl q_{j}}{\pl a_{j}}&=&p_{j}\,+\,\frac{1}{4}\,q_{j}\,u\,
-\,\sum_{k\neq j}(-1)^{k}\,a_{k}\,\frac{q_{j}p_{k}-p_{j}q_{k}}{a_{j}-a_{k}}\,q_{k}
\label{qj} \\ \noalign{\vskip3pt}
a_{j}\,\frac{\pl p_{j}}{\pl a_{j}}&=&\frac{1}{4}(\al^{2}-a_{j}+2v)\,q_{j}
-\frac{1}{4}p_{j}\,u\,-\sum_{k\neq j}(-1)^{k}\,a_{k}\,\frac{q_{j}p_{k}-p_{j}q_{k}}
{a_{j}-a_{k}}\,p_{k} \label{pj}\\ \noalign{\vskip3pt}
\frac{\pl u}{\pl a_{j}}&=&(-1)^{j}\,q_{j}^{2} \label{uj}\\ \noalign{\vskip3pt} 
\frac{\pl v}{\pl a_{j}}&=&(-1)^{j}\,p_{j}\,q_{j}. \label{vj}
\end{aligned}$$ Moreover the quantities $R(a_{j},a_{j})$ appearing in ([\[diff\]](#diff){reference-type="ref" reference="diff"}) are given by a\_j R(a\_j,a\_j)=\_kj(-1)\^k a\_k  +p\_j\^2 -  (\^2-a\_j+2v) q\_j\^2+ p\_j q\_j u. []{#Rjj label="Rjj"} These equations are quite similar to eqs. (1.4)--(1.9) of [@tw2], as is their derivation.

## The ordinary differential equation

For the special case $J=(0,s)$ the above equations can be used to show that $q(s;\la)$, the quantity $q$ of the last section corresponding to the endpoint $s$, satisfies s(q\^2-1)(s q')' = q(sq')\^2+(s-\^2)q+sq\^3(q\^2-2) ('=). []{#qeq label="qeq"} with boundary condition q(s;) \~  s\^/2  ,     s. []{#qeq_bc label="qeq_bc"} This equation is reducible to a special case of the $P_{V}$ differential equation; explicitly, if $q(s)=(1+y(x))/(1-y(x))$ with $s=x^2$, then $y(x)$ satisfies $P_V$ with $\alpha^\prime=-\beta^\prime=\alpha^2/8$, $\gamma^\prime=0$ and $\delta^\prime=-2$. (We have primed the usual $P_V$ parameters to avoid confusion with the $\alpha$ in our kernel. We mention that this special $P_V$ can be expressed algebraically in terms of a third Painlevé transcendent and its first derivative [@gromak]. We mention also that an argument can be given that ([\[qeq\]](#qeq){reference-type="ref" reference="qeq"}) must be reducible to one of the 50 canonical types of differential equations found by Painlevé, without an explicit verification being necessary. This will be discussed at the end of section II B.)  It is sometimes convenient to transform ([\[qeq\]](#qeq){reference-type="ref" reference="qeq"}) by making the substitution $$q(s)=\cos\psi(s),$$ so that $\psi$ satisfies \^ +1s \^= 18s( 2) -\^24s\^2  \^3  .[]{#psi_eq label="psi_eq"}

The Fredholm determinant is expressible in terms of $q$ by the formula D(J;) = (-\_0\^s q(t)\^2  dt). []{#Drep label="Drep"} Denoting by $R(s)$ minus the logarithmic derivative of $D(J;\la)$ with respect to $s$, we have also the representation R(s)=\^2(s) + s(dds)\^2 - \^2 s \^2(s)   . []{#R_psi label="R_psi"} Furthermore, $R(s)$ itself satisfies a differential equation which in the Jimbo-Miwa-Okamoto $\sigma$ notation for Painlevé III (see, in particular, (3.13) in [@jimbo]) is (s\^)\^2+\^(-s\^) (4\^)-\^2(\^)\^2=0 []{#sigma_eq label="sigma_eq"} where $\sigma(s)=s R(s)$; it has small $s$ expansion $$\begin{aligned}
\sigma(s;\lambda)&=&c_\al \, s^{1+\al}
 \left[1-\fr{1}{2(2+\al)} s +\fr{3+2\al}{16(1+\al)(2+\al)
(3+\al)} s^2 + \cdots\right]\nonumber \\ \noalign{\vskip3pt}
&&+ \fr{1}{1+\al}c_\al^2 \, s^{2+2\al}\left[1-
\fr{3+2\al}{2(2+\al)^2} s + \cdots\right]\nonumber \\ \noalign{\vskip3pt}
&& + \fr{1}{(1+\al)^2}c_\al^3\,  s^{3+
3\al}\left[1+\cdots\right]+\cdots
\end{aligned}$$ where $$c_\al = \fr{\lambda}{2^{2\al+2}} \fr{1}{\Gamma(1+\al)\Gamma(2+\al)}\, .$$

We mention that in the special case $\al=0$ and $\lambda=1$ we have $D(J;1)=e^{-s/4}$, $q(s;1)=1$, $\psi(s,1)=0$, and $\sigma(s,1)=s/4$ exactly [@edelman88; @edelman91; @forrester].
