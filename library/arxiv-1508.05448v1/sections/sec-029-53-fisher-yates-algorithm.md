---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-029-53-fisher-yates-algorithm
section_title: "Fisher-Yates Algorithm"
section_number: 5.3
pages: 105-110
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.984
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
The Fisher-Yates algorithm is a method of obtaining a uniform random permutation from a finite set. The algorithm was first introduced by Fisher and Yates in [@FisherYates]. Their original introduction of the algorithm was as a \"paper and pencil\" type algorithm for generating a random permutation of $n$ numbers by hand. The algorithm was first presented as a computer algorithm by Durstenfeld [@Durstenfeld] and became more widely known in a work by Knuth [@Knuth].

The algorithm consists of the following four steps:

::: fy
**Fisher Yates Algorithm 1**. * \
*1) Set a counting variable $j$ to be equal to $1$. Let $n$ denote the length of the desired sequence. We will let $L$ be a sequence which holds our permutation. We will begin by letting $L=(1)$.\
2) Let $m=i+1$. Pick an integer uniformly at random between $1$ and $m$. Call this integer $k$.\
3) If $k=m$, then append $k$ to the end of the list $L$. Otherwise, insert $m$ into $L$ at position $k$.\
4) Increase $i$ by $1$. If $i<n$, then return to step 2. Otherwise, the algorithm is complete.**
:::

To see this algorithm in action, we will do an example for $n=4$. To begin with, $i=1$ and $L=(1)$. To generate our random integers for this example, we used the Python generator *random.randint()*.\
\
**Iteration 1**\
1) $i=1$ and $L=1$.\
2) Since $m=i+1$, $m=2$. Generating a random integer between $1$ and $2$, we get $k=2$.\
3) Since $k=m$, we append $k$ to the end of $L$, giving $L=(1,2)$.\
4) We increase $i$ to $2$, and since $i<n$, we go back to step $2$ for another iteration.\
\
**Iteration 2**\
2) $i=2$, so $m=3$. Generating a random number between $1$ and $3$, we get $k=2$.\
3) Since $k<m$, we insert $m$ into position $k$ in the list. This gives $L=(1,3,2)$.\
4) Increasing $i$ by $1$, we have $i=3$, which is still less than $n$, so we go on for another iteration.\
\
**Iteration 3**\
2) $i=3$, $m=4$.\
3) We generate a random number between $1$ and $4$ and get $k=3$. Since $k<m$, we insert $4$ into position $3$, which gives $L=(1,3,4,2)$.\
4) Once we increase $i$ by $1$, we notice that $i=4$, and so the algorithm terminates.\
\
We end up with $L=(1,3,4,2)$ as our random permutation. A Python code for performing this algorithm on a computer is given in the appendix.\
\
As mentioned, this algorithm shuffles the numbers $(1,\dots,n)$ uniformly, so that each permutation is equally likely. Since we are trying to simulate a Mallows random permutation, we have adapted this algorithm to return a permutation distributed according to the Mallows measure.

::: fy2
**Fisher Yates Algorithm for a Mallows Permutation 1**. * \
*

**For a permutation of length $n$, with Mallows parameter $q$, we have the following algorithm to generate a Mallows distributed random permutation.\
\
1) Begin with $i=1$ and $L=(1)$.\
2) Let $m=i+1$ and let $k$ be a random integer distributed according to a geometric distribution with probability $p=1-q$.\
3) Let $j=1+((k-1)\%m)$, where by $\%m$, we mean modulo $m$.\
4) If $j=1$, append $m$ to the end of the list $L$. Otherwise, insert $m$ into $L$ at position $m+1-j$.\
5) Increment $i$ by $1$. If $i<n$, go back to step 2. Otherwise, the algorithm terminates.**
:::

We will not go through an example here, as this algorithm runs very similarly to the uniform Fisher Yates algorithm. Since it may not be obvious, we will prove why this modified algorithm generates a random permutation distributed according to the Mallows measure.

::: thm
The modified Fisher Yates algorithm stated above does give a permutation distributed according to the Mallows measure.
:::

