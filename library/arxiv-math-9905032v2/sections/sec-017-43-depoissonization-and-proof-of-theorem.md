---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-017-43-depoissonization-and-proof-of-theorem
section_title: "Depoissonization and proof of Theorem"
section_number: 4.3
pages: 33-35
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.938
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
[]{#s43 label="s43"}

Fix some $m=1,2,\dots$ and denote by $F_n$ the distribution function of $\lambda_1,\dots,\lambda_m$ under the Plancherel measure $M_n$

$$F_n(x_1,\dots,x_m)=M_n\left(\left\{\lambda\,\left|\,
\lambda_i< x_i\,, \  1\le i\le 
m\right.\right\}\right) \,.$$

Also, set

$$F(\theta,x)=e^{-\theta} \sum_{k=0}^\infty\frac {\theta^k}{k!}\, F_k(x).$$

This is the distribution function corresponding to the measure $M^\theta$.

The measures $M_n$ can be obtained as distribution at time $n$ of a certain random growth process of a Young diagram, see e.g. [@VK2]. This implies that

$$F_{n+1}(x)\le F_n(x)\,, \quad x\in\mathbb{R}^m \,.$$

Also, by construction, $F_n$ is monotone in $x$ and similarly

$$\label{e4101}
F(\theta,x) \le F(\theta,y)\,, \quad x_i \le y_i\,, \quad i=1,\dots,m \,.$$

We shall use these monotonicity properties together with the following lemma.

::: lemma
[]{#l48 label="l48"} There exist constants $C>0$ and $n_0>0$ such that for any nonincreasing sequence $\{b_n\}_{n=0}^\infty\subset[0,1]$

$$1\ge b_0\ge b_1\ge b_2\ge b_3\ge\dots\ge 0,$$

and its exponential generating function

$$B(\theta)=e^{-\theta} \sum_{k=0}^\infty\frac {\theta^k}{k!}\cdot b_k$$

we have for all $n>n_0$ the following inequalities:

$$B(n+4\sqrt{n\ln n})-\frac C{n^2}\le b_n\le B(n-4\sqrt{n\ln n})+\frac C{n^2}.$$
:::

This lemma implies that for all $x\in \mathbb{R}^m$

$$\label{e411}
F(n+4\sqrt{n\ln n},x)-\frac C{n^2}\le F_n(x)\le F(n-4\sqrt{n\ln n},x)+\frac 
C{n^2}\,.$$

Set

$$\bar 1=(1,\dots,1)\,.$$

Theorem [\[t4\]](#t4){reference-type="ref" reference="t4"} asserts that

$$\label{e412}
F\left(\theta, 2{\theta}^\frac12\, \bar 1+ \theta^{\frac 16} \, x\right)\to F(x),\quad \theta\to +\infty,\quad x\in 
\mathbb{R}^m,$$

where $F(x)$ is the corresponding distribution function for the Airy ensemble. Note that $F(x)$ is continuous.

Denote $n_\pm=n\pm 4\sqrt{n\ln n}$. Then for $i=1,\dots,m$

$$2n^\frac12_\pm +n^\frac16_\pm\, x_i =2n^\frac12  +n^{\frac 16}\, x_i +O((\ln n)^{1/2}) \,.$$

Hence, for any $\varepsilon>0$ and all sufficiently large $n$ we have

$$2n^\frac12_+ +n_+^{\frac 16} \, (x_i-\varepsilon)
\le
2n^\frac12 +n^{\frac 16}\, x_i 
\le 2n^\frac12_- +n_-^{\frac 16} \, (x_i+\varepsilon) \,,$$

for $i=1,\dots,m$. By [\[e4101\]](#e4101){reference-type="eqref" reference="e4101"} this implies that

$$\begin{aligned}
F\left(n_+,2n^\frac12\,\bar 1+n^{\frac 16}\, x\right)&\ge 
F\left(n_+,2n^\frac12_+\, \bar 1+n_+^{\frac 16} \, \left(x-\varepsilon\, \bar 1\right)\right)\\
F\left(n_-,2n^\frac12\,\bar 1+n^{\frac 16}\, x\right)&\le 
F\left(n_-,2n^\frac12_-\, \bar 1+n_-^{\frac 16} \, \left(x+\varepsilon\, \bar 1\right)\right) \,. 
\end{aligned}$$

From this and [\[e411\]](#e411){reference-type="eqref" reference="e411"} we obtain

$$\begin{gathered}
F\left(n_+,2n^\frac12_+\, \bar 1+n_+^{\frac 16} \, \left(x-\varepsilon\, \bar 1\right)\right)-\frac C{n^2}\\ \le 
F_n\left(2n^\frac12\,\bar 1+n^{\frac 16}\, x \right)\le \\  
F\left(n_-,2n^\frac12_-\, \bar 1+n_-^{\frac 16} \,\left(x+\varepsilon\, \bar 1\right)\right)+\frac C{n^2} \,. 
\end{gathered}$$

From this and [\[e412\]](#e412){reference-type="eqref" reference="e412"} we conclude that

$$F\left(x-\varepsilon\,\bar 1\right)+o(1)\le F_n\left(2n^\frac12\,\bar 1+n^{\frac 16}\, x \right)\le 
F\left(x+\varepsilon\, \bar 1\right)+o(1)$$

as $n\to\infty$. Since $\varepsilon>0$ is arbitrary and $F(x)$ is continuous we obtain

$$F_n \left(2n^\frac12\,\bar 1+n^{\frac 16}\, x \right)\to F(x),\quad n\to \infty, \quad x\in \mathbb{R}^m,$$

which is the statement of Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"}.
