---
doc_id: arxiv-2509.20302v1
doc_title: "Universality in the resurgence of generalized Tracy-Widom distributions"
section_id: sec-002-3-trans-series-expansion
section_title: "Trans-series expansion"
section_number: 3
pages: 2-3
source_pdf: 2509.20302v1.pdf
source_sha256: 59837f5b511c9e07
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.901
doc_brief: "Universality in the resurgence of generalized Tracy-Widom distributions — We analyze determinants associated with Bessel kernels and generic symbol functions, which govern a class of ob- servables"
---
Based on the previous results [@Bajnok2024; @Bajnok20251], concrete examples and many consistency checks we conjecture that the strong coupling expansion (valid for $g>0$) has the trans-series structure $$\begin{aligned}
{\cal D}(g)=A & e^{4\pi g\sum_{i}(x_{i}-y_{i})}g^{\frac{\beta^{2}+2\ell\beta}{2}}\times\\
 & \quad\sum_{\{\delta_{i}=0,1\}}e^{-8\pi g\sum_{i}\delta_{i}x_{i}}S^{\{\delta_{i}\}}{\cal D}^{\{\delta_{i}\}}(g)\nonumber 
\end{aligned}$$ where ${\cal D}^{\{\delta_{i}\}}(g)$ are asymptotic series in $g^{-1}$, $e^{-8\pi gx_{i}}$ are non-perturbative scales and $S^{\{\delta_{i}\}}$ are their corresponding Stokes constants. $A$ is a convenient normalization, which can be calculated from $\chi$ [@Beccaria:2022ypy]. The generic framework to calculate the trans-series for the logarithm of the determinant already provides a similar structure. The simplification is that the sum involves only at most once each non-perturbative scale, so no higher power appears (similarly to the expectation value of the Wilson loop). In particular, if we have only a finite number of zeros, then the trans-series contains only a finite number of non-perturbative corrections.

The logarithm of the perturbative part $\ln D^{\{0,0,\dots\}}(g)$ was already calculated in [@Belitsky:2020qrm; @Belitsky:2020qir]. After exponentialization we parametrize it as $${\cal D}^{\{\}}(g)\equiv{\cal D}^{\{0,0,\dots\}}(g)=\sum_{k=0}^{\infty}{\cal D}_{k}^{\{\}}g^{-k}$$ by introducing the convention that in the upper index we list the nonzero $\delta$s only. The coefficients can be calculated from a system of integro-differential equation with the first few coefficients being [@Belitsky:2020qrm; @Belitsky:2020qir]: $$\begin{aligned}
{\cal D}_{0}^{\{\}} & =1\quad;\quad{\cal D}_{1}^{\{\}}=\frac{1-4\ell_{\beta}^{2}}{16}I_{1}\\
{\cal D}_{2}^{\{\}} & =\frac{16\ell_{\beta}^{4}-40\ell_{\beta}^{2}+9}{512}I_{1}^{2}\quad;\quad\ell_{\beta}=\ell+\beta\nonumber \\
{\cal D}_{3}^{\{\}} & =-\frac{\left(16\ell_{\beta}^{4}-40\ell_{\beta}^{2}+9\right)\left((4\ell_{\beta}^{2}-17)I_{1}^{3}+8I_{2}\right)}{24576}\nonumber 
\end{aligned}$$ in terms of the moments: $$I_{n}=(-1)^{n-1}\sum_{k\geq1}\left[\frac{1}{(2\pi x_{k})^{2n-1}}-\frac{1}{(2\pi y_{k})^{2n-1}}\right]\label{eq:moments}$$ We choose $S^{\{\}}=1$, which fixes $A$ uniquely. Assigning the degree $n$ to $I_{n}$ we can show that only terms with degree up to the given order appear. Higher order expressions, ${\cal D}_{k>3}^{\{\}}$, can be obtained from [@Belitsky:2020qrm; @Belitsky:2020qir] by exponentiation.

