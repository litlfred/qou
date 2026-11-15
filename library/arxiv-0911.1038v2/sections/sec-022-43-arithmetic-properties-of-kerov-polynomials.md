---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-022-43-arithmetic-properties-of-kerov-polynomials
section_title: "Arithmetic properties of Kerov polynomials"
section_number: 4.3
pages: 21-25
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.846
latex_coverage_ratio: 0.971
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
### Auxiliary results

We present two theorems we need to prove Lemma [\[lem:div\]](#lem:div){reference-type="ref" reference="lem:div"}.

::: theorem
[]{#theo:dfs label="theo:dfs"} Let $k\geq 1$ and let $s_2,s_3,\dots$ be a sequence of non-negative integers with only finitely many non-zero elements. The coefficient of $R_2^{s_2} R_3^{s_3} \cdots$ in the Kerov polynomial $K_{k}$ is equal to the number of triples $(\sigma_1,\sigma_2,q)$ with the following properties:

1.  []{#enum:first-condition label="enum:first-condition"} $\sigma_1,\sigma_2$ is a factorization of the cycle; in other words $\sigma_1,\sigma_2\in \mathfrak{S}(k)$ are such that $\sigma_1
    \circ \sigma_2=(1,2,\dots,k)$;

2.  []{#enum:ilosc2 label="enum:ilosc2"} the number of cycles of $\sigma_2$ is equal to the number of factors in the product $R_2^{s_2} R_3^{s_3} \cdots$; in other words $|C(\sigma_2)|=s_2+s_3+\cdots$;

3.  []{#enum:boys-and-girls label="enum:boys-and-girls"} the total number of cycles of $\sigma_1$ and $\sigma_2$ is equal to the degree of the product $R_2^{s_2} R_3^{s_3} \cdots$; in other words $|C(\sigma_1)|+|C(\sigma_2)|=2 s_2+3 s_3+4 s_4+\cdots$;

4.  []{#enum:kolorowanie label="enum:kolorowanie"} $q:C(\sigma_2)\rightarrow \{2,3,\dots\}$ is a coloring of the cycles of $\sigma_2$ with a property that each color $i\in\{2,3,\dots\}$ is used exactly $s_i$ times (informally, we can think that $q$ is a map which to cycles of $C(\sigma_2)$ associates the factors in the product $R_2^{s_2} R_3^{s_3}
    \cdots$);

5.  []{#enum:marriage label="enum:marriage"} for every set $A\subset C(\sigma_2)$ which is nontrivial (i.e., $A\neq\emptyset$ and $A\neq C(\sigma_2)$) there are more than $\sum_{i\in A} \big( q(i)-1 \big)$ cycles of $\sigma_1$ which intersect $\bigcup A$.
:::

We say that a partition $\Pi$ of the set $[k]=\{1,\dots,k\}$ is a *pushing partition* if any pair of neighboring elements of $[k]$ with respect to the cyclic order (i.e. $i$ and $i+1$ are a pair of neighboring elements for any $1\leq i\leq k-1$ as well as $1$ and $k$) does not belong to the same block of $\Pi$.

The cyclic group $\mathbb{Z}/ k \mathbb{Z}$ acts on the set of all partitions (respectively, the set of pushing partitions) of the set $[k]$ as follows: for a partition $\Pi$ of $[k]$ and $i\in \mathbb{Z}/ k \mathbb{Z}$ we define $i + \Pi$ as the partition of $[k]$ with a property that $a,b$ belong to the same block of $\Pi$ if and only if $a',b'$ belong to the same block of $i +
\Pi$ for all $a,b,a',b'\in [k]$ such that $a+i \equiv a' \pmod k$, $b+i \equiv b' \pmod k$.

For any pushing partition $\Pi$ it is possible (see [@{'Sniady2006a}]) to define the normalized character $\Sigma_\Pi$. It has a property that $\Sigma_\Pi=\Sigma_\pi$, where the right-hand side should be understood as in [\[eq:character\]](#eq:character){reference-type="eqref" reference="eq:character"} for some $\pi\in\mathfrak{S}(l)$, $l\geq 1$. So defined partition-indexed character has the following properties:

::: theorem
[]{#theo:discrete-math label="theo:discrete-math"}  

-   The map $\Pi\mapsto\Sigma_\Pi$ is constant on the orbits of the action of the cyclic group $\mathbb{Z}/ k \mathbb{Z}$ on the set of pushing partitions of $[k]$.

-   For any integer $k\geq 2$ $$\label{eq:pushing}
      R_k = \sum_{\Pi} I_\Pi\ \Sigma_\Pi ,$$ where the sum runs over pushing partitions of $[k]$ and $I_\Pi\in \mathbb{Z}$, called free index, is constant on the orbits of the action of the cyclic group $\mathbb{Z}/ k \mathbb{Z}$ on the set of pushing partitions of $[k]$.

-   For the minimal partition $\Pi=\big\{ \{1\}, \dots, \{k\} \big\}$ the corresponding character is given by $$\Sigma_{ \{ \{1\}, \dots, \{k\} \} } = \Sigma_{k-1}.$$
:::

### Proof of Lemma [\[lem:div\]](#lem:div){reference-type="ref" reference="lem:div"}

::: proof
*Proof of Lemma [\[lem:div\]](#lem:div){reference-type="ref" reference="lem:div"}.* In the following we shall prove that the coefficients are integer numbers. Their nonnegativity would follow from Theorem [\[theo:dfs\]](#theo:dfs){reference-type="ref" reference="theo:dfs"}.

In order to prove that the coefficients of $\frac{\Sigma_{p}-R_{p+1}+2 R_2}{p}$ are integer we consider the action of the cyclic group $\mathbb{Z}/p\mathbb{Z}$ on the set of triples $(\sigma_1,\sigma_2,q)$ which contribute to Theorem [\[theo:dfs\]](#theo:dfs){reference-type="ref" reference="theo:dfs"} defined by conjugation $$\psi(i) (\sigma_1,\sigma_2,q) = \big(
c^i \sigma_1 c^{-i}, c^i \sigma_2 c^{-i}, q'),$$ where $c=(1,2,\dots,k)$ is the cycle and $q'(a) = q(c^{-i} a c^i)$ for $a \in C(\sigma_2)$.

All orbits of this action consist of $p$ elements except for the fixpoints of this action which are of the form $\sigma_1=c^a$, $\sigma_2=c^{1-a}$. These fixpoints contribute to the monomial $R_{p+1}$ (with multiplicity $1$) and to the monomial $R_2$ (with multiplicity $p-2$). This finishes the proof of the integrality of coefficients of [\[lem:gal_a\]](#lem:gal_a){reference-type="ref" reference="lem:gal_a"}.

We apply Theorem [\[theo:discrete-math\]](#theo:discrete-math){reference-type="ref" reference="theo:discrete-math"} in the case when $k=p$ is a prime number. The right-hand side of [\[eq:pushing\]](#eq:pushing){reference-type="eqref" reference="eq:pushing"} is constant on each orbit of the action of the cyclic group $\mathbb{Z}/ p \mathbb{Z}$. Each orbit of this action consists of $p$ elements, except for the fixpoints. The only pushing partition of $[p]$ which is invariant under the action of the cyclic group $\mathbb{Z}/ p \mathbb{Z}$ is the minimal partition $\big\{ \{1\}, \dots, \{p\} \big\}$. In this way we proved that $$\begin{gathered}
  R_p = \Sigma_{p-1} + p\ \big( \text{linear combination of the characters $\Sigma_\pi$}
\\ 
\text{for $\pi\in\mathfrak{S}(l)$, $l\geq 1$ with integer coefficients} \big). 
\end{gathered}$$ Thanks to Kerov polynomials, each $\Sigma_\pi$ can be written as a polynomial in free cumulants with integer coefficients. This shows part [\[lem:gal_b\]](#lem:gal_b){reference-type="ref" reference="lem:gal_b"}.

In the following we shall use the notations and results presented in the paper of Biane [@Biane2003]. In order to prove part [\[lem:gal_c\]](#lem:gal_c){reference-type="ref" reference="lem:gal_c"} we consider the formal power series $$H(z) = z-\sum_{j\geq 1} {B}_{j+1}z^{-j}$$ where ${B}_{j}$ are Boolean cumulants. Biane showed that $$\label{eq:hahaha}
(-p-1)\Sigma_{p+1} =
[z^{-1}]H(z)H(z-1)\cdots H(z-p)$$ and $$(-p-1) {R}_{p+2} =  [z^{-1}]H(z)^{p+1}.$$ We know from [@Biane2003] that $B_j$ is a polynomial in free cumulants $R_2,R_3,\dots$ with integer coefficients as well as $\Sigma_{p+1}$ is a polynomial in Boolean cumulants $B_2,B_3,\dots$ with integer coefficients; hence it suffices to show that $(-p-1)(\Sigma_{p+1}-R_{p+2}+R_3)$ is a polynomial in Boolean cumulants with all coefficients divisible by $p$. It is equivalent to show that $\Sigma_{p+1}-R_{p+2}+R_3=0$ under additional assumption that all coefficients of the power series are taken from a field of characteristic $p$, hence all formulas are considered in a field of characteristic $p$ from now.

From [\[eq:hahaha\]](#eq:hahaha){reference-type="eqref" reference="eq:hahaha"} it follows that $$[B_3] \Sigma_{p+1} = \frac{1}{p+1} \sum_{0\leq z \leq p}
\frac{1}{2} \frac{d^2}{dz^2} 
\big[ z (z-1) \cdots (z-p) \big].$$ From Fermat's little theorem (see for example [@GrahamKnuthPatashnik]) it follows that in the field of characteristic $p$ $$z (z-1) \cdots (z-p) = z (z^p-z)=z^{p+1}-z^2$$ hence $$\label{eq:B3}
 [B_3] \Sigma_{p+1} = \frac{1}{p+1} \sum_{0\leq z \leq p} (-1)=-1.$$

We define ${B}_0 = -1$ and ${B}_1 = 0$; then using binomial formula we have $$H(z-i)=\sum_{j\geq-1}\sum_{k\geq 0} 
(-1)^{k+1} \binom{-j}{k} i^k {B}_{j+1}  z^{-(j+k)},$$ hence $$\begin{gathered}
\label{eq:iloczynn}
-\frac{1}{p+1} H(z)H(z-1)\cdots H(z-p) = 







\\ -\frac{1}{p+1} \sum_{k \in A} \sum_{j \in B}
(-1)^{|k|_1+p+1} 
\\
\left(\prod_{0 \leq i \leq
p}\binom{-j_i}{k_i}i^{k_i}{B}_{j_i+1}\right)
z^{-|j|_0-|k|_1},
\end{gathered}$$ where $A,B \subset \mathbb{Z}^{p+1}$ such that $$A = \{(k_0,k_1,\dots,k_p): k_i \geq 0\
\text{for}\ 0 \leq i \leq p\},$$ $$B = \{(j_0, j_1,\dots,j_p): j_i \geq -1\
\text{for}\ 0 \leq i \leq p\}$$ and for $k = (k_0, k_1, \dots, k_p)$, $i \in \{0,1\}$ the sum $k_i + k_{i+1} +\cdots + k_p$ is denoted by $|k|_i$. For any $a\in
\mathbb{Z}/p\mathbb{Z}$ such that $a\neq 0$ the map $x\mapsto ax$ is a bijection of the multiset $(0,1,\dots,p)\subset\mathbb{Z}/p\mathbb{Z}$ (notice that $0=p$ appears twice in this multiset) therefore the left-hand side of [\[eq:iloczynn\]](#eq:iloczynn){reference-type="eqref" reference="eq:iloczynn"} is equal to $$\begin{gathered}
\label{eq:iloczynn2}
-\frac{1}{p+1} H(z)H(z-a)\cdots H(z-pa) = 







\\ -\frac{1}{p+1} \sum_{k \in A} \sum_{j \in B}
(-1)^{|k|_1+p+1} a^{|k|_1} 
\\
\left(\prod_{0 \leq i \leq
p}\binom{-j_i}{k_i}i^{k_i}{B}_{j_i+1}\right)
z^{-|j|_0-|k|_1}.
\end{gathered}$$

The coefficient of $z^{-1}$ in [\[eq:iloczynn2\]](#eq:iloczynn2){reference-type="eqref" reference="eq:iloczynn2"} can be viewed as a polynomial in $a$; we shall denote it by $P(a)$. In the following we will study its coefficients of highest degrees. We are interested only in the summands for which $|j|_0+|k|_1=1$; since $|j|_0\geq
-p-1$ therefore $|k|_1\leq p+2$ and the degree of $P(a)$ is at most $p+2$.

However, $|k|_1=p+2$ would correspond to the case $j=(-1,\-1,\dots,-1)$ which is equivalent to setting $B_2=B_3=\cdots=0$; therefore $[a^{p+2}] P(a)=0$.

For $|k|_1=p+1$ there is no summand for which $j_0,\dots,j_p\neq 0$ hence $[a^{p+1}] P(a)=0$.

For $|k|_1=p$ every summand which contributes is of the following form: one of the numbers $j_0,\dots,j_p$ is equal to $1$ and all the others are equal to $-1$. This shows that $[a^p] P(a)$ viewed as a polynomial in $B_2,B_3,\dots$ contains only one monomial, namely a multiple of $B_2$; also $[B_2] P(a)$ viewed as a polynomial in $a$ contains only one monomial namely a multiple of $a^p$. Therefore $[a^{p}]P(a)$ is a multiple of $B_2$ and the value of the coefficient of $B_2$ fulfills: $$[B_2][a^{p}]P(a)=[B_2] P(1)=[B_2] \Sigma_{p+1}.$$ Since $p$ is odd, the expansion of $\Sigma_{p+1}$ into Boolean cumulants contains only summands which are of odd degree [@Biane2003]; it follows that $[a^{p}]P(a)=0$.

In an analogous way we prove that $[a^{p-1}]P(a)$ is a multiple of $B_3$ and $$[B_3][a^{p-1}]P(a)=[B_3] \Sigma_{p+1}= -1$$ from [\[eq:B3\]](#eq:B3){reference-type="eqref" reference="eq:B3"}.

In this way we proved that $P(a)$ is a polynomial of degree $p-1$ which takes the same value for all $a\in\{1,\dots,p-1\}$. Polynomial $$\widetilde{P}(a)=  -B_3 a^{p-1} + P(0)$$ has the same properties. It follows that $P-\widetilde{P}$ has degree at most $p-2$ which takes the same value for all $a\in\{1,\dots,p-1\}$ hence it must be equal to the constant. It follows that $\widetilde{P}=P$.

Therefore $$\Sigma_{p+1} = P(1) = -B_3 +  R_{p+2}.$$ Observation that $B_3=R_3$ finishes the proof for the third expression. ◻
:::

It is interesting that for the first two expressions we managed to find combinatorial proofs while for the last expression there seems to be no natural candidate for a combinatorial approach.
