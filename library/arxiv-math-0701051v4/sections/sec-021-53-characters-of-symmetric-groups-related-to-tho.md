---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-021-53-characters-of-symmetric-groups-related-to-tho
section_title: "Characters of symmetric groups related to Thoma characters"
section_number: 5.3
pages: 17-19
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.628
latex_coverage_ratio: 0.968
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
Vershik and Kerov [@VershikKerov1981] proved that if $\pi$ is a fixed permutation with the lengths of non-trivial cycles $k_1,\dots,k_r$ then for any Young diagram $\lambda$ with $n$ boxes

$$\chi^{\lambda}(\pi) =
\prod_{i=1}^r \left[ \sum_j
\alpha_j^{k_i} - \sum_j (-\beta_{j})^{k_i} \right] + O\left(\frac{1}{n}\right)$$

where $\alpha_j=\frac{\lambda_j}{n}$, $\beta_j=\frac{\lambda'_j}{n}$; we prefer to write this formula in an equivalent form $$\label{eq:vershik-kerov2}
\chi^{\lambda}(\pi) = \frac{n^l}{(n)_l}
\prod_{i=1}^r \left[ \sum_j
\alpha_j^{k_i} - \sum_j (-\beta_{j})^{k_i} \right] + O\left(\frac{1}{n}\right).$$

In this section we will prove Theorem [\[theo:estimate-free\]](#theo:estimate-free){reference-type="ref" reference="theo:estimate-free"} which together with Theorem [\[theo:equiv-cumulants\]](#theo:equiv-cumulants){reference-type="ref" reference="theo:equiv-cumulants"} give a uniform estimate for the error term in the formula [\[eq:vershik-kerov2\]](#eq:vershik-kerov2){reference-type="eqref" reference="eq:vershik-kerov2"}. In particular, for $A=n$ and $\varepsilon = \frac{D}{n}$ we recover the result of Vershik and Kerov.

::: theorem
[]{#theo:estimate-free label="theo:estimate-free"} There exist constants $a,C>0$ with the following property. Let $k_1,\dots,k_r$ be positive integers; we denote $k_1+\ldots+k_r=l$. If $\lambda$ is a Young diagram having $n$ boxes with less than $A$ rows and columns and such that $\varepsilon=\frac{(k_1^2+\cdots+k_r^2) n}{A^2} < C$ then $$\label{eq:freecumulants-estimate}
\left| \frac{\prod_{i=1}^r R_{k_i+1}(\lambda)}{n^l} - \prod_{i=1}^r \left[
\sum_j
\alpha_j^{k_i} - \sum_j (-\beta_{j})^{k_i} \right] \right|
\leq  \varepsilon \left(\frac{A}{n}\right)^{l-r} a^r,$$ where $\alpha_j=\frac{\lambda_j}{n}$, $\beta_i=\frac{\lambda'_j}{n}$.
:::

::: proof
*Proof.* Firstly, let us consider the case $r=1$. Note that $$\begin{aligned}
N^\lambda\big(e,(1,\ldots,k)\big) =\sum_j (n \alpha_j)^k,\quad
N^\lambda\big((1,\ldots,k),e\big) =\sum_j (n \beta_j)^k
\end{aligned}$$ therefore Theorem [\[theo:cumulants\]](#theo:cumulants){reference-type="ref" reference="theo:cumulants"} implies that the left-hand side of [\[eq:freecumulants-estimate\]](#eq:freecumulants-estimate){reference-type="eqref" reference="eq:freecumulants-estimate"} is equal to $$\Bigg|\frac{1}{n^k} \sum_{\substack{\sigma_1,\sigma_2 \in S_k \backslash \{e\}
\\ \sigma_1 \sigma_2 = \pi \\ |\sigma_1| + |\sigma_2| = |\pi|}}
(-1)^{|\sigma_1|} N^\lambda(\sigma_1,\sigma_2)\Bigg|.$$ For a pair of permutations $\sigma_1,\sigma_2$ which contributes to the above sum we consider the bipartite graph $G$ and the graph $\tilde{G}$ given by Lemma [\[lem:grafGprim\]](#lem:grafGprim){reference-type="ref" reference="lem:grafGprim"}. Clearly, in this case graph $\tilde{G}$ has more than one component. With Lemma [\[lem:numer-of-cutted-graphs\]](#lem:numer-of-cutted-graphs){reference-type="ref" reference="lem:numer-of-cutted-graphs"} and Lemma [\[lem:grafGprim\]](#lem:grafGprim){reference-type="ref" reference="lem:grafGprim"} $$\begin{gathered}
\label{eq:estimate-a-la-vk}
\left(\frac{n}{A}\right)^{k-1} \left|
\frac{R^\lambda_{k+1}}{n^k} - \sum_j \big( \alpha_j^{k} - 

(-\beta_{j})^{k} \big) \right|
\leq \\ \sum_{s \geq 2} \frac{(C_0 k)^{2s-2}}{(2s-2)!}
\left(\frac{n}{A^2}\right)^{s-1} \leq
 \frac{2 C_0^2 k^2 n}{A^2}= 2 C_0^2 \varepsilon,
\end{gathered}$$ where the last inequality holds true if $\frac{2 C_0^2 k^2 n}{A^2}=2 C_0^2
\varepsilon$ is smaller than some positive constant and the proof is finished in the case $r=1$.

For the general case, we put $\epsilon_i = \frac{k_i^2
n}{A^2}$. We denote $$\begin{aligned}
 X_i&=\frac{1}{a} \left(\frac{n}{A}\right)^{k_i-1}
\frac{R^\lambda_{{k_i}+1}}{n^{k_i}},\\
 Y_i&=\frac{1}{a} \left(\frac{n}{A}\right)^{k_i-1} \sum_j \big( \alpha_j^{k_i} -
(-\beta_{j})^{k_i} \big).
\end{aligned}$$ Let us fix $a>2$. Clearly, $|Y_i|< \frac{2}{a}< 1$ hence [\[eq:estimate-a-la-vk\]](#eq:estimate-a-la-vk){reference-type="eqref" reference="eq:estimate-a-la-vk"} shows that $|X_i|<1$ if $\varepsilon$ is smaller than some positive constant. Telescopic summation $$\begin{gathered}
X_1 \cdots X_r - Y_1 \cdots Y_r= X_1 \cdots X_{r-1} (X_r-Y_r)+\\
 X_1 \cdots X_{r-2} (X_{r-1}-Y_{r-1}) Y_r + \cdots 
+(X_1-Y_1) Y_2 \cdots Y_r
\end{gathered}$$ shows that $$\begin{gathered}
 \frac{1}{a^r} \left(\frac{n}{A}\right)^{l-r}
\left| \frac{\prod_{i=1}^r R^\lambda_{k_i+1}}{n^l} - \prod_{i=1}^r \left[ \sum_j
\alpha_j^{k_i} - \sum_j (-\beta_{j})^{k_i} \right] \right| \leq \\
\frac{2 C_0 (\epsilon_1+\cdots+\epsilon_r)}{a}.\qedhere
\end{gathered}$$ ◻
:::
