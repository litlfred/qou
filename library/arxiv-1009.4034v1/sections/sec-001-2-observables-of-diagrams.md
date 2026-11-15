---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2"
section_id: sec-001-2-observables-of-diagrams
section_title: "Observables of diagrams"
section_number: 2
pages: 5-8
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.97
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 — In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of Young diagrams under the"
---
[]{#obs label="obs"} In the setting of random partitions, the algebra of polynomial functions[^1] on Young diagrams and its various bases play an extremely important role that can be compared to the one played by the moments of a real random variable. Hence, the **generating function** of a Young diagram $\lambda$ is defined by $$G_{\lambda}(z)=\frac{\prod_{i=1}^{v-1}z-y_{i}}{\prod_{i=1}^{v}z-x_{i}},$$ where $x_{1}<y_{1}<x_{2}<y_{2}<\cdots<x_{v-1}<y_{v-1}<x_{v}$ are the **interlacing coordinates** of $\lambda$, that is to say, the sequences of local minima and local maxima of the function $s\mapsto \lambda(s)$. Alternatively, if $\sigma(s)=\frac{\lambda(s)-|s|}{2}$, then $$G_{\lambda}(z)=\frac{1}{z}\exp\left(-\int_{\R}\frac{\sigma'(s)}{z-s}\,ds\right).$$ This latter definition allows to consider the generating function of more general objects such as **continuous Young diagrams**, *i.e.*, functions $s\mapsto \omega(s)$ that satisfy the two following properties:

1.  $\omega$ is Lipschitz with constant $1$, *i.e.*, $|\omega(s)-\omega(t)|\leq |s-t|$ for all $s,t$.

2.  $\omega(s)=|s|$ for $s$ big enough.

Given a (continuous) diagram $\lambda$, the coefficients $\tilh_{n}(\lambda)$ of the power serie $z^{-1}G_{\lambda}(z^{-1})$ generate an algebra $\obs$ of **observables of diagrams**. One may also consider as an algebraic basis for $\obs$ the coefficients $\tilp_{n}(\lambda)$ given by the formula $$z^{-1}G_{\lambda}(z^{-1})=1+\sum_{n=1}^{\infty} \tilh_{n}(\lambda)\,z^n=\exp\left(\sum_{n=1}^{\infty} \frac{\tilp_{n}(\lambda)}{n}\,z^{n}\right).$$ For a true Young diagram $\lambda$, $\tilp_{n}(\lambda)=\sum_{i=1}^{v}(x_{i})^{n}-\sum_{i=1}^{v-1}(y_{i})^{n}$ is the $n$-th moment of the interlacing coordinates, whereas for a continuous diagram, one can give the following formula: $$\tilp_{n}(\omega)=\int_{\R} \sigma''(s)\,s^{n}\,ds=\frac{1}{(n+1)(n+2)}\int_{\R}\sigma(s)\,s^{n+2}\,ds$$ Notice that $\tilh_{1}(\lambda)=\tilp_{1}(\lambda)=0$ for any (continuous) diagram $\lambda$; on the other hand, one can show that the other coefficients are algebraically independant (viewed as functions on diagrams). So, $$\obs=\C[\tilh_{2},\tilh_{3},\ldots]=\C[\tilp_{2},\tilp_{3},\ldots],$$ see [@IO02 §2]. The **weight grading** on this algebra is then defined by setting $\wt(\tilp_{k\geq 2})=k$, and it provides a filtration of algebra on $\obs$ that is well-behaved with respect to scaling of continuous diagrams. More precisely, if $\omega$ is a continuous diagram and if $\omega^{t}$ is the scaled diagram defined by $$\omega^{t}(s)=\frac{\omega(st)}{t}$$ (see figure [\[scaling\]](#scaling){reference-type="ref" reference="scaling"}), then for any homogeneous observable $f$ of weight $k$, $f(\omega^{t})=t^{k}\,f(\omega)$. In particular, if $\lambda$ is a true Young diagram and if $\lambda^{*}=\lambda^{1/\sqrt{|\lambda|}}=\lambda^{1/\sqrt{n}}$, then $f(\lambda^{*})=n^{-\frac{k}{2}}\,f(\lambda)$.

Another algebraic basis of $\obs$ consists in the **free cumulants** of the transition measures of the continuous Young diagrams. First, if $\lambda$ is a (continuous) Young diagram, we define its **transition measure** $\mu_{\lambda}$ by $$G_{\lambda}(z)=\int_{\R}\frac{\mu_{\lambda}(s)}{z-s}.$$ In other words, the generating function of $\lambda$ is the Stieltjes transform of the transition measure. Notice that the $\tilh_{n}(\lambda)$'s are precisely the moments of the compactly supported measure $\mu_{\lambda}$. Then, the free cumulants of the measure $\mu_{\lambda}$ are the coefficients of the formal inverse $R_{\lambda}$ of $G_{\lambda}$ in a neighboorhood of infinity: $$R_{\lambda}(G_{\lambda}(z))=z \,\,\,\text{for }z\text{ big enough}\qquad;\qquad R_{\lambda}(z)=\frac{1}{z}\left(1+\sum_{n=1}^{\infty}R_{n}(\mu_\lambda)\,z^{n}\right)$$ see [@VDN92] for the uses of this notion in free probability. By Lagrange inversion, the free cumulants also satisfy the formula $$R_{n+1}(\lambda)=R_{n+1}(\mu_{\lambda})=-\frac{1}{n}[z^{-1}](G_{\lambda}(z))^{-n},$$ and $R_{n+1}$ is therefore an observable of diagrams that is homogeneous with weight $n+1$. R. Speicher has given a simple combinatorial interpretation of the change of basis formulas between the $\tilh$'s and the $R$'s, see [@NS06]. These formulas implie in particular that the $R_{k\geq 2}$'s are algebraically independant, so $\obs=\C[R_{2},R_{3},\ldots]$.

Finally, another algebraic basis comes from the so-called **central characters**, that allow to relie the algebra $\obs$ to the representation theory of the symmetric groups. If $\lambda$ and $\mu$ are two partitions of same size $n$, one denotes by $\chi^{\lambda}(\mu)$ the value of the normalized irreducible character of $\sym_{n}$ of label $\lambda$ on a permutation $\sigma_{\mu}$ of cycle type $\mu$. Then, if $\lambda$ and $\mu$ are two partitions of sizes $n$ and $k$, one sets: $$\varSigma_{\mu}(\lambda)=\begin{cases} n^{\downarrow k}\,\chi^{\lambda}(\mu\sqcup 1^{n-k})&\text{if }n\geq k,\\
0&\text{otherwise}.
\end{cases}$$ Here, $\mu\sqcup 1^{n-k}$ is the completed partition obtained by adding parts of size $1$ to $\mu$, and $n^{\downarrow k}$ is the falling factorial $n(n-1)\cdots(n-k+1)$. It is true, although totally non trivial, that the $\varSigma_{\mu}$'s are observables of diagrams; *cf.* [@IO02 §3-4]. More precisely, $\wt(\varSigma_{\mu})=|\mu|+\ell(\mu)$, and the top homogeneous component of $\varSigma_{\mu}$ is $$R_{\mu+1}=R_{\mu_{1}+1}R_{\mu_{2}+1}\cdots R_{\mu_{r}+1},$$ see [@Bia98] and [@IO02 §10]. As a consequence, $\obs=\C[\varSigma_{1},\varSigma_{2},\ldots]$ is freely generated by the central characters of cycles, and one has a factorization property of characters in top homogeneous component: $$\varSigma_{\mu_{1}}\,*\,\varSigma_{\mu_{2}}=\varSigma_{\mu_{1}\sqcup \mu_{2}}+\big(\text{observable of weight less than }\mu_{1}+\mu_{2}+\ell(\mu_{1})+\ell(\mu_{2})-2\big)$$ In fact, there exists multivariate polynomials with non-negative integer coefficients $K_{k}$ such that $\varSigma_{k}=K_{k}(R_{k+1},R_{k},\ldots,R_{2})$ for any $k \geq 1$; these **Kerov polynomials** are studied for instance in [@DFS08]. In §[\[core\]](#core){reference-type="ref" reference="core"}, we will rather have to exprime the $\tilp$'s as polynomials in the $\varSigma$'s. We refer to [@IO02 Proposition 3.7] for a proof of the following result:

::: proposition
[]{#changeofbasis label="changeofbasis"} For $k \geq 2$, $\tilp_{k}$ is the top homogeneous component of weight $k$ of the observable $$\sum_{\substack{\mu=1^{m_{1}}2^{m_{2}}\cdots s^{m_{s}}\\|\mu|+\ell(\mu)=k }} \frac{k^{\downarrow \ell(\mu)}}{\prod_{i\geq 1} m_{i}!}\prod_{i\geq 1}(\varSigma_{i})^{m_{i}}\,.$$
:::

::: examples
Let us write the first $\tilp_{k}$'s in the linear basis of central characters $(\varSigma_{\mu})_{\mu \in \bigsqcup_{n \in \N}\Part_{n}}$: $$\begin{aligned}
\tilp_{1}&=0\quad\qquad\,;\qquad\tilp_{2}=2\varSigma_{1}\\
\tilp_{3}&=3\varSigma_{2}\qquad;\qquad\tilp_{4}=4\varSigma_{3}+6\varSigma_{1,1}+2\varSigma_{1}\\
\tilp_{5}&=5\varSigma_{4}+20\varSigma_{2,1}+15\varSigma_{2}\\
\tilp_{6}&=6\varSigma_{5}+30\varSigma_{3,1}+15\varSigma_{2,2}+20\varSigma_{1,1,1}+30\varSigma_{1,1}+60\varSigma_{3}+2\varSigma_{1}
\end{aligned}$$ Hence, one sees for instance that $\tilp_{6}$ is the top homogeneous component of $6\varSigma_{5}+30\varSigma_{3,1}+15\varSigma_{2,2}+20\varSigma_{1,1,1}$, and if one uses the factorization property of the central characters, one sees that these formulas agree with Proposition [\[changeofbasis\]](#changeofbasis){reference-type="ref" reference="changeofbasis"}.
:::

[^1]: In the same setting, another fruitful approach relie on determinantal point processes, see *e.g.* [@BO00] and [@BO05].
