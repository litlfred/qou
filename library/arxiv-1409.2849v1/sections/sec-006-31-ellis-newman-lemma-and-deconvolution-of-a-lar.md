---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-006-31-ellis-newman-lemma-and-deconvolution-of-a-lar
section_title: "Ellis-Newman lemma and deconvolution of a large Gaussian noise"
section_number: 3.1
pages: 11-13
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.909
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
Suppose for a moment that  hypothesis \eqref{hyp:laplacemod} is replaced by the stronger hypotheses of Definition \ref{def:mod2}, with $c=+\infty$ and therefore $\mathcal{B}_c=\CC$. Fix then $0<a<b$, and consider the partial integral $\esper[\E^{(X_n)^2/2t_n}\,\mathbbm{1}_{t_na \leq X_n \leq t_nb}]$. By integration by parts of Riemann-Stieltjes integrals, one has:
\begin{align*}
\int_{t_na}^{t_nb}\E^{\frac{x^2}{2t_n}}\,\proba_n[dx] &= \left[-\E^{\frac{x^2}{2t_n}} \,\proba_n[X_n \geq x]\right]_{t_na}^{t_nb} + \int_{t_na}^{t_nb} \frac{x}{t_n}\,\E^{\frac{x^2}{2t_n}}\,\proba_n[X_n \geq x]\,dx\\
&=\left[-\E^{\frac{t_n\, x^2}{2}} \,\proba_n[X_n \geq t_nx]\right]_{a}^{b} + \int_{a}^{b} t_n x\,\E^{\frac{t_n\,x^2}{2}}\,\proba_n[X_n \geq t_n x]\,dx\\
&= \left(\left[-\frac{\psi(x)}{\sqrt{2\pi t_n}\,x}\right]_a^b +\sqrt{\frac{t_n}{2\pi}} \int_a^b \psi(x)\,dx\right)(1+o_{a,b}(1))\end{align*}
\begin{align*}
&=\left(\sqrt{\frac{t_n}{2\pi}} \int_a^b \psi(x)\,dx\right)(1+o_{a,b}(1))
\end{align*}
because of the estimates of precise deviations \eqref{eq:upbound}. In this computation, $o_{a,b}(1)$ is uniform for $a,b$ in compact sets of $(0,+\infty)$. In fact this estimate remains true for $a,b$ in a compact set of $\R$; hence, $a$ and $b$ can be possibly negative. If the  estimate is also true with $a=-\infty$ and $b=+\infty$, then 
\begin{align*}\qproba_n[t_na \leq Y_n \leq t_nb]&=\frac{\esper[\E^{(X_n)^2/2t_n}\,\mathbbm{1}_{t_na \leq X_n \leq t_nb}]}{\esper[\E^{(X_n)^2/2t_n}]}\\
& = \frac{\sqrt{\frac{t_n}{2\pi}}\,\int_a^b \psi(x)\,dx}{\sqrt{\frac{t_n}{2\pi}}\,\int_{-\infty}^{+\infty} \psi(x)\,dx}\, (1+o(1))\\
&= \frac{\int_a^b \psi(x)\,dx}{\int_{-\infty}^{+\infty} \psi(x)\,dx} \,(1+o(1)),
\end{align*}
so $(\frac{Y_n}{t_n})_{n \in \N}$ converges in law to the density $\psi(x)/\int_{\R}\psi(x)\,dx$.\bigskip

We now wish to identify the most general conditions under which this convergence in law happens. To this purpose, it is useful to produce random variables with density $\psi_n(x)/\int_{\R}\psi_n(x)\,dx$. They are given by the following Proposition, which appeared in \cite{EN78} as Lemma 3.3:

\begin{proposition}\label{prop:enlemma}
Let $G_n$ be a centred Gaussian variable with variance $\frac{1}{t_n}$, and independent from $Y_n$. The law of $W_n=G_n+\frac{Y_n}{t_n}$ has density $\psi_n(x)/\int_{\R}\psi_n(x)\,dx$.
\end{proposition}

\begin{proof}
Denote $Z_n=\esper[\E^{(X_n)^2/2t_n}]$, and $f_X(x)\,dx$ (respectively, $\proba_X$) the density (respectively, the law) of a random variable $X$. One has
\begin{align*}
\proba[W_n \leq w]&= \int_{- \infty}^w \left( \int_{\R} f_{G_n}(x-u)\,\proba_{\frac{Y_n}{t_n}}[du]\right)\,dx\\
&=\sqrt{\frac{t_n}{2\pi}}\int_{- \infty}^w \left( \int_{\R} \E^{-\frac{t_n\,(x-\frac{y}{t_n})^2}{2}}\,\proba_{Y_n}[dy]\right)\,dx\\
&=\sqrt{\frac{t_n}{2\pi}}\int_{- \infty}^w \left( \int_{\R} \E^{yx-\frac{y^2}{2t_n}}\,\qproba_{n}[dy]\right)\,\E^{-\frac{t_n\,x^2}{2}}\,dx\\
&=\frac{1}{Z_n}\,\sqrt{\frac{t_n}{2\pi}}\int_{- \infty}^w \left( \int_{\R} \E^{yx}\,\proba_{n}[dy]\right)\,\E^{-\frac{t_n\,x^2}{2}}\,dx\\
&=\frac{1}{Z_n}\,\sqrt{\frac{t_n}{2\pi}}\int_{- \infty}^w \psi_n(x)\,dx.
\end{align*}
Making $w$ go to $+\infty$ gives an equation for $Z_n=\sqrt{\frac{t_n}{2\pi}}\int_{\R} \psi_n(x)\,dx$. One concludes that:
$$\proba[W_n \leq w] = \frac{\int_{-\infty}^w \psi_n(x)\,dx}{\int_{-\infty}^\infty \psi_n(x)\,dx}.$$
\end{proof}
This important property was not used in our previous works: to get the residue of deconvolution $\psi_n$ of a random variable $X_n$ by a large Gaussian variable of variance $t_n$ (that is to say that one wants to \emph{remove} a Gaussian variable of variance $t_n$ from $X_n$), one can make the exponential change of measure \eqref{eq:exponchange}, and \emph{add} an independent Gaussian variable of variance $t_n$: the random variable thus obtained, which is $t_nW_n$ with the previous notation, has density proportional to $\psi_n(w/t_n)\,dw$.
\medskip
