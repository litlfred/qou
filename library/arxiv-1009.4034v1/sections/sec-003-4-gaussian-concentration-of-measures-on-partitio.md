---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2"
section_id: sec-003-4-gaussian-concentration-of-measures-on-partitio
section_title: "Gaussian concentration of measures on partitions"
section_number: 4
pages: 12-13
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.994
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 — In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of Young diagrams under the"
---
[]{#sniady label="sniady"} To establish the gaussian concentration of probability measures on partitions coming from reducible representations of symmetric groups, P. Śniady has developed in [@Sni06] a theory of cumulants of observables that works in a very general setting, and in particular for Schur-Weyl measures. If $X_{1},\ldots,X_{r}$ are real or complex random variables, we recall that the **joint cumulant** of $X_{1},\ldots,X_{r}$ is $$k(X_{1},\ldots,X_{r})=\left.\frac{\partial^{r}}{\partial t_{1}\cdots \partial t_{r}}\right|_{t_{1}=t_{2}=\cdots=t_{r}=0}\!\!\!\log \esper[\exp(t_{1}X_{1}+\cdots+ t_{r}X_{r})]\,.$$ In particular, gaussian vectors are characterized by the vanishing of joint cumulants of order $r\geq 3$, and the first and second joint cumulants give the expectation of the gaussian vector and its covariance matrix. That said, if $a_{1},\ldots,a_{r}$ commute in the group algebra $\C\sym_{n}$, and if $\proba$ is a probability measure on $\Part_{n}$, then one can consider the $a_{i}$'s as commutative random variables by setting $$a_{i}=a_{i}(\lambda)=\chi^{\lambda}(a_{i})$$ with $\lambda$ picked randomly according to $\proba$; as a consequence, the joint cumulant $k(a_{1},\ldots,a_{r})$ makes sense. On the other hand, we have seen that observables of diagrams may also be considered as random variables, and besides, any observable can be interpreted as an element of the center of the group algebra $\C\sym_{n}$, see [@Sni06 §2.1]; so, the joint cumulant of observables of diagrams also makes sense. Then, the major result of [@Sni06] is the following:

::: theorem
[]{#sniadytheo label="sniadytheo"} Let $(\proba_{n})_{n \in \N}$ be a family a probability measures on the sets $\Part_{n}$ of integer partitions, and let us denote by $(\esper_{n})_{n \in \N}$ and $(k_{n})_{n \in \N}$ the corresponding expectations and joint cumulants. The following assertions are equivalent:

1.  For all positive integers $l_{1},\ldots,l_{r}$, $$k_{n}(\varSigma_{l_{1}},\ldots,\varSigma_{l_{r}})\,n^{-\frac{l_{1}+\cdots+l_{r}-r+2}{2}}=O(1).$$

2.  For all integers $l_{1},\ldots,l_{r} \geq 2$, $$k_{n}(R_{l_{1}},\ldots,R_{l_{r}})\,n^{-\frac{l_{1}+\cdots+l_{r}-2r+2}{2}}=O(1).$$

3.  If $\sigma_{l_{1}}, \ldots,\sigma_{l_{r}}$ are disjoint cycles of respective lengths $l_{1},\ldots,l_{r}$, then $$k_{n}(\sigma_{l_{1}},\ldots,\sigma_{l_{r}})\,n^{\frac{l_{1}+\cdots+l_{r}+r-2}{2}}=O(1).$$

Moreover, if these assertions hold, then the following limits are equal (assuming that they exist): $$\begin{aligned}
c_{l+1}&=\lim_{n\to \infty} \esper_{n}[\varSigma_{l}]\,n^{-\frac{l+1}{2}}=\lim_{n\to \infty} \esper_{n}[R_{l+1}]\,n^{-\frac{l+1}{2}}=\lim_{n \to \infty} \esper_{n}[\sigma_{l}]\,n^{\frac{l-1}{2}}\\
v_{l+1,m+1}&=\lim_{n \to \infty}k_{n}(\varSigma_{l},\varSigma_{m})\,n^{-\frac{l+m}{2}}=\lim_{n \to \infty}k_{n}(R_{l+1},R_{m+1})\,n^{-\frac{l+m}{2}}\\
&=\lim_{n \to \infty}k_{n}(\sigma_{l},\sigma_{m})\,n^{\frac{l+m}{2}}-lm\,c_{l+1}\,c_{m+1}+\sum_{\substack{l=a_{1}+\cdots+a_{r}\\ m=b_{1}+\cdots + b_{r}}} \frac{lm}{r}\,c_{a_{1}+b_{1}}\cdots c_{a_{r}+b_{r}}
\end{aligned}$$ In this setting, the random processes $$\left(n^{-\frac{l}{2}}\,\big(R_{l+1}-\esper_{n}[R_{l+1}]\big)\right)_{l\geq 1}\quad\text{and}\quad\left(n^{-\frac{l}{2}}\,\big({\varSigma_{l}}-\esper_{n}[\varSigma_{l}]\big)\right)_{l\geq 1}$$ converge in finite-dimensional laws towards a gaussian process whose covariance matrix is $(v_{l+1,m+1})_{l,m \geq 1}$.
:::

Under a Schur-Weyl measure $\SWa$ with parameters $\alpha=1/2$ and $c>0$, the expectation of a permutation of cycle type $\mu$ is $\SWa[\sigma_{\mu}]=N^{\ell(\mu)-|\mu|}\simeq c^{|\mu|-\ell(\mu)}\,n^{\frac{\ell(\mu)-|\mu|}{2}}$, and this expression is multiplicative with respect to the lengths of the cycles of $\sigma_{\mu}$. Consequently, given disjoint cycles of lengths $l_{1},\ldots,l_{r}$, one has: $$k_{n}(\sigma_{l_{1}},\ldots,\sigma_{l_{r}})=\begin{cases}N^{1-l_{1}}&\text{if }r=1,\\ 0&\text{otherwise}.\end{cases}$$ From this, one deduces that Schur-Weyl measures with parameters $\alpha=1/2$ and $c>0$ satisfy the hypotheses of Theorem [\[sniadytheo\]](#sniadytheo){reference-type="ref" reference="sniadytheo"}, and the limit of the random process $$\left(X_{l}=\frac{\varSigma_{l}}{n^{\frac{l}{2}}}-c^{l-1}n^{\frac{1}{2}}\right)_{l \geq 2}$$ is a centered gaussian process with covariance matrix $$v_{l+1,m+1}=0-lm\,c^{l+m-2}+\sum_{r\geq 1}\sum_{\substack{l=a_{1}+\cdots+a_{r}\\ m=b_{1}+\cdots + b_{r}}} \frac{lm}{r} \,c^{l+m-2r}=\sum_{r\geq 2} \binom{l}{r}\binom{m}{r}\,r\,c^{l+m-2r},$$ see [@Sni06 Example 6]. In particular, when $c=0$, the random variables $\sqrt{n}\,\chi^{\lambda}(\sigma_{l})$ converge in finite-dimensional laws towards independent normal variables of variance $l$; this is a form of Kerov's central limit theorem. As we shall see in §[\[ksw\]](#ksw){reference-type="ref" reference="ksw"}, the extension of Kerov's theorem to the case of Schur-Weyl measures stems from a very natural idea; namely, one wanted to produce *independent* gaussian variables from the fluctuations ${\varSigma_{l}}\,{n^{-\frac{l}{2}}}-c^{l-1}n^{\frac{1}{2}}$ when $c$ is not equal to $0$ and the fluctuations are not asymptotically independent. The obvious way to do this was to perform a Gram-Schmidt orthogonalisation in the gaussian space of the limiting process, and we discovered that the orthogonalized basis is related to translated versions of the Chebyshev polynomials of the second kind.
