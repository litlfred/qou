---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP"
section_id: sec-001-2-irreducible-characters-of-cksn
section_title: "Irreducible characters of CkSn"
section_number: 2
pages: 4-7
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.925
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP — The paper studies how to compute irreducible characters of the generalized symmetric group Ck ≀Sn by iterative algorithms."
---
The generalized symmetric group $C_k\wr S_n$ is the wreath product of the cyclic group $C_k$ of order $k$ with the symmetric group $S_n$ of $n$ elements, i.e. the semidirect product $C_k^{n}\rtimes S_n$, where the symmetric group $S_n$ acts on the direct product $C_k^{n}=C_k\times \cdots \times C_k$ by permutating the factors. The multiplication is given by $$\begin{aligned}
    (g;\sigma)\cdot (h;\tau)=(g\sigma(h);\sigma\tau),
\end{aligned}$$ where $g,h\in C_k^{n}$ and $\sigma,\tau\in S_n$.

Since $C_k$ is an abelian group of order $k$, there are exactly $k$ conjugacy classes, given by $\{1\},\{c\},\cdots,\{c^{k-1}\}$, where $C_k=\langle c \rangle$. The order of the centralizer of each conjugacy class is $k$. Its irreducible characters are given by $\gamma_i$, $i=0, \ldots, k-1$, where $\gamma_i(c^j)=\omega^{ij}$, and $\omega=e^{2\pi i/k}$ is the $k$-th primitive root of unity. The space of class functions on $C_k$ is given by $$\begin{aligned}
    R(C_k)=\bigoplus_{i=0}^{k-1}\mathbb{C}\gamma_i.
\end{aligned}$$

The conjugacy classes of $C_k\wr S_n$ are parametrized by colored partitions. The color set is $I=\{0,1,\cdots,k-1\}$, the indexing set of conjugacy classes. The conjugacy class of an element $x=(g;\sigma)\in C_k\wr S_n$ corresponds to *the $I$-colored partition* $\boldsymbol{\lambda}=(\lambda^{(i)})$, which consists of $|I|$ partitions $\lambda^{(i)}$ such that $\Arrowvert\boldsymbol{\lambda}\Arrowvert=\sum_{i=0}^{k-1}|\lambda^{(i)}|=n$, the $i$th partition $\lambda^{(i)}$ given by $$\begin{aligned}
    \lambda^{(i)}=(1^{m_1(c^{i})}2^{m_2(c^{i})}\cdots),
\end{aligned}$$ where $m_j(c^i)$ equals to the number of $j$-cycles in $\sigma$ whose cycle product is $c^i$. We also say that the colored partition $\boldsymbol{\lambda}=(\lambda^{(i)})$ is supported at its constituent subpartitions $\lambda^{(i)}$. In particular, a colored partition $\boldsymbol{\lambda}$ supported at only one color has one nontrivial constituent subpartition, and all other constituents are empty.

Given a partition $\lambda=(\lambda_1, \lambda_2, \ldots, \lambda_l)$, one can paint the parts with the colors $\{0, 1, \ldots, k-1\}$, to get $k^{l(\lambda)}$ colored partitions $\boldsymbol{\lambda}$, which are referred as the colored partitions arising from $\lambda$. On the other hand, all these $k^{l(\lambda)}$ colored partitions become to the partition $\lambda$ by erasing their colors. If $\boldsymbol{\lambda}=(\lambda^{(i)})$ is a colored partition, we define the *weighted length* $\eta(\boldsymbol{\lambda})$ as $\sum_i il(\lambda^{(i)})$.

We also call $\boldsymbol{\lambda}$ the type of the conjugacy class. It is known that two elements are conjugate in $C_k\wr S_n$ if and only if they have the same type.

A *hook* is a special partition of the form $(a, 1^b)$, where $a-1$ is the length of its arm and $b$ is the length of its leg. The hook length is defined as $a+b$. For a general partition $\lambda$, its hook length at $x=(i, j)\in \lambda$, of the Young diagram, is defined by $$h(x)=\lambda_{i}+\lambda_j'-i-j+1,$$ and the hook length of $\lambda$ is defined as the product of $h(x)$ for $x\in \lambda$, where $\lambda'$ is the conjugate of $\lambda$.

