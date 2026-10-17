---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains"
section_id: sec-005-132-asymptotic-of-the-quantum-invariants-of-the
section_title: "Asymptotic of the quantum invariants of the Whitehead chains"
section_number: 1.3.2
pages: 5-5
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.889
latex_coverage_ratio: 0.93
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by M1 and all"
---
In the second part of this paper, we generalize the previous results on the Whitehead link to the Whitehead chains.

::: theorem
[]{#CJWNN label="CJWNN"} We have $$\begin{aligned}
\lim_{N\to \infty} \frac{2\pi}{N+\frac{1}{2}} \log| J_{\vec{N}} (W_{a,1,c,d}, e^{\frac{2\pi i}{N+\frac{1}{2}}})| 
= \operatorname{Vol}({\mathbb S}^3 \backslash W_{a,1,c,d})
\end{aligned}$$
:::

As a consequence, we can show that

::: corollary
[]{#TVW label="TVW"}For any $a\in {\mathbb Z}$, $b\geq 1$, $c,d \in {\mathbb N}$ with $c+d\geq 1$, Conjectures [\[tvGM\]](#tvGM){reference-type="ref" reference="tvGM"} is true for $TV_r({\mathbb S}^3\backslash W_{a,b,c,d})$.
:::

Moreover, if we colored the belt by $M_1$ and all the clasps by $M_2$ (see Figure [1](#W0120){reference-type="ref" reference="W0120"} for an example), we have the following result.

::: theorem
[]{#mainthmWa1c0 label="mainthmWa1c0"} There exists some $\delta>0$ such that for any $1-\delta < s_1,s_2 < 1$, we have $$\begin{aligned}
&\quad\lim_{N\to \infty} \frac{2\pi}{N+\frac{1}{2}} \log| J_{M_1, M_2} (W_{0,1,c,0}, e^{\frac{2\pi i}{N+\frac{1}{2}}})| \\
&= \operatorname{Vol}({\mathbb S}^3 \backslash W_{0,1,c,0} , u_1=2\pi i (1-s_1), v_2 = v_3 = \dots v_{c+1} = 4\pi i (1 - s_2))
\end{aligned}$$
:::

![the link $W_{0,1,2,0}$ with belt colored by $M_1$ and all other components colored by $M_2$](W1120){#W0120 width="0.65\\linewidth"}

Note that Theorem [\[mainthmWa1c0\]](#mainthmWa1c0){reference-type="ref" reference="mainthmWa1c0"} gives a positive answer to Conjecture [\[GVCHL\]](#GVCHL){reference-type="ref" reference="GVCHL"} for the sequence of colors $(M_1,M_2,\dots,M_2)$ with $s_2=1$.
