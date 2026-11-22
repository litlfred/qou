---
doc_id: arxiv-math-0401084v3
doc_title: "Some limits of the colored Jones polynomials of the figure-eight knot"
section_id: sec-003-4-proof-of-the-main-theorem
section_title: "Proof of the main theorem"
section_number: 4
pages: 14-15
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
toc_source: outline
text_source: latex
latex_prose_ratio: 0.871
latex_coverage_ratio: 0.818
doc_brief: "Some limits of the colored Jones polynomials of the figure-eight knot — We calculate limits of the colored Jones polynomials of the ﬁgure- eight knot and conclude that in most cases they determine"
---
In this section we will prove the main theorem.

First we will calculate the derivative of $H(u):=H(y,m^2)$.

::: lem
$$\frac{d\,\bigl(H(u)-\pi\sqrt{-1}u\bigr)}{du}
  =
  \frac{v}{2}.$$
:::

::: proof
*Proof.* We first calculate the partial derivatives of $H(\xi,\eta)$. We have $$\begin{split}
  \frac{\partial\,H(\xi,\eta)}{\partial\xi}
  &=
  \
  \frac{1}{\xi}
  \left\{
     \log\left(1-\xi^{-1}\eta^{-1}\right)
    +\log\left(1-\xi\eta^{-1}\right)
    +\log\eta
  \right\}
  \\
  &=
  \frac{1}{\xi}\log\left(\eta+\eta^{-1}-\xi-\xi^{-1}\right)
\end{split}$$ and $$\begin{split}
  \frac{\partial\,H(\xi,\eta)}{\partial\eta}
  &=
  \frac{1}{\eta}
  \left\{
     \log\left(1-\xi^{-1}\eta^{-1}\right)
    -\log\left(1-\xi\eta^{-1}\right)
    +\log(-\xi)
  \right\}
  \\
  &=
  \frac{1}{\eta}
  \left\{
    \log\left(\frac{1-\xi\eta}{\eta-\xi}\right)
    +\pi\sqrt{-1}
  \right\}.
\end{split}$$ Since $$\left.\frac{\partial\,H(\xi,\eta)}{\partial\,\xi}\right|_{\xi=y,\eta=m^2}
  =
  \frac{1}{y}\log\left(m+m^{-1}-y-y^{-1}\right)
  =0$$ from [\[eq:y\]](#eq:y){reference-type="eqref" reference="eq:y"} we have $$\begin{split}
  \frac{d\,H(u)}{du}
  &=
  \left.\frac{\partial\,H(\xi,\eta)}{\partial\xi}\right|_{\xi=y,\eta=m^2}
  \times\frac{d\,y}{du}
  +
  \left.\frac{\partial\,H(\xi,\eta)}{\partial\eta}\right|_{\xi=y,\eta=m^2}
  \times\frac{d\,m^2}{du}
  \\
  &=
  \log\left(\frac{1-ym^2}{m^2-y}\right)+\pi\sqrt{-1}.
\end{split}$$ But since $$\begin{cases}
  ym^2+zm^2=1
  \\
  z^{-1}+m^2y^{-1}=1,
\end{cases}$$ we have $$\frac{d\,\bigl(H(u)-\pi\sqrt{-1}u\bigr)}{du}
  =
  \log\bigl(z(1-z)\bigr)
  =
  \frac{v}{2}.$$ ◻
:::

Next we will calculate $H(0)$.

::: lem
$$H(0)=\sqrt{-1}\operatorname{Vol}\left(S^3\setminus{E}\right)$$
:::

::: proof
*Proof.* Since $m\bigr|_{u=0}=-1$ and $y\bigr|_{u=0}=\exp(-\pi\sqrt{-1}/3)$, we have $$H(0)
  =
   \operatorname{Li}_2\left(e^{-\pi\sqrt{-1}/3}\right)
  -\operatorname{Li}_2\left(e^{ \pi\sqrt{-1}/3}\right)
  =
  4\sqrt{-1}\operatorname{\text{\tencyr\cyracc L}}(\pi/6)$$ from [\[eq:H_on_circle\]](#eq:H_on_circle){reference-type="eqref" reference="eq:H_on_circle"}.

On the other hand from the equality $$\operatorname{\text{\tencyr\cyracc L}}(2\theta)=2\operatorname{\text{\tencyr\cyracc L}}(\theta)-2\operatorname{\text{\tencyr\cyracc L}}(\pi/2-\theta)$$ (see for example [@Milnor:BULAM382 Lemma 1]), we have $4\operatorname{\text{\tencyr\cyracc L}}(\pi/6)=6\operatorname{\text{\tencyr\cyracc L}}(\pi/3)$, which equals the volume of $S^3\setminus{E}$. ◻
:::

::: proof
*Proof of Corollary [\[cor:Vol_CS\]](#cor:Vol_CS){reference-type="ref" reference="cor:Vol_CS"}.* We see that $$\Phi(u)
  =
  4H(u)-4\pi\sqrt{-1}u-4H(0)$$ and so $$f(u)
  =
  H(u)-\pi\sqrt{-1}u-uv/4-\sqrt{-1}\operatorname{Vol}\left(S^3\setminus{E}\right)$$ since $\operatorname{CS}\left(S^3\setminus{E}\right)=0$. Therefore from Theorem [\[thm:Yoshida\]](#thm:Yoshida){reference-type="ref" reference="thm:Yoshida"} $$\begin{split}
  \operatorname{Vol}\left(E_{u}\right)+\sqrt{-1}\operatorname{CS}\left(E_{u}\right)
  &=
  \frac{H(u)}{\sqrt{-1}}
  -\pi{u}
  -\frac{uv}{4\sqrt{-1}}
  -\frac{\pi}{2}\lambda(\gamma).
\end{split}$$ ◻
:::
