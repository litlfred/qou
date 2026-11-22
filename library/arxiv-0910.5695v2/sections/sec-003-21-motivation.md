---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-003-21-motivation
section_title: "Motivation"
section_number: 2.1
pages: 2-7
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.652
latex_coverage_ratio: 0.969
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
[]{#motivation label="motivation"}

Let $d$ be a nonnegative integer, and let $F$ be a field of characteristic zero. Let us consider the tensor category $\operatorname{Rep}(S_d; F)$ of finite dimensional representations over $F$ of the symmetric group $S_d$. Note that we take $S_0$ to be the trivial group whose one element is the identity permutation of the empty set. Let $V_d$ denote the natural $d$-dimensional representation of $S_d$ with basis $\{v_1,\ldots, v_d\}$, so that $S_d$ acts by permuting the basis elements ($V_0$ is taken to be 0). Setting $V_d^{\otimes 0}=F$ for all $d\geq 0$, we have the following well-known result:

::: proposition
[]{#full label="full"} Any irreducible representation of $S_d$ is a direct summand of $V_d^{\otimes n}$ for some nonnegative integer $n$.
:::

As a consequence of Proposition [\[full\]](#full){reference-type="ref" reference="full"}, one way to understand $\operatorname{Rep}(S_d; F)$ is to study objects of the form $V^{\otimes n}_d$ and morphisms between those objects. We will now use set partitions to construct some such morphisms. Our notation will be similar to that of [@MR2143201].

By a *partition* $\pi$ of a finite set $S$ we mean a collection $\pi_1,\ldots,\pi_n$ of disjoint subsets of $S$ with $S=\bigcup_i \pi_i$. The sets $\pi_i$ will be called *parts* of $\pi$. Given a partition $\pi$ of $\{1,\ldots, n, 1',\ldots, m'\}$, a *partition diagram of $\pi$* is any graph with vertices labelled $\{1,\ldots, n, 1',\ldots, m'\}$ whose connected components partition the vertices into the parts of $\pi$. We will always draw partition diagrams using the following convention:

-   Vertices $1,\ldots, n$  (resp. $1',\ldots, m'$) are aligned horizontally and increasing\
    from left to right with $i$ directly above $i'$.

-   Edges lie entirely below the vertices labelled $1,\ldots, n$ and above the vertices\
    labelled $1',\ldots, m'$.

We will abuse notation by writing $\pi$ for both the partition and the partition diagram.

::: example
[]{#pd label="pd"} The graph $$\includegraphics{diss1.pdf}$$ is a partition diagram for the partition $\{\{1,3,2',3'\},\{2,4\},\{1'\}\}$. Note a partition diagram representing this partition is not unique, but its connected components are.$\hfill\rotatebox{45}{$\Box$}$
:::

To each partition of the set $\{1,\ldots, n, 1',\ldots, m'\}$ we will associate a linear map $V_d^{\otimes n}\to V^{\otimes m}_d$. Before doing so, we introduce some notation.

-   Let $P_{n,m}$ denote the set of all partitions of $\{1,\ldots, n, 1',\ldots, m'\}$, let $P_{n,0}$ denote the set of all partitions of $\{1,\ldots, n\}$, let $P_{0,m}$ denote the set of all partitions of $\{1',\ldots, m'\}$, and let $P_{0,0}$ denote the set consisting of the empty partition. Finally, let $F P_{n, m}$ denote the $F$-vector space with basis $P_{n,m}$.

-   For nonnegative integers $n$ and $d$, let $[n, d]$ denote the set of all functions from $\{j~|~1\leq j\leq n\}$ to $\{j~|~1\leq j\leq d\}$. In particular, $[0, d]=\{\varnothing\}$ for all $d$, and $[n, 0]=\varnothing$ for all $n\not=0$. Given ${\mbox{\boldmath${i}$}}\in[n, d]$ and $j\in\{j~|~1\leq j\leq n\}$, write $i_j$ for the image of $j$ under ${\mbox{\boldmath${i}$}}$.

-   For ${\mbox{\boldmath${i}$}}\in[n, d]$ and ${\mbox{\boldmath${i}$}}'\in[m, d]$, the *$({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring* of a partition $\pi\in P_{n, m}$ is obtained by coloring the vertices of $\pi$ labelled $j$ (resp. $j'$) by the integer $i_j$ (resp. $i'_j$). Saying an $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring of $\pi$ is *good* means vertices are colored the same whenever they are in the same connected component of $\pi$. Saying an $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring of $\pi$ is *perfect* means vertices are colored the same if and only if they are in the same connected component of $\pi$.

-   For $n\not=0$ and ${\mbox{\boldmath${i}$}}\in[n, d]$, set $v_{\mbox{\boldmath${i}$}}:=v_{i_1}\otimes\cdots\otimes v_{i_n}\in V_d^{\otimes n}$. Set $v_\varnothing:=1\in V^{\otimes0}_d$ where $\varnothing$ is the unique element of $[0, d]$.

We are now ready to associate partitions in $P_{n,m}$ with linear maps $V_d^{\otimes n}\to V^{\otimes m}_d$.

::: definition
[]{#f label="f"} For nonnegative integers $n, m$, and $d$, define the $F$-linear map $f:FP_{n, m}\to\operatorname{Hom}_{S_d}(V_d^{\otimes n}, V_d^{\otimes m})$ by setting $$f(x)(v_{\mbox{\boldmath${i}$}})=\sum_{{\mbox{\boldmath${i}$}}'\in[m, d]}f(x)^{\mbox{\boldmath${i}$}}_{ {\mbox{\boldmath${i}$}}'}v_{{\mbox{\boldmath${i}$}}'}\qquad (x\in FP_{n, m}, \mbox{\boldmath${i}$}\in[n, d])$$ where $$f(\pi)^{\mbox{\boldmath${i}$}}_{{\mbox{\boldmath${i}$}}'}:=\left\{\begin{array}{ll}
1, & \text{if the $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring of $\pi$ is good},\\
0, & \text{otherwise}.
\end{array}\right.\qquad (\pi\in P_{n,m})$$
:::

Indeed, $f(x)$ commutes with the action of $S_d$ which merely permutes the colors.

::: example
\(1\) If $\varnothing\in P_{0,0}$ denotes the empty partition, then $f(\varnothing):F\to F$ is the identity map.

\(2\) Assume $d>0$ and let $\pi$ be the partition with partition diagram $$\includegraphics{diss2.pdf}$$ Then $f(\pi):V_d^{\otimes 6}\to V_d^{\otimes 7}$ is given by $$f(\pi)(v_{\mbox{\boldmath${i}$}})=\left\{\begin{array}{ll}
\sum\limits_{1\leq k, j\leq d} v_k\otimes v_j\otimes v_{i_4}\otimes v_j\otimes v_{i_6}\otimes v_{i_6}\otimes v_{i_6}, & \text{if $i_1=i_2$ and $i_4=i_5$},\\
0, & \text{otherwise}.
\end{array}\right.$$ for ${\mbox{\boldmath${i}$}}\in[6,d]$.

\(3\) Assume $d>0$ and let $\pi$ be the partition with partition diagram $$\includegraphics{diss10.pdf}$$ Then $f(\pi):F\to V_d^{\otimes 5}$ is given by $$f(\pi)(1)=\sum_{1\leq i, j, k\leq d}v_i\otimes v_j\otimes v_i\otimes v_k\otimes v_j.$$ $\hfill\rotatebox{45}{$\Box$}$
:::

Next we wish to show that $f$ is surjective. A proof of this fact when $n=m$ can be found in [@MR2143201 Theorem 3.6]. Their proof extends to the case $n\not=m$ without difficulty. For completeness we will give a modified version of their proof. Before doing so, we must introduce a bit more notation.

-   Let $\leq$ be the partial order on $P_{n,m}$ defined by $\pi\leq\mu$ whenever the partition $\mu$ is coarser than the partition $\pi$ (i.e. $r$ and $s$ are in the same part of $\mu$ whenever they are in the same part of $\pi$ for each pair $r, s\in\{1,\ldots, n, 1',\ldots, m'\}$).

-   Define the basis $\{x_\pi~|~\pi\in P_{n,m}\}$ of $F P_{n,m}$ inductively by setting $$\label{xpi} x_\pi:=\pi-\sum\limits_{\mu\gneqq \pi} x_\mu.$$

::: example
\(1\) $x_\pi=\pi$ when $\pi$ is any partition consisting of one part.

\(2\) Let $\pi\in P_{4,3}$ be the partition with the partition diagram given in Example [\[pd\]](#pd){reference-type="ref" reference="pd"}. Then $x_\pi=\pi-\mu_1-\mu_2-\mu_3+2\mu_4$ where $$\includegraphics{diss3.pdf}$$ $\hfill\rotatebox{45}{$\Box$}$
:::

We are now ready to prove the following:

::: theorem
[]{#sw label="sw"} For integers $n, m, d\geq 0$, the map $f: F P_{n,m}\to\operatorname{Hom}_{S_d}(V_d^{\otimes n}, V_d^{\otimes m})$ (see Definition [\[f\]](#f){reference-type="ref" reference="f"}) has the following properties:

1.  $f$ is surjective.

2.  $\ker(f)=\text{Span}_ F\{x_\pi~|~\pi\text{ has more than $d$ parts}\}$.

In particular, $f$ is an isomorphism of $F$-vector spaces whenever $d\geq n+m$.
:::

::: proof
*Proof.* (compare with [@MR2143201 proof of Theorem 3.6(a)]) If $d=0$ then the theorem is certainly true. Now assume $d>0$. For $g\in\operatorname{Hom}_{S_d}(V_d^{\otimes n}, V_d^{\otimes m})$ write $$g(v_{\mbox{\boldmath${i}$}}):=\sum_{{\mbox{\boldmath${i}$}}'\in[m, d]}g^{\mbox{\boldmath${i}$}}_{{\mbox{\boldmath${i}$}}'}v_{{\mbox{\boldmath${i}$}}'}\qquad({\mbox{\boldmath${i}$}}\in[n, d])$$ Since $g$ commutes with the action of $S_d$, the matrix entries, $g^{\mbox{\boldmath${i}$}}_{{\mbox{\boldmath${i}$}}'}$, are constant on the $S_d$-orbits of the matrix coordinates $\{({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')\}_{{\mbox{\boldmath${i}$}}\in[n,d], {\mbox{\boldmath${i}$}}'\in[m,d]}$. Each $S_d$-orbit of $\{({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')\}_{{\mbox{\boldmath${i}$}}\in[n,d], {\mbox{\boldmath${i}$}}'\in[m,d]}$ corresponds to a partition $\pi\in P_{n,m}$ as follows: $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$ is in the orbit corresponding to $\pi$ if and only if the $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring of $\pi$ is perfect. A straightforward induction argument shows $$\label{fx}
f(x_\pi)^{\mbox{\boldmath${i}$}}_{{\mbox{\boldmath${i}$}}'}=\left\{\begin{array}{ll}
1, & \text{if the $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring of $\pi$ is perfect},\\
0, & \text{otherwise}.
\end{array}\right.\quad({\mbox{\boldmath${i}$}}\in[n,d], {\mbox{\boldmath${i}$}}'\in[m,d])$$ Thus $g$ is an $F$-linear combination of the $f(x_\pi)$'s. This proves part (1).

To prove part (2) notice that for $\pi\in P_{n,m}$, there exist ${\mbox{\boldmath${i}$}}\in[n, d]$ and ${\mbox{\boldmath${i}$}}'\in[m, d]$ such that the $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring of $\pi$ is perfect if and only if $\pi$ has at most $d$ parts. Hence, by ([\[fx\]](#fx){reference-type="ref" reference="fx"}), $f(x_\pi)$ is the zero map if and only if $\pi$ has more than $d$ parts. Part (2) now follows since $\{x_\pi~|~\pi\in P_{n,m}\}$ is a basis for $F P_{n,m}$. ◻
:::

We conclude our investigation of morphisms of the form $f(\pi):V_d^{\otimes n}\to V_d^{\otimes m}$ by studying the composition of such morphisms. First we require the following:

::: definition
[]{#star label="star"} Given partition diagrams $\pi\in P_{n,m}$ and $\mu\in P_{m,l}$, construct a new diagram $\mu\star\pi$ by identifying the vertices $1',\ldots, m'$ of $\pi$ with the vertices $1,\ldots, m$ of $\mu$ and renaming them $1'',\ldots,m''$ as illustrated below. $$\includegraphics{diss4.pdf}$$ Now let $\ell(\mu, \pi)$ denote the number of connected components of $\mu\star\pi$ whose vertices are not among $1,\ldots, n, 1', \ldots, l'$. Finally, let $\mu\cdot\pi\in P_{n,l}$ be the partition obtained by restricting $\mu\star\pi$ to $\{1,\ldots, n, 1',\ldots, l'\}$ (i.e. $r$ and $s$ are in the same part of $\mu\cdot\pi$ if and only if $r$ and $s$ are in the same part of $\mu\star\pi$).
:::

We are now ready to state

::: proposition
[]{#comp label="comp"} $f(\mu)f(\pi)=d^{\ell(\mu, \pi)}f(\mu\cdot\pi)$ for any $\pi\in P_{n,m}$, $\mu\in P_{m,l}$.
:::

Before we give a proof of Proposition [\[comp\]](#comp){reference-type="ref" reference="comp"} let us consider an example.

::: example
In this example we will verify Proposition [\[comp\]](#comp){reference-type="ref" reference="comp"} when $$\includegraphics{diss5.pdf}$$ On the one hand, $$\includegraphics{diss6.pdf}$$ Thus $\ell(\mu,\pi)=2$ and $$\includegraphics{diss7.pdf}$$ Therefore we have $d^{\ell(\mu, \pi)}f(\mu\cdot\pi)(v_{i_1}\otimes v_{i_2}\otimes v_{i_3}\otimes v_{i_4})=d^2\delta_{i_1, i_3}v_{i_2}\otimes v_{i_2}\otimes v_{i_2}\otimes v_{i_4}\otimes v_{i_4}$ where $\delta_{i,j}$ is the Kronecker delta function.

On the other hand, $$\begin{array}{rl}
f(\mu) f(\pi)(v_{\mbox{\boldmath${i}$}}) & =f(\mu)\left(\delta_{i_1,i_3}\sum\limits_{1\leq j, k, l\leq d}v_{j}\otimes v_{i_4}\otimes v_{j}\otimes v_{k}\otimes v_{l}\otimes v_{i_2}\otimes v_{i_2}\right)\\
& =\delta_{i_1,i_3}\sum\limits_{1\leq j, k, l\leq d}f(\mu)\left(v_{j}\otimes v_{i_4}\otimes v_{j}\otimes v_{k}\otimes v_{l}\otimes v_{i_2}\otimes v_{i_2}\right)\\
& =\delta_{i_1,i_3}\sum\limits_{1\leq j, k, l\leq d}\delta_{j,k}~v_{i_2}\otimes v_{i_2}\otimes v_{i_2}\otimes v_{i_4}\otimes v_{i_4} \\
& =\delta_{i_1,i_3}\sum\limits_{1\leq j, l\leq d}v_{i_2}\otimes v_{i_2}\otimes v_{i_2}\otimes v_{i_4}\otimes v_{i_4}   \\
& =d^2\delta_{i_1,i_3}~v_{i_2}\otimes v_{i_2}\otimes v_{i_2}\otimes v_{i_4}\otimes v_{i_4}. \\
\end{array}$$ for any ${\mbox{\boldmath${i}$}}\in[4, d]$, as desired.$\hfill\rotatebox{45}{$\Box$}$
:::

Now to show Proposition [\[comp\]](#comp){reference-type="ref" reference="comp"} holds in general.

Suppose $\pi\in P_{n,m}$ and $\mu\in P_{m, l}$ for some integers $n, m, l\geq 0$. By Definition [\[f\]](#f){reference-type="ref" reference="f"} the matrix coordinates of $f(\mu) f(\pi):V_d^{\otimes n}\to V_d^{\otimes l}$ are given by $$\label{comp1}(f(\mu) f(\pi))_{{\mbox{\boldmath${i}$}}'}^{\mbox{\boldmath${i}$}}=\sum_{{\mbox{\boldmath${i}$}}''\in[m,d]}f(\mu)_{{\mbox{\boldmath${i}$}}'}^{{\mbox{\boldmath${i}$}}''}f(\pi)_{{\mbox{\boldmath${i}$}}''}^{{\mbox{\boldmath${i}$}}}.$$ Hence $(f(\mu) f(\pi))_{{\mbox{\boldmath${i}$}}'}^{\mbox{\boldmath${i}$}}$ is the number of ${\mbox{\boldmath${i}$}}''\in[m,d]$ such that the $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}'')$-coloring of $\pi$ and the $({\mbox{\boldmath${i}$}}'', {\mbox{\boldmath${i}$}}')$-coloring of $\mu$ are simultaneously good. These are exactly the ${\mbox{\boldmath${i}$}}''\in[m,d]$ such that coloring the vertices $j, j', j''$ of $\mu\star\pi$ with integers $i_j, i'_j, i''_j$ respectively, gives a good coloring of $\mu\star\pi$. Any good coloring of $\mu\star\pi$ gives rise to a good coloring of $\mu\cdot\pi$. Clearly any good coloring of $\mu\cdot\pi$ arises in this way. Moreover, two good colorings of $\mu\star\pi$ give the same good coloring of $\mu\cdot\pi$ if and only if the two colorings of $\mu\star\pi$ differ only at connected components whose vertices are not among $1,\ldots, n, 1', \ldots, l'$. Since there are $d$ choices of color for each component, we see the number of ${\mbox{\boldmath${i}$}}''\in[m, d]$ such that the $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}'')$-coloring of $\pi$ and the $({\mbox{\boldmath${i}$}}'', {\mbox{\boldmath${i}$}}')$-coloring of $\mu$ are simultaneously good is $d^{\ell(\mu, \pi)}f(\mu\cdot\pi)_{{\mbox{\boldmath${i}$}}'}^{{\mbox{\boldmath${i}$}}}$. The result follows. $\hfill\Box$

::: remark
From Proposition [\[comp\]](#comp){reference-type="ref" reference="comp"} the structure constants of the composition $f(\mu)f(\pi)$ are polynomial in the integer $d$. We will exploit this fact in section [0.1](#defRep){reference-type="ref" reference="defRep"} when we define the category $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ which "interpolates\" the category $\operatorname{Rep}(S_t; F)$ for nonnegative integer $t$, but is defined for arbitrary $t\in F$.
:::

## Definition of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ {#defRep}

In this section we define Deligne's tensor category $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ for arbitrary $t\in F$ following [@Del07 §8] (so our definition is different from the one given in [@Del07 §2]). To construct $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ we will first use partitions to construct the smaller category $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$. We then obtain $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ from $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ using the process of Karoubification.

As in the previous section, assume $d$ is a nonnegative integer and that $F$ is a field of characteristic zero. Let $\operatorname{Rep}_0(S_d; F)$ denote the full subcategory of $\operatorname{Rep}(S_d; F)$ whose objects are of the form $V_d^{\otimes n}$ for $n\geq 0$. Clearly the objects in $\operatorname{Rep}_0(S_d; F)$ are indexed by nonnegative integers, and by Theorem [\[sw\]](#sw){reference-type="ref" reference="sw"} the morphisms in $\operatorname{Rep}_0(S_d; F)$ are given (albeit not uniquely) by $F$-linear combinations of maps $f(\pi)$ indexed by set partitions. Moreover, the structure constants of compositions of the $f(\pi)$'s are polynomials in $d$ (see Proposition [\[comp\]](#comp){reference-type="ref" reference="comp"}). Using this data, we now define a tensor category similar to $\operatorname{Rep}_0(S_d; F)$ replacing the integer $d$ with an arbitrary element of $F$.

Let $t\in F$.

::: definition
The category $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ has

Objects: $[n]$ for each $n\in\mathbb{Z}_{\geq 0}$.

Morphisms: $\operatorname{Hom}_{ \underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)}([n], [m]):=FP_{n,m}$.

Composition: $FP_{m,l}\times FP_{n,m}\to FP_{n,l}$ is defined to be the bilinear map satisfying $\mu\circ\pi=t^{\ell(\mu,\pi)}\mu\cdot\pi$ for each $\pi\in P_{n,m}$, $\mu\in P_{m,l}$.
:::

To see that composition is associative, it is enough to show $\nu\circ(\mu\circ\pi)=(\nu\circ\mu)\circ\pi$ for all $\pi\in P_{n,m}$, $\mu\in P_{m,l}$, $\nu\in P_{l,k}$. To do so, consider the partition $$\includegraphics{diss8.pdf}$$ Notice that $\nu\cdot(\mu\cdot\pi)$, $(\nu\cdot\mu)\cdot\pi\in P_{n,k}$ are both obtained by restricting the partition $\nu\star\mu\star\pi$ to the set $\{1,\ldots,n,1',\ldots,k'\}$. Furthermore, $\ell(\mu,\pi)+\ell(\nu,\mu\cdot\pi)$ and $\ell(\nu,\mu)+\ell(\nu\cdot\mu,\pi)$ are both the number of connected components of $\nu\star\mu\star\pi$ whose vertices are not among $\{1,\ldots,n,1',\ldots,k'\}$. Hence composition is associative.

One can easily check that the partition in $P_{n,n}$ whose parts are all of the form $\{j, j'\}$ is the identity morphism $\text{id}_n:[n]\to[n]$.

::: example
The identity morphism $\text{id}_7:[7]\to[7]$ is given by $$~\hspace{1.45in}\includegraphics{diss9.pdf}\hspace{1.4in}\rotatebox{45}{$\Box$}$$
:::

Before giving $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ the structure of a tensor category, we pause to give the following definition which will play an important role in later sections.

::: definition
[]{#FP label="FP"} (compare with [@MR1103994], [@MR1265453]) The *partition algebra* $FP_n(t)$ is defined to be the endomorphism algebra $\text{End}_{ \underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)}([n])$.
:::

::: remark
[]{#Snembedding label="Snembedding"} We identify each element of the symmetric group $S_n$ with a partition in $P_{n,n}$ as follows: $\sigma \leftrightarrow \{\{i, \sigma(i)'\}\,|\, 1\leq i\leq n\}$. This identification extends linearly to an inclusion of algebras $FS_n\hookrightarrow FP_n(t)$ for each $t\in F$.
:::

Now to define tensor products. While reading the following definitions, the reader may find it helpful to keep in mind the analogy studied in section [\[motivation\]](#motivation){reference-type="ref" reference="motivation"} between the objects $[n]$ (resp. morphisms $\pi$) in $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ and the objects $V_d^{\otimes n}$ (resp. morphisms $f(\pi)$) in $\operatorname{Rep}(S_d; F)$.

::: definition
For objects $[n], [m]$ in $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ set $[n]\otimes[m]:=[n+m]$. For morphisms we let $\otimes: FP_{n_1,m_1}\times FP_{n_2, m_2}\to FP_{n_1+n_2, m_1+m_2}$ be the bilinear map such that $$\includegraphics{diss11.pdf}$$ for all $\pi\in P_{n_1, m_1}$, $\mu\in P_{n_2, m_2}$.
:::

::: example
Suppose $$\includegraphics{diss12.pdf}$$ Then $$\hspace{1.3in}\includegraphics{diss13.pdf}\hspace{.4in}\rotatebox{45}{$\Box$}$$
:::

Next we wish to show that $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ is a tensor category with the following choices.

-   (associativity) $\alpha_{n,m,l}:([n]\otimes[m])\otimes[l] \to[n]\otimes([m]\otimes[l])$ is the identity morphism $\text{id}_{n+m+l}$.

-   (commutativity) $\beta_{n,m}:[n]\otimes[m]\to[m]\otimes[n]$ is the partition in $P_{n+m,n+m}$ whose parts are of the form $\{j, (m+j)'\}$ or $\{n+j, j'\}$ as illustrated below. $$\includegraphics{diss14.pdf}$$

-   (unit) Set ${\bf 1}:=[0]$. Both unit morphisms $[0]\otimes[n]\to[n]$ and $[n]\otimes[0]\to[n]$ are the identity morphism $\text{id}_n$.

-   (duals) Set $[n]^\vee:=[n]$ with the morphism $ev_n:[n]^\vee\otimes [n]\to {\bf 1}$ (resp. $coev_n:{\bf 1}\to [n]\otimes [n]^\vee$) given by the partition in $P_{2n,0}$ (resp. $P_{0,2n}$) whose parts are of the form $\{j, n+j\}$ (resp. $\{j',(n+j)'\}$) as illustrated below.

$$\includegraphics{diss16.pdf}$$ $$\includegraphics{diss15.pdf}$$

The triangle and pentagon axioms are easily satisfied, as all morphisms in both diagrams are identity morphisms. The following diagrams illustrate the hexagon axiom. $$\includegraphics{diss17.pdf}$$ The diagrams below illustrate that the choice of dual objects as well as the evaluation and coevaluation morphisms make $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ into a rigid category. $$\includegraphics{diss18.pdf}$$ Finally, $\text{End}_{ \underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)}({\bf 1})=F$ as $P_{0,0}$ contains only the empty partition. Thus $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ is a tensor category.

::: remark
[]{#fzero label="fzero"} For $d\in\mathbb{Z}_{\geq0}$, the connection between $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_d; F)$ and $\operatorname{Rep}_0(S_d; F)$ can be made more precise as follows. The functor $\mathcal{F}_0: \underline{\operatorname{Re}}\!\operatorname{p}_0(S_d; F)\to  \operatorname{Rep}_0(S_d; F)$ given on objects by $[n]\mapsto V_d^{\otimes n}$, and on morphisms as the $F$-linear map $\pi\mapsto f(\pi)$ is a tensor functor. $\mathcal{F}_0$ is certainly surjective on objects. Moreover, by Theorem [\[sw\]](#sw){reference-type="ref" reference="sw"}(1), $\mathcal{F}_0$ is surjective on morphisms. However, by Theorem [\[sw\]](#sw){reference-type="ref" reference="sw"}(2), $\mathcal{F}_0$ does not give an equivalence of categories.
:::

Now we are ready to use the process of Karoubification to define Deligne's category. For more on this process see [@Del07 1.7-8]. Informally, $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ is the category obtained from $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ by adding formal direct sums and images of idempotents. Let us be more precise:

::: definition
Let $\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)$ denote the *additive envelope* of $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ so that $\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)$ has

Objects: finite tuples of objects in $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ written as $A_1\oplus\cdots\oplus A_k$ for objects $A_1,\ldots, A_k$ in $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$. We also include the empty tuple which is the zero object in $\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)$.

Morphisms: $\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)}\left(\bigoplus_{i=1}^kA_i, \bigoplus_{i=1}^lB_i\right)$ is the set of all $l\times k$-matrices whose $(i,j)$-entry is a morphism $A_j\to B_i$ in $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$.

Composition: given by matrix multiplication along with the induced composition from $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$.
:::

::: definition
Let $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ denote the *Karoubian envelope*[^1] of $\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)$ which has

Objects: pairs $(A, e)$ where $A$ is an object in $\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)$ and $e\in\text{End}_{\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)}(A)$ is an idempotent.

Morphisms: $\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)}\left((A,e), (B,f)\right):=f\operatorname{Hom}_{\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)}(A, B)e$.

Composition: induced from composition in $\underline{\operatorname{Re}}\!\operatorname{p}_1(S_t; F)$.
:::

The following properties of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ follow from general theory of additive and Karoubian envelopes.

::: proposition
[]{#proprep label="proprep"} (1) The obvious tensor product on objects and morphisms, as well as the obvious associativity, commutativity, unit, and dual constraints make $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ a tensor category.

\(2\) Given a nonnegative integer $n$ and a nonzero idempotent $e\in FP_n(t)$, the object $([n], e)$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ is indecomposable if and only if $e$ is primitive[^2]. Moreover, every indecomposable object in $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ is isomorphic to one of the form $([n], e)$. Finally, given two primitive idempotents $e, e'\in FP_n(t)$, the objects $([n], e)$ and $([n], e')$ are isomorphic if and only if $e$ and $e'$ are conjugate[^3] in $FP_n(t)$.

\(3\) (Krull-Schmidt property) Every object in $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ can be decomposed as a finite direct sum of indecomposable objects. Moreover, if $A=L_1\oplus\cdots\oplus L_r$ and $A=L'_1\oplus\cdots\oplus L'_s$ are two decomposition of $A$ into indecomposables, then $r=s$ and there is a permutation $\sigma\in S_r$ with $L_i\cong L_{\sigma(i)}'$ for all $1\leq i\leq r$.
:::

::: remark
Informally, studying the category $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ is a way to simultaneously study the partition algebras $FP_n(t)$ for all $n\geq 0$ (see Definition [\[FP\]](#FP){reference-type="ref" reference="FP"}). In this line of thinking, studying $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$ is a way to simultaneously study all finitely generated projective right $FP_n(t)$-modules for all $n\geq 0$.
:::

##  {#trace}

We close this section by examining the trace of a morphism in $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$. First, notice that $\text{tr}\,:\text{End}_{\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)}([n])\to F$ is an $F$-linear map. Furthermore, if $\pi:[n]\to [n]$ is a partition diagram (not equal to $\text{id}_0$) then, by the definition of trace (see [@Del07 3.3]), $\text{tr}\,(\pi)=t^\ell$ where $\ell$ is the number of connected components in the diagram $$\includegraphics{diss36.pdf}$$ Clearly $\ell$ is also the number of connected components in the following *trace diagram*$$\includegraphics{diss37.pdf}$$

::: example
[]{#traces label="traces"}(i) The only endomorphisms in $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_0; F)$ with nonzero trace are nonzero scalar multiples of $\text{id}_0$.

\(ii\) In $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$, $\dim([0])=\text{tr}\,(\text{id}_0)=1$ and $\dim([n])=\text{tr}\,(\text{id}_n)=t^n$ for all positive $n$.

\(iii\) Consider $\pi:[7]\to [7]$ given by $$\includegraphics{diss38.pdf}$$ $\text{tr}\,(\pi)=t^4$ since there are 4 connected components in the diagram $$~\hspace{1.4in}\includegraphics{diss39.pdf}\hspace{1.3in}\rotatebox{45}{$\Box$}$$
:::

[^1]: Some authors, including Deligne, refer to Karoubian envelopes as pseudo-abelian completions.

[^2]: An idempotent is *primitive* if it is nonzero and it cannot be written as a sum $e_1+e_2$ where $e_1$ and $e_2$ are nonzero idempotents with $e_1e_2=e_2e_1=0$.

[^3]: Recall that two idempotents $e,e'$ in a finite dimensional algebra $A$ are conjugate if and only if the modules $Ae$ and $Ae'$ are isomorphic.
