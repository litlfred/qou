---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-034-75-proof-of-the-central-limit-theorem
section_title: "Proof of the central limit theorem"
section_number: 7.5
pages: 50-51
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.796
latex_coverage_ratio: 0.902
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
We are now ready to prove the main result of this section:

::: proof
*Proof of Theorem [\[theo:FluctuationsJackCharacters\]](#theo:FluctuationsJackCharacters){reference-type="ref" reference="theo:FluctuationsJackCharacters"}.* Let $\tilde{\Xi}_d = (\Xi_2,\dots,\Xi_{d+1})$. In order to show that $$\left( \frac{\mathop{\mathrm{Ch}}_{(k)}}{ \sqrt{k} n^{k/2}} \right)_{k=2,3,\dots} \xrightarrow{d} \left( \Xi_k \right)_{k=2,3,\dots}$$ as $n \to \infty$, it is enough to show, that for all $d \in \mathbb{N}$ and for any smooth function $h$ on $\mathbb{R}^d$, with all derivatives bounded, one has, as $n \to \infty$: $$\left| \mathbb{E}_n^{(\alpha)}h(\tilde{W}_d) - \mathbb{E}h(\tilde{\Xi}_d) \right| \to 0.$$

Fix a positive integer $d$ and a function $h:\mathbb{R}^d \to \mathbb{R}$ as above. Let $\varSigma = (\mathbb{E}_n^{(\alpha)})(\tilde{W}_d\tilde{W}_d^t)$. As $h$ has its first derivative bounded, one has $$\left| \mathbb{E}\left( h(\tilde{\Xi}_d) - 
h(\varSigma^{1/2}\tilde{\Xi}_d) \right) \right| \le
|h|_1 \cdot d\, \lVert \mathop{\mathrm{Id}}- \varSigma^{1/2} \rVert \cdot \mathbb{E}(\lVert \tilde{\Xi}_d \rVert).$$ But $|h|_1$ and $\mathbb{E}_n^{(\alpha)}(\lVert \tilde{\Xi}_d \rVert)$ are fixed finite numbers, while $\lVert \mathop{\mathrm{Id}}- \varSigma^{1/2} \rVert$ is $O(n^{-1/2})$ by Proposition [\[prop:SteinCondition2\]](#prop:SteinCondition2){reference-type="ref" reference="prop:SteinCondition2"}. Hence, $$\left| \mathbb{E}\left( h(\tilde{\Xi}_d) - 
    h(\varSigma^{1/2}\tilde{\Xi}_d) \right) \right| = O(n^{-1/2}).
    \label{eq:forget_Sigma}$$

By Corollary [\[cor:SteinCondition1\]](#cor:SteinCondition1){reference-type="ref" reference="cor:SteinCondition1"} and Proposition [\[prop:SteinCondition2\]](#prop:SteinCondition2){reference-type="ref" reference="prop:SteinCondition2"} we know, that the pair $(\tilde{W}_d, \tilde{W}_d^*)$ satisfies all hypotheses of Theorem [\[theo:MultivariateStein\]](#theo:MultivariateStein){reference-type="ref" reference="theo:MultivariateStein"}. Using this theorem, we get $$\left| \mathbb{E}_n^{(\alpha)}h(\tilde{W}_d) - \mathbb{E}h(\varSigma \tilde{\Xi}_d)\right| \leq |h|_2\frac{A}{4} + |h|_3\frac{B}{12},$$ where $$A = \sum_{2 \leq i,j \leq d+1} \frac{n}{i} \sqrt{\mathop{\mathrm{Var}}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i - W_i^*)(W_j - W_j^*)\right)}$$ and $$B = \sum_{2 \leq i,j,k \leq d+1} \frac{n}{i} \mathbb{E}_n^{(\alpha)} |(W_i^* - W_i)(W_j^* - W_j)(W_k^* - W_k)|.$$ Propositions [\[prop:ErrorTermA\]](#prop:ErrorTermA){reference-type="ref" reference="prop:ErrorTermA"} and [\[prop:ErrorTermB\]](#prop:ErrorTermB){reference-type="ref" reference="prop:ErrorTermB"} imply that $$\left| \mathbb{E}_n^{(\alpha)}h(\tilde{W}_d) - \mathbb{E}h(\varSigma^{1/2} \tilde{\Xi}_d)\right| = O(n^{-1/2}).$$ Together with equation [\[eq:forget_Sigma\]](#eq:forget_Sigma){reference-type="eqref" reference="eq:forget_Sigma"}, it finishes the proof. ◻
:::
