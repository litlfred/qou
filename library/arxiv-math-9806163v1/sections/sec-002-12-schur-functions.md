---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-002-12-schur-functions
section_title: "Schur Functions"
section_number: 1.2
pages: 4-6
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.877
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempotents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
For details and proofs on the results mentioned in this subsection we refer the reader to [@mc] Ch.I, sec. 3. Suppose $x_1,x_2,\ldots x_r$ is a finite set of variables. For some partition $\alpha$ we set $x^{\alpha}=x_1^{\alpha_1}\ldots x_r^{\alpha_r}$. Let $\delta=[r-1,r-2,\ldots,1,0]$. We define the following determinant. $$a_{\alpha+\delta}=\det(x_i^{\lambda_j+r-j})$$ This determinant is divisible in $\mathbb{Z}[x_1,\ldots,x_r]$ by the Vandermonde determinant which is given by $$a_{\delta}=\det(x_i^{r-j}).$$ Then the symmetric *Schur function* is defined as follows: $$s_{\alpha}(x_1,\ldots,x_r)={a_{\alpha+\delta}\over{a_{\delta}}}.$$ Take $x_i=q^{i-1}$ ($1\leq i \leq r$). If $\lambda$ is a partition of length $\leq r$, we have $$\label{sfq}
s_{\alpha}(1,q,\ldots, q^{r-1})=q^{n(\alpha)}\prod_{1\leq i<j \leq r}{1-q^{\alpha_i-\alpha_j+j-i}\over{1-q^{j-i}}}$$ where $n(\alpha)=\sum_{i=1}^{l(\alpha)}{(i-1)\alpha_i}$. We define the following Schur function as a normalization of equation ([\[sfq\]](#sfq){reference-type="ref" reference="sfq"}): $$s_{\alpha,r}(q)={s_{\alpha}(1,q,\ldots,q^{r-1})\over{s_{[1]}(1,q,\ldots,q^{r-1})^{|\alpha|}}}=q^{n(\alpha)}\prod_{1\leq i<j \leq r}{(1-q)(1-q^{\alpha_i-\alpha_j+j-i})\over(1-q^r)(1-q^{j-i})}\notag$$ Notice that $s_{\alpha,r}(q)=0$ whenever $l(\alpha)>r$. Also if $\chi^{\alpha}(q)$ denotes the character of a matrix in $Gl(r)$ with eigenvalues $q^{(-r+1)/2}$, $q^{(-r+3)/2}$, $\ldots$, $q^{(r-1)/2}$ and if the number of boxes in $\alpha$ is $n$, $s_{\alpha,r}(q)=\chi^{\alpha}(q)/(\chi^{[1]}(q))^n$. Let $r=r_1+r_2$; then the Schur function for $\mu=[m+\alpha_1,\ldots,m+\alpha_{r_1},\beta_1,\ldots,\beta_{r_2}]$ is given by $$\label{eq:sf}
s_{\mu,r}(q)=q^{n(\mu)}\prod_{1\leq i<j\leq r}{(1-q)(1-q^{\mu_i-\mu_j+j-i})\over{(1-q^r)(1-q^{j-i})}}.$$ After some rearrangement of equation ([\[eq:sf\]](#eq:sf){reference-type="ref" reference="eq:sf"}) we get the following equation for the Schur function of $\mu$: $$\begin{aligned}
\label{eq:slr}
s_{\mu,r}(q) &=&  q^{mr_1(r_1-1)/2+r_1|\beta|}{({1-q\over{1-q^r}})^{|\mu|}}s_{\alpha}(1,q,\ldots,q^{r_1-1})s_{\beta}(1,q,\ldots,q^{r_2-1}) \notag \\ 
&&\prod_{i=1}^{r_1}\prod_{j=1}^{r_2}{{1-q^{m+r_1+\alpha_i-\beta_j+j-i}}\over{1-q^{r_1+j-i}}}.
\end{aligned}$$ The expression of this Schur function in ([\[eq:slr\]](#eq:slr){reference-type="ref" reference="eq:slr"}) is useful in the proof of the weight formula! .5in
