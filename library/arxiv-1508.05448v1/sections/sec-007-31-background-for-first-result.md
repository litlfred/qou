---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-007-31-background-for-first-result
section_title: "Background for First Result"
section_number: 3.1
pages: 36-41
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.989
doc_brief: "Concentration of Measure Techniques and Applications — 25 sections: Front matter; Biographical Sketch; Acknowledgments"
---
In a recent work of Chatterjee and Ledoux on concentration of measure for random submatrices [@ChatLed], it is proved that for an arbitrary Hermitian matrix of order $n$ and $k\leq n$ sufficiently large, the distribution of eigenvalues is almost the same for any principal submatrix of order $k$. Their proof uses the random transposition walk on the symmetric group $S_n$ and concentration of measure techniques. To further generalize their results, we observe that it is important to use a Markov chain which does not change too many matrix entries all at once and whose spectral gap is known. Instead of looking at a Markov chain on $S_n$, we first consider a Markov chain on the special orthogonal group $SO(n)$. $SO(n)$ is the group of $n\times n$ orthogonal matrices with determinant $1$. As a linear transformation, every element of $SO(n)$ is a rotation and preserves distances. We introduce Kac's walk on $SO(n)$ and demonstrate that it is sufficiently similar to the transposition Markov chain to allow for Chatterjee and Ledoux's results to carry over to the more general case of operator compressions. It should be noted that a similar result has been proved by Meckes and Meckes [@MeckesMeckes] using different techniques. In a more recent work [@MeckesMeckes2], Meckes and Meckes have extended their techniques to include several other classes of random matrices and prove almost sure convergence of the empirical spectral measure. The purpose of this paper is to highlight the fact that the methods of Chatterjee and Ledoux can be extended to include more general cases, provided the Markov chain used satisfies appropriate conditions. To emphasize this point, we also apply the method to get a concentration of measure result for a compression by a matrix of Gaussians using Kac's walk coupled to a thermostat. We also show an application of this method applied to the length of the longest increasing subsequence of a random walk evolving under the asymmetric exclusion process. The results of this section can be found in [@SNandMW].\
\
Following the notation of Chatterjee and Ledoux, for a given Hermitian matrix $A$ of order $n$, with eigenvalues given by $\lambda_1,\dots,\lambda_n$, we let $F_A$ denote the empirical spectral distribution function of $A$. This is defined as $$F_A(x):=\frac{\#\{i:\lambda_i\leq x\}}{n}$$

# Kac's Walk on $SO(n)$

The following model, introduced by Kac [@Kac], describes a system of particles evolving under a random collision mechanism such that the total energy of the system is conserved. Given a system of $n$ particles in one dimension, the state of the system is specified by $\vec{v}=(v_1,\dots v_n)$, the velocities of the particles. At a time step $t$, $i$ and $j$ are chosen uniformly at random from $\{1,\dots, n\}$ and $\theta$ is chosen uniformly at random on $(-\pi, \pi]$. The $i$ and $j$ correspond to a collision between particles $i$ and $j$ such that the energy, $$E=\sum_{k=1}^n v_k^2$$ is conserved. Under this constraint, after a collision, the new velocities will be of the form $v_i^{\mathrm{new}}=v_i\cos(\theta)+v_j\sin(\theta)$ and $v_j^{\mathrm{new}}=v_j\cos(\theta)-v_i\sin(\theta)$. For $i<j$, let $R_{ij}(\theta)$ be the rotation matrix given by: $$R_{ij} (\theta) = \begin{pmatrix} I & & & & \\
        &\cos(\theta) &&\sin(\theta)& \\
        &&I&& \\
        &-\sin(\theta) &&\cos(\theta)& \\
        &&&& I \end{pmatrix}$$ where the $\cos(\theta)$ and $\sin(\theta)$ terms are in the rows and columns labeled $i$ and $j$, and the $I$ denote identity matrices of different sizes (possibly 0). We will use the convention that $R_{ii}{\theta}=I$. After one step of the process, $\vec{v}_{new}=R_{ij}(\theta)\vec{v}$.

In our case, we will be considering this process acting on $SO(n)$, so instead of vectors in $\mathbb{R}^n$, our states will be given by matrices $G\in SO(n)$. Then we can define the one-step Markov transition operator for Kac's walk, $Q$, on continuous functions of $SO(n)$: $$Qf(G) = \frac{1}{\binom{n}{2}} \sum_{i<j} \int_0^{2\pi} f(R_{ij}(\theta)G)\frac{1}{2\pi} d\theta$$ for any $G\in SO(n)$, and where $f$ is a continuous function on $SO(n)$. Notice that this is a slightly different setup than we introduced in Chapter 2. Instead of a finite state space Markov chain, we now have an infinite state space. We will pause to discuss the differences between our previous case and this case. Since our state space is infinite, we cannot define our transition probabilities using finite dimensional matrices. We instead define a Markov transition operator on continuous functions of our space. In the context of our earlier discussion from before, $$Qf(G)=\mathbb{E}(f(X_1)\; | \; X_0=G)$$ In other words, $Qf(G)$ gives us the expected value after one step of the chain, conditioned on the fact that we start at $G\in SO(n)$. It turns out that this fully specifies our Markov chain. In order to generalize the methods of Chatterjee and Ledoux to this case, we need to know the invariant distribution and the spectral gap of Kac's walk. This is given in the following result.

::: thm
Kac's walk on $SO(n)$ is ergodic and its invariant distribution is the uniform distribution on $SO(n)$. Furthermore, the spectral gap of Kac's walk on $SO(n)$ is $\frac{n+2}{2(n-1)n}$.
:::

