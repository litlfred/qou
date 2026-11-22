---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-007-5-combinatorial-proof-of-an-identity-related-to
section_title: "Combinatorial proof of an identity related to the Jacobi Triple Product"
section_number: 5
pages: 13-16
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
toc_source: outline
text_source: latex
latex_prose_ratio: 0.872
latex_coverage_ratio: 0.939
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on truncated"
---
[]{#sec-JTP label="sec-JTP"}

In this section we give both analytic and combinatorial proofs of an identity which includes as particular cases the conjectural identities (6.7), (6.10), (6.12), (6.13) in [@M1].

First, we recall the Jacobi Triple Product identity in its general form. See, for example, [@KK] where a combinatorial proof is provided. For integers $m$ and $s$ such that $0<s<m$, and complex numbers $q$ and $z$ with $|q|<1$ and $z\neq 0$, we have $$\label{JTP} (zq^s,z^{-1}q^{m-s}, q^m;q^m)_\infty=\sum_{i=-\infty}^\infty(-z)^iq^{m(i^2-i)/2+si}.$$

::: theorem
[]{#T-gen label="T-gen"}Let $m, s$ be positive integers such that $m\geq 2$ and $0<s<m$. Then, $$\label{I6.7-gen}\frac{(q^s,q^{2m-s},q^{2m};q^{2m})_\infty(q^{2m-2s},q^{2m+2s} ;q^{4m})_\infty}{(q^s, q^{m-s};q^{m})_\infty}=\sum_{n=-\infty}^\infty q^{n(mn+s)}.$$
:::

::: corollary
If $m=5$, then for $s=1,2,3,4$, we obtain the respective identities (6.7), (6.10), (6.12), (6.13) in [@M1].
:::

::: remark
In [@KMR], the authors point out that identities (6.7), (6.10), (6.12), (6.13) in [@M1] follow from the Jacobi Triple Product identity.
:::

::: proof
*Analytic proof.* Since $$\begin{aligned}
(q^s;q^{m})_\infty& =(q^s;q^{2m})_\infty(q^{m+s};q^{2m})_\infty\\ (q^{2m+2s};q^{4m})_\infty& =  (q^{m+s};q^{2m})_\infty(-q^{m+s};q^{2m})_\infty,
\end{aligned}$$ to prove identity [\[I6.7-gen\]](#I6.7-gen){reference-type="eqref" reference="I6.7-gen"}, we need to show that $$\begin{aligned}
\label{eq_staircase}(-q^{m+s};q^{2m})_\infty(-q^{m-s};q^{2m})_\infty(q^{2m};q^{2m})_\infty=\sum_{n=-\infty}^\infty q^{n(mn+s)},
  
\end{aligned}$$ which is precisely [\[JTP\]](#JTP){reference-type="eqref" reference="JTP"} with $q$ replaced by $q^2$ and $z$ replaced by $-q^{m-s}$. ◻
:::

::: proof
*Combinatorial proof.* To simplify the exposition, we first define a sign reversing involution to prove combinatorially the trivial cancellation $$\frac{(q;q)_\infty}{(q;q)_\infty}=1.$$ We say that an involution defined on a set of pairs (or tuples) of partitions is sign reversing, if the involution changes the parity of the length of the first partition in each pair (or tuple). Let $\mathcal{QP}(n)$ be the set of pairs of partitions $(\lambda, \mu)\vdash n$ with $\lambda$ a distinct partition and $\mu$ an unrestricted partition. The map $F:\mathcal{QP}(n)\setminus \{(\emptyset, \emptyset)\} \to \mathcal{QP}(n)\setminus \{(\emptyset, \emptyset)\}$ defined by $$F(\lambda, \mu)=\begin{cases}(\lambda\cup(\mu_1), \mu\setminus(\mu_1)) & \text{ if } \lambda_1<\mu_1 \\ (\lambda\setminus(\lambda_1), \mu\cup(\lambda_1)) & \text{ if } \lambda_1 \geq \mu_1 \end{cases}$$ is a sign reversing involution. Recall that, following our convention, if $\nu=\emptyset$, then $\nu_1=0$. Since $(q;q)_\infty/(q;q)_\infty$ is the generating function for $$qp_{e-o}(n):=|\{(\lambda, \mu)\in \mathcal{QP}(n), \ell(\lambda) \textrm{ even}\}|-|\{(\lambda, \mu)\in \mathcal{QP}(n), \ell(\lambda) \textrm{ odd}\}|,$$ this completes the argument.

We continue with the combinatorial proof of Theorem [\[T-gen\]](#T-gen){reference-type="ref" reference="T-gen"}.

If $m=2$, then [\[I6.7-gen\]](#I6.7-gen){reference-type="eqref" reference="I6.7-gen"} becomes $$\label{I6.7-2}\frac{(q,q^{3},q^{4};q^{4})_\infty(q^{2},q^{6} ;q^{8})_\infty}{(q;q^{2})^2_\infty}=\sum_{n=-\infty}^\infty q^{n(2n+1)}.$$ Using the transformation $F$ above on pairs of partitions with odd parts, we have that [\[I6.7-2\]](#I6.7-2){reference-type="eqref" reference="I6.7-2"} is equivalent to $$\label{I6.7-2'}\frac{(q^{2};q^{2})_\infty}{(q;q^{2})_\infty}=\sum_{n=0}^\infty q^{n(n+1)/2}.$$ This is Gauss's identity [@A72 Identity (1.3)] with $q$ replaced by $-q$. However, since $\ell_o(\lambda)\equiv |\lambda| \mod 2$, Andrews' combinatorial proof of Gauss' identity given in [@A72] also proves [\[I6.7-2\]](#I6.7-2){reference-type="eqref" reference="I6.7-2"} combinatorially.

For the remainder of the proof let $m\geq 3$.

Denote by $\mathcal A(n)$ the set consisting of pairs of partitions $(\lambda, \mu)\vdash n$ such that

-   $\lambda$ is a partition with distinct parts congruent to $0$, $s$ or $-s$ modulo $2m$ or congruent to $2m+2s$ or $2m-2s$ modulo $4m$;

-   $\mu$ is a partition with parts congruent to $s$ or $-s$ modulo $m$. (Thus, $\mu$ has parts congruent to $s,m+s,-s$ or $m-s$ modulo $2m$.)

Define $$\mathcal A_e(n):=\{(\lambda, \mu)\in \mathcal A(n) \mid \ell(\lambda) \text{ even}\}$$ and $$\mathcal A_o(n):=\{(\lambda, \mu)\in \mathcal A(n) \mid \ell(\lambda) \text{ odd}\}.$$

The left hand side of [\[I6.7-gen\]](#I6.7-gen){reference-type="eqref" reference="I6.7-gen"} is the generating function for the sequence $a_{e-o}(n):=|\mathcal A_e(n)|-|\mathcal A_o(n)|$.

We define a sign reversing involution $\varphi$ on a subset of $\mathcal A(n)$.

If $(\lambda, \mu)\in \mathcal A(n)$, we write $$\lambda=\lambda^{0,2m}\cup \lambda^{\pm s,2m}\cup\lambda^{\pm(2m+2s), 4m},\hspace{.1in}\mu= \mu^{\pm s,2m}\cup \mu^{\pm(m+s),2m}$$ and we consider several cases.

[Case 1:]{.underline} $\lambda^{\pm s,2m}\cup \mu^{\pm s,2m}\neq \emptyset$ (i.e., there is at least one part congruent to $\pm s\pmod{2m}$ in $\lambda$ or in $\mu$). Define $\varphi(\lambda, \mu):=F(\lambda, \mu)$.

Hence, $\varphi$ is a sign reversing involution on the subset of pairs $(\lambda, \mu)$ in $\mathcal A(n)$ with $\lambda^{\pm s, 2m}\cup \mu^{\pm s, 2m}\neq \emptyset$.

[Case 2:]{.underline} $\lambda^{\pm s,2m}\cup \mu^{\pm s,2m}= \emptyset$ and ($\lambda^{\pm(2m+2s),4m}\neq \emptyset$ or $\mu^{\pm(m+s),2m}$ has at least one repeated part). In this case the involution is similar to that of [@G]. Let $a$ be the largest part in $\lambda^{\pm(2m+2s),4m}$ and $b$ be the largest repeated part in $\mu^{\pm(m+s),2m}$ (with $a=0$ or $b=0$ if no such part exists).

\(i\) If $a<2b$, remove two parts equal to $b$ from $\mu^{\pm(m+s),2m}$ and insert a part equal to $2b$ into $\lambda^{\pm(2m+2s),4m}$, i.e., $$\varphi(\lambda, \mu):=(\lambda\cup (2b), \mu\setminus  (b,b)).$$

\(i\) If $a\geq 2b$, remove part $a$ from $\lambda^{\pm(2m+2s),4m}$ and insert two parts equal to $a/2$ into $\mu^{\pm(m+s),2m}$, i.e., $$\varphi(\lambda, \mu):=(\lambda\setminus  (a), \mu\cup  (a/2, a/2)).$$ Again, $\varphi$ is a sign reversing involution on the subset of pairs in $\mathcal A(n)$ satisfying $\lambda^{\pm s,2m}\cup \mu^{\pm s,2m}= \emptyset$ and ($\lambda^{\pm(2m+2s),4m}\neq \emptyset$ or $\mu^{\pm(m+s),2m}$ has at least one repeated part).

[Case 3:]{.underline} $\lambda^{\pm s,2m}= \mu^{\pm s,2m}=\lambda^{\pm(2m+2s),4m}= \emptyset$ and $\mu^{\pm(m+s),2m}$ is a partition with distinct parts. Note that in this case $\lambda=\lambda^{0,2m}$ and $\mu=\mu^{\pm(m+s),2m}$. Thus, to complete the proof, we need a combinatorial proof of [\[eq_staircase\]](#eq_staircase){reference-type="eqref" reference="eq_staircase"}. Of course, using $2m$ in place of $m$ and $z=-q^m$ in the proof of [@KK] also provides a combinatorial proof of [\[eq_staircase\]](#eq_staircase){reference-type="eqref" reference="eq_staircase"}. However, the proof provided below is simpler.

We denote by $\mathcal C(n)$ the subset of pairs $(\lambda, \mu)\in \mathcal A(n)$ satisfying the conditions of Case 3. We define a sign reversing involution on the set $$\mathcal C^*(n)=\mathcal C(n) \setminus  \left(\{(\emptyset, \delta_{m-s, 2m, k})\mid k\geq 0\} \cup\{(\emptyset, \delta_{m+s, 2m, |k|})\mid k<0\}\right).$$

Now we use a particular case of [@BM Lemma 2.1]. Following the notation in [@BM] we denote by $\mathcal Q_{2m,m-s}(n)$ the set of distinct partitions of $n$ with all parts congruent to $m\pm s\pmod{2m}$ and by $\mathcal W_{2m,m-s}(n)$ the set of pairs $(\nu, k(mk-s))$, where $\nu$ is a partition into parts divisible by $2m$, $k\in \mathbb Z$, and $|\nu|+ k(mk-s)=n$. Then, the map $\xi_{2m,m-s}: \mathcal Q_{2m,m-s}(n)\to \mathcal W_{2m,m-s}(n)$ defined in [@BM Lemma 2.1] is a bijection.

Let $\mathcal D(n)$ be the set of triples $(\lambda, \nu, k(mk-s))$, where $\lambda$ and $\nu$ have parts divisible by $2m$, $\lambda$ has distinct parts, $k\in \mathbb Z$, and $|\lambda|+|\mu|+k(mk-s)=n$. The map $\zeta:\mathcal C(n)\to \mathcal D(n)$ defined by $\zeta(\lambda,\mu)=(\lambda, \xi_{2m,m-s}(\mu))$ is a bijection.

We define a sign reversing involution $\psi$ on $\mathcal D(n)\setminus (\emptyset, \emptyset, k(mk-s))$. Let $(\lambda, \nu, k(mk-s))\in \mathcal D(n)$ with $\lambda\cup \nu \neq \emptyset$ and define $\psi(\lambda, \nu, k(mk-s))=(F(\lambda, \nu),k(mk-s)).$ Then the proof of [@BM Lemma 2.1] shows that the map $\varphi(\lambda,\mu):=\zeta^{-1}\circ\psi\circ\zeta(\lambda, \mu)$ is a sign reversing involution on $\mathcal C^{*}(n)$.

Hence, the left hand side of [\[I6.7-gen\]](#I6.7-gen){reference-type="eqref" reference="I6.7-gen"} is the generating function for $|\mathcal C(n)\setminus \mathcal C^*(n)|$.

This completes the combinatorial proof of Theorem [\[T-gen\]](#T-gen){reference-type="ref" reference="T-gen"}. ◻
:::

The combinatorial proof of Theorem [\[T-gen\]](#T-gen){reference-type="ref" reference="T-gen"} above also gives a combinatorial proof of [@KMR Theorem 38].

::: theorem
Let $a$ be $1$ or $3$. Furthermore, let $(a_n)_{n\geq 0}$ be the sequence of non-negative integers $j$ such that $16j+a^2$ is a square. Then $$\label{Th38}\sum_{n=0}^\infty q^{a_n}=(q^8;q^8)_\infty(-q^{4+a};q^8)_\infty(-q^{4-a};q^8)_\infty.$$
:::

::: proof
*Combinatorial Proof.* First note that, if $a\in \{1,3\}$, then $16j+a^2$ is a square if and only if $j=k(4k-a)$ for some $k\in \mathbb Z$. Then, Case 3 in the proof of Theorem [\[T-gen\]](#T-gen){reference-type="ref" reference="T-gen"} with $m=4$ and $s=a$ proves the theorem. ◻
:::
