---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER"
section_id: sec-002-3-summation
section_title: "Summation"
section_number: 3
pages: 7-10
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.955
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — We study the asymptotic behavior of the N-dimensional colored Jones polynomial"
---
In this section, we use the quantum dilogarithm $T_N(z)$ to express $J_N(E;e^{\xi/N})$ without the product of a sequence.

Since the figure-eight knot $E$ is amphicheiral, its colored Jones polynomial is symmetric, that is, $J_{N}(E;q)=J_{N}(E;q^{-1})$. So we have $J_{N}(E;e^{\xi/N})=J_{N}(E;e^{-\xi/N})$ and we do not need to consider the case where $\xi<0$.

Recall that we choose a positive real number $\theta$ so that $\tan\theta<\frac{\pi}{\xi}$ and that we put $\gamma:=\frac{\xi}{2N\pi\sqrt{-1}}$. Putting $z:=\frac{\xi}{2\pi\sqrt{-1}}(1-l/N)$ ($0<l<N$) in [\[eq:lem\]](#eq:lem){reference-type="eqref" reference="eq:lem"}, we have $$\frac{\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1-l/N)-\frac{\xi}{4N\pi\sqrt{-1}}\right)\right)}
       {\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1-l/N)+\frac{\xi}{4N\pi\sqrt{-1}}\right)\right)}
  =
  1-e^{\xi(1-l/N)}$$ since $$\operatorname{Re}\left(\frac{\xi}{2\pi\sqrt{-1}}\left(1-\frac{l}{N}\right)e^{\theta\sqrt{-1}}\right)
  =
  \frac{\xi}{2\pi}\left(1-\frac{l}{N}\right)\sin\theta
  <
  \frac{1}{2}\left(1-\frac{l}{N}\right)\cos\theta,$$ which is between $0$ and $\cos\theta$. Therefore we have $$\begin{split}
  \prod_{l=1}^{k}\bigl(1-e^{(N-l)\xi/N}\bigr)
  &=
  \prod_{l=1}^{k}
  \frac{\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}\left(1-\frac{2l+1}{2N}\right)\right)\right)}
       {\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}\left(1-\frac{2l-1}{2N}\right)\right)\right)}
  \\
  &=
  \frac{\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1-\frac{2k+1}{2N})\right)\right)}
       {\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1-\frac{1}{2N})\right)\right)}.
\end{split}$$

Similarly, putting $z:=\frac{\xi}{2\pi\sqrt{-1}}(1+l/N)$ ($0<l<N$) in [\[eq:lem\]](#eq:lem){reference-type="eqref" reference="eq:lem"}, we have $$\frac{\exp
        \left(
          T_{N}
          \left(
            \frac{\xi}{2\pi\sqrt{-1}}(1+l/N)-\frac{\xi}{4N\pi\sqrt{-1}}
          \right)
        \right)}
       {\exp
        \left(
          T_{N}
          \left(
            \frac{\xi}{2\pi\sqrt{-1}}(1+l/N)+\frac{\xi}{4N\pi\sqrt{-1}}
          \right)
        \right)}
  =
  1-e^{\xi(1+l/N)}$$ since $$\operatorname{Re}\left(\frac{\xi}{2\pi\sqrt{-1}}\left(1+\frac{l}{N}\right)e^{\theta\sqrt{-1}}\right)
  =
  \frac{\xi}{2\pi}\left(1+\frac{l}{N}\right)\sin\theta
  <
  \frac{1}{2}\left(1+\frac{l}{N}\right)\cos\theta,$$ which is between $0$ and $\cos\theta$. So we have $$\begin{split}
  \prod_{l=1}^{k}\bigl(1-e^{(N+l)\xi/N}\bigr)
  &=
  \prod_{l=1}^{k}
  \frac{\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}\left(1+\frac{2l-1}{2N}\right)\right)\right)}
       {\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}\left(1+\frac{2l+1}{2N}\right)\right)\right)}
  \\
  &=
  \frac{\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1+\frac{1}{2N})\right)\right)}
       {\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1+\frac{2k+1}{2N})\right)\right)}.
