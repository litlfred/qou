---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-016-35-an-additional-application-the-length-of-the-l
section_title: "An Additional Application: The Length of the Longest Increasing Subsequence of a Random Walk Evolving under the Asymmetric Exclusion Process"
section_number: 3.5
pages: 47-55
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.973
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Consider a random walk X on $\{1,\dots,n\}$. Represent $X$ by some element in $\{0,1\}^n$, where $X_i=0$ corresponds to a step down in the walk at position $i$ and $X_i=1$ corresponds to a step up. We will assume that $$\sum_{i=1}^n X_i =\frac{n}{2}$$ so that we have the same number of up steps as down steps. We can now look at this random walk as the initial configuration of a particle process with $X_i=1$ corresponding to a particle in position $i$ and $X_i=0$ corresponding to no particle at position $i$. Consider the asymmetric exclusion process acting on this configuration with the following dynamics. At each step of the process, a number $i$ is chosen uniformly in $\{1,\dots,n-1\}$. If $X_i=X_{i+1}$, then the configuration stays the same. If $X_i=1$ and $X_{i+1}=0$, then the values of $X_i$ and $X_{i+1}$ switch with probability $1-q/2$ and if $X_i=0$ and $X_{i+1}=1$, then the values switch with probability $q/2$. Viewed in this way, the asymmetric exclusion process can be viewed as a Markov process on the set of random walks. See [@Liggett] for an in depth discussion of the asymmetric exclusion process.

::: thm
The spectral gap of the ASEP is $\lambda_n=1-\Delta^{-1}\cos(\pi/n)$, where $\Delta=\frac{q+q^{-1}}{2}$ for a parameter $q$ satisfying $0<q<1$.
:::

In our case, take $q=1-c/n^{\alpha}$, for a constant $c$, and $0<\alpha<1$, such that $q\approx e^{-c/n^{\alpha}}$. Then Taylor approximating and simplifying gives $$\lambda_n=c^2/2n^{2\alpha}$$ Now let $M_X$ denote the height of the midpoint of the random walk at a fixed time during the process. In other words, $M_X=X_{n/2}$, assuming $n$ is even. Note that the range of this function is $[-n/2,n/2]$. Let $M_x'$ be the evolution of $M_x$ after one step of the process. Notice that $$\|M_x-M_x'\|_{\infty}\leq 1$$ since switching the position of two adjacent particles can change the height of the midpoint by at most $1$. Then $$\||M||_{\infty}^2=\frac{1}{2}\max_{X}\mathbb{E}(M_x-M_x')^2$$ $$\leq \frac{1}{2}(1)^2\left(\frac{1}{n-1}\right)=\frac{1}{2(n-1)}$$ The $\frac{1}{n-1}$ appears because the only choice of $i$ that will effect the midpoint is $i=n/2$.\
\
Now plugging into the Chatterjee Ledoux theorem, we have the following result.

::: thm
Letting $M_X$ denote the height of the midpoint of the random walk after evolution under the asymmetric exclusion process, for all $r>0$ and $q=1-c/n^{\alpha}$, $$\mathbb{P}(|M_X-\mathbb{E}M_X|\geq r)\leq 6\exp\left(-r/2\sqrt{\frac{c^2/2n^{2\alpha}}{1/(2(n-1))}}\right) =6\exp\left(-r/2\sqrt{\frac{c^2(n-1)}{n^{2\alpha}}}\right)$$
:::

Notice that this implies that the height of the midpoint has fluctuations bounded above by a constant $n^{\alpha-1/2}$ for $0<\alpha<1$.

Consider the length of the longest increasing (non-decreasing) subsequence of the random walk. This is defined as $$L_X=\max\{k \;   : \; i_1<i_2<\dots<i_k \; \mathrm{and} \; X_{i_1}\leq X_{i_2}\leq\dots\leq X_{i_k}\}$$ See [@PeresRW] for a more in depth description of this topic and results for the simple random walk.

![A longest increasing subsequence of a random walk](randomwalk.png)

Notice that the height of the midpoint gives a lower bound on the length of the longest increasing subsequence. Using ASEP as our Markov process and the spectral gap above, we can prove concentration of measure for $L_X$. Notice that switching the position of two adjacent particles via ASEP can only change $L_X$ by at most $1$. As before, let $X'$ be the evolution of $X$ after one step of the process. Then, bounding the probability above by $1$, we have $$\||L\||_{\infty}^2=\frac{1}{2}\max_X\mathbb{E}(L_X-L_{X'})^2$$ $$\leq \frac{1}{2} (1)^2=\frac{1}{2}$$ so plugging into the Chatterjee Ledoux formula, we get the following result.

