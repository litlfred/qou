---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-013-31-proof-of-theorem-26
section_title: "Proof of Theorem 2.6"
section_number: 3.1
pages: 12-14
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.895
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.proof.thm1 label="sub.proof.thm1"}

First, we need to prove that the summation in Equation [\[eq.tau\]](#eq.tau){reference-type="eqref" reference="eq.tau"} is well-defined over the set $(\mathbb Z/k\mathbb Z)^N$. This was observed in [@GZ1] and uses the fact that $\theta^k$ is a solution to the Neumann-Zagier equations.

::: lemma
[]{#lem.periodic label="lem.periodic"}[@GZ1] The summation in Equation [\[eq.tau\]](#eq.tau){reference-type="eqref" reference="eq.tau"} is $k$-periodic.
:::

::: proof
*Proof.* We need to show that $$a_{m+k e_j}(\theta)=a_m(\theta) \,.$$ This follows from the definition of $a_m(\theta)$ given in Equation [\[eq.amth\]](#eq.amth){reference-type="eqref" reference="eq.amth"}, the fact that $z$ is a solution to the Neumann-Zagier equations, and Lemma [\[lem.cyclic\]](#lem.cyclic){reference-type="ref" reference="lem.cyclic"} for the cyclic dilogarithm. ◻
:::

To prove Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}, recall the Galois extension $F_{G,k}/F_k$, and the element $a_m(\theta)$ of $F_{G,k}$. Let $\sigma_j$ denote the $j$-th generator of the Galois group from Equation [\[eq.sigma\]](#eq.sigma){reference-type="eqref" reference="eq.sigma"}, and let $$\epsilon_j(\theta)=a_{e_j}(\theta)^{-1} \,.$$ The next lemma was observed in [@GZ1].

::: lemma
[]{#lem.asigma label="lem.asigma"}[@GZ1] For all $m$ we have: $$\frac{a_{m}(\sigma_j\theta)}{a_{m+e_j}(\theta)} = \epsilon_j(\theta) \,.$$
:::

::: proof
*Proof.* It suffices to show that the left hand side of the above equation is independent of $m$, since the right hand side is the value at $m=0$. To prove this claim, we compute $$\begin{aligned}
\frac{a_{m}(\sigma_j\theta)}{a_{m+e_j}(\theta)} &=
\frac{e^{\pm \pi i \mathbf B^{-1}\nu \cdot m}}{
e^{\pm \pi i \mathbf B^{-1}\nu \cdot (m+e_j)}} \cdot
\frac{\zeta^{\frac12 \left(m^T\mathbf B^{-1}\mathbf A m \pm \mathbf B^{-1}\nu \cdot m\right)}}{
\zeta^{\frac12 \left((m+e_j)^T\mathbf B^{-1}\mathbf A (m+e_j) \pm \mathbf B^{-1}\nu \cdot (m+e_j)\right)}} 
\cdot \\ 
& \quad \prod_{i=1}^N \frac{(\sigma_j \theta_i)^{-(\mathbf B^{-1} \mathbf A m)_i}}{
\theta_i^{-(\mathbf B^{-1} \mathbf A (m+e_j))_i}} \cdot \prod_{i=1}^N
\frac{(\zeta \theta_i^{-1};\zeta )_{m_i+\delta_{i,j}}}{
(\zeta \sigma_j \theta_i^{-1};\zeta )_{m_i}}\,.
\end{aligned}$$ We focus on the $m$-dependent part of each of the 4 fractions. Obviously, $$\frac{e^{\pm \pi i \mathbf B^{-1}\nu \cdot m}}{
e^{\pm \pi i \mathbf B^{-1}\nu \cdot (m+e_j)}} =
\left(\text{term independent of $m$}\right) \,.$$ Next, $$\frac{\zeta^{\frac12 \left(m^T\mathbf B^{-1}\mathbf A m \pm \mathbf B^{-1}\nu 
\cdot m\right)}}{
\zeta^{\frac12 \left((m+e_j)^T\mathbf B^{-1}\mathbf A (m+e_j) \pm \mathbf B^{-1}\nu 
\cdot (m+e_j)\right)}} = \zeta^{-(\mathbf B^{-1}\mathbf A m)_j} \times 
\left(\text{term independent of $m$}\right).$$ Splitting the product of the third fraction to the case when $j \neq i$ and the case when $j=i$ implies that $$\prod_{i=1}^N \frac{(\sigma_j \theta_i)^{-(\mathbf B^{-1} \mathbf A m)_i}}{
\theta_i^{-(\mathbf B^{-1} \mathbf A (m+e_j))_i}} 
= \zeta^{(\mathbf B^{-1}\mathbf A m)_j} \times 
\left(\text{term independent of $m$}\right) \,.$$ Using the identity $$\frac{(\zeta \theta_j^{-1};\zeta)_{m_j+1}}{(\zeta^2 \theta_j^{-1};\zeta)_{m_j}}=
1-\zeta \theta_j^{-1} \,,$$ and splitting the product of the fourth fraction to the case when $j \neq i$ and the case when $j=i$ implies that $$\frac{(\zeta \theta_i^{-1};\zeta )_{m_i+\delta_{i,j}}}{
(\zeta \sigma_j \theta_i^{-1};\zeta )_{m_i}} =
\left(\text{term independent of $m$}\right) \,.$$ This completes the proof of the lemma. ◻
:::

Using the fact that the sum is $m$-periodic it follows that $$\label{eq.fs1}
\sigma_j \left( \sum_{m \in (\mathbb Z/k\mathbb Z)^N} a_m(\theta) \right)= e_j(\theta)
\sum_{m \in (\mathbb Z/k\mathbb Z)^N} a_m(\theta)\,.$$ Suppose that $f(m,\theta)$ is a rational function of $\theta$ with the property that $$\label{eq.fksigma}
f(m,\sigma_j\theta)=f(m+e_j,\theta)$$ for all $j=1,\dots,N$ and all $m$. Then, it follows that for all $m$ we have $$a_m(\sigma_j \theta) f(m,\sigma_j\theta) = \epsilon_j(\theta) a_{m+e_j}(\theta) f(m+e_j,\theta) \,.$$ Summing up, we obtain that $$\label{eq.fs2}
\sigma_j \left( \sum_{m \in (\mathbb Z/k\mathbb Z)^N} a_m(\theta) f(m,\theta) \right)= \epsilon_j(\theta)
\sum_{m \in (\mathbb Z/k\mathbb Z)^N} a_m(\theta) f(m,\theta) \,.$$ Equations [\[eq.fs1\]](#eq.fs1){reference-type="eqref" reference="eq.fs1"} and [\[eq.fs2\]](#eq.fs2){reference-type="eqref" reference="eq.fs2"} and the fact that $F_{G,k}/F_k$ is a Galois extension imply that if $f$ satisfies Equation [\[eq.fksigma\]](#eq.fksigma){reference-type="eqref" reference="eq.fksigma"}, then $\mathrm{Av}(f(-,\theta))\in F_k$.

Now observe that the vertex weights of the Feynman diagrams are $\mathbb Q(\zeta)$-linear combinations of values of the polylogarithm ${\rm Li}_l(\zeta^{m_i+s}\theta_i^{-1})$ for $l <0$. Since the polylogarithm is a rational function, and $\zeta^{m_i}\theta_i^{-1}$ satisfies Equation [\[eq.fksigma\]](#eq.fksigma){reference-type="eqref" reference="eq.fksigma"} for all $i$ and $j$, Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} follows. 0◻