\end{split}$$ Therefore we have from [\[eq:J_N_fig8\]](#eq:J_N_fig8){reference-type="eqref" reference="eq:J_N_fig8"} $$\begin{split}
  &J_N\bigl(E;\exp(\xi/N)\bigr)
  \\
  &=
  \frac{\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1+\frac{1}{2N})\right)\right)}
       {\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1-\frac{1}{2N})\right)\right)}
  \\
  &\quad\times
  \sum_{k=0}^{N-1}
  e^{-k\xi}
  \frac{\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1-\frac{2k+1}{2N})\right)\right)}
       {\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1+\frac{2k+1}{2N})\right)\right)}.
\end{split}$$ We use the following lemma, a proof of which is given in Section [\[sec:proofs_lemmas\]](#sec:proofs_lemmas){reference-type="ref" reference="sec:proofs_lemmas"}.

::: lem
[]{#lem:T_special label="lem:T_special"} We have $$\frac{\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1+\frac{1}{2N})\right)\right)}
       {\exp\left(T_{N}\left(\frac{\xi}{2\pi\sqrt{-1}}(1-\frac{1}{2N})\right)\right)}
  =
  \frac{1}{1-e^{\xi}}
  =
  \frac{-e^{-\xi/2}}{2\sinh(\xi/2)}.$$
:::

Now we define $$f_{N}(z)
  :=
  \frac{1}{N}
  \left(
    T_{N}\left(\frac{\xi(1-z)}{2\pi\sqrt{-1}}\right)
    -
    T_{N}\left(\frac{\xi(1+z)}{2\pi\sqrt{-1}}\right)
  \right)
  -\xi z
  +2\pi\sqrt{-1}z$$ so that $$\label{eq:Jones_sum}
  J_N\bigl(E;\exp(\xi/N)\bigr)
  =
  \frac{1}{2\sinh(\xi/2)}
  \sum_{k=0}^{N-1}\exp\left(N\times f_{N}\left(\frac{2k+1}{2N}\right)\right).$$ Since $T_{N}(z)$ is defined for $z$ with $0<\operatorname{Re}(z e^{\theta\sqrt{-1}})<\cos\theta$, the function $f_{N}(z)$ is defined for $z$ with $$\left|\frac{\operatorname{Im}{z}}{\tan\theta}+\operatorname{Re}{z}\right|<1$$ from the assumption $\tan\theta<\frac{\pi}{\xi}$.

From Proposition [\[prop:T_N_L_2\]](#prop:T_N_L_2){reference-type="ref" reference="prop:T_N_L_2"}, $f_N(z)$ converges to the following function: $$F(z)
  :=
  \frac{1}{\xi}
  \left(
    \mathcal{L}_2\left(\frac{\xi(1-z)}{2\pi\sqrt{-1}}\right)
    -
    \mathcal{L}_2\left(\frac{\xi(1+z)}{2\pi\sqrt{-1}}\right)
  \right)
  -\xi z+2\pi\sqrt{-1}z$$ in the region $$\left\{
    z\in\mathbb{C}\Bigm|
    \left|\frac{\operatorname{Im}{z}}{\tan\theta}+\operatorname{Re}{z}\right|
    \le
    1-\frac{2\pi\nu}{\xi\sin\theta},
    |\operatorname{Re}{z}|\le\frac{2\pi M}{\xi}-1
  \right\}.$$ Since $\operatorname{Im}\left(\frac{\xi(1\pm z)}{2\pi\sqrt{-1}}\right)=\frac{-\xi}{2\pi}(1\pm\operatorname{Re}{z})$, $$F(z)
  =
  \frac{1}{\xi}
  \left(
    \operatorname{Li}_2\left(e^{-\xi(1+z)}\right)
    -
    \operatorname{Li}_2\left(e^{-\xi(1-z)}\right)
  \right)
  +\xi z$$ when $-1<\operatorname{Re}{z}<1$ from [\[eq:L2\]](#eq:L2){reference-type="eqref" reference="eq:L2"}.

::: rem
[]{#rem:F_real label="rem:F_real"} When $x$ is real and $-1<x<1$, then $F(x)$ is also real.
:::

From Lemma [\[lem:der_L\]](#lem:der_L){reference-type="ref" reference="lem:der_L"}, the first and the second derivatives of $F(z)$ are given as follows: $$\begin{aligned}
  F'(z)
  &=
  \mathcal{L}_1\left(\frac{\xi(1-z)}{2\pi\sqrt{-1}}\right)
  +
  \mathcal{L}_1\left(\frac{\xi(1+z)}{2\pi\sqrt{-1}}\right)
  -\xi+2\pi\sqrt{-1},
  \\
  F''(z)
  &=
  \frac{\xi}{2\pi\sqrt{-1}}
  \left(
    \mathcal{L}_0\left(\frac{\xi(1-z)}{2\pi\sqrt{-1}}\right)
    -
    \mathcal{L}_0\left(\frac{\xi(1+z)}{2\pi\sqrt{-1}}\right)
  \right)
  \\
  &=
  \frac{\xi(e^{-\xi z}-e^{\xi z})}{e^{\xi}+e^{-\xi}-e^{\xi z}-e^{-\xi z}}.
\end{aligned}$$ Note that when $-1<\operatorname{Re}{z}<1$, we have $$\label{eq:F'}
\begin{split}
  F'(z)
  &=
  \log(1-e^{-\xi(1-z)})+\log(1-e^{-\xi(1+z)})+\xi
  \\
  &=
  \log(e^{\xi}+e^{-\xi}-e^{\xi z}-e^{-\xi z})
\end{split}$$ from [\[eq:L1\]](#eq:L1){reference-type="eqref" reference="eq:L1"}, since $\operatorname{Im}\left(\frac{\xi(1\pm z)}{2\pi\sqrt{-1}}\right)=-\frac{\xi}{2\pi}(1\pm\operatorname{Re}{z})$.

We assume that $\xi>\kappa$, where $\kappa:=\operatorname{arccosh}(3/2)=\log(\frac{3+\sqrt{5}}{2})=0.962\dots$. Put $$\varphi(\xi)
  :=
  \operatorname{arccosh}\left(\cosh(\xi)-\frac{1}{2}\right)
  =
  \log
  \left(
    \cosh(\xi)-\frac{1}{2}+\frac{1}{2}\sqrt{(2\cosh(\xi)-1)^2-4}
  \right).$$ Note that since $\xi>\kappa$, we have $\cosh(\xi)>\cosh(\varphi(\xi))$ and $\cosh(\xi)>\cosh(\kappa)=\frac{3}{2}$. So we have $0<\varphi(\xi)<\xi$. Note also that this definition is the same as that in Section [\[sec:introduction\]](#sec:introduction){reference-type="ref" reference="sec:introduction"}.

Since $0<\varphi(\xi)<\xi$, we have $$\begin{aligned}
  F(\varphi(\xi)/\xi)
  &=
  \frac{1}{\xi}
  \left(
    \operatorname{Li}_2(e^{-\xi-\varphi(\xi)})-\operatorname{Li}_2(e^{-\xi+\varphi(\xi)})
  \right)
  +\varphi(\xi),
  \label{eq:F_phi}
  \\
  F'(\varphi(\xi)/\xi)
  &=0,
  \label{eq:F'_phi}
  \\
  F''(\varphi(\xi)/\xi)
  &=
  -\xi\sqrt{(2\cosh(\xi)-1)^2-4}.
  \label{eq:F''_phi}
\end{aligned}$$ The second equality follows since $$e^{\varphi(\xi)}+e^{-\varphi(\xi)}
  =
  e^{\xi}+e^{-\xi}-1.$$

Put $$S(\xi)
  :=
  \xi F(\varphi(\xi)/\xi)
  =
  \operatorname{Li}_2(e^{-\xi-\varphi(\xi)})-\operatorname{Li}_2(e^{-\xi+\varphi(\xi)})
  +
  \xi\varphi(\xi).$$ Since $$\begin{split}
  \frac{d\,S(\xi)}{d\,\xi}
  &=
  (1+\varphi'(\xi))\log(1-e^{-\xi-\varphi(\xi)})
  -
  (1-\varphi'(\xi))\log(1-e^{-\xi+\varphi(\xi)})
  \\
  &\quad
  +\varphi(\xi)+\xi\varphi'(\xi)
  \\
  &=
  \log\frac{e^{\varphi(\xi)}-e^{-\xi}}{1-e^{-\xi+\varphi(\xi)}}
  +
  \varphi'(\xi)\log\left(e^{\xi}+e^{-\xi}-e^{\varphi(\xi)}-e^{-\varphi(\xi)}\right)
  \\
  &=
  \log\frac{e^{\varphi(\xi)}-e^{-\xi}}{1-e^{-\xi+\varphi(\xi)}}
  >0
\end{split}$$ and $S(\kappa)=0$, $S(\xi)>0$ for $\xi>\kappa$.

Recalling that $F(x)\in\mathbb{R}$ when $x$ is real and $-1<x<1$, we have the following lemma.

::: lem
As a function of a real variable $x$, the real-valued function $F(x)$ takes its maximum $S(\xi)/\xi$ at $x=\varphi(\xi)/\xi$ in the half open interval $[0,1)$. Moreover, it is strictly increasing (decreasing, respectively) when $x<\varphi(\xi)/\xi$ ($x>\varphi(\xi)/\xi$, respectively).
:::

::: proof
*Proof.* Since we have $$F'(x)
  =
  \log(e^{\xi}+e^{-\xi}-e^{\xi x}-e^{-\xi x}),$$ we see that $F'(x)$ is strictly decreasing. Since $F(0)=0$ and $F'(x)$ becomes $0$ when $x=\varphi(\xi)/\xi<1$, the lemma follows. ◻
:::

We have the following corollary.

::: cor
For any $c_{-}$ and $c_{+}$ with $0<c_{-}<\varphi(\xi)/\xi<c_{+}<1$, there exists $\delta>0$ such that $F(x)<S(\xi)/\xi-\delta$ if $x<c_{-}$ or $x>c_{+}$.
:::

So we have $e^{N\times F(x)}<e^{N(S(\xi)/\xi-\delta)}$ if $x\not\in[c_{-},c_{+}]$. Since $f_N(x)$ uniformly converges to $F(x)$ from Proposition [\[prop:T_N_L_2\]](#prop:T_N_L_2){reference-type="ref" reference="prop:T_N_L_2"}, we also have $\left|e^{N\times f_N(x)}\right|<e^{N(S(\xi)/\xi-\delta')}$ for some $\delta'>0$ if $x\not\in[c_{-},c_{+}]$ and $N$ is sufficiently large.

Therefore we have $$\begin{aligned}
  \left|\sum_{0<k/N<c_{-}}\exp\left(N\times f_N\left(\frac{2k+1}{2N}\right)\right)\right|
  &<
  c_{-}Ne^{N(S(\xi)/\xi-\delta')}
  \\
  \intertext{and}
  \left|\sum_{c_{+}<k/N<1}\exp\left(N\times f_N\left(\frac{2k+1}{2N}\right)\right)\right|
  &<
  (1-c_{+})Ne^{N(S(\xi)/\xi-\delta')}.
\end{aligned}$$ As a result, we have $$\begin{split}
  &\sum_{k=0}^{N-1}\exp\left(N\times f_N\left(\frac{2k+1}{2N}\right)\right)
  \\
  =&
  \sum_{c_{-}\le k/N\le c_{+}}\exp\left(N\times f_N\left(\frac{2k+1}{2N}\right)\right)
  +
  O\left(Ne^{N(S(\xi)/\xi-\delta')}\right).
\end{split}$$ From [\[eq:Jones_sum\]](#eq:Jones_sum){reference-type="eqref" reference="eq:Jones_sum"}, we also have $$\begin{gathered}
\label{eq:J_summation}
  J_N\bigl(E;\exp(\xi/N)\bigr)
  \\
  =
  \frac{1}{2\sinh(\xi/2)}
  \sum_{c_{-}\le k/N\le c_{+}}\exp\left(N\times f_N\left(\frac{2k+1}{2N}\right)\right)
  +
  O\left(Ne^{N(S(\xi)/\xi-\delta')}\right).
\end{gathered}$$
