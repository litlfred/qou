---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-002-split-terwilliger-algebra-of-the-hamming-scheme
section_title: "Split Terwilliger algebra of the Hamming scheme"
section_number: null
pages: 4-9
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
[]{#sec:split label="sec:split"} In this section, we consider split distance distribution on a partition of $\{1, \dots, n\}$ with two subsets $T_{1}$ and $T_{2}$ such that $T_{1}\cap T_{2}=\emptyset$, $\lvert T_{1}\rvert = n_{1}$, $\lvert T_{2}\rvert = n_{2}$, and $n_1+n_2=n$.

Let $G_{u}$ be the group of all distance-preserving automorphisms of the power set of $T_{u}$, for $u = 1, 2$. We consider the group $G_{1} \times G_{2}$ acting on ${\cal P}$ by $$(g, h) \cdot X = g(X \cap T_{1}) \cup h(X \cap T_{2})$$ for $(g, h) \in G_{1} \times G_{2}$ and $X \in {\cal P}$. Observe that an orbit of $G_{1} \times G_{2}$ on ${\cal P} \times {\cal P}$ can be similarly represented by $(i, j, t, i', j', t')$ with $i, j, t \in \{0, \dots, n_{1}\}$, $i', j', t' \in \{0, \dots, n_{2}\}$, $i+j-2t \in \{0, \dots, n_{1}\}$ and $i'+j'-2t' \in \{0, \dots, n_{2}\}$ and we define $\lvert {\cal P} \rvert \times \lvert {\cal P}\rvert$ matrices $M_{i, j, i', j'}^{t, t'}$ by $$\left(M_{i, j, i', j'}^{t, t'}\right)_{X,Y}  = \left\{
    \begin{aligned}
        &1, \quad 
        \begin{aligned}
            &\text{if } \lvert X \cap T_{1}\rvert = i, \lvert X \cap T_{2} \rvert = i',\\
            &\lvert Y \cap T_{1}\rvert = j, \lvert Y \cap T_{2}\rvert = j', \\
            &\text{and } \lvert X \cap Y \cap T_{1}\rvert = t, \lvert X \cap Y \cap T_{2}\rvert = t';
        \end{aligned}\\
    &0, \quad \text{otherwise.}
    \end{aligned} \right.$$ Let ${\cal A}_{n_{1}, n_{2}}$ be the collection of all linear combinations of $\{M_{i, j, i', j'}^{t, t'}\}$ over the complex field $\mathbb{C}$. One can verify that ${\cal A}_{n_{1}, n_{2}}$ is closed under matrix multiplication and adjoint, and ${\cal A}_{n_{1}, n_{2}}$ forms a $\mathbb{C}^{*}$-algebra, which we call a *2-split Terwilliger algebra* of the Hamming scheme. By definition, we have the following lemma.

::: lemma
[]{#lem:le_1 label="lem:le_1"} The algebra ${\cal A}_{n_{1}, n_{2}}$ is isomorphic to the algebra ${\cal A}_{n_{1}} \otimes {\cal A}_{n_{2}}$, where $\otimes$ is the matrix tensor product.
:::

::: proof
*Proof.* We denote $M_{i, j}^{n_{1}, t}$'s and $M_{i', j'}^{n_{2}, t'}$'s as the generators of ${\cal A}_{n_{1}}$, ${\cal A}_{n_{2}}$, respectively, for $i, j, t \in \{0, \dots, n_{1}\}$, $i', j', t' \in \{0, \dots, n_{2}\}$. For $X, Y \in {\cal P}$, $$(M_{i, j, i', j'}^{t, t'})_{X, Y} = 1  \label{eq:Mijt_split}$$ if and only if $\lvert X \cap T_{1}\rvert = i$, $\lvert Y \cap T_{1}\rvert = j$, $\lvert X \cap Y \cap T_{1}\rvert = t$ and $\lvert X \cap T_{2}\rvert = i'$, $\lvert Y \cap T_{2}\rvert = j'$, $\lvert X \cap Y \cap T_{2}\rvert = t'$.\
Suppose that the generators of ${\cal A}_{n_{1}}$ and ${\cal A}_{n_{2}}$ are indexed by the power sets ${\cal P}_{1}$, ${\cal P}_{2}$ of $T_{1}$ and $T_{2}$, respectively. We observe that ([\[eq:Mijt_split\]](#eq:Mijt_split){reference-type="ref" reference="eq:Mijt_split"}) is equivalent to $$(M_{i, j}^{n_{1}, t})_{X\cap T_{1}, Y\cap T_{1}} = 1 \text{ and } (M_{i', j'}^{n_{2}, t'})_{X\cap T_{2}, Y\cap T_{2}} = 1.$$ Also, the size of the matrix $M_{i, j}^{n_{1}, t} \otimes M_{i', j'}^{n_{2}, t'}$ is equal to $2^{n_{1}+n_{2}} \times 2^{n_{1}+n_{2}}$. Immediately, we have $$M_{i, j, i', j'}^{t, t'} = M_{i, j}^{n_{1}, t} \otimes M_{i', j'}^{n_{2}, t'}, \label{eq:Mijt_prod}$$ since the right (left) hand side of ([\[eq:Mijt_prod\]](#eq:Mijt_prod){reference-type="ref" reference="eq:Mijt_prod"}) forms a set of generators for ${\cal A}_{n_{1}, n_{2}}$ (${\cal A}_{n_{1}} \otimes {\cal A}_{n_{2}}$). ◻
:::

As a consequence, we have a block-diagonal formula for the $2$-split Terwilliger algebra of the Hamming scheme, which is an extension of the block-diagonal formula for the Terwilliger algebra of the Hamming scheme with the definition of tensor product. As in Schrijver's decomposition of the Terwilliger algebra, this split decomposition is irreducible. By certain basic results from representation theory, ${\cal A}_{n_{1}, n_{2}}$ will be mapped to a direct sum of simple ${\cal A}_{n_{1}, n_{2}}$-modules. Thus we have the following corollary.

::: corollary
[@Sch05 equation $(56)$] []{#cor:blo label="cor:blo"} There is an isomorphism from ${\cal A}_{n_{1}, n_{2}}$ to $$\bigoplus_{k = 0}^{\left\lfloor \frac{n_{1}}{2} \right\rfloor} \bigoplus_{k' = 0}^{\left\lfloor \frac{n_{2}}{2} \right\rfloor} \mathbb{C}^{N_{k, k'} \times N_{k. k'}},$$ with $N_{k, k'} = (n_{1}-2k+1)(n_{2}-2k'+1)$ that maps $A = \sum_{i, j, i', j', t, t'}x_{i, j, i', j'}^{t, t'} M_{i, j, i', j'}^{t, t'}$ to $$\bigoplus_{k = 0}^{\lfloor \frac{n_{1}}{2} \rfloor} \bigoplus_{k' = 0}^{\lfloor \frac{n_{2}}{2} \rfloor} {\cal B}_{k, k'},$$ where $$\begin{aligned}
            {\cal B}_{k, k'} = \left( \sum_{t, t'}  \alpha_{i, j, i', j'}^{k, n_{1}, n_{2}} \beta_{i, j, k}^{n_{1}, t} \beta_{i', j', k'}^{n_{2}, t'}  x_{i, j, i', j'}^{t, t'} \right)_{((i, i'), (j, j')) = ((k, k'), (k, k'))}^{((n_{1}-k, n_{2}-k'), (n_{1}-k, n_{2}-k'))}
        \end{aligned}$$ with $$\begin{aligned}
        \beta_{i, j, k}^{n_{l}, t} = & \sum_{u = 0}^{n_{l}} (-1)^{u-t} \binom{u}{t} \binom{n_{l}-2k}{u-k} \binom{n_{l}-k-u}{i-u} \binom{n_{l}-k-u}{j-u},
    
\end{aligned}$$ for $l = 1, 2$ and $$\alpha_{i, j, i', j'}^{k, n_{1}, n_{2}} = \binom{n_{1}-2k}{i-k}^{-\frac{1}{2}} \binom{n_{1}-2k}{j-k}^{-\frac{1}{2}} \binom{n_{2}-2k'}{i'-k'}^{-\frac{1}{2}} \binom{n_{2}-2k'}{j'-k'}^{-\frac{1}{2}}.$$
:::

::: remark
The formula in Corollary [\[cor:blo\]](#cor:blo){reference-type="ref" reference="cor:blo"} was provided by Schrijver in [@Sch05] to provide SDP constraints for a constant-weight code of weight $w$ by choosing $n_{1}=w$ and $n_{2}=n-w$.
:::

Now we can derive additional semidefinite constraints on a nontrivial code $C\subset {\mathcal P}$ from the 2-split Terwilliger algebra of the Hamming scheme. Define $$x_{i, j, i', j'}^{t, t'} = \frac{1}{\lvert C\rvert \binom{n_{1}}{i-t, j-t, t} \binom{n_{2}}{i'-t', j'-t', t'}} \lambda^{t, t'}_{i, j, i', j'},$$ where $$\begin{aligned}
        \lambda^{t, t'}_{i, j, i', j'} = \{&(X, Y, Z) \in C^{3} : \lvert (X \Delta Y)\cap T_{1}\rvert = i, \lvert (X \Delta Z)\cap T_{1}\rvert = j, \\
        &\lvert((X \Delta Y)\cap (X \Delta Z))\cap T_{1}\rvert = t,\\
        &\lvert(X \Delta Y)\cap T_{2}\rvert = i', \lvert(X \Delta Z)\cap T_{2}\rvert = j',\\
        &\lvert((X \Delta Y)\cap (X \Delta Z))\cap T_{2}\rvert = t' \}\rvert,
    \end{aligned}$$ for $i, j, t \in \{0, \dots, n_{1}\}$, $i', j', t' \in \{0, \dots, n_{2}\}$ with $i-t \geq 0$, $j-t \geq 0$, $i+j-2t \leq n_{1}$, $i'-t' \geq 0$, $j'-t' \geq 0$ and $i'+j'-2t' \leq n_{2}$. Also, the size of the code is $$\lvert C \rvert=\sum_{a = 0}^{n} \sum_{i+i' = a} \binom{n_{1}}{i}\binom{n_{2}}{i'} x_{i, 0, i', 0}^{0, 0}.$$

Let $\lambda_{a, b}^{c}$, $x_{a, b}^{c}$ and $M_{a, b}^{c}$ be defined as in Schrijver's SDP in the previous section. From the definitions, we have the following identities: $$\begin{aligned}
    \lambda_{a, b}^{c} =& \sum_{i+i' = a, j+j' = b, t+t' = c} \lambda_{i, j, i', j'}^{t, t'},   \label{eqn:id_1}\\
    x_{a, b}^{c} =& \sum_{i+i' = a, j+j' = b, t+t' =c} \frac{\binom{n_{1}}{i-t, j-t, t} \binom{n_{2}}{i'-t', j'-t', t'}}{\binom{n}{a-c, b-c, c}}x_{i, j, i', j'}^{t, t'},  \label{eqn:id_2}\\
    M_{a, b}^{c} =& \sum_{i+i' = a, j+j' = b, t+t' = c} M_{i, j, i', j'}^{t, t'}.  \label{eqn:id_3}
\end{aligned}$$

Consider the following two sets of automorphisms: $$\begin{aligned}
    & \Pi_{\rm s} = \{(\pi_{1}, \pi_{2}) \in G_{1} \times G_{2} \mid \emptyset \in (\pi_{1}, \pi_{2})(C)\},\\
    & \Pi_{\rm s}' = \{(\pi_{1}, \pi_{2}) \in G_{1} \times G_{2} \mid \emptyset \notin (\pi_{1}, \pi_{2})(C)\}.
\end{aligned}$$ Here the subscript $\rm s$ stands for split. Similarly, we define $$\begin{aligned}
    & R_{\rm s} = \frac{1}{\lvert \Pi_{\rm s} \rvert} \sum_{(\pi_{1}, \pi_{2}) \in \Pi_{\rm s}} \chi^{(\pi_{1}, \pi_{2})(C)} (\chi^{(\pi_{1}, \pi_{2})(C)})^{T}, \\
    & R_{\rm s}' = \frac{1}{\lvert \Pi_{\rm s}'\rvert}\sum_{(\pi_{1}, \pi_{2}) \in \Pi_{\rm s}'} \chi^{(\pi_{1}, \pi_{2})(C)} (\chi^{(\pi_{1}, \pi_{2})(C)})^{T}.
\end{aligned}$$ One can immediately see that $R_{\rm s}$ and $R_{\rm s}'$ are positive semidefinite and they only depend on the action $G_{1} \times G_{2}$ on $C$. Moreover, $R_{\rm s}$ and $R_{\rm s}'$ are elements of ${\cal A}_{n_{1}, n_{2}}$ as a consequence of the following proposition.

::: proposition
[]{#pro:R_R' label="pro:R_R'"} $$\begin{aligned}
            &R_{\rm s} = \sum_{i, j, i', j', t ,t'} x_{i, j, i', j'}^{t, t'}M_{i, j, i', j'}^{t, t'},\\
            & 
            \begin{aligned}
                R_{\rm s}' =& \frac{\lvert C \rvert}{2^{n}-\lvert C\rvert}\sum_{i, j, i', j', t ,t'} \left( x_{i+j-2t, 0, i'+j'-2t', 0}^{0, 0}-x_{i, j, i', j'}^{t, t'}\right) \\
                &\cdot M_{i, j, i', j'}^{t, t'}.
            \end{aligned}
        \end{aligned}$$
:::

::: proof
*Proof.* Let $X \in {\cal P}$. We define $\Pi_{s}^{X} = \{(\pi_{1}, \pi_{2}) \in \Pi_{1} \times \Pi_{2} \mid (\pi_{1}, \pi_{2})(X) = \emptyset\}$. For an element $(\pi_{1}, \pi_{2}) \in \Pi_{s}^{X}$, we can see $\pi_{1}$ as a permutation of $T_{1}$ and $\pi_{2}$ as a permutation of $T_{2}$. Hence, we have $\lvert \Pi_{s}^{X}\rvert = n_{1} ! n_{2} !$. Define $$\begin{aligned}
        & R_{s}^{X} = \frac{1}{\lvert \Pi_{s}^{X} \rvert} \sum_{(\pi_{1}, \pi_{2}) \in \Pi_{s}^{X}} \chi^{(\pi_{1}, \pi_{2})(C)} (\chi^{(\pi_{1}, \pi_{2})(C)})^{T}, \\
        &
        \begin{aligned}
            \lambda^{t, t', X}_{i, j, i', j'} = \lvert\{&(Y, Z) \in C^{2} : \lvert(X \Delta Y)\cap T_{1}\rvert = i, \lvert(X \Delta Z)\cap T_{1}\rvert = j,\\ 
            &\lvert((X \Delta Y)\cap (X \Delta Z))\cap T_{1}\rvert = t,\\
            &\lvert(X \Delta Y)\cap T_{2}\rvert = i', \lvert(X \Delta Z)\cap T_{2}\rvert = j',\\
            &\lvert((X \Delta Y)\cap (X \Delta Z))\cap T_{2}\rvert = t' \}\rvert.
        \end{aligned}
    
\end{aligned}$$ For $(\pi_{1}, \pi_{2}) \in \Pi_{s}^{X}$ and fixed $i, j, t, i', j', t'$, observe that the number of $1$'s in $$(\chi^{(\pi_{1}, \pi_{2})(C)} (\chi^{(\pi_{1}, \pi_{2})(C)})^{T})_{Y, Z}$$ such that $(M_{i, j, i', j'}^{t, t'})_{Y, Z} = 1$ is $\lambda^{t, t', X}_{i, j, i', j'}$. There are $\binom{n_{1}}{i-t, j-t, t} \binom{n_{2}}{i'-t', j'-t', t'}$ such $(Y, Z)$. Thus, $$R_{s}^{X} = \sum_{i, j, i', j', t, t'} \frac{1}{\binom{n_{1}}{i-t, j-t, t} \binom{n_{2}}{i'-t', j'-t', t'}} \lambda^{t, t', X}_{i, j, i', j'} M_{i, j, i', j'}^{t, t'}.$$ Next, we see that $$R_{s} = \sum_{X \in C} \frac{R_{s}^{X}}{\lvert C\rvert}, \quad R_{s}' = \sum_{X \notin C} \frac{R_{s}^{X}}{\lvert {\cal P} \setminus C \rvert},$$ and $$\sum_{X \in C} \lambda^{t, t', X}_{i, j, i', j'} = \lambda^{t, t'}_{i, j, i', j'}.$$ Therefore, $$\begin{aligned}
            R_{s} =& \sum_{X \in C} \frac{R_{s}^{X}}{\lvert C \rvert}\\
            =& \frac{1}{\lvert C \rvert} \sum_{i, j, i', j', t, t'} \frac{1}{\binom{n_{1}}{i-t, j-t, t} \binom{n_{2}}{i'-t', j'-t', t'}} \left(\sum_{X \in C} \lambda^{t, t', X}_{i, j, i', j'}\right) M_{i, j, i', j'}^{t, t'}\\
            =& \sum_{i, j, i', j', t, t'} \frac{\lambda^{t, t'}_{i, j, i', j'}}{\lvert C\rvert \binom{n_{1}}{i-t, j-t, t} \binom{n_{2}}{i'-t', j'-t', t'}} M_{i, j, i', j'}^{t, t'}\\
            =& \sum_{i, j, i', j', t, t'} x_{i, j, i', j'}^{t, t'} M_{i, j, i', j'}^{t, t'}.
        \end{aligned}$$ For $(Y, Z) \in C^{2}$ with $\lvert Y \Delta Z \cap T_{1}\rvert = i+j-2t$, $\lvert Y \Delta Z \cap T_{2}\rvert = i'+j'-2t'$. The number of $X \in {\cal P}$ such that $\lvert (X \Delta Y)\cap T_{1}\rvert = i, \lvert(X \Delta Z)\cap T_{1}\rvert = j, \lvert((X \Delta Y)\cap (X \Delta Z))\cap T_{1}\rvert = t, \lvert(X \Delta Y)\cap T_{2}\rvert = i', \lvert(X \Delta Z)\cap T_{2}\rvert = j', \lvert((X \Delta Y)\cap (X \Delta Z))\cap T_{2}\rvert = t'$ is $\binom{i+j-2t}{i-t}\binom{n_{1}-t-j+2t}{t}\binom{i'+j'-2t'}{i'-t'}\binom{n_{2}-i'-j'+2t'}{t'}$.\
Thus we have $$\begin{aligned}
            \sum_{X \in {\cal P}} \lambda_{i, j, i', j'}^{t, t', X} = &\binom{i+j-2t}{i-t}\binom{n_{1}-t-j+2t}{t}\binom{i'+j'-2t'}{i'-t'} \binom{n_{2}-i'-j'+2t'}{t'} \lambda_{i+j-2t, 0, i'+j'-2t', 0}^{0, 0}.
        \end{aligned}$$ Hence, $$\begin{aligned}
            R_{s}' =& \sum_{X \in {\cal P} \setminus C} \frac{R_{s}^{X}}{2^{n}-\lvert C \rvert}\\
            =& \frac{1}{2^{n}-\lvert C \rvert} \sum_{i, j, i', j', t, t'} \frac{1}{\binom{n_{1}}{i-t, j-t, t}\binom{n{2}}{i'-t', j'-t', t'}} \left( \sum_{X \in {\cal P} \setminus C} \lambda_{i, j, i', j'}^{t, t', X} \right) M_{i, j, i', j'}^{t, t'}\\
            =& \frac{\lvert C \rvert}{2^{n}-\lvert C \rvert} \sum_{i, j, i', j', t, t'} \frac{1}{\lvert C \rvert \binom{n_{1}}{i-t, j-t, t}\binom{n{2}}{i'-t', j'-t', t'}}\\
            & \cdot \left( \binom{i+j-2t}{i-t}\binom{n_{1}-t-j+2t}{t} \right. \binom{i'+j'-2t'}{i'-t'}\\
            & \cdot \binom{n_{2}-i'-j'+2t'}{t'} \left. \lambda_{i+j-2t, 0, i'+j'-2t', 0}^{0, 0} - \lambda_{i, j, i', j'}^{t, t'} \right) M_{i, j, i', j'}^{t, t'}\\
            =& \frac{\lvert C \rvert}{2^{n}-\lvert C\rvert} \sum_{i, j, i', j', t, t'} \left( \frac{\binom{i+j-2t}{i-t}\binom{n_{1}-t-j+2t}{t} \binom{i'+j'-2t'}{i'-t'}\binom{n_{2}-i'-j'+2t'}{t'}}{\lvert C \rvert \binom{n_{1}}{i-t, j-t, t}\binom{n_{2}}{i'-t', j'-t', t'}} \right. \\
            &\cdot \lambda_{i+j-2t, 0, i'+j'-2t', 0}^{0, 0}  - \left. x_{i, j, i', j'}^{t, t'} \right) M_{i,j, i', j'}^{t, t'}.
        \end{aligned}$$ Using the identities $$\begin{aligned}
        &\binom{n_{1}}{i-t, j-t, t}^{-1} \binom{i+j-2t}{i-t}\binom{n_{1}-i-j+2t}{t} = \binom{n_{1}}{i+j-2t}^{-1} \text{ and }\\
        &\binom{n_{2}}{i'-t', j'-t', t'}^{-1} \binom{i'+j'-2t'}{i'-t'}\binom{n_{2}-i'-j'+2t'}{t'} = \binom{n_{2}}{i'+j'-2t'}^{-1},
    
\end{aligned}$$ we have $$\begin{aligned}
            R_{s}' =& \frac{\lvert C\rvert}{2^{n}-\lvert C\rvert} \sum_{i, j, i', j', t, t'} \left(\frac{1}{\lvert C\rvert \binom{n_{1}}{i+j-2t}\binom{n_{2}}{i'+j'-2t'}} \right. \left.\lambda_{i+j-2t, 0, i'+j'-2t', 0}^{0, 0} - x_{i, j, i', j'}^{t, t'} \right) M_{i, j, i', j'}^{t, t'}\\
            =& \frac{\lvert C \rvert}{2^{n}-\lvert C\rvert} \sum_{i, j, i', j', t, t'} \left( x_{i+j-2t, 0, i'+j'-2t', 0}^{0, 0}-x_{i, j, i', j'}^{t, t'}\right) M_{i, j, i', j'}^{t, t'}.
        \end{aligned}$$ ◻
:::

Using Theorem [\[cor:blo\]](#cor:blo){reference-type="ref" reference="cor:blo"} and the positive semidefiniteness of $R_{\rm s}$ and $R_{\rm s}'$, we have the following semidefinite constraints. For each $k = 0, \dots, \lfloor \frac{n_{1}}{2} \rfloor$ and $k' = 0, \dots, \lfloor \frac{n_{2}}{2} \rfloor$, the following matrices are positive semidefinite: $$\begin{aligned}
    \left( \sum_{t, t'} \alpha_{i, j, i', j'}^{k, n_{1}, n_{2}} \beta_{i, j, k}^{n_{1}, t} \beta_{i', j', k'}^{n_{2}, t'} x_{i, j, i', j'}^{t, t'}  \right)_{((i, i'), (j, j')) = ((k, k'), (k, k'))}^{((n_{1}-k, n_{2}-k'), (n_{1}-k, n_{2}-k'))}, \label{sem1}
\end{aligned}$$ $$\begin{aligned}
    \left( \sum_{t, t'} \alpha_{i, j, i', j'}^{k, n_{1}, n_{2}}  \beta_{i, j, k}^{n_{1}, t} \beta_{i', j', k'}^{n_{2}, t'} (x_{i+j-2t, 0, i'+j'-2t', 0}^{0, 0} -x_{i, j, i', j'}^{t, t'}) \right)_{((i, i'), (j, j')) = ((k, k'), (k, k'))}^{((n_{1}-k, n_{2}-k'), (n_{1}-k, n_{2}-k'))}. \label{sem2}
\end{aligned}$$

::: proposition
[]{#pro:lin label="pro:lin"} Let $C$ be a code with length $n$ and minimum distance at least $d$. Then $x_{i,j,i',j'}^{t,t'}$ corresponding to $C$ satisfy the following linear constraints: for $i, j, t, a, b, c \in \{0, \dots,$ $n_{1}\}$ and $i', j', t', a', b', c' \in \{0, \dots, n_{2}\}$, $$\begin{aligned}
        \begin{array}{cl}
            \mbox{(i) }& x_{0, 0, 0, 0}^{0, 0} = 1; \\
            \mbox{(ii) }& 0 \leq x_{i, j, i', j'}^{t, t'} \leq x_{i, 0, i', 0}^{0, 0};  \\
            \mbox{(iii) }& x_{i, 0, i', 0}^{0, 0} + x_{0, j, 0, j'}^{0, 0} \leq 1 + x_{i, j, i', j'}^{t, t'}; \\
            \mbox{(iv) }& x_{i, j, i', j'}^{t, t'} = x_{a, b, a', b'}^{c, c'} \mbox{ if } ((i, i'), (j, j'), (i+j-2t, i'+j'-2t'));  \\
            &\mbox{ is a permutation of } ((a, a'), (b, b'), (a+b-2c, a'+b'-2c')),  \\
            \mbox{(v) }&  x_{i, j, i', j'}^{t, t'} = 0 \mbox{ if } \{i+i', j+j', (i+i')+(j+j')-2(t+t')\} \cap \{1, \dots, d-1\} \neq \emptyset. \label{eq:split_cons}
        \end{array}
    
\end{aligned}$$
:::

Constraints (i) and (iv) come from the definition of $x_{i, j, i', j'}^{t, t'}$. Constraints (ii) and (iii) are because of the positive semidefiniteness of $R$ and $R'$. Constraint (iv) is the requirement of the minimum distance.

The split distance distribution of $C$ with respect to the partition $\{T_1,T_2\}$ is $\{A_{i, j}\}$, where $$A_{i, j} = \frac{1}{\lvert C \rvert} \lvert \{(a, b) \in C \times C \mid \lvert a \Delta b \cap T_{1}\rvert = i, \lvert a \Delta b \cap T_{2}\rvert = j\}\rvert.$$ It has been shown that generalized Delsarte's inequalities on $A_{i,j}$ hold [@Sim95].

::: corollary
[@Sim95 Generalized Delsarte's inequalities] []{#coro:gen_del label="coro:gen_del"} $$\sum_{i, j} A_{i, j} K_{p}^{n_{1}}(i) K_{q}^{n_{2}}(j) \geq 0, \label{eq:split_del}$$ for $p = 0, \dots, n_{1}$ and $q = 0, \dots, n_{2}$, where $$K_{k}^{n}(x) = \sum_{y=0}^k (-1)^{y} \binom{x}{y} \binom{n-x}{k-y}$$ is the binary Krawchuk polynomial.
:::

We can show that the generalized Delsarte's inequalities on $\{A_{i,j}\}$ can be derived from the positive semidefiniteness of $R_s$ and $R_s'$ in Proposition [\[pro:R_R\'\]](#pro:R_R'){reference-type="ref" reference="pro:R_R'"}.

::: lemma
If $R_s$ and $R_s'$ are positive semidefinite, then ([\[eq:split_del\]](#eq:split_del){reference-type="ref" reference="eq:split_del"}) holds.
:::

::: proof
*Proof.* Define a matrix $$D_{s} =  R_{s} + \frac{2^{n}-\lvert C \rvert}{\lvert C \rvert}R_{s}'= \sum_{i, j, i', j', t, t'} x_{i+j-2t, 0, i'+j'-2t', 0}^{0, 0} M_{i, j, i', j'}^{t, t'},$$ which is a nonnegative linear combination of positive semidefinite matrices $R_{s}$ and $R_{s}'$, and hence is positive semidefinite. We can rewrite $D_{s}$ as $$D_{s} = \sum_{k, k'} x_{k, 0, k', 0}^{0, 0} M_{k, k'},$$ where $$(M_{k, k'})_{X, Y} = \left\{
        \begin{aligned}
            &1, \text{ if } \lvert X \Delta Y \cap T_{1}\rvert = k, \lvert X \Delta Y \cap T_{2}\rvert = k';\\
            &0, \text{ otherwise.}
        \end{aligned} \right.$$ Define matrices $D_{a}^{m}$ for $0\leq a,m\leq n$ with entries $$(D_{a}^{m})_{X, Y} = \left\{
        \begin{aligned}
            &1, \text{ if } \lvert X \Delta Y\rvert = a;\\
            &0, \text{ otherwise,}
        \end{aligned}
        \right.$$ for indexes $X, Y$ in the power set of $\{1, \dots, m\}$. Notice that $\{D_{a}^{m}\}$ forms a basis for the Bose--Mesner algebra of the Hamming scheme with length $m$. Using the isomorphism in Lemma [\[lem:le_1\]](#lem:le_1){reference-type="ref" reference="lem:le_1"}, one finds that $M_{k, k'}$ is isomorphic to $D_{k}^{n_{1}} \otimes D_{k'}^{n_{2}}$. By [@Del73], we learn that Krawchuk polynomials $K_{a}^{m}(p)$ are eigenvalues of the matrices $\{D_{a}^{m}\}$ for $0 \leq p \leq m$ and, moreover, the matrices $\{M_{k, k'}\}$ are commutative. Consequently, to diagonalize $D_{s}$, we simply have to diagonalize $M_{k, k'}$ and the semidefinite conditions become $$\label{ineq:cor_2}
        \sum_{k, k'} x_{k, 0, k', 0}^{0, 0} K_{k}^{n_{1}}(p) K_{k'}^{n_{2}}(q) \geq 0,$$ for $p \in \{0, \dots, n_{1}\}$ and $q \in \{0, \dots, n_{2}\}$. Recall that the Krawchuk polynomial obeys the following symmetric relation [@MS77]: $$\binom{m}{a}K_{b}^{m}(a) = \binom{m}{b}K_{a}^{m}(b).$$ Thus the inequality ([\[ineq:cor_2\]](#ineq:cor_2){reference-type="ref" reference="ineq:cor_2"}) becomes $$\sum_{k, k'} \binom{n_{1}}{k}\binom{n_{2}}{k'} x_{k, 0, k', 0}^{0, 0} \binom{n_{1}}{p} \binom{n_{2}}{q}K_{k}^{n_{1}}(p) K_{k'}^{n_{2}}(q) \geq 0,$$ which implies the result. ◻
:::

Let ${\cal N}_{k}$ be the collection of codes $S \subset {\cal P}$ with minimum distance at least $d$ and $\lvert S \rvert \leq k$. Schrijver's SDP can be generalized by considering the $k$-points relation of codewords. The generalized version is as follows [@GMS12].

::: proposition
[@GMS12 Generalized SDP bound] []{#pro:gen_sch_sdp label="pro:gen_sch_sdp"} For $S \in {\cal N}_{k}$, define $${\cal N}(S) = \{S' \subset {\cal P} : S \subset S', \lvert S \rvert + 2\lvert S' \setminus S \rvert \leq k \}.$$ Let $x = \{x_{i}\}_{i \in {\cal N}_{k}} \subset \mathbb{R}$ be a set of non-negative numbers. Define the $\lvert{\cal N}(S)\rvert \times \lvert{\cal N}(S)\rvert$ matrix indexed by ${\cal N}(S)$ as $$\label{gen_Sch}
        \left( M_{S}(x)\right)_{S', S''} = \left\{
        \begin{aligned}
            &x_{S' \cup S''}, \quad \text{ if } S' \cup S'' \text{ has minimum distance at least } d;\\
            &0,  \quad \quad \quad \quad \text{otherwise,}
        \end{aligned}\right.$$ for $S', S'' \in {\cal N}(S)$. Then, $$\label{equ:k_sdp}
        A(n, d) \leq A_{k}(n, d) = {\rm max}\left\{\sum_{i \in {\cal P}}x_{\{i\}} : x_{\emptyset} = 1, x_{S} \geq 0 \text{ and } M_{S}(x) \text{ is positive semidefinite for each } S \in {\cal N}_{k} \right\}.$$
:::

It can be shown that the generalized Schrijver's SDP constraints with $k = 4$ induces our positive semidefinite constraint on $R_{s}$.

::: proposition
The positive semidefinite constraints in the quadruple semidefinite program in ([\[equ:k_sdp\]](#equ:k_sdp){reference-type="ref" reference="equ:k_sdp"}) imply the positive semidefiniteness of $R_{s}$.
:::

::: proof
*Proof.* Let $C$ be a code of length $n$ and minimum distance $d$. Consider $S = \{\emptyset, u\}  \in {\cal N}_{4}$, where $u$ has $1$ in the first $n_{1}$ positions and $0$ in the other $n_{2}$ positions, which is a subset of $C$. Let $x$ be defined as $x_{i} = 1$ if $i \subset C$ and $x_{i} = 0$ for the other cases. Observe that there is an one-to-one correspondence between $N(S) = \{S \cup \{v\} : v \in {\cal P}\}$ and ${\cal P}$ by sending $S \cup \{v\}$ to $v$. Thus, $M_{S}(x)$ can be indexed by ${\cal P}$ and $$\left( M_{S}(x)\right)_{v, w} = \left\{
        \begin{aligned}
            &1, \quad \text{if } \{v, w\} \subset C;\\
            &0,  \quad \text{otherwise.}
        \end{aligned}\right.$$ Notice that $M_{S}(x) = \chi^{C} (\chi^{C})^{T}$ is positive semidefinite and $$R_{s}^{u} = \frac{1}{\lvert \Pi_{s}^{u}\rvert} \sum_{(\pi_{1}, \pi_{2}) \in \Pi_{s}^{u}} \chi^{(\pi_{1}, \pi_{2})(C)} (\chi^{(\pi_{1}, \pi_{2})(C)})^{T}.$$ We observe that each $\chi^{(\pi_{1}, \pi_{2})(C)} (\chi^{(\pi_{1}, \pi_{2})(C)})^{T}$ is similar to $M_{S}(x) = \chi^{C} (\chi^{C})^{T}$ by changing the order of the basis. Thus, $R_{s}^{u}$ is semidefinite. ◻
:::
