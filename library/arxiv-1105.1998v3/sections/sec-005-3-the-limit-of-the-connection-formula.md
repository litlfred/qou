---
doc_id: arxiv-1105.1998v3
doc_title: "A Connection Formula of the Hahn-Exton q-Bessel Function"
section_id: sec-005-3-the-limit-of-the-connection-formula
section_title: "The limit of the connection formula"
section_number: 3
pages: 6-7
source_pdf: 1105.1998v3.pdf
source_sha256: daf3bffad8eb2749
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.929
doc_brief: "A Connection Formula of the Hahn-Exton q-Bessel Function — We show a connection formula of the Hahn–Exton q-Bessel function around the origin and the infinity."
---
[]{#section3 label="section3"}

In this section, we show that the limit $p\to 1^-$ of the connection formula gives a connection formula of the Bessel function. At first, we assume that $0<p<1$ and $0<\sqrt{p}<1$. For the Bessel function, we set the Hankel function of the first and the second kind $H_\nu^{(1)}(z)$ and $H_\nu^{(2)}(z)$.

::: definition
The Hankel function of the first kind is given by $$H_\nu^{(1)}(z):=\frac{\Gamma \left(\frac{1}{2}-\nu\right)}{\pi i\sqrt{\pi}}\left(\frac{z}{2}\right)^\nu\int_{1+\infty i}^{(1+)}e^{izt}\left(t^2-1\right)^{\nu -\frac{1}{2}}dt,\qquad -\pi <\arg z<2\pi .$$ The Hankel function of the second kind is defined by $$H_\nu^{(2)}(z):=\frac{\Gamma \left(\frac{1}{2}-\nu\right)}{\pi i\sqrt{\pi}}\left(\frac{z}{2}\right)^\nu\int_{-1+\infty i}^{(-1-)}e^{izt}\left(t^2-1\right)^{\nu -\frac{1}{2}}dt,\qquad -2\pi <\arg z<\pi .$$
:::

The contour for $H_\nu^{(1)}(z)$ is a path starting from $t=+1+\infty i$, rounding the circle around $t=1$ counterclockwise, and going back to $t=+1+\infty i$. Moreover, the contour for $H_\nu^{(2)}(z)$ is a path starting from $t=-1+\infty i$, rounding the circle around $t=1$ clockwise, and going back to $t=-1+\infty i$.

The Hankel functions can be written by $J_\nu (z)$: $$\begin{gathered}
H_\nu^{(1)}(z) =\frac{ie^{-\nu\pi i}}{\sin\nu\pi}\left\{J_\nu (z)-e^{\nu\pi i}J_{-\nu}(z)\right\},\label{ha1}\\
H_\nu^{(2)}(z) =-\frac{ie^{\nu\pi i}}{\sin\nu\pi}\left\{J_\nu (z)-e^{-\nu\pi i}J_{-\nu}(z)\right\}.\label{ha2}
\end{gathered}$$ The Hankel functions have asymptotic expansions around $z=0$ [@Ol]: $$\begin{gathered}
H_\nu^{(1)}(z) \sim \left(\frac{2}{\pi z}\right)^{\frac{1}{2}}e^{i\zeta}\sum_{s\ge 0}i^s\frac{A_s(\nu )}{z^s},\qquad -\pi +\delta \leq \arg z\leq 2\pi -\delta ,\\
H_\nu^{(2)}(z) \sim \left(\frac{2}{\pi z}\right)^{\frac{1}{2}}e^{-i\zeta}\sum_{s\ge 0}(-i)^s\frac{A_s(\nu )}{z^s},\qquad -2\pi +\delta \leq \arg z\leq \pi -\delta ,
\end{gathered}$$ as $z\to \infty$. Here, $\delta$ is an any small constant, $$A_s(\nu )=\frac{(4\nu^2-1^2)(4\nu^2-3^2)\cdots \left\{4\nu^2-(2s-1)^2\right\}}{s!8^s}$$ and $$\zeta =z-\frac{1}{2}\nu\pi -\frac{1}{4}\pi .$$ In this sense, ([\[ha1\]](#ha1){reference-type="ref" reference="ha1"}) and ([\[ha2\]](#ha2){reference-type="ref" reference="ha2"}) considered as connection formula of the Bessel equation.
