---
doc_id: arxiv-2605.15740v1
doc_title: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants"
section_id: sec-002-21-preliminaries-and-auxiliary-results
section_title: "Preliminaries and auxiliary results"
section_number: 2.1
pages: 6-8
source_pdf: 2605.15740v1.pdf
source_sha256: aa7f99d6633113c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.88
latex_coverage_ratio: 0.853
doc_brief: "Bailey pairs, Eichler integrals and unified Witten-Reshetikhin-Turaev invariants — In 1999, Lawrence and Zagier expressed the Witten-Reshetikhin-Turaev (WRT) invariant of the Poincar´e homology"
---
Recall that a Bailey pair relative to $a$ is a pair of sequences $(\alpha_n,\beta_n)_{n \geq 0}$ satisfying $$\begin{aligned}
\beta_n &= \sum_{k=0}^n \frac{\alpha_k}{(q)_{n-k}(aq)_{n+k}} \label{pairdef} \\
&= \frac{1}{(q)_n(aq)_n} \sum_{k=0}^n \frac{(q^{-n})_k}{(aq^{n+1})_k}(-1)^kq^{nk -\binom{k}{2}} \alpha_k. \label{pairdefbis}
\end{aligned}$$ The first equation is the original definition [@An1], while the second follows from an application of the identity [@Ga-Ra Appendix I, Eq. (I.10)] $$\label{qPochn-k}
(x)_{n-k} = \frac{(x)_n}{(q^{1-n}/x)_k}(-q/x)^kq^{\binom{k}{2} - nk}.$$

We begin by reviewing two important facts about Bailey pairs. First, we require a special case of the Bailey lemma [@An1].

