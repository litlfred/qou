---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-031-41-slowly-growing-sequence-of-moments-determines
section_title: "Slowly growing sequence of moments determines the measure"
section_number: 4.1
pages: 29-30
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.952
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
::: lemma
[]{#lem:Carleman label="lem:Carleman"} Assume that $\mu$ is a probability measure which is supported on the interval $[x_0,\infty)$ (respectively, on the interval $(-\infty,x_0]$) for some $x_0\in\mathbb{R}$ and such that $$\label{eq:moments-slow}
    | m_{l} | \leq C^l\ l^{2l}$$ holds true for some constant $C$ and all integers $l\geq 1$, where $$m_l = m_l(\mu) = \int_\mathbb{R}x^l \dif\mu$$ is the $l$-th moment of $\mu$.

Then the measure $\mu$ is uniquely determined by its moments.

Similarly, if the measure $\mu$ is supported on the real line $\mathbb{R}$ and such that $$\label{eq:moments-slow'}
    | m_{l} | \leq C^l\ l^{l}$$ holds true for some constant $C$ and all integers $l\geq 1$, then the measure $\mu$ is uniquely determined by its moments.
:::

::: proof
*Proof.* In the case when $\mu$ is supported on the interval $[0,\infty)$ this is exactly Stieltjes moment problem, while in the case when $\mu$ is supported on the real line $\mathbb{R}$ this is exactly the Hamburger moment problem. It is easy to check that the assumptions [\[eq:moments-slow\]](#eq:moments-slow){reference-type="eqref" reference="eq:moments-slow"}, and [\[eq:moments-slow\'\]](#eq:moments-slow'){reference-type="eqref" reference="eq:moments-slow'"} imply that the Carleman's conditions in both Stieltjes and Hamburger, respectively, problems are satisified and it follows that the measure $\mu$ is uniquely determined by its moments.

Now, assume that $\mu$ is a probability measure which is supported on the interval $[x_0,\infty)$. We define a probability measure $\mu_{x_0}$ supported on the interval $[0,\infty)$, as a translation of $\mu$ that is, for any measurable set $A \subset \mathbb{R}$ we have $$\mu_{x_0}(A) := \mu(A+x_0).$$ Let us compute the moments of $\mu_{x_0}$: $$m_l(\mu_{x_0}) = \int_\mathbb{R}x^l \dif\mu_{x_0} = \int_\mathbb{R}(x-x_0)^l \dif\mu =
    \sum_{k}\binom{l}{k}(-x_0)^{l-k}\int_\mathbb{R}x^k \dif\mu.$$ This leads to the following inequalities: $$\begin{gathered}
 \left|m_l(\mu_{x_0}) \right| \leq \sum_{k}\binom{l}{k}|x_0|^{l-k}\ |m_k|
    \leq \\
    \sum_{k}\binom{l}{k}|x_0|^{l-k}\ C^k\ k^{2k} \leq
    (C+|x_0|)^l\ l^{2l}.
    
\end{gathered}$$

By Carleman's criterion it means that the measure $\mu_{x_0}$ is uniquely determined by its moments, which is equivalent by the construction that the measure $\mu$ is uniquely determined by its moments, too.

The case, when $\mu$ is supported on the interval $(-\infty,x_0]$ is analogous, and we leave it as a simple exercise. ◻
:::
