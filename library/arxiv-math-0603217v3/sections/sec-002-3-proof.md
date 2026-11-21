---
doc_id: arxiv-math-0603217v3
doc_title: "A version of the volume conjecture"
section_id: sec-002-3-proof
section_title: "Proof"
section_number: 3
pages: 3-4
source_pdf: 0603217v3.pdf
source_sha256: d7375d4fee00dd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 0.984
doc_brief: "A version of the volume conjecture — We propose a version of the volume conjecture that would relate a certain limit of the colored Jones polynomials of a knot to the volume function deﬁned by a"
---
In this section we prove Conjecture [\[conj:parameterization\]](#conj:parameterization){reference-type="ref" reference="conj:parameterization"} for torus knots. (To be honest, [\[eq:volume\]](#eq:volume){reference-type="eqref" reference="eq:volume"} is proved only up to a constant, that is, we prove [\[eq:Schlafli\]](#eq:Schlafli){reference-type="eqref" reference="eq:Schlafli"} instead.)

Let $T(a,b)$ be the torus knot of type $(a,b)$, where $a$ and $b$ are coprime integers with $a>1$ and $b>1$. Then the author proved in [@Murakami:INTJM62004 Theorem 1.1] the following theorem.

::: thm
Suppose that $|r|>1/(ab)$, $\operatorname{Re}{r}>0$ and $\operatorname{Im}{r}>0$, then $$\lim_{N\to\infty}
  \frac{\log{J_N\left(T(a,b);\exp(2\pi r\sqrt{-1}/N)\right)}}{N}
  =
  \left(1-\frac{1}{2abr}-\frac{abr}{2}\right)\pi\sqrt{-1}.$$
:::

Therefore the functions $H\bigl(T(p,q);u\bigr)$ and $v_{T(a,b)}(u)$ in Conjecture [\[conj:parameterization\]](#conj:parameterization){reference-type="ref" reference="conj:parameterization"} are defined as follows: $$\begin{aligned}
  H\bigl(T(p,q);u\bigr)
  &=
  (u+2\pi\sqrt{-1})
  \left(
    1
    -\frac{1}{2ab\left(1+\frac{u}{2\pi\sqrt{-1}}\right)}
    -\frac{ab\left(1+\frac{u}{2\pi\sqrt{-1}}\right)}{2}
  \right)
  \pi\sqrt{-1}
  \\
  &=
  \frac{-(ab(u+2\pi\sqrt{-1})-2\pi\sqrt{-1})^2}{4ab}
  \\
  \intertext{and}
  v_{T(a,b)}(u)
  &=
  2\frac{d\;H\bigl(T(a,b);u\bigr)}{d\;u}-2\pi\sqrt{-1}
  =
  -ab(u+2\pi\sqrt{-1})
\end{aligned}$$ for $u$ with $|u+2\pi\sqrt{-1}|>2\pi/(ab)$, $\operatorname{Re}(u)<0$ and $\operatorname{Im}(u)>-2\pi$.

So the volume function $V\bigl(T(a,b);u\bigr)$ is $$\begin{split}
  V\bigl(T(a,b);u\bigr)
  &=
  \operatorname{Im}{\bigl(H(T(a,b);u\bigr)}-\pi\operatorname{Re}(u)-\frac{1}{2}\operatorname{Re}(u)\operatorname{Im}(v_{T(a,b)}(u))
  \\
  &=
  -\frac{1}{4}ab\operatorname{Im}(u^2)
  -ab\pi\operatorname{Re}(u)
  +\pi\operatorname{Re}(u)
  \\
  &\phantom{=}
  -\pi\operatorname{Re}(u)
  -\frac{1}{2}\operatorname{Re}(u)(-ab\operatorname{Im}(u)-2ab\pi)
  \\
  &=
  0.
\end{split}$$

On the other hand the right hand side of [\[eq:Schlafli\]](#eq:Schlafli){reference-type="eqref" reference="eq:Schlafli"} equals $$-\frac{1}{2}
  \left(
    \operatorname{Re}\bigl(u(t)\bigr)
    (-ab)
    \frac{d\,\operatorname{Im}\bigl(u(t)\bigr)}{d\,t}
   +ab\operatorname{Re}\bigl(u(t)\bigr)
    \frac{d\,\operatorname{Im}\bigl(u(t)\bigr)}{d\,t}
  \right)
  =
  0,$$ which proves [\[eq:Schlafli\]](#eq:Schlafli){reference-type="eqref" reference="eq:Schlafli"}.

This confirms Conjecture [\[conj:parameterization\]](#conj:parameterization){reference-type="ref" reference="conj:parameterization"} for the torus knot $T(a,b)$.

::: rem
The volume function for a torus knot would be zero. See [@Garoufalidis/Le:Kauffman Appendix B].
:::

::: rem
Note that the pair $\left(u,v_{T(a,b)}(u)\right)$ satisfies the equality: $$(-1)\times{u}+\left(\frac{-1}{ab}\right)\times{v_{T(a,b)}(u)}=2\pi\sqrt{-1}.$$ So the corresponding geometric object would be the generalized Dehn surgery along the torus knot $T(a,b)$ with invariant $\bigl(1,1/(ab)\bigr)$, or the $ab$-Dehn surgery with cone-angle $2ab\pi$ [@Thurston:GT3M Chapter 4, § 4.5] (see also Remark [\[rem:Dehn\]](#rem:Dehn){reference-type="ref" reference="rem:Dehn"}). It would be interesting that the $ab$-Dehn surgery along the torus knot $T(a,b)$ is reducible [@Moser:PACJM1971].
:::
