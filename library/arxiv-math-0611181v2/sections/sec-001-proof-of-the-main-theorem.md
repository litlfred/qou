---
doc_id: arxiv-math-0611181v2
doc_title: "Proof of the volume conjecture for Whitehead chains"
section_id: sec-001-proof-of-the-main-theorem
section_title: "Proof of the main theorem"
section_number: null
pages: 3-6
source_pdf: 0611181v2.pdf
source_sha256: 6931e3ebca584de9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.994
doc_brief: "Proof of the volume conjecture for Whitehead chains — We prove the volume conjecture for an inﬁnite family of links called White- head chains that generalizes both the Whitehead link and the"
---
In this section we give an overview of the proof of the main theorem, postponing the proofs of the more technical lemmas to the next section.

The first step is to obtain an expression for the colored Jones polynomials of a general Whitehead chain.

::: lem
Let $a,b,c,d$ be integers, with $b \geq 2$ and $c,d \geq 0$. We have the following formulas for the colored Jones polynomial: $$J_N(W_{a,1,c,d})(e^{\frac{2\pi i}{N}}) =  \phi_N\sum_{n=0}^{N-1}(2n+1)\chi_{N,n}^{4a-c+d}\left(\sum_{k=0}^{N-1-n} S_{n,k}\right)^{c+d}$$ $J_{N}(W_{a,b,c,d})(e^{\frac{2\pi i}{N}})=0$ when $N$ is even and for $N=2M+1$ we have: $$J_{N}(W_{a,b,c,d})(e^{\frac{2\pi i}{N}}) =  \phi_N N^{b}\chi_{N,M}^{4a-c+d}\left(\sum_{k=0}^{M} S_{M,k}\right)^{c+d}$$ Where we define $\phi_N =
\exp\left(\frac{(N-1)(c-d)}{N}\pi i\right)$ if $c+d = 1$ and $\phi_N = (-1)^{(N-1)(c-d)}$ otherwise, and we define $\chi$ and $S$ by $$\chi_{N,n}=\exp\left(\frac{n(n+1-N)}{2N}\pi i\right), \quad
S_{n,k} =
\prod_{j=1}^n\frac{2\sin^2(\frac{(k+j)\pi}{N})}{\sin(\frac{j\pi}{N})}$$
:::

::: proof
*Proof.* Recall that the unnormalized $N$-colored Jones invariants are intertwining operators of $V_N\otimes V_N$, where $V_N$ corresponds to the $N$-dimensional irreducible representation of $sl_2$. Using the decomposition $V_N\otimes V_N
= \bigoplus_{n=0}^{N-1}V_{2n+1}$ one can write the unnormalized colored Jones invariants of the tangles in figure 1 in the following way [@HaoZheng]: $$\tilde{J}_N(t)=\bigoplus_{n=0}^{N-1}
\mathrm{Tangle}(n,t)\cdot\mathrm{id}_{V_{2n+1}}$$ were the function $\mathrm{Tangle}(n,t)$ depends on the tangle and $t=e^{h}$. If we define $[n] =
\frac{t^{\frac{n}{2}}-t^{-\frac{n}{2}}}{t^{\frac{1}{2}}-t^{-\frac{1}{2}}}$ then the functions for the tangles in figure 1 are:

$$\mathrm{T}(n,t) =  t^{n(n+1)},\quad \mathrm{B}(n,t) =  \frac{[N(2n+1)]}{[2n+1]}$$

$$\mathrm{C}(n,t) =  t^{(N^2-1)/2+N(N-1)/2}\sum_{k=0}^{N-1-n}t^{-N(n+k)}\prod_{j=1}^n\frac{(1-t^{N-j-k})(1-t^{j+k})}{1-t^{j}}$$

The colored Jones polynomials of the mirror-images of these tangles are obtained by replacing $t$ by $t^{-1}$. The factor $t^{(N^2-1)/2}$ in the formula for $\mathrm{C}(n,t)$ is a correction due to framing that should be included only if both strands in the clasp belong to the same component. For Whitehead chains this means that it should be included only when $c+d = 1$.

By the multiplicativity of the colored Jones invariant with respect to composition of tangles we can now calculate the colored Jones polynomial of all Whitehead chains. The general formula for the normalized version of the colored Jones polynomial of the Whitehead chains is: $$J_N(W_{a,b,c,d})(t) = \sum_{n=0}^{N-1}\frac{[2n+1]}{[N]}\mathrm{T}(n,t)^a\mathrm{B}(n,t)^b\mathrm{C}(n,t)^c\mathrm{C}(n,t^{-1})^d$$ The factor $\frac{[2n+1]}{[N]}$ comes from the normalization and from taking the closure of composition of the tangles.