The leading non-perturbative correction is related to the nearest zero $x_{1}$, has magnitude $e^{-8\pi gx_{1}}$, and can be parametrized as $${\cal D}^{\{1\}}(g)\equiv{\cal D}^{\{1,0,\dots\}}(g)=\sum_{k=0}^{\infty}{\cal D}_{k}^{\{1\}}g^{-k}$$ Using the methods developed in [@Bajnok2024; @Bajnok20251] the coefficients can be determined to be $$\begin{aligned}
{\cal D}_{0}^{\{1\}} & =1\quad;\quad{\cal D}_{1}^{\{1\}}=\frac{\left(1-4\ell_{\beta}^{2}\right)(\pi x_{1}I_{1}-1)}{16\pi x_{1}},\\
{\cal D}_{2}^{\{1\}} & =\frac{\left(16\ell_{\beta}^{4}-40\ell_{\beta}^{2}+9\right)(\pi x_{1}I_{1}-1)^{2}}{512\pi^{2}x_{1}^{2}}\nonumber \\
{\cal D}_{3}^{\{1\}} & =-\frac{\left(16\ell_{\beta}^{4}-40\ell_{\beta}^{2}+9\right)}{24576\pi^{3}x_{1}^{3}}\biggl(4\ell_{\beta}^{2}(\pi x_{1}I_{1}-1)^{3}+\nonumber \\
 & 8\pi^{3}x_{1}^{3}I_{2}-17\pi x_{1}I_{1}(\pi x_{1}I_{1}(\pi x_{1}I_{1}-3)+3)+19\biggr)\nonumber 
\end{aligned}$$ and the corresponding Stokes constant is [@Beccaria:2022ypy; @Bajnok2024; @Bajnok20251] $$\begin{aligned}
S^{\{1\}} & =\frac{e^{i\pi\ell_{\beta}}}{4\pi x_{1}}\frac{\Phi(2i\pi x_{1})}{\Phi'(-2i\pi x_{1})}\\
 & =-ie^{i\pi\ell_{\beta}}\prod_{j>1}\frac{(x_{1}+x_{j})}{(x_{1}-x_{j})}\prod_{j}\frac{(x_{1}-y_{j})}{(x_{1}+y_{j})}\nonumber 
\end{aligned}$$ We have calculated many more terms, ${\cal D}_{k}^{\{1\}}$, for $k=4,\dots$ and observed that the perturbative part can be mapped to the leading non-perturbative correction by the replacements $I_{n}\to I_{n}+\frac{2(-1)^{n}}{(2\pi x_{1})^{2n-1}}$.

This is a very interesting result and has far-reaching consequences. First, it implies that the two asymptotic series ${\cal D}^{\{\}}$ and ${\cal D}^{\{1\}}$ have the *same perturbative expansion* in terms of their own moments $I_{n}^{\{\}}\equiv I_{n}$ and $I_{n}^{\{1\}}=I_{n}^{\{\}}+\frac{2(-1)^{n}}{(2\pi x_{1})^{2n-1}}$. From the definition of the moments it is clear, that if $I_{n}^{\{\}}$ corresponds to $\{x_{1},x_{2},\dots\vert y_{1},y_{2},\dots\}$ then $I_{n}^{\{1\}}$ corresponds to $\{-x_{1},x_{2},\dots\vert y_{1},y_{2},\dots\}\equiv\{x_{2},\dots\vert x_{1},y_{1},y_{2},\dots\}$. This nicely matches with the magnitude of the correction $e^{-8\pi gx_{1}}$, which alltogether with the $e^{4\pi gx_{1}}$ prefactor flips also the sign of $x_{1}$ in the exponent. Formally we are turning $x_{1}$ to a new $y$. We can then think of ${\cal D}^{\{1\}}$ as the perturbative part corresponding to the symbol $\Phi^{\{1\}}$ labeled by $\{x_{2},\dots\vert x_{1},y_{1},y_{2},\dots\}$.

In the case of the Wilson loop, when we have only one $x_{1}$, the transformation $x_{1}\to-x_{1}$ changes the sign of every moment, which leads to the observed $w_{n}\to(-1)^{n}w_{n}$ relation.
