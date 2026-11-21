---
doc_id: arxiv-math-0603217v3
doc_title: "A version of the volume conjecture"
section_id: sec-003-4-comments
section_title: "Comments"
section_number: 4
pages: 4-5
source_pdf: 0603217v3.pdf
source_sha256: d7375d4fee00dd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.849
latex_coverage_ratio: 0.976
doc_brief: "A version of the volume conjecture — We propose a version of the volume conjecture that would relate a certain limit of the colored Jones polynomials of a knot to the volume function deﬁned by a"
---
In [@Gukov:COMMP2005 (5.29)], Gukov proposed the following conjecture.

::: conj
[@Gukov:COMMP2005][]{#conj:Gukov label="conj:Gukov"} Let $K$ be a knot in the three-sphere. For $a\in\mathbb{C}\setminus\mathbb{Q}$, define the function $l(a)$ as follows: $$\label{eq:lambda}
  l(a):=
  -\frac{d}{d\,a}
  \left\{
    a\lim_{N\to\infty}
    \frac{\log{J_N\left(K;\exp(2\pi{a}\sqrt{-1}/N)\right)}}{N}
  \right\}.$$ Then the pair $\left(\exp\bigl(l(a)\bigr),-\exp(\pi{a}\sqrt{-1})\right)$ is a zero of the $A$-polynomial of $K$ introduced in [@Cooper/Culler/Gillet/Long/Shalen:INVEM1994].
:::

Using our parameterization $u:=2\pi{a}\sqrt{-1}-2\pi\sqrt{-1}$, we have $l(a)=-v_{K}(u)/2-\pi\sqrt{-1}$. Then Conjecture [\[conj:Gukov\]](#conj:Gukov){reference-type="ref" reference="conj:Gukov"} states that the pair $\left(-\exp\bigl(-v_{K}(u)/2\bigr),\exp(u/2)\right)$ is a zero of the $A$-polynomial.

In the case of the figure-eight knot, we can prove this. For the torus knot $T(a,b)$, either $\left(-\exp\bigl(-v_{K}(u)/2\bigr),\exp(u/2)\right)$ or $\left(-\exp\bigl(v_{K}(u)/2\bigr),\exp(u/2)\right)$ is a zero of the $A$-polynomial. (See, for example, [@XZhang:2004 Example 4.1] for the $A$-polynomials of torus knots.) This would depend on how we choose a meridian/longitude pair.

::: rem
[]{#rem:Garoufalidis2 label="rem:Garoufalidis2"} If $|a|$ is small enough the right hand side of [\[eq:lambda\]](#eq:lambda){reference-type="eqref" reference="eq:lambda"} vanishes [@Garoufalidis/Le:Kauffman]. This corresponds to the $(\mathfrak{l}-1)$-factor of the $A$-polynomial [@Cooper/Culler/Gillet/Long/Shalen:INVEM1994 2.5]. See Remark [\[rem:Garoufalidis1\]](#rem:Garoufalidis1){reference-type="ref" reference="rem:Garoufalidis1"}.
:::

The function $H(K;u)$ defined by [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"} is a kind of potential function introduced in [@Neumann/Zagier:TOPOL85 Theorem 3]. (To be more precise, $\Phi(u)=4H(K;u)-4\pi{u}\sqrt{-1}$, where $\Phi(u)$ is Neumann--Zagier's potential function.) The following observation indicates a relation between $H(K;u)$ and the Alexander polynomial.

::: obs
Let $\Delta(K;t)$ be the Alexander polynomial of a knot $K$. For the figure-eight knot and torus knots, the equations $H(K;u)=0$ and $\Delta\bigl(K;\exp(u)\bigr)=0$ share a root. Note that here we regard $H(K;u)$ as a function defined on the whole complex plane.
:::

::: proof
*Proof.* First note that $\Delta(E;t)=-t^2+3t-1$ and $\Delta\bigl(T(a,b);t\bigr)
=\left(t^{ab}-1\right)(t-1)/\left(t^a-1\right)\left(t^b-1\right)$.

For the figure-eight knot $E$, we have from [@Murakami/Yokota:JREIA] $$H(E;u)
  =
  \operatorname{Li}_2(y^{-1}\exp(-u))-\operatorname{Li}_2(y\exp(-u))+\left(\log(-y)+\pi\sqrt{-1}\right)u,$$ where $y$ is a solution to the equation $y+y^{-1}=2\cosh(u)-1$. Put $u:=\pm\operatorname{arccosh}(3/2)$. Then $y=1$ and so $H(E;u)$ vanishes. Note that we take the branch of $\log$ so that $\log(-1)=-\pi\sqrt{-1}$. It is easy to see that $\exp(\pm\operatorname{arccosh}(3/2))$ are the roots of $\Delta(E;\exp(u))=0$.

For the torus knot $T(a,b)$ the zero of $H\bigl(T(a,b);u\bigr)$ is $2\pi\sqrt{-1}/(ab)-2\pi\sqrt{-1}$. It is also a zero of $\Delta(T(a,b);\exp(u))$. ◻
:::