Using our Markov transition operator, we can define the Dirichlet form, $\mathcal{Q}\left(\cdot,\cdot \right)$. As discussed in chapter 2, it is well known that for a Markov chain with spectral gap, $\lambda_1$, the Poincare inequality holds: $$\lambda_1 \mathrm{Var}(f) \leq \mathcal{Q}\left(f,f \right).$$ For the Kac's walk, we have $$\mathcal{Q}\left(f,f \right) = \frac 1 {2\binom{n}{2}} \sum_{1 \leq i<j\leq n} \int_0^{2\pi} \frac{1}{2\pi} \int_{SO(n)} \left(f(G) - f(R_{ij}(\theta)G)\right)^2 d\mu_n(G) d\theta,$$ where $\mu_n$ is the Haar measure on $SO(n)$ normalized so that the total measure is $1$.

Let us define the triple norm: $$|||f|||_\infty^2 = \frac 1 {2\binom{n}{2}} \sup_{G\in SO(n)}\sum_{1 \leq i<j\leq n} \int_0^{2\pi} \frac{1}{2\pi} \left|f(G) - f(R_{ij}(\theta)G)\right|^2 d\theta.$$ The following result is analogous to Theorem 3.3 from Ledoux's Concentration of Measure Phenomenon book [@LedouxCOM] (discussed and proved in chapter 2) . We reproduce the proof of the theorem here to verify that even though our situation does not satisfy the conditions of the theorem, the exact same argument carries through for Kac's walk on $SO(n)$. We omit some details here as they are the same as the argument in chapter 2.

::: thm
Consider Kac's walk on $SO(n)$, and let $F:SO(n)\to \mathbb{R}$ be given such that $|||F|||_\infty\leq 1$. Then, $F$ is integrable with respect to $\mu_n$, and for every $r\geq 0$, $$\mu_n\left (F \geq \int F d\mu_n + r\right) \leq 3 e^{-r\sqrt{\lambda_1}/2}$$ where $\lambda_1= \frac{n+2}{2(n-1)n}$ is the spectral gap of Kac's walk on $SO(n)$.
:::

::: proof
*Proof.* We first demonstrate that $\mathcal{Q}\left(e^{\lambda F/2},e^{\lambda F/2} \right))\leq \frac{\lambda^2 |||F|||_\infty^2}{4} \int_{SO(n)} e^{\lambda F(G)} d\mu_n(G)$ by using symmetry (see chapter 2 for details). $$\begin{aligned}
        \mathcal{Q}\left(e^{\lambda F/2},e^{\lambda F/2} \right) &= \frac 1 {2\binom{n}{2}} \sum_{1 \leq i<j\leq n} \int_0^{2\pi} \frac{1}{2\pi} \int_{SO(n)} \left(e^{\lambda F(G)} - e^{\lambda F(R_{ij}(\theta)G)}\right)^2 d\mu_n(G) d\theta \\
        & =  \frac 1 {\binom{n}{2}} \sum_{1 \leq i<j\leq n} \int_0^{2\pi} \frac{1}{2\pi} \int_{F(G)>F(R_{ij}(\theta)G)} \left(e^{\lambda F(G)} - e^{\lambda F(R_{ij}(\theta)G)}\right)^2 d\mu_n(G) d\theta \\
        & \leq \frac{\lambda^2}{4} \frac 1 {2 \binom{n}{2}} \sum_{1 \leq i<j\leq n} \int_0^{2\pi} \frac{1}{2\pi} \int_{SO(n)} \left(F(G) - F(R_{ij}(\theta)G)\right)^2 e^{\lambda F(G)} d\mu_n(G) d\theta \\
        & = \frac{\lambda^2}{4} |||F|||_\infty^2 \int_{SO(n)} e^{\lambda F(G)} d\mu_n(G)
    
\end{aligned}$$ Setting $\Lambda(\lambda) = \int_{SO(n)} e^{\lambda F(G)} d\mu_n(G)$, we combine this with the Poincare inequality to obtain $$\lambda_1 \mathrm{Var}(e^{\lambda F/2}) = \lambda_1 \left(\Lambda(\lambda)-\Lambda^2\left(\frac{\lambda}2\right)\right) \leq \mathcal{Q}\left(e^{\lambda F/2},e^{\lambda F/2} \right) \leq \frac{\lambda^2}{4} |||F|||_\infty^2 \Lambda(\lambda).$$ Incorporating the assumption $|||F|||_\infty\leq1$ yields $$\Lambda(\lambda) \leq \frac{1}{1-\frac{\lambda^2}{4\lambda_1}} \Lambda^2(\lambda/2).$$ Iterating the inequality $n$ times gives $$\Lambda(\lambda) \leq \prod_{k=0}^{n-1} \left(\frac{1}{1-\frac{\lambda^2}{4^{k+1}\lambda_1}}\right)^{2^k} \Lambda^{2^n}(\lambda/2^n).$$ Since $\Lambda(\lambda) = 1+ o(\lambda)$, we see that $\Lambda^{2^n}(\lambda/2^n) \to 1$ as $n\to \infty$. This gives the upper bound $$\Lambda(\lambda)\leq \prod_{k=0}^\infty \left(\frac{1}{1-\frac{\lambda^2}{4^{k+1}\lambda_1}}\right)^{2^k}.$$ By plugging in $\lambda=\sqrt{\lambda_1}$, using the crude estimate $\prod_{k=0}^\infty \left(\frac{1}{1-\frac{1}{4^{k+1}}}\right)^{2^k} < 3$, and applying Chebyshev's inequality (similarly to as in chapter 2), we obtain the result. ◻
:::