::: thm
Letting $L_X$ denote the length of the longest increasing subsequence of the random walk after evolution under the asymmetric exclusion process, for all $r>0$ and $q=1-c/n^{\alpha}$, $$\mathbb{P}(|L_X-\mathbb{E}L_X|\geq r)\leq 6\exp\left(-r/2\sqrt{\frac{c^2}{n^{2\alpha}}}\right)$$
:::

This implies that the fluctuations are bounded above by a constant times $n^{\alpha}$. In particular, for $q=1-c/\sqrt{n}$, the fluctuations are bounded above by a constant times $\sqrt{n}$.

In order to give some context to the size of the fluctuations, we calculate height of the midpoint, which gives a lower bound on the length of the longest increasing subsequence of the walk under this distribution.

::: thm
[]{#height label="height"} For $q<1-c/n$ and $c=-20\log(3/5)$, the height of the midpoint of the random walk is $kn$ for some constant $k>0$.
:::

Before we give the proof, we will need the following lemma.

::: lem
Consider a random walk with independent steps. Assume that $\mathbb{P}(X_k=0)=\frac{1}{aq^k+1}$ and $\mathbb{P}(X_k=1)=\frac{aq^k}{aq^k+1}$ for some $a>0$, $q\in (0,1)$ and $k\in\mathbb{Z}_{+}$. Consider $N_X=\sum_{i=1}^n X_i$. This gives us the number of up steps in our random walk, or equivalently, the number of particles in our particle process. The fluctuations of $N_X$ are at most order $\sqrt{n}$.
:::

::: proof
*Proof.* We begin by calculating the variance of $N_X$. We can then use Chebyshev's inequality to bound the fluctuations. Since the $X_i$ are independent, $$\mathrm{Var}(N_X)=\sum_{i=1}^n \mathrm{Var}(X_i)$$ Using the probabilities given in the lemma, we know that $$\mathrm{Var}(X_i)=\frac{aq^i}{aq^i+1}-\left (\frac{aq^i}{aq^i+1}\right)^2$$ $$=\frac{aq^i}{aq^i+1}\left (1-\frac{aq^i}{aq^i+1}\right)$$ This gives $$\mathrm{Var}(N_X)=\sum_{i=1}^n\frac{aq^i}{aq^i+1}\left (1-\frac{aq^i}{aq^i+1}\right)$$ A derivative calculation show that $\frac{aq^i}{aq^i+1}\left (1-\frac{aq^i}{aq^i+1}\right)$ is decreasing in $i$, so $$\mathrm{Var}(N_X)\leq n \left(\frac{aq}{aq+1}\right)\left(1-\frac{aq}{aq+1}\right)$$ Since we only care about the order of the fluctuations, we can bound the positive value $$\left(\frac{aq}{aq+1}\right)\left(1-\frac{aq}{aq+1}\right)$$ by $1$, giving us $$\mathrm{Var}(N_X)\leq n$$ Plugging into Chebyshev's inequality tells us that $$\mathbb{P}\left(|N_X-\mathbb{E}(N_X)|\geq k\right)\leq \frac{n}{k^2}$$ which proves our result. ◻
:::

We are now set to prove theorem [\[height\]](#height){reference-type="ref" reference="height"}

::: proof
*Proof.* The basic idea of the proof of theorem [\[height\]](#height){reference-type="ref" reference="height"} is as follows. We will begin by assuming that the steps of our random walk are independent, so that our measure is a product measure. Recall, the steps are not independent, since we are conditioning on the fact that we have exactly $n/2$ steps up and $n/2$ steps down. However, if $n$ is large, the steps are *close* to independent. By bounding the fluctuations of the number of particles in our product system, we can then relate our non-independent state to the product state.

Begin by assuming that $$\frac{P(X_k=0)}{P(X_k=1)}=aq^k$$ so that we have a product measure. Then we know that $$P(X_k=0)=\frac{1}{aq^k+1}$$ and $$P(X_k=1)=\frac{aq^k}{aq^k+1}$$ Then $$\mathbb{E}\left(\sum_{i=1}^k X_i\right)=\sum_{i=1}^k\frac{aq^i}{aq^i+1}$$ Since the summand is decreasing in $i$, we get the bounds $$k\left(\frac{aq^k}{aq^k+1}\right)\leq \mathbb{E}\left(\sum_{i=1}^k  X_i\right)\leq k\left(\frac{aq}{aq+1}\right)$$ We will work in this generality for now, and add in appropriate values of $a$ and $k$ later. Using this information, we can get bounds on the height of the random walk at point $k$. Let $H_k$ be the height of the random walk at position $k$. For convenience later, we will assume that $X_i=1$ corresponds to a step down in the walk, and that $X_i=0$ corresponds to a step up. Provided that we can prove that our height is $cn$ for $c<0$, our theorem will be proved. We have $$\mathbb{E}(H_k)=(-1)\sum_{i=1}^k X_i+\left(k-\sum_{i=1}^k X_i\right)=k-2\left(\sum_{i=1}^k X_i\right)$$ Plugging in our bounds on $\mathbb{E}\left(\sum_{i=1}^k X_i\right)$, we get $$-k\left(2\left(\frac{aq}{aq+1}\right)-1\right)\leq\mathbb{E}(H_k)\leq -k\left(2\left(\frac{aq^k}{aq^k+1}
\right)-1\right)$$

At this point, we need a bound on the number of particles in the system. Since we are assuming the $X_i$ are independent, we can use the result from the previous lemma, which gives us $$\mathbb{P}\left(\left |\sum_{i=1}^n X_i-M\right |>u\right)\leq 4\exp(-u^2/4M)$$ where $M$ is a median for the number of particles. Estimating the median by the expectation of the number of particles, we see that $M$ should at least be close to $n/2\left(\frac{aq}{aq+1}\right)$. If we choose $a$ appropriately corresponding to $q$, we should be able to make the constant order $1$, making our expectation order $n$. Then, by the concentration of measure inequality, $\sum_{i=1}^n X_i$ has fluctuations on the order of $\sqrt{n}$. This is reasonably small compared with the expected number of particles in the system.

Recall that we are actually concerned with finding the height of the midpoint, so plugging in $k=n/2$, we have that $$-n/2\left(2\left(\frac{aq}{aq+1}\right)-1\right)\leq\mathbb{E}(H_{n/2})\leq -n/2\left(2\left(\frac{aq^{n/2}}{aq^{n/2}+1}
\right)-1\right)$$ At this point, we can ignore the lower bound, using the fact that that a lower bound is $-n/2$ anyway, regardless of the configuration. We will refer to our interface as the position in which $\mathbb{P}(X=0)=\mathbb{P}(X=1)$. For now, we will put our interface at $9n/20$, which will be just to the left of the midpoint. In other words, $a=q^{-9n/20}$ and at position $9n/20$, $\mathbb{P}(X=0)=\mathbb{P}(X=1)$. We will push it to the edge at $n/2$ at the end, since moving the interface to the right only increases the probability of more $X_i$ being equal to $1$, hence lowering the expectation of the midpoint. Using this interface, we will first look at the height of the random walk at position $8n/20$. Using the upper bound from above, we have that $$\mathbb{E}(H_{8n/20})\leq \frac{-8n}{20}\left(2\left(\frac{q^{-n/20}}{q^{-n/20}+1}\right)-1\right)$$ Beyond this point, if we assume that all of the remaining steps between $8n/20$ and $n/2$ are steps up, we have that $$\mathbb{E}(H_{n/2})\leq \frac{-8n}{20}\left(2\left(\frac{q^{-n/20}}{q^{-n/20}+1}\right)-1\right) + \frac{2n}{20}$$ The important thing to notice here, is this actually gives us an upper bound on the height of the midpoint in the fixed particle number (ASEP) random walk. In the product state configuration, with our interface at $\frac{9n}{20}$, we know that the fluctuations in the number of down steps are less than $\frac{n}{20}$. By assuming that all steps after site $\frac{8n}{20}$ are up, we have accounted for the worst case scenario where we actually have $\sqrt{n}$ less down steps then we expect. If some of the steps after site $\frac{8n}{20}$ are actually down instead of up, this will only serve to lower the height of our midpoint. Hence, we have, that in the ASEP (fixed number of down steps) random walk generated using the blocking measures, $$\mathbb{E}(H_{n/2})\leq \mathbb{E}(H_{n/2})\leq \frac{-8n}{20}\left(2\left(\frac{q^{-n/20}}{q^{-n/20}+1}\right)-1\right) + \frac{2n}{20}$$ We would like to show that for an appropriate choice of $q$, this is $cn$ for some constant $c<0$. This is true provided that $$\frac{8}{20}\left(2\left(\frac{q^{-n/20}}{q^{-n/20}+1}\right)-1\right)>\frac{2}{20}$$ Solving this inequality gives a condition on q, which is $$q>\left(\frac{3}{5}\right)^{\frac{20}{n}}$$ or $$q>e^{20/n\log(3/5)}$$ Taylor expanding the exponential gives $$q> 1+\frac{20}{n}\log(3/5)+\frac{400}{2n^2}(\log(3/5))^2+\dots$$ As $n\rightarrow\infty$, taking $q>1-\alpha/n$ with $\alpha=-20\log(3/5)$ should be sufficient. As long as this condition is satisfied, our expectation is $cn$ for a constant $c<0$.

At this point, we do want to move the interface to $a=q^{-n/2}$, such that $\mathbb{P}(X_{n/2}=0)=\mathbb{P}(X_{n/2}=1)$. This simply increases our probability of down steps between $\frac{9n}{20}$ and $\frac{n}{2}$. Since adding extra down steps only decreases the expectation of the height of the midpoint, the theorem is proved. ◻
:::
