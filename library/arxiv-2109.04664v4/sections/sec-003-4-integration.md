---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER"
section_id: sec-003-4-integration
section_title: "Integration"
section_number: 4
pages: 10-14
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.945
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — We study the asymptotic behavior of the N-dimensional colored Jones polynomial"
---
[]{#sec:integration label="sec:integration"} In this section, we use the Poisson summation formula (see [@Ohtsuki:QT2016 Proposition 4.2]) to change the summation in [\[eq:J_summation\]](#eq:J_summation){reference-type="eqref" reference="eq:J_summation"} into an integration. Then by using the saddle point method (see also [@Ohtsuki:QT2016 Proposition 3.2]) to prove Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

Define $$\psi(z)
  :=
  F(z+\varphi(\xi)/\xi)-F(\varphi(\xi)/\xi)$$ in the region $$\label{eq:region_psi}
  \left\{
    z\in\mathbb{C}
    \Bigm|
    -\frac{\varphi(\xi)}{\xi}\le\operatorname{Re}{z}<1-\frac{\varphi(\xi)}{\xi},
    -1-\frac{\varphi(\xi)}{\xi}<\frac{\operatorname{Im}{z}}{\tan\theta}+\operatorname{Re}{z}<1-\frac{\varphi(\xi)}{\xi}
  \right\}.$$ Then since $\psi(0)=0$, $\psi'(0)=0$, and $\psi''(0)=-\xi\sqrt{(2\cosh(\xi)-1)^2-4}$ from [\[eq:F\'\_phi\]](#eq:F'_phi){reference-type="eqref" reference="eq:F'_phi"} and [\[eq:F\'\'\_phi\]](#eq:F''_phi){reference-type="eqref" reference="eq:F''_phi"}, $\psi(z)$ is of the form $$\psi(z)
  =
  \frac{-\xi}{2}\sqrt{(2\cosh(\xi)-1)^2-4}\times z^2+a_3z^3+a_4z^4+\cdots$$ in [\[eq:region_psi\]](#eq:region_psi){reference-type="eqref" reference="eq:region_psi"}.

::: lem
[]{#lem:psi_negative label="lem:psi_negative"} If $x\ne0$ is real and satisfies $-\varphi(\xi)/\xi\le x<1-\varphi(\xi)/\xi$, then $\psi(x)<0$.
:::

::: proof
*Proof.* Since $e^{\xi}+e^{-\xi}-e^{\varphi(\xi)}-e^{-\varphi(\xi)}=1$, we have $$\label{eq:psi'}
\begin{split}
  \psi'(x)
  &=
  \log(e^{\xi}+e^{-\xi}-e^{\xi x+\varphi(\xi)}-e^{-\xi x-\varphi(\xi)})
  \\
  &=
  \log(e^{\varphi(\xi)}+e^{-\varphi(\xi)}-e^{\xi x+\varphi(\xi)}-e^{-\xi x-\varphi(\xi)}+1)
  \\
  &=
  \log
  \left(
    e^{-\varphi(\xi)}(1-e^{\xi x})(e^{2\varphi(\xi)}-e^{-\xi x})+1
  \right)
\end{split}$$ from [\[eq:F\'\]](#eq:F'){reference-type="eqref" reference="eq:F'"}. Therefore we see that $\psi'(x)=0$ if $x=0$ or $-2\varphi(\xi)/\xi$, $\psi'(x)>0$ if $-2\varphi(\xi)/\xi<x<0$, and $\psi'(x)<0$ otherwise.

Therefore for $-\varphi(\xi)/\xi<x<0$, $\psi(x)$ is monotonically increasing and for $0<x<1-\varphi(\xi)/\xi$ it is monotonically decreasing. So $\psi(x)$ takes its unique maximum $0$ at $x=0$, which shows that $\psi(x)<0$ when $x\ne0$. ◻
:::

Now we use the following proposition.

::: prop
[]{#prop:Poisson label="prop:Poisson"} Let $b_{-}$ and $b_{+}$ be real numbers with $b_{-}<0<b_{+}$. Put $$\begin{aligned}
  \Lambda
  &:=
  \left\{
    \frac{k}{N}\Bigm| k\in\mathbb{Z}, b_{-}\le\frac{k}{N}\le b_{+}
  \right\},
  \\
  C
  &:=
  \{t\in\mathbb{R}\mid b_{-}\le t\le b_{+}\},
  \\
  D
  &:=
  \{z\in\mathbb{C}\mid\operatorname{Re}{\psi(z)}<0\}.
\end{aligned}$$ Assume that $\psi(z)$ is a holomorphic function of the form $$\label{eq:f}
  \psi(z)
  =
  az^2+a_3z^3+a_4z^4+\cdots$$ with $\operatorname{Re}(a)<0$, defined in a neighborhood $P$ of $0\in\mathbb{C}$ that includes the $\delta_0$-neighborhood $N_{\delta_0}$ of $0$ for $\delta_0>0$. We choose $P$ so that the region $D\cap P$ has two connected components. We also assume the following:

1.  $b_{-}$ and $b_{+}$ are in different components of $D\cap P$ and moreover $\operatorname{Re}{\psi(b_{\pm})}<-\varepsilon_0$ for some $\varepsilon_0>0$,

2.  Both $b_{-}$ and $b_{+}$ are in a connected component of $$\label{eq:R+}
      \{x+y\sqrt{-1}\mid x\in[b_{-},b_{+}],y\in[0,\delta_0],\operatorname{Re}{\psi(x+y\sqrt{-1})}<2\pi y\}$$

3.  Both $b_{-}$ and $b_{+}$ are in a connected component of $$\label{eq:R-}
      \{x-y\sqrt{-1}\mid x\in[b_{-},b_{+}],y\in[0,\delta_0],\operatorname{Re}{\psi(x-y\sqrt{-1})}<2\pi y\}$$

Then there exists $\varepsilon>0$, depending on $a$ and $\varepsilon_0$, such that $$\frac{1}{N}
  \sum_{z\in\Lambda}
  e^{N\psi(z)}
  =
  \int_{C}e^{N\psi(z)}\,dz
  +
  O(e^{-N\varepsilon}).$$
:::

We will show that $\psi(z)$ satisfies the assumptions of Proposition [\[prop:Poisson\]](#prop:Poisson){reference-type="ref" reference="prop:Poisson"}.

Put $b_{-}:=-\varphi(\xi)/(2\xi)$, $b_{+}:=(1-\varphi(\xi)/\xi)/2$, $\delta_0:=\frac{1}{2}(1-\varphi(\xi)/\xi)\sin\theta$. Define the following regions: $$\begin{aligned}
  P
  &:=
  \left\{
    z\in\mathbb{C}
    \mid
    -\frac{\varphi(\xi)}{\xi}<\operatorname{Re}{z}<1-\frac{\varphi(\xi)}{\xi},
    -1-\frac{\varphi(\xi)}{\xi}<\frac{\operatorname{Im}{z}}{\tan\theta}+\operatorname{Re}{z}<1-\frac{\varphi(\xi)}{\xi}
  \right\},
  \\
  D_{-}
  &:=
  \{z\in\mathbb{C}\mid\operatorname{Re}{\psi(z)}<0,\operatorname{Re}{z}<0\},
  \\
  D_{+}
  &:=
  \{z\in\mathbb{C}\mid\operatorname{Re}{\psi(z)}<0,\operatorname{Re}{z}>0\}.
\end{aligned}$$ Note that $P$ is just the region [\[eq:region_psi\]](#eq:region_psi){reference-type="eqref" reference="eq:region_psi"} and so $\psi(z)$ is holomorphic in $P$. See Figure [1](#fig:P){reference-type="ref" reference="fig:P"}.

<figure id="fig:P">
<embed src="picture.eps" />
<p>(see below). <span id="fig:P" label="fig:P"></span></p>
<figcaption>The parallelogram is the boundary of <span class="math inline"><em>P</em></span>, the circle is the boundary of <span class="math inline"><em>N</em><sub><em>δ</em><sub>0</sub></sub></span>, the red region is <span class="math inline"><em>D</em><sub>−</sub></span>, and the green region is <span class="math inline"><em>D</em><sub>+</sub></span>. The cyan rectangle indicates the boundary of <span class="math inline"><em>R</em><sub>+</sub> ∪ <em>R</em><sub>−</sub></span></figcaption>
</figure>

Then, we show the following lemma, from which the assumptions of Proposition [\[prop:Poisson\]](#prop:Poisson){reference-type="ref" reference="prop:Poisson"} hold.

::: lem
[]{#lem:Poisson_psi label="lem:Poisson_psi"} We assume that $\sin{\theta}<\frac{\varphi(\xi)}{\xi-\varphi(\xi)}$ and that $\tan\theta<\frac{\pi}{2\xi}$. Then, the function $\psi(z)$ satisfies the following:

1.  $\psi(z)$ is a holomorphic function of the form [\[eq:f\]](#eq:f){reference-type="eqref" reference="eq:f"} defined in the $\delta_0$-neighborhood $N_{\delta_0}$ of $0\in\mathbb{C}$.

2.  Both $D_{+}\cap P$ and $D_{-}\cap P$ are connected, and $b_{\pm}\in D_{\pm}\cap P$. Moreover, $\operatorname{Re}\psi(b_{\pm})<-\varepsilon_0$ for some $\varepsilon_0>0$.

3.  Condition (2) in Proposition [\[prop:Poisson\]](#prop:Poisson){reference-type="ref" reference="prop:Poisson"} is satisfied.

4.  Condition (3) in Proposition [\[prop:Poisson\]](#prop:Poisson){reference-type="ref" reference="prop:Poisson"} is satisfied.
:::

::: proof
*Proof.*

1.  The distances to the upper side, the lower side, the left side, and the right side of $P$ from the origin $O$ is $(1-\varphi(\xi)/\xi)\sin\theta$, $(1+\varphi(\xi)/\xi)\sin\theta$, $\varphi(\xi)/\xi$ and $1-\varphi(\xi)/\xi$, respectively. Since $(1-\varphi(\xi)/\xi)\sin\theta<\varphi(\xi)/\xi$ from the assumption $\sin\theta<\frac{\varphi}{\xi-\varphi(\xi)}$, $\delta_0$ is less than these distances. So $N_{\delta_0}$ is contained in the parallelogram $P$. Moreover since $\psi''(0)=F''(\varphi(\xi)/\xi)=-\xi\sqrt{(2\cosh(\xi)-1)^2-4}<0$, $\psi(z)$ is of the form [\[eq:f\]](#eq:f){reference-type="eqref" reference="eq:f"} with $a:=-\frac{\xi}{2}\sqrt{(2\cosh(\xi)-1)^2-4}$.

2.  We first show that $b_{\pm}\in D_{\pm}\cap P$. It is clear that $b_{-}<0$, $b_{+}>0$, and $b_{\pm}\in P$. The inequality $\operatorname{Re}\psi(b_{\pm})<0$ follows from Lemma [\[lem:psi_negative\]](#lem:psi_negative){reference-type="ref" reference="lem:psi_negative"}. So, we can choose $\varepsilon_0>0$ so that $\operatorname{Re}\psi(b_{\pm})<-\varepsilon_0$.

    Next, we will show that for each $x\ne0$ with $-\varphi(\xi)/\xi<x<1-\varphi(\xi)/\xi$, the set $\{y\in\mathbb{R}\mid\operatorname{Re}\psi(x+y\sqrt{-1})<0\}\cap P$ is an open interval containing $0$. Then, we can see that $D_{\pm}\cap P$ is connected.

    If we put $$g(x,y)
      :=
      e^{\xi}+e^{-\xi}-e^{\xi(x+y\sqrt{-1})+\varphi(\xi)}-e^{-\xi(x+y\sqrt{-1})-\varphi(\xi)},$$ then we have $$\label{eq:arg}
      \frac{d}{d\,y}\operatorname{Re}\psi(x+y\sqrt{-1})
      =
      -\arg g(x,y)$$ from [\[eq:psi\'\]](#eq:psi'){reference-type="eqref" reference="eq:psi'"}. Now we have $$\begin{aligned}
      \operatorname{Re}g(x,y)
      &=
      2\cosh{\xi}
      -
      2\cosh\left(\xi\left(x+\frac{\varphi(\xi)}{\xi}\right)\right)\cos(\xi y),
      \intertext{and}
      \operatorname{Im}g(x,y)
      &=
      -\sinh\left(\xi\left(x+\frac{\varphi(\xi)}{\xi}\right)\right)\sin(\xi y).
      \notag
    \end{aligned}$$

    We can see that $\operatorname{Re}g(x,y)$ is positive since $0<x+\varphi(\xi)/\xi<1$. We will show that $\operatorname{Im}g(x,y)<0$ ($\operatorname{Im}g(x,y)>0$) if $y>0$ ($y<0$, respectively). If $x+y\sqrt{-1}\in P$, then $-2\tan\theta<y<\tan\theta$ (see Figure [1](#fig:P){reference-type="ref" reference="fig:P"}). Together with the assumption $\tan\theta<\frac{\pi}{2\xi}$, we conlude that $|y|\le2\tan\theta<\pi/\xi$, and so $|\xi y|<\pi$. This implies that $\sin(\xi y)>0$ ($\sin(\xi y)<0$, respectively) if $y>0$ ($y<0$, respectively). Since $x+\varphi(\xi)/\xi>0$, we see that $\operatorname{Im}g(x,y)<0$ ($\operatorname{Im}g(x,y)>0$) if $y>0$ ($y<0$, respectively).

    Therefore $\arg{g(x,y)}$ is positive (negative, respectively) when $y<0$ ($y>0$, respectively). It follows that if $y>0$ ($y<0$, respectively), $\operatorname{Re}\psi(x+y\sqrt{-1})$ is monotonically increasing (decreasing, respectively) with respect to $y$. Since $\operatorname{Re}\psi(x)<0$ from Lemma [\[lem:psi_negative\]](#lem:psi_negative){reference-type="ref" reference="lem:psi_negative"}, we see that $\{y\in\mathbb{R}\mid\operatorname{Re}\psi(x+y\sqrt{-1})<0\}\cap P$ is an open interval containing $0$.

    Therefore, we conclude that $D_{\pm}\cap P$ is connected.

3.  We will show that the region $R_{+}:=[b_{-},b_{+}]\times[0,\delta_0]\setminus\{O\}$ is contained in the region $\{x+y\sqrt{-1}\in\mathbb{C}\mid\operatorname{Re}\psi(x+y\sqrt{-1})<2\pi y\}$, which means that the region [\[eq:R+\]](#eq:R+){reference-type="eqref" reference="eq:R+"} equals $R_{+}$. Then we can find a path connecting $b_{-}$ and $b_{+}$ in $R_{+}$, proving Condition (2).

    In fact, we can show if $b_{-}\le x\le b_{+}$ and $0\le y\le\delta_0$ ($(x,y)\ne(0,0)$), then $\operatorname{Re}\psi(x+y\sqrt{-1})-2\pi y<0$ as follows.

    When $y>0$, then $\operatorname{Im}g(x,y)<0$ from the argument in (ii), and so $g(x,y)$ is in the fourth quadrant in the complex plane because $\operatorname{Re}g(x,y)>0$. Therefore we have $0>\arg g(x,y)>-\pi/2$. This shows that $\frac{d}{d\,y}\bigl(\operatorname{Re}\psi(x+y\sqrt{-1})-2\pi y\bigr)<0$ when $y>0$ from [\[eq:arg\]](#eq:arg){reference-type="eqref" reference="eq:arg"}, and so we conclude that $\operatorname{Re}\psi(x+y\sqrt{-1})-2\pi y<0$ since $\operatorname{Re}\psi(x)\le0$ from Lemma [\[lem:psi_negative\]](#lem:psi_negative){reference-type="ref" reference="lem:psi_negative"}.

4.  We will show that the region $R_{-}:=[b_{-},b_{+}]\times[-\delta_0,0]\setminus\{O\}$ is in the region $\{x+y\sqrt{-1}\in\mathbb{C}\mid\operatorname{Re}\psi(x+y\sqrt{-1})<-2\pi y\}$, which means that the region [\[eq:R-\]](#eq:R-){reference-type="eqref" reference="eq:R-"} equals $R_{-}\cup\{O\}$. Then we can find a path connecting $b_{-}$ and $b_{+}$ in $R_{-}$, proving Condition (3).

    We will show if $b_{-}\le x\le b_{+}$ and $-\delta_0\le y\le0$ ($(x,y)\ne(0,0)$), then $\operatorname{Re}\psi(x+y\sqrt{-1})+2\pi y<0$.

    When $y<0$, then $\operatorname{Im}g(x,y)>0$ from the argument in (ii), and so $g(x,y)$ is in the first quadrant because $\operatorname{Re}g(x,y)>0$. Therefore we have $0<\arg g(x,y)<\pi/2$. This shows that $\frac{d}{d\,y}\bigl(\operatorname{Re}\psi(x+y\sqrt{-1})+2\pi y\bigr)>0$ when $y<0$, and so we conclude that $\operatorname{Re}\psi(x+y\sqrt{-1})+2\pi y<0$ since $\operatorname{Re}\psi(x)\le0$ from Lemma [\[lem:psi_negative\]](#lem:psi_negative){reference-type="ref" reference="lem:psi_negative"}.

 ◻
:::

Now we can prove Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

::: proof
*Proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.* From Proposition [\[prop:Poisson\]](#prop:Poisson){reference-type="ref" reference="prop:Poisson"}, there exists $\varepsilon>0$ such that $$\frac{1}{N}
  \sum_{-\varphi(\xi)/(2\xi)\le k/N\le(1-\varphi(\xi)/\xi)/2}
  e^{N\psi(k/N)}
  \\
  =
  \int_{-\varphi(\xi)/(2\xi)}^{(1-\varphi(\xi)/\xi)/2}
  e^{N\psi(z)}\,dz
  +
  O\left(e^{-N\varepsilon}\right).$$ Since $f_N(z+\varphi(\xi)/\xi+1/(2N))-S(\xi)/\xi$ uniformly converges to $\psi(z)$, we have $$\begin{gathered}
  \frac{1}{N}
  \sum_{-\varphi(\xi)/(2\xi)\le k/N\le(1-\varphi(\xi)/\xi)/2}
  e^{N\left(f_N(k/N+\varphi(\xi)/\xi+1/(2N))-S(\xi)/\xi\right)}
  \\
  =
  \int_{-\varphi(\xi)/(2\xi)}^{(1-\varphi(\xi)/\xi)/2}
  e^{N\psi(z)}\,dz
  +O(e^{-N\varepsilon})
\end{gathered}$$ from [@Ohtsuki:QT2016 Remark 4.4]. Putting $l/N:=k/N+\varphi(\xi)/\xi$, we also have $$\begin{gathered}
  \sum_{-\varphi(\xi)/(2\xi)\le k/N\le(1-\varphi(\xi)/\xi)/2}
  e^{N\left(f_N\left(k/N+\varphi(\xi)/\xi+1/(2N)\right)-S(\xi)/\xi\right)}
  \\
  =
  e^{-N S(\xi)/\xi}
  \sum_{\varphi(\xi)/(2\xi)\le l/N\le(1+\varphi(\xi)/\xi)/2}
  \exp\left(N\times f_N\left(\frac{2l+1}{2N}\right)\right).
\end{gathered}$$ Thus we obtain $$\begin{gathered}
\label{eq:Poisson_f_N}
  \sum_{\varphi(\xi)/(2\xi)\le k/N\le(1+\varphi(\xi)/\xi)/2}
  \exp\left(N\times f_N\left(\frac{2k+1}{2N}\right)\right)
  \\
  =
  N\times e^{N S(\xi)/\xi}
  \left(
    \int_{-\varphi(\xi)/(2\xi)}^{(1-\varphi(\xi)/\xi)/2}
    e^{N\psi(z)}\,dz
    +
    O\left(e^{-N\varepsilon}\right)
  \right).
\end{gathered}$$ Now by using the saddle point method [@Ohtsuki:QT2016 Proposition 3.2] (see also [@Ohtsuki:QT2016 Remark 3.3]), we have $$\label{eq:saddle}
  \int_{-\varphi(\xi)/(2\xi)}^{(1-\varphi(\xi)/\xi)/2}
  e^{N\psi(z)}\,dz
  =
  \frac{\sqrt{\pi}}{\sqrt{\frac{\xi}{2}\sqrt{(2\cosh(\xi)-1)^2-4}}\sqrt{N}}
  \left(
    1+O(N^{-1})
  \right).$$ Putting $c_{-}:=\varphi(\xi)/(2\xi)$ and $c_{+}:=(1+\varphi(\xi)/\xi)/2$ in [\[eq:J_summation\]](#eq:J_summation){reference-type="eqref" reference="eq:J_summation"}, we finally have $$\begin{split}
  &J_N\bigl(E;\exp(\xi/N)\bigr)
  \\
  =&
  \frac{N\times e^{N S(\xi)/\xi}}{2\sinh(\xi/2)}
  \left(
    \int_{-\varphi(\xi)/(2\xi)}^{(1-\varphi(\xi)/\xi)/2}
    e^{N\psi(z)}\,dz
    +O\left(e^{-N\min\{\varepsilon,\delta'\}}\right)
  \right)
  \\
  =&
  \frac{\sqrt{\pi}\sqrt{N} e^{N\times S(\xi)/\xi}}
       {2\sinh(\xi/2)\sqrt{\frac{\xi}{2}\sqrt{(2\cosh(\xi)-1)^2-4}}}
  \left(1+O(N^{-1})\right).
\end{split}$$ where we use [\[eq:Poisson_f_N\]](#eq:Poisson_f_N){reference-type="eqref" reference="eq:Poisson_f_N"} at the first equality and [\[eq:saddle\]](#eq:saddle){reference-type="eqref" reference="eq:saddle"} at the second. Letting $T(\xi)$ denote $\frac{2}{\sqrt{(2\cosh(\xi)-1)^2-4}}$, we have $$J_N\bigl(E;\exp(\xi/N)\bigr)
  =
  \frac{\sqrt{\pi}}{2\sinh(\xi/2)}
  \sqrt{T(\xi)}
  \sqrt{\frac{N}{\xi}}
  \times
  e^{\frac{N}{\xi}S(\xi)}
  \left(1+O(N^{-1})\right).$$ Since $J_{N}(E;e^{-\xi/N})=J_{N}(E;e^{\xi/N})$ we obtain the required formula. ◻
:::
