---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2)"
section_id: sec-008-9-the-asymptotic-of-the-character-and-plancherel
section_title: "The asymptotic of the character and Plancherel measures for Uq(sl2)"
section_number: 9
pages: 23-28
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.948
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of unity into direct sums"
---
[]{#as9 label="as9"} In this section we will compute the asymptotic of the character and the Plancherel measures on tilting submodules of $T(1)^{\otimes N}$ when $N\to \infty$. We will start with computing the asymptotic of the multiplicity of $T(k)\subset T(1)^{\otimes N}$.

## The asymptotic of the multiplicity function

Note that in the tensor product $T(1)^{\otimes N}$ only submodules $T(k)$ with $k\equiv N \,\mathrm{mod}\,2$ can occur. For sufficiently large $k$ the decomposition of $T(1)\otimes T(k)$ is $2l$ periodic. This is why it is natural to write $N$ in base $2l$: $$N=2lN_1+N_0,\quad N_0=0,1,\ldots,2l-1.$$ Writing $k=lk_1+k_0$ we see that $N=k\,\mathrm{mod}\,2$ have the following implication:

-   $N_0$ is even and $k\equiv 0\,\mathrm{mod}\,2$ or $N_0$ is odd and $k\equiv 1\,\mathrm{mod}\,2$ imply $k_0\equiv N_0\,\mathrm{mod}\,2$

-   $N_0$ is even and $k\equiv 1\,\mathrm{mod}\,2$ or $N_0$ is odd and $k\equiv 0\,\mathrm{mod}\,2$ imply $k_0\equiv (N_0+1)\,\mathrm{mod}\,2$

Let us define a parameter $$\gamma=
\begin{cases}
1,&\text{if $k_0\equiv (N_0+1)\,\mathrm{mod}\,2$,}\\
0,&\text{if $k_0\equiv N_0\,\mathrm{mod}\,2$.}
\end{cases}$$ In the limit $N\to\infty$ $k_0$ remains discrete, and its parity is controlled by $\gamma$. Later we will see that limiting distribution is independent of both $N_0$ and $\gamma$.

The following theorem describes the pointwise asymptotic of the multiplicity function

::: theorem
[]{#multasymptmain label="multasymptmain"} Assume that $N=2lN_1+N_0$, $k=k_1l+k_0$, $N_1\to\infty$, $k_1\to\infty$ such that $l$, $N_0=0, \ldots, 2l-1$, $k_0=0, \ldots, l-1$ and $\xi=\frac{k_1}{2N_1}$ remain fixed. Then the asymptotic of the multiplicity has the following form: $$\label{mass}
        M^{(l)}_{T(k)}(N)=\frac{\mu_{k_0}^{(l)}(\xi,N_0,\gamma)}{\sqrt{2\pi\, 2lN_1}}\mathrm{exp}(2lN_1 S(\xi))\left(1+O\left(\frac{1}{N_1}\right)\right)$$ where $$S(\xi)=-\left(\frac{1-\xi}{2}\right)\mathrm{ln}\left(\frac{1-\xi}{2}\right)-\left(\frac{1+\xi}{2}\right)\mathrm{ln}\left(\frac{1+\xi}{2}\right),$$ and if $k_0\neq l-1$ $$\mu_{k_0}^{(l)}(\xi,N_0,\gamma)=\frac{2^{2+N_0}\xi}{\sqrt{(1-\xi^2)^{1+N_0}}}\Big(\frac{1-\xi}{1+\xi}\Big)^{\frac{\gamma l}{2}}\frac{\frac{1}{1+\xi}\Big(\frac{1+\xi}{1-\xi}\Big)^{\frac{l-k_0}{2}}-\frac{1}{1-\xi}\Big(\frac{1+\xi}{1-\xi}\Big)^{-\frac{l-k_0}{2}}}{\Big(\frac{1+\xi}{1-\xi}\Big)^{\frac{l}{2}}-\Big(\frac{1+\xi}{1-\xi}\Big)^{-\frac{l}{2}}},$$ if $k_0=l-1$ $$\mu_{k_0}^{(l)}(\xi,N_0,\gamma)=\frac{2^{2+N_0}\xi}{\sqrt{(1-\xi^2)^{1+N_0}}}\frac{1}{1+\xi}\Big(\frac{1-\xi}{1+\xi}\Big)^{\frac{l(1+\gamma)-1}{2}}.$$
:::

The proof of this theorem is presented in Appendix [\[apmultas\]](#apmultas){reference-type="ref" reference="apmultas"}.

## The pointwise asymptotic of the character measure density

Now let us find the asymptotic of the character measure density function $p^{(l)}_N(k;t)$ when $k$, $N\to\infty$ in the same way as in Theorem [\[multasymptmain\]](#multasymptmain){reference-type="ref" reference="multasymptmain"}. All we have to do is to combine the results of Theorem [\[multasymptmain\]](#multasymptmain){reference-type="ref" reference="multasymptmain"} with the asymptotical expansions of characters.

Using explicit formulae for characters we find that when $k_0\neq l-1$ $$\begin{aligned}
    \frac{\mathrm{ch}_{T(k)}(e^t)}{(\mathrm{ch}_{T(1)}(e^t))^N}=\frac{(e^{t(k_0+1)}+e^{-t(k_0+1)})(e^{tk_1l}-e^{-tk_1l})}{e^{t}-e^{-t}}\Big(\frac{e^{2t}-e^{-2t}}{e^{t}-e^{-t}}\Big)^{-N}=\\
    =\frac{(e^{t(k_0+1)}+e^{-t(k_0+1)})e^{t \gamma l}}{(e^{t}-e^{-t})(e^t+e^{-t})^{N_0}}\Big(\frac{e^{\xi t}}{e^{t}+e^{-t}}\Big)^{2lN_1}(1+o(1)),\nonumber
\end{aligned}$$ and when $k_0=l-1$ $$\begin{aligned}
    \frac{\mathrm{ch}_{T(lk_1+l-1)}(e^t)}{(\mathrm{ch}_{T(1)}(e^t))^N}=\frac{e^{tl(1+\gamma)}}{(e^{t}-e^{-t})(e^{t}+e^{-t})^{N_0}}\Big(\frac{e^{\xi t}}{e^{t}+e^{-t}}\Big)^{2lN_1}(1+o(1)).
\end{aligned}$$

Combining these formulae with the results of Theorem [\[multasymptmain\]](#multasymptmain){reference-type="ref" reference="multasymptmain"} we obtain that if $N=2N_1l+N_0$, $k=k_1l+k_0$, and $N_1$, $k_1\to\infty$ such that $l$, $k_0$, $N_0$, $t$ and $\xi=\frac{k_1}{2N_1}$ remain fixed we have the following pointwise asymptotic for the probability measure density function $$\label{charas}
    p^{(l)}_N(k;t)=\frac{\nu_{k_0}^{(l)}(\xi,N_0,\gamma;t)}{\sqrt{2\pi\, 2lN_1}}\mathrm{exp}(2lN_1 (S(\xi)-f(t)+t\xi))\left(1+O\left(\frac{1}{N_1}\right)\right),$$ where $$f(t)=\mathrm{ln}(e^t+e^{-t}),$$ and if $k_0\neq l-1$ $$\begin{aligned}
    &\nu_{k_0}^{(l)}(\xi,N_0,\gamma;t)=\frac{e^{t\gamma l}(e^{t(k_0+1)}+e^{-t(k_0+1)})}{(e^{t}-e^{-t})(e^t+e^{-t})^{N_0}}\frac{2^{2+N_0}\xi}{\sqrt{ (1-\xi^2)^{1+N_0}}}\Big(\frac{1-\xi}{1+\xi}\Big)^{\frac{\gamma l}{2}}\frac{\frac{1}{1+\xi}\Big(\frac{1+\xi}{1-\xi}\Big)^{\frac{l-k_0}{2}}-\frac{1}{1-\xi}\Big(\frac{1+\xi}{1-\xi}\Big)^{-\frac{l-k_0}{2}}}{\Big(\frac{1+\xi}{1-\xi}\Big)^{\frac{l}{2}}-\Big(\frac{1+\xi}{1-\xi}\Big)^{-\frac{l}{2}}},
\end{aligned}$$ if $k_0=l-1$ $$\nu_{k_0}^{(l)}(\xi,N_0,\gamma;t)=\frac{e^{tl(1+\gamma)}}{(e^{t}-e^{-t})(e^t+e^{-t})^{N_0}}\frac{2^{2+N_0}\xi}{\sqrt{(1-\xi^2)^{1+N_0}}} \frac{1}{1+\xi}\Big(\frac{1-\xi}{1+\xi}\Big)^{\frac{l(1+\gamma)-1}{2}}.$$

By definition $\xi\in[0,1)$. Note that the function $S(\xi)$, the large deviation rate function has its maximum at the isolated critical point $\xi_0$, i.e. $$\frac{\partial}{\partial\xi}(S(\xi)-f(t)+t\xi)=0$$ has a unique solution $$\label{xi0}
\xi_0=\frac{e^t-e^{-t}}{e^t+e^{-t}}.$$ In addition, $S(\xi_0)=0$.

Thus, we have a typical large deviation behavior of the density function $p^{(l)}_N(k;t)$: it is exponentially decaying when $\xi\neq\xi_0$ and it decays as $N_1^{-\frac{1}{2}}$ when $\xi=\xi_0$. Thus, asymptotically, the character measure concentrates in the neighborhood of $\xi=\xi_0$.

## The asymptotic of the character measure for $U_q(\mathfrak{sl}_2)$ {#aschar}

The following theorem describes the weak limit of the character probability measure for $U_q(\mathfrak{sl}_2)$.

::: theorem
[]{#theomch label="theomch"} Let $\xi_0$ be as in ([\[xi0\]](#xi0){reference-type="ref" reference="xi0"}), $N=2lN_1+N_0$ and $N_1\to\infty$ such that $N_0$, $l$, $t$ are fixed. Then for $k=k_1l+k_0$, random variables $k_0$ and $\alpha=\frac{k_1-2N_1 \xi_0}{\sqrt{2N_1}}$ converge to random variables on $\{0,\ldots,l-1\}\times\mathbb{R}$ and the character probability distribution weakly converges to the tensor product of two distributions $p_1(\bullet;t)\otimes p_2(\bullet;t)$ on $\{0,\ldots,l-1\}\times\mathbb{R}$. The distribution $p_1(\bullet;t)$ is a discrete probability distribution on $k_0=0,1,\ldots,l-1$ with density given by $$\label{p1}
        p_1(k_0;t)=\begin{cases}
            \frac{(e^{t(k_0+1)}+e^{-t(k_0+1)})(e^{t(l-1-k_0)}-e^{-t(l-1-k_0)})}{l(e^{tl}-e^{-tl})},& \textit{if $k_0=0,\ldots,l-2$},\\
            \frac{1}{l},& \textit{if $k_0=l-1$}.
        \end{cases}$$ The distribution $p_2(\bullet;t)$ is a Gaussian distribution on $\mathbb{R}$ with density given by $$\label{p2}
        p_2(\alpha;t)=\sqrt{\frac{l}{2\pi}}\mathrm{cosh}(t)e^{-\frac{\alpha^2l}{2}\left(\mathrm{cosh}(t)\right)^2}.$$
:::

The proof of this theorem is presented in Appendix [\[approofchar\]](#approofchar){reference-type="ref" reference="approofchar"}. The meaning of weak convergence is also recalled there.

Note that the asymptotic of the character measure is derived for $N_0$ being fixed, but it does not depend on $N_0$. The only dependence is the condition $N=k\,\mathrm{mod}\,2$. It implies that:

-   for even $N_0$ the summation over $k=k_1 l+k_0$ amounts for the summation over $k_0$ and $k_1$ of the same parity,

-   for odd $N_0$ the summation over $k=k_1 l+k_0$ amounts for the summation over $k_0$ and $k_1$ of the opposite parity.

In the limit $N_1\to\infty$ this dependence on $N_0$ disappears. Dependence on $\gamma$ disappears as well. Period $2l$ covers $k_1$, $k_1+1$, which for any $k_1$ includes all values of $k_0=0,\ldots,l-1$, so parity of $k_0$ doesn't have to be controlled.

This is why we conjecture that the asymptotic does not depend on $N_0$. To be precise, consider a sequence $$N^{(p)}=2lN_1^{(p)}+N_0^{(p)},\quad N_1^{(p)}\to\infty\text{ as }p\to\infty,$$ and $N_0^{(p)}=0,1,\ldots,2l-1$. For each $p\in\mathbb{Z}_{>0}$ let $k=lk_1+k_0\in\mathbb{Z}_{\geq 0}$ be the random variable distributed with respect to the character measure $p_{N^{(p)}}^{(l)}(k;t)$. We expect the following is true. As $p\to\infty$ with $l$, $t$ being fixed and $k=2N_1^{(p)}\xi_0+\sqrt{2N_1^{(p)}}\alpha$, $\alpha\in\mathbb{R}$, the character measure converges to the measure on $\{0,\ldots,l-1\}\times\mathbb{R}$ with the density $p_1(k_0;t)p_2(\alpha;t)$ as above, and the limit does not depend on the choice of sequences $\{N_1^{(p)}\}_{p\in\mathbb{Z}_{\geq 0}}$, $\{N_0^{(p)}\}_{p\in\mathbb{Z}_{\geq 0}}$.

## The asymptotic of the Placherel measure

Now let us find the asymptotic of the Plancherel measure when $N\to\infty$ and $l$ is fixed. From definition [\[planchdef\]](#planchdef){reference-type="ref" reference="planchdef"} it is evident that the same ideas as explored in Subsection [0.3](#aschar){reference-type="ref" reference="aschar"} are applicable to the Plancherel measure.

In the considered limit we have the following asymptotical expression for dimensions when $k_0\neq l-1$ $$\frac{\dim T(k)}{(\dim  T(1))^N}=\frac{2^{2-N_0}\xi l N_1}{2^{2lN_1}}\left(1+O\left(\frac{1}{N_1}\right)\right),$$ and when $k_0=l-1$ $$\frac{\dim T(lk_1+l-1)}{(\dim  T(1))^N}=\frac{2^{1-N_0}\xi l N_1}{2^{2lN_1}}\left(1+O\left(\frac{1}{N_1}\right)\right).$$

We obtain the following pointwise asymptotic for the probability measure distribution $$\label{Planchas}
    p^{(l)}_N(k)=\frac{\nu^{(l)}_{k_0}(\xi,N_0,\gamma)}{\sqrt{2\pi\,2lN_1}}\mathrm{exp}(2lN_1(S(\xi)-\mathrm{ln}2))\left(1+O\left(\frac{1}{N_1}\right)\right),$$ where if $k_0\neq l-1$ $$\nu^{(l)}_{k_0}(\xi,N_0,\gamma)=\frac{16\xi^2lN_1}{\sqrt{(1-\xi^2)^{1+N_0}}}\Big(\frac{1-\xi}{1+\xi}\Big)^{\frac{\gamma l}{2}}\frac{\frac{1}{1+\xi}\Big(\frac{1+\xi}{1-\xi}\Big)^{\frac{l-k_0}{2}}-\frac{1}{1-\xi}\Big(\frac{1+\xi}{1-\xi}\Big)^{-\frac{l-k_0}{2}}}{\Big(\frac{1+\xi}{1-\xi}\Big)^{\frac{l}{2}}-\Big(\frac{1+\xi}{1-\xi}\Big)^{-\frac{l}{2}}},$$ and if $k_0=l-1$ $$\nu^{(l)}_{k_0}(\xi,N_0,\gamma)=\frac{8\xi^2 lN_1}{\sqrt{(1-\xi^2)^{1+N_0}}}\frac{1}{1+\xi}\Big(\frac{1-\xi}{1+\xi}\Big)^{\frac{l(1+\gamma)-1}{2}}$$

Similarly to the character measure, the large deviation rate function $S(\xi)$ for the Plancherel measure has its maximum at the isolated critical point $\xi_0$, i.e. $$\frac{\partial}{\partial\xi}(S(\xi)-\mathrm{ln}2)=0$$ has a unique solution $\xi_0=0$, where the Plancherel measure concentrates asymptotically. Thus, we have the following theorem.

::: theorem
[]{#planchfluct label="planchfluct"} Let $N=2lN_1+N_0$ and $N_1\to\infty$ such that $N_0$, $l$ are fixed. Then for $k=k_1l+k_0$, random variables $k_0$ and $\alpha=\frac{k_1}{\sqrt{2N_1}}$ converge to random variables on $\{0,\ldots,l-1\}\times \mathbb{R}_{\geq 0}$ and the Plancherel probability distribution weakly converges to the tensor product of two distributions $p_1(\bullet)\otimes p_2(\bullet)$ on $\{0,\ldots,l-1\}\times \mathbb{R}_{\geq 0}$. The distribution $p_1(\bullet)$ is a discrete probability distribution on $k_0=0,1,\ldots,l-1$ with density given by $$p_1(k_0)=\begin{cases}
    \frac{2(l-1-k_0)}{l^2},& \textit{if $k_0=0,\ldots,l-2$},\\
    \frac{1}{l},& \textit{if $k_0=l-1$}
    \end{cases},$$ The distribution $p_2(\bullet)$ is a radial part of the Gaussian distribution on $\mathbb{R}^3$ with density given by $$p_2(\alpha)=\sqrt{\frac{2}{\pi}}l^{\frac{3}{2}}\alpha^2e^{-\frac{\alpha^2 l}{2}}.$$
:::

The proof of this theorem is presented in Appendix [\[approofplanch\]](#approofplanch){reference-type="ref" reference="approofplanch"}.

This asymptotic does not depend on $N_0$, $\gamma$. This is why we expect that the theorem holds for any sequence $\{N^{(p)}\}_{p\in\mathbb{Z}_{\geq 0}}$ with $N^{(p)}\to\infty$ as $p\to\infty$.

## The near Plancherel asymptotic of the character measure

Now consider the character measure but assume that $t=\frac{u}{\sqrt{2N_1}}$ as $N_1\to\infty$. In this case the character measure weakly converges to a deformation of a limiting measure obtained in Theorem [\[planchfluct\]](#planchfluct){reference-type="ref" reference="planchfluct"}.

::: theorem
[]{#intermsc label="intermsc"} Let $N=2lN_1+N_0$ and $N_1\to\infty$ such that $N_0$, $l$ are fixed and $t=\frac{u}{\sqrt{2N_1}}$. Then for $k=k_1l+k_0$, random variables $k_0$ and $b=\frac{k_1}{\sqrt{2N_1}}$ converge to random variables on $\{0,\ldots,l-1\}\times \mathbb{R}_{\geq 0}$ and the character probability distribution weakly converges to the tensor product of two distributions $p_1(\bullet)\otimes p_2(\bullet;u)$ on $\{0,\ldots,l-1\}\times \mathbb{R}_{\geq 0}$. The distribution $p_1(\bullet)$ is a discrete probability distribution on $k_0=0,1,\ldots,l-1$ with density given by $$p_1(k_0)=\begin{cases}
    \frac{2(l-1-k_0)}{l^2},& \textit{if $k_0=0,\ldots,l-2$},\\
    \frac{1}{l},& \textit{if $k_0=l-1$}
    \end{cases},$$ The distribution $p_2(\bullet;u)$ is a distribution on $\mathbb{R}_{\geq 0}$ with density given by $$p_2(b,u)=\frac{b}{u}\sqrt{\frac{l}{2\pi}}(e^{lbu}-e^{-lbu})e^{-\frac{u^2l}{2}} e^{-\frac{b^2l}{2}}.$$
:::

The proof of this theorem is presented in Appendix [\[proofintermsc\]](#proofintermsc){reference-type="ref" reference="proofintermsc"}. Analogously, we expect that this theorem holds for any sequence of $\{N^{(p)}\}_{p\in\mathbb{Z}_{\geq 0}}$, where $N^{(p)}\to\infty$ as $p\to\infty$.

## The Poisson asymptotic of the character measure

There is the limit when $N\to\infty$ and $t\to\infty$ such that the random walk induced by the Markov process for the character measure is drifted with the critical slope, meaning, the limit shape $\xi_0$ is on the right boundary of the Weyl alcove. It turns out that when $t$ increases logarithmically as $N\to\infty$ the character probability distribution weakly converges to a Poisson distribution in the vicinity of the right boundary of the Weyl alcove.

The following theorem gives the pointwise asymptotic of the multiplicity function in the limit when $N\to\infty$, $k\to\infty$ such that $N-k$ is fixed.

::: theorem
[]{#multdrift label="multdrift"} Assume that $N=2lN_1+N_0$, $k=k_1l+k_0$, $N_1\to\infty$, $k_1\to\infty$, such that $l$, $N_0=0,\dots,2l-1$, $k_0=0,\dots,l-1$ remain fixed, $N-k=2s$ for some $s\in\mathbb{Z}_{\geq 0}$. Then the asymptotic of $M^{(l)}_{T(k)}(N)$ is given by $$M^{(l)}_{T(k)}(N)=\frac{N^\frac{N-k}{2}}{\big(\frac{N-k}{2}\big)!}\Big(1+o(1)\Big).$$
:::

The proof of this theorem is presented in Appendix [\[poisproof1\]](#poisproof1){reference-type="ref" reference="poisproof1"}.

Using results of the Theorem [\[multdrift\]](#multdrift){reference-type="ref" reference="multdrift"}, we obtain the following limiting probability distribution for the character measure near the right boundary.

::: theorem
[]{#mesdrift label="mesdrift"} Let $N=2lN_1+N_0$ and $N_1\to\infty$, such that $N_0$, $l$ are fixed. If $t\to\infty$ such that $\theta=Ne^{-2t}$ is fixed, then for $k=k_1l+k_0$, random variable $s=\frac{N-k}{2}$ converges to a random variable on $\mathbb{Z}_{\geq 0}$ and the character probability distribution weakly converges to the Poisson distribution on $\mathbb{Z}_{\geq 0}$ with density given by $$p(s;\theta)=\frac{\theta^{s}e^{-\theta}}{s!}.$$
:::

The proof of this theorem is presented in Appendix [\[poisproof2\]](#poisproof2){reference-type="ref" reference="poisproof2"}. This result coincides with the one for classical Lie algebra $\mathfrak{sl}_2$.
