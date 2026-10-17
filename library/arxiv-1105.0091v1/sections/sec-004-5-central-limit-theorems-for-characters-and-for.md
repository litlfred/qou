---
doc_id: arxiv-1105.0091v1
doc_title: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra"
section_id: sec-004-5-central-limit-theorems-for-characters-and-for
section_title: "Central limit theorems for characters and for partitions"
section_number: 5
pages: 36-42
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.976
doc_brief: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra — In this paper, we review the representation theory of the inﬁnite symmetric group, and"
---
[]{#clt label="clt"} In the previous paragraph, it was shown that all the coherent systems of measures $(\mathbb{P}_{n,\omega})_{n \in \mathbb{N}}$ have a property of concentration, that can be seen at the level of characters or directly for the geometry of the random partitions. In this section, we shall prove that the concentration is always gaussian, which is quite a striking fact. However, the geometric version of our central limit theorem will be a little less precise than the algebraic one: indeed, one cannot study with our method of moments the fluctuations of rows or columns corresponding to equal coordinates of the point $\omega$ of the Thoma simplex. This will be done in §[\[oconnell\]](#oconnell){reference-type="ref" reference="oconnell"} by entirely different methods, that relie essentially on the interpretation of the measures $\mathbb{P}_{n,\omega}$ as push-forwards of the measures $\mathbb{Q}_{n,\omega}$.

## Central limit theorem for the irreducible characters

In this paragraph, we fix permutations $\sigma^{(1)},\ldots,\sigma^{(r)} \in \mathfrak{S}_{\infty}$ of cycle types $\mu^{(1)},\ldots,\mu^{(r)}$; the partitions $\mu^{(i)}$ are all defined up to parts of size $1$, but this will not change our results. For convenience, we shall denote $p_{\mu}(A-B+\gamma E)=p_{\mu}(\omega)$.

::: theorem
[]{#mainalg label="mainalg"} We consider the random vector $(\Delta_{n,\omega}(\sigma^{(1)}),\ldots,\Delta_{n,\omega}(\sigma^{(r)}))$, with $$\Delta_{n,\omega}(\sigma)=\sqrt{n}\,\left(\chi^{\lambda}(\sigma)-\chi^{\omega}(\sigma)\right)$$ and $\lambda$ chosen randomly according to $\mathbb{P}_{n,\omega}$. As $n$ goes to infinity, this vector converges in joint law to a centered gaussian vector $(\Delta_{\infty,\omega}(\sigma^{(1)}),\ldots,\Delta_{\infty,\omega}(\sigma^{(r)}))$, and the covariance matrix of this vector is: $$\begin{aligned}
&k(\Delta_{\infty,\omega}(\sigma^{(i)}),\Delta_{\infty,\omega}(\sigma^{(j)}))\\
&=\sum_{a \in \mu^{(i)},\,\,
b\in \mu^{(j)} } ab\,\,p_{\mu_{i}\sqcup \mu_{j}\setminus \{a,b\}}(\omega)\,\,(p_{a+b-1}(\omega)-p_{a}(\omega)\,p_{b}(\omega)).
\end{aligned}$$ In particular, $k(\Delta_{\infty,\omega}(\sigma),\Delta_{\infty,\omega}(\tau))=lm\,\,(p_{l+m-1}(\omega)-p_{l}(\omega)\,p_{m}(\omega))$ if $\sigma$ and $\tau$ are cycles of lengths $l$ and $m$.
:::

::: proof
*Proof.* For any partition $\mu$, $$\sqrt{n}\,\left(\chi^{\lambda}(\mu\sqcup 1^{n-|\mu|})-p_{\mu}(\omega)\right)=\sqrt{n} \left(\frac{\varSigma_{\mu}(\lambda)-\mathbb{E}_{n,\omega}[\varSigma_{\mu}]}{n^{|\mu|}}\right)+O\left(\frac{1}{\sqrt{n}}\right),$$ so it is sufficient to show that the random vector $$V=\sqrt{n}\left(\frac{\varSigma_{\mu^{(1)}}}{n^{|\mu^{(1)}|}},\ldots,\frac{\varSigma_{\mu^{(r)}}}{n^{|\mu^{(r)}|}}\right)$$ converges to a gaussian vector with the announced covariance matrix. However, for $s\geq 3$, by using Theorem [\[estimate\]](#estimate){reference-type="ref" reference="estimate"}, one sees that $$\begin{aligned}
k_{n,\omega}\left(\varSigma_{\mu^{(i_{1})}},\ldots,\varSigma_{\mu^{(i_{s})}}\right)&=O\left(n^{|\mu^{(i_{1})}|+\cdots+|\mu^{(i_{s})}|-s+1}\right)\\
k_{n,\omega}\left(\sqrt{n}\,\frac{\varSigma_{\mu^{(i_{1})}} }{n^{|\mu^{(i_{1})}|}},\ldots,\sqrt{n}\,\frac{\varSigma_{\mu^{(i_{s})}} }{n^{|\mu^{(i_{s})}|}} \right)&=O\left(n^{1-\frac{s}{2}}\right)\to 0.
\end{aligned}$$ Thus, $V$ converges indeed towards a gaussian vector. To compute the covariances, we use the following trick: $$\begin{aligned}
k_{n,\omega}(\varSigma_{\mu},\varSigma_{\nu})&=\mathbb{E}_{n,\omega}[\varSigma_{\mu}\,\varSigma_{\nu}]-\mathbb{E}_{n,\omega}[\varSigma_{\mu}]\,\mathbb{E}_{n,\omega}[\varSigma_{\nu}]\\
&=\mathbb{E}_{n,\omega}[\varSigma_{\mu}\,\varSigma_{\nu}-\varSigma_{\mu\sqcup \nu}]+\big(\mathbb{E}_{n,\omega}[\varSigma_{\mu\sqcup\nu}]-\mathbb{E}_{n,\omega}[\varSigma_{\mu}]\,\mathbb{E}_{n,\omega}[\varSigma_{\nu}]\big).
\end{aligned}$$ The term of higher degree in the first part of the right-hand side is exactly the expectation of the subdominant term of a product $\varSigma_{\mu}\,\varSigma_{\nu}$. We have calculated this subdominant term after Proposition [\[matching\]](#matching){reference-type="ref" reference="matching"}; hence, $$\begin{aligned}
\mathbb{E}_{n,\omega}[\varSigma_{\mu}\,\varSigma_{\nu}-\varSigma_{\mu\sqcup \nu}]&=\sum_{a \in \mu,b \in \nu}ab\,\,\mathbb{E}_{n,\omega}[\varSigma_{(\mu\sqcup\nu \sqcup \{a+b-1\}) \setminus \{a,b\}}]\\
&\simeq \left(\sum_{a \in \mu,\,b \in \nu}ab\,\, p_{\mu\sqcup\nu \setminus \{a,b\}}(\omega)\,\,p_{a+b-1}(\omega)\right)n^{|\mu|+|\nu|-1}.
\end{aligned}$$ On the other hand, $\mathbb{E}_{n,\omega}[\varSigma_{\mu\sqcup\nu}]-\mathbb{E}_{n,\omega}[\varSigma_{\mu}]\,\mathbb{E}_{n,\omega}[\varSigma_{\nu}]$ is easily computed to be equal to $$p_{\mu \sqcup \nu}(\omega) \,\,\left[n^{\downarrow |\mu|+|\nu|}-n^{\downarrow |\mu|}\,n^{\downarrow |\nu|}\right]\simeq - \,|\mu|\,|\nu|\,\,p_{\mu \sqcup \nu}(\omega) \,\,n^{|\mu|+|\nu|-1}$$ Dividing everything by $n^{|\mu|+|\nu|-1}$ and writing $$|\mu|\,|\nu|\,\,p_{\mu \sqcup \nu}(\omega)=\sum_{a\in \mu,\,b\in \nu}ab\,\,p_{\mu\sqcup\nu \setminus \{a,b\}}(\omega)\,\,p_{a}(\omega)\,p_{b}(\omega),$$ we obtain exactly the announced formula. ◻
:::

So, for any integer $k\geq 2$, if $\sigma$ is a $k$-cycle, then $$\sqrt{n}\,\left(\frac{\chi^{\lambda}(\sigma)-\chi^{\omega}(\sigma)}{k}\right)$$ converges under the laws $\mathbb{P}_{n,\omega}$ to a centered gaussian variable of variance $p_{2k-1}(\omega)-p_{k}(\omega)^{2}$. Again, this result is not precise enough when $\omega=\mathbf{0}$ --- fortunately, this is the only problematic point. Actually, it has been shown in [@IO02 Theorem 6.1] that under Plancherel measures, if $\sigma$ is a $k$-cycle, then $$n^{\frac{k}{2}}\,\left(\frac{\chi^{\lambda}(\sigma)}{\sqrt{k}}\right)$$ converges to a centered gaussian variable of variance $1$. We shall say a little bit more on these kind of results in the conclusion of our paper.

## Gaussian behaviour of the rows and of the columns {#gaussrow}

Now, let us look at the consequences of Theorem [\[mainalg\]](#mainalg){reference-type="ref" reference="mainalg"} for the geometry of the random partitions. First, let us give a central limit theorem for the random measures $X_{\lambda}$ under coherent systems of probability measures $(\mathbb{P}_{n,\omega})_{n \in \mathbb{N}}$. In the following, $\mathscr{C}^{1}([-1,1])$ is endowed with the topology of uniform convergence of the functions and of their derivatives, and measures are now considered as elements of the dual space of $\mathscr{C}^{1}([-1,1])$ --- this dual space contains $\mathscr{P}([-1,1]) \subset \mathscr{M}([-1,1])=\mathscr{C}^{0}([-1,1])^{*}$.

::: theorem
[]{#mainmeasure label="mainmeasure"} We consider the random measure $\nabla_{n,\omega}=\sqrt{n}\,(X_{\lambda}-X_{\omega})$, with $\lambda$ chosen randomly according to $\mathbb{P}_{n,\omega}$. As $n$ goes to infinity, $\nabla_{n,\omega}$ converges to a centered gaussian element $\nabla_{\infty,\omega}$ in $\mathscr{C}^{1}([-1,1])^{*}$, and for any functions $f,g \in \mathscr{C}^{1}([-1,1])$, $$k(\nabla_{\infty,\omega}(f),\nabla_{\infty,\omega}(g))=X_{\omega}((xf(x))'(xg(x))')-X_{\omega}((xf(x))')\,X_{\omega}((xg(x))').$$
:::

::: proof
*Proof.* We have shown in our "algebraic" central limit theorem that the random vector $$\left(\sqrt{n}\,\left(\frac{\varSigma_{k}}{n^{k}} - p_{k}(\omega)\right)\right)_{k\geq 1}$$ converges to a centered gaussian vector with covariance matrix $$lm\,(p_{l+m-1}(\omega)-p_{l}(\omega)\,p_{m}(\omega)).$$ By using the same arguments as before, one can replace $\varSigma_{k}$ by $p_{k}$, and therefore, the same results holds for $$\begin{aligned}
\left(\sqrt{n}\,\left(\frac{p_{k}(\lambda)}{n^{k}}-p_{k}(\omega) \right)\right)_{k \geq 1}&=\left(\sqrt{n}\,\left(X_{\lambda}(x^{k})-X_{\omega}(x^{k}) \right)\right)_{k\geq 0}\\
&=(\nabla_{n,\omega}(x^{k}))_{k\geq 0},
\end{aligned}$$ although with a shift of index: $$k(\nabla_{\infty,\omega}(x^{l}),\nabla_{\infty,\omega}(x^{m}))=(l+1)(m+1)\,(p_{l+m+1}(\omega)-p_{l+1}(\omega)\,p_{m+1}(\omega)).$$ Now, this computation of covariances can be rewritten as: $$\begin{aligned}
k(\nabla_{\infty,\omega}(x^{l}),\nabla_{\infty,\omega}(x^{m}))&=(l+1)(m+1)\,(X_{\omega}(x^{l}\,x^{m})-X_{\omega}(x^{l})\,X_{\omega}(x^{m}))\\
&=X_{\omega}((x^{l+1})'(x^{m+1})')-X_{\omega}((x^{l+1})')\,X_{\omega}((x^{m+1})').
\end{aligned}$$ By multilinearity, for any polynomials $f$ and $g$ in $\mathbb{R}[x]$, $\nabla_{n,\omega}(f)$ and $\nabla_{n,\omega}(g)$ converge towards centered gaussian variables, and the covariance of the limiting distibutions writes as $$k(\nabla_{\infty,\omega}(f),\nabla_{\infty,\omega}(g))=X_{\omega}((xf(x))'(xg(x))')-X_{\omega}((xf(x))')\,X_{\omega}((xg(x))').$$ Finally, one uses the density of $\mathbb{R}[x]$ in $\mathscr{C}^{1}([-1,1])$ to get the same result for any functions $f,g \in \mathscr{C}^{1}([-1,1])$. However, notice that one has first to apply a random version of the Banach-Steinhaus theorem for the (random) linear forms $\nabla_{n,\omega} : \mathscr{C}^{1}([-1,1])\to \mathbb{R}$ (see [@Tha87] or [@VV95]). Indeed, because of the factor $\sqrt{n}$, it is not clear *a priori* that one can get a uniform bound on expressions like $$\sqrt{n}\,\left(X_{\lambda}(f-f_{k})-X_{\omega}(f-f_{k})\right)$$ with $(f_{k})_{k \in \mathbb{N}}$ sequence of polynomials approximating $f$ in $\mathscr{C}^{1}([-1,1])$ --- this point was left unexplained in [@FM10]. ◻
:::

Unfortunately, Theorem [\[mainmeasure\]](#mainmeasure){reference-type="ref" reference="mainmeasure"} is sufficient to describe the fluctuations of the row $\lambda_{i}$ or the column $\lambda_{j}'$ only when $\alpha_{i-1}>\alpha_{i}>\alpha_{i+1}$ or when $\beta_{j-1}>\beta_{j}>\beta_{j+1}$. Indeed, our method of moments will not allow to distinguish at order $\sqrt{n}$ the parts corresponding to equal coordinates. We fix distinct coordinates $\alpha_{i_{1}}\neq \alpha_{i_{2}}\neq \cdots \neq \alpha_{i_{r}}\neq 0$ and $\beta_{j_{1}}\neq \beta_{j_{2}} \neq \cdots \neq \beta_{j_{s}}\neq 0$ of the point $\omega \in \Omega$, and we denote by $m_{k}$ (respectively, $w_{k}$) the multiplicity of $\alpha_{i_{k}}$ (resp., of $\beta_{j_{k}}$), so $$\alpha_{i_{k}-1}>\alpha_{i_{k}}=\alpha_{i_{k}+1}=\cdots=\alpha_{i_{k}+m_{k}-1}>\alpha_{i_{k}+m_{k}}$$ and similarly for $\beta_{j_{k}}$. We then denote $$\begin{aligned}
\Lambda_{i_{k},m_{k},n}&=\sqrt{n}\left( \frac{\lambda_{i_{k}}}{n}+ \frac{\lambda_{i_{k}+1}}{n}+\cdots+ \frac{\lambda_{i_{k}+m_{k}-1}}{n}-m_{k}\,\alpha_{i_{k}}\right);\\
\Lambda_{j_{k},w_{k},n}'&=\sqrt{n}\left( \frac{\lambda_{j_{k}}'}{n}+ \frac{\lambda_{j_{k}+1}'}{n}+\cdots+ \frac{\lambda_{j_{k}+w_{k}-1}'}{n}-w_{k}\,\beta_{j_{k}}\right).
\end{aligned}$$

::: theorem
[]{#almostgeom label="almostgeom"} As $n$ goes to infinity, the random vector $$(\Lambda_{i_{1},m_{1},n},\ldots,\Lambda_{i_{r},m_{r},n},\Lambda_{j_{1},w_{1},n}',\ldots,\Lambda_{j_{s},w_{s},n}')$$ converges to a centered gaussian vector $(\Lambda_{i_{1},m_{1},\infty},\ldots,\Lambda_{j_{s},l_{s},\infty}')$, with the following covariances: $$\begin{aligned}
k(\Lambda_{i_{k},m_{k},\infty},\Lambda_{i_{l},m_{l},\infty})&=\delta_{kl}\,m_{k}\,\alpha_{i_{k}}-m_{k}m_{l}\,\alpha_{i_{k}}\alpha_{i_{l}}\,;\\
k(\Lambda_{j_{k},w_{k},\infty}',\Lambda_{j_{l},w_{l},\infty}')&=\delta_{kl}\,w_{k}\,\beta_{j_{k}}-w_{k}w_{l}\,\beta_{j_{k}}\beta_{j_{l}}\,;\\
k(\Lambda_{i_{k},m_{k},\infty},\Lambda_{j_{l},w_{l},\infty}')&=-m_{k}w_{l}\,\alpha_{i_{k}}\beta_{j_{l}}.
\end{aligned}$$ In particular, if $\alpha_{i}$ and $\alpha_{j}$ are two "isolated" coordinates of the sequence $\alpha$, then the random variables $X_{i,n}=\sqrt{n}\left(\frac{\lambda_{i}}{n}-\alpha_{i}\right)$ and $X_{j,n}=\sqrt{n}\left(\frac{\lambda_{j}}{n}-\alpha_{j}\right)$ converge jointly in law to centered gaussian variables $X_{i,\infty}$ and $X_{j,\infty}$, with $$k(X_{i,\infty},X_{j,\infty})=\delta_{ij}\,\alpha_{i}-\alpha_{i}\alpha_{j}.$$
:::

::: proof
*Proof.* We consider test functions $f_{k}$ and $g_{l}$ such that:

1.  All these functions are in $\mathscr{C}^{1}([-1,1])$, non-negative and with values in $[0,1]$.

2.  For any $k$, there is a neighbourhood $W_{k}=[\alpha_{i_{k}}-\varepsilon_{k},\alpha_{i_{k}}+\varepsilon_{k}]$ of $\alpha_{i_{k}}$ such that $W_{k}$ does not contain any element of the set $\{\alpha_{i\geq 1},-\beta_{j\geq 1},0\} \setminus \{\alpha_{i_{k}}\}$, and the support of $f_{k}$ is contained in $W_{k}$. Moreover, there is a neighboorhood $V_{k}\subset W_{k}$ of $\alpha_{i_{k}}$ such that $f_{|V_{k}}=1$.

3.  Similarly, for any $l$, there is a neighbourhood $W_{l}'=[-\beta_{j_{l}}-\varepsilon_{l}',-\beta_{j_{l}}+\varepsilon_{l}']$ of $-\beta_{j_{l}}$ such that $W_{l}'$ does not contain any element of $\{\alpha_{i\geq 1},-\beta_{j\geq 1},0\} \setminus \{\beta_{j_{l}}\}$, and the support of $g_{l}$ is contained in $W_{l}'$. Moreover, there is a neighboorhood $V_{l}'\subset W_{l}'$ of $-\beta_{j_{l}}$ such that $g_{|V_{l}'}=1$.

<figure>
<div class="center">
<p><span><span> <embed src="graphic_functiontest.pdf" /></span></span></p>
</div>
<figcaption>Test functions for the proof of the geometric central limit theorem.</figcaption>
</figure>

We fix an index $k$. Since $\frac{\lambda_{i}}{n} \to \alpha_{i}$ for all $i$, with probability going to $1$ as $n$ goes to infinity, the intersection of the support of $X_{\lambda}$ with $W_{k}$ consists exactly in $$\left\{\frac{\lambda_{i_{k}}}{n},\frac{\lambda_{i_{k}+1}}{n},\ldots,\frac{\lambda_{i_{k}+m_{k}-1}}{n}\right\},$$ that are even in $V_{k}$ with big probability. So, $$X_{\lambda}(f_{k})=\frac{\lambda_{i_{k}}+ \lambda_{i_{k}+1}+\cdots+\lambda_{i_{k}+m_{k}-1}}{n}$$ with probability going to $1$; on the other hand, $X_{\omega}(f_{k})=m_{k}\,\alpha_{i_{k}}$. Hence, $$\Lambda_{i_{k},m_{k},n}=\nabla_{n,\omega}(f_{k})$$ for any $k$ with probability going to $1$; similarly, $\Lambda_{j_{l},w_{l},n}'=\nabla_{n,\omega}(g_{l})$ with big probability. Then, by Theorem [\[mainmeasure\]](#mainmeasure){reference-type="ref" reference="mainmeasure"}, the random vector of the statement of our theorem converges in law to a centered gaussian vector $$(\Lambda_{i_{1},m_{1},\infty},\ldots,\Lambda_{i_{r},m_{r},\infty},\Lambda_{j_{1},l_{1},\infty}',\ldots,\Lambda_{j_{s},l_{s},\infty}'),$$ with $k(\Lambda_{i_{k},m_{k},\infty},\Lambda_{i_{l},m_{l},\infty})$ equal to $$X_{\omega}((xf_{k}(x))' (xf_{l}(x))')-X_{\omega}((xf_{k}(x))')\,X_{\omega}((xf_{l}(x))'),$$ and the same kind of formula with variables $\Lambda_{j_{k},w_{k},\infty}'$. Now, notice that $f_{k}'(x)=0$ for any $x$ in the support of $X_{\omega}$, and any $k$. Hence, the previous covariance may be written as $$X_{\omega}(f_{k}f_{l})-X_{\omega}(f_{k})\,X_{\omega}(f_{l})=\delta_{kl}\,m_{k}\,\alpha_{i_{k}}-m_{k}m_{l}\,\alpha_{i_{k}}\alpha_{i_{l}},$$ and the proof for the other covariance formulas is the same with functions $g_{l}$ instead of functions $f_{k}$. ◻
:::
