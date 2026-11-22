---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP"
section_id: sec-002-3-two-iterative-formulas
section_title: "Two Iterative Formulas"
section_number: 3
pages: 7-13
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.954
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP — The paper studies how to compute irreducible characters of the generalized symmetric group Ck ≀Sn by iterative algorithms."
---
Using techniques of vertex operators, we have the following commutation relations for the vertex operators (cf. [@J3]): $$\begin{aligned}
\label{e:com1a}
    zX_i(z)X_i(w)&+wX_i(w)X_i(z)=0, \\ \label{e:com2a}
    A_i^*(z)X_i(w)&=X_i(w)A_i^*(z)+\frac{w}{z-w}X_i(w),\\
 \label{e:com3a}
    X_i^*(z)A_i(w)&=A_i(w)X_i^*(z)+\frac{w}{z-w}X_i^*(z).
\end{aligned}$$ Taking the coefficients of $z^mw^n$, we derive the following commutation relations among the components.

::: prop
[]{#P:3.1 label="P:3.1"} For $m,n\in \mathbb{N}$,$i\in I$, we have $$\begin{aligned}
\label{e:com1}
        X_{im}X_{in}&=-X_{i(n-1)}X_{i(m+1)}, \\ \label{e:com2}
        X_{im}^*.1&=0, \quad a_{-im}^*.1=0, \\ \label{e:com3}
        a_{-im}^*X_{in}&=X_{in}a_{-im}^*+X_{i(n-m)},\\ \label{e:com4}
        X_{im}^*a_{-in}&=a_{-in}X_{im}^*+X_{i(m-n)}^*.
     
\end{aligned}$$
:::

Recall that for two partitions $\mu \subset\lambda$, if the skew partition $\lambda-\mu$ is connected and contains no $2*2$ boxes, we call $\lambda-\mu$ a *rim hook* or *border strip*. The height of $\lambda-\mu$ is defined to be one less than the number of rows occupied, denoted by $\mathrm{ht}(\lambda-\mu)$ or $\mathrm{ht}(\lambda/\mu)$. For example, take $\lambda=(5,3,2,2), \mu=(2,1,1)$, then $\lambda-\mu$ can be depicted as\

::: center
$\young(::~~~,:~~,:~,~~)$
:::

 \
which is a $8$-rim hook of $\lambda$ with height 3. Note that a hook is a special case of the rim hook.

If $\xi$ is a rim hook contained in a Young diagram $\lambda$, then $\lambda\setminus\xi$ denotes the *subdiagram* of $\lambda$ obtained by removing $\xi$. It is clear that $\lambda\setminus\xi$ is also a Young diagram, so we also use it refer to the associated partition. In the above example, $\xi=(5, 3, 2, 2)-(2, 1, 1)$ is the rim hook, and the difference partition is $$\label{e:minus}
\lambda\setminus\xi=(2, 1, 1).$$

A colored partition $\boldsymbol{\lambda}=(\lambda^{(i)})$ is contained in a colored partition $\boldsymbol{\mu}=(\mu^{(i)})$, denoted by $\boldsymbol{\lambda}\subset\boldsymbol{\mu}$, if each constituent partition $\lambda^{(i)}\subset\mu^{(i)}$. The difference $\boldsymbol{\xi}=\boldsymbol{\lambda}-\boldsymbol{\mu}$ is called a rim-hook if one of the constituents $\lambda^{(i)}-\mu^{(i)}$ is a rim-hook and all other constituents are identical, i.e., the colored rim-hook $\boldsymbol{\xi}$ is only supported at the $i$th constituent.

For an integral $l$-tuple $\mu=(\mu_1, \ldots, \mu_l)$, we define the lowering operator $T_n$ ($1\leq n\leq l-1$) by $$\begin{aligned}
        T_n: \quad (\mu_1,\cdots \mu_n,\mu_{n+1},\cdots \mu_l) \mapsto (\mu_1,\cdots \mu_{n+1}-1,\mu_n+1,\cdots \mu_l).
     
\end{aligned}$$ Now we give a characterization of $m$-rim hook $\eta$ by using lowering operators. Let $\xi=(\lambda_1,\cdots,\lambda_{i-1},\lambda_{i}-m,\lambda_{i+1},\cdots,\lambda_l)$ be the integral $l$-tuple obtained by the action [\[e:com3\]](#e:com3){reference-type="eqref" reference="e:com3"} of vertex operators.

::: lem
[]{#l:mstrip label="l:mstrip"} Any $m$-rim hook $\eta$ can be written as a difference of a partition $\lambda$ and $\mathrm{ht}(\eta)$ applications of $T_{i}$ to the integral $l$-tuple $(\lambda_1, \ldots, \lambda_{i-1}, \lambda_i-m, \lambda_{i+1}, \ldots,
\lambda_l)$.
:::

::: proof
*Proof.* Assume that a $m$-rim hook $\eta$ begins at the $i$-th row of $\lambda$. If its height is 0, i.e., it only occupies the $i$-th row of $\lambda$. Then $m\leq \lambda_i-\lambda_{i+1}$, or $\lambda_i-m\geq \lambda_{i+1}$, so $\xi$ is already a partition and $\eta=\lambda-\xi$. Suppose now $\mathrm{ht}(\eta)=1$ and that it occupies the $i$-th and $(i+1)$-th rows of $\lambda$. By definition of a rim hook, $\lambda_i-\lambda_{i+1}+2\leq m\leq \lambda_i-\lambda_{i+2}+1$, so $\lambda_{i+2}-1\leq \lambda_i-m\leq \lambda_{i+1}-2$. Hence $\eta=\lambda-T_i(\xi)$ and $T_i(\xi)$ is a partition. In general, if the height of an $m$-rim hook is $r\geq 1$, one has $$\begin{aligned}
\notag
    \sum_{j=0}^{r-1} &(\lambda_{i+j}-\lambda_{i+j+1}+1)+1 \leq m\\
    &\leq \sum_{j=0}^{r-1}(\lambda_{i+j}-\lambda_{i+j+1}+1)+(\lambda_{i+r}-\lambda_{i+r+1}).
\end{aligned}$$ Then $\lambda_{i+r+1}-r\leq \lambda_i-m\leq \lambda_{i+r}-(r+1)$, and we obtain $\eta=\lambda-T_{i+r-1}\cdots T_{i}(\xi)$. ◻
:::

::: lem
[]{#l:MN1 label="l:MN1"} For each $j\in I$, any partition $\lambda=(\lambda_1,\lambda_2,\cdots \lambda_l)$, and any $m\in \mathbb{N}$, we have $$\begin{aligned}
\label{e:action}
    a_{-jm}^*s_{j\lambda}
 &=\sum_\mu(-1)^{\mathrm{ht}(\lambda/\mu)}s_{j\mu},
    
\end{aligned}$$ summed over all partitions $\mu$ such that $\lambda-\mu$ is an $m$-rim hook.
:::

::: proof
*Proof.* Repeatedly using [\[e:com3\]](#e:com3){reference-type="eqref" reference="e:com3"} we have that $$\begin{aligned}
        a_{-jm}^*s_{j\lambda}=\sum_{i=1}^{l}X_{j\lambda_1}\cdots X_{j\lambda_i-m}\cdots X_{j\lambda_l}.1.
    
\end{aligned}$$ The vector $X_{j\lambda_1}\cdots X_{j\lambda_i-m}\cdots X_{j\lambda_l}.1$ is the Schur function associated with integral $l$-tuple $(\lambda_1, \ldots, \lambda_{i-1}, \lambda_i-m, \lambda_{i+1}\ldots, \lambda_l)$. If $\lambda_i-m<\lambda_{i+1}$, we need to straighten out the integral $l$-tuple to partition. We use [\[e:com1\]](#e:com1){reference-type="eqref" reference="e:com1"} to rewrite $$X_{j\lambda_1}\cdots X_{j\lambda_i-m}\cdots X_{j\lambda_l}.1=-X_{j\lambda_1}\cdots X_{j\lambda_{i+1}-1}X_{j\lambda_i-m+1}\cdots X_{j\lambda_l}.1.$$

If $\lambda_i-m+1=\lambda_{i+1}$, then the term vanishes. If $\lambda_i-m+1<\lambda_{i+2}$, then we repeat the swapping $(\lambda_i-m+1, \lambda_{i+2})\to (\lambda_{i+2}-1, \lambda_{i+2}-m+2)$ until we have a partition. Suppose after $r$ steps, we reach the partition $$\begin{aligned}
    \xi=(\lambda_1,\cdots,\lambda_{i-1},\lambda_{i+1}-1,\cdots,\lambda_{i+r}-1,\lambda_i-m+r,\lambda_{i+r+1},\cdots,\lambda_l).
    
\end{aligned}$$ Then the skew partition $$\lambda-\xi=(0^{i-1}, \lambda_i-\lambda_{i+1}+1, \ldots,
\lambda_{i+r}-\lambda_i+m-r, \lambda_{i+r+1}, \ldots, \lambda_l)$$ is a $m$-rim hook and $s_{j\lambda}=(-1)^rs_{j\xi}$.

Conversely, suppose $\xi$ is a partition such that $\lambda-\xi$ is a horizontal $m$-strip. By Lemma [\[l:mstrip\]](#l:mstrip){reference-type="ref" reference="l:mstrip"} the term $s_{\xi}$ appears in the expansion of $a_{-jm}^*s_{j\lambda}$. Therefore [\[e:action\]](#e:action){reference-type="eqref" reference="e:action"} is proved. ◻
:::

::: exmp
$$\begin{aligned}
        a_{-1,4}^*s_{1(5,3,2)}&=s_{1(1,3,2)}+s_{1(5,-1,2)}+s_{1(5,3,-2)}\\\nonumber
        &=-s_{1(2,2,2)}-s_{1(5,1,0)}        
    
\end{aligned}$$
:::

Similarly, a colored partition $\boldsymbol{\mu}\subset\boldsymbol{\lambda}$ such that $\boldsymbol{\lambda}-\boldsymbol{\mu}$ is a *colored rim hook* if and only if one of its constituents is a rim hook and the others are $\phi$. The height of $\boldsymbol{\lambda}-\boldsymbol{\mu}$ is exactly the height of its nonempty constituent, denoted by $\mathrm{ht}(\boldsymbol{\lambda}-\boldsymbol{\mu})$ or $\mathrm{ht}(\boldsymbol{\lambda}/\boldsymbol{\mu})$. For example, if $\boldsymbol{\lambda}=((2,1),(5,3,2,2),(4))$, and $\boldsymbol{\mu}=((2,1),(2,1,1),(4))$, then $\boldsymbol{\lambda}-\boldsymbol{\mu}$ is an 8-rim hook colored at the second constituent with height $3$.\

::: center
$\{\emptyset$, $\young(::~~~,:~~,:~,~~)$, $\emptyset\}$
:::

If $\boldsymbol{\xi}$ is a colored rim hook contained in a colored Young diagram $\boldsymbol{\lambda}$, then $\boldsymbol{\lambda}\setminus\boldsymbol{\xi}$ denotes the *colored subdiagram* of $\boldsymbol{\lambda}$ obtained by removing $\boldsymbol{\xi}$. Similarly we also use $\boldsymbol{\lambda}\setminus\boldsymbol{\xi}$ to denote the associated colored partition.

Now we are ready to give a vertex algebraic proof of the Murnaghan-Nakayama rule for the generalized symmetric group $C_k\wr S_n$. The formula [\[e:MN-rule1\]](#e:MN-rule1){reference-type="eqref" reference="e:MN-rule1"} was first proved by group theoretical method in [@AK].

::: thm
[]{#t:MN-gensym label="t:MN-gensym"} Given colored partitions $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\cdots,\lambda^{(k-1)})$ and $\boldsymbol{\rho}=(\rho^{(0)},\rho^{(1)},\cdots,\rho^{(k-1)})$ of $n$, where $\rho^{(s)}=(\rho^{(s)}_1,\cdots,\rho^{(s)}_m,\cdots,\rho^{(s)}_{l(s)})$. Then the value of the irreducible character $\chi^{\boldsymbol{\lambda}}$ of $C_k\wr S_n$ at the class $\boldsymbol{\rho}$ is given by $$\begin{aligned}
\label{e:MN-rule1}
        \chi^{\boldsymbol{\lambda}}_{\boldsymbol{\rho}}=\sum_{j=0}^{k-1}\sum_{\boldsymbol{\xi_j}}(-1)^{\mathrm{ht}(\boldsymbol{\xi_j})}\omega^{-sj}\chi^{\boldsymbol{\lambda}\backslash\boldsymbol{\xi_j}}_{\boldsymbol{\rho}\setminus\rho^{(s)}_m},
    
\end{aligned}$$ where ${\boldsymbol{\xi_j}}$ runs through all colored $\rho^{(s)}_m$-rim hooks contained in ${\boldsymbol{\lambda}}$ that are supported at the $j$-th constituent.
:::

::: proof
*Proof.* Fixing $j\in I$, it follows from [\[e:2.6\]](#e:2.6){reference-type="eqref" reference="e:2.6"} that: $$a_{-j\rho^{(s)}_m}^*s_{i\lambda^{(i)}}=0,$$ if $i\neq j$. Then nonzero contributions only come from $$a_{-j\rho^{(s)}_m}^*s_{\boldsymbol{\lambda}}=s_{0\lambda^{(0)}}\cdots (a_{-j\rho^{(s)}_m}^*s_{j\lambda^{(j)}})\cdots s_{(k-1)\lambda^{(k-1)}}.$$ By Lemma [\[l:MN1\]](#l:MN1){reference-type="ref" reference="l:MN1"}, $a_{-j\rho^{(s)}_m}^*s_{\boldsymbol{\lambda}}$ is expanded into an alternating sum of $s_{\boldsymbol{\lambda}\backslash\boldsymbol{\xi_j}}$ such that $\boldsymbol{\xi_j}$ is a colored $\rho^{(s)}_m$-rim hook supported at the $j$-th constituent. By Theorem [\[t:FJW\]](#t:FJW){reference-type="ref" reference="t:FJW"} and converting back to the basis ${\widetilde{a}_{-s\rho^{(s)}_m}}$, using $$\begin{aligned}
         {\widetilde{a}_{-s\rho^{(s)}_m}}=\sum_{j=0}^{k-1}\omega^{-sj}a_{-j\rho^{(s)}_m},
     
\end{aligned}$$ we have shown the theorem. ◻
:::

::: exmp
In the group $C_3\wr S_{12}$, we have $$\begin{aligned}
        \chi^{((4,1),(3,1,1),(2))}_{((5,2),(3),(1,1))}=-\chi^{(\emptyset,(3,1,1),(2))}_{((2),(3),(1,1))}+\chi^{((4,1),\emptyset,(2))}_{((2),(3),(1,1))}.
    
\end{aligned}$$ Similarly in $C_3\wr S_{14}$, one has $$\begin{aligned}
        \chi^{((3,2),(4,2,1),(2))}_{((2,1),(4,3),(3,1))}=-\chi^{((1),(4,2,1),(2))}_{((2,1),(3),(3,1))}-\omega^2\chi^{((3,2),(1,1,1),(2))}_{((2,1),(3),(3,1))},
    
\end{aligned}$$ where $\omega$ is the 3-rd primitive root of unity.
:::

Similar to the symmetric group, we have the following result by applying Theorem [\[t:MN-gensym\]](#t:MN-gensym){reference-type="ref" reference="t:MN-gensym"}. Recall that a *colored hook* is a special colored partition if and only if one of its constituent is a hook and the others are $\emptyset$. The length of arm and leg of a colored hook are exactly those of its nonempty constituent respectively. Obviously a colored hook is a special colored rim hook.

::: prop
Let $\boldsymbol{\kappa}_i$ be a colored partition supported only at the $i$-th constituent $(n)$ and $\omega$ the $k$-th primitive root of unity. Then the irreducible character $\chi^{\boldsymbol{\lambda}}$ of $C_k\wr S_n$ satisfies $$\begin{aligned}
        \chi^{\boldsymbol{\lambda}}(\boldsymbol{\kappa}_i)=(-1)^r\omega^{-ij} \quad or \quad 0
    
\end{aligned}$$ according as $\boldsymbol{\lambda}$ is a colored hook or not, where $j$ is the index of its non-empty constituent and $r$ is its length of leg.
:::

Now we study how to decompose the irreducible characters using the dual vertex operator in the other direction.

For each partition $\rho=(\rho_1,\rho_2,\cdots,\rho_l)$, a *subpartition* denoted by $\mu\vartriangleleft\rho$ is $\mu=\emptyset$ or $\mu=(\rho_{i_1},\rho_{i_2},\cdots,\rho_{i_s})$, for some $1\leqslant i_1<\cdots<i_s\leqslant l$. Obviously, there are $2^{l(\rho)}$ subpartitions $\mu$ such that $\mu\vartriangleleft\rho$ and $\rho\backslash\mu$ is also a partition. For example, if $\rho=(4,2,2,1)$, and $\mu=(2,1)$, then $\mu\vartriangleleft\rho$ and $\rho\backslash\mu=(4,2)$. Moreover, $\mu\cup\tau$ of partitions $\mu$ and $\tau$, is defined as the union of parts of $\mu$ and $\tau$ in the descending order.

::: lem
[]{#l:3.8 label="l:3.8"} For any partition $\rho=(\rho_1,\rho_2,\cdots,\rho_l)$, $m\in \mathbb{N}$, and $i,j\in I$, one has that $$\begin{aligned}
        X_{jm}^*\widetilde{a}_{-i\rho}=\sum_{\mu\vartriangleleft\rho}\omega^{-ij\cdot(l(\mu))}\widetilde{a}_{-i\rho\backslash\mu}X_{j(m-|\mu|)}^*,
     
\end{aligned}$$ summed over all subpartitions of $\rho$.
:::

::: proof
*Proof.* For each $1\leq s\leq l$, it follows from the linearity of $\widetilde{a}_{-i\rho_s}$ and the action of [\[e:com4\]](#e:com4){reference-type="eqref" reference="e:com4"} that $$\begin{aligned}
        X_{jm}^*\widetilde{a}_{-i\rho_s}=\widetilde{a}_{-i\rho_s}X_{jm}^*+\omega^{-ij}X_{j(m-\rho_s)}^*.
    
\end{aligned}$$

In the case of length $2$ partition, the expression becomes

$$\begin{aligned}
        \widetilde{a}_{-i\rho}X_{jm}^*+\omega^{-ij}\widetilde{a}_{-i\rho_1}X_{j(m-\rho_2)}^*+\omega^{-ij}\widetilde{a}_{-i\rho_2}X_{j(m-\rho_1)}^*+\omega^{-ij\cdot 2}X_{j(m-|\rho|)}^*.
    
\end{aligned}$$ Using induction on $l(\rho)$, we get the lemma. ◻
:::

For two colored partitions $\boldsymbol{\mu}$ and $\boldsymbol{\rho}$, if for each $i\in I$, such that $\mu^{(i)}\vartriangleleft\rho^{(i)}$, we write $\boldsymbol{\mu}\vartriangleleft\boldsymbol{\rho}$. The set minus $\boldsymbol{\rho}\backslash\boldsymbol{\mu}$ (removing the empty rows) is also a colored partition. For example, if $\boldsymbol{\rho}=((5,3,1),(4,2,2,1),(4))$, and $\boldsymbol{\mu}=((3),(2,1),(4))$, then $\boldsymbol{\mu}\vartriangleleft\boldsymbol{\rho}$ and $\boldsymbol{\rho}\backslash\boldsymbol{\mu}=((5,1),(4,2),\emptyset)$.

A colored partition $\boldsymbol{\rho}$ naturally gives rise to a partition by forgetting the colors, we call this partition the *rearrangement* of $\boldsymbol{\rho}$. For example, take $\boldsymbol{\rho}=((5,1),\emptyset,(4,2))$, it can be rearranged into a regular partition $(5,4,2,1)$.

We also define the length of a colored partition $l(\boldsymbol{\rho})$ as the sum of $l(\rho^{(i)})$. Recall that the weighted length $\eta(\boldsymbol{\rho})$ is defined as $\sum_iil(\rho^{(i)})$. The juxtaposition $\boldsymbol{\mu}\cup \boldsymbol{\tau}$ of two colored partitions is defined as $(\mu^{(i)}\cup \tau^{(i)})$.

Now we are ready to give our second main result--the dual Maunaghan-Nakayama rule for the generalized symmetric group.

::: thm
[]{#t:3.9 label="t:3.9"} Given colored partitions $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\cdots,\lambda^{(k-1)})$ and $\boldsymbol{\rho}=(\rho^{(0)},\rho^{(1)},\cdots,\rho^{(k-1)})$ of $n$. Then for any fixed $j\in I$, the irreducible character value of $C_k\wr S_n$ is given by $$\begin{aligned}
\label{e:MN-rule2}
        \chi^{\boldsymbol{\lambda}}_{\boldsymbol{\rho}}=\sum_{\substack{\boldsymbol{\mu}\vartriangleleft\boldsymbol{\rho},\|\boldsymbol{\mu}\|\geq\lambda^{(j)}_1\\\boldsymbol{\tau}\vdash \|\boldsymbol{\mu}\|-\lambda^{(j)}_1}}\omega^{(\eta(\boldsymbol{\tau})-\eta(\boldsymbol{\mu}))j}\frac{{(-1)}^{l(\boldsymbol{\tau})}}{k^{l(\boldsymbol{\tau})}z_{\tau}}\chi^{\boldsymbol{\lambda}\setminus \lambda^{(j)}_1}_{(\boldsymbol{\rho}\backslash\boldsymbol{\mu})\cup\boldsymbol{\tau}}
    
\end{aligned}$$ where the sum is over colored partitions $\boldsymbol{\mu}$ and $\boldsymbol{\tau}$ such that $\boldsymbol{\mu}\vartriangleleft\boldsymbol{\rho}$, with weight bigger than $\lambda^{(j)}_1$, and $\boldsymbol{\tau}$ of weight $\|\boldsymbol{\mu}\|-\lambda^{(j)}_1$. $z_{\tau}$ is defined in [\[e:innerprod\]](#e:innerprod){reference-type="eqref" reference="e:innerprod"}, $\tau$ is the rearrangement of $\boldsymbol{\tau}$, and $\eta(\boldsymbol{\tau})$, $\eta(\boldsymbol{\mu})$ are the weighted lengths $\sum_ii l(\tau^{(i)})$, $\sum_ii l(\mu^{(i)})$ respectively.
:::

::: proof
*Proof.* Applying Lemma [\[l:3.8\]](#l:3.8){reference-type="ref" reference="l:3.8"} repeatedly, one has $$\begin{aligned}
\label{p:1}
        X_{jm}^*\widetilde{a}_{-\boldsymbol{\rho}}=\sum_{\boldsymbol{\mu}\vartriangleleft\boldsymbol{\rho}}\omega^{-\eta(\boldsymbol{\mu})j}\widetilde{a}_{-\boldsymbol{\rho}\backslash\boldsymbol{\mu}}X_{j(m-\|\boldsymbol{\mu}\|)}^*.1,
    
\end{aligned}$$ summed over all colored partitions $\boldsymbol{\mu}$ such that $\boldsymbol{\mu}\vartriangleleft\boldsymbol{\rho}$. By [\[e:com2\]](#e:com2){reference-type="eqref" reference="e:com2"}, nonzero items survive only when $m-\|\boldsymbol{\mu}\| \leq 0$. Taking the coefficient of $z^{n}$ in $X_j(z)^*$, we have that $$\begin{aligned}
\label{p:2}
        X_{jn}^*.1=\sum_{\rho\vdash n}\frac{{(-1)}^{l(\rho)}}{z_\rho}a_{-j\rho} \quad for \quad n\geq 0.
    
\end{aligned}$$ By [\[e:2.9\]](#e:2.9){reference-type="eqref" reference="e:2.9"} and [\[e:2.11\]](#e:2.11){reference-type="eqref" reference="e:2.11"}, for a partition $\tau=(\tau_1, \tau_2, \cdots, \tau_{l(\tau)})$ we have

$$\begin{aligned}
        \label{e:3.20}
        a_{-j\tau}&=\frac{1}{k^{l(\tau)}}\prod_{s=1}^{l(\tau)}\left(\sum_{i_s=0}^{k-1}\omega^{ji_s}\widetilde{a}_{-i_s\tau_s}\right)
    \\ \nonumber
        &=\frac{1}{k^{l(\tau)}}\sum_{(i_1,\cdots i_{l(\tau)})\in I^{l(\tau)}}\omega^{|i|j}\widetilde{a}_{-i_1\tau_1}\cdots \widetilde{a}_{-i_{l(\tau)}\tau_{l(\tau)}},
        
\end{aligned}$$ where $(i_1,\cdots i_{l(\tau)})$ runs through the Cartesian product $I^{l(\tau)}$ and $|i|=i_1+\cdots +i_{l(\tau)}$.

We rewrite the $k^{l(\tau)}$ summands by reordering factors according to their colors, where the pairs $(i_1, \tau_1), (i_2, \tau_2), \ldots, (i_{l(\tau)}, \tau_{l(\tau)})$ are rearranged according to their colors. Then the composition $(\tau_1, \tau_2, \ldots, \tau_{l(\tau)})$ becomes a colored partition $\boldsymbol{\tau}$ and the summation of its colors $|i|=i_1+\cdots+i_{l(\tau)}$ becomes $\eta(\boldsymbol{\tau})$. Therefore $$\label{e:conversion}
    a_{-j\tau}=\frac1{k^{l(\tau)}}\sum_{\boldsymbol{\tau}}
    \omega^{j\eta(\boldsymbol{\tau})}\tilde{a}_{-\boldsymbol{\tau}},$$ where the sum runs through all colored partitions arising from $\tau$. Plugging [\[e:conversion\]](#e:conversion){reference-type="eqref" reference="e:conversion"} into [\[e:3.20\]](#e:3.20){reference-type="eqref" reference="e:3.20"} and using [\[p:1\]](#p:1){reference-type="eqref" reference="p:1"} and [\[p:2\]](#p:2){reference-type="eqref" reference="p:2"}, we have derived the recurrence formula. ◻
:::

We remark that the dual Murnaghan-Nakayama rule of $C_k\wr S_n$ offers a different iterative route from the Ariki-Koike version by directly simplifying the indexing colored-partition of the irreducible representation by removing the largest row in a fixed constituent, while the usual Murnaghan-Nakayama rule is iterated by removing all possible rim-hooks from the indexing partition in all constituents.

When $k=1$, we have the following dual Maunaghan-Nakayama rule for the symmetric group, which seems new to the authors' knowledge.

::: thm
[]{#c:3.10 label="c:3.10"} The irreducible character value of $S_n$ is given by $$\begin{aligned}
        \chi^{\lambda}_{\rho}=\sum_{\substack{\mu\vartriangleleft\rho,|\mu|\geq\lambda_1\\\tau\vdash |\mu|-\lambda_1}}\frac{{(-1)}^{l(\tau)}}{z_\tau}\chi^{\lambda\setminus \lambda_1}_{(\rho\backslash\mu)\cup\tau},
    
\end{aligned}$$ summed over partitions $\mu$ and $\tau$ such that $\mu$ is a subpartition of $\rho$ with weight bigger than $\lambda_1$, and $\tau$ of weight $|\mu|-\lambda_1$.
:::

::: exmp
Using the recurrence relation, we see that in $C_2\wr S_4$ $$\begin{aligned}
        \chi^{((1),(3))}_{((2,1),(1))}=-\frac{1}{2}\chi^{((1),\emptyset)}_{((1),\emptyset)}+\frac{1}{2}\chi^{((1),\emptyset)}_{(\emptyset,(1))}.
    
\end{aligned}$$ Similarly in $C_3\wr S_8$, we have $$\begin{aligned}
\notag
        \chi^{((2),(5),(1))}_{((3,1),(2),(2))}=&\frac{8}{9}\chi^{((2),\emptyset,(1))}_{((3),\emptyset,\emptyset)}-\frac{1}{9}\omega\chi^{((2),\emptyset,(1))}_{(\emptyset,(3),\emptyset)}-\frac{1}{9}\omega^2\chi^{((2),\emptyset,(1))}_{(\emptyset,\emptyset,(3))}\\\nonumber
        &-\frac{1}{9}\chi^{((2),\emptyset,(1))}_{((2,1),\emptyset,\emptyset)}-\frac{5}{18}\omega^2\chi^{((2),\emptyset,(1))}_{(\emptyset,(2,1),\emptyset)}-\frac{5}{18}\omega\chi^{((2),\emptyset,(1))}_{(\emptyset,\emptyset,(2,1))}\\\nonumber
        &+\frac{1}{18}\omega\chi^{((2),\emptyset,(1))}_{((2),(1),\emptyset)}+\frac{1}{18}\omega^2\chi^{((2),\emptyset,(1))}_{((2),\emptyset,(1))}-\frac{5}{18}\chi^{((2),\emptyset,(1))}_{(\emptyset,(2),(1))}\\\nonumber
        &+\frac{5}{9}\omega\chi^{((2),\emptyset,(1))}_{((1),(2),\emptyset)}+\frac{5}{9}\omega^2\chi^{((2),\emptyset,(1))}_{((1),\emptyset,(2))}-\frac{5}{18}\chi^{((2),\emptyset,(1))}_{(\emptyset,(1),(2))}\\\nonumber
        &+\frac{4}{81}\chi^{((2),\emptyset,(1))}_{((1,1,1),\emptyset,\emptyset)}-\frac{1}{162}\chi^{((2),\emptyset,(1))}_{(\emptyset,(1,1,1),\emptyset)}-\frac{1}{162}\chi^{((2),\emptyset,(1))}_{(\emptyset,\emptyset,(1,1,1))}\\\nonumber
        &+\frac{5}{54}\omega\chi^{((2),\emptyset,(1))}_{((1,1),(1),\emptyset)}+\frac{5}{54}\omega^2\chi^{((2),\emptyset,(1))}_{((1,1),\emptyset,(1))}-\frac{1}{54}\omega\chi^{((2),\emptyset,(1))}_{(\emptyset,(1,1),(1))}\\\nonumber
        &-\frac{1}{54}\omega^2\chi^{((2),\emptyset,(1))}_{(\emptyset,(1),(1,1))}+\frac{1}{27}\omega^2\chi^{((2),\emptyset,(1))}_{((1),(1,1),\emptyset)}+\frac{1}{27}\omega\chi^{((2),\emptyset,(1))}_{((1),\emptyset,(1,1))}\\\nonumber
        &+\frac{2}{27}\chi^{((2),\emptyset,(1))}_{((1),(1),(1))},
    
\end{aligned}$$ where $\omega$ is the 3-rd primitive root of unity. For example, in the expansion of $\chi^{((2),\emptyset,(1))}_{(\emptyset,(2,1),\emptyset)}$, there are only two terms: $\boldsymbol{\mu}=((3,1),\emptyset,(2)), \boldsymbol{\tau}=(\emptyset,(1),\emptyset)$ and $\boldsymbol{\mu'}=((3,1),(2),(2)), \boldsymbol{\tau'}=(\emptyset,(2,1),\emptyset)$. Therefore its coefficient is a sum of two terms.
:::

The following is a special case of a direct consequence of Theorem [\[t:3.9\]](#t:3.9){reference-type="ref" reference="t:3.9"}.

::: prop
Let $\boldsymbol{\kappa}_i$ be a colored partition supported only at the $i$th constituent $(n)$. Then for any colored partition $\boldsymbol{\rho}=(\rho^{(0)},\rho^{(1)},\cdots,\rho^{(k-1)})$ of $n$, we have that $$\begin{aligned}
        \chi^{\boldsymbol{\kappa}_i}_{\boldsymbol{\rho}}=\omega^{-\eta(\boldsymbol{\rho})i},
    
\end{aligned}$$ where $\eta(\boldsymbol{\rho})$ is the weight length $\sum_i il({\rho}^{(i)})$.
:::
