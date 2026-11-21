---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-009-23-gaussian-integrals
section_title: "Gaussian integrals"
section_number: 2.3
pages: 13-14
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.947
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
Some computations involving the Gaussian density are used several times throughout the paper, so we decided to present them together here.

\begin{lemma}[Gaussian integrals]\label{lem:gaussintegral}~
\begin{enumerate}
\item \label{item:gaussmoment} moments: $$\frac{1}{\sqrt{2\pi}}\int_\R \E^{-\frac{x^2}{2}}\,x^{2m}\,dx=(2m-1)!!=(2m-1)(2m-3)\cdots 3\,1,$$ and the odd moments vanish.\vspace{2mm}
\item \label{item:gaussfourier} Fourier transform: with $g(x)=\frac{\E^{-\frac{x^2}{2}}}{\sqrt{2\pi}}$, one has
$$g^*(\zeta)=\int_\R g(x)\,\E^{\I x\zeta}\,dx=\E^{-\frac{\zeta^2}{2}}.$$
More generally, with the Hermite polynomials $H_{r}(x)=(-1)^{r}\,\E^{\frac{x^{2}}{2}}\,\,\frac{\partial^{r}}{\partial x^{r}}(\E^{-\frac{x^{2}}{2}})$, one has
$$(g\,H_{r})^{*}(\zeta)=(\I \zeta)^{r}\,\E^{-\frac{\zeta^{2}}{2}}.$$
\item \label{item:gausstail} tails: if $a \to +\infty$, then
\begin{align*}
&\int_{0}^{\infty} \E^{-\frac{(y+a)^{2}}{2}}\,dy=\frac{\E^{-\frac{a^{2}}{2}}}{a}\left(1-\frac{1}{a^{2}}+O\!\left(\frac{1}{a^{4}}\right)\right)\\
&\int_{0}^{\infty} y\,\E^{-\frac{(y+a)^{2}}{2}}\,dy=\frac{\E^{-\frac{a^{2}}{2}}}{a^{2}}\left(1+O\!\left(\frac{1}{a^{2}}\right)\right)\end{align*}
\begin{align*}
&\int_{0}^{\infty} y^{2}\,\E^{-\frac{(y+a)^{2}}{2}}\,dy=O\!\left(\frac{\E^{-\frac{a^{2}}{2}}}{a^{3}}\right)\\
&\int_{0}^{\infty} y^{3}\,\E^{-\frac{(y+a)^{2}}{2}}\,dy=O\!\left(\frac{\E^{-\frac{a^{2}}{2}}}{a^{2}}\right)
\end{align*}
In particular, the tail of the Gaussian distribution is $\frac{1}{\sqrt{2\pi}}\int_{a}^\infty\E^{-\frac{x^2}{2}}\,dx\simeq\frac{1}{a\sqrt{2\pi}}\,\E^{-\frac{a^2}{2}}$.
\vspace{1mm}
\item \label{item:gausscomplex} complex transform: for $\beta>0$,
$$
\int_{\R}\frac{\E^{-\frac{\beta^{2}}{2}}}{2\pi}\,\frac{\E^{-\frac{w^{2}}{2}}}{\beta+\I w}\,dw=\int_{\beta}^{\infty} \frac{\E^{-\frac{\alpha^{2}}{2}}}{\sqrt{2\pi}}\,d\alpha=\proba[\mathcal{N}_{\R}(0,1)\geq \beta].
$$
\vspace{1mm}
\end{enumerate}
\end{lemma}

\begin{proof}    
Recall that the generating series of Hermite polynomials (\cite[Chapter 5]{Sze75}) is 
$$\sum_{r =0}^{\infty} H_{r}(x)\,\frac{t^{r}}{r!}=\E^{\frac{x^2}{2}}\,\sum_{r=0}^\infty\frac{(-t)^r}{r!}\,\frac{\partial^r}{\partial x^r}\left(\E^{-\frac{x^2}{2}}\right)= \E^{\frac{x^2}{2}}\,\E^{-\frac{(x-t)^2}{2}}=\E^{-\frac{t^2}{2}+tx}.$$ 
Integrating against $g(x)\,\E^{\I x \zeta}\,dx$ yields
\begin{align*}\sum_{r=0}^\infty (g(x)\,H_r(x))^*(\zeta)\,\frac{t^r}{r!}&=\frac{1}{\sqrt{2\pi}}\int_\R \E^{-\frac{(x-t)^2}{2}+\I\zeta x}\,dx\\
&=\frac{\E^{\I\zeta t}}{\sqrt{2\pi}}\int_\R \E^{-\frac{y^2}{2}+\I\zeta y}\,dy = \E^{\I\zeta t-\frac{\zeta^2}{2}} = \sum_{r=0}^\infty (\I \zeta)^r\E^{-\frac{\zeta^2}{2}}\frac{t^r}{r!}
\end{align*}
whence the identity \eqref{item:gaussfourier} for Fourier transforms.\bigskip

With $r=0$, one gets the Fourier transform of the Gaussian $g^*(\zeta)=\E^{-\frac{\zeta^2}{2}}$, hence the moments \eqref{item:gaussmoment} by derivation at $\zeta=0$. The estimate of tails \eqref{item:gausstail} is obtained by an integration by parts; notice that similar techniques yield the tails of distributions $x^m\,\E^{-x^2/2}\,dx$ with $m\geq 1$. Finally, as for the complex transform \eqref{item:gausscomplex}, remark that 
$$F(\beta)=\int_{\R}\frac{\E^{-\frac{\beta^{2}}{2}}}{2\pi}\,\frac{\E^{-\frac{w^{2}}{2}}}{\beta+\I w}\,dw=\frac{1}{2\I\pi} \int_{\Gamma=\beta+ \I \R}\frac{\E^{\frac{(z-\beta)^{2}-\beta^{2}}{2}}}{z}\,dz,$$ the second integral being along the complex curve $\Gamma=\beta+\I \R$. 
By standard complex analysis arguments, this integral is the same along any line $\Gamma'=\beta'+i\R$ (for $\beta' >0$).
Namely
\[F(\beta)= \frac{1}{2\I\pi} \int_{\Gamma'=\beta'+ \I \R}\frac{\E^{\frac{(z-\beta)^{2}-\beta^{2}}{2}}}{z}\,dz.\]

Since $\lim_{\beta \to +\infty} F(\beta)=0$, 
$$
F(\beta)=-\int_\beta^\infty F'(\alpha)\,d\alpha
=\int_{\beta}^{\infty} \left(\frac{1}{2\I \pi}\int_{\Gamma'=\beta'+\I \R} \E^{\frac{(z-\alpha)^{2}-\alpha^{2}}{2}}\,dz\right)d\alpha.
$$
Again, the integration line $\Gamma'$ in the second integral can be replaced by 
$\Gamma=\alpha+\I \R$ and we get
$$F(\beta)
=\int_{\beta}^{\infty} \left(\frac{1}{2\I \pi}\int_{\Gamma=\alpha+\I \R} \E^{\frac{(z-\alpha)^{2}-\alpha^{2}}{2}}\,dz\right)d\alpha.
=\int_{\beta}^{\infty} \frac{\E^{-\frac{\alpha^{2}}{2}}}{\sqrt{2\pi}}\,d\alpha,$$
which is the tail $\proba[\mathcal{N}_{\R}(0,1)\geq \beta]$ of a standard Gaussian law.
\end{proof}
\noindent Also, there will be several instances of the Laplace method for asymptotics of integrals, but each time in a different setting; so we found it more convenient to reprove it each time.
\bigskip
\bigskip