::: exmp
In $C_3\wr S_7$, $$\begin{aligned}
        x=((1,1,1,\omega^1,\omega^1,\omega^2,1);(1,2,3)(4,5)(6,7));\\
        y=((1,\omega^2,\omega^1,1,1,1,\omega^1);(1,4,5)(2,6)(3,7))
    
\end{aligned}$$ are conjuagate, since they have the same type $((3),(\phi),(2,2))$.
:::

Irreducible characters of the generalized symmetric group $C_k\wr S_n$ were determined by Specht [@S]. Frenkel, Wang, and the second author have given a vertex algebraic method to express the irreducible character values by matrix coefficients of certain vertex operators [@FJW], which we now recall in the following.

Let $\{a_n(\gamma_i)|n\in \mathbb{Z},i\in I\}\cup\{c\}$ be the set of generators of the Heisenberg algebra $\mathcal{H}$ with defining relations $$\begin{aligned}
=n\delta_{n,-m}\delta_{i,j}c,
\end{aligned}$$ $$\begin{aligned}
=0.
\end{aligned}$$

Consider the Fock space $V=\mathrm{Sym}(a_{-n}(\gamma_i)'s)$, the polynomial algebra on the variables $a_{-n}(\gamma_i)$,$n\in \mathbb{N}$ and $i\in I$. The algebra $\mathcal{H}$ acts on $V$ by the following rule: $$\begin{aligned}
    &a_{-n}(\gamma_i).v=a_{-n}(\gamma_i)v,\\
    &c.v=v, \\ \notag
    &a_n(\gamma_i).a_{-n_1}(\alpha_1)a_{-n_2}(\alpha_2)\cdots a_{-n_k}(\alpha_k)\\ \label{e:2.6}
    &=\sum_{j=1}^{k}\delta_{n,n_j}\langle \gamma_i,\alpha_j\rangle a_{-n_1}(\alpha_1)a_{-n_2}(\alpha_2)\cdots a_{-n_k}(\alpha_k)
\end{aligned}$$ where $\alpha_j\in R(C_k)$, $\langle \gamma_i,\gamma_j\rangle =\delta_{i,j}$ and $\langle \gamma_i,\alpha_j\rangle$ is extended the whole space by linearity.

For convenience, we denote $a_n(\gamma_i):=a_{in}$, where the first index $i$ stands for $\gamma_i$. The space $V$ is equipped with a bilinear form given by $$\begin{aligned}
    \langle 1,1\rangle =1, \quad a_{in}^*=a_{-in},
\end{aligned}$$ where $a_{in}^*$ denotes the adjoint of $a_{in}$. We denote by $A_i(z)$ and $A_i^*(z)$ the generating series: $$\begin{aligned}
    A_i(z)=\sum_{n\in \mathbb{N}}a_{-in}z^n, \quad A_i^*(z)=\sum_{n\in \mathbb{N}}a_{in}z^{-n}.
\end{aligned}$$

Moreover, for a partition $\lambda=(\lambda_1,\lambda_2,\cdots \lambda_l)$, we define $$\begin{aligned}
\label{e:2.9}
    a_{-i\lambda}=a_{-i\lambda_1}a_{-i\lambda_2}\cdots a_{-i\lambda_l},
\end{aligned}$$ which form an orthogonal basis: $$\begin{aligned}
\label{e:innerprod}
    \langle a_{-i\lambda}, a_{-j\mu}\rangle=\delta_{i,j}\delta_{\lambda \mu}z_\lambda,
\end{aligned}$$ where $z_\lambda=\prod_i i^{m_i}m_i!$ for $(1^{m_1}2^{m_2}\cdots)$, the exponential notation of $\lambda$.

In fact, $\mathcal{H}$ has another set of generators consisting of the Fourier transform of the first set: $\{\widetilde{a}_{in}|n\in \mathbb{Z},i\in I\}\cup\{c\}$, where $$\begin{aligned}
\label{e:2.11}
    \widetilde{a}_{in}=\sum_{j=0}^{k-1}\omega^{-ij}a_{jn}.
\end{aligned}$$ Under the inverse Fourier transform, we have that $$\begin{aligned}
    a_{in}=\frac{1}{k}\sum_{j=0}^{k-1}\omega^{ij}\widetilde{a}_{jn}.
\end{aligned}$$

Similarly, for a partition $\lambda=(\lambda_1, \lambda_2, \ldots, \lambda_l)$ we denote $$\begin{aligned}
    \widetilde{a}_{-i\lambda}=\widetilde{a}_{-i\lambda_1}\widetilde{a}_{-i\lambda_2}\cdots \widetilde{a}_{-i\lambda_l}.
\end{aligned}$$

For a colored partition $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\cdots,\lambda^{(k-1)})$, let $$\begin{aligned}
    \widetilde{a}_{-\boldsymbol{\lambda}}=\widetilde{a}_{-0\lambda^{(0)}}\widetilde{a}_{-1\lambda^{(1)}}\cdots \widetilde{a}_{-(k-1)\lambda^{(k-1)}}.
