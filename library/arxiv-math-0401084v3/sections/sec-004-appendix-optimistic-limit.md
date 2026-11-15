---
doc_id: arxiv-math-0401084v3
doc_title: "Some limits of the colored Jones polynomials of the figure-eight knot"
section_id: sec-004-appendix-optimistic-limit
section_title: "Appendix. Optimistic limit"
section_number: null
pages: 15-16
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
toc_source: outline
text_source: latex
latex_prose_ratio: 0.88
latex_coverage_ratio: 0.971
doc_brief: "Some limits of the colored Jones polynomials of the figure-eight knot — We calculate limits of the colored Jones polynomials of the ﬁgure- eight knot and conclude that in most cases they determine"
---
In this appendix, we will consider integral surgeries along the figure-eight knot.

Let $E_{p,1}$ be the $p$-surgery along the figure-eight knot with $p\in\mathbb{Z}$. Then our parameter $u$ and $v$ satisfies $pu+v=2\pi\sqrt{-1}$. From Corollary [\[cor:Vol_CS\]](#cor:Vol_CS){reference-type="ref" reference="cor:Vol_CS"} we have $$\operatorname{Vol}(E_{p,1})+\sqrt{-1}\operatorname{CS}(E_{p,1})
  \equiv
  \frac{H(u)}{\sqrt{-1}}-\pi{u}-\frac{uv}{4\sqrt{-1}}
  -\frac{\pi}{2}\lambda(\gamma)
  \mod{\pi^2\sqrt{-1}\mathbb{Z}}.$$ By [@Meyerhoff/Neumann:COMMH92 (4.6)], we have $$\lambda(\gamma)
  =\frac{2\pi\sqrt{-1}}{p}-\frac{v}{p}
  =u.$$ (Note that we follow orientation conventions of [@Neumann/Zagier:TOPOL85; @Yoshida:INVEM85] and so the sign of $v$ is opposite to that in [@Meyerhoff/Neumann:COMMH92].) Therefore $$\begin{split}
  &\operatorname{Vol}(E_{p,1})+\sqrt{-1}\operatorname{CS}(E_{p,1})
  \\
  &\quad\equiv
  {}-\sqrt{-1}\operatorname{Li}_2\left(y^{-1}\exp(-u)\right)
  +\sqrt{-1}\operatorname{Li}_2\left(y\exp(-u)\right)
  -\sqrt{-1}u\left\{\log(-y)+\pi\sqrt{-1}\right\}
  \\
  &\quad\quad
  -\pi{u}-\frac{u}{4\sqrt{-1}}(2\pi\sqrt{-1}-pu)
  -\frac{\pi}{2}u
  \\
  &\quad\equiv
  \frac{1}{\sqrt{-1}}
  \left\{
    \operatorname{Li}_2\left(y^{-1}\exp(-u)\right)
    -\operatorname{Li}_2\left(y\exp(-u)\right)
    +u\log(-y)-u\pi\sqrt{-1}+\frac{pu^2}{4}
  \right\}
  \\
  &\quad\quad\quad\mod{\pi^2\sqrt{-1}\mathbb{Z}}
\end{split}$$ and so $$\begin{gathered}
  -\operatorname{CS}(E_{p,1})+\sqrt{-1}\operatorname{Vol}(E_{p,1})
  \\
  \equiv
  \operatorname{Li}_2\left(y^{-1}\exp(-u)\right)
  -\operatorname{Li}_2\left(y\exp(-u)\right)
  +u\log(-y)-u\pi\sqrt{-1}+\frac{pu^2}{4}
  \mod{\pi^2\mathbb{Z}}.
\end{gathered}$$

Now we define $$\begin{split}
  V_p(\xi,\eta)
  &:=
  \operatorname{Li}_2\left(\xi^{-1}\eta^{-1}\right)
  -\operatorname{Li}_2\left(\xi\eta^{-1}\right)
  +(\log(-\xi))(\log{\eta})-\pi\sqrt{-1}\log\eta+\frac{p}{4}(\log{\eta})^2
  \\
  &=
  H(\xi,\eta)+\frac{p}{4}(\log{\eta})^2-2\pi\sqrt{-1}\log\eta.
\end{split}$$ We will calculate $\partial\,V_p(\xi,\eta)/\partial{\xi}\bigr|_{\xi=y,\eta=m^2}$ and $\partial\,V_p(\xi,\eta)/\partial{\eta}\bigr|_{\xi=y,\eta=m^2}$. First we have from [\[eq:y\]](#eq:y){reference-type="eqref" reference="eq:y"} $$\left.
    \frac{\partial\,V_p(\xi,\eta)}{\partial{\xi}}
  \right|_{\xi=y,\eta=m^2}
  =
  \left.
    \frac{\partial\,H(\xi,\eta)}{\partial{\xi}}
  \right|_{\xi=y,\eta=m^2}
  =
  0.$$ Next we have $$\left.
    \frac{\partial\,V_p(\xi,\eta)}{\partial\eta}
  \right|_{\xi=y,\eta=m^2}
  =
  \left.
    \frac{\partial\,H(\xi,\eta)}{\partial\eta}
  \right|_{\xi=y,\eta=m^2}
  +
  \frac{p\log\left(m^2\right)}{2m^2}
  -\frac{2\pi\sqrt{-1}}{m^2}.$$ On the other hand $$\begin{split}
  \frac{v}{2}
  &=
  \frac{d\,H(u,m^2)}{du}
  -\pi\sqrt{-1}
  \\
  &=
  \left.
    \frac{\partial\,H(\xi,\eta))}{d\xi}
  \right|_{\xi=y,\eta=m^2}
  +
  \left.
    \frac{\partial\,H(\xi,\eta)}{d\eta}
  \right|_{\xi=y,\eta=m^2}
  \times
  \frac{d\,m^2}{du}
  -
  \pi\sqrt{-1}
  \\
  &=
  \exp{u}\times
  \left.
    \frac{\partial\,H(\xi,\eta)}{d\eta}
  \right|_{\xi=y,\eta=m^2}
  -
  \pi\sqrt{-1}.
\end{split}$$ Therefore $$\left.
    \frac{\partial\,V_p(\xi,\eta)}{\partial\eta}
  \right|_{\xi=y,\eta=m^2}
  =
  \frac{v/2+\pi\sqrt{-1}}{\exp{u}}
  +\frac{pu}{2\exp{u}}
  -\frac{2\pi\sqrt{-1}}{\exp{u}}
  =0.$$

In [@Murakami:SURIK00] the first author calculated a 'fake' limit of the Witten--Reshetikhin--Turaev invariants of the $(p,1)$-Dehn surgery of the figure-eight knot and obtained the following observation.

::: obs*
Let $p$ be an integer between $-100$ and $100$, and $\tau_p$ the 'optimistic' limit of the Witten--Reshetikhin--Turaev invariant of the $(p,1)$-Dehn surgery along the figure-eight knot. Then there exists $(\xi_0,\eta_0)$ such that the following equalities hold numerically (up to 8 digits):

1.  $\dfrac{\partial\,V_p}{\partial\xi}(\xi_0,\eta_0)
      =\dfrac{\partial\,V_p}{\partial\eta}(\xi_0,\eta_0)=0$, and

2.  $\tau_p=V_p(\xi_0,\eta_0)=\operatorname{CS}(E_{p,1})+\sqrt{-1}\operatorname{Vol}(E_{p,1})$.
:::

Note that the observation above was confirmed by the second author [@Yokota:GTM02]. Note also that the sign of $\operatorname{CS}$ is reversed since the orientation convention here is different.