Routine calculations now yield the above formulas. ◻
:::

From now on we will use the shorthand $J_{N,a,b,c,d} =
J_N(W_{a,b,c,d})(e^{\frac{2\pi i}{N}})$.

The next step in proving the main theorem is to investigate the asymptotics of the above formulas for the colored Jones polynomials as $N\to \infty$. The factors $S_{n,k}$ turn out to play a crucial role because they dominate the absolute value of the $(n,k)$-th term. There exists a unique maximum $\tilde{S}_N =
S_{\left\lfloor\frac{N}{2}\right\rfloor,\left\lfloor\frac{N}{4}\right\rfloor}$ for the $S_{n,k}$. This term dominates all others so that most of the asymptotics of $J_{N,a,b,c,d}$ can be read off from this term only. In order to make this precise we need to compare the other values of $S_{n,k}$ to the maximum value.

Let us choose a fixed number $\delta \in (\frac{1}{2},\frac{c+d+5}{2(c+d+4)})$ once and for all, where the numbers $c$ and $d$ are the parameters of $W_{a,b,c,d}$. Define $n'=|n-\left\lfloor\frac{N}{2}\right\rfloor|$ and $k' =
|k-\left\lfloor\frac{N}{4}\right\rfloor|$ to be the distances from the maximum. The next lemma shows how we can estimate the other values of $S_{n,k}$.

::: lem
Using the above definitions of $n',k'$ and $\delta$ we have:$\mathrm{a)}$ If $n'+k' < N^\delta$ then $S_{n,k}\tilde{S}_N^{-1} = \exp(-\frac{\pi}{N}(n'^2+2n'k'+2k'^2))
+ \mathcal{O}(N^{3\delta - 2})$, as $N \to \infty$. $\mathrm{b)}$ There are $C,\epsilon >
0$ such that if $n'+k' \geq N^\delta$ then $S_{n,k}\tilde{S}_N^{-1} < C \exp(-\epsilon N^{2\delta - 1})$
:::

In lemma 3 the asymptotics of the maximum value $\tilde{S}_N$ are expressed using the Lobachevski function $\Lambda(\theta) = -\int_0^{\theta}\log|2\sin(x)|dx$.

::: lem
$\tilde{S}_N \sim \exp\left(
\frac{4N}{\pi}\Lambda(\frac{\pi}{4})-\frac{1}{2}\log2N \right), \quad N\to\infty$
:::

The asymptotics of $J_{N,a,1,c,d}$ is reduced to that of $\tilde{S}_N$ by the following lemma. By CS we mean the constant defined in the statement of the main theorem.

::: lem
There is a nonzero constant $C \in \mathbb{C}$ such that: $$J_{N,a,1,c,d}\sim CN^{(c+d+3)/2}\tilde{S}_N^{c+d}e^{\frac{i\mathrm{CS}}{2\pi}},\quad N\to\infty$$
:::

There is a similar lemma for the case $b \geq 2$. We confine ourselves to the odd-colored Jones polynomials, since the even ones are $0$ in $e^{\frac{2\pi
i}{N}}$. In lemma 5 we reduce the asymptotics of the odd colored Jones polynomial to those of the maximal term $\tilde{S}_N$:

::: lem
For $b\geq 2$ and $N$ odd we have: $J_{N,a,b,c,d}\sim$ $$\exp\left(-(c+d)\log\sqrt{2}+(4a+3c-3d)\pi i/4\right) N^{(c+d+2b)/2}\tilde{S}_N^{c+d}e^{\frac{i\mathrm{CS}}{2\pi}}$$
:::

Postponing the proofs of these lemmas to the next subsection we can now prove the main theorem.

::: proof
*Proof.* (of the main theorem) Using an explicit decomposition of the complement into ideal octahedra it can be shown that $\mathrm{Vol}(W_{a,b,c,d}) =
8(c+d)\Lambda(\frac{\pi}{4})$, see [@van; @der; @Veen]. Let us first suppose that $b = 1$. According to lemma 4 there is a constant $C'$ such that we have: $$J_{N,a,1,c,d}\sim
\exp\left(\log(\tilde{S}_N^{c+d})+\frac{c+d+3}{2}\log(N)+Ni\frac{\mathrm{CS}}{2\pi}+
C' \right)$$ Using lemma 3 we get: $$\sim \exp\frac{1}{2\pi}\left((\mathrm{Vol}(W_{a,1,c,d})+i\mathrm{CS})N + 3\pi\log(N)+ E\right),\  N\to\infty$$ The case $b \geq 2$ follows in the same way by combining lemma 3 and lemma 5. ◻
:::
