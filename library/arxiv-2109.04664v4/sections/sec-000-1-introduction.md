---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.83
latex_coverage_ratio: 0.901
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — We study the asymptotic behavior of the N-dimensional colored Jones polynomial"
---
[]{#sec:introduction label="sec:introduction"} Let $N\ge2$ be an integer.

In [@Kashaev:MODPLA95], R. Kashaev introduced a link invariant $\langle K\rangle_{N}$ for a knot $K$ in the three-sphere $S^3$ by using the so-called quantum dilogarithm. In [@Kashaev:LETMP97], he studied its asymptotic behavior when $N\to\infty$ for several hyperbolic knots and conjectured that it would determine its hyperbolic volume for any *hyperbolic* knot, where a knot is called hyperbolic if its complement possesses a complete hyperbolic structure with finite volume. More precisely he conjectured

::: conj
Let $H$ be a *hyperbolic* knot in $S^3$. Then the following equality holds. $$\label{eq:Kashaev}
  \lim_{N\to\infty}
  \frac{\log\left|\langle H\rangle_{N}\right|}{N}
  =
  \frac{\operatorname{V}\left(S^3\setminus{H}\right)}{2\pi},$$ where $\operatorname{V}\left(S^3\setminus{H}\right)$ is the hyperbolic volume.
:::

Let $J_{N}(K;q)$ be the colored Jones polynomial associated with the $N$-dimensional irreducible representation of the Lie algebra $\mathfrak{sl}(2;\mathbb{C})$ [@Kirby/Melvin:INVEM1991; @Reshetikhin/Turaev:INVEM1991]. We normalize it so that $J_{N}(U;q)=1$ for the unknot $U$, and that $J_{2}(K;q)$ is the ordinary Jones polynomial [@Jones:BULAM31985]. In [@Murakami/Murakami:ACTAM12001], J. Murakami and the first author proved that Kashaev's invariant $\langle K\rangle_{N}$ coincides with the $N$-dimensional colored Jones polynomial $J_{N}(K;q)$ evaluated at $q=e^{2\pi\sqrt{-1}/N}$. They also generalized Kashaev's conjecture for general knots:

::: conj
For *any* knot $K\subset{S^3}$, we have $$\label{eq:VC}
  \lim_{N\to\infty}
  \frac{\log\left|J_{N}\left(K;e^{2\pi\sqrt{-1}/N}\right)\right|}{N}
  =
  \frac{\operatorname{Vol}\left(S^3\setminus{K}\right)}{2\pi}.$$ Here, $\operatorname{Vol}(S^3\setminus{K})$ is the simplicial volume, also known as the Gromov norm [@Gromov:INSHE82] (see also [@Soma:INVEM1981]), which is normalized so that $\operatorname{Vol}\left(S^3\setminus{H}\right)=\operatorname{V}\left(S^3\setminus{H}\right)$ if $H$ is hyperbolic.
:::

Kashaev's conjecture was complexified by T. Takata, J. Murakami, M. Okamoto, Y. Yokota and the first author in [@Murakami/Murakami/Okamoto/Takata/Yokota:EXPMA02] by dropping the absolute value symbol (and replacing $\langle H\rangle_{N}$ with $J_{N}\left(H;e^{2\pi\sqrt{-1}/N}\right)$) in [\[eq:Kashaev\]](#eq:Kashaev){reference-type="eqref" reference="eq:Kashaev"}.

::: conj
For a hyperbolic knot $H$, we have $$\label{eq:CVC}
  \lim_{N\to\infty}
  \frac{\log J_{N}\left(H;e^{2\pi\sqrt{-1}/N}\right)}{N}
  =
  \frac{\operatorname{V}\left(S^3\setminus{H}\right)+\sqrt{-1}\operatorname{CS}(S^3\setminus{H})}{2\pi},$$ where $\operatorname{CS}$ is the $SO(3)$ Chern--Simons invariant of $H$ associated with the Levi-Civita connection [@Meyerhoff:LMSLN112].
:::

More detailed asymptotic formulas are known for several knots [@Andersen/Hansen:JKNOT2006; @Ohtsuki:QT2016; @Ohtsuki/Yokota:MATPC2018]: $$\langle H\rangle_{N}
  \underset{N\to\infty}{\sim}
  \omega(H)N^{3/2}\exp\left(\frac{N}{2\pi}\operatorname{CV}(H)\right),$$ where $\operatorname{CV}(H):=\operatorname{Vol}\left(S^3\setminus{H}\right)+\sqrt{-1}\operatorname{CS}(S^3\setminus{H})$ is the complex volume and $2\sqrt{-1}\omega(H)^2$ is the adjoint (cohomological) Reidemeister torsion twisted by the holonomy representation of $\pi_1(S^3\setminus{H})$ to $\rm{SL}(2;\mathbb{C})$ [@Ohtsuki/Takata:GEOTO2015].

It was also generalized by replacing $2\pi\sqrt{-1}$ with another complex number $\xi$ [@Dimofte/Gukov/Lenells/Zagier:CNTP2010; @Murakami:JTOP2013].

::: conj
Let $\xi\ne2\pi\sqrt{-1}$ be a complex number close to $2\pi\sqrt{-1}$, and $H$ a hyperbolic knot. Then we have $$\label{eq:GVC}
  J_{N}\left(H;e^{\xi/N}\right)
  \underset{N\to\infty}{\sim}
  \frac{C}{\sinh(\xi)}\times\tau(\xi)^{1/2}\left(\frac{N}{\xi}\right)^d
  \exp\left(\frac{N}{\xi}S(\xi)\right)$$ with $d$ a constant. Here $S(\xi)$ and $\tau(\xi)$ are related to the $\rm{SL}(2;\mathbb{C})$ Chern--Simons invariant and the adjoint Reidemeister torsion, respectively, both associated with a certain representation of $\pi_1(S^3\setminus{H})$ to $\rm{SL}(2;\mathbb{C})$.
:::

In this paper, we are mainly interested in the figure-eight knot. We first list known results for the asymptotic behavior of the colored Jones polynomial of the figure-eight knot $E$.

We define a function $\varphi$ as $$\varphi(\xi)
  :=
  \operatorname{arccosh}\left(\cosh(\xi)-\frac{1}{2}\right)$$ for a complex number $\xi$, where we use the following branch of $\operatorname{arccosh}$: $$\operatorname{arccosh}(x)
  :=
  \log\left(x-\sqrt{-1}\sqrt{1-x^2}\right),$$ and we choose the branch cut of $\log$ as $(-\infty,0)$. Note that $\varphi(0)=-\pi\sqrt{-1}/3$ and $\varphi(\kappa)=0$, where $\kappa:=\log\left(\frac{3+\sqrt{5}}{2}\right)$. We also define $$\begin{aligned}
  S(\xi)
  &:=
  \operatorname{Li}_2(e^{-\xi-\varphi(\xi)})-\operatorname{Li}_2(e^{-\xi+\varphi(\xi)})+\xi\varphi(\xi),
  \\
  \tilde{S}(\xi)
  &:=
  \operatorname{Li}_2(e^{-\xi-\varphi(\xi)})-\operatorname{Li}_2(e^{-\xi+\varphi(\xi)})
  +(\xi-2\pi\sqrt{-1})(\varphi(\xi)+2\pi\sqrt{-1}),
  \\
  T(\xi)
  &:=
  \frac{2}{\sqrt{(2\cosh(\xi)+1)(2\cosh(\xi)-3)}},
\end{aligned}$$ where $$\operatorname{Li}_2(z):=-\int_{0}^{z}\frac{\log(1-x)}{x}\,dx$$ is the dilogarithm function, where we choose the branch cut as $(1,\infty)$. Note that $S(0)=\tilde{S}(2\pi\sqrt{-1})=\operatorname{Li}_2(e^{\pi\sqrt{-1}/3})-\operatorname{Li}_2(e^{-\pi\sqrt{-1}/3})=\sqrt{-1}\times 2.02988...$.

The quantities $S(\xi)$, $\tilde{S}(\xi)$, and $T(\xi)$ are related to the Chern--Simons invariant and the adjoint Reidemeister torsion associated with a certain representation of $\pi_1\left(S^3\setminus{E}\right)$ to $\rm{SL}(2;\mathbb{C})$. See Section [\[sec:CST\]](#sec:CST){reference-type="ref" reference="sec:CST"} for details.

1.  $\xi=2\pi\sqrt{-1}$:

    This corresponds to the case of the Volume Conjecture. Kashaev sketched a proof of [\[eq:VC\]](#eq:VC){reference-type="eqref" reference="eq:VC"} in [@Kashaev:LETMP97], and then T. Ekholm gave a detailed proof of [\[eq:VC\]](#eq:VC){reference-type="eqref" reference="eq:VC"}. See for example [@Murakami/Yokota:2018 Section 3.2] for Ekholm's proof. Later, J.E. Andersen and S.K. Hansen [@Andersen/Hansen:JKNOT2006 Theorem 1] followed Kashaev's method to prove the following asymptotic formula. $$J_{N}\left(E;e^{2\pi\sqrt{-1}/N}\right)
      \underset{N\to\infty}{\sim}
      2\pi^{3/2}\left(\frac{N}{2\pi\sqrt{-1}}\right)^{3/2}T(2\pi\sqrt{-1})^{1/2}
      \exp\left(\frac{N}{2\pi\sqrt{-1}}\tilde{S}(2\pi\sqrt{-1})\right).$$ Since $S(0)=\sqrt{-1}\operatorname{Vol}\left(S^3\setminus{E}\right)$, this refines the Volume Conjecture for the figure-eight knot.

2.  $\xi$ is close to $2\pi\sqrt{-1}$ and not purely imaginary:

    Y. Yokota and the first author proved the following formula [@Murakami/Yokota:JREIA2007]. $$\label{eq:Yokota}
      \lim_{N\to\infty}
      \frac{\log J_{N}(E;e^{\xi/N})}{N}
      =
      \frac{\tilde{S}(\xi)}{\xi}.$$

3.  $\xi$ is purely imaginary with $5\pi/3<|\xi|<7\pi/3$, and $2\pi/|\xi|$ is irrational with finite irrationality measure:

    In [@Murakami:KYUMJ2004] (see [@Murakami:KYUMJ2016] for correction), the first author proved the following formula. $$\lim_{N\to\infty}
      \frac{\log J_{N}(E;e^{\xi/N})}{N}
      =
      \frac{\tilde{S}(\xi)}{\xi}.$$ See also [@Murakami:Novosibirsk 6.2.2].

4.  $\xi$ is of the form $2\pi\sqrt{-1}+u$ for a real number $u$ with $0<|u|<\kappa$:

    The first author proved the following asymptotic formula [@Murakami:JTOP2013 Theorem 1.4]: $$\label{eq:J_top}
      J_{N}\left(E;e^{\xi/N}\right)
      \underset{N\to\infty}{\sim}
      \frac{\sqrt{-\pi}}{2\sinh(u/2)}T(\xi)^{1/2}\left(\frac{N}{\xi}\right)^{1/2}
      \exp\left(\frac{N}{\xi}\tilde{S}(\xi)\right).$$ Note that this refines [\[eq:Yokota\]](#eq:Yokota){reference-type="eqref" reference="eq:Yokota"} when $\xi$ is as above.

5.  $\xi$ satisfies the inequalities $|2\cosh{\xi}-2|<1$ and $|\operatorname{Im}{\xi}|<\pi/3$:

    In this case, $J_{N}\left(E;e^{\xi/N}\right)$ converges. In fact, we have $$\lim_{N\to\infty}
      J_{N}\left(E;e^{\xi/N}\right)
      =
      \frac{1}{\Delta(E;e^{\xi})},$$ where $\Delta(E;t)=-t+3-t^{-1}$ is the normalized Alexander polynomial of the figure-eight knot $E$ [@Murakami:JPJGT2007 Theorem 1.1].

    See [@Garoufalidis/Le:GEOTO2011] for general knots.

6.  $\xi=\pm\kappa$:

    In this case, $J_{N}\left(E;e^{\kappa/N}\right)$ grows polynomially. More precisely, we have $$J_{N}\left(E;e^{\kappa/N}\right)
      \underset{N\to\infty}{\sim}
      \frac{\Gamma(1/3)}{(3\kappa)^{2/3}}N^{2/3},$$ where $\Gamma(z)$ is the Gamma function [@Hikami/Murakami:COMCM2008 Theorem 1.1].

7.  $\xi$ is real and $|\xi|>\kappa$:

    The first author proved the following formula [@Murakami:KYUMJ2004 Theorem 8.1] (see also [@Murakami:ACTMV2008 Theorem 3.2] and [@Murakami:Novosibirsk Lemma 6.7]). $$\label{eq:Kyungpook}
      \lim_{N\to\infty}
      \frac{\log J_{N}(E;e^{\xi/N})}{N}
      =
      \frac{S(\xi)}{|\xi|}.$$

The purpose of this paper is to refine [\[eq:Kyungpook\]](#eq:Kyungpook){reference-type="eqref" reference="eq:Kyungpook"}. We will show

::: thm
[]{#thm:main label="thm:main"} If $\xi$ is real and $|\xi|>\kappa$, then we have $$J_{N}\left(E;e^{\xi/N}\right)
  \underset{N\to\infty}{\sim}
  \frac{\sqrt{\pi}}{2\sinh(|\xi|/2)}T(\xi)^{1/2}\left(\frac{N}{|\xi|}\right)^{1/2}
  \exp\left(\frac{N}{|\xi|}S(\xi)\right).$$
:::

Moreover, we can show that $T(\xi)$ is the Reidemeister torsion twisted by the adjoint action of a representation $\rho$ of $\pi_1(S^3\setminus{E})$ to $\rm{SL}(2;\mathbb{C})$ determined by $\xi$, and that $S(\xi)-\xi\eta/2$ is the Chern--Simons invariant of $\rho$ associated with the meridian and the preferred longitude of $E\subset S^{3}$. See Section [\[sec:CST\]](#sec:CST){reference-type="ref" reference="sec:CST"} for details.

::: rem
Suppose that $u:=\xi-2\pi\sqrt{-1}$ is a small complex number or a real number with $|u|<\kappa$. In this case $\operatorname{Im}\varphi(u)<0$. By using a well-known formula $$\operatorname{Li}_2(z)+\operatorname{Li}_2(z^{-1})+\frac{\pi^2}{6}+\frac{1}{2}\left(\log(-z)\right)^2=0.$$ we have $$\begin{split}
  &\tilde{S}(\xi)
  \\
  =&
  -\operatorname{Li}_2(e^{\xi+\varphi(\xi)})+\operatorname{Li}_2(e^{\xi-\varphi(\xi)})
  -\frac{1}{2}\left(\log(-e^{\xi+\varphi(\xi)})\right)^2
  +\frac{1}{2}\left(\log(-e^{\xi-\varphi(\xi)})\right)^2
  \\
  &+u(\varphi(\xi)+2\pi\sqrt{-1})
  \\
  \\
  =&
  -\operatorname{Li}_2(e^{u+\varphi(u)})+\operatorname{Li}_2(e^{u-\varphi(u)})
  -\frac{1}{2}\left(u+\varphi(u)+\pi\sqrt{-1}\right)^2
  \\
  &+\frac{1}{2}\left(u-\varphi(u)-\pi\sqrt{-1}\right)^2
   +(2\pi\sqrt{-1}+u)\varphi(u)
  \\
  =&
  -\operatorname{Li}_2(e^{u+\varphi(u)})+\operatorname{Li}_2(e^{u-\varphi(u)})-u\varphi(u).
\end{split}$$ In the second equality, we use the fact that $\operatorname{Im}\varphi(u)<0$. Therefore [\[eq:J_top\]](#eq:J_top){reference-type="eqref" reference="eq:J_top"} coincides with the formula appearing in [@Murakami:JTOP2013 Theorem 1.4].
:::

::: rem
In [@Murakami:JTOP2013], the first author followed [@Andersen/Hansen:JKNOT2006] to obtain the asymptotic formula, but in the current paper we follow [@Ohtsuki:QT2016].
:::
