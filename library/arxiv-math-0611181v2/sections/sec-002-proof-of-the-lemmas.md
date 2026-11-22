---
doc_id: arxiv-math-0611181v2
doc_title: "Proof of the volume conjecture for Whitehead chains"
section_id: sec-002-proof-of-the-lemmas
section_title: "Proof of the lemmas"
section_number: null
pages: 6-13
source_pdf: 0611181v2.pdf
source_sha256: 6931e3ebca584de9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.809
doc_brief: "Proof of the volume conjecture for Whitehead chains — We prove the volume conjecture for an inﬁnite family of links called White- head chains that generalizes both the Whitehead link and the"
---
In this section we prove the more technical lemmas 2,3,4 and 5.

::: proof
*Proof.* (of lemma 2) The proof of this lemma hinges on the following key estimate of $S_{n,k}$ in terms of the Lobachevski function $\Lambda(x)$ that was proved in [@HaoZheng]. Define $f(x,y)=
-2\Lambda(x+y)+2\Lambda(y)+\Lambda(x)$. For integers $0\leq n,k, n+k < N$ we have the uniform estimate $$\log S_{n,k}=\frac{N}{\pi}f(\frac{n\pi}{N},\frac{k\pi}{N})+\mathcal{O}(\log N),\quad N\to \infty$$ Before we can apply this result we first need to show that inside the triangle $0<x,y,x+y<\pi$ the function $f$ has a unique critical point $(\frac{\pi}{2},\frac{\pi}{4})$ and reaches its maximum there, which equals $4\Lambda(\frac{\pi}{4})$. Moreover the Taylor expansion of $f$ around the critical point is: $$f(\frac{\pi}{2}+x,\frac{\pi}{4}+y)=f(\frac{\pi}{2},\frac{\pi}{4})-(x^2+2xy+2y^2)+\mathcal{O}(|x|^3+|y|^3)$$ Lemma 2 part a) and b) are direct consequences of these facts once we note that the difference between $S_{\lfloor
\frac{N}{2}\rfloor,\lfloor \frac{N}{4}\rfloor}$ and the actual critical value $f(\frac{\pi}{2},\frac{\pi}{4})$ becomes negligibly small as $N$ grows.

To find the critical points of $f$ in $0<x,y,x+y<\pi$ we use the fundamental theorem of calculus to differentiate $\Lambda$ and find the system of equations: $2\sin^2(x+y)=\sin(x)$ and $\sin(x+y)=\sin(y)$. For $0<x,y,x+y<\pi$ this has the unique solution $(x,y)=(\frac{\pi}{2},\frac{\pi}{4})$. To determine the nature of the critical point we differentiate again and this will be left to the reader.

The value of $f$ at its critical point is $f(\frac{\pi}{2},\frac{\pi}{4})=-2\Lambda(\frac{3}{4}\pi)+2\Lambda(\frac{\pi}{4})+\Lambda(\frac{\pi}{2})=4\Lambda(\frac{\pi}{4})$ because $\Lambda(x)=-\Lambda(\pi-x)$. ◻
:::

The next lemma is an expanded version of a result proven in [@HaoZheng].

::: proof
*Proof.* (of lemma 3) If we define $s_n = -\sum_{j=1}^n \log|2\sin(j\pi/N)|$ then we can write $\log \tilde{S}_N = -2s_{\left\lfloor N/4 \right\rfloor + \left\lfloor N/2 \right\rfloor}+2s_{\left\lfloor N/4 \right\rfloor}+s_{\left\lfloor N/2 \right\rfloor}$. It was shown in [@HaoZheng] that for $0<n<\frac{5}{6}N$ we have $s_n = \frac{N}{\pi}\Lambda(\frac{n\pi}{N})-\frac{1}{2}\log n + \mathcal{O}(1)$, as $N\to \infty$. To prove the lemma we need to expand a little further. Assuming that $r = \lim_{N\to\infty}n/N$ exists, we show that $$s_n = \frac{N}{\pi}\Lambda(\frac{n\pi}{N})-\frac{1}{2}\log \frac{n\sin(r\pi)}{r\pi} + \mathcal{O}(N^{-1}), \quad N\to \infty$$ By applying the above expansion for $s_n$ three times we then find the desired expansion for $\tilde{S}_N$.

