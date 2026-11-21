---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-002-21-inductive-definitions
section_title: "Inductive definitions."
section_number: 2.1
pages: 2-6
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.989
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 9 sections: Front matter; Introduction.; Preliminaries on surreal numbers."
---
This section is dedicated to fix the notations and recall some of the definitions and results obtained in [@conway_numb-games] and [@gonshor_surreal]. We will also use results from [@ehrlich:simpl-hierarc] and [@ehrlich-vdd:surreal-exp].

We denote by $\textbf{On}$ the proper class of **ordinal numbers**. A **surreal number** is any map $a:\alpha\rightarrow \{\ominus,\oplus\}$ where $\alpha\in\textbf{On}$. Any surreal may be canonically represented as a sequence of pluses and minuses called its **sign sequence**. The ordinal $\alpha$ on which the surreal number $a$ is defined is called its **length**. Set $l(a):=\alpha$. The proper class of all surreal numbers is denoted by $\textbf{No}$.

It is totally ordered as follows. Let $a$ and $b$ be any two surreal numbers with $l(a)\leq l(b)$. Consider the sign sequence of $a$ completed with 0's so that the two sign sequences have same length. Then consider the **lexicographical order** between them, denoted by $\leq$, based on the following relation:

::: center
$\ominus<0<\oplus$.
:::

A subset of $\textbf{No}$ is said to be **initial** if it is made of surreals whose lengths are less than or equal to a given ordinal. As in [@ehrlich:simpl-hierarc], $\textbf{No}$ is endowed with a partial ordering called the **simplicity** :

::: center
$a\textrm{ is simpler than }b\textrm{, write }a<_sb \Leftrightarrow a\textrm{ is a proper initial segment of }b$.
:::

Given a surreal $a\in \textbf{No}$, any surreal number $a'<_sa$ is called a **truncation** of $a$.

The construction of surreal numbers makes heavy use of the key idea of \"cuts between sets\" in the classical construction of real numbers. Take two pairs $(L,R)$ (as \"Left\" and \"Right\") and $(L',R')$ of *subsets* of **No** with $L<R$ and $L'<R'$. $(L',R')$ is said to be **cofinal** in $(L,R)$ if for any $(a,b)\in L\times R$, there is $(a',b')\in L'\times R'$, such that $a<a'<b'<b$. Note that cofinality is a transitive relation. The following results are fundamental. In particular, given a surreal $a\in\textbf{No}$, we will considere the pair $(L_a,R_a)$ where $L_a=\{b\in\textbf{No}\ ;\ b<a\textrm{ and }b<_sa\}$ and $R_a=\{b\in\textbf{No}\ ;\ b>a\textrm{ and }b<_sa\}$.

