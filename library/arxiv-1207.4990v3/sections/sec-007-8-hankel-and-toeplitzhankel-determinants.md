---
doc_id: arxiv-1207.4990v3
doc_title: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results"
section_id: sec-007-8-hankel-and-toeplitzhankel-determinants
section_title: "Hankel and Toeplitz+Hankel determinants"
section_number: 8
pages: 40-42
source_pdf: 1207.4990v3.pdf
source_sha256: 02aa065f4f65b857
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 1.0
doc_brief: "Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model. Some history and some recent results — 12 sections: Front matter; Setting the problem; Toeplitz meets Ising"
---
In [@DIK1] the authors also consider Hankel and Toeplitz + Hankel determinants with FH-type singularities. For a weight $w=w(x) \ge 0$ on $[-1,1]$, the associated Hankel determinant is given by [@Sz5] $$\label{eq108}
D_n^{(H)}(w) = \det \left(\int^1_{-1} x^{j+k}\, w(x) \, dx\right)^{n-1}_{j, k=0} \ .$$ The Hankel determinant $D_n^{(H)}(w)$ is related to the polynomials orthogonal with respect to the weight $w$ on the interval $[-1,1]$ in a similar way as a Toeplitz determinant is related to OPUC's.

For fixed $r=0,1,2, \dots$ we consider $w(x)$ of the following form: $$\label{eq109}
w(x) =e^{U(x)} \prod^{r+1}_{j=0} \left|x-\lambda_j\right|^{2\alpha_i}\, \omega_j(x)$$ where $$\begin{aligned}
&1=\lambda_0 > \lambda_1 > \dots > \lambda_{r+1} =-1, \\
&\omega_j(x) =  \left\{
\begin{array}{lll}
e^{i\pi\,\beta_j}, &\qquad  -1\le x\le \lambda_j, &\qquad \Re \beta_j \in \left(-\frac{1}{2}, \frac{1}{2}\right] \\
e^{-i\pi\,\beta_j}, &\qquad  1 \ge x > \lambda_j
\end{array}\right. \\
&\qquad \beta_0 = \beta_{r+1} =0, \qquad\qquad  \Re \alpha_j >-\frac{1}{2}, \qquad j=0,1, \dots, r+1
\end{aligned}$$ and where $U(x)$ is a sufficiently smooth function on $[-1,1]$.

::: remark
[]{#remark7 label="remark7"} Note that there is no loss of generality in setting $\beta_0 = \beta_{r+1}=0$ and $\Re\beta_j \in \left(-\frac{1}{2},
\frac{1}{2}\right]$ as the functions $\omega_0(x), \omega_{r+1}(x)$ are just constant on $(-1,1)$ and $\omega_j \left(x; \beta_j + k_j\right)
= (-1)^{k_j} \, \omega_j \left(x; \beta_j\right)$ for $k_j \in \mathbb{Z}$.
:::

In [@DIK1] the authors prove that for $w$ as in [\[eq109\]](#eq109){reference-type="eqref" reference="eq109"} with $\Re\beta_j \in \left(-\frac{1}{2}, \frac{1}{2}\right),
\:j=1, \dots, r$, as $n\to\infty$, $$\label{eq110}
D_n^{(H)}(w) =2^{-n^2} \, G^n_H \, n^{-\frac{1}{4}+2 \left(\alpha^2_0 + \alpha^2_r\right) + \sum^n_{j=1} \left(\alpha^2_j-\beta^2_j\right)}
\, E_H \left(1+o(1)\right)$$ for certain explicit constants $G_H$ and $E_H$ depending on $U(x)$, $\lambda_j$ and $\beta_j$ (see (1.37) in [@DIK1]). This result is derived by introducing the function $$\label{eq111}
f\!\left(e^{i\theta}\right) = f\!\left(e^{i(2\pi-\theta)}\right) \equiv w(\cos \theta) \, |\sin \theta|, \qquad\qquad 0\le \theta< 2\pi$$ on $S^1$. With $w$ as in [\[eq109\]](#eq109){reference-type="eqref" reference="eq109"}, $f$ has FH singularities of the form $$\label{eq112}
\begin{aligned}
f\!\left(e^{i\theta}\right) &= c\, e^{V\left(e^{i\theta}\right)} \left|z-1\right|^{4\alpha_0 +1} \left|z+1\right|^{4\alpha_{r+1} +1}
\, \prod^r_{j=1} \left|z-z_j\right|^{2\alpha_j}  \left|z-z'_j\right|^{2\alpha_j} \\
&\qquad\times \prod^r_{j=1} \left[g_{z_j, -\beta_j} (z) \, z^{\beta_j}_j \; g_{z'_j,\, \beta_j} (z)\left(z'_j\right)^{-\beta_j}\right],
\qquad 0 \le \theta<2\pi
\end{aligned}$$ where $$\left\{\begin{aligned}
\cos\,\theta_j &=\lambda_j,\quad z_j = e^{i\theta_j},\quad j=0,1,\dots, r+1,\quad 0=\theta_0< \theta_1 < \dots < \theta_{r+1} =\pi\\
z'_j &= e^{i\left(2\pi -\theta_j\right)}, \qquad j=0,1,\dots, r+1\\
c &= 2^{-2\left(\sum^{r+1}_{j=0} \,\alpha_j\right)-1} \; e^{2i \sum^r_{j=1}\, \beta_j \, \arcsin \lambda_j}
\end{aligned}
\right.$$ and $$\label{eq113}
V\!\left(e^{i\theta}\right) = U(\cos \theta).$$ The Hankel determinant $D_n^{(H)}(w)$ and the Toeplitz determinant $D_{2n}(f)$ are related in the following way: $$\label{eq114}
D_n^{(H)}(w)^2 = \frac{\pi^{2n}}{4^{(n-1)^2}} \; \frac{\left(\pi_{2n} (0) + 1 \right)^2}{\pi_{2n} (1) \, \pi_{2n}(-1)}
\; D_{2n} (f)$$ where $\pi_k(z)=z^k + \dots, k\ge 0$, are the monic orthogonal polynomials with respect to the weight $f\!\left(e^{i\theta}\right) \frac{d\theta}{2\pi}$ on $S^1$ as in [\[eq105\]](#eq105){reference-type="eqref" reference="eq105"}, $$\int^{2\pi}_0 \pi_k \left(e^{i\theta}\right) e^{-ij\theta} \, f\!\left(e^{i\theta}\right) \frac{d\theta}{2\pi} =0,
\qquad  0 \le j < k.$$ As the semi-norm $|||\beta||| <1$ for $f\!\left(e^{i\theta}\right)$, we may use Ehrhardt's result to evaluate $D_{2n}(f)$, $n\to\infty$, and the result [\[eq110\]](#eq110){reference-type="eqref" reference="eq110"} follows from [\[eq114\]](#eq114){reference-type="eqref" reference="eq114"} by computing the asymptotics for $\pi_{2n}
(z)$ for $z=0, \pm 1$. Note that if $\Re \beta_j = \frac{1}{2}$ for some $j \in \{0, 1, \dots, r+1\}$, then $\left|\Re \beta_j - \Re \left(-\beta_j\right)\right|=1$ and so $||| \beta |||=1$. In this case we would have had to use the Basor-Tracy form [\[eq100\]](#eq100){reference-type="eqref" reference="eq100"} for $D_{2n}(f)$: we have restricted our attention to the case $\Re \beta_j \in \left(-\frac{1}{2}, \frac{1}{2}\right)$ only for simplicity.

::: remark
[]{#remark8 label="remark8"} For a discussion of results of various authors, particularly Basor and Ehrhardt, related to [\[eq110\]](#eq110){reference-type="eqref" reference="eq110"}, see [@DIK1], Remark 1.24.
:::

For even FH symbols $f$, i.e., $f\!\left(e^{i\theta}\right) = f\!\left(e^{i(2\pi-\theta)}\right)$, the authors in [@DIK1] also consider Toeplitz + Hankel determinants of four types defined in terms of the Fourier coefficients $f_k$ of $f$, $$\label{eq115} 
\det \left(f_{j-k} + f_{j+k}\right)^{n-1}_{j,\, k=0}, \quad\det \left(f_{j-k}- f_{j+k+2}\right)^{n-1}_{j,\, k=0},
\quad\det \left(f_{j-k}\pm f_{j+k+1}\right)^{n-1}_{j,\,k=0}.$$ Such matrices arise, in particular, in the theory of classical groups and its application to random matrix theory and statistical mechanics, and there are simple relations between these determinants and Hankel determinants on $[-1,1]$ with added singularities at the end-points (see [@DIK1] and the references therein). For example, for $f\!\left(e^{i\theta}\right)=f\left(e^{i(2\pi-\theta)}\right)$, $$\label{eq116}
\det \left(f_{j-k} + f_{j+k}\right)^{n-1}_{j,\,k=0}=\frac{2^{n^2-2n +2}}{\pi^n} \: D_n^{(H)}(v)$$ where $D_n^{(H)}(v)$ is the Hankel determinant with symbol $v(x) = f\!\left(e^{i\theta(x)}\right)/\sqrt{1-x^2}$, $\theta(x)= \arccos x$, on $[-1,1]$, with similar formulae for the other three determinants. Let $f\!\left(e^{i\theta}\right) = f\left(e^{i(2\pi-\theta)}\right)$ with FH singularities at $0=\theta_0 < \theta_1 < \dots
< \theta_r < \theta_{r+1} =\pi$ and complementary singularities at $2\pi-\theta_j$, $1\le j \le r$. Suppose that $\Re \beta_j\in (-\frac{1}{2}, \frac{1}{2})$, $j=1, \dots, r$, and $\beta_0 = \beta_{r+1}=0$. Then utilizing [\[eq116\]](#eq116){reference-type="eqref" reference="eq116"} and [\[eq110\]](#eq110){reference-type="eqref" reference="eq110"}, the authors show that as $n\to\infty$ $$\label{eq117}
\begin{aligned}
\det \left(f_{j-k} + f_{j+k}\right)^{n-1}_{j,\,k=0} &= G^n_{T+H} \,  n^{\sum^{r}_{j=1} \left(\alpha^2_j-\beta^2_j\right)
+\frac{1}{2}\left(\alpha_0^2+\alpha_{r+1}^2-\alpha_0-\alpha_{r+1}\right)} \\
& \quad \times E_{T+H} \left(1+o(1)\right)
\end{aligned}$$ for certain explicit constants $G_{T+H}$, $E_{T+H}$, with similar results for the other three Toeplitz+Hankel determinants in [\[eq115\]](#eq115){reference-type="eqref" reference="eq115"}.

::: remark
[]{#remark9 label="remark9"} For a discussion of the related results of Basor and Ehrhardt for determinants of type [\[eq115\]](#eq115){reference-type="eqref" reference="eq115"}, see [@DIK1], Remark 1.27.
:::

::: remark
In [@FF] the authors discuss a large number of conjectures and results for Toeplitz, Hankel, and Toeplitz+Hankel determinants with FH-type singularities. The determinants arise in turn from problems in statistical physics. Many of the conjectures in [@FF] can now be resolved using results from [@DIK1] such as [\[eq110\]](#eq110){reference-type="eqref" reference="eq110"} and [\[eq117\]](#eq117){reference-type="eqref" reference="eq117"}.
:::