To prove the expansion for $s_n$ we reason as follows: for $x\in [0,\frac{5}{6}\pi]-\{0,u\}$ we have $$\frac{\sin(x-u)}{x-u} \frac{x}{\sin x} = 1+\frac{-x\cos x +\sin x}{x\sin x}u + \mathcal{O}(u^2), \quad u \to 0$$ Now taking the logarithm and expanding $\log(1+f)$ around $f = 0$ we find: $$\log|\frac{\sin(x-u)}{\sin x}| = \log|\frac{x-u}{x}| +\frac{-x\cos x +\sin x}{x\sin x}u + \mathcal{O}(u^2)$$ Following [@HaoZheng] p.7 we set $x = j\pi/N$ and find: $$s_n - \frac{N}{\pi}\Lambda(\frac{n\pi}{N})= \sum_{j=1}^n \frac{N}{\pi}\int_{0}^{\frac{\pi}{N}}\log\frac{\sin(j\pi/N-u)}{\sin j\pi/N}du =$$ $$-\frac{1}{2}\log n - \frac{1}{2}\log 2\pi + \sum_{j=1}^n \frac{N}{\pi}\int_{0}^{\frac{\pi}{N}}\frac{-(j\pi/N)\cos(j\pi/N) +\sin j\pi/N}{j\pi/N\sin j\pi/N}u du +\mathcal{O}(N^{-1})$$ The term $-\frac{1}{2}\log 2\pi$ is the constant contribution of the Sterling series used in [@HaoZheng] p.7. After integration with respect to $u$ we can write the above sum as a Riemann sum. A computation then shows that the limit of this sum equals $\frac{1}{2}(\log r\pi-\log\sin r\pi)$. ◻
:::

Although the proof of lemma 4 below is quite long the main idea is simple: Use lemma 2 to estimate the value of the colored Jones polynomial in terms of the maximum value $\tilde{S}_N$.

::: proof
*Proof.* (of lemma 4) For convenience we will assume throughout the proof that $c+d \geq 2$, so that the value of CS is $\frac{-4a-7c+7d}{8}2\pi^2$. The proof in the case $c+d =1$ is completely analogous. According to lemma 1 the formula for the N-colored Jones polynomial of the one-belted Whitehead chain is $$J_{N,a,1,c,d} =  \phi_N\sum_{n=0}^{N-1}(2n+1)\chi_{N,n}^{4a-c+d}\left(\sum_{k=0}^{N-1-n} S_{n,k}\right)^{c+d}$$ Define the quotient $Q_N =
J_{N,a,1,c,d}N^{-(c+d+3)/2}\tilde{S}_N^{-(c+d)}e^{\frac{4a+7c-7d}{8}N\pi
i}$. We aim to show that $Q_\infty = \lim_{N\to\infty}Q_N = C$ for some nonzero complex constant.

**Step 1:** By expanding the $c+d$-th power of the sum we obtain a multi-sum over all N-tuples of natural numbers $n,\mathbf{k}<N$ such that $n+k_j<N$. Define Central to be the set of all such tuples that satisfy $n+ \mathrm{max}\ k_j < N^\delta$ and define Far to be the set of tuples such that $n+ \mathrm{max}\
k_j \geq N^\delta$. We can then rewrite $Q_N$ as follows: $$Q_N=\phi_N e^{\frac{4a+7c-7d}{8}N\pi i} N^{-(c+d+3)/2}\sum_{\mathrm{Central}}(2n+1)\chi_{N,n}^{4a-c+d}S_{n,k_1}\cdots S_{n,k_{c+d}}\tilde{S}_N^{-(c+d)}$$ $$+\phi_N e^{\frac{4a+7c-7d}{8}N\pi i} N^{-(c+d+3)/2}\sum_{\mathrm{Far}}(2n+1)\chi_{N,n}^{4a-c+d}S_{n,k_1}\cdots S_{n,k_{c+d}}\tilde{S}_N^{-(c+d)}$$ The Far sum converges to zero absolutely, because each tuple $n,\mathbf{k}$ in the sum contains a $k_m$ such that $n+k_m\geq
N^\delta$. According to lemma 2b this means that $S_{n,k_m}\tilde{S}_N^{-1}=\mathcal{O}(\exp(-\epsilon
N^{2\delta-1}))$. We can estimate all other factors $S_{n,k_j}\tilde{S}_N^{-1}$ by a constant and conclude that the sum of absolute values of the Far sum converges to zero since $\delta > 1/2$. So far we have shown that $Q_\infty=$ $$\lim_{N\to\infty} \phi_N e^{\frac{4a+7c-7d}{8}N\pi i} N^{-\frac{c+d+3}{2}}\sum_{\mathrm{Central}}(2n+1)\chi_{N,n}^{4a-c+d}S_{n,k_1}\cdots S_{n,k_{c+d}}\tilde{S}_N^{-(c+d)}$$