::: proof
*Proof.* Recall that the Mallows measure is given by $$\mathbb{P}_{n,q}(\pi)=\frac{q^{\mathrm{Inv}(\pi)}}{Z_{n,q}}$$ where $$Z_{n,q}=\prod_{k=1}^n\frac{1-q^k}{1-q}$$ We will prove the theorem by induction. We will start with the case $n=2$. In this case, the only possible permutations are $(1,2)$ and $(2,1)$. Based on the Mallows measure, $$\mathbb{P}\left \{(1,2)\right\}=\frac{1-q}{1-q^2}$$ and $$\mathbb{P}\left\{(2,1)\right\}=\frac{q(1-q)}{1-q^2}$$ Consider our algorithm. We always start with $(1)$. In this case, we will either be adding $2$ at the end of the permutation, or we will be inserting $2$ into slot $1$, giving us $(2,1)$. Given the algorithm above, if $j=1$, then we will get $(1,2)$ and if $j=2$ we have $(2,1)$. $j=1$ only if $k=1,3,5,...$. Using the fact that $k$ is a geometric random variable, we have $$\mathbb{P}\left\{(1,2)\right\}=\mathbb{P}\{j=1\}=\mathbb{P}\{k\; \mathrm{is} \;\mathrm{odd}\}$$ $$=\sum_{i=0}^{\infty}(1-q)q^{2i}$$ $$=\frac{1-q}{1-q^2}$$ as desired. On the other hand $$\mathbb{P}\{(2,1)\}=\mathbb{P}\{j=2\}=\mathbb{P}\{k\; \mathrm{is}\;\mathrm{even}\}$$ $$=\sum_{i=0}^{\infty}(1-q)q^{2k+1}$$ $$=\frac{q(1-q)}{1-q^2}$$ This completes the proof of the base case.

For the inductive step, suppose that for a permutation of length $n$, the algorithm does in fact give a permutation distributed according to the Mallows measure. In other words, letting $\pi$ be a permutation of length $n$, we know that $$\mathbb{P}_{n,q}(\pi)=\frac{q^{\mathrm{Inv}(\pi)}}{\prod_{k=1}^n\frac{1-q^k}{1-q}}$$ Suppose now that $\pi '$ is the same permutation as $\pi$, except with the element $n+1$ added in via the algorithm given. We need to prove that $$\mathbb{P}_{n+1}(\pi)=\frac{q^{\mathrm{Inv}(\pi)}q^{\mathrm{Inv}_{n+1}(\pi ')}}{\prod_{k=1}^{n+1}\frac{1-q^k}{1-q}}$$ where $\mathrm{Inv}_{n+1}(\pi ')$ denotes the number of inversions caused by the element $n+1$. We can assume that we have run our algorithm successfully up until $n$ and just need to perform the last step of the algorithm to add in $n+1$. In this case, $i=n$ and $m=n+1$. If $j=1$, we know that adding in $n+1$ will cause no additional inversions, so $q^{\mathrm{Inv}_{n+1}(\pi ')}=1$. $j=1$ only if $k-1$ is a multiple of $n+1$. Using the fact that $k$ is a geometric variable, we have $$\mathbb{P}\{j=1\}=\mathbb{P}\{(k-1)\%(n+1)=0\}$$ $$=\sum_{i=0}^{\infty}q^{i(n+1)}(1-q)=\frac{1-q}{1-q^{n+1}}$$ This implies that $$\mathbb{P}_{n+1}(\pi')=\frac{q^{\mathrm{Inv}(\pi)}}{\prod_{k=1}^{n+1}\frac{1-q^k}{1-q}}$$ as desired (since adding in the last point did not cause any additional inversions).

Now suppose that $j=2$. This implies that $(k-1)\%(n+1)=1$. This will occur only if $k=\ell(n+1)+1$ for some integer $\ell$. If $j=2$, then $\mathrm{Inv}_{n+1}(\pi ')=1$, since $n+1$ will only cause an inversion with an element in the $n$th position. We have $$\mathbb{P}\{j=2\}=\sum_{i=0}^{\infty} q^{i(n+1)+1}(1-q)=\frac{q(1-q)}{1-q^{n+1}}$$ and in this case, we have $$\mathbb{P}_{n+1}(\pi)=\frac{q^{\mathrm{Inv}(\pi)}q}{\prod_{k=1}^{n+1}\frac{1-q^k}{1-q}}$$ as desired.

This pattern will continue in general. Suppose that adding in $n+1$ causes $I$ inversions. Then, we know that it must have been added in at position $n+1-I$. From the algorithm, this means that $j=I+1$. This will occur only if $(k-1)\%(n+1)=I$. In this case $$\mathbb{P}\{j=I+1\}=\sum_{i=0}^{\infty}q^{i(n+1)+I}(1-q)=\frac{q^I(1-q)}{1-q^{n+1}}$$ From this, we have $$\mathbb{P}_{n+1}(\pi')=\frac{q^{\mathrm{Inv}(\pi)}q^{I}}{\prod_{k=1}^{n+1}\frac{1-q^k}{1-q}}$$ which completes the proof. ◻
:::
