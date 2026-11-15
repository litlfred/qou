---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-024-53-fluctuations-of-rows
section_title: "Fluctuations of rows"
section_number: 5.3
pages: 22-23
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.894
latex_coverage_ratio: 0.979
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[]{#subsect:fluctuations_row label="subsect:fluctuations_row"} As before, we denote by $X_\lambda$ the probability measure on $[-1,1]$ associated to a Young diagram $\lambda$, and by $X_{\infty;q}$ the limit probability measure of the $X_{\lambda}$ under the $q$-Plancherel measures. If $f \in \mathscr{C}^1([-1,1])$ is a continuously differentiable function on $[-1;1]$, we define the rescaled deviation of $f$ under $q$-Plancherel measure. It is the random variable $D_{n,q}(f)$ obtained by composition of $q$-Plancherel measure by the function: $$\lambda \mapsto \sqrt{n}\,\left(X_\lambda(f)-X_{\infty;q}(f)\right),$$ where $\mu(f)$ is a short notation for $\int_{-1}^1 f d\mu$.

In this context, the convergence in law of rescaled power sums can be reformulated as a convergence in law of the vector $\big(D_{n,q}(x^l)\big)_{1 \leq l \leq k}$ towards a gaussian vector $(Z_{q;l})$ with covariance matrix: $$\begin{aligned}
k(Z_{q;l},Z_{q;m}) &= X_{\infty;q}((l+1)(m+1)\,x^{l}x^m)-(l+1)(m+1)\,X_{\infty;q}(x^{l})\,X_{\infty;q}(x^{m}) ;\\
&=X_{\infty;q}\left((x^{l+1})'\,(x^{m+1})'\right)-X_{\infty;q}\left((x^{l+1})'\right)\,X_{\infty;q}\left((x^{m+1})'\right).
\end{aligned}$$ Recall that with respect to the $\mathscr{C}^1$-topology, $\mathbb{R}[X]$ is dense in the space of continuously differentiable functions $\mathscr{C}^1([-1,1])$. By using this density together with the bilinearity of $D_{n,q}$ and covariance, we conclude that for any functions $f_1,f_2,\ldots,f_r \in \mathscr{C}^1([-1,1])$, the vector of rescaled deviations $D_{n,q}(f_i)$ converges towards a gaussian vector $(Z_{q;f_i})_{i \in \left[\!\left[1,r\right]\!\right]}$ with covariance matrix: $$k(Z_{q;f_i},Z_{q;f_j}) = X_{\infty;q}\left((xf_i)'\,(xf_j)'\right)-X_{\infty;q}\left((xf_i)'\right)\,X_{\infty;q}\left((xf_j)'\right).$$

::: proof
*Proof of Theorem [\[th:second_order_as_rows\]](#th:second_order_as_rows){reference-type="ref" reference="th:second_order_as_rows"}.* If $i \geq 1$, we denote by $f_i$ a class $\mathscr{C}^1$ and non-negative function such that $f_i(x)=1$ on a vicinity $V_i$ of $q^{i-1}\,(1-q)$ and $f_i(x)=0$ outside a vicinity $W_i\supset V_i$, *cf.* figure [1](#galactica){reference-type="ref" reference="galactica"}. We shall also suppose that the $W_i$ are disjoint open sets; in particular, $X_{\infty;q}(f_i)=q^{i-1}(1-q)$. Since $f_i'(q^{i-1}(1-q))=0$, $(xf_i)'(q^{i-1}(1-q)) = f_i(q^{i-1}(1-q))=1$, and as a consequence, $$X_{\infty;q}((x\,f_i(x))'^2)-X_{\infty;q}((x\,f_i(x))')^2=q^{i-1}(1-q)-q^{2(i-1)}(1-q)^2.$$

<figure id="galactica">
<div class="center">
<p><span><span>(-20,-4)(80,13) (-20,0)(80,0) (0,-2)(0,20) (-15,0.2)(5,0.2)(20,0.2)(34,0.2)(39,1)(46,14)(50,15)(54,14)(61,1)(67,0.2)(75,0.2) (75,-1)(75,1) (50,-1)(50,1) (37,-8)(37,1) (63,-8)(63,1) (37,-7)(63,-7) (50,-9.5)<span><span class="math inline"><em>W</em><sub><em>i</em></sub></span></span> (50,3)<span><span class="math inline"><em>q</em><sup><em>i</em> − 1</sup>(1−<em>q</em>)</span></span> </span></span></p>
</div>
<figcaption>Graphical representation of the test function <span class="math inline"><em>f</em><sub><em>i</em></sub></span>.<span id="galactica" label="galactica"></span></figcaption>
</figure>

Moreover, $f_i\,f_j=0$ for all $i\neq j$, and the same holds for $f_i\,f_j'$, $f_i'\,f_j$ or $f_i'\,f_j'$. Therefore, the covariance matrix of the corresponding limit gaussian vector $(Z_{q;f_i})_{i \geq 1}$ is: $$\begin{aligned}
X_{\infty;q}\left((x\,f_i(x))'\,(x\,f_j(x))'\right)-X_{\infty;q}\left((x\,f_i(x))'\right)\,X_{\infty;q}\left((x\,f_j(x))'\right)&=-X_{\infty;q}\left((x\,f_i(x))'\right)\,X_{\infty;q}\left((x\,f_j(x))'\right) ;\\
&=-(1-q)^2\,q^{i+j-2}.
\end{aligned}$$ Finally, for $n$ large enough and outside a set of arbitrary small probability, $a_i^*(\lambda)/n$ is in $V_i$, $a_{i-1}^*(\lambda)/n$ is in $V_{i-1}$ and $a_{i+1}^*(\lambda)/n$ is in $V_{i+1}$. Thus, with a probability close to $1$, the support of $X_\lambda$ and the support of $f_i \neq 0$ intersect only at $a_i^*(\lambda)/n$, and $X_\lambda(f_i)=a_i^*(\lambda)/n$. As a consequence, $$\sqrt{n}\,\left(\frac{a_i^*(\lambda)}{n}-q^{i-1}(1-q)\right)=\sqrt{n}\,\left(X_\lambda(f_i)-X_{\infty;q}(f_i)\right),$$ outside a set of arbitrary small probability, and the repartition functions of these random variables have the same asymptotic behavior. Theorem [\[th:second_order_as_rows\]](#th:second_order_as_rows){reference-type="ref" reference="th:second_order_as_rows"} follows then from the estimation $a_i^*(\lambda)=\lambda_i+O(1)$. ◻
:::
