---
doc_id: arxiv-1207.4990v3
doc_title: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results"
section_id: sec-006-7-basor-tracy-conjecture
section_title: "Basor-Tracy conjecture"
section_number: 7
pages: 36-40
source_pdf: 1207.4990v3.pdf
source_sha256: 02aa065f4f65b857
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.924
doc_brief: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results — 12 sections: Front matter; Setting the problem; Toeplitz meets Ising"
---
As already observed in [@BottSilb5] [@BottSilb6], Ehrhardt's condition on the seminorm, $|||\beta|||<1$, is not just a technical matter. In a critical calculation in 1991, Basor and Tracy [@BasTr] considered a particular symbol $f\!\left(e^{i\theta}\right)$ which has two FH singularities at $z_0=1$ and $z_1=e^{i\,\pi}=-1$ respectively $$\label{eq94}
f\!\left(e^{i\theta}\right) =  g_{1, \frac{1}{2}}(z) \, g_{-1, -\frac{1}{2}}(z)\, e^{i\,\pi/2}$$ with $\beta_0= \frac{1}{2}, \, \beta_1 = -\frac{1}{2}$ so that $|||\beta|||=1$. By direct computation they found that as $n\to \infty$ $$\label{eq95}
D_n(f) = \frac{1+(-1)^n}{2} \sqrt{\frac{2}{n}} \; G\left(\frac{1}{2}\right)^2  G\left(\frac{3}{2}\right)^2 \left(1+O(1)\right)$$ which is not of the general FH asymptotic form. Basor and Tracy observed, however, that $f\!\left(e^{i\theta}\right)$ had another FH representation with $\beta_0=-\frac{1}{2}$ and $\beta_1= \frac{1}{2}$, $$\label{eq96}
f\!\left(e^{i\theta}\right) =e^{i\,\pi} \:g_{1, -\frac{1}{2}} (z) \: g_{-1, \frac{1}{2}}(z) \, e^{-i\,\pi/2} \ .$$ If one substitutes the values $V=0$, $\alpha_0=\alpha_1=0$, $\beta_0=\frac{1}{2}$, $\beta_1=-\frac{1}{2}$ into [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"}, one obtains for [\[eq94\]](#eq94){reference-type="eqref" reference="eq94"} $$\begin{aligned}
&n^{-\left(\frac{1}{4} + \frac{1}{4}\right)} \,\left|1-e^{i\pi}\right|^{-\frac{1}{2}} \:\frac{G\left(\frac{3}{2}\right) G\left(\frac{1}{2}\right)
}{G(1)} \:\frac{G\left(\frac{1}{2}\right) G\left(\frac{3}{2}\right)}{G(1)} \; \left(1+o(1)\right)\\
&\qquad \qquad = (2n)^{-\frac{1}{2}} \: G\left(\tfrac{3}{2}\right)^2 \: G\left(\tfrac{1}{2}\right)^2 \left(1+ o(1)\right)
\end{aligned}$$ as $G(1)=1$. On the other hand, if one substitutes the values $V=i\,\pi$, $\alpha_0=\alpha_1=0$, $\beta_0=-\frac{1}{2}$, $\beta_1=\frac{1}{2}$, one obtains for [\[eq96\]](#eq96){reference-type="eqref" reference="eq96"} $$e^{in\pi} \,(2n)^{-\frac{1}{2}} \, G^2 \left(\tfrac{1}{2}\right) G^2\left(\tfrac{3}{2}\right) \left(1+ o(1)\right).$$ Just adding these two asymptotic forms, we obtain precisely the Basor-Tracy result [\[eq95\]](#eq95){reference-type="eqref" reference="eq95"}. So we see that if a symbol $f\!\left(e^{i\theta}\right)$ has more than one FH representation, then the asymptotics of $D_n(f)$ is given, at least in this case, by some combination of the Fisher-Hartwig asymptotics for each of them. Based on this example, Basor and Tracy [@BasTr] made the following bold, general conjecture. First note the following. Let $f\!\left(e^{i\theta}\right)$ be a Fisher-Hartwig symbol as in [\[eq74\]](#eq74){reference-type="eqref" reference="eq74"}. Let $n_0, n_1, \dots, n_m$ be a set of integers with $\sum^m_{j=0} n_j=0$, and let $f\left(z; \widehat{\beta}\right)$ denote the FH symbol obtained by replacing $\beta_j$ with $\widehat{\beta}_j= \beta_j+n_j$, $0\le j\le m$, and $e^{V(z)}$ by $\left(\prod^n_{j=0}
z_j^{n_i}\right) e^V = e^{V+i \sum^m_{j=0} \, n_j\, \theta_j}$. Then $f(\widehat{\beta})=f\left(z;\widehat{\beta}\right)$ gives another FH representation for $f(z)$, $$\label{eq97}
f(z) =f\left( z;\widehat{\beta}\right), \qquad \widehat{\beta}_j = \beta_j +n_j, \quad \sum^m_{j=0} n_j=0 \ .$$ Moreover, it is easy to see that all FH representations of $f(z)$ arise in this way. Given $\beta$, we call $$\label{eq98}
O_\beta = \left\{ \widehat{\beta}: \widehat{\beta}_j = \beta_j + n_j, \quad \sum^n_{j=0} n_j=0 \right\}$$ the *orbit* of $\beta$. We consider the discrete minimization problem $$\label{eq99}  
F_\beta = \min_{\widehat{\beta}\in O_\beta} \left(\sum^m_{j=0} \left(\Re \widehat{\beta}_j\right)^2\right).$$ It is clear that the minimum is indeed obtained in $O_\beta$. Let $\mathcal{M}_\beta=\left\{\widehat{\beta}\in O_\beta
: \sum^n_{j=0} \left(\Re \widehat{\beta}_j\right)^2 = F_\beta\right\}$. We say $\mathcal{M}_\beta$ is *non-degenerate* if $\alpha_i \pm \widehat{\beta}_j \neq -1, -2, \dots$ for all $j=0, \dots, m$ and all $\widehat{\beta}\in \mathcal{M}_\beta$.

::: conject
[@BasTr][]{#conject8 label="conject8"} Let $f\!\left(e^{i\theta}\right)$ be given as in [\[eq74\]](#eq74){reference-type="eqref" reference="eq74"} with $V\!\left(e^{i\theta}\right)$ sufficiently smooth on $S^1$ and $\Re \alpha_j
>-\frac{1}{2}$, $0\le j\le m$. Suppose $\mathcal{M}_\beta$ is non-degenerate. Then as $n\to\infty$, $$\label{eq100}
D_n(f) = \sum_{\widehat{\beta}\in \mathcal{M}_\beta} \left[R_n \left(f(\widehat{\beta})\right) (1+o(1))\right].$$ Each $R_n\left(f(\widehat{\beta})\right)$ stands for the FH asymptotic form [\[eq84\]](#eq84){reference-type="eqref" reference="eq84"} [\[eq89\]](#eq89){reference-type="eqref" reference="eq89"} with $\widehat{\beta}$ and $\left(\prod^m_{j=0} z_j^{n_j} \right) e^V$ in place of $\beta$ and $e^V$ respectively.
:::

Note that by the definition of $\mathcal{M}_\beta$, all the terms $R_n\left(f(\widehat{\beta})\right)$ in [\[eq100\]](#eq100){reference-type="eqref" reference="eq100"} have the same order of magnitude. Indeed for all $\widehat{\beta}\in \mathcal{M}_\beta$, $\Re \sum^m_{j=0}\, \widehat{\beta}_j^2=
F_\beta-\sum^m_{j=0} \left(\Im \beta_j\right)^2$.

To see how this conjecture works for $f\!\left(e^{i\theta}\right)$ in [\[eq94\]](#eq94){reference-type="eqref" reference="eq94"}, where $\beta_0 = \frac{1}{2}$ and $\beta_1=
-\frac{1}{2}$, and $n_0 + n_1 =0$, consider $$\sum^1_{j=0} \left(\Re  \beta_j + n_j \right)^2 = \left(\frac{1}{2}+ n_0 \right)^2 + \left(-\frac{1}{2}-n_0 \right)^2  = 2 \left(\frac{1}{2}+ n_0\right)^2$$ which clearly achieves its minimum at $n_0=0=-n_1$ and also at $n_0=-1=-n_1$. These values correspond to $\widehat{\beta}= \beta=\left(\frac{1}{2}, -\frac{1}{2}\right)$ and $\widehat{\beta}= \left(\frac{1}{2}-1, -\frac{1}{2}+ 1\right)= \left(-\frac{1}{2}, \frac{1}{2}\right)$, respectively. Thus the leading asymptotics of $D_n(f)$ is a sum of contributions from $f(z) = f(z;\beta)$ and $f(z) = f\left(z;\widehat{\beta}\right)$, as in [\[eq95\]](#eq95){reference-type="eqref" reference="eq95"}.

Conjecture [\[conject8\]](#conject8){reference-type="ref" reference="conject8"} was proved recently in [@DIK1].

::: theorem
[]{#BT label="BT"} [@DIK1] Conjecture [\[conject8\]](#conject8){reference-type="ref" reference="conject8"} holds.
:::

The relation of the semi-norm $|||\beta|||$ to the minimization problem is given by the following elementary result.

::: lemma
[]{#lem9 label="lem9"}[@DIK1] Given $\beta$, there are only two, mutually exclusive, possibilities: Either

1.  There exists $\widehat{\beta}\in O_\beta$ such that $|||\widehat{\beta}||| <1$. Then such a $\widehat{\beta}$ is unique and it is the unique element of $\mathcal{M}_\beta=\left\{\widehat{\beta}\right\}$

or

1.  There exists $\widehat{\beta}\in O_\beta$ such that $|||\widehat{\beta}|||=1$. Then there are at least two such $\widehat{\beta}$'s and all of them are obtained from each other by a repeated application of the following rule: add 1 to a $\widehat{\beta}_j$ with the smallest real part, $\Re\widehat{\beta}_j = \min_k \, \Re  \widehat{\beta}_k$, and subtract 1 from a $\widehat{\beta}_{j'}$ with the largest real part, $\Re\widehat{\beta}_{j'} = \max_k \:\Re  \widehat{\beta}_k$. Moreover $\mathcal{M}_\beta=\left\{ \widehat{\beta}\in O_\beta: |||\widehat{\beta}||| =1 \right\}$.
:::

Clearly for $f\!\left(e^{i\theta}\right)$ in [\[eq94\]](#eq94){reference-type="eqref" reference="eq94"}, $|||\widehat{\beta}|||=1$, if and only if $\widehat{\beta}=\beta$ or $\widehat{\beta}=\beta
+(-1, 1)$. Also we see from (i) that the case $|||\beta ||| <1$ in Ehrhardt's Theorem corresponds to a unique minimizer in [\[eq99\]](#eq99){reference-type="eqref" reference="eq99"}, and hence to a single term in [\[eq100\]](#eq100){reference-type="eqref" reference="eq100"}.

The proof of Conjecture [\[conject8\]](#conject8){reference-type="ref" reference="conject8"} in [@DIK1] proceeds as follows. Given $\beta$, if there exists $\widehat{\beta}\in O_\beta$ with $|||\widehat{\beta}|||<1$, then $\widehat{\beta}$ is unique and as $n\to\infty$, $D_n(f) = R_n \left(f(\widehat{\beta})\right)
(1+o(1))$ (Ehrhardt's Theorem). On the other hand, if there exists $\widehat{\beta}\in  O_\beta$ with $|||\widehat{\beta}|||=1$, then $\mathcal{M}_\beta = \left\{\widehat{\beta}\in O_\beta: ||| \widehat{\beta}||| =1\right\}$ has at least two elements. Then for some $b$, $$\label{eq101}
b \le \Re  \widehat{\beta}_j \le b+1$$ for all $\widehat{\beta}_j$, and for some $p,\, \ell >0$ there are $p$ values of $j$ such that $\Re\widehat{\beta}_j=b$ and $\ell$ values for which $\Re \widehat{\beta}_j = b+1$. Let $\widetilde{f}\!\left(e^{i\theta}\right)$ be the FH symbol (*not* a FH-representation of $f\!\left(e^{i\theta}\right)$) with $\alpha_j$, $V$ as before but $\tilde{\beta}_j=
\widehat{\beta}_j$ if $\Re \widehat{\beta}_j < b+1$ and $\tilde{\beta}_j = \widehat{\beta}_j-1$ if $\Re \widehat{\beta}_j = b+1$. Then clearly $$\label{eq102}
f(z) = c\, z^\ell\, \widetilde{f}(z)$$ for some simple constant $c$, and by a general relation $$\label{eq103}
D_n(f) = \frac{c^n (-1)^{\ell n} \, F_n\, D_n (\widetilde{f})}{\prod^{\ell-1}_{j=0} j!}$$ where $$\label{eq104}
F_n = \det \left(\frac{d^{j}\widetilde{\pi}_{n+k}}{dz^j}\,(0) \right)_{0\le j, k\le \ell-1}\$$ and $\widetilde{\pi}_q(z) = z^q + \dots,  q \ge 0$, are the monic orthogonal polynomials with respect to the (in general non-real) weight $\widetilde{f}\!\left(e^{i\theta}\right) \frac{d\theta}{2\pi}$ on $S^1$, $$\label{eq105}
\int^{2\pi}_0 \widetilde{\pi}_q \left(e^{i\theta}\right) e^{-ir\theta} \: \widetilde{f}\!\left(e^{i\theta}\right) \frac{d\theta}{2\pi} =0,
\qquad 0 \le r< q.$$ (A part of the proof of Conjecture [\[conject8\]](#conject8){reference-type="ref" reference="conject8"} consists in showing that the $\widetilde{\pi}_q$'s exist and are unique for $q$ sufficiently large, $q\ge q_{\widetilde{f}}$.) Now clearly $|||\tilde{\beta}|||<1$, and so we can evaluate $D_n(\widetilde{f})$ as $n\to\infty$ using Ehrhardt's Theorem. The proof of the conjecture then reduces by [\[eq103\]](#eq103){reference-type="eqref" reference="eq103"} [\[eq104\]](#eq104){reference-type="eqref" reference="eq104"} to evaluating the polynomials $\widetilde{\pi}_n(z),  \dots,
\widetilde{\pi}_{n+\ell-1}(z)$ and their derivatives at $z=0$, as $n\to\infty$. This is effected by using the steepest-descent method of Deift and Zhou for Riemann-Hilbert problems mentioned in Section [\[secSzego\]](#secSzego){reference-type="ref" reference="secSzego"} above (see also, for example, [@DKMVZ1], [@DKMVZ2]). The fact that orthogonal polynomials with respect to a weight on the line, can be expressed in terms of a Riemann-Hilbert problem is due to Fokas, Its and Kitaev in [@FIK]: the extension of this result to orthogonal polynomials on the circle is given in [@BDJ].

::: remark
[]{#degen label="degen"} As noted above, for the Ising model, at $T>T_c$, $\varphi_{\text{ons}}\!\left(e^{i\theta}\right)$ in [\[106\]](#106){reference-type="eqref" reference="106"} corresponds to a degenerate case for Ehrhardt's Theorem. However $\varphi_{\text{ons}}\!\left(e^{i\theta}\right)=-e^{-i\theta}
\;\widetilde{\varphi}\!\left(e^{i\theta}\right)$ where $\widetilde{\varphi}\!\left(e^{i\theta}\right)= \frac{\left(1-\gamma_1\, e^{i\theta}\right) \left(\gamma_2-e^{i\theta}\right)}{
\left|1-\gamma_1\,e^{i\theta}\right| \left|1-\gamma_2 \, e^{i\theta}\right|}$ is smooth, nonzero, and has no winding on $S^1$. Hence $D_n(\widetilde{\varphi})$ can be computed as $n\to\infty$ using SSLT as in [\[eq47\]](#eq47){reference-type="eqref" reference="eq47"}. Analogous to [\[eq102\]](#eq102){reference-type="eqref" reference="eq102"}, [\[eq103\]](#eq103){reference-type="eqref" reference="eq103"}, we have the formula $$\label{eq106}
D_n (\varphi_{\text{ons}}) = \widehat{\pi}_n(0) \, D_n(\widetilde{\varphi})$$ where $\widehat{\pi}_n(z)=z^n + \dots, n\ge 0$ are the complementary orthogonal polynomials to the $\widetilde{\pi}_n$'s (see [@DIK1]) $$\label{eq107}
\int^{2\pi}_0 \widehat{\pi}_n \!\left(e^{-i\theta}\right) e^{i\,j\theta}\: \widetilde{\varphi}\!\left(e^{i\theta}\right) \frac{d\theta}{2\pi} =0,
\qquad 0 \le j < n.$$ Applying the steepest descent method to the Riemann-Hilbert Problem for $\widehat{\pi}_n$, and taking into account the analyticity of $\widetilde{\varphi}(z)$ in an annulus around $\{|z|=1\}$, we obtain the precise decay rate of $\widehat{\pi}_n(0)$ as $n\to\infty$, and hence via [\[eq106\]](#eq106){reference-type="eqref" reference="eq106"}, the precise leading order exponential decay rate $c n^{-1/2}\gamma^{-n}_2 \left(1+o(1)\right)$ as in [\[eq64\]](#eq64){reference-type="eqref" reference="eq64"}. The steepest descent method also yields the higher order terms in the expression, to any desired order. An alternative, and very elegant, proof of [\[eq64\]](#eq64){reference-type="eqref" reference="eq64"} using a contour deformation argument, is given in [@FF]. For $\varphi_{\rm diag}(e^{i\theta})$ and the diagonal correlation function, the situation is similar, and one obtains: $$\left\langle\sigma_{1,1}\,\sigma_{1+n, 1+n}\right\rangle=
\frac{k_{\rm ons}^{-n}}{\sqrt{n}}
\frac{\sqrt{\pi}}{(1-k_{\rm ons}^{-2})^{1/4}}(1+o(1)),\qquad T>T_c.$$ We also note that in Section 10.7 of [@BottSilb3] and in the papers [@BottWid1] [@Wid7], the authors also analyze the Toeplitz determinants arising in the case $T>T_c$.
:::

::: remark
[]{#remark6 label="remark6"} Formulae [\[eq103\]](#eq103){reference-type="eqref" reference="eq103"} and [\[eq106\]](#eq106){reference-type="eqref" reference="eq106"} should be compared respectively with formulae [\[eq61\]](#eq61){reference-type="eqref" reference="eq61"} and [\[eq52\]](#eq52){reference-type="eqref" reference="eq52"} in [@FisHart1].
:::
