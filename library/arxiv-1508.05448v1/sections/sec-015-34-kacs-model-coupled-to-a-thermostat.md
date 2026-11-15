---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-015-34-kacs-model-coupled-to-a-thermostat
section_title: "Kac's Model Coupled to a Thermostat"
section_number: 3.4
pages: 44-47
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.984
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Using a spectral gap result from [@BLV], we are able to demonstrate the application of this method to a more complicated Markov chain. In this system, the particles from Kac's system interact amongst themselves with a rate $\lambda$ and interact with a particle from a thermostat with rate $\mu$. The particles in the thermostat are Gaussian with variance $\frac{1}{\beta}$, so they have already reached equilibrium. The Markov transition operator for Kac's walk is defined as in $(1)$ and the Markov transition operator for the thermostat is given by $$Rf(G)=\frac{1}{n}\sum_{j=1}^n \frac{1}{2\pi}\int_{0}^{2\pi}\int_{\mathbb{R}^n}
 \sqrt{\frac{\beta}{2\pi}}^ne^{-\frac{\beta}{2}\omega_{ij}^{*2}(\theta)}f(V_j(\theta, \omega)G)d\theta d\omega$$ where $\omega=(\omega_1,\omega_2,\dots,\omega_n)$, $V_j(\theta, \omega)$ sends each element $g_{ij}$ in column $j$ to $g_{ij}cos(\theta)+\omega_i\sin(\theta)$ for $i=1$ to $n$ and $\omega_{ij}^*=-g_{ij}\sin(\theta)+\omega_i\cos(\theta)$. In [@BLV], they consider the Markov chain acting on a vector. We consider the Markov chain acting on a matrix by treating the matrix as $n$ independent vectors. Using this adaption, the following theorem follows immediately from the results proved in [@BLV].

::: thm
Kac's walk coupled to a thermostat has unique invariant measure given by $$\nu_n=\prod_{i,j} \sqrt{\frac{\beta}{2\pi}}e^{-\frac{\beta}{2}v_{ij}^2}$$ and has spectral gap $\frac{\mu}{2n}$
:::

For the thermostat alone (letting $\lambda=0$), we can again prove a theorem analogous to Chatterjee and Ledoux's theorem 3.3. Let $\mathcal{G}$ be the set of $n\times n$ matrices with independent and identically distributed $\mathcal{N}(0,1/\beta)$ entries. We can define the Dirichlet form and the triple norm for the thermostat as $$\mathcal{Q}(f,f)=\frac{1}{2n}\sum_{j=1}^n\frac{1}{2\pi}\int_0^{2\pi}\int_{\mathbb{R}^n}\int_{G\in\mathcal{G}}\left(\frac{\beta}{2\pi}\right)^{n/2}e^{-\frac{\beta}{2}w_{ij}^{*2}}(f(V_j(\theta,w))G-f(G))d\nu_ndwd\theta$$ $$|||f|||_\infty^2=\sup_{G\in\mathcal{G}}\; \;\frac{1}{2n}\sum_{j=1}^n\frac{1}{2\pi}\int_0^{2\pi}\int_{\mathbb{R}^n}\left(\frac{\beta}{2\pi}\right)^{n/2}e^{-\frac{\beta}{2}w_j^{*2}}|f(V_j(\theta,w))G-f(G)|^2dwd\theta$$ Using these, we can prove a concentration of measure result for the thermostat analogous to Theorem 3.2.2

::: thm
Consider the Gaussian thermostat and let $F:\mathcal{G}\rightarrow\mathbb{R}$ be such that $|||F|||_\infty\leq 1$. Then $F$ is integrable with respect to $\nu_n$ and for every $r\geq 0$, $$\nu_n(F\geq Fd\nu_n+r)\leq 3e^{-r\sqrt{\lambda_1}/2}$$ where $\lambda_1=\frac{\mu}{2n}$ is the spectral gap of the thermostat process.
:::

We omit the proof here as it is similar to the proof of Theorem 3.2.2.\
\
Using this result and Theorem 3.4.1, we can prove the following concentration of measure inequality.

::: thm
Take any $1\leq k\leq n$ and an $n$-dimensional Hermitian matrix $G$. Let $S$ be an $n\times k$ matrix whose $k$ columns are the first $k$ columns of a random matrix with distribution $\nu_n$. Let $A$ be the $k\times k$ matrix obtained by conjugating $G$ by $S$. Letting $F$ denote the expected spectral distribution of $A$, then for each $r>0$, $$\mathbb{P}(\|F_A-F\|_{\infty}\geq \frac{1}{\sqrt{k}}+r)\leq 12\sqrt{k}\exp\left(-r\sqrt{\frac{k\mu}{108}}\right)$$ where $\mu$ is the rate of the interaction with the thermostat.
:::

::: proof
*Proof.* The proof of this theorem closely follows the proof of Theorem 3.3.1, with appropriate changes made. Let $A$ be stated as above, and let $A'$ be $A$ after one step of the Markov chain. Fix $x\in\mathbb{R}$ and let $f(x)=F_A(x)$, where where $F_A$ is the empirical spectral distribution of $A$. Notice that rank($A-A')\leq 3$, since after one step of the chain, at most 3 columns of $A$ will be changed (two from Kac's Walk, and one from the thermostat). Again using the inequality from [@Bai], we know that $$\|f(A)-f(A')\|_{\infty}\leq\frac{3}{k}$$ $$|||f|||_\infty^2 =\frac{1}{2{n\choose 2}{n}}\sup_A\sum_{1\leq i <j\leq n} \sum_{k=1}^n\mathbb{E}|f(A)-f(A')|^2$$ where the first sum is over possible interactions in Kac's process and the second is over possible particle interactions with the thermostat. The above is $$\leq \frac{1}{2}\left(\frac{3}{k}\right)^2\left(\frac{3k}{n}\right)=\frac{27}{2kn}$$ Using theorems 3.4.1 and 3.4.2, we have that $$\mathbb{P}(|F_A(x)-F(x)|\geq r)\leq 6\exp\left(-\frac{r}{2}\sqrt{\frac{\frac{\mu}{2n}}{\frac{27}{2kn}}}\right)$$ $$=6\exp\left(-\frac{r}{2}\sqrt{\frac{k\mu}{27}}\right)$$ Following the rest of the proof in 3.2.1 (with the appropriate numbers changed), we get $$\mathbb{P}(\|F_A-F\|_{\infty}\geq \frac{1}{\sqrt{k}}+r)\leq 12\sqrt{k}\exp\left(-r\sqrt{\frac{k\mu}{108}}\right)$$ ◻
:::
