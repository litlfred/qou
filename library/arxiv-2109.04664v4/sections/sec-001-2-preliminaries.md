---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 4-7
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.958
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — We study the asymptotic behavior of the N-dimensional colored Jones polynomial"
---
In this section, we first introduce the colored Jones polynomial, and then we define a quantum dilogarithm, and variants of the logarithm and the dilogarithm. We also describe some of their properties.

For a knot $K$ in the three-sphere $S^3$, we denote by $J_N(K;q)$ the colored Jones polynomial of $K$ associated with the $N$-dimensional irreducible representation of the Lie algebra $\frak{sl}(2;\mathbb{C})$ [@Kirby/Melvin:INVEM1991; @Reshetikhin/Turaev:INVEM1991]. We normalize it so that $J_N(U;q)=1$ for the unknot $U\subset S^3$. Note that $J_2(K;q)$ is the original Jones polynomial [@Jones:BULAM31985].

Let $E$ be the figure-eight knot. We use the following formula obtained by K. Habiro [@Habiro:SURIK2000 P. 36 (1)] and T.T.Q. Le [@Le:TOPOA2003 P. 129]. See also [@Masbaum:ALGGT12003]. $$\label{eq:J_N_fig8}
\begin{split}
  J_N(E;q)
  &=
  \sum_{k=0}^{N-1}
  \prod_{l=1}^{k}\left(q^{(N-l)/2}-q^{-(N-l)/2}\right)\left(q^{(N+l)/2}-q^{(N+l)/2}\right)
  \\
  &=
  \sum_{k=0}^{N-1}
  q^{-kN}
  \prod_{l=1}^{k}\left(1-q^{N-l}\right)\left(1-q^{N+l}\right).
\end{split}$$

Next, we define functions $T_N(z)$, $\mathcal{L}_{0}(z)$, $\mathcal{L}_{1}(z)$, and $\mathcal{L}_{2}(z)$, which are related as $$\begin{aligned}
  T_{N}(z)
  &=
  \frac{N}{\xi}\mathcal{L}_{2}(z)+O(1/N)\quad(N\to\infty),
  \\
  \frac{d\,\mathcal{L}_{2}}{d\,z}(z)
  &=
  -2\pi\sqrt{-1}\mathcal{L}_{1}(z),
  \\
  \frac{d\,\mathcal{L}_{1}}{d\,z}(z)
  &=
  -\mathcal{L}_{0}(z).
\end{aligned}$$

Let $\xi$ be a positive real number. We define $C_{0}:=(-\infty,-1]\cup\{e^{\tau\sqrt{-1}}\mid0\le\tau\le\pi\}\cup[1,\infty)$ and $C_{\theta}:=e^{\sqrt{-1}\theta}C_{0}$, where $\theta$ is a positive real number with $\tan\theta<\frac{\pi}{\xi}$ and we orient $C_{0}$ from left to right.

