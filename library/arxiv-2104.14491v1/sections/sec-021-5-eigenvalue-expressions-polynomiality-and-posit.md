---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mos"
section_id: sec-021-5-eigenvalue-expressions-polynomiality-and-posit
section_title: "Eigenvalue expressions, polynomiality and positivity"
section_number: 5
pages: 11-12
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.918
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
Our evolution formulae for the Khovanov polynomials must give the positive Laurent polynomials in $q$ and $t$, but it is far from obvious that they do. Now we rewrite the formulae so that this property becomes explicit.

In this section, we introduce the eigenvalue variables $$\begin{aligned}
u=1,\ \ x=q^2t,\ \ y=q^4t^6.\label{evars}
\end{aligned}$$ as follows. First we substitute $$\begin{aligned}
q^2=\frac{x^4}{y},\ \ t=\frac{y}{x^3}.
\end{aligned}$$ Then we place proper powers of $u$ to complete the coefficients to the fractions of homogeneous polynomials, so that the total homogeneity degree is the same for all three coefficients in each series. Introduce the functions $$\begin{aligned}
S_2(\nu;y,x)=\mathtt{sgn}(\nu)\frac{x^{\nu}-y^{\nu}}{x-y}=\hspace{-3mm}\sum^{\max(0,\nu)}_{\substack{i+j=\nu-1\\\min(1,\nu)}}\hspace{-3mm}x^iy^j,
\end{aligned}$$ and $$\begin{aligned}
S_3(\nu;u,x,y)=\frac{u^{\nu}}{(u-x)(u-y)}+\frac{x^{\nu}}{(x-u)(x-y)}+\frac{y^{\nu}}{(y-u)(y-x)}=
\hspace{-3mm}\sum^{\max(0,\nu)}_{\substack{i+j+k=\nu-2\\\min(1,\nu)}}\hspace{-5mm}x^iy^jz^k  
\end{aligned}$$ Then the reduced AAK for the positive-torus half-family can be presented in an explicitly positive-polynomial form as $$\begin{aligned}
\mathfrak{K}^{\mathtt{Tor}_{n>0}}=x^{4n-2}\Big(\left(x^2+u^2+uy+y^2\right)S_2\left(\textstyle{\frac{1}{2}}(n-1);y^2,x^2\right)+S_3\left(2-n;u^2,x^2,y^2\right)\Big).
\label{Tor-eval}
\end{aligned}$$ A similar form for the negative-torus half-family can be obtained via the mirror symmetry $$\begin{aligned}
\mathfrak{K}^{\mathtt{Tor}_{n}}(x,y,u)=\mathfrak{K}^{\mathtt{Tor}_{-n}}(x^{-1},y^{-1},u^{-1}).
\end{aligned}$$ Similarly, the AAK for the twist family can be expanded as $$\begin{aligned}
\mathfrak{K}^{\mathtt{Tw}_n}=p_2x^{2\nu}+P_1S_2(\nu;u^2,x^2)+P_3S_2(\nu;y^2,x^2)+P_{13}S_3(\nu;u^2,x^2,y^2),\label{Tw-eval}
\end{aligned}$$ with the explicitly positive polynomial coefficients given by ([\[Tw-EvalC\]](#Tw-EvalC){reference-type="ref" reference="Tw-EvalC"}). Note that there are infinitely many expansions similar to ([\[Tor-eval\]](#Tor-eval){reference-type="ref" reference="Tor-eval"},[\[Tw-eval\]](#Tw-eval){reference-type="ref" reference="Tw-eval"}), and we just try to find the most nice one. $$\begin{aligned}
\begin{array}{|l|c|c|}
    \hline
    n&\ge2&\le0\\
    \hline\rule{0pt}{4mm}
    \nu&\frac{2-n}{2}\le0&\frac{-n}{2}\ge0\\
    \hline\rule{0pt}{4mm}
    p_2&x^{-9}y^{-1}\left(u^2x^2+u^2y^2+x^2y^2+ux(u^2+xy)\right)&0\\
    \hline\rule{0pt}{4mm}
    P_1&u^2x^{-7}(x+y)&u^4y^{-2}(u+x)(u+y)+u^6x^{-2}+u^2x^3y^{-1}\\
    \hline\rule{0pt}{4mm}
    P_3&x^{-6}y^{-1}(u+x)(u^2+xy)&x^{-1}y^{-1}(x+u)(ux^2+yu^2+xy^2+uxy)\\
    \hline\rule{0pt}{4mm}
    P_{13}&x^{-7}(u+x)(u+y)(x+y)(u^2+xy)&u^2x^{-1}y^{-1}(u+x)^2(u+y)(x+y)\\
    \hline
\end{array}
\label{Tw-EvalC}
\end{aligned}$$
