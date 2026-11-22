---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-022-93-tasep-coulomb-gas-and-random-matrices
section_title: "TASEP, Coulomb gas, and random matrices"
section_number: 9.3
pages: 13-13
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.859
latex_coverage_ratio: 0.988
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
[]{#sec:TASEPRM label="sec:TASEPRM"}

In proving Theorem [\[thm:Johansson\]](#thm:Johansson){reference-type="ref" reference="thm:Johansson"}, Johansson also proved an unexpected connection of TASEP to Coulomb gas and random matrices [@Johansson00]. Consider the probability density function on $\mathbb{R}_+^n$ given by $$\label{eq:Coulomb}
    p(x_1, \cdots, x_n) = c_{n, m} e^{2\sum_{1\le i<j\le n} \log |x_j-x_i|- \sum_{i=1}^n V(x_i) }, 
    \quad V(x)= x-(m-n)\log x,$$ where $c_{m,n}$ is the normalization constant. Let $x_{\max}=\max\{x_1, \cdots, x_n\}$.

Johansson proved that for $m\ge n$, the last passage time $L(m,n)$ of the exponential DLPP has the same distribution as $x_{\max}$. The density function [\[eq:Coulomb\]](#eq:Coulomb){reference-type="eqref" reference="eq:Coulomb"} is said to define a Coulomb gas with potential $V$ on $\mathbb{R}_+$ since the term $\log |x_i-x_j|$ is the 2d Coulomb potential of two equal charges at $x_i$ and $x_j$. The function $V(x)$ represents the confining potential.

Let $X$ be an $n\times m$ random matrix with entries that are independent complex normal variables of mean zero and variance $1/2$. The random matrix $W=XX^*$ is called the complex Wishart matrix, and its eigenvalue density function is precisely [\[eq:Coulomb\]](#eq:Coulomb){reference-type="eqref" reference="eq:Coulomb"} [@Forrester10]. Thus, $L(m,n)$ has the same distribution as the largest eigenvalue of a complex Wishart matrix. See also [@Borodin-Peche08]. The connection of the exponential DLPP to Coulomb gas and the random matrix is special, and we do not expect to hold for general random variables $w_s$.

There are universality results for both Coulomb gas and random matrices. The Tracy-Widom limit theorem is proved for the Coulomb gases with a general potential $V$. The paper [@Deift-Kriecherbauer-McLaughlin-Venakides-Zhou99] showed the limit theorem for generic analytic potentials, and [@Baik-Kriecherbauer-McLaughlin-Miller07] proved for discrete Coulomb gases in which particles are restricted to be only on a discrete set.

Universality is a central question in random matrix theory, and there have been remarkable successes. The largest eigenvalue of a large class of random Hermitian matrices with independent entries converges to the Tracy-Widom distribution [@Soshnikov99; @Tao-Vu10; @Erdos-Knowles-Yau-Yin12; @Lee-Yin14].
