---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-018-53-on-the-equivalence-relation-t
section_title: "On the equivalence relation t"
section_number: 5.3
pages: 29-34
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.966
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
In this section we prove some elementary properties of the equivalence relation $\stackrel{t}{\sim}$ and give examples.

We say a $\stackrel{t}{\sim}$-equivalence class is *trivial* if it contains only one Young diagram. Soon we will see that the $\stackrel{t}{\sim}$-equivalence classes are all trivial unless $t$ is a nonnegative integer (see Corollary [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}(1)). First, we prove the following easy proposition.

::: proposition
[]{#gs label="gs"} Suppose $\lambda$ is a Young diagram and write $\lambda_\mu(t)=(\mu_0, \mu_1,\ldots)$. Suppose further that $\tau:\mathbb{Z}_{\geq 0}\to\mathbb{Z}_{\geq 0}$ is a bijection and set $\mu'=(\mu'_0, \mu'_1,\ldots)$ where $\mu'_{i}=\mu_{\tau^{-1}(i)}$. There exists a Young diagram $\lambda'$ such that $\mu'=\mu_{\lambda'}(t)$ if and only if $\mu_i'\in\mathbb{Z}$ with $\mu'_i>\mu'_{i+1}$ for all $i>0$.
:::

::: proof
*Proof.* Suppose $\lambda'$ satisfies $\mu'=\mu_{\lambda'}(t)$. Then $\mu'_i=\lambda_i'-i>\lambda_{i+1}'-i-1=\mu'_{i+1}$ for all $i>0$.

On the other hand, suppose $\mu'_i>\mu'_{i+1}$ for all $i>0$. Set $\lambda_i'=\mu_i+i$ for all $i\geq0$ and $\lambda'=(\lambda_1', \lambda_2',\ldots)$. Since $\mu_i>\mu_{i+1}$ and $\mu'_i>\mu'_{i+1}$ for all $i>0$, $\tau(i)$ must equal $i$ for all $i>\text{max}\{\tau(0), \tau^{-1}(0)\}$. Thus $\lambda'_i=\lambda_i$ for all $i>\text{max}\{\tau(0), \tau^{-1}(0)\}$. This shows $\lambda_i'=0$ for all but finitely many values of $i$. Moreover, $\mu_i>\mu_{i+1}$ for $i>0$ implies $\lambda_i'\geq\lambda_{i+1}'$ for all $i>0$. Thus $\lambda'$ is indeed a Young diagram. Finally, choose $k>\text{max}\{\tau(0), \tau^{-1}(0)\}$ with $\lambda_k=0$. Then $\lambda_k'=0$ as well. Furthermore, $t=\sum_{i=0}^k\lambda_i=\sum_{i=0}^k\mu_i+\frac{k(k+1)}{2}=\sum_{i=0}^k\mu'_i+\frac{k(k+1)}{2}=\sum_{i=0}^k\lambda_i'$, which implies $\lambda_0'=t-|\lambda'|$. ◻
:::

::: corollary
[]{#gensim label="gensim"} (1) The $\stackrel{t}{\sim}$-equivalence classes are all trivial unless $t\in\mathbb{Z}_{\geq0}$.

\(2\) Suppose $d\in\mathbb{Z}_{\geq0}$ and $\lambda$ is a Young diagram. The $\stackrel{d}{\sim}$-equivalence class containing $\lambda$ is nontrivial if and only if the coordinates of $\mu_\lambda(d)$ are pairwise distinct.
:::

::: proof
*Proof.* Suppose $\lambda$ is a Young diagram. It follows from Proposition [\[gs\]](#gs){reference-type="ref" reference="gs"} that the $\stackrel{t}{\sim}$-equivalence class containing $\lambda$ is nontrivial if and only if the coordinates of $\mu_\lambda(t)$ are all integers which are pairwise distinct. This proves part (2). Also, this implies the $\stackrel{t}{\sim}$-equivalence classes are all trivial unless $t\in\mathbb{Z}$. Finally, if $t$ is a negative integer, then $\lambda_{|\lambda|-t}=0$ which implies $\mu_{|\lambda|-t}=\mu_0$. This proves part (1). ◻
:::

::: example
\(1\) Let $\lambda=(2, 1, 0,\ldots)$. Then $\mu_\lambda(t)=(t-3, 1, -1, -3, -4,\ldots)$. Thus, by Corollary [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}, $\lambda$ is in a nontrivial $\stackrel{t}{\sim}$-equivalence class if and only if $t\in\mathbb{Z}_{\geq 0}$ and $t\not=0, 2, 4$.

\(2\) If we let $\varnothing$ denote the Young diagram $(0,\ldots)$, then $\mu_\varnothing(t)=(t, -1, -2, -3,\ldots)$. Thus, by Corollary [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}, $\lambda$ is in a nontrivial $\stackrel{t}{\sim}$-equivalence class if and only if $t\in\mathbb{Z}_{\geq 0}$. $\rotatebox{45}{$\Box$}$
:::

The following proposition will allow us to give a complete description of nontrivial $\stackrel{t}{\sim}$-equivalence classes.

::: proposition
[]{#mindiagprop label="mindiagprop"} Suppose $d$ is a nonnegative integer and $\lambda$ is a Young diagram in a nontrivial $\stackrel{d}{\sim}$-equivalence class. Label the coordinates of $\mu_\lambda(d)$ by $\mu_0, \mu_1,\ldots$ so that $\mu_{i}<\mu_{i-1}$ for all $i>0$ (such a labeling is possible by Corollary [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}(2)). For each integer $i\geq0$, set $\lambda^{(i)}=(\lambda^{(i)}_1, \lambda^{(i)}_2,\ldots)$ where $$\label{lambdai}\lambda_j^{(i)}:=\left\{\begin{array}{ll}
\mu_{j-1}+j &\text{if $j\leq i$},\\
\mu_j+j & \text{if $j>i$}.
\end{array}\right.$$ for each $j>0$. Then $\lambda^{(0)}\subset\lambda^{(1)}\subset\lambda^{(2)}\subset\cdots$ is a complete list of the Young diagrams $\stackrel{d}{\sim}$-equivalent to $\lambda$.
:::

::: proof
*Proof.* Given $i\geq0$, $\lambda^{(i)}$ is a Young diagram with $\mu_{\lambda^{(i)}}(d)=(\mu_0^{(i)}, \mu_1^{(i)},\ldots)$ where $$\mu_j^{(i)}=\left\{\begin{array}{ll}
\mu_{i} &\text{if $j=0$},\\
\mu_{j-1} & \text{if $0<j\leq i$},\\
\mu_j &  \text{if $j> i$}.
\end{array}\right.$$ Hence $\lambda^{(i)}\stackrel{d}{\sim}\lambda$ for all $i\geq0$. Moreover, it follows from Proposition [\[gs\]](#gs){reference-type="ref" reference="gs"} that $\lambda^{(0)}, \lambda^{(1)}, \lambda^{(2)},\ldots$ is a complete list of Young diagrams which are $\stackrel{d}{\sim}$-equivalent to $\lambda$. Furthermore, $\lambda^{(i-1)}_j=\lambda^{(i)}_j$ for all $j\not=i$ and $\lambda^{(i-1)}_{i}=\mu_i+i<\mu_{i-1}+i=\lambda^{(i)}_i$ for each $i>0$. Hence $\lambda^{(i-1)}\subset\lambda^{(i)}$ for all $i>0$. ◻
:::

::: corollary
[]{#mindiag label="mindiag"} A Young diagram $\lambda$ is the minimal element in a nontrivial $\stackrel{d}{\sim}$-equivalence class if and only if $\lambda(d)$ is a Young diagram. In particular, the nontrivial $\stackrel{d}{\sim}$-equivalence classes are parametrized by Young diagrams of size $d$. Moreover, if $\{\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\}$ is a nontrivial $\stackrel{d}{\sim}$-equivalence class, then for each $i\geq 0$ the Young diagram $\lambda^{(i)}$ is obtained from the Young diagram $\lambda^{(0)}(d)$ by removing row $i$ and adding one box to row $j$ for each $j=0,\ldots, i-1$.
:::

::: proof
*Proof.* Suppose $\lambda$ is a Young diagram with the property that $\lambda(d)$ is also a Young diagram. Then $d-|\lambda|>\lambda_1-1>\lambda_2-2>\cdots$. Thus, by Corollary [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}(2), $\lambda$ is in a nontrivial $\stackrel{d}{\sim}$-equivalence class. Moreover, $\lambda=\lambda^{(0)}$ (using the notation in Proposition [\[mindiagprop\]](#mindiagprop){reference-type="ref" reference="mindiagprop"}) is the minimal element in its $\stackrel{d}{\sim}$-equivalence class. Conversely, suppose $\{\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\}$ is a nontrivial $\stackrel{d}{\sim}$-equivalence class and let $\mu_0,\mu_1,\ldots$ be as in Proposition [\[mindiagprop\]](#mindiagprop){reference-type="ref" reference="mindiagprop"}. From ([\[lambdai\]](#lambdai){reference-type="ref" reference="lambdai"}) we have $d-|\lambda^{(0)}|=\mu_0\geq\mu_1+1=\lambda_1^{(0)}$. Hence $\lambda^{(0)}(d)$ is a Young diagram. Finally, using ([\[lambdai\]](#lambdai){reference-type="ref" reference="lambdai"}) we see $\lambda^{(i)}_1=\mu_0+1=d-|\lambda^{(0)}|+1$, $\lambda^{(i)}_j=\mu_{j-1}+j=\lambda^{(0)}_{j-1}+1$ for $0<j\leq i$, and $\lambda^{(i)}_{j}=\lambda^{(0)}_j$ for $j>i$. The result follows. ◻
:::

::: example
[]{#3class label="3class"} (1) The only nontrivial $\stackrel{0}{\sim}$-equivalence class is $\{\varnothing, (1), (1^2), (1^3),\ldots\}$.

\(2\) Below are the three nontrivial $\stackrel{3}{\sim}$-equivalence classes of Young diagrams. $$\includegraphics{diss47.pdf}$$  $\rotatebox{45}{$\Box$}$
:::

Next we show how the polynomials $P_\lambda$ defined in section [\[dim\]](#dim){reference-type="ref" reference="dim"} can be used to determine when a Young diagram is in a trivial $\stackrel{d}{\sim}$-equivalence class.

::: proposition
[]{#zero label="zero"} Suppose $\lambda$ is a Young diagram and $d$ is a nonnegative integer. $\lambda$ is in a trivial $\stackrel{d}{\sim}$-equivalence class if and only if $P_\lambda(d)=0$.
:::

::: proof
*Proof.* By Corollary [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}, $\lambda$ is in a trivial $\stackrel{d}{\sim}$-equivalence class if and only if the coordinates of $\mu_\lambda(d)$ are not distinct, which occurs if and only if $d-|\lambda|=\lambda_i-i$ for some $i>0$. However, $d-|\lambda|>\lambda_i-i$ when $i>|\lambda|$, so $\lambda$ is in a trivial $\stackrel{d}{\sim}$-equivalence class if and only if $d=|\lambda|+\lambda_i-i$ for some $0<i\leq|\lambda|$. The result now follows from Proposition [\[roots\]](#roots){reference-type="ref" reference="roots"}. ◻
:::

We conclude this section by defining a total order on the nontrivial $\stackrel{d}{\sim}$-equivalence classes. This ordering will be useful in section [\[secblocks\]](#secblocks){reference-type="ref" reference="secblocks"}.

::: definition
If $B$ and $B'$ are nontrivial $\stackrel{d}{\sim}$-equivalence classes with minimal diagrams $\lambda$ and $\lambda'$ respectively, we write $B\prec B'$ if $\lambda(d)\prec\lambda'(d)$ (see section [\[notation\]](#notation){reference-type="ref" reference="notation"}).
:::

::: example
\(1\) The nontrivial $\stackrel{3}{\sim}$-equivalence classes in Example [\[3class\]](#3class){reference-type="ref" reference="3class"}(2) are listed in decreasing order.

\(2\) Below are the seven nontrivial $\stackrel{5}{\sim}$-equivalence classes with $B_0\prec\cdots\prec B_6$. $$\includegraphics{diss48.pdf}$$  $\rotatebox{45}{$\Box$}$
:::

## The functor $-\otimes L(\Box)$ {#part1}

In this section we explain how to decompose the tensor product $L(\lambda)\otimes L(\Box)$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ where $\lambda$ is an arbitrary Young diagram. The following lemma will be our main tool in our study of decomposing tensor products.

::: lemma
[]{#tdlemma label="tdlemma"} Suppose $\lambda, \mu, \lambda^{(1)},\ldots, \lambda^{(m)}$ are Young diagrams with the property $L(\lambda)\otimes L(\mu)=L(\lambda^{(1)})\oplus\cdots\oplus L(\lambda^{(m)})$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$. Then there exists an integer $N$ such that $L_{\lambda(d)}\otimes L_{\mu(d)}=L_{\lambda^{(1)}(d)}\oplus\cdots\oplus L_{\lambda^{(m)}(d)}$ in $\operatorname{Rep}(S_d; F)$ whenever $d$ is an integer with $d\geq N$.
:::

::: proof
*Proof.* By Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(4) we can find an integer $N$ such that whenever $d$ is an integer with $d\geq N$ the following two properties are satisfied:

1.  $\operatorname{Lift}_d$ acts as the identity on all of the objects $L(\lambda), L(\mu), L(\lambda^{(1)}),\ldots, L(\lambda^{(m)})$.

2.  $\lambda(d), \mu(d), \lambda^{(1)}(d),\ldots, \lambda^{(m)}(d)$ are all Young diagrams.

If $d\geq N$, by ($\star$) and Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(1), we have $$\operatorname{Lift}_d(L(\lambda)\otimes L(\mu))=L(\lambda^{(1)})\oplus\cdots\oplus L(\lambda^{(m)})$$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$. Hence, by ($\star$) and Proposition [\[Liftprop\]](#Liftprop){reference-type="ref" reference="Liftprop"}(3), $$L(\lambda)\otimes L(\mu)=L(\lambda^{(1)})\oplus\cdots\oplus L(\lambda^{(m)})$$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_d; F)$. If we apply the tensor functor $\mathcal{F}$ to the equality above, the result follows from Proposition [\[Findy\]](#Findy){reference-type="ref" reference="Findy"} along with ($\star\star$). ◻
:::

From Lemma [\[tdlemma\]](#tdlemma){reference-type="ref" reference="tdlemma"}, along with the well-known simple algorithm for decomposing $L_\lambda\otimes L_{(d-1, 1, 0,\ldots)}$ in $\operatorname{Rep}(S_d; F)$ (see e.g. [@MR0095209]), we have the following algorithm for decomposing $L(\lambda)\otimes L(\Box)$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$.

::: proposition
[]{#tenone label="tenone"} $L(\lambda)\otimes L(\Box)=\bigoplus_{\nu}L(\nu)^{\oplus a_\nu}$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ where $a_\nu$ is the number of times the Young diagram $\nu$ is obtained from $\lambda$ as a result of one of the following three procedures:

\(1\) Add an addable[^1] box to $\lambda$.

\(2\) Delete a removable box from $\lambda$.

\(3\) First delete a removable box from $\lambda$, then add an addable box to the resulting Young diagram.
:::

::: example
[]{#expart1 label="expart1"} In this example we will apply Proposition [\[tenone\]](#tenone){reference-type="ref" reference="tenone"} to $L(\lambda)\otimes L(\Box)$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ where $\lambda=(3, 1)$. The following figure illustrates all of the adding and removing of boxes necessary to apply Proposition [\[tenone\]](#tenone){reference-type="ref" reference="tenone"}. $$\includegraphics{diss45.pdf}$$ Therefore, in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$, $L(\lambda)\otimes L(\Box)$ decomposes as a direct sum of two copies of $L(\lambda)$ and one copy of the indecomposable object corresponding to each of the Young diagrams $(3, 1^2), (3, 2), (4, 1), (3), (2, 1), (4), (2^2), (2, 1^2)$. $\rotatebox{45}{$\Box$}$
:::

::: corollary
[]{#tenonecor label="tenonecor"} Suppose $L(\lambda)\otimes L(\Box)=\bigoplus_{\nu}L(\nu)^{\oplus a_\nu}$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ and let $d$ be a nonnegative integer.. Then $a_\nu=1$ whenever $\nu\not=\lambda$ is such that the coordinates of $\mu_\lambda(d)-\mu_\nu(d)$ are all zero except for exactly one $1$ and one $-1$, and $a_\nu=0$ for all other $\nu\not=\lambda$.
:::

::: proof
*Proof.* Assume $\nu\not=\lambda$ is a Young diagram and write $\mu_\lambda(d)=(\mu_0, \mu_1,\ldots)$ and $\mu_\nu(d)=(\mu_0', \mu_1',\ldots)$. $\nu$ is obtained from $\lambda$ by adding one addable box (resp. deleting a removable box) if and only if $\mu_0-\mu_0'=|\nu|-|\lambda|$ equals $1$ (resp. $-1$), and there exists an $i>0$ such that $\mu_i-\mu'_i=\lambda_i-\nu_i$ is equal to $-1$ (resp. $1$) and $\mu_j-\mu'_j=\lambda_j-\nu_j=0$ for all $0<j\not=i$. Similarly, $\nu$ is obtained from $\lambda$ by first deleting a removable box and then adding an addable box if and only if $\mu_0=\mu_0'$ and the numbers $\mu_1-\mu_1',\mu_2-\mu_2',\ldots$ are all zero except for exactly one $1$ and one $-1$. The result now follows from Proposition [\[tenone\]](#tenone){reference-type="ref" reference="tenone"}. ◻
:::

We conclude this section with a technical lemma concerning tensoring with $L(\Box)$ which will be useful in subsequent sections.

::: lemma
[]{#oneboxlemma label="oneboxlemma"} Fix a nonnegative integer $d$ and suppose $B=\{\lambda^{(0)}\subset \lambda^{(1)}\subset\cdots\}$ is a nontrivial $\stackrel{d}{\sim}$-equivalence class.

\(1\) If $B$ is minimal with respect to $\prec$, then for each integer $i>0$ there exists a Young diagram $\rho$, in a trivial $\stackrel{d}{\sim}$-equivalence class, with $L(\rho)\otimes L(\Box)=\bigoplus_{\nu}L(\nu)^{\oplus a_\nu}$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ where $$a_{\lambda^{(j)}}=\left\{\begin{array}{ll}
1 & \text{if }j\in\{i, i-1\},\\
0 & \text{if }j\not\in\{i, i-1\}.\\
\end{array}\right.$$

\(2\) If $B$ is not minimal with respect to $\prec$, then there exists a nontrivial $\stackrel{d}{\sim}$-equivalence class $B'=\{\rho^{(0)}\subset \rho^{(1)}\subset\cdots\}$ such that $B'\precneqq B$,  and for each integer $i\geq0$, $L(\rho^{(i)})\otimes L(\Box)=\bigoplus_{\nu}L(\nu)^{\oplus a_\nu}$ and $L(\lambda^{(i)})\otimes L(\Box)=\bigoplus_{\nu}L(\nu)^{\oplus b_\nu}$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_T; K)$ where $$a_{\lambda^{(j)}}=b_{\rho^{(j)}}=\left\{\begin{array}{ll}
1 & \text{if }j=i,\\
0 & \text{if }j\not=i.\\
\end{array}\right.$$
:::

::: proof
*Proof.* (1) Assume $B$ is the minimal $\stackrel{d}{\sim}$-equivalence class. Then $$\label{miniblock}\lambda^{(i)}=\left\{\begin{array}{ll}
(2^i, 1^{d-i-1}) & \text{if }0\leq i<d,\\
(2^d, 1^{i-d}) & \text{if }i\geq d.\\
\end{array}\right.$$ Now fix $i>0$ and set $$\rho:=\left\{\begin{array}{ll}
(1^d) & \text{if }i=1,\\
(3, 2^{i-2}, 1^{d-i})&  \text{if } 1<i<d,\\
(2^{d-1}, 1) & \text{if }i=d,\\
(3, 2^{d-1}, 1^{i-d-1})  & \text{if } i> d.
\end{array}\right.$$ If we set $\mu_\rho(d)=(\mu_0, \mu_1,\ldots)$, then it is easy to check that $$\mu_0=\left\{\begin{array}{ll}
\mu_i & \text{if }1\leq i\leq d,\\
\mu_{i+1} & \text{if }i> d.\\
\end{array}\right.$$ Hence $\rho$ is in a trivial $\stackrel{d}{\sim}$-equivalence class (see Corollary [\[gensim\]](#gensim){reference-type="ref" reference="gensim"}). Finally, comparing $\rho$ to the Young diagrams in ([\[miniblock\]](#miniblock){reference-type="ref" reference="miniblock"}) and using Proposition [\[tenone\]](#tenone){reference-type="ref" reference="tenone"}, it is easy to check that $\rho$ satisfies part (1).

\(2\) Suppose $B$ is not minimal so that $\lambda^{(0)}(d)=(\lambda_0, \lambda_1,\ldots)$ is a Young diagram of size $d$ distinct from $(1^d)$. Then $\lambda^{(0)}(d)$ has a row with more than one box. Let $m$ be the maximal integer with $\lambda_m>1$, and let $k$ be the minimal positive integer with $\lambda_k=0$. Let $\rho^{(0)}$ be the Young diagram with $\rho^{(0)}(d)$ obtained from $\lambda^{(0)}(d)$ by deleting one box from row $m$ and adding one box to row $k$ $$\includegraphics{diss54.pdf}$$ Since $\rho^{(0)}(d)$ is a Young diagram of size $d$ with $\rho^{(0)}(d)\prec\lambda^{(0)}(d)$, $\rho^{(0)}$ is the minimal element in a nontrivial $\stackrel{d}{\sim}$-equivalence class $B'=\{\rho^{(0)}\subset\rho^{(1)}\subset\cdots\}$ which satisfies $B'\precneqq B$ (see Corollary [\[mindiag\]](#mindiag){reference-type="ref" reference="mindiag"}). By Corollary [\[tenonecor\]](#tenonecor){reference-type="ref" reference="tenonecor"} it suffices to show that the coordinates of $\mu_{\lambda^{(i)}}(d)-\mu_{\rho^{(j)}}(d)$ are all zero except for one $1$ and one $-1$ if and only if $i=j$.

Write $\mu_{\lambda^{(0)}}(d)=(\mu_0, \mu_1,\ldots)$ and $\mu_{\rho^{(0)}}(d)=(\mu'_0, \mu'_1,\ldots)$. For an integer $i\geq0$, let $\tau_i:\mathbb{Z}_{\geq 0}\to\mathbb{Z}_{\geq 0}$ be the bijection mapping $0\mapsto i$, $j\mapsto j-1$ ($0<j\leq i$), and $j\mapsto j$ ($j>i$). Then, by Proposition [\[mindiagprop\]](#mindiagprop){reference-type="ref" reference="mindiagprop"}, $\mu_{\lambda^{(i)}}(d)=(\mu_{\tau_i(0)}, \mu_{\tau_i(1)},\ldots)$ and $\mu_{\rho^{(j)}}(d)=(\mu'_{\tau_j(0)}, \mu'_{\tau_j(1)},\ldots)$ for all $i, j\geq 0$. Now suppose $i, j\geq 0$ are such that the coordinates of $\mu_{\lambda^{(i)}}(d)-\mu_{\rho^{(j)}}(d)$ are all zero except for one $1$ and one $-1$. Equivalently, setting $\tau=\tau_i^{-1}\tau_j$, there exist nonnegative integers $m', k'$ such that $$\label{mutau}\mu_l-\mu_{\tau(l)}'=\left\{\begin{array}{ll}
1 & \text{if $l=m'$,}\\
-1& \text{if $l=k'$,}\\
0 & \text{otherwise.}
\end{array}\right.$$ By the construction of $\rho^{(0)}(d)$ we have $$\mu_l-\mu_l'=\left\{\begin{array}{ll}
1 & \text{if $l=m$,}\\
-1& \text{if $l=k$,}\\
0 & \text{otherwise.}
\end{array}\right.$$ Since $\mu_0>\mu_1>\cdots$ (resp. $\mu'_0>\mu'_1>\cdots$), neither $\mu_m$ nor $\mu_k$ (resp. $\mu'_m$ nor $\mu'_k$) is equal to $\mu_l=\mu_l'$ whenever $l\not=m, k$. Moreover, since $k>m$ we have $\mu_m-\mu_k'=\mu_m'-\mu_k'+1>1$ and $\mu_k-\mu_m'=\mu_k'-\mu_m'-1<-1$. Hence ([\[mutau\]](#mutau){reference-type="ref" reference="mutau"}) holds if and only if $m=m'$, $k=k'$, and $\tau$ is the identity map. However, $\tau=\tau_i^{-1}\tau_j$ is the identity map if and only if $i=j$. This completes the proof. ◻
:::

[^1]: Given a Young diagram $\lambda$, an addable (resp. removable) box of $\lambda$ is a box which can be added to (resp. removed from) $\lambda$ resulting in a new Young diagram.