\end{aligned}$$ Then $\widetilde{a}_{-\boldsymbol{\lambda}}$ form another basis of $\mathcal{H}$.

We introduce the vertex operator $X_i(z)$ and its adjoint $X_i^*(z)$ as the linear maps: $V\longrightarrow V[[z, z^{-1}]]$ given by $$\begin{aligned}
    X_i(z)&=\mbox{exp} \left( \sum\limits_{n\geq 1} \frac{1}{n}a_{-in}z^{n} \right) \mbox{exp} \left( -\sum \limits_{n\geq 1} \frac{1}{n}a_{in}z^{-n} \right)\\ \notag
    &=\sum_{n\in\mathbb Z}X_{in}z^n,\\
    X_i^*(z)&=\mbox{exp} \left( -\sum\limits_{n\geq 1} \frac{1}{n}a_{-in}z^{n} \right) \mbox{exp} \left( \sum \limits_{n\geq 1} \frac{1}{n}a_{in}z^{-n} \right)\\ \notag
    &=\sum_{n\in\mathbb Z}X_{in}^*z^{-n}.
\end{aligned}$$

In fact, for a partition $\lambda=(\lambda_1,\lambda_2,\cdots, \lambda_l)$, it is known that $$\begin{aligned}
    s_{i\lambda}=X_{i\lambda_1}X_{i\lambda_2}\cdots X_{i\lambda_l}.1
\end{aligned}$$ is the Schur function associated to the parition $\lambda$ in the variables $a_{-in}$ (as a power-sum symmetric function) [@J2]. Then we have $$\begin{aligned}
    \langle s_{i\lambda}, s_{i\mu}\rangle=\delta_{\lambda \mu}.
\end{aligned}$$

For a colored partition $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\cdots,\lambda^{(k-1)})$, we denote $$\begin{aligned}
        s_{\boldsymbol{\lambda}}=s_{0\lambda^{(0)}}s_{1\lambda^{(1)}}\cdots s_{(k-1)\lambda^{({k-1})}}.
\end{aligned}$$ We recall the following vertex algebraic formulation of Specht characters:

::: thm
[@FJW] []{#t:FJW label="t:FJW"} Given colored partitions $\boldsymbol{\lambda}=(\lambda^{(0)},\lambda^{(1)},\cdots,\lambda^{(k-1)})$ and $\boldsymbol{\rho}=(\rho^{(0)},\rho^{(1)},\cdots,\rho^{(k-1)})$ of $n$, the matrix coefficient $$\begin{aligned}
        \langle s_{\boldsymbol{\lambda}}, \widetilde{a}_{-\boldsymbol{\rho}} \rangle
    
\end{aligned}$$ is equal to the value of the irreducible character $\chi^{\boldsymbol{\lambda}}$ at the conjugacy class of type $\boldsymbol{\rho}$ in $C_k\wr S_n$.
:::
