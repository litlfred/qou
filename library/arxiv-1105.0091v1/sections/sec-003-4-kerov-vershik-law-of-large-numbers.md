---
doc_id: arxiv-1105.0091v1
doc_title: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra"
section_id: sec-003-4-kerov-vershik-law-of-large-numbers
section_title: "Kerov-Vershik law of large numbers"
section_number: 4
pages: 31-36
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.99
doc_brief: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra — In this paper, we review the representation theory of the inﬁnite symmetric group, and"
---
[]{#largenumbers label="largenumbers"} In this section, we recall the results of Kerov and Vershik; although nothing is new here, we shall introduce the important concept of a (random) probability measure associated to a (random) diagram, that will later prove useful for the analysis of the fluctuations of the rows and columns, see §[\[gaussrow\]](#gaussrow){reference-type="ref" reference="gaussrow"}.

## Law of large numbers for the irreducible characters

Given an irreducible character $\chi^{\omega}$, we replace it on $\mathfrak{S}_{n}$ by the random function $\chi^{\lambda}$, where $\lambda$ is taken according to the probability measure $\mathbb{P}_{n,\omega}$. The law of large numbers of Kerov and Vershik ensures that $\chi^{\lambda}$ converges to $\chi^{\omega}$:

::: theorem
[]{#llnalg label="llnalg"} For any permutation $\sigma \in \mathfrak{S}_{\infty}$, $$\chi^{\lambda}(\sigma) \longrightarrow_{\mathbb{P}_{n,\omega}} \chi^{\omega}(\sigma),$$ where the long right arrow means that one has convergence in probability.
:::

::: proof
*Proof.* For any partition $\mu$, $\mathbb{E}_{n,\omega}\!\left[\frac{\varSigma_{\mu}}{n^{|\mu|}}\right]\simeq p_{\mu}(A-B+\gamma E)$, and $$\begin{aligned}
\mathbb{E}_{n,\omega}\!\left[\left(\frac{\varSigma_{\mu}}{n^{|\mu|}}\right)^{2}\right]&=\mathbb{E}_{n,\omega}\!\left[\frac{\varSigma_{\mu \sqcup \mu}}{n^{2|\mu|}}\right]+\frac{1}{n^{2|\mu|}}\,\mathbb{E}_{n,\omega}[\text{obs. of degree at most }2|\mu|-1]\\
&= \left(p_{\mu}(A-B+\gamma E)\right)^{2}+O(n^{-1})\simeq \left(p_{\mu}(A-B+\gamma E)\right)^{2}.
\end{aligned}$$ Here, we have used the estimate $\mathbb{E}_{n,\omega}[X]=O(n^{\deg X})$ mentioned at the end of the previous paragraph, the factorization property of the symbols $\varSigma_{\mu}$ in higher degree, and the computation of the expectations $\mathbb{E}_{n,\omega}[\varSigma_{\mu}]$ performed at the end of §[\[polfunc\]](#polfunc){reference-type="ref" reference="polfunc"}. Because of Bienaymé-Chebyshev inequality, these two estimates ensure that $\frac{\varSigma_{\mu}}{n^{|\mu|}}\simeq \chi^{\lambda}(\mu \sqcup 1^{n-|\mu|})$ converges in probability towards $p_{\mu}(A-B+\gamma E)=\chi^{\omega}(\mu)$. ◻
:::

Again, Theorem [\[llnalg\]](#llnalg){reference-type="ref" reference="llnalg"} can be given an uniform flavour: namely, for any $\sigma \in \mathfrak{S}_{\infty}$, and any $\varepsilon>0$, $$\sup_{\omega \in \Omega} \mathbb{P}_{n,\omega}[|\chi^{\lambda}(\sigma)-\chi^{\omega}(\sigma)|\geq \varepsilon] \to_{n \to \infty} 0.$$ On the other hand, we shall see in Section [\[clt\]](#clt){reference-type="ref" reference="clt"} that in fact, a much stronger result holds: for any permutation $\sigma$, the renormalized difference $\sqrt{n}\,(\chi^{\lambda}(\sigma)-\chi^{\omega}(\sigma))$ converges in law towards a centered gaussian variable. Now, let us remark that for any $k$, $$\mathbb{E}_{n,\omega}\!\left[\left(\frac{p_{k}-\varSigma_{k}}{n^{k}}\right)^{2}\right]=\frac{\mathbb{E}_{n,\omega}[\text{obs. of degree at most }2k-2]}{n^{2k}}=O(n^{-2}) \to 0.$$ So, Theorem [\[llnalg\]](#llnalg){reference-type="ref" reference="llnalg"} implies that for any $k\geq 1$, and any $\omega \in \Omega$, $$\frac{p_{k}(\lambda)}{n^{k}} \longrightarrow_{\mathbb{P}_{n,\omega}} p_{k}(A-B+\gamma E).$$ We are now going to interpret this result in geometric terms, thereby proving a law of large numbers for the first rows $\lambda_{1},\lambda_{2},\ldots$ and the first columns $\lambda_{1}',\lambda_{2}',\ldots$ of a random partition $\lambda$ chosen according to a law $\mathbb{P}_{n,\omega}$.

## Random measures associated to random partitions

We denote by $\mathscr{P}([-1,1])$ the set of borelian probability measures on the interval $[-1,1]$; this is a metrizable compact set for Skorohod's topology of weak convergence, see [@Bil69 Chapter 1]. A distance compatible with this topology is provided by any dense sequence of functions in the space of continuous (real-valued) functions $\mathscr{C}([-1,1])$ --- by Stone-Weierstrass theorem, such a sequence $(f_{n})_{n \in \mathbb{N}}$ exists, and we can for instance take $\{f_{n}\}_{n \in \mathbb{N}}=\mathbb{Q}[x]$. Thus, $$d(m_{1},m_{2})=\sum_{n=0}^{\infty}\frac{1}{2^{n}} \min(1,|m_{1}(f_{n})-m_{2}(f_{n})|)$$ is a distance on $\mathscr{P}([-1,1])$ that defines the topology of weak convergence[^1]. Now, to any partition $\lambda$ of size $n$, we associate a probability measure $X_{\lambda} \in \mathscr{P}([-1,1])$: $$X_{\lambda}=\sum_{i=1}^{d} \frac{a_{i}}{n}\,\delta_{\left(\frac{a_{i}}{n}\right)}+\sum_{i=1}^{d} \frac{b_{i}}{n}\,\delta_{\left(-\frac{b_{i}}{n}\right)},$$ where the $a$'s and the $b$'s are the Frobenius coordinates of $\lambda$. Notice that the moments of $X_{\lambda}$ are up to a shift of index the renormalized Frobenius moments of $\lambda$: $$\forall k \geq 0,\,\,\,X_{\lambda}(x^{k})=\frac{p_{k+1}(\lambda)}{n^{k+1}}.$$ If $\lambda$ is random, we will then consider $X_{\lambda}$ as a **random measure**, that is to say a random point of the space $\mathscr{P}([-1,1])$.

If $\omega =((\alpha_{1},\alpha_{2},\ldots),(\beta_{1},\beta_{2},\ldots))$ is a point of the Thoma simplex $\Omega$, we can also associate to it a probability measure $X_{\omega} \in \mathscr{P}([-1,1])$: $$X_{\omega}=\sum_{i=1}^{\infty} \alpha_{i}\,\delta_{(\alpha_{i})}+\sum_{i=1}^{\infty} \beta_{i}\,\delta_{(-\beta_{i})} + \gamma \,\delta_{0}.$$ The moments of $X_{\omega}$ are up to a shift of index the specializations of the power sums on the formal alphabet $A-B+\gamma E$: $$\forall k \geq 0,\,\,\, X_{\omega}(x^{k})=p_{k+1}(A-B+\gamma E).$$ We have seen in the previous paragraph that under the coherent system of measures $\mathbb{P}_{n,\omega}$, $\frac{p_{k}(\lambda)}{n^{k}}$ converges in probability towards $p_{k}(A-B+\gamma E)$ for any $k$. Consequently, $$\forall k \geq 0,\,\,\, X_{\lambda}(x^{k}) \longrightarrow_{\mathbb{P}_{n,\omega}} X_{\omega}(x^{k}).$$ By linearity, we have the same result for any evaluation of the measures on a polynomial in $\mathbb{Q}[x]$, and since $\mathbb{Q}[x]$ is dense in $\mathscr{C}([-1,1])$, we conclude that:

::: proposition
For the topology of weak convergence, $$X_{\lambda}\longrightarrow_{\mathbb{P}_{n,\omega}} X_{\omega}.$$
:::

More concretely, for *any* function $f \in \mathscr{C}([-1,1])$ and any $\varepsilon>0$, $\mathbb{P}_{n,\omega}[|X_{\lambda}(f)-X_{\omega}(f)|\geq \varepsilon] \to 0$. In fact, these convergences are again uniform on the Thoma simplex: $$\sup_{\omega \in \Omega}\mathbb{P}_{n,\omega}[|X_{\lambda}(f)-X_{\omega}(f)|\geq \varepsilon]\to_{n \to \infty} 0.$$

Finally, let us translate the Kerov-Vershik law of large numbers in terms of the asymptotic geometry of the random partitions. From the result on random measures, it is easy to guess that the following should be true:

::: theorem
[]{#llngeom label="llngeom"} Take $\lambda$ randomly according to a measure $\mathbb{P}_{n,\omega}$, with $\omega=(\alpha,\beta)$. $$\forall i \geq1,\,\,\,\frac{\lambda_{i}}{n}\simeq \frac{a_{i}}{n} \longrightarrow_{\mathbb{P}_{n,\omega}} \alpha_{i}\qquad;\qquad \forall j \geq1,\,\,\,\frac{\lambda_{j}'}{n}\simeq \frac{b_{j}}{n} \longrightarrow_{\mathbb{P}_{n,\omega}} \beta_{j}.$$
:::

::: proof
*Proof.* One of the main difficulty when recovering the shapes of the partitions is that we have to take account of the multiplicities of the coordinates $\alpha_{i},\beta_{j}$ of the point $\omega \in \Omega$. Let us prove rigorously that if $\alpha_{1}=\alpha_{2}=\cdots=\alpha_{m}>\alpha_{m+1}$ are the biggest coordinates of $\alpha$, then the renormalized $m$ first parts of $\lambda$ converge in probability to the value $\alpha_{1}$. We fix $\varepsilon>0$, and we split the proof in two parts.

1.  First, let us prove that $\frac{a_{1}}{n}$ is smaller than $\alpha_{1}+2\varepsilon$ with probability going to $1$ as $n$ goes to infinity (of course, we suppose $\alpha_{1}<1$, this case being obvious). We consider a test function $f_{\varepsilon}^{+}$ that takes its values in $[0,1]$, is continuous, and is equal to $1$ after $\alpha_{1}+2\varepsilon$ and to $0$ before $\alpha_{1}+\varepsilon$ (see Figure [1](#functionplus){reference-type="ref" reference="functionplus"}). On the one hand, $X_{\omega}(f_{\varepsilon}^{+})=0$, and on the other hand, $$X_{\lambda}(f_{\varepsilon}^{+})\geq (\alpha_{1}+2\varepsilon)\,\,\mathrm{card}\,\left\{i \,\,\big|\,\, \frac{a_{i}}{n} \geq \alpha_{1}+2\varepsilon\right\}.$$ Since $X_{\lambda}(f_{\varepsilon})$ converges in probability to $X_{\omega}(f_{\varepsilon}^{+})=0$, this implies that the cardinality is equal to $0$ for $n$ big enough and with big probability.

    <figure id="functionplus">
    <div class="center">
    <p><span><span> <embed src="graphic_functionplus.pdf" /></span></span></p>
    </div>
    <figcaption>Test function <span class="math inline"><em>f</em><sub><em>ε</em></sub><sup>+</sup></span>.<span id="functionplus" label="functionplus"></span></figcaption>
    </figure>

2.  Similarly, let us prove that $\frac{a_{m}}{n}$ is bigger than $\alpha_{1}-2\varepsilon$ with probability going to $1$ as $n$ goes to infinity (again, we suppose that $\alpha_{1}>0$, this case being obvious). We consider a test function $f_{\varepsilon}^{-}$ that takes its values in $[0,1]$, is continuous, and is equal to $1$ after $\alpha_{1}-\varepsilon$ and to $0$ before $\alpha_{1}-2\varepsilon$ (see Figure [2](#functionminus){reference-type="ref" reference="functionminus"}).

    <figure id="functionminus">
    <div class="center">
    <p><span><span> <embed src="graphic_functionminus.pdf" /></span></span></p>
    </div>
    <figcaption>Test function <span class="math inline"><em>f</em><sub><em>ε</em></sub><sup>−</sup></span>.<span id="functionminus" label="functionminus"></span></figcaption>
    </figure>

    For $\varepsilon$ small enough, we may also suppose that $\alpha_{1}-2\varepsilon>\alpha_{m+1}$. Then, $X_{\omega}(f_{\varepsilon}^{-})=m\alpha_{1}$, whereas $$X_{\lambda}(f_{\varepsilon}^{-}) \leq (\alpha_{1}+2\varepsilon) \,\,\mathrm{card}\,\left\{i \,\,\big|\,\, \frac{a_{i}}{n} \geq \alpha_{1}-2\varepsilon\right\}$$ with big probability --- indeed, we already know that the $a_{i}$'s are smaller than $\alpha_{1}+2\varepsilon$ with probability almost $1$. For $\varepsilon$ small enough and as $n$ goes to infinity, this leads to the inequality $\mathrm{card}\,\{i \,\,|\,\, \frac{a_{i}}{n} \geq \alpha_{1}-2\varepsilon\} \geq m$, which is equivalent to ask that $\frac{a_{m}}{n} \geq \alpha_{1}-2\varepsilon$.

Thus, for any $\varepsilon>0$, the probability of the event $$\alpha_{1}+2\varepsilon\geq \frac{a_{1}}{n}\geq \cdots \geq \frac{a_{m}}{n} \geq \alpha_{1}-2\varepsilon$$ goes to $1$ as $n$ goes to infinity, which is exactly Theorem [\[llngeom\]](#llngeom){reference-type="ref" reference="llngeom"} for the $m$ first rows of $\lambda$. Now, an induction enables us to treat the other rows, and the columns are treated exactly the same way. ◻
:::

::: example
When $\omega=\mathbf{0}$, the law of large numbers ensures that all the rows of $\lambda$ are some $o(n)$, and similarly for its columns. Actually, it is a well-known fact that the rows and the columns have order of magnitude $\sqrt{n}$, and that there is a limit shape for the random partitions under Plancherel measures after scaling the Young diagrams in both directions by the factor $\sqrt{n}$ (*cf.* [@LS77; @KV77]):

<figure>
<div class="center">
<p><span><span> <embed src="graphic_plancherel.pdf" /></span></span></p>
</div>
<figcaption>Random partition under the Plancherel measure <span class="math inline">ℙ<sub><em>n</em>, <strong>0</strong></sub> = ℙ<sub><em>n</em></sub></span>.</figcaption>
</figure>

Hence, for this particular point of $\Omega$, the law of large numbers is not precise enough; however, an accurate law of large numbers and a central limit theorem can be proved in this case (and for other classes of measures on partitions) by a slight modification of the tools that we use here (see [@IO02; @Mel11]). Another important example is when $\omega=(\alpha,\beta)$ with $\alpha$ and $\beta$ geometric progressions of same ratio $q$. However, these examples are better understood in the setting of the Hecke algebras, see Section [\[qtplancherel\]](#qtplancherel){reference-type="ref" reference="qtplancherel"}.
:::

To conclude this section, let us interpret the geometric law of large numbers in terms of properties of $\omega$-shuffles. We fix an integer $r$. Given a shuffle $\sigma$ of $n_{1}+n_{2}+\cdots+m_{1}+m_{2}+\cdots+l$ cards as in §[\[riffleshuffle\]](#riffleshuffle){reference-type="ref" reference="riffleshuffle"}, it is obvious that the maximal sum $$\ell(iw_{1})+\ell(iw_{2})+\cdots+\ell(iw_{r})$$ of the lengths of $r$ disjoint increasing subwords in $\sigma$ is at least $n_{1}+n_{2}+\cdots+n_{r}$. Indeed, it suffices to consider the words $$iw_{j}=\left[\!\left[n_{1}+\cdots+n_{j-1}+1,n_{1}+\cdots+n_{j}\right]\!\right],$$ because they stay in this order in $\sigma$.

::: example
Take $r=1$, $n=9=5+4$. Any shuffle of $12345$ and $6789$ contains an increasing subword of length at least $5$, namely, $12345$. However, for many shuffles, one can do better: for instance, $162378495$ is a shuffle of $12345$ with $6789$, and it contains an increasing subword of length $6$, namely, $123789$.
:::

Thus, the $r$-th Greene invariant of $\sigma$, which we shall denote by $GI_{r}(\sigma)$, is bigger than $n_{1}+\cdots+n_{r}$. Now, if the sizes of the blocks are taken according to a multinomial law of parameter $(\alpha,\beta,\gamma)$, then the law of large numbers ensures that $\frac{n_{i}}{n}$ converges in probability to $\alpha_{i}$. Thus, with probability going to $1$, if $\sigma$ is a permutation obtained by an $\omega$-shuffle, then $$\frac{GI_{r}(\sigma)}{n} \geq \alpha_{1}+\cdots + \alpha_{r}-\varepsilon$$ for any $\varepsilon>0$. However, one could imagine that "many" $\omega$-shuffles yield permutations with greater Greene invariants (this impression may be strengthened by the randomized block of size $l\simeq n\gamma$). The Kerov-Vershik law of large numbers and Propositions [\[frompermtopar\]](#frompermtopar){reference-type="ref" reference="frompermtopar"} and [\[apocalyptica\]](#apocalyptica){reference-type="ref" reference="apocalyptica"} ensure that it is not the case:

::: proposition
Let $\sigma$ be a permutation of size $n$ chosen randomly according to $\mathbb{Q}_{n,\omega}$. As $n$ goes to infinity, $$\frac{GI_{r}(\sigma)}{n} \longrightarrow_{\mathbb{Q}_{n,\omega}} \alpha_{1}+\cdots+\alpha_{r}.$$ Of course, the same holds if one replaces the increasing subwords by the decreasing subwords and the $\alpha$'s by the $\beta$'s.
:::

::: proof
*Proof.* Because of Proposition [\[frompermtopar\]](#frompermtopar){reference-type="ref" reference="frompermtopar"}, the distribution of $GI_{r}(\sigma)$ under $\mathbb{Q}_{n,\omega}$ is the same as the distribution of $\lambda_{1}+\cdots+\lambda_{r}$ under $\mathbb{P}_{n,\omega}$. Then, it suffices to apply Theorem [\[llngeom\]](#llngeom){reference-type="ref" reference="llngeom"}. ◻
:::

Hence, $\omega$-shuffles do not create bigger increasing subwords than those given by the sizes of the blocks. In Section [\[clt\]](#clt){reference-type="ref" reference="clt"}, we are going to prove a central limit theorem that will improve this result. Hence, assuming that the $\alpha_{i}$'s are all distinct, up to order $\sqrt{n}$ (and not $n$), the asymptotic distribution of $GI_{r}(\sigma)$ is the same as the asymptotic distribution of the size $n_{1}+\cdots+n_{r}$ of the $r$ first blocks of the $\omega$-shuffle, that is to say $$n\,(\alpha_{1}+\cdots+\alpha_{r})+\sqrt{n}\,\sqrt{(\alpha_{1}+\cdots+\alpha_{r})(1-\alpha_{1}-\cdots-\alpha_{r})}\,\,\mathcal{N}(0,1)+o(\sqrt{n})$$ with $\mathcal{N}(0,1)$ a standard gaussian variable.

[^1]: Here, for any $f \in \mathscr{C}([-1,1])$ and any $m \in \mathscr{P}([-1,1])$, $m(f)=\int_{-1}^{1} f(x) \,m(dx)$.
