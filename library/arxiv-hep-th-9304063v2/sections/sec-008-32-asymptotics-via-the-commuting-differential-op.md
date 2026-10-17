---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: sec-008-32-asymptotics-via-the-commuting-differential-op
section_title: "Asymptotics via the commuting differential operator"
section_number: 3.2
pages: 12-18
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 10 sections: Front matter; Introduction and Statement of Resu; The System of Partial Differential"
---
Throughout this section we take $\la=1$. The operator $K$, when rescaled to act on $(0,1)$ instead of $(0,s)$, has kernel $s\,K(sx,sy)$. By ([\[Krep2\]](#Krep2){reference-type="ref" reference="Krep2"}) this is equal to $${s \over 4}\int_{0}^{1}\phi(sxt)\,\phi(syt)\,dt,$$ and so $K$ (rescaled, as it will be throughout this section), is the square of the operator on $(0,1)$ with kernel $$J(x,y)={\st{s}\over 2}\,\phi(sxy)={\st{s}\over 2}\,J_{\al}(\st{sxy}).$$ This function satisfies the differential equation x\^2J\_xx+xJ\_x+(-)J=0.[]{#W1 label="W1"} The operator $J$ will commute with a differential operator $${\cal L}= \frac{d}{dx}\alpha(x)\frac{d}{dx}+\beta(x)$$ if $\alpha(0)=\alpha(1)=0$ and if $$\alpha(y)J_{yy}+\alpha'(y)J_{y}+\beta(y)J=\alpha(x)J_{xx}+\alpha'(x)J_{x}+\beta(x)J.$$ If we use ([\[W1\]](#W1){reference-type="ref" reference="W1"}) we see that this will be satisfied if $$-\alpha(x)\left[x^{-1}J_{x}+(\frac{sy}{4x}-\frac{\alpha^{2}}{4x^{2}})\right]
+\alpha'(x)J_{x}+\beta(x)J$$ $$=\mbox{the same expression with $x$ and $y$ interchanged.}$$ Equating the terms involving the first derivatives of $J$ gives $$(\alpha'(x)-x^{-1}\alpha(x))J_{x}=(\alpha'(y)-y^{-1}\alpha(y))J_{y}.$$ But $x\,J_{x}=y\,J_{y}$, so the above will hold if $$x^{-1}(\alpha'(x)-x^{-1}\alpha(x))=y^{-1}(\alpha'(y)-y^{-1}\alpha(y)).$$ This is satisfied if $\alpha(x)$ is a quadratic without constant term and, of course, we choose $$\alpha(x)=x(1-x).$$ What is required of $\beta$, then, is seen to be $$\beta(x)-x(1-x)(\frac{sy}{4x}-\frac{\alpha^{2}}{4x^{2}})
=\beta(y)-y(1-y)(\frac{sx}{4y}-\frac{\alpha^{2}}{4y^{2}}),$$ which is satisfied by $$\beta(x)=-\frac{\al^{2}}{4x}-\frac{sx}{4}.$$ We write the differential equation, for which the eigenfunctions $f(x)$ are the eigenfunctions of $J$, as (x(1-x)f'x))'+(\--)f(x)=0.[]{#W2 label="W2"} The boundary conditions are that $f(x)$ be bounded as $x\rightarrow1$ and that $f(x)$ be asymptotic to a constant times $x^{\al/2}$ as $x\rightarrow0.$ The reason we wrote the eigenvalues as we did is that for each $i$ the $\mu$ corresponding to the i'th largest eigenvalue is bounded as $s\rightarrow\infty$. This is easily seen by an oscillation argument. So we assume $i$ is fixed and proceed to find the asymptotics of the corresponding eigenfunction $f(x)$ as $s\rightarrow\infty$. We assume it normalized so that f(x)\~x\^/2 as x.[]{#W3 label="W3"}

### The region $x\ll 1$

The approximating equation is $$f''(x)+\frac{1}{x}f'(x)+(\frac{\mu\sqrt{s}}{x}-\frac{\al^{2}}{4x^{2}}-
\frac{s}{4})f(x)=0.$$ The solution of this equation which satisfies ([\[W3\]](#W3){reference-type="ref" reference="W3"}) is $$x^{\al/2}e^{-\sqrt{s}x/2}\Phi(\frac{1+\al}{2}-\mu,1+\al,\sqrt{s}x)$$ where $\Phi$ is the confluent hypergeometric function [@erdelyi]. We deduce that when $x\ll1$, f(x)\~x\^/2 e\^-x/2 (-,1+,x). []{#W4 label="W4"}

### The region $x\ll 1, \protect\sqrt{s}   x\gg 1$

$\mu\neq i+\frac{1+\al}{2}\ (i=0,1,\ldots)$. Then from the known asymptotics of $\Phi$ as its argument tends to $\infty$ (6.13(3) of [@erdelyi]) we deduce that f(x)\~  s\^-(+) x\^\--  e\^x/2.[]{#W5 label="W5"} *Case 2.* $\mu=i+\frac{1+\al}{2}$. Then (-i,1+,x)=  L\^\_i(x)[]{#W6 label="W6"} where $L^{\al}_{i}$ is the generalized Laguerre polynomial (6.9(36) of [@erdelyi]). So we find that in this case f(x)\~(-1)\^i s\^  x\^i+ e\^-x/2.[]{#W7 label="W7"}

### The region $\protect \sqrt{s}\; x\gg\, 1$, $(1-x)\; s\gg\, 1$

Here we use the standard WKB approximation for the solutions of a differential equation $(p\,f')'+q\,f=0$ given by $e^{\pm y}/(p\,q)^{\frac{1}{4}}$ where $y=\int\sqrt{q/p}$. In the case of our equation ([\[W2\]](#W2){reference-type="ref" reference="W2"}), the range of validity of the approximation is as indicated in the heading of this section. To be definite, we take $$y=-\int_{x}^{1}\sqrt{q(z)/p(z)}\,dz.$$ It is easy to compute that for the range in question we have $$y=-\sqrt{s}\,\sqrt{1-x}-\mu\,\log x+2\,\mu\log(1+\sqrt{1-x})+o(1).$$ Also, in this case $p\,q$ is asymptotically $-s/4$ times $x^{2}(1-x)$. Hence $$f(x)\sim\left(a(s)\,x^{-\mu}\,(1+\sqrt{1-x})^{2\mu}\,e^{-\sqrt{s}\sqrt{1-x}}\right.$$ .+b(s) x\^ (1+)\^-2 e\^) []{#W8 label="W8"} where $a(s)$ and $b(s)$ are constants depending on $s$.

### The region $x\rightarrow 1$

Letting $y=1-x,f(x)=g(y)$ gives the approximating equation $$(y\,g(y)')'-\frac{s}{4}\,g(y)\,=\,0.$$ The general solution of this is a constant times $I_{0}(\sqrt{y})$ where $I_{0}$ is the modified Bessel function. Thus we deduce that as $x\rightarrow1$ f(x)\~ c(s) I\_0()[]{#W9 label="W9"} for some c(s).

### Determination of $a(s)$, $b(s)$ and $c(s)$

From the asymptotics of $I_{0}$ at infinity and ([\[W9\]](#W9){reference-type="ref" reference="W9"}) we deduce that $$f(x)\sim\frac{c(s)}{\sqrt{2\pi}\,s^{\frac{1}{4}}}\frac{e^{\sqrt{s}\sqrt{1-x}}}
{(1-x)^{\frac{1}{4}}}$$ when $x\rightarrow1$ and $s(1-x)\rightarrow\infty.$ Comparing this with ([\[W8\]](#W8){reference-type="ref" reference="W8"}) shows that $a(s)=0$ and that c(s)\~ s\^ b(s).[]{#W10 label="W10"} And now comparing ([\[W8\]](#W8){reference-type="ref" reference="W8"}) with ([\[W5\]](#W5){reference-type="ref" reference="W5"}) and ([\[W7\]](#W7){reference-type="ref" reference="W7"}) in their overlapping range of validity we see that we must be in case 2 and that b(s)\~(-1)\^i  2\^2n++1  e\^-.[]{#W11 label="W11"}

What we shall need from all this is, first, the asymptotics of $f(1)$. This follows immediately from ([\[W9\]](#W9){reference-type="ref" reference="W9"}), ([\[W10\]](#W10){reference-type="ref" reference="W10"}), ([\[W11\]](#W11){reference-type="ref" reference="W11"}), and the fact that $I_{0}(0)=1$: f(1) \~ (-1)\^n    s\^+ e\^-2\^2n++1.[]{#W12 label="W12"} We shall also need the asymptotics of $\int f(x)^{2}dx$. It follows from the asymptotics we have derived that the main contribution to this integral comes from an arbitrarily small neighborhood of $x=0$. It follows from ([\[W4\]](#W4){reference-type="ref" reference="W4"}), ([\[W6\]](#W6){reference-type="ref" reference="W6"}) and the fact $$\int_{0}^{\infty}\,x^{\al}\,e^{-x}\,L_{i}^{\al}(x)^{2}\,dx\,=\,
\frac{\Gamma(\al+i+1)}{i!}$$ that $$\int_{0}^{1}\,f(x)^{2}\,dx\sim
\frac{\Gamma(\al+1)^{2}\,i!}{\Gamma(\al+i+1}\,s^{-\frac{\al}{2}-\frac{1}{2}}.$$ We put these two relations together to get what we *really* want, which is \~   s\^i++1 e\^-2 2\^4i+2+2.[]{#W13 label="W13"}

### The asymptotics of $\lambda_{i}$

Since ${\cal L}$ commutes with our integral operator $K$, rescaled to act on $(0,1)$, the set $\{f_{i}\}$ of eigenfunctions corresponding to the eigenvalues $\mu_{0}<\mu_{1}<\ldots$ of ${\cal L}$ is the set of eigenfunctions of $K$ corresponding to its eigenvalues, in some order.\
\
**Lemma 1**. *The eigenvalues of $K$ are simple*.\
\
. Since the eigenvalues of $K$ are the squares of the eigenvalues of $J$ what we have to show is that if $f_{1}(x)$ and $f_{2}(x)$ are eigenfunctions of ${\cal L}$ (they need not correspond to any particular $\mu$ here) and if for some $\nu$ we have either $$\int_{0}^{1}J_{\al}(\sqrt{sxy})f_{i}(y)dy=\nu f_{i}(x)\;\;\;\;\;\;\;(i=1,2)$$ or $$\int_{0}^{1}J_{\al}(\sqrt{sxy})f_{1}(y)dy=\nu f_{1}(x),\;\;
\int_{0}^{1}J_{\al}(\sqrt{sxy})f_{2}(y)dy=-\nu f_{2}(x)$$ then $f_{1}$ and $f_{2}$ are linearly dependent. We shall assume them normalized so that they both have the value $1$ at $x=1$.

Notice first that $\nu\neq0$ for otherwise if we expand the $f_{1}$ equation near $x=0$ we would find that $$\int_{0}^{1}x^{\frac{\al}{2}+k}f_{1}(x)dx=0,\;\; k=0,1,\ldots,$$ and $f_{1}$ would be identically 0.

Next we define $$H(x)=e^{-x/2}J_{\al}(\sqrt{s\,e^{-x}}),\;
g_{i}(x)=e^{-x/2}f_{i}(e^{-x}),$$ make the obvious variable changes, and find that our relations become []{#L1.1 label="L1.1"}\_0\^H(x+y) g\_i(y) dy= g\_i(x),(i=1,2), []{#L1.2 label="L1.2"}\_0\^H(x+y) g\_1(y) dy= g\_1(x), \_0\^H(x+y) g\_2(y) dy=-g\_2(x).

What comes now is almost identical to the proof of Lemma 1 of [@tw2]. Assuming first that ([\[L1.1\]](#L1.1){reference-type="ref" reference="L1.1"}) holds, we differentiate twice this relation with $i=1$ and then integrate by parts twice to obtain $$\nu\,g_{1}(x)=-H'(x)+H(x)\,g_{1}'(0)+\int_{0}^{\infty}H(x+y)\,g_{1}(y)\,dy.$$ If we multiply both sides by $g_{2}(x)$ and integrate, using ([\[L1.1\]](#L1.1){reference-type="ref" reference="L1.1"}) and its differentiated version, we obtain (recall that $g_{i}(0)=1$) $$\nu\int_{0}^{\infty}g_{1}''(x)\,g_{2}(x)\,dx=-\nu g_{2}'(0)+\nu g_{1}'(0)+
\nu\int_{0}^{\infty}g_{2}(y)\,g_{1}''(y)\,dy.$$ Thus, since $\nu\neq0$, we have $g_{1}'(0)=g_{2}'(0)$. Equivalently, $f_{1}'(1)
=f_{2}'(1)$. But since also $f_{1}(1)=f_{2}(1)$, it follows from equation (2) that the corresponding eigenvalues $\mu$ must be the same, and so the eigenfunctions are the same.

Next, assume ([\[L1.2\]](#L1.2){reference-type="ref" reference="L1.2"}) holds. Differentiating both sides of the first relation once and integrating by parts give $$\nu\,g_{1}'(x)=-H(x)-\int_{0}^{\infty}H(x+y)\,g_{1}'(y)\,dy.$$ Multiplying both sides of this by $g_{2}(x)$ and integrating, using the second part of ([\[L1.2\]](#L1.2){reference-type="ref" reference="L1.2"}), we obtain $$\nu \int_{0}^{\infty}g_{1}'(x)\,g_{2}(x)\,dx=-\nu+\nu\int_{0}^{\infty}g_{2}(y)
\,g_{1}'(y)\,dy,$$ contradicting $\nu\neq0$.0◻\
Now that we know the eigenvalues $\lambda_{i}$ of $K$ are simple we can order them so that $\lambda_{0}>\lambda_{1}>\ldots$ . There is a permutation $\sigma$ of **N** such that the eigenvalue corresponding to $f_{i}$ is $\lambda_{\sigma(i)}$. This permutation is independent of $s$ since the eigenvalues $\mu_{i}$ and $\lambda_{i}$ both vary continuously with $s$. The next lemma allows us to compute $d\lambda_{i}/ds$ for each $i$.

**Lemma 2**. *Let $\lambda$ be a simple eigenvalue of an integral operator on $(0,1)$ with symmetric kernel of the form $s\,K(sx,sy)$ where $K(x,y)$ is smooth and symmetric. Let $f$ be a corresponding eigenfunction. Then* $$\frac{d\lambda}{ds}\,=\,\frac{\lambda}{s}\frac{f(1)^{2}} 
{\int_{0}^{1}f(x)^{2}\,dx}.$$ **Proof**. We may assume $f$ normalized so that $\int_{0}^{1}f(x)^{2}dx=1$. Then according to Lemma 3 of [@tw2] we have $$\frac{d\lambda}{ds}=\int_{0}^{1}\int_{0}^{1}\frac{\partial}{\partial s}(s\,K(sx,sy))\,
f(y)\,f(x)\,dy\,dx.$$ (This holds no matter what the form of the kernel.) In the case at hand the first factor in the integrand equals $$K(sx,sy)\,+\,(x\frac{\partial}{\partial x}\,+\,y\frac{\partial}{\partial y})K(sx,sy)$$ and we easily deduce from this that the integral itself equals $$\frac{\lambda}{s}\left(\int_{0}^{1}f(x)^{2}dx\,+\,\int_{0}^{1}x\,f'(x)\,f(x)\,dx\,+\,
\int_{0}^{1}y\,f'(y)\,f(y)\,dy\right)$$ and integration by parts shows that the expression in parentheses equals $f(1)^{2}$.0◻

**Remark**. It is easily seen that the conclusion of the lemma holds when the kernel has a mild singularity at $0$ such as our Besssel kernel has when $\al\,<\,0$.\
\
. *For each $i$ we have $\lambda_{i}\,\rightarrow\,1$ as $s\,\rightarrow\,\infty$.*\
\
**Proof**. The Hankel transform, when rescaled by the variable change $x\mapsto\sqrt{x}$, is the integral operator $H$ on $(0,\infty)$ with kernel $\hf J_{\al}(\sqrt{xy})$ and so our operator $K$ on $(0,s)$ may be thought of as $P_{s}\,H\,P_{s}\,H\,P_{s}$ where $P_{s}$ denotes the projection from $L_{2}
(0,\infty)$ to $L_{2}(0,s)$. Since, as is well-known, $H^{2}=I$, the minimax characterization of the eigenvalues shows that for each $i$ the eigenvalue of $P_{s}\,H\,P_{s}$ with i'th largest absolute value tends to $\pm\,1$ as $s\rightarrow
\infty$. Since our operator is the square of this one, the statement of the lemma follows. 0◻

We can now deduce the asymptotic formula (15) for the eigenvalues $\lambda_{i}$. We apply Lemma 2 to the eigenvalue $\lambda_{\sigma(i)}$ associated with the eigenfunction $f_{i}(x)$ of ([\[W2\]](#W2){reference-type="ref" reference="W2"}) and use ([\[W13\]](#W13){reference-type="ref" reference="W13"}) to deduce $$\frac{d\,\log\lambda_{\sigma(i)}}{ds}\sim\frac{2\pi}{\Gamma(\al+i+1)\,i!}
\,s^{i+\frac{\al}{2}}\,e^{-2\sqrt{s}}\,2^{4i+2\al+2}.$$ Recalling Lemma 3 we see that we can integrate from $s$ to $\infty$ and we obtain $$1\,-\,\lambda_{\sigma(i)}\sim\frac{2\pi}{\Gamma(\al+i+1)\,i!}\,
s^{i+\frac{\al+1}{2}}\,e^{-2\sqrt{s}}\,2^{4i+2\al+2}.$$

It remains to show that $\sigma(i)=i$ for all $i$. But it is clear from the above formula that $i<j$ implies that $\lambda_{\sigma(i)}>\lambda_{\sigma(j)}$ for large $s$ (and so for all $s$) and therefore $\sigma(i)<\sigma(j)$. Since $\sigma:{\bf N}
\rightarrow {\bf N}$ is onto, we must have $\sigma(i)=i$ for all $i$.

We wish to thank Professor F. J. Dyson for bringing to our attention the notion of "hard edge" random matrix ensembles. This work was supported in part by the National Science Foundation, DMS--9001794 and DMS--9216203, and this support is gratefully acknowledged.

::: references
E. W. Barnes, *The theory of the $G$-function*, Quart. J. Pure and Appl. Math. **31** (1900) 264--314.

E. L. Basor, C. A. Tracy, and H. Widom, *Asymptotics of level spacing distributions for random matrices*, Phys. Rev. Letts. **69** (1992) 5--8.

M. J. Bowick and E. Brézin, *Universal scaling of the tail of the density of eigenvalues in random matrix models*, Phys. Letts. **B268** (1991) 21--28.

B. V. Bronk, *Exponential ensemble for random matrices*, J. Math. Phys. **6** (1965) 228--237.

F. J. Dyson, *Fredholm determinants and inverse scattering problems*, Commun. Math. Phys. **47** (1976) 171--183.

F. J. Dyson, *The Coulomb fluid and the fifth Painlevé transcendent*, IASSNSS-HEP-92/43 preprint, to appear in the proceedings of a conference in honor of C. N. Yang, ed. S.-T. Yau.

A. Edelman, *Eigenvalues and Condition Numbers of Random Matrices*, SIAM J. Matrix Anal. Appl. **9** (1988) 543--560.

A. Edelman, *The distribution and moments of the smallest eigenvalue of a random matrix of Wishart type*, Linear Alg. and Its Appl. **159** (1991) 55--80.

A. Erdélyi (ed.), *Higher Transcendental Functions*, Vols. I and II (McGraw-Hill, New York, 1953).

H. Flaschka and A. C. Newell, *Monodromy- and Spectrum-Preserving Deformations I*, Commun. Math. Phys. **76** (1980) 65--116.

P. J. Forrester, *The spectrum edge of random matrix ensembles*, preprint.

I. S. Gradshteyn and I. M. Ryzhik, *Tables of Integrals, Series, and Products*, Corrected and Enlarged Edition (Academic, San Diego, 1980).

V. I. Gromak, *Reducibility of Painlevé equations*, Diff. Urav. **20** (1984) 1674--1683.

M. Jimbo, *Monodromy problem and the boundary condition for some Painlevé equations*, Publ. RIMS, Kyoto Univ. **18** (1982) 1137--1161.

M. Jimbo, T. Miwa, Y. Môri, and M. Sato, *Density matrix of an impenetrable Bose gas and the fifth Painlevé transcendent*, Physica **1D** (1980) 80--158.

R. D. Kamien, H. D. Politzer, and M. B. Wise, *Universality of random-matrix predictions for the statistics of energy levels*, Phys. Rev. Letts. **60** (1988) 1995--1998.

G. Mahoux and M. L. Mehta, *A method of integration over matrix variables: IV*, J. Phys. I France **1** (1991) 1093--1108.

M. L. Mehta, *Random Matrices*, 2nd edition (Academic, San Diego, 1991).

M. L. Mehta, *A non-linear differential equation and a Fredholm determinant*, J. de Phys. I France, **2** (1992) 1721--1729.

M. L. Mehta and G. Mahoux, *Level spacing functions and non-linear differential equations*, to appear in J. Phys. I France.

B. M. McCoy, C. A. Tracy, and T. T. Wu, *Painlevé functions of the third kind*, **18** (1977) 1058--1092.

G. Moore, *Matrix models of 2D gravity and isomonodromic deformation*, Prog. Theor. Physics Suppl. No. **102** (1990) 255--285.

T. Nagao and M. Wadati, *Correlation functions of random matrix ensembles related to classical orthogonal polynomials*, J. Phys. Soc. Japan **60** (1991) 3298--3322.

L. A. Pastur, *On the universality of the level spacing distribution for some ensembles of random matrices*, Letts. Math. Phys. **25** (1992) 259--265.

C. E. Porter, *Statistical Theory of Spectra: Fluctuations* (Academic, New York, 1965).

M. Sato, T. Miwa, and M. Jimbo, *Holonomic quantum fields, III, IV*, Publ. RIMS Kyoto Univ. **15** (1979) 577--629; **15** (1979) 871--972.

C. A. Tracy and H. Widom, *Introduction to random matrices*, to appear in the proceedings of the $8^{th}$ Scheveningen Conference, Springer Lecture Notes in Physics.

C. A. Tracy and H. Widom, *Level spacing distributions and the Airy kernel*, to appear in Commun. Math. Phys.

H. Widom, *The asymptotics of a continuous analogue of orthogonal polynomials*, to appear in J. Approx. Th.

T. T. Wu, B. M. McCoy, C. A. Tracy, and E. Barouch, *Spin-spin correlation functions for the two-dimensional Ising model: Exact theory in the scaling region*, Phys. Rev. **B13** (1976) 316--374.
:::