::: thm
[]{#theo:cofin label="theo:cofin"}

1.  [@gonshor_surreal Theorem 2.1] For any pair $(L,R)$ with $L<R$, there exists a *unique* surreal $a\in \textbf{No}$ of minimal length such that $L<a<R$. We set $\langle L|R\rangle:=a\in\textbf{No}$, and call it the **cut** between $L$ and $R$.

2.  [@gonshor_surreal Theorem 2.6] Suppose that $\langle L\ |\ R\rangle=a\in\textbf{No}$, $L'<a<R'$ for some pair $(L',R')$ cofinal in $(L,R)$, then $\langle L'\ |\ R'\rangle=a$.

3.  [@gonshor_surreal Theorems 2.8 and 2.9] One always has $a=\langle L_a\ |\ R_a\rangle$ and, for any cut $\langle L'\ |\ R'\rangle=a$, then $(L',R')$ is cofinal in $(L_a,R_a)$.
:::

::: defn
This representation $a=\langle L_a\ |\ R_a\rangle$ of $a$ is called *its* **canonical cut**. By abuse of notation, we also denote the canonical cut by $a=\langle a^L\ |\ a^R\rangle$ where $a^L$ and $a^R$ are general elements of the canonical sets $L_a$ and $R_a$ (e.g. $a^L=n$ if $L_a=\mathbb{N}$).
:::

The preceding results allow to define maps and operations on surreal numbers *recursively*, that is by induction on the length of the surreals considered since $a^L$ and $a^R$ are simpler than $a$. Concerning the algebraic structure of $\textbf{No}$, we have:

::: thm
[]{#theo:NO-reel-clos label="theo:NO-reel-clos"}

1.  [@gonshor_surreal Theorems 3.3, 3.6, 3.7 and Ch. 5, Sect. D] The proper class $\textbf{No}$ endowed with its lexicographical ordering $\leq$ and the following operations, is a real closed field (in the sense of proper classes): for any $a,b\in\textbf{No}$,

    ::: center
    $\begin{array}
    {llcl}\emph{addition: }&a+b&:=&\langle a^L+b,\ a+b^L\ |\ a^R+b,\ a+b^R\rangle\\
     \emph{neutral\ element}: &0&=&\langle\emptyset\ |\ \emptyset\rangle ; \\
    \emph{multiplication: }&a.b&:=& \langle a^L.b+a.b^L-a^L.b^L,\ a^R.b+a.b^R-a^R.b^R\ |\ \\ 
    &&&\ \ \ \ \ \ a^L.b+a.b^R-a^L.b^R,\ a^R.b+a.b^L-a^R.b^L\rangle  \\
    \emph{neutral\ element}: &1&=&\oplus=\langle 0\ |\ \emptyset\rangle. \\
    \end{array}$
    :::

2.  [@ehrlich:simpl-hierarc Theorems 9 and 19] Any divisible ordered abelian group, respectively any real closed field, is isomorphic to an initial subgroup of $(\textbf{No},+)$, respectively an initial subfield of $(\textbf{No},+,.)$.
:::

Note that Gonshor proves also, for the cited operations as well as for the following maps, the so-called **uniformity properties** [@gonshor_surreal Theorems 3.2, 3.5 etc.]. For example in the case of the addition, this means that $a+b$ may be obtained by taking any cuts $a=\langle L\ |\ R\rangle$ and $b=\langle L'\ |\ R'\rangle$ instead of taking their canonical cuts, and applying the same formula as above. In other words, *the formulas do not depend on the cuts for which $a^L,\ a^R,\ b^L,\ b^R$ are general elements*.

Any **real number** is identified to the sign sequence corresponding to its binary expansion. Thus they are the sequences of length finite or equal to $\omega$, the later being non ultimately constant. These sequences form a subfield of the surreals having the least upper bound property, i.e. a copy of the ordered set of the reals: $\mathbb{R}\subset \textbf{No}$.

Surreal numbers $a\in\textbf{No}$ such that $a>\mathbb{R}$ or $a<\mathbb{R}$ are called **infinitely large**: we denote by $\textbf{No}^{\gg 1}$ their proper class. Those that verify $0<a<\mathbb{R}_{>0}$ or $0>a>\mathbb{R}_{<0}$ are called **infinitesimals**: we denote by $\textbf{No}^{\ll 1}$ their proper class.

Any ordinal number $\alpha\in\textbf{On}$ is identified to the surreal number whose sign sequence is a sequence of $\oplus$'s of length $\alpha$. The operations precedingly defined on the surreal numbers correspond to the **natural sum and product** (see e.g. [@hausdorff-mengenlehre]). So we consider $\textbf{On}\subset\textbf{No}$.

In the following theorem, we sum up the main results about the so-called **Conway normal form** of a surreal number:

::: thm
[]{#theo:NO-series-gene label="theo:NO-series-gene"}

1.  [@gonshor_surreal Theorems 5.1 to 5.4] The recursive formula:

    ::: center
    $\forall a\in\textbf{No}$, $\omega^{a}:=\langle 0,\ n.\omega^{a^L}\ |\ \omega^{a^R}/2^n\}$
    :::

    (where it is understood that $n\in\mathbb{N}$), defines a map:

    ::: center
    $\begin{array}{llcl}
    \Omega:&\textbf{No}&\rightarrow&\textbf{No}\\
    &a&\mapsto&\Omega(a):=\omega^a
    \end{array}$
    :::

    with values in $\textbf{No}_{>0}$ and that extends the exponentiation with base $\omega$ of the ordinals. Moreover, for any $a\in\textbf{No}$, $\omega^a$ is the representative of minimal length of its **Archimedean equivalence class** ($\forall x,y \in \textbf{No}_{>0},\ x\sim_{arch} y\Leftrightarrow \exists n\in\mathbb{N},\ n.x\geq y \geq x/n$).

2.  [@gonshor_surreal Theorems 5.5 to 5.8] The field of surreals is a field of **generalized series** [@matu-kuhlm:hardy-deriv-gener-series Definition 2.5] in the following sense: any surreal number $a\in\textbf{No}$ can be written uniquely as $a=\displaystyle\sum_{i<\lambda}\omega^{a_i}r_i$ where the transfinite sequence $(a_i)_{i<\lambda}$ is strictly decreasing and, for any $i$, $r_i\in\mathbb{R}\setminus\{0\}$. In particular, $\omega^{\textbf{No}}$ is seen as the group of **(generalized) monomials**:

    ::: center
    $\textbf{No}=\mathbb{R}((\omega^{\textbf{No}}))$.
    :::
:::

In particular, the proper class $\omega^{\textbf{No}}$ is a complete system of representatives of the Archimedean equivalence classes of $\textbf{No}_{>0}$, each of its elements being the reprensentative of minimal length in its class.

Moreover, note that the map denoted by $Ind$ in [@gonshor_surreal], which sends any surreal $a$ to the exponent $a_0$ of the leading monomial of its normal form, is a **valuation**. It is the natural valuation of the real closed field $\textbf{No}$ [@kuhl:ord-exp]. In particular, $Ind(\omega^{a})=a$ for any $a\in\textbf{No}$.

We deduce immediately that $\textbf{No}$ is a **Hahn field of series** [@hahn:nichtarchim] in the following sense:

::: prop
[]{#prop:N0-Hahn label="prop:N0-Hahn"}

1.  For any $a\in \textbf{No}$, $\omega^{\omega^a}$ is the representative of minimal length in its **equivalence class of comparability** ($\forall x,y\in\textbf{No}_{>0}^{\gg 1},\ x\sim_{comp} y\Leftrightarrow (\exists n\in\mathbb{N},\ x^n\geq y \geq x^{1/n}$, and we set $1/x\sim_{comp}x$).

2.  Any surreal $a\in\textbf{No}$ can be written uniquely $a=\displaystyle\sum_{i<\lambda}\left(\displaystyle\prod_{j<\lambda_i} \left(\omega^{\omega^{b_{i,j}}}\right)^{s_{i,j}}\right)r_i$ where, for any $i$, we identify $\displaystyle\prod_{j<\lambda_i} \left(\omega^{\omega^{b_{i,j}}}\right)^{s_{i,j}}=\omega^{a_i}$ where $a_i=\displaystyle\sum_{j\in\lambda_i}\omega^{b_{i,j}}$ (so the tranfinite sequences $(a_i)_{i<\lambda}$ and for any $i$, $(b_{i,j})_{j<\lambda_i}$, are strictly decreasing, and for any $i,j$, $s_{i,j},r_i\in\mathbb{R}\setminus\{0\}$). In particular, we call $\omega^{\omega^{\textbf{No}}}$ the chain of **fundamental monomials** of **No** [@matu-kuhlm:hardy-deriv-gener-series Definition 2.2]:

    ::: center
    $\textbf{No}=\mathbb{R}\left(\left(\left(\omega^{\omega^{\textbf{No}}} \right)^{\mathbb{R}}\right)\right)$.\
    :::
:::

The proper class $\omega^{\omega^{\textbf{No}}}$ is a complete set of representatives of the comparability classes of $\textbf{No}_{>0}^{\gg 1}$, each of its elements being the one of minimal length in its class.\
Following the ideas of Conway, Gonshor described also a proper class of **generalized epsilon numbers** [@conway_numb-games p.35]:

::: thm
[]{#theo:eps-nbres label="theo:eps-nbres"} The recursive formula:

::: center
$\forall a\in\textbf{No}$, $\epsilon_{a}:=\langle \Omega^n(1),\ \Omega^n(\epsilon_{a^L}+1)\ |\ \Omega^n(\epsilon{a^R}-1)\}$
:::

(where it is understood that $n\in\mathbb{N}$), defines a map:

::: center
$\begin{array}{llcl}
\epsilon: &\textbf{No}&\rightarrow&\textbf{No}\\
a&\mapsto&\epsilon(a):=\epsilon_a
\end{array}$
:::

with values in $\textbf{No}_{>0}^{\gg 1}$ bigger than $\Omega^n(1)$ for any $n$, and which extends the classical epsilon numbers map on ordinals [@sierpinski_ordinal-cardinal]. Moreover, $\epsilon(\textbf{No})$ is the proper class of all the fixed points of the map $\Omega$ :

::: center
$\forall a\in\textbf{No},\ \omega^{\epsilon_a}=\epsilon_a$.\
:::
:::

Gonshor defines inductively in [@gonshor_surreal] an **exponential map** $\exp:(\textbf{No},+)\rightarrow(\textbf{No}_{>0},.)$ which is surjective (and consequently its inverse, the **logarithmic map** $\log:(\textbf{No}_{>0},.)\rightarrow(\textbf{No},+)$) using the Taylor expansion of the real exponential map. Here we give only the results we will need in this article:

::: thm
[]{#theo:exp label="theo:exp"} The exponential map $\exp:\textbf{No}\rightarrow\textbf{No}_{>0}$ and its inverse $\log:\textbf{No}_{>0}\rightarrow\textbf{No}$, coincide on the real numbers with the usual real exponential and logarithmic maps, and are such that:

::: center
$\begin{array}{rlcl}
1.\ \textrm{for any }a\in\textbf{No},& \exp(\displaystyle\sum_{i<\lambda}\omega^{a_i}r_i)&=& \omega^{\sum_{i<\lambda}\omega^{g(a_i)}r_i}\\
\textrm{where }& g(a)&:=&\langle  Ind(a),\ g(a^L)\ |\ g(a^R)\rangle ;\\
2.\ \textrm{for any }b\in\textbf{No},& \log(\displaystyle\prod_{j<\lambda} \left(\omega^{\omega^{b_{j}}}\right)^{s_{j}})&=& \displaystyle\sum_{j<\lambda}\omega^{h(b_j)}\\
\textrm{where }& h(b)&:=&\langle  0,\ h(b^L)\ |\ h(b^R),\ \omega^b/2^n\rangle.
\end{array}$
:::

We have $\exp=\log^{-1}$ and $h=g^{-1}$ on $\textbf{No}$.
:::

Note that $g$ is not defined at 0.
