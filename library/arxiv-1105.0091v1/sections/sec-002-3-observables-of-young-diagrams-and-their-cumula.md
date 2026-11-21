---
doc_id: arxiv-1105.0091v1
doc_title: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra"
section_id: sec-002-3-observables-of-young-diagrams-and-their-cumula
section_title: "Observables of Young diagrams and their cumulants"
section_number: 3
pages: 22-31
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.989
doc_brief: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra — In this paper, we review the representation theory of the inﬁnite symmetric group, and"
---
[]{#obs label="obs"} For the asymptotic analysis of Young diagrams, we are basically going to use a method of moments, but we have to define precisely what we mean by the moments of a partition. We shall essentially follow [@IO02], and [@Sni06b; @FM10] for the combinatorics of cumulants.

## Polynomial functions on Young diagrams {#polfunc}

If $\lambda$ is a partition, we associate to it two finite alphabets $A(\lambda)$ and $B(\lambda)$ called the **Frobenius coordinates**: $$\begin{aligned}
A(\lambda)&=\left\{\lambda_{1}-\frac{1}{2},\lambda_{2}-\frac{3}{2},\ldots,\lambda_{d}-\frac{2d-1}{2}\right\};\\
B(\lambda)&=A(\lambda')=\left\{\lambda_{1}'-\frac{1}{2},\lambda_{2}'-\frac{3}{2},\ldots,\lambda_{d}'-\frac{2d-1}{2}\right\}.
\end{aligned}$$ Here, $d$ is the size of the diagonal of $\lambda$, that is to say the number of boxes of the Young diagram of $\lambda$ that belong to the first diagonal.

::: example
If $\lambda=(6,3,2,2)$, its Young diagram is $$\yng(2,2,3,6)$$ and the Frobenius coordinates are $A=\{\frac{11}{2},\frac{3}{2}\}$ and $B=\{\frac{7}{2},\frac{5}{2}\}$ --- they are easily computed by drawing the diagonal and measuring the rows and columns starting from the diagonal.
:::

The **Frobenius moments** of $\lambda$ are the power sums $$p_{k}(\lambda)=p_{k}\left(A(\lambda)-\overline{B}(\lambda)\right)=\left(\sum_{i=1}^{d}a_{i}^{k}\right)+(-1)^{k-1}\left(\sum_{i=1}^{d}b_{i}^{k}\right).$$ For instance, $p_{1}(\lambda)=|\lambda|$ for any partition. The functions $p_{k}$ generate freely over $\mathbb{C}$ an algebra called the algebra of **observables of diagrams**, and denoted $\mathscr{O}$ (*cf.* [@KO94; @IO02]). This algebra is isomorphic to $\mathbf{Sym}$, and it is naturally graded by $\deg p_{k}=k$. It does not contain all the polynomial functions of the coordinates of the partitions, but it will prove sufficiently large[^1] in our setting.

We now define new functions on Young diagrams by renormalizing the values of the irreducible characters of the symmetric groups. Recall that for any partitions $\lambda,\mu$ of the same size, $\chi^{\lambda}(\mu)$ denotes the value of the *normalized* irreducible character of $\mathfrak{S}_{n}$ of label $\lambda$ on a permutation of cycle type $\mu$; thus, $\zeta^{\lambda}(\mu)=(\dim \lambda)\,\chi^{\lambda}(\mu)$. Then, for any partitions $\lambda,\mu$, we set: $$\varSigma_{\mu}(\lambda)=\begin{cases}
n(n-1)\ldots (n-|\mu|+1)\,\chi^{\lambda}(\mu \sqcup 1^{n-|\mu|}) &\text{if }n=|\lambda|\geq |\mu|,\\
0&\text{otherwise}.
\end{cases}$$ For convenience, we will denote $n(n-1)\cdots (n-k+1)=n^{\downarrow k}$ for any $n$ and $k$ --- this is the Pochhammer symbol for falling factorials. Thus, $\varSigma_{\mu}(\lambda)=|\lambda|^{\downarrow |\mu|}\,\chi^{\lambda}(\mu \sqcup 1^{|\lambda|-|\mu|})$. An essential result exposed in details in [@IO02] is the following:

::: theorem
[]{#ivanovolshanski label="ivanovolshanski"} Viewed as a function on Young diagrams, $\varSigma_{\mu}$ is an element of $\mathscr{O}$, and is of degree $|\mu|$. Moreover, $$\forall \mu,\,\,\,\varSigma_{\mu}=p_{\mu}+(\text{terms of degree at most } |\mu|-1),$$ see [@IO02 Proposition 3.4].
:::

::: example
Actually, there is an explicit formula for the $\varSigma_{k}$'s that is due to Wassermann ([@Was81], [@IO02 Proposition 3.3]). Hence, one can compute $\varSigma_{1}=p_{1}$, $\varSigma_{2}=p_{2}$, $\varSigma_{3}=p_{3}-\frac{3}{2}p_{11}+\frac{5}{4}p_{1}$, $\varSigma_{4}=p_{4}-4p_{21}+\frac{11}{2}p_{2}$.
:::

Theorem [\[ivanovolshanski\]](#ivanovolshanski){reference-type="ref" reference="ivanovolshanski"} implies in particular that the symbols $\varSigma_{\mu}$ factorize in higher degree, that is to say that for any partitions $\mu$ and $\nu$, $$\varSigma_{\mu}\,\varSigma_{\nu}=\varSigma_{\mu \sqcup \nu}+(\text{terms of degree at most }|\mu|+|\nu|-1).$$ The next paragraph is devoted to a better description of the products $\varSigma_{\mu}\,\varSigma_{\nu}$; we shall rely on the formalism of partial permutations (*cf.* [@IK99]). To conclude this paragraph, let us compute the expectation of a symbol $\varSigma_{\mu}(\lambda)$ when $\lambda$ is chosen randomly according to a measure $\mathbb{P}_{n,\omega}$ (we suppose that $n \geq |\mu|$): $$\begin{aligned}
\mathbb{E}_{n,\omega}[\varSigma_{\mu}(\lambda)]&=n^{\downarrow |\mu|} \, \sum_{\lambda \in \mathfrak{Y}_{n}} \mathbb{P}_{n,\omega}[\lambda]\,\,\chi^{\lambda}(\mu \sqcup 1^{n-|\mu|})\\
&=n^{\downarrow |\mu|} \, \sum_{\lambda \in \mathfrak{Y}_{n}} s_{\lambda}(A-B+\gamma E)\,\,\zeta^{\lambda}(\mu \sqcup 1^{n-|\mu|})\\
&=_{(\text{Frobenius formula})}n^{\downarrow |\mu|}\,p_{\mu \sqcup 1^{n-|\mu|}}(A-B+\gamma E)\\
&=n^{\downarrow |\mu|}\,p_{\mu}(A-B+\gamma E).
\end{aligned}$$ Theorem [\[ivanovolshanski\]](#ivanovolshanski){reference-type="ref" reference="ivanovolshanski"} implies that $(\varSigma_{\mu})_{\mu \in \mathfrak{Y}}$ is a linear basis of $\mathscr{O}$; hence, by using this simple formula, we will be able to compute the expectation of *any* observable of diagrams under a coherent measure $\mathbb{P}_{n,\omega}$. In particular, we shall compute in Sections [\[largenumbers\]](#largenumbers){reference-type="ref" reference="largenumbers"} and [\[clt\]](#clt){reference-type="ref" reference="clt"} the joint moments of the Frobenius observables $p_{k}$; they will provide information on the geometry of the random partitions under the probability measures $\mathbb{P}_{n,\omega}$.

## Ivanov-Kerov algebra of partial permutations

If $\sigma \in \mathfrak{S}_{\infty}$, we call admissible set for $\sigma$ a finite subset $S \subset \mathbb{N}^{*}$ such that if $x \notin S$, then $\sigma(x)=x$. A **partial permutation** is a pair $(\sigma,S)$ with $S$ admissible set for $\sigma$. Said in other words, a partial permutation is a subset $S \subset\mathbb{N}^{*}$ and a permutation $\sigma \in \mathfrak{S}(S)$. One can multiply these objects by the rule $$(\sigma,S)\times(\tau,T)=(\sigma\tau,S\cup T).$$ We denote $\deg (\sigma,S)=\mathrm{card}\,S$, and we construct a graded algebra $\mathscr{A}_{\infty}$ by looking at all the formal linear combinations of partial permutations with bounded degree. For any $n$, this algebra $\mathscr{A}_{\infty}$ can be projected onto the group algebra $\mathbb{C}\mathfrak{S}_{n}$: $$\begin{aligned}
\pi_{n} : \mathscr{A}_{\infty}&\to \mathbb{C}\mathfrak{S}_{n}\\
(\sigma,S)&\mapsto \begin{cases}
\sigma &\text{if }S \subset \left[\!\left[1,n\right]\!\right],\\
0 &\text{otherwise}.
\end{cases}
\end{aligned}$$ There is a natural action of $\mathfrak{S}_{\infty}$ on $\mathscr{A}_{\infty}$: on the basis elements $(\sigma,S)$, it is defined by $$(\sigma,S)^{\tau}=(\tau\sigma\tau^{-1},\tau(S)),$$ and it is compatible with the product of partial permutations. Moreover, two partial permutations $(\sigma,S)$ and $(\tau,T)$ are conjugated if and only if $\mathrm{card}\,S=\mathrm{card}\,T$, and the cyclic type of $\sigma_{|S}$ is the same as the cyclic type of $\tau_{|T}$. Thus, the invariant algebra $\mathscr{B}_{\infty}=(\mathscr{A}_{\infty})^{\mathfrak{S}_{\infty}}$ (called the **Ivanov-Kerov algebra**) has a linear basis labelled by partitions of arbitrary size: $$\mathscr{B}_{\infty}=\mathrm{Vect}((A_{\lambda})_{\lambda \in \mathfrak{Y}}),\quad\text{with }A_{\mu}=\sum_{|S|=|\mu|}\sum_{\substack{\sigma \in \mathfrak{S}(S)\\ t(\sigma)=\mu}}(\sigma,S).$$ Actually, we would rather use a renormalized version of this basis, defined as follows: $$\varSigma_{\mu}=\sum\left[(a_{11},\ldots,a_{1\mu_{1}})(a_{21},\ldots,a_{2\mu_{2}})\cdots(a_{r1},\ldots,a_{r\mu_{r}}), \{a_{ij} \}_{\substack{1 \leq i \leq \ell(\mu) \\ 1\leq j \leq \mu_{i}}}\right]$$ where the sum is taken over injective $\mathbb{N}^{*}$-valued functions $i,j \mapsto a_{ij}$ with $1 \leq i \leq \ell(\mu)$ and $1\leq j \leq \mu_{i}$.

::: proposition
[]{#fringe label="fringe"} The family $(\varSigma_{\mu})_{\mu \in \mathfrak{Y}}$ is a linear basis of $\mathscr{B}_{\infty}$, and for any $n$ and any partition $\lambda \in \mathfrak{Y}_{n}$, $$\varSigma_{\mu}(\lambda)=\chi^{\lambda}(\pi_{n}(\varSigma_{\mu})).$$
:::

::: proof
*Proof.* Here, an irreducible character $\chi^{\lambda}$ is extended by linearity from the group $\mathfrak{S}_{n}$ to the algebra $\mathbb{C}\mathfrak{S}_{n}$. It is not hard to see that $\varSigma_{\mu}$ is a multiple of $A_{\mu}$ for any partition $\mu$; hence, $(\varSigma_{\mu})_{\mu}$ is indeed a linear basis of $\mathscr{B}_{\infty}$. Now, for any $n$, $\pi_{n}(\varSigma_{\mu})$ consists in $n^{\downarrow |\mu|}$ elements of $\mathfrak{S}_{n}$ of cycle type $\mu \sqcup 1^{n-|\mu|}$, corresponding to all the possible $|\mu|$-arrangements of the $a_{ij}$'s. Hence, $$\chi^{\lambda}(\pi_{n}(\varSigma_{\mu}))=n^{\downarrow |\mu|}\,\chi^{\lambda}(\mu \sqcup 1^{n-|\mu|})=\varSigma_{\mu}(\lambda).$$ ◻
:::

Now, Proposition [\[fringe\]](#fringe){reference-type="ref" reference="fringe"} allows to compute a product of two symbols $\varSigma$ in $\mathscr{B}_{\infty}$ instead of $\mathscr{O}$. Indeed, for any partitions $\lambda,\mu,\nu$, $$\begin{aligned}
\varSigma_{\mu}(\lambda) \,\varSigma_{\nu}(\lambda)&=\chi^{\lambda}(\pi_{n}(\varSigma_{\mu}))\,\,\chi^{\lambda}(\pi_{n}(\varSigma_{\nu}))=\chi^{\lambda}(\pi_{n}(\varSigma_{\mu}) \, \pi_{n}(\varSigma_{\nu}))\\
&=\chi^{\lambda}(\pi_{n}(\varSigma_{\mu}\times_{\mathscr{B}_{\infty}} \varSigma_{\nu}))=(\varSigma_{\mu}\times_{\mathscr{B}_{\infty}} \varSigma_{\nu})(\lambda)
\end{aligned}$$ where we used the fact that for any elements $a,b$ of the center $Z(\mathbb{C}\mathfrak{S}_{n})$ of the group algebra, and any normalized irreducible character $\chi^{\lambda}$ of $\mathfrak{S}_{n}$, $\chi^{\lambda}(ab)=\chi^{\lambda}(a)\,\chi^{\lambda}(b)$ --- this is true for any finite group. With this new point of view, the combinatorics of the symbols $\varSigma$ has been investigated by P. Śniady in [@Sni06a; @Sni06b], and later by V. Féray and the author in [@FM10]. Thus, one can give a semi-explicit description of a product $\varSigma_{\mu}\,\varSigma_{\nu}$ by using **partial matchings**. To this purpose, let us introduce some additional notations. We denote by $\mathfrak{A}_{k}$ the set of $k$-arrangements of integers in $\mathbb{N}^{*}$, and if $A=(a_{1},\ldots,a_{k})\in \mathfrak{A}_{k}$, we denote by $C(A)$ the corresponding $k$-cycle, viewed as a partial permutation with support $\{a_{1},\ldots,a_{k}\}$. Then, $\varSigma_{\mu}$ can be rewritten as $$\varSigma_{\mu}=\sum_{\substack{\forall i,\,\,A_{i} \in \mathfrak{A}_{\mu_{i}} \\ \forall i \neq j,\,\,A_{i} \cap A_{j}=\emptyset}}C(A_{1})\,C(A_{2})\,\cdots \,C(A_{\ell(\mu)}),$$ and given two partitions $\mu$ and $\nu$, $$\varSigma_{\mu}\,\varSigma_{\nu}=\!\!\sum_{\substack{\forall i,\,\,A_{i} \in \mathfrak{A}_{\mu_{i}} \\ \forall i \neq j,\,\,A_{i} \cap A_{j}=\emptyset}}\,\,\,\sum_{\substack{\forall k,\,\,B_{k} \in \mathfrak{A}_{\nu_{k}} \\ \forall k \neq l,\,\,B_{k} \cap B_{l}=\emptyset}} \!\!C(A_{1})\,\cdots \,C(A_{\ell(\mu)})\,C(B_{1})\,\cdots \,C(B_{\ell(\nu)}).$$ To any sequences $(a_{ij})_{i,j}$ and $(b_{kl})_{k,l}$ appearing in this expression, we associate a partial matching of the set $I_{A}$ of the $(i,j)$'s with the set $I_{B}$ of the $(k,l)$'s: $$(i,j) \sim (k,l)\text{ if }a_{ij}=b_{kl}.$$ Then, given a partial matching $M$ of $I_{A}$ with $I_{B}$, if we sum the products $$C(A_{1})\,\cdots \,C(A_{\ell(\mu)})\,C(B_{1})\,\cdots \,C(B_{\ell(\nu)})$$ corresponding to this partial matching, we obtain a term $\varSigma_{\rho(M,\mu,\nu)}$: indeed, if one knows which of the $a_{ij}$'s are equal to which of the $b_{kl}$'s, then one can rewrite the product as a product of *disjoint* cycles in a way that does not depend on the values of the $a$' and the $b$'s (*cf.* [@FM10 §3.4]). Thus:

::: lemma
[]{#matching label="matching"} For any partition $\mu$ and $\nu$, $$\varSigma_{\mu}\,\varSigma_{\nu}=\sum_{M} \varSigma_{\rho(M,\mu,\nu)}$$ where the sum runs over all the partial matchings $M$ of $I_{A}$ with $I_{B}$.
:::

We refer again to [@FM10] for more details on this combinatorial lemma. The reader should also notice that the degree of a term $\varSigma_{\rho(M,\mu,\nu)}$ corresponding to a partial matching $M$ is $|\mu|+|\nu|-|M|$, where $|M|$ is the size of the partial matching, that is to say the number of pairs $(a \in I_{A},b \in I_{B})$ in $M$.

::: example
Let us compute the term of higher degree and the subdominant term of a product $\varSigma_{\mu}\,\varSigma_{\nu}$.

0.  If $\deg \varSigma_{\rho(M,\mu,\nu)}=|\mu|+|\nu|$, then $|M|=0$, and $M=\emptyset$. The cycles corresponding to the empty matching are disjoint ones; thus, the only term of degree $|\mu|+|\nu|$ in $\varSigma_{\mu}\,\varSigma_{\nu}$ is indeed $\varSigma_{\mu \sqcup \nu}$.

1.  If $\deg \varSigma_{\rho(M,\mu,\nu)}=|\mu|+|\nu|-1$, then $|M|=1$ and $M$ contains only one pair $(a,b)$. Suppose that $a$ is in a cycle $C(A_{i})$ of length $\mu_{i}$, and that $b$ is in a cycle $C(B_{j})$ of length $\nu_{j}$. Then, $C(A_{i})$ and $C(B_{j})$ intersect in exactly one point, so their product is a $(\mu_{i}+\nu_{j}-1)$-cycle; and all the other cycles $C(A_{i'})$ or $C(B_{j'})$ stay disjoint. Thus, such a matching yields a term $$\varSigma_{(\mu\sqcup \nu \sqcup \{\mu_{i}+\nu_{j}-1\})\setminus \{\mu_{i},\nu_{j}\} },$$ and one has to sum over all possible matchings of size $1$ to get the subdominant term of $\varSigma_{\mu}\,\varSigma_{\nu}$.

So, for any partitions $\mu=(\mu_{1},\ldots,\mu_{r})$ and $\nu=(\nu_{1},\ldots,\nu_{s})$, $$\varSigma_{\mu}\,\varSigma_{\nu}=\varSigma_{\mu \sqcup \nu}+\sum_{i=1}^{r}\sum_{j=1}^{s} \mu_{i}\nu_{j}\,\varSigma_{(\mu\sqcup \nu \sqcup \{\mu_{i}+\nu_{j}-1\})\setminus \{\mu_{i},\nu_{j}\} }$$ plus an observable of degree at most $|\mu|+|\nu|-2$. In particular, for two symbols $\varSigma_{l}$ and $\varSigma_{m}$ corresponding to cycles, $$\varSigma_{l}\,\varSigma_{m}=\varSigma_{l,m}+lm\,\varSigma_{l+m-1}+(\text{observable of degree at most }l+m-2).$$
:::

## Śniady's theory of cumulants of observables

In order to prove results of asymptotic gaussian behaviour in the setting of the representation theory of $\mathfrak{S}_{\infty}$, we shall use in Section [\[clt\]](#clt){reference-type="ref" reference="clt"} Śniady's theory of **cumulants of observables** (*cf.* [@Sni06a; @Sni06b]), though in a setting that is slightly different from the setting of his papers, and with another gradation on the algebra $\mathscr{O}$. If $X_{1},\ldots,X_{r}$ are real random variables defined on a common probability space, we recall that their **joint cumulant** is defined by: $$k(X_{1},X_{2},\ldots,X_{r})=\left.\frac{\partial^{r}}{\partial t_{1}\partial t_{2}\cdots \partial t_{r}} \right|_{t=0}\log \mathbb{E}\left[\exp(t_{1}X_{1}+t_{2}X_{2}+\cdots+t_{r}X_{r})\right].$$ In particular, $k(X)=\mathbb{E}[X]$ is the expectation and $k(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\,\mathbb{E}[Y]$ is the covariance. With the definition given above, it is obvious that a gaussian vector $X=(X_{1},\ldots,X_{n})$ is characterized by the vanishing of all the joint cumulants of the coordinates of order $r\geq 3$. On the other hand, one can give an equivalent combinatorial definition of the joint cumulants. For any integer $n$, we denote by $\mathfrak{P}_{n}$ the set of **set partitions** of $\left[\!\left[1,n\right]\!\right]$, and if $\pi=\pi_{1}\sqcup \pi_{2}\sqcup\cdots \sqcup \pi_{s}$ is such a set partition, we denote $\ell(\pi)=s$ and $\mu(\pi)=(-1)^{\ell(\pi)-1}\,(\ell(\pi)-1)!$. Then, $$k(X_{1},X_{2},\ldots,X_{r})=\sum_{\pi \in \mathfrak{P}_{r}} \mu(\pi) \,\left(\prod_{i=1}^{\ell(\pi)}\,\mathbb{E}\!\left[\prod_{j \in \pi_{i}} X_{j}\right]\right).$$

::: example
For instance, when $r=3$, one has to sum over the $5$ set partitions of $\mathfrak{P}_{3}$, and $k(X,Y,Z)$ is equal to $$\mathbb{E}[XYZ]-\mathbb{E}[XY]\,\mathbb{E}[Z]-\mathbb{E}[XZ]\,\mathbb{E}[Y]-\mathbb{E}[YZ]\,\mathbb{E}[X]+2\,\mathbb{E}[X]\,\mathbb{E}[Y]\,\mathbb{E}[Z].$$
:::

Now, in the algebra of observables of diagrams $\mathscr{O}$, we can in fact define three kind of cumulants. First, if $\mathbb{P}$ is a probability law on partitions, then any $X \in \mathscr{O}$ can be considered as a random variable $X(\lambda)$, and one can define the joint cumulant of observables $X_{1},\ldots,X_{r}$. That said, one can define on $\mathscr{O}\simeq \mathscr{B}_{\infty}$ a new product $\bullet$, called **disjoint product**, and given by the following rule: $$\forall \mu,\nu,\,\,\,\varSigma_{\mu}\bullet \varSigma_{\nu}=\varSigma_{\mu\sqcup \nu}.$$ This new product is the restriction to $\mathscr{B}_{\infty}$ of the disjoint product of partial permutations: $$(\sigma,S)\bullet (\tau,T)=\begin{cases}(\sigma\tau,S\sqcup T)&\text{if }S\cap T=\emptyset,\\
0&\text{otherwise}.
\end{cases}$$ We will denote by $\mathscr{O}^{\bullet}$ the algebra of observables endowed with this new product. The **disjoint cumulant** of some observables $X_{1},\ldots,X_{r}$ is then defined exactly in the same way as for the standard cumulant: $$k^{\bullet}(X_{1},X_{2},\ldots,X_{r})=\sum_{\pi \in \mathfrak{P}_{r}} \mu(\pi) \,\left(\prod_{i\leq \ell(\pi)}\,\mathbb{E}\!\left[\prod_{j \in \pi_{i}}^{\bullet} X_{j}\right]\right).$$ Finally, we define the **identity cumulant** of observables $X_{1},\ldots,X_{r}$ as the new observable $$k^{\mathrm{id}} (X_{1},X_{2},\ldots,X_{r})=\sum_{\pi \in \mathfrak{P}_{r}} \mu(\pi) \,\left(\prod_{i \leq \ell(\pi)}^{\bullet}\,\left[\prod_{j \in \pi_{i}} X_{j}\right]\right).$$ The three kind of cumulants are related by the following identity, that can be understood as a computation of expectation *via* conditioning, see [@Bri69] and [@Sni06b Lemma 4.8]: $$k(X_{1},\ldots,X_{r})=\sum_{\pi \in \mathfrak{P}_{r}} k^{\bullet}\left(k^{\mathrm{id}}(X_{j \in \pi_{1}}),k^{\mathrm{id}}(X_{j \in \pi_{2}}),\ldots,k^{\mathrm{id}}(X_{j \in \pi_{\ell(\pi)}})\right).$$

The expansion of an identity cumulant $k^{\mathrm{id}}(\varSigma_{l_{1}},\ldots,\varSigma_{l_{r}})$ in partial permutations has been computed in [@FM10 Lemma 19]. Given arrangements $A_{1},\ldots,A_{r}$, we define a relation $\sim$ by $i \sim j \iff A_{i}\cap A_{j}\neq \emptyset$. The transitive cloture of $\sim$ is an equivalence relation, and we denote by $\pi(A_{1},\ldots,A_{r})$ the corresponding set partition in $\mathfrak{P}_{r}$.

::: lemma
[]{#identitycumulant label="identitycumulant"} For any $l_{1},\ldots,l_{r}$, $$k^{\mathrm{id}}(\varSigma_{l_{1}},\ldots,\varSigma_{l_{r}})=\sum_{\substack{\forall i,\,\,A_{i} \in \mathfrak{A}_{l_{i} } \\ \pi(A_{1},\ldots,A_{r})=\left[\!\left[1,r\right]\!\right]}} C(A_{1})\,C(A_{2})\,\cdots\,C(A_{r}).$$
:::

::: proof
*Proof.* The three kind of cumulants can be defined inductively by the relations: $$\begin{aligned}
X_{1}X_{2}\cdots X_{r}&=\sum_{\pi \in \mathfrak{P}_{r}} k^{\mathrm{id}}(X_{j \in \pi_{1}})\bullet k^{\mathrm{id}}(X_{j \in \pi_{2}})\bullet \cdots \bullet k^{\mathrm{id}}(X_{j \in \pi_{\ell(\pi)}})\,;\\
\mathbb{E}[X_{1}X_{2}\cdots X_{r}]&=\sum_{\pi \in \mathfrak{P}_{r}} k(X_{j \in \pi_{1}})\, k(X_{j \in \pi_{2}})\,\cdots \, k(X_{j \in \pi_{\ell(\pi)}})\,;\\
\mathbb{E}[X_{1}\bullet X_{2}\bullet \cdots \bullet X_{r}]&=\sum_{\pi \in \mathfrak{P}_{r}} k^{\bullet}(X_{j \in \pi_{1}})\, k^{\bullet}(X_{j \in \pi_{2}})\,\cdots \, k^{\bullet}(X_{j \in \pi_{\ell(\pi)}}).
\end{aligned}$$ In particular, the first relation enables us to prove Proposition [\[identitycumulant\]](#identitycumulant){reference-type="ref" reference="identitycumulant"} by induction on $r$, see [@FM10 Lemma 19]. ◻
:::

Now, the degree in $\mathscr{O}\simeq \mathscr{B}_{\infty}$ is the restriction of the degree $\deg(\sigma,S)=|S|$ of the algebra of partial permutations $\mathscr{A}_{\infty}$. However, in any product of cycles appearing in the expansion of $k^{\mathrm{id}} (\varSigma_{l_{1}},\ldots,\varSigma_{l_{r}})$, the joint support of the cycles $C(A_{1}),\ldots,C(A_{r})$ has for cardinality at most $l_{1}+l_{2}+\cdots+l_{r}-(r-1)$ --- this is imposed by the condition $\pi(A_{1},\ldots,A_{r})=\left[\!\left[1,r\right]\!\right]$. Hence, Proposition [\[identitycumulant\]](#identitycumulant){reference-type="ref" reference="identitycumulant"} implies that $$\forall l_{1},\ldots,l_{r},\,\,\,\deg k^{\mathrm{id}}(\varSigma_{l_{1}},\ldots,\varSigma_{l_{r}}) \leq l_{1}+\cdots+l_{r}-(r-1).$$ This leads to the following estimate, that will be crucial in the proof of our central limit theorem for the irreducible characters of $\mathfrak{S}_{\infty}$.

::: theorem
[]{#estimate label="estimate"} For $\omega \in \Omega$, we denote by $k_{n,\omega}$ and $k_{n,\omega}^{\bullet}$ the cumulant and the disjoint cumulant of observables with respect to the expectation $\mathbb{E}_{n,\omega}$. For any observables $X_{1},\ldots,X_{r}$, $$\begin{aligned}
k_{n,\omega}^{\bullet}(X_{1},\ldots,X_{r})&=O\left(n^{\deg X_{1} +\cdots+\deg X_{r}-r+1}\right);\\
k_{n,\omega}(X_{1},\ldots,X_{r})&=O\left(n^{\deg X_{1} +\cdots+\deg X_{r}-r+1}\right). 
\end{aligned}$$
:::

::: proof
*Proof.* Because of the multilinearity of cumulants and of some compatibility relation with respect to the products (see [@Sni06b Theorem 4.4]), it is sufficient to prove these estimates for an algebraic basis of $\mathscr{O}^{\bullet}$ or $\mathscr{O}$, so we will suppose in the following that $X_{i}=\varSigma_{l_{i}}$ with positive integers $l_{1},\ldots,l_{r}\geq 1$. Now, notice that for any partition $\mu$, $$\mathbb{E}_{n,\omega}[\varSigma_{\mu}]=p_{\mu}(A-B+\gamma E)\,\,n^{\downarrow |\mu|}=p_{\mu}(A-B+\gamma E)\,\,\mathbb{E}_{n,\omega}[\varSigma_{1^{|\mu|}}].$$ Thus, one can rewrite a disjoint cumulant $k_{n,\omega}^{\bullet}(\varSigma_{l_{1}},\ldots,\varSigma_{l_{r}})$ as follows: $$\begin{aligned}
k_{n,\omega}^{\bullet}(\varSigma_{l_{1}},\ldots,\varSigma_{l_{r}})&=\sum_{\pi \in \mathfrak{P}_{r}}\mu(\pi)\,\left(\prod_{i\leq \ell(\pi)}\,\mathbb{E}_{n,\omega}\!\left[\prod_{j \in \pi_{i}}^{\bullet} \varSigma_{l_{j}}\right]\right)\\
&\!\!\!\!\!\!\!\!\!\!\!\!=p_{l_{1},\ldots,l_{r}}(A-B+\gamma E) \,\,\sum_{\pi \in \mathfrak{P}_{r}}\mu(\pi)\,\left(\prod_{i\leq \ell(\pi)}\,\mathbb{E}_{n,\omega}\!\left[\prod_{j \in \pi_{i}}^{\bullet} \varSigma_{1^{l_{j}}}\right]\right)\\
&\!\!\!\!\!\!\!\!\!\!\!\!=p_{l_{1},\ldots,l_{r}}(A-B+\gamma E)\,\,k_{n,\omega}^{\bullet}(\varSigma_{1^{l_{1}}},\ldots,\varSigma_{1^{l_{r}}}).
\end{aligned}$$ So, in order to prove the estimate for disjoint cumulants, it is sufficient to treat the case of observables $\varSigma_{1^{l}}$. However, for these observables, the expectation $\mathbb{E}_{n,\omega}[\varSigma_{1^{l}}]=n^{\downarrow l}$ does not depend on $\omega$, and the estimate is simply an algebraic result on the degree of some polynomial combinations of falling factorials of $n$. It has been proved in [@Sni06b Lemma 4.8] that: $$k^{\bullet}_{n}(\varSigma_{1^{l_{1}}},\ldots, \varSigma_{1^{l_{r}}})=O\left(n^{l_{1}+\cdots+l_{r}-r+1}\right).$$ Thus, the proof is complete for the disjoint cumulants. As for the standard cumulants, one uses the aforementioned formula: $$k_{n,\omega}(X_{1},\ldots,X_{r})=\sum_{\pi \in \mathfrak{P}_{r}} k^{\bullet}_{n,\omega}\left(k^{\mathrm{id}}(X_{j \in \pi_{1}}),k^{\mathrm{id}}(X_{j \in \pi_{2}}),\ldots,k^{\mathrm{id}}(X_{j \in \pi_{\ell(\pi)}})\right).$$ Since the estimate for disjoint cumulants has been proved, it suffices now to show that for any set partition $\pi \in \mathfrak{P}_{r}$, $$\left(\sum_{i=1}^{\ell(\pi)} \deg k^{\mathrm{id}}(X_{j} \in \pi_{i})\right)- \ell(\pi)+1 \leq \deg X_{1} +\cdots+\deg X_{r} -r+1.$$ This is trivial because of Proposition [\[identitycumulant\]](#identitycumulant){reference-type="ref" reference="identitycumulant"}: $$\begin{aligned}
\sum_{i=1}^{\ell(\pi)} \deg k^{\mathrm{id}}(X_{j} \in \pi_{i})&\leq \sum_{i=1}^{\ell(\pi)} \left(\sum_{j \in \pi_{i}} \deg X_{i}-|\pi_{i}|+1\right)\\
&\leq\deg X_{1}+\cdots+\deg X_{r}-r+\ell(\pi).
\end{aligned}$$ Notice that the estimates of our Theorem can be made independent of $\omega$: indeed, for any integers $l_{1},\ldots,l_{r}$, $|p_{l_{1},\ldots,l_{r}}(A-B+\gamma E)|\leq 1$, and these quantities are the only ones that depend explicitly on $\omega$ in our proof. ◻
:::

A particular case of Theorem [\[estimate\]](#estimate){reference-type="ref" reference="estimate"} is when $r=1$; thus, $\mathbb{E}_{n,\omega}[X]=O(n^{\deg X})$ for any observable $X$. This simple fact and the multiplicativity of the irreducible characters of $\mathfrak{S}_{\infty}$ will now be used in Section [\[largenumbers\]](#largenumbers){reference-type="ref" reference="largenumbers"}, in which we shall recall the results of Kerov and Vershik (see [@KV81a]) and their proofs.

[^1]: However, we should mention that there is a bigger algebra of observables of diagrams that contains $\mathscr{O}$, is isomorphic to $\mathbf{QSym}$ and allows to decompose the observables of $\mathscr{O}$ in combinatorial summands; see in particular [@DFS10].