::: lemma
[]{#Baileylemma label="Baileylemma"} If $(\alpha_n,\beta_n)$ is a Bailey pair relative to $a$, then so is $(\alpha_n',\beta_n')$, where $$\label{alphaprime}
\alpha_n' = a^nq^{n^2}\alpha_n$$ and $$\label{betaprime}
\beta_n' = \sum_{j=0}^n \frac{a^jq^{j^2}}{(q)_{n-j}} \beta_j.$$
:::

Second, we have a special case of the Bailey lattice [@Ag-An-Br1].

::: lemma
[]{#Baileylattice label="Baileylattice"} If $(\alpha_n,\beta_n)$ is a Bailey pair relative to $q^2$, then $(\alpha_n^*,\beta_n)$ is a Bailey pair relative to $q$, where $$\label{alphastar}
\alpha_n^* = (1-q^2)\left(\frac{\alpha_n}{1-q^{2n+2}} - \frac{q^{2n}\alpha_{n-1}}{1-q^{2n}} \right).$$ By convention we take $\alpha_{-1} = 0$.
:::

Using Lemmas [\[Baileylemma\]](#Baileylemma){reference-type="ref" reference="Baileylemma"} and [\[Baileylattice\]](#Baileylattice){reference-type="ref" reference="Baileylattice"}, we establish three auxiliary results which will allow us to relate the $q$-multisums in Theorem [\[main\]](#main){reference-type="ref" reference="main"} to polynomial sums at roots of unity. The first result is for Bailey pairs relative to $q$.

::: proposition
[]{#keychainlemma label="keychainlemma"} If $(\alpha_k,\beta_k)$ is a Bailey pair relative to $q$, then for any $p \geq 1$ we have $$\label{keychainlemmaeq}
\begin{aligned}
\sum_{n-1 \geq n_p \geq \cdots \geq n_1\geq 0}& \frac{q^{(n-n_p-1)(n-n_p)}\beta_{n-n_p-1}}{(q)_{n_p}} \prod_{i=1}^{p-1} q^{(n-n_i-1)(n-n_i)} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \\
&= \frac{1}{(q)_{n-1}(q^2)_{n-1}} \sum_{k=0}^{n-1} \frac{(q^{1-n})_k}{(q^{1+n})_k}(-1)^kq^{nk -\binom{k+1}{2} + p(k^2+k)}\alpha_k.
\end{aligned}$$
:::

::: proof
*Proof.* Suppose that $(\alpha_k,\beta_k)$ is a Bailey pair relative to $q$. Iterating [\[alphaprime\]](#alphaprime){reference-type="eqref" reference="alphaprime"} and [\[betaprime\]](#betaprime){reference-type="eqref" reference="betaprime"} $p$ times we obtain another Bailey pair relative to $q$, $$\label{alpha^p}
        \alpha_k^{(p)} = q^{p(k^2+k)}\alpha_k$$ and $$\beta_k^{(p)} = \sum_{k \geq n_p \geq \cdots \geq n_1\geq 0} \frac{q^{n_p(n_p+1) + \cdots + n_1(n_1+1)}}{(q)_{k-n_p} \cdots (q)_{n_2-n_1}} \beta_{n_1}.$$ Now in $\beta_k^{(p)}$ we replace $k$ by $n-1$ and then make the change of indices $n_i \rightarrow n - 1 - n_{p-i+1}$ for $1 \leq i \leq p$. The result is $$\beta_{n-1}^{(p)} = \sum_{n-1 \geq n_p \geq \cdots \geq n_1\geq 0} \frac{q^{(n - n_1 - 1)(n- n_1) + \cdots + (n-n_p-1)(n-n_p)}}{(q)_{n_1} (q)_{n_2-n_1} \cdots (q)_{n_p-n_{p-1}}} \beta_{n -n_p -1}.$$ Multiplying numerator and denominator by $(q)_{n_p}$ and then converting to $q$-binomial coefficients ([\[qbc\]](#qbc){reference-type="ref" reference="qbc"}) gives the left-hand side of [\[keychainlemmaeq\]](#keychainlemmaeq){reference-type="eqref" reference="keychainlemmaeq"}. The right-hand side follows from inserting [\[alpha\^p\]](#alpha^p){reference-type="eqref" reference="alpha^p"} into [\[pairdefbis\]](#pairdefbis){reference-type="eqref" reference="pairdefbis"}. This completes the proof. ◻
:::

Our second auxiliary result is analogous to Proposition [\[keychainlemma\]](#keychainlemma){reference-type="ref" reference="keychainlemma"}, but for Bailey pairs relative to $q^2$. In what follows, we define $a_n^*$ for any sequence $a_n$ by $$\label{astar}
    a_n^* = (1-q^2)\left(\frac{a_n}{1-q^{2n+2}} - \frac{q^{2n}a_{n-1}}{1-q^{2n}} \right)$$ in analogy with [\[alphastar\]](#alphastar){reference-type="eqref" reference="alphastar"}.

::: proposition
[]{#keychainlemmabis label="keychainlemmabis"} If $(\alpha_k,\beta_k)$ is a Bailey pair relative to $q^2$, then for any $p \geq 1$ we have $$\label{keychainlemmabiseq}
\begin{aligned}
\sum_{n-1 \geq n_p \geq \cdots \geq n_1\geq 0}& \frac{q^{(n-n_p-1)(n-n_p+1)}\beta_{n-n_p-1}}{(q)_{n_p}} \prod_{i=1}^{p-1} q^{(n-n_i-1)(n-n_i+1)} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \\
&= \frac{1}{(q)_{n-1}(q^2)_{n-1}} \sum_{k=0}^{n-1} \frac{(q^{1-n})_k}{(q^{1+n})_k}(-1)^kq^{nk -\binom{k+1}{2}} (q^{p(k^2+2k)} \alpha_k)^*.
\end{aligned}$$
:::

::: proof
*Proof.* Suppose that $(\alpha_k,\beta_k)$ is a Bailey pair relative to $q^2$. We argue as in Proposition [\[keychainlemma\]](#keychainlemma){reference-type="ref" reference="keychainlemma"} with the same iterations of [\[alphaprime\]](#alphaprime){reference-type="eqref" reference="alphaprime"} and [\[betaprime\]](#betaprime){reference-type="eqref" reference="betaprime"} (but with $a=q^2$) and the same changes of indices. The result is a Bailey pair relative to $q^2$, $$\label{iteratedalphaq^2}
        \alpha_k^{(p)} = q^{p(k^2+2k)}\alpha_k$$ and $$\label{iteratedbetaq^2}
        \beta_{n-1}^{(p)} = \sum_{n-1 \geq n_p \geq \cdots \geq n_1\geq 0} \frac{q^{(n - n_1 - 1)(n- n_1 +1) + \cdots + (n-n_p-1)(n-n_p+1)}}{(q)_{n_1} (q)_{n_2-n_1} \cdots (q)_{n_p-n_{p-1}}} \beta_{n -n_p +1}.$$ Now we change this to a Bailey pair relative to $q$ using Lemma [\[Baileylattice\]](#Baileylattice){reference-type="ref" reference="Baileylattice"} and then insert it into [\[pairdefbis\]](#pairdefbis){reference-type="eqref" reference="pairdefbis"} to complete the proof. ◻
:::

The third auxiliary result also applies to Bailey pairs relative to $q^2$, but in a different way.

::: proposition
[]{#keychainlemmater label="keychainlemmater"} If $(\alpha_k,\beta_k)$ is a Bailey pair relative to $q^2$, then for any $p \geq 1$ we have $$\label{keychainlemmatereq}
        \begin{aligned}
            \sum_{n-1 \geq n_p \geq \cdots \geq n_1\geq 0}& \frac{q^{(n-n_p-1)(n-n_p+1)}\beta_{n-n_p-1}}{(q)_{n_p}} \prod_{i=1}^{p-1} q^{(n-n_i-1)(n-n_i+1)} \begin{bmatrix} n_{i+1} \\ n_i \end{bmatrix} \\
            &= \frac{(1-q^2)}{(q)_{n-1}(q)_{n}} \sum_{k=0}^{n-1} \frac{(q^{1-n})_k}{(q^{2+n})_k}(-1)^k q^{nk -\binom{k+1}{2} + p(k^2+2k)} \alpha_k.
        \end{aligned}$$
:::

::: proof
*Proof.* This follows from substituting [\[iteratedalphaq\^2\]](#iteratedalphaq^2){reference-type="eqref" reference="iteratedalphaq^2"} and [\[iteratedbetaq\^2\]](#iteratedbetaq^2){reference-type="eqref" reference="iteratedbetaq^2"} into the definition of a Bailey pair in [\[pairdefbis\]](#pairdefbis){reference-type="eqref" reference="pairdefbis"} with $a=q^2$. ◻
:::