**Step 2:** In the next step we replace the factor $(2n+1)$ in the expression for $Q_\infty$ by a factor $N$. This is done by showing that the difference converges to zero. The absolute value of the difference is less than $$N^{-(c+d+3)/2}\sum_{\mathrm{Central}}|2n+1-N|S_{n,k_1}\cdots
S_{n,k_{c+d}}\tilde{S}_N^{-(c+d)}$$ For central tuples $n,\mathbf{k}$ we have $n'<N^\delta$ and hence $2n+1=N+\mathcal{O}(N^\delta)$. The number of terms in the sum is of order $\mathcal{O}(N^{(c+d+1)\delta})$ and the product $S_{n,k_1}\cdots S_{n,k_{c+d}}\tilde{S}_N^{-(c+d)}$ is $\mathcal{O}(1)$ by lemma 2a. Therefore the absolute value of the difference is at most of order $\mathcal{O}(N^{-(c+d+3)/2+(c+d+2)\delta})$. Since $\delta <
\frac{c+d+5}{2(c+d+4)}<\frac{c+d+3}{2(c+d+2)}$ the difference converges to zero and we have: $$Q_\infty= \lim_{N\to\infty}\phi_N
e^{\frac{4a+7c-7d}{8}N\pi i}
N^{-(c+d+1)/2}\sum_{\mathrm{Central}}\chi_{N,n}^{4a-c+d}S_{n,k_1}\cdots
S_{n,k_{c+d}}\tilde{S}_N^{-(c+d)}$$

