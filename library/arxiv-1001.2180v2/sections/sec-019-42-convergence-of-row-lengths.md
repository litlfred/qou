---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-019-42-convergence-of-row-lengths
section_title: "Convergence of row lengths"
section_number: 4.2
pages: 15-16
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.981
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[]{#subsect:convergence_rows label="subsect:convergence_rows"} Note that the limit values of the rescaled $p_k$'s are the power sums of the sequence $((1-q),(1-q)q,(1-q)q^2,\ldots)$. Indeed, $$\sum_{i=1}^\infty (1-q)^k\, q^{(i-1)k}=\frac{(1-q)^k}{1-q^k}.$$ In this paragraph, we show that the convergence of power sums implies the convergence of the sequence. This corresponds to the end of the proof of Theorem [\[th:first_order_as_rows\]](#th:first_order_as_rows){reference-type="ref" reference="th:first_order_as_rows"}.

The main idea is to consider, given a Young diagram $\lambda$ of size $n$, the probability measure $X_\lambda$ defined by $$X_\lambda=\sum_{i=1}^d (a_i^*(\lambda)/n)\,\delta_{(a_i^*(\lambda)/n)}+(b_i^*(\lambda)/n)\,\delta_{(-b_i^*(\lambda)/n)}.$$ The $k$-th moment of $X_\lambda$ is exactly $p_{k+1}(\lambda)/n^{k+1}$. So, thanks Lemma [\[lem:cv_powersums\]](#lem:cv_powersums){reference-type="ref" reference="lem:cv_powersums"}, under $q$-Plancherel measure, the moments of $X_\lambda$, which can be seen as random variables, converge in probability towards the moments of the measure $$X_{\infty;q}=\sum_{i=1}^\infty (1-q)q^{i-1}\,\delta_{(1-q)q^{i-1}}.$$

::: lemma
[]{#lem:cv_fct_repartition label="lem:cv_fct_repartition"} As usual, we consider a sequence of random diagrams $\lambda_n \in \mathscr{Y}_n$ taken with $q$-Plancherel measure. At any point $x \neq (1-q)\,q^{i-1}$, one has convergence in probability of the repartition functions, that is to say: $$\sum_{\substack{y\leq x\\ ny \in A_\lambda+\overline{B}_\lambda}} \!\!\!\!|y|\quad \longrightarrow_{M_{n,q}} \sum_{(1-q)q^{i-1} \leq x} \!\!\!\!(1-q)q^{i-1}.$$
:::

::: proof
*Proof.* In the following, we consider $\lambda \mapsto X_\lambda$ as a *measure-valued random variable* $X_{n,q}$; its law is by definition the image of $M_{n,q}$ by $\lambda \mapsto X_\lambda$. The set $\mathscr{M}([-1,1])$ of probability measures on $[-1,1]$, where $X_{n,q}$ takes its values, is included in the dual of $\mathscr{C}([-1,1])$ and is compact and metrizable with respect to the $*$-weak topology[^1]. Indeed, if $(f_n)_{n \in \mathbb{N}}$ is a sequence of continuous functions dense in $\mathscr{C}([-1,1])$, then $$d(m_1,m_2)=\sum_{n \in \mathbb{N}} \frac{1}{2^n} \,\max(1,|m_1(f_n)-m_2(f_n)|)$$ is a distance compatible with the topology of $\mathscr{M}([-1,1])$. We choose $\{f_n\}_{n \in \mathbb{N}}=\mathbb{Q}[X]$ (dense by Stone-Weierstrass theorem), thus the convergence of moments implies that $X_{n,q}$ converges in probability in $(\mathscr{M}([-1,1]),d)$ towards $X_{\infty;q}$.

But, for Radon measures on the real line, the weak convergence $X_{n,q} \rightharpoonup X_{\infty;q}$ is equivalent to the convergence of repartition functions $F_{X_{n,q}}(x) \to F_{X_{\infty;q}}(x)$ at points $x \in [-1,1]$ where $F_{X_{\infty;q}}$ is continuous --- it is a part of the Portmanteau theorem ([@Bil69 Chapter1]). ◻
:::

::: proof
*End of proof of Theorem [\[th:first_order_as_rows\]](#th:first_order_as_rows){reference-type="ref" reference="th:first_order_as_rows"}.* Now, let us take $x=1-q+\eta$ with $\eta >0$ sufficiently small. We also fix $1-q>\varepsilon>0$. Note that $F_{X_{\infty;q}}=1$ on an open set containing $x$. Consequently, for $n$ big enough and outside a set of arbitrarily small probability, all rows of $\lambda$ are smaller than $nx$, because $$F_{X_\lambda}(x)=\sum_{\substack{y \leq x \\ ny \in A+\overline{B}}} \!\!\!\!|y|\,\,\, \geq F_{X_{\infty;q}}(x)-\varepsilon= 1-\varepsilon> q,$$ and this could not be if a row were bigger than $n(1-q+\eta)$. Indeed, we would then have $$F_{X_\lambda}(1) \geq F_{X_{n,q}}(x)+1-q+\eta > 1+\eta>1.$$ Hence, for $n$ big enough, $a_1^*(\lambda)/n$ is smaller than $x$ outside a set of arbitrary small probability. Now, if $x'=1-q-\eta$, then $F_{X_{\infty;q}}=q$ on an open set containing $x'$, and therefore, for $n$ big enough and outside a set of arbitrarily small probability, some rows of $\lambda$ are bigger than $nx'$; otherwise, we would have $$F_{X_\lambda}(1)=F_{X_\lambda}(x')\leq F_{X_{\infty;q}}(x')+\varepsilon= q+\varepsilon<1.$$ We conclude that for $n$ big enough and outside a set of arbitrarily small probability, the rescaled first column $a_1^{*}(\lambda)/n$ is between $x'$ and $x$. Consequently, $a_1^*(\lambda)/n$ converges in probability towards $1-q$, and the same argument holds for the following rows (with an induction on the index $i$ of the row). Of course, $a_i^*(\lambda)/n-\lambda_i/n=O(1/n)$, so we have proved Theorem [\[th:first_order_as_rows\]](#th:first_order_as_rows){reference-type="ref" reference="th:first_order_as_rows"}. ◻
:::

::: remark
[]{#RemColumns label="RemColumns"} Unfortunately, our estimates are not strong enough to prove almost surely convergence.

Let us look at the first column of a random diagram under the $q$-Plancherel measure. If we take $x=0$ in Lemma [\[lem:cv_fct_repartition\]](#lem:cv_fct_repartition){reference-type="ref" reference="lem:cv_fct_repartition"}, then we see that $\sum_{i=1}^d b_i^*(\lambda)/n$ goes to $0$ in probability: so, the column lengths are $o(n)$. Nevertheless, we can not determine their precise order of magnitude.
:::

::: remark
The same proof works for any measure for which we can compute expectation of character values as soon as (the following condition implies the convergence of variance of power sums towards $0$ in Lemma [\[lem:cv_powersums\]](#lem:cv_powersums){reference-type="ref" reference="lem:cv_powersums"}): $$\mathbb{E}[\Sigma_{k,k}] = \mathbb{E}[\Sigma_k]^2 + o(n^{2k}).$$ This is similar to the result obtained by Biane for balanced diagrams in [@Bia01].
:::

[^1]: It is a particular case of the Prohorov theorem: if $E$ is a separable and complete metric space (in other words, a polish space), then the same holds for the set of probability measures $\mathscr{M}(E)$, see [@Bil69 Chapter 1]. As a consequence, convergence in probability makes sense for random probability measures on a closed subset of the real line.