Consider the following integrals: $$\int_{C_{\theta}}\frac{e^{(2z-1)x}}{x\sinh(x)\sinh(\gamma x)}\,dx,
  \quad
  \int_{C_{\theta}}\frac{e^{(2z-1)x}}{x^{m}\sinh(x)}\,dx,$$ where $m=0,1,2$, $\gamma:=\frac{\xi}{2N\pi\sqrt{-1}}$ for an integer $N\ge2$, and $z$ is a complex number with $0<\operatorname{Re}(ze^{\sqrt{-1}\theta})<\cos\theta$. Here we follow [@Faddeev:LETMP1995] to introduce $T_N(z)$, which plays an important role in the paper. Note that the set of the poles of the integrands are $$\{k\pi\sqrt{-1}\mid k\in\mathbb{Z}\}\cup\{2lN\pi^2/\xi\mid l\in\mathbb{Z}\}
  \quad\text{and}\quad
  \{k\pi\sqrt{-1}\mid k\in\mathbb{Z}\},$$ respectively. Therefore, if $N$ is large enough, then the only pole inside the unit circle centered at the origin is $0\in\mathbb{C}$ and so the path of integral $C_{\theta}$ avoids the poles. Proofs of their convergences (Lemmas [\[lem:converge_T\]](#lem:converge_T){reference-type="ref" reference="lem:converge_T"} and [\[lem:integrals\]](#lem:integrals){reference-type="ref" reference="lem:integrals"} below) are given in Section [\[sec:proofs_lemmas\]](#sec:proofs_lemmas){reference-type="ref" reference="sec:proofs_lemmas"}.

::: lem
[]{#lem:converge_T label="lem:converge_T"} The integral $\int_{C_{\theta}}\frac{e^{(2z-1)x}}{x\sinh(x)\sinh(\gamma x)}\,dx$ converges if $z\in\mathbb{C}$ satisfies $-\frac{\xi\sin\theta}{4N\pi}<\operatorname{Re}(ze^{\theta\sqrt{-1}})<\cos\theta+\frac{\xi\sin\theta}{4N\pi}$.
:::

::: lem
[]{#lem:integrals label="lem:integrals"} If $z\in\mathbb{C}$ satisfies $0<\operatorname{Re}(ze^{\theta\sqrt{-1}})<\cos\theta$, then the integral $\int_{C_{\theta}}\frac{e^{(2z-1)x}}{x^{m}\sinh(x)}\,dx$ converges for $m=0,1,2$.
:::

Now define functions $T_N(z)$ and $\mathcal{L}_{m}(z)$ ($m=0,1,2$) by using the integrals above.

::: defn
Fix an integer $N\ge2$ and put $\gamma:=\frac{\xi}{2N\pi\sqrt{-1}}$. We define $$T_N(z)
  :=
  \frac{1}{4}
  \int_{C_{\theta}}
  \frac{e^{(2z-1)x}}{x\sinh(x)\sinh(\gamma x)}\,dx,$$ for a complex number $z$ with $-\frac{\xi\sin\theta}{4N\pi}<\operatorname{Re}(ze^{\theta\sqrt{-1}})<\cos\theta+\frac{\xi\sin\theta}{4N\pi}$.
:::

::: defn
For a complex number $z$ with $0<\operatorname{Re}(ze^{\sqrt{-1}\theta})<\cos\theta$, we define $$\begin{aligned}
  \mathcal{L}_0(z)
  &:=
  \int_{C_{\theta}}\frac{e^{(2z-1)x}}{\sinh(x)}\,dx,
  \\
  \mathcal{L}_1(z)
  &:=
  -\frac{1}{2}
  \int_{C_{\theta}}\frac{e^{(2z-1)x}}{x\sinh(x)}\,dx,
  \\[5mm]
  \mathcal{L}_2(z)
  &:=
  \frac{\pi\sqrt{-1}}{2}
  \int_{C_{\theta}}\frac{e^{(2z-1)x}}{x^2\sinh(x)}\,dx.
\end{aligned}$$
:::

::: lem
[]{#lem:L0_1_2 label="lem:L0_1_2"} For $m=0,1,2$, we calculate $\mathcal{L}_{m}(z)$ as follows. $$\begin{aligned}
  \mathcal{L}_0(z)
  &=
  \frac{-2\pi\sqrt{-1}}{1-e^{-2\pi\sqrt{-1}z}},
  \label{eq:L0}
  \\
  \mathcal{L}_1(z)
  &=
  \begin{cases}
    \log\left(1-e^{2\pi\sqrt{-1}z}\right)&\text{if $\operatorname{Im}{z}\ge0$,}
    \\[3mm]
    \pi\sqrt{-1}(2z-1)+\log\left(1-e^{-2\pi\sqrt{-1}z}\right)&\text{if $\operatorname{Im}{z}<0$,}
  \end{cases}
  \label{eq:L1}
  \\[5mm]
  \mathcal{L}_2(z)
  &=
  \begin{cases}
    \operatorname{Li}_2\left(e^{2\pi\sqrt{-1}z}\right)&\text{if $\operatorname{Im}{z}\ge0$,}
    \\[3mm]
    \pi^2\left(2z^2-2z+\frac{1}{3}\right)-\operatorname{Li}_2\left(e^{-2\pi\sqrt{-1}z}\right)
    &\text{if $\operatorname{Im}{z}<0$}.
  \end{cases}
  \label{eq:L2}
\end{aligned}$$
:::

Proofs are also given in Section [\[sec:proofs_lemmas\]](#sec:proofs_lemmas){reference-type="ref" reference="sec:proofs_lemmas"}.

::: rem
In [\[eq:L1\]](#eq:L1){reference-type="eqref" reference="eq:L1"} and [\[eq:L2\]](#eq:L2){reference-type="eqref" reference="eq:L2"}, we use $\log(1-x)$ and $\operatorname{Li}_2(x)$ only for $|x|\le1$ ($x\ne1$).
:::

Since $$\begin{split}
  T_{N}(z-\gamma/2)-T_{N}(z+\gamma/2)
  &=
  \int_{C_{\theta}}
  \frac{e^{(2z-\gamma-1)x}-e^{(2z+\gamma-1)x}}{4x\sinh(x)\sinh(\gamma x)}\,dx
  \\
  &=
  -
  \int_{C_{\theta}}
  \frac{e^{(2z-1)x}}{2x\sinh(x)}\,dx
  \\
  &=
  \mathcal{L}_1(z),
\end{split}$$ we have the following corollary.

::: cor
If $0<\operatorname{Re}(ze^{\theta\sqrt{-1}})<\cos\theta$, then we have $$\label{eq:lem}
  \frac{\exp\left(T_{N}(z-\gamma/2)\right)}{\exp\left(T_{N}(z+\gamma/2)\right)}
  =
  1-e^{2\pi\sqrt{-1}z}.$$
:::

We will show relations among the functions $T_{N}(z)$ and $\mathcal{L}_{m}(z)$ ($m=0,1,2$).

We can prove that $\frac{1}{N}T_{N}(z)$ uniformly converges to $\frac{1}{\xi}\mathcal{L}_{2}(z)$. More precisely, we have the following proposition. See [@Ohtsuki:QT2016 Proposition A.1].

::: prop
[]{#prop:T_N_L_2 label="prop:T_N_L_2"} For any positive real number $M$ and a sufficiently small positive real number $\nu$, we have $$T_N(z)
  =
  \frac{N}{\xi}\mathcal{L}_2(z)
  +
  O(1/N)
  \quad(N\to\infty)$$ in the region $$\{z\in\mathbb{C}\mid\nu\le\operatorname{Re}(ze^{\theta\sqrt{-1}})\le\cos\theta-\nu,|\operatorname{Im}{z}|\le M\}.$$ In particular, the function $\frac{1}{N}T_N(z)$ uniformly converges to $\frac{1}{\xi}\mathcal{L}_2(z)$ in the region above.
:::

A proof is given in Section [\[sec:proofs_lemmas\]](#sec:proofs_lemmas){reference-type="ref" reference="sec:proofs_lemmas"}. Since we may regard $\mathcal{L}_2(z)$ as a variant of the dilogarithm from Lemma [\[lem:L0_1_2\]](#lem:L0_1_2){reference-type="ref" reference="lem:L0_1_2"}, the function $T_{N}(z)$ is another quantum dilogarithm.

The functions $\mathcal{L}_{0}(z)$, $\mathcal{L}_{1}(z)$, and $\mathcal{L}_{2}(z)$ are related as follows.

::: lem
[]{#lem:der_L label="lem:der_L"} The derivatives of $\mathcal{L}_1(z)$ and $\mathcal{L}_2(z)$ are given as follows: $$\begin{aligned}
  \frac{d\,\mathcal{L}_2}{d\,z}(z)
  &=
  -2\pi\sqrt{-1}\mathcal{L}_1(z),
  \\
  \dfrac{d\,\mathcal{L}_1}{d\,z}(z)
  &=
  -\mathcal{L}_0(z).
\end{aligned}$$
:::

::: proof
*Proof.* We have $$\begin{split}
  \frac{d\,\mathcal{L}_2}{d\,z}(z)
  &=
  \frac{\pi\sqrt{-1}}{2}\int_{C_{\theta}}\left(\frac{d}{d\,z}\frac{e^{(2z-1)x}}{x^2\sinh(x)}\right)\,dx
  \\
  &=
  \pi\sqrt{-1}\int_{C_{\theta}}\frac{e^{(2z-1)x}}{x\sinh(x)}\,dx
  \\
  &=
  -2\pi\sqrt{-1}\mathcal{L}_1(z),
\end{split}$$ and $$\begin{split}
  \frac{d\,\mathcal{L}_1}{d\,z}(z)
  &=
  -\frac{1}{2}\int_{C_{\theta}}\left(\frac{d}{d\,z}\frac{e^{(2z-1)x}}{x\sinh(x)}\right)\,dx
  \\
  &=
  -\int_{C_{\theta}}\frac{e^{(2z-1)x}}{\sinh(x)}\,dx
  \\
  &=
  -\mathcal{L}_0(z),
\end{split}$$ completing the proof. ◻
:::