**Step 3:** Define the $(c+d+1)$-variable Gaussian function $$g_N(x,\mathbf{y}) = \exp-\frac{\pi}{N}\left(( c+d
-(4a+c-d)i)\frac{x^2}{2}+2\sum_{j=1}^{c+d}(y_j+\frac{x}{2})^2\right)$$ and let $\psi = \exp(\frac{4a+3c-3d}{4}\pi i)$. We will show that $$Q_\infty  = \lim_{N \to \infty}\psi
N^{-(c+d+1)/2}\sum_{\mathrm{Central}}g_N(n',\mathbf{k'})$$ Starting with the sum from step 2 we use lemma 2 to replace the factors $S_{n,k_j}\tilde{S}^{-1}$ by exponentials and error terms: $$\lim_{N\to\infty}\phi_N e^{\frac{4a+7c-7d}{8}N\pi i} N^{-(c+d+1)/2}\sum_{\mathrm{Central}}\chi_{N,n}^{4a-c+d}\cdot$$ $$\prod_{j=1}^{c+d}\left(\exp(-\frac{\pi}{N}(n'^2+2n'k_j' + 2k_j'^2))+\mathcal{O}(N^{3\delta-2})\right)$$ To show that the error terms can be removed we estimate the contribution of their absolute values. There are $\mathcal{O}(N^{(c+d+1)\delta})$ terms in the sum so their contribution is of order $\mathcal{O}(N^{(c+d+1)\delta+3\delta-2-(c+d+1)/2})$. This converges to zero because $\delta <\frac{c+d+5}{2(c+d+4)}$. Next we look at the phase factors $\phi_N$ and $\chi_{N,n}$. We have $\lim_{N\to \infty}\phi_N =e^{(c-d)\pi i}$. Furthermore: $$\chi_{N,n}e^{\frac{N\pi i}{8}} =
\exp(\frac{n'^2}{2N}-\frac{N}{8}+\frac{n}{2N}+\frac{N}{8})\pi i =
\exp(\frac{n'^2}{2N}\pi i) \exp(\frac{n}{2N}\pi i)$$ Since $n=\frac{N}{2}+\mathcal{O}(N^\delta)$ we have $\lim_{N\to\infty}\frac{n}{2N} = \frac{1}{4}$. If we apply this to the above sum we get the desired expression.

**Step 4:** It seems natural to replace the previous sum by an integral, this is done in step 4. We will show that $$Q_\infty = \lim_{N \to \infty}\psi N^{-(c+d+1)/2}\int_{|x|+
\mathrm{max}|y_j|<N^\delta-1}g_N(|x|,\mathbf{|y|})\mathrm{d}x\mathrm{d}\mathbf{y}$$ The strategy is to estimate the absolute value of the difference between sum and integral. First we write the sum from step 3 as follows: $$Q_\infty=\lim_{N\to\infty}\psi N^{-(c+d+1)/2}\sum_{\mathrm{Central}}\int_{B(n,\mathbf{k})}g_N(n',\mathbf{k'})\mathrm{d}x\mathrm{d}\mathbf{y}$$ where $B(n,\mathbf{k})=[n-\frac{N}{2}-\frac{1}{2},n-\frac{N}{2}+\frac{1}{2})\times\prod_{j = 1}^{c+d}[k_j-\frac{N}{4}-\frac{1}{2},k_j-\frac{N}{4}+\frac{1}{2})$. The absolute value of the difference between the sum and the proposed integral above is: $$N^{-(c+d+1)/2}|\sum_{\mathrm{central}}\int_{B(n,\mathbf{k})}g_N(n',\mathbf{k'})\mathrm{d}x\mathrm{d}\mathbf{y}-\int_{|x|+ \mathrm{max}|y_j|<N^\delta-1}g_N(|x|,\mathbf{|y|})\mathrm{d}x\mathrm{d}\mathbf{y}|$$ The union of the disjoint blocks $B(n,\mathbf{k})$ as $n,\mathbf{k}$ runs through Central, covers the entire integration domain $|x|+ \mathrm{max}|y_j|<N^\delta-1$ so we can subtract the integrals. However some blocks continue over the boundary of the domain of integration, resulting in a slight error. The terms $n,\mathbf{k}$ such that the corresponding blocks $B(n,\mathbf{k})$ intersect the complement of the domain will be called Border terms. We can estimate the above quantity as follows: $$<
N^{-(c+d+1)/2}\sum_{\mathrm{Central}}\int_{B(n,\mathbf{k})}|g_N(n',\mathbf{k'})-g_N(|x|,\mathbf{|y|})|\mathrm{d}x\mathrm{d}\mathbf{y}$$ $$+N^{-(c+d+1)/2}\sum_{\mathrm{Border}}|g_N(n',\mathbf{k'})|$$ Both sums will be shown to converge to zero, we start with the second one. Since the number of terms on the Border of the integration domain is $\mathcal{O}(N^{(c+d)\delta})$ and $g_N(n',\mathbf{k'})= \mathcal{O}(1)$ the second sum is of order $\mathcal{O}(N^{-(c+d+1)/2+(c+d)\delta})$. This implies that the sum converges to zero because $\delta<\frac{c+d+5}{2(c+d+4)}<\frac{c+d+1}{2(c+d)}$.For the first sum we need to estimate the integrands: $$|g_N(n',\mathbf{k'})-g_N(|x|,\mathbf{|y|})|=|g_N(n',\mathbf{k'})||1-$$ $$\exp\frac{-\pi}{N}\left((c+d -(4a+c-d)i)\frac{|x|^2-n'^2}{2}+2\sum_{j=1}^{c+d}(|y_j|+\frac{|x|}{2})^2-(k_j'+\frac{n'}{2})^2\right)|$$ The last expression is of order $\mathcal{O}(N^{\delta-1})$ because $|g_N(n',\mathbf{k'})|=\mathcal{O}(1)$ and $|x|^2-n'^2 = (|x|+n')(|x|-n')$ and $(|y_j|+\frac{|x|}{2})^2-(k_j'+\frac{n'}{2})^2 = (|y_j|+\frac{|x|}{2}+k_j'+\frac{n'}{2})(|y_j|+\frac{|x|}{2}-k_j'-\frac{n'}{2})$. We integrate over $B(n,\mathbf{k})$ so $|n'-|x||<1$ and $|k_j'-|y_j||<1$ and all terms are central so $|x|+n'<N^\delta$ and $k_j'+|y_j|<N^\delta$. Therefore the second sum is of order $\mathcal{O}(N^{-(c+d+1)/2+\delta-1+(c+d+1)\delta})$ and thus converges to zero, because $\delta<\frac{c+d+5}{2(c+d+4)}<\frac{c+d+3}{2(c+d+2)}$.

**Step 5:** We make the substitution $x=\sqrt{N}w$ and $y_j = \sqrt{N}z_j$ with Jacobian $N^{(c+d+1)/2}$. This gives: $$Q_\infty = \lim_{M \to \infty}\psi
\int_{w+\mathrm{max}|z_j|<\frac{(N^\delta-1)}{\sqrt{N}}}$$ $$\exp(-\pi\left(( c+d
-(4a+c-d)i)\frac{|w|^2}{2}+2\sum_{j=1}^{c+d}(|z_j|+\frac{|x|}{2})^2\right))\mathrm{d}w\mathrm{d}\mathbf{z}$$ Now $\delta>\frac{1}{2}$ and the integrand is rapidly decreasing so the limit exists and is equal to: $$\psi \int_{\mathbb{R}^{c+d+1}}\exp(-\pi\left(( c+d -(4a+c-d)i)\frac{|w|^2}{2}+2\sum_{j=1}^{c+d}(|z_j|+\frac{|w|}{2})^2\right))\mathrm{d}w\mathrm{d}\mathbf{z}$$

**Step 6:** In this final step we need to show that $Q_\infty \neq 0$. We know that $\psi \neq 0$, but what about the complicated Gaussian integral above? We can write it as an iterated integral and get rid of the absolute value signs by integrating $2^{c+d+1}$ times over the positive hyper-quadrant $w,z_j>0$: $$Q_\infty= \psi 2^{c+d+1}\int_{0}^\infty\exp(-\pi( c+d
-(4a+c-d)i)\frac{w^2}{2})\mathrm{d}w\ \cdot$$ $$\prod_{j=1}^{c+d}\int_{0}^\infty\exp(-2\pi(z_j+\frac{w}{2})^2))\mathrm{d}z_j\mathrm{d}w$$ Using the substitutions $y_j = \sqrt{2\pi}(z_j+\frac{w}{2})$ we get the integral below. We only want to check that the integral is nonzero so all constants in front of the integral and the Jacobian are written as $C$. $$Q_\infty= C\int_{0}^\infty\exp(-\pi( c+d
-(4a+c-d)i)\frac{w^2}{2})\cdot\prod_{j=1}^{c+d}\int_{\frac{\sqrt{\pi}w}{\sqrt{2}}}^\infty\exp(-y_j^2)\mathrm{d}y_j\mathrm{d}w$$ If we define the complementary error function by $\mathrm{erfc}(x)
= \frac{2}{\sqrt{\pi}}\int_{x}^\infty \exp(-y^2)\mathrm{d}y$, then we can write the integral more concisely as: $$Q_\infty= C\int_{0}^\infty\exp(-\pi( c+d -(4a+c-d)i)\frac{w^2}{2})\mathrm{erfc}^{c+d}\left(\frac{\sqrt{\pi}w}{\sqrt{2}}\right)\mathrm{d}w =$$ $$C\int_{0}^\infty\exp(-\pi(c+d)\frac{w^2}{2})\mathrm{erfc}^{c+d}\left(\frac{\sqrt{\pi}w}{\sqrt{2}}\right)\cdot$$ $$\left(\cos(\frac{4a+c-d}{2}\pi w^2) + i\sin(\frac{4a+c-d}{2}\pi w^2)\right)\mathrm{d}w$$ After the substitution $x = \sqrt{\frac{4a+c-d}{2}}w$ we note that the imaginary part of integral is nonzero, because both the exponential function and the complementary error function are bounded and decrease monotonically and the decrease is quite rapid. Therefore the integral over the part where the sine is positive dominates the integral over its complement, showing that the integral is a positive scalar multiple of $C$. ◻
:::

The same proof also works for lemma 5 but in this case it is much easier because the value of $n$ is fixed at the maximum. The Gaussian integral at the end of step 5 is now a standard Gaussian integral so that the constant in front of lemma 5 can be computed easily.
